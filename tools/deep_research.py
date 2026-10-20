#!/usr/bin/env python3
"""
tools/deep_research.py
Enhanced research pipeline for DeFi/crypto project articles.

Layers on top of the basic research:
  1. Homepage + docs + fees page (TinyFish fetch)
  2. Web searches: reviews, fees, referral, security, Reddit, competitors
  3. DeFiLlama API  - TVL, chains, 24h volume (DEX/DeFi projects)
  4. CoinGecko API  - token price, market cap, rank (no key required)
  5. Returns a unified dict for article generation

Replaces the old research() function in write_article.py.
"""
import json, os, re, subprocess, requests
from pathlib import Path
from datetime import date
from urllib.parse import urlparse
from dotenv import load_dotenv

load_dotenv()
TINYFISH_API_KEY = os.getenv("TINYFISH_API_KEY", "")
_PROXY = os.getenv("PROXY", "") or (
    ":".join(filter(None, [
        os.getenv("PROXY_HOST", ""),
        os.getenv("PROXY_PORT", ""),
        os.getenv("PROXY_USER", ""),
        os.getenv("PROXY_PASS", ""),
    ])) or ""
)


# ─── TinyFish helpers ─────────────────────────────────────────────────────────

def _tf_env() -> dict:
    env = os.environ.copy()
    env["TINYFISH_API_KEY"] = TINYFISH_API_KEY
    if _PROXY:
        parts = _PROXY.split(":")
        if len(parts) >= 2:
            env["HTTPS_PROXY"] = f"http://{':'.join(parts)}"
    return env


def tf_search(query: str, num: int = 5) -> str:
    r = subprocess.run(
        f'tinyfish search query {json.dumps(query)} --limit {num}',
        capture_output=True, shell=True, env=_tf_env(), timeout=60,
    )
    return r.stdout.decode("utf-8", "ignore")


def tf_fetch(url: str, fmt: str = "markdown") -> str:
    r = subprocess.run(
        f'tinyfish fetch content get --format {fmt} {json.dumps(url)}',
        capture_output=True, shell=True, env=_tf_env(), timeout=90,
    )
    return r.stdout.decode("utf-8", "ignore")


def _truncate(text: str, max_chars: int) -> str:
    if len(text) > max_chars:
        return text[:max_chars] + "\n...[truncated]"
    return text


def _domain(url: str) -> str:
    return urlparse(url.lower().rstrip("/")).netloc


def _brand(url: str) -> str:
    return _domain(url).split(".")[0]


def _guess_docs_url(base_url: str, homepage_md: str) -> str:
    candidates = re.findall(r'https?://[^\s\)"\']+docs[^\s\)"\']*', homepage_md, re.IGNORECASE)
    if candidates:
        return candidates[0].rstrip("/.,")
    dom = _domain(base_url)
    return f"https://docs.{dom}"


# ─── DeFiLlama API ────────────────────────────────────────────────────────────

def _defillama_fetch(domain: str) -> dict:
    """Get TVL, chains, volume from DeFiLlama (free, no key)."""
    result = {
        "tvl": "", "chains": "", "volume_24h": "",
        "category": "", "defillama_url": "",
    }
    try:
        resp = requests.get("https://api.llama.fi/protocols", timeout=15)
        if resp.status_code != 200:
            return result
        keyword = domain.split(".")[0].lower()
        match = None
        for p in resp.json():
            name_lc = p.get("name", "").lower()
            slug_lc = p.get("slug", "").lower()
            if keyword == slug_lc or keyword in name_lc or name_lc in keyword:
                match = p
                break
        if not match:
            return result

        slug = match.get("slug", "")
        result["defillama_url"] = f"https://defillama.com/protocol/{slug}"
        result["category"] = match.get("category", "")
        tvl = match.get("tvl")
        if tvl:
            result["tvl"] = f"${float(tvl):,.0f}"
        chains = match.get("chains", [])
        result["chains"] = ", ".join(chains[:12]) if chains else ""

        # 24h DEX volume
        vol_url = (
            f"https://api.llama.fi/summary/dexs/{slug}"
            "?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true&dataType=dailyVolume"
        )
        vol_r = requests.get(vol_url, timeout=10)
        if vol_r.status_code == 200:
            vd = vol_r.json()
            vol = vd.get("total24h") or vd.get("totalVolume24h")
            if vol:
                result["volume_24h"] = f"${float(vol):,.0f}"
    except Exception as exc:
        print(f"[defillama] Warning: {exc}")
    return result


# ─── CoinGecko API ────────────────────────────────────────────────────────────

def _coingecko_fetch(domain: str) -> dict:
    """Get token price, market cap, rank (CoinGecko public API, no key)."""
    result = {
        "price_usd": "", "market_cap": "",
        "cg_rank": "", "symbol": "", "token_name": "",
    }
    try:
        keyword = domain.split(".")[0].lower()
        headers = {"User-Agent": "Mozilla/5.0"}
        search_r = requests.get(
            f"https://api.coingecko.com/api/v3/search?query={keyword}",
            timeout=15, headers=headers,
        )
        if search_r.status_code != 200:
            return result
        hits = search_r.json().get("coins", [])
        if not hits:
            return result

        coin = hits[0]
        for h in hits:
            if keyword in h.get("id", "").lower() or keyword == h.get("symbol", "").lower():
                coin = h
                break

        cg_id = coin.get("id", "")
        result["symbol"]     = coin.get("symbol", "").upper()
        result["token_name"] = coin.get("name", "")
        result["cg_rank"]    = str(coin.get("market_cap_rank") or "")

        price_r = requests.get(
            f"https://api.coingecko.com/api/v3/simple/price"
            f"?ids={cg_id}&vs_currencies=usd&include_market_cap=true",
            timeout=15, headers=headers,
        )
        if price_r.status_code == 200:
            pd = price_r.json().get(cg_id, {})
            price = pd.get("usd")
            mcap  = pd.get("usd_market_cap")
            if price:
                result["price_usd"] = f"${price:,.4f}" if price < 1 else f"${price:,.2f}"
            if mcap:
                result["market_cap"] = f"${float(mcap):,.0f}"
    except Exception as exc:
        print(f"[coingecko] Warning: {exc}")
    return result


# ─── Main pipeline ────────────────────────────────────────────────────────────

def deep_research(url: str, site_type: str) -> dict:
    """
    Full research pipeline. Returns a rich dict for article generation.
    Drop-in replacement for the old research() function.
    """
    dom   = _domain(url)
    brand = _brand(url)
    today = date.today()

    print(f"\n[research] {'='*52}")
    print(f"[research] Target : {url}")
    print(f"[research] Type   : {site_type}")
    print(f"[research] {'='*52}\n")

    # 1. Homepage
    print("[research] 1/9  Homepage...")
    homepage = tf_fetch(url)

    # 2. Docs
    docs_url = _guess_docs_url(url, homepage)
    print(f"[research] 2/9  Docs: {docs_url}")
    docs_md = tf_fetch(docs_url)

    # 3. Fees / tokenomics page (best-effort)
    fees_md = ""
    fees_page = f"{url.rstrip('/')}/fees"
    print(f"[research] 3/9  Fees page: {fees_page}")
    fees_md = tf_fetch(fees_page)

    # 4-9. Web searches
    print("[research] 4/9  Search: reviews & features...")
    review_hits = tf_search(f"{brand} review 2026 features pros cons beginner")

    print("[research] 5/9  Search: fees & costs...")
    fees_hits = tf_search(f"{brand} fees trading costs 2026")

    print("[research] 6/9  Search: referral / affiliate...")
    referral_hits = tf_search(f"{brand} referral affiliate program how to earn 2026")

    print("[research] 7/9  Search: security & audits...")
    security_hits = tf_search(f"{brand} security smart contract audit hack exploit history")

    print("[research] 8/9  Search: Reddit sentiment...")
    reddit_hits = tf_search(f"site:reddit.com {brand} review experience opinion 2026")

    print("[research] 9/9  Search: competitors...")
    if site_type == "dex":
        comp_q = f"{brand} vs 1inch uniswap paraswap which is better DEX aggregator"
    elif site_type == "cex":
        comp_q = f"{brand} vs binance coinbase kraken bybit comparison 2026"
    else:
        comp_q = f"{brand} alternatives competitors comparison 2026"
    competitor_hits = tf_search(comp_q)

    # External APIs
    defillama = {}
    if site_type in ("dex", "generic"):
        print("[research] API  DeFiLlama...")
        defillama = _defillama_fetch(dom)
    coingecko = {}
    print("[research] API  CoinGecko...")
    coingecko = _coingecko_fetch(dom)

    print("\n[research] Done. Building research bundle...\n")

    return {
        # Meta
        "url":             url,
        "domain":          dom,
        "brand":           brand,
        "site_type":       site_type,
        "today":           today.strftime("%B %d, %Y"),
        "today_iso":       today.isoformat(),
        # Raw content
        "homepage_md":     _truncate(homepage, 5000),
        "docs_md":         _truncate(docs_md, 4000),
        "docs_url":        docs_url,
        "fees_md":         _truncate(fees_md, 2000),
        # Search results
        "review_hits":     _truncate(review_hits, 3000),
        "fees_hits":       _truncate(fees_hits, 2000),
        "referral_hits":   _truncate(referral_hits, 2000),
        "security_hits":   _truncate(security_hits, 2000),
        "reddit_hits":     _truncate(reddit_hits, 2000),
        "competitor_hits": _truncate(competitor_hits, 2000),
        # DeFiLlama
        "defillama":       defillama,
        "tvl":             defillama.get("tvl", ""),
        "chains":          defillama.get("chains", ""),
        "volume_24h":      defillama.get("volume_24h", ""),
        "defillama_url":   defillama.get("defillama_url", ""),
        "defi_category":   defillama.get("category", ""),
        # CoinGecko
        "coingecko":       coingecko,
        "token_symbol":    coingecko.get("symbol", ""),
        "token_price":     coingecko.get("price_usd", ""),
        "market_cap":      coingecko.get("market_cap", ""),
        "cg_rank":         coingecko.get("cg_rank", ""),
        "token_name":      coingecko.get("token_name", ""),
    }

#!/usr/bin/env python3
"""
tools/write_article.py
Research a DeFi/crypto site and generate a beginner-friendly review article.

Flow:
  1. Use TinyFish to fetch the site + docs + extra sources
  2. Optionally run capture_devices.py automatically for device screenshots
  3. Fill the Jinja2 template with researched data
  4. Write the finished Markdown article to --out

Usage:
    python tools/write_article.py --url https://kyberswap.com --type dex --slug kyberswap-review-2026
    python tools/write_article.py --url https://uniswap.org --type dex --slug uniswap-review-2026 --no-screenshots
    python tools/write_article.py --url https://binance.com --type cex --slug binance-review-2026

Environment (see .env.example):
    TINYFISH_API_KEY   — required
    PROXY              — optional, format host:port:user:pass
"""
import asyncio, os, sys, json, re, argparse, subprocess, textwrap
from pathlib import Path
from datetime import date
from dotenv import load_dotenv

load_dotenv()
TINYFISH_API_KEY = os.getenv("TINYFISH_API_KEY", "")
PROXY = os.getenv("PROXY", "")  # host:port:user:pass

# ─── TinyFish helpers ────────────────────────────────────────────────────────

def tf_search(query: str, num: int = 5) -> str:
    """Run a TinyFish web search and return raw text."""
    env = _tf_env()
    r = subprocess.run(
        f'tinyfish search query {json.dumps(query)} --limit {num}',
        capture_output=True, shell=True, env=env, timeout=60
    )
    return r.stdout.decode("utf-8", "ignore")

def tf_fetch(url: str, fmt: str = "markdown") -> str:
    """Fetch page content via TinyFish."""
    env = _tf_env()
    r = subprocess.run(
        f'tinyfish fetch content get --format {fmt} {json.dumps(url)}',
        capture_output=True, shell=True, env=env, timeout=90
    )
    return r.stdout.decode("utf-8", "ignore")

def _tf_env() -> dict:
    env = os.environ.copy()
    env["TINYFISH_API_KEY"] = TINYFISH_API_KEY
    if PROXY:
        parts = PROXY.split(":")
        if len(parts) >= 2:
            env["HTTPS_PROXY"] = f"http://{':'.join(parts)}"
    return env

# ─── Research pipeline ────────────────────────────────────────────────────────

def research(url: str, site_type: str) -> dict:
    """
    Fetch and return structured research data about the site.
    Returns a dict with keys used by the template.
    """
    domain = url.rstrip("/").split("//")[-1].split("/")[0]
    print(f"[research] Fetching homepage: {url}")
    homepage = tf_fetch(url)

    docs_url = _guess_docs_url(url, homepage)
    docs_content = ""
    if docs_url:
        print(f"[research] Fetching docs: {docs_url}")
        docs_content = tf_fetch(docs_url)

    print("[research] Running web searches...")
    review_hits    = tf_search(f"{domain} review 2026 features fees security")
    referral_hits  = tf_search(f"{domain} referral affiliate program how to")
    security_hits  = tf_search(f"{domain} security audit exploit history")
    competitor_q   = "1inch paraswap uniswap comparison" if site_type == "dex" else "binance coinbase kraken comparison"
    competitor_hits = tf_search(f"{domain} vs {competitor_q}")

    return {
        "url":             url,
        "domain":          domain,
        "site_type":       site_type,
        "today":           date.today().strftime("%B %d, %Y"),
        "today_iso":       date.today().isoformat(),
        # raw research blobs — the template prompt uses these
        "homepage_md":     _truncate(homepage, 4000),
        "docs_md":         _truncate(docs_content, 3000),
        "docs_url":        docs_url or "",
        "review_hits":     _truncate(review_hits, 3000),
        "referral_hits":   _truncate(referral_hits, 2000),
        "security_hits":   _truncate(security_hits, 2000),
        "competitor_hits": _truncate(competitor_hits, 2000),
    }

def _guess_docs_url(base_url: str, homepage_md: str) -> str:
    """Try to find a docs link from the homepage."""
    candidates = re.findall(r'https?://[^\s\)"\']+docs[^\s\)"\']*', homepage_md, re.IGNORECASE)
    if candidates:
        return candidates[0].rstrip("/.,")
    domain = base_url.rstrip("/").split("//")[-1].split("/")[0]
    return f"https://docs.{domain}"

def _truncate(text: str, max_chars: int) -> str:
    if len(text) > max_chars:
        return text[:max_chars] + "\n...[truncated]"
    return text

# ─── Article generation ───────────────────────────────────────────────────────

SYSTEM_PROMPT = """\
You are an expert crypto/DeFi technical writer who specialises in beginner-friendly reviews.
Your audience includes complete non-crypto beginners. Use plain English analogies (e.g. "think of it like Google Flights").
Rules:
- Never use jargon without immediately explaining it in parentheses.
- Use live data from the research material provided.
- Follow the template structure EXACTLY — replace every {{PLACEHOLDER}} with real content.
- Keep the tone friendly and factual.
- Tables, bullet lists, and step-by-step numbered lists are encouraged.
- Do NOT fabricate stats — if a number is not in the research, write "N/A (check docs)".
"""

def build_article_via_tinyfish(research_data: dict, template: str, screenshots_dir: Path) -> str:
    """
    Ask TinyFish AI to fill the template using the research data.
    Falls back to a direct placeholder-fill if AI is unavailable.
    """
    screenshot_map = _build_screenshot_map(screenshots_dir, research_data["domain"])
    template_filled = template
    for key, val in screenshot_map.items():
        template_filled = template_filled.replace(f"{{{{{key}}}}}", val)

    user_prompt = f"""\
Here is research data about {research_data['url']} ({research_data['site_type'].upper()}):

=== HOMEPAGE (markdown) ===
{research_data['homepage_md']}

=== DOCS ===
{research_data['docs_md']}

=== REVIEW SEARCH RESULTS ===
{research_data['review_hits']}

=== REFERRAL / AFFILIATE INFO ===
{research_data['referral_hits']}

=== SECURITY HISTORY ===
{research_data['security_hits']}

=== COMPETITOR COMPARISON ===
{research_data['competitor_hits']}

=== TODAY ===
{research_data['today']}

Fill the following Markdown article template. Replace every {{PLACEHOLDER}} with real content from the research above.
Output ONLY the finished Markdown — no preamble, no code fences, no explanation.

{template_filled}
"""

    env = _tf_env()
    payload = json.dumps({
        "model": "gpt-4o",
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user",   "content": user_prompt}
        ],
        "max_tokens": 8000
    })

    print("[write_article] Sending research to TinyFish AI for article generation...")
    r = subprocess.run(
        'tinyfish ai chat complete --stdin',
        input=payload.encode("utf-8"),
        capture_output=True, shell=True, env=env, timeout=180
    )
    stdout = r.stdout.decode("utf-8", "ignore").strip()

    # If tinyfish AI endpoint not available, fall back to returning template with raw data
    if not stdout or r.returncode != 0:
        print("[write_article] WARNING: TinyFish AI unavailable, using template with research notes.")
        stub = template_filled.replace("{{RESEARCH_HOMEPAGE}}", research_data["homepage_md"][:1000])
        return stub

    # Strip markdown code fence if model wrapped it
    if stdout.startswith("```"):
        stdout = re.sub(r"^```[a-z]*\n?", "", stdout)
        stdout = re.sub(r"\n?```$", "", stdout)
    return stdout

def _build_screenshot_map(screenshots_dir: Path, domain: str) -> dict:
    """Map template screenshot placeholders to relative paths."""
    base = screenshots_dir / domain
    mapping = {
        "SS_DESKTOP":     str(base / "desktop.png"),
        "SS_TABLET":      str(base / "tablet.png"),
        "SS_PHONE":       str(base / "phone.png"),
        "SS_STEP1":       str(base / "tutorial" / "step1_homepage_connect_btn.png"),
        "SS_STEP2":       str(base / "tutorial" / "step2_network_dropdown.png"),
        "SS_STEP3":       str(base / "tutorial" / "step3_swap_eth_usdc.png"),
        "SS_STEP4":       str(base / "tutorial" / "step4_limit_order_tab.png"),
        "SS_WALLET_PICK": str(base / "wallet-flow" / "07_wallet_picker.png"),
        "SS_CONNECTED":   str(base / "wallet-flow" / "10_kyberswap_connected.png"),
        "SS_REF_DESKTOP": str(base / "ref" / "desktop.png"),
    }
    return mapping

# ─── Screenshots helper ───────────────────────────────────────────────────────

def run_capture_devices(url: str, out_dir: Path):
    print(f"[capture] Running capture_devices.py for {url} ...")
    script = Path(__file__).parent / "capture_devices.py"
    r = subprocess.run(
        [sys.executable, str(script), url, "--out", str(out_dir)],
        timeout=300
    )
    if r.returncode != 0:
        print("[capture] WARNING: capture_devices.py returned non-zero — screenshots may be missing.")

# ─── Main ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Research a site and write a review article")
    parser.add_argument("--url",          required=True, help="Site URL, e.g. https://kyberswap.com")
    parser.add_argument("--type",         required=True, choices=["dex", "cex", "nft", "generic"],
                        dest="site_type", help="Site category for template selection")
    parser.add_argument("--slug",         required=True, help="Output filename slug, e.g. kyberswap-review-2026")
    parser.add_argument("--out",          default="articles", help="Output directory for article")
    parser.add_argument("--screenshots",  default="screenshots", help="Root dir for screenshots")
    parser.add_argument("--no-screenshots", action="store_true",
                        help="Skip running capture_devices.py (use if screenshots already exist)")
    parser.add_argument("--template",     default=None,
                        help="Path to custom template (default: templates/{type}_review_template.md)")
    args = parser.parse_args()

    if not TINYFISH_API_KEY:
        print("ERROR: TINYFISH_API_KEY not set. Copy .env.example to .env and fill it in.")
        sys.exit(1)

    # Resolve template
    repo_root = Path(__file__).parent.parent
    tpl_path = Path(args.template) if args.template else repo_root / "templates" / f"{args.site_type}_review_template.md"
    if not tpl_path.exists():
        # Fall back to generic template
        tpl_path = repo_root / "templates" / "dex_review_template.md"
    template = tpl_path.read_text(encoding="utf-8")
    print(f"[template] Using: {tpl_path}")

    # Resolve paths
    out_dir       = repo_root / args.out
    screenshots_dir = repo_root / args.screenshots
    domain        = args.url.rstrip("/").split("//")[-1].split("/")[0]
    article_path  = out_dir / f"{args.slug}.md"

    # Step 1 – screenshots
    device_ss_dir = screenshots_dir / domain
    if not args.no_screenshots:
        run_capture_devices(args.url, device_ss_dir)
    else:
        print(f"[capture] Skipped. Using existing screenshots in {device_ss_dir}")

    # Step 2 – research
    data = research(args.url, args.site_type)

    # Step 3 – generate article
    article = build_article_via_tinyfish(data, template, screenshots_dir)

    # Step 4 – write output
    out_dir.mkdir(parents=True, exist_ok=True)
    article_path.write_text(article, encoding="utf-8")
    print(f"\n✅  Article saved: {article_path}")
    print(f"    Screenshots:    {device_ss_dir}")

if __name__ == "__main__":
    main()

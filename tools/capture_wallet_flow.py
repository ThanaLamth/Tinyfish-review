#!/usr/bin/env python3
"""
tools/capture_wallet_flow.py
Automate MetaMask v13 setup + DEX wallet connection flow.
Captures screenshots at every key step.

Requires: MetaMask extension (extracted zip, path set in .env MM_EXT_PATH)
On Ubuntu: needs Xvfb or real display. Use run_wallet_flow.sh wrapper.

Usage:
    # Ubuntu (headless via Xvfb):
    Xvfb :99 -screen 0 1440x900x24 &
    DISPLAY=:99 python tools/capture_wallet_flow.py --url https://kyberswap.com

    # With custom tip link:
    python tools/capture_wallet_flow.py \
        --url "https://kyberswap.com/swap/ethereum?inputCurrency=ETH&outputCurrency=0xA0b8...&feeReceiver=0xYOUR_WALLET&enableTip=true"

    # Re-run (wallet already set up, just unlock):
    python tools/capture_wallet_flow.py --url https://kyberswap.com --reuse
"""
import asyncio, os, shutil, json, argparse, sys
from pathlib import Path
from playwright.async_api import async_playwright
from dotenv import load_dotenv

load_dotenv()

# ── Config ──────────────────────────────────────────────────────────────────
TINYFISH_API_KEY = os.getenv("TINYFISH_API_KEY", "")
PROXY_HOST  = os.getenv("PROXY_HOST", "")
PROXY_PORT  = os.getenv("PROXY_PORT", "")
PROXY_USER  = os.getenv("PROXY_USER", "")
PROXY_PASS  = os.getenv("PROXY_PASS", "")
WALLET_PW   = os.getenv("WALLET_PASSWORD", "Demo@Wallet2026!")
USER_DATA   = os.getenv("USER_DATA_DIR", "/tmp/pw-mm-demo")
MM_EXT_ID   = "nkbihfbeogaeaoehlefnkodbefgpgknn"

def get_mm_ext_path():
    """Find MetaMask extension path — env var, common Ubuntu paths, or Windows."""
    env_path = os.getenv("MM_EXT_PATH", "")
    if env_path and os.path.isdir(env_path):
        return env_path
    candidates = [
        "/opt/metamask",
        "/usr/local/lib/metamask",
        str(Path.home() / ".metamask"),
        # Windows fallback
        str(Path.home() / "AppData/Local/Google/Chrome/User Data/Default/Extensions" / MM_EXT_ID),
    ]
    for c in candidates:
        # Windows: find the versioned subfolder
        p = Path(c)
        if p.is_dir():
            subs = [x for x in p.iterdir() if x.is_dir() and x.name[0].isdigit()]
            if subs:
                return str(sorted(subs)[-1])
            return c
    raise FileNotFoundError(
        "MetaMask extension not found. Set MM_EXT_PATH in .env or download:\n"
        "  wget https://github.com/MetaMask/metamask-extension/releases/download/v13.48.0/metamask-chrome-13.48.0.zip\n"
        "  unzip metamask-chrome-13.48.0.zip -d /opt/metamask"
    )

def get_proxy():
    if PROXY_HOST and PROXY_PORT:
        cfg = {"server": f"http://{PROXY_HOST}:{PROXY_PORT}"}
        if PROXY_USER: cfg["username"] = PROXY_USER
        if PROXY_PASS: cfg["password"] = PROXY_PASS
        return cfg
    return None

async def shot(page, out_dir: Path, name: str, msg: str = ""):
    out_dir.mkdir(parents=True, exist_ok=True)
    p = out_dir / f"{name}.png"
    await page.screenshot(path=str(p), full_page=False)
    kb = p.stat().st_size // 1024
    print(f"  [SHOT] {name}.png ({kb}KB)  {msg}")
    return str(p)

async def click_if_visible(page, selector, timeout=3000):
    try:
        el = page.locator(selector).first
        if await el.is_visible(timeout=timeout):
            await el.click()
            return True
    except Exception:
        pass
    return False

async def setup_metamask(context, mm_page, out_dir: Path):
    """Full MetaMask v13 onboarding OR unlock if already set up."""
    await mm_page.bring_to_front()
    await mm_page.wait_for_load_state("domcontentloaded")
    await asyncio.sleep(2)
    await shot(mm_page, out_dir, "01_mm_welcome")

    # If already set up: unlock with password
    try:
        pw_field = mm_page.locator('input[type="password"]').first
        unlock_btn = mm_page.locator('button:has-text("Unlock")').first
        if await pw_field.is_visible(timeout=3000):
            await pw_field.fill(WALLET_PW)
            await unlock_btn.click()
            await asyncio.sleep(2)
            await shot(mm_page, out_dir, "01b_mm_unlocked", "Unlocked with password")
            return mm_page
    except Exception:
        pass

    # Fresh onboarding
    await mm_page.get_by_text("I have an existing wallet", exact=True).click(timeout=8000)
    await asyncio.sleep(2)
    await shot(mm_page, out_dir, "02_mm_import_options", "Google/Apple/Telegram/SRP options")

    await mm_page.get_by_text("Import using Secret Recovery Phrase", exact=True).click(timeout=8000)
    await asyncio.sleep(2)
    await shot(mm_page, out_dir, "03_mm_seed_input", "Seed phrase textarea")

    # Generate wallet if no mnemonic set
    mnemonic = os.getenv("WALLET_MNEMONIC", "")
    if not mnemonic:
        try:
            from mnemonic import Mnemonic
            mnemonic = Mnemonic("english").generate(strength=128)
            print(f"  [INFO] Generated mnemonic: {mnemonic[:30]}...")
        except ImportError:
            mnemonic = "napkin innocent ugly turn pigeon sport dentist series split normal page require"

    # Type seed phrase word by word (triggers React onChange)
    ta = mm_page.locator('textarea').first
    await ta.click()
    await ta.type(mnemonic, delay=40)
    await asyncio.sleep(2)
    await shot(mm_page, out_dir, "04_mm_seed_filled", "12 words typed")

    await mm_page.locator('button:has-text("Continue")').first.click(timeout=8000)
    await asyncio.sleep(2)

    # Set password
    pws = await mm_page.locator('input[type="password"]').all()
    if len(pws) >= 1:
        await pws[0].fill(WALLET_PW)
        if len(pws) >= 2:
            await pws[1].fill(WALLET_PW)
        await click_if_visible(mm_page, 'input[type="checkbox"]')
        for label in ["Create password", "Import my wallet", "Import", "Confirm"]:
            if await click_if_visible(mm_page, f'button:has-text("{label}")', 2000):
                await asyncio.sleep(3)
                break
    await shot(mm_page, out_dir, "05_mm_password_set", "Password screen")

    # Click through onboarding completion screens
    for label in ["Got it!", "Done", "Next", "Skip", "Continue"]:
        await click_if_visible(mm_page, f'button:has-text("{label}")', 2000)
        await asyncio.sleep(0.8)

    await asyncio.sleep(2)
    await shot(mm_page, out_dir, "06_mm_ready", "Wallet ready")
    return mm_page

async def connect_to_dex(context, mm_page, url: str, out_dir: Path):
    """Open DEX, connect MetaMask, capture screenshots."""
    ks_page = await context.new_page()
    await ks_page.goto(url, timeout=60000, wait_until="domcontentloaded")
    await asyncio.sleep(6)
    await shot(ks_page, out_dir, "07_dex_loaded", "DEX loaded with ref link pre-filled")

    # Click Connect button
    connect_btn = ks_page.get_by_role("button", name="Connect").first
    await connect_btn.click(timeout=15000)
    await asyncio.sleep(2)
    await shot(ks_page, out_dir, "08_wallet_picker", "Wallet selection modal")

    # Accept Terms if present
    await click_if_visible(ks_page, 'input[type="checkbox"]')
    await asyncio.sleep(0.5)
    await shot(ks_page, out_dir, "08b_terms_accepted", "Terms accepted")

    # Click MetaMask
    await ks_page.get_by_text("MetaMask", exact=True).first.click(timeout=8000)

    # Wait for MetaMask popup via page event
    popup = None
    popup_future = asyncio.get_event_loop().create_future()
    def on_page(pg):
        if MM_EXT_ID in pg.url and not popup_future.done():
            popup_future.set_result(pg)
    context.on("page", on_page)
    try:
        popup = await asyncio.wait_for(popup_future, timeout=10.0)
    except asyncio.TimeoutError:
        for pg in context.pages:
            if MM_EXT_ID in pg.url and pg != mm_page:
                popup = pg; break
    context.remove_listener("page", on_page)

    if popup:
        await asyncio.sleep(1.5)
        await popup.bring_to_front()
        await shot(popup, out_dir, "09_mm_connect_popup", "MetaMask connection popup")
        for label in ["Next", "Connect"]:
            if await click_if_visible(popup, f'button:has-text("{label}")', 4000):
                await asyncio.sleep(1.5)
                await shot(popup, out_dir, f"09b_mm_{label.lower()}", f"Clicked {label}")
    else:
        print("  [WARN] MetaMask popup not caught")

    await asyncio.sleep(3)
    await ks_page.bring_to_front()
    await asyncio.sleep(2)
    await shot(ks_page, out_dir, "10_dex_connected", "DEX with wallet connected")
    return ks_page

async def main(url: str, out_dir: Path, reuse: bool):
    mm_ext_path = get_mm_ext_path()
    print(f"\nMetaMask: {mm_ext_path}")
    print(f"Output:   {out_dir}")
    print(f"Proxy:    {PROXY_HOST}:{PROXY_PORT}" if PROXY_HOST else "Proxy:    none\n")

    if not reuse and os.path.exists(USER_DATA):
        shutil.rmtree(USER_DATA, ignore_errors=True)
    os.makedirs(USER_DATA, exist_ok=True)

    launch_args = {
        "user_data_dir": USER_DATA,
        "headless": False,
        "args": [
            f"--disable-extensions-except={mm_ext_path}",
            f"--load-extension={mm_ext_path}",
            "--no-first-run", "--disable-popup-blocking",
        ],
        "viewport": {"width": 1440, "height": 900},
        "ignore_https_errors": True,
    }
    proxy = get_proxy()
    if proxy:
        launch_args["proxy"] = proxy

    async with async_playwright() as pw:
        context = await pw.chromium.launch_persistent_context(**launch_args)
        await asyncio.sleep(3)

        # Find or open MetaMask page
        mm_page = None
        for pg in context.pages:
            if MM_EXT_ID in pg.url:
                mm_page = pg; break
        if not mm_page:
            mm_page = await context.new_page()
            await mm_page.goto(f"chrome-extension://{MM_EXT_ID}/home.html")

        mm_page = await setup_metamask(context, mm_page, out_dir)
        ks_page = await connect_to_dex(context, mm_page, url, out_dir)

        print(f"\nAll done! Screenshots in {out_dir}")
        await context.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Capture MetaMask + DEX wallet connect flow")
    parser.add_argument("--url", required=True, help="DEX URL (optionally with tip params)")
    parser.add_argument("--out", default=None, help="Output directory")
    parser.add_argument("--reuse", action="store_true", help="Reuse existing wallet profile (skip setup)")
    args = parser.parse_args()

    if args.out:
        out_dir = Path(args.out)
    else:
        domain = args.url.replace("https://", "").split("/")[0]
        out_dir = Path("screenshots") / domain / "wallet-flow"

    asyncio.run(main(args.url, out_dir, args.reuse))

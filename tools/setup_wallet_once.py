#!/usr/bin/env python3
"""
tools/setup_wallet_once.py
One-time MetaMask wallet setup — run this ONCE on a new machine.
Saves the wallet profile to a permanent directory so capture_wallet_flow.py
can reuse it every time with --reuse (no re-onboarding needed).

Usage:
    python tools/setup_wallet_once.py

After this completes:
    python tools/capture_wallet_flow.py --url https://kyberswap.com --reuse
    ./run_wallet_flow.sh --url https://kyberswap.com --reuse

Profile is saved to:  ~/.tinyfish-review/mm-profile/
Ready flag written:   ~/.tinyfish-review/wallet_ready.flag

To reset (re-do setup): delete ~/.tinyfish-review/mm-profile/ and re-run this script.
"""
import asyncio, os, sys, json
from pathlib import Path
from datetime import datetime
from playwright.async_api import async_playwright
from dotenv import load_dotenv

load_dotenv()

WALLET_PW       = os.getenv("WALLET_PASSWORD",  "Demo@Wallet2026!")
WALLET_MNEMONIC = os.getenv("WALLET_MNEMONIC",  "napkin innocent ugly turn pigeon sport dentist series split normal page require")
MM_EXT_ID       = "nkbihfbeogaeaoehlefnkodbefgpgknn"

# Permanent profile directory (survives reboots)
PROFILE_DIR = Path.home() / ".tinyfish-review" / "mm-profile"
FLAG_FILE   = Path.home() / ".tinyfish-review" / "wallet_ready.flag"
LOG_DIR     = Path.home() / ".tinyfish-review" / "setup-shots"

PROXY_HOST = os.getenv("PROXY_HOST", "")
PROXY_PORT = os.getenv("PROXY_PORT", "")
PROXY_USER = os.getenv("PROXY_USER", "")
PROXY_PASS = os.getenv("PROXY_PASS", "")

def get_mm_ext_path():
    env_path = os.getenv("MM_EXT_PATH", "")
    if env_path and os.path.isdir(env_path):
        return env_path
    candidates = [
        "/opt/metamask",
        "/usr/local/lib/metamask",
        str(Path.home() / ".metamask"),
        str(Path.home() / "AppData/Local/Google/Chrome/User Data/Default/Extensions" / MM_EXT_ID),
    ]
    for c in candidates:
        p = Path(c)
        if p.is_dir():
            subs = [x for x in p.iterdir() if x.is_dir() and x.name[0].isdigit()]
            if subs:
                return str(sorted(subs)[-1])
            return c
    raise FileNotFoundError(
        "MetaMask extension not found.\n"
        "Ubuntu:  unzip metamask-chrome-13.48.0.zip -d /opt/metamask\n"
        "Set MM_EXT_PATH in .env if using a custom path."
    )

async def shot(page, name: str, msg: str = ""):
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    p = LOG_DIR / f"{name}.png"
    await page.screenshot(path=str(p), full_page=False)
    print(f"  [shot] {name}.png  {msg}")

async def click_text(page, text: str, timeout: int = 8000):
    await page.get_by_text(text, exact=True).first.click(timeout=timeout)
    await asyncio.sleep(1.5)

async def click_btn_if_visible(page, label: str, timeout: int = 3000) -> bool:
    try:
        el = page.locator(f'button:has-text("{label}")').first
        if await el.is_visible(timeout=timeout):
            await el.click()
            await asyncio.sleep(1)
            return True
    except Exception:
        pass
    return False

async def run_setup():
    if FLAG_FILE.exists():
        info = json.loads(FLAG_FILE.read_text())
        print(f"\nWallet already set up on {info.get('date')}.")
        print(f"Profile: {PROFILE_DIR}")
        print("To reset: delete the profile dir and re-run.")
        print(f"\n  rm -rf \"{PROFILE_DIR}\"")
        sys.exit(0)

    mm_path = get_mm_ext_path()
    print(f"\nMetaMask extension: {mm_path}")
    print(f"Profile directory:  {PROFILE_DIR}")
    PROFILE_DIR.mkdir(parents=True, exist_ok=True)

    launch_args = {
        "user_data_dir": str(PROFILE_DIR),
        "headless": False,
        "args": [
            f"--disable-extensions-except={mm_path}",
            f"--load-extension={mm_path}",
            "--no-first-run", "--disable-popup-blocking",
            "--window-size=1440,900",
        ],
        "viewport": {"width": 1440, "height": 900},
        "ignore_https_errors": True,
    }
    if PROXY_HOST and PROXY_PORT:
        proxy = {"server": f"http://{PROXY_HOST}:{PROXY_PORT}"}
        if PROXY_USER: proxy["username"] = PROXY_USER
        if PROXY_PASS: proxy["password"] = PROXY_PASS
        launch_args["proxy"] = proxy

    async with async_playwright() as pw:
        context = await pw.chromium.launch_persistent_context(**launch_args)
        await asyncio.sleep(3)

        # Open MetaMask
        mm_page = None
        for pg in context.pages:
            if MM_EXT_ID in pg.url:
                mm_page = pg; break
        if not mm_page:
            mm_page = await context.new_page()
            await mm_page.goto(f"chrome-extension://{MM_EXT_ID}/home.html")
            await asyncio.sleep(3)

        await mm_page.bring_to_front()
        await shot(mm_page, "01_welcome", "Welcome screen")

        # Step: I have an existing wallet
        await click_text(mm_page, "I have an existing wallet")
        await shot(mm_page, "02_import_choice", "Import options")

        # Step: Import Secret Recovery Phrase
        await click_text(mm_page, "Import using Secret Recovery Phrase")
        await shot(mm_page, "03_seed_input", "Seed phrase form")

        # Enter seed phrase word by word via keyboard (bypass LavaMoat)
        ta = mm_page.locator('textarea').first
        await ta.click()
        await asyncio.sleep(0.5)
        for word in WALLET_MNEMONIC.split():
            await ta.type(word + " ", delay=40)
        await asyncio.sleep(1)
        await shot(mm_page, "04_seed_filled", "Seed filled")

        # Continue
        await click_btn_if_visible(mm_page, "Continue", 6000)
        await shot(mm_page, "05_after_continue", "After continue")

        # Password fields
        for selector in ['input#password', 'input[data-testid="create-password-new"]',
                         'input[placeholder*="New password"]', 'input[type="password"]']:
            try:
                pw_field = mm_page.locator(selector).first
                if await pw_field.is_visible(timeout=2000):
                    await pw_field.fill(WALLET_PW)
                    # Confirm password field
                    conf_field = mm_page.locator('input[type="password"]').nth(1)
                    if await conf_field.is_visible(timeout=1000):
                        await conf_field.fill(WALLET_PW)
                    break
            except Exception:
                pass

        # Check terms checkbox if present
        await click_btn_if_visible(mm_page, "", 1000)  # dummy
        try:
            chk = mm_page.locator('input[type="checkbox"]').first
            if await chk.is_visible(timeout=2000):
                await chk.check()
        except Exception:
            pass

        # Import / Create password button
        for label in ["Import my wallet", "Create password", "Import", "Confirm"]:
            if await click_btn_if_visible(mm_page, label, 3000):
                await asyncio.sleep(4)
                break

        await shot(mm_page, "06_importing", "Importing wallet")
        await asyncio.sleep(4)

        # Click through completion screens
        for label in ["Got it!", "Done", "Next", "Skip", "Continue"]:
            await click_btn_if_visible(mm_page, label, 2000)
            await asyncio.sleep(0.8)

        await asyncio.sleep(2)
        await shot(mm_page, "07_wallet_ready", "Wallet ready — setup complete")

        print("\n✅  MetaMask setup complete!")
        print(f"    Profile: {PROFILE_DIR}")
        print(f"    Shots:   {LOG_DIR}")

        await context.close()

    # Write ready flag
    FLAG_FILE.parent.mkdir(parents=True, exist_ok=True)
    FLAG_FILE.write_text(json.dumps({
        "date":        datetime.now().isoformat(),
        "profile_dir": str(PROFILE_DIR),
        "mnemonic_set": bool(WALLET_MNEMONIC),
        "mm_ext":      mm_path,
    }, indent=2), encoding="utf-8")

    # Write .env hint
    env_hint = f"\n# Auto-written by setup_wallet_once.py\nUSER_DATA_DIR={PROFILE_DIR}\n"
    env_file = Path(__file__).parent.parent / ".env"
    if env_file.exists():
        existing = env_file.read_text(encoding="utf-8")
        if "USER_DATA_DIR" not in existing:
            with open(env_file, "a", encoding="utf-8") as f:
                f.write(env_hint)
            print(f"\n    USER_DATA_DIR appended to .env → {env_file}")

    print("\nNext steps:")
    print("  python tools/capture_wallet_flow.py --url https://kyberswap.com --reuse")
    print("  ./run_wallet_flow.sh --url https://kyberswap.com --reuse")

if __name__ == "__main__":
    asyncio.run(run_setup())

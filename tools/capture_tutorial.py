"""
tools/capture_tutorial.py
Capture step-by-step tutorial screenshots for a DEX site.
Navigates the site and takes targeted screenshots at each step.

Usage:
    python tools/capture_tutorial.py https://app.1inch.io --out screenshots/app.1inch.io/tutorial
"""
import argparse, sys
from pathlib import Path
from playwright.sync_api import sync_playwright

def capture_tutorial(url: str, out_dir: Path):
    out_dir.mkdir(parents=True, exist_ok=True)
    base = url.rstrip("/")

    with sync_playwright() as pw:
        browser = pw.chromium.launch(
            headless=True,
            args=["--no-sandbox", "--disable-dev-shm-usage"]
        )
        ctx = browser.new_context(
            viewport={"width": 1440, "height": 900},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/129.0.0.0 Safari/537.36",
        )
        page = ctx.new_page()

        # Dismiss cookie banner helper
        def dismiss_cookie():
            try:
                page.click("text=I agree", timeout=3000)
            except:
                try:
                    page.click("text=Accept", timeout=1000)
                except:
                    pass

        # Step 1 - Homepage with Connect button
        print("  [step1] Homepage + Connect button...")
        page.goto(base, timeout=45000, wait_until="domcontentloaded")
        page.wait_for_timeout(3500)
        dismiss_cookie()
        page.wait_for_timeout(500)
        page.screenshot(path=str(out_dir / "step1_homepage_connect_btn.png"))
        print(f"         saved step1 ({(out_dir/'step1_homepage_connect_btn.png').stat().st_size//1024}KB)")

        # Step 2 - Navigate to swap page, look for network selector
        print("  [step2] Swap page / network dropdown...")
        try:
            page.goto(f"{base}/#/swap", timeout=30000, wait_until="domcontentloaded")
        except:
            pass
        page.wait_for_timeout(3000)
        dismiss_cookie()
        # Try clicking network selector to open dropdown
        try:
            # 1inch has a network selector in top area
            page.locator("[class*='NetworkSelector'], [class*='network'], [data-testid*='network']").first.click(timeout=3000)
            page.wait_for_timeout(1000)
        except:
            pass
        page.screenshot(path=str(out_dir / "step2_network_dropdown.png"))
        print(f"         saved step2 ({(out_dir/'step2_network_dropdown.png').stat().st_size//1024}KB)")

        # Step 3 - Swap interface (ETH -> USDC)
        print("  [step3] Swap interface ETH->USDC...")
        try:
            page.goto(f"{base}/#/swap/ETH/USDC", timeout=30000, wait_until="domcontentloaded")
        except:
            pass
        page.wait_for_timeout(4000)
        dismiss_cookie()
        page.screenshot(path=str(out_dir / "step3_swap_eth_usdc.png"))
        print(f"         saved step3 ({(out_dir/'step3_swap_eth_usdc.png').stat().st_size//1024}KB)")

        # Step 4 - Limit order tab
        print("  [step4] Limit order tab...")
        try:
            page.goto(f"{base}/#/limit-order/ETH/USDC", timeout=30000, wait_until="domcontentloaded")
        except:
            try:
                page.click("text=Limit", timeout=3000)
            except:
                pass
        page.wait_for_timeout(3000)
        dismiss_cookie()
        page.screenshot(path=str(out_dir / "step4_limit_order_tab.png"))
        print(f"         saved step4 ({(out_dir/'step4_limit_order_tab.png').stat().st_size//1024}KB)")

        browser.close()
    print(f"\nDone. Tutorial screenshots in: {out_dir}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("url")
    parser.add_argument("--out", default=None)
    args = parser.parse_args()

    if args.out:
        out_dir = Path(args.out)
    else:
        domain = args.url.replace("https://","").replace("http://","").split("/")[0]
        out_dir = Path("screenshots") / domain / "tutorial"

    print(f"\nCapturing tutorial screenshots: {args.url}")
    capture_tutorial(args.url, out_dir)

if __name__ == "__main__":
    main()

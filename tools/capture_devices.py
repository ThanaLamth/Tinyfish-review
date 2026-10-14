#!/usr/bin/env python3
"""
tools/capture_devices.py
Capture screenshots of any URL on 3 device types: desktop, tablet, phone.
Uses TinyFish remote CDP browser — no local Chrome needed.

Usage:
    python tools/capture_devices.py https://kyberswap.com
    python tools/capture_devices.py https://binance.com --out ./screenshots/binance
    python tools/capture_devices.py https://site.com --device phone
"""
import asyncio, subprocess, json, os, argparse, sys
from pathlib import Path
from playwright.async_api import async_playwright
from dotenv import load_dotenv

load_dotenv()
TINYFISH_API_KEY = os.getenv("TINYFISH_API_KEY", "")

DEVICE_PROFILES = {
    "desktop": {
        "width": 1440, "height": 900, "device_scale_factor": 1,
        "mobile": False,
        "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
    },
    "tablet": {
        "width": 1024, "height": 1366, "device_scale_factor": 2,
        "mobile": True,
        "user_agent": "Mozilla/5.0 (iPad; CPU OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
    },
    "phone": {
        "width": 430, "height": 932, "device_scale_factor": 3,
        "mobile": True,
        "user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
    },
}

def create_tinyfish_session(start_url: str) -> str:
    env = os.environ.copy()
    env["TINYFISH_API_KEY"] = TINYFISH_API_KEY
    r = subprocess.run(
        f'tinyfish browser session create --url "{start_url}" --pretty',
        capture_output=True, shell=True, env=env
    )
    raw = r.stdout.decode("utf-8", "ignore")
    for line in raw.splitlines():
        if "CDP URL:" in line:
            return line.split("CDP URL:")[-1].strip()
    raise RuntimeError(f"Could not parse CDP URL:\n{raw}")

async def capture_device(cdp_url: str, url: str, device_name: str, profile: dict, out_dir: Path) -> str:
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{device_name}.png"

    async with async_playwright() as pw:
        browser = await pw.chromium.connect_over_cdp(cdp_url)
        all_contexts = browser.contexts
        if all_contexts and all_contexts[0].pages:
            page = all_contexts[0].pages[0]
        else:
            page = await (all_contexts[0] if all_contexts else await browser.new_context()).new_page()

        cdp_session = await page.context.new_cdp_session(page)
        await cdp_session.send("Emulation.setDeviceMetricsOverride", {
            "width": profile["width"], "height": profile["height"],
            "deviceScaleFactor": profile["device_scale_factor"],
            "mobile": profile["mobile"],
            "screenWidth": profile["width"], "screenHeight": profile["height"],
        })
        await cdp_session.send("Emulation.setUserAgentOverride", {"userAgent": profile["user_agent"]})

        await page.goto(url, timeout=45000, wait_until="domcontentloaded")
        await page.wait_for_timeout(4000)
        await page.set_viewport_size({"width": profile["width"], "height": profile["height"]})
        await page.wait_for_timeout(1000)
        await page.screenshot(path=str(out_path), full_page=True)
        await browser.close()

    size_kb = out_path.stat().st_size // 1024
    print(f"  [{device_name:8s}] {profile['width']}x{profile['height']} -> {out_path.name} ({size_kb}KB)")
    return str(out_path)

async def main(url: str, out_dir: Path, devices: list):
    print(f"\nCapturing: {url}")
    print(f"Devices:   {', '.join(devices)}")
    print(f"Output:    {out_dir}\n")
    results = {}
    for device_name in devices:
        profile = DEVICE_PROFILES[device_name]
        print(f"  [{device_name}] Starting TinyFish session...")
        cdp_url = create_tinyfish_session(url)
        path = await capture_device(cdp_url, url, device_name, profile, out_dir)
        results[device_name] = path

    summary_path = out_dir / "capture_summary.json"
    summary_path.write_text(json.dumps({"url": url, "screenshots": results}, indent=2), encoding="utf-8")
    print(f"\nDone! Summary: {summary_path}")
    return results

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Capture URL on desktop/tablet/phone via TinyFish")
    parser.add_argument("url", help="Target URL")
    parser.add_argument("--out", default=None, help="Output directory")
    parser.add_argument("--device", default="all", choices=["all", "desktop", "tablet", "phone"])
    args = parser.parse_args()

    if not TINYFISH_API_KEY:
        print("ERROR: TINYFISH_API_KEY not set. Copy .env.example to .env and add your key.")
        sys.exit(1)

    if args.out:
        out_dir = Path(args.out)
    else:
        domain = args.url.replace("https://", "").replace("http://", "").split("/")[0]
        out_dir = Path("screenshots") / domain

    devices = list(DEVICE_PROFILES.keys()) if args.device == "all" else [args.device]
    asyncio.run(main(args.url, out_dir, devices))

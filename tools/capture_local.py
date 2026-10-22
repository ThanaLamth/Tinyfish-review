#!/usr/bin/env python3
"""
tools/capture_local.py
Capture screenshots using local Playwright (no TinyFish credits needed).
Fallback for when TinyFish browser sessions are unavailable.

Usage:
    python tools/capture_local.py https://app.1inch.io --out screenshots/app.1inch.io
    python tools/capture_local.py https://uniswap.org
"""
import argparse, json, sys, os, time
from pathlib import Path
from playwright.sync_api import sync_playwright

DEVICE_PROFILES = {
    "desktop": {
        "width": 1440, "height": 900, "device_scale_factor": 1, "is_mobile": False,
        "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
    },
    "tablet": {
        "width": 1024, "height": 1366, "device_scale_factor": 2, "is_mobile": True,
        "user_agent": "Mozilla/5.0 (iPad; CPU OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
    },
    "phone": {
        "width": 430, "height": 932, "device_scale_factor": 3, "is_mobile": True,
        "user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
    },
}

def capture_all(url: str, out_dir: Path, devices: list, proxy: str = ""):
    out_dir.mkdir(parents=True, exist_ok=True)
    results = {}

    proxy_cfg = None
    if proxy:
        parts = proxy.split(":")
        if len(parts) == 4:
            proxy_cfg = {
                "server": f"http://{parts[0]}:{parts[1]}",
                "username": parts[2],
                "password": parts[3],
            }

    with sync_playwright() as pw:
        for device_name in devices:
            prof = DEVICE_PROFILES[device_name]
            out_path = out_dir / f"{device_name}.png"
            print(f"  [{device_name:8s}] {prof['width']}x{prof['height']} ... ", end="", flush=True)

            launch_args = {"headless": True, "args": ["--no-sandbox", "--disable-dev-shm-usage"]}
            if proxy_cfg:
                launch_args["proxy"] = proxy_cfg

            browser = pw.chromium.launch(**launch_args)
            ctx = browser.new_context(
                viewport={"width": prof["width"], "height": prof["height"]},
                device_scale_factor=prof["device_scale_factor"],
                is_mobile=prof["is_mobile"],
                user_agent=prof["user_agent"],
                locale="en-US",
                extra_http_headers={"Accept-Language": "en-US,en;q=0.9"},
            )
            page = ctx.new_page()
            try:
                page.goto(url, timeout=45000, wait_until="domcontentloaded")
                page.wait_for_timeout(4000)
                page.screenshot(path=str(out_path), full_page=False)
                size_kb = out_path.stat().st_size // 1024
                print(f"{out_path.name} ({size_kb} KB)")
                results[device_name] = str(out_path)
            except Exception as exc:
                print(f"FAILED: {exc}")
            finally:
                browser.close()

    summary = out_dir / "capture_summary.json"
    summary.write_text(json.dumps({"url": url, "screenshots": results}, indent=2), encoding="utf-8")
    print(f"Done. Summary: {summary}")
    return results


def main():
    parser = argparse.ArgumentParser(description="Capture URL on 3 devices using local Playwright")
    parser.add_argument("url", help="Target URL")
    parser.add_argument("--out", default=None)
    parser.add_argument("--device", default="all", choices=["all", "desktop", "tablet", "phone"])
    parser.add_argument("--proxy", default=os.getenv("PROXY", ""), help="host:port:user:pass")
    args = parser.parse_args()

    if args.out:
        out_dir = Path(args.out)
    else:
        domain = args.url.replace("https://", "").replace("http://", "").split("/")[0]
        out_dir = Path("screenshots") / domain

    devices = list(DEVICE_PROFILES.keys()) if args.device == "all" else [args.device]

    print(f"\nCapturing: {args.url}")
    print(f"Devices:   {', '.join(devices)}")
    print(f"Output:    {out_dir}\n")
    capture_all(args.url, out_dir, devices, proxy=args.proxy)


if __name__ == "__main__":
    main()

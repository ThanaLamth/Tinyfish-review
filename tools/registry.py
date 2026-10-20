#!/usr/bin/env python3
"""
tools/registry.py
Tracks all written articles to prevent duplicate processing.

Usage (standalone):
    python tools/registry.py list
    python tools/registry.py check https://kyberswap.com
    python tools/registry.py add https://newsite.com --slug newsite-review-2026 --type dex --path articles/newsite-review-2026.md
"""
import json, sys, argparse
from pathlib import Path
from datetime import date
from urllib.parse import urlparse

REGISTRY_PATH = Path(__file__).parent.parent / "articles" / "registry.json"


def _normalize(url: str) -> str:
    parsed = urlparse(url.lower().rstrip("/"))
    return parsed.netloc or parsed.path


def load() -> list:
    if not REGISTRY_PATH.exists():
        return []
    try:
        return json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return []


def save(records: list):
    REGISTRY_PATH.parent.mkdir(parents=True, exist_ok=True)
    REGISTRY_PATH.write_text(json.dumps(records, indent=2, ensure_ascii=False), encoding="utf-8")


def check(url: str) -> dict:
    """Return existing record if url/domain already written, else empty dict."""
    needle = _normalize(url)
    for rec in load():
        if _normalize(rec.get("url", "")) == needle:
            return rec
    return {}


def register(url: str, slug: str, site_type: str, article_path: str, git_pushed: bool = False):
    """Add a new entry to the registry. Skips if already present."""
    if check(url):
        print(f"[registry] Already registered, skipping: {url}")
        return
    records = load()
    records.append({
        "url":          url,
        "domain":       _normalize(url),
        "slug":         slug,
        "site_type":    site_type,
        "date_written": date.today().isoformat(),
        "article_path": str(article_path),
        "git_pushed":   git_pushed,
    })
    save(records)
    print(f"[registry] Registered: {url}  ->  {slug}")


def mark_pushed(url: str):
    """Mark an existing registry entry as git-pushed."""
    records = load()
    needle = _normalize(url)
    for rec in records:
        if _normalize(rec.get("url", "")) == needle:
            rec["git_pushed"] = True
    save(records)


# ─── CLI ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Article registry management")
    sub = parser.add_subparsers(dest="cmd")

    sub.add_parser("list", help="List all registered articles")

    p_check = sub.add_parser("check", help="Check if a URL is already registered")
    p_check.add_argument("url")

    p_add = sub.add_parser("add", help="Manually add a registry entry")
    p_add.add_argument("url")
    p_add.add_argument("--slug",  required=True)
    p_add.add_argument("--type",  required=True, dest="site_type")
    p_add.add_argument("--path",  required=True, dest="article_path")

    p_rm = sub.add_parser("remove", help="Remove an entry (to allow re-write)")
    p_rm.add_argument("url")

    args = parser.parse_args()

    if args.cmd == "list":
        records = load()
        if not records:
            print("Registry is empty.")
            return
        print(f"{'Date':12s}  {'Domain':35s}  {'Slug':45s}  Pushed")
        print("-" * 100)
        for r in records:
            pushed = "yes" if r.get("git_pushed") else "no"
            print(f"{r.get('date_written','?'):12s}  {r.get('domain','?'):35s}  {r.get('slug','?'):45s}  {pushed}")

    elif args.cmd == "check":
        rec = check(args.url)
        if rec:
            print(f"DUPLICATE  {args.url}")
            print(json.dumps(rec, indent=2))
            sys.exit(1)
        else:
            print(f"OK - not in registry: {args.url}")

    elif args.cmd == "add":
        if check(args.url):
            print(f"Already registered: {args.url}")
            sys.exit(1)
        register(args.url, args.slug, args.site_type, args.article_path)

    elif args.cmd == "remove":
        records = load()
        needle = _normalize(args.url)
        before = len(records)
        records = [r for r in records if _normalize(r.get("url", "")) != needle]
        if len(records) == before:
            print(f"Not found in registry: {args.url}")
        else:
            save(records)
            print(f"Removed: {args.url}")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()

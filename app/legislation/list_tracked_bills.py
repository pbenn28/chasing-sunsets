#!/usr/bin/env python3
"""Lists every bill currently tracked in app/legislation/*.md.

Run this before sweeping external trackers (GovTrack, congress.gov, AAF, etc.)
for missing AI legislation, so you know what's already covered without
opening every file by hand.

Usage: python3 app/legislation/list_tracked_bills.py
"""
import glob
import os

import yaml


def main():
    bills_dir = os.path.dirname(os.path.abspath(__file__))
    entries = []

    for filepath in sorted(glob.glob(os.path.join(bills_dir, "*.md"))):
        with open(filepath) as f:
            content = f.read()
        metadata = yaml.safe_load(content.split("---", 2)[1]) or {}
        entries.append({
            "slug": os.path.splitext(os.path.basename(filepath))[0],
            "title": metadata.get("title", ""),
            "bill_numbers": metadata.get("bill_numbers") or [],
            "status": metadata.get("status", ""),
        })

    for e in entries:
        numbers = ", ".join(e["bill_numbers"]) if e["bill_numbers"] else "(no bill number yet — discussion draft)"
        print(f"- {e['title']}")
        print(f"    numbers: {numbers}")
        print(f"    status:  {e['status']}")
        print(f"    slug:    {e['slug']}")

    print(f"\n{len(entries)} bills currently tracked.")


if __name__ == "__main__":
    main()

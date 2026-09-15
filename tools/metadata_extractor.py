#!/usr/bin/env python3
"""
metadata_extractor.py
-----------------------
Simulates metadata extraction from acquired evidence files: file size,
modification time, and SHA-256, similar to what `exiftool` or a forensic
suite's "file listing" view would produce for non-proprietary file types.

Usage:
    python3 metadata_extractor.py <folder>
"""

import argparse
import hashlib
import os
from datetime import datetime, timezone


def sha256_of_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(65536), b""):
            h.update(block)
    return h.hexdigest()


def main():
    parser = argparse.ArgumentParser(description="Extract basic forensic metadata for files in a folder.")
    parser.add_argument("folder")
    args = parser.parse_args()

    print(f"{'FILE':40} {'SIZE(B)':>8} {'MODIFIED (UTC)':22} SHA-256")
    for root, _, files in os.walk(args.folder):
        for name in sorted(files):
            path = os.path.join(root, name)
            rel = os.path.relpath(path, args.folder)
            size = os.path.getsize(path)
            # File modification time — in a real case this is a key
            # forensic timestamp (when was this file last written?).
            mtime = datetime.fromtimestamp(os.path.getmtime(path), tz=timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
            digest = sha256_of_file(path)
            # Truncate the hash for display readability; full hash is
            # already recorded separately in evidence-hashes.sha256.
            print(f"{rel:40} {size:>8} {mtime:22} {digest[:16]}...")


if __name__ == "__main__":
    main()
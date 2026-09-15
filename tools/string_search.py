#!/usr/bin/env python3
"""
string_search.py
------------------
Simulates a forensic keyword/string search across acquired evidence files
(analogous to `grep -R`, EnCase's keyword search, or Autopsy's keyword
search module).

Usage:
    python3 string_search.py <folder> <keyword1> [keyword2 ...]

For each keyword, reports every file and line where it appears, so an
investigator can build an evidence log of relevant hits.
"""

import argparse
import os
import re
import sys


def search(folder, keywords):
    hits = []
    # Walk every file in the evidence folder and check each line
    # against every keyword we were given.
    for root, _, files in os.walk(folder):
        for name in sorted(files):
            path = os.path.join(root, name)
            try:
                with open(path, "r", errors="ignore") as f:
                    for lineno, line in enumerate(f, 1):
                        for kw in keywords:
                            # re.escape() so keywords with special chars
                            # (like "$" in a filename) don't break the regex
                            if re.search(re.escape(kw), line, re.IGNORECASE):
                                hits.append((os.path.relpath(path, folder), lineno, kw, line.strip()))
            except (UnicodeDecodeError, OSError):
                # Skip binary/unreadable files (e.g. skimmer_dump.bin's
                # non-text sections) rather than crashing the whole scan.
                continue
    return hits


def main():
    parser = argparse.ArgumentParser(description="Forensic string/keyword search over a folder.")
    parser.add_argument("folder")
    parser.add_argument("keywords", nargs="+")
    args = parser.parse_args()

    hits = search(args.folder, args.keywords)
    if not hits:
        print("No hits found.")
        sys.exit(0)

    print(f"{'FILE':40} {'LINE':>5} {'KEYWORD':15} CONTEXT")
    for path, lineno, kw, context in hits:
        print(f"{path:40} {lineno:>5} {kw:15} {context}")
    print(f"\nTotal hits: {len(hits)}")


if __name__ == "__main__":
    main()
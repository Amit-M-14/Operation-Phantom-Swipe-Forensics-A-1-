#!/usr/bin/env python3
"""
hash_generator.py
------------------
Digital forensics evidence hashing utility.

Purpose: Computes SHA-256 hashes for a directory of acquired files,
simulating the hashing step performed after imaging/seizing digital
evidence (e.g., with `sha256sum` on a write-blocked source, or via
tools like FTK Imager / EnCase / dc3dd in a real investigation).

Usage:
    python3 hash_generator.py <folder> [--out hashes.sha256]

Hashing evidence immediately after acquisition, and again before/after
analysis, is how an investigator proves the evidence was not altered
(integrity verification) — a core requirement for admissibility.
"""

import argparse
import hashlib
import os
import sys
from datetime import datetime, timezone


def sha256_of_file(path, block_size=65536):
    # Read the file in chunks (not all at once) so this scales to
    # large evidence files without blowing up memory.
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(block_size), b""):
            h.update(block)
    return h.hexdigest()


def main():
    parser = argparse.ArgumentParser(description="Compute SHA-256 hashes of evidence files.")
    parser.add_argument("folder", help="Folder containing acquired evidence files")
    parser.add_argument("--out", default="evidence-hashes.sha256", help="Output hash log file")
    args = parser.parse_args()

    if not os.path.isdir(args.folder):
        print(f"Error: {args.folder} is not a directory", file=sys.stderr)
        sys.exit(1)

    results = []
    # Walk every file in the folder (including subfolders like skimmer/ and phone/)
    for root, _, files in os.walk(args.folder):
        for name in sorted(files):
            full_path = os.path.join(root, name)
            rel_path = os.path.relpath(full_path, args.folder)
            digest = sha256_of_file(full_path)
            results.append((rel_path, digest))

    # Write a timestamped log — timestamps matter for chain-of-custody records
    timestamp = datetime.now(timezone.utc).isoformat()
    with open(args.out, "w") as out:
        out.write(f"# SHA-256 Evidence Hash Log\n")
        out.write(f"# Generated (UTC): {timestamp}\n")
        out.write(f"# Source folder: {args.folder}\n\n")
        for rel_path, digest in results:
            line = f"{digest}  {rel_path}"
            print(line)
            out.write(line + "\n")

    print(f"\n[{len(results)} file(s) hashed] -> {args.out}")


if __name__ == "__main__":
    main()
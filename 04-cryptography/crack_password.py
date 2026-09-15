#!/usr/bin/env python3
"""
crack_password.py
-------------------
Simulates a dictionary-attack password recovery on a password-protected
ZIP archive found in the seized evidence, analogous to what an
investigator would do with `fcrackzip`, `zip2john` + `John the Ripper`,
or `hashcat` mode 17200/17210 (Legacy PKZIP / WinZip AES) on real evidence.

This script tries each candidate password from a wordlist against an
AES-encrypted archive using pyzipper (Python's built-in zipfile module
cannot read AES-encrypted zips, only the older ZipCrypto format, so
pyzipper is required here).

Usage:
    python3 crack_password.py <zip_file> <wordlist.txt>

Legal/ethical note: this script is run ONLY against evidence lawfully
seized under this investigation's authority (or, in this coursework
context, against a file the student created themselves). Running password
recovery tools against systems/files you do not have legal authority
over is illegal in most jurisdictions.
"""

import argparse
import sys
import time
import pyzipper


def crack(zip_path, wordlist_path):
    with pyzipper.AESZipFile(zip_path) as zf:
        with open(wordlist_path, "r") as wl:
            candidates = [line.strip() for line in wl if line.strip()]

        print(f"Loaded {len(candidates)} candidate passwords from {wordlist_path}")
        start = time.time()

        for i, candidate in enumerate(candidates, 1):
            try:
                zf.extractall(pwd=candidate.encode("utf-8"))
                elapsed = time.time() - start
                print(f"\n[+] SUCCESS after {i} attempt(s), {elapsed:.4f}s")
                print(f"[+] Password found: '{candidate}'")
                return candidate
            except RuntimeError:
                print(f"[-] Attempt {i}: '{candidate}' -> failed")
                continue

        print("\n[-] Password not found in wordlist.")
        return None


def main():
    parser = argparse.ArgumentParser(description="Dictionary attack against a password-protected zip.")
    parser.add_argument("zip_file")
    parser.add_argument("wordlist")
    args = parser.parse_args()

    result = crack(args.zip_file, args.wordlist)
    sys.exit(0 if result else 1)


if __name__ == "__main__":
    main()
# Operation Phantom Swipe
### Investigating a Cross-Border ATM & Credit Card Fraud Ring
**Assignment 1 — Unit 1: Foundations of Digital Forensics**

## Authorship Declaration

This repository was prepared by Amit Mohanty (2301730325) as
Assignment 1 for [CyberCrime and Investigation]. All simulated evidence (card numbers,
communication logs, GPS coordinates, financial figures) is fabricated
for coursework purposes only and does not reference real individuals,
accounts, or devices.

## Repository Structure

```
├── 01-classification/         # Sub-Problem 1: Cybercrime taxonomy & legal mapping
│   └── cybercrime-taxonomy.md
├── 02-evidence-collection/    # Sub-Problem 2: Simulated seizure & chain of custody
│   ├── chain-of-custody-form.md
│   ├── acquisition-log.md
│   ├── evidence-hashes.sha256
│   └── simulated-devices/
│       ├── skimmer/           # Dummy data from seized skimmer device
│       └── phone/              # Dummy data from seized suspect phone
├── 03-media-analysis/         # Sub-Problem 3: Search, analysis, artefact extraction
│   ├── search-strategy.md
│   ├── evidence-log.md
│   ├── string-search-results.txt
│   ├── metadata-extraction-results.txt
│   └── extracted-artefacts/   # 6 documented artefacts
├── 04-cryptography/           # Sub-Problem 4: Password recovery simulation
│   ├── locked_evidence.zip    # Password-protected evidence folder (AES-256)
│   ├── wordlist.txt
│   ├── crack_password.py
│   ├── crack-run-output.txt   # Actual run output (password recovered)
│   └── cryptography-writeup.md
├── 05-report/                 # Sub-Problem 5: Legal-technical report
│   ├── generate_report.py     # Script that builds the .docx
│   └── Legal-Technical-Report.docx
├── tools/                     # Reusable forensic scripts
│   ├── hash_generator.py
│   ├── string_search.py
│   └── metadata_extractor.py
└── .github/workflows/validate.yml   # CI: checks all deliverables are present
```

## Execution Guide

Dependencies are managed with `uv`. Set up once:
```bash
uv sync
```

### 1. Regenerate evidence hashes
```bash
uv run tools/hash_generator.py 02-evidence-collection/simulated-devices \
    --out 02-evidence-collection/evidence-hashes.sha256
```

### 2. Re-run the keyword search across evidence
```bash
uv run tools/string_search.py 02-evidence-collection/simulated-devices \
    wallet track mule batch skimmer
```

### 3. Re-run metadata extraction
```bash
uv run tools/metadata_extractor.py 02-evidence-collection/simulated-devices
```

### 4. Re-run the password recovery (dictionary attack) on the locked folder
```bash
cd 04-cryptography
uv run crack_password.py locked_evidence.zip wordlist.txt
```
Expected output: password `sunshine1` recovered on the 5th attempt (full
log in `crack-run-output.txt`).

### 5. Regenerate the report
```bash
cd 05-report
uv run generate_report.py
```

## Tools Used

| Tool | Type | Purpose |
|---|---|---|
| `tools/hash_generator.py` | Python (stdlib `hashlib`) | SHA-256 integrity hashing of acquired evidence |
| `tools/string_search.py` | Python (stdlib) | Keyword/string search across evidence files |
| `tools/metadata_extractor.py` | Python (stdlib) | File metadata cataloguing (size, mtime, hash) |
| `04-cryptography/crack_password.py` | Python (`pyzipper`) | Dictionary-attack password recovery on AES-encrypted zip |
| `05-report/generate_report.py` | Python (`python-docx`) | Generates the Word report |
| GitHub Actions | CI | Automated structure/deliverable validation |

These simulate real forensic tooling (`sha256sum`/FTK Imager, `grep -R`/
Autopsy keyword search, `exiftool`, and `hashcat`/John the Ripper
respectively) at a scale appropriate for coursework.

## Deliverables Checklist (per assignment brief)

- [x] Simulated media files, extracted artefacts, password-protected folder
- [x] Legal-technical report (DOCX)
- [x] Cracking/analysis tools used (Python)
- [x] Tool run outputs (search results, crack log)
- [x] Chain of custody form
- [x] Hash values of collected artefacts (SHA-256, 6 files)
- [x] Execution guide, tools used, authorship declaration (this file)
- [x] GitHub Action for validating repo structure

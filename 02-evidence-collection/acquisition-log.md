# Evidence Acquisition Log

| Timestamp (UTC) | Action | Tool (simulated) | Operator | Result |
|---|---|---|---|---|
| 2026-06-12T00:50:00Z | Photographed skimmer in situ before removal | Camera | Investigator | 6 photos logged |
| 2026-06-12T00:55:00Z | Removed skimmer, bagged, sealed (TE-4471) | — | Investigator | Sealed |
| 2026-06-12T01:40:00Z | Phone isolated in Faraday bag on seizure | Faraday bag | Investigator | Sealed (TE-4472) |
| 2026-06-13T04:30:00Z | Skimmer flash dumped via write-blocked interface | JTAG/UART reader + write-blocker | Analyst | `skimmer_dump.bin`, `skimmer_firmware_info.txt`, `capture_metadata.csv` |
| 2026-06-13T05:10:00Z | Phone logically imaged | ADB (write-blocked, USB debug mode) | Analyst | `fraud_app_manifest.txt`, `comm_logs.txt`, `gps_log.json` |
| 2026-06-13T05:30:00Z | SHA-256 hashes computed for all extracted files | `tools/hash_generator.py` | Analyst | `evidence-hashes.sha256` (6 files) |
| 2026-06-13T05:45:00Z | Hash values cross-checked against a second run | `tools/hash_generator.py` | Analyst | Match confirmed — no drift |

**Note on real-world equivalents:** In an actual investigation the tools
used here would be replaced with forensic-grade equivalents — e.g. Cellebrite
UFED or Magnet AXIOM for the phone, and a hardware write-blocker (Tableau/
WieBetech) plus FTK Imager or `dc3dd` for the skimmer's flash memory. This
simulation uses simplified scripted extraction to demonstrate the same
methodology.
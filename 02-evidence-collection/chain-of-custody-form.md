# Chain of Custody Form
## Case: Operation Phantom Swipe — Cross-Border ATM & Credit Card Fraud

**Case No.:** OPS-2026-014
**Investigating Officer:** [Your Name]
**Location of Seizure:** ATM Branch 14 & Suspect Residence

---

### Item 1

| Field | Detail |
|---|---|
| Evidence ID | EVD-001 |
| Description | Covert ATM skimmer overlay device |
| Seized From | ATM Branch 14, card slot overlay |
| Date/Time Seized | 2026-06-12, 06:20 IST |
| Seized By | [Your Name], Digital Forensics Investigator |
| Condition on Seizure | Intact, powered off, no visible tamper damage |
| Storage | Anti-static evidence bag, tamper-evident seal #TE-4471 |
| Imaging Method | Onboard flash dumped via write-blocked JTAG/UART interface (simulated) |
| SHA-256 (image) | See `evidence-hashes.sha256` — skimmer/skimmer_dump.bin |

### Item 2

| Field | Detail |
|---|---|
| Evidence ID | EVD-002 |
| Description | Suspect's mobile phone (Android) containing fraudulent app |
| Seized From | Suspect's person, at time of detention |
| Date/Time Seized | 2026-06-12, 07:10 IST |
| Seized By | [Your Name], Digital Forensics Investigator |
| Condition on Seizure | Powered on, placed in Faraday bag immediately to prevent remote wipe |
| Storage | Faraday evidence bag, tamper-evident seal #TE-4472 |
| Imaging Method | Logical acquisition via forensic write-blocker + ADB (simulated) |
| SHA-256 (extracted files) | See `evidence-hashes.sha256` — phone/*.* |

---

### Custody Transfer Log

| # | Date/Time | Released By | Received By | Purpose | Signature |
|---|---|---|---|---|---|
| 1 | 2026-06-12 07:30 | [Your Name] (Field) | [Your Name] (Lab) | Transport to forensic lab | ______ |
| 2 | 2026-06-12 09:00 | [Your Name] (Lab) | Evidence Locker | Secure storage pending analysis | ______ |
| 3 | 2026-06-13 10:00 | Evidence Locker | [Your Name] (Analyst) | Forensic imaging & analysis | ______ |
| 4 | 2026-06-13 17:00 | [Your Name] (Analyst) | Evidence Locker | Return after imaging complete | ______ |

---

### Evidence Handling Principles Applied

- **Write blockers:** All imaging performed through a hardware/software
  write-blocker so the original media is mounted read-only, preventing
  any modification of source data (timestamps, deleted-file remnants, etc.).
- **Hashing before and after:** SHA-256 hash computed immediately after
  acquisition and re-verified before analysis and again before reporting,
  to prove the working copy matches the original bit-for-bit.
- **Bag and tag:** Each item sealed in tamper-evident packaging immediately
  on seizure, with a unique seal number logged.
- **Faraday isolation:** The phone was isolated from cellular/Wi-Fi/Bluetooth
  networks immediately to prevent remote wipe or evidence tampering.
- **Minimal handling:** Only the assigned analyst accessed original media;
  all analysis was performed on verified forensic copies, never the original.
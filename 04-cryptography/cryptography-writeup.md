# Cryptography Component — Password Recovery Simulation

## 1. Scenario

During analysis, one folder in the seized data (`locked_evidence.zip`,
containing a note on suspect offshore-account routing) was found to be
password-protected with AES-256 encryption. A dictionary attack was
simulated to recover access.

## 2. Method

`crack_password.py` performs a dictionary attack against the AES-encrypted
ZIP archive using the `pyzipper` library (Python's built-in `zipfile`
module cannot read AES-encrypted zips, only the older ZipCrypto format).
This is functionally equivalent to using `hashcat` mode 17200/17210
(WinZip AES) or `John the Ripper` with `zip2john` on real forensic
hardware, which support both legacy and AES-encrypted archives.

A 10-entry wordlist (`wordlist.txt`) of common/weak passwords was used.
**Actual run output** (`crack-run-output.txt`):

Loaded 10 candidate passwords from wordlist.txt
[-] Attempt 1: '123456' -> failed
[-] Attempt 2: 'password' -> failed
[-] Attempt 3: 'qwerty123' -> failed
[-] Attempt 4: 'letmein' -> failed

[+] SUCCESS after 5 attempt(s), 0.0012s
[+] Password found: 'sunshine1'


The password `sunshine1` was recovered on the 5th attempt.

## 3. Why a Dictionary Attack (vs. Pure Brute Force)

- **Brute force** tries every possible character combination — guaranteed
  to succeed eventually, but for an 8+ character alphanumeric password
  this can take from hours to years depending on hardware and password
  complexity, and AES-256 specifically has no known practical shortcut —
  brute force against the key itself is computationally infeasible, so
  cracking always targets the *password*, not the cipher.
- **Dictionary attack** tries known/likely passwords first (leaked
  password lists, common patterns, personalization based on the suspect's
  known interests/dates). This is dramatically faster when the target
  reused a weak or common password — as demonstrated here, where the
  correct password was a dictionary word plus a digit, found in
  milliseconds rather than requiring exhaustive search.
- In real casework, tools like **hashcat** and **John the Ripper** combine
  both: dictionary + rule-based mutations (adding numbers, capitalization,
  leetspeak) before falling back to brute force, and can leverage GPU
  acceleration for speed.

## 4. Reflection on Password Strength in Criminal Scenarios

This case illustrates a very common pattern in real investigations:
individuals engaged in sophisticated fraud schemes (skimming hardware,
cross-border money mule networks) frequently protect their own sensitive
files with **weak, memorable passwords** — a mismatch between operational
sophistication and personal security hygiene. This is a well-documented
phenomenon in digital forensics casework and is precisely why dictionary
and rule-based attacks succeed so often in practice, even against strong
encryption algorithms like AES-256, without needing to resort to lengthy
brute-force searches.

## 5. Ethical & Legal Implications: Brute-Forcing vs. Lawful Decryption Requests

| Aspect | Brute-force / password cracking | Lawful decryption request |
|---|---|---|
| **Legal basis** | Requires that investigators already have lawful custody of the device/data (e.g., under a search warrant) — cracking a password on *lawfully seized* evidence is legitimate forensic work | Compels a person (via court order) to provide a password or decrypt data themselves |
| **Rights implications** | Does not require suspect cooperation; no self-incrimination concerns | In many jurisdictions raises constitutional/self-incrimination questions (e.g., right against self-incrimination under Article 20(3) of the Indian Constitution) |
| **Reliability** | Works only if the password is weak/guessable; strong passwords + strong encryption (AES-256 with a high-entropy password) can be practically uncrackable | Guarantees access if compliance is obtained, regardless of password strength |
| **Proportionality concerns** | Should be scoped to evidence within the warrant's authority; cracking devices/accounts outside that scope is unlawful | Court oversight is generally built into the process, providing a check on scope |
| **Time/resource cost** | Can be very fast (weak passwords) or practically infeasible (strong passwords) | Typically resolved once compliance/court order is obtained, but can be contested and delayed in court |

**Conclusion:** Investigators should default to lawful process (warrants
for the device, court orders where applicable for compelled decryption)
and use technical cracking only within that lawful scope, on lawfully
acquired evidence, and only where proportionate — not as a substitute for
due process, and not against systems/accounts outside the warrant's
authority.
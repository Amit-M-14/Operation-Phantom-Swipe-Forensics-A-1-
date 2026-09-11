# Cybercrime Classification & Legal Mapping
## Case: Operation Phantom Swipe — Cross-Border ATM & Credit Card Fraud Ring

## 1. Scenario Summary

The case involves a fraud ring operating an ATM skimming device to capture card
data and PINs, combined with an app on a suspect's phone used to clone card
data and conduct fraudulent online transactions across borders.

## 2. Identified Crime Types

| # | Crime | Description |
|---|-------|-------------|
| 1 | ATM Skimming | Covert hardware device attached to an ATM card slot to copy magnetic-stripe data, often paired with a hidden camera or fake keypad to capture PINs |
| 2 | Credit Card Cloning | Using captured track data to write a duplicate magnetic stripe onto a blank card |
| 3 | Online Card Fraud / Card-Not-Present (CNP) Fraud | Using stolen card data to make unauthorized online purchases without the physical card |
| 4 | Identity Theft | Use of victims' personal/financial identity to conduct transactions |
| 5 | Unauthorized Access to a Computer System | Installing/using the fraudulent app and accessing financial systems without authorization |
| 6 | Cross-Border Data Transfer of Stolen Financial Data | Movement of skimmed data across jurisdictions for exploitation |

## 3. Taxonomy of Cybercrimes Observed

**Category A — Device-Based / Hardware Crime**
- ATM skimming (physical device + digital data capture)

**Category B — Data/Financial Crime**
- Card cloning, CNP fraud, identity theft

**Category C — Computer-Related Crime**
- Unauthorized access via fraudulent mobile app, malware/app misuse

**Category D — Transnational/Organized Crime**
- Cross-border data exfiltration and money movement, implicating multiple
  jurisdictions and requiring Mutual Legal Assistance Treaty (MLAT) cooperation

**Justification for taxonomy:** The classification follows the standard
digital forensics distinction between the *means* of the crime (hardware
skimmer = device-based), the *object* of the crime (financial/card data =
data crime), the *method of access* (unauthorized system/app use = computer
crime), and the *scope* (multi-jurisdictional = organized/transnational
crime). Grouping this way maps cleanly onto different legal provisions and
different evidence-handling requirements for each category.

## 4. Legal Mapping

### 4.1 Indian IT Act, 2000 (as amended)

| Section | Provision | Applicability |
|---|---|---|
| Sec 43 | Penalty for unauthorized access, downloading, damage to computer systems | Unauthorized access to card data / phone app |
| Sec 43A | Compensation for failure to protect sensitive personal data | If a bank/merchant's negligence contributed |
| Sec 66 | Computer-related offences (dishonestly/fraudulently doing an act under Sec 43) | Skimming device use, data theft |
| Sec 66C | Identity theft — fraudulent use of electronic signature, password, or unique identification | Use of stolen card/PIN data |
| Sec 66D | Cheating by personation using computer resource | Fraudulent online transactions |
| Sec 43 + 66B | Receiving stolen computer resource/communication device dishonestly | Possession of skimmed data/cloned cards |

### 4.2 Indian Penal Code, 1860 (now largely mirrored in BNS 2023, referenced here as IPC per assignment scope)

| Section | Provision | Applicability |
|---|---|---|
| Sec 420 | Cheating and dishonestly inducing delivery of property | Fraudulent withdrawal/purchase |
| Sec 379 | Theft | Theft of card data/funds |
| Sec 468 | Forgery for purpose of cheating | Cloned card = forged document |
| Sec 471 | Using a forged document as genuine | Using cloned card at ATM/POS |
| Sec 34 | Common intention | Multiple actors in the ring acting together |
| Sec 120B | Criminal conspiracy | Organized nature of the ring |

### 4.3 International — Budapest Convention on Cybercrime (2001)

| Article | Provision | Applicability |
|---|---|---|
| Art. 2 | Illegal access | Unauthorized access to card systems/app |
| Art. 3 | Illegal interception | Skimming = interception of card data in transit through the reader |
| Art. 7 | Computer-related forgery | Cloned card data |
| Art. 8 | Computer-related fraud | Online fraudulent transactions |
| Art. 25 | Mutual legal assistance | Cross-border evidence sharing/extradition cooperation |

**Note:** India is not a signatory to the Budapest Convention but the
Convention is referenced here as the international benchmark framework and
is relevant when cooperating with signatory states during cross-border
investigation.

## 5. Summary Table (Crime → Law)

| Crime | IT Act | IPC | Budapest Convention |
|---|---|---|---|
| ATM Skimming | 43, 66 | 379, 420 | Art. 2, 3 |
| Card Cloning | 66C | 468, 471 | Art. 7 |
| Online/CNP Fraud | 66D | 420 | Art. 8 |
| Organized/Cross-border | 66, 43 | 120B, 34 | Art. 25 |
# Electronic Media Search Strategy

## 1. Objective

Locate and document evidentiary artefacts within the acquired skimmer and
phone data without altering the underlying evidence (all analysis run
against forensic copies, never the sealed originals).

## 2. Approach

1. **File/metadata inventory first** — before searching content, catalog
   every acquired file with size, modification time, and hash
   (`tools/metadata_extractor.py`), producing a baseline for the evidence
   log.
2. **Keyword/string search** — run targeted keyword searches across all
   extracted text-based files (`tools/string_search.py`) for terms
   associated with the crime: financial terms ("wallet", "batch", "track"),
   operational terms ("mule", "skimmer"), and any card-number-like patterns.
   This mirrors keyword-search modules in tools like Autopsy/EnCase.
3. **Structured data review** — GPS logs and CSV metadata reviewed directly
   for timestamps/coordinates that place the suspect device at the scene.
4. **Cross-referencing** — artefacts found in one source (e.g., a GPS
   timestamp) are cross-checked against artefacts in another source (e.g.,
   a communication log entry at a similar time) to corroborate the
   narrative — this is how ART-004 and ART-006 support ART-002/ART-003.
5. **Chain of evidence for each artefact** — every artefact extracted is
   logged with its source file, extraction method, and relevance (see
   `evidence-log.md` and `extracted-artefacts/`).

## 3. Tools Used (with real-world equivalents)

| Simulated Tool | Purpose | Real-world Equivalent |
|---|---|---|
| `hash_generator.py` | Integrity hashing | `sha256sum`, FTK Imager |
| `string_search.py` | Keyword search | `grep -R`, Autopsy Keyword Search, EnCase |
| `metadata_extractor.py` | File metadata cataloguing | `exiftool`, Autopsy File Listing |

## 4. Search Terms Used

`wallet`, `track`, `mule`, `batch`, `skimmer`

## 5. Results Summary

10 keyword hits across 2 files, yielding 6 documented artefacts (card
track data, mule account reference, coordination messages, and two GPS
placements). Full raw output in `string-search-results.txt` and
`metadata-extraction-results.txt`.
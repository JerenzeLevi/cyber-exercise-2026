# OFA P2-09 — Information-Stealer POST Profile

## Objective
What Content-Type was used, how many POST transactions occurred, and what was the largest request body size, for POSTs to the information-stealer destination (`79.141.165.202`)?

**Hint given:** Aggregate HTTP POSTs to the information-stealer destination. Submit size as digits only.

## Investigation

**Tool used:** Security Onion Hunt — Zeek HTTP logs.

**Method:**
Aggregated all `zeek.http` POST transactions to `79.141.165.202` (the StealC endpoint identified in OFA P2-08):
- Total POST count: **22** (confirmed via a unique-match query).
- Largest request body size: **466352 bytes** (confirmed via a unique-match query).
- Content-Type: Zeek's `file.orig_mime_types` reported `text/plain` — but this is a **content-sniffed** value derived by Zeek's file-magic detection, not a literal captured `Content-Type:` request header. This Zeek deployment does not appear to log the raw HTTP request header for this field separately.

## Evidence

- POST count to 79.141.165.202: 22 (verified)
- Largest POST body: 466352 bytes (verified)
- Zeek `file.orig_mime_types`: text/plain (sniffed, not header-literal)

## Attempts Submitted (all rejected)

`CTK{text/plain|22|466352}` plus two alternate Content-Type guesses. The count and size portions are considered solid; the Content-Type value is the likely point of failure.

## Status

**UNRESOLVED — left blank per explicit instruction.** Do not guess an answer without further direction. If revisited, next step would be to check whether Zeek logged a literal `Content-Type` request header field separately from the sniffed MIME type, or to try the generic/canonical MIME convention lesson learned in Phase 5 (e.g. `application/octet-stream` in place of a sniffed type).

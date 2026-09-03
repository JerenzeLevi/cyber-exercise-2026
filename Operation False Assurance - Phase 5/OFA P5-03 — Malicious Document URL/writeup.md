# OFA P5-03 — Malicious Document URL

## Objective
Identify the complete HTTP URL that delivered the initial malicious document.

## Investigation

**Tool used:** Security Onion Hunt — Zeek HTTP logs.

**Method:**
Filtered HTTP GET requests from the infected client (`192.168.200.95`) for document-type responses (Word/RTF) in the earliest portion of the Phase 5 timeline. Identified the initial malicious-document delivery URL.

## Evidence

- Full HTTP GET URL retrieving the initial lure document from `r2consulting.net`.

## Finding

| Item | Value |
|---|---|
| Malicious document URL | http://r2consulting.net/IRS-TRANSCRIPTS-037J/2/ |

## Answer

```
CTK{http://r2consulting.net/IRS-TRANSCRIPTS-037J/2/}
```

**Status: ACCEPTED** — confirmed by the challenge platform.

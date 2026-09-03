# OFA P5-04 — Document Response Metadata

## Objective
Identify the filename and MIME type recorded for the malicious document's HTTP response.

## Investigation

**Tool used:** Security Onion Hunt — Zeek HTTP/file logs.

**Method:**
Expanded the `zeek.http`/`zeek.files` record for the response to the document URL identified in OFA P5-03 (`http://r2consulting.net/IRS-TRANSCRIPTS-037J/2/`), reading the recorded filename and MIME type fields.

## Evidence

- Filename: `transcript-June152018-017188/2.doc`
- MIME type: `application/msword`

## Finding

| Item | Value |
|---|---|
| Filename | transcript-June152018-017188/2.doc |
| MIME type | application/msword |

## Answer

```
CTK{transcript-June152018-017188/2.doc|application/msword}
```

**Status: ACCEPTED** — confirmed by the challenge platform.

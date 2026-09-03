# OFA P3-07 — Executable Metadata

## Objective
Provide the filename, MIME type, and response body size of the executable delivered in Phase 3.

**Hint given:** Use HTTP and file metadata. Submit size as digits only.

## Investigation

**Tool used:** Security Onion Hunt — Zeek HTTP/File logs.

**Method:**
Identified an executable transfer with filename `Renewable.exe`, response body size `10647040` bytes (one attempt used `10647310`, likely a transcription error, and was also rejected). Two MIME type conventions were tried:
- Zeek's file-magic-detected type: `application/x-dosexec`
- The generic Windows-download convention: `application/x-msdownload`

## Attempts Submitted (all rejected)

- `CTK{Renewable.exe|application/x-dosexec|10647040}` (submitted twice)
- `CTK{Renewable.exe|application/x-dosexec|10647310}`
- `CTK{Renewable.exe|application/x-msdownload|10647040}` (submitted twice)

## Status

**UNRESOLVED.** Filename and byte size are believed correct (`10647040`, confirmed as the standard value across most attempts). The blocking factor is likely the MIME type field. Per the Phase 5 answer-key lesson (generic MIME convention, e.g. `application/octet-stream`, is sometimes preferred over Zeek's file-magic-sniffed type), the untested next candidate is `CTK{Renewable.exe|application/octet-stream|10647040}` — not yet submitted.

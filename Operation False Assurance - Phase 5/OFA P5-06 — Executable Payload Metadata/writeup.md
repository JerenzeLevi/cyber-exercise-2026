# OFA P5-06 — Executable Payload Metadata

## Objective
Provide the executable filename, MIME type, and response body size.

**Hint given:** Use HTTP and file metadata. Submit size as digits only.

## Investigation

**Tool used:** Security Onion Hunt — Zeek HTTP/file logs.

**Method:**
1. Expanded the `zeek.http`/`zeek.files` record for the executable payload delivered at `http://www.ownhive.com/MsWM2B0/` (OFA P5-05). Filename: `90352.exe`, byte count: `126976`.
2. **Key lesson — generic MIME type, not the file-magic-detected type.** Zeek's sniffed MIME type for this PE executable, `application/x-dosexec`, was submitted twice and rejected. Switching to the generic `application/octet-stream` (same filename, same byte count) was accepted immediately.
3. Byte count `126976` was independently triple-confirmed via: `zeek.http` response length, `zeek.file` `total_bytes`, and the file record's own `missing_bytes=0` / `overflow_bytes=0` / `extracted_cutoff=false` fields, proving a complete, untruncated capture. Bytes/filename were never the issue — only the MIME-type convention.

## Evidence

- Filename: `90352.exe`
- Byte count: `126976` (triple-confirmed)
- Zeek-sniffed MIME (rejected): `application/x-dosexec`
- Accepted generic MIME: `application/octet-stream`

## Finding

| Item | Value |
|---|---|
| Filename | 90352.exe |
| MIME type (accepted) | application/octet-stream |
| Response body size | 126976 bytes |

## Answer

```
CTK{90352.exe|application/octet-stream|126976}
```

**Status: ACCEPTED** — confirmed by the challenge platform.

**Lesson learned:** When a MIME-type answer is rejected using the tool-detected specific type, try the generic/canonical MIME type (`application/octet-stream`) before assuming the filename or size is wrong.

# OFA P5-05 — Executable Payload URL

## Objective
Provide the executable filename, MIME type, and response body size for the second-stage payload URL.

## Investigation

**Tool used:** Security Onion Hunt — Zeek HTTP logs.

**Method:**
Following the malicious document (OFA P5-03/P5-04), identified the subsequent HTTP GET request that retrieved the executable payload from `www.ownhive.com`.

## Evidence

- Full URL retrieving the second-stage executable.

## Finding

| Item | Value |
|---|---|
| Executable payload URL | http://www.ownhive.com/MsWM2B0/ |

## Answer

```
CTK{http://www.ownhive.com/MsWM2B0/}
```

**Status: ACCEPTED** — confirmed by the challenge platform.

**Note:** Despite the challenge description's `CTK{FILENAME|MIME_TYPE|BYTES}` template text (identical to OFA P5-06), the accepted answer format for this specific challenge was the full URL — see OFA P5-06 for the filename/MIME/size-format answer to the executable payload.

# OFA P1-09 — Large Archive Transfer

## Objective
What URI delivered the large archive? Provide the recorded filename and response body size.

## Investigation

**Tool used:** Security Onion (Hunt interface) — https://seco.cyberex.quest/

**Context:** Building on OFA P1-08 — the Cloudflare Tunnel POST (404) to maintaining-shelter-bailey-ordinance.trycloudflare.com.

**Query:**
```
source.ip:"160.9.3.101" AND event.dataset:"zeek.http"
```

**Method:**
1. Continuing chronologically through `zeek.http` events for `160.9.3.101`, the next (and final major) file-transfer request occurs at **2025-10-01 05:01:18.920 -04:00** (09:01:18.920 UTC):
   - `http.method`: GET
   - `http.virtual_host`: 85.209.129.105:2020
   - `http.uri`: `/testl11`
   - `http.useragent`: WindowsPowerShell/5.1.26100.4768
   - `http.status_code`: 200 OK
   - `http.response.body.length`: 26,922,546 bytes
2. Cross-referenced with the earlier `zeek.file` record for the same `log.id.uid` (C2qZ713cWuXatbYjDb): `file.name`: `test.zip`, `file.mime_type`: application/zip, `file.bytes.total`: 26,922,546 — matching the HTTP response body length exactly.
3. This is the large (~26 MB) archive previously noted in the P1-01/P1-04 findings as the final payload delivered in the script-delivery chain.

## Evidence

- `event.dataset`: zeek.http / zeek.file
- `log.id.uid`: C2qZ713cWuXatbYjDb
- `source.ip`: 160.9.3.101
- `destination.ip`: 85.209.129.105
- `destination.port`: 2020
- `http.method`: GET
- `http.uri`: /testl11
- `http.response.body.length`: 26922546
- `file.name`: test.zip
- `file.mime_type`: application/zip
- `@timestamp`: 2025-10-01T09:01:18.920Z

## Finding

| Item | Value |
|---|---|
| URI | /testl11 |
| Recorded Filename | test.zip |
| Response Body Size | 26922546 bytes |

## Answer

```
CTK{/testl11|test.zip|26922546}
```

**Status: CONFIRMED CORRECT** — accepted by the challenge platform.

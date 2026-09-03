# OFA P1-06 — Second Script Delivery

## Objective
What URI delivered the second script, and what filename was recorded for the response?

## Investigation

**Tool used:** Security Onion (Hunt interface) — https://seco.cyberex.quest/

**Context:** Building on OFA P1-05 — the first script (scriptv2.ps1) was delivered via GET /19 at 05:00:47.201 -04:00.

**Query:**
```
source.ip:"160.9.3.101" AND event.dataset:"zeek.http"
```

**Method:**
1. Continuing chronologically through the `zeek.http` events for `160.9.3.101`, the next request after the first script delivery occurs at **2025-10-01 05:00:53.575 -04:00** (09:00:53.575 UTC):
   - `http.method`: GET
   - `http.virtual_host`: 85.209.129.105:2020
   - `http.uri`: `/test112`
   - `http.useragent`: WindowsPowerShell/5.1.26100.4768
   - `http.status_code`: 200 OK
   - `file.resp_filenames`: `["test.ps1"]`
2. Notably, this request used a genuine PowerShell user-agent (unlike the first request's curl/8.14.1), consistent with the first delivered script (scriptv2.ps1) executing and reaching back out to fetch a second-stage script.

## Evidence

- `event.dataset`: zeek.http
- `log.id.uid`: Cktb803yzkrrCkYDyc
- `source.ip`: 160.9.3.101
- `destination.ip`: 85.209.129.105
- `destination.port`: 2020
- `http.method`: GET
- `http.uri`: /test112
- `http.virtual_host`: 85.209.129.105:2020
- `http.useragent`: WindowsPowerShell/5.1.26100.4768
- `file.resp_filenames`: test.ps1
- `@timestamp`: 2025-10-01T09:00:53.575Z

## Finding

| Item | Value |
|---|---|
| URI | /test112 |
| Filename Recorded for Response | test.ps1 |

## Answer

```
CTK{/test112|test.ps1}
```

**Status: CONFIRMED CORRECT** — accepted by the challenge platform.

# OFA P1-05 — First Script Delivery

## Objective
What URI delivered the first script, and what filename was recorded for the response?

## Investigation

**Tool used:** Security Onion (Hunt interface) — https://seco.cyberex.quest/

**Context:** Building on OFA P1-01 through P1-04 — affected workstation `160.9.3.101`; PowerShell delivery server `85.209.129.105:2020`.

**Query:**
```
source.ip:"160.9.3.101" AND event.dataset:"zeek.http"
```

**Method:**
1. Listed all `zeek.http` events for the affected workstation, ascending by timestamp.
2. The first HTTP request to the delivery server occurs at **2025-10-01 05:00:47.201 -04:00** (09:00:47.201 UTC):
   - `http.method`: GET
   - `http.virtual_host`: 85.209.129.105:2020
   - `http.uri`: `/19`
   - `http.useragent`: curl/8.14.1
   - `http.status_code`: 200 OK
   - `file.resp_filenames`: `["scriptv2.ps1"]`
3. A second, later request (05:00:53.575 -04:00) to `/test112` — this time using a genuine `WindowsPowerShell/5.1.26100.4768` user-agent — delivered `test.ps1`. This is a distinct, subsequent event and not the first script delivery.

## Evidence

- `event.dataset`: zeek.http
- `log.id.uid`: CqGE2b39Yb7ePbbQ25
- `source.ip`: 160.9.3.101
- `destination.ip`: 85.209.129.105
- `destination.port`: 2020
- `http.method`: GET
- `http.uri`: /19
- `http.virtual_host`: 85.209.129.105:2020
- `http.useragent`: curl/8.14.1
- `file.resp_filenames`: scriptv2.ps1
- `@timestamp`: 2025-10-01T09:00:47.201Z

## Finding

| Item | Value |
|---|---|
| URI | /19 |
| Filename Recorded for Response | scriptv2.ps1 |

## Answer

```
CTK{/19|scriptv2.ps1}
```

**Status: CONFIRMED CORRECT** — accepted by the challenge platform.

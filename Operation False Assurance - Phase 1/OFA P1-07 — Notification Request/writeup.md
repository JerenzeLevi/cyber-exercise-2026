# OFA P1-07 — Notification Request

## Objective
Which HTTP method and URI were used for the notification request, and what response status was returned?

## Investigation

**Tool used:** Security Onion (Hunt interface) — https://seco.cyberex.quest/

**Context:** Building on OFA P1-06 — the second script (test.ps1) was delivered via GET /test112 at 05:00:53.575 -04:00.

**Query:**
```
source.ip:"160.9.3.101" AND event.dataset:"zeek.http"
```

**Method:**
1. Continuing chronologically through `zeek.http` events for `160.9.3.101`, the next request after the second script delivery occurs at **2025-10-01 05:00:57.970 -04:00** (09:00:57.970 UTC):
   - `http.method`: POST
   - `http.virtual_host`: 85.209.129.105:2020
   - `http.uri`: `/notify`
   - `http.useragent`: WindowsPowerShell/5.1.26100.4768
   - `http.request.body.length`: 14 bytes
   - `http.response.body.length`: 4 bytes
   - `http.status_code`: 200 OK
2. The small, fixed-size request/response and the explicit `/notify` URI are consistent with a check-in/beacon request confirming successful script execution back to the attacker's delivery server, rather than a file transfer.

## Evidence

- `event.dataset`: zeek.http
- `log.id.uid`: C8kmUG21ryBXI6qCA8
- `source.ip`: 160.9.3.101
- `destination.ip`: 85.209.129.105
- `destination.port`: 2020
- `http.method`: POST
- `http.uri`: /notify
- `http.status_code`: 200
- `@timestamp`: 2025-10-01T09:00:57.970Z

## Finding

| Item | Value |
|---|---|
| HTTP Method | POST |
| URI | /notify |
| Response Status | 200 |

## Answer

```
CTK{POST|/notify|200}
```

**Status: CONFIRMED CORRECT** — accepted by the challenge platform.

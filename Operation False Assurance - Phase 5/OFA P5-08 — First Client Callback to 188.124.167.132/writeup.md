# OFA P5-08 — First Client Callback to 188.124.167.132

## Objective
Identify the infected client's first POST to `188.124.167.132:8082`. Provide the UTC time and URI path.

**Hint given:** Filter HTTP from `192.168.200.95` to `188.124.167.132:8082` and sort ascending.

## Investigation

**Tool used:** Security Onion Hunt — Zeek HTTP logs.

**Query:**
```
source.ip:"192.168.200.95" AND destination.ip:"188.124.167.132" AND destination.port:8082 AND http.method:"POST"
```
Sorted ascending by `@timestamp`.

**Method:**
Filtered all POST requests from the infected client `192.168.200.95` to the C2 endpoint `188.124.167.132:8082`, sorted ascending, and took the first record.

## Evidence

- First POST timestamp: `2025-10-11 09:07:06 UTC`
- URI path: `/del9/LINWOOD-WIN-PC_W617601.A59A58979C2CD535524D2D1317484AC8/90`

## Finding

| Item | Value |
|---|---|
| First callback time (UTC) | 2025-10-11 09:07:06 UTC |
| URI path | /del9/LINWOOD-WIN-PC_W617601.A59A58979C2CD535524D2D1317484AC8/90 |

## Answer

```
CTK{2025-10-11 09:07:06 UTC|/del9/LINWOOD-WIN-PC_W617601.A59A58979C2CD535524D2D1317484AC8/90}
```

**Status: ACCEPTED** — confirmed by the challenge platform.

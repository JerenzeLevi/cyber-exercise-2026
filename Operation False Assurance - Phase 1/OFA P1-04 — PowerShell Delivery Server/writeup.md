# OFA P1-04 — PowerShell Delivery Server

## Objective
Identify the IPv4 address and TCP port of the server that delivered the PowerShell-related files.

## Investigation

**Tool used:** Security Onion (Hunt interface) — https://seco.cyberex.quest/

**Context:** Building on OFA P1-01/P1-02/P1-03 — affected workstation `160.9.3.101`, first website `www.sepco.com`, next TLS server `louglas.com`.

**Query:**
```
source.ip:"160.9.3.101" AND event.dataset:"zeek.file"
```

**Method:**
1. Pulled all `zeek.file` (Zeek `files.log`) records for the affected workstation to identify files transferred over the network.
2. Results show 8 files, several delivered from `85.209.129.105`:

| Time (UTC-4) | Destination IP | Filename | MIME Type | Bytes |
|---|---|---|---|---|
| 05:00:47.505 | 85.209.129.105 | scriptv2.ps1 | text/plain | 16,255 |
| 05:00:53.871 | 85.209.129.105 | test.ps1 | text/plain | 30,691 |
| 05:00:57.970 | 85.209.129.105 | (unnamed) | text/plain | 14 |
| 05:00:58.749 | 85.209.129.105 | (unnamed) | (unset) | 4 |
| 05:01:19.215 | 85.209.129.105 | test.zip | application/zip | 26,922,546 |

3. Two files (`scriptv2.ps1`, `test.ps1`) have explicit `.ps1` (PowerShell script) extensions, both delivered from `85.209.129.105`. A `test.zip` (the large ~26 MB payload previously noted in P1-01/P1-02 evidence) was delivered from the same host.
4. Cross-referenced with earlier `zeek.http` findings (OFA P1-01 investigation): all HTTP GET/POST activity to `85.209.129.105` used TCP port **2020**, a non-standard port for HTTP.
5. Other files in the list (f.txt, json.txt, unnamed 2788-byte object) came from unrelated hosts (64.95.13.172, 104.16.231.132, 142.250.114.102) and are not PowerShell-related.

## Evidence

- `event.dataset`: zeek.file / zeek.http
- `destination.ip`: 85.209.129.105
- `destination.port`: 2020
- `file.name`: scriptv2.ps1, test.ps1
- `file.mime_type`: text/plain
- `log.id.fuid`: FEyXoY2QnMecF2y39 (scriptv2.ps1), FjNcF03kqfJD4VwdYe (test.ps1)
- `@timestamp`: 2025-10-01T09:00:47.505Z (scriptv2.ps1)

## Finding

| Item | Value |
|---|---|
| PowerShell Delivery Server IPv4 | 85.209.129.105 |
| TCP Port | 2020 |

## Answer

```
CTK{85.209.129.105|2020}
```

**Status: CONFIRMED CORRECT** — accepted by the challenge platform.

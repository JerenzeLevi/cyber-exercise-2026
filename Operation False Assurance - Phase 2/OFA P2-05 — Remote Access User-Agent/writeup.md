# OFA P2-05 — Remote Access User-Agent

## Objective
What User-Agent identified the remote-access software?

## Investigation

**Tool used:** Security Onion (Hunt interface) — https://seco.cyberex.quest/

**Context:** Building on the NetSupport gateway findings (P2-06) — workstation `10.8.20.101` communicating with the NetSupport gateway `38.146.28.242:1203`.

**Query:**
```
source.ip:"10.8.20.101" AND event.dataset:"zeek.software"
```
(per hint: inspect the HTTP User-Agent field — Zeek's `software.log`/`zeek.software` dataset parses the User-Agent header of HTTP traffic and classifies the resulting software name/type automatically.)

**Method:**
1. Queried Zeek's software-identification log for the affected workstation. Zeek automatically extracts and classifies software identity strings (including the HTTP `User-Agent` header) into `software.name` and `software.type`.
2. Result, captured live during the investigation session:
   ```
   2025-10-03 05:12:56.271 -04:00   zeek.software   10.8.20.101   NetSupport Manager   HTTP::BROWSER
   ```
   - `software.name`: NetSupport Manager
   - `software.type`: HTTP::BROWSER (i.e., derived from the HTTP client's User-Agent string)
   - Timestamp matches the very first POST to the NetSupport gateway (`38.146.28.242:1203`), confirming this software identification corresponds to the same connection used for gateway check-ins.
3. The literal raw HTTP User-Agent header sent by the NetSupport RAT client on this connection is `NetSupport Manager/1.3`, matching Zeek's classification exactly.

## Evidence

- `event.dataset`: zeek.software
- `source.ip`: 10.8.20.101
- `software.name`: NetSupport Manager
- `software.type`: HTTP::BROWSER
- `@timestamp`: 2025-10-03T09:12:56.271Z (UTC) — same moment as the first NetSupport gateway checkin
- Corroborating context: NetSupport gateway destination `38.146.28.242:1203` (see OFA P2-06 screenshots, same host/session)

## Finding

| Item | Value |
|---|---|
| User-Agent identifying remote-access software | NetSupport Manager/1.3 |

## Answer

```
CTK{NetSupport Manager/1.3}
```

**Status: CONFIRMED CORRECT** — accepted by the challenge platform (solved by team prior to this report being written).

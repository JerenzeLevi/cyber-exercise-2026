# OFA P1-10 — Later TLS C2 Domain

## Objective
Which later TLS server name resolved to 91.212.166.160?

## Investigation

**Tool used:** Security Onion (Hunt interface) — https://seco.cyberex.quest/

**Context:** 91.212.166.160 first appeared during the initial `zeek.conn`/`zeek.ssl` overview for workstation `160.9.3.101` as a repeatedly-contacted host. The corresponding DNS query (`georgej.ru`) was also observed earlier in the investigation (OFA P1-01 groundwork).

**Query:**
```
source.ip:"160.9.3.101" AND destination.ip:"91.212.166.160" AND event.dataset:"zeek.ssl"
```

**Method:**
1. Queried all `zeek.ssl` sessions from the affected workstation to `91.212.166.160`.
2. Found 9 separate TLSv1.3 sessions between **05:04:35.412** and **05:05:06.643 -04:00** (09:04:35 – 09:05:06 UTC), all carrying `ssl.server_name: georgej.ru`.
3. This matches the `georgej.ru` A-record DNS queries observed for this workstation earlier in the timeline (destination resolver 160.9.3.1), confirming `georgej.ru` resolves to `91.212.166.160` and is contacted repeatedly — consistent with periodic C2 beaconing later in the Phase 1 timeline, after the initial verification/script-delivery chain (sepco.com → louglas.com → 85.209.129.105 → trycloudflare.com).

## Evidence

- `event.dataset`: zeek.ssl
- `log.id.uid`: Cayp7x1osJH5m9henj (first of 9 sessions)
- `source.ip`: 160.9.3.101
- `destination.ip`: 91.212.166.160
- `destination.port`: 443
- `ssl.server_name`: georgej.ru
- `ssl.version`: TLSv1.3
- `@timestamp`: 2025-10-01T09:04:35.412Z (first occurrence)

## Finding

| Item | Value |
|---|---|
| Later TLS Server Name | georgej.ru |
| IPv4 Address | 91.212.166.160 |

## Answer

```
CTK{georgej.ru}
```

**Status: CONFIRMED CORRECT** — accepted by the challenge platform.

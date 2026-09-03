# OFA P4-06 — TCP 2222 Connection Count

## Objective
Quantify the exact number of distinct outbound TCP connection streams established to the C2 server `86.159.48.25:2222`.

## Investigation

**Tool used:** Security Onion Hunt — Zeek connection logs.

**Query:**
```
destination.ip:"86.159.48.25" AND destination.port:2222 | groupby event.dataset network.transport
```

**Method:**
1. Aggregated all connection streams to `86.159.48.25:2222` in the `zeek.conn` dataset.
2. The aggregation confirmed exactly 41 distinct TCP connection sessions.
3. Each individual connection was mirrored by a corresponding Suricata NIDS alert (41 total alerts) for Dridex JA3 hash beaconing, corroborating the connection count independently.

## Evidence

- `zeek.conn` aggregation: 41 distinct TCP sessions to `86.159.48.25:2222`
- Suricata: 41 matching Dridex JA3 beaconing alerts (1:1 correlation)

## Finding

| Item | Value |
|---|---|
| Distinct TCP/2222 connections | 41 |

## Answer

```
CTK{41}
```

**Status: CONFIRMED CORRECT** — accepted by the challenge platform (997 pts).

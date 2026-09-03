# OFA P4-01 — Compromised Workstation

## Objective
Definitively identify the primary compromised workstation acting as the threat actor's operational beachhead in Phase 4 ("Interactive Control and Long-Lived External Sessions").

## Investigation

**Tool used:** Security Onion — Suricata NIDS alerts, Zeek connection records (`zeek.conn`), Active Directory NTLM/SMB authentication telemetry.

**Method:**
1. Correlated Suricata alerts, Zeek connection metadata, and NTLM/SMB authentication logs across the Phase 4 import (incident date 2025-10-08).
2. Identified internal IPv4 `10.11.28.101` as the origin of multiple severe malware signatures: Dridex C2 beaconing on TCP/2222 (`ET JA3 Hash - [Abuse.ch] Possible Dridex`) and W32.DarkVNC BackConnect remote control on port 443 (`ET MALWARE W32.DarkVNC Variant Checkin`).
3. Confirmed `10.11.28.101` established over 78 external interactive sessions across three distinct external C2 servers (`86.159.48.25`, `78.31.67.7`, `108.177.235.29`), and is a domain member of `mytallbeer.com` (OFA.LOCAL) communicating with Domain Controller `10.11.28.2`.

## Evidence

- Suricata: Dridex JA3 beaconing (port 2222) and DarkVNC BackConnect (port 443), both from `10.11.28.101`.
- 78+ external interactive sessions across 3 distinct C2 IPs.
- Domain-member authentication traffic to DC `10.11.28.2`.

## Finding

| Item | Value |
|---|---|
| Compromised workstation | 10.11.28.101 |

## Answer

```
CTK{10.11.28.101}
```

**Status: CONFIRMED CORRECT** — accepted by the challenge platform.

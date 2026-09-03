# OFA P2-01 — Affected Workstation and Internal DNS Resolver

## Objective
Identify the workstation compromised during Phase 2 and the internal DNS resolver it used.

## Investigation

**Tool used:** Security Onion (Hunt / Alerts interface)

**Method:**
1. Reviewed Security Onion Alerts for the Phase 2 import batch (incident date 2025-10-03) and found 59 alert events spanning NetSupport RAT, StealC infostealer, and exploit-kit detections, all sourced from a single internal host.
2. Queried `event.dataset:"zeek.dns" AND destination.port:53`, grouped by `source.ip`, to confirm which host's DNS traffic correlated with the alerting activity.
3. Confirmed 100% of the host's outbound DNS lookups (13 query groups) were handled exclusively by one internal resolver.

## Evidence

- Suricata alerts: 59 events across NetSupport RAT, StealC, and exploit-kit (ZPHP) detections, all from `10.8.20.101`.
- Zeek DNS: all 13 DNS query groups from `10.8.20.101` routed to resolver `10.8.20.1`.
- Zeek logs used: `zeek.dns`, `zeek.conn`, `zeek.http`; Suricata `alert` events.

## Finding

| Item | Value |
|---|---|
| Affected Workstation IPv4 | 10.8.20.101 |
| Internal DNS Resolver IPv4 | 10.8.20.1 |

## Answer

```
CTK{10.8.20.101|10.8.20.1}
```

**Status: CONFIRMED CORRECT** — accepted by the challenge platform.

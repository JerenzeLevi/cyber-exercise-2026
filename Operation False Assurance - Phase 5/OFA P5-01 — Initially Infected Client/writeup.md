# OFA P5-01 — Initially Infected Client

## Objective
Identify the initially infected client IPv4 address and hostname.

**Hint given:** Use DHCP and connection metadata.

## Investigation

**Tool used:** Security Onion Hunt — Zeek DHCP and connection logs.

**Method:**
Correlated DHCP lease/hostname metadata with the earliest malicious connection activity in the Phase 5 import (incident date 2025-10-11). Identified client `192.168.200.95` with DHCP-registered hostname `Linwood-Win-PC` as the first host in the AD segment to exhibit malicious document/payload activity.

## Evidence

- Zeek DHCP: hostname `Linwood-Win-PC` bound to `192.168.200.95`
- Earliest malicious HTTP activity (document delivery) originates from this host

## Finding

| Item | Value |
|---|---|
| Initially infected client IP | 192.168.200.95 |
| Hostname | Linwood-Win-PC |

## Answer

```
CTK{192.168.200.95|Linwood-Win-PC}
```

**Status: ACCEPTED** — confirmed by the challenge platform.

# OFA P4-05 — External TCP 2222 Destination

## Objective
Identify the external IP address contacted by the compromised workstation over non-standard port TCP/2222.

## Investigation

**Tool used:** Security Onion Hunt — Zeek connection/SSL logs, Suricata alerts.

**Method:**
1. Searched for anomalous outbound traffic to destination port 2222/TCP and found 124 persistent, recurring connection streams originating from `10.11.28.101`.
2. All streams targeted the same external IP address.
3. Suricata alert inspection confirmed the `ET JA3 Hash - [Abuse.ch] Possible Dridex` signature, with beaconing recurring at consistent ~3-minute intervals — Zeek SSL/connection logs confirmed this as an interactive, encrypted C2 session.

## Evidence

- 124 recurring connection streams to a single external IP on TCP/2222
- Suricata: `ET JA3 Hash - [Abuse.ch] Possible Dridex`
- ~3-minute periodic beaconing cadence

## Finding

| Item | Value |
|---|---|
| External TCP/2222 destination IP | 86.159.48.25 |

## Answer

```
CTK{86.159.48.25}
```

**Status: CONFIRMED CORRECT** — accepted by the challenge platform (997 pts).

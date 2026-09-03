# OFA P4-04 — Suspicious Domain Resolution

## Objective
Identify the suspicious domain resolving to a C2 destination contacted by the compromised workstation.

## Investigation

**Tool used:** Security Onion — Zeek SSL/TLS handshake metadata (`zeek.ssl`), DNS resolution logs.

**Method:**
1. Analyzed outbound C2 channels from `10.11.28.101`, identifying recurring encrypted communication to external IP `108.177.235.29` over TCP/443.
2. Extracted the TLS Server Name Indication (SNI) and matching DNS resolution record for that IP.
3. Correlated with Suricata NIDS telemetry linking the traffic to known banking-trojan/modular-loader C2 signatures (Dridex/Qbot family).

## Evidence

- Destination IP `108.177.235.29` resolves from SNI/DNS to domain `jesofidiwi.com`
- Suricata: banking trojan/loader C2 signature correlation

## Finding

| Item | Value |
|---|---|
| Suspicious domain | jesofidiwi.com |

## Answer

```
CTK{jesofidiwi.com}
```

**Status: CONFIRMED CORRECT** — accepted by the challenge platform (997 pts).

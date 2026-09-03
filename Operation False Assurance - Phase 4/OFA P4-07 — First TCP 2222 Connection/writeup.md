# OFA P4-07 — First TCP 2222 Connection

## Objective
Determine the UTC timestamp of the first TCP/2222 connection between the compromised workstation and its C2 server.

## Investigation

**Tool used:** Security Onion — Zeek connection telemetry (`zeek.conn`), Suricata NIDS alerts.

**Method:**
1. Correlated `zeek.conn` records and Suricata alerts for outbound TCP/2222 traffic from `10.11.28.101` to `86.159.48.25`.
2. Sorted matching connection records ascending by timestamp to isolate the first occurrence.
3. Confirmed the first TCP/2222 connection commenced at `2025-10-08 09:01:59.259 UTC`, formatted to seconds precision as `2025-10-08 09:01:59 UTC`.
4. The session encapsulated an encrypted TLSv1.2 channel with a JA3 client fingerprint matched to the Dridex banking-trojan/modular C2 loader family.

## Evidence

- First `zeek.conn` record to `86.159.48.25:2222`: `2025-10-08 09:01:59.259 UTC`
- TLSv1.2, JA3 fingerprint matched to Dridex (`ET JA3 Hash - [Abuse.ch] Possible Dridex`)

## Finding

| Item | Value |
|---|---|
| First TCP/2222 connection (UTC) | 2025-10-08 09:01:59 UTC |

## Answer

```
CTK{2025-10-08 09:01:59 UTC}
```

**Status: CONFIRMED CORRECT** — accepted by the challenge platform.

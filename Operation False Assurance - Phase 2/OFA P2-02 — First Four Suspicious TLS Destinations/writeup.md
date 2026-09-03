# OFA P2-02 — First Four Suspicious TLS Destinations

## Objective
Identify, in order of first contact, the first four suspicious TLS destinations (domain + IP pairs) reached by the infected workstation `10.8.20.101`.

## Investigation

**Tool used:** Security Onion (Hunt interface) — Zeek DNS and SSL/TLS logs.

**Method:**
1. Queried Zeek DNS and SSL logs for `10.8.20.101`, sorted ascending by `@timestamp`, to identify the sequence of external HTTPS (TCP/443) connections made shortly after the incident window opened (~09:00 UTC on 2025-10-03).
2. Cross-referenced each TLS SNI/Host value against its resolved IP in the corresponding DNS answer to build ordered domain→IP pairs.
3. Identified four suspicious domains contacted in sequence before the NetSupport RAT gateway (`westford-systems.icu`) and NetSupport's own location-service host (`geo.netsupportsoftware.com`) appeared later in the timeline.

## Evidence

- `dieselfilters.com` → `209.59.180.92`
- `islonline.org` → `23.23.49.179` (triggered a Suricata "ET EXPLOIT_KIT ZPHP Domain in DNS Lookup" alert)
- `woop-bicks.com` → `172.86.90.13`
- `cf-2-up.com` → `45.61.150.28`

These four connections occurred at approximately 09:00 UTC, ahead of the NetSupport RAT beacon session (~09:49–09:58 UTC) and the StealC exfiltration POSTs (~10:02:45–10:02:46 UTC), consistent with an initial malware delivery/check-in stage.

## Finding

| Order | Domain | IP |
|---|---|---|
| 1 | dieselfilters.com | 209.59.180.92 |
| 2 | islonline.org | 23.23.49.179 |
| 3 | woop-bicks.com | 172.86.90.13 |
| 4 | cf-2-up.com | 45.61.150.28 |

## Answer

```
CTK{dieselfilters.com|209.59.180.92|islonline.org|23.23.49.179|woop-bicks.com|172.86.90.13|cf-2-up.com|45.61.150.28}
```

**Status: CONFIRMED CORRECT** — accepted by the challenge platform.

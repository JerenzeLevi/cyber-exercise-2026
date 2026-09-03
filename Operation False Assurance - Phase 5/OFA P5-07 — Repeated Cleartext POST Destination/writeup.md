# OFA P5-07 — Repeated Cleartext POST Destination

## Objective
Which destination IP received repeated cleartext HTTP POSTs on TCP 443, and how many POST transactions were indexed?

**Hint given:** Filter HTTP POSTs to destination.port:443 and count transactions.

## Investigation

**Tool used:** Security Onion Hunt — Zeek HTTP/connection logs, Suricata alerts.

**Method:**
Identified destination `74.195.13.150` receiving repeated cleartext (unencrypted) HTTP POST requests despite the connections using TCP/443. Three interpretations of "transactions indexed" were tested in order:
1. Raw `zeek.http` POST log entries: **32** (corroborated independently by a Suricata alert-rule count of exactly 32) — **rejected**.
2. Unique TCP connections that carried at least one POST, via `network.community_id` grouping: **20** — **rejected**.
3. Total `zeek.conn` records to `74.195.13.150:443` regardless of whether each carried a POST: **26** — **ACCEPTED**.

**Key lesson:** "Transactions indexed" can mean total TCP connections to the destination, not the application-layer transaction count. Interpretation: 20 of the 26 total connections carried the 32 cleartext POSTs; the other 6 connected but did not POST.

## Evidence

- Destination IP: `74.195.13.150`
- 32 raw POST log entries (rejected count)
- 20 unique connections carrying POSTs (rejected count)
- 26 total `zeek.conn` records to destination:443 (accepted count)

## Finding

| Item | Value |
|---|---|
| Destination IP | 74.195.13.150 |
| Transaction count (accepted) | 26 |

## Answer

```
CTK{74.195.13.150|26}
```

**Status: ACCEPTED** — confirmed by the challenge platform.

**Lesson learned:** For "how many X were indexed/transactions" style counts, test multiple granularities (raw log-entry count, activity-matching connection count, AND total connection count to the destination/port) before assuming the destination or scope is wrong.

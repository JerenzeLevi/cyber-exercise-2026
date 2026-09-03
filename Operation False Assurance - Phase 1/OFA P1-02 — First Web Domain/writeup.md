# OFA P1-02 — First Web Domain

## Objective
What was the first web domain queried by the workstation, and what IPv4 address was returned?

## Investigation

**Tool used:** Security Onion (Hunt / Dashboards interface) — https://seco.cyberex.quest/

**Note:** This finding depends on the affected workstation identified in OFA P1-01: `160.9.3.101` (DNS resolver `160.9.3.1`, import batch `495ee14fa7e950512fce637bcc361290`, dated 2025-10-01). See that writeup for how the correct host/import was identified among the 11 evidence batches present in this Security Onion instance.

**Query:**
```
source.ip:"160.9.3.101"
```
Sorted by Timestamp ascending (per hint: "Use DNS metadata and sort by time ascending").

**Method:**
1. Sorted all events for `160.9.3.101` (all datasets, not just DNS) ascending by timestamp.
2. The very first record in the entire evidence set for this host is a `zeek.dns` query at exactly **2025-10-01 09:00:00.000 UTC** (05:00:00.000 -04:00) — the deliberate start-of-capture marker.
3. Expanded the record for full DNS answer details.

## Evidence

- `event.dataset`: zeek.dns
- `log.id.uid`: CuhnDu3ogRkMIJxGHh
- `dns.query.name`: www.sepco.com
- `dns.highest_registered_domain`: sepco.com
- `dns.subdomain`: www
- `dns.query.type_name`: A
- `dns.response.code_name`: NOERROR
- `dns.answers.name` / `dns.resolved_ip`: ["148.72.11.102"] (single answer, no ambiguity)
- `source.ip`: 160.9.3.101 → `destination.ip`: 160.9.3.1 (resolver)
- `@timestamp`: 2025-10-01T09:00:00.000Z

## Analysis

Immediately following this DNS resolution, `160.9.3.101` established an HTTPS session to `148.72.11.102` (matches the "unusual verification page" the employee encountered per the scenario). Approximately 47 seconds later the same host began repeated HTTP GET/POST traffic to `85.209.129.105:2020` — including one ~26 MB response — followed by a POST to a Cloudflare Tunnel hostname (`maintaining-shelter-bailey-ordinance.trycloudflare.com`). This sequence (verification page → script/payload delivery via a disposable tunnel) directly matches the Phase 1 title, "Fraudulent Verification and Script Delivery."

## Finding

| Item | Value |
|---|---|
| First Web Domain Queried | www.sepco.com |
| Returned IPv4 Address | 148.72.11.102 (single A record, unambiguous) |

## Answer

```
CTK{www.sepco.com|148.72.11.102}
```

**Status: CONFIRMED CORRECT** — accepted by the challenge platform.

# OFA P1-01 — Affected Workstation and DNS Resolver

## Objective
Identify the affected workstation IPv4 address and the DNS resolver it used.

## Investigation

**Tool used:** Security Onion (Hunt / Dashboards interface) — https://seco.cyberex.quest/

**Key correction:** An initial pass identified host `10.8.29.128` (import batch `9a18be5326e6b3fee0c6028ca1853eab`, dated 2024-08-29) as the affected workstation. That flag was rejected. Re-examination showed this Security Onion instance holds **11 separate imported evidence batches** (`import.id`), most of which are unrelated demo/sample captures dated 2024 with no connection to the scenario. The correct Phase 1 evidence is import batch `495ee14fa7e950512fce637bcc361290`, the only one dated **2025-10-01**, matching the scenario's stated October 2025 timeframe (RULES.txt). It is also the earliest of five sequential October-2025-dated imports (Oct 1, 3, 5, 8, 11) representing the six stages of the intrusion referenced in the scenario, followed by a sixth stage (EternalBlue/DoublePulsar lateral movement, Oct 14, subnet 192.168.116.0/24).

**Query:**
```
event.dataset:"zeek.dns" AND destination.port:53 | groupby source.ip
```
Time range: Last 24 months.

**Method:**
1. Enumerated all hosts issuing real (unicast, port 53) DNS queries across every import batch, filtering out LLMNR/NBNS/mDNS broadcast noise (ports 137/5355).
2. Checked each candidate host's earliest timestamp and `import.id` to separate genuine scenario evidence from unrelated bundled sample data. Hosts dated 2024 (10.8.29.128, 172.17.0.99, 10.9.11.102, 10.9.16.101, 10.10.15.101) were ruled out as unrelated demo captures.
3. Of the October 2025-dated hosts, `160.9.3.101` has the earliest activity: its evidence window begins at exactly **2025-10-01 09:00:00.000 UTC** (05:00:00.000 -04:00) — a clean capture-start marker — with the very first logged event being a DNS query to `160.9.3.1`.
4. Confirmed resolver consistency: 51 of 53 real DNS queries from `160.9.3.101` went to `160.9.3.1` (the other 2 are mDNS multicast, irrelevant).
5. Confirmed this workstation's activity narrative fits the Phase 1 title ("Fraudulent Verification and Script Delivery"): first DNS query resolves a lure domain, followed immediately by an HTTPS session, then within ~47 seconds by repeated HTTP GET/POST to a non-standard port including a ~26 MB payload transfer, and a POST to a `trycloudflare.com` tunnel endpoint (see OFA P1-02 writeup for full detail).

## Evidence

- `event.dataset`: zeek.dns
- `observer.name`: cyberseco
- `import.id`: 495ee14fa7e950512fce637bcc361290
- `import.file`: dns.log
- `log.id.uid`: CuhnDu3ogRkMIJxGHh
- `source.ip`: 160.9.3.101
- `source.port`: 52322
- `destination.ip` (resolver): 160.9.3.1
- `destination.port`: 53
- `network.transport`: udp
- `@timestamp`: 2025-10-01T09:00:00.000Z

## Finding

| Item | Value |
|---|---|
| Affected Workstation IPv4 | 160.9.3.101 |
| DNS Resolver IPv4 | 160.9.3.1 |

## Answer

```
CTK{160.9.3.101|160.9.3.1}
```

**Status: CONFIRMED CORRECT** — accepted by the challenge platform.

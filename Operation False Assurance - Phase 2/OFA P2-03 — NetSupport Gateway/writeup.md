# OFA P2-03 — NetSupport Gateway

## Objective
Identify the domain that resolved to the NetSupport Manager RAT gateway, and the gateway's IP address and destination port.

## Investigation

**Tool used:** Security Onion Hunt — Zeek DNS/HTTP logs, Suricata alerts.

**Query:**
```
event.dataset:zeek.dns && dns.resolved_ip:"38.146.28.242"
```

**Method:**
1. At `2025-10-03 09:12:56 UTC`, host `10.8.20.101` issued a DNS A-record query for `westford-systems.icu` to internal resolver `10.8.20.1`, which returned a single answer: `38.146.28.242`.
2. Roughly 37 minutes later (~09:49–09:58 UTC), the same host began exchanging NetSupport Manager RAT beacon traffic (`CMD=POLL` / `CMD=ENCD` to `/fakeurl.htm`) with that exact IP over TCP port **1203**.
3. A reverse query, `dns.query.name:"westford-systems.icu" | groupby dns.resolved_ip`, returned exactly one grouped result (count 1), confirming a clean, exclusive one-to-one domain-to-IP mapping — no other domain resolved to `38.146.28.242` and no other IP was ever returned for `westford-systems.icu`.
4. Suricata confirmed 48/48 "ET REMOTE_ACCESS NetSupport Remote Admin Checkin" alerts from `10.8.20.101` to `38.146.28.242:1203`.

## Evidence

- `dns.query.name`: westford-systems.icu → `dns.resolved_ip`: 38.146.28.242
- Suricata rule: `ET REMOTE_ACCESS NetSupport Remote Admin Checkin` (48 events)
- Destination port: TCP/1203
- Beacon path: `/fakeurl.htm`

## Finding

| Item | Value |
|---|---|
| Gateway domain | westford-systems.icu |
| Gateway IP | 38.146.28.242 |
| Destination port | 1203 |

## Answer

```
CTK{westford-systems.icu|38.146.28.242|1203}
```

**Status: CONFIRMED CORRECT** — accepted by the challenge platform.

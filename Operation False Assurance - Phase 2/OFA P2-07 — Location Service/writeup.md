# OFA P2-07 — Location Service

## Objective
Identify the location-service hostname and URI path contacted by the infected workstation alongside its NetSupport RAT gateway activity.

## Investigation

**Tool used:** Security Onion Hunt — Zeek DNS/HTTP logs.

**Method:**
1. At `09:12:56.132 UTC`, host `10.8.20.101` issued a DNS query for `geo.netsupportsoftware.com` to resolver `10.8.20.1`, receiving three Cloudflare (AS13335) A-records: `104.26.0.231`, `104.26.1.231`, `172.67.68.212`.
2. ~262 ms later, at `09:12:56.394 UTC`, the same host sent an HTTP GET to `104.26.1.231:80` with `Host: geo.netsupportsoftware.com` and URI `/location/loca.asp`, receiving a `200 OK` with a 15-byte response body.
3. This request occurred within the same second as the DNS resolution of the NetSupport RAT gateway domain `westford-systems.icu` (OFA P2-03), indicating both lookups originate from the same NetSupport Manager client startup sequence.
4. The small fixed response and `/location/loca.asp` path are consistent with NetSupport Manager's built-in client-geolocation check-in feature, hosted on the vendor's own Cloudflare-fronted infrastructure — **not** attacker-controlled infrastructure. This request is a benign, corroborating timing indicator, not a C2 channel.

## Evidence

- `dns.query.name`: geo.netsupportsoftware.com → 3 Cloudflare A-records
- `http.virtual_host`: geo.netsupportsoftware.com, `http.uri`: /location/loca.asp
- `http.status_code`: 200, `http.response.body.length`: 15

## Finding

| Item | Value |
|---|---|
| Location-service hostname | geo.netsupportsoftware.com |
| URI path | /location/loca.asp |

## Answer

```
CTK{geo.netsupportsoftware.com|/location/loca.asp}
```

**Status: CONFIRMED CORRECT** — accepted by the challenge platform.

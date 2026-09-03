# OFA P1-08 — Cloudflare Tunnel Transaction

## Objective
Identify the Cloudflare Tunnel hostname, POST URI, and response status code.

## Investigation

**Tool used:** Security Onion (Hunt interface) — https://seco.cyberex.quest/

**Context:** Building on OFA P1-07 — the notification beacon (POST /notify, 200 OK) to 85.209.129.105:2020.

**Query:**
```
source.ip:"160.9.3.101" AND event.dataset:"zeek.http"
```

**Method:**
1. Continuing chronologically through `zeek.http` events for `160.9.3.101`, the next request occurs at **2025-10-01 05:01:15.089 -04:00** (09:01:15.089 UTC), to a different, disposable Cloudflare Tunnel hostname rather than the delivery server directly:
   - `http.method`: POST
   - `http.virtual_host`: `maintaining-shelter-bailey-ordinance.trycloudflare.com`
   - `http.uri`: `/BSVjy5VpVrgO`
   - `http.useragent`: WindowsPowerShell/5.1.26100.4768
   - `http.request.body.length`: 2,788 bytes
   - `http.response.body.length`: 0 bytes
   - `http.status_code`: 404 Not Found
2. The use of a `trycloudflare.com` quick tunnel hostname (auto-generated, random subdomain) indicates the attacker used a disposable Cloudflare Tunnel to relay traffic and obscure their real backend infrastructure. The 404 response suggests either the tunnel endpoint had already been torn down or the specific random URI path was not recognized by the receiving service at the time of the request.

## Evidence

- `event.dataset`: zeek.http
- `log.id.uid`: Cp61j16BYOZNBVlca
- `source.ip`: 160.9.3.101
- `destination.ip`: 104.16.231.132 (Cloudflare anycast)
- `destination.port`: 80
- `http.method`: POST
- `http.virtual_host`: maintaining-shelter-bailey-ordinance.trycloudflare.com
- `http.uri`: /BSVjy5VpVrgO
- `http.status_code`: 404
- `@timestamp`: 2025-10-01T09:01:15.089Z

## Finding

| Item | Value |
|---|---|
| Cloudflare Tunnel Hostname | maintaining-shelter-bailey-ordinance.trycloudflare.com |
| POST URI | /BSVjy5VpVrgO |
| Response Status Code | 404 |

## Answer

```
CTK{maintaining-shelter-bailey-ordinance.trycloudflare.com|/BSVjy5VpVrgO|404}
```

**Status: CONFIRMED CORRECT** — accepted by the challenge platform.

# OFA P1-03 — Next TLS Server Name

## Objective
Which TLS server name appeared immediately after the first website, and what IPv4 address did it use?

## Investigation

**Tool used:** Security Onion (Hunt interface) — https://seco.cyberex.quest/

**Context:** Building on OFA P1-01/P1-02 — affected workstation `160.9.3.101`, first website `www.sepco.com` (148.72.11.102).

**Query:**
```
source.ip:"160.9.3.101" AND event.dataset:"zeek.ssl"
```
Sorted by Timestamp ascending (default hunt order for this host).

**Method:**
1. Pulled all `zeek.ssl` events for the affected workstation, ascending by timestamp.
2. The first six TLS sessions (05:00:00.277 - 05:00:00.571 -04:00) all show `ssl.server_name: www.sepco.com` to `148.72.11.102:443` — these are the multiple parallel connections that make up loading the first website.
3. The next TLS session chronologically, at **05:00:00.993 -04:00** (09:00:00.993 UTC), is to a different server:
   - `ssl.server_name`: `louglas.com`
   - `destination.ip`: `192.153.57.201`
   - `destination.port`: 443
   - `ssl.version`: TLSv1.2
   - `ssl.validation_status`: ok

## Evidence

- `event.dataset`: zeek.ssl
- `log.id.uid`: CPyXoy4rWDbQ1I1fY4
- `source.ip`: 160.9.3.101
- `source.port`: 49881
- `destination.ip`: 192.153.57.201
- `destination.port`: 443
- `ssl.server_name`: louglas.com
- `ssl.version`: TLSv1.2
- `@timestamp`: 2025-10-01T09:00:00.993Z

## Finding

| Item | Value |
|---|---|
| Next TLS Server Name | louglas.com |
| IPv4 Address | 192.153.57.201 |

## Answer

```
CTK{louglas.com|192.153.57.201}
```

**Status: CONFIRMED CORRECT** — accepted by the challenge platform.

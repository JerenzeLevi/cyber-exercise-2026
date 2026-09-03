# OFA P2-08 — Information-Stealer Endpoint

## Objective
Identify the information-stealer's destination IP address and the URI path it POSTs to.

## Investigation

**Tool used:** Security Onion Alerts and Hunt — Suricata alerts, Zeek HTTP/File logs.

**Method:**
1. Queried `rule.name:*StealC*` in Alerts and found high-severity events: **ET MALWARE StealC CnC Activity (POST)** (sid 2066559) and **ET MALWARE StealC_V2 CnC Activity (POST)** (sid 2066280), both tagged `malware_family: Stealc`, from `10.8.20.101` to `79.141.165.202:80`.
2. Pivoted on `destination.ip:"79.141.165.202"`, returning 72 correlated events (`suricata.alert`, `zeek.http`, `zeek.file`).
3. Expanded a `zeek.http` record: `http.method: POST`, `http.uri: /a9b024dccb2b4f24.php`, `Content-Type: application/json`, response `200 OK`.
4. `79.141.165.202` resolves to HZ Hosting Ltd (AS59711), Amsterdam, Netherlands — a hosting provider commonly abused for stealer C2 infrastructure. The Suricata alert and Zeek HTTP/file records share the same `network.community_id` (`1:9l1BjSVXGaDlnEJ+WCYS0zcOplY=`), tying them to the same flow.

## Evidence

- Destination: `79.141.165.202:80`
- URI: `/a9b024dccb2b4f24.php`
- Suricata sids: 2066559, 2066280 (`malware_family: Stealc`)
- First observed: `2025-10-03 10:02:45 UTC`

## Finding

| Item | Value |
|---|---|
| Info-stealer destination IP | 79.141.165.202 |
| POST URI path | /a9b024dccb2b4f24.php |

## Answer

```
CTK{79.141.165.202|/a9b024dccb2b4f24.php}
```

**Status: CONFIRMED CORRECT** — accepted by the challenge platform.

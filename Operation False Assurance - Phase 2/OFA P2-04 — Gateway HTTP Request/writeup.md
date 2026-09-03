# OFA P2-04 — Gateway HTTP Request

## Objective
Identify the HTTP method and request URI repeatedly used by the infected workstation during its NetSupport RAT gateway session with `38.146.28.242:1203`.

## Investigation

**Tool used:** Security Onion Hunt — Zeek HTTP logs.

**Query:**
```
event.dataset:zeek.http && destination.ip:"38.146.28.242"
```

**Method:**
1. The query returned 48 matching HTTP transaction records, all originating from `10.8.20.101:63910` to `38.146.28.242` on TCP/1203.
2. Expanding individual event records showed `http.method = POST` and `http.uri = http://38.146.28.242/fakeurl.htm` on every record; `http.useragent` confirmed the client as `NetSupport Manager/1.3`.
3. Reviewing the events in descending time order showed this exact POST repeating at approximately 60-second intervals (e.g. 09:56:59.230, 09:56:02.679, 09:55:02.491, 09:54:02.408 UTC), consistent with a periodic RAT check-in beacon.
4. All 48 records shared identical method, URI, destination IP, and destination port — confirming a single, static, repeated HTTP request pattern with no variation.

## Evidence

- `http.method`: POST
- `http.uri`: http://38.146.28.242/fakeurl.htm
- `http.useragent`: NetSupport Manager/1.3
- 48/48 events identical; ~60-second beacon cadence

## Finding

| Item | Value |
|---|---|
| HTTP Method | POST |
| Request URI | http://38.146.28.242/fakeurl.htm |

## Answer

```
CTK{POST|http://38.146.28.242/fakeurl.htm}
```

**Status: CONFIRMED CORRECT** — accepted by the challenge platform.

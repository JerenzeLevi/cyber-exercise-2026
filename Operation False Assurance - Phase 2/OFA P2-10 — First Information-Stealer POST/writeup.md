# OFA P2-10 — First Information-Stealer POST

## Objective
At what UTC time was the first information-stealer POST observed?

**Hint given:** Sort matching HTTP events by `@timestamp` ascending.

## Investigation

**Tool used:** Security Onion Hunt — Zeek HTTP logs.

**Query:**
```
event.dataset:zeek.http AND destination.ip:"79.141.165.202" AND http.method:"POST"
```
Sorted ascending by `@timestamp`.

**Method:**
1. Filtered all `zeek.http` POST transactions to the StealC endpoint `79.141.165.202` (identified in OFA P2-08).
2. Sorted ascending by timestamp and took the first record.
3. First matching event: `@timestamp: 2025-10-03T06:02:45.033-04:00`, which converts to `2025-10-03 10:02:45 UTC`.
4. Re-verified live against Security Onion before final submission to confirm no earlier POST existed to this destination.

## Evidence

- First `zeek.http` POST to 79.141.165.202
- `@timestamp`: 2025-10-03T06:02:45.033-04:00 (America/New_York, UTC-4) = `2025-10-03 10:02:45 UTC`
- Corroborated by Suricata: 3 back-to-back StealC CnC POST alerts at 10:02:45–10:02:46 UTC (see OFA P2-08)

## Finding

| Item | Value |
|---|---|
| First information-stealer POST (UTC) | 2025-10-03 10:02:45 UTC |

## Answer

```
CTK{2025-10-03 10:02:45 UTC}
```

**Status: CONFIRMED CORRECT** — accepted by the challenge platform.

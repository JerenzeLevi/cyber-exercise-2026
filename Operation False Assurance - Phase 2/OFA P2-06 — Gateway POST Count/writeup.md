# OFA P2-06 — Gateway POST Count

## Objective
How many POST transactions to the NetSupport gateway (`38.146.28.242:1203`) are indexed?

## Investigation

**Tool used:** Security Onion Hunt — Zeek HTTP logs, Suricata alerts.

**Method:**
Multiple independent granularities were tested and cross-checked:
1. Raw `zeek.http` POST log entries to `38.146.28.242`: **48**.
2. Suricata "ET REMOTE_ACCESS NetSupport Remote Admin Checkin" alert count: **48** (matches #1).
3. HTTP method breakdown (`groupby http.method`) confirmed all 48 events were POST.
4. Cross-host/time-range verification reproduced 48 consistently.
5. Applying the Phase 5 lesson that "transactions indexed" can mean **distinct TCP connections** rather than raw log-entry count: all 48 POSTs ride a single persistent TCP connection (`zeek.conn` count = 1, `network.community_id` grouping = 1), suggesting a possible alternate answer of `CTK{1}` — **this was never submitted**, documented here only as an untested lead.

## Evidence

- 48 `zeek.http` POST records to `38.146.28.242:1203`, all with identical method/URI (`POST /fakeurl.htm`).
- 48 Suricata "NetSupport Remote Admin Checkin" alerts (independent corroboration).
- All 48 requests ride a single `zeek.conn` record / community_id (1 persistent connection).

## Attempts Submitted (all rejected)

`CTK{48}`, `CTK{048}`, `CTK{3}`, `CTK{49}`, `CTK{96}`, `CTK{149}`

## Status

**CLOSED — unresolved, per explicit instruction to stop pursuing this challenge.** The literal event count (48) is verified four independent ways and matches the challenge hint exactly, yet was rejected by the platform on every attempt. No Kibana credentials were available to independently cross-check the platform's expected answer. The connection-count interpretation (`CTK{1}`) remains an untested, plausible alternate answer if this challenge is ever revisited.

# OFA P5-10 — PNG-Named Objects

## Objective
Which three PNG-named objects were requested by the domain controller after compromise?

## Investigation

**Tool used:** Security Onion Hunt — Zeek HTTP logs.

**Method:**
1. Filtered HTTP GET/POST requests from the compromised Domain Controller (`192.168.200.4`) for objects with `.png` filenames, following its first C2 callback (OFA P5-09).
2. Identified three distinct PNG-named objects: `table.png`, `worming.png`, `toler.png`.
3. **Key lesson — alphabetical order, not chronological.** Chronological first-seen order (`table.png, worming.png, toler.png`) was tried twice and rejected. Switching to plain alphabetical order (`table.png, toler.png, worming.png`) fixed it immediately.

## Evidence

- Three PNG-named objects requested by the DC: `table.png`, `toler.png`, `worming.png`
- Zeek HTTP records for each filename, source `192.168.200.4`

## Finding

| Item | Value |
|---|---|
| PNG-named objects (alphabetical) | table.png, toler.png, worming.png |

## Answer

```
CTK{table.png|toler.png|worming.png}
```

**Status: ACCEPTED** — confirmed by the challenge platform.

**Lesson learned:** When a challenge lists multiple filenames/objects with no explicit ordering instruction, try alphabetical order before chronological (first-seen) order.

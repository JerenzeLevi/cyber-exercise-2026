# OFA P3-02 — Unusual DNS Query

## Objective
What unusual DNS name was queried at the start of the capture?

**Hint given:** Inspect the earliest DNS queries from `10.9.24.101`.

## Investigation

**Tool used:** Security Onion Hunt — Zeek DNS logs.

**Method:**
Inspected the earliest `zeek.dns` records from host `10.9.24.101`, sorted ascending by `@timestamp`. Two candidate unusual DNS names surfaced:
1. A long, non-dictionary, DGA-style subdomain: `xsppqsedvcfymaswjihwraid` (tried standalone, with a repeated-label form `xsppqsedvcfymaswjihwraid.xsppqsedvcfymaswjihwraid`, and with a trailing dot).
2. A short, plausible C2-style domain: `fixatmu.pics`.

## Attempts Submitted (all rejected)

- `CTK{xsppqsedvcfymaswjihwraid}`
- `CTK{xsppqsedvcfymaswjihwraid.xsppqsedvcfymaswjihwraid}`
- `CTK{xsppqsedvcfymaswjihwraid.xsppqsedvcfymaswjihwraid.}`
- `CTK{fixatmu.pics}`

## Status

**UNRESOLVED.** Multiple plausible candidates for "the earliest unusual DNS query" from `10.9.24.101` have all been rejected. Next steps if revisited: re-verify the actual earliest-by-timestamp record (not just the most visually unusual one), check for a different source host filter, and consider whether the expected answer is a full FQDN with a specific TLD/casing not yet tried.

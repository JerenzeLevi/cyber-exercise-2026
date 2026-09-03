# OFA P4-02 — Active Directory Domain

## Objective
Identify the enterprise Active Directory domain infrastructure the compromised workstation belongs to.

## Investigation

**Tool used:** Security Onion — Zeek NTLM protocol logs (`zeek.ntlm`).

**Method:**
1. Examined Zeek NTLM negotiation telemetry for direct internal authentication traffic from compromised workstation `10.11.28.101` to Domain Controller `10.11.28.2` (`WIN-FGG5B8C1BYF`).
2. NTLM authentication metadata exposed the fully qualified Active Directory domain name.
3. Confirmed at `2025-10-05 08:00:00 UTC`: SMB/NTLMv2 authentication negotiation from `10.11.28.101:49794` to `10.11.28.2:139`, with challenge-response completing and revealing the domain.

## Evidence

- `zeek.ntlm` NTLM challenge-response exposing FQDN `WIN-FGG5B8C1BYF.mytallbeer.com`
- SMB/NetBIOS-SSN negotiation, source `10.11.28.101`, destination DC `10.11.28.2`

## Finding

| Item | Value |
|---|---|
| Active Directory domain | mytallbeer.com |

## Answer

```
CTK{mytallbeer.com}
```

**Status: CONFIRMED CORRECT** — accepted by the challenge platform (997 pts).

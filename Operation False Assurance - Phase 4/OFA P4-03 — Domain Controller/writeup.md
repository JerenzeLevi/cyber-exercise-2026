# OFA P4-03 — Domain Controller

## Objective
Identify the internal IP address and hostname of the Domain Controller targeted by the compromised workstation.

## Investigation

**Tool used:** Security Onion — Zeek NTLM authentication logs (`zeek.ntlm`), DNS SRV records (`zeek.dns`).

**Method:**
1. Investigated NTLM authentication streams and DNS SRV resource records from workstation `10.11.28.101` (PCAP import `9159a1b68fa050d28393c1863352b9d1`).
2. At `2025-10-08 09:00:05 UTC`, an NTLM handshake between `10.11.28.101` and `10.11.28.2` exposed the server's NetBIOS name `WIN-FGG5B8C1BYF` and domain tree `mytallbeer.com`.
3. Confirmed the same host `10.11.28.2` handling core domain services: DNS (53), Kerberos (88), NTLM/NetBIOS (139), LDAP (389), and SMB (445) for the `mytallbeer.com` forest — the profile of an authoritative Domain Controller.

## Evidence

- NTLM handshake exposing NetBIOS name `WIN-FGG5B8C1BYF`, FQDN `WIN-FGG5B8C1BYF.mytallbeer.com`
- Full domain-service port footprint (53/88/139/389/445) hosted on `10.11.28.2`

## Finding

| Item | Value |
|---|---|
| Domain Controller IP | 10.11.28.2 |
| Domain Controller hostname | WIN-FGG5B8C1BYF |

## Answer

```
CTK{10.11.28.2|WIN-FGG5B8C1BYF}
```

**Status: CONFIRMED CORRECT** — accepted by the challenge platform (997 pts).

# OFA P5-02 — AD Domain and Domain Controller

## Objective
Identify the Active Directory domain, and the domain controller hostname and IPv4 address.

## Investigation

**Tool used:** Security Onion Hunt — Zeek NTLM/Kerberos authentication logs.

**Method:**
Examined authentication traffic between client `192.168.200.95` and the internal AD infrastructure. Identified Domain Controller `192.168.200.4` (`OYSTER-DC`) servicing the `oystertainment.com` domain.

**Key correction:** The Kerberos SPN traffic showed mixed-case domain casing, but the authoritative NTLM field returned the domain in lowercase (`oystertainment.com`) — the lowercase form was the accepted answer, not the mixed-case Kerberos SPN casing.

## Evidence

- NTLM authoritative field: domain = `oystertainment.com` (lowercase)
- DC hostname: `OYSTER-DC`
- DC IP: `192.168.200.4`

## Finding

| Item | Value |
|---|---|
| AD domain | oystertainment.com |
| DC hostname | OYSTER-DC |
| DC IP | 192.168.200.4 |

## Answer

```
CTK{oystertainment.com|OYSTER-DC|192.168.200.4}
```

**Status: ACCEPTED** — confirmed by the challenge platform.

**Lesson learned:** When domain casing differs between NTLM and Kerberos SPN fields, use the NTLM-authoritative casing.

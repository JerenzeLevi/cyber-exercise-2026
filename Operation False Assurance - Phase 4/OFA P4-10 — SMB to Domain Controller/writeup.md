# OFA P4-10 — SMB to Domain Controller

## Objective
Identify the internal server receiving SMB (TCP/445) connections from the compromised workstation, the destination port/protocol, and the UTC time of the first such connection.

## Investigation

**Tool used:** Security Onion — Zeek `smb_mapping.log`, connection logs, DCE-RPC telemetry.

**Method:**
1. Identified compromised workstation `10.11.28.101` establishing repeated authenticated SMB sessions (TCP/445) to internal server `10.11.28.2`, identified via `smb_mapping.log` as `WIN-FGG5B8C1BYF.mytallbeer.com` — the Domain Controller for the `mytallbeer.com` AD domain.
2. Confirmed 7 SMB/445 connections between `09:12:36 UTC` and `10:27:36 UTC` (2025-10-08), with an earlier related TCP/139 session logged at `09:00:05 UTC`. Six sessions mapped the IPC$ administrative pipe; one mapped the SYSVOL share.
3. The same host pair also exchanged DNS, LDAP, Kerberos, and DCE-RPC (epmapper, netlogon, lsarpc, and 80 `drsuapi` calls including DRSBind/DRSCrackNames/DRSUnbind) traffic in the surrounding window — consistent with AD reconnaissance/enumeration tooling (e.g. BloodHound-style collectors) rather than routine file access.
4. No `IDL_DRSGetNCChanges` call (the operation used for DCSync-style credential replication) was found in the reviewed DCE-RPC data, so full replication/hash-dump activity is **not confirmed** from this evidence alone.

## Evidence

- 7 SMB/445 sessions, `10.11.28.101` → `10.11.28.2`, first at `2025-10-08 09:12:36 UTC`
- IPC$ (PIPE) mapped x6, SYSVOL (DISK) mapped x1
- Destination identity: `WIN-FGG5B8C1BYF.mytallbeer.com` (Domain Controller, `mytallbeer.com`)
- Supporting DCE-RPC enumeration traffic (epmapper, netlogon, lsarpc, 80 drsuapi calls)

## Finding

| Item | Value |
|---|---|
| SMB destination server | 10.11.28.2 |
| Port / protocol | 445/TCP |
| First SMB/445 connection (UTC) | 2025-10-08 09:12:36 UTC |

## Answer

```
CTK{10.11.28.2|445|2025-10-08 09:12:36 UTC}
```

**Status: CONFIRMED CORRECT** — accepted by the challenge platform.

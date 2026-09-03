# OFA P5-11 — Client-to-DC SMB Communication

## Objective
Which client and server IP addresses communicated over SMB/TCP 445 during this phase?

## Investigation

**Tool used:** Security Onion Hunt — Zeek connection/SMB logs.

**Method:**
Filtered `zeek.conn`/`zeek.smb` traffic on destination port 445, identifying the initially infected client (`192.168.200.95`, OFA P5-01) communicating directly with the Domain Controller (`192.168.200.4`, OFA P5-02) over SMB — consistent with lateral movement / internal reconnaissance following the client's initial compromise.

## Evidence

- SMB (TCP/445) sessions: `192.168.200.95` ↔ `192.168.200.4`

## Finding

| Item | Value |
|---|---|
| Client IP | 192.168.200.95 |
| Server IP | 192.168.200.4 |
| Port | 445 |

## Answer

```
CTK{192.168.200.95|192.168.200.4|445}
```

**Status: ACCEPTED** — confirmed by the challenge platform.

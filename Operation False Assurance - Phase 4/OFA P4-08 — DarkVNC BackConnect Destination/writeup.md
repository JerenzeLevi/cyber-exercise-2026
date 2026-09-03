# OFA P4-08 — DarkVNC BackConnect Destination

## Objective
Identify the external IP address receiving the interactive reverse-VNC (DarkVNC/BackConnect) session near the end of the capture window.

## Investigation

**Tool used:** Security Onion Hunt — Zeek connection telemetry, Suricata NIDS alerts.

**Method:**
1. Investigated anomalous high-volume outbound traffic on destination port TCP/443 from `10.11.28.101` near the end of the packet capture window.
2. Aggregated `destination.port:443` traffic and found external IP `78.31.67.7` receiving sustained, high-throughput interactive streams between `10:24:35 UTC` and `10:42:00 UTC`.
3. Suricata NIDS alerts confirmed this was not standard HTTPS browsing but an active reverse interactive screen-sharing session: `ET MALWARE W32.DarkVNC Variant Checkin` and `ET MALWARE BackConnect CnC Activity`.
4. This represents the adversary upgrading their interactive foothold to a full GUI-based remote administrative session via reverse VNC tunneled over port 443.

## Evidence

- Sustained high-throughput streams `10.11.28.101` → `78.31.67.7:443`, `10:24:35`–`10:42:00 UTC`
- Suricata: `ET MALWARE W32.DarkVNC Variant Checkin`, `ET MALWARE BackConnect CnC Activity`
- Zeek flow initialization: `2025-10-08 10:24:35.468 UTC`, `10.11.28.101:50001` → `78.31.67.7:443`

## Finding

| Item | Value |
|---|---|
| DarkVNC/BackConnect destination IP | 78.31.67.7 |

## Answer

```
CTK{78.31.67.7}
```

**Status: CONFIRMED CORRECT** — accepted by the challenge platform.

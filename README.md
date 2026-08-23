<div align="center">

# 🛡️ Operation False Assurance
### Cyber Exercise — Incident Response & OSINT Investigation

**Sole Author & Contributor:** [JerenzeLevi](https://github.com/JerenzeLevi)

![Status](https://img.shields.io/badge/status-in%20progress-yellow)
![Phases](https://img.shields.io/badge/phases-5-blue)
![Type](https://img.shields.io/badge/type-Incident%20Response%20Exercise-critical)
![License](https://img.shields.io/badge/license-Personal%20Work-lightgrey)

</div>

---

## 📖 Scenario Background

> A regional financial organization reported a series of suspicious network events affecting several systems across its enterprise environment.
>
> The first indication of compromise occurred in **October 2025**, when an employee encountered an unusual verification page while browsing the Internet. What initially appeared to be an isolated web event was followed by increasingly suspicious activity over the next two weeks.
>
> Security monitoring later identified evidence of **unauthorized downloads, external command-and-control communication, credential and information theft, remote access activity, internal network movement, and compromise of critical infrastructure.**
>
> The incident escalated into a **ransomware outbreak** affecting multiple Windows systems.

The Security Operations Center recovered network evidence from **six stages of the intrusion**. This repository documents the reconstruction of that attack — tracing affected systems, malicious infrastructure, attacker progression, and containment/recovery recommendations — across five investigative phases.

---

## 🗂️ Repository Structure

```
CyberExercise/
├── Operation False Assurance - Phase 1/   # Initial compromise & first web-based delivery chain
├── Operation False Assurance - Phase 2/   # C2 infrastructure, remote access tooling, info-stealer activity
├── Operation False Assurance - Phase 3/   # DNS anomalies & executable metadata analysis
├── Operation False Assurance - Phase 4/   # Domain compromise, lateral movement, BackConnect C2
├── Operation False Assurance - Phase 5/   # Full kill-chain reconstruction, client-to-DC SMB activity
├── OSINT/                                  # Open-source intelligence gathering artifacts
└── RULES.txt                               # Exercise rules & engagement scope
```

Each phase folder contains individually numbered challenge sub-folders (e.g. `OFA P1-01 — Affected Workstation and DNS Resolver`) along with supporting evidence, screenshots, and a merged `.docx`/`.pdf` report per phase.

---

## 🔍 Phase Overview

| Phase | Focus | Status |
|:-----:|-------|:------:|
| **1** | Initial infection vector, DNS resolver, TLS delivery infrastructure, PowerShell payload chain | ✅ Reported |
| **2** | NetSupport RAT gateway, remote-access user-agent, information-stealer endpoints | ✅ Reported |
| **3** | Suspicious DNS queries, malicious executable metadata | 🟡 In progress |
| **4** | Active Directory compromise, TCP/2222 C2, DarkVNC BackConnect, SMB to Domain Controller | ✅ Reported |
| **5** | End-to-end kill chain — malicious document → payload → C2 callback → DC compromise | ✅ Complete |

---

## 🌐 Related Public Reference Material

Supplementary open-source posts referenced during the OSINT portion of this exercise:

- 🔗 [SyBorg SCC — Facebook Post](https://www.facebook.com/SyBorgSCC/posts/pfbid0Eb1aaAhuUSoZ8eMy3MyAdNJVZSPzhrHRTYXK6g41MtzUKsSkyuYeQqMZYV3jnyx3l)
- 🔗 [Facebook Post — Reference #2](https://www.facebook.com/permalink.php?story_fbid=pfbid0tixBu17CfsnCeqCbfBmsfGiqmrx5GhWv3s1se6axV97nBdUDuGed6y9P5jwWYPMbl&id=61562252220588)

---

## ⚖️ Rules of Engagement

- Logs are monitored centrally at the **Cyber Operation Center**.
- Uploaded credentials belong to the assigned team — **do not access another team's account**.
- **Honesty is the best policy.**
- Password resets sync after 15 minutes and incur a **10-point penalty**.

*(Full text: [`RULES.txt`](./RULES.txt))*

---

## 🧑‍💻 Ownership

This repository, all its findings, write-ups, and screenshots are the **original work of a single author**: **JerenzeLevi** (`omandamjerenze@gmail.com`). No other individuals have contributed content to this repository.

<div align="center">

---
*Compiled for the Operation False Assurance cyber defense exercise.*
</div>

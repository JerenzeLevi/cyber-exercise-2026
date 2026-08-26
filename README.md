<div align="center">

# 🛡️ Operation False Assurance
### Cyber Exercise — Incident Response & OSINT Investigation

**Repository maintained by:** [JerenzeLevi](https://github.com/JerenzeLevi)

![Status](https://img.shields.io/badge/status-in%20progress-yellow)
![Phases](https://img.shields.io/badge/phases-6-blue)
![Type](https://img.shields.io/badge/type-Incident%20Response%20Exercise-critical)
![Result](https://img.shields.io/badge/RESCOM%202026-🏆%20Champion-gold)

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

The Security Operations Center recovered network evidence from **six stages of the intrusion**. This repository documents the reconstruction of that attack — tracing affected systems, malicious infrastructure, attacker progression, and containment/recovery recommendations — across six investigative phases.

---

## 🗂️ Repository Structure

```
CyberExercise/
├── Operation False Assurance - Phase 1/   # Initial compromise & first web-based delivery chain
├── Operation False Assurance - Phase 2/   # C2 infrastructure, remote access tooling, info-stealer activity
├── Operation False Assurance - Phase 3/   # DNS anomalies & executable metadata analysis
├── Operation False Assurance - Phase 4/   # Domain compromise, lateral movement, BackConnect C2
├── Operation False Assurance - Phase 5/   # Full kill-chain reconstruction, client-to-DC SMB activity
├── Operation False Assurance - Phase 6/   # (pending)
├── OSINT/                                  # Open-source intelligence gathering artifacts
└── RULES.txt                               # Exercise rules & engagement scope
```

Each phase folder contains individually numbered challenge sub-folders (e.g. `OFA P1-01 — Affected Workstation and DNS Resolver`) along with supporting evidence, screenshots, and a merged `.docx`/`.pdf` report per phase.

> **Scope note:** This directory only includes challenges I personally investigated and solved. Within the team's six-phase submission, I served both as a solver and as report writer — I authored and submitted **3 of the 6** consolidated phase reports (Phases 1, 2, and 5).

---

## 🔍 Phase Overview

<div align="center">

| Phase | Focus | Solved & Documented By | My Contribution |
|:-----:|-------|-------------------------|------------------|
| **1** | Initial infection vector, DNS resolver, TLS delivery infrastructure, PowerShell payload chain | **Jerenze Levi Omandam** | ✅ Solved all + documented |
| **2** | NetSupport RAT gateway, remote-access user-agent, information-stealer endpoints (challenge 6 left blank — closed; challenge 9 left blank — unsolved) | Team / **Jerenze Levi Omandam** (report) | ✅ Documented |
| **3** | Suspicious DNS queries, malicious executable metadata | Jefferson Balde | 🟡 Attempted 2 challenges, unsolved (no time) |
| **4** | Active Directory compromise, TCP/2222 C2, DarkVNC BackConnect, SMB to Domain Controller | Rendonn Clyde Pidor | — |
| **5** | End-to-end kill chain — malicious document → payload → C2 callback → DC compromise | **Jerenze Levi Omandam** | ✅ Solved all + documented |
| **6** | *(full write-up)* | Keshley Nitz Martinez & Rendonn Clyde Pidor | — |

</div>

---

## 🎖️ Team — BYEBUST (9RCDG)

<div align="center">

**RESCOM-Wide Cyber Exercise 2026 — 🏆 National Champion, 1st Place**
**Score: 58,763 pts · Event: Aug 22 – Aug 23, 2026 (2:00 PM close) · Venue: Kuta Dao, Pagadian City**

| Rank | Name | Role |
|:----:|------|------|
| 2LT | Charlie M. Galanay QMN PA (RES) | Team Officer |
| PVT | Keshley Nitz Martinez PA (RES) | Team Leader |
| PVT | Jefferson Balde PA (RES) | Member |
| PVT | Jerenze Levi Omandam PA (RES) | Member |
| PVT | Rendonn Clyde Pidor PA (RES) | Member |

</div>

---

## 🌐 Championship Publication Materials

Official pubmats announcing Team BYEBUST's national-level championship at RESCOM-Wide Cyber Exercise 2026, as republished by campus organizations and press.

> **Note:** GitHub strips `<iframe>` embeds from rendered READMEs for security reasons — the embeds below will only render live on platforms that allow raw HTML (e.g. a personal site or GitHub Pages). The 🔗 link under each card always works on GitHub itself.

<div align="center">

<h4>🐦 SyBorg Club (SCC)</h4>

<iframe src="https://www.facebook.com/plugins/post.php?href=https%3A%2F%2Fwww.facebook.com%2FSyBorgSCC%2Fposts%2Fpfbid02JSTHkqdjKswtLHbYE9zxWASGwMZ4bDaTDH2MdTzUY6WBq5xYEusoN56myjszuEkSl&show_text=true&width=500" width="500" height="699" style="border:none;overflow:hidden" scrolling="no" frameborder="0" allowfullscreen="true" allow="autoplay; clipboard-write; encrypted-media; picture-in-picture; web-share"></iframe>

🔗 [View post on Facebook](https://www.facebook.com/SyBorgSCC/posts/pfbid02JSTHkqdjKswtLHbYE9zxWASGwMZ4bDaTDH2MdTzUY6WBq5xYEusoN56myjszuEkSl)

<br>

<h4>🎓 CCS Grand Student Council (Saint Columban College)</h4>

<iframe src="https://www.facebook.com/plugins/post.php?href=https%3A%2F%2Fwww.facebook.com%2Fpermalink.php%3Fstory_fbid%3Dpfbid02xaPu5g32XF47b5XaRf5vP37AirYsRuTTEhQM7faEQpKKs4xauSqQvLauyChR5EbWl%26id%3D61562252220588&show_text=true&width=500" width="500" height="773" style="border:none;overflow:hidden" scrolling="no" frameborder="0" allowfullscreen="true" allow="autoplay; clipboard-write; encrypted-media; picture-in-picture; web-share"></iframe>

🔗 [View post on Facebook](https://www.facebook.com/permalink.php?story_fbid=pfbid02xaPu5g32XF47b5XaRf5vP37AirYsRuTTEhQM7faEQpKKs4xauSqQvLauyChR5EbWl&id=61562252220588)

<br>

<h4>💻 SCC PSITS</h4>

<iframe src="https://www.facebook.com/plugins/post.php?href=https%3A%2F%2Fwww.facebook.com%2Fpermalink.php%3Fstory_fbid%3Dpfbid02bwnCFomLY3hyUthRQ7DmUdT7avHrSXP8oeznBckYBnjSMwLk5NNhkriLDkdMEq1Gl%26id%3D100094561405868&show_text=true&width=500" width="500" height="486" style="border:none;overflow:hidden" scrolling="no" frameborder="0" allowfullscreen="true" allow="autoplay; clipboard-write; encrypted-media; picture-in-picture; web-share"></iframe>

🔗 [View post on Facebook](https://www.facebook.com/permalink.php?story_fbid=pfbid02bwnCFomLY3hyUthRQ7DmUdT7avHrSXP8oeznBckYBnjSMwLk5NNhkriLDkdMEq1Gl&id=100094561405868)

<br>

<h4>📰 The HARP Publication</h4>

<iframe src="https://www.facebook.com/plugins/post.php?href=https%3A%2F%2Fwww.facebook.com%2FTheHARPPublication%2Fposts%2Fpfbid02Vq4qDFJei6yrc41BHjEYWSWRPh3T7Li6dPa9JqcW5TvHKfj9SEtQyEXRoHLnndDul&show_text=true&width=500" width="500" height="738" style="border:none;overflow:hidden" scrolling="no" frameborder="0" allowfullscreen="true" allow="autoplay; clipboard-write; encrypted-media; picture-in-picture; web-share"></iframe>

🔗 [View post on Facebook](https://www.facebook.com/TheHARPPublication/posts/pfbid02Vq4qDFJei6yrc41BHjEYWSWRPh3T7Li6dPa9JqcW5TvHKfj9SEtQyEXRoHLnndDul)

</div>

---

## ⚖️ Rules of Engagement

- Logs are monitored centrally at the **Cyber Operation Center**.
- Uploaded credentials belong to the assigned team — **do not access another team's account**.
- **Honesty is the best policy.**
- Password resets sync after 15 minutes and incur a **10-point penalty**.

*(Full text: [`RULES.txt`](./RULES.txt))*

---

## 🧑‍💻 Ownership

This repository contains **only the challenges, solutions, and documentation I personally contributed** as part of Team BYEBUST's submission to Operation False Assurance. All content here — findings, write-ups, and screenshots — is authored and maintained solely by **Jerenze Levi Omandam** (`omandamjerenze@gmail.com`). Team member names above are credited for the shared exercise/competition context only; no other individuals have contributed content to this repository.

<div align="center">

---
*Compiled for the Operation False Assurance cyber defense exercise — RESCOM-Wide Cyber Exercise 2026.*
</div>

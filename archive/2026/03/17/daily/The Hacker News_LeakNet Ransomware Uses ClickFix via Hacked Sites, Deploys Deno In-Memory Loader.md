---
title: LeakNet Ransomware Uses ClickFix via Hacked Sites, Deploys Deno In-Memory Loader
url: https://thehackernews.com/2026/03/leaknet-ransomware-uses-clickfix-via.html
source: The Hacker News
date: 2026-03-17
fetch_date: 2026-03-18T04:22:52.952395
---

# LeakNet Ransomware Uses ClickFix via Hacked Sites, Deploys Deno In-Memory Loader

#1 Trusted Cybersecurity News Platform

Followed by 5.20+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Subscribe – Get Latest News](#email-outer)

* [** Home](/)
* [** Newsletter](#email-outer)
* [** Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEguiZ85S7494GyqhFt9uP48C8ggEnb3bp9Qmsdv4LOYjNWfa98MKx17Dk7o1nJrEV3ai3edIGIgwt6oO5iJMmYLcyu6PojcvJnO4IfLhVK2dzGKFyEroFjKQhnp2hd5Cc6G4CynJRfb55aclnGwj7rse9jMncn_vu_tFqQZtHZH3Sb5dMXwRKN-kSVYUMzD/s1700-e365/ai-d.png)](https://thehackernews.uk/wiz-ai-security-d)

# [LeakNet Ransomware Uses ClickFix via Hacked Sites, Deploys Deno In-Memory Loader](https://thehackernews.com/2026/03/leaknet-ransomware-uses-clickfix-via.html)

**Ravie Lakshmanan**Mar 17, 2026Ransomware / Windows Security

[![LeakNet Ransomware](data:image/png;base64... "LeakNet Ransomware")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjNHJfW8wlD2yQtP3pzAZhSRXNrzlhxXWqqG6GiAH3nbBo44Bz5mQxZ1LtsokhDYs-FC2t8hyphenhyphenY-TlNvck_Rtou9A_AA9lRnKNDRbMxZTpHfAe-6WETM-yJoWzxTANKVWrcZFdu7sax22JeTcWAVwuLKMibTNkLwSRyC0_HfBgCFM6EWqPl5-HbGtJEiSCTC/s1700-e365/leaknet-ransomware.jpg)

The ransomware operation known as **LeakNet** has adopted the [ClickFix](https://thehackernews.com/2026/03/clickfix-campaigns-spread-macsync-macos.html) social engineering tactic delivered through compromised websites as an initial access method.

The use of ClickFix, where users are tricked into manually running malicious commands to address non-existent errors, is a departure from relying on traditional methods for obtaining initial access, such as through stolen credentials acquired from initial access brokers (IABs), ReliaQuest [said](https://reliaquest.com/blog/threat-spotlight-casting-a-wider-net-clickfix-deno-and-leaknets-scaling-threat) in a technical report published today.

The second important aspect of these attacks is the use of a staged command-and-control (C2) loader built on the Deno JavaScript runtime to execute malicious payloads directly in memory.

"The key takeaway here is that both entry paths lead to the same repeatable post-exploitation sequence every time," the cybersecurity company said. "That gives defenders something concrete to work with: known behaviors you can detect and disrupt at each stage, well before ransomware deployment, regardless of how LeakNet got in."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/not-fast-enough-d)

LeakNet first emerged in [November 2024](https://www.watchguard.com/wgrd-security-hub/ransomware-tracker/leaknet), [describing](https://x.com/ido_cohen2/status/1957353482089877838) itself as a "digital watchdog" and framing its activities as focused on internet freedom and transparency. According to data captured by [Dragos](https://www.dragos.com/blog/dragos-industrial-ransomware-analysis-q2-2025), the group has also [targeted](https://redpiranha.net/news/threat-intelligence-report-august-19-august-25-2025) industrial entities.

The use of ClickFix to breach victims offers several advantages, the most significant being that it reduces dependence on third-party suppliers, lowers per-victim acquisition cost, and removes the operational bottleneck of waiting for valuable accounts to hit the market.

In these attacks, the legitimate-but-compromised sites are used to serve fake CAPTCHA verification checks that instruct users to copy and paste a "msiexec.exe" command to the Windows Run dialog. The attacks are not confined to a specific industry vertical, instead casting a wide net to infect as many victims as possible.

The development comes as more threat actors are adopting the ClickFix playbook, as it abuses trusted, everyday workflows to entice users into running rogue commands via legitimate Windows tooling in a manner that feels routine and safe.

"LeakNet's adoption of ClickFix marks both the first documented expansion of the group’s initial access capability and a meaningful strategic shift," ReliaQuest said.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjJYJyZnGmucbi-HR1XvleO-jSEpIAP4Sa48hrdVmsE69QBZKkJKVvHSNFirRRc5IrRJdGhPx85ELKJSMM1pVUNceFD281LmmF50pwUS2wE3O4CiTrW0Nv2R1lKfjTrlfdXfrad1KgsXHpzfH302QYMr8WSnuwtYVKfqxqvEoRLtsrcRamTRH7DA-uWxkE3/s1700-e365/leaknet.png)

"By moving away from IABs, LeakNet removes a dependency that naturally constrained how quickly and broadly it could operate. And because ClickFix is delivered through legitimate—but compromised—websites, it doesn’t present the same obvious signals at the network layer as attacker-owned infrastructure."

Besides the use of ClickFix to initiate the attack chain, LeakNet is assessed to be using a Deno-based loader to execute Base64-encoded JavaScript directly in memory so as to minimize on-disk evidence and evade detection. The payload is designed to fingerprint the compromised system, contact an external server to fetch next-stage malware, and enter into a polling loop that repeatedly fetches and executes additional code through Deno.

Separately, ReliaQuest said it also observed an intrusion attempt in which threat actors used Microsoft Teams-based phishing to socially engineer a user into launching a payload chain that ended in a similar Deno-based loader. While the activity remains unattributed, the use of the bring your own runtime (BYOR) approach either signals a broadening of LeakNet's initial access vectors, or that other threat actors have adopted the technique.

LeakNet's post-compromise activity follows a consistent methodology: it starts with the use of DLL side-loading to launch a malicious DLL delivered via the loader, followed by lateral movement using PsExec, data exfiltration, and encryption.

"LeakNet runs cmd.exe /c klist, a built-in Windows command that displays active authentication credentials on the compromised system. This tells the attacker which accounts and services are already reachable without the need for requesting new credentials, so they can move faster and more deliberately," ReliaQuest said.

"For staging and exfiltration, LeakNet uses S3 buckets, exploiting the appearance of normal cloud traffic to reduce its detection footprint."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/cyber-comm-guide-d)

The development comes as Google revealed that Qilin (aka Agenda), Akira (aka RedBike), Cl0p, Play, SafePay, INC Ransom, Lynx, RansomHub, DragonForce (aka FireFlame and FuryStorm), and Sinobi emerged as the top 10 ransomware brands with the most victims claimed...
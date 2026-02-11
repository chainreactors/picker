---
title: Patch Tuesday, February 2026 Edition
url: https://krebsonsecurity.com/2026/02/patch-tuesday-february-2026-edition/
source: Over Security - Cybersecurity news aggregator
date: 2026-02-10
fetch_date: 2026-02-11T04:24:01.152098
---

# Patch Tuesday, February 2026 Edition

Advertisement

[![](/b-doppel/5.png)](https://www.doppel.com/?utm_source=krebsonsecurity&utm_medium=display&utm_campaign=fy27brandcampaign&utm_content=outpace)

Advertisement

[![](/b-keeper/6.png)](https://www.keepersecurity.com/privileged-access-management/?utm_source=KrebsOnSecurity&utm_medium=Sponsored&utm_campaign=KrebsOnSecurity_020126&utm_id=Krebs)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Patch Tuesday, February 2026 Edition

February 10, 2026

[0 Comments](https://krebsonsecurity.com/2026/02/patch-tuesday-february-2026-edition/#respond)

**Microsoft** today released updates to fix more than 50 security holes in its **Windows** operating systems and other software, including patches for a whopping six “zero-day” vulnerabilities that attackers are already exploiting in the wild.

![](https://krebsonsecurity.com/wp-content/uploads/2022/07/winupdatedate.png)

Zero-day #1 this month is [CVE-2026-21510](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2026-21510), a security feature bypass vulnerability in **Windows Shell** wherein a single click on a malicious link can quietly bypass Windows protections and run attacker-controlled content without warning or consent dialogs. CVE-2026-21510 affects all currently supported versions of Windows.

The zero-day flaw [CVE-2026-21513](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2026-21513) is a security bypass bug targeting **MSHTML**, the proprietary engine of the default Web browser in Windows. [CVE-2026-21514](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2026-21514) is a related security feature bypass in **Microsoft Word.**

The zero-day [CVE-2026-21533](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2026-21533) allows local attackers to elevate their user privileges to “SYSTEM” level access in **Windows Remote Desktop Services**. [CVE-2026-21519](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2026-21519) is a zero-day elevation of privilege flaw in the **Desktop Window Manager** (DWM), a key component of Windows that organizes windows on a user’s screen. Microsoft fixed a different zero-day in DWM [just last month](https://krebsonsecurity.com/2026/01/patch-tuesday-january-2026-edition/).

The sixth zero-day is [CVE-2026-21525](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-21525), a potentially disruptive denial-of-service vulnerability in the **Windows Remote Access Connection Manager**, the service responsible for maintaining VPN connections to corporate networks.

**Chris Goettl** at **Ivanti** reminds us Microsoft has issued several out-of-band security updates since January’s Patch Tuesday. On January 17, Microsoft pushed a fix that resolved a credential prompt failure when attempting remote desktop or remote application connections. On January 26, Microsoft patched a zero-day security feature bypass vulnerability ([CVE-2026-21509](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2026-21509)) in **Microsoft Office**.

**Kev Breen** at **Immersive** notes that this month’s Patch Tuesday includes several fixes for remote code execution vulnerabilities affecting **GitHub Copilot** and multiple integrated development environments (IDEs), including **VS Code**, **Visual Studio**, and **JetBrains** products. The relevant CVEs are [CVE-2026-21516](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2026-21516), [CVE-2026-21523](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2026-21523), and [CVE-2026-21256](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2026-21256).

Breen said the AI vulnerabilities Microsoft patched this month stem from a command injection flaw that can be triggered through prompt injection, or tricking the AI agent into doing something it shouldn’t — like executing malicious code or commands.

“Developers are high-value targets for threat actors, as they often have access to sensitive data such as API keys and secrets that function as keys to critical infrastructure, including privileged AWS or Azure API keys,” Breen said. “When organizations enable developers and automation pipelines to use LLMs and agentic AI, a malicious prompt can have significant impact. This does not mean organizations should stop using AI. It does mean developers should understand the risks, teams should clearly identify which systems and workflows have access to AI agents, and least-privilege principles should be applied to limit the blast radius if developer secrets are compromised.”

The **SANS Internet Storm Center** has a [clickable breakdown](https://isc.sans.edu/diary/Microsoft%20Patch%20Tuesday%20-%20February%202026/32700) of each individual fix this month from Microsoft, indexed by severity and CVSS score. Enterprise Windows admins involved in testing patches before rolling them out should keep an eye on [askwoody.com](https://www.askwoody.com/2026/february-2026-security-updates/), which often has the skinny on wonky updates. Please don’t neglect to back up your data if it has been a while since you’ve done that, and feel free to sound off in the comments if you experience problems installing any of these fixes.

*This entry was posted on Tuesday 10th of February 2026 04:49 PM*

[Latest Warnings](https://krebsonsecurity.com/category/latest-warnings/) [Security Tools](https://krebsonsecurity.com/category/security-tools/) [Time to Patch](https://krebsonsecurity.com/category/patches/)

[Chris Goettl](https://krebsonsecurity.com/tag/chris-goettl/) [CVE-2026-21256](https://krebsonsecurity.com/tag/cve-2026-21256/) [CVE-2026-21509](https://krebsonsecurity.com/tag/cve-2026-21509/) [CVE-2026-21510](https://krebsonsecurity.com/tag/cve-2026-21510/) [CVE-2026-21513](https://krebsonsecurity.com/tag/cve-2026-21513/) [CVE-2026-21514](https://krebsonsecurity.com/tag/cve-2026-21514/) [CVE-2026-21516](https://krebsonsecurity.com/tag/cve-2026-21516/) [CVE-2026-21519](https://krebsonsecurity.com/tag/cve-2026-21519/) [CVE-2026-21523](https://krebsonsecurity.com/tag/cve-2026-21523/) [CVE-2026-21525](https://krebsonsecurity.com/tag/cve-2026-21525/) [CVE-2026-21533](https://krebsonsecurity.com/tag/cve-2026-21533/) [Desktop Window Manager](https://krebsonsecurity.com/tag/desktop-window-manager/) [Immersive](https://krebsonsecurity.com/tag/immersive/) [Ivanti](https://krebsonsecurity.com/tag/ivanti/) [Kev Breen](https://krebsonsecurity.com/tag/kev-breen/) [Microsoft Word](https://krebsonsecurity.com/tag/microsoft-word/) [MSHTML](https://krebsonsecurity.com/tag/mshtml/) [sans internet storm center](https://krebsonsecurity.com/tag/sans-internet-storm-center/) [Windows Remote Desktop Services](https://krebsonsecurity.com/tag/windows-remote-desktop-services/) [Windows shell](https://krebsonsecurity.com/tag/windows-shell/)

Post navigation

[← Please Don’t Feed the Scattered Lapsus ShinyHunters](https://krebsonsecurity.com/2026/02/please-dont-feed-the-scattered-lapsus-shiny-hunters/)

### Leave a Reply [Cancel reply](/2026/02/patch-tuesday-february-2026-edition/#respond)

Your email address will not be published. Required fields are marked \*

Comment \*

Name \*

Email \*

Website

Δ

Advertisement

[![](/b-doppel/3.png)](https://www.doppel.com/?utm_source=krebsonsecurity&utm_medium=display&utm_campaign=fy27brandcampaign&utm_content=fight)

Advertisement

Mailing List

[Subscribe here](/subscribe/)

Search KrebsOnSecurity

Search for:

Recent Posts

* [Patch Tuesday, February 2026 Edition](https://krebsonsecurity.com/2026/02/patch-tuesday-february-2026-edition/)
* [Please Don’t Feed the Scattered Lapsus ShinyHunters](https://krebsonsecurity.com/2026/02/please-dont-feed-the-scattered-lapsus-shiny-hunters...
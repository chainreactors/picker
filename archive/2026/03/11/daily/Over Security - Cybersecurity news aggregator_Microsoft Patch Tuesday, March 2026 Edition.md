---
title: Microsoft Patch Tuesday, March 2026 Edition
url: https://krebsonsecurity.com/2026/03/microsoft-patch-tuesday-march-2026-edition/
source: Over Security - Cybersecurity news aggregator
date: 2026-03-11
fetch_date: 2026-03-12T04:08:36.809623
---

# Microsoft Patch Tuesday, March 2026 Edition

Advertisement

[![](/b-knowbe4/48.jpg)](https://www.knowbe4.com/training-humans-ai-agents?utm_source=krebs&utm_medium=display&utm_campaign=traininghumansandai&utm_content=bannerai)

Advertisement

[![](/b-knowbe4/45.png)](https://info.knowbe4.com/ai-ksat-demo-kb4-con?utm_source=krebs&utm_medium=display&utm_campaign=aiagent&utm_content=demo)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Microsoft Patch Tuesday, March 2026 Edition

March 10, 2026

[6 Comments](https://krebsonsecurity.com/2026/03/microsoft-patch-tuesday-march-2026-edition/#comments)

**Microsoft Corp.** today pushed security updates to fix at least 77 vulnerabilities in its **Windows** operating systems and other software. There are no pressing “zero-day” flaws this month (compared to February’s five zero-day treat), but as usual some patches may deserve more rapid attention from organizations using Windows. Here are a few highlights from this month’s Patch Tuesday.

![](https://krebsonsecurity.com/wp-content/uploads/2026/03/winupdatechecking.png)

Two of the bugs Microsoft patched today were publicly disclosed previously. [CVE-2026-21262](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2026-21262) is a weakness that allows an attacker to elevate their privileges on **SQL Server 2016** and later editions.

“This isn’t just any elevation of privilege vulnerability, either; the advisory notes that an authorized attacker can elevate privileges to sysadmin over a network,” Rapid7’s **Adam Barnett** said. “The CVSS v3 base score of 8.8 is just below the threshold for critical severity, since low-level privileges are required. It would be a courageous defender who shrugged and deferred the patches for this one.”

The other publicly disclosed flaw is [CVE-2026-26127](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2026-26127), a vulnerability in applications running on **.NET**. Barnett said the immediate impact of exploitation is likely limited to denial of service by triggering a crash, with the potential for other types of attacks during a service reboot.

It would hardly be a proper Patch Tuesday without at least one critical **Microsoft Office** exploit, and this month doesn’t disappoint. [CVE-2026-26113](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2026-26113) and [CVE-2026-26110](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2026-26110) are both remote code execution flaws that can be triggered just by viewing a booby-trapped message in the Preview Pane.

**Satnam Narang** at **Tenable** notes that just over half (55%) of all Patch Tuesday CVEs this month are privilege escalation bugs, and of those, a half dozen were rated “exploitation more likely” — across Windows Graphics Component, Windows Accessibility Infrastructure, Windows Kernel, Windows SMB Server and Winlogon. These include:

–[CVE-2026-24291](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2026-24291): Incorrect permission assignments within the Windows Accessibility Infrastructure to reach SYSTEM (CVSS 7.8)
–[CVE-2026-24294](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2026-24294): Improper authentication in the core SMB component (CVSS 7.8)
–[CVE-2026-24289](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2026-24289): High-severity memory corruption and race condition flaw (CVSS 7.8)
–[CVE-2026-25187](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2026-25187): Winlogon process weakness discovered by Google Project Zero (CVSS 7.8).

**Ben McCarthy**, lead cyber security engineer at **Immersive**, called attention to [CVE-2026-21536](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2026-21536), a critical remote code execution bug in a component called the Microsoft Devices Pricing Program. Microsoft has already resolved the issue on their end, and fixing it requires no action on the part of Windows users. But McCarthy says it’s notable as one of the first vulnerabilities identified by an AI agent and officially recognized with a CVE attributed to the Windows operating system. It was discovered by **XBOW**, a fully autonomous AI penetration testing agent.

XBOW has consistently ranked at or near the top of the Hacker One bug bounty leaderboard for the past year. McCarthy said CVE-2026-21536 demonstrates how AI agents can identify critical 9.8-rated vulnerabilities without access to source code.

“Although Microsoft has already patched and mitigated the vulnerability, it highlights a shift toward AI-driven discovery of complex vulnerabilities at increasing speed,” McCarthy said. “This development suggests AI-assisted vulnerability research will play a growing role in the security landscape.”

Microsoft earlier provided patches to address nine browser vulnerabilities, which are not included in the Patch Tuesday count above. In addition, Microsoft issued a crucial out-of-band (emergency) [update on March 2](https://support.microsoft.com/en-us/topic/march-2-2026-kb5082314-os-build-20348-4776-out-of-band-606518e5-28d2-4ebe-be25-26287e2fc703) for **Windows Server 2022** to address a certificate renewal issue with passwordless authentication technology Windows Hello for Business.

Separately, **Adobe** shipped updates to fix 80 vulnerabilities — some of them critical in severity — in [a variety of products](https://helpx.adobe.com/security/Home.html), including **Acrobat** and **Adobe Commerce**. **Mozilla Firefox** v. 148.0.2 resolves three high severity CVEs.

For a complete breakdown of all the patches Microsoft released today, check out the SANS Internet Storm Center’s [Patch Tuesday post](https://isc.sans.edu/forums/diary/Microsoft%20Patch%20Tuesday%20March%202026/32782/). Windows enterprise admins who wish to stay abreast of any news about problematic updates, [AskWoody.com](https://www.askwoody.com) is always worth a visit. Please feel free to drop a comment below if you experience any issues apply this month’s patches.

*This entry was posted on Tuesday 10th of March 2026 08:32 PM*

[Security Tools](https://krebsonsecurity.com/category/security-tools/) [The Coming Storm](https://krebsonsecurity.com/category/comingstorm/) [Time to Patch](https://krebsonsecurity.com/category/patches/)

[Adam Barnett](https://krebsonsecurity.com/tag/adam-barnett/) [adobe](https://krebsonsecurity.com/tag/adobe/) [Ben McCarthy](https://krebsonsecurity.com/tag/ben-mccarthy/) [CVE-2026-21262](https://krebsonsecurity.com/tag/cve-2026-21262/) [CVE-2026-24289](https://krebsonsecurity.com/tag/cve-2026-24289/) [CVE-2026-24291](https://krebsonsecurity.com/tag/cve-2026-24291/) [CVE-2026-24294](https://krebsonsecurity.com/tag/cve-2026-24294/) [CVE-2026-25187](https://krebsonsecurity.com/tag/cve-2026-25187/) [CVE-2026-26110](https://krebsonsecurity.com/tag/cve-2026-26110/) [CVE-2026-26113](https://krebsonsecurity.com/tag/cve-2026-26113/) [CVE-2026-26127](https://krebsonsecurity.com/tag/cve-2026-26127/) [Immersive](https://krebsonsecurity.com/tag/immersive/) [Microsoft Office](https://krebsonsecurity.com/tag/microsoft-office/) [Microsoft Patch Tuesday March 2026](https://krebsonsecurity.com/tag/microsoft-patch-tuesday-march-2026/) [mozilla firefox](https://krebsonsecurity.com/tag/mozilla-firefox/) [Satnam Narang](https://krebsonsecurity.com/tag/satnam-narang/) [Tenable](https://krebsonsecurity.com/tag/tenable/) [XBOW](https://krebsonsecurity.com/tag/xbow/)

Post navigation

[← How AI Assistants are Moving the Security Goalposts](https://krebsonsecurity.com/2026/03/how-ai-assistants-are-moving-the-security-goalposts/)
[Iran-Backed Hackers Claim Wiper Attack on Medtech Firm Stryker →](https://krebsonsecurity.com/2026/03/iran-backed-hackers-claim-wip...
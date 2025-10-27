---
title: Six 0-Days Lead Microsoft’s August 2024 Patch Push
url: https://krebsonsecurity.com/2024/08/six-0-days-lead-microsofts-august-2024-patch-push/
source: Over Security - Cybersecurity news aggregator
date: 2024-08-14
fetch_date: 2025-10-06T18:04:25.806066
---

# Six 0-Days Lead Microsoft’s August 2024 Patch Push

Advertisement

[![](/b-knowbe4/36.jpg)](https://www.knowbe4.com/resources/kits/cybersecurity-awareness-month?utm_source=Krebs&utm_medium=display&utm_campaign=cybersecurityawarenessmonth&utm_content=hrm+)

Advertisement

[![](/b-knowbe4/41.png)](https://gateway.on24.com/wcc/eh/1815783/human-risk-management-summit?partnerref=krebs)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Six 0-Days Lead Microsoft’s August 2024 Patch Push

August 13, 2024

[13 Comments](https://krebsonsecurity.com/2024/08/six-0-days-lead-microsofts-august-2024-patch-push/#comments)

**Microsoft** today released updates to fix at least 90 security vulnerabilities in **Windows** and related software, including *a whopping six zero-day flaws* that are already being actively exploited by attackers.

![](https://krebsonsecurity.com/wp-content/uploads/2024/08/clicktofix.png)

This month’s bundle of update joy from Redmond includes patches for security holes in **Office**, **.NET**, **Visual Studio**, **Azure**, **Co-Pilot**, **Microsoft Dynamics**, **Teams**, **Secure Boot,** and of course Windows itself. Of the six zero-day weaknesses Microsoft addressed this month, half are local privilege escalation vulnerabilities — meaning they are primarily useful for attackers when combined with other flaws or access.

[CVE-2024-38106](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2024-38106), [CVE-2024-38107](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2024-38107) and [CVE-2024-38193](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2024-38193) all allow an attacker to gain SYSTEM level privileges on a vulnerable machine, although the vulnerabilities reside in different parts of the Windows operating system.

Microsoft’s advisories include little information about the last two privilege escalation flaws, other than to note they are being actively exploited. Microsoft says CVE-2024-38106 exists in the Windows Kernel and is being actively exploited, but that it has a high “attack complexity,” meaning it can be tricky for malware or miscreants to exploit reliably.

“Microsoft lists exploit complexity as high due to the attacker needing to win a race condition,” Trend Micro’s **ZeroDay Initiative** (ZDI) noted. “However, some races are easier to run than others. It’s times like this where the CVSS can be misleading. Race conditions do lead to complexity high in the CVSS score, but with attacks in the wild, it’s clear this bug is readily exploitable.”

Another zero-day this month is [CVE-2024-38178](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2024-38178), a remote code execution flaw that exists when the built-in **Windows Edge** browser is operating in “Internet Explorer Mode.” IE mode is not on by default in Edge, but it can be enabled to work with older websites or applications that aren’t supported by modern Chromium-based browsers.

“While this is not the default mode for most users, this exploit being actively exploited suggests that there are occasions in which the attacker can set this or has identified an organization (or user) that has this configuration,” wrote **Kev Breen**, senior director of threat research at Immersive Labs.

[CVE-2024-38213](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2024-38213) is a zero-day flaw that allows malware to bypass the “Mark of the Web,” a security feature in Windows that marks files downloaded from the Internet as untrusted (this Windows Smartscreen feature is responsible for the “Windows protected your PC” popup that appears when opening files downloaded from the Web).

“This vulnerability is not exploitable on its own and is typically seen as part of an exploit chain, for example, modifying a malicious document or exe file to include this bypass before sending the file via email or distributing on compromised websites,” Breen said.

The final zero-day this month is [CVE-2024-38189](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2024-38189), a remote code execution flaw in **Microsoft Project**. However, Microsoft and multiple security firms point out that this vulnerability only works on customers who have already disabled notifications about the security risks of running VBA Macros in Microsoft Project (not the best idea, as malware has a long history of hiding within malicious Office Macros).

Separately, **Adobe** today released 11 security bulletins addressing at least 71 security vulnerabilities across a range of products, including **Adobe Illustrator**, **Dimension**, **Photoshop**, **InDesign**, **Acrobat** and **Reader**, **Bridge**, **Substance 3D Stager**, **Commerce**, **InCopy**, and **Substance 3D Sampler/Substance 3D Designer**. Adobe says it is not aware of active exploitation against any of the flaws it fixed this week.

It’s a good idea for Windows users to stay current with security updates from Microsoft, which can quickly pile up otherwise. That doesn’t mean you have to install them on Patch Tuesday each month. Indeed, waiting a day or three before updating is a sane response, given that sometimes updates go awry and usually within a few days Microsoft has fixed any issues with its patches. It’s also smart to back up your data and/or image your Windows drive before applying new updates.

For a more detailed breakdown of the individual flaws addressed by Microsoft today, check out the [SANS Internet Storm Center’s list](https://isc.sans.edu/forums/diary/Microsoft%20August%202024%20Patch%20Tuesday/31164/). For those admins responsible for maintaining larger Windows environments, it pays to keep an eye on [Askwoody.com](https://www.askwoody.com/), which frequently points out when specific Microsoft updates are creating problems for a number of users.

*This entry was posted on Tuesday 13th of August 2024 05:43 PM*

[Time to Patch](https://krebsonsecurity.com/category/patches/)

[CVE-2024-38106](https://krebsonsecurity.com/tag/cve-2024-38106/) [CVE-2024-38107](https://krebsonsecurity.com/tag/cve-2024-38107/) [CVE-2024-38178](https://krebsonsecurity.com/tag/cve-2024-38178/) [CVE-2024-38189](https://krebsonsecurity.com/tag/cve-2024-38189/) [CVE-2024-38193](https://krebsonsecurity.com/tag/cve-2024-38193/) [CVE-2024-38213](https://krebsonsecurity.com/tag/cve-2024-38213/) [Kev Breen](https://krebsonsecurity.com/tag/kev-breen/) [mark of the web](https://krebsonsecurity.com/tag/mark-of-the-web/) [Microsoft Project](https://krebsonsecurity.com/tag/microsoft-project/) [Windows Edge](https://krebsonsecurity.com/tag/windows-edge/) [Zero Day Initiative](https://krebsonsecurity.com/tag/zero-day-initiative/)

Post navigation

[← Cybercrime Rapper Sues Bank over Fraud Investigation](https://krebsonsecurity.com/2024/08/cybercrime-rapper-sues-bank-over-fraud-investigation/)
[NationalPublicData.com Hack Exposes a Nation’s Data →](https://krebsonsecurity.com/2024/08/nationalpublicdata-com-hack-exposes-a-nations-data/)

## 13 thoughts on “Six 0-Days Lead Microsoft’s August 2024 Patch Push”

1. [Not Simon](https://infosec.exchange/%40screaminggoat) [August 13, 2024](https://krebsonsecurity.com/2024/08/six-0-days-lead-microsofts-august-2024-patch-push/#comment-613761)

   Just wanted to mention that CVE-2024-38199 (9.8 critical) Windows Line Printer Daemon (LPD) Service Remote Code Execution Vulnerability is publicly disclosed: <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-38199> An unauthenticated attacker could send a specially crafted print task to a shared vulnerable Windows Line Printer Daemon (LPD) service across a network. Successful exploitation could result in remote code execution on the server.
2. [Alexander Akpodiete](https:www.atawatech.com) [...
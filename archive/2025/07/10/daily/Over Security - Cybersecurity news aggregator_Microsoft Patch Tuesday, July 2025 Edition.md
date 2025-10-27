---
title: Microsoft Patch Tuesday, July 2025 Edition
url: https://krebsonsecurity.com/2025/07/microsoft-patch-tuesday-july-2025-edition/
source: Over Security - Cybersecurity news aggregator
date: 2025-07-10
fetch_date: 2025-10-06T23:51:03.436458
---

# Microsoft Patch Tuesday, July 2025 Edition

Advertisement

[![](/b-action1/1.jpg)](https://action1.com/double-endpoints-free-cam2025/?utm_source=paidmedia&refid=Display_CAM_Krebs)

Advertisement

[![](/b-knowbe4/37.jpg)](https://www.knowbe4.com/resources/kits/cybersecurity-awareness-month?utm_source=Krebs&utm_medium=display&utm_campaign=cybersecurityawarenessmonth&utm_content=hrm+)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Microsoft Patch Tuesday, July 2025 Edition

July 8, 2025

[9 Comments](https://krebsonsecurity.com/2025/07/microsoft-patch-tuesday-july-2025-edition/#comments)

**Microsoft** today released updates to fix at least 137 security vulnerabilities in its **Windows** operating systems and supported software. None of the weaknesses addressed this month are known to be actively exploited, but 14 of the flaws earned Microsoft’s most-dire “critical” rating, meaning they could be exploited to seize control over vulnerable Windows PCs with little or no help from users.

![](https://krebsonsecurity.com/wp-content/uploads/2022/07/winupdatedate.png)

While not listed as critical, [CVE-2025-49719](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2025-49719) is a publicly disclosed information disclosure vulnerability, with all versions as far back as **SQL Server 2016** receiving patches. Microsoft rates CVE-2025-49719 as less likely to be exploited, but the availability of proof-of-concept code for this flaw means its patch should probably be a priority for affected enterprises.

**Mike Walters**, co-founder of **Action1**, said CVE-2025-49719 can be exploited without authentication, and that many third-party applications depend on SQL server and the affected drivers — potentially introducing a supply-chain risk that extends beyond direct SQL Server users.

“The potential exposure of sensitive information makes this a high-priority concern for organizations handling valuable or regulated data,” Walters said. “The comprehensive nature of the affected versions, spanning multiple SQL Server releases from 2016 through 2022, indicates a fundamental issue in how SQL Server handles memory management and input validation.”

**Adam Barnett** at **Rapid7** notes that today is the end of the road for **SQL Server 2012**, meaning there will be no future security patches even for critical vulnerabilities, even if you’re willing to pay Microsoft for the privilege.

Barnett also called attention to [CVE-2025-47981](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2025-47981), a vulnerability with a CVSS score of 9.8 (10 being the worst), a remote code execution bug in the way Windows servers and clients negotiate to discover mutually supported authentication mechanisms. This pre-authentication vulnerability affects any Windows client machine running **Windows 10 1607** or above, and all current versions of **Windows Server**. Microsoft considers it more likely that attackers will exploit this flaw.

Microsoft also patched at least four critical, remote code execution flaws in **Office** ([CVE-2025-49695](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2025-49695), [CVE-2025-49696](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2025-49696), [CVE-2025-49697](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2025-49697), [CVE-2025-49702](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2025-49702)). The first two are both rated by Microsoft as having a higher likelihood of exploitation, do not require user interaction, and can be triggered through the Preview Pane.

Two more high severity bugs include [CVE-2025-49740](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2025-49740) (CVSS 8.8) and [CVE-2025-47178](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2025-47178) (CVSS 8.0); the former is a weakness that could allow malicious files to bypass screening by **Microsoft Defender SmartScreen**, a built-in feature of Windows that tries to block untrusted downloads and malicious sites.

CVE-2025-47178 involves a remote code execution flaw in **Microsoft Configuration Manager**, an enterprise tool for managing, deploying, and securing computers, servers, and devices across a network. **Ben Hopkins** at **Immersive** said this bug requires very low privileges to exploit, and that it is possible for a user or attacker with a read-only access role to exploit it.

“Exploiting this vulnerability allows an attacker to execute arbitrary SQL queries as the privileged SMS service account in Microsoft Configuration Manager,” Hopkins said. “This access can be used to manipulate deployments, push malicious software or scripts to all managed devices, alter configurations, steal sensitive data, and potentially escalate to full operating system code execution across the enterprise, giving the attacker broad control over the entire IT environment.”

Separately, **Adobe** has [released security updates](https://helpx.adobe.com/security/security-bulletin.html) for a broad range of software, including **After Effects**, **Adobe Audition**, **Illustrator**, **FrameMaker**, and **ColdFusion**.

The **SANS Internet Storm Center** has [a breakdown of each individual patch](https://isc.sans.edu/diary/Microsoft%20Patch%20Tuesday%2C%20July%202025/32088), indexed by severity. If you’re responsible for administering a number of Windows systems, it may be worth keeping an eye on [AskWoody](https://www.askwoody.com/) for the lowdown on any potentially wonky updates (considering the large number of vulnerabilities and Windows components addressed this month).

If you’re a Windows home user, please consider backing up your data and/or drive before installing any patches, and drop a note in the comments if you encounter any problems with these updates.

*This entry was posted on Tuesday 8th of July 2025 08:53 PM*

[Latest Warnings](https://krebsonsecurity.com/category/latest-warnings/) [Security Tools](https://krebsonsecurity.com/category/security-tools/) [Time to Patch](https://krebsonsecurity.com/category/patches/)

[Action1](https://krebsonsecurity.com/tag/action1/) [Adam Barnett](https://krebsonsecurity.com/tag/adam-barnett/) [adobe](https://krebsonsecurity.com/tag/adobe/) [Ben Hopkins](https://krebsonsecurity.com/tag/ben-hopkins/) [CVE-2025-47178](https://krebsonsecurity.com/tag/cve-2025-47178/) [CVE-2025-47981](https://krebsonsecurity.com/tag/cve-2025-47981/) [CVE-2025-49695](https://krebsonsecurity.com/tag/cve-2025-49695/) [CVE-2025-49696](https://krebsonsecurity.com/tag/cve-2025-49696/) [CVE-2025-49697](https://krebsonsecurity.com/tag/cve-2025-49697/) [CVE-2025-49702](https://krebsonsecurity.com/tag/cve-2025-49702/) [CVE-2025-49719](https://krebsonsecurity.com/tag/cve-2025-49719/) [CVE-2025-49740](https://krebsonsecurity.com/tag/cve-2025-49740/) [Microsoft Configuration Manager](https://krebsonsecurity.com/tag/microsoft-configuration-manager/) [Microsoft Defender SmartScreen](https://krebsonsecurity.com/tag/microsoft-defender-smartscreen/) [Microsoft Patch Tuesday July 2025 Edition](https://krebsonsecurity.com/tag/microsoft-patch-tuesday-july-2025-edition/) [Mike Walters](https://krebsonsecurity.com/tag/mike-walters/) [Office](https://krebsonsecurity.com/tag/office/) [Rapid7](https://krebsonsecurity.com/tag/rapid7/) [SQL Server 2012](https://krebsonsecurity.com/tag/sql-server-2012/) [SQL Server 2016](https://krebsonsecurity.com/tag/sql-server-2016/)

Post navigation

[← Big Tech’s Mixed Response to U.S. Treasury Sanctions](https://krebsonsecurity.com/2025/07/big-techs-mixed-response-to-u-s-treasury-sanctions/)
[UK Arrests Four in ‘Scattered Spider’ Ransom Group →](https://krebsonsecurity.com/2025/07/uk-charges-four-in-scattered-spider-ransom-gr...
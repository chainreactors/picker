---
title: Microsoft Patches a Record 570 Security Flaws
url: https://krebsonsecurity.com/2026/07/microsoft-patches-a-record-570-security-flaws/
source: Krebs on Security
date: 2026-07-14
fetch_date: 2026-07-15T04:49:58.611827
---

# Microsoft Patches a Record 570 Security Flaws

Advertisement

[![](/b-flashpoint/5.png)](https://flashpoint.io/ignite/?utm_source=krebsonsecurity&utm_medium=display&utm_campaign=brand-ignite&utm_content=noise-a)

Advertisement

[![](/b-keeper/14.png)](https://www.keepersecurity.com/privileged-access-management/?utm_source=KrebsOnSecurity&utm_medium=Sponsored&utm_campaign=KrebsOnSecurity_020126&utm_id=Krebs)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Microsoft Patches a Record 570 Security Flaws

July 14, 2026

[12 Comments](https://krebsonsecurity.com/2026/07/microsoft-patches-a-record-570-security-flaws/#comments)

**Microsoft Corp.** today released software updates to plug at least 570 security holes in its **Windows** operating systems and other software, almost triple the number of vulnerabilities the software giant fixed in its record-smashing Patch Tuesday release last month. Microsoft attributed the burgeoning patch counts to vulnerability discoveries aided by artificial intelligence.

![A picture of a windows laptop in its updating stage, saying do not turn off the computer.](https://krebsonsecurity.com/wp-content/uploads/2021/07/windupate.png)

Nearly 60 of the bugs quashed in July’s Patch Tuesday earned a “critical” severity rating, meaning miscreants or malware could use them to seize remote control over a Windows device with little or no help from the user. Microsoft also addressed three zero-day flaws, including two that are already being exploited in the wild.

Two of the zero-day weaknesses allow an attacker to elevate their user rights on a Windows system, as do approximately 250 other elevation of privilege flaws fixed this month; they include [CVE-2026-56155](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2026-56155) — an **Active Directory Federation Services** bug — and [CVE-2026-56164](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2026-56164), a **Microsoft Sharepoint** vulnerability.

[CVE-2026-50661](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2026-50661) is a security feature bypass in **Windows BitLocker** that could allow attackers to gain access to encrypted data if they have physical access to the device. Microsoft said this bug has been detailed publicly, but that it is not aware of any active exploitation.

In a blog post on July 9, Microsoft Executive Vice President **Pavan Davuluri** wrote that Windows users will notice “a higher volume of security updates included in each security release” as a result of AI aiding in the discovery of vulnerabilities.

“The pace of vulnerability discovery is changing with advances in AI making it possible to find more issues, faster, across more code, with new mechanisms that can accelerate both discovery and analysis,” Davuluri [wrote](https://blogs.windows.com/windowsexperience/2026/07/09/evolving-windows-vulnerability-management-to-meet-the-speed-of-ai-powered-discovery/).

**Jack Bicer**, director of vulnerability research at **Action1**, called attention to [CVE-2026-48561](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2026-48561), a remote code execution flaw in Microsoft Copilot (with a 9.6 CVSS threat score) that allows an unauthorized attacker to execute code over the network. Microsoft says an attacker could exploit this bug by hosting a malicious website that causes Microsoft Edge for Android to automatically send crafted prompts to Copilot when a user visits the site.

As AI advances the state of vulnerability discovery and remediation, it is also making it easier for attackers to quickly devise working exploits for known software flaws. Microsoft has long labeled security bugs using its “exploitability index,” which is Redmond’s best guess as to how likely it is that attackers will be able to figure out a reliable way to exploit a given vulnerability.

But **Satnam Narang**, senior staff research engineer at **Tenable**, argues that Microsoft’s exploitability index needs to do a better job of shifting with the machine speed of discovery. For example, Microsoft originally gave this month’s SharePoint zero-day an exploitability rating of “less likely,” although the flaw was [added](https://www.cisa.gov/news-events/alerts/2026/07/01/cisa-adds-one-known-exploited-vulnerability-catalog) to CISA’s Known Exploited Vulnerabilities list on July 1.

“Anthropic’s Red Team’s own findings for known vulnerabilities (n-days) revealed how fragile this system has become, with its Mythos Preview model being able to produce proof-of-concept exploits for 13 of 14 vulnerabilities that were rated ‘Exploitation Less Likely’ or ‘Exploitation Unlikely,'” Narang said. “What this means is that our way of looking at Patch Tuesday has changed, because the exploitability index is centered around humans, not AI tools, and as these tools continue to improve, defense needs to improve alongside it.”

**Chris Goettl** at **Ivanti** observed that the record patch numbers from Microsoft come as a number of other major software makers are increasing their patch cadence, including Adobe which announced today it is moving to twice-monthly security bulletins published on the 2nd and 4th Tuesday of each month (Adobe also cited AI for accelerating their patch cycles). **Cisco**, **Mozilla** and **Oracle** also are shipping updates more frequently, while Google’s patch batches in June 2026 totaled more than 900 security fixes, Goettl noted.

Backing up your Windows system and/or data is always a good idea before applying operating system updates. Given the volume of patches addressed this month it may be wise for end users to wait a few days before applying these fixes. It’s not uncommon for security patches to introduce system stability issues, and those chances probably increase quite a bit with the gigantic patch count released today.

Further reading:

[Action1’s Patch Tuesday blog](https://www.action1.com/patch-tuesday/patch-tuesday-july-2026/?vyi)

[Automox’s rundown](https://listen.automox.com/episodes/patch-fix-tuesday-july-2026-e34)

*This entry was posted on Tuesday 14th of July 2026 03:22 PM*

[Security Tools](https://krebsonsecurity.com/category/security-tools/) [The Coming Storm](https://krebsonsecurity.com/category/comingstorm/) [Time to Patch](https://krebsonsecurity.com/category/patches/)

[Action1](https://krebsonsecurity.com/tag/action1/) [Active Directory Federation Services](https://krebsonsecurity.com/tag/active-directory-federation-services/) [Chris Goettl](https://krebsonsecurity.com/tag/chris-goettl/) [CVE-2026-48561](https://krebsonsecurity.com/tag/cve-2026-48561/) [CVE-2026-50661](https://krebsonsecurity.com/tag/cve-2026-50661/) [CVE-2026-56155](https://krebsonsecurity.com/tag/cve-2026-56155/) [CVE-2026-56164](https://krebsonsecurity.com/tag/cve-2026-56164/) [Ivanti](https://krebsonsecurity.com/tag/ivanti/) [Jack Bicer](https://krebsonsecurity.com/tag/jack-bicer/) [Microsoft Corp.](https://krebsonsecurity.com/tag/microsoft-corp/) [Patch Tuesday July 2026](https://krebsonsecurity.com/tag/patch-tuesday-july-2026/) [Pavan Davuluri](https://krebsonsecurity.com/tag/pavan-davuluri/) [Satnam Narang](https://krebsonsecurity.com/tag/satnam-narang/) [Tenable](https://krebsonsecurity.com/tag/tenable/) [Windows BitLocker](https://krebsonsecurity.com/tag/windows-bitlocker/)

Post navigation

[← Lessons Learned from CISA’s Recent GitHub Leak](https://krebsonsecurity.com/2026/07/lessons-learned-from-cisas-recent-github-leak/)

## 12 thoughts on “Microsoft Patches a Record 570 Security Flaws”

1. DB in Denver [July 14, 2026](https://krebsonsecurity.com/2026/07/microsoft-patches-a-record-570-security-flaws/#comment-657862)

   Still as confused as before … how could there be 570 flaws if Micro...
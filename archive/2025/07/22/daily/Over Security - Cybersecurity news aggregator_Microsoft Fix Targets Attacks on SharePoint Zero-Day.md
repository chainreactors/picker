---
title: Microsoft Fix Targets Attacks on SharePoint Zero-Day
url: https://krebsonsecurity.com/2025/07/microsoft-fix-targets-attacks-on-sharepoint-zero-day/
source: Over Security - Cybersecurity news aggregator
date: 2025-07-22
fetch_date: 2025-10-06T23:50:00.894694
---

# Microsoft Fix Targets Attacks on SharePoint Zero-Day

Advertisement

[![](/b-knowbe4/36.jpg)](https://www.knowbe4.com/resources/kits/cybersecurity-awareness-month?utm_source=Krebs&utm_medium=display&utm_campaign=cybersecurityawarenessmonth&utm_content=hrm+)

Advertisement

[![](/b-gartner/4.jpg)](https://www.gartner.com/en/conferences/na/identity-access-management-us?utm_source=krebs&utm_medium=banner&utm_campaign=EVT_NA_2025_IAM20_PP_MP6_KREBSONSECURITY)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Microsoft Fix Targets Attacks on SharePoint Zero-Day

July 21, 2025

[7 Comments](https://krebsonsecurity.com/2025/07/microsoft-fix-targets-attacks-on-sharepoint-zero-day/#comments)

On Sunday, July 20, **Microsoft Corp.** issued an emergency security update for a vulnerability in **SharePoint Server** that is actively being exploited to compromise vulnerable organizations. The patch comes amid reports that malicious hackers have used the SharePoint flaw to breach U.S. federal and state agencies, universities, and energy companies.

![](https://krebsonsecurity.com/wp-content/uploads/2025/07/ms-sharepoint-ss.png)

In [an advisory](https://msrc.microsoft.com/blog/2025/07/customer-guidance-for-sharepoint-vulnerability-cve-2025-53770/) about the SharePoint security hole, a.k.a. [CVE-2025-53770](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2025-53770), Microsoft said it is aware of active attacks targeting on-premises SharePoint Server customers and exploiting vulnerabilities that were only partially addressed by [the July 8, 2025 security update](https://krebsonsecurity.com/2025/07/microsoft-patch-tuesday-july-2025-edition/).

The **Cybersecurity & Infrastructure Security Agency** (CISA) [concurred](https://www.cisa.gov/news-events/alerts/2025/07/20/microsoft-releases-guidance-exploitation-sharepoint-vulnerability-cve-2025-53770), saying CVE-2025-53770 is a variant on a flaw Microsoft patched earlier this month ([CVE-2025-49706)](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2025-49706). Microsoft notes the weakness applies only to SharePoint Servers that organizations use in-house, and that SharePoint Online and Microsoft 365 are not affected.

**The Washington Post** [reported](https://www.washingtonpost.com/technology/2025/07/20/microsoft-sharepoint-hack/) on Sunday that the U.S. government and partners in Canada and Australia are investigating the hack of SharePoint servers, which provide a platform for sharing and managing documents. The Post reports at least two U.S. federal agencies have seen their servers breached via the SharePoint vulnerability.

According to CISA, attackers exploiting the newly-discovered flaw are retrofitting compromised servers with a backdoor dubbed “**ToolShell**” that provides unauthenticated, remote access to systems. CISA said ToolShell enables attackers to fully access SharePoint content — including file systems and internal configurations — and execute code over the network.

Researchers at **Eye Security** said they first spotted large-scale exploitation of the SharePoint flaw on July 18, 2025, and soon found dozens of separate servers compromised by the bug and infected with ToolShell. In [a blog post](https://research.eye.security/sharepoint-under-siege/), the researchers said the attacks sought to steal SharePoint server ASP.NET machine keys.

“These keys can be used to facilitate further attacks, even at a later date,” Eye Security warned. “It is critical that affected servers rotate SharePoint server ASP.NET machine keys and restart IIS on all SharePoint servers. Patching alone is not enough. We strongly advise defenders not to wait for a vendor fix before taking action. This threat is already operational and spreading rapidly.”

Microsoft’s advisory says the company has issued updates for **SharePoint Server Subscription Edition** and **SharePoint Server 2019**, but that it is still working on updates for supported versions of **SharePoint 2019** and **SharePoint 2016**.

CISA advises vulnerable organizations to enable the anti-malware scan interface (AMSI) in SharePoint, to deploy Microsoft Defender AV on all SharePoint servers, and to disconnect affected products from the public-facing Internet until an official patch is available.

The security firm **Rapid7** [notes](https://www.rapid7.com/blog/post/etr-zero-day-exploitation-of-microsoft-sharepoint-servers-cve-2025-53770/) that Microsoft has described CVE-2025-53770 as related to a previous vulnerability — [CVE-2025-49704](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2025-49704), patched earlier this month — and that CVE-2025-49704 was part of an exploit chain demonstrated at the **Pwn2Own** hacking competition in May 2025. That exploit chain invoked a second SharePoint weakness — [CVE-2025-49706](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2025-49706) — which Microsoft unsuccessfully tried to fix in this month’s Patch Tuesday.

Microsoft also has issued a patch for a related SharePoint vulnerability — [CVE-2025-53771](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2025-53771); Microsoft says there are no signs of active attacks on CVE-2025-53771, and that the patch is to provide more robust protections than the update for CVE-2025-49706.

*This is a rapidly developing story. Any updates will be noted with timestamps.*

*This entry was posted on Monday 21st of July 2025 10:45 AM*

[Latest Warnings](https://krebsonsecurity.com/category/latest-warnings/) [The Coming Storm](https://krebsonsecurity.com/category/comingstorm/) [Time to Patch](https://krebsonsecurity.com/category/patches/)

[CISA](https://krebsonsecurity.com/tag/cisa/) [CVE-2025-49704](https://krebsonsecurity.com/tag/cve-2025-49704/) [CVE-2025-49706](https://krebsonsecurity.com/tag/cve-2025-49706/) [CVE-2025-53770](https://krebsonsecurity.com/tag/cve-2025-53770/) [CVE-2025-53771](https://krebsonsecurity.com/tag/cve-2025-53771/) [Cybersecurity & Infrastructure Security Agency](https://krebsonsecurity.com/tag/cybersecurity-infrastructure-security-agency/) [Eye Security](https://krebsonsecurity.com/tag/eye-security/) [Microsoft Corp.](https://krebsonsecurity.com/tag/microsoft-corp/) [Rapid7](https://krebsonsecurity.com/tag/rapid7/) [SharePoint Server](https://krebsonsecurity.com/tag/sharepoint-server/)

Post navigation

[← Poor Passwords Tattle on AI Hiring Bot Maker Paradox.ai](https://krebsonsecurity.com/2025/07/poor-passwords-tattle-on-ai-hiring-bot-maker-paradox-ai/)
[Phishers Target Aviation Execs to Scam Customers →](https://krebsonsecurity.com/2025/07/phishers-target-aviation-execs-to-scam-customers/)

## 7 thoughts on “Microsoft Fix Targets Attacks on SharePoint Zero-Day”

1. [James Schumaker](https://shoeone.blogspot.com) [July 21, 2025](https://krebsonsecurity.com/2025/07/microsoft-fix-targets-attacks-on-sharepoint-zero-day/#comment-628670)

   Last March, the FBI was tasked to review roughly 100,000 documents relating to the Epstein case. The spreadsheet detailing the number of times President Trump was mentioned was done in Excel on an internal SharePoint server. I’m wondering if it might have been vulnerable to compromise. <https://www.muellershewrote.com/p/the-epstein-cover-up-at-the-fbi>

   1. mealy [July 21, 2025](https://krebsonsecurity.com/2025/07/microsoft-fix-targets-attacks-on-sharepoint-zero-day/#comment-628672)

      Maybe, but without chain of custody and documented handling, you couldn’t trust it to be legit.

      1. Fr00tL00ps [July 22, 2025](https://krebsonsecurity.com/2025/07/microsoft-fix-targets-attacks-on-sharepoint-zero-day/#comment-628680)

         Tell that to the MAGA crowd. Even when it’s proven legit, it’s still ‘fAkE nEwS’. ¯⁠\⁠\_⁠(⁠ツ⁠)\_/¯

 ...
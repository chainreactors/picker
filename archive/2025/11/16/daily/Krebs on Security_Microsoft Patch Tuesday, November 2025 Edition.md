---
title: Microsoft Patch Tuesday, November 2025 Edition
url: https://krebsonsecurity.com/2025/11/microsoft-patch-tuesday-november-2025-edition/
source: Krebs on Security
date: 2025-11-16
fetch_date: 2025-11-17T03:12:56.409317
---

# Microsoft Patch Tuesday, November 2025 Edition

Advertisement

[![](/b-action1/1.jpg)](https://action1.com/double-endpoints-free-cam2025/?utm_source=paidmedia&refid=Display_CAM_Krebs)

Advertisement

[![](/b-sysdig/2.png)](https://content.foleon.com/sysdig/sysdig-cloud-defense-report-2025/?utm_source=krebs-on-security&utm_medium=display&utm_campaign=aware_amer_the-right-way_na_ung_display&utm_content=AD000462_1240x160)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Microsoft Patch Tuesday, November 2025 Edition

November 16, 2025

[3 Comments](https://krebsonsecurity.com/2025/11/microsoft-patch-tuesday-november-2025-edition/#comments)

**Microsoft** this week pushed security updates to fix more than 60 vulnerabilities in its **Windows** operating systems and supported software, including at least one zero-day bug that is already being exploited. Microsoft also fixed a glitch that prevented some **Windows 10** users from taking advantage of an extra year of security updates, which is nice because the zero-day flaw and other critical weaknesses patched today affect all versions of Windows, including Windows 10.

![](https://krebsonsecurity.com/wp-content/uploads/2021/07/windupate.png)

Affected products this month include the Windows OS, **Office**, **SharePoint**, **SQL Server**, **Visual Studio**, **GitHub Copilot**, and **Azure Monitor Agent**. The zero-day threat concerns a memory corruption bug deep in the Windows innards called [CVE-2025-62215](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-62215). Despite the flaw’s zero-day status, Microsoft has assigned it an “important” rating rather than critical, because exploiting it requires an attacker to already have access to the target’s device.

“These types of vulnerabilities are often exploited as part of a more complex attack chain,” said **Johannes Ullrich**, dean of research for the **SANS Technology Institute**. “However, exploiting this specific vulnerability is likely to be relatively straightforward, given the existence of prior similar vulnerabilities.”

**Ben McCarthy**, lead cybersecurity engineer at **Immersive**, called attention to [CVE-2025-60274](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-60724), a critical weakness in a core Windows graphic component (GDI+) that is used by a massive number of applications, including Microsoft Office, web servers processing images, and countless third-party applications.

“The patch for this should be an organization’s highest priority,” McCarthy said. “While Microsoft assesses this as ‘Exploitation Less Likely,’ a 9.8-rated flaw in a ubiquitous library like GDI+ is a critical risk.”

Microsoft patched a critical bug in **Office** — [CVE-2025-62199](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-62199) — that can lead to remote code execution on a Windows system. **Alex Vovk**, CEO and co-founder of **Action1**, said this Office flaw is a high priority because it is low complexity, needs no privileges, and can be exploited just by viewing a booby-trapped message in the Preview Pane.

Many of the more concerning bugs addressed by Microsoft this month affect Windows 10, an operating system that Microsoft officially ceased supporting with patches last month. As that deadline rolled around, however, Microsoft began offering Windows 10 users an extra year of free updates, so long as they register their PC to an active Microsoft account.

Judging from the comments on [last month’s Patch Tuesday post](https://krebsonsecurity.com/2025/10/patch-tuesday-october-2025-end-of-10-edition/), that registration worked for a lot of Windows 10 users, but some readers reported the option for an extra year of updates was never offered. **Nick Carroll**, cyber incident response manager at **Nightwing**, notes that Microsoft has recently released an out-of-band update to address [issues when trying to enroll](https://www.howtogeek.com/microsoft-broke-windows-10s-extended-security-updates-but-a-fix-has-arrived/) in the Windows 10 Consumer Extended Security Update program.

“If you plan to participate in the program, make sure you update and install [KB5071959](https://support.microsoft.com/en-us/topic/november-11-2025-kb5071959-windows-10-version-22h2-os-build-19045-6466-out-of-band-565c78a7-5b5f-4cbd-8ca8-2a73a48f4e2b) to address the enrollment issues,” Carroll said. “After that is installed, users should be able to install other updates such as today’s KB5068781 which is the latest update to Windows 10.”

**Chris Goettl** at **Ivanti** notes that in addition to Microsoft updates today, third-party updates from **Adobe** and **Mozilla** have already been released. Also, an update for **Google Chrome** is expected soon, which means **Edge** will also be in need of its own update.

The **SANS Internet Storm Center** has a [clickable breakdown](https://isc.sans.edu/diary/Microsoft%20Patch%20Tuesday%20for%20November%202025/32468) of each individual fix from Microsoft, indexed by severity and CVSS score. Enterprise Windows admins involved in testing patches before rolling them out should keep an eye on [askwoody.com](https://www.askwoody.com/2025/september-2025-updates-are-out/), which often has the skinny on any updates gone awry.

As always, please don’t neglect to back up your data (if not your entire system) at regular intervals, and feel free to sound off in the comments if you experience problems installing any of these fixes.

*[Author’s note: This post was intended to appear on the homepage on Tuesday, Nov. 11. I’m still not sure how it happened, but somehow this story failed to publish that day. My apologies for the oversight.]*

*This entry was posted on Sunday 16th of November 2025 04:47 PM*

[Time to Patch](https://krebsonsecurity.com/category/patches/)

[Action1](https://krebsonsecurity.com/tag/action1/) [Alex Vovk](https://krebsonsecurity.com/tag/alex-vovk/) [Azure Monitor Agent](https://krebsonsecurity.com/tag/azure-monitor-agent/) [Chris Goettl](https://krebsonsecurity.com/tag/chris-goettl/) [CVE-2025-60274](https://krebsonsecurity.com/tag/cve-2025-60274/) [CVE-2025-62199](https://krebsonsecurity.com/tag/cve-2025-62199/) [CVE-2025-62215](https://krebsonsecurity.com/tag/cve-2025-62215/) [GitHub Copilot](https://krebsonsecurity.com/tag/github-copilot/) [Ivanti](https://krebsonsecurity.com/tag/ivanti/) [Johannes Ullrich](https://krebsonsecurity.com/tag/johannes-ullrich/) [KB5071959](https://krebsonsecurity.com/tag/kb5071959/) [Microsoft Patch Tuesday November 2025](https://krebsonsecurity.com/tag/microsoft-patch-tuesday-november-2025/) [Nick Carroll](https://krebsonsecurity.com/tag/nick-carroll/) [Nightwing](https://krebsonsecurity.com/tag/nightwing/) [Office](https://krebsonsecurity.com/tag/office/) [SANS Technology Institute](https://krebsonsecurity.com/tag/sans-technology-institute/) [Sharepoint](https://krebsonsecurity.com/tag/sharepoint/) [SQL Server](https://krebsonsecurity.com/tag/sql-server/) [Visual Studio](https://krebsonsecurity.com/tag/visual-studio/)

Post navigation

[← Google Sues to Disrupt Chinese SMS Phishing Triad](https://krebsonsecurity.com/2025/11/google-sues-to-disrupt-chinese-sms-phishing-triad/)

## 3 thoughts on “Microsoft Patch Tuesday, November 2025 Edition”

1. Larry Pearsonovich [November 16, 2025](https://krebsonsecurity.com/2025/11/microsoft-patch-tuesday-november-2025-edition/#comment-632371)

   I have Windows 10 and since mid October have still been experiencing what look like updates. I was planning to let it ride until my PC said it could take no more and I would switch to a Linux system already purchased.

   After the last update pause I turned on my PC and all my Microsoft 365 programs (Word, Excel, PP, etc.) had disa...
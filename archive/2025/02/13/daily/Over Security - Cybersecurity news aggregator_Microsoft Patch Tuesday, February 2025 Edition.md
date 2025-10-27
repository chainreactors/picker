---
title: Microsoft Patch Tuesday, February 2025 Edition
url: https://krebsonsecurity.com/2025/02/microsoft-patch-tuesday-february-2025-edition/
source: Over Security - Cybersecurity news aggregator
date: 2025-02-13
fetch_date: 2025-10-06T20:48:28.312830
---

# Microsoft Patch Tuesday, February 2025 Edition

Advertisement

[![](/b-action1/1.jpg)](https://action1.com/double-endpoints-free-cam2025/?utm_source=paidmedia&refid=Display_CAM_Krebs)

Advertisement

[![](/b-sysdig/2.png)](https://content.foleon.com/sysdig/sysdig-cloud-defense-report-2025/?utm_source=krebs-on-security&utm_medium=display&utm_campaign=aware_amer_the-right-way_na_ung_display&utm_content=AD000462_1240x160)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Microsoft Patch Tuesday, February 2025 Edition

February 11, 2025

[19 Comments](https://krebsonsecurity.com/2025/02/microsoft-patch-tuesday-february-2025-edition/#comments)

**Microsoft** today issued security updates to fix at least 56 vulnerabilities in its Windows operating systems and supported software, including two zero-day flaws that are being actively exploited.

![](https://krebsonsecurity.com/wp-content/uploads/2021/07/windupate.png)

All supported Windows operating systems will receive an update this month for a buffer overflow vulnerability that carries the catchy name [CVE-2025-21418](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-21418). This patch should be a priority for enterprises, as Microsoft says it is being exploited, has low attack complexity, and no requirements for user interaction.

**Tenable** senior staff research engineer **Satnam Narang** noted that since 2022, there have been nine elevation of privilege vulnerabilities in this same Windows component — three each year — including one in 2024 that was exploited in the wild as a zero day (CVE-2024-38193).

“CVE-2024-38193 was exploited by the North Korean APT group known as Lazarus Group to implant a new version of the FudModule rootkit in order to maintain persistence and stealth on compromised systems,” Narang said. “At this time, it is unclear if CVE-2025-21418 was also exploited by Lazarus Group.”

The other zero-day, [CVE-2025-21391](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-21391), is an elevation of privilege vulnerability in Windows Storage that could be used to delete files on a targeted system. Microsoft’s advisory on this bug references something called “CWE-59: Improper Link Resolution Before File Access,” says no user interaction is required, and that the attack complexity is low.

**Adam Barnett**, lead software engineer at **Rapid7**, said although the advisory provides scant detail, and even offers some vague reassurance that ‘an attacker would only be able to delete targeted files on a system,’ it would be a mistake to assume that the impact of deleting arbitrary files would be limited to data loss or denial of service.

“As long ago as 2022, ZDI researchers set out how a motivated attacker could parlay arbitrary file deletion into full SYSTEM access using techniques which also involve creative misuse of symbolic links,”Barnett wrote.

One vulnerability patched today that was publicly disclosed earlier is [CVE-2025-21377](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-21377), another weakness that could allow an attacker to elevate their privileges on a vulnerable Windows system. Specifically, this is yet another Windows flaw that can be used to steal NTLMv2 hashes — essentially allowing an attacker to authenticate as the targeted user without having to log in.

According to Microsoft, minimal user interaction with a malicious file is needed to exploit CVE-2025-21377, including selecting, inspecting or “performing an action other than opening or executing the file.”

“This trademark linguistic ducking and weaving may be Microsoft’s way of saying ‘if we told you any more, we’d give the game away,'” Barnett said. “Accordingly, Microsoft assesses exploitation as more likely.”

The [SANS Internet Storm Center](https://isc.sans.edu/diary/Microsoft%20February%202025%20Patch%20Tuesday/31674) has a handy list of all the Microsoft patches released today, indexed by severity. Windows enterprise administrators would do well to keep an eye on [askwoody.com](http://www.askwoody.com), which often has the scoop on any patches causing problems.

It’s getting harder to buy Windows software that isn’t also bundled with Microsoft’s flagship Copilot artificial intelligence (AI) feature. Last month Microsoft started bundling Copilot with **Microsoft Office 365**, which Redmond has since rebranded as “**Microsoft 365 Copilot**.” Ostensibly to offset the costs of its substantial AI investments, Microsoft also jacked up prices from 22 percent to 30 percent for upcoming license renewals and new subscribers.

Office-watch.com [writes](https://office-watch.com/2025/microsoft-365-classic/) that existing Office 365 users who are paying an annual cloud license do have the option of “Microsoft 365 Classic,” an AI-free subscription at a lower price, but that many customers are not offered the option until they attempt to cancel their existing Office subscription.

In other security patch news, **Apple** has shipped iOS 18.3.1, which fixes a [zero day](https://support.apple.com/en-us/122174) vulnerability (CVE-2025-24200) that is showing up in attacks.

**Adobe** has issued security updates that fix a total of 45 vulnerabilities across **InDesign**, **Commerce**, **Substance 3D** **Stager**, **InCopy**, **Illustrator**, **Substance 3D Designer** and **Photoshop Elements**.

**Chris Goettl** at **Ivanti** notes that **Google Chrome** is shipping an update today which will trigger updates for Chromium based browsers including **Microsoft Edge**, so be on the lookout for Chrome and Edge updates as we proceed through the week.

*This entry was posted on Tuesday 11th of February 2025 11:58 PM*

[Other](https://krebsonsecurity.com/category/other/) [Time to Patch](https://krebsonsecurity.com/category/patches/)

[Adam Barnett](https://krebsonsecurity.com/tag/adam-barnett/) [adobe](https://krebsonsecurity.com/tag/adobe/) [apple](https://krebsonsecurity.com/tag/apple/) [CVE-2024-38193](https://krebsonsecurity.com/tag/cve-2024-38193/) [CVE-2025-21377](https://krebsonsecurity.com/tag/cve-2025-21377/) [CVE-2025-21391](https://krebsonsecurity.com/tag/cve-2025-21391/) [CVE-2025-21418](https://krebsonsecurity.com/tag/cve-2025-21418/) [Google Chrome](https://krebsonsecurity.com/tag/google-chrome/) [Microsoft 365 Copilot](https://krebsonsecurity.com/tag/microsoft-365-copilot/) [Microsoft Patch Tuesday February 2025](https://krebsonsecurity.com/tag/microsoft-patch-tuesday-february-2025/) [Rapid7](https://krebsonsecurity.com/tag/rapid7/) [sans internet storm center](https://krebsonsecurity.com/tag/sans-internet-storm-center/) [Satnam Narang](https://krebsonsecurity.com/tag/satnam-narang/) [Tenable](https://krebsonsecurity.com/tag/tenable/)

Post navigation

[← Teen on Musk’s DOGE Team Graduated from ‘The Com’](https://krebsonsecurity.com/2025/02/teen-on-musks-doge-team-graduated-from-the-com/)
[Nearly a Year Later, Mozilla is Still Promoting OneRep →](https://krebsonsecurity.com/2025/02/nearly-a-year-later-mozilla-is-still-promoting-onerep/)

## 19 thoughts on “Microsoft Patch Tuesday, February 2025 Edition”

1. Josh [February 12, 2025](https://krebsonsecurity.com/2025/02/microsoft-patch-tuesday-february-2025-edition/#comment-621992)

   you forgot about DC strong cert enforcement:

   <https://support.microsoft.com/en-us/topic/kb5014754-certificate-based-authentication-changes-on-windows-domain-controllers-ad2c23b0-15d8-4340-a468-4d4f3b188f16#bkmk_certmap>

   if organizations have not taken action, authentication could be broken. even though the KB is old, February 2025 is when MS flips the switch: “domain controllers will move to Full Enforcement mode when the February 2025 Windows security update is installed. Authentication will be...
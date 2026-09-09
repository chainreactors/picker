---
title: Microsoft Plugs Nearly 1,000 Security Holes
url: https://krebsonsecurity.com/2026/09/microsoft-plugs-nearly-1000-security-holes/
source: Over Security
date: 2026-09-08
fetch_date: 2026-09-09T06:56:32.194461
---

# Microsoft Plugs Nearly 1,000 Security Holes

Advertisement

[![](/b-gartner/15.png)](https://www.gartner.com/en/conferences/na/symposium-us/conference-resources/security?utm_medium=display&utm_campaign=EVT_NA_2026_SYM36_PD_BN1_CYBERINSIGHTS&utm_term=krebs)

Advertisement

[![](/b-flashpoint/6.png)](https://flashpoint.io/ignite/?utm_source=krebsonsecurity&utm_medium=display&utm_campaign=brand-ignite&utm_content=noise-a)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Microsoft Plugs Nearly 1,000 Security Holes

September 8, 2026

[5 Comments](https://krebsonsecurity.com/2026/09/microsoft-plugs-nearly-1000-security-holes/#comments)

**Microsoft Corp.** today issued updates to plug at least 974 security holes in its **Windows** operating systems and other software, by far its biggest single patch batch ever. Microsoft says artificial intelligence is helping to speed the discovery of vulnerabilities, but security experts warn that many organizations already are struggling to prioritize the more human-intensive endeavor of testing and deploying so many fixes each month.

![](https://krebsonsecurity.com/wp-content/uploads/2026/09/shutterstock_278764853.jpg)

Image: Shutterstock.com, Kirill Makarov.

This month’s patch bundle obliterates the software giant’s [previous record set in July](https://krebsonsecurity.com/2026/07/microsoft-patches-a-record-570-security-flaws/), when it released updates for at least 570 security vulnerabilities. September’s Patch Tuesday brings this year’s total to more than 2,600, more than twice Microsoft’s previous record-setting patch year in 2020 (1,245) and with three more months to go.

There are two “zero-day” flaws fixed this month that are being actively exploited: both [CVE-2026-81963](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2026-81963) and [CVE-2026-85880](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2026-85880) allow an attacker to elevate their privileges on Windows system.

Fully 113 of the bugs addressed today earned Microsoft’s “critical” rating, meaning they could be abused by malware or miscreants to seize control over a vulnerable Windows machine with little or no help from the user.

Among the more serious critical flaws this month is [CVE-2026-69730](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2026-69730), a DNS weakness present in Windows Server 2012 onward and on Windows 10. Microsoft warns that an unauthenticated attacker could leverage this weakness simply by sending a specially crafted packet to an affected system, and that it is likely to be exploited.

Also scary is [CVE-2026-69829](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2026-69829), a critical, remote code execution flaw in the Windows Shell. This vulnerability has a CVSS base score of 9.8 (10 is the most severe), and can be exploited with low attack complexity, no privileges, and no user interaction.

![](https://krebsonsecurity.com/wp-content/uploads/2026/09/msrc-sug-sept2026.png)

Microsoft’s summary of the security updates released today. Image: msrc.microsoft.com.

Microsoft is hardly alone in shipping monster patch bundles lately. Many other large software companies, including Adobe, Cisco, Google, Mozilla and Oracle, all have recently credited AI-assisted research with increasing their patch cadence and volume (Google said today it is now going to ship security updates every two weeks).

**Tyler Reguly**, associate director of security research and development at **Fortra**, said one core challenge with deploying Windows updates is that they need to be tested before being installed across an organization because not all third-party software works seamlessly in the face of changes to the underlying operating system.

“It’s time to put our CISOs and CSOs on notice,” Reguly said. “How are you helping your teams through these difficult times? Do you have your teams deploy after hours and on weekends to avoid disruption to the business environment? Do you reward them for that effort? Time to dig into your budget and buy dinner for your teams that are working on Saturday to get patches rolled out before users return to work on Monday.”

**Satnam Narang** is senior staff research engineer at **Tenable**. Narang said it’s important to recognize that while the number of vulnerabilities being patched by Microsoft is rising, the number of flaws that can and will affect most organizations remains quite low.

“AI-assisted vulnerability discovery in 2026 is creating larger haystacks, but it isn’t finding more needles,” he said. “It’s critical that organizations understand which vulnerabilities actually apply to them, whether they pose a threat by being reachable and exploitable, and prioritize remediation based on this risk context.”

Of course, regular Windows users don’t need to test patches before deploying them, but they still need to open Windows Update periodically or else assent to the program’s nag notices about pending updates. And at the rate these Windows patch releases are ballooning in size, it’s probably best not to let them pile up month after month.

Enterprise Windows admins will want to keep an eye on [askwoody.com](https://www.askwoody.com/2026/september-2026-windows-updates-are-released/) for news of any updates that appear to be causing problems. As always, the **SANS Internet Storm Center** has [a per-patch breakdown](https://isc.sans.edu/diary/September%202026%20Microsoft%20Patch%20Tuesday/33320) ordered by severity and urgency.

*This entry was posted on Tuesday 8th of September 2026 05:44 PM*

[Latest Warnings](https://krebsonsecurity.com/category/latest-warnings/) [Security Tools](https://krebsonsecurity.com/category/security-tools/) [Time to Patch](https://krebsonsecurity.com/category/patches/)

[CVE-2026-69730](https://krebsonsecurity.com/tag/cve-2026-69730/) [CVE-2026-69829](https://krebsonsecurity.com/tag/cve-2026-69829/) [CVE-2026-81963](https://krebsonsecurity.com/tag/cve-2026-81963/) [CVE-2026-85880](https://krebsonsecurity.com/tag/cve-2026-85880/) [Fortra](https://krebsonsecurity.com/tag/fortra/) [Microsoft Patch Tuesday September 2026](https://krebsonsecurity.com/tag/microsoft-patch-tuesday-september-2026/) [Satnam Narang](https://krebsonsecurity.com/tag/satnam-narang/) [Tenable](https://krebsonsecurity.com/tag/tenable/) [Tyler Reguly](https://krebsonsecurity.com/tag/tyler-reguly/)

Post navigation

[← FBI Probes Service Selling 153M+ Drivers Licenses](https://krebsonsecurity.com/2026/09/fbi-probes-service-selling-153m-drivers-licenses/)

## 5 thoughts on “Microsoft Plugs Nearly 1,000 Security Holes”

1. Artem [September 8, 2026](https://krebsonsecurity.com/2026/09/microsoft-plugs-nearly-1000-security-holes/#comment-660429)

   We need to know how many of ’em were discovered using AI.

   [Reply](https://krebsonsecurity.com/2026/09/microsoft-plugs-nearly-1000-security-holes/?replytocom=660429#respond) →
2. Bob [September 8, 2026](https://krebsonsecurity.com/2026/09/microsoft-plugs-nearly-1000-security-holes/#comment-660433)

   Windows has more bugs than it has features

   [Reply](https://krebsonsecurity.com/2026/09/microsoft-plugs-nearly-1000-security-holes/?replytocom=660433#respond) →

   1. Jojo [September 8, 2026](https://krebsonsecurity.com/2026/09/microsoft-plugs-nearly-1000-security-holes/#comment-660438)

      A lot of heads should be rolling at Microsoft!

      [Reply](https://krebsonsecurity.com/2026/09/microsoft-plugs-nearly-1000-security-holes/?replytocom=660438#respond) →
3. Jojo [September 8, 2026](https://krebsonsecurity.com/2026/09/microsoft-plugs-nearly-1000-security-holes/#comment-660436)

   I wonder how many of these bugs were previously known and used by NSA, CIA and other w...
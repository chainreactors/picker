---
title: Microsoft Patch Tuesday, September 2025 Edition
url: https://krebsonsecurity.com/2025/09/microsoft-patch-tuesday-september-2025-edition/
source: Over Security - Cybersecurity news aggregator
date: 2025-09-10
fetch_date: 2025-10-02T19:54:50.486669
---

# Microsoft Patch Tuesday, September 2025 Edition

Advertisement

[![](/b-gartner/3.jpg)](https://www.gartner.com/en/conferences/na/identity-access-management-us?utm_source=krebs&utm_medium=banner&utm_campaign=EVT_NA_2025_IAM20_PP_MP6_KREBSONSECURITY)

Advertisement

[![](/b-sysdig/2.png)](https://content.foleon.com/sysdig/sysdig-cloud-defense-report-2025/?utm_source=krebs-on-security&utm_medium=display&utm_campaign=aware_amer_the-right-way_na_ung_display&utm_content=AD000462_1240x160)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Microsoft Patch Tuesday, September 2025 Edition

September 9, 2025

[5 Comments](https://krebsonsecurity.com/2025/09/microsoft-patch-tuesday-september-2025-edition/#comments)

**Microsoft Corp.** today issued security updates to fix more than 80 vulnerabilities in its **Windows** operating systems and software. There are no known “zero-day” or actively exploited vulnerabilities in this month’s bundle from Redmond, which nevertheless includes patches for 13 flaws that earned Microsoft’s most-dire “critical” label. Meanwhile, both **Apple** and **Google** recently released updates to fix zero-day bugs in their devices.

![](https://krebsonsecurity.com/wp-content/uploads/2022/07/winupdatedate.png)

Microsoft assigns security flaws a “critical” rating when malware or miscreants can exploit them to gain remote access to a Windows system with little or no help from users. Among the more concerning critical bugs quashed this month is [CVE-2025-54918](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2025-54918). The problem here resides with **Windows NTLM**, or NT LAN Manager, a suite of code for managing authentication in a Windows network environment.

Redmond rates this flaw as “Exploitation More Likely,” and although it is listed as a privilege escalation vulnerability, **Kev Breen** at **Immersive** says this one is actually exploitable over the network or the Internet.

“From Microsoft’s limited description, it appears that if an attacker is able to send specially crafted packets over the network to the target device, they would have the ability to gain SYSTEM-level privileges on the target machine,” Breen said. “The patch notes for this vulnerability state that ‘Improper authentication in Windows NTLM allows an authorized attacker to elevate privileges over a network,’ suggesting an attacker may already need to have access to the NTLM hash or the user’s credentials.”

Breen said another patch — [CVE-2025-55234](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2025-55234), a 8.8 CVSS-scored flaw affecting the **Windows SMB** client for sharing files across a network — also is listed as privilege escalation bug but is likewise remotely exploitable. This vulnerability was publicly disclosed prior to this month.

“Microsoft says that an attacker with network access would be able to perform a replay attack against a target host, which could result in the attacker gaining additional privileges, which could lead to code execution,” Breen noted.

[CVE-2025-54916](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2025-54916) is an “important” vulnerability in **Windows NTFS** — the default filesystem for all modern versions of Windows — that can lead to remote code execution. Microsoft likewise thinks we are more than likely to see exploitation of this bug soon: The last time Microsoft patched an NTFS bug was in March 2025 and it was already being exploited in the wild as a zero-day.

“While the title of the CVE says ‘Remote Code Execution,’ this exploit is not remotely exploitable over the network, but instead needs an attacker to either have the ability to run code on the host or to convince a user to run a file that would trigger the exploit,” Breen said. “This is commonly seen in social engineering attacks, where they send the user a file to open as an attachment or a link to a file to download and run.”

Critical and remote code execution bugs tend to steal all the limelight, but **Tenable** Senior Staff Research Engineer **Satnam Narang** notes that nearly half of all vulnerabilities fixed by Microsoft this month are privilege escalation flaws that require an attacker to have gained access to a target system first before attempting to elevate privileges.

“For the third time this year, Microsoft patched more elevation of privilege vulnerabilities than remote code execution flaws,” Narang observed.

On Sept. 3, Google [fixed two flaws](https://www.bleepingcomputer.com/news/security/google-fixes-actively-exploited-android-flaws-in-september-update/) that were detected as exploited in zero-day attacks, including CVE-2025-38352, an elevation of privilege in the Android kernel, and CVE-2025-48543, also an elevation of privilege problem in the Android Runtime component.

Also, Apple recently patched its seventh zero-day (CVE-2025-43300) of this year. It was part of [an exploit chain](https://techcrunch.com/2025/08/29/whatsapp-fixes-zero-click-bug-used-to-hack-apple-users-with-spyware/) used along with a vulnerability in the **WhatsApp** (CVE-2025-55177) instant messenger to hack Apple devices. Amnesty International [reports](https://x.com/DonnchaC/status/1961444710620303653) that the two zero-days have been used in “an advanced spyware campaign” over the past 90 days. The issue is fixed in iOS 18.6.2, iPadOS 18.6.2, iPadOS 17.7.10, macOS Sequoia 15.6.1, macOS Sonoma 14.7.8, and macOS Ventura 13.7.8.

The **SANS Internet Storm Center** has a [clickable breakdown](https://isc.sans.edu/forums/diary/Microsoft%20Patch%20Tuesday%20September%202025/32270/) of each individual fix from Microsoft, indexed by severity and CVSS score. Enterprise Windows admins involved in testing patches before rolling them out should keep an eye on [askwoody.com](https://www.askwoody.com/2025/september-2025-updates-are-out/), which often has the skinny on wonky updates.

AskWoody also reminds us that we’re now just two months out from Microsoft discontinuing free security updates for Windows 10 computers. For those interested in safely extending the lifespan and usefulness of these older machines, check out [last month’s Patch Tuesday coverage](https://krebsonsecurity.com/2025/08/microsoft-patch-tuesday-august-2025-edition/) for a few pointers.

As ever, please don’t neglect to back up your data (if not your entire system) at regular intervals, and feel free to sound off in the comments if you experience problems installing any of these fixes.

*This entry was posted on Tuesday 9th of September 2025 05:21 PM*

[Latest Warnings](https://krebsonsecurity.com/category/latest-warnings/) [The Coming Storm](https://krebsonsecurity.com/category/comingstorm/) [Time to Patch](https://krebsonsecurity.com/category/patches/)

[apple](https://krebsonsecurity.com/tag/apple/) [CVE-2025-38352](https://krebsonsecurity.com/tag/cve-2025-38352/) [CVE-2025-48543](https://krebsonsecurity.com/tag/cve-2025-48543/) [CVE-2025-54916](https://krebsonsecurity.com/tag/cve-2025-54916/) [CVE-2025-54918](https://krebsonsecurity.com/tag/cve-2025-54918/) [CVE-2025-55177](https://krebsonsecurity.com/tag/cve-2025-55177/) [CVE-2025-55234](https://krebsonsecurity.com/tag/cve-2025-55234/) [google](https://krebsonsecurity.com/tag/google/) [Immersive](https://krebsonsecurity.com/tag/immersive/) [Kev Breen](https://krebsonsecurity.com/tag/kev-breen/) [microsoft](https://krebsonsecurity.com/tag/microsoft/) [NT LAN Manager](https://krebsonsecurity.com/tag/nt-lan-manager/) [sans internet storm center](https://krebsonsecurity.com/tag/sans-internet-storm-center/) [Satnam Narang](https://krebsonsecurity.com/tag/satnam-narang/) [Tenable](https://krebsonsecurity.com/tag/tenable/) [WhatsApp](https://krebsonsecurity.com/tag/whats...
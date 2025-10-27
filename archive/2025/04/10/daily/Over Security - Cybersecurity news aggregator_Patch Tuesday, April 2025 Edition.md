---
title: Patch Tuesday, April 2025 Edition
url: https://krebsonsecurity.com/2025/04/patch-tuesday-april-2025-edition/
source: Over Security - Cybersecurity news aggregator
date: 2025-04-10
fetch_date: 2025-10-06T22:07:30.426283
---

# Patch Tuesday, April 2025 Edition

Advertisement

[![](/b-gartner/3.jpg)](https://www.gartner.com/en/conferences/na/identity-access-management-us?utm_source=krebs&utm_medium=banner&utm_campaign=EVT_NA_2025_IAM20_PP_MP6_KREBSONSECURITY)

Advertisement

[![](/b-ninjio/7.png)](https://ninjio.com/lp46d-krebs/)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Patch Tuesday, April 2025 Edition

April 8, 2025

[7 Comments](https://krebsonsecurity.com/2025/04/patch-tuesday-april-2025-edition/#comments)

**Microsoft** today released updates to plug at least 121 security holes in its **Windows** operating systems and software, including one vulnerability that is already being exploited in the wild. Eleven of those flaws earned Microsoft’s most-dire “critical” rating, meaning malware or malcontents could exploit them with little to no interaction from Windows users.

![](https://krebsonsecurity.com/wp-content/uploads/2021/07/windupate.png)

The zero-day flaw already seeing exploitation is [CVE-2025-29824](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2025-29824), a local elevation of privilege bug in the Windows **Common Log File System** (CLFS) driver.  Microsoft rates it as “important,” but as **Chris Goettl** from **Ivanti** points out, risk-based prioritization warrants treating it as critical.

This CLFS component of Windows is no stranger to Patch Tuesday: According to Tenable’s **Satnam Narang**, since 2022 Microsoft has patched 32 CLFS vulnerabilities — averaging 10 per year — with six of them exploited in the wild. The [last CLFS zero-day](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2024-49138) was [patched in December 2024](https://krebsonsecurity.com/2024/12/patch-tuesday-december-2024-edition/).

Narang notes that while flaws allowing attackers to install arbitrary code are consistently top overall Patch Tuesday features, the data is reversed for zero-day exploitation.

“For the past two years, elevation of privilege flaws have led the pack and, so far in 2025, account for over half of all zero-days exploited,” Narang wrote.

Rapid7’s **Adam Barnett** warns that any Windows defenders responsible for an [LDAP server](https://en.wikipedia.org/wiki/Lightweight_Directory_Access_Protocol) — which means almost any organization with a non-trivial Microsoft footprint — should add patching for the critical flaw [CVE-2025-26663](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2025-26663) to their to-do list.

“With no privileges required, no need for user interaction, and code execution presumably in the context of the LDAP server itself, successful exploitation would be an attractive shortcut to any attacker,” Barnett said. “Anyone wondering if today is a re-run of December 2024 Patch Tuesday can take some small solace in the fact that the worst of the [trio of LDAP critical RCEs published at the end of last year](https://www.rapid7.com/blog/post/2024/12/10/patch-tuesday-december-2024/#ldap-critical-rce) was likely easier to exploit than today’s example, since today’s CVE-2025-26663 requires that an attacker win a race condition. Despite that, Microsoft still expects that exploitation is more likely.”

Among the critical updates Microsoft patched this month are remote code execution flaws in **Windows Remote Desktop** services (RDP), including [CVE-2025-26671](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2025-26671), [CVE-2025-27480](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2025-27480) and [CVE-2025-27482](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2025-27482); only the latter two are rated “critical,” and Microsoft marked both of them as “Exploitation More Likely.”

Perhaps the most widespread vulnerabilities fixed this month were in web browsers. **Google Chrome** [updated](https://chromereleases.googleblog.com/) to fix 13 flaws this week, and **Mozilla Firefox** fixed [eight bugs](https://www.mozilla.org/en-US/security/advisories/mfsa2025-20/), with possibly more updates coming later this week for **Microsoft** **Edge**.

As it tends to do on Patch Tuesdays, **Adobe** has [released 12 updates](https://helpx.adobe.com/security/security-bulletin.html) resolving 54 security holes across a range of products, including **ColdFusion**, **Adobe Commerce**, **Experience Manager Forms**, **After Effects**, **Media Encoder**, **Bridge**, **Premiere Pro**, **Photoshop**, **Animate**, **AEM Screens**, and **FrameMaker**.

**Apple** users may need to patch as well. On March 31, Apple released a huge security update (more than three gigabytes in size) to fix issues in a range of their products, including [at least one zero-day flaw](https://www.bleepingcomputer.com/news/security/apple-backports-zero-day-patches-to-older-iphones-and-macs/).

And in case you missed it, on March 31, 2025 **Apple** released [a rather large batch of security updates](https://support.apple.com/en-us/100100?is=1ef7934f6635b02395adcab09a0c1b24bf0ea745b648bfe87189de8aadc7300b) for a wide range of their products, from **macOS** to the **iOS** operating systems on **iPhones** and **iPads**.

Earlier today, Microsoft included a note saying **Windows 10** security updates weren’t available but would be released as soon as possible. It appears from browsing [askwoody.com](https://www.askwoody.com/2025/april-2025-updates-out/) that this snafu has since been rectified. Either way, if you run into complications applying any of these updates please leave a note about it in the comments below, because the chances are good that someone else had the same problem.

As ever, please consider backing up your data and or devices prior to updating, which makes it far less complicated to undo a software update gone awry. For more granular details on today’s Patch Tuesday, check out the [SANS Internet Storm Center’s roundup](https://isc.sans.edu/forums/diary/Microsoft%20April%202025%20Patch%20Tuesday/31838/). Microsoft’s update guide for April 2025 [is here](https://msrc.microsoft.com/update-guide/releaseNote/2025-Apr).

For more details on Patch Tuesday, check out the write-ups from [Action1](https://www.action1.com/patch-tuesday/patch-tuesday-april-2025/?vyj) and [Automox](https://www.automox.com/blog/patch-tuesday-april-2025).

*This entry was posted on Tuesday 8th of April 2025 11:09 PM*

[Latest Warnings](https://krebsonsecurity.com/category/latest-warnings/) [Security Tools](https://krebsonsecurity.com/category/security-tools/) [The Coming Storm](https://krebsonsecurity.com/category/comingstorm/) [Time to Patch](https://krebsonsecurity.com/category/patches/)

[Chris Goettl](https://krebsonsecurity.com/tag/chris-goettl/) [CLFS](https://krebsonsecurity.com/tag/clfs/) [Common Log File System](https://krebsonsecurity.com/tag/common-log-file-system/) [CVE-2025-26671](https://krebsonsecurity.com/tag/cve-2025-26671/) [CVE-2025-27480](https://krebsonsecurity.com/tag/cve-2025-27480/) [CVE-2025-27482](https://krebsonsecurity.com/tag/cve-2025-27482/) [CVE-2025-29824](https://krebsonsecurity.com/tag/cve-2025-29824/) [Ivanti](https://krebsonsecurity.com/tag/ivanti/) [microsoft](https://krebsonsecurity.com/tag/microsoft/) [Satnam Narang](https://krebsonsecurity.com/tag/satnam-narang/) [windows](https://krebsonsecurity.com/tag/windows/) [Windows Remote Desktop Services](https://krebsonsecurity.com/tag/windows-remote-desktop-services/)

Post navigation

[← Cyber Forensic Expert in 2,000+ Cases Faces FBI Probe](https://krebsonsecurity.com/2025/04/cyber-forensic-expert-in-2000-cases-faces-fbi-probe/)
[China-based SMS Phishing Triad Pivots to Banks →](https://krebsonsecurity.com/2025/04/china-based-sms-phishing-triad-pivots-to-banks/)

## 7 thoughts on “Patch Tuesday, April...
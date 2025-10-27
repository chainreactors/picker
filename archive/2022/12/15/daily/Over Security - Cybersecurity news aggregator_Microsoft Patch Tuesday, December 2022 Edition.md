---
title: Microsoft Patch Tuesday, December 2022 Edition
url: https://krebsonsecurity.com/2022/12/microsoft-patch-tuesday-december-2022-edition/
source: Over Security - Cybersecurity news aggregator
date: 2022-12-15
fetch_date: 2025-10-04T01:33:27.821209
---

# Microsoft Patch Tuesday, December 2022 Edition

Advertisement

[![](/b-sysdig/1.png)](https://content.foleon.com/sysdig/sysdig-cloud-defense-report-2025/?utm_source=krebs-on-security&utm_medium=display&utm_campaign=aware_amer_the-right-way_na_ung_display&utm_content=AD000460_1240x110)

Advertisement

[![](/b-ninjio/7.png)](https://ninjio.com/lp46d-krebs/)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Microsoft Patch Tuesday, December 2022 Edition

December 14, 2022

[7 Comments](https://krebsonsecurity.com/2022/12/microsoft-patch-tuesday-december-2022-edition/#comments)

**Microsoft** has released its final monthly batch of security updates for 2022, fixing more than four dozen security holes in its various **Windows** operating systems and related software. The most pressing patches include a zero-day in a Windows feature that tries to flag malicious files from the Web, a critical bug in **PowerShell**, and a dangerous flaw in **Windows 11** systems that was detailed publicly prior to this week’s Patch Tuesday.

![](https://krebsonsecurity.com/wp-content/uploads/2021/07/windupate.png)

The security updates include patches for **Azure**, **Microsoft Edge,** **Office**, **SharePoint Server**, **SysInternals**, and the **.NET framework**. Six of the update bundles earned Microsoft’s most dire “critical” rating, meaning they fix vulnerabilities that malware or malcontents can use to remotely commandeer an unpatched Windows system — with little to no interaction on the part of the user.

The bug already seeing exploitation is [CVE-2022-44698](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-44698), which allows attackers to bypass the Windows SmartScreen security feature. The vulnerability allows attackers to craft documents that won’t get tagged with Microsoft’s “Mark of the Web,” despite being downloaded from untrusted sites.

“This means no Protected View for Microsoft Office documents, making it easier to get users to do sketchy things like execute malicious macros, said **Greg Wiseman**, product manager at security firm **Rapid7**. This is the second Mark of the Web flaw Microsoft has patched in as many months; both were first publicly detailed over the past two months [on Twitter by security researcher Will Dormann](https://twitter.com/wdormann/status/1602727668344053767).

Publicly disclosed (but not actively exploited for now) is [CVE-2022-44710](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-44710), which is an elevation of privilege flaw in the DirectX graphics component of Windows 11.

Another notable critical bug is [CVE-2022-41076](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-41076), a remote code execution flaw in PowerShell — a key component of Windows that makes it easier to automate system tasks and configurations.

**Kevin Breen** at **Immersive Labs** said while Microsoft doesn’t share much detail about CVE-2022-41076 apart from the designation ‘Exploitation More Likely,’ they also note that successful exploitation requires an attacker to take additional actions to prepare the target environment.

“What actions are required is not clear; however, we do know that exploitation requires an authenticated user level of access,” Breen said. “This combination suggests that the exploit requires a social engineering element, and would likely be seen in initial infections using attacks like MalDocs or LNK files.”

Speaking of malicious documents, **Trend Micro’s Zero Day Initiative** highlights [CVE-2022-44713](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-44713), a spoofing vulnerability in **Outlook for Mac**.

“We don’t often highlight spoofing bugs, but anytime you’re dealing with a spoofing bug in an e-mail client, you should take notice,” ZDI’s **Dustin Childs** wrote. “This vulnerability could allow an attacker to appear as a trusted user when they should not be. Now combine this with the SmartScreen Mark of the Web bypass and it’s not hard to come up with a scenario where you receive an e-mail that appears to be from your boss with an attachment entitled “Executive\_Compensation.xlsx”. There aren’t many who wouldn’t open that file in that scenario.”

Microsoft also [released guidance](https://msrc.microsoft.com/update-guide/vulnerability/ADV220005) on reports that certain software drivers certified by Microsoft’s Windows Hardware Developer Program were being used maliciously in post-exploitation activity.

Three different companies reported evidence that malicious hackers were using these signed malicious driver files to lay the groundwork for ransomware deployment inside victim organizations. One of those companies, **Sophos**, published [a blog post Tuesday](https://news.sophos.com/en-us/2022/12/13/signed-driver-malware-moves-up-the-software-trust-chain/) detailing how the activity was tied to the [Russian ransomware group **Cuba**](https://www.cisa.gov/uscert/ncas/alerts/aa22-335a), which has extorted an estimated $60 million from victims since 2019.

Of course, not all scary and pressing security threats are Microsoft-based. Also on Tuesday, **Apple** released a bevy of security updates to iOS, iPadOS, macOS, tvOS and Safari, including  a patch for a [newly discovered zero-day vulnerability](https://thehackernews.com/2022/12/new-actively-exploited-zero-day.html) that could lead to remote code execution.

Anyone responsible for maintaining **Fortinet** or **Citrix** remote access products probably needs to update, as both are dealing with [active attacks](https://media.defense.gov/2022/Dec/13/2003131586/-1/-1/0/CSA-APT5-CITRIXADC-V1.PDF) on [just-patched flaws](https://www.bleepingcomputer.com/news/security/fortinet-says-ssl-vpn-pre-auth-rce-bug-is-exploited-in-attacks/).

For a closer look at the patches released by Microsoft today (indexed by severity and other metrics) check out the [always-useful Patch Tuesday roundup](https://isc.sans.edu/forums/diary/Microsoft%20December%202022%20Patch%20Tuesday/29336/) from the **SANS Internet Storm Center**. And it’s not a bad idea to hold off updating for a few days until Microsoft works out any kinks in the updates: [AskWoody.com](https://www.askwoody.com/) usually has the lowdown on any patches that may be causing problems for Windows users.

As always, please consider backing up your system or at least your important documents and data before applying system updates. And if you run into any problems with these updates, please drop a note about it here in the comments.

*This entry was posted on Wednesday 14th of December 2022 12:01 PM*

[Latest Warnings](https://krebsonsecurity.com/category/latest-warnings/) [Security Tools](https://krebsonsecurity.com/category/security-tools/) [Time to Patch](https://krebsonsecurity.com/category/patches/)

[Apple zero-day](https://krebsonsecurity.com/tag/apple-zero-day/) [CVE-2022-41076](https://krebsonsecurity.com/tag/cve-2022-41076/) [CVE-2022-44698](https://krebsonsecurity.com/tag/cve-2022-44698/) [CVE-2022-44710](https://krebsonsecurity.com/tag/cve-2022-44710/) [CVE-2022-44713](https://krebsonsecurity.com/tag/cve-2022-44713/) [Greg Wiseman](https://krebsonsecurity.com/tag/greg-wiseman/) [Immersive Labs](https://krebsonsecurity.com/tag/immersive-labs/) [Kevin Breen](https://krebsonsecurity.com/tag/kevin-breen/) [Microsoft Patch Tuesday December 2022](https://krebsonsecurity.com/tag/microsoft-patch-tuesday-december-2022/) [PowerShell](https://krebsonsecurity.com/tag/powershell/) [Rapid7](https://krebsonsecurity.com/tag/rapid7/) [sophos](https://krebsonsecurity.com/tag/sophos/) [Trend Micro's Zero Day Initiative](https://krebsonsecurity.com/tag/trend-micros-zero-day-initiative/) [Will Dormann](https://krebsonsecurity.com/tag/will-do...
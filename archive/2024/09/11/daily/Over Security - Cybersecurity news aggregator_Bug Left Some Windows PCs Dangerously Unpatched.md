---
title: Bug Left Some Windows PCs Dangerously Unpatched
url: https://krebsonsecurity.com/2024/09/bug-left-some-windows-pcs-dangerously-unpatched/
source: Over Security - Cybersecurity news aggregator
date: 2024-09-11
fetch_date: 2025-10-06T18:32:07.670800
---

# Bug Left Some Windows PCs Dangerously Unpatched

Advertisement

[![](/b-gartner/3.jpg)](https://www.gartner.com/en/conferences/na/identity-access-management-us?utm_source=krebs&utm_medium=banner&utm_campaign=EVT_NA_2025_IAM20_PP_MP6_KREBSONSECURITY)

Advertisement

[![](/b-knowbe4/37.jpg)](https://www.knowbe4.com/resources/kits/cybersecurity-awareness-month?utm_source=Krebs&utm_medium=display&utm_campaign=cybersecurityawarenessmonth&utm_content=hrm+)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Bug Left Some Windows PCs Dangerously Unpatched

September 10, 2024

[28 Comments](https://krebsonsecurity.com/2024/09/bug-left-some-windows-pcs-dangerously-unpatched/#comments)

**Microsoft Corp.** today released updates to fix at least 79 security vulnerabilities in its **Windows** operating systems and related software, including multiple flaws that are already showing up in active attacks. Microsoft also corrected a critical bug that has caused some **Windows 10** PCs to remain dangerously unpatched against actively exploited vulnerabilities for several months this year.

![](https://krebsonsecurity.com/wp-content/uploads/2022/07/winupdatedate.png)

By far the most curious security weakness Microsoft disclosed today has the snappy name of [CVE-2024-43491](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-43491), which Microsoft says is a vulnerability that led to the rolling back of fixes for some vulnerabilities affecting “optional components” on certain Windows 10 systems produced in 2015. Those include Windows 10 systems that installed the monthly security update for Windows released in March 2024, or other updates released until August 2024.

**Satnam Narang**, senior staff research engineer at **Tenable**, said that while the phrase “exploitation detected” in a Microsoft advisory normally implies the flaw is being exploited by cybercriminals, it appears labeled this way with CVE-2024-43491 because the rollback of fixes reintroduced vulnerabilities that were previously know to be exploited.

“To correct this issue, users need to apply both the September 2024 Servicing Stack Update and the September 2024 Windows Security Updates,” Narang said.

**Kev Breen**, senior director of threat research at **Immersive Labs**, said the root cause of CVE-2024-43491 is that on specific versions of Windows 10, the build version numbers that are checked by the update service were not properly handled in the code.

“The [notes from Microsoft](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-43491) say that the ‘build version numbers crossed into a range that triggered a code defect’,” Breen said. “The short version is that some versions of Windows 10 with optional components enabled was left in a vulnerable state.”

Zero Day #1 this month is [CVE-2024-38226](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-38226), and it concerns a weakness in **Microsoft Publisher**, a standalone application included in some versions of **Microsoft Office**. This flaw lets attackers bypass Microsoft’s “**Mark of the Web**,” a Windows security feature that marks files downloaded from the Internet as potentially unsafe.

Zero Day #2 is [CVE-2024-38217](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-38217), also a Mark of the Web bypass affecting Office. Both zero-day flaws rely on the target opening a booby-trapped Office file.

Security firm **Rapid7** notes that CVE-2024-38217 has been publicly disclosed via [an extensive write-up](https://www.elastic.co/security-labs/dismantling-smart-app-control), with exploit code also available on GitHub.

According to Microsoft, [CVE-2024-38014](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-38014), an “elevation of privilege” bug in the Windows Installer, is also being actively exploited.

June’s coverage of Microsoft Patch Tuesday was titled “[Recall Edition](https://krebsonsecurity.com/2024/06/patch-tuesday-june-2024-recall-edition/),” because the big news then was that Microsoft was facing a torrent of criticism from privacy and security experts over “**Recall**,” a new artificial intelligence (AI) feature of Redmond’s flagship Copilot+ PCs that constantly takes screenshots of whatever users are doing on their computers.

At the time, Microsoft responded by suggesting Recall would no longer be enabled by default. But last week, the software giant clarified that [what it really meant](https://www.theverge.com/2024/9/2/24233992/microsoft-recall-windows-11-uninstall-feature-bug) was that the ability to disable Recall was a bug/feature in the preview version of Copilot+ that will not be available to Windows customers going forward. Translation: New versions of Windows are shipping with Recall deeply embedded in the operating system.

It’s pretty rich that Microsoft, which already collects an insane amount of information from its customers on a near constant basis, is calling the Recall removal feature a bug, while treating Recall as a desirable feature. Because from where I sit, Recall is a feature nobody asked for that turns Windows into a bug (of the surveillance variety).

When Redmond first responded to critics about Recall, they noted that Recall snapshots never leave the user’s system, and that even if attackers managed to hack a Copilot+ PC they would not be able to exfiltrate on-device Recall data.

But that claim rang hollow after former Microsoft threat analyst **Kevin Beaumont** [detailed on his blog](https://doublepulsar.com/recall-stealing-everything-youve-ever-typed-or-viewed-on-your-own-windows-pc-is-now-possible-da3e12e9465e) how any user on the system (even a non-administrator) can export Recall data, which is just stored in an SQLite database locally.

As it is apt to do on Microsoft Patch Tuesday, Adobe has [released updates](https://helpx.adobe.com/security.html) to fix security vulnerabilities in a range of products, including **Reader** and **Acrobat**, **After Effects**, **Premiere Pro**, **Illustrator**, **ColdFusion**, **Adobe Audition**, and **Photoshop**. Adobe says it is not aware of any exploits in the wild for any of the issues addressed in its updates.

Seeking a more detailed breakdown of the patches released by Microsoft today? Check out the SANS Internet Storm Center’s [thorough list](https://isc.sans.edu/forums/diary/Microsoft%2BSeptember%2B2024%2BPatch%2BTuesday/31254/). People responsible for administering many systems in an enterprise environment would do well to keep an eye on [AskWoody.com](https://www.askwoody.com), which often has the skinny on any wonky Windows patches that may be causing problems for some users.

As always, if you experience any issues applying this month’s patch batch, consider dropping a note in the comments here about it.

*This entry was posted on Tuesday 10th of September 2024 05:46 PM*

[Time to Patch](https://krebsonsecurity.com/category/patches/)

[CVE-2024-38217](https://krebsonsecurity.com/tag/cve-2024-38217/) [CVE-2024-38226](https://krebsonsecurity.com/tag/cve-2024-38226/) [CVE-2024-43491](https://krebsonsecurity.com/tag/cve-2024-43491/) [Immersive Labs](https://krebsonsecurity.com/tag/immersive-labs/) [Kev Breen](https://krebsonsecurity.com/tag/kev-breen/) [mark of the web](https://krebsonsecurity.com/tag/mark-of-the-web/) [microsoft](https://krebsonsecurity.com/tag/microsoft/) [Microsoft Office](https://krebsonsecurity.com/tag/microsoft-office/) [Patch Tuesday September 2024](https://krebsonsecurity.com/tag/patch-tuesday-september-2024/) [Rapid7](https://krebsonsecurity.com/tag/rapid7/) [Satnam Narang](https://krebsonsecurity.com/tag/satnam-narang/)

Post navigation

[← Sextortion Scams Now Include Photos of Your Home](https://krebsonsecurity....
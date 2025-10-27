---
title: Microsoft Patch Tuesday, January 2023 Edition
url: https://krebsonsecurity.com/2023/01/microsoft-patch-tuesday-january-2023-edition/
source: Krebs on Security
date: 2023-01-11
fetch_date: 2025-10-04T03:35:34.237974
---

# Microsoft Patch Tuesday, January 2023 Edition

Advertisement

[![](/b-gartner/7.jpg)](https://www.gartner.com/en/conferences/na/identity-access-management-us?utm_source=krebs&utm_medium=banner&utm_campaign=EVT_NA_2025_IAM20_PP_MP6_KREBSONSECURITY)

Advertisement

[![](/b-gartner/8.jpg)](https://www.gartner.com/en/conferences/na/identity-access-management-us?utm_source=krebs&utm_medium=banner&utm_campaign=EVT_NA_2025_IAM20_PP_MP6_KREBSONSECURITY)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Microsoft Patch Tuesday, January 2023 Edition

January 10, 2023

[28 Comments](https://krebsonsecurity.com/2023/01/microsoft-patch-tuesday-january-2023-edition/#comments)

**Microsoft** today released updates to fix nearly 100 security flaws in its **Windows** operating systems and other software. Highlights from the first **Patch Tuesday** of 2023 include a zero-day vulnerability in Windows, printer software flaws reported by the **U.S. National Security Agency**, and a critical **Microsoft SharePoint Server** bug that allows a remote, unauthenticated attacker to make an anonymous connection.

![](https://krebsonsecurity.com/wp-content/uploads/2022/07/winupdatedate.png)

At least 11 of the patches released today are rated “Critical” by Microsoft, meaning they could be exploited by malware or malcontents to seize remote control over vulnerable Windows systems with little or no help from users.

Of particular concern for organizations running **Microsoft SharePoint Server** is [CVE-2023-21743](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-21743). This is a Critical security bypass flaw that could allow a remote, unauthenticated attacker to make an anonymous connection to a vulnerable SharePoint server. Microsoft says this flaw is “more likely to be exploited” at some point.

But patching this bug may not be as simple as deploying Microsoft updates. **Dustin Childs**, head of threat awareness at **Trend Micro’s Zero Day Initiative**, said sysadmins need to take additional measures to be fully protected from this vulnerability.

“To fully resolve this bug, you must also trigger a SharePoint upgrade action that’s also included in this update,” Childs said. “Full details on how to do this are in the bulletin. Situations like this are why people who scream ‘Just patch it!’ show they have never actually had to patch an enterprise in the real world.”

Eighty-seven of the vulnerabilities earned Redmond’s slightly less dire “Important” severity rating. That designation describes vulnerabilities “whose exploitation could result in compromise of the confidentiality, integrity, or availability of user data, or of the integrity or availability of processing resources.”

Among the more Important bugs this month is [CVE-2023-21674](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-21674), which is an “elevation of privilege” weakness in most supported versions of Windows that has already been abused in active attacks.

**Satnam Narang**, senior staff research engineer at **Tenable**, said although details about the flaw were not available at the time Microsoft published its advisory on Patch Tuesday, it appears this was likely chained together with a vulnerability in a Chromium-based browser such as Google Chrome or Microsoft Edge in order to break out of a browser’s sandbox and gain full system access.

“Vulnerabilities like CVE-2023-21674 are typically the work of advanced persistent threat (APT) groups as part of targeted attacks,” Narang said. “The likelihood of future widespread exploitation of an exploit chain like this is limited due to auto-update functionality used to patch browsers.”

By the way, when was the last time you completely closed out your Web browser and restarted it? Some browsers will automatically download and install new security updates, but the protection from those updates usually only happens after you restart the browser.

Speaking of APT groups, the U.S. National Security Agency is credited with reporting [CVE-2023-21678](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-21678), which is another “important” vulnerability in the Windows Print Spooler software.

There have been so many vulnerabilities patched in Microsoft’s printing software over the past year (including the dastardly [PrintNightmare attacks and borked patches](https://krebsonsecurity.com/2021/07/microsoft-issues-emergency-patch-for-windows-flaw/)) that KrebsOnSecurity has joked about Patch Tuesday reports being sponsored by Print Spooler. Tenable’s Narang points out that this is the third Print Spooler flaw the NSA has reported in the last year.

**Kevin Breen** at **Immersive Labs** called special attention to [CVE-2023-21563](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-21563), which is a security feature bypass in **BitLocker**, the data and disk encryption technology built into enterprise versions of Windows.

“For organizations that have remote users, or users that travel, this vulnerability may be of interest,” Breen said. “We rely on BitLocker and full-disk encryption tools to keep our files and data safe in the event a laptop or device is stolen. While information is light, this appears to suggest that it could be possible for an attacker to bypass this protection and gain access to the underlying operating system and its contents. If security teams are not able to apply this patch, one potential mitigation could be to ensure Remote Device Management is deployed with the ability to remotely disable and wipe assets.”

There are also two **Microsoft Exchange** vulnerabilities patched this month — [CVE-2023-21762](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-21762) and [CVE-2023-21745](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-21745). Given the rapidity with which threat actors exploit new Exchange bugs to steal corporate email and infiltrate vulnerable systems, organizations using Exchange should patch immediately. Microsoft’s advisory says these Exchange flaws are indeed “more likely to be exploited.”

**Adobe** released four patches addressing 29 flaws in **Adobe Acrobat** and **Reader**, **InDesign**, **InCopy**, and **Adobe Dimension**. The update for Reader fixes 15 bugs with eight of these being ranked Critical in severity (allowing arbitrary code execution if an affected system opened a specially crafted file).

For a more granular rundown on the updates released today, see [the SANS Internet Storm Center roundup](https://isc.sans.edu/forums/diary/Microsoft%20January%202023%20Patch%20Tuesday/29420/). Nearly 100 updates is a lot, and there are bound to be a few patches that cause problems for organizations and end users. When that happens, [AskWoody.com](https://www.askwoody.com/2023/batten-down-the-hatches-for-january-updates/) usually has the lowdown.

Please consider backing up your data and/or imaging your system before applying any updates. And please sound off in the comments if you experience any problems as a result of these patches.

*This entry was posted on Tuesday 10th of January 2023 05:28 PM*

[Latest Warnings](https://krebsonsecurity.com/category/latest-warnings/) [Security Tools](https://krebsonsecurity.com/category/security-tools/) [Time to Patch](https://krebsonsecurity.com/category/patches/)

[CVE-2023-21563](https://krebsonsecurity.com/tag/cve-2023-21563/) [CVE-2023-21674](https://krebsonsecurity.com/tag/cve-2023-21674/) [CVE-2023-21678](https://krebsonsecurity.com/tag/cve-2023-21678/) [CVE-2023-21743](https://krebsonsecurity.com/tag/cve-2023-21743/) [CVE-2023-21745](https://krebsonsecurity.com/tag/cve-2023-21745/) [CVE-2023-21762](https://krebsonsecurity.com/tag/cve-2023-21762/) [Dustin Childs]...
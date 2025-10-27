---
title: Patch Tuesday, June 2025 Edition
url: https://krebsonsecurity.com/2025/06/patch-tuesday-june-2025-edition/
source: Over Security - Cybersecurity news aggregator
date: 2025-06-12
fetch_date: 2025-10-06T22:55:59.172976
---

# Patch Tuesday, June 2025 Edition

Advertisement

[![](/b-action1/1.jpg)](https://action1.com/double-endpoints-free-cam2025/?utm_source=paidmedia&refid=Display_CAM_Krebs)

Advertisement

[![](/b-gartner/8.jpg)](https://www.gartner.com/en/conferences/na/identity-access-management-us?utm_source=krebs&utm_medium=banner&utm_campaign=EVT_NA_2025_IAM20_PP_MP6_KREBSONSECURITY)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Patch Tuesday, June 2025 Edition

June 10, 2025

[4 Comments](https://krebsonsecurity.com/2025/06/patch-tuesday-june-2025-edition/#comments)

**Microsoft** today released security updates to fix at least 67 vulnerabilities in its **Windows** operating systems and software. Redmond warns that one of the flaws is already under active attack, and that software blueprints showing how to exploit a pervasive Windows bug patched this month are now public.

![](https://krebsonsecurity.com/wp-content/uploads/2021/07/windupate.png)

The sole zero-day flaw this month is [CVE-2025-33053](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2025-33053), a remote code execution flaw in the Windows implementation of **WebDAV** — an HTTP extension that lets users remotely manage files and directories on a server. While WebDAV isn’t enabled by default in Windows, its presence in legacy or specialized systems still makes it a relevant target, said **Seth Hoyt**, senior security engineer at **Automox**.

**Adam Barnett**, lead software engineer at **Rapid7**, said Microsoft’s advisory for CVE-2025-33053 does not mention that the Windows implementation of WebDAV is listed as deprecated since November 2023, which in practical terms means that the WebClient service no longer starts by default.

“The advisory also has attack complexity as low, which means that exploitation does not require preparation of the target environment in any way that is beyond the attacker’s control,” Barnett said. “Exploitation relies on the user clicking a malicious link. It’s not clear how an asset would be immediately vulnerable if the service isn’t running, but all versions of Windows receive a patch, including those released since the deprecation of WebClient, like Server 2025 and Windows 11 24H2.”

Microsoft warns that an “elevation of privilege” vulnerability in the **Windows Server Message Block** (SMB) client ([CVE-2025-33073](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2025-33073)) is likely to be exploited, given that proof-of-concept code for this bug is now public. CVE-2025-33073 has a CVSS risk score of 8.8 (out of 10), and exploitation of the flaw leads to the attacker gaining “SYSTEM” level control over a vulnerable PC.

“What makes this especially dangerous is that no further user interaction is required after the initial connection—something attackers can often trigger without the user realizing it,” said **Alex Vovk**, co-founder and CEO of **Action1**. “Given the high privilege level and ease of exploitation, this flaw poses a significant risk to Windows environments. The scope of affected systems is extensive, as SMB is a core Windows protocol used for file and printer sharing and inter-process communication.”

Beyond these highlights, 10 of the vulnerabilities fixed this month were rated “critical” by Microsoft, including eight remote code execution flaws.

Notably absent from this month’s patch batch is a fix for a newly discovered weakness in **Windows Server 2025** that allows attackers to act with the privileges of any user in Active Directory. The bug, dubbed “**BadSuccessor**,” was [publicly disclosed](https://github.com/akamai/BadSuccessor) by researchers at **Akamai** on May 21, and several public proof-of-concepts are now available. Tenable’s Satnam Narang said organizations that have at least one Windows Server 2025 domain controller should review permissions for principals and limit those permissions as much as possible.

**Adobe** has released updates for **Acrobat Reader** and six other products addressing at least 259 vulnerabilities, most of them in an update for **Experience Manager**. **Mozilla Firefox** and **Google Chrome** both recently released security updates that require a restart of the browser to take effect. The latest Chrome update fixes two zero-day exploits in the browser (CVE-2025-5419 and CVE-2025-4664).

For a detailed breakdown on the individual security updates released by Microsoft today, check out the [Patch Tuesday roundup](https://isc.sans.edu/diary/Microsoft%20Patch%20Tuesday%20June%202025/32032) from the **SANS Internet Storm Center**. Action 1 has [a breakdown of patches from Microsoft](https://www.action1.com/patch-tuesday/patch-tuesday-june-2025/?vyj) and a raft of other software vendors releasing fixes this month. As always, please back up your system and/or data before patching, and feel free to drop a note in the comments if you run into any problems applying these updates.

*This entry was posted on Tuesday 10th of June 2025 08:10 PM*

[Security Tools](https://krebsonsecurity.com/category/security-tools/) [Time to Patch](https://krebsonsecurity.com/category/patches/)

[Acrobat Reader](https://krebsonsecurity.com/tag/acrobat-reader/) [Action1](https://krebsonsecurity.com/tag/action1/) [Adam Barnett](https://krebsonsecurity.com/tag/adam-barnett/) [Akamai](https://krebsonsecurity.com/tag/akamai/) [Alex Vovk](https://krebsonsecurity.com/tag/alex-vovk/) [Automox](https://krebsonsecurity.com/tag/automox/) [BadSuccessor](https://krebsonsecurity.com/tag/badsuccessor/) [CVE-2025-33053](https://krebsonsecurity.com/tag/cve-2025-33053/) [CVE-2025-33073](https://krebsonsecurity.com/tag/cve-2025-33073/) [Experience Manager](https://krebsonsecurity.com/tag/experience-manager/) [Google Chrome](https://krebsonsecurity.com/tag/google-chrome/) [mozilla firefox](https://krebsonsecurity.com/tag/mozilla-firefox/) [Patch Tuesday June 2025](https://krebsonsecurity.com/tag/patch-tuesday-june-2025/) [Rapid7](https://krebsonsecurity.com/tag/rapid7/) [sans internet storm center](https://krebsonsecurity.com/tag/sans-internet-storm-center/) [Seth Hoyt](https://krebsonsecurity.com/tag/seth-hoyt/) [WebDAV](https://krebsonsecurity.com/tag/webdav/) [Windows Server Message Block](https://krebsonsecurity.com/tag/windows-server-message-block/)

Post navigation

[← Proxy Services Feast on Ukraine’s IP Address Exodus](https://krebsonsecurity.com/2025/06/proxy-services-feast-on-ukraines-ip-address-exodus/)
[Inside a Dark Adtech Empire Fed by Fake CAPTCHAs →](https://krebsonsecurity.com/2025/06/inside-a-dark-adtech-empire-fed-by-fake-captchas/)

## 4 thoughts on “Patch Tuesday, June 2025 Edition”

1. Secret Squirrel [June 10, 2025](https://krebsonsecurity.com/2025/06/patch-tuesday-june-2025-edition/#comment-627199)

   Thanks Brian.

   KB5060842 failed to install on one of my PCs. According to windowslatest.com, there is an issue and some users may need to wait for a revised version of KB5060842.
2. odot2 [June 11, 2025](https://krebsonsecurity.com/2025/06/patch-tuesday-june-2025-edition/#comment-627220)

   I had the same issue as Squirrel. Failed to install on my HP zBook Workstation.
3. PJ [June 14, 2025](https://krebsonsecurity.com/2025/06/patch-tuesday-june-2025-edition/#comment-627364)

   Is there an Adobe updater that updates all Adobe software at once, or do you have to do it one software title at a time?

   1. Jason [June 24, 2025](https://krebsonsecurity.com/2025/06/patch-tuesday-june-2025-edition/#comment-627651)

      You can do it through the creative cloud app. It should do all software at once.

Comments are closed.

Advertisement

[![](/b-knowbe4/38.jpg)](https://www.knowbe4.com/resources/kits/cybersecurity-awareness-month?utm_source=Krebs&utm_me...
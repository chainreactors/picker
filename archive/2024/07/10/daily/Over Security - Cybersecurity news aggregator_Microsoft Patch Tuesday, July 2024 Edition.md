---
title: Microsoft Patch Tuesday, July 2024 Edition
url: https://krebsonsecurity.com/2024/07/microsoft-patch-tuesday-july-2024-edition/
source: Over Security - Cybersecurity news aggregator
date: 2024-07-10
fetch_date: 2025-10-06T17:46:53.659262
---

# Microsoft Patch Tuesday, July 2024 Edition

Advertisement

[![](/b-knowbe4/40.png)](https://gateway.on24.com/wcc/eh/1815783/human-risk-management-summit?partnerref=krebs)

Advertisement

[![](/b-gartner/4.jpg)](https://www.gartner.com/en/conferences/na/identity-access-management-us?utm_source=krebs&utm_medium=banner&utm_campaign=EVT_NA_2025_IAM20_PP_MP6_KREBSONSECURITY)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Microsoft Patch Tuesday, July 2024 Edition

July 9, 2024

[24 Comments](https://krebsonsecurity.com/2024/07/microsoft-patch-tuesday-july-2024-edition/#comments)

**Microsoft Corp.** today issued software updates to plug at least 139 security holes in various flavors of **Windows** and other Microsoft products. Redmond says attackers are already exploiting at least two of the vulnerabilities in active attacks against Windows users.

![](https://krebsonsecurity.com/wp-content/uploads/2022/07/winupdatedate.png)

The first Microsoft zero-day this month is [CVE-2024-38080](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2024-38080), a bug in the **Windows Hyper-V** component that affects **Windows 11** and **Windows Server 2022** systems. CVE-2024-38080 allows an attacker to increase their account privileges on a Windows machine. Although Microsoft says this flaw is being exploited, it has offered scant details about its exploitation.

The other zero-day is [CVE-2024-38112](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2024-38112), which is a weakness in **MSHTML**, the proprietary engine of Microsoft’s **Internet Explorer** web browser. **Kevin Breen**, senior director of threat research at **Immersive Labs**, said exploitation of CVE-2024-38112 likely requires the use of an “attack chain” of exploits or programmatic changes on the target host, a la Microsoft’s description: “Successful exploitation of this vulnerability requires an attacker to take additional actions prior to exploitation to prepare the target environment.”

“Despite the lack of details given in the initial advisory, this vulnerability affects all hosts from **Windows Server 2008 R2** onwards, including clients,” Breen said. “Due to active exploitation in the wild this one should be prioritized for patching.”

**Satnam Narang**, senior staff research engineer at **Tenable**, called special attention to [CVE-2024-38021](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2024-38021), a remote code execution flaw in **Microsoft Office**. Attacks on this weakness would lead to the disclosure of NTLM hashes, which could be leveraged as part of an NTLM relay or “pass the hash” attack, which lets an attacker masquerade as a legitimate user without ever having to log in.

“One of the more successful attack campaigns from 2023 used CVE-2023-23397, an elevation of privilege bug in Microsoft Outlook that could also leak NTLM hashes,” Narang said. “However, CVE-2024-38021 is limited by the fact that the Preview Pane is not an attack vector, which means that exploitation would not occur just by simply previewing the file.”

The security firm **Morphisec**, credited with reporting CVE-2024-38021 to Microsoft, said it respectfully disagrees with Microsoft’s “important” severity rating, arguing the Office flaw deserves a more dire “critical” rating given how easy it is for attackers to exploit.

“Their assessment differentiates between trusted and untrusted senders, noting that while the vulnerability is zero-click for trusted senders, it requires one click user interaction for untrusted senders,” Morphisec’s **Michael Gorelik** said in [a blog post about their discovery](https://blog.morphisec.com/cve-2024-38021-microsoft-outlook-moniker-rce-vulnerability). “This reassessment is crucial to reflect the true risk and ensure adequate attention and resources are allocated for mitigation.”

In last month’s Patch Tuesday, Microsoft fixed a flaw in its Windows WiFi driver that attackers could use to install malicious software just by sending a vulnerable Windows host a specially crafted data packet over a local network. **Jason Kikta** at **Automox** said this month’s CVE-2024-38053 — a security weakness in **Windows Layer Two Bridge Network** — is another local network “ping-of-death” vulnerability that should be a priority for road warriors to patch.

“This requires close access to a target,” Kikta said. “While that precludes a ransomware actor in Russia, it is something that is outside of most current threat models. This type of exploit works in places like shared office environments, hotels, convention centers, and anywhere else where unknown computers might be using the same physical link as you.”

Automox also highlighted three vulnerabilities in Windows Remote Desktop a service that allocates Client Access Licenses (CALs) when a client connects to a remote desktop host ([CVE-2024-38077](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2024-38077), [CVE-2024-38074](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2024-38074), and [CVE-2024-38076](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2024-38076)). All three bugs have been assigned a CVSS score of 9.8 (out of 10) and indicate that a malicious packet could trigger the vulnerability.

**Tyler Reguly** at **Fortra** noted that today marks the End of Support date for **SQL Server 2014**, a platform that according to Shodan still has ~110,000 instances publicly available. On top of that, more than a quarter of all vulnerabilities Microsoft fixed this month are in SQL server.

“A lot of companies don’t update quickly, but this may leave them scrambling to update those environments to supported versions of MS-SQL,” Reguly said.

It’s a good idea for Windows end-users to stay current with security updates from Microsoft, which can quickly pile up otherwise. That doesn’t mean you have to install them on Patch Tuesday. Indeed, waiting a day or three before updating is a sane response, given that sometimes updates go awry and usually within a few days Microsoft has fixed any issues with its patches. It’s also smart to back up your data and/or image your Windows drive before applying new updates.

For a more detailed breakdown of the individual flaws addressed by Microsoft today, check out the [SANS Internet Storm Center’s list](https://isc.sans.edu/diary/Microsoft%20Patch%20Tuesday%20July%202024/31058). For those admins responsible for maintaining larger Windows environments, it often pays to keep an eye on [Askwoody.com](https://www.askwoody.com/), which frequently points out when specific Microsoft updates are creating problems for a number of users.

As ever, if you experience any problems applying any of these updates, consider dropping a note about it in the comments; chances are decent someone else reading here has experienced the same issue, and maybe even has a solution.

*This entry was posted on Tuesday 9th of July 2024 03:50 PM*

[Time to Patch](https://krebsonsecurity.com/category/patches/)

[AskWoody.com](https://krebsonsecurity.com/tag/askwoody-com/) [Automox](https://krebsonsecurity.com/tag/automox/) [CVE-2024-38021](https://krebsonsecurity.com/tag/cve-2024-38021/) [CVE-2024-38074](https://krebsonsecurity.com/tag/cve-2024-38074/) [CVE-2024-38076](https://krebsonsecurity.com/tag/cve-2024-38076/) [CVE-2024-38077](https://krebsonsecurity.com/tag/cve-2024-38077/) [CVE-2024-38080](https://krebsonsecurity.com/tag/cve-2024-38080/) [CVE-2024-38112](https://krebsonsecurity.com/tag/cve-2024-38112/) [Fortra](https://krebsonsecurity.com/tag/fortra/) [Immersive Labs](https://krebsonsecurity.com/tag/immersive-labs/) [Jason Kikta](https://krebsonsecurity.com/tag/jason-kikta/) [Kevin Breen](https://krebsonsecurity.com/tag...
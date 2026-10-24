---
title: BlackX UEFI Bootkit Bypasses Secure Boot on Patched Windows Systems Missing Revocations
url: https://thehackernews.com/2026/10/blackx-uefi-bootkit-bypasses-secure.html
source: The Hacker News
date: 2026-10-23
fetch_date: 2026-10-24T06:48:21.327663
---

# BlackX UEFI Bootkit Bypasses Secure Boot on Patched Windows Systems Missing Revocations

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgpv5Y6QePil1MjgPiKuj9qVcOEzN1QdpjV55lFLD7Nyll1Wy1-rDkPzUxoUxZBjyhD74ycWms55yNl3nOcVfzpirEVdQnc0bfulwnXhfb5IAO5oii05bR8bzttfawsmnOSBqpuNre7TO6eDyDJn4FhPAsISdesN9Nsfq-7UgOE6XMHMH5tSwffhl-qhK9h/s728-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/ai-threat-guide-d)

# [BlackX UEFI Bootkit Bypasses Secure Boot on Patched Windows Systems Missing Revocations](https://thehackernews.com/2026/10/blackx-uefi-bootkit-bypasses-secure.html)

**Ravie Lakshmanan**Oct 23, 2026Malware / Cyber Espionage

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj0cTK7D5hQFR-3qGTicTlfi6_CbnMIgCJWIojDeXmZr91hrIPqhhxZ72mAsnB6kBOcCdscZOL_VN8RhAdYIxq3d128rkaDweIApSaV5w3IzB1YGN3XNnlarG0IKN5VuDJy_RnPBxXZoKQ1Yh950YFNz-b_pbvEY_QlQa5Tr-BP4366UgkGIg968J-QEN1M/s1700-nu-rw-lo-l85-e365/uefi.jpg)

Diplomatic organizations in Central Asia have been targeted by a sophisticated new Unified Extensible Firmware Interface (UEFI) bootkit called **BlackX**.

The activity, which singled out diplomatic entities in Tajikistan, Uzbekistan, and Turkmenistan in early 2026, is suspected to be orchestrated by a China-linked state-sponsored hacking group known as [APT41](https://thehackernews.com/2026/03/apt41-linked-silver-dragon-targets.html), Kaspersky said in a [technical report](https://securelist.com/uefi-bootkit-blackx/121539/) published this week.

The primary objective behind deploying the malware is to undermine Microsoft Windows startup defenses, along with third-party security solutions, while maintaining long-term, covert access to compromised devices.

Notably, BlackX is assessed to be an updated version of [BlackLotus](https://thehackernews.com/2023/03/blacklotus-becomes-first-uefi-bootkit.html), a notorious bootkit that was first observed being advertised on cybercrime forums in late 2022, before its existence was officially confirmed by ESET in March 2023.

[BlackLotus](https://thehackernews.com/2023/06/nsa-releases-guide-to-combat-powerful.html) is designed to exploit a now-patched Secure Boot bypass vulnerability tracked as [CVE-2022-21894](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2022-21894) (CVSS score: 4.4), also known as Baton Drop, to load malicious code before the operating system starts. However, successful exploitation hinges on an attacker having administrator privileges or physical access to a target host.

"It is critical to note that a threat actor's use of this bootkit is primarily a persistence and defense evasion mechanism," Microsoft [noted](https://www.microsoft.com/en-us/security/blog/2023/04/11/guidance-for-investigating-attacks-using-cve-2022-21894-the-blacklotus-campaign/) at the time. "It is not a first-stage payload or an initial access vector and can only be deployed to a device to which a threat actor has already gained either privileged access or physical access."

That said, completely addressing the threat requires additional actions beyond installing the latest update, including [running manual steps](https://techcommunity.microsoft.com/blog/windows-itpro-blog/revoking-vulnerable-windows-boot-managers/4121735) to apply Microsoft's Secure Boot revocation mitigations, such as [adding](https://support.microsoft.com/en-us/servicing/os/windows/2023/03/how-to-manage-the-windows-boot-manager-revocations-for-secure-boot-changes-associated-with-cve-2023) the "Windows Production PCA 2011" certificate to the Secure Boot UEFI Forbidden List (DBX).

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-governance-platform-d)

The Russian cybersecurity company has found that attackers are capitalizing on the fact that organizations have not carried out these manual steps, enabling them to still use the Baton Drop vulnerability even on systems that have the "patch" applied.

"On October 19, 2026, this certificate expired, but this does not prevent the vulnerable binaries from loading unless the certificate is blocklisted," researchers Georgy Kucherin, Vladimir Nestor, and Vasily Berdnikov said.

"It is likely that the threat actor behind this campaign took into account that few organizations realized the importance of manually activating the Baton Drop patch. As such, we believe they decided to invest time in understanding how BlackLotus works and creating a copycat of this bootkit."

Attackers have been observed deploying BlackX after breaching victim networks through an unspecified method and gaining administrator privileges. To install the bootkit, the threat actor drops the following files -

* inst.exe, an installer executable
* PVMDIJGKAX2, an encrypted extensionless file containing files and strings required for the installation

The installer is then launched via the command line as "C:\ProgramData\Intel\inst.exe PVMDIJGKAX2 Q46F6MDLI3RX2KV1," where "Q46F6MDLI3RX2KV1" is the RC4 key used for decryption.

The binary then drops additional files to both system and UEFI partitions to exploit CVE-2022-21894 in a manner that's "remarkably similar" to the one used in BlackLotus. The end goal remains the same: install Machine Owner Keys (MOK) to load arbitrary EFI files on the infected hosts and interfere with Secure Boot.

What's interesting here is that the source code of BlackLotus has never entered the public domain, indicating that the threat actors behind BlackX either reverse-engineered the original bootkit or purchased its source code from another party.

"Either way, this is an interesting observation, as we rarely see APT actors borrow ideas or code from cybercrime actors," Kaspersky said.

The UEFI payload delivered following the exploitation of the vulnerability is engineered to inject a malicious driver into the Windows kernel. The driver has been signed with a certificate belonging to a company named Wenjiang District Mingyu Network Technology Service Studio. The certificate has since been revoked by the issuer.

Like in the case of the bring your own vulnerable driver ([BYOVD](https://thehackernews.com/2026/03/54-edr-killers-use-byovd-to-exploit-34.html)) attack, the driver attempts to tamper with the functioning of endpoint security software installed on the machine. In an interesting twist, some of the unauthorized modifications are allowed to run only if security programs asso...
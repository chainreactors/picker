---
title: Bee-Ware of Trigona, An Emerging Ransomware Strain
url: https://buaq.net/go-153763.html
source: unSafe.sh - 不安全
date: 2023-03-17
fetch_date: 2025-10-04T09:49:47.544999
---

# Bee-Ware of Trigona, An Emerging Ransomware Strain

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/1a47c34e4e6b98d1239ef4d21f47c64b.jpg)

Bee-Ware of Trigona, An Emerging Ransomware Strain

This post is also available i
*2023-3-16 21:0:56
Author: [unit42.paloaltonetworks.com(查看原文)](/jump-153763.htm)
阅读量:57
收藏*

---

![A pictorial representation of ransomware like Trigona. It shows an exchange of money for keys in front of a laptop screen.](https://unit42.paloaltonetworks.com/wp-content/uploads/2023/03/Ransomware-r3d1.png)

This post is also available in:
[日本語 (Japanese)](https://unit42.paloaltonetworks.jp/trigona-ransomware-update/)

## Executive Summary

Trigona ransomware is a relatively new strain that security researchers first discovered in late October 2022. By analyzing Trigona ransomware binaries and ransom notes obtained from VirusTotal, as well as information from Unit 42 incident response, we determined that Trigona was very active during December 2022, with at least 15 potential victims being compromised. Affected organizations are in the manufacturing, finance, construction, agriculture, marketing and high technology industries.

Unit 42 researchers identified two new Trigona ransom notes in January 2023 and two in February 2023. Trigona’s ransom notes are unique; rather than the usual text file, they are instead presented in an HTML Application with embedded JavaScript containing unique computer IDs (CID) and victim IDs (VID).

Palo Alto Networks helps detect and prevent Trigona ransomware with the following products and services: [Cortex XDR](https://docs-cortex.paloaltonetworks.com/p/XDR), [Prisma Cloud](https://docs.paloaltonetworks.com/prisma/prisma-cloud) and [Next-Generation Firewalls](https://docs.paloaltonetworks.com/ngfw) (including cloud-delivered security subscriptions such as [WildFire](https://docs.paloaltonetworks.com/wildfire)) and through [incident response](https://start.paloaltonetworks.com/contact-unit42.html).

| **Related Unit 42 Topics** | [**Ransomware**](https://unit42.paloaltonetworks.com/category/ransomware/)**,** [**Ransomware Threat Report**](https://unit42.paloaltonetworks.com/tag/ransomware-threat-report/), [**CryLock**](https://unit42.paloaltonetworks.com/tag/crylock/) |
| --- | --- |

[Trigona Overview](#post-127253-_ny2qloj26cvd)

## Trigona Overview

The first mention of Trigona, also the name of a family of stingless bees, comes from [a tweet by security researchers](https://twitter.com/malwrhunterteam/status/1587581807595249666) in late October 2022. Malware samples were passed to BleepingComputer, which in turn published [a blog post on the ransomware](https://www.bleepingcomputer.com/news/security/trigona-ransomware-spotted-in-increasing-attacks-worldwide/) on Nov. 29, 2022. Unit 42 consultants also have seen Trigona firsthand in the course of incident response.

Unit 42 researchers have observed Trigona’s threat operator engaging in behavior such as obtaining initial access to a target’s environment, conducting reconnaissance, transferring malware via remote monitoring and management (RMM) software, creating new user accounts and deploying ransomware.

## Ransomware Analysis

### Ransomware Binary

Unit 42 obtained and analyzed a sample of the Trigona ransomware binary, named svhost.exe. Upon execution, the ransomware binary uses TDCP\_rijndael (a Delphi AES library) to encrypt files. The ransomware then appends the .\_locked file extension, modifies registry keys to maintain persistence, and drops ransom notes.

The ransomware binary supports the following command line arguments:

|  |  |
| --- | --- |
| **Argument** | **Description** |
| /full | Performs all functions of the ransomware. Encrypts both local and network files. Creates two registry keys for persistence, one for the ransomware binary and another for the ransom note. |
| /!autorun | Skips creation of registry keys for persistence |
| /test\_cid “test” | Overwrites default victim generated CID and replace with “test” value |
| /test\_vid “test” | Overwrites default VID and replace with “test” value |
| /p, /path “path” | Encrypts only files contained within specified path |
| /!local | Does not encrypt local system files, only encrypts files on local network |
| /!lan | Does not encrypt local network files, only encrypts files on local system |
| /autorun\_only “path” | Creates registry key for persistence only. Allows for optional “path” to be provided to override default path, does not encrypt files |

The ransomware establishes persistence through the creation of two keys in CurrentVersion\Run. Keys found in CurrentVersion\Run contain references to programs that will execute when a user logs in.

One key executes the ransomware binary whenever the user logs in, ensuring that the encryption process would resume upon reboot. The other key ensures that the ransom note is opened every time the user logs in.

### Ransom Note

Trigona’s ransom note is dropped to the system with the name how\_to\_decrypt.hta. The HTML code in this file contains embedded JavaScript functionality, which displays ransom note details as shown below in Figure 1.

![Image 1 is a screenshot of a sample Trigona ransom note that tells a business its network is encrypted, the three steps of instructions for data recovery, and tips to make the price cheaper. There is also a “Need help?” link.](https://unit42.paloaltonetworks.com/wp-content/uploads/2023/03/word-image-127253-1.png)

Figure 1. Sample Trigona ransom note.

Unit 42 researchers observed that the JavaScript within the ransom note contains the following information:

* A uniquely generated CID and VID
* A link to the negotiation Tor portal
* An email address to contact.

The contact email shown below in Figure 2 is [[email protected]](https://unit42.paloaltonetworks.com/cdn-cgi/l/email-protection)[.]org. We have also seen [[email protected]](https://unit42.paloaltonetworks.com/cdn-cgi/l/email-protection)[.]com used as the contact email in other Trigona ransom notes.

![Image 2 is a screenshot of JavaScript code showing the unique computer and victim IDs, which here have been redacted. ](https://unit42.paloaltonetworks.com/wp-content/uploads/2023/03/word-image-127253-2.png)

Figure 2. Embedded JavaScript containing campaign ID and victim ID.

### Victimology

By looking at the victim ID in the embedded JavaScript in the Trigona ransom notes, we were able to identify at least 15 potential victims that were compromised in December 2022. We also identified two new Trigona ransom notes in January 2023 and two in February 2023.

Trigona ransomware has been linked to compromises impacting multiple organizations worldwide, in sectors including manufacturing, finance, construction, agriculture, marketing and high technology. The companies impacted were in the United States, Italy, France, Germany, Australia and New Zealand.

### Leak Site Analysis

When Trigona was first observed, there was no evidence of this group using a leak site for double extortion. Their ransom note pointed the victims to their negotiation portal instead. During the investigation of this ransomware family, we observed that [a researcher identified a leak site attributed to Trigona](https://twitter.com/paul_eubanks/status/1628497550679351303?cxt=HHwWjoCxnZ35ypktAAAA) hosted on the IP address 45.227.253[.]99.

Unit 42 researchers pivoted on the SSH key for 45.227.253[.]99 and identified three other IP addresses related to Trigona’s infrastructure:

* 45.227.253[.]106
* 45.227.253[.]98
* 45.227.253[.]107

Each IP shares the same SSH key of ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBMjqeyIfJyuimtE414TBCxN+lHleN5/P3CNiD4uln5xyHjyw4muLe...
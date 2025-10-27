---
title: From Conti to Akira | Decoding the Latest Linux & ESXi Ransomware Families
url: https://buaq.net/go-175201.html
source: unSafe.sh - 不安全
date: 2023-08-24
fetch_date: 2025-10-04T11:58:54.050040
---

# From Conti to Akira | Decoding the Latest Linux & ESXi Ransomware Families

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

![](https://8aqnet.cdn.bcebos.com/9a14cde5f5ece3cb87f5230df792ca0f.jpg)

From Conti to Akira | Decoding the Latest Linux & ESXi Ransomware Families

The evolution of the ransomware landscape has seen a shift from the more traditional approach invol
*2023-8-23 20:59:44
Author: [www.sentinelone.com(查看原文)](/jump-175201.htm)
阅读量:29
收藏*

---

The [evolution of the ransomware landscape](https://www.sentinelone.com/blog/ransoms-without-ransomware-data-corruption-and-other-new-tactics-in-cyber-extortion/) has seen a shift from the more traditional approach involving Windows payloads to ones targeting other platforms, most notably Linux. In this shift, ransomware operators are shortening the time gaps between different payload releases and bringing feature parity across diverse platforms.

Strategically dipping into code from well known ransomware families such as [Conti](https://www.sentinelone.com/anthology/conti/), [Babuk](https://www.sentinelone.com/anthology/babuk/), or [Lockbit](https://www.sentinelone.com/anthology/lockbit-3-0-lockbit-black/), ransomware operators are reusing and modifying codebases to create novel attack techniques. As more cases of this come to light, it is critical for security teams to stay vigilant and adaptive in their defenses.

In this post, we highlight several recent ransomware families that have unleashed their Linux/ESXi-focused payloads shortly upon launch of their operations. Understanding the capabilities of these payloads is an important step in gauging future risk and key to enabling security teams to prepare their defenses accordingly.

![](https://www.sentinelone.com/wp-content/uploads/2023/08/From-Conti-to-Akira-Decoding-the-Latest-Linux-ESXi-Ransomware-Families-3.jpg)

## The Rise of the Linux Ransomware Threat

Looking back just four or five years, prominent ransomware operators’ primary focus was devices running Windows. Non-Windows flavors of their payloads required extra skill and time to develop and release. Such is not the case now, with languages like Rust and Go allowing for quick multi-platform ports for eager malware developers.

The state of the threat landscape as we see it today includes ransomware operators  releasing payloads for multiple platforms simultaneously. In this approach, there are no longer significant gaps of time between the usual Windows-targeted payloads and the Linux-focused and/or ESXi payloads. In addition, it is now standard for payloads across platforms to exhibit feature parity. Out of the gate, these Linux and ESXi-focused lockers contain all the requisite functionality of their Windows counterparts.

Modern ransomware operators are also increasingly reusing builders and code (sometimes leaked) or modifying codebases to suit their needs while maintaining the primary code as a model. Security researchers note that the primary families from which these have been derived are [Conti](https://www.sentinelone.com/anthology/conti/), [Babuk](https://www.sentinelone.com/anthology/babuk/), [LockBit](https://www.sentinelone.com/anthology/lockbit-3-0-lockbit-black/). These variants are capable of targeting both Linux and VMWare ESXi environments, with the aim of encrypting the virtual machines (VMs) hosted on ESXi servers that are often crucial to business operations and services.

Typically, attackers exploit vulnerabilities in ESXi, weak credentials, or other security vulnerabilities to gain access to the virtualized environment. The ability to efficiently target and encrypt virtual machines is highly attractive to ransomware operators. Fully-virtualized infrastructure can be encrypted and compromised in minutes with the right, and robust, payloads.

## MONTI Locker

MONTI locker has a history going back to mid-2022, with a number of [attacks](https://blogs.blackberry.com/en/2022/09/the-curious-case-of-monti-ransomware-a-real-world-doppelganger) on VMware ESXi servers.

![](https://www.sentinelone.com/wp-content/uploads/2023/08/Linux_Locker_1.jpg)

The most recent versions of MONTI ESXI Ransomware support a variety of command-line arguments, many of which are carryovers from [Conti](https://www.sentinelone.com/anthology/conti/), from which MONTI Locker borrows code. The operators behind MONTI Locker have shown signs of moving in a more bespoke direction as of late, however.

[Researchers recently](https://www.trendmicro.com/en_us/research/23/h/monti-ransomware-unleashes-a-new-encryptor-for-linux.html) documented a sample that appears to shed the old Conti-based encryptor along with a few of the command-line parameters. These more recent samples have removed the `--size`, `--log` and `--vmlist` parameters.

Available command-line parameters for MONTI Locker include:

|  |  |
| --- | --- |
| **Argument** | **Function** |
| — path | Path to file / volumes |
| –whitelist | List of virtual machines to skip (can accept .txt file input) |
| –vmkill | Toggle termination of virtual machines |
| –vmlist | Accepts a list (.txt file) of virtual machine names |
| –detach | Detach from the screen/terminal |
| –log |  |
| –prockiller | Toggles termination of processes with handles open on targeted files (for encryption) |
| –size | Partial file encryption, toggles percentages between 10 and 50 |
| –world-id= | Targeting specific World IDs within VMWare |

![August 2023 MONTI Locker help screen](https://www.sentinelone.com/wp-content/uploads/2023/08/Linux_Locker_7.jpg)

August 2023 MONTI Locker help screen

Also of note is MONTI Locker’s ability to update the MOTD file (Message of the Day) on affected servers. This file (`/etc/motd`) controls what users see upon login to vCenter, for example. Post-infection, servers encrypted with MONTI Locker will display the configured ransom note.

![MOTD and Index.html references in MONTI Locker](https://www.sentinelone.com/wp-content/uploads/2023/08/Linux_Locker_2.jpg)

MOTD and *Index.html* references in MONTI Locker

MONTI Locker’s overall attack volume is lower than some of the other threats in this post. Their targeting is quite selective, and they are adept at playing the long game when it comes to the overall lifespan of their infection campaigns. As we will note with Akira, it will be interesting to see how MONTI Locker evolves outside of Conti as well as how quickly those changes will come to fruition.

## Akira Ransomware

Linux variants of the [Akira ransomware](https://www.sentinelone.com/anthology/akira/) family have been observed since June of 2023 though the broader operations go back to April. Initial delivery of Akira ransomware occurs via exploitation of vulnerable, publicly available, services and applications. The group has also been known to [target](https://arcticwolf.com/resources/blog/conti-and-akira-chained-together/) weaknesses in multi factor authentication (or a lack there-of) . Akira attackers do not discriminate when it comes to victimology. As of this writing, they have targeted educational institutions as well as those in the financial, manufacturing, real estate, and medical industries.

![](https://www.sentinelone.com/wp-content/uploads/2023/08/Linux_Locker_11.jpg)

Traditionally, Akira ransomware payloads are borrowed from [Conti](https://www.sentinelone.com/anthology/conti/). The Linux versions of Akira ransomware use the Crypto++ library to handle encryption on devices. Akira provides a short command set that does not include any options to shutdown VMs prior to encryption. They do, however, allow the attacker some control over speed of encryption and the likelihood of practical recovery by the victim via the `-n` parameter. The greater that value, the more of the file gets encrypted...
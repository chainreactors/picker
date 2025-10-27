---
title: CatB Ransomware | File Locker Sharpens Its Claws to Steal Data with MSDTC Service DLL Hijacking
url: https://buaq.net/go-153245.html
source: unSafe.sh - 不安全
date: 2023-03-14
fetch_date: 2025-10-04T09:28:01.035666
---

# CatB Ransomware | File Locker Sharpens Its Claws to Steal Data with MSDTC Service DLL Hijacking

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

![](https://8aqnet.cdn.bcebos.com/70b3e9ecfa7e5a7b5d02e0fa41289396.jpg)

CatB Ransomware | File Locker Sharpens Its Claws to Steal Data with MSDTC Service DLL Hijacking

The CatB ransomware family, sometimes referred to as CatB99 or Baxtoy, was first observed in late 2
*2023-3-13 21:52:51
Author: [www.sentinelone.com(查看原文)](/jump-153245.htm)
阅读量:39
收藏*

---

The CatB ransomware family, sometimes referred to as CatB99 or Baxtoy, was first observed in late 2022, with campaigns being observed steadily since November. The group’s activities have gained [attention](https://minerva-labs.com/blog/new-catb-ransomware-employs-2-year-old-dll-hijacking-technique-to-evade-detection/) due to their ongoing use of DLL hijacking via Microsoft Distributed Transaction Coordinator (MSDTC) to extract and launch ransomware payloads.

String similarities in the ransom notes as well as modifications left by the ransomware payloads suggest that CatB may be either an evolution or direct rebrand of the Pandora ransomware, which was active in early to mid-2022 and targeted the automotive industry.

In this post, we offer a technical analysis of the CatB ransomware and its abuse of the legitimate MSDTC service, describing its evasion tactics, encryption behavior, and its attempts to steal credentials and browser data.

![](https://www.sentinelone.com/wp-content/uploads/2023/03/CatB-Ransomware-File-Locker-Sharpens-Its-Claws-to-Steal-Data-with-MSDTC-Service-DLL-Hijacking-2.jpg)

## CatB Ransomware Technical Information

CatB payloads are distributed as a two DLL set. A dropper DLL is responsible for initial evasive environmental checks as well as dropping and launching the second DLL, which serves the ransomware payload.

![CatB Ransomware Process Graph](https://www.sentinelone.com/wp-content/uploads/2023/03/CatB_5.jpg)

CatB Ransomware Process Graph

First, the dropper is distributed in the form of a UPX-packed DLL (`versions.dll`). This dropper deposits the second DLL payload (`oci.dll`) onto the target host. The dropper DLL is responsible for any sandbox evasion techniques required by the threat actor. Sandbox evasion inhibits the analysis process and ultimately leads to more time in the target environment for the attacker.

CatB performs three primary checks in an attempt to determine if the payload is being executed within a virtual environment. These are direct checks for type and size of physical RAM, type and size of physical hard disks, and checking for odd or anomalous combinations of processors and cores.

Upon execution, CatB payloads rely on [DLL search order hijacking](https://attack.mitre.org/techniques/T1574/001/) to drop and load the malicious payload. The dropper (`versions.dll`) drops the payload (`oci.dll`) into the System32 directory.

![Oci.dll payloads in System32 (view from Singularity™ Console)](https://www.sentinelone.com/wp-content/uploads/2023/03/CatB_12.jpg)

*Oci.dll* payloads in System32 (view from Singularity™ Console)

The malware then abuses the MSDTC service, manipulating the permissions and startup parameters. As a result, the system will inject the malicious `oci.dll` into the service’s executable (`msdtc.exe`) when the MSDTC service is restarted. `Taskill.exe` is used to terminate the msdtc.exe process once the service configuration changes have been made.

![Msdtc.exe termination syntax](https://www.sentinelone.com/wp-content/uploads/2023/03/CatB_10.jpg)

*Msdtc.exe* termination syntax

CatB ransomware excludes the following files and extensions from the encryption process: `.msi`, `.dll`, `.sys`, `.iso` and `NTUSER.DAT`.

![Encryption exclusions in payload DLL](https://www.sentinelone.com/wp-content/uploads/2023/03/CatB_1.jpg)

Encryption exclusions in payload DLL

In addition to the hardcoded exclusions, the local disk volumes to be encrypted are also configured in a similar manner. By default, the `oci.dll` payload will attempt to encrypt `C:\users` (crawl whole tree), `I:`, `H:`, `G:`, `F:`, `E:`, and `D:`.

![Local encryption targets in oci.dll](https://www.sentinelone.com/wp-content/uploads/2023/03/CatB_11.jpg)

Local encryption targets in *oci.dll*

The lack of post-encryption alterations is a trait that sets CatB apart from other contemporaries. Once encrypted, there is no blatant indicator – no separate ransom note dropped, no change to the desktop wallpaper, and no antagonizing file extensions. Instead, what could be considered the ransom note is inserted into the beginning of each encrypted file.

![Ransom note appended to head of encrypted file (catb991 variation)](https://www.sentinelone.com/wp-content/uploads/2023/03/CatB_4.jpg)

Ransom note appended to head of encrypted file (catb991 variation)

Per the ransom note, the only way to engage the threat actor is via email at the provided catB9991 protonmail address. Beyond that, a single Bitcoin (BTC) address is provided for payment submissions. The ransom price is set to increase each day for five days and, following the fifth day, there will be “permanent data loss” if the victim does not comply.

Based on observations, there is no evidence to indicate that CatB operators are generating payment wallets for each victim as the Bitcoin address provided is not unique to each sample.

![Generation of unique key file](https://www.sentinelone.com/wp-content/uploads/2023/03/CatB_9.jpg)

Generation of unique key file

A key file is deposited onto each infected host in `c:\users\public\`. This file must be included in email correspondence with the attackers as it is, ideally, a unique identifier for each victim or host.

![Key file dropped for each victim](https://www.sentinelone.com/wp-content/uploads/2023/03/CatB_8.jpg)

Key file dropped for each victim

文章来源: https://www.sentinelone.com/blog/decrypting-catb-ransomware-analyzing-their-latest-attack-methods/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)
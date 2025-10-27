---
title: Hypervisor Ransomware | Multiple Threat Actor Groups Hop on Leaked Babuk Code to Build ESXi Lockers
url: https://buaq.net/go-162917.html
source: unSafe.sh - 不安全
date: 2023-05-12
fetch_date: 2025-10-04T11:38:23.101108
---

# Hypervisor Ransomware | Multiple Threat Actor Groups Hop on Leaked Babuk Code to Build ESXi Lockers

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

![](https://8aqnet.cdn.bcebos.com/2e022cde952cfcdc243181da0b147a02.jpg)

Hypervisor Ransomware | Multiple Threat Actor Groups Hop on Leaked Babuk Code to Build ESXi Lockers

Executive SummarySentinelLabs identified 10 ransomware families using VMware ESXi lockers based o
*2023-5-11 17:55:6
Author: [www.sentinelone.com(查看原文)](/jump-162917.htm)
阅读量:45
收藏*

---

## Executive Summary

* SentinelLabs identified 10 ransomware families using VMware ESXi lockers based on the 2021 Babuk source code leaks.
* These variants emerged through H2 2022 and H1 2023, which shows an increasing trend of Babuk source code adoption.
* Leaked source code enables actors to target Linux systems when they may otherwise lack expertise to build a working program.
* Source code leaks further complicate attribution, as more actors will adopt the tools.

## Background

Throughout early 2023, SentinelLabs observed an increase in VMware ESXi ransomware based on Babuk (*aka* Babak, Babyk). The Babuk leaks in September 2021 provided unprecedented insight into the development operations of an organized ransomware group.

Due to the prevalence of ESXi in on-prem and hybrid enterprise networks, these hypervisors are valuable targets for ransomware. Over the past two years, organized ransomware groups adopted Linux lockers, including ALPHV, Black Basta, Conti, Lockbit, and REvil. These groups focus on ESXi before other Linux variants, leveraging built-in tools for the ESXi hypervisor to kill guest machines, then encrypt crucial hypervisor files.

We identified overlap between the leaked Babuk source code and ESXi lockers attributed to Conti and REvil, with iterations of the latter sharply resembling one another. We also compared them to the leaked Conti Windows locker source code, finding shared, bespoke function names and features.

In addition to these notorious groups, we also found smaller ransomware operations using the Babuk source code to generate more recognizable ESXi lockers. Ransom House’s Mario and a previously undocumented ESXi version of Play Ransomware comprise a small handful of the growing Babuk-descended ESXi locker landscape.

## Babuk Background

Babuk was one of the early players in the ESXi ransomware space. The group’s longevity was crippled in 2021 when a Babuk developer [leaked](https://www.bleepingcomputer.com/news/security/babuk-ransomwares-full-source-code-leaked-on-hacker-forum/) the builder source code for Babuk’s C++-based Linux Executable & Linkable Format (ELF) ESXi, Golang-based Network Attached Storage (NAS), and C++-based Windows ransomware tooling.

Through early 2022, there were few indications that actors had adapted the leaked Babuk source code, aside from a short-lived ‘[Babuk 2.0’](https://intel471.com/blog/malware-source-code-leak-history) variant and the occasional new Windows [ransomware](https://www.sentinelone.com/labs/new-rook-ransomware-feeds-off-the-code-of-babuk/) du jour. As cybercrime research is often laser-focused on Windows, Linux trends can develop under the radar.

SentinelLabs identified Babuk-descended ransomware through the string `Doesn’t encrypted files: %d\n` in the source code’s `/бабак/esxi/enc/main.cpp`.

![Unique strings in Babuk source code main.cpp](https://www.sentinelone.com/wp-content/uploads/2023/05/Babyk_4.jpg)

The Babuk builder specifies a file name for the newly generated binary, `e_esxi.out`. Several samples we identified share a similar naming convention:

|  |  |
| --- | --- |
| **Ransomware Family** | **File Name** |
| Mario | emario.out |
| Play | e\_esxi.out |
| Babuk 2023 aka XVGV | RansomWare-e\_esxi-XVGV2.out |

For encryption, ESXi Babuk uses an implementation of the Sosemanuk stream cipher to encrypt targeted files, in contrast with Babuk for Windows, which uses the HC-128 cipher. Both ESXi and Windows Babuk use Curve25519-Donna to generate the encryption key.

## Generations of Babuk

### Comparison Methodology

SentinelLabs compiled an unstripped Babuk binary to establish a baseline of how Babuk looks and behaves, referred to henceforth as ‘Baseline Babuk.’ To understand whether the variants we identified are related to Babuk, we compared each variant to this Baseline Babuk sample and highlighted notable similarities and differences.

### Babuk 2023 (.XVGV)

SHA1: `e8bb26f62983055cfb602aa39a89998e8f512466`

XVGV, *aka* Babuk 2023, emerged in March 2023 on Bleeping Computer’s [forum](https://www.bleepingcomputer.com/forums/t/783412/babuk-linux-esxi-ransomware-xvgv-extension/) as highlighted by @[malwrhunterteam](https://twitter.com/malwrhunterteam/status/1636495878251839489). Baseline Babuk and XVGV share code derived from `main.cpp`, argument processing functions from `args.cpp`, and encryption implementation.

Like Babuk, XVGV requires the operator to provide a directory to encrypt as an argument. During dynamic analysis, we provided the test system’s user directory. On the first run, the sample generated a ransom note, `HowToRestore.txt`, in all child directories.

However, only six files were encrypted, each with either `.log` or `.gz` file extensions. Looking at the file extension inclusions reveals why the damage was limited: XVGV targets VMware-centric files and excludes those which do not match a designated list. This is a behavior shared with Baseline Babuk, though the XVGV author added more file extensions.

![XVGV .rodata segment references to file extensions (left) and Babuk source code equivalent](https://www.sentinelone.com/wp-content/uploads/2023/05/Babyk_5.jpg)

XVGV *.rodata* segment references to file extensions (left) and Babuk source code equivalent

### Play (.FinDom)

SHA1: `dc8b9bc46f1d23779d3835f2b3648c21f4cf6151`

This file references the file extension `.FinDom`, as well as the ransom email address `[[email protected]](https://www.sentinelone.com/cdn-cgi/l/email-protection)`, which are artifacts [associated](https://www.bleepingcomputer.com/forums/t/773651/play-ransomware-play-findom-support-topic/page-2) with Play Ransomware. This is the first known version of Play built for a Linux system, which aligns this actor with the [trend](https://s1.ai/icefire) of ransomware groups increasingly targeting Linux. Play contains the same file searching functionality as Baseline Babuk; it also implements encryption using Sosemanuk.

![Baseline Babuk (left) and Play disassembly of a ransom note construction function.](https://www.sentinelone.com/wp-content/uploads/2023/05/Babyk_8.jpg)

Baseline Babuk (left) and Play disassembly of a ransom note construction function

The Play binary was submitted to VirusTotal as part of an archive (SHA1: `9290478cda302b9535702af3a1dada25818ad9ce`) containing various hack tools and utilities–including AnyDesk, NetCat, a privilege escalation batch file, and encoded PowerShell Empire scripts–which are associated with ransomware group techniques after achieving initial access.

### Mario (.emario)

SHA1: `048b3942c715c6bff15c94cdc0bb4414dbab9e07`

Mario ransomware is operated by Ransom House, a group that emerged in [2021](https://www.bleepingcomputer.com/news/security/new-ransomhouse-group-sets-up-extortion-market-adds-first-victims/). Ransom House initially claimed that they target vulnerable networks to steal data without encrypting files. However, the group has since adopted cryptographic lockers.

The samples share a very similar `find_files_recursive` function, including the default ransom note filename `How To Restore Your Files.txt`. The encryption functions are also the same.

The verbose ransom note content is the most unique part of Mario’s ESXi locker. The Ransom House actors provide very explicit ...
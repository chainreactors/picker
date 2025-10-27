---
title: Custom-Branded Ransomware: The Vice Society Group and the Threat of Outsourced Development
url: https://buaq.net/go-141049.html
source: unSafe.sh - 不安全
date: 2022-12-23
fetch_date: 2025-10-04T02:18:02.802649
---

# Custom-Branded Ransomware: The Vice Society Group and the Threat of Outsourced Development

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

![](https://8aqnet.cdn.bcebos.com/11d85ee7b1a319d3751a9f561f622425.jpg)

Custom-Branded Ransomware: The Vice Society Group and the Threat of Outsourced Development

Executive SummaryThe Vice Society group has adopted a new custom-branded ransomware payload in re
*2022-12-22 21:57:3
Author: [www.sentinelone.com(查看原文)](/jump-141049.htm)
阅读量:46
收藏*

---

## Executive Summary

* The Vice Society group has adopted a new custom-branded ransomware payload in recent intrusions
* This ransomware variant, dubbed “PolyVice”, implements a robust encryption scheme, using NTRUEncrypt and ChaCha20-Poly1305 algorithms
* We assess it is likely that the group behind the custom-branded ransomware for Vice Society is also selling similar payloads to other groups

## Background

First identified in June 2021, [Vice Society](https://www.microsoft.com/en-us/security/blog/2022/10/25/dev-0832-vice-society-opportunistic-ransomware-campaigns-impacting-us-education-sector/) is a well-resourced ransomware group that has successfully breached various types of organizations. Using the [classic double extortion](https://www.sentinelone.com/blog/ransoms-without-ransomware-data-corruption-and-other-new-tactics-in-cyber-extortion/) technique, they set about maximizing financial gain with purely opportunistic targeting. In recent months, Vice Society has expanded its target selection strategy to include additional sensitive sectors.

The TTPs are nothing new. They include initial network access through compromised credentials, exploitation of known vulnerabilities (e.g., [PrintNightmare](https://www.sentinelone.com/blog/printnightmare-latest-patch-almost-puts-microsoft-vulnerability-to-bed/)), internal network reconnaissance, abuse of legitimate tools (*aka* COTS and [LOLBins](https://www.sentinelone.com/blog/how-do-attackers-use-lolbins-in-fileless-attacks/)), commodity backdoors, and [data exfiltration](https://www.sentinelone.com/blog/ransoms-without-ransomware-data-corruption-and-other-new-tactics-in-cyber-extortion/).

Rather than using or developing their own locker payload, Vice Society operators [have deployed third-party ransomware](https://www.cisa.gov/uscert/ncas/alerts/aa22-249a) in their intrusions, including [HelloKitty](https://www.sentinelone.com/labs/hellokitty-ransomware-lacks-stealth-but-still-strikes-home/), Five Hands, and [Zeppelin](https://www.sentinelone.com/blog/the-good-the-bad-and-the-ugly-in-cybersecurity-week-36-2-2/).

## Vice Society Ransomware and Links to Other Ransomware Variants

In a recent intrusion, we identified a ransomware deployment that appended the file extension `.ViceSociety` to all encrypted files in addition to dropping ransom notes with the file name “AllYFilesAE” in each encrypted directory.

Our initial analysis suggested the ransomware, which we dubbed “PolyVice”, was in the early stages of development. The presence of debugging messages suggested that the Vice Society group may be developing their own ransomware implementation.

Zeppelin ransomware, previously seen used by the group, [was recently found](https://www.bleepingcomputer.com/news/security/researchers-secretly-helped-decrypt-zeppelin-ransomware-for-2-years/) to implement a weak encryption scheme that allows for decryption of locked files, potentially motivating the group to adopt a new locker.

However, further investigation showed that a decryptor related to the PolyVice variant first appeared in the wild on July 13, 2022, indicating that the locker could not have been in the early stages of development and that a “release” version existed prior to the group’s use of Zeppelin and other ransomware variants.

Our analysis suggests that Vice Society has used a toolkit overpopulated with different ransomware strains and variants.

* We identified significant overlap in the encryption implementation observed in the “RedAlert” ransomware, a Linux locker variant [targeting VMware ESXi servers](https://www.esentire.com/blog/esentire-threat-intelligence-malware-analysis-redalert), suggesting that both variants were developed by the same group of individuals.

* According to [Microsoft](https://www.microsoft.com/en-us/security/blog/2022/10/25/dev-0832-vice-society-opportunistic-ransomware-campaigns-impacting-us-education-sector/), Vice Society adopted the RedAlert variant in late September 2022. We haven’t been able to confirm if a RedAlert Windows variant payload existed in the wild at the time, or if the Windows variant we track as PolyVice has any relation with it.

Further investigation also revealed that the codebase used to build the Vice Society Windows payload has been used to build custom-branded payloads for other threat groups, including the “Chily” and “SunnyDay” ransomware.

![Code similarities between PolyVice and Chily Ransomware](https://www.sentinelone.com/wp-content/uploads/2022/12/PolyVice_1.jpg)
![Code similarities between PolyVice and SunnyDay Ransomware](https://www.sentinelone.com/wp-content/uploads/2022/12/PolyVice_13.jpg)

Code similarities between Vice Society and SunnyDay Ransomware

These numbers provide clear evidence that the code is maintained by the same developers.

* The Vice Society branded payload has 100% matched functions compared to the Chily branded payload, indicating that the executable codebase is identical.

* The SunnyDay branded payload is an older version of the codebase that has a 100% match on 410 functions and is missing an additional 37 net new functions implemented in the Vice Society codebase.

The real difference is in the intended use of the code exemplified by the data section, where all of the ransomware campaign details are stored, such as the encrypted file extension, ransom note file name, hardcoded master key, ransom note content, and wallpaper text.

![Data section comparison Vice Society (above) Chily Ransomware (below)](https://www.sentinelone.com/wp-content/uploads/2022/12/PolyVice_5.jpg)

Data section comparison Vice Society (above) Chily Ransomware (below)

We assess it’s likely that a previously unknown developer or group of developers with specialized expertise in ransomware development is selling custom-branded ransomware payloads to multiple groups. The details embedded in these payloads make it highly unlikely that Vice Society, SunnyDay, and Chily ransomware are operated by the same group.

The delivery method for this “Locker as a Service” is unclear, but the code design suggests the ransomware developer provides a builder that enables buyers to independently generate any number of lockers/decryptors by binary patching a template payload. This allows buyers to customize their ransomware without revealing any source code. Unlike other known RaaS builders, buyers can generate branded payloads, enabling them to run their own RaaS programs.

## Analyzing PolyVice | Initialization of the NTRU Asymmetric Keys

PolyVice ransomware is a 64-bit Windows binary compiled with MinGW (SHA1: `c8e7ecbbe78a26bea813eeed6801a0ac9d1eacac`)

PolyVice implements a hybrid encryption scheme that combines asymmetric and symmetric encryption to securely encrypt files.

For asymmetric encryption, it uses an [open source implementation](https://github.com/tbuktu/libntru) of the [NTRUEncrypt](https://en.wikipedia.org/wiki/NTRUEncrypt) algorithm, which is known to be quantum-resistant. For symmetric encryption, it uses an [open source implementation](https://github.com/grigorig/chachapoly) of the [ChaCha20-Poly1305](https://en.wikipedia.org/wiki/ChaCha20-Poly1305) algorithm, a stream cipher with message authentication, a 256-bit key and 96-bit nonce.

In the initialization phase, it imports ...
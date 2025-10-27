---
title: LockBit for Mac | How Real is the Risk of macOS Ransomware?
url: https://buaq.net/go-159273.html
source: unSafe.sh - 不安全
date: 2023-04-19
fetch_date: 2025-10-04T11:32:52.754899
---

# LockBit for Mac | How Real is the Risk of macOS Ransomware?

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

![](https://8aqnet.cdn.bcebos.com/aa2272bd047e33f309d0b87bb33946b1.jpg)

LockBit for Mac | How Real is the Risk of macOS Ransomware?

On April 16th, Twitter user @malwrhunterteam tweeted details of a sample of the LockBit ransomware
*2023-4-18 22:58:23
Author: [www.sentinelone.com(查看原文)](/jump-159273.htm)
阅读量:34
收藏*

---

On April 16th, Twitter user [@malwrhunterteam](https://twitter.com/malwrhunterteam/status/1647384505550876675?s=20) tweeted details of a sample of the LockBit ransomware compiled for Apple’s macOS arm64 architecture. LockBit claims to be “the oldest ransomware affiliate program on the planet”, and news that one of the major cybercrime outfits in the ransomware landscape was now targeting macOS devices has predictably raised concerns about the ransomware threat on Mac devices.

In this post, we explore both the details of the LockBit sample uncovered and the larger question of how real is the risk of ransomware on macOS endpoints.

![](https://www.sentinelone.com/wp-content/uploads/2023/04/LockBit-for-Mac-How-Real-is-the-Risk-of-macOS-Ransomware.jpg)

## LockBit for Mac | Testing, Testing, 1 2 3

The sample of LockBit ransomware for Mac was discovered on VirusTotal on April 16th, and according to [@vxunderground](https://twitter.com/vxunderground/status/1647427900352733185?s=20) may have been compiled as early as 17th November 2022.

![lockbit ransomware variants for macOS](https://www.sentinelone.com/wp-content/uploads/2023/04/lockbit_macOS_9.jpg)

Source: vxunderground

A further sample was uploaded to VirusTotal on the 8th December, 2022.

![lockbit for macOS on VirusTotal](https://www.sentinelone.com/wp-content/uploads/2023/04/lockbit_macOS_13.jpg)

Source: VirusTotal

The macOS samples are compiled solely for the Apple ARM M1/M2 (*aka* Apple silicon) architecture. No macOS Intel sample is known at this time.

Importantly for concerned users, no occurrences of LockBit for Mac have yet been reported in the wild, no victims claimed, and no distribution method is known to be associated with the malware. However, early claims that the sample was [non-functional](https://twitter.com/patrickwardle/status/1647684088458022912?s=20) were incorrect.

LockBit 3.0 typically requires a [unique password to execute](https://www.sentinelone.com/labs/lockbit-3-0-update-unpicking-the-ransomwares-latest-anti-analysis-and-evasion-techniques/); in the case of the Mac sample, the hardcoded password is “test” – one of several clues as to the current state of development of the threat.

The Mac variant is a direct descendant of the [LockBit for Linux](https://www.trendmicro.com/en_my/research/22/a/analysis-and-Impact-of-lockbit-ransomwares-first-linux-and-vmware-esxi-variant.html) variant first spotted in Jan 2022, and contains much the same code.

The ransomware functions as intended to encrypt targeted files, which are subsequently appended with the `.lockbit` extension. The locker also deposits a rather lengthy ransom note in the parent folder with the name `!!!-Restore-My-Files-!!!`.

![The ransom note is encrypted in the locker_Apple_M1_64< binary](https://www.sentinelone.com/wp-content/uploads/2023/04/lockbit_macOS_2.jpg)

The ransom note is encrypted in the *locker\_Apple\_M1\_64* binary

The ransom note gives a clear indication of the intended victims.

![Opening paragraph of the LockBit for Mac ransom note](https://www.sentinelone.com/wp-content/uploads/2023/04/lockbit_macOS_7.jpg)

Opening paragraph of the LockBit for Mac ransom note

LockBit is known for attacking and extorting organizations rather than random individuals on the internet, and the aim of the developers is to make large profits from locking and stealing business data.

The Mac sample does not appear to implement any functionality for exfiltrating the data it locks, nor does it have any method of persistence: more clear signs that this is a “work in progress” and not a genuine payload intended for use in the wild.

## LockBit for Mac | Execution and Encryption

Despite the underdeveloped nature of the samples, it is clear that the authors are experimenting with similar functionality seen in lockers for other platforms. The malware is intended to be executed by a human operator or configuration file and offers a number of different encryption options. These mirror those seen in the Linux version noted above.

![Command line options that can be passed to the malware on execution](https://www.sentinelone.com/wp-content/uploads/2023/04/lockbit_macOS_10.jpg)

Command line options that can be passed to the malware on execution

These can be seen reflected in the methods seen in the code.

![Encryption functions in the LockBit for Mac ransomware sample](https://www.sentinelone.com/wp-content/uploads/2023/04/lockbit_macOS_8.jpg)

Encryption functions in the LockBit for Mac ransomware sample

Although there is a list of hardcoded extension names, many of which are not applicable to macOS, the locker is not restricted to encrypting only files with those extensions. As noted above, an operator may specify a particular destination and attempt to encrypt all files in that destination, [partially or entirely](https://www.sentinelone.com/blog/ransoms-without-ransomware-data-corruption-and-other-new-tactics-in-cyber-extortion/).

![LockBit is not restricted to the list of hardcoded extensions](https://www.sentinelone.com/wp-content/uploads/2023/04/lockbit_macOS_3.jpg)

LockBit is not restricted to the list of hardcoded extensions

Much of the code and methods apply to non-macOS platforms such as Windows, ESXi and Linux, indicating that the samples were likely compiled from the same cross-platform source code.

![A lot of the LockBit code is redundant for macOS targets](https://www.sentinelone.com/wp-content/uploads/2023/04/lockbit_macOS_4.jpg)

A lot of the LockBit code is redundant for macOS targets

On execution on an Apple M1 or M2 device, the LockBit ransomware queries for the model name via `sysctl hw.model`, likely as part of anti-analysis measures.

Encryption takes advantage of the publicly available library [Mbed TLS](https://fuchsia.googlesource.com/third_party/github.com/ARMmbed/mbedtls/%2B/HEAD/programs/aes/aescrypt2.c). Interestingly, there appear to be no cross-references to the functions intended to decrypt locked files.

![Multiple cross-references appear for encryption functions, but none for decryption](https://www.sentinelone.com/wp-content/uploads/2023/04/lockbit_macOS_6.jpg)

Multiple cross-references appear for encryption functions, but none for decryption

According to one media [report](https://www.bleepingcomputer.com/news/security/lockbit-ransomware-encryptors-found-targeting-mac-devices/), the public-facing representative of LockBit, known as LockBitSupp, said that the Mac encryptor is “actively being developed”. Perhaps, more complete samples may be over the horizon with the missing functionality.

## Is Ransomware a Real Risk on macOS Today?

Due to the rampant nature of the ransomware threat on other platforms, it is only natural to wonder how safe Macs are from ransomware actors. While some security vendors have [incorrectly](https://www.crowdstrike.com/blog/how-crowdstrike-analyzes-macos-malware-to-optimize-automated-detection-capabilities/) made much of it in the past, the reality is that there is no publicly recorded case of any business ever paying a ransom demand as a result of macOS ransomware. This is not surprising when you look at the history of attempts to build ransomware on macOS to date.

The most recent known Mac ransomware prior to the LockBit sample found this week was [EvilQuest](https://www.sentinel...
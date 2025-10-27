---
title: AceLdr - Cobalt Strike UDRL For Memory Scanner Evasion
url: https://buaq.net/go-144647.html
source: unSafe.sh - 不安全
date: 2023-01-09
fetch_date: 2025-10-04T03:20:41.014958
---

# AceLdr - Cobalt Strike UDRL For Memory Scanner Evasion

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

![](https://8aqnet.cdn.bcebos.com/cd18bdb053471f81e33736f5b0592d55.jpg)

AceLdr - Cobalt Strike UDRL For Memory Scanner Evasion

A position-independent reflective loader for Cobalt Strike. Zero results from Hunt-Sleeping-
*2023-1-8 19:30:0
Author: [www.kitploit.com(查看原文)](/jump-144647.htm)
阅读量:42
收藏*

---

[![](https://blogger.googleusercontent.com/img/a/AVvXsEhZeWXaM7lP8v3qst9OxNnwL3j8pK1LRyKzwJDsJuuyImNffH3_PQ3K9OEU4LIwv4ke_lsKP8MD1jigC9_EJJUQYJp1JfLaIb86fwgWN_c619d9458BcnRJPJnXrzpTst3nmmbGINlyvj2-1CDfiNW7C-6v4bwYOPM2HsLa-4QHGgVCp_k_QH-cmXW31A=w640-h360)](https://blogger.googleusercontent.com/img/a/AVvXsEhZeWXaM7lP8v3qst9OxNnwL3j8pK1LRyKzwJDsJuuyImNffH3_PQ3K9OEU4LIwv4ke_lsKP8MD1jigC9_EJJUQYJp1JfLaIb86fwgWN_c619d9458BcnRJPJnXrzpTst3nmmbGINlyvj2-1CDfiNW7C-6v4bwYOPM2HsLa-4QHGgVCp_k_QH-cmXW31A)

A position-independent reflective loader for Cobalt Strike. Zero results from [Hunt-Sleeping-Beacons](https://github.com/thefLink/Hunt-Sleeping-Beacons "Hunt-Sleeping-Beacons"), [BeaconHunter](https://github.com/3lp4tr0n/BeaconHunter "BeaconHunter"), [BeaconEye](https://github.com/CCob/BeaconEye "BeaconEye"), [Patriot](https://github.com/joe-desimone/patriot "Patriot"), [Moneta](https://github.com/forrest-orr/moneta "Moneta"), [PE-sieve](https://github.com/hasherezade/pe-sieve "PE-sieve"), or [MalMemDetect](https://github.com/waldo-irc/MalMemDetect "MalMemDetect").

## Features

#### Easy to Use

Import a single CNA script before generating shellcode.

#### Dynamic Memory Encryption

Creates a new heap for any allocations from [Beacon](https://www.kitploit.com/search/label/Beacon "Beacon") and encrypts entries before sleep.

#### Code [Obfuscation](https://www.kitploit.com/search/label/Obfuscation "Obfuscation") and Encryption

Changes the memory containing CS executable code to non-executable and encrypts it (FOLIAGE).

#### Return Address [Spoofing](https://www.kitploit.com/search/label/Spoofing "Spoofing") at Execution

Certain WinAPI calls are executed with a spoofed return address (InternetConnectA, NtWaitForSingleObject, RtlAllocateHeap).

#### Sleep Without Sleep

Delayed execution using WaitForSingleObjectEx.

#### RC4 Encryption

All [encryption](https://www.kitploit.com/search/label/Encryption "encryption") performed with SystemFunction032.

## Known Issues

* Not compatible with loaders that rely on the shellcode thread staying alive.

## References

This project would not have been possible without the following:

* [FOLIAGE](https://github.com/secidiot/FOLIAGE "FOLIAGE")
* [x64 return address spoofing (source + explanation)](https://www.unknowncheats.me/forum/anti-cheat-bypass/268039-x64-return-address-spoofing-source-explanation.html "x64 return address spoofing (source + explanation)")

Other features and inspiration were taken from the following:

* [https://www.arashparsa.com/bypassing-pesieve-and-moneta-the-easiest-way-i-could-find/](https://www.arashparsa.com/bypassing-pesieve-and-moneta-the-easiest-way-i-could-find/ "https://www.arashparsa.com/bypassing-pesieve-and-moneta-the-easiest-way-i-could-find/")
* [https://github.com/secidiot/TitanLdr](https://github.com/secidiot/TitanLdr "https://github.com/secidiot/TitanLdr")
* [https://github.com/JLospinoso/gargoyle](https://github.com/JLospinoso/gargoyle "https://github.com/JLospinoso/gargoyle")
* [https://www.forrest-orr.net/post/masking-malicious-memory-artifacts-part-ii-insights-from-moneta](https://www.forrest-orr.net/post/masking-malicious-memory-artifacts-part-ii-insights-from-moneta "https://www.forrest-orr.net/post/masking-malicious-memory-artifacts-part-ii-insights-from-moneta")
* [https://www.arashparsa.com/hook-heaps-and-live-free/](https://www.arashparsa.com/hook-heaps-and-live-free/ "https://www.arashparsa.com/hook-heaps-and-live-free/")
* [https://blog.f-secure.com/hunting-for-gargoyle-memory-scanning-evasion/](https://blog.f-secure.com/hunting-for-gargoyle-memory-scanning-evasion/ "https://blog.f-secure.com/hunting-for-gargoyle-memory-scanning-evasion/")
* [https://www.elastic.co/blog/detecting-cobalt-strike-with-memory-signatures](https://www.elastic.co/blog/detecting-cobalt-strike-with-memory-signatures "https://www.elastic.co/blog/detecting-cobalt-strike-with-memory-signatures")

AceLdr - Cobalt Strike UDRL For Memory Scanner Evasion
![AceLdr - Cobalt Strike UDRL For Memory Scanner Evasion](https://blogger.googleusercontent.com/img/a/AVvXsEhZeWXaM7lP8v3qst9OxNnwL3j8pK1LRyKzwJDsJuuyImNffH3_PQ3K9OEU4LIwv4ke_lsKP8MD1jigC9_EJJUQYJp1JfLaIb86fwgWN_c619d9458BcnRJPJnXrzpTst3nmmbGINlyvj2-1CDfiNW7C-6v4bwYOPM2HsLa-4QHGgVCp_k_QH-cmXW31A=s72-w640-c-h360)
Reviewed by Zion3R
on
8:30 AM
Rating: 5

文章来源: http://www.kitploit.com/2023/01/aceldr-cobalt-strike-udrl-for-memory.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)
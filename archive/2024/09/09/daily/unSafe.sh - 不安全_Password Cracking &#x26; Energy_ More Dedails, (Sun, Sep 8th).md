---
title: Password Cracking &#x26; Energy: More Dedails, (Sun, Sep 8th)
url: https://buaq.net/go-260834.html
source: unSafe.sh - 不安全
date: 2024-09-09
fetch_date: 2025-10-06T18:20:04.558133
---

# Password Cracking &#x26; Energy: More Dedails, (Sun, Sep 8th)

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

![](https://8aqnet.cdn.bcebos.com/310e52f62cab4d26993b5cb9a4497a5f.jpg)

Password Cracking &#x26; Energy: More Dedails, (Sun, Sep 8th)

Here are more details on the power consumption of my desktop computer when I crack passwords (cfr d
*2024-9-8 23:24:37
Author: [isc.sans.edu(查看原文)](/jump-260834.htm)
阅读量:13
收藏*

---

Here are more details on the power consumption of my desktop computer when I crack passwords (cfr diary entry "[Quickie: Password Cracking & Energy](https://isc.sans.edu/diary/Quickie%2BPassword%2BCracking%2BEnergy/31122)").

The vertical scale of this chart is expressed in Watts:

![](https://isc.sans.edu/diaryimages/images/20240908-165651.png)

1. 0 Watt: my desktop computer is turned off
2. 76 Watt average: my desktop computer is turned on & idling
3. 151 Watt average: hashcat is running in dictionary attack mode cracking SHA256 hashes
4. 445 Watt average: hashcat is running in brute-force attack mode cracking SHA256 hashes

The most power is required (445 Watt) when hashcat is using the GPU ( NVIDIA GeForce RTX 3080) in brute-force attack mode. For comparison, 445 Watt average continuous is enough to heat my office in winter to a nice & comfy temperature, I don't need central heating in that room when hashcat is running for many hours.

You might wonder if 445 Watt is enough for that, given that electrical heaters typically come in 1000+ Watt models. But electrical heaters don't consume electrical power constantly to heat a room, they have a thermostat that shuts of current flow regularly when the desired room temperature is reached. They are more powerfull so that they can heat up a room faster. While my desktop computer requires 445 Watt continuously when cracking with the GPU.

Didier Stevens

文章来源: https://isc.sans.edu/diary/rss/31242
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)
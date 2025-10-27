---
title: 木马版超级马里奥被用于传播恶意程序
url: https://buaq.net/go-170757.html
source: unSafe.sh - 不安全
date: 2023-06-29
fetch_date: 2025-10-04T11:46:25.864911
---

# 木马版超级马里奥被用于传播恶意程序

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

![]()

木马版超级马里奥被用于传播恶意程序

*2023-6-28 22:10:43
Author: [www.solidot.org(查看原文)](/jump-170757.htm)
阅读量:30
收藏*

---

* 文章
* 皮肤

* 分类:
* [首页](https://www.solidot.org/)
* [Linux](https://linux.solidot.org/)
* [科学](https://science.solidot.org/)
* [科技](https://technology.solidot.org/)
* [移动](https://mobile.solidot.org/)
* [苹果](https://apple.solidot.org/)
* [硬件](https://hardware.solidot.org/)
* [软件](https://software.solidot.org/)
* [安全](https://security.solidot.org/)
* [游戏](https://games.solidot.org/)
* [书籍](https://books.solidot.org/)
* [idle](https://idle.solidot.org/)
* [云计算](https://cloud.solidot.org/)

[![安全](https://icon.solidot.org/images/topics/topicsecurity.png)](https://www.solidot.org/search?tid=100 "安全")

[Wilson](https://www.solidot.org/~Wilson) (42865)发表于 2023年06月28日 22时10分 星期三

《Super Mario 3: Mario Forever》是经典任天堂游戏的免费重制版，保留了超级马里奥系列的游戏机制，更新了图像和音频。它非常受欢迎，下载量多达数百万次。安全公司 Cyble 的研究人员发现，攻击者正利用一个木马版的安装程序传播恶意程序。木马版本主要通过游戏论坛、社交媒体和恶意广告传播，它包含了一个合法版的游戏拷贝，以及两个恶意负荷 java.exe 和 atom.exe，其中 java.exe 是门罗币的挖矿程序，atom.exe 是 SupremeBot 挖矿客户端。SupremeBot 还会通过指令控制服务器下载额外的负荷 wime.exe——一个开源的信息窃取程序 Umbral Stealer，从被感染的设备上窃取数据，包括浏览器上储存的密码、cookies、加密货币钱包，Discord、Minecraft、Roblox 和 Telegram 的凭证。

https://blog.cyble.com/2023/06/23/trojanized-super-mario-game-installer-spreads-supremebot-malware/

﻿

文章来源: https://www.solidot.org/story?sid=75368
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)
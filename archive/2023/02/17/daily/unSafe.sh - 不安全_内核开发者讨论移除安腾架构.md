---
title: 内核开发者讨论移除安腾架构
url: https://buaq.net/go-149701.html
source: unSafe.sh - 不安全
date: 2023-02-17
fetch_date: 2025-10-04T06:50:27.591936
---

# 内核开发者讨论移除安腾架构

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

内核开发者讨论移除安腾架构

因基本上没人用且没人维护，内核开发者讨论是否移除英特尔的安腾/IA64 架构，讨论结果还是让它活着。问题最早是 Arm 开发者 Ard Biesheuvel 提出的，他指出内核的 IA64
*2023-2-16 22:32:24
Author: [www.solidot.org(查看原文)](/jump-149701.htm)
阅读量:17
收藏*

---

因基本上没人用且没人维护，内核开发者讨论是否移除英特尔的安腾/IA64 架构，讨论结果还是让它活着。问题最早是 Arm 开发者 Ard Biesheuvel 提出的，他指出内核的 IA64 版本无人维护，而根据一位可能是仅剩的用户报告它已经出问题一个月了，但没人关心，因此提议干脆移除它。Linux 作者 Linus Torvalds 说他不是 IA64 架构粉丝，但完全移除一个架构还是令人难过，而且它的维护负担看起来并不大。他同时表示，如果没人愿意花时间去处理故障，那么结束对 IA64 的支持只能是唯一选项。物理学家兼 Debian 维护者 John Paul Adrian Glaubitz 站出来拯救了 IA64，表示他有时间维护该架构，而且他还有一台安腾服务器可以测试。英特尔是在 2021 年退役了安腾处理器产品。

https://www.theregister.com/2023/02/16/itanium\_linux\_kernel/

文章来源: https://www.solidot.org/story?sid=74156
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)
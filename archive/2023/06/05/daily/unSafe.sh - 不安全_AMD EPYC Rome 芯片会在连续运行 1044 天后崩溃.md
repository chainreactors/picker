---
title: AMD EPYC Rome 芯片会在连续运行 1044 天后崩溃
url: https://buaq.net/go-167159.html
source: unSafe.sh - 不安全
date: 2023-06-05
fetch_date: 2025-10-04T11:44:27.695746
---

# AMD EPYC Rome 芯片会在连续运行 1044 天后崩溃

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

AMD EPYC Rome 芯片会在连续运行 1044 天后崩溃

AMD 披露了一个 99.99% 的用户都体会不到的处理器 bug：EPYC Rome 芯片会在连续运行 1044 天后崩溃。EPYC Rome 是 2019 年发布的基于 Zen 2 架
*2023-6-4 19:14:9
Author: [www.solidot.org(查看原文)](/jump-167159.htm)
阅读量:31
收藏*

---

AMD 披露了一个 99.99% 的用户都体会不到的处理器 bug：EPYC Rome 芯片会在连续运行 1044 天后崩溃。EPYC Rome 是 2019 年发布的基于 Zen 2 架构的第二代 EPYC 处理器，目前最新的 EPYC 处理器是第四代 Genoa。对于该 bug AMD 表示它无意去修复。该 bug 与处理器核心未能退出 CC6 睡眠状态有关，故障的确切触发时间与扩频和 REFCLK 频率有关。解决该问题有两种，其一是在连续运行 1044 天前重启下，其二是禁用 CC6 睡眠状态。今天的内核补丁可以在不重启的情况下打上，但固件更新等仍然需要强制性重启，因此连续运行 1044 天是极其罕见的情况。

https://www.tomshardware.com/news/amds-epyc-rome-chips-could-hang-after-1044-days-of-uptime

文章来源: https://www.solidot.org/story?sid=75145
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)
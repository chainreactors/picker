---
title: 恶意程序滥用微软 IIS 功能在 Windows 上执行恶意代码
url: https://buaq.net/go-149862.html
source: unSafe.sh - 不安全
date: 2023-02-18
fetch_date: 2025-10-04T07:20:23.306535
---

# 恶意程序滥用微软 IIS 功能在 Windows 上执行恶意代码

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

恶意程序滥用微软 IIS 功能在 Windows 上执行恶意代码

安全公司赛门铁克的研究人员发现一种恶意程序滥用微软 IIS 的一项功能隐蔽的渗出数据和执行恶意代码。微软 IIS（Internet Information Services）是广泛使用的
*2023-2-17 18:12:6
Author: [www.solidot.org(查看原文)](/jump-149862.htm)
阅读量:23
收藏*

---

安全公司赛门铁克的研究人员发现一种恶意程序滥用微软 IIS 的一项功能隐蔽的渗出数据和执行恶意代码。微软 IIS（Internet Information Services）是广泛使用的 Web 服务器，它的一项功能叫 Failed Request Event Buffering（FREB），旨在帮助管理员诊断错误，FREB 能从缓存中将部分错误相关的请求写入磁盘。黑客找到了滥用该功能的方法，攻击者首先需要入侵运行 IIS 的 Windows 系统，启用 FREB，通过将恶意代码注入 IIS 进程内存劫持执行，它随后就能拦截所有 HTTP 请求，寻找特殊格式的请求，这种特殊的请求能以隐蔽的方式执行远程代码，系统上没有可疑文件或进程在运行。研究人员将这种恶意程序命名为 Frebniis。

https://arstechnica.com/?p=1918304

文章来源: https://www.solidot.org/story?sid=74164
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)
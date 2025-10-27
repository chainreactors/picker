---
title: 中国公司收购 Polyfill 之后植入恶意程序
url: https://buaq.net/go-247948.html
source: unSafe.sh - 不安全
date: 2024-06-30
fetch_date: 2025-10-06T16:54:45.157113
---

# 中国公司收购 Polyfill 之后植入恶意程序

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

中国公司收购 Polyfill 之后植入恶意程序

polyfill.js 是广泛使用的用于支持旧浏览器的开源库，有逾 10 万网站通过 cdn.polyfill.io 域名嵌入了该脚本。今年二月，一家中国公司收购了该域名和相关 Githu
*2024-6-29 21:47:11
Author: [www.solidot.org(查看原文)](/jump-247948.htm)
阅读量:22
收藏*

---

polyfill.js 是广泛使用的用于支持旧浏览器的开源库，有逾 10 万网站通过 cdn.polyfill.io 域名嵌入了该脚本。今年二月，一家中国公司收购了该域名和相关 Github 账号，然后通过 cdn.polyfill.io 向移动设备植入恶意程序。新拥有者还迅速删除了 Github 上的相关讨论。Polyfill 原作者建议移除该脚本，因为现代浏览器不再需要它，但如果必须使用，可以用 CDN 服务商 Fastly 和 Cloudflare 的替代。安全研究人员发现，植入的恶意程序使用假的 Google 分析域名 www.googie-anaiytics.com 将移动设备用户重定向到博彩网站。代码针对逆向工程有特定保护代码，而且只在特定时间对特定移动设备激活。它在检测到管理员后不会激活。当检测到网络分析服务时它会延迟执行。研究人员给恶意程序起名为“跳转（tiaozhuan）”——恶意代码使用的一个函数名叫 check\_tiaozhuan。

https://sansec.io/research/polyfill-supply-chain-attack

文章来源: https://www.solidot.org/story?sid=78560
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)
---
title: Blind SSRF in Skype (Microsoft)
url: https://buaq.net/go-133133.html
source: unSafe.sh - 不安全
date: 2022-10-29
fetch_date: 2025-10-03T21:11:28.217449
---

# Blind SSRF in Skype (Microsoft)

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

Blind SSRF in Skype (Microsoft)

TypeError: Too many redirects.https://infosecwriteups.com/blind-ssrf-in-skype-microsoft-6639f4961052
*2022-10-28 18:59:6
Author: [infosecwriteups.com(查看原文)](/jump-133133.htm)
阅读量:112
收藏*

---

TypeError: Too many redirects.https://infosecwriteups.com/blind-ssrf-in-skype-microsoft-6639f4961052?source=rss----7b722bfd1b8d--bug\_bounty, https://medium.com/m/global-identity?redirectUrl=https%3A%2F%2Finfosecwriteups.com%2Fblind-ssrf-in-skype-microsoft-6639f4961052%3Fsource%3Drss----7b722bfd1b8d--bug\_bounty, https://infosecwriteups.com/blind-ssrf-in-skype-microsoft-6639f4961052?source=rss----7b722bfd1b8d--bug\_bounty&gi=1952fb5bba78, https://medium.com/m/global-identity?redirectUrl=https%3A%2F%2Finfosecwriteups.com%2Fblind-ssrf-in-skype-microsoft-6639f4961052%3Fsource%3Drss----7b722bfd1b8d--bug\_bounty, https://infosecwriteups.com/blind-ssrf-in-skype-microsoft-6639f4961052?source=rss----7b722bfd1b8d--bug\_bounty&gi=1f7cd16250e5, https://medium.com/m/global-identity?redirectUrl=https%3A%2F%2Finfosecwriteups.com%2Fblind-ssrf-in-skype-microsoft-6639f4961052%3Fsource%3Drss----7b722bfd1b8d--bug\_bounty, https://infosecwriteups.com/blind-ssrf-in-skype-microsoft-6639f4961052?source=rss----7b722bfd1b8d--bug\_bounty&gi=fda7db4d23a7, https://medium.com/m/global-identity?redirectUrl=https%3A%2F%2Finfosecwriteups.com%2Fblind-ssrf-in-skype-microsoft-6639f4961052%3Fsource%3Drss----7b722bfd1b8d--bug\_bounty, https://infosecwriteups.com/blind-ssrf-in-skype-microsoft-6639f4961052?source=rss----7b722bfd1b8d--bug\_bounty&gi=ad47d3a12010, https://medium.com/m/global-identity?redirectUrl=https%3A%2F%2Finfosecwriteups.com%2Fblind-ssrf-in-skype-microsoft-6639f4961052%3Fsource%3Drss----7b722bfd1b8d--bug\_bounty, https://infosecwriteups.com/blind-ssrf-in-skype-microsoft-6639f4961052?source=rss----7b722bfd1b8d--bug\_bounty&gi=ac14706d1c48, https://medium.com/m/global-identity?redirectUrl=https%3A%2F%2Finfosecwriteups.com%2Fblind-ssrf-in-skype-microsoft-6639f4961052%3Fsource%3Drss----7b722bfd1b8d--bug\_bounty, https://infosecwriteups.com/blind-ssrf-in-skype-microsoft-6639f4961052?source=rss----7b722bfd1b8d--bug\_bounty&gi=7a04b46201e7, https://medium.com/m/global-identity?redirectUrl=https%3A%2F%2Finfosecwriteups.com%2Fblind-ssrf-in-skype-microsoft-6639f4961052%3Fsource%3Drss----7b722bfd1b8d--bug\_bounty, https://infosecwriteups.com/blind-ssrf-in-skype-microsoft-6639f4961052?source=rss----7b722bfd1b8d--bug\_bounty&gi=ed270f8eabb0, https://medium.com/m/global-identity?redirectUrl=https%3A%2F%2Finfosecwriteups.com%2Fblind-ssrf-in-skype-microsoft-6639f4961052%3Fsource%3Drss----7b722bfd1b8d--bug\_bounty, https://infosecwriteups.com/blind-ssrf-in-skype-microsoft-6639f4961052?source=rss----7b722bfd1b8d--bug\_bounty&gi=a0bfd145e4, https://medium.com/m/global-identity?redirectUrl=https%3A%2F%2Finfosecwriteups.com%2Fblind-ssrf-in-skype-microsoft-6639f4961052%3Fsource%3Drss----7b722bfd1b8d--bug\_bounty, https://infosecwriteups.com/blind-ssrf-in-skype-microsoft-6639f4961052?source=rss----7b722bfd1b8d--bug\_bounty&gi=301e5edd54df, https://medium.com/m/global-identity?redirectUrl=https%3A%2F%2Finfosecwriteups.com%2Fblind-ssrf-in-skype-microsoft-6639f4961052%3Fsource%3Drss----7b722bfd1b8d--bug\_bounty, https://infosecwriteups.com/blind-ssrf-in-skype-microsoft-6639f4961052?source=rss----7b722bfd1b8d--bug\_bounty&gi=a6794b66eec7

文章来源: https://infosecwriteups.com/blind-ssrf-in-skype-microsoft-6639f4961052?source=rss----7b722bfd1b8d--bug\_bounty
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)
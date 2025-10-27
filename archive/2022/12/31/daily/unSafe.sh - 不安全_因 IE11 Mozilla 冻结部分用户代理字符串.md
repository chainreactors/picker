---
title: 因 IE11 Mozilla 冻结部分用户代理字符串
url: https://buaq.net/go-143488.html
source: unSafe.sh - 不安全
date: 2022-12-31
fetch_date: 2025-10-04T02:46:57.578585
---

# 因 IE11 Mozilla 冻结部分用户代理字符串

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

因 IE11 Mozilla 冻结部分用户代理字符串

两周前，用户向 Mozilla 报告了一个用户代理字符串（UA string）引发的网站兼容性问题。UA string 始于 1990 年代，网站可以利用这一数据调整性能和功能，或屏蔽过时
*2022-12-30 23:8:36
Author: [www.solidot.org(查看原文)](/jump-143488.htm)
阅读量:19
收藏*

---

两周前，用户向 Mozilla 报告了一个用户代理字符串（UA string）引发的网站兼容性问题。UA string 始于 1990 年代，网站可以利用这一数据调整性能和功能，或屏蔽过时的浏览器。即将发布的 Firefox 110 的 UA string 是 Mozilla/5.0 (Windows NT 10.0; Win64; x64; **rv:110.0**) Gecko/20100101 Firefox/110，用户报告它导致了 bestbuy.com 显示错误信息，声称不支持该浏览器，它建议用户下载最新版本的 Chrome、Firefox 或 Microsoft Edge。调查发现，原因是 IE11 的 UA string——Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko。Firefox 110 的 UA string 包含了 rv:11，因此被网站识别为它不再支持的 IE11。Mozilla 的解决方法是冻结版本号，Mozilla/5.0 (Windows NT 10.0; Win64; x64; **rv:109.0**) Gecko/20100101 Firefox/110。

https://bugzilla.mozilla.org/show\_bug.cgi?id=1805967

文章来源: https://www.solidot.org/story?sid=73776
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)
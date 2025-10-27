---
title: Obfuscating C2 Traffic with Google Cloud Functions
url: https://buaq.net/go-157012.html
source: unSafe.sh - 不安全
date: 2023-04-05
fetch_date: 2025-10-04T11:29:20.226366
---

# Obfuscating C2 Traffic with Google Cloud Functions

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

![](https://8aqnet.cdn.bcebos.com/fa6209259dafb816058fcb9edf04a129.jpg)

Obfuscating C2 Traffic with Google Cloud Functions

04 April 2023IntroductionIn a previous article Maldoc Transfers in the Google Cloud, I wrote about
*2023-4-4 21:38:35
Author: [fortynorthsecurity.com(查看原文)](/jump-157012.htm)
阅读量:24
收藏*

---

04 April 2023

#### Introduction

In a previous article [Maldoc Transfers in the Google Cloud](https://fortynorthsecurity.com/blog/redirecting-maldoc-transfers-in-the-cloud/), I wrote about using a Google Cloud Provider serverless function to serve malicious documents from a Google controlled domain. After writing that article, I continued to play explore what Google Cloud could provide to offensive security practitioners.

We've previously published a [blog post](https://fortynorthsecurity.com/blog/azure-functions-functional-redirection/) as well as a [Proof-of-Concept](https://github.com/FortyNorthSecurity/FunctionalC2) for using Azure serverless functions as C2 redirectors. Using this previous research as a jumping-off point, I've ported this redirector function to Google Cloud Provider as well. The PoC is available from the [FunctionalC2 github repository](https://github.com/FortyNorthSecurity/FunctionalC2).

---

文章来源: https://fortynorthsecurity.com/blog/obfuscating-c2-traffic-with-google-cloud-functions/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)
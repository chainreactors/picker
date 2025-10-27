---
title: Maldoc Transfers in the Google Cloud
url: https://buaq.net/go-151762.html
source: unSafe.sh - 不安全
date: 2023-03-03
fetch_date: 2025-10-04T08:30:44.317452
---

# Maldoc Transfers in the Google Cloud

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

![](https://8aqnet.cdn.bcebos.com/4261fb9663b1b144fcb86c606f44035c.jpg)

Maldoc Transfers in the Google Cloud

02 March 2023On a recent red team engagement, we faced the challenge of serving a backdoored Excel
*2023-3-2 23:16:48
Author: [fortynorthsecurity.com(查看原文)](/jump-151762.htm)
阅读量:20
收藏*

---

02 March 2023

On a recent red team engagement, we faced the challenge of serving a backdoored Excel document as part of a social engineering campaign against an environment using very strong reputation-based URL filtering. Although [we](https://fortynorthsecurity.com/blog/azure-functions-functional-redirection) and [others](https://www.trustedsec.com/blog/front-validate-and-redirect/) have written in detail about abusing serverless cloud functions to redirect C2 traffic, this time we needed the reverse: a way to serve a file to the victim's machine while bypassing their environment's domain reputation controls. What we came up with was a simple Python function that fetches data from any attacker specified URL and serves it to a victim visiting a Google-controlled domain. This post will walk through the procedures we used to successfully bypass our target's domain reputation filtering service.

### Setup

Google Cloud currently allows the deployment of HTTP functions in Node.js, Python, Go, Java, C#, Ruby, and PHP.  Most of this section is based off of their great [quickstart documentation](https://cloud.google.com/functions/docs/create-deploy-http-python). We are using Python for this example.

This walkthrough assumes the reader has already created a Google Cloud account.

---

文章来源: https://fortynorthsecurity.com/blog/redirecting-maldoc-transfers-in-the-cloud/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)
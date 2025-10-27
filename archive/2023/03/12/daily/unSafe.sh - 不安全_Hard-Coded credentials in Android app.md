---
title: Hard-Coded credentials in Android app
url: https://buaq.net/go-153021.html
source: unSafe.sh - 不安全
date: 2023-03-12
fetch_date: 2025-10-04T09:21:32.195086
---

# Hard-Coded credentials in Android app

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

Hard-Coded credentials in Android app

In the Android, application it is a package called apk(android package kit), it is similar to a zip-
*2023-3-11 22:31:59
Author: [infosecwriteups.com(查看原文)](/jump-153021.htm)
阅读量:22
收藏*

---

In the Android, application it is a package called apk(android package kit), it is similar to a zip-like format to extract the data from apk, we use [apktool](https://ibotpeaches.github.io/Apktool/) and JADX-GUI.

> [JADX-GUI](https://github.com/skylot/jadx) is a very awesome tool to extract the data from apk and view the decompiled code. If we normally extract the data file, we couldn’t able to read. It is a hard thing to read. Using JADX we can able to easily understand code.

Photo by [Denny Müller](https://unsplash.com/%40redaquamedia?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)

Every app had the strings.xml, which is a file used to store the strings in the application package.

**How I found the API Key disclosure issue!**

1. Download the apk file from the internet(which app you want to test)

2. Open JADX -> File ->Add File -> Click the test.apk It takes some time to decompile it (depending on your system environment)

3. Scroll Down the left side can able to see Resources -> resources.arsc -> res -> values -> strings.xml

4. Sometimes it may have API Keys, AWS Keys, Default passwords, admin creds, etc

**Note:-**

If you find any API Key please refer [to this](https://github.com/streaak/keyhacks) git repository to explain the impact

Linkedin : [Barath Stalin](https://www.linkedin.com/in/barathstalin/)

文章来源: https://infosecwriteups.com/what-is-in-the-strings-xml-b204b2e9bd67?source=rss----7b722bfd1b8d--bug\_bounty
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)
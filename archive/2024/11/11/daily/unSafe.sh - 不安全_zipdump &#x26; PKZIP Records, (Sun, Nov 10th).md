---
title: zipdump &#x26; PKZIP Records, (Sun, Nov 10th)
url: https://buaq.net/go-271962.html
source: unSafe.sh - 不安全
date: 2024-11-11
fetch_date: 2025-10-06T19:13:30.572118
---

# zipdump &#x26; PKZIP Records, (Sun, Nov 10th)

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

![](https://8aqnet.cdn.bcebos.com/854ebab98ff217ae3b903703f8f12ef4.jpg)

zipdump &#x26; PKZIP Records, (Sun, Nov 10th)

In yesterday's diary entry "zipdump & Evasive ZIP Concatenation" I showed how one can inspect the P
*2024-11-10 23:14:6
Author: [isc.sans.edu(查看原文)](/jump-271962.htm)
阅读量:13
收藏*

---

In yesterday's diary entry "[zipdump & Evasive ZIP Concatenation](https://isc.sans.edu/diary/zipdump%20%26%20Evasive%20ZIP%20Concatenation/31426)" I showed how one can inspect the PKZIP records that make up a ZIP file.

My tool [zipdump.py](https://github.com/DidierStevens/DidierStevensSuite/blob/master/zipdump.py) can also inspect the data of PKZIP file records, and decompress it (not decrypt it).

To select the data of a PKZIP file record, use option -s data. Here we also use option -a to do a hex-ascii dump of the data:

![](https://isc.sans.edu/diaryimages/images/20241110-084718.png)

When option -d is used (to perform a binary dump), only the raw data is send to stdout, no other metadata:

![](https://isc.sans.edu/diaryimages/images/20241110-085753.png)

And when option -s decompress is used, the data is decompressed (only INFLATE is supported):

![](https://isc.sans.edu/diaryimages/images/20241110-085816.png)

These options could also be helpful for corrupt ZIP files.

Didier Stevens

文章来源: https://isc.sans.edu/diary/rss/31428
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)
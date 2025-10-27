---
title: Google Earth Zero Features Found error
url: https://buaq.net/go-144986.html
source: unSafe.sh - 不安全
date: 2023-01-11
fetch_date: 2025-10-04T03:30:56.194552
---

# Google Earth Zero Features Found error

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

Google Earth Zero Features Found error

I was getting this error message when importing CSV file with Lat/Long in Dec
*2023-1-10 23:58:20
Author: [acassis.wordpress.com(查看原文)](/jump-144986.htm)
阅读量:699
收藏*

---

I was getting this error message when importing CSV file with Lat/Long in Decimal Degrees on Google Earth: “Found zero features in file”.

It was strange because when I was going to File -> Import the Google Earth was displaying the data correctly in the preview.

After some investigation I fixed the issue and it was cause because these two things:

1. In the import screen click on Next and then Next again, in the Specify Field Types use type “string” to Latitude and Longitude instead of default “floating point”.
2. My CSV file had a space after comma: “Name, XX.XXXXXX, XX.XXXXXX”. It should be: “Name,XX.XXXXXX,XX.XXXXXX”

After fixing these issues everything worked fine.

文章来源: https://acassis.wordpress.com/2023/01/10/google-earth-zero-features-found-error/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)
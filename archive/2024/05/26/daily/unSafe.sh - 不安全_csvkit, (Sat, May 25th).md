---
title: csvkit, (Sat, May 25th)
url: https://buaq.net/go-241566.html
source: unSafe.sh - 不安全
date: 2024-05-26
fetch_date: 2025-10-06T16:49:10.608424
---

# csvkit, (Sat, May 25th)

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

![](https://8aqnet.cdn.bcebos.com/40ab6ec5d458c2825fbc319a67ef0344.jpg)

csvkit, (Sat, May 25th)

Published: 2024-05-25Last Updated: 2024-05-25 08:08:10 UTCby Didier Stevens (Version: 1)After r
*2024-5-25 16:8:10
Author: [isc.sans.edu(查看原文)](/jump-241566.htm)
阅读量:5
收藏*

---

**Published**: 2024-05-25

After reading my diary entry "[Checking CSV Files](https://isc.sans.edu/diary/Checking%2BCSV%2BFiles/30796)", a reader informed me that CSV toolkit [csvkit](https://github.com/wireservice/csvkit) also contains a command to check CSV files: [csvstat.py](https://github.com/wireservice/csvkit/blob/master/csvkit/utilities/csvstat.py).

Here is this tool running on the same CSV file I used in my diary entry:

![](https://isc.sans.edu/diaryimages/images/20240520-142856.png)

![](https://isc.sans.edu/diaryimages/images/20240520-143024.png)

csvkit has a lot of dependencies, it took my quite some effort to install it on a machine without Internet connection. I had to download, transfer and install 50+ packages.

Didier Stevens
Senior handler
[blog.DidierStevens.com](http://blog.DidierStevens.com)

文章来源: https://isc.sans.edu/diary/rss/30938
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)
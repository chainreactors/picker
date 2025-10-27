---
title: Riccardo Mottola: GNUStep now has badges
url: https://buaq.net/go-173619.html
source: unSafe.sh - 不安全
date: 2023-08-04
fetch_date: 2025-10-04T11:59:58.406472
---

# Riccardo Mottola: GNUStep now has badges

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

Riccardo Mottola: GNUStep now has badges

Finally I got around implementing and committing badge support in GNUStep! I think it is one of the
*2023-8-3 22:36:3
Author: [multixden.blogspot.com(查看原文)](/jump-173619.htm)
阅读量:10
收藏*

---

Finally I got around implementing and committing badge support in [GNUStep](http://www.gnustep.org)! I think it is one of the fine additions Apple did to the original OpenStep spec

While Apple had it since MacOS 10.5, GNUstep didn't and GNUMail had to manage 3 different code paths: One for GNUstep, one for 10.4 Mac and one for 10.5 and later which I implemented myself, since GNUMail originally didn't have it.
First, I with Fred and Richard brought up GNUmail code to match the 10.4 code path, which is generic and just draws the Icon. To do this, I had to change the code, since ImageReps are not writable in GNUstep, so NSCustomImageRep had to be used and it woks both on GNUstep and on Mac.

Later, proper badges support has been added in GNUstep, here the look with [GNUMail](https://www.nongnu.org/gnustep-nonfsf/gnumail/) and with a small test application, which is ported directly from Mac and compiled using xcode [buildtool](https://github.com/gnustep/libs-xcode).

![](data:image/png;base64...)

As we were tried to match certain Apple behaviours, like ellipsis, but also an addition: I made the colors themable.

Here a nice screenshot of the two things working with the *Sonne* [theme](https://gap.nongnu.org/themes/index.html). Thematic was enhanced to handle the badgeColor with its three shades matching the ring, text and badge background.

![](data:image/png;base64...)

文章来源: http://multixden.blogspot.com/2023/08/gnustep-now-has-badges.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)
---
title: 免升级Xcode 解决 “Unsupported OS version”
url: https://buaq.net/go-147059.html
source: unSafe.sh - 不安全
date: 2023-01-30
fetch_date: 2025-10-04T05:09:48.631439
---

# 免升级Xcode 解决 “Unsupported OS version”

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

免升级Xcode 解决 “Unsupported OS version”

每次iOS系统更新需要对应升级Xcode都是一件很恼人的事情。 可以通过下载所需的iOS Device Suppoert文件可以快速
*2023-1-29 17:43:10
Author: [www.uedbox.com(查看原文)](/jump-147059.htm)
阅读量:33
收藏*

---

每次iOS系统更新需要对应升级Xcode都是一件很恼人的事情。 可以通过下载所需的iOS Device Suppoert文件可以快速解决“Unsupported iOS version”问题。 每个iOS版本支持文件都很小，大约在20MB以下。可以通过以下方法快速应对此问题。

1. 前往[github.com/iGhibli/iOS…](https://github.com/iGhibli/iOS-DeviceSupport) 下载所需要的对应iOS版本的支持文件
2. 解压文件，得到名为iOS版本的目录（如14.6）
3. 将整个目录复制到如下路径 /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/DeviceSupport/
4. 重启Xcode

文章来源: https://www.uedbox.com/post/68706/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)
---
title: Certificate expiration affecting macOS App Store and VPP apps
url: https://buaq.net/go-149215.html
source: unSafe.sh - 不安全
date: 2023-02-14
fetch_date: 2025-10-04T06:29:20.004082
---

# Certificate expiration affecting macOS App Store and VPP apps

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

![](https://8aqnet.cdn.bcebos.com/6cad36bedb7a221539dcaaee19630eca.jpg)

Certificate expiration affecting macOS App Store and VPP apps

Home > Apple Volume Purchase Program, Mac administration, macOS > Certificate expiration aff
*2023-2-13 22:49:26
Author: [derflounder.wordpress.com(查看原文)](/jump-149215.htm)
阅读量:34
收藏*

---

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Apple Volume Purchase Program](https://derflounder.wordpress.com/category/apple-volume-purchase-program/), [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/) > Certificate expiration affecting macOS App Store and VPP apps

## Certificate expiration affecting macOS App Store and VPP apps

Mac admins who have previously installed macOS apps from the Mac App Store (MAS) or the Volume Purchase Program (VPP) may be seeing some of those apps displaying warning messages on launch that the application is damaged.

![Screenshot 2023 02 07 at 5 37 40 PM](https://derflounder.files.wordpress.com/2023/02/screenshot-2023-02-07-at-5.37.40-pm.png?w=260&h=244 "Screenshot 2023-02-07 at 5.37.40 PM.png")

When observed, this behavior may be appearing because the certificates Apple has been using to digitally sign apps have recently expired, on February 6th 2023 or February 7th 2023. (Both expiration dates have appeared in signing certificates on the apps I’ve checked.)

![Screenshot 2023 02 13 at 11 39 25](https://derflounder.files.wordpress.com/2023/02/screenshot-2023-02-13-at-11.39.25.png?w=600&h=401 "Screenshot 2023-02-13 at 11.39.25.png")

When the code signing is detected as being invalid, Apple’s security tools are blocking launch as a consequence. In most cases, it appears that the code signing is still appearing as valid despite being past the expiration date.

---

文章来源: https://derflounder.wordpress.com/2023/02/13/certificate-expiration-affecting-macos-app-store-and-vpp-apps/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)
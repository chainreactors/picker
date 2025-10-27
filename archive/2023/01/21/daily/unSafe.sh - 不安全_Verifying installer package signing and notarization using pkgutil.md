---
title: Verifying installer package signing and notarization using pkgutil
url: https://buaq.net/go-146363.html
source: unSafe.sh - 不安全
date: 2023-01-21
fetch_date: 2025-10-04T04:27:10.296380
---

# Verifying installer package signing and notarization using pkgutil

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

![](https://8aqnet.cdn.bcebos.com/ac9880d50f0ddca21276a03b00755fdb.jpg)

Verifying installer package signing and notarization using pkgutil

Home > Mac administration, macOS, Notarization > Verifying installer package signing and not
*2023-1-20 23:37:30
Author: [derflounder.wordpress.com(查看原文)](/jump-146363.htm)
阅读量:24
收藏*

---

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/), [Notarization](https://derflounder.wordpress.com/category/notarization/) > Verifying installer package signing and notarization using pkgutil

## Verifying installer package signing and notarization using pkgutil

Recently I needed a way to verify whether an installer package was signed and notarized. I’ve been using Apple’s [stapler](https://keith.github.io/xcode-man-pages/stapler.1.html) tool as my usual go-to for verifying notarization. However, the **stapler** tool needs for Xcode to to be installed and I needed a solution that worked regardless of Xcode or the Xcode Command Line Tools being installed on the Mac in question.

After some digging, I found that [pkgutil](https://www.manpagez.com/man/1/pkgutil/)‘s **check-signature** function on macOS Monterey and later works great for this and doesn’t have any dependencies on Xcode or the Xcode Command Line Tools. The **pkgutil** tool is installed as part of macOS and the **check-signature** function displays the following on Monterey and later:

**If a package is not signed:**

![Screenshot 2023 01 20 at 10 25 38 AM](https://derflounder.files.wordpress.com/2023/01/screenshot-2023-01-20-at-10.25.38-am.png?w=596&h=104 "Screenshot 2023-01-20 at 10.25.38 AM.png")

**If a package is signed with a certificate:**

![Screenshot 2023 01 20 at 10 24 52 AM](https://derflounder.files.wordpress.com/2023/01/screenshot-2023-01-20-at-10.24.52-am.png?w=599&h=419 "Screenshot 2023-01-20 at 10.24.52 AM.png")

**If a package is signed with a certificate and trusted by Apple’s notarization service:**

![Screenshot 2023 01 20 at 10 23 29 AM](https://derflounder.files.wordpress.com/2023/01/screenshot-2023-01-20-at-10.23.29-am.png?w=600&h=436 "Screenshot 2023-01-20 at 10.23.29 AM.png")

To use the **check-signature** function, you should be able to use the command shown below (substituting */path/to/installer.pkg* with the actual directory path of the installer package you want to check.):

文章来源: https://derflounder.wordpress.com/2023/01/20/verifying-installer-package-signing-and-notarization-using-pkgutil/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)
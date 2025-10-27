---
title: 解决真机调试Failed to prepare device for development.报错,Xcode 不能安装APP
url: https://buaq.net/go-147058.html
source: unSafe.sh - 不安全
date: 2023-01-30
fetch_date: 2025-10-04T05:09:48.009966
---

# 解决真机调试Failed to prepare device for development.报错,Xcode 不能安装APP

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

解决真机调试Failed to prepare device for development.报错,Xcode 不能安装APP

错误信息Failed to prepare device for development. This operati
*2023-1-29 17:52:51
Author: [www.uedbox.com(查看原文)](/jump-147058.htm)
阅读量:28
收藏*

---

## 错误信息

### **Failed to prepare device for development.**

This operation can fail **if** the version **of** the OS **on** the device is incompatible **with** the installed version **of** Xcode. You may also need **to** restart your mac and device **in** **order** **to** correctly detect compatibility.

不能装APP，说版本不对。

## 解决

1. Check /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/DeviceSupport/ for directory name 15.4 (your iOS version).
2. If the directory is missing download support files for 15.4 (your iOS version) from [github.com/filsv/iPhon…](https://github.com/filsv/iPhoneOSDeviceSupport) and place it in the above path.
3. Restart Xcode.

检查`/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/DeviceSupport/` 这里面是不是有IOS对应版本的文件夹, 如果没有，下载装进去！

下载地址：[github.com/filsv/iPhon…](https://github.com/filsv/iPhoneOSDeviceSupport)

或者地址（这个更全面）：[https://github.com/iGhibli/iOS-DeviceSupport/](https://github.com/iGhibli/iOS-DeviceSupport/tree/master/DeviceSupport)

重启Xcode，解决了！

这个其实和[免升级Xcode 解决 “Unsupported OS version”](https://www.uedbox.com/post/68706/)是相同的解决方法。

文章来源: https://www.uedbox.com/post/68707/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)
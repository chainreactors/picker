---
title: ADB指令-修改休眠时间和屏幕亮度_yinxianze的博客-CSDN博客_adb设置休眠时间
url: https://buaq.net/go-141766.html
source: unSafe.sh - 不安全
date: 2022-12-29
fetch_date: 2025-10-04T02:39:21.066066
---

# ADB指令-修改休眠时间和屏幕亮度_yinxianze的博客-CSDN博客_adb设置休眠时间

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

ADB指令-修改休眠时间和屏幕亮度\_yinxianze的博客-CSDN博客\_adb设置休眠时间

*2022-12-28 22:57:15
Author: [blog.csdn.net(查看原文)](/jump-141766.htm)
阅读量:361
收藏*

---

![](https://csdnimg.cn/release/blogv2/dist/pc/img/original.png)

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](https://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

#获取当前亮度值

adb shell settings get system screen\_brightness

30

#更改亮度值(亮度值在0—255之间)

adb shell settings put system screen\_brightness

150

#获取屏幕休眠时间

adb shell settings get system screen\_off\_timeout

15000

#更改休眠时间，10分钟

adb shell settings put system screen\_off\_timeout

600000

#获取日期时间选项中通过网络获取时间的状态，1为允许、0为不允许

adb shell settings get global auto\_time

1

#更改该状态，从1改为0

adb shell settings put global auto\_time

0

文章来源: https://blog.csdn.net/yinxianze/article/details/123201276
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)
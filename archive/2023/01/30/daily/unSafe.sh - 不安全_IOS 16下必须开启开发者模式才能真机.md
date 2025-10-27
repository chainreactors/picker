---
title: IOS 16下必须开启开发者模式才能真机
url: https://buaq.net/go-147071.html
source: unSafe.sh - 不安全
date: 2023-01-30
fetch_date: 2025-10-04T05:09:43.875741
---

# IOS 16下必须开启开发者模式才能真机

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

![](https://8aqnet.cdn.bcebos.com/fa94bde7ad756c2b78a1834f7642dec5.jpg)

IOS 16下必须开启开发者模式才能真机

IOS 16下真机调试报错Failed to prepare device for development问题描述在
*2023-1-29 19:24:42
Author: [www.uedbox.com(查看原文)](/jump-147071.htm)
阅读量:42
收藏*

---

## IOS 16下真机调试报错Failed to prepare device for development

### 问题描述

在**IOS 16**以前的版本，出现**Failed to prepare device for development**错误一般是DeviceSupport问题，但在升级IOS 16后，根据《[解决真机调试Failed to prepare device for development.报错,Xcode 不能安装APP](https://www.uedbox.com/post/68707/)》已经安装了16.2版本，但依然无法真机调试，还是提示**Failed to prepare device for development**错误。

### 原因

在IOS 16后，加入了“开发者模式”且默认是关闭的，如果要真机调试或安装IPA，就必须先手动打开开发者模式才行。

![IOS 16下必须开启开发者模式才能真机](https://www.uedbox.com/wp-content/uploads/2023/01/8800514.png)

### 解决

知道问题了，那打开就行，路径在： iPhone “`设置->隐私与安全性->安全性`”，如果你能在这里看到“开发者模式”这个选项，点击并开启就行，它会要求你重启，重启后弹窗点打开就完成了。

但大奇怪的设计又出现了，很多IOS 16设备竟然看不到开发者模式这个设置项？比如笔者。如何打开呢？看文章《[升级 iOS 16 后没有开发者模式怎么办？如何打开开发者模式？](https://www.uedbox.com/post/68710/)》。后面的步骤是一样的。

文章来源: https://www.uedbox.com/post/68709/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)
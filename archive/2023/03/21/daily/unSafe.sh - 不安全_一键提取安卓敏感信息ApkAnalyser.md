---
title: 一键提取安卓敏感信息ApkAnalyser
url: https://buaq.net/go-154413.html
source: unSafe.sh - 不安全
date: 2023-03-21
fetch_date: 2025-10-04T10:06:16.036940
---

# 一键提取安卓敏感信息ApkAnalyser

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

一键提取安卓敏感信息ApkAnalyser

最后编辑时间: 2023-03-20（New Article）
*2023-3-20 23:42:14
Author: [blog.upx8.com(查看原文)](/jump-154413.htm)
阅读量:56
收藏*

---

最后编辑时间: 2023-03-20（New Article）

一键提取安卓应用中可能存在的敏感信息。

* 20200304

  修复“apkPath is not defined”，参数带进来的路径忘记赋值直接写了...

Windows:[releases](https://github.com/TheKingOfDuck/ApkAnalyser/releases/download/1.0/apkAnalyser.zip)

✔️即兴开发，Enjoy it~~

### 用法

* 懒人做法，将所有app放到程序自动创建的apps目录，再运行主程序就好了，不用加参数。

### 功能

目前提取了APK内:

* 所有字符串
* 所有URLs
* 所有ip
* 可能是hash值的字符串
* 存在的敏感词（如oss.aliyun）
* 可能是accessKey的值

[![](https://camo.githubusercontent.com/7260ada421c98f72c069afb64d73db3ad285efa94d482929133af3a1dab60dbb/68747470733a2f2f626c6f672e677a7365632e6f72672f706f73742d696d616765732f313538323239313938373938322e706e67)](https://camo.githubusercontent.com/7260ada421c98f72c069afb64d73db3ad285efa94d482929133af3a1dab60dbb/68747470733a2f2f626c6f672e677a7365632e6f72672f706f73742d696d616765732f313538323239313938373938322e706e67)

使用Python开发，依赖于apkutils模块，可执行文件使用pyinstaller打包。

下载地址：<https://wwtc.lanzoum.com/iRUL20qn411g>

文章来源: https://blog.upx8.com/3318
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)
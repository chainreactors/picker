---
title: 记一次chrome插件调试
url: https://www.anquanke.com/post/id/282224
source: 安全客-有思想的安全新媒体
date: 2022-10-29
fetch_date: 2025-10-03T21:11:30.270659
---

# 记一次chrome插件调试

首页

阅读

* [安全资讯](https://www.anquanke.com/news)
* [安全知识](https://www.anquanke.com/knowledge)
* [安全工具](https://www.anquanke.com/tool)

活动

社区

学院

安全导航

内容精选

* [专栏](/column/index.html)
* [精选专题](https://www.anquanke.com/subject-list)
* [安全KER季刊](https://www.anquanke.com/discovery)
* [360网络安全周报](https://www.anquanke.com/week-list)

# 记一次chrome插件调试

阅读量**390338**

发布时间 : 2022-10-28 14:30:03

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

![]()

## 前言

因为谷歌翻译退出中国，导致翻译不太好用了，所以去谷歌商店找了个用着还不错的翻译插件，没想到发现其全文翻译的功能每天只能使用3次，不限使用需要开会员。之前还没做过插件调试，这次就简单试试水，最后成功达到了目的，遂记录下。

## 调试过程

### 思路

因为这个插件每天只能全文翻译三次，当超过次数后会弹窗提示，导致功能不可用。猜测肯定是哪里做了一个计数，同时还有会员、功能翻译次数的判断，那么思路无非就是修改这个判断的结果，从而达到无限制使用的目的

### 前置知识

Chrome插件基本由mainfest.json, content-script, background.js, popup组成

mainfest.json: 插件的配置文件

content-script: 用来向页面注入css和js

background.js: 常驻于浏览器的一个脚本, 始终在运行

popup: 即点击插件的logo以后弹出的窗口

### debug

打开chrome，在源码栏选择content scripts栏，全局搜索提示“非会员每天”定位到判断函数，随便在上面下个断点

![]()

点击插件翻译按钮，简单跟了几步就发现一个关键判断，这里的参数值不用关心是如何生成的，只需要知道这里判断return的结果会对上面的判断产生影响

![]()

其中一个判断值就是i这个对象

![]()

i这个对象里面有个字典，其中pageTranslateLimit这个值中的times很关键

只需要将它每次修改为0，那么上面的次数判断就能绕过，充不充会员也就没啥意义了

### 修改覆盖

在chrome的地址栏输入chrome://version/后, 可以看到你的chrome根目录

![]()

在该目录下的Extensions是插件目录，右键插件图标管理扩展程序就能看到插件的id值

![]()

将原目录的文件拷出来，然后修改99.js文件，在关键函数下重新赋值即可

![]()

然后删除原版插件，打开开发者模式，加载修改后的文件

![]()

然后就能愉快的无限制使用翻译功能了

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**雷石安全实验室**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/282224](/post/id/282224)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [Chrome](/tag/Chrome)

**+1**0赞

收藏

![](https://p2.ssl.qhimg.com/t01ebe472d127128939.png)雷石安全实验室

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t01ebe472d127128939.png)](/member.html?memberId=148196)

[雷石安全实验室](/member.html?memberId=148196)

欢迎关注公众号@雷石安全实验室 安全工作者不定期分享渗透、APT、企业安全建设等新鲜干货

* 文章
* **48**

* 粉丝
* **44**

### TA的文章

* ##### [frida inlinehook 巧解Android逆向题](/post/id/286239)

  2023-02-15 10:30:45
* ##### [frida inlinehook 巧解Android逆向题](/post/id/284343)

  2023-01-03 15:30:42
* ##### [frida hook native层巧解Android逆向题](/post/id/283461)

  2022-12-01 10:30:06
* ##### [webshell免杀之函数与变量玩法](/post/id/282736)

  2022-11-07 14:00:27
* ##### [一道Android逆向题的取巧解题思路](/post/id/282006)

  2022-10-31 14:30:32

### 相关文章

* ##### [PyPI包通过安装Chrome扩展窃取加密货币](/post/id/286434)

  2023-02-16 10:30:31
* ##### [Chrome支持无密码身份验证Passkeys](/post/id/284253)

  2022-12-12 11:30:26
* ##### [303个！Chrome或成2022年漏洞最多的浏览器](/post/id/281442)

  2022-10-10 11:00:01
* ##### [Internet下载管理器？假Chrome插件被安装200000次](/post/id/278815)

  2022-08-25 15:30:14
* ##### [Chrome V8命令执行漏洞（CVE-2022-1310）分析](/post/id/276964)

  2022-08-09 14:30:04
* ##### [CVE-2021-21230](/post/id/269872)

  2022-03-14 10:30:05
* ##### [Chrome-V8 CVE-2021-30588](/post/id/269014)

  2022-03-07 10:30:45

### 热门推荐

文章目录

* [前言](#h2-0)
* [调试过程](#h2-1)
  + [思路](#h3-2)
  + [前置知识](#h3-3)
  + [debug](#h3-4)
  + [修改覆盖](#h3-5)

![](https://p0.qhimg.com/t11098f6bcd5614af4bf21ef9b5.png)

安全KER

* [关于我们](/about)
* [联系我们](/note/contact)
* [用户协议](/note/protocol)
* [隐私协议](/note/privacy)

商务合作

* [合作内容](/note/business)
* [联系方式](/note/contact)
* [友情链接](/link)

内容需知

* [投稿须知](https://www.anquanke.com/contribute/tips)
* [转载须知](/note/repost)
* 官网QQ群：568681302

合作单位

* [![安全KER](https://p0.ssl.qhimg.com/t01592a959354157bc0.png)](http://www.cert.org.cn/)
* [![安全KER](https://p0.ssl.qhimg.com/t014f76fcea94035e47.png)](http://www.cnnvd.org.cn/)

Copyright © 北京奇虎科技有限公司 三六零数字安全科技集团有限公司 安全KER All Rights Reserved [京ICP备08010314号-66](https://beian.miit.gov.cn/)[![](https://icon.cnzz.com/img/pic.gif)](https://www.cnzz.com/stat/website.php?web_id=1271278035 "站长统计")

微信二维码

**X**![安全KER](https://p0.ssl.qhimg.com/t0151209205b47f2270.jpg)
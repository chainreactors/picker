---
title: frida hook native层巧解Android逆向题
url: https://www.anquanke.com/post/id/283461
source: 安全客-有思想的安全新媒体
date: 2022-12-02
fetch_date: 2025-10-04T00:16:08.041147
---

# frida hook native层巧解Android逆向题

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

# frida hook native层巧解Android逆向题

阅读量**420650**

发布时间 : 2022-12-01 10:30:06

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

![]()

## 前言

最近还是老朋友发来一道Android逆向题，挺有意思，用frida hook native层解出了题目，记录下学习的过程。

## Java层静态分析

直接拖进jadx，MainActivity内容如下：

![]()

代码不多，基本流程就是，获取输入字符，通过一个反射调用（调用的函数是加密了，要用native层的decode解密）处理了一下输入字符串，然后通过check函数进行判断，前面的是处理过的输入字符串，后面的一串应该是密钥之类的。

![]()

## firda hook java层

首先比较关心decode解密的数据是啥，直接hook一下，可以看到反射调用的是base64，那么后续传入比较的字符串就是base64处理过了，我们解出来的flag应该也是要base64解密一次。
看到还有一串“Hikari#a0344y3y#1930121”，应该是传入check的密钥。

![]()

接下来比较关心的就是check函数是怎么处理输入的字符串。

## Native层静态分析

直接解压把libcheck.so拖入ida。
发现是静态注册的，直接能在导出函数里找到，关键步骤还是再最后几行，可以看到是通过RC4进行了加密，与一个数组进行了比较判断，跟进do\_crypt函数后，处理伪码后如下：

![]()

那么这个数组的内容应该就是要找的加密后的flag。

![]()

## Frida hook native

记录下函数地址，关掉ida。

![]()

直接上frida，先来hook一下这个函数，看看输入输出，这里从上面可以看到是arm指令后面计算函数地址不需要加1，打印下输入输出的内容。

![]()

动态调试起来输入结果如下：

![]()

能成功hook了，刚好这里是通过RC4算法进行的加密，那么我们只需要把输入的内容替换成上面找到的flag的密文，就应该能得到真实的flag（base64编码后的）。
通过frida操作内存，把输入的参数arg[1]hook并覆写内存成我们密文的内容，这里需要注意一点，你输入的文本尽可能长一点，不然获取到的结果不全。
打印内存得到了一串字符串，base64解码一下，得到flag。

## 总结

题目设置刚刚好，后面看了别人的wp，发现rc4是魔改过的，但是这里是rc4，那么就可以这么取巧去做一下，运气也不错，直接做了出来，主要还是学习一下frida对native层的hook。

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**雷石安全实验室**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/283461](/post/id/283461)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [逆向工程](/tag/%E9%80%86%E5%90%91%E5%B7%A5%E7%A8%8B)

**+1**0赞

收藏

![](https://p2.ssl.qhimg.com/t01ebe472d127128939.png)雷石安全实验室

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

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

* ##### [WMCTF 2022 挑战赛 chess writeup](/post/id/278828)

  2022-08-25 15:30:28
* ##### [Android Native层逆向探索](/post/id/273725)

  2022-06-02 10:30:56
* ##### [通过手动给upx去壳简单了解逆向](/post/id/272639)

  2022-05-06 10:30:50
* ##### [苹果无线生态系统安全性指南](/post/id/239355)

  2022-01-20 10:00:30
* ##### [H2Miner挖矿蠕虫新变种](/post/id/259034)

  2021-11-15 15:30:11
* ##### [静态注入PE导入表](/post/id/253112)

  2021-09-16 16:30:45
* ##### [2021WMCTF中的Re1&Re2](/post/id/252318)

  2021-09-10 16:30:51

### 热门推荐

文章目录

* [前言](#h2-0)
* [Java层静态分析](#h2-1)
* [firda hook java层](#h2-2)
* [Native层静态分析](#h2-3)
* [Frida hook native](#h2-4)
* [总结](#h2-5)

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
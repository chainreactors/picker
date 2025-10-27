---
title: 一道Android逆向题的取巧解题思路
url: https://www.anquanke.com/post/id/282006
source: 安全客-有思想的安全新媒体
date: 2022-11-01
fetch_date: 2025-10-03T21:24:43.201921
---

# 一道Android逆向题的取巧解题思路

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

# 一道Android逆向题的取巧解题思路

阅读量**406257**

发布时间 : 2022-10-31 14:30:32

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

![]()

## 前言

最近朋友发来一道Android逆向题，挺有意思，花时间研究了一下，在算法逆不出来的情况下（我太菜），用frida取巧解出了题目，记录下学习的过程。

## 抛出问题

安装打开题目发现是要求输入字符串。

![]()

随便输入提示错误。

![]()

## Java层静态分析

拖进jadx，先分析下java层。里面类有点多，估计是垃圾代码，直接看Androidmanifest文件找到启动的Activity去分析。

![]()

找到对应的类，一看上面就是一个byte数组，一个loadLibrary，一个native函数，so逆向跑不了。
下面看到对应的按钮点击事件。

![]()

继续跟进去看，找到了核心的逻辑，是通过encry函数处理输入字符串，返回一个byte数组，然后和前面的byte数组比较是否相等，那前面的byte数组应该就是加密后的flag，我们要做的就是逆出来。

![]()

## Native层静态分析

encry是写在native层，对apk解包，取出对应的so（libencry.so）拖进ida。
可以看到是静态注册的，直接能在导出函数里找到。

![]()

转成C伪码，看一下，我还是太菜，不会。

![]()

动态调了下，也没调明白，我太菜了。

## Frida动态hook

关掉ida，直接上frida，先来hook一下这个函数，看看输入输出。
可以hook到，输入的参数以及输出的byte数组

![]()

这里开始测试（猜），flag格式一般就是flag{xxxxxx},我输入“flag{”进行测试，hook结果如下：

![]()

对比Java层中的byte数组，发现前几位已经能对上了，但是最后一位对不上，应该是因为so层中的加密算法后一位会影响前一位。
到这里就已经可以get到一个比较取巧的思路了，写个rpc脚本调用一位一位爆破flag。

## Frida rpc调用

直接hook encry函数，主动调用。
js部分如下：

![]()

python调用，爆破部分如下：

![]()

一位一位遍历所有可打印字符跑起来。
成功获取（爆出）到flag。

![]()

## 总结

常规做法做不出来，只能取巧，题目设置也刚好，最终还是以结果为导向，能解题的方法总是好方法。这里只是举例了用frida，实际上也可以使用unidbg去主动调用so进行爆破，原理是差不多的。

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**雷石安全实验室**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/282006](/post/id/282006)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [移动安全](/tag/%E7%A7%BB%E5%8A%A8%E5%AE%89%E5%85%A8)

**+1**0赞

收藏

![](https://p2.ssl.qhimg.com/t01ebe472d127128939.png)雷石安全实验室

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

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

* ##### [为什么你的 Wi-Fi 路由器可以兼作 Apple AirTag](/post/id/297701)

  2024-07-09 19:34:08
* ##### [三星 Galaxy 推出新的 Auto Blocker 反恶意软件功能](/post/id/291153)

  2023-11-01 11:49:21
* ##### [frida inlinehook 巧解Android逆向题](/post/id/286239)

  2023-02-15 10:30:45
* ##### [iOS静态方式绕过svc反动态调试](/post/id/285183)

  2023-01-09 14:30:35
* ##### [英媒：英国大臣的手机或可在20分钟内被黑客破解](/post/id/285095)

  2023-01-05 11:45:59
* ##### [frida inlinehook 巧解Android逆向题](/post/id/284343)

  2023-01-03 15:30:42
* ##### [知道手机投屏可以看剧，不知道还能被用来窃取隐私！](/post/id/282936)

  2022-11-09 17:30:51

### 热门推荐

文章目录

* [前言](#h2-0)
* [抛出问题](#h2-1)
* [Java层静态分析](#h2-2)
* [Native层静态分析](#h2-3)
* [Frida动态hook](#h2-4)
* [Frida rpc调用](#h2-5)
* [总结](#h2-6)

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
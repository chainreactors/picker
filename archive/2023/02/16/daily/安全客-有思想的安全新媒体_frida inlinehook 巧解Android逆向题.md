---
title: frida inlinehook 巧解Android逆向题
url: https://www.anquanke.com/post/id/286239
source: 安全客-有思想的安全新媒体
date: 2023-02-16
fetch_date: 2025-10-04T06:45:17.826090
---

# frida inlinehook 巧解Android逆向题

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

# frida inlinehook 巧解Android逆向题

阅读量**337229**

发布时间 : 2023-02-15 10:30:45

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

![]()

## 前言

最近又又又是老朋友发来一道Android逆向题，比赛时没做出来，后来参考了别人的思路，还是用frida解出了题目，学到一些思路记录下。

## Java层静态分析

直接拖进jadx，MainActivity内容如下，代码不多，基本流程就是，获取输入字符，通过一个native层的checkflag判断输入是否正确：

## Native层静态分析

直接解压把libnative-lib.so拖入ida。
发现是静态注册的，直接能在导出函数里找到，处理伪码后如下，直接是ollvm当时就放弃了：

![]()

尝试用脚本模拟执行so，反混淆一下，emmmmm区别不大，但是好像勉强能看了？

![]()

翻了下看到进来有几处检测，一个很明显判断长度是否16：

![]()

另外两处sub\_78B0 sub\_74E0，是检测调试：

![]()

直接patch掉这个检测：

![]()

后面一长串看不懂了，绕晕了，后面看到一个地方很有意思：

![]()

上面这个判断很可疑（其实就是瞎猫撞死耗子），如果这里不行，就没有后文了，显然发了这篇文章这里肯定是可以的。

## Frida inlinehook

记录下指令地址，掏出frida开始hook这条指令看看寄存器的值。

![]()

跑起来，输入测试flag观察结果，我输入个f000000000000000，可以看到出现一次判断成功，后面第二次不相等了就没有后面的判断了：

![]()

再次试试，fl00000000000000，可以看到判断成功两次，同样第三次判断不相等又没有后文了：

![]()

根据上面的判断，那思路其实已经有了，逐位爆破应该就是能获取到flag，剩下就是脚本问题，这个好解决，构造一个主动调用，在java层调用checkflag函数，同时inlinehook观察指令判断情况一位一位爆破就行，代码如下：

![]()

![]()

然后一开始出了个bug，想不通，后来发现是我的flag填充位有问题，不能是0（因为flag中是包含0的，我的代码逻辑没考虑这么多，所以到下一位是0的时候，前一位爆破完，就标志位会出错了）：

![]()

最后在代码中把填充位换成其他字符，换成z，就愉快的跑出结果了：

![]()

## 总结

题目设置刚刚好（我看就是不想让人做出来），后面看了别人的wp是用unidbg做的，这个我不怎么会就换成用frida，直接做了出来，主要还是学习一下frida的inlinehook。

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**雷石安全实验室**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/286239](/post/id/286239)

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

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

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
* ##### [iOS静态方式绕过svc反动态调试](/post/id/285183)

  2023-01-09 14:30:35
* ##### [英媒：英国大臣的手机或可在20分钟内被黑客破解](/post/id/285095)

  2023-01-05 11:45:59
* ##### [frida inlinehook 巧解Android逆向题](/post/id/284343)

  2023-01-03 15:30:42
* ##### [知道手机投屏可以看剧，不知道还能被用来窃取隐私！](/post/id/282936)

  2022-11-09 17:30:51
* ##### [一道Android逆向题的取巧解题思路](/post/id/282006)

  2022-10-31 14:30:32

### 热门推荐

文章目录

* [前言](#h2-0)
* [Java层静态分析](#h2-1)
* [Native层静态分析](#h2-2)
* [Frida inlinehook](#h2-3)
* [总结](#h2-4)

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
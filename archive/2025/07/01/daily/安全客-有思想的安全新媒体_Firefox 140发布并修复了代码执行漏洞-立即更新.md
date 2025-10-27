---
title: Firefox 140发布并修复了代码执行漏洞-立即更新
url: https://www.anquanke.com/post/id/309127
source: 安全客-有思想的安全新媒体
date: 2025-07-01
fetch_date: 2025-10-06T23:50:52.045532
---

# Firefox 140发布并修复了代码执行漏洞-立即更新

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

# Firefox 140发布并修复了代码执行漏洞-立即更新

阅读量**36294**

发布时间 : 2025-06-30 18:18:22

**x**

##### 译文声明

本文是翻译文章，文章原作者 Guru Baran，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/firefox-140-released/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

Mozilla 发布了 Firefox 140，解决了多个关键安全漏洞，包括一个可能导致代码执行的高影响的释放后使用漏洞。

此更新修补了 12 个不同的安全漏洞，从内存安全问题到影响桌面和移动版本浏览器的特定于平台的漏洞。

## 解决了影响较大的安全漏洞

**CVE-2025-6424：FontFaceSet 中存在释放后使用**

CVE-2025-6424 是由 DEVCORE 研究团队的安全研究人员 LJP 和 HexRabbit 在 Firefox 的 FontFaceSet 组件中发现的高影响释放后使用漏洞。

当程序在释放或解除分配内存后继续使用内存时，就会出现释放后使用漏洞，从而导致内存损坏。

在此特定情况下，漏洞存在于 FontFaceSet 中，它是 Firefox 字体处理系统的一部分，用于管理 Web 字体和字体加载作。

触发后，此缺陷会导致可能被利用的崩溃，攻击者可以利用该崩溃在受害者的系统上执行任意代码。

**CVE-2025-6436：内存安全错误集合**

CVE-2025-6436 包含 Firefox 139 和 Thunderbird 139 中存在的多个内存安全漏洞。

此 CVE 由 Mozilla 的内部安全团队报告，包括 Andrew McCreight、Gabriele Svelto、Beth Rennie 和 Mozilla 模糊测试团队，表明它是通过 Mozilla 正在进行的安全测试流程发现的。

与单个特定漏洞不同，CVE-2025-6436 表示一组内存安全问题，这些问题显示了内存损坏的证据。

内存安全 bug 可能包括缓冲区溢出、释放后使用情况、双重释放错误和其他内存管理缺陷。

## 其他安全漏洞

此更新还解决了 CVE-2025-6425，这是一个中等影响的漏洞，其中 WebCompat WebExtension 暴露了一个持久性 UUID，该 UUID 可用于跨容器和浏览模式跟踪用户。

安全研究员 Rob Wu 发现了一个隐私问题，它可能允许攻击者持续对浏览器进行指纹识别。

CVE-2025-6426 是一个影响较小的缺陷，会影响 Firefox for macOS，其中带有终端扩展名的可执行文件会在没有适当的警告对话框的情况下打开，从而可能使用户面临恶意软件执行。该漏洞由安全研究人员 pwn2car 报告。

Android 用户可从修复两个不同的问题中受益。CVE-2025-6428 解决了一个 URL纵漏洞，该漏洞导致 Firefox for Android 错误地遵循链接查询字符串参数中指定的 URL，而不是预期目的地，从而可能促进网络钓鱼攻击。

此外，CVE-2025-6431 还解决了外部应用程序提示符的绕过机制，该机制可能会使用户暴露于第三方应用程序中的安全漏洞。

该版本包括针对多个内容安全策略 （CSP） 绕过漏洞的修复。

CVE-2025-6427 解决了通过子文档作绕过 connect-src 指令的问题，而 CVE-2025-6430 解决了 embed 和 object 标签中可能导致跨站点脚本攻击的 Content-Disposition 标头处理问题。

用户应立即更新到 Firefox 140 以防止这些漏洞。

这些修复的全面性，尤其是影响较大的内存安全问题，使得此更新对于维护浏览器安全至关重要。

系统管理员应优先跨组织网络部署此更新，以防止对记录的漏洞进行潜在利用。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/firefox-140-released/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/309127](/post/id/309127)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/firefox-140-released/)

如若转载,请注明出处： <https://cybersecuritynews.com/firefox-140-released/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **545**

* 粉丝
* **5**

### TA的文章

* ##### [国庆重保+攻防演练大考在即！360大模型安全服务专项方案筑牢AI防线](/post/id/312460)

  2025-09-29 18:06:17
* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Meta 旨在打造机器人领域的“Android”，为下一代人形AI提供通用平台](/post/id/312454)

  2025-09-29 18:05:34
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33

### 相关文章

* ##### [国庆重保+攻防演练大考在即！360大模型安全服务专项方案筑牢AI防线](/post/id/312460)

  2025-09-29 18:06:17
* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Meta 旨在打造机器人领域的“Android”，为下一代人形AI提供通用平台](/post/id/312454)

  2025-09-29 18:05:34
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33
* ##### [Morte僵尸网络被披露：正利用路由器与企业应用漏洞，迅速扩张其“加载器即服务”活动](/post/id/312444)

  2025-09-29 18:04:01
* ##### [Akira勒索软件利用SonicWall VPN账户发起急速入侵](/post/id/312438)

  2025-09-29 18:03:28

### 热门推荐

文章目录

* [解决了影响较大的安全漏洞](#h2-0)
* [其他安全漏洞](#h2-1)

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
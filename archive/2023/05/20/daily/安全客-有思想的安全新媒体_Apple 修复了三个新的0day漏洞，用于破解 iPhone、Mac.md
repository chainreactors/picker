---
title: Apple 修复了三个新的0day漏洞，用于破解 iPhone、Mac
url: https://www.anquanke.com/post/id/288789
source: 安全客-有思想的安全新媒体
date: 2023-05-20
fetch_date: 2025-10-04T11:37:03.652391
---

# Apple 修复了三个新的0day漏洞，用于破解 iPhone、Mac

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

# Apple 修复了三个新的0day漏洞，用于破解 iPhone、Mac

阅读量**214417**

发布时间 : 2023-05-19 12:00:40

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

近日，Apple 发布公告修复了三个新的0day漏洞，这些漏洞可能已经被用于攻击 iPhone、Mac 和 iPad。

这些安全漏洞均在多平台 WebKit 浏览器引擎中发现，并被跟踪为 CVE-2023-32409、CVE-2023-28204 和 CVE-2023-32373。

第一个漏洞是沙箱逃逸，它使远程攻击者能够突破 Web 内容沙箱。

另外两个是可以帮助攻击者访问敏感信息的越界读取和一个允许在受感染设备上执行任意代码的释放后使用问题，这两个问题都是在诱使目标加载恶意制作的网页之后（网页内容）。

Apple 通过改进边界检查、输入验证和内存管理解决了 macOS Ventura 13.4、iOS 和 iPadOS 16.5、tvOS 16.5、watchOS 9.5 和 Safari 16.5 中的三个零日漏洞。

受影响的设备列表非常广泛，因为该错误会影响较旧和较新的型号，其中包括：

* iPhone 6s（所有机型）、iPhone 7（所有机型）、iPhone SE（第 1 代）、iPad Air 2、iPad mini（第 4 代）、iPod touch（第 7 代）和 iPhone 8 及更新机型
* iPad Pro（所有机型）、iPad Air 第三代及更新机型、iPad 第五代及更新机型、iPad mini 第五代及更新机型
* 运行 macOS Big Sur、Monterey 和 Ventura 的 Mac
* Apple Watch Series 4 及更新机型
* Apple TV 4K（所有型号）和 Apple TV HD

该公司还透露，CVE-2023-28204 和 CVE-2023-32373（由匿名研究人员报告）首先通过 5 月 1 日发布的适用于 iOS 16.4.1 和 macOS 13.3.1 设备的快速安全响应 (RSR) 补丁解决  。

值得一提的是，谷歌威胁分析小组的 Clément Lecigne 和国际特赦组织安全实验室的 Donncha Ó Cearbhaill 报告了 CVE-2023-32409。

这两位研究人员所属的组织定期披露有关利用零日漏洞在政客、记者、持不同政见者等的智能手机和计算机上部署雇佣间谍软件的国家支持活动的详细信息。

![]()

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/288789](/post/id/288789)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)

**+1**6赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=168535)

[安全客](/member.html?memberId=168535)

这个人太懒了，签名都懒得写一个

* 文章
* **122**

* 粉丝
* **0**

### TA的文章

* ##### [注册机内藏勒索软件！收款竟用支付宝？](/post/id/292743)

  2024-01-19 11:10:00
* ##### [全球首发！《2023年度统信UOS安全威胁防御报告》来了](/post/id/292263)

  2023-12-29 11:27:27
* ##### [数字安全“奥斯卡”落幕，ISC 2023创新百强重磅出炉](/post/id/292240)

  2023-12-29 10:24:44
* ##### [一个安全运营工程师的自白](/post/id/291372)

  2023-11-15 10:40:17
* ##### [打造实战型安全人才新高地，360发布ISC安全课SaaS化教培平台](/post/id/291209)

  2023-11-03 17:22:35

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
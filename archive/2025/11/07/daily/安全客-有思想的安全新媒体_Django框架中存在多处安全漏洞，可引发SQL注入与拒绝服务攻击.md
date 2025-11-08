---
title: Django框架中存在多处安全漏洞，可引发SQL注入与拒绝服务攻击
url: https://www.anquanke.com/post/id/313045
source: 安全客-有思想的安全新媒体
date: 2025-11-07
fetch_date: 2025-11-08T03:01:05.831497
---

# Django框架中存在多处安全漏洞，可引发SQL注入与拒绝服务攻击

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

# Django框架中存在多处安全漏洞，可引发SQL注入与拒绝服务攻击

阅读量**21829**

发布时间 : 2025-11-07 10:26:09

**x**

##### 译文声明

本文是翻译文章，文章原作者 Divya，文章来源：gbhackers

原文地址：<https://gbhackers.com/multiple-django-flaws/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

Django开发团队已发布**关键安全补丁**，修复了两个可能导致应用遭受**拒绝服务攻击（DoS）** 和**SQL注入漏洞**的重大缺陷。

2025年11月5日，Django按照标准安全发布政策，针对**5.2.8、5.1.14和4.2.26版本**发布安全更新。

这两个已披露的漏洞对已部署的Django应用构成不同程度的风险：一个是影响QuerySet操作的**高危SQL注入漏洞**，另一个是影响Windows系统安装的**中危拒绝服务漏洞**。Django开发者应**立即优先更新**部署至修复版本。

![]()

### **QuerySet操作中的SQL注入漏洞**

更严重的漏洞编号为**CVE-2025-64459**，影响Django的QuerySet过滤操作。

安全研究人员发现，当开发者使用**特制字典（通过字典展开）作为\_connector参数**时，`QuerySet.filter()` 、`QuerySet.exclude()` 、`QuerySet.get()` 方法以及`Q()`类存在SQL注入风险。

该漏洞允许攻击者向数据库查询中注入恶意SQL命令，可能导致**未授权访问、修改或删除数据**。

其严重性源于高可利用性：开发者在日常使用这些QuerySet操作时，若处理未经验证的不可信用户输入，可能**无意中引入SQL注入漏洞**。

利用此漏洞的攻击者可绕过应用安全控制，直接对底层数据库执行**任意SQL命令**，对生产环境构成严重威胁。

### **Windows系统上的拒绝服务漏洞**

**CVE-2025-64458**修复了Windows平台上`HttpResponseRedirect`和`HttpResponsePermanentRedirect`函数存在的拒绝服务漏洞。

问题源于Python中**低效的NFKC Unicode规范化处理**——当处理包含大量Unicode字符的输入时，该过程会消耗大量系统资源，导致应用无响应。

攻击者可构造包含**过量Unicode数据的特制请求**，使规范化过程占用显著系统资源，最终导致应用瘫痪。

尽管该漏洞被归类为中危，Windows管理员仍需保持警惕：成功利用可能**中断服务可用性**。

此攻击**无需身份验证且可远程执行**，是针对Windows部署的Django应用的潜在攻击向量。

### **修复建议与影响范围**

所有受影响的Django版本（包括开发主分支和Django 6.0 beta）均已应用修复这两个漏洞的补丁。

运行Django **4.2、5.1或5.2版本**的组织应立即更新至修复版本。

受影响版本占已部署Django实例的很大比例，因此这是影响整个Django生态系统的**广泛安全问题**。

本文翻译自gbhackers [原文链接](https://gbhackers.com/multiple-django-flaws/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/313045](/post/id/313045)

安全KER - 有思想的安全新媒体

本文转载自: [gbhackers](https://gbhackers.com/multiple-django-flaws/)

如若转载,请注明出处： <https://gbhackers.com/multiple-django-flaws/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **663**

* 粉丝
* **6**

### TA的文章

* ##### [黑客正滥用Windows Hyper-V功能隐匿Linux虚拟机，以规避终端检测与响应机制的检测](/post/id/313062)

  2025-11-07 10:27:48
* ##### [谷歌发出警告：新型PROMPTFLUX恶意软件正利用Gemini API实现源代码自我重写](/post/id/313072)

  2025-11-07 10:27:39
* ##### [开源安全模型OpenGuardrails发布，旨在为现实世界AI应用保驾护航](/post/id/313066)

  2025-11-07 10:27:29
* ##### [为遵循欧盟监管要求，苹果将于欧盟地区关闭Apple Watch的自动Wi-Fi同步功能](/post/id/313079)

  2025-11-07 10:27:22
* ##### [美国CISA发布警告：Gladinet CentreStack与Triofox文件共享软件中的漏洞正遭攻击利用](/post/id/313069)

  2025-11-07 10:27:13

### 相关文章

* ##### [黑客正滥用Windows Hyper-V功能隐匿Linux虚拟机，以规避终端检测与响应机制的检测](/post/id/313062)

  2025-11-07 10:27:48
* ##### [谷歌发出警告：新型PROMPTFLUX恶意软件正利用Gemini API实现源代码自我重写](/post/id/313072)

  2025-11-07 10:27:39
* ##### [开源安全模型OpenGuardrails发布，旨在为现实世界AI应用保驾护航](/post/id/313066)

  2025-11-07 10:27:29
* ##### [为遵循欧盟监管要求，苹果将于欧盟地区关闭Apple Watch的自动Wi-Fi同步功能](/post/id/313079)

  2025-11-07 10:27:22
* ##### [美国CISA发布警告：Gladinet CentreStack与Triofox文件共享软件中的漏洞正遭攻击利用](/post/id/313069)

  2025-11-07 10:27:13
* ##### [恶意软件Gootloader重出江湖，采用ZIP文件新策略隐匿恶意负载](/post/id/313076)

  2025-11-07 10:27:01
* ##### [远程控制木马EndClient通过滥用遭泄露的代码签名证书来规避防病毒软件检测](/post/id/313056)

  2025-11-07 10:26:52

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
---
title: 关键vBulletin论坛漏洞让攻击者执行远程代码
url: https://www.anquanke.com/post/id/307791
source: 安全客-有思想的安全新媒体
date: 2025-05-28
fetch_date: 2025-10-06T22:24:33.216398
---

# 关键vBulletin论坛漏洞让攻击者执行远程代码

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

# 关键vBulletin论坛漏洞让攻击者执行远程代码

阅读量**44550**

发布时间 : 2025-05-27 12:41:54

**x**

##### 译文声明

本文是翻译文章，文章原作者 古鲁 巴兰，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/vbulletin-forum-rce-vulnerability/>

译文仅供参考，具体内容表达以及含义原文为准。

[vBulletin](https://cybersecuritynews.com/vbulletin-forums-breached/)世界上最受欢迎的论坛平台之一vBulletin的新发现漏洞使数千个在线社区面临未经身份验证的远程代码执行(RCE)的风险。

该漏洞存在于 PHP 8.1 或更高版本上的 vBulletin 5.x 和 6.x 版本中,允许攻击者调用受保护的内部方法,打破基本安全边界,并在无需身份验证的情况下实现完整的系统妥协。

此漏洞的核心是 vBulletin 依赖 PHP 的 Reflection API 来定制 Model-View-Controller (MVC) 框架和 API 系统。

## 反射 API 和动态路由

该平台的架构使用动态路由,其中API端点映射到基于传入HTTP请求的控制器方法。

例如,对 /ajax/api/user/fetchProfileInfo 的 AJAX 调用被路由到 vB\_Api\_User::fetchProfileInfo() 方法。

关键问题来自vBulletin如何使用ReflectionMethod::invoke()和ReflectionMethod::invokeArgs()函数。

从 PHP 8.1 开始,这些函数允许调用受保护和私有方法,而无需 setAccessible(true),这是对以前 PHP 版本的更改。

这种微妙的转变意味着,如果应用程序不执行可见性检查,则旨在成为内部助手的方法现在可以直接由远程用户调用。

简化的易受攻击代码模式包括:

向/api.php 请求的?method=protectedMethod 将直接在 PHP 8.1+ 上调用受保护方法,绕过预期的访问控制。

## 剥削 路径

虽然调用受保护方法的能力是危险的,但当其中一种方法可用于执行代码时,就会出现真正的威胁。

在 vBulletin 中,vB\_Api\_Ad::replaceAdTemplate() 方法是一个受保护的函数,旨在插入或更新广告模板。

攻击者发现,他们可以通过精心制作的HTTP POST请求调用此方法,将任意模板代码注入系统。

vBulletin 模板引擎支持使用 <vb:if> 标签的条件逻辑。由于模板解析器如何过滤输入存在单独的缺陷,攻击者可以绕过限制并使用变量函数调用注入PHP代码。例如:

此模板一旦注入,允许攻击者执行通过POST请求发送的系统命令,有效地在服务器上授予Webshell。

概念验证漏洞利用演示了攻击者如何获得shell访问,运行任意命令,并完全破坏底层系统,[所有这些都无需身份验证。](https://cybersecuritynews.com/authentication/)

此漏洞链已确认适用于在 PHP 8.1+ 上运行的 vBulletin 5.1.0、5.7.5、6.0.1 和 6.0.3。该漏洞被认为在6.0.4版本中进行了修补。

此漏洞对开发人员来说是一个警告:依靠方法可见性(公共,受保护,私有)作为安全边界从根本上是不安全的,特别是在使用动态调度和反射时。

在 PHP 8.1 中引入新行为,其中 ReflectionMethod 可以默认调用受保护和私有方法,这意味着应用程序必须在应用程序级别明确执行访问控制。

vBulletin RCE漏洞表明,底层编程语言的微妙变化会对Web应用程序安全产生灾难性后果。

它强调了明确访问控制的重要性,以及依靠语言级可见性在动态Web框架中的安全性的危险。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/vbulletin-forum-rce-vulnerability/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/307791](/post/id/307791)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/vbulletin-forum-rce-vulnerability/)

如若转载,请注明出处： <https://cybersecuritynews.com/vbulletin-forum-rce-vulnerability/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全知识](/tag/%E5%AE%89%E5%85%A8%E7%9F%A5%E8%AF%86)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**3赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

[安全客](/member.html?memberId=170061)

这个人太懒了，签名都懒得写一个

* 文章
* **2096**

* 粉丝
* **6**

### TA的文章

* ##### [英国通过数据访问和使用监管法案](/post/id/308719)

  2025-06-20 17:11:10
* ##### [CISA警告：严重缺陷（CVE-2025-5310）暴露加油站设备](/post/id/308715)

  2025-06-20 17:09:03
* ##### [大多数公司高估了AI治理，因为隐私风险激增](/post/id/308708)

  2025-06-20 17:05:02
* ##### [研究人员发现了有史以来最大的数据泄露事件，暴露了160亿个登录凭证](/post/id/308704)

  2025-06-20 17:02:15
* ##### [CVE-2025-6018和CVE-2025-6019漏洞利用：链接本地特权升级缺陷让攻击者获得大多数Linux发行版的根访问权限](/post/id/308701)

  2025-06-20 16:59:36

### 相关文章

* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33
* ##### [CISA称黑客利用GeoServer漏洞成功入侵一联邦机构](/post/id/312347)

  2025-09-24 16:45:06
* ##### [SolarWinds紧急发布补丁，修复高危远程代码执行漏洞CVE-2025-26399](/post/id/312357)

  2025-09-24 16:43:11
* ##### [Chrome浏览器存在高危漏洞，可致攻击者窃取敏感信息并引发系统崩溃](/post/id/312366)

  2025-09-24 16:42:08
* ##### [CVE-2025-55241：CVSS评分10.0的Microsoft Entra ID漏洞可能危及全球所有租户](/post/id/312294)

  2025-09-22 18:14:51

### 热门推荐

文章目录

* [反射 API 和动态路由](#h2-0)
* [剥削 路径](#h2-1)

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
---
title: Microsoft Copilot中的严重缺陷可能允许零点击攻击
url: https://www.anquanke.com/post/id/308454
source: 安全客-有思想的安全新媒体
date: 2025-06-14
fetch_date: 2025-10-06T22:50:22.275870
---

# Microsoft Copilot中的严重缺陷可能允许零点击攻击

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

# Microsoft Copilot中的严重缺陷可能允许零点击攻击

阅读量**98424**

发布时间 : 2025-06-13 15:38:31

**x**

##### 译文声明

本文是翻译文章，文章原作者 David Jones，文章来源：cybersecuritydive

原文地址：<https://www.cybersecuritydive.com/news/flaw-microsoft-copilot-zero-click-attack/750456/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

研究人员表示，Microsoft 的 Copilot AI 工具中最近修复的一个关键漏洞可能让远程攻击者只需发送电子邮件即可从组织窃取敏感数据。

该漏洞被称为 EchoLeak 并分配了标识符CVE-2025-32711，可能允许黑客发起攻击，而目标用户无需执行任何作。EchoLeak 是已知的第一个针对 AI 代理的零点击攻击，据称 researchers at Aim Security, ，它在周三的一篇博文中发布了调查结果。

“这个漏洞代表了 AI 安全研究的重大突破，因为它展示了攻击者如何在不需要任何用户交互的情况下自动从 Microsoft 365 Copilot 的上下文中泄露最敏感的信息，”Aim Security 的联合创始人兼首席技术官 Adir Gruss 通过电子邮件告诉 Cybersecurity Dive。

EchoLeak 攻击可能利用了研究人员所说的“LLM 范围违规”，其中来自组织外部的不受信任的输入可以征用 AI 模型来访问和窃取特权数据。

易受攻击的数据可能包括 Copilot 有权访问的所有内容，包括聊天历史记录、OneDrive 文档、Sharepoint 内容、Teams 对话和来自组织的预加载数据。

Gruss 表示，直到最近，Microsoft Copilot 的默认配置才使大多数组织面临攻击风险，尽管他警告说，没有证据表明任何客户实际上成为目标。

几个月来一直与研究人员就该漏洞进行协调的 Microsoft 发布 an advisory on Wednesday 称，该问题已完全解决，客户无需采取进一步行动。

“我们感谢 Aim Labs 发现并负责任地报告此问题，以便在我们的客户受到影响之前解决它，”Microsoft 的一位发言人通过电子邮件表示。

Microsoft 表示，它已经更新了产品以缓解这个问题。该公司还实施了深度防御措施，以进一步增强其安全态势。

Forrester 副总裁兼首席分析师 Jeff Pollard 表示，该漏洞与之前对 AI 代理潜在安全风险的担忧一致。

本文翻译自cybersecuritydive [原文链接](https://www.cybersecuritydive.com/news/flaw-microsoft-copilot-zero-click-attack/750456/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/308454](/post/id/308454)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritydive](https://www.cybersecuritydive.com/news/flaw-microsoft-copilot-zero-click-attack/750456/)

如若转载,请注明出处： <https://www.cybersecuritydive.com/news/flaw-microsoft-copilot-zero-click-attack/750456/>

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

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

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
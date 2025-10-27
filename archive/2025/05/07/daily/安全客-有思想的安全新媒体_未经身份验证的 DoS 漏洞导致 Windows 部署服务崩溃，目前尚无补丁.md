---
title: 未经身份验证的 DoS 漏洞导致 Windows 部署服务崩溃，目前尚无补丁
url: https://www.anquanke.com/post/id/307079
source: 安全客-有思想的安全新媒体
date: 2025-05-07
fetch_date: 2025-10-06T22:24:57.462561
---

# 未经身份验证的 DoS 漏洞导致 Windows 部署服务崩溃，目前尚无补丁

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

# 未经身份验证的 DoS 漏洞导致 Windows 部署服务崩溃，目前尚无补丁

阅读量**43899**

发布时间 : 2025-05-06 14:22:11

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/unauthenticated-dos-vulnerability-crashes-windows-deployment-services-no-patch/>

译文仅供参考，具体内容表达以及含义原文为准。

![预授权 DoS，Windows 部署服务]()

根据安全研究员彭志娘的详细技术分析，Windows 部署服务 (WDS) 中新披露的一个拒绝服务 (DoS) 漏洞可能引发远程、未经身份验证的崩溃，威胁企业网络安全。该漏洞于 2025 年初被发现，并已向微软负责任地披露。攻击者可以利用该漏洞利用伪造的 UDP 数据包耗尽系统内存，导致服务器在几分钟内完全无响应，且无需任何身份验证或用户交互。

“*我们演示了 WDS 中的远程 DoS，攻击者可以在无需身份验证（预身份验证）或用户交互（0-click）的情况下破坏您的 WDS 网络*，”Peng在他的报告中解释道。

问题的根源在于 WDS 使用基于 UDP 的 TFTP 服务（端口 69）通过 PXE 启动来传送 Windows 安装映像。当客户端连接服务器时，WDS 会分配一个 CTftpSession 对象。然而，可创建的会话数量没有限制。

报告指出：“*核心问题在于 EndpointSessionMapEntry 对会话数量没有限制。**攻击者可以伪造客户端 IP 地址和端口号，反复创建新会话，直到系统资源耗尽*。”

在运行具有 8GB RAM 的 Windows Server Insider Preview 的测试环境中，Peng 只需发送大量具有随机源地址和端口的欺骗性 UDP 数据包，便可在 7 分钟内使整个系统崩溃。

Peng 概述了一个简单的攻击策略，该策略需要：

* 使用随机源 IP 和端口欺骗 UDP 数据包。
* 将数据包发送到端口 69 上的目标 WDS 服务器。
* 允许 WDS 在内存中创建和存储无限的会话对象。

尽管 Peng 出于道德原因只提供了伪代码，但该漏洞利用技术实现起来却很简单，只需要在运行 Ubuntu 或类似操作系统的攻击者机器上编写基本的脚本即可。

该漏洞于 2025 年 2 月 8 日报告给微软，并于 2025 年 3 月 4 日得到确认。然而，微软后来拒绝修补该问题，并于 4 月 23 日表示其“不符合*安全**服务**标准*”。

彭先生严厉批评了这一决定：“*我们认为这仍然是他们 SDL 栏中的一个重要的 DoS漏洞，我们在与微软就此案进行沟通时感到非常难过*。”

他强调，这是一种零点击攻击，可以远程瘫痪基于 PXE 的部署基础设施，这对于任何依赖 WDS 的组织来说都是一个关键问题。

由于微软尚未发布修复程序，Peng 提出了明确的建议：“*为了保护您的 PXE 网络免受此威胁，请不要使用 Windows 部署服务*。”

本文翻译自securityonline [原文链接](https://securityonline.info/unauthenticated-dos-vulnerability-crashes-windows-deployment-services-no-patch/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/307079](/post/id/307079)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/unauthenticated-dos-vulnerability-crashes-windows-deployment-services-no-patch/)

如若转载,请注明出处： <https://securityonline.info/unauthenticated-dos-vulnerability-crashes-windows-deployment-services-no-patch/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**2赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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
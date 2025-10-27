---
title: 黑客滥用DNS盲区隐藏并投递恶意软件
url: https://www.anquanke.com/post/id/310251
source: 安全客-有思想的安全新媒体
date: 2025-07-19
fetch_date: 2025-10-06T23:39:07.139517
---

# 黑客滥用DNS盲区隐藏并投递恶意软件

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

# 黑客滥用DNS盲区隐藏并投递恶意软件

阅读量**78370**

发布时间 : 2025-07-18 17:30:36

**x**

##### 译文声明

本文是翻译文章，文章原作者 Guru Baran，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/dns-blind-spots-exploited/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

一种复杂的新型攻击手法正被黑客广泛采用：他们**将恶意软件隐藏在DNS记录中**，从而利用大多数组织安全基础设施中的**关键盲点**。该技术将互联网的域名系统（DNS）转变为一种**非常规的文件存储系统**，使攻击者能够分发恶意软件，同时规避传统检测机制。

近期利用被动DNS情报平台DNSDB Scout的调查显示，网络犯罪分子正在将恶意软件文件**分割后存储在DNS的TXT记录中**。

![]()

这些记录最初被设计用于存储域名的描述性文本，但实际上可以**保存任意数据**，直到DNS服务器将其删除或覆盖。

攻击方法包括将恶意可执行文件**转换为十六进制格式**，然后将其**分片并存储在多个子域名中**。

DomainTools的研究人员通过搜索十六进制格式的文件头标志（magic bytes）并使用复杂的正则表达式模式，成功识别出**多种可执行文件及常见文件类型**的证据。

### **TXT记录中的恶意软件**

在对2021至2022年DNS记录的分析中，安全研究人员识别出**三个不同域名**的TXT记录中包含可执行文件的文件头，它们**共享相同的子域名模式**。

![]()

最重要的发现涉及域名**“\*.felix.stf.whitetreecollective[.]com”**，其包含数百个按整数值迭代命名的子域名，每个子域名中存储可执行文件的不同片段。

研究人员通过将这些片段按整数值顺序重新组合，成功还原了完整的恶意软件文件，并得出以下**SHA256哈希值**：

* • 7ff0ecf2953b8662ede1577e330a514f09992c18aa3c14ed77cf2ffc115b0866
* • e7b22ba761a7f853b63933ffe517cc61596710dbdee992a429ac1bc8d04186a1

这两份文件被识别为Joke Screenmate恶搞软件，这是一种玩笑性质的软件，具有多种干扰性行为，包括**模拟破坏行为、干扰用户控制、显示非请求内容和导致系统性能问题等**。

调查还发现了一个更令人担忧的现象：**TXT记录中存储了恶意的PowerShell命令**。

研究人员在**与“drsmitty[.]com”相关**的DNS记录中发现了**编码的stager脚本**，这些脚本会连接至**“cspg[.]pw”**，并利用Covenant C2服务器的默认端点**（/api/v1/nps/payload/stage1）**来投递下一阶段的载荷。

这一技术代表了恶意软件投递方式的重大进化，因为与对Web和电子邮件通信的广泛监测相比，安全解决方案通常**忽视DNS流量**。

同一C2域名在DNS记录中**可追溯至2017年7月**，表明这一攻击路径已经运行多年。

DNS隧道技术和恶意软件存储方式暴露出企业安全策略中的**根本性弱点**。DNS尽管是现代数字基础设施的骨干，却常常**被排除在可视化与合规规划之外**。

最新研究表明，**90%**的恶意软件会**在攻击链中使用DNS**，**95%**的恶意软件**使用DNS与指挥控制（C2）服务器通信**。

随着**加密DNS协议**（如DoH（DNS over HTTPS）和DoT（DNS over TLS））的兴起，检测工作变得更加复杂。这些旨在保护用户隐私的技术也**为攻击者的恶意活动提供了额外掩护**。

安全专家强调，组织必须**部署全面的DNS监控和过滤解决方案**，以识别这些复杂的攻击。

随着网络犯罪分子持续滥用DNS等受信任协议，企业已无法再将DNS视为**只需最小安全关注**的实用服务。

这一攻击路径的发现凸显了**部署DNS安全解决方案的迫切需求**，这些方案能够识别**正常请求与恶意用途**之间的区别，从而将DNS从安全盲点转变为积极的防御机制。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/dns-blind-spots-exploited/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/310251](/post/id/310251)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/dns-blind-spots-exploited/)

如若转载,请注明出处： <https://cybersecuritynews.com/dns-blind-spots-exploited/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**6赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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
---
title: 谷歌Gemini for Workspace存在漏洞：攻击者可在邮件中隐藏恶意脚本
url: https://www.anquanke.com/post/id/309989
source: 安全客-有思想的安全新媒体
date: 2025-07-15
fetch_date: 2025-10-06T23:16:44.058462
---

# 谷歌Gemini for Workspace存在漏洞：攻击者可在邮件中隐藏恶意脚本

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

# 谷歌Gemini for Workspace存在漏洞：攻击者可在邮件中隐藏恶意脚本

阅读量**47653**

发布时间 : 2025-07-14 17:24:06

**x**

##### 译文声明

本文是翻译文章，文章原作者 Guru Baran，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/google-gemini-for-workspace-vulnerability/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

安全研究人员发现，**谷歌Gemini for Workspace**存在一个**重大漏洞**，威胁者可借此**在邮件中嵌入隐藏的恶意指令**。

攻击者利用这款人工智能助手的**“总结此邮件”**功能，显示伪造的、看似来自谷歌官方的安全警告，进而可能实施凭证窃取和社会工程学攻击。

#### ****核心要点****

1. 攻击者利用不可见的HTML/CSS代码**在邮件中隐藏恶意指令**，Gemini在总结邮件时会对这些代码进行处理。
2. 此类攻击**仅需精心构造的HTML标签**，无需链接、附件或脚本。
3. Gemini会**显示攻击者伪造的、看似来自谷歌的钓鱼警告**，诱骗用户泄露凭证。
4. 该漏洞影响**Gmail、文档（Docs）、幻灯片（Slides）和云端硬盘（Drive）**，可能在谷歌Workspace中催生**人工智能蠕虫**。

一名研究人员向0DIN提交了相关发现（提交ID：0xE24D9E6B），并演示了这一漏洞。攻击者通过嵌入在邮件中的特制HTML和CSS代码，**采用提示词注入技术操纵Gemini的人工智能处理功能**。

与传统钓鱼攻击不同，这种攻击**无需链接、附件或外部脚本**，仅需在邮件正文中隐藏经过特殊格式处理的文本。

攻击原理是**利用Gemini对隐藏HTML指令的处理方式**。攻击者将指令嵌入**<Admin>**标签内，同时使用白色文字配白色背景、字体大小设为零等CSS样式，使内容对收件人不可见。

当受害者点击Gemini的“总结此邮件”功能时，人工智能助手会将隐藏指令**当作合法的系统命令**进行处理，并在总结结果中如实呈现攻击者伪造的安全警报。

##### ****谷歌GeminiforWorkspace漏洞详情****

该漏洞属于**间接提示词注入（IPI）**，即提供给人工智能模型的外部内容中包含隐藏指令，这些指令会成为有效提示词的一部分。安全专家按照**0DIN分类法**，将这种攻击归为**“策略→元提示→欺骗性格式”**类别，社会影响评分中等。

概念验证示例显示，攻击者可插入包含管理员风格指令的**不可见跨度（span）**，这些指令会指示Gemini在邮件总结中添加**紧急安全警告**。

![]()

这类警告通常会催促收件人**拨打特定电话或访问特定网站**，为凭证收集或语音钓鱼方案创造条件。

该漏洞的影响范围不止于Gmail，还可能波及谷歌Workspace中**集成Gemini的其他产品**，包括文档、幻灯片和云端硬盘的搜索功能。这形成了一个重大的跨产品攻击面，**任何涉及Gemini处理第三方内容的工作流程**都可能成为潜在的注入载体。

安全研究人员警告称，一旦SaaS账户遭到入侵，攻击者可能会利用**自动化的新闻通讯、客户关系管理系统（CRM）以及工单邮件**，将其转化为成千上万个“钓鱼信标”，对广大用户构成广泛而持续的网络安全威胁。

这种技术还引发了对未来**“人工智能蠕虫”**的担忧——此类蠕虫可能在邮件系统中**自我复制**，从单个钓鱼尝试升级为**自主传播**。

##### ****缓解措施****

安全团队应采取多项防御措施，包括**对入站HTML进行代码检查以剥离不可见样式、配置大语言模型（LLM）防火墙，以及部署可扫描Gemini输出内容中可疑信息的后处理过滤器**。

各组织还应加强**用户意识培训**，强调人工智能总结仅为参考信息，而非权威的安全警报。

对于谷歌等人工智能提供商，建议的缓解措施包括**在接收内容时进行HTML清理、改进上下文归因以区分人工智能生成文本与源材料，以及增强可解释性功能**，向用户揭示隐藏的提示词。

这一漏洞凸显了一个新的现实：**人工智能助手已成为攻击面的新组成部分**，安全团队需将其作为潜在威胁载体进行监测、沙箱隔离和密切监控。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/google-gemini-for-workspace-vulnerability/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/309989](/post/id/309989)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/google-gemini-for-workspace-vulnerability/)

如若转载,请注明出处： <https://cybersecuritynews.com/google-gemini-for-workspace-vulnerability/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**6赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

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
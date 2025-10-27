---
title: 严重的 GitHub MCP 漏洞：通过 “问题 ”的提示注入使私有仓库面临人工智能劫持风险
url: https://www.anquanke.com/post/id/307912
source: 安全客-有思想的安全新媒体
date: 2025-05-29
fetch_date: 2025-10-06T22:25:29.002792
---

# 严重的 GitHub MCP 漏洞：通过 “问题 ”的提示注入使私有仓库面临人工智能劫持风险

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

# 严重的 GitHub MCP 漏洞：通过 “问题 ”的提示注入使私有仓库面临人工智能劫持风险

阅读量**62964**

发布时间 : 2025-05-28 13:50:21

**x**

##### 译文声明

本文是翻译文章，文章原作者 Victoria Mossi，文章来源：webpronews

原文地址：<https://www.webpronews.com/critical-github-mcp-flaw-prompt-injection-via-issues-exposes-private-repos-to-ai-hijacking/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

在一项通过开发者社区发出冲击波的重大开发中,Invariant Labs的安全研究人员发现了GitHub的模型上下文协议(MCP)实现中的一个关键漏洞。

在一项通过开发人员社区发出冲击波的重大开发中,Invariant Labs的安全研究人员发现了GitHub的模型上下文协议(MCP)实现中的一个关键漏洞。

这个安全漏洞于2025年5月26日披露,允许攻击者利用GitHub的MCP服务器访问私有存储库,从而可能暴露机密代码、凭据和敏感信息。

该漏洞使恶意行为者能够通过特制的GitHub问题劫持用户的代理,然后强制其从私人存储库中提取数据,否则这些数据将无法访问。这一启示正值像Anthropic的Claude这样的AI助手越来越多地与开发工具和平台集成。

该漏洞利用了 MCP 协议中的提示注入技术和权限管理弱点的组合。当用户通过MCP将Claude或类似的AI助手连接到GitHub时,他们授予AI代表他们与存储库进行交互的权限。然而,当前的实现未能正确隔离和保护这些交互。

根据Invariant Labs的发现,攻击者可以在GitHub Issues中嵌入恶意指令,当由AI助手处理时,可以重定向助手的操作。被劫持的助手不是执行预期任务,而是可以被操纵以从用户可以访问的私有存储库中访问、读取和潜在地窃取数据。

**对AI工具生态系统的更广泛影响**

这个漏洞凸显了人们对HiddenLayer在2025年4月的分析中称之为“代理世界中的模型上下文陷阱”的日益关注。随着用户越来越依赖AI助手来执行跨多个服务的复杂任务,安全性影响变得更加明显,也难以推理。

GitHub MCP漏洞演示了不同MCP服务器的权限组合如何创建意外的攻击向量。在类似于HiddenLayer记录的场景中,攻击者理论上可以嵌入间接提示注入,该注入利用GitHub访问以及其他工具来窃取敏感信息,而不会触发额外的权限请求。

“LLM可用的API组合与间接提示注入威胁的安全挑战很难推理,”HiddenLayer的报告指出,该报告在GitHub MCP漏洞被发现前几周就有先见之明地警告了这些类型的漏洞。

**缓解策略与行业反应**

Anthropic的支持文档强调,用户在使用远程MCP集成时应“仅连接到受信任的服务器”并“仔细查看请求的权限”。然而,GitHub漏洞表明,即使是受信任的平台也可能存在重大安全风险。

Invariant Labs建议实施专用安全扫描器,例如其MCP扫描和Guardrails工具,以防止此类漏洞。用于检测有毒物质流动的安全分析仪是最早发现这一特定漏洞的。

与此同时,安全界呼吁围绕MCP实施制定更强有力的标准。AlibaCloudSecurity打开的GitHub问题警告说,“MCP协议表现出不充分的安全设计,这增加了广泛的网络钓鱼攻击的风险” – 鉴于最近发生的事件,这一担忧已被证明是有效的。

随着组织继续采用人工智能助手并将其与开发工作流程集成,这一事件清楚地提醒人们安全影响。将人工智能系统连接到像GitHub这样的强大工具的能力极大地提高了工作效率,但也引入了传统权限模型可能无法充分解决的复杂安全考虑因素。

行业专家建议对MCP集成采取谨慎的方法,特别是那些提供敏感数据存储库访问的集成。目前,开发人员应该仔细审核他们的AI助手集成,并考虑限制对私有存储库的访问,直到GitHub和其他MCP提供商实施更强大的安全措施。

本文翻译自webpronews [原文链接](https://www.webpronews.com/critical-github-mcp-flaw-prompt-injection-via-issues-exposes-private-repos-to-ai-hijacking/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/307912](/post/id/307912)

安全KER - 有思想的安全新媒体

本文转载自: [webpronews](https://www.webpronews.com/critical-github-mcp-flaw-prompt-injection-via-issues-exposes-private-repos-to-ai-hijacking/)

如若转载,请注明出处： <https://www.webpronews.com/critical-github-mcp-flaw-prompt-injection-via-issues-exposes-private-repos-to-ai-hijacking/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [安全知识](/tag/%E5%AE%89%E5%85%A8%E7%9F%A5%E8%AF%86)
* [安全热点](/tag/%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)

**+1**2赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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
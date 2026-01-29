---
title: Descope推出面向AI代理与MCP生态的专用身份基础设施
url: https://www.anquanke.com/post/id/314555
source: 安全客-有思想的安全新媒体
date: 2026-01-28
fetch_date: 2026-01-29T04:03:58.146761
---

# Descope推出面向AI代理与MCP生态的专用身份基础设施

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

# Descope推出面向AI代理与MCP生态的专用身份基础设施

阅读量**15809**

发布时间 : 2026-01-28 10:06:56

**x**

##### 译文声明

本文是翻译文章，文章原作者 Industry News，文章来源：helpnetsecurity

原文地址：<https://www.helpnetsecurity.com/2026/01/27/descope-agentic-identity-hub-2-0/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

Descope 对旗下**智能体身份中枢（Agentic Identity Hub）** 完成功能升级，为 MCP 协议开发者与 AI 智能体开发人员，打造了适配其 AI 系统的**标准化身份基础设施**。企业如今可通过 Descope，将 AI 智能体与人类用户同等视为一级身份主体进行管理，为内部及外部 MCP 服务器配置 OAuth 2.1 协议与工具级权限范围，同时依托企业级策略管控能力，对智能体访问 MCP 服务器的行为进行合规治理。

2025 年是 AI 智能体迈入主流应用的元年，但身份管理始终是困扰开发团队与安全团队的核心瓶颈。MCP 协议开发者与 AI 智能体开发人员难以满足企业安全团队对产品落地的合规要求 ——Descope 近期针对 400 余名身份领域决策者的调研显示，**88% 的企业已在使用或计划使用 AI 智能体，仅有 37% 的企业将其从试点阶段推进至实际落地**。

与此同时，安全团队也陷入两难：既要为智能体化 AI 应用筑牢安全防线，又不能阻碍技术创新。OWASP 智能体应用十大安全风险中，所有风险的整改方案均涉及身份相关措施，可见为 AI 智能体打造专属的身份认证服务体系，已是行业的迫切需求。

此外，MCP 这类协议的快速普及，也带来了诸多安全漏洞与开发负担 —— 目前已有 2000 台 MCP 服务器处于无安全防护状态；而 MCP 协议规范中要求开发者实现 OAuth 2.1、PKCE、动态客户端注册（DCR）、上下文身份元数据协议（CIMD）等多项功能，也让开发团队的工作压力大幅增加。

Descope 的无代码身份平台，支持企业通过可视化工作流，为客户、合作伙伴、AI 智能体及 MCP 服务器快速创建并调整身份验证流程。目前已有 GoFundMe、Databricks、GoodRx、Navan、[You.com](https://You.com)等超 1000 家企业选择 Descope，借助其能力优化客户体验、防范账户劫持风险，并实现对客户身份与机器身份的 360 度全维度管理。

本次升级后的 Descope 智能体身份中枢，兼顾开发团队与安全团队的双重需求 —— 为开发人员提供安全易用的身份基础设施，同时帮助安全团队通过策略化治理，实现对 AI 智能体的全生命周期管理。

Descope 智能体身份中枢的核心能力包括：

1. **智能体身份管理**：可集中展示所有接入企业应用、API 及 MCP 服务器的智能体身份（无论动态创建或手动注册）。每个智能体均拥有专属身份标识及配套属性，涵盖关联用户、所属租户、已授权的工具级权限范围、OAuth 客户端 ID 等关键信息。
2. **全维度 MCP 认证授权**：助力 MCP 服务器开发者，为内部及对外提供服务的 MCP 服务器，配置符合协议规范的认证与访问控制能力。企业可实现用户授权流程支持、高安全性动态客户端注册、CIMD 协议适配、智能体级与工具级的精细化授权范围管控，同时为 B2B 场景下的 MCP 应用实现租户级权限隔离。
3. **凭证保管库**：统一管理、存储并自动刷新 AI 智能体访问第三方系统所需的各类凭证（含 OAuth 令牌、API 密钥）。AI 智能体开发人员可从 50 余种预制连接模板中选择使用，并借助动态客户端注册预设配置，让智能体动态对接第三方 MCP 服务器，代表用户安全调用外部 API 接口。
4. **企业级策略管控**：企业可自定义精细化的授权控制策略，明确哪些 AI 智能体可访问 MCP 服务器、可调用哪些工具级权限，并支持基于用户角色、JWT 声明、租户属性、智能体类型等多维度配置策略。
5. **AI 智能体日志审计**：为企业提供所有 AI 智能体操作行为的全维度可视能力，可监控智能体的访问对象与访问时间、识别访问控制配置错误、撤销可疑恶意智能体的访问权限，同时将审计事件同步至第三方安全信息与事件管理（SIEM）平台。

Descope 首席执行官斯拉维克・马尔科维奇表示：“AI 智能体正在打破传统的身份管理体系。这类智能体具备自主性、可扩展性，且行为存在非确定性，无法沿用人类用户或服务账户的管理方式。Descope 智能体身份中枢是专为 AI 智能体打造的专属身份认证服务平台，为开发人员提供了所需的抽象层能力，助力其安全地将 AI 系统推向市场，同时确保权限最小化原则的落地与协议合规性的持续满足。感谢首批已采用该中枢的客户，我们也很荣幸能成为企业安全落地 AI 应用所需的核心基础设施之一。”

Descope 客户、WisdomAI 首席执行官索汉・马宗达称：“Descope 智能体身份中枢将我们的开发人员从工具开发与系统集成的工作中解放出来，让他们能将更多精力投入到核心功能的研发与落地中。我们面向客户的 MCP 服务器，正是以 Descope 作为认证层，这一服务器已服务于多家财富 500 强企业。依托 Descope 的能力，我们既能向客户展现 AI 分析平台的价值，也能对内置的身份管控能力充满信心。”

Descope 客户、Cequence Security 首席技术官施雷扬斯・梅塔表示：“Descope 是 Cequence AI 网关的核心底层组件。其对 MCP 认证的灵活支持与开发友好性，为 Cequence AI 网关的客户提供了重要助力，让他们能将自身应用、API 与数据安全地对接至 AI 智能体。”

本文翻译自helpnetsecurity [原文链接](https://www.helpnetsecurity.com/2026/01/27/descope-agentic-identity-hub-2-0/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/314555](/post/id/314555)

安全KER - 有思想的安全新媒体

本文转载自: [helpnetsecurity](https://www.helpnetsecurity.com/2026/01/27/descope-agentic-identity-hub-2-0/)

如若转载,请注明出处： <https://www.helpnetsecurity.com/2026/01/27/descope-agentic-identity-hub-2-0/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [行业资讯](/tag/%E8%A1%8C%E4%B8%9A%E8%B5%84%E8%AE%AF)

**+1**0赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **970**

* 粉丝
* **6**

### TA的文章

* ##### [反制黑客：研究人员对“哈萨克远控木马”间谍攻击活动实施黑洞诱捕](/post/id/314594)

  2026-01-28 10:10:00
* ##### [人机验证陷阱：ClearFake恶意软件诱导用户自我入侵](/post/id/314580)

  2026-01-28 10:09:09
* ##### [“G\_Wagon”恶意软件藏身仿冒NPM界面库，伺机窃取云服务密钥](/post/id/314577)

  2026-01-28 10:09:08
* ##### [CVE-2026-0994：谷歌Protocol Buffers曝出高严重性拒绝服务漏洞](/post/id/314571)

  2026-01-28 10:08:23
* ##### [法国将弃用Zoom和Teams，改用本土自主研发平台Visio](/post/id/314576)

  2026-01-28 10:08:22

### 相关文章

* ##### [反制黑客：研究人员对“哈萨克远控木马”间谍攻击活动实施黑洞诱捕](/post/id/314594)

  2026-01-28 10:10:00
* ##### [人机验证陷阱：ClearFake恶意软件诱导用户自我入侵](/post/id/314580)

  2026-01-28 10:09:09
* ##### [“G\_Wagon”恶意软件藏身仿冒NPM界面库，伺机窃取云服务密钥](/post/id/314577)

  2026-01-28 10:09:08
* ##### [CVE-2026-0994：谷歌Protocol Buffers曝出高严重性拒绝服务漏洞](/post/id/314571)

  2026-01-28 10:08:23
* ##### [法国将弃用Zoom和Teams，改用本土自主研发平台Visio](/post/id/314576)

  2026-01-28 10:08:22
* ##### [布鲁塞尔对马斯克旗下人工智能企业展开深度伪造调查，科技对峙局势升级](/post/id/314572)

  2026-01-28 10:07:52
* ##### [遭攻击：微软紧急修复Office零日漏洞（CVE-2026-21509），漏洞已在野被利用](/post/id/314561)

  2026-01-28 10:07:36

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
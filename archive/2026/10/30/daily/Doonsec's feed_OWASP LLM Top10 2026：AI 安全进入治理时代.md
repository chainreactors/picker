---
title: OWASP LLM Top10 2026：AI 安全进入治理时代
url: https://mp.weixin.qq.com/s/fpRGdg-0qGhAHY6xh_2kHA
source: Doonsec's feed
date: 2026-10-30
fetch_date: 2026-10-31T07:44:34.893464
---

# OWASP LLM Top10 2026：AI 安全进入治理时代

# OWASP LLM Top10 2026：AI 安全进入治理时代

原创

CSL
CSL

联想全球安全实验室

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**点击蓝字**

**关注我们**

**Lyric**

**从模型安全到 Agent 治理，企业需要重新定义 AI 安全边界**

当企业开始部署越来越多的 Agent 时，安全团队需要管理的已经不只是系统和数据，而是一批拥有权限、能够执行任务、会直接影响业务结果的数字员工。

**前言**

OWASP Top 10 真正变化的不是漏洞，而是治理对象。过去二十年，OWASP Top 10 一直被视为应用安全领域的重要风向标。

很多人在关注 OWASP LLM Top 10 2026 新增了哪些风险。但在笔者看来，更值得关注的问题是：为什么这些风险会出现。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0UKPAuBeu7llZribYwKSpOWCWxnERUNehicOaiaPaSNsJuM4gGfic28vWKiaavY9jNibaPdicchSI5sjyghTib5NTdVBMFOVehsL8ickxgZOKib5ATibVk/640?wx_fmt=png)

**图1：从模型到治理**

在大模型应用初期，业界关注的主要是越狱、提示词注入、敏感信息泄露等模型层风险；而随着 Agent、RAG、MCP 和工具调用能力开始进入真实业务场景，企业面对的挑战已经不再局限于模型本身。

Agent 开始接入知识库、调用 MCP、连接业务系统、操作数据库、发送邮件、创建工单，甚至参与实际业务流程。AI 正在从一个负责回答问题的工具，变成一个能够执行任务的系统。

OWASP LLM Top 10 2026 最重要的变化，不是新增了哪些漏洞，而是 AI 安全关注点正在从模型安全（Model Security）扩展到 Agent 安全（Agent Security），并进一步延伸至整个 AI 生态的治理问题。

目前针对 AI 安全的关注点正在发生迁移，安全关注点正在从模型本身逐渐扩展到围绕模型构建的整个运行生态。对于企业安全来说，需要解决的问题已经不再只是“模型是否安全”，而是“企业是否能够管理这些越来越有能力的 Agent”以及“企业如何能够'安全'地使用这些越来越有能力的 Agent”。

![](https://mmbiz.qpic.cn/mmbiz_png/8P2MPgLgDcgyd1jJeibtDvLJutcYE2f14ibPuP5fV6wnicVcLBskbyiaaxVV6VBZfWDR6FSskGriaJkOddptyCpfJ22pSesSkbugj9D12EXERniak/640?wx_fmt=png)

**PART.01**

**Prompt Injection**

**已经变成业务安全问题**

Prompt Injection 一直被认为是大模型最典型的攻击方式。在过去，大多数攻击影响的是模型输出。例如泄露提示词、绕过限制、生成违规内容等。

但在 Agent 时代，一次 Prompt Injection 可能直接影响业务执行。因为今天的 Agent 往往拥有：

* 访问知识库的权限
* 查询数据库的权限
* 发送邮件的权限
* 调用业务系统的权限

![](https://mmbiz.qpic.cn/mmbiz_jpg/0UKPAuBeu7nm8VQqhP73gMegBZibvc8L4d9nWmMrDhm9MAsI3KeM0eCG0IjysKvmhHjyIX0Ge4zQY6KE6T5iauFQAd98iahCbOxwourpD35s58/640?wx_fmt=jpeg)

**图2：业务风险增加**

攻击者真正感兴趣的已经不是让模型说错一句话，而是让 Agent 做错一件事。

一个被成功注入的 Agent，可能读取敏感数据、发送错误指令、修改业务配置，甚至执行高风险操作。因此，Prompt Injection 已经不再只是内容安全问题，而是业务安全问题。未来企业需要保护的不只是模型输入，更要保护 Agent 的决策过程和执行过程。

![](https://mmbiz.qpic.cn/mmbiz_png/8P2MPgLgDcgyd1jJeibtDvLJutcYE2f14ibPuP5fV6wnicVcLBskbyiaaxVV6VBZfWDR6FSskGriaJkOddptyCpfJ22pSesSkbugj9D12EXERniak/640?wx_fmt=png)

**PART.02**

**未来企业 AI 重大安全事件**

**可能首先发生在供应链**

软件行业对供应链风险并不陌生。过去几年，从开源组件漏洞到软件供应链攻击，越来越多事件表明，攻击者正在从“攻击单个系统”转向“影响整个生态”。

随着模型、MCP、Agent Framework 以及第三方插件被广泛引入企业环境，类似的趋势正在AI领域快速出现。

一个典型的企业 Agent 背后，往往涉及基础模型、Embedding 模型、Agent Framework、MCP 服务、第三方插件以及外部 API 等多个组件。

![](https://mmbiz.qpic.cn/mmbiz_png/0UKPAuBeu7l7Hx3kicU3hxEYhkcCF5WaolEnRtvOnH6VJUdPOSiaLdWibzh3tum3gtuiaKCLUAxuO3IONtsQ1p1v0vkY7bd5gJJa8Qbicpbonq8M/640?wx_fmt=png)

**图3：供应链风险扩展**

企业信任的，已不再是一个模型，而是一整条 AI 链路。

这意味着任何一个环节出现问题，都可能影响最终结果。一个恶意插件、一个被篡改的 MCP 服务、一个存在后门的 Agent 框架，都可能成为攻击入口。因此未来 AI 领域的大型安全事件，很可能首先发生在供应链，而不是模型本身。

企业需要建立自己的 AI 资产台账和 AI 供应链管理机制，清楚知道自己正在使用什么、依赖什么、信任什么。

![](https://mmbiz.qpic.cn/mmbiz_png/8P2MPgLgDcgyd1jJeibtDvLJutcYE2f14ibPuP5fV6wnicVcLBskbyiaaxVV6VBZfWDR6FSskGriaJkOddptyCpfJ22pSesSkbugj9D12EXERniak/640?wx_fmt=png)

**PART.03**

**Agent 正在成为企业**

**新的****高权限主体**

这是 OWASP LLM Top 10 2026 中最值得我们关注的变化之一。在很多企业场景中，Agent 拥有的实际权限范围甚至可能超过普通员工。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0UKPAuBeu7kRh5NfDglo5jpJH2M9iaibNibxI4Ie1GKzJtCcrBeQ7J1PfTFAsXfUcibW9450VhOicP5tlf2nDbstcHKXG2TshCFAhHwg3JunM2o0/640?wx_fmt=png)

**图4：Agent 成为新主体**

过去几十年，企业安全体系主要围绕“人、系统、数据”三个对象构建。而在 Agent 逐步融入业务流程后，组织内部实际上诞生了一类新的数字主体。

与传统自动化脚本相比，Agent 具备任务理解、规划、协同甚至自主执行能力，这些行为将直接影响业务结果。因此，Agent 已经不适合再被简单视为一个程序组件。从治理视角看，它更接近一种具备特定权限和职责边界的新型身份主体。

企业需要回答：

* Agent 有哪些权限？
* Agent 能访问哪些系统？
* Agent 执行了什么操作？
* Agent 出了问题谁负责？

这些问题已经超出了传统应用安全范畴，开始进入身份治理、权限治理和风险治理领域。

未来几年，Agent Governance 很可能成为企业安全建设的重要方向。

![](https://mmbiz.qpic.cn/mmbiz_png/8P2MPgLgDcgyd1jJeibtDvLJutcYE2f14ibPuP5fV6wnicVcLBskbyiaaxVV6VBZfWDR6FSskGriaJkOddptyCpfJ22pSesSkbugj9D12EXERniak/640?wx_fmt=png)

**PART.04**

**传统身份治理体系正在失效**

很多企业认为，增加几次 AI 测试、红队评估或者越狱验证，就能够解决 AI 安全问题。事实上远远不够。

过去企业已经建立了较为成熟的身份管理、权限管理、审计管理和合规管理体系，但这些体系最初都是围绕人类用户设计的。

当越来越多业务活动由 Agent 完成时，企业会遇到一系列新的管理问题。例如：Agent 账号归属谁管理、Agent 触发高风险操作时如何审批、Agent 访问敏感数据如何留痕、Agent 产生错误决策后如何界定责任等。

这些问题在传统安全体系中往往缺少成熟经验。

因此，OWASP 2026 释放的重要信号并不是攻击面扩大本身，而是企业现有治理框架需要完成一次面向 AI 时代的升级。

![](https://mmbiz.qpic.cn/mmbiz_png/8P2MPgLgDcgyd1jJeibtDvLJutcYE2f14ibPuP5fV6wnicVcLBskbyiaaxVV6VBZfWDR6FSskGriaJkOddptyCpfJ22pSesSkbugj9D12EXERniak/640?wx_fmt=png)

**PART.05**

**AI 安全正在走向生态治理**

如果把前面几个变化放在一起观察，会发现它们都指向同一个现状：**企业今天面对的已经不再是一个模型，而是一个包含 Agent、RAG、Memory、MCP、Tool、Plugin 以及业务系统的复杂生态。**

早期 AI 应用通常围绕“用户、模型、输出结果”构建。而今天的企业 AI 系统往往涉及 Agent、记忆系统、知识库、工具链、MCP 服务以及各种业务系统。随之扩大的不仅是系统能力，还有攻击面和风险边界。数据、身份、权限、工具、供应链以及运行环境，都可能成为影响最终安全状态的关键因素。

因此，AI 安全治理的重点将不再局限于模型防护，而是建立覆盖数据、身份、权限、供应链和运行环境的整体治理体系。

换句话说，AI 安全正在从模型安全走向生态治理。

**企业安全团队应该如何应对？**

![](https://mmbiz.qpic.cn/mmbiz_png/8P2MPgLgDchFDP9iceGiaasCavoxhhrl6IxCfnVmIy5hibr5Ueodn9iasSmJe3iat9x00OwuQSvYghRo5GHPWEkUPgWcZ759oDMCCia9ZNBCukmL4/640?wx_fmt=png)

面对新的风险版图，仅依靠传统应用安全体系已经无法满足需求。

企业需要将 AI 纳入现有安全治理框架，并围绕资产、身份、供应链、运行时安全和持续验证构建系统化能力。

![](https://mmbiz.qpic.cn/mmbiz_png/0UKPAuBeu7kKqvyBXJdW9icCl2oLCXYD5ZLYNbSgaXJUnofZEI9pDEJfoXiceUtF9IGEompgc5k0R4jrjfibrl4YD8x0MhX7vRRuMgiaXVicV0Xw/640?wx_fmt=png)

**图5：AI 治理能力框架**

**第一，建立 AI 资产管理能力**

企业首先需要回答一个基础问题：组织内部到底部署了多少AI能力。明确有多少模型有多少 Agent，接入了多少 MCP 服务，使用了哪些第三方插件。看不见的资产，无法被治理。模型、Agent、MCP 服务、插件以及第三方 AI 服务都应纳入统一资产管理范围。

**第二，建立 Agent 权限治理能力**

Agent 权限设计应遵循最小权限原则，并建立高风险操作审批、权限定期审计以及异常行为监测机制，避免 Agent 获得超出业务需求的权限。

**第三，建立 AI 供应链治理能力**

持续评估模型来源、框架来源、MCP 服务来源以及第三方插件来源，构建可追溯的信任链条。

**第四，建立 AI 红队能力**

针对 Prompt Injection、Tool Abuse、Goal Hijacking、Context Poisoning 等典型场景开展持续验证，而非一次性测试，确保安全控制能够经受真实攻击场景验证。

**第五，建立 Agent 治理框架**

未来企业需要像管理员工一样管理 Agent。围绕身份、权限、行为审计、风险监测和责任归属建立完整治理机制，将 Agent 真正纳入企业安全管理体系。

**笔者观察：企业正在迎来新的治理对象**

![](https://mmbiz.qpic.cn/mmbiz_png/8P2MPgLgDchFDP9iceGiaasCavoxhhrl6IxCfnVmIy5hibr5Ueodn9iasSmJe3iat9x00OwuQSvYghRo5GHPWEkUPgWcZ759oDMCCia9ZNBCukmL4/640?wx_fmt=png)

OWASP LLM Top 10 2026 真正释放的信号是：AI 安全的核心正在从漏洞防护转向治理建设。

当 Agent 开始拥有权限、执行任务并影响业务结果时，企业需要面对的不再只是模型风险，而是治理风险。

AI 正在成为新的生产力。

Agent 正在成为新的数字主体。

未来决定企业 AI 安全水平的，未必是谁部署了更多 Agent，而是谁能够率先建立成熟、可信、可持续运营的 Agent 治理体系。

对于企业而言，最重要的问题或许已经不是如何使用 AI，而是如何治理 AI。

**往期精彩合集**

●[自进化长效智能体：Prime Agent 项目全方位解析](https://mp.weixin.qq.com/s?__biz=MzU1ODk1MzI1NQ==&mid=2247494845&idx=1&sn=13d80f3810c5911ba87f371f2c65fe4f&scene=21#wechat_redirect)

●[Lenovo thinkstation PGX 修复与多卡连接](https://mp.weixin.qq.com/s?__biz=MzU1ODk1MzI1NQ==&mid=2247494550&idx=1&sn=ee2bba2a018f9e94fb8aadf639d7bf8e&scene=21#wechat_redirect)

●[模型再强也救不了：你还没看过推理引擎怎么跑](https://mp.weixin.qq.com/s?__biz=MzU1ODk1MzI1NQ==&mid=2247494504&idx=1&sn=b9c6188a4cf15c52df8fe796ad70facc&scene=21#wechat_redirect)

●[色不异空——不可思议的“侧信道攻击”](https://mp.weixin.qq.com/s?__biz=MzU1ODk1MzI1NQ==&mid=2247494437&idx=1&sn=a92c09a15c1f15211d3b2b559ead8e4d&scene=21#wechat_redirect)

●[AI 重构软件供应链安全：既是“矛”，也是“盾”](https://mp.weixin.qq.com/s?__biz=MzU1ODk1MzI1NQ==&mid=2247494722&idx=1&sn=7b9cbac401125cde87c0562fb9eb3eba&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/0UKPAuBeu7nJ096D4fKNIjice1LYJePZ1kAZpDPzXMAhibggTiajnjue7iaLap5prXiaK76TvJ0ZUKHtjX6EiaNk2wUzGN9dvLgeNDntLzN6UCBD4/640?wx_fmt=gif&from=appmsg)

预览时标签不可点

不喜欢

![]()

微信扫一扫
关注该公众号

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/PicDhHpwdziaibPZd0FJCTel2o5j0mRe7AsGTibmwUbRoonkSFQBNETSL4jqgjKSCE7z3B8KeR9q94miagM69SFsB3A/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过
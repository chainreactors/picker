---
title: 活动回顾｜慢雾创始人余弦出席首届 Agentic AI 创新与安全论坛
url: https://mp.weixin.qq.com/s/IoI7Rfq3g8Q7EZN3Ct73ag
source: Doonsec's feed
date: 2026-04-01
fetch_date: 2026-04-02T04:26:43.380716
---

# 活动回顾｜慢雾创始人余弦出席首届 Agentic AI 创新与安全论坛

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8z8bibAexaCITAhibvubPhhicVOH6dHibT1NuYPn4CM8d4ciaHWyk2Yl6TmFuVSzv6SGP4BDqbYkWq2pptbia6vCpMlHm4GxVoW7xeZjIRQfE8cl8/0?wx_fmt=jpeg)

# 活动回顾｜慢雾创始人余弦出席首届 Agentic AI 创新与安全论坛

慢雾科技

![]()

在小说阅读器中沉浸阅读

******# 3 月 27 日，由香港数码港、ME Group 及 iPollo 联合主办的首届 Agentic AI 创新与安全论坛暨香港第一届 Web 4.0 国际峰会在香港数码港盛大举行。本次峰会以“Agentic AI 创新应用：Web 4.0 时代的技术变革与产业融合”为主题，汇聚了香港特区政府财政司司长陈茂波、香港数码港主席陈细明、香港数码港董事及 Nano Labs 创始人孔剑平以及著名天使投资人蔡文胜等政产学研各界顶尖力量，共同探讨 AI 从“对话”向“行动”跨越新纪元下的机遇与挑战。

在代理式人工智能(Agentic AI) 备受瞩目的当下，其带来的安全议题尤为关键。慢雾(SlowMist) 创始人余弦受邀出席本次峰会，并发表了题为《AI 与加密世界的安全挑战及防御创新》的主题演讲，与全球行业领袖分享了慢雾(SlowMist) 在 AI 安全领域的最新观察与实践。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8z8bibAexaCIvXWA9ibGDhJBJsVoeTYksSib9JdWq8ouqAjFYSQHt5tw5tGQHmv0wCjbJHGJOLZtnFNOTXCkkJQuEkHJbNOBwrQ0hWcFNztlEA/640?wx_fmt=jpeg&from=appmsg)

##******

******## 聚焦前沿：深度剖析 OpenClaw 与 AI Agent 安全威胁

随着 AI 技术不断渗透加密世界，以“养龙虾”(OpenClaw) 为代表的 AI Agent 应用迅速走红。但在热潮背后，一个更深层的问题正在浮现：AI Agent 的安全边界，尚未真正建立。

在演讲中，余弦从 OpenClaw 入手进行了深入拆解，并提出了一个关键判断：“文本即指令。”他解释称，在 AI Agent 的运行语境中，所有输入都不再只是“信息”，而是潜在可执行的指令。这意味着模型接收到的任何外部信息——无论来源是用户输入、文档说明，还是第三方 Skill——都有可能被直接解释并执行，从而将攻击面从代码层扩展到“认知层”。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8z8bibAexaCLFSHnIdONt2TG1nBmUIWM5Hfmj01miakwrVQlsDcHdW12lI2MxTByib54R2uLHhyQjCh1sC6dYVN1XNibabb1IAOic55CcJlwOTmA/640?wx_fmt=jpeg&from=appmsg)

在这一机制下，攻击路径被极大简化。攻击者无需突破传统安全防线，只需构造精心设计的文本内容，就可能诱导 Agent 执行非预期操作，例如资产转移、敏感信息泄露，甚至远程命令执行。这种攻击路径的隐蔽性和低成本，使其具备极高的现实威胁。

基于上述机制，余弦进一步总结了当前 OpenClaw 面临的三类核心风险：

* 输入与意图操控（用户交互层）： 攻击者可通过“直接提示词注入”诱骗 Agent 执行高危操作。特别值得警惕的是间接供应链投毒——攻击者在 Skill 的 Markdown 文档中植入恶意指令。由于 Markdown 往往承担“安装入口”角色，原本的“说明文本”极易演变为恶意执行脚本（如 curl | bash），导致数据窃取。
* 决策与编排层风险（应用逻辑层）： 这种错误并非来自模型本身，而是来自“错误的执行逻辑”。攻击者可以干扰 Agent 的逻辑推理，使其在加密货币转账等业务流程中篡改收款地址，造成直接资金损失。
* 模型层风险（核心大脑）： 包括模型产生的“幻觉”导致其执行不存在或危险的系统命令，以及模型从训练数据中误学到的不安全操作模式。

余弦指出，“OpenClaw 所暴露的问题并非孤立现象，而是当前 AI Agent 生态普遍面临的结构性挑战。”换句话说，安全问题已经不再是某一个项目的“个案”，而是整个行业都必须正视的系统性风险。

## 攻防兼备：构建 AI Agent 的安全开源生态

面对不断演化的威胁形态，余弦在演讲中提出了慢雾(SlowMist) “攻防兼备”的安全思路：不仅要理解攻击路径，更要将防御能力嵌入 Agent 的运行机制，实现安全内建。

他向与会嘉宾展示了慢雾(SlowMist) 围绕 AI Agent 所构建的一系列开源工具与实践方案，旨在推动形成一个透明、可验证、可复用的安全生态：

* [OpenClaw 极简安全实践指南](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247504374&idx=1&sn=aa99d127fe69cabd9107ea6c24cc08c2&scene=21#wechat_redirect)：一份从认知层到基础设施层的端到端安全部署手册，为高权限AI Agent在真实生产环境中的部署提供了系统性的“安全思想钢印”。
* [SlowMist Agent Security Skill](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247504542&idx=1&sn=877bb46e71ffb4b97ef69748773ee304&scene=21#wechat_redirect)：一个综合安全审查框架，为 OpenClaw 等智能体增加一双“慧眼”。它不仅能发现常规 Skills 的投毒风险，还能识别链上钱包地址、代码仓库及 URL 的风险。
* [MistTrack Skills](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247504357&idx=1&sn=c632f2459fe03685f87d2016f1d825ee&scene=21#wechat_redirect)：一个即插即用的 Agent 技能包，为 AI Agent 提供专业的加密货币 AML 合规与地址风险分析能力，可用于链上地址风险评估与交易前风险判断。
* [MCP Security Checklist](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247501811&idx=1&sn=6a798626f6205fa8bac0d87f78c675a9&scene=21&poc_token=HBzBzGmjYFjAT41NrB4hmQMyXh7tkpVblhw_92EF#wechat_redirect)： 一份体系化的安全检查清单，用于快速审计和加固 Agent 服务，帮助团队在部署 MCPs/Skills 及相关 AI 工具链时避免遗漏关键防御点。
* [恶意 MCP 演示](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247501940&idx=1&sn=729c9b768a35b9299ff9ffd15676c68f&scene=21#wechat_redirect)：一个开源的恶意 MCP 服务器示例，用于复现真实攻击场景并测试防御体系的健壮性，可用于安全研究与防御验证。

通过这一系列实践，余弦强调：”安全能力必须内建于 Agent，而非仅依赖外围防护。”只有将防御机制与 Agent 的运行逻辑深度绑定，AI Agent 才能在复杂的 Web3 与 AI 生态中持续、安全地运作。

## 系统化安全：ADSS 全面防护 AI + Web3 生态

在演讲最后，余弦介绍了慢雾(SlowMist) 提出的 ADSS (AI Development Security Solution)。

如果说前述工具属于“战术能力”，那么 ADSS 更像是一套系统级安全框架。其核心理念是：将零散的安全动作升级为可执行、可审计、可持续的系统化安全运营机制。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8z8bibAexaCJPP0ZYu1kNbMHbbK49UZo73780AjuetbR5OrgJLLRCccUNEicicgEicvpVfZgia6nX9e7wBbic7WHHMDibicrQNLgxYdibSAs7dUoaxk8/640?wx_fmt=png&from=appmsg)

ADSS 从多个层面构建 AI + Web3 的安全治理能力：

* L1 安全治理（开发基线）：建立统一的开发与使用安全标准，覆盖开发工具、Agent 框架、插件生态及运行环境，为团队提供统一的策略来源与审计标准。
* L2 权限与操作约束：通过收敛 Agent 权限边界、最小化工具调用权限、引入关键操作的人机确认机制，有效控制高风险行为的执行范围。
* L3 外部交互防护：在 URL、依赖仓库、插件来源等外部资源层面引入实时威胁感知，降低恶意内容或供应链投毒进入执行链路的概率。
* L4 链上资产隔离：针对涉及链上交易的操作，结合链上风险分析与独立签名机制，使 Agent 能构造交易而不直接接触私钥，减少高价值资产操作带来的系统性风险。
* L5 持续巡检与复盘：通过日志审计、周期性安全复核与运营机制，实现“执行前可预检、执行中可约束、执行后可复盘”的闭环安全能力。

余弦指出，ADSS 并非单一工具，而是一套可持续、可演进的安全运营体系。它旨在在不显著降低开发效率和自动化能力的前提下，通过系统化策略、持续审计与能力联动，帮助团队构建可审计、可升级的 Agent 安全体系，从而应对 AI 与 Web3 深度融合背景下不断演化的安全威胁。

## 结语******

******## 首届 Agentic AI 创新与安全论坛不仅汇聚了行业顶尖力量，也为 AI Agent 安全提供了前瞻性思路。随着 Agentic AI 与 Web3 的深度融合，安全挑战将持续升级。作为全球领先的区块链安全公司，慢雾(SlowMist) 将继续推动系统化安全治理落地，通过 ADSS、开源工具与实践，为 AI Agent 构建内生安全能力，助力行业在创新浪潮中实现安全可控、可持续发展。******

**往期回顾**

[Odaily专访余弦：Anthropic核弹级新模型泄漏，如何影响加密安全攻防？](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247504594&idx=1&sn=88d0a2ea27ea5f4bd87967e3411848f6&scene=21#wechat_redirect)

[慢雾：Web3 安全年框服务全面升级](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247504592&idx=1&sn=5b14e6284530b087155c3c9b13b86e3c&scene=21#wechat_redirect)

[安全预警：Apifox 桌面客户端官方 CDN 脚本遭供应链投毒](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247504575&idx=1&sn=fa2ad5b1d103daaa52b67a16aa6fcef8&scene=21#wechat_redirect)

[LiteLLM 供应链攻击事件始末](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247504575&idx=2&sn=0602625406cc37b3c62e48b13ce706dd&scene=21#wechat_redirect)

[SlowMist Agent Security Skill 正式发布，守护 AI Agent 每一道防线](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247504542&idx=1&sn=877bb46e71ffb4b97ef69748773ee304&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbEP8f4tadFenoLauzHpicWdWbVap3aia38LUGPflBho9ibDHXjoG5fecGJSaYa4S4zYdoicXibSmjv9tg/640?wx_fmt=png&from=appmsg)

**慢雾导航**

**慢雾科技官网**

*https://www.slowmist.com/*

**慢雾区官网**

*https://slowmist.io/*

**慢雾 GitHub**

*https://github.com/slowmist*

**Telegram**

*https://t.me/slowmistteam*

**Twitter**

*https://twitter.com/@slowmist\_team*

**Medium**

*https://medium.com/@slowmist*

**知识星球**

*https://t.zsxq.com/Q3zNvvF*

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbCKRaQNEUrvPEphjODejx61A2PcXPPj3dFegU3unrp2nr60oBfYXAZDj99nIXojoia9p6UDy4iaqQw/0?wx_fmt=png)

慢雾科技

向上滑动看下一个

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbCKRaQNEUrvPEphjODejx61A2PcXPPj3dFegU3unrp2nr60oBfYXAZDj99nIXojoia9p6UDy4iaqQw/0?wx_fmt=png)

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
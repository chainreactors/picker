---
title: Grok 被利用背后：AI Agent 权限链滥用分析
url: https://mp.weixin.qq.com/s/l5RwiwhMb3_Y6i_SR2NZqw
source: Doonsec's feed
date: 2026-05-06
fetch_date: 2026-05-07T05:25:44.078505
---

# Grok 被利用背后：AI Agent 权限链滥用分析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8z8bibAexaCJ2hNABVy38kmqBuQR979iaia2pnAiaxPRaKSS0sdSBdPRwHQ8dwWZ42zXmDEUN8NlU5v3G0AoLMVeoXKvsemjknf0LVlMickO0mhk/0?wx_fmt=jpeg)

# Grok 被利用背后：AI Agent 权限链滥用分析

慢雾安全团队
慢雾安全团队

慢雾科技

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

******# 背景

近日，Base 链上发生一起针对 AI Agent 与自动化交易系统结合的权限滥用事件。攻击者通过在 X 平台向 @grok 发送特定构造内容，诱导其输出被外部交易 Agent (@bankrbot) 识别的转账指令，最终导致链上真实资产转移。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8z8bibAexaCJ4X4lK2QpUdruHd7OYibicolscCZkS3VNgmIpDYmhIhu2Y5CbYGqUOnZUNfQP0LZxZV8YxpJJkaDZrdx9ibaeszrrQPfUKJqDllw/640?wx_fmt=png&from=appmsg)

(https://x.com/bankrbot/status/2051192437797015859)

## 关于“Grok 钱包”：

事件中被标记为“Grok 钱包”的地址 (0xb1058c959987e3513600eb5b4fd82aeee2a0e4f9) 并不属于 xAI 官方控制。该地址是由 @bankrbot 为 X 账号 @grok 自动生成的关联钱包，私钥由 Bankr 依赖的第三方钱包服务托管，实际控制权在 Bankr 手中。BaseScan 已将该地址标签由 “Grok” 修正为 Bankr 1 等相关标识。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8z8bibAexaCJAuDvhc4WjbK3cK9LZmQBBHM3UrI1hQlCLtTHCYwcpKG1ktXLMapDarvNhviaqxx7XnaPtW4hicJBqsRRjbSqibeRhfGPg55v2Q4/640?wx_fmt=png&from=appmsg)

(https://basescan.org/address/0xb1058c959987e3513600eb5b4fd82aeee2a0e4f9)

该钱包持有的大量 DRB（约 30 亿枚），同样源于 Bankr 的机制设计：今年早些时候，有用户向 Grok 询问代币命名建议，Grok 回复 “DebtReliefBot”（简称 DRB）。随后，Bankr 系统将该回复解析为部署信号，在 Base 链上触发了相关代币的创建流程，并按照其 Launchpad 规则，将创建者份额分配至该关联钱包。

# 攻击流程

本次攻击主要分为权限升级和指令注入两个关键阶段，形成了“不可信输入 → AI 输出 → 外部 Agent 执行 → 资产转移”的完整链路。

1.权限升级阶段

攻击者（关联地址 ilhamrafli.base.eth）通过中心化机制开通了该钱包的 Bankr Club Membership。这一操作解锁了 @bankrbot 的高权限工具集（agentic toolset），为其后续转账执行提供了必要权限。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8z8bibAexaCJ5zRiaoFhWtt4XGn5iaC82DsxzC1tHzpgBr51M6tF0tKklu95Jvmd7g0JdQPiauwScVy8ZCGfAh9ibU2Biarskt9TlaWbpAJColicicU/640?wx_fmt=png&from=appmsg)

(https://x.com/bankrbot/status/2051005172202258526)

2.Prompt Injection 执行阶段

攻击者向 @grok 发送一段精心构造的摩尔斯电码（Morse Code），Grok 按照用户要求进行翻译/解码后，输出了明文指令并 @bankrbot。@bankrbot 将 Grok 的公开回复视为有效可执行命令，直接在 Base 链上发起转账操作。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8z8bibAexaCJ32lwg2xJH4pEV1sUqqAYia5MU9icZunTLa9w7z5e5Qs9U3yuUpkEibibRSQNjEVicYPz2WCTUy2u8etNl4gibkQLueoaeDCJqvdgMc/640?wx_fmt=png&from=appmsg)

(https://basescan.org/tx/0x6fc7eb7da9379383efda4253e4f599bbc3a99afed0468eabfe18484ec525739a)

攻击者随后迅速将 DRB 兑换为 USDC/ETH。攻击完成后，相关账号快速删除内容并下线。

本次攻击的巧妙之处在于，充分利用了 Grok 的“帮助性”响应特性，绕过了 @bankrbot 对指令来源的常规过滤，构建起 AI 输出与链上执行的闭环。

## 资金追回情况

事件发生后，社区与 Bankr 团队追踪显示，约 80%~88% 的资金价值已通过协商形式回流（主要以 USDC 和 ETH 形式）。剩余部分据相关方表述，作为非正式 bug bounty 处理。Bankrbot 已公开确认攻击细节，并采取了相应限制措施。

## 根本原因分析

* 信任模型缺陷：Bankrbot 将 Grok 的自然语言输出直接映射为可执行金融指令，而未对指令来源、意图真实性或异常模式（摩尔斯电码等非标准编码）进行充分验证。
* 权限隔离不足：会员资格激活直接赋予高危工具权限，缺乏二次确认或额度限制。
* Agent 间边界模糊：Grok 作为对话式 AI，其输出本不应等同于金融授权，但被下游执行层视为可信信号。
* 输入处理风险：LLM 容易被提示注入或非标准编码绕过安全过滤器，这已是已知问题，但在与真实资产执行层结合时放大为高额损失。

值得强调的是，Grok 本身并未持有私钥或直接执行链上操作，它更像是被利用的中间环节，真正的执行主体是 @bankrbot 的自动化交易体系。

# 安全启示

此次事件为 AI + Crypto Agent 领域提供了重要实战教训：

* 自然语言输出必须与金融动作严格解耦；
* 高价值操作需引入多重验证、额度控制、异常检测（编码类型、金额阈值、来源白名单等）；
* Agent 间交互应优先采用结构化、可验证的协议，而非纯文本指令；
* Prompt Injection 威胁模型需纳入全链路 Agent 设计，包括间接利用其他 AI 的能力。

# 总结

这是一起典型的 AI Agent 权限链安全事件。尽管 Grok 被 Prompt Injection 利用，但问题的根本在于：Bankrbot 体系中，将 AI 输出与真实资产执行层进行松散绑定。该事件为 AI + Crypto Agent 领域提供了一个极具参考价值的实战案例，也明确传递出一个信号：当 Agent 被赋予链上执行能力时，必须建立严格的信任边界与安全控制机制。未来，相关基础设施的安全设计仍需持续强化，以应对这一类跨系统、跨语义边界的新型攻击模式。******

**往期回顾**

[慢雾出品｜链接真实世界资产：从协议族解析到安全实践](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247504861&idx=1&sn=0f71a6b7fafe17ee9cd5e6cf07b83e41&scene=21#wechat_redirect)

[慢雾 2026 香港 Web3 嘉年华之旅圆满收官!](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247504841&idx=1&sn=289fc7c20f2f00f8313ea5a5c378f90f&scene=21#wechat_redirect)

[Hacking Time 回顾：慢雾携手行业专家，深度拆解 AI & Web3 的攻防新范式](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247504768&idx=1&sn=4589da9b7bea88de8f7b4dbd5cbfd0c8&scene=21#wechat_redirect)

[专访慢雾：Kelp DAO rsETH × LayerZero 事件是 DeFi 乐高结构系统性风险的集中爆发](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247504741&idx=1&sn=73749cca984e571fbcd6cac83e515423&scene=21#wechat_redirect)

[解读｜FBI 发布《2025 年互联网犯罪报告》](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247504729&idx=1&sn=aa1c7332bba7ac7bbe4f74220e2322e6&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_png/8z8bibAexaCLqYqc9l9poJTcO8JBsibl6nSSJoiaasoqFToYClTV5oAl2oE6IcqhNsiciagmyhOAsRCrdxdrOKqxpZicVQqlu0WrcOb5vDfKMGsSc/640?wx_fmt=png&from=appmsg)

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
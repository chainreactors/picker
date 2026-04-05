---
title: Claude Code 源代码泄露数天后发现高危漏洞
url: https://mp.weixin.qq.com/s/uBXEx-nkeFOdRI3VjTJicw
source: Doonsec's feed
date: 2026-04-04
fetch_date: 2026-04-05T04:35:46.629011
---

# Claude Code 源代码泄露数天后发现高危漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6TibdXOYxjiaPoxoW63hEfAkgFvz5xVnyJVTvsWOVwNgVyhKxJj5xE30LsBs38TNl8A5LfUel7Ihd6JJjm4Bwa38A79sDHtLfnczyo/0?wx_fmt=jpeg)

# Claude Code 源代码泄露数天后发现高危漏洞

幻泉之洲

![]()

在小说阅读器中沉浸阅读

> 本文分析了Anthropic公司AI开发助手Claude Code近期遭遇的安全事件：先是源映射意外泄露导致51.2万行源代码暴露，随后Adversa AI团队又发现其权限系统中的高危安全绕过漏洞。该漏洞可导致‘deny’规则被静默跳过，使攻击者可能窃取开发者凭据、污染研发流水线。

## 事件概述

Anthropic的AI编程助手Claude Code近期接连遭遇打击。先是3月底源代码意外泄露，几天后，安全团队又在其权限系统中发现了一个高危漏洞。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6Tibe9LadzX9DWdb9w0qmUxmKsAic6DZhQ7m1Qpt3Jg9En903Fwr6xFWfal2XTsKic3etDvuoRN9P3GbgTCYnltqbnRbR2Dt9bwEdtQ/640?wx_fmt=png&from=appmsg)

## 源代码泄露事件

3月31日，Anthropic在发布Claude Code v2.1.88时，不小心把用于调试的JavaScript源映射（sourcemap）文件也打包到了npm包中。研究员Chaofan Shou很快发现了这一点，并在X上公布了链接。全球安全研究人员随即开始研究这些反混淆后的代码。

来自英属哥伦比亚大学的25岁学生Sigrid Jin与Yeachan Heo合作，成功重构了Claude Code。雅虎的报道说，他们两个人，用了10台OpenClaw，一台MacBook Pro笔记本，花了几小时就重建并共享了这款流行AI助手的源代码。这再次证明，信息一旦上网，就很难彻底消失。

现在，网上流传着这些重构的代码，包含1900个文件，总计约51.2万行TypeScript代码。

这对Anthropic来说很尴尬，但还算不上灾难。Tanium公司的安全与产品设计研究高级总监Melissa Bischoping解释说，虽然Claude Code泄露确实带来了风险，但这和模型权重、训练数据或客户数据被泄露不一样。这次曝光的东西，更像是当前版本Claude Code如何工作的“操作蓝图”。

关键在于，研究人员虽然能看清Claude Code是如何工作的，却无法真正重建它，因为泄露内容不包含Claude模型权重、训练数据、客户数据、API接口或凭据。Bischoping继续解释：“这并非一份通往完美攻击的路线图，但它确实提供了关于该工具如何处理输入、强制执行权限和抵抗滥用的深刻洞察。”

她还补充了一个风险：“这次泄露的另一层风险是，对手可能会利用这个蓝图来制造表面上看起来和行为都像Claude Code的山寨品，但这些山寨品会在内部植入恶意软件或窃取凭据和数据。”

总结起来就是，这件事让Anthropic尴尬和难堪，但并没有直接危害Claude Code本身的安全。

## 高危权限绕过漏洞详情

然而，Adversa AI红队现在发现了一个真实存在的高危漏洞。根据Adversa的报告，Claude Code是一个超过51.9万行的TypeScript应用，允许开发者直接从命令行与Claude交互。它可以编辑文件、执行shell命令、搜索代码库、管理git工作流和编排复杂的多步骤开发任务。(https://adversa.ai/claude-code-security-bypass-deny-rules-disabled/)

Claude Code的权限系统基于三类规则：

* **allow**规则：自动批准特定命令。
* **deny**规则：硬性阻止特定命令。
* **ask**规则：总是向用户询问。

例如，一个配置规则可能如下所示：

{ “deny”: [“Bash(curl:\*)”, “Bash(wget:\*)”],“allow”: [“Bash(npm:\*)”, “Bash(git:\*)”] }

意思是，永远不允许curl或wget命令（防止数据外泄），但自动允许npm和git命令（这些是常见的开发工具）。

这套方案听起来正确且合理。然而，问题在于，**deny规则可以被绕过**。Adversa报告指出：“这个权限系统是AI助手与开发者系统之间的主要安全边界。当它无声无息地失效时，开发者就失去了安全网。”

问题的根源，要追溯到Anthropic为了提高性能而做的一次调整。此前，复杂的复合命令曾导致UI卡住。为了解决这个问题，Anthropic将分析限制在最多50个子命令。如果超过这个数量，系统就会回退到一个通用的‘ask’提示。代码注释写道：“50这个上限很宽松：合法的用户命令不会拆解得那么细。超过上限时，我们回退到‘ask’（安全默认值 — 我们无法证明安全性，所以进行询问）。”

但Adversa发现的漏洞是，这个过程可以被操纵。Anthropic的假设没有考虑到来自提示注入（prompt injection）的AI生成命令——即恶意的CLAUDE.md文件可以指示AI生成一个看起来像合法构建流程、但实际上包含50多个子命令的管道。

一旦这么做了，系统会立即触发“behavior: ‘ask’ // NOT ‘deny’”。Adversa写道：“deny规则、安全验证器、命令注入检测——所有这些都被跳过了。”第51个命令确实会按预期回退到ask，但**用户完全不会得到任何提示，告知所有deny规则都已被忽略**。

## 攻击影响与风险

Adversa警告说，有动机的攻击者可以将看起来真实的构建步骤嵌入到恶意代码仓库的CLAUDE.md文件中。整个过程看起来常规，但由于子命令数超过50，根本不会对每个子命令进行分析。这可能导致攻击者窃取SSH私钥、AWS凭证、GitHub令牌、npm令牌或环境变量中的机密。

其后果可能是大规模的凭据窃取、供应链攻击、云基础设施入侵以及CI/CD流水线投毒。

Adversa在测试中也发现，Claude的LLM安全层在某些情况下能独立捕获一些明显的恶意命令并拒绝执行。这体现了良好的纵深防御。然而，**权限系统的漏洞独立于LLM层而存在——它是安全策略执行代码中的一个bug。**一个精心构造、看起来像合法构建指令的提示注入，也完全可能绕过LLM层。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/KK6rkaWbMNbNvNRWVlQ1KyqceSk3WZAqKUsEjFj2Mfib1H7RQOOarzKolWvdD1W3PGicFOEABZLLpNoL2u9RdAXg/0?wx_fmt=png)

幻泉之洲

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/KK6rkaWbMNbNvNRWVlQ1KyqceSk3WZAqKUsEjFj2Mfib1H7RQOOarzKolWvdD1W3PGicFOEABZLLpNoL2u9RdAXg/0?wx_fmt=png)

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
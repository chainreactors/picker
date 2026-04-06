---
title: AI生成了海量的代码，安全怎么办？看最近几笔融资代表的方向
url: https://mp.weixin.qq.com/s/GKqqy4eVGZlQ3ItGC1YGSQ
source: Doonsec's feed
date: 2026-04-05
fetch_date: 2026-04-06T04:39:34.488327
---

# AI生成了海量的代码，安全怎么办？看最近几笔融资代表的方向

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ccVb6wGibibCENoyjHXphkcXVzncibBHnIxXfUDnicia82vI2Oo0h7RHJicUsD4iaHhfc9QQuskaFTKyIUY3ibOL14uQwqrCv1DzicGnLCYH7hae3lHA/0?wx_fmt=jpeg)

# AI生成了海量的代码，安全怎么办？看最近几笔融资代表的方向

原创

孙志敏
孙志敏

AI与安全

![]()

在小说阅读器中沉浸阅读

随着AI的发展，尤其是claude code等工具被广泛采用后，大量代码用AI生成，一方面，确实大幅提升了开发效率，另一方面，传统的代码质量，安全性等基础手段，基本都无法使用了，甚至连基本的测试都做不完了。

我们已经进入了一个软件编写速度超过安全保障速度的时代。同时，代码是安全的基础，这又是一个人人皆红队的时代，代码安全显得更加重要。

代码的海量增长，需要新的质量保证手段。但到底如何保证，还在不断探索中。很多公司已经看到了机会，最近在此领域发生的三笔融资案例，可以供我们参考。

01

Depthfirst：模型和Agent同步发展

## 2026年3月31日，Depthfirst宣布完成8000万美元B轮融资，距离它3个月前从Stealth状态浮出水面拿到4000万美元A轮，仅过去不到90天。两轮融资累计金额达到1.2亿美元。

Depthfirst 的使命是构建通用安全智能，以保障全球软件的安全。他们相信，实现这一目标需要优化整个技术栈，从产品到代理和模型，以实现两大核心功能：漏洞检测和验证。

![](https://mmbiz.qpic.cn/mmbiz_png/fRp5p4jMuDQjdXQXUMBDtPtLS0iaiaxVKblUBecgRUn30Lv2liaIUfnwcVib2D28Om4F0LpOd4oiah0psOJlRBHqewA/640)

1)模型

![](https://mmbiz.qpic.cn/mmbiz_png/jLdw7EZFJmIjAic1276gZeyjcsS9UMqa3VkvD2WgU11EyJAoVCSagkO3Kmia89jgusIXDficZIgTTb6ia32cibxVKgQ/640)

他们自己训练了dfs-mini1的模型，该模型基于 gpt-oss-120b，在漏洞发现上性能大幅提升，而成本大幅降低。在考虑所有推广活动的总代币支出后，实现了成本与性能的帕累托最优。在 pass@8 测试中，该模型以比所有已评估的前沿模型低 10-30 倍的总成本脱颖而出，这得益于更短的迭代周期和更低的底层模型单代币定价。

![](https://mmbiz.qpic.cn/mmbiz_png/fRp5p4jMuDQjdXQXUMBDtPtLS0iaiaxVKblUBecgRUn30Lv2liaIUfnwcVib2D28Om4F0LpOd4oiah0psOJlRBHqewA/640)

2)AI Agent

![](https://mmbiz.qpic.cn/mmbiz_png/jLdw7EZFJmIjAic1276gZeyjcsS9UMqa3VkvD2WgU11EyJAoVCSagkO3Kmia89jgusIXDficZIgTTb6ia32cibxVKgQ/640)

Depthfirst的核心产品叫做**General Security Intelligence（通用安全智能）**。这是一个AI原生的安全平台，通过部署自定义AI Agent，分析和理解企业的代码库、基础设施和工作流程，利用深度上下文和机器学习来检测传统工具经常遗漏的细微、复杂漏洞。

它的技术路径和传统SAST工具有本质差别。传统静态扫描靠规则匹配，就像用一张漏洞特征表去逐行对照代码；而depthfirst的Agent能够理解业务逻辑、上下文关联和攻击链路，更接近于一位真正的安全专家在做代码审计。

效果数据相当惊人：在正式推出产品的四个月内，其Agent发现的真实漏洞数量是传统静态分析工具的8倍，同时将误报率降低了85%。同时，Depthfirst平台的修复建议，有80%被开发者直接接受并合并，而自家研发的安全专用模型dfs-mini1，在性能超越前沿通用大模型的同时，运行成本仅为后者的1/10到1/30。

可以这么认为，Depthfirst是一个完整的漏洞处理工具，通过微调模型增强漏洞发现能力，通过Agent理解代码并给出修复建议，这是一个完全聚焦于漏洞的解决方案。

02

Qodo：用AI做代码审查和治理

Qodo（前身为CodiumAI）成立于2022年，创始人Itamar Friedman曾是阿里巴巴以色列AI实验室总监。2026年3月底，Qodo完成7000万美元B轮融资，此前已分别完成1100万美元种子轮和4000万美元A轮。公司的客户名单包括Monday.com、Ford、Intuit、NVIDIA、Walmart、Red Hat等。

Qodo的思路与depthfirst形成了明显区分：它不是专门的"漏洞猎人"，而是定位于**整个软件开发生命周期中的质量层**——从开发者在IDE里敲第一行代码，到PR合并进入主干，全程都有Qodo的Agent在旁。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ccVb6wGibibCHAtQeJibAyu5PZ0hNpubZD6qLuSIYM4eiaHzYBXka6ic4vomS9jlZJJsx3sM57VTsTF4cg00nuSibgjeTibgEpfwpCs5ibsiagrT2lIQ/640?wx_fmt=png&from=appmsg)

Qodo有两个技术组件值得重点关注。

第一个是**Context Engine（上下文引擎）**。Qodo的关注点不只是"这次改了什么"，而是"这次改动如何影响整个系统"——它将组织标准、历史上下文和风险容忍度都纳入考量。这让它能够发现跨文件、跨仓库的隐蔽安全问题，而不是停留在单文件的语法层面检查。

第二个是2026年初推出的**Rules System（规则系统）**。这是一套活的标准管理机制，能够从代码库的历史审查决策中**自动提炼**安全规范，然后将其自动执行到每一次代码变更中，并跟踪规则的采纳率和违规趋势。

在Martian的代码审查基准测试中，Qodo得分64.3%，比第二名高出10分以上，比Claude Code Review高出25分，尤其擅长捕捉复杂逻辑Bug和跨文件问题。

Qodo 构建了一套专门的基础设施，充当高级监管者的角色。该系统确保每一项自动化操作都经过对您代码库和团队实际情况的深入验证。

简单地说，Qodo在用AI的方法，增强传统DevSecOps里的安全审查能力，其技术最大的特点是让AI尽可能多的理解上下文及遵守规则，这是非常强的工程化的观点。

03

Coder：从开发和执行环境层管住AI Agent

如果说depthfirst和Qodo是在"检查代码写得是否安全"，那Coder解决的是一个更底层的问题：**当AI Agent本身在帮你写代码的时候，谁来管住Agent的行为？**

这是Agentic AI时代特有的新型安全挑战。

Coder的判断是：AI工具已经在软件开发生命周期中广泛存在，问题不是"要不要用"，而是"如何管控"。在本地开发中不加管控地使用AI工具会引入安全风险、影子使用和成本失控；而一味封堵AI则会拖慢交付速度。

在开发环境上，Coder的产品体系围绕**自托管控制平面**构建，所有代码和数据在客户自己的基础设施上运行，核心安全机制包含三层：Workspaces（隔离环境）是基础。Agent不在开发者的笔记本上运行，而是运行在由Terraform模板定义的标准化隔离容器中，工作空间销毁后不留任何痕迹，Agent无法接触开发者本地的凭证、SSH Key或其他敏感文件。

在执行环境上，Coder的多层隔离非常好的规范了Agent的行为。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ccVb6wGibibCGCG5N4yUr5O5YcpYT3j5CYqpNg3YxoNWQia43SP9Ix00ruQibTBYvFAPibojvPUWFqKzNHCsCJxnpbv0aWm7hibslFse5ibEWAm0Fs/640?wx_fmt=png&from=appmsg)

隔离层（Isolation）：Coder 的 Mux 工具能在用户的开发环境中运行 AI 编码 agent，允许多个 agent 并行工作，同时为 AI 自动化工作流创建隔离工作区，以降低网络安全风险。

这里的"隔离工作区"是关键词——每个 agent 跑在独立的沙箱里，横向移动（Lateral Movement）的可能性被约束在最小范围。

**访问控制层（Access Control）**：管理员可以限制开发团队的 AI agent 被允许使用哪些 MCP 服务器和工具，还可以定义更细粒度的控制，例如规定 agent 在执行在线研究时可以访问哪些网站。

这实际上是将传统的网络访问控制（ACL）和工具白名单（Tool Allowlisting）机制引入了 AI agent 的运行时管理，精确匹配了 MCP 协议安全中"工具滥用"这一核心威胁向量。

**审计与治理层（Audit & Governance）**：付费版本会生成审计日志，供管理员监控 AI agent 的活动；另有一个管理工具可以对开发相关的推理费用设置上限。

审计日志解决的是可见性（Visibility）问题，是事后追溯和合规的基础；费用上限则是一种资源滥用防护，防止 agent 被操控后大量消耗推理资源。

Coder的思想聚焦于AI Agent在代码开发环境和运行环境里的治理，这是全新的理念，与传统的代码质量管控思路完全不同。

04

小结

代码安全里的一些关键动作，象SAST,DAST等，都是几十年积累下来的，在AI写代码之前的环境里，已经得到广泛认可和应用。

但面对AI生成的海量代码，这些方法已经力不从心。如何往前走，需要非常多的探索，并需要时间来确定答案。

虽然当前有诸多不确定的因素，但从这三笔融资来看，资本已经形成了一个清晰的共同判断：**这个问题，必须用AI来解，而且要比代码生成更专业。**

未来会怎么发展，我们拭目以待。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/rhmRSVBNbicqDIxcZyn1sK1icxG8aZVh9lVqRTa042xtzVBrJs2tcFPYv4HmkmFCDu8mtZJYw4x2vrbBx2mJf2AA/0?wx_fmt=png)

AI与安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/rhmRSVBNbicqDIxcZyn1sK1icxG8aZVh9lVqRTa042xtzVBrJs2tcFPYv4HmkmFCDu8mtZJYw4x2vrbBx2mJf2AA/0?wx_fmt=png)

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
---
title: 北京大学 | ContractTinker：基于大语言模型的真实场景智能合约漏洞修复系统
url: https://mp.weixin.qq.com/s/UOwZCl-WxvefyRv76t9Z6g
source: Doonsec's feed
date: 2026-01-16
fetch_date: 2026-01-17T03:24:36.276833
---

# 北京大学 | ContractTinker：基于大语言模型的真实场景智能合约漏洞修复系统

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6Dibw6L070WG2Nicoh5RleJfFsy495gRPib4oxkRxMkfRKtVXfQvjxJD6kVw4Ky1zDR6j2OgdnbtFyqq8L4Pvb7Nw/0?wx_fmt=jpeg)

# 北京大学 | ContractTinker：基于大语言模型的真实场景智能合约漏洞修复系统

原创

何利军
何利军

安全学术圈

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WG2Nicoh5RleJfFsy495gRPib1Z6D2EaIwEXoMtqVslkXhuXWc5AicMmWHgxngnYdO0vnliaXmibMKsmRA/640?wx_fmt=png&from=appmsg)

> **论文题目：ContractTinker: LLM-Empowered Vulnerability Repair for Real-World Smart Contracts**
> **论文作者：Che Wang，Jiashuo Zhang，Jianbo Gao，Libin Xia，Zhi Guan，Zhong Chen**
> **发表会议：ASE**
> **主题类型：漏洞修复，智能合约，大语言模型**
> **笔记作者：何利军@Web攻击检测与追踪**
> *主编：黄诚@安全学术圈*

# 研究概述

由于智能合约的不可变性及其与区块链金融活动的紧密关联，其极易遭受各类攻击。为防范攻击，现实应用的开发者常依赖 Code4Rena 等第三方安全审计服务，在部署合约前识别安全漏洞。然而，即便有第三方审计报告，漏洞修复仍是复杂且耗时的任务，尤其对不熟悉安全攻击的开发者而言更是如此。因此，自动化程序修复(APR)成为极具研究热度与实用价值的课题，它通过为特定类型漏洞自动生成补丁简化开发者工作。已有若干 APR 工具被提出以协助开发者打补丁，这些工具通常针对重入、整数溢出等具有明确底层特征的漏洞，基于预定义模式生成补丁。之前的研究表明，现实中的漏洞多为与合约业务逻辑紧密相关的高层级功能缺陷。由于缺乏对这些高层语义的理解，现有基于模式的方法难以有效应对现实漏洞。

本文提出了开发了ContractTinker——一款由大语言模型(LLMs)驱动的现实智能合约漏洞修复工具。ContractTinker 利用大语言模型理解智能合约的高层业务逻辑，分别从审计报告和合约代码中提取结构信息与漏洞上下文。

图1给出了ContractTinker整体工作流程。首先，用户输入项目文件和审计报告。随后，ContractTinker 分两步处理：一方面分析项目以提取完整的依赖图，另一方面从报告中提取有效的结构信息。在获取必要要素后，工具进行漏洞定位以过滤无用元素，并构建上下文依赖图(CDG)和程序切片。在补丁生成阶段，我们采用 “思维链”(chain of thought)概念，将任务拆解为多个步骤以逐步推导补丁逻辑。最后，工具使用另一个独立的大语言模型(LLM)评估生成的补丁代码，若未修复漏洞则进行优化。最终输出经过验证的有效补丁。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WG2Nicoh5RleJfFsy495gRPibFQcXnmttTkqWwyh7HDCUH1gzl3j90qlHictJUXmhjYyUuHJoZNPRUcA/640?wx_fmt=png&from=appmsg)

图 1 ContractTinker 工作流程

# 贡献分析

* 贡献点1：论文提出了一款大语言模型赋能的智能合约漏洞修复工具ContractTinker。通过采用思维链（CoT）机制，引导大语言模型将审计报告中的漏洞描述映射到智能合约的语义层面，并生成相应的修复补丁；
* 贡献点2：整合了静态分析技术，帮助大语言模型在复杂的真实智能合约项目中精确定位漏洞，同时提升补丁生成效率；

# 代码分析

代码链接：https://github.com/CheWang09/LLM4SMAPR

该代码使用了subprocess、slither、re、json、openai、transformers、logging、time、os、tqdm、networkx等库，这些库均为开源类库的集成。

**1. 该代码的实现难度较高且工作量较大，主要体现在以下方面：**

* **静态分析深度依赖：**需集成Slither构建依赖图（DG）和程序切片，涉及跨合约调用、继承关系及数据流追踪的复杂处理，需处理AST解析、函数调用图生成及多文件项目解析，对智能合约语义理解的准确性要求高；
* **LLM协同逻辑复杂：**需设计多阶段Chain-of-Thought提示工程（如漏洞攻击分析、策略生成、补丁生成），涉及LLM接口的灵活适配（如GPT-3.5与GPT-4的切换）、生成结果的解析与后处理，需解决模型幻觉与代码逻辑一致性难题；
* **模块协同与数据流管理：**代码包含文档解析、项目分析、上下文准备、补丁生成与验证等多个子系统，需维护跨模块数据结构（如依赖图、代码片段、漏洞上下文）的一致性，错误处理与日志跟踪复杂度高；
* **工程化挑战：**需处理Solidity编译环境配置（solc remaps）、多合约项目解析、大规模代码切片的高效提取，以及LLM生成补丁的自动化验证流程（如编译检查与逻辑验证）。总体工作量预计需3-6个月，涉及静态分析优化、LLM提示迭代、多模块联调及实际漏洞场景适配，尤其在跨合约数据流追踪与幻觉抑制方面需投入大量研发资源。

**2. 代码主要分为五个模块：**

* **文档解析模块（Document Parser）：**专注于审计报告的语义解析与结构化信息抽取。支持灵活扩展，可适配多种审计报告格式（如Markdown/PDF/JSON等），通过自然语言处理技术提取漏洞描述、定位信息及修复建议等关键元数据。
* **补丁生成模块（Patch Generator）：**作为核心模块，主要负责漏洞修复补丁的生成。该模块实现了漏洞定位功能，并构建了覆盖完整生成任务的流程化处理框架。通过整合漏洞上下文信息与程序分析结果，驱动多阶段补丁生成过程。
* **程序分析模块（Program Analyzer）：**实现智能合约项目的全方位静态分析。通过构建跨合约的依赖关系图（Dependency Graph）和数据流图（Data Flow Graph），揭示函数调用关系、状态变量读写依赖等关键语义信息，为LLM驱动的链式推理（Chain-of-Thought）提供结构化程序特征支撑。
* **提示工程工具（Prompt Utils）：**封装多粒度提示模板库，覆盖漏洞分析、修复策略生成、补丁代码合成等子任务。提供模板定制接口，支持根据具体漏洞类型动态组合上下文元素（如代码片段、依赖路径），实现提示内容与目标场景的精准对齐。
* **LLM接口层（LLM Interface）：**提供标准化的语言模型接入框架。通过模块化接口设计支持主流LLM（如GPT系列、Llama等）的灵活切换，允许开发者配置模型参数、优化采样策略，并集成缓存机制和速率限制等工程优化功能。

# 论文点评

论文基于48个高风险的现实漏洞进行实验，尽管结果显示了48%的有效修复率和21%需微调的补丁，但样本规模较小且覆盖的漏洞类型不够全面。智能合约漏洞种类繁多（如重入攻击、逻辑漏洞、权限问题等），而实验未明确说明选取的漏洞类型分布。若实验集中于特定类型的漏洞（如逻辑漏洞），可能导致结论对其他类型漏洞的泛化能力不足。此外，缺乏对复杂业务逻辑场景的针对性测试（如多合约交互、跨链操作）可能低估实际场景中的修复难度。

论文未深入探讨不同LLM模型（如GPT-3.5、GPT-4、CodeT5）的性能差异，也未对比传统修复工具（如SGuard、EVMPatch）在相同数据集上的表现。LLM的“幻觉”问题虽通过Chain-of-Thought（CoT）和静态分析缓解，但未量化其缓解效果。例如，未统计因LLM生成错误逻辑导致的无效补丁比例。此外，论文未讨论LLM对代码上下文长度（如长函数或复杂依赖）的适应能力，可能影响大规模项目的修复效果。

我认为本论文可以优化静态分析与LLM的协同机制增强数据流分析：结合符号执行验证补丁的安全性，避免“以错纠错”；跨合约依赖建模：扩展依赖图（DG）以支持外部库调用和继承关系；动态上下文注入：在CoT过程中动态调整程序切片范围，适应复杂逻辑。

论文在LLM与静态分析结合修复智能合约漏洞的方向上具有创新性，但在实验全面性、技术深度和自动化验证方面存在改进空间。未来工作可通过扩展数据集、优化分析算法、完善验证流程进一步提升工具的实用性和可靠性。此外，探索LLM与形式化方法的深度结合（如生成可验证的补丁约束）可能是突破现有瓶颈的关键路径。

# 论文文献

1. Wang C, Zhang J, Gao J, et al. Contracttinker: Llm-empowered vulnerability repair for real-world smart contracts[C]//Proceedings of the 39th IEEE/ACM International Conference on Automated Software Engineering. 2024: 2350-2353.

> [安全学术圈招募队友-ing](http://mp.weixin.qq.com/s?__biz=MzU5MTM5MTQ2MA==&mid=2247484475&idx=1&sn=2c91c6a161d1c5bc3b424de3bccaaee0&chksm=fe2efbb0c95972a67513c3340c98e20c752ca06d8575838c1af65fc2d6ddebd7f486aa75f6c3&scene=21#wechat_redirect)
> 有兴趣加入学术圈的请联系 **secdr#qq.com**

---

**专题最新征文**

* [期刊征文 | 暗网抑制前沿进展](https://mp.weixin.qq.com/s?__biz=MzU5MTM5MTQ2MA==&mid=2247491610&idx=1&sn=8b6c9caf92435cbd9b76b77686619972&scene=21#wechat_redirect) (中文核心)
* [期刊征文 | 网络攻击分析与研判](https://mp.weixin.qq.com/s?__biz=MzU5MTM5MTQ2MA==&mid=2247491661&idx=1&sn=ab0a97741cdf854757ef3024b03f1d44&scene=21#wechat_redirect) (CCF T2)
* [期刊征文 | 域名安全评估与风险预警](https://mp.weixin.qq.com/s?__biz=MzU5MTM5MTQ2MA==&mid=2247491703&idx=1&sn=7f351031fc81e1b63d5215ddb8dc91b5&scene=21#wechat_redirect) (CCF T2)

---

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/6Dibw6L070WFvZRQiafv3iccicic1dIYUEQ1ZzLh1a10l7tfw7zkWkRbY9kEPBwX2NiadOrwFl9a48as9qiayp3eOgDUQ/0?wx_fmt=png)

安全学术圈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/6Dibw6L070WFvZRQiafv3iccicic1dIYUEQ1ZzLh1a10l7tfw7zkWkRbY9kEPBwX2NiadOrwFl9a48as9qiayp3eOgDUQ/0?wx_fmt=png)

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
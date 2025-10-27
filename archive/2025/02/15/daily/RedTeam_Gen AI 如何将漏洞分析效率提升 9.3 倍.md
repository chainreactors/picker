---
title: Gen AI 如何将漏洞分析效率提升 9.3 倍
url: https://mp.weixin.qq.com/s?__biz=Mzg5NjAxNjc5OQ==&mid=2247484095&idx=1&sn=4291f26d60d708ee44796c81558c2a91&chksm=c006ca4ff771435967a52c3bc89a5f6d4765067a03d5b26f5187e7731299e0c9549df93d839d&scene=58&subscene=0#rd
source: RedTeam
date: 2025-02-15
fetch_date: 2025-10-06T20:39:23.119665
---

# Gen AI 如何将漏洞分析效率提升 9.3 倍

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/6USuqjXjYk77hnmh5sns4icmcIXe4eWIhwus1lIFt9EhMhMZkeYKzOiaiaVxZZQaI7X60gD6AaeN4HdgdMMbmfaDw/0?wx_fmt=jpeg)

# Gen AI 如何将漏洞分析效率提升 9.3 倍

原创

tonghuaroot

RedTeam

## 摘要

NVIDIA 的 Agent Morpheus 通过 Gen AI 与事件驱动型 RAG 框架，将企业级 CVE 分析从人工主导的耗时流程转变为自动化、智能化的高效系统，显著提升漏洞管理效率与准确性。

## 要点总结

1. **传统 CVE 分析的痛点**：人工分析效率低，漏洞修复盲目性高，误报与兼容性问题频发。
2. **Agent Morpheus 的核心技术**：基于 Llama3 模型的动态检查清单生成与AI Agent 工具链，实现全流程自动化。
3. **多源情报融合**：整合漏洞数据库、威胁情报、SBOM 等多源数据，提升分析准确性。
4. **标准化输出与反馈闭环**：自动生成 VEX 文档，并通过人工审核反馈持续优化模型。
5. **性能突破**：NVIDIA NIM 推理微服务与 Morpheus 框架实现 9.3 倍效率提升，满足企业级实时需求。
6. **企业级价值**：端到端自动化流程显著降低安全团队工作量，提升漏洞管理效率。
7. **未来挑战**：需解决模型幻觉抑制与合规性适配问题，确保技术应用的可靠性与合法性。

## 前言

软件开发和部署过程复杂。现代企业应用程序具有复杂的软件依赖关系，形成了一个互联的网络，提供了前所未有的功能，但也带来了成倍增加的复杂性。

随着 CVE 漏洞数据库中报告的安全漏洞数量在 2022 年创下历史新高，修补软件安全问题变得越来越具有挑战性。

截至2023年底，累计报告的漏洞已超过 20 万，传统的漏洞扫描和修补方法显然已变得无法管理。利用 Gen AI，可以降低安全团队负担的同时提高漏洞防御能力。

一些组织已经开始考虑使用 Gen AI 来帮助自动化这一过程。然而，在企业规模上实施这一方法需要收集、理解和综合大量信息。

## AI Agent 和 RAG 为 CVE 分析增加了智能

检测和修复 CVE 的第一个步骤是扫描软件中是否存在已知 CVE 的签名，这一过程不应就此停止。

一个合理的下一步可能是通过生成拉取请求并将软件包版本更新为已修补或修复的版本来修复 CVE。然而，要求在**每次检测到 CVE 时都升级软件包是不现实的，特别是在新的 CVE 通常在软件包升级可用之前就被发现的情况下。**

由于软件依赖关系的复杂性，即使存在非漏洞版本的包，更新到一个无漏洞的版本也不总是可行。调查 CVE 以确定最佳解决路径极为劳动密集。

Gen AI Agent 加速了人工安全分析师进行更广泛研究和调查CVE及扫描到的软件 Container ，以确定是否需要进行升级，从而大幅提高速度。

![image](https://mmbiz.qpic.cn/mmbiz_png/6USuqjXjYk77hnmh5sns4icmcIXe4eWIh7ia4RMFBTNtegRFJpNOzFpBorBSohMkAoqwyiaag6Gquic1u8Bu5P3xCw/640?wx_fmt=png&from=appmsg)

image

在这个 CVE 分析AI工作流示例中，我们正是做到了这一点。我们的 Gen AI 应用称为“Agent Morpheus”，它采取了额外的步骤来判断一个漏洞是否真正存在，生成一个任务清单来全面调查CVE，最重要的是，它确定了漏洞是否可被利用，这是分析的关键部分。

**企业软件并不总是需要更新以修复每个检测到的 CVE 来保持安全，这在许多情况下也不现实。**原因之一可能是修复版本的漏洞包尚未由维护者提供。另一个挑战是现代软件项目的依赖链如此复杂，更新一个包可能导致与其他依赖项的兼容性问题，并且破坏软件。

难道软件必须在每个 CVE 修复之前都不发布吗？显然不是，但发布者应该确保他们的软件中没有高风险的、可能在使用过程中被利用的 CVE。

**区分 Container 是否存在漏洞（CVE存在）和是否可被利用（漏洞能够被执行并滥用）非常重要。**

Container 中的 CVE 可能无法被利用，原因有很多。例如，CVE 扫描结果可能是误报，CVE 签名错误，漏洞库实际上并未出现在 Container 中。

另一些不需要修补的 CVE 则可能更加复杂，例如，漏洞库可能需要特定的运行时依赖项，而这些依赖项并不在其中。例如， Container 中的一个 .jar 文件的 CVE 可能需要 JRE ，但 Container 中没有 JRE。由于没有 JRE，.jar 文件无法执行，因此 CVE 无法被利用。

另一个非可利用 CVE 的例子是，当库中的漏洞代码或功能根本没有被软件使用或访问，或者存在缓解条件。

判断每个 CVE 是否可被利用的方法是独特的，依赖于特定漏洞的实际情况。它需要分析师综合来自各种情报来源的 CVE 信息，并将其应用于 Container 或软件项目。这是一个手动过程，既繁琐又耗时。

## 在没有人工提示的情况下获得额外的上下文、推理和标准的安全理由

Agent Morpheus 采取了不同的方法，它结合了 RAG 和 AI Agent，在事件驱动的工作流中进行数据检索、合成、规划和更高层次的推理。

该工作流连接到多个漏洞数据库和威胁情报源，以及与特定软件项目相关的资产和数据，如源代码、SBOM、文档和通用互联网搜索工具。

该工作流使用四个不同的 Llama3 LLM ，其中三个经过 LoRA 微调，分别用于以下任务：

* 规划，或独特的任务清单生成阶段
* AI Agent 阶段，用于在特定软件项目上下文中执行清单项目
* 总结阶段，结合所有任务
* 将不可利用 CVE 的标准化理由转换为通用的机器可读并可分发的 VEX 格式

由于工作流生成清单，且 AI Agent 独立运行该清单项有效地与自己对话，它可以独立于人工分析师进行，而无需提示。这使得过程更为高效，因为人工分析师只在获得足够的信息以决定下一步时才参与。

漏洞扫描事件通过传递 Container 中检测到的 CVE 列表触发工作流。这些结果与最新的漏洞和威胁情报相结合，为工作流提供有关特定CVE及其当前漏洞的实时信息。

这些信息被添加到 LLM LoRA 微调模型的提示中，该模型专门任务是生成独特的计划或清单，用于判断 CVE 是否可被利用。例如，前述 .jar 文件的清单项目可能包括一个条目：“检查软件项目是否具有执行漏洞 .jar 文件所需的 JRE”。清单项目被传递给 AI Agent，后者检索必要信息并执行任务。

AI Agent 可以访问与软件项目和 Container 相关的多个资产，有效地执行清单项并做出决策。例如，它可以在软件材料清单和项目的源代码中搜索 JRE，并得出结论，环境无法运行 .jar 文件，因此 CVE 不可利用，并且 Container 不需要立即修补。

![image](https://mmbiz.qpic.cn/mmbiz_jpg/6USuqjXjYk77hnmh5sns4icmcIXe4eWIhucPXWGB5JwXlB8meYiavXlSlfJwKlia8AOeVic9ljnpbOLgiazbYUE91rQ/640?wx_fmt=jpeg&from=appmsg)

image

除了数据源，AI Agent 还可以访问一些工具，帮助它克服当前 LLM 的某些局限性。

例如，LLM在执行数学计算时常常表现不佳。这可以通过让 LLM 访问计算器工具来克服。对于我们的工作流，我们发现模型在比较软件包版本号时存在困难，例如 1.9.1 版本早于 1.10 版本。我们构建了一个版本比较工具，代理使用该工具来确定包版本之间的关系。

![image](https://mmbiz.qpic.cn/mmbiz_jpg/6USuqjXjYk77hnmh5sns4icmcIXe4eWIhrHzKibPuT1LUYWNAwZANs66hgXicq5jqOOqUvQvpezJXLDIiaibhiaTblKg/640?wx_fmt=jpeg&from=appmsg)

image

## 通过事件驱动的 RAG 加速软件交付

使用 Agent Morpheus，组织可以将软件漏洞的处理时间从数小时或数天缩短到几秒钟。它可以独立感知、推理和行动，而无需人工分析师的提示或协助。当完成分析后，Agent Morpheus 将汇总结果呈现给人工分析师，后者可以决定最佳的后续行动。

任何人工批准的修补豁免或对 Agent Morpheus 总结的更改都会反馈到LLM微调数据集，以根据人工输出不断改进模型。

![image](https://mmbiz.qpic.cn/mmbiz_png/6USuqjXjYk77hnmh5sns4icmcIXe4eWIh6zACd9kSLb1AChXBX8EF7wZSMwBkLx4qt6jjd2O33ugglPwXQgHKQw/640?wx_fmt=png&from=appmsg)

image

Agent Morpheus 与我们的 Container Registry 和内部安全工具完全集成，能够完全自动化整个过程，从 Container 上传到生成最终的VEX文档。

1. 该过程从 Container 上传事件触发，每当用户向注册表推送新 Container 时，都会发生该事件。
2. Container 上传后，它会立即使用传统的 CV E扫描器（如 Anchore ）进行扫描。扫描结果传递给Agent Morpheus服务。
3. Agent Morpheus 检索列出的 CVE 的必要情报，并准备任何代理工具。
4. 运行 Agent Morpheus 模型和 Agent，生成每个 CVE 的最终总结和分类。
5. 每个 CVE 的最终总结和分类然后发送到安全分析师的 Dashboard 供其审核。分析师将审核原始 Container 扫描报告、改进的总结和来自 Agent Morpheus 的理由，并做出最终的 CVE 推荐。
6. 推荐将发送进行同行评审。必须做出的任何更改将返回给分析师。
7. 在 VEX 文档完成同行评审后，最终文档将发布并与 Container 一起分发。
8. 对总结或分析师豁免的任何更改会被编入新的训练数据集，用于不断重新训练模型，并根据分析师的输出自动改进系统。

Agent Morpheus 使用 NVIDIA NIM 推理微服务来加速部署时间和推理速度。

Agent Morpheus 使用三个 LoRA 定制版本的 Llama3 模型和一个基础 Llama3 模型，所有模型都托管在单个 NIM Container 中，根据需要动态加载 LoRA 适配器。

NIM 还能够处理 LLM 请求的突发情况，这对于工具的运行至关重要。**平均而言，Agent Morpheus 每个 CVE 需要约 41 个 LLM 查询**！由于 Container 扫描每次可能会生成数十个 CVE，因此一个 Container 的待处理LLM请求数可能轻松达到数千个。NIM能够处理这种工作负载，并消除了开发自定义 LLM 服务的需求。

与传统的聊天机器人管道不同，Agent Morpheus的事件驱动工作流不受人工响应时间的限制。相反，经过加速的工作流可以使用传统机器学习管道的并行化和优化技术，完成所有 CVE 或事件的处理。

使用 Morpheus 网络安全框架，我们构建了一个管道，协调大量的 LLM 请求，并使得这些请求能够异步和并行执行。每个 CVE 的清单项及 CVE 本身完全独立，可以并行运行。

当串行运行时，处理包含 20 个 CVE 的 Container 需要 2842.35 秒。使用 Morpheus并行运行时，同一个 Container 的处理时间为304.72秒，速度提升了9.3倍！

Morpheus 通过将管道转换为微服务，简化了与 Container Registry 和安全仪表板服务的集成。通过HttpServerSourceStage，这个源阶段，Agent Morpheus 真正成为了事件驱动，并在每次 Container 上传到注册表时自动触发，使其能够跟上企业软件漏洞管理的极高需求。

以上内容编译自 Nvidia

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/6USuqjXjYk7KoXCtYjrNnB2XprMPwXgFMP2CGxa880Qdfw9zo3A3rl7TTUJF0iaI90KwgZMTem4JVjDSS3XrClw/0?wx_fmt=png)

RedTeam

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/6USuqjXjYk7KoXCtYjrNnB2XprMPwXgFMP2CGxa880Qdfw9zo3A3rl7TTUJF0iaI90KwgZMTem4JVjDSS3XrClw/0?wx_fmt=png)

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
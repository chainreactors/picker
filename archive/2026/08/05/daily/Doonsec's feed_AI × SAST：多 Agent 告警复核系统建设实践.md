---
title: AI × SAST：多 Agent 告警复核系统建设实践
url: https://mp.weixin.qq.com/s/g4mt_Dn6k9B4EM6o4FBtZQ
source: Doonsec's feed
date: 2026-08-05
fetch_date: 2026-08-06T04:58:14.178363
---

# AI × SAST：多 Agent 告警复核系统建设实践

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ogrJiczzwv0Aoh7S7C7nRg8yZkQX3WMUaHZdIDXYA0V7Ev6iavaByY2fWecsMbkUsUIy1okKWF9ibq2ZNByLXXRwcxznILgBT6VQvnVic2K7a0Q/0?wx_fmt=jpeg)

# AI × SAST：多 Agent 告警复核系统建设实践

王壮
王壮

度小满安全应急响应中心

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

SAST（静态应用安全测试）是企业代码安全建设中的基础能力。在实际运营过程中，SAST 会持续产生大量告警，其中的误报需要安全工程师逐条复核。随着告警量增长，复核成本和告警信任度，都会直接影响漏洞运营的效果。

大模型具备较强的代码理解能力，可以用于分析告警对应的数据流、业务逻辑和安全检查。基于这一能力，我们建设了一套多 Agent 协作的 SAST 告警自动复核系统，用于判断漏洞是否有效，并输出可供安全人员核验的代码证据。

目前，系统主要面向 Java 场景进行调优。本文将介绍该系统在上下文构建、Agent 职责划分和证据约束方面的一些实践。![]()![]()![]()![]()![]()![]()![]()![]()![]()![]()![]()![]()![]()

01

![](https://mmbiz.qpic.cn/mmbiz_gif/RZJWmrQJibAv0YVfsexib2whMmxTW9XjMM22NEbShnPBkicorKHtd0c9Uob2eW5z5CsbveRGet1wktl3dkKcDxNAAbR0ibsR9jU5aEU4zc3NY0c/640?from=appmsg)

背景

![](https://mmbiz.qpic.cn/mmbiz_gif/RZJWmrQJibAv0YVfsexib2whMmxTW9XjMM22NEbShnPBkicorKHtd0c9Uob2eW5z5CsbveRGet1wktl3dkKcDxNAAbR0ibsR9jU5aEU4zc3NY0c/640?from=appmsg)

![]()![]()![]()![]()![]()![]()![]()![]()![]()![]()![]()![]()![]()

SAST 误报的处理成本，不仅取决于误报数量，也取决于单条告警的分析难度。安全工程师通常需要沿数据流查看多个方法，确认 Source 是否可控、Sink 是否可触发，以及中间是否存在有效的过滤或校验。对一些链路较长的告警，还需要继续追踪配置、工具方法和跨服务调用。

当误报率较高时，安全工程师的大量时间会消耗在误报确认上，并且在多次收到无效告警后，也容易对后续告警降低重视程度。因此，自动复核的目标不是简单地为告警打上“真”或“假”的标签，而是减少无效告警对运营人力的占用，同时保证真实漏洞不被错误过滤。

02

![](https://mmbiz.qpic.cn/mmbiz_gif/RZJWmrQJibAv0YVfsexib2whMmxTW9XjMM22NEbShnPBkicorKHtd0c9Uob2eW5z5CsbveRGet1wktl3dkKcDxNAAbR0ibsR9jU5aEU4zc3NY0c/640?from=appmsg)

问题与挑战

![](https://mmbiz.qpic.cn/mmbiz_gif/RZJWmrQJibAv0YVfsexib2whMmxTW9XjMM22NEbShnPBkicorKHtd0c9Uob2eW5z5CsbveRGet1wktl3dkKcDxNAAbR0ibsR9jU5aEU4zc3NY0c/640?from=appmsg)

2.1 分析结果需要直接用于安全运营

对安全运营来说，只确认数据能够从 Source 到达 Sink 并不足够。复核结果还需要回答漏洞的实际影响，包括部署环境、服务链路、可利用条件和可能造成的危害。不同漏洞类型的分析方法也不相同，例如：

* 任意文件读取：需要确认攻击者是否可以访问任意路径，以及是否可以实际获取文件内容
* 开源组件漏洞：需要结合组件版本和代码中的危险方法调用进行判断
* 命令执行：需要区分攻击者是否能执行任意命令，还是只能注入部分参数，并进一步分析其影响范围

这些判定不能完全依赖大模型的通用安全知识。不同团队对漏洞有效性和危害程度的定义不同，系统需要把内部安全运营标准纳入分析过程。

2.2 长上下文会影响分析稳定性

Agent 需要获取足够多的代码上下文，才能对漏洞进行判断。这些上下文主要包括两部分：

* 漏洞数据流：用于了解数据如何从 Source 经过业务逻辑，最终到达漏洞触发点
* 每个数据流节点对应的代码上下文，用于检查安全过滤、业务校验和数据类型变化。

如果一次性向模型提供过多代码，不仅会增加 Token 消耗，还会使模型的注意力被无关代码稀释，导致分析约束被忽略，并增加幻觉的概率。如果只提供告警行附近的固定代码窗口，又可能缺少关键方法的实现。因此，如何选择分析所需的代码，是该系统设计中的一个重点。

03

![](https://mmbiz.qpic.cn/mmbiz_gif/RZJWmrQJibAv0YVfsexib2whMmxTW9XjMM22NEbShnPBkicorKHtd0c9Uob2eW5z5CsbveRGet1wktl3dkKcDxNAAbR0ibsR9jU5aEU4zc3NY0c/640?from=appmsg)

系统设计

![](https://mmbiz.qpic.cn/mmbiz_gif/RZJWmrQJibAv0YVfsexib2whMmxTW9XjMM22NEbShnPBkicorKHtd0c9Uob2eW5z5CsbveRGet1wktl3dkKcDxNAAbR0ibsR9jU5aEU4zc3NY0c/640?from=appmsg)

系统将一条 SAST 告警的复核过程拆分为告警解析、上下文构建、数据流验证、代码取证和结论汇总几个环节。复核结果分为误报、真实漏洞和分析失败，同时保留支撑结论的代码证据。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ogrJiczzwv0BSBpKojKcJdGqEsmLu4ob2kEAyiaaLcPhOm1Eiafc4oJ9I4JE68vsa8Jq2GLMEI1S7V0Hg6jFibiadprMRxCGjyneq1YQD1n3jhgY/640?wx_fmt=png&from=appmsg)![]()![]()![]()![]()![]()![]()![]()![]()![]()![]()![]()![]()![]()

3.1 告警解析与上下文构建

输入层负责把 SAST 产出的原始告警转换为后续 Agent 可以直接处理的结构化任务。系统首先从告警中提取两类信息：

* 漏洞类型：用于选择对应的安全分析约束
* 数据流节点序列：包括每个节点的文件和行号

随后，系统通过 AST 定位每个节点所在的完整方法体，并对相同方法的代码上下文进行去重。这部分内容作为固定上下文，随告警一起进入后续分析流程。

3.2 安全分析约束

大模型在训练过程中学习了大量通用安全知识，但不同团队的漏洞运营标准并不完全一致。我们将内部的漏洞有效性标准、安全实现、常见误报模式和分析纪律整理为约束文档，并随告警注入分析流程。

约束分为两类：

* 通用约束：描述安全过滤的识别方法、过滤有效性标准和分析边界
* 漏洞类型约束：针对具体类型给出有效性标准、安全实现和常见误报模式

为减少无关信息对分析的影响，系统根据告警类型渐进式地提供相关约束。

在实际判断中，约束主要覆盖以下三个方面：

| 约束维度 | 核心问题 |
| --- | --- |
| 数据流有效性 | 数据流本身是否错误或断裂，Source 和 Sink 是否有效，污点是否被配置文件、数据库数据等操作影响 |
| 过滤逻辑有效性 | 过滤方法是否能够完全消除风险，是否存在绕过方式 |
| 漏洞有效性 | 漏洞的实际风险情况，以及在当前业务逻辑中是否可以造成实际危害 |

3.3 Verifier Agent：数据流有效性门控

Verifier Agent 位于漏洞判定之前，用于检查数据流在污点传播语义上是否成立。这一步会提前排除数据流分析错误的告警，以及当前暂不关注的漏洞类型。

常见的排除场景包括：

* 污点传播错误，例如污点从obj.a错误流转到obj.b
* 数据类型不可利用，例如数据流中途经过int或boolean类型转换，后续数据已无法承载注入类漏洞的 Payload
* 二次注入场景，例如污点入库后再被查出，或数据流经过 HTTP 请求的响应，后续数据实际来自新的信任边界

Verifier Agent 输出数据流是否有效的判断及精简的分析结论。根据判断结果，流程可以直接结束，也可以继续进入后续的漏洞分析。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ogrJiczzwv0AzdoEhgpjaIgfXs9303xkoCX8IDeQKzlepkobjvic6QvjQr3G9NjTzoQXEiadhnicuBwMFSweBKZx56ENm2zFkwGChkVRmlXn2Qw/640?wx_fmt=png&from=appmsg)![]()![]()![]()![]()![]()![]()![]()![]()![]()![]()![]()![]()![]()

3.4 Dispatcher Agent：任务调度与结论汇总

Dispatcher Agent 是漏洞分析的主流程，也是唯一可以对"是否为真实漏洞"作出最终判定的 Agent。其主要职责包括：

* 评估当前证据是否足以支持漏洞有效性判断
* 确定需要继续分析的数据流节点，以及每个节点需要补充的证据
* 为 Analyze Agent 下发取证任务，并对各个任务的结果进行汇总

Dispatcher Agent 以多轮循环的方式工作。每轮会输出一个结构化决策，再由固化的流程检查是否满足结束条件。

整体过程如下：证据不足 → 下发节点粒度的取证任务 → 并行执行并汇总 → 重新评估证据 → 证据充分后输出最终结论

3.5 Analyze Agent：执行节点粒度的代码取证

Analyze Agent 是 Dispatcher Agent 的执行者。每个 Analyze Agent 实例只处理单个数据流节点上的一个分析任务，不关注整条告警的最终判定。

Analyze Agent 采用 ReAct 方式工作，根据任务需要调用code-cli搜索代码、读取文件，并回答与当前节点相关的具体问题。

为了保证结论可以核验，Analyze Agent 输出的证据必须来自工具返回的原文片段，并附带对应的代码位置。它只输出证据和单节点结论，不参与告警的最终判定。

![](https://mmbiz.qpic.cn/mmbiz_png/ogrJiczzwv0D69iaVXq6LibPNibyq6bRlk3CmAVibRxDV7hYxCAMz7f2RUYNfFLAz5CWWkwkqomkdt8rRyJN06Nq7ib3pv4WmpCL7VXy8j8tPhGxE/640?wx_fmt=png&from=appmsg)![]()![]()![]()![]()![]()![]()![]()![]()![]()![]()![]()![]()![]()

04

![](https://mmbiz.qpic.cn/mmbiz_gif/RZJWmrQJibAv0YVfsexib2whMmxTW9XjMM22NEbShnPBkicorKHtd0c9Uob2eW5z5CsbveRGet1wktl3dkKcDxNAAbR0ibsR9jU5aEU4zc3NY0c/640?from=appmsg)

核心设计

![](https://mmbiz.qpic.cn/mmbiz_gif/RZJWmrQJibAv0YVfsexib2whMmxTW9XjMM22NEbShnPBkicorKHtd0c9Uob2eW5z5CsbveRGet1wktl3dkKcDxNAAbR0ibsR9jU5aEU4zc3NY0c/640?from=appmsg)

4.1 决策与执行分离

在证据不充分时，LLM 容易根据局部信息提前收敛。例如，代码中调用了一个看起来具有安全校验功能的方法，模型可能在未查看方法实现的情况下，直接判断漏洞无效。即使在 Prompt 中要求"证据不足时必须派发取证任务"，在长上下文中这类约束仍然可能被忽略。

为此，我们将决策和取证分开：Dispatcher Agent：负责按照分析约束评估证据并作出决策，但不允许调用代码分析工具Analyze Agent：可以调用工具，但只负责执行单节点取证任务，不对告警作出最终结论。

除了职责隔离，系统还通过工程约束检查分析结果。Analyze Agent 的结论必须具有对应的工具调用记录和代码位置，缺少证据的结论不会被 Dispatcher Agent 采用。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ogrJiczzwv0AfwpF1viagAZA2QA25MwIEcfJXl7vOHckDUeXbXUXKAJjyGHmUBPuOCdkLmo76t3JcGic1xticslia0IocLqQZE7NVoic61JCY97fk/640?wx_fmt=png&from=appmsg)![]()![]()![]()![]()![]()![]()![]()![]()![]()![]()![]()![]()![]()

4.2 代码上下文惰性加载

给 LLM 的代码上下文面临两难：给太多代码会导致注意力被无关代码稀释、约束遵守性下降、幻觉概率上升；只给告警行附近的窗口，又经常会缺失关键信息。

系统参考安全工程师的实际分析过程，将代码上下文分为固定上下文和动态上下文。

* `固定上下文：包括漏洞原始数据流，以及数据流节点对应的方法上下文。它反映当前告警的基本数据流情况，所有分析都以此为基础。`
* `动态上下文：由 Analyze Agent 根据当前取证任务按需获取，例如查看过滤方法的实现、追踪某个对象的来源或确认配置项的取值。`

这种方式避免了一次性引入大量与当前问题无关的代码，同时也不受限于固定行数的代码窗口。

4.3 拆分 Agent 职责

从功能上看，Verifier Agent 的数据流验证也可以合并到 Dispatcher Agent 中。两者分析的是同一条数据流，如果由 Dispatcher Agent 顺带完成验证，可以减少一次 Agent 调用从而节省时间和 token。早期版本曾经采用过接近这种方式的设计，但实际测试结果并不理想。

原因是两类分析的目标不同："数据流是否成立"：主要关注污点传播语义；"是否为真实漏洞"：主要关注防护逻辑、可利用性和危害取证将两套分析约束同时放入一个 Agent，会增加上下文规模，也更容易出现注意力偏移。

因此，系统对每个组件的职责和信息边界进行了限制：

* Verifier Agent 不负责漏洞有效性判定
* Dispatcher Agent 不直接查看数据流之外的代码
* Analyze Agent 不获取完整数据流信息
* code-cli 也不需要感知当前正在分析一个安全漏洞

通过这种拆分，可以减少单个 Agent 需要同时处理的约束和上下文数量。![]()![]()![]()![]()![]()![]()![]()![]()![]()![]()![]()![]()

05

![](https://mmbiz.qpic.cn/mmbiz_gif/RZJWmrQJibAv0YVfsexib2whMmxTW9XjMM22NEbShnPBkicorKHtd0c9Uob2eW5z5CsbveRGet1wktl3dkKcDxNAAbR0ibsR9jU5aEU4zc3NY0c/640?from=appmsg)

评测结果与后续规划

![](https://mmbiz.qpic.cn/mmbiz_gif/RZJWmrQJibAv0YVfsexib2whMmxTW9XjMM22NEbShnPBkicorKHtd0c9Uob2eW5z5CsbveRGet1wktl3dkKcDxNAAbR0ibsR9jU5aEU4zc3NY0c/640?from=appmsg)

根据公司内部 500+ 条漏洞评测集的测试结果，按照当前的评测口径：

* ✅ 系统整体准确率约为 90%+
* ✅ SSRF 准确率约为 95%
* ✅ SQL 注入准确率约为 90%

目前评测和调优主要集中在 Java 场景，这些结果还不能代表其他语言和所有漏洞类型。

后续的优化工作主要包括：

* 提高超长数据流场景下的分析稳定性
* 继续细化部分漏洞类型的分析约束
* 进一步优化上下文空间
* 扩展多语言场景的覆盖能力
* 推进评测集自动化接入和 Bad Case 自动分析

从当前的实践结果看，在代码安全分析场景中，单纯增加 Prompt 约束并不能解决所有稳定性问题。将任务按分析目标进行拆分，并通过流程和工程校验约束 Agent 的行为，是这套系统能够稳定输出结果的关键。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ogrJiczzwv0BTAfgJUIibTIfhXB0dZMkdEXmTLohR6Hf50pty8l0T8icD3TpDymTiab5Q0bdt2rj6b28nl4lFB3EzkjcOjFbkIaLdQSZcjk3KZ4/640?wx_fmt=png&from=appmsg)![]()![]()![]()![]()![]()![]()![]()![]()![]()![]()![]()![]()![]()

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/VXdOaCBgqbARRTNiaHF1fsic81KYZT01mlH0BC2Gn4IEGS2v9qb0uA7h17LaQ2EuUE2lup1BRmPHSuC9v6u0ThRg/0?wx_fmt=png)

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
---
title: Cloudflare 如何搭建 AI 漏洞发现流水线
url: https://mp.weixin.qq.com/s/9Brj5DXFKOcOfWmFajbwdg
source: Doonsec's feed
date: 2026-06-22
fetch_date: 2026-06-23T06:03:12.783435
---

# Cloudflare 如何搭建 AI 漏洞发现流水线

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/bJmDO3bwicPVicIBHTYJvlTJ0Oib2OMF6s5qqb9Y4rywG8zqXCkia0w1qAFvaJd7MaNv8HeTZr42h5JL4MQnqVibOgTHlfdp6t0iadkgjUv02ibdics/0?wx_fmt=jpeg)

# Cloudflare 如何搭建 AI 漏洞发现流水线

Cloudflare Blog
Cloudflare Blog

不吃猹的瓜

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bJmDO3bwicPVjtkDLFHG0hoGHTuNAyTbibyj6XH36QJVyP7ReXGJRWlp47VhpLFYRjXUYeHYibcq5Hub04pNRWnQR4gfOLdVUJLMibXbKRkpGSU/640?wx_fmt=png&from=appmsg)

几周前，我们发布了 Project Glasswing 的初步发现，观察当你把 frontier security models 指向企业代码库时会发生什么。我们也探讨了我们的防御结构如何适应变化，以保护基础设施和客户免受 frontier AI 带来的威胁。从那以后，AI 生态仍在快速变化。那些围绕单一模型紧密构建系统的开发者，已经体验过当这个模型不再可用，或被更强模型取代时会发生什么。这些市场变化只会进一步强化我们的核心判断：无论某一天领先的是哪个底层模型，agentic workflows 的未来都不在独立模型、prompt 或单 agent session 里。

要从一个局部的安全 “skill” 走向持续的、fleet-wide 扫描 pipeline，需要一种把模型当作可替换组件的架构。依赖单一模型天然会限制防御覆盖面，因为同一个系统会倾向于用完全相同的视角看代码路径。为了抵消这一点，模型应该被频繁替换并交叉测试。通过在 pipeline 中使用不同模型，例如用一个模型做初始发现，再用完全不同的模型做验证，我们可以确保漏洞由不同的逻辑集合交叉检查。此外，真正的企业级 harness 不能只看孤立仓库，还必须沿着跨仓库依赖追踪漏洞，最终把成千上万的原始候选过滤成可信、已 triage、可执行修复的队列。

这篇文章会从实践角度介绍如何构建这种 model-agnostic 层，重点讲我们如何管理状态控制、消除误报，并在规模化场景下协调端到端 triage。

## 先回应两个质疑

上一篇文章解释了为什么通用 coding agents 无法胜任这项工作。主要问题在于，agent 一次只能持有一个假设，在覆盖真实 repo 的一小部分后上下文窗口就会塞满，然后又会在 context compaction 过程中丢失信息。更多细节可以阅读那篇文章。

在继续之前，我们想先回答两个可能出现的问题。

**“为什么不用 subagents，而要用 harness？”** Subagents 很有用，也是一个不错的起点。但安全分析需要数百个独立 investigation，它们要能跨 run 存活，不能共享同一个上下文窗口，还要能在之后重新界定范围并互相引用。它需要 persistence、deduplication、resumability，最终还需要 fleet-wide dependency tracing。这是一个 orchestration 问题，单靠 prompt 到不了那里。

**“这篇博客只是 frontier models 的广告吗？”** 不是。我们的方法以 harness 为中心，而不是以模型为中心。在漏洞发现上，我们会使用当前最适合需求的 frontier model。把不同模型指向同一个目标时，它们各自会找出不同部分的 bug。真正持久的是 harness 这一层。如果你要构建自己的系统，就从第一天起把它设计成 model-agnostic。这样你才能不受限制地自由选择任何模型。

## 一切都从一个 skill 开始

我们一开始写了一个约 450 行的 `security-audit` skill，在单个 repository 上运行，并不断调整 prompts，直到它能暴露真实 bug。后来，我们加入了 orchestration，让它成为整个系统的 plumbing。真正的价值在 prompts 本身，而我们的 prompts 至今仍几乎原封不动地保留着初始 skill 中的攻击者场景、bug 类别和 anti-pattern 检测。

这个 skill 被设计成在一个 session 中运行 7 阶段 audit：

* 三个并行 research agents 做 recon，并写出 `architecture.md`。
* 每个攻击类别运行一个 **Hunter** agent，尝试破坏代码，而不是审查代码。
* 对抗式 validators 尝试推翻每个 finding。
* 存活下来的 finding 会被写成面向人的 vulnerability report。
* 它们也会按 schema 输出为 `findings.json`，然后由机械检查验证该文件。
* 最后，一个全新的 agent 会独立地针对源码重新验证每个 finding。
* 存活并重新验证过的 findings 会提交到 ingest API。

第一个 skill 几乎可以直接映射到后来的 harness：

| **Skill phase** | **Harness stage** |
| --- | --- |
| Recon agents write `architecture.md` | Recon |
| Hunters run per attack class | Hunt |
| Validators disprove findings | Validate |
| Surviving findings become a report | Report |
| `findings.json` is checked mechanically for schema adherence, not correctness | Mechanical validation of line numbers and functions in findings |
| Fresh agent re-verifies findings | Independent validation |

这个 skill 能工作，但很快暴露出自己的限制。从覆盖指标看，单次运行只能找到多次运行中大约一半的 bug。根据我们的经验，它找到的 bug 也更偏向简单、不太隐蔽的那类。一旦你的流程基本变成“跑十次，然后手工 diff”，你大概就该开始考虑真正的 harness 了。

在运行和微调 skill 的过程中，我们撞上了三堵墙：

* **Context exhaustion**：一个小时后，上下文窗口被填满，模型会吞噬自己的记忆，立刻忘掉它花了一上午追踪的 bug。我们通过完全外部化状态打破这个瓶颈，把 LLM 当成无状态计算引擎。
* **Persistence**：中途崩溃意味着从头再来。因为一次 AI rate-limit error 或连接抖动而丢掉数小时工作，是一种极其昂贵的架构教训。
* **Cross-repo reasoning**：单仓库 session 完全看不到消费它的应用之间的关系。而当你检查组件之间的接口时，浮现出来的 bug 数量可能比想象中更多。

**建议：** 一个真实但最小的 harness，只需要把 Recon、Hunt 和 Validate 阶段保存在数据库中，并配一个不能提交自己 findings 的独立 **Validator**。在你还没有多个重要 repository 之前，完全跳过 cross-repo tracing。在你真正被噪声淹没之前，不要上专门的 Deduplication agent。先在开发环境里从一个 skill 开始，把 prompts 调好；只有当缺少下一个架构阶段成为明确瓶颈时，再去构建它。

## 把 skill 编码成 pipeline

这个领域里大多数 AI security write-ups 讲的是单个 repo 或一个 curated benchmark；用这种方式跑完整 fleet，并且做 cross-repo tracing，据我们所见还没有太多公开写法。我们的代码库横跨大量语言，包括 Rust、Go、C、Lua、TypeScript 和 Python，还有各种配置管理系统、静态配置和许多额外上下文。因此，我们必须提出一套适合自己的新方法。从第一次 slash-command run，到能覆盖 128 个不同 repos、自动查找并追问相关依赖的 fleet scanner，大约花了六周。编码化过程大多是机械性的：我们把 skill 的每个 phase 提升成独立 agent，在后面放一个数据库，在前面放一个 orchestrator。映射关系几乎一一对应。

整个 fleet 运行在一个统一 harness 上，不做按语言调优，并追踪 repos 之间的依赖。把语法处理交给模型，使系统具备语言无关性；但真正的差异点在于它能追踪 repo *之间*的依赖。Harness 本身不关心自己看的是 C 指针还是 TypeScript 文件；它关注的是安全 orchestration 的高层逻辑。这让我们能在数百个不同代码库上扩展，而无需编写自定义语言解析。

## 一个两阶段漏洞研究 workflow

我们的整个漏洞研究 workflow 建立在一个两阶段 operational framework 上：**Vulnerability Discovery Harness (VDH)** 和 \*\*Vulnerability Validation System (VVS)\*\*。

VDH 作为我们的发现引擎，主动扫描代码库以暴露潜在安全问题。一旦 bug 进入 VVS（它允许多个 harness 向其中输入），它们就会经过 Deduplication、Judgment，最后进入 Fixing 阶段，后面会展开说明。

我们在 VDH 中使用一个模型，但在 VVS 中使用完全不同的模型，因此两个模型实际上是在互相复核。这有明显的安全收益：强制 Model B（VVS）判断 Model A（VDH）的输出，可以确保 finding 由一组完全不同的逻辑权重和训练数据评估；它像一个无偏、对抗式第三方，唯一职责就是无情地压力测试 Model A 的假设。从运营角度看，我们也受益于把模型供应商视作可替换商品。模型供应商可能随着时间调整 temperature、caching 和 inference effort budgets，甚至在同一个模型版本内也会变化。与其构建一个依赖模型长期表现可预测的系统，不如让 harness 能吸收下游波动而不崩。

## Stage 1: Vulnerability Discovery Harness (VDH)

上一篇文章讲过每个 agent/stage 的用途，所以这里讲它没覆盖的部分：stage 之间的 glue，以及决定系统能否工作的一些细节。

| **Agent/stage** | **Primary Role** | **Sub-agents / Tooling** |
| --- | --- | --- |
| **Recon** | 梳理目标架构并映射潜在威胁向量 | 3 个并行 Recon sub-agents 写出 `architecture.md` |
| **Hunt** | 按类别发起攻击、编译片段、探测 binaries | 它会派生 siblings（取决于模型，这些 siblings 处理 fleet-wide 任务的 9% 到 20%）。它会访问并写入 Wishlist tool。 |
| **Validate** | 先机械检查 finding，再以对抗方式推翻它 | 分两 pass 运行：plain code 处理初始 schema/path 检查，然后一个隔离 agent 尝试在 finding 被提交前推翻它。 |
| **Gapfill** | 为覆盖不足的 cell 生成新的 hunt tasks | 对任何仍显薄弱的（area × attack-class）cell 入队新的 hunt tasks |
| **Dedup** | 识别并合并重叠 findings | 组合 deterministic code 和 agents，按 root cause 对 findings 聚类，并实时折叠到一起 |
| **Trace** | 遍历 dependency graph；生成 consumer-repo tasks | 遍历 graph，在每个识别出的 consumer repo 内添加 hunt tasks，确保能捕获 cross-repo bugs |
| **Feedback** | 从已有 reports 中学习并优化后续 runs | 接收 validation failures、shallow runs 和反复漏报，并立即重写队列中的 prompts，让后续 tasks 更聚焦。 |
| **Report** | 渲染 human-readable report | 只是一个脚本，不需要模型 |

*Table 1: Vulnerability Discovery Harness (VDH)*

第四到第八阶段会作为连续的 producer-consumer loop 运行。随着初始 hunt 推进，**Gapfill, Feedback** 和 **Trace agents** 会生成新 tasks；**Dedup** 会把重叠 findings 折回到一起，loop 的其余部分则继续消费队列。这确保了即使某个漏洞在周期很晚才被发现，也仍会在同一次 run 内被验证、报告，并与其他代码比对，确认是否包含相同 bug。

这样拆分 pipeline 可以保证严格的上下文控制。如果填满上下文窗口，模型就会开始幻觉。我们让每个 agent 的工作极度聚焦，把上下文使用量控制在总窗口的 25% 以下。天真的“*read all files*”方法每次都会冲破这个限制。

有一件事让我们吃了亏：必须先考虑 persistence，再考虑 parallelism。你不会想因为一个意外错误就扔掉五小时的 run。每个 stage 都写入同一个 SQLite 数据库，并以（`run_id`, `repo`, `stage`）作为 key。任何 stage 都可以 resume、retry，或被拉进后续 run，而无需重做工作。Findings 会在产生时流式保存，所以一次 crash 只会损失正在执行的 task，其他都不会丢。

**建议：** 有时候 transient API error 会以文本形式出现在（`200 OK`）response stream 中，而不是抛出 code exception。对 orchestrator 来说，这看起来完全像是一个干净完成的 task。你必须显式分类响应文本，而不能只相信 exception type，否则最终会把空 run 记成成功。

### Dynamic threat modeling

在 **Recon** 阶段，agent 会自己写 threat model，而不是拿到一份现成的 threat model。除了大约十个内置 attack classes（多种 injection、memory corruption、protocol parsing、timing side channels 等）之外，**Recon** agent 可以现场发明 repo-specific classes，每个 class 都带有自己的 methodology。它会写出一个专门为该代码库定制的 taxonomy，用来更精确地界定 **Hunter** agents 的范围。

只读源码不足以理解代码在压力下的行为，尤其是 C 和其他低层语言中的微妙 undefined-behavior bugs。**Hunter** agents 会越过代码阅读，进入主动执行。它们编译片段、构建小版本并攻击它们。质量上最大的跃升，来自给 **Hunters** 一个 sandbox（基于 `unshare` 构建）来 crash binaries。

**建议：** 如果 harness 本身跑在 Docker 里，这个 sandbox 需要 `seccomp=unconfined` 和 `apparmor=unconfined`，否则它会静默启动失败。这是一个一行修复，但如果你和我们一样不是 nested containerization 专家，它能帮你省下一天抓头发的时间。

### Micro-forks 和 wishlist

除了核心 pipeline stages，我们还加入了两个专门机制，让 **Hunters** 具备更强自主性：它们可以调整关注点、请求外部资源，而不会打断正在进行的分析。

**Sibling Forking**：如果 **Hunter** agent 碰到一条有意思但超出当前范围的代码路径，这个机制能防止它跑偏。它使用 tool call 派生一个带有精确结构化 seed 的 sibling agent。从整个 fleet 看，这大约占任务的 9%，不过比例高度依赖模型：根据负责 hunting 的模型不同，从接近 0 到约五分之一不等。

**The Wishlist**：当 agent 需要一个自己没有的工具时，通常是 **Validator** 想确认 Proof of Concept (PoC)，或 **Hunter** 想构建某些东西（比如特定 build environment、VM 或一些 prod config files），它会写入一个中心 wishlist。它提供足够上下文，让系统在人工提供依赖后能自动重新运行完全相同的 task。其中有些可以部分自愈：如果 container 需要带着某些改动重建，可以让一个 generic coding harness 监控日志，并在 run 之后自主完成。

自 wishlist 加入以来，它已经在 128 个 repos 中被写入 25,472 次，是 agents 与我们反馈沟通的主要方式。我们写这篇文章时刚收到的一条是：“\*I need a FreeBSD VM to confirm this PoC end-to-end.\*”

### Fleet-wide cro...
---
title: Harness 工程实战第3篇：上下文工程与记忆
url: https://mp.weixin.qq.com/s/w2uauQ_apgVwBg_yv-xuLw
source: Doonsec's feed
date: 2026-07-07
fetch_date: 2026-07-08T05:00:07.336759
---

# Harness 工程实战第3篇：上下文工程与记忆

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/4yRoMuNP850fCykwlZIY2KctqXb9qzzf21CyZCmd3zNibgXZzkzcIrLriaqniaBpFHWnbspaEc402hJuaIC6xpOsezAIsBnuhib4wgJ6NoNETh8/0?wx_fmt=jpeg)

# Harness 工程实战第3篇：上下文工程与记忆

原创

Max Luo
Max Luo

白帽子罗棋琛

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

长跑任务为什么必然失败？根因通常不在模型能力，而在 context 管理。Prompt 是可复用资产：一次设计，可以被反复调用，cache 成本近乎可以忽略。Context 则完全不同：它是每个任务独有的运行时状态，越跑越长、越跑越贵，还会被工具输出、历史推理和错误假设持续污染。

当任务跑得足够久，Agent 不是突然开始 hallucination，而是逐步陷入三重故障：关键事实被挤出窗口，目标在多轮推理中漂移，最后用残缺上下文合理化自己的下一步。

本篇按“症状 → 分类 → 路线 → 杀手 → 预告”五步展开。先用一段示意性的漂移 trace 展示失忆、漂移、合理化如何叠加；再借 Lilian Weng 的记忆分类（Semantic / Episodic / Procedural）和 Cognition AI *Don't Build Multi-Agents* 的 “share context” 原则建立分类基础；接着区分 RAG-as-Memory 和 Context-as-Memory 两条主流路线；然后给出三个杀手的工程定义和因果链；

行业里真正把 context 当成一等公民讨论的，是 Anthropic 在 *Building Effective Agents* 里的 Context Engineering 论点，以及 Cognition AI 2025 年 *Don't Build Multi-Agents* 提出的 “share context, share full traces” 原则。学术侧，Lilian Weng 在 *LLM Powered Autonomous Agents* 中把记忆拆成 short-term / long-term，MemGPT 用操作系统类比解释分层记忆管理，Liu 等人在 *Lost in the Middle* 中提供了 context 中段注意力衰减的实证。

本篇把这些工业和学术结论压缩成 Harness 工程里的三种“杀手”：失忆、漂移、合理化，并展开它们在 CyberClaw 实际 trace 里的痕迹。

## 1. 一段示意性的"漂移"trace

一段简化过的 Agent trace，任务是"修复 issue #42 的失败测试"：

```
1. [T+00:00]用户输入：修 issue #42。
2. [T+00:02]Agent：好的，我先看一下 CI 日志。
3. [T+00:03] tool: read_file(".github/workflows/ci.yml")
4. [T+00:05]Agent：找到了，是 cargo test 在module foo 失败。
5. [T+00:08] tool: read_file("src/foo.rs")
6. [T+00:12]Agent：我注意到第47行有一处 unwrap()，可能是空指针。
7. [T+00:14] tool: edit_file("src/foo.rs", line=47, replace="unwrap()",with="?")
8. [T+00:18] tool: run("cargo test --package foo")
9. [T+00:25] tool output:仍然失败，第47行已修但第89行报新错。
10. ...
11. [T+00:47] tool: run("cargo test --package foo")# 第 14 次重试
12. [T+00:48]Agent：让我重新检查 unwrap()的位置。
13. [T+00:50] tool: read_file("src/foo.rs")
14. ...
15. [T+01:23]Agent：根据之前的分析，问题应该在 lifetime 上...
16. [T+01:24] tool: read_file("src/foo.rs")# 第 8 次读同一文件
17. ...
18. [T+02:11]Agent：我已经定位并修复了这个 bug。
19. [T+02:12] tool: git_commit("修复 issue #42")
20. [T+02:13] tool output: nothing to commit, working tree clean
21. [T+02:14]Agent：commit 成功，issue 已修复。
```

最后一段最致命：Agent 说"已修复"，但 `git status` 已经告诉它没东西可提交。它没看见这条 tool output，因为它的 context 早就装不下整个 2 小时的对话了。

这不是 hallucination 这么轻巧的问题。这是长跑任务的结构性病灶：context 是有状态的、可累积的、可污染的。跑得越久，毛病越多。

第 5 节会把这种病拆成三个具体的"杀手"。先看行业怎么给"记忆"这件事立分类。

---

## 2. Lilian Weng 的记忆分类：借用认知科学

![](https://mmbiz.qpic.cn/mmbiz_png/4yRoMuNP853oiajRZ32rthJaFAnCkGPjP0Gelq3nMxtsfqdmiadwQBDSAXjZ1z6Q0l1TWHob2kdTsk7ZZia9yqZ5efwsibfxqbK2E4H8YpD3kYI/640?wx_fmt=png&from=appmsg)

来源：Lilian Weng（前 OpenAI Head of Applied Research）在 2023 年 6 月发了一篇博客 *LLM Powered Autonomous Agents*。这篇文章后来被反复引用、被写进无数综述，核心贡献之一是把认知科学的记忆分类直接搬到 Agent 工程上。

她画的分类树（简化版）：

```
1. Memory
2. ├──SensoryMemory原始输入的瞬时缓冲（LLM 里≈输入 token / embedding）
3. ├──Short-term Memory工作记忆/当前 context window
4. └──Long-term Memory
5. ├──Declarative(显性)
6. │├──SemanticMemory事实性知识（"Rust E0521 是 lifetime 错误"）
7. │└──EpisodicMemory经历性事件（"昨天部署 X 服务失败因为迁移阻塞"）
8. └──ProceduralMemory怎么做的规则（"修 bug 的标准流程：复现 → 隔离 → 修 → 验证"）
```

每一类对应不同的存储与检索范式：

| 类型 | 存储位置 | 典型检索 | Agent 用例 |
| --- | --- | --- | --- |
| Short-term | Context window | 直接读 | 当前对话上下文 |
| Semantic | 向量库 / 知识图谱 | 语义相似度 | "Rust 的 borrow checker 怎么用" |
| Episodic | 时序数据库 + 因果索引 | 按时间 + 按结论 | "上次部署 X 失败的原因" |
| Procedural | 文件化规则 / 结构化模板 | 模式匹配 | "修 bug 标准流程" |

最容易忽略的是 Episodic 和 Procedural：

* 大部分团队把"长期记忆"做成 RAG 语义检索（覆盖 Semantic），但 Agent 真正需要的"上次为什么失败"是 Episodic
* "修 bug 的流程"不该靠 LLM 每次重新推理，应该靠 Procedural memory 直接读出固定步骤，但很少有团队把这一类做成显式存储

第 17 篇会展开 CyberClaw 的 `cyberclaw-memory-extraction` crate，它把 trace 反向蒸馏成 `MemCell` / `Episode` / `AtomicFact` / `Foresight` 四种结构化原子，显式覆盖 Episodic 和 Procedural。这是本系列后续会反复提到的 Cold-Path Extraction。

---

## 3. Cognition 的反多 Agent 论：context 灾难

2025 年 Cognition AI（做 Devin 那家）发了一篇博客 *Don't Build Multi-Agents*。这篇文章在 X / HN 上引发激烈讨论，核心论点是行业反共识的：

> 大多数情况下，单线程线性 Agent 优于多 Agent。

理由不在"多 Agent 难调"这种工程口水，而在信息论层面：context 是稀缺资源，多 Agent 是 context 灾难。

### 3.1 为什么 context 比 prompt 稀缺

开篇已经点过这个不对称：prompt 一次设计、百万次复用，context 每次任务独有、复用率为零。稀缺之外还有一个陷阱：LLM 平均能"有效消化"的 context 远小于宣传的 200k，公开 long-context 评测（RULER / NIAH 等）显示多数模型在窗口中段表现明显低于首尾，模型对中段内容的注意力下降（俗称 "lost in the middle"）。所以 context 不仅贵，还经常半浪费。

### 3.2 Cognition 的两条核心原则

> 1. Share context — 所有 actor 看同一份完整 trace
> 2. Share full traces, not just decisions — 共享的不是结论而是推理过程

第一条对应"不要 manager pattern"：manager Agent 把决策结论传给 child Agent，但没传完整推理过程，child 在自己的 context 里独立推理，可能得出和 manager 矛盾的子结论。

第二条对应"不要分裂 trace"：哪怕真的要拆任务，也要让每个 Agent 看到完整的之前的推理，不只是 "your task is X" 这种压缩指令。

### 3.3 反 Manager Pattern 的工程含义

OpenAI 在 *Practical Guide* 里把 manager pattern 当成"多 Agent 编排"的主流模式。Cognition 直接反对：

> Manager pattern 的本质是用 token 节省去换取错误率上升。

省 token：manager 只传"指令"给 child，不传完整 context。 增错误：child 用残缺的 context 推理，决策大概率和 manager 不一致。

### 3.4 Steelman：什么时候多 Agent 真的赢

Cognition 的论点不是"永远不要多 Agent"，而是"默认选单线程，多 Agent 是例外"。三种场景下多 Agent 真的有优势，一是任务可完全独立分割（如并行翻译 10 段文本，子任务无相互依赖、context 可独立）；二是子任务需要不同 modality（如代码 + 图像，不同模型擅长不同输入）；三是 token 预算允许 redundancy（如投票多次取一致，用多倍 token 换可靠性）。三条都满足"context 无需共享"，这是多 Agent 不退化为灾难的前提。

常见误用（看起来合理但错的）：

* "我把任务拆给 5 个 Agent 看起来更整洁"，是审美决策不是工程决策
* "manager Agent 协调 5 个 worker"，大概率退化成 context 灾难
* "每个子任务独立 LLM 调用更可调试"，实际更难调试，问题出在跨 Agent 的 context 不一致

第 11 篇会展开 CyberClaw 三种 multi-agent 形态对比，它们各自适合的"真正赢"场景，以及 SubAgentOrchestrator 为什么有"深度 3 / 子数 5 / 预算 0.5"的硬上限。

---

## 4. RAG-as-Memory vs Context-as-Memory：两条路线

长期记忆有两条主流工程路线，常常被混在一起讨论但本质不同。RAG-as-memory 是无状态的，把检索结果拼进当前任务的 context，每次任务都独立检索一次。Context-as-memory 是有状态的，用 trace + summarization 攒一份持续记忆跨任务复用。

判别哪条路：问"Rust 的 borrow checker 怎么用？"是事实查询，走 RAG（Semantic memory）。问"我们上次部署失败的原因是什么？"是经验复用，走 Context-as-memory（Episodic memory）。问"修 bug 的标准流程是什么？"两条都不行，需要的是 Procedural memory，靠结构化规则而非检索。问"刚才用户说的'那个 bug'指的是？"是当前会话状态，也是 Context-as-memory。

最容易栽的坑：把 RAG 当万能记忆。

RAG 能很好地解决"事实查询"，但不能解决经验复用。"上次部署失败的原因"如果靠语义相似度检索，会拉到一堆"看起来相关但其实无关"的事故报告。Episodic memory 需要的是按因果关系检索而不是按文本相似度。

第 17 篇会展开为什么 CyberClaw 把 Episodic memory 和 RAG 完全分开，前者是 Cold-Path Extraction 的产物（结构化 `Episode`），后者通过 `Connector` 接入（不直接挂 Memory Core）。

---

## 5. 三个杀手

![](https://mmbiz.qpic.cn/mmbiz_png/4yRoMuNP8539deLlNTuFHx16icry5ic6FO0Cd4MTic4fxx4iaibgQS6I4Ggn6PNFHbK1YkhxukWicq4MZn8gSRSwibJ4FkMvKUMPwnQfQU8y6iccIGI/640?wx_fmt=png&from=appmsg)

第 1 节的"漂移 trace"展示的不是一个 bug，是三个杀手的合谋。三者互为因果：失忆让关键事实丢出 context → Agent 在残缺信息上漂移目标 → 漂移之后用剩下的上下文合理化下一步 → 合理化又把更多无关内容塞进 context 反过来加剧失忆。把它们拆开看：

### 5.1 失忆（Amnesia）

症状：Agent 在 T+02:13 没看见 `nothing to commit` 这条 tool output。

机制：context window 满了之后，最老的内容被截断。早期的对话、初始的任务定义、关键的 tool 返回值，直接消失。

反面：你不能说"模型记住了任务"，它只记得 context window 还能装下的最后一部分。

对策（第 16 篇展开）：分层记忆 L0/L1/L2 + 4 阶段压缩管线。把"会被丢失的内容"在丢失前结构化压成摘要，挪到 L1；把"长期可能要用的事实"沉到 L2。

### 5.2 漂移（Drift）

漂移和失忆不一样。失忆是"丢了"，漂移是"歪了"。

回到第 1 节那段 trace。T+01:23 Agent 说"问题应该在 lifetime 上"，任务开始时根本没人提 lifetime。这个判断是自己推理出来的，要命的是它出现得很自然：之前几轮 Agent 自己说过 "borrow checker" / "ownership" 之类的词，再绕几轮，"lifetime" 就冒出来了。每一轮 LLM 输出被加进下一轮 input，Agent 在自己的话里看见上一轮自己说的话，倾向继续。几十轮下来，初始意图被累积输出污染，没人能回溯它是什么时候第一次冒出来的。

这条反面工程师要刻在心里：你不能假设"Agent 还在做用户最初要它做的事"，它做的是"它觉得它在做的事"。这两件事会越走越远。

对策见第 13、14 篇：append-only `ProgressJournal` 锚定关键节点 + 阶段性 ExpectedOutcome 比对。Agent 每过 N 轮要回到 Journal 里那条硬记录："用户最初要的是什么。"

### 5.3 合理化（Rationalization）

症状：Agent 在 T+02:11 说"我已经定位并修复了这个 bug"，其实它在 T+02:13 才会发现没东西可提交。它先做的不是验证，是先得出结论。

机制：Agent 在自己的 trace 里看到"我已经分析过 N 个文件"、"我已经试过 M 个方案"，会自然地推出"那一定快接近答案了"。LLM 不区分"努力过"和"做对了"，它把前者合理化成后者。

反面：你不能让 Agent 自己说"我修好了"，它说的不算。必须有外部 Verifier 用 evidence 裁定。

对策（第 14 篇展开）：Generator-Evaluator 分离。Generator 写代码，Evaluator 在独立 context 里只看 evidence（cargo test 输出、git diff、文件状态），不看 reasoning。

---

三者是合谋。失忆先把关键事实挤出 context，Agent 拿着残缺信息就开始漂移目标；漂移之后它又用剩下的上下文把下一步合理化掉；这套合理化继续往 context 里塞无关内容，回头加剧失忆。一个咬一个。

根源只有一条：

> Context 是有状态、可累积、可污染的资源，而 LLM 没有"自我修正" context 的能力。

这个问题不能靠"让 Agent 自己更聪明"解决，只能靠 harness 外置，压缩、锚定、外部验证三件事都不能在 Agent context 内部进行。

---

## 6. 预告：本系列怎么把这三个杀手按下去

| 杀手 | 对策 | 出现在 |
| --- | --- | --- |
| 失忆 | 三层记忆 L0/L1/L2 + 4 阶段压缩管线（ `ContextCompressor`） | 第 16 篇 |
|...
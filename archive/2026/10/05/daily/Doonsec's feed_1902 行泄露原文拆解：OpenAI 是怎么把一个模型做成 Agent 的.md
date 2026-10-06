---
title: 1902 行泄露原文拆解：OpenAI 是怎么把一个模型做成 Agent 的
url: https://mp.weixin.qq.com/s/d5GgSUNIy0BvV8smjaG4Jg
source: Doonsec's feed
date: 2026-10-05
fetch_date: 2026-10-06T08:19:54.318262
---

# 1902 行泄露原文拆解：OpenAI 是怎么把一个模型做成 Agent 的

# 1902 行泄露原文拆解：OpenAI 是怎么把一个模型做成 Agent 的

原创

asaotomo
asaotomo

Hx0极客圈

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

AI 工程 · 原文拆解

1902 行泄露原文拆解
OpenAI 是怎么把一个模型做成 Agent 的

我把 GPT-6 Sol Codex 那份泄露文件完整读了一遍，也核对了它的来源与时间。它不是一个"系统提示词"，而是 54 个模块的运行时配置合集，其中 25 个是 Codex 的 Rust 源码路径。权限矩阵、长任务续跑、上下文交接、多智能体、安全分类器——本文逐块拆开，每块给出可迁移的做法。

· 情报等级：高　· 全文引用均已逐字比对原始文件　· 2026-10-05

这几天，中文互联网上在传一件事：OpenAI 正在使用的代码模型 **GPT-6 Sol Codex**，它的完整系统提示词被人放到了公开的 GitHub 仓库里，任何人都能下载。

但这件事的价值，远不止"提示词被看到了"。我把这份文件下载下来，逐行读完 1903 行，也核对了它从哪来、什么时候被放上去、到底有多大。读完之后可以这么说：**它其实是一份生产级 AI Agent 的工程蓝图。**

本文分两部分：**前半**讲清这份文件的来龙去脉与核证过程，附完整证据链；**后半**逐模块拆解，每块给出能迁移到自己项目里的做法。如果你只想看结论，可以直接跳到第 11 节。

先给一个最小事实集：泄露的是**一份 1903 行、约 30 万字符的文本文件**，内含 **54 个模块**；它于 **2026 年 9 月 22 日 21:43（UTC）**被提交到一个公开仓库，10 月初在中文圈引发大规模讨论。

01事情的来龙去脉

1.1 传播是怎么起来的

这一轮讨论的起点是一条微博爆料帖：爆料者称提取了 GPT-6 Sol Codex 高达 29.4 万字符的完整系统提示词与工具定义，共 1902 行指令，并给出了 GitHub 链接。随后 IT 之家等科技媒体跟进报道，把它推到了更广的读者面前。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/PUTQGRQ4GO8jAcL6wzkzYkJ2J0vlRXCdl6s6xr31MJID2V1fyww5ldnBibdkYUbSxdZBkxuTmvTqezxq5ujSC3YQHryYlFDXVTwE1nUFCtLs/640?wx_fmt=jpeg)

图1 | 微博上流传的爆料帖。它给出的数字基本属实，但时间与定性需要说清。

这条帖子里给出的两个关键数字——**29.4 万字符**和 **1902 行**——后面我们都逐一核对过，基本属实。但它对**时间**与**性质**的表述，需要说清楚。

1.2 文件放在哪

承载这份文件的，是一个叫 **CL4R1T4S** 的公开仓库，由安全研究者 Pliny the Liberator 维护。它的自我介绍写得很直白："LEAKED SYSTEM PROMPTS FOR CHATGPT, CLAUDE, GEMINI, GROK, PERPLEXITY, CURSOR, LOVABLE, REPLIT, AND MORE!"——给所有 AI 系统做"透明度"。

![](https://mmbiz.qpic.cn/mmbiz_jpg/PUTQGRQ4GOicFamMb3UAiaHuMHDoF0I5nQWXMvTcJZOsqRKxKNl1t8jFiapibkgufXwYL8bffqrW1ialibo6g6IONfbdJSe2kbLkY196g3Ptad3pY/640?wx_fmt=jpeg&from=appmsg)

图2 | 承载文件的仓库 CL4R1T4S——50,950 star、10,448 fork，按厂商分目录。

截至 10 月 5 日，该仓库有 **50,950 star、10,448 fork**，采用 AGPL-3.0 协议。标签里既有 leaked、hacking，也有 prompt-engineering、red-teaming——它把自己定位成红队资料库。仓库按厂商分目录，OpenAI、Anthropic、Google、xAI 都有。

1.3 文件本身长什么样

文件路径是 OPENAI/Codex\_Desktop/GPT-6-Sol\_Prompts.txt。GitHub 页面本身给出了三个可直接核对的数字：

![](https://mmbiz.qpic.cn/mmbiz_jpg/PUTQGRQ4GOickNR2dT1GAyYGibzdLPh0gvFXtyPL4AWia7oMPFLicxnwicOELVNfmCJKgia8HfOesomjyMYphxzdPKHOBFSS3ibtic8WWBoaqOKLkAs/640?wx_fmt=jpeg&from=appmsg)

图3 | 文件页：1902 lines (1333 loc) · 157 KB，任何人都能下载全文。

|  |  |  |
| --- | --- | --- |
| 项目 | 实测值 | 来源 |
| **行数** | 1902 lines (1333 loc) | GitHub 文件头 |
| **体积** | 157 KB（161,166 字节） | GitHub 文件头 / 仓库 API |
| **字符数** | 160,753 字符 | 下载全文后本地统计 |
| **配套文件** | GPT-6-Sol\_Tools.json（139,048 字节） | 仓库 API |

主文件与工具定义相加约 **30 万字符**，与爆料帖中"29.4 万字符"的说法吻合。

1.4 什么时候被放上去的

这一点可以直接查提交记录。GitHub 的提交历史页显示，创建这个文件的那次提交来自 **Sep 23, 2026**，提交信息是 "Create GPT-6-Sol\_Prompts.txt"，commit 号为 722edf2。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/PUTQGRQ4GO93yTj7WWs9IEDKANeP21Rr71QicdIsKIGg33j9ibibjGMzR4hibHNdSDsD9jsEDwgicWbZWniaWTDUasZ7OvdfELSWKBicDGXDp9L2DQ/640?wx_fmt=jpeg&from=appmsg)

图4 | 提交记录：Commits on Sep 23, 2026 → “Create GPT-6-Sol\_Prompts.txt”（722edf2）。

这里有个容易看错的地方：**仓库 API 返回的时间戳是 2026-09-22 21:43（UTC），而 GitHub 页面显示 Sep 23**——因为 21:43 UTC 换算成北京时间是次日凌晨 05:43。两种写法都对，说的是同一个时刻。

对比一下传播时间：中文圈的集中讨论出现在 **10 月 5 日**。也就是说，**文件本身比这轮讨论早了将近两周**。

1.5 三条基本事实的核证结果

把流传最广的几种说法与核查结果并排放，读起来最清楚：

|  |  |  |
| --- | --- | --- |
| 流传的说法 | 核查结果 | 依据 |
| "刚刚泄露 / 今天的事" | **不准确。** 文件于北京时间 9 月 23 日凌晨就已提交，10 月 5 日才是中文圈的讨论高峰 | 提交记录 722edf2 与仓库 API 时间戳 |
| "OpenAI 的模型被破解了" | **定性不准确。** 被公开的是一份任何人都能下载的文本；爆料者没有公开提取方法。泄露的是提示词与工程配置，**不是权重、不是训练数据、不是用户数据** | 仓库内文件内容；原帖未提及方法 |
| "30 万字系统提示词" | **基本属实，但要说清口径** ：主文件 160,753 字符，另有 139,048 字节的工具定义，合计约 30 万 | 文件头 + 本地统计 + 仓库 API |

把这三条说清楚，后面看内容时才不会跑偏：**我们面对的是一份"两周前就已经公开、体量约 30 万字符、内容为提示词与工程配置"的文本**，不是一次正在发生的事故。

02它不是一个提示词，而是 54 个模块

下载全文后，第一件让我意外的事是它的结构。**1902 行里包含 54 个具名模块，用 ===== 分隔。**按前缀分三类：

|  |  |  |
| --- | --- | --- |
| 前缀 | 数量 | 是什么 |
| model\_messages.\* | **12** | 运行时拼进上下文的提示词模块（主指令、多智能体角色、token 预算、安全分类器、浏览器权限策略） |
| desktop.\* | **17** | 桌面客户端内部模块，代号被压缩过（G3 / K3 / q3 / Y3 / X3 / Z3 …） |
| codex-rs/… | **25** | **Codex 的 Rust 源码文件路径** ——这是本次泄露里信息量最大的部分 |

那 25 个 codex-rs/ 路径，等于把 Codex 的**项目目录结构**一并交了出来：

codex-rs/prompts/templates/permissions/approval\_policy/\*
codex-rs/prompts/templates/permissions/sandbox\_mode/\*
codex-rs/prompts/templates/compact/\*
codex-rs/prompts/templates/review/rubric.md
codex-rs/ext/goal/templates/goals/\*
codex-rs/ext/memories/templates/memories/\*
codex-rs/ext/web-search/\*
codex-rs/models-manager/prompt.md
codex-rs/protocol/src/prompts/base\_instructions/default.md

看懂这个结构，后面每一块都顺理成章：**Codex 不是一个"带提示词的模型"，而是一个有扩展系统（ext）、有权限层（permissions）、有协议层（protocol）的完整工程。**下面按模块拆。

03干货一：权限系统是一张矩阵，不是一句"要小心"

这是全文最值得学的一块。多数 Agent 项目的权限设计是一句"危险操作要先问用户"，而 Codex 把它拆成了**两个正交维度**。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/PUTQGRQ4GOibw0hdoP1BMlflyzRKAgTEPGhQmGPNdKHSzEgsYib2tAvWIcfPS7X7KNlzOWniadS9Npr1sTc64FHjibiawE5P1ic2bgOZJC8zKJ5eI/640?wx_fmt=jpeg&from=appmsg)

图5 | 权限三层示意：审批策略 → 命令分段 → 沙箱模式，三者独立配置。（图源：本文整理）

3.1 审批策略：四种

|  |  |
| --- | --- |
| 策略 | 行为 |
| never | 完全不允许提权，请求直接拒绝 |
| on\_request | 用户批准、或命中已有规则，命令可跑在沙箱外 |
| on\_request\_rule\_ request\_permission | **优先申请"沙箱内的额外权限"** （网络、文件读写路径），而不是直接要求跑出沙箱 |
| unless\_trusted | 默认都要批准，除非有明确的 exec policy 规则放行 |

3.2 沙箱模式：三种

1**read-only**——只允许读文件。

2**workspace-write**——可读，可写 cwd 和 writable\_roots；写别处需要批准。

3**danger-full-access**——不做文件系统沙箱，所有命令放行。

3.3 最有价值的一处：命令分段求值

如果只记一条，记这条。原文规定：命令字符串会**按 shell 控制符拆成独立片段**——管道 |、逻辑符 &&||、分隔符 ;、子 shell 边界 (...) 和 $(...)——**每个片段单独判定**。

原文举例：git pull | tee output.txt
会被拆成两个片段分别评估：
["git", "pull"]　和　["tee", "output.txt"]

![](https://mmbiz.qpic.cn/mmbiz_jpg/PUTQGRQ4GO9XmLk1ibSf9L9U2lY1buTCqTbl5bIArtV5P7HOL80PISFO9sBTfveslGhia3rCAY03O4W4p6Q6nSFXr9iaIwEGakEdbg5LbNyiaDM/640?wx_fmt=jpeg&from=appmsg)

图6 | 文件原文第 1312–1330 行：片段拆分规则，以及那个 git pull 的例子。（图源：GitHub）

而**更复杂的 shell 特性——重定向 >、命令替换 $(...)、环境变量 FOO=bar、通配符 \* ?——不参与规则匹配**。原文给的理由很关键：**"以限制一条已批准规则所能覆盖的范围"**。

这条设计的精髓在于：**白名单必须建立在"可完全解析"的输入上。**一条规则如果无法确定它到底会执行什么，就不应该被自动放行。

![](https://mmbiz.qpic.cn/mmbiz_jpg/PUTQGRQ4GOibUjWbnx8LDEpibStYNFkkvIibmtte2ABV9PZUMib7G99Yuib6wxylET6wPbvvUGbtJiarOtLYbZdZbHpARicFnQbe5YNFY1wscD8dd0/640?wx_fmt=jpeg&from=appmsg)

图7 | 为什么「解析不了就不放行」：参与匹配与不参与匹配的两类语法。

3.4 prefix\_rule 的三条禁令

用户批准一次后，可以沉淀成可复用的前缀规则（prefix\_rule）。原文对它的限制写得非常清楚：

✕**禁止过宽的前缀**——原文点名不许 ["python3"]、["python", "-"] 这类"等于放行任意脚本"的前缀。

✕**破坏性命令永不给前缀规则**——原文：NEVER provide a prefix\_rule argument for destructive commands like rm。

✕**命令里带 heredoc / herestring 时不给**——因为内容无法静态判定。

🛡️ 可迁移做法：权限要"分层"，不要"一刀切"

把"要不要问用户"拆成三个独立问题：**① 文件系统允许写到哪（沙箱模式）② 什么情况下可以跑出沙箱（审批策略）③ 一次批准能复用多大范围（前缀规则）**。三个问题分开设计，才能做到"日常操作不打扰、危险操作拦得住"。

另外那条"**无法完全解析的输入不参与规则匹配**"，可以直接搬到任何工具白名单场景：**凡是解析不确定的，一律降级为人工确认，而不是当成安全。**

04干货二：权限的"松"，是靠一个机制换来的

文件里有一段语气很重的指令，中文圈引用最多：

"**The user gets very frustrated when you stop and ask for confirmation or permission**, so make sure to explicitly explain why you need the confirmation…"

配套的是第 26 行这条工作原则——**把用户审批放到流程的最后一步**：

"You MUST complete the work that is already authorized and necessary to make the proposed action concrete and reviewable **before** asking the user for permission as a final step. For example, before deploying a change, writing to an external application, merging a PR or publishing a site, **do all the work first so that user approval is the final step**."

很多人把这段读成"OpenAI 教模型别烦用户"。但把它和上一节的权限矩阵放在一起看，结论正好相反：

**它之所以敢让模型"少问"，是因为沙箱在下面兜着。**改代码、跑测试、建草稿 PR——这些都在 workspace-write 沙箱里，可回滚、可审阅，所以不需要打断用户；而部署、合并、发布这些不可逆动作，仍然要走 require\_escalated 请人签字。

🎯 可迁移做法：自主性的前提是"可回滚"

判断一个动作该不该让 Agent 自主执行，不要问"它重不重要"，要问 **"错了能不能撤"**。可逆 → 放手做，做完一起看；不可逆 → 停下来，让人签在具体结果上。
这条判据比"高风险/低风险"更好落地，因为它可操作、可枚举。

配合这条原则，还有两个工程细节。第 62 行规定：**持续工作期间，不能让用户超过 60 秒收不到一条进展更新**（走 commentary 通道）。第 99 行则硬编码了工具偏好——搜索首选 rg 而不是 grep，独立搜索用 await Promise.allSettled([...]) 批量并发。

05干货三：长任务——目标跨回合存活，且不许被偷换

文件里有一整块 codex-rs/ext/goal/templates/goals/，是长任务续跑机制。其中最值得抄的是它对**"目标漂移"**的防守：

"This goal persists across turns. Ending this turn **does not require shrinking the objective to what fits now**."

"Keep the full objective intact. If it cannot be finished now, make concrete progress toward the real requested end state, leave the goal active, and **do not redefine success around a...
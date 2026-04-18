---
title: 从Vibe Coding到Agentic Engineering：重构后台开发全流程
url: https://mp.weixin.qq.com/s/pr8oQ9wEC7Oa1NvvW89j6w
source: Doonsec's feed
date: 2026-04-17
fetch_date: 2026-04-18T04:28:21.565844
---

# 从Vibe Coding到Agentic Engineering：重构后台开发全流程

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/KVER9adz904szngkJV1gTzqoZzdQGmaa8Qx62MQX7ERT1QZowzIIMSxFD4R7vwFWrrGAko0y159xrMWqsHibYuIqjcrsgN36WSJ4S5gJKCHs/0?wx_fmt=jpeg)

# 从Vibe Coding到Agentic Engineering：重构后台开发全流程

原创

腾讯程序员
腾讯程序员

腾讯技术工程

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/j3gficicyOvasVeMDmWoZ2zyN8iaSc6XWYj79H3xfgvsqK9TDxOBlcUa6W0EE5KBdxacd2Ql6QBmuhBJKIUS4PSZQ/640?wx_fmt=gif&from=appmsg)

作者：seanguo

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KVER9adz905N77ueDJTib4a0yibQaEGC8pyGvcJ4gByqXs7RnrSnqL1Z5IlV0S4fBOcfHMGy9ic0P994JsRx46u717gUqNDQlmibxCl5ibe2157I/640?wx_fmt=png&from=appmsg)

### 引言

做后台开发的同事应该都有这个体会：从接到需求到最终发布，我们要在 PM、GitPlatform、编辑器、DevOps 平台、Galileo 之间来回横跳。每次切换都在丢上下文——刚在 PM 看完需求描述，切到编辑器就忘了某个细节；部署完测试环境去查日志，又得回忆刚才改了哪几行代码。

你可能听过 **Vibe Coding** 这个说法——打开 AI 对话框，用自然语言描述需求，让模型直接生成代码，跑通就算完。原型验证很爽，但一旦要上生产，问题就来了：生成的代码质量不可控、没有审查流程、改完了 commit message 也是乱的。说到底，Vibe Coding 是"提示即祈祷"（prompt-and-pray），你把需求扔给 AI，然后祈祷它别出错。

今年行业里逐渐形成了一个更成熟的概念：**Agentic Engineering**（智能体工程）。核心思路是——人负责定义目标、约束条件和质量标准，AI 作为自主智能体在**结构化流程**中执行规划、编码、测试和迭代，每个关键节点都有人工审核。它不是让 AI 随意发挥，而是把 AI 的能力嵌入到一套有纪律的工程体系里。

最近一周，我用 **Claude Code + 自定义 Skill/Command/MCP 体系** 做了一次实践：把从需求到发布的所有环节串到一个终端会话里。AI 全程保持对当前任务的理解，在预设的流程框架内自主执行；我只需要在关键节点做决策——审批计划、确认部署、审查代码。回过头看，这套东西就是 Agentic Engineering 在后台开发场景的一个落地样本。

这篇文章把整个流程拆开给大家看，从需求到发布每一步怎么跑的，踩过哪些坑，最后沉淀出了什么（~~🔥token的十大技巧~~）。

~~不过，说实话，虽然过程很完美，但消耗的 token 数量也不容小觑。迫切需要更高的 token 额度了~~

![](https://mmbiz.qpic.cn/mmbiz_png/KVER9adz905fiaLiawcKG08ZTnib8Up1HAqZk6JG1nVfGILvicJ5TK8tpicwxSGbalick2bFZK85bVwQHwLRVKfnrzUniaXcB3OU7YhzNLhYex8TiaQ/640?wx_fmt=png&from=appmsg)

#### 全流程概览

先看效果。下面是整个流程的各阶段概览——从需求到发布，开发者的角色从"亲自执行"变成了"审核确认"：

| 阶段 | 核心工具 | 开发者做什么 |
| --- | --- | --- |
| ① 需求创建 + 分支初始化 | `pm-dev` | 口述需求 |
| ② 需求澄清 | `brainstorming` | 回答 2-3 个问题 |
| ③ 制定实施计划 | `writing-plans` | 审核计划 |
| ④ 并行开发 | `executing-plans` + `/commit` | 几乎无需干预 |
| ⑤ 代码自审 | `code-review` | 审核报告 |
| ⑥ 编译部署 | `dtools` | 确认部署参数 |
| ⑦ 日志排查 | `galileo-log-query` | 手动触发测试 |
| ⑧ 创建 MR | `/create-mr` | 确认 MR 信息 |
| ⑨ AI 辅助评审 | `/review-mr` | 审核 AI 评审意见 |
| ⑩ 修复评审意见 | `/fix-mr` | 确认修复方案 |
| ⑪ 合入发布 | CI/CD | 点 Merge + 灰度发布 |

后面各阶段会逐个展开细节。

#### 工具体系速览

这套[工具链](https://git.example.com/alice/dot-agents/tree/master)分三层，理解了层次关系，后面的内容就好跟了：

| 层次 | 说明 | 示例 |
| --- | --- | --- |
| **Skill** （技能） | 核心业务逻辑，由系统根据上下文自动触发，或被 Command 调用。每个 Skill 有独立的工具权限白名单和执行流程 | `pm-dev` 、`git-workflow`、`code-review`、`dtools`、`galileo-log-query`、`git-context`、`wiki-doc`、`service-analyzer` |
| **Command** （斜杠命令） | 用户通过 `/xxx` 主动调用的入口，轻量级路由，委托给对应的 Skill 执行 | `/commit` 、`/create-mr`、`/review-mr`、`/fix-mr`、`/analyze-codebase` |
| **MCP Server** （外部服务） | 通过 Model Context Protocol 连接的外部平台 API，为 Skill 提供数据和操作能力 | GitPlatform MCP、PM MCP、Galileo MCP、KnowledgeBase 知识库 MCP、InternalWiki MCP |

此外还有一类来自 `superpowers` 插件的**结构化工作流 Skill**（`brainstorming`、`writing-plans`、`executing-plans`、`subagent-driven-development`、`verification-before-completion` 等），它们定义了从需求澄清到代码交付的标准流程，防止 AI 跳过关键步骤自由发挥。

下面以一个**真实的小变更需求**为例，走完从需求到发布的全流程——「RedeemReward 接口数据上报逻辑变更：无论领取是否成功，都要上报结果，新增 errcode/errmsg 字段」。选这个需求是因为它体量适中（涉及 go mod 依赖更新、结构体扩展、接口逻辑重构），刚好能展示每个阶段的自动化能力，又不会因为业务本身太复杂而分散注意力。![](https://mmbiz.qpic.cn/mmbiz_png/KVER9adz906ufNaBXMBRTfxRaRozZCialEiaHIcInfvLraEhDIuhAG5hRlfLD51nYbw54KxhO1IlX2fjUNNCwTXPCUwQZqic47I4s7SlDSgasw/640?wx_fmt=png&from=appmsg)

### 阶段 1：需求获取与分支初始化

> [!info] 使用的工具**`pm-dev`** (Skill) — PM 开发初始化工具，两种入口：
>
> 1. 给 PM URL → 自动解析需求 ID，拉取需求标题和正文
> 2. 不给 URL → 通过 brainstorming 澄清需求后，自动调用 PM MCP 创建需求单
>
> 创建完成后自动：建分支（`feature/{username}_{short_id}`）→ 保存需求文档到 `docs/pm/` → 衔接后续开发流程

**场景**：手头没有现成的 PM 需求单，直接在终端里口述需求就行。

**操作**：输入 `/pm-dev` 命令并附上需求描述：

```
❯ /pm-dev RedeemReward
接口里的数据上报逻辑变更，无论领取是否成功，都要上报结果
（上报数据新增 errcode, errmsg 字段）。新字段要更新
git.example.com/org/component/report_data/reportstruct go mod 获取。
```

Claude Code 检测到当前在 master 分支，又没有 PM URL，就弹出选择：

```
· 没有检测到 PM 需求单信息，请选择如何继续？ → 自动创建新需求单
```

接下来 AI 会进入 brainstorming 模式澄清需求（详见阶段 2），澄清完自动创建 PM 需求单：

```
⏺ pm - stories_create
  workspace_id: "12345678"
  name: "RedeemReward上报逻辑变更新增错误码"
  description: "RedeemReward 接口的数据上报逻辑变更：无论领取是否成功，都要上报结果..."

✅ 需求单创建成功
  - 标题: RedeemReward上报逻辑变更新增错误码
  - 链接: https://pm.example.com/pm_fe/12345678/story/detail/1012345678001958011
```

口述需求，AI 交互澄清后，自动创建的需求单示例：

![](https://mmbiz.qpic.cn/mmbiz_png/KVER9adz907cwUWXIgR1smwE9TYHJp82mMtZicNWsfSVQMtGNF9vsRVT0sKtItHap6OXL2edP20icrVib0rWnrfVQW6ZFoz26d9ZMPqx0Oy9qU/640?wx_fmt=png&from=appmsg)

随后自动创建开发分支并保存需求文档：

```
⏺ git checkout -b feature/alice_131900001
⏺ Write(docs/pm/131900001.md)  — 保存需求文档
```

**效果**：一段口述 → PM 需求单 → 规范命名的开发分支 → 需求文档落盘。全程没打开过 PM 页面。

> [!tip] Skill 也可以当命令用`pm-dev` 是一个 Skill（系统根据上下文自动触发），但你也可以通过 `/pm-dev` 显式调用它。实际上，所有 Skill 都支持以 `/skill-name` 的方式手动触发——当你明确知道要用哪个 Skill 时，直接 `/xxx` 调用比等待自动触发更高效。

> [!tip] 有现成的 PM 需求单？ 直接提供链接即可：`/pm-dev https://pm.example.com/xxx/story/detail/10xxx`，AI 会自动拉取需求详情并创建开发分支。

直接拉取需求单示例：

![](https://mmbiz.qpic.cn/mmbiz_png/KVER9adz9075quZFeibaY05fqgxicgJOHmmXRsrricVia8pXVVOMdBwJSZ7Ygun5C0WVHichrYznJQgiauPibficEMSF6FHndNfMju1Joian5NryDyDY/640?wx_fmt=png&from=appmsg)

补充一个 AI aha moment 的例子：

我在开发 pm-dev skill 的时候，发现项目管理 MCP Server 并不支持将链接里面的长ID（1012345678001900001）转成 short\_id（131900001）。但是想要自动创建特性管理值就需要用到 short\_id，那该怎么做呢？

**AI 直接推测出了 short\_id 和 ID 的关系！**（我开发这么久的需求，见过的需求 url & short ID 无数，从来都没有发现两者之间的关系。这个时候我就感觉 AI 是真的能够发现我们肉眼所发现不到的规律。）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KVER9adz905DkLkmFJU0ictz7sUmeXnoaO9TWABaGKsOb5bqNPdNVUoicz4nQu7lltnaZtp5gGtMeCf1qLwBg93nWIKagB5T2pRhyYPDJ3TPk/640?wx_fmt=png&from=appmsg)

### 阶段 2：交互式需求澄清

> [!info] 使用的工具**`superpowers:brainstorming`** (Skill) — 结构化的需求澄清流程。AI 不会直接写代码，而是先探索代码库了解现状，然后通过提问-回答逐步明确需求边界、技术方案和实现路径，最终产出一份双方达成共识的设计方案。
>
> **`wiki-doc`** (Skill) / **`knot` MCP** — 知识库检索。澄清过程中 AI 可以搜内部 Wiki 文档或通过 KnowledgeBase 知识库做语义检索，为设计决策补充技术背景和历史方案参考。

**场景**：需求描述就一句话，AI 得先搞清楚代码现状和变更细节才能动手。

> [!info] 链式调用 这个阶段不需要手动触发——`pm-dev` 完成需求创建和分支初始化后，会自动链式调用 `brainstorming` 进入需求澄清。brainstorming 完成后又会接着调用 `writing-plans`（阶段 3），形成 **需求 → 澄清 → 计划** 的自动流水线。

**操作**：AI 先自动探索项目代码，了解 RedeemReward 接口和上报逻辑的现有实现：

```
⏺ Explore(探索 RedeemReward 和上报逻辑)
  Done (20 tool uses · 93.8k tokens · 56s)
```

然后基于代码理解，抛出关键问题：

```
🤔 新增的 errcode/errmsg 字段是加到现有的 Report_table_001（数据上报表）上，
   还是用一个新的上报表？

❯ 复用 Report_table_001 表, 更新 go mod 以后就有新增的 2 个字段了
```

AI 理解后，提出两种实现方案并给出推荐：

```
方案 A（推荐）：在 RedeemReward 末尾统一上报，不提前 return
  将上报逻辑移到函数末尾，把第三方调用的 error 信息传入上报参数。
  - 优点：改动集中，与现有 ReportConsumeCount 风格一致
  - 缺点：需要调整 error 处理流程

方案 B：在每个 return 前都加一次上报调用
  - 优点：不改变原有 return 逻辑
  - 缺点：多处重复调用，容易遗漏
```

```
· 你倾向哪种实现方式？ → 方案 A：统一上报 (Recommended)
```

确认方案后，AI 输出完整的设计方案：

```
设计方案:

1. 数据结构变更 — CardReportParam 新增 ErrCode/ErrMsg 字段
2. RedeemReward 流程变更 — 用 defer 确保上报一定执行
3. 变更文件清单:
   ┌──────────────────────────┬──────────────────────────────────────┐
   │           文件           │                 变更                 │
   ├──────────────────────────┼──────────────────────────────────────┤
   │ go.mod                   │ 升级 report_data 版本           │
   │ repo/report/card_report.go │ CardReportParam 新增字段，ReportCard │
   │                          │ 填充新字段                           │
   │ logic/redeem_reward.go      │ 重构 RedeemReward，无论成败都上报       │
   └──────────────────────────┴──────────────────────────────────────┘
```

**效果**：AI 不是闭门造车——先读代码、再提问、再出方案。设计文档自动保存到 `docs/plans/` 并 commit。

> [!tip] 不要重复造轮子`pm-dev` 早期版本曾经自己实现了头脑风暴/写计划/执行计划的功能，后来发现 `superpowers` 插件已经提供了成熟的 brainstorming、writing-plans、executing-plans 等 Skill，经过大量打磨，效果更好。最终把自制逻辑替换为链式调用现成 Skill。**教训：自定义 Skill 的核心价值是编排和串联，而不是从零实现所有能力。**

> [!tip] 知识库补充上下文 在澄清过程中，AI 可以通过 `wiki-doc` 搜索内部 Wiki 文档，或通过 `knot` 知识库检索已有的技术方案，为设计决策提供依据。

### 阶段 3：制定实施计划

> [!info] 使用的工具**`superpowers:writing-plans`** (Skill) — 结构化计划编写。AI 深入读代码细节（结构体字段、错误处理方式、依赖版本），确保计划里每个 Task 都有精确的文件路径、代码变更描述和验证标准。计划自动保存到 `docs/plans/` 并 commit，人工审核通过后才进入执行。

**场景**：设计方案确认后，AI 自动深入阅读代码，生成可执行的实施计划。

**操作**：AI 先扎进代码细节——结构体字段、错误处理方式、go mod 版本——确保计划里的代码路径和修改点都是准确的：

```
⏺ Read: repo/report/card_report...
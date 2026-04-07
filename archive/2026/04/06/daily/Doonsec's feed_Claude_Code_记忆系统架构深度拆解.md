---
title: Claude_Code_记忆系统架构深度拆解
url: https://mp.weixin.qq.com/s/kCL6XOUU_tp8D97Un7mp7w
source: Doonsec's feed
date: 2026-04-06
fetch_date: 2026-04-07T04:26:10.711140
---

# Claude_Code_记忆系统架构深度拆解

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/xPqpNF2xtKYaSEheG8Dxy6kSKdfuQn45PibMz6bhDLVYic0ia98Z8AZ6XIFYYKJ4lu284lZmawCsyeM6icckaENajQNQP5fDUd0DhNJiaCxwqlAQ/0?wx_fmt=jpeg)

# Claude\_Code\_记忆系统架构深度拆解

原创

辞令
辞令

WhITECat安全团队

![]()

在小说阅读器中沉浸阅读

-----------后台回复“claude”获取源码，便于对照研究

Claude Code

记忆系统架构深度拆解

Memory System Architecture Analysis

基于 claude-code-main 源码深度分析

2026 · 安全架构研究

一、整体架构鸟瞰

Claude Code 的记忆系统是多层次、文件驱动的架构。其核心设计哲学是：

记忆 ≠ 对话历史。记忆是跨会话持久的结构化知识，对话历史只存活于当前 session。

整体分为 5 层，从底向上依次为：

| 层级 | 名称 | 核心机制 | 文件位置 |
| --- | --- | --- | --- |
| Layer 5 | 上下文注入层 | system prompt / user context block | context.ts / memdir.ts |
| Layer 4 | 智能检索层 | findRelevantMemories (Sonnet 侧查询) | memdir/findRelevantMemories.ts |
| Layer 3 | 自动提取层 | extractMemories (后台 forked agent) | services/extractMemories/ |
| Layer 2 | 文件存储层 | memdir (~/.claude/projects//memory/) | memdir/paths.ts |
| Layer 1 | 指令记忆层 | CLAUDE.md 体系 (Managed/User/Project/Local) | utils/claudemd.ts |

二、Layer 1：指令记忆层（CLAUDE.md 体系）

文件：src/utils/claudemd.ts

这是静态的「行为规范」层，由人工配置，不是 AI 自主写入的。用于定义 AI 在特定项目、用户或机构场景下的行为约束。

2.1 加载顺序（优先级从低到高）

越靠近当前工作目录（CWD）的文件优先级越高，后加载意味着更高权重，对应「局部覆盖全局」的直觉：

| 优先级 | 类型 | 路径 | 特点 |
| --- | --- | --- | --- |
| 最低 (1) | Managed | /etc/claude-code/CLAUDE.md | 全局策略，机构级管控 |
| 低 (2) | User | ~/.claude/CLAUDE.md | 用户私有全局指令 |
| 中 (3) | Project | ./CLAUDE.md / ./.claude/CLAUDE.md | 项目级，已提交到 repo |
| 高 (4) | Local | ./CLAUDE.local.md | 项目私有，gitignored |
| 最高 (5) | AutoMem | ~/.claude/projects/.../MEMORY.md | AI 自主写入的记忆索引 |

2.2 @include 指令

CLAUDE.md 文件支持引用其他文件，用 marked lexer 扫描 AST token，只在非代码块文本节点提取 @path：

@./shared/coding-standards.md

@~/my-global-rules.md

@/absolute/path/to/rules.md

•  最大嵌套深度：5 层（MAX\_INCLUDE\_DEPTH = 5）

•  防止循环引用：processedPaths Set 追踪已处理路径

•  支持 ~/、./、/absolute 三种路径前缀

•  非文本格式文件（图片、PDF）自动跳过

2.3 条件规则（.claude/rules/\*.md）

带 paths: frontmatter 的规则文件仅在操作匹配文件时才注入上下文：

---

paths:

  - "src/api/\*\*"

  - "\*.go"

---

所有 Go 文件必须包含错误处理...

这意味着编辑 Go 文件时才加载 Go 规范，编辑 API 文件时才加载 API 规范，有效控制 context window 使用量。

三、Layer 2：文件存储层（memdir）

文件：src/memdir/

这是 AI 自主读写的持久记忆目录，是整个记忆系统的数据层基础。

3.1 目录结构

~/.claude/

  projects/

    /        ← 按 git 根目录隔离

      memory/

        MEMORY.md               ← 索引文件 (entrypoint)

        user\_role.md            ← 用户信息记忆

        feedback\_testing.md     ← 行为反馈记忆

        team/                   ← 团队共享记忆 (需开启 TEAMMEM)

          MEMORY.md

          project\_deadline.md

路径解析优先级（src/memdir/paths.ts）：

•  CLAUDE\_COWORK\_MEMORY\_PATH\_OVERRIDE 环境变量（Cowork/SDK 使用）

•  settings.json 中的 autoMemoryDirectory（支持 ~/ 展开）

•  默认：      /projects//memory/

注意：为了多 worktree 共享同一记忆，路径基于 findCanonicalGitRoot() 而非 CWD，保证同一 repo 的不同 worktree 共享记忆。

3.2 四种记忆类型

来自 src/memdir/memoryTypes.ts，每种类型有明确的 scope 和语义：

| 类型 | 默认 Scope | 保存时机 | 使用时机 |
| --- | --- | --- | --- |
| user | 始终私有 | 了解用户角色、偏好、知识背景时 | 工作需要基于用户画像时 |
| feedback | 私有（项目规范→团队） | 用户纠错或确认非显式做法时 | 避免重复犯同类错误时 |
| project | 强烈建议团队 | 了解进展、截止日期、决策背景时 | 理解请求背后动机时 |
| reference | 通常团队 | 发现外部系统资源时 | 引用外部系统信息时 |

3.3 记忆文件格式

每个记忆文件使用 YAML frontmatter 标注元数据，内容遵循结构化模板：

---

name: 用户背景

description: 用户是数据科学家，关注可观测性

type: user

---

[记忆正文]

\*\*Why:\*\* 用户提到 logging 调研项目

\*\*How to apply:\*\* 回答时侧重可观测性角度

Why + How to apply 的结构化要求源于 eval 验证：知道"为什么"可以让模型判断边界情况，而不是盲目执行规则。

3.4 MEMORY.md 索引文件

MEMORY.md 是轻量索引，不是内容本身，每行一条指针：

- [用户背景](user\_role.md) — 数据科学家，Go 专家，React 新手

- [测试规范](feedback\_testing.md) — 不允许 mock 数据库

硬性限制（避免撑爆 system prompt）：

•  最大行数：200 行（MAX\_ENTRYPOINT\_LINES）

•  最大字节：25,000 字节（MAX\_ENTRYPOINT\_BYTES）

•  超限自动截断并附 WARNING 提示模型

3.5 不该保存的内容（明确排除）

代码中明确定义了记忆的「负边界」，即使用户明确要求也拒绝保存：

•  代码模式、约定、架构、文件路径 — 可以通过 grep/读代码获取

•  Git 历史、最近变更 — git log / git blame 更权威

•  调试方案或修复配方 — 答案在代码里，背景在 commit message

•  已在 CLAUDE.md 文档化的内容 — 重复保存

•  临时任务细节、进行中的工作 — 只在当前会话有用

四、Layer 3：自动提取层（extractMemories）

文件：src/services/extractMemories/extractMemories.ts

这是整个架构最精妙的设计：AI 在每轮对话结束后自动从对话中提取值得记住的内容，写入持久记忆目录。

4.1 触发时机

每次主 agent 产出最终回复（无 tool call 的 stop 事件）时，fire-and-forget 异步触发提取流程。由 handleStopHooks 在 stopHooks.ts 中调用。

4.2 Forked Agent 模式

提取器使用 runForkedAgent 模式，关键设计：

| 特性 | 设计 | 原因 |
| --- | --- | --- |
| Prompt Cache 共享 | 与主 agent 使用相同 cache key | 提取几乎不增加额外 token 成本 |
| 工具权限沙箱 | 只允许读取 + 仅限 memdir 的写入 | 防止提取 agent 误改代码 |
| 最大轮数限制 | maxTurns: 5 | 防止验证死循环消耗大量 turns |
| 不记录 transcript | skipTranscript: true | 避免与主线程产生竞态条件 |
| 互斥机制 | inProgress 标志 + pendingContext stash | 防止并发运行 |

4.3 游标机制

每次提取只处理增量消息，不重复处理已处理的历史：

let lastMemoryMessageUuid: string | undefined

// 只计算上次游标之后的新消息数

const newMessageCount = countModelVisibleMessagesSince(

  messages, lastMemoryMessageUuid

)

// 成功后推进游标

lastMemoryMessageUuid = messages.at(-1)?.uuid

4.4 主 Agent 互斥

如果主 agent 已经自己写了记忆（更主动、更精确），跳过背景提取，推进游标：

if (hasMemoryWritesSince(messages, lastMemoryMessageUuid)) {

  // 跳过背景提取，推进游标

  lastMemoryMessageUuid = lastMessage.uuid

  return

}

4.5 工具权限沙箱细节

createAutoMemCanUseTool() 定义了精确的权限边界：

•  ✅ 允许：FileRead、Grep、Glob（无限制读取）

•  ✅ 允许：Bash（仅 isReadOnly 的命令：ls/grep/cat/stat 等）

•  ✅ 允许：FileWrite/FileEdit（仅限 memoryDir 路径内）

•  ❌ 拒绝：所有其他工具

REPL 工具被允许，因为它内部的每个操作仍会经过 canUseTool 检查，保持相同的安全约束。

4.6 流量控制

•  inProgress 标志：防止同一时间并发运行多个提取

•  pendingContext stash：并发请求被 stash，extraction 结束后执行一次 trailing run

•  turnsSinceLastExtraction：支持 N 轮节流（tengu\_bramble\_lintel 功能开关）

•  drainPendingExtraction()：进程关闭前等待所有提取完成（60s 超时）

五、Layer 4：智能检索层（findRelevantMemories）

文件：src/memdir/findRelevantMemories.ts

问题：记忆越来越多，全部加载会撑爆 context window。方案：用 Sonnet 做二阶检索，只加载当前查询真正相关的记忆。

5.1 检索流程

| 步骤 | 操作 | 说明 |
| --- | --- | --- |
| 1 | scanMemoryFiles() | 扫描所有 .md 文件，只读 frontmatter 前 30 行 |
| 2 | formatMemoryManifest() | 格式化为文本清单，含类型/文件名/时间戳/描述 |
| 3 | sideQuery(Sonnet) | 让 Sonnet 判断哪些记忆和当前查询相关 |
| 4 | 返回最多 5 个 | 过滤已展示过的记忆（alreadySurfaced），避免重复 |
| 5 | 注入上下文 | 按需加载完整记忆文件内容到对话上下文 |

5.2 Sonnet 检索 Prompt 的设计细节

检索 prompt 经过精心设计，有几个关键约束：

•  "up to 5" 上限：防止过度注入导致 context 膨胀

•  "CERTAIN will be helpful"：不确定就不选，宁可遗漏不要误选

•  recently used tools 排除：正在用的工具不需要加载它的使用文档

•  warnings/gotchas 例外：工具相关的警告/坑点仍然加载，正在使用时最重要

5.3 新鲜度机制（memoryAge.ts）

记忆超过 1 天，自动附加 staleness warning 防止过时数据被当作事实：

export function memoryFreshnessText(mtimeMs: number): string {

  const d = memoryAgeDays(mtimeMs)

  if (d <= 1) return ''  // 新鲜记忆：无警告

  return `This memory is ${d} days old. ` +

    `Claims about code behavior may be outdated. ` +

    `Verify against current code before asserting as fact.`

}

5.4 扫描性能优化

scanMemoryFiles() 的单次扫描设计减少了 syscall 开销：

•  readFileInRange() 内部 stat，一次调用同时获取 mtimeMs 和内容

•  只读前 30 行（FRONTMATTER\_MAX\_LINES）：只需要 frontmatter，不读全文

•  并行处理所有文件（Promise.allSettled）

•  最多处理 200 个文件（MAX\_MEMORY\_FILES）

•  按 mtime 降序排序：最近修改的优先

六、Layer 5：上下文注入层

文件：src/memdir/memdir.ts, src/context.ts, src/utils/claudemd.ts

6.1 两种注入路径

| 注入路径 | 时机 | 内容 | 特点 |
| --- | --- | --- | --- |
| System Prompt | 会话开始时固定 | Git 状态快照 + 记忆系统行为指令 + MEMORY.md 索引 | 静态，整会话缓存 |
| User Context | 每轮对话前动态注入 | CLAUDE.md 内容 + 相关记忆文件 + 当前日期 | 动态，按需更新 |

6.2 buildMemoryLines()：行为指令注入

这个函数向模型注入记忆系统的完整「操作手册」，包括：

•  四种类型的定义，每种附带 when\_to\_save 和 how\_to\_use

•  明确的不该记的内容列表（代码模式、git 历史、临时状态等）

•  两步保存流程：先写 topic 文件，再更新 MEMORY.md 索引

•  记忆与 Plan、Tasks 的使用边界区分

•  staleness 验证要求：推荐前先验证文件/函数是否仍然存在

6.3 Prompt 设计中的 A/B 测试证据

代码注释中包含大量 eval 实验结果，说明 prompt 经过严格验证：

| 实验 | 失败方案 | 成功方案 | 效果 |
| --- | --- | --- | --- |
| H1 验证指令位置 | 放在 'When to access' 下的 bullet | 独立的 H2 section | 0/3 → 3/3 |
| H5 read-side 噪声 | 作为 bullet 嵌套 | 独立 section | 0/2 → 3/3 |
| H6 ignore 反模式 | 无说明 | 显式命名 anti-pattern | eval score 提升 |
| Section 标题措辞 | 'Trusting what you recall' (抽象) | 'Before recommending from memory' (行动导向) | 0/3 → 3/3 |

6.4 TRUSTING\_RECALL\_SECTION 核心哲学

这个 section 体现了记忆系统设计的核心哲学：

"The memory says X exists" is not the same as "X exists now."

具体规则：

•  记忆中提到特定函数/文件/flag → 在推荐前先验证它还存在

•  记忆中总结了 repo 状态 → 用 git log 或读代码替代，不直接引用

•  用户说「忽略记忆」→ 视 MEMORY.md 为空，不引用、不对比、不提及

七、特殊模式

7.1 KAIROS 模式（助手日志模式）

为持久运行的 assistant session 设计的长会话记忆策略：

|  | 普通模式 | KAIROS 模式 |
| --- | --- | --- |
...
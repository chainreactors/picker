---
title: Hermes Kanban 使用指南：多智能体任务编排实战
url: https://mp.weixin.qq.com/s/BPSXWB6aLqoSUENJ3jG1aQ
source: Doonsec's feed
date: 2026-05-25
fetch_date: 2026-05-26T06:02:51.861186
---

# Hermes Kanban 使用指南：多智能体任务编排实战

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BowImrBK4tLtfBh45s3VEpw3oUk2OD41LXvh1hcDVnEtJpDO2ibf9vh5gDwR97mhukksZGUkDBia7g8vu885rSlxpfrtJ5AINoekALOHGcJ1o/0?wx_fmt=jpeg)

# Hermes Kanban 使用指南：多智能体任务编排实战

原创

adra1n
adra1n

YY的黑板报

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

如果你在用 Hermes Agent，很可能已经遇到过这个场景：一个任务包含多个独立的工作流，比如"调研三种方案 → 写对比分析 → 生成代码 → 审查代码"。如果只靠一个 AI 助手从头做到尾，中间一旦中断就全丢了，而且一个大 prompt 里塞太多东西，AI 容易顾此失彼。

Hermes Kanban 就是来解决这个问题的。

## 它不是看板软件，而是一个 AI 任务调度系统

不要被名字骗了。它不是 Trello、Notion 那种项目管理看板——虽然它确实有一块 SQLite 底层的任务看板。

**Hermes Kanban 是一个多智能体任务编排系统。**核心逻辑是：

1. 1. 你把一个大任务拆成多个小任务
2. 2. 每个任务分配一个「AI 工人」（由某个 Hermes profile 扮演）
3. 3. 任务之间可以设置依赖关系（先做 A，再做 B，C 和 D 可以并行）
4. 4. 调度器自动把就绪的任务分配给对应的 profile 去执行
5. 5. 执行结果通过元数据和摘要传递给下游任务

整个过程完全自动化，你只需要把任务拆好、依赖关系定义清楚。

## 核心概念

### Board（看板）

一个 SQLite 数据库文件，存储所有任务和状态。默认在 `~/.hermes/kanban/kanban.db`。可以用 `hermes kanban init`初始化，用 `hermes kanban boards`管理多个看板（一个项目一个看板）。

### Task（任务）

看板上的一个工作项，包含标题、描述、负责人（profile）、状态和可选的父任务依赖。

状态流转：`todo`→ `ready`→ `claimed`（正在执行）→ `done`/ `blocked`。

创建一个任务：

```
hermes kanban create "调研 Postgres 迁移方案" \
  --assignee researcher-profile \
  --body "对比 AWS RDS、Aurora、自建 Postgres 的成本和性能"
```

### Profile（工人配置）

每个 Hermes profile 就像一个 AI 工人，有自己的模型、工具集和技能。你可以配多个 profile：

* • `planner-profile`— 负责拆任务、写计划
* • `researcher-profile`— 负责调研、搜索、分析
* • `developer-profile`— 负责写代码
* • `reviewer-profile`— 负责审查代码

配好了 profile，Kanban 调度器就知道把什么任务派给谁。

### 依赖链（Dependency）

父任务完成后，子任务自动从 `todo`升为 `ready`。通过 `--parent`参数设置：

```
# 先创建父任务
t1=$(hermes kanban create "调研方案A" --assignee researcher-profile --json | jq -r '.task_id')

# 子任务依赖父任务
hermes kanban create "写对比报告" --assignee writer-profile --parent "$t1"
```

## 三种工作模式

### 1. 串行流水线（Pipeline）

适用于有明确的先后顺序：调研 → 实现 → 审查。

```
T1: 调研方案 (researcher) → T2: 实现代码 (developer) → T3: 审查 (reviewer)
```

每个任务 `--parent`指向上一个任务，调度器自动串行。

### 2. 并行扇出（Fan-out + Fan-in）

适用于多个独立调研后汇总。这是 Kanban 最能提效的场景。

```
T1: 调研方案A (researcher) ─┐
T2: 调研方案B (researcher) ─┤→ T4: 对比汇总 (writer)
T3: 调研方案C (researcher) ─┘
```

T1、T2、T3 同时跑，T4 等它们全部完成后自动启动。

### 3. 同 profile 排队

多个任务分配给同一个 profile，调度器会按优先级串行处理。适合一个开发者 profile 接多个小需求。

## 实战：写一篇技术文章

就拿我现在做的事举个例子。我要写这篇介绍 Hermes Kanban 的文章，实际走的是这样一个 Kanban 流程：

```
T1: 查阅 Kanban 文档和源码 (researcher)
      ↓
T2: 撰写文章草稿 (writer)
      ↓
T3: 审核并修正 (reviewer)
      ↓
T4: 发布到 YY的黑板报 (publisher)
```

这就是串行流水线模式。每个任务完成时都会输出 structured metadata——源码改动了哪些文件、调研参考了哪些来源——下游任务可以直接读取，不需要人工传话。

## 调度器怎么工作的

调度器（dispatcher）默认集成在 Hermes Gateway 里。它每隔一段时间扫描一次看板：

1. 1. 找所有状态为 `ready`且没有正在运行的任务
2. 2. 按优先级排序
3. 3. 把任务分配给对应的 profile，派发一个子进程去执行
4. 4. 工人启动后先 `kanban_show`确认状态，然后工作，完成后 `kanban_complete`
5. 5. 如果工人卡住了，可以 `kanban_block`等待人工介入

你不需要手动调度，调度器全自动。

## 工人崩了怎么办

Kanban 有恢复机制。当某个工人持续崩溃、超时或幻觉时，看板会用 ⚠ 标记该任务，并提供三个操作：

| 操作 | 命令 | 场景 |
| --- | --- | --- |
| 回收 | `hermes kanban reclaim <task_id>` | 强行释放被卡住的 worker，让任务回到 ready 状态 |
| 重分配 | `hermes kanban reassign <task_id> <new-profile>` | 换一个 profile 来执行，可能模型更合适 |
| 改模型 | 编辑 profile 配置后 reclaim | 换模型重新试 |

所有恢复操作都有审计日志，方便事后排查。

## Workers 之间的信息传递

这是 Kanban 设计最巧妙的地方——不是靠自然语言传纸条。

每个任务完成时，worker 提交 structured metadata：

```
kanban_complete(
    summary="vLLM throughput 最高，SGLang latency 最低",
    metadata={
        "recommendation": "vLLM",
        "benchmarks": {"vllm": 1.0, "sglang": 0.87, "trtllm": 0.72},
        "sources_read": 12,
    },
)
```

下游任务看到的是格式化的数据，而不是一段需要重新理解的文字。这大幅降低了多轮对话中的信息丢失和幻觉。

## 什么时候该用 Kanban

| 场景 | 用 Kanban | 直接对话 |
| --- | --- | --- |
| 需要多个 specialist 协作 | ✅ | ❌ |
| 任务可能跑很久，中途会中断 | ✅ | ❌ |
| 你想在中间环节介入（加需求/改方向） | ✅ | ❌ |
| 多个子任务可以并行 | ✅ | ❌ |
| 需要审计轨迹 | ✅ | ❌ |
| 问一个简单问题，一步搞定 | ❌ | ✅ |

## 一句话总结

**Hermes Kanban 是把大任务拆成小任务、交给不同 AI 工人并行协作、自动编排依赖关系的多智能体调度系统。**

它不复杂——核心就三样东西：**任务、工人（profile）、依赖链**。知道这三样，你就可以把你的工作流从「单线程聊天」升级成「多智能体流水线」了。

---

如果你对 AI 开发工具和效率系统感兴趣，欢迎关注「YY的黑板报」，我们一起探索技术的乐趣。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/SvuJD1DySG2d6mQWxGEyagnIWESbzcu70bFm0XE7XrypIlcD3ic3MJ28Xibqic0Crfaltk51bVKOibr7Xg0fGASj9Q/0?wx_fmt=png)

YY的黑板报

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/SvuJD1DySG2d6mQWxGEyagnIWESbzcu70bFm0XE7XrypIlcD3ic3MJ28Xibqic0Crfaltk51bVKOibr7Xg0fGASj9Q/0?wx_fmt=png)

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
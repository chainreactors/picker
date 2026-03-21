---
title: Agent开发｜从0实现Agent（二）：深度构建TodoWrite、子Agent任务拆解与Skill体系（规划与协调篇）
url: https://mp.weixin.qq.com/s/yQWLw7Pzoz12O3k5UX4fkA
source: Doonsec's feed
date: 2026-03-20
fetch_date: 2026-03-21T03:59:53.520935
---

# Agent开发｜从0实现Agent（二）：深度构建TodoWrite、子Agent任务拆解与Skill体系（规划与协调篇）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/XkUCeyh2WibianuUBEBlSWn2PggeGITfluAoRmnpZNMEFqHH2IibeOiaXrBI46xdfXsZCoq9ibTBtTj0JhtRG8EGH2YLgia3pdWYcR8ibny0puicHgs/0?wx_fmt=jpeg)

# Agent开发｜从0实现Agent（二）：深度构建TodoWrite、子Agent任务拆解与Skill体系（规划与协调篇）

原创

Real返璞归真
Real返璞归真

Real返璞归真

![]()

在小说阅读器中沉浸阅读

## 公众号

欢迎关注公众号【Real返璞归真】，我们将不定期分享**CTF竞赛、二进制安全、JS/安卓逆向、AI安全**等领域的前沿知识与技术内容。

## 前言

### 简介

> ❝
>
> Agent = LLM + 工具 + 循环
>
> 模型就是智能体，我们的工作就是给它工具，然后让开。

前面两次实验，我们完成了**基础Agent运行**和**工具调用**。

本篇文章将通过3个实验，增强Agent的**规划与协调机制**：

* 加入plan计划清单功能。
* 引入子agent，将复杂的大任务拆分为小任务，以保证上下文干净。
* 引入skill，按需加载调用工具，不再将全部的工具使用说明放到初始的System Prompt。

### 参考资料

learn-claude-code：https://github.com/shareAI-lab/learn-claude-code

> ❝
>
> **12 个递进式课程, 从简单循环到隔离化的自治执行。****每个课程添加一个机制。每个机制有一句格言。**
>
> **s01***"One loop & Bash is all you need"* — 一个工具 + 一个循环 = 一个智能体
>
> **s02***"加一个工具, 只加一个 handler"* — 循环不用动, 新工具注册进 dispatch map 就行
>
> **s03***"没有计划的 agent 走哪算哪"* — 先列步骤再动手, 完成率翻倍
>
> **s04***"大任务拆小, 每个小任务干净的上下文"* — 子智能体用独立 messages[], 不污染主对话
>
> **s05***"用到什么知识, 临时加载什么知识"* — 通过 tool\_result 注入, 不塞 system prompt
>
> **s06***"上下文总会满, 要有办法腾地方"* — 三层压缩策略, 换来无限会话
>
> **s07***"大目标要拆成小任务, 排好序, 记在磁盘上"* — 文件持久化的任务图, 为多 agent 协作打基础
>
> **s08***"慢操作丢后台, agent 继续想下一步"* — 后台线程跑命令, 完成后注入通知
>
> **s09***"任务太大一个人干不完, 要能分给队友"* — 持久化队友 + 异步邮箱
>
> **s10***"队友之间要有统一的沟通规矩"* — 一个 request-response 模式驱动所有协商
>
> **s11***"队友自己看看板, 有活就认领"* — 不需要领导逐个分配, 自组织
>
> **s12***"各干各的目录, 互不干扰"* — 任务管目标, worktree 管目录, 按 ID 绑定

## s03：TodoWrite - Plan Before You Act

> ❝
>
> An agent without a plan drifts; list the steps first, then execute
>
> 没有计划的 Agent 只会漂移；先列出步骤，再开始执行。

### 问题

多步任务中，模型会丢失进度，导致重复进行做过的事、跳步或跑偏。

对话越长越严重：工具结果不断填满上下文, 系统提示的影响力逐渐被稀释。

一个 10 步重构可能做完 1-3 步就开始即兴发挥，因为 4-10 步已经被挤出注意力了。

### 解决方案

```
+--------+      +-------+      +---------+
|  User  | ---> |  LLM  | ---> | Tools   |
| prompt |      |       |      | + todo  |
+--------+      +---+---+      +----+----+
                    ^                |
                    |   tool_result  |
                    +----------------+
                          |
              +-----------+-----------+
              | TodoManager state     |
              | [ ] task A            |
              | [>] task B  <- doing  |
              | [x] task C            |
              +-----------------------+
                          |
              if rounds_since_todo >= 3:
                inject <reminder> into tool_result
```

### 工作原理

![image-20260316182253092](https://mmbiz.qpic.cn/mmbiz_png/XkUCeyh2WibiaDoq81ibuicL7CIDlq2A4q1WoAXh9J9ha5kfOjvNK7v3iaia9cq6OfCDgibheYBEDSV5Vm5veUxTho978YWZknQDPhhdmnZVgUw4CE/640?wx_fmt=png&from=appmsg)

1. 定义`TodoManager`存储带状态的任务，同一时间只允许一个任务`in_progress`：

   ```
   class TodoManager:
       def __init__(self):
           self.items = []

       def update(self, items: list) -> str:
           if len(items) > 20:
               raise ValueError("Max 20 todos allowed")

           validated = []
           in_progress_count = 0

           for i, item in enumerate(items):
               text = str(item.get("text", "")).strip()
               status = str(item.get("status", "pending")).lower()
               item_id = str(item.get("id", str(i + 1)))

               if not text:
                   raise ValueError(f"Item {item_id}: text required")

               if status not in ("pending", "in_progress", "completed"):
                   raise ValueError(f"Item {item_id}: invalid status '{status}'")

               if status == "in_progress":
                   in_progress_count += 1

               validated.append({
                   "id": item_id,
                   "text": text,
                   "status": status
               })

           if in_progress_count > 1:
               raise ValueError("Only one task can be in_progress at a time")

           self.items = validated
           return self.render()

       def render(self) -> str:
           if not self.items:
               return "No todos."

           lines = []
           for item in self.items:
               marker = {
                   "pending": "[ ]",
                   "in_progress": "[>]",
                   "completed": "[x]"
               }[item["status"]]

               lines.append(f"{marker} #{item['id']}: {item['text']}")

           done = sum(1 for t in self.items if t["status"] == "completed")
           lines.append(f"\n({done}/{len(self.items)} completed)")

           return "\n".join(lines)
   ```
2. 增加`todo`工具：

   ```
   TOOL_HANDLERS = {
       # ...base tools...
       "todo": lambda **kw: TODO.update(kw["items"]),
   }
   ```
3. 引入`nag reminder`，模型连续三轮以上不调用todo时注入提示：

   ```
   if rounds_since_todo >= 3 and messages:
       last = messages[-1]
       if last["role"] == "user" and isinstance(last.get("content"), list):
           last["content"].insert(0, {
               "type": "text",
               "text": "<reminder>Update your todos.</reminder>",
           })
   ```
4. 修改系统提示词，引导LLM编写todo清单：

   ```
   SYSTEM = f"""You are a coding agent at {WORKDIR}.
   Use the todo tool to plan multi-step tasks. Mark in_progress before starting, completed when done.
   Prefer tools over prose."""
   ```

### 完整代码

```
#!/usr/bin/env python3
"""
s03_todo_write.py - TodoWrite

The model tracks its own progress via a TodoManager. A nag reminder
forces it to keep updating when it forgets.

    +----------+      +-------+      +---------+
    |   User   | ---> |  LLM  | ---> | Tools   |
    |  prompt  |      |       |      | + todo  |
    +----------+      +---+---+      +----+----+
                          ^               |
                          |   tool_result |
                          +---------------+
                                |
                    +-----------+-----------+
                    | TodoManager state     |
                    | [ ] task A            |
                    | [>] task B <- doing   |
                    | [x] task C            |
                    +-----------------------+
                                |
                    if rounds_since_todo >= 3:
                      inject <reminder>

Key insight: "The agent can track its own progress -- and I can see it."
"""

import os
import subprocess
from pathlib import Path
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv(override=True)

if os.getenv("ANTHROPIC_BASE_URL"):
    os.environ.pop("ANTHROPIC_AUTH_TOKEN", None)

WORKDIR = Path.cwd()
client = Anthropic(base_url=os.getenv("ANTHROPIC_BASE_URL"))
MODEL = os.environ["MODEL_ID"]

SYSTEM = f"""You are a coding agent at {WORKDIR}.
Use the todo tool to plan multi-step tasks. Mark in_progress before starting, completed when done.
Prefer tools over prose."""

# -- TodoManager: structured state the LLM writes to --

class TodoManager:
    def __init__(self):
        self.items = []

    def update(self, items: list) -> str:
        if len(items) > 20:
            raise ValueError("Max 20 todos allowed")

        validated = []
        in_progress_count = 0

        for i, item in enumerate(items):
            text = str(item.get("text", "")).strip()
            status = str(item.get("status", "pending")).lower()
            item_id = str(item.get("id", str(i + 1)))

            if not text:
                raise ValueError(f"Item {item_id}: text required")

            if status not in ("pending", "in_progress", "completed"):
                raise ValueError(f"Item {item_id}: invalid status '{status}'")

            if status == "in_progress":
                in_progress_count += 1

            validated.append({
                "id": item_id,
                "text": text,
                "status": status
            })

        if in_progress_count > 1:
            raise ValueError("Only one task can be in_progress at a time")

        self.items = validated
        return self.render()

    def render(self) -> str:
        if not self.items:
            return "No todos."

        lines = [...
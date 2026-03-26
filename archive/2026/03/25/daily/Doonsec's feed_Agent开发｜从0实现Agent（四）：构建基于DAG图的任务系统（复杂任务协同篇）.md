---
title: Agent开发｜从0实现Agent（四）：构建基于DAG图的任务系统（复杂任务协同篇）
url: https://mp.weixin.qq.com/s/g9EtWtWA_TuEWhmaS_wIGw
source: Doonsec's feed
date: 2026-03-25
fetch_date: 2026-03-26T04:26:56.307914
---

# Agent开发｜从0实现Agent（四）：构建基于DAG图的任务系统（复杂任务协同篇）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/XkUCeyh2Wibia9wMPibDvc5nRjRozgHFicH54xrm5ZicNIDv3E41G4Atqm3RUSNASibQXEWgw1ogFibibk826B1OBO8blAZHDXJyN3zOFhl3hsxYKRA/0?wx_fmt=jpeg)

# Agent开发｜从0实现Agent（四）：构建基于DAG图的任务系统（复杂任务协同篇）

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

前面三次实验，我们完成了**基础Agent运行**、**工具调用**、**任务规划**、**SKill封装**和**上下文压缩**。

本篇文章将通过1个实验，实现更完善的基于DAG图的Agent任务系统。

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

## s07：任务系统 - Task Graph + Dependencies

> ❝
>
> A file-based task graph with ordering, parallelism, and dependencies -- the coordination backbone for multi-agent work
>
> 基于文件的任务图，具备排序、并行和依赖管理——多智能体工作的协调核心。

### 问题

s03 的 `TodoManager` 只是内存中的扁平清单: 没有顺序、没有依赖，状态只有是否完成。

真实目标是有结构的 — 任务 B 依赖任务 A，任务 C 和 D 可以并行，任务 E 要等 C 和 D 都完成。

没有显式的关系，智能体分不清什么能做、什么被卡住、什么能同时跑。而且清单只活在内存里，上下文压缩 (s06) 以后就没了。

### 解决方案

把扁平清单升级为持久化到磁盘的任务图。每个任务是一个 JSON 文件，有状态、前置依赖 (blockedBy) 和后置依赖 (blocks)。

任务图随时回答三个问题:

* 什么可以做？状态为 pending 且 blockedBy 为空的任务。
* 什么被卡住？等待前置任务完成的任务。
* 什么做完了？状态为 completed 的任务, 完成时自动解锁后续任务。

```
.tasks/
  task_1.json  {"id":1, "status":"completed"}
  task_2.json  {"id":2, "blockedBy":[1], "status":"pending"}
  task_3.json  {"id":3, "blockedBy":[1], "status":"pending"}
  task_4.json  {"id":4, "blockedBy":[2,3], "status":"pending"}

任务图 (DAG):
                 +----------+
            +--> | task 2   | --+
            |    | pending  |   |
+----------+     +----------+    +--> +----------+
| task 1   |                          | task 4   |
| completed| --> +----------+    +--> | blocked  |
+----------+     | task 3   | --+     +----------+
                 | pending  |
                 +----------+

顺序:   task 1 必须先完成, 才能开始 2 和 3
并行:   task 2 和 3 可以同时执行
依赖:   task 4 要等 2 和 3 都完成
状态:   pending -> in_progress -> completed
```

这个任务图是 s07 之后所有机制的协调骨架：后台执行 (s08)、多 agent 团队 (s09+)、worktree 隔离 (s12) 都读写这同一个结构。

### 工作原理

![image-20260317100036994](https://mmbiz.qpic.cn/sz_mmbiz_png/XkUCeyh2WibiaTZX6xKsgvXU4U2MukPJvTaEibNnmnoYVa5gaf2Prjzddpd53WEwwHicacibb5YGNHCLlqQrRlW0ZrzdxNUqe8ygBNLybzIibWSFA/640?wx_fmt=png&from=appmsg)

1. 修改`TaskManager`，每个任务一个 JSON 文件，定义CRUD + 依赖图：

   ```
   class TaskManager:
       def __init__(self, tasks_dir: Path):
           self.dir = tasks_dir
           self.dir.mkdir(exist_ok=True)
           self._next_id = self._max_id() + 1

       def create(self, subject, description=""):
           task = {"id": self._next_id, "subject": subject,
                   "status": "pending", "blockedBy": [],
                   "blocks": [], "owner": ""}
           self._save(task)
           self._next_id += 1
           return json.dumps(task, indent=2)
   ```
2. 定义依赖解除功能，完成任务时，自动将其 ID 从其他任务的 blockedBy 中移除，解锁后续任务：

   ```
   def _clear_dependency(self, completed_id):
       for f in self.dir.glob("task_*.json"):
           task = json.loads(f.read_text())
           if completed_id in task.get("blockedBy", []):
               task["blockedBy"].remove(completed_id)
               self._save(task)
   ```
3. 状态变更 + 依赖关联，使用update 处理状态转换和依赖边：

   ```
   def update(self, task_id, status=None,
              add_blocked_by=None, add_blocks=None):
       task = self._load(task_id)
       if status:
           task["status"] = status
           if status == "completed":
               self._clear_dependency(task_id)
       self._save(task)
   ```
4. 将四个任务工具加入`dispatch map`：

   ```
   TOOL_HANDLERS = {
       # ...base tools...
       "task_create": lambda **kw: TASKS.create(kw["subject"]),
       "task_update": lambda **kw: TASKS.update(kw["task_id"], kw.get("status")),
       "task_list":   lambda **kw: TASKS.list_all(),
       "task_get":    lambda **kw: TASKS.get(kw["task_id"]),
   }
   ```

   从 s07 起, 任务图是多步工作的默认选择。s03 的 Todo 仍可用于单次会话内的快速清单。

### 完整代码

```
#!/usr/bin/env python3
"""
s07_task_system.py - Tasks

Tasks persist as JSON files in .tasks/ so they survive context compression.

Each task has a dependency graph (blockedBy/blocks).

    .tasks/
      task_1.json  {"id":1, "subject":"...", "status":"completed", ...}
      task_2.json  {"id":2, "blockedBy":[1], "status":"pending", ...}
      task_3.json  {"id":3, "blockedBy":[2], "blocks":[], ...}

    Dependency resolution:

    +----------+     +----------+     +----------+
    | task 1   | --> | task 2   | --> | task 3   |
    | complete |     | blocked  |     | blocked  |
    +----------+     +----------+     +----------+

         |
         +--- completing task 1 removes it from task 2's blockedBy

Key insight: "State that survives compression -- because it's outside the conversation."
"""

import json
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
TASKS_DIR = WORKDIR / ".tasks"

SYSTEM = f"You are a coding agent at {WORKDIR}. Use task tools to plan and track work."

# -- TaskManager: CRUD with dependency graph, persisted as JSON files --

class TaskManager:

    def __init__(self, tasks_dir: Path):
        self.dir = tasks_dir
        self.dir.mkdir(exist_ok=True)
        self._next_id = self._max_id() + 1

    def _max_id(self) -> int:
        ids = [int(f.stem.split("_")[1]) for f in self.dir.glob("task_*.json")]
        return max(ids) if ids else 0

    def _load(self, task_id: int) -> dict:
        path = self.dir / f"task_{task_id}.json"
        if not path.exists():
            raise ValueError(f"Task {task_id} not found")
        return json.loads(path.read_text())

    def _save(self, task: dict):
        path = self.dir / f"task_{task['id']}.json"
        path.write_text(json.dumps(task, indent=2))

    def create(self, subject: str, description: str = "") -> str:
        task = {
            "id": self._next_id,
            "subject": subject,
            "description": description,
            "status": "pending",
            "blockedBy": [],
            "blocks": [],
            "owner": "",
        }
        self._save(task)
        self._next_id += 1
        return json.dumps(task, indent=2)

    def get(self, task_id: int) -> str:
        return json.dumps(self._load(task_id), indent=2)

    def update(
        self,
        task_id: int,
        status: str = None,
        add_blocked_by: list = None,
        add_blocks: list = None,
    ) -> str:

        task = self._load(task_id)

        if status:
            if status not in ("pending", "in_progress", "completed"):
                raise ValueError(f"Invalid status: {status}")

            task["status"] = status

            if status == "completed":
                self._clear_dependency(task_id)

        if add_blocked_by:
            task["blockedBy"] = list(set(task["blockedBy"] + add_blocked_by))

        if add_blocks:
            task["blocks"] = list(set(task["blocks"] + add_blocks))

            for blocked_id in add_blocks:
                try:
                   ...
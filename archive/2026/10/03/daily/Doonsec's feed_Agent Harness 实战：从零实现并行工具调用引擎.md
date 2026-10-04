---
title: Agent Harness 实战：从零实现并行工具调用引擎
url: https://mp.weixin.qq.com/s/dE2qVwbptBwgz6gkdc565w
source: Doonsec's feed
date: 2026-10-03
fetch_date: 2026-10-04T07:36:24.036598
---

# Agent Harness 实战：从零实现并行工具调用引擎

# Agent Harness 实战：从零实现并行工具调用引擎

原创

Z
Z

威胁情报Z分析

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

|  |
| --- |
| 本文目标：讲清楚一个能在生产用的 Agent 运行时（Harness）里，"并行工具调用引擎"到底由哪几块组成、为什么必须按 DAG 调度、关键代码怎么写。读完你可以直接照抄一个 200 行以内的 Python asyncio 最小引擎，并理解为什么 OpenAI / Anthropic 把 parallel tool calls 做成一等公民。 |

一、为什么必须做并行工具调用

绝大多数人第一次写 Agent，用的都是最朴素的 ReAct 循环：LLM 决定调一个工具 → 等它返回 → 把结果塞回上下文 → 再问 LLM。这个模型在工具少、时延低的时候没问题，但一旦工具数上来，端到端时延就变成所有工具延迟之和。

真实 Agent 一次用户请求往往要调多个工具：查天气、搜新闻、读文件、跑计算器、写库——其中大部分彼此没有数据依赖。串行调用等于让用户干等 N 次网络往返，而这些往返本可以在一个事件循环里同时飞出去。

并行工具调用引擎要解决的不是"能不能并发"这种操作系统问题，而是这三件更难的事：

1依赖识别：LLM 一次吐出 N 个工具调用，引擎怎么知道哪些能并行、哪些必须等前面的结果？

1调度执行：怎么在不打爆下游 API、不打爆自己事件循环的前提下，把无依赖的工具同时发出去？

1失败隔离：一个工具超时或炸了，不能拖垮整轮；要让 LLM 看到 error 而不是整个会话崩溃。

二、整体架构：五层各司其职

整个引擎在概念上可以拆成五层。规划层负责让 LLM 说清楚要调什么；调度层把这堆调用编译成可执行的依赖图；执行层真正并发跑工具；收敛层把结果整理回上下文，再决定是继续问 LLM 还是结束。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0LGiaGIrzXulVAuu7ZpNHten0jdmkja9fiamP0TrpXrO3UZgeeiciaaU9ua7efFvPVLnibRy9QGrYrk3LlouvrvMdyww1MiaVOFh8uL8u6lg5TSy0/640?wx_fmt=png&from=appmsg)

几个容易踩坑的点：

1Planner 不直接负责执行。LLM 输出的是一个"计划"（一组 tool\_call，每个带 depends\_on），Harness 负责把它编译成 DAG 而不是逐条 await。

1调度层必须有环检测。LLM 偶尔会输出"A 依赖 B、B 又依赖 A"的计划，这一步必须在执行前拒绝并回喂 LLM，不能带着环跑。

1执行层用信号量而非无脑 gather。一次吐 20 个工具、每个都打 HTTP，不加并发上限会直接把对方限流掉。

三、一次 Turn 的状态机

把视角收敛到"一次用户请求"内部，引擎其实是一个状态机：从用户输入出发，要么走到"输出最终回答"结束，要么进入"工具执行 → 结果回灌 → 再问 LLM"的循环，直到 LLM 不再要求调工具为止。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0LGiaGIrzXumtRwx35PoKgcic5KGSGicDByBwP19trj00OL9GbVIzib5TQOL6tD6qT8Z7E4a9iclA5yWxZHXxBdEAFIxPNjTvCxyfy02xhFhApMQ/640?wx_fmt=png&from=appmsg)

关键设计点是循环边界在 LLM 这一侧，不在工具层。引擎不知道"什么时候算够了"，它只知道"LLM 这一轮还要不要继续调工具"。这种边界划分让引擎本身保持很薄，所有策略（什么时候停、要不要重试）都能通过 prompt 或外层 system message 调，不用改调度代码。

四、DAG 调度核心：把工具列表变成可并行执行的图

调度层最核心的数据结构是一张有向无环图（DAG）。节点是工具调用，边是"我必须等你出结果才能跑"。拓扑排序之后，同一层的节点之间没有依赖，可以一次性并发飞出去；下一层节点必须等上一层全部 settle。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0LGiaGIrzXulfc2wu6GtYIxwwtyZbgSNhCzE5XHCKDL7oZnSIqxGlhBCCyQSWQ9CJYoElFhCbNdUmgqfdsnHrWljddHqjn3lrxDOcj9110Hk/640?wx_fmt=png&from=appmsg)

这套调度带来两个直接结论：

1端到端时延由关键路径决定，而不是工具总数。本例中工具总数 4 个、串行要 4s；DAG 调度后关键路径 3 层共 3s。工具再多，只要每层内可并行，时延就是"层数 × 单层最大耗时"。

1依赖关系是 LLM 写出来的，不是引擎猜的。这要求工具 schema 里要么让 LLM 显式输出 depends\_on，要么由 Harness 静态分析参数里是否引用了上游 tool\_call 的结果。OpenAI 风格是后者：模型在 args 里写 ${tool\_call\_3.result}，Harness 做字符串替换时顺带建边。

五、关键设计决策

|  |  |  |
| --- | --- | --- |
| 决策点 | 做法 | 为什么 |
| 并发上限 | asyncio.Semaphore(N)，N 默认 5~10 | 防打爆下游、防自己 fd 耗尽；N 按下游限流配置调 |
| 单工具超时 | asyncio.wait\_for(tool(...), timeout=10) | 一个工具 hang 住不能拖死整轮；超时结果作为 error 喂回 LLM |
| 失败策略 | 默认不重试；可重试错误（429/5xx）指数退避 2 次；其他错误直接落 error\_result | LLM 看到错误信息后可以自己决定换个参数再调一次 |
| 错误传播 | 依赖该工具的下游节点自动收到 error\_dependency\_failed，不强行执行 | 避免拿半成品算半天，结果上游就错了 |
| 结果回灌格式 | 每个 tool\_call 对应一条 tool 角色消息，带 tool\_call\_id 关联 | 对齐 OpenAI / Anthropic 的协议，LLM 才能把结果对上当初的调用 |
| 最大轮次 | 硬性 cap（如 10 轮），超过直接截断并告诉 LLM | 防止 LLM 陷入"调工具-看结果-再调同一个"的死循环烧 token |

六、代码实现：一个 200 行的最小引擎

下面是完整可运行的 Python 实现，只用标准库 asyncio。它包含工具注册、DAG 构建、拓扑并行调度、超时与错误隔离，最后用一个多工具查询场景跑通。

6.1 工具注册与调用计划

|  |
| --- |
| python                   tools.py —— 工具注册表与装饰器                   import asyncio                   import time                   from dataclasses import dataclass, field                   from typing import Any, Callable                    @dataclass                   class ToolCall:                       id: str                       # 例如 "call\_1"                       name: str                     # 工具名                       args: dict                    # 参数（已替换好上游引用）                       depends\_on: list[str] = field(default\_factory=list)                    @dataclass                   class ToolResult:                       call\_id: str                       name: str                       ok: bool                       value: Any = None             # 成功时的返回值                       error: str | None = None      # 失败时的错误信息                    class ToolRegistry:                       def \_\_init\_\_(self):                           self.\_fns: dict[str, Callable] = {}                           self.\_schemata: list[dict] = []                        def register(self, name: str, description: str, parameters: dict):                           def deco(fn):                               self.\_fns[name] = fn                               self.\_schemata.append({                                   "type": "function",                                   "function": {"name": name, "description": description,                                                "parameters": parameters},                               })                               return fn                           return deco                        async def invoke(self, name: str, args: dict, timeout: float = 10.0) -> Any:                           fn = self.\_fns[name]                           return await asyncio.wait\_for(fn(\*\*args), timeout=timeout) |

6.2 DAG 构建与分层调度

|  |
| --- |
| python                   scheduler.py —— 拓扑分层 + 并发执行                   async def run\_plan(registry: ToolRegistry,                                      plan: list[ToolCall],                                      max\_concurrency: int = 5) -> dict[str, ToolResult]:                       # 1) 建图：统计每个节点的入度 & 后继                       by\_id = {c.id: c for c in plan}                       indeg = {c.id: len(c.depends\_on) for c in plan}                       successors: dict[str, list[str]] = {c.id: [] for c in plan}                       for c in plan:                           for dep in c.depends\_on:                               if dep not in by\_id:                                   raise ValueError(f"{c.id} 依赖不存在的 {dep}")                               successors[dep].append(c.id)                        # 2) 环检测：拓扑排序后若仍有剩余节点，就是有环                       order, ready = [], [cid for cid, d in indeg.items() if d == 0]                       while ready:                           cid = ready.pop()                           order.append(cid)                           for nxt in successors[cid]:                               indeg[nxt] -= 1                               if indeg[nxt] == 0:                                   ready.append(nxt)                       if len(order) != len(plan):                           raise ValueError("工具调用计划存在循环依赖")                        # 3) 按层执行：每一层内部并发                       sem = asyncio.Semaphore(max\_concurrency)                       results: dict[str, ToolResult] = {}                       done = set()                        while len(done) < len(plan):                           layer = [c for c in plan                                    if c.id not in done and all(d in done for d in c.depends\_on)]                           if not layer:                               break  # 兜底，正常已被环检测拦住                            async def run\_one(call: ToolCall) -> ToolResult:                               async with sem:                                   # 上游若失败，本节点不执行，直接标记依赖失败                                   failed\_upstream = next((results[d] for d in call.depends\_on                                                           if not results[d].ok), None)                                   if failed\_upstream:                                       return ToolResult(call.id, call.name, ok=False,                                                         error=f"依赖 {failed\_upstream.call\_id} 失败")                                   t0 = time.perf\_counter()                                   try:                                       value = await registry.invoke(call.name, call.args)                                       return ToolResult(call.id, call.name, ok=True, value=value)                                   except Exception as e:                                       return ToolResult(call.id, call.name, ok=False, error=str(e))                                   finally:                                       print(f"  [{time.perf\_counter()-t0:5.2f}s] {call.name} done")                            for r in await asyncio.gather(\*(run\_one(c) for c in layer)...
---
title: 智能体协作的三条路线：Subagent、Agent Teams 与 Swarm
url: https://mp.weixin.qq.com/s/d9IHLMTGOAy1d7WIEMOfXQ
source: Doonsec's feed
date: 2026-11-27
fetch_date: 2026-11-28T09:37:13.321007
---

# 智能体协作的三条路线：Subagent、Agent Teams 与 Swarm

# 智能体协作的三条路线：Subagent、Agent Teams 与 Swarm

原创

APT-101
APT-101

APT-101

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

同时跑起十个 Agent，和让十个 Agent 组成一个团队，是两件完全不同的事。前者一个循环开十个会话就够了；后者得操心任务怎么分、消息怎么传、做完谁来验收。

Google Antigravity 内置了一个 /swarm 功能，可以让多个 Agent 像开发团队一样分工、通信、并行执行、交叉验证。把它和 Codex 的 Subagents、Claude Code 的 Agent Teams 放在一起看，三家都在解决多 Agent 协作，但在任务调度、通信机制和生命周期管理上走出了三条不同的路线。

先说结论：三者不是谁替代谁，Swarm 也不是彻底去中心化的架构。真正值得关注的，是它们如何组织任务、传递信息，以及如何判断整个团队已经完成了工作。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PIWj1VguNovuouUgBYe7JolW2d1ow5U9Y3JsW2Yk1RSkqtXXPeGuTTdMFjR4n8KRZ1fp0EtaglnhmaLGVRTSBWBUWlKmricFgN2ABMEOHzwU/640?wx_fmt=png&from=appmsg)

 图1 三条路线：Codex 层级委派 / Claude Code 共享任务 / Antigravity Swarm 共享消息板与独立验证

## 一、Codex Subagents：层级式任务委派

Codex 的多 Agent 协作以经典的层级式委派为基础。主 Agent 负责理解需求、拆解任务，创建拥有独立上下文的子 Agent，向它们下发任务、追加指令、等待结果，最后汇总交付。

Multi-Agent V1 里，这套协作靠几个核心工具串联：

| 工具 | 职责 |
| --- | --- |
| spawn\_agent | 创建子 Agent |
| send\_input | 向已有 Agent 发送指令 |
| wait\_agent | 等待执行结果 |
| resume\_agent / close\_agent | 恢复或关闭 Agent |

最新公开源码中的 Multi-Agent V2 开始把消息传递和任务调度解耦，并用层级化的 Task Path 标识不同 Agent。send\_message 只负责投递消息，不会直接开启新的执行轮次；followup\_task 负责向已有 Agent 分配后续任务，并在必要时重新启动执行。V2 还引入了 Mailbox 消息等待、Agent 列表查询和执行中断（具体工具是否可用取决于模型和运行时配置）。

Codex 还支持给不同角色配不同的模型、推理强度和沙箱策略：成本低的模型跑代码搜索，复杂逻辑和代码审查交给更强的。

它正在从父子任务委派扩展到更灵活的通信与生命周期管理，适合代码库探索、并行审查这类相对独立的子任务。

## 二、Claude Code Agent Teams：共享任务列表加收件箱

Claude Code 的 Agent Teams 在独立会话之上，引入了两个关键组件：Shared Task List（共享任务列表）和 Mailbox（收件箱）。

整个团队由四部分组成：

* **Team Lead**：组建团队、拆解任务、汇总结果
* **Teammates**：拥有独立会话和上下文的团队成员
* **Task List**：维护共享任务的状态、归属和依赖关系
* **Mailbox**：成员之间的消息传递

启用 Task 系列工具后，成员完成当前任务，可以主动去共享列表里认领尚未分配、且没有依赖阻塞的新任务。并发认领的竞争由 File Locking（文件锁）处理，前置任务一完成，下游依赖自动解除阻塞。

每个成员有一个独立的 JSON 收件箱：

```
~/.claude/teams/{team-name}/inboxes/{agent-name}.json
```

成员通过 SendMessage 直接向其他 Agent 发消息，不必所有信息都经过 Team Lead 转述。前端 Agent 发现后端接口缺少字段，直接找后端 Agent 协商修改就行。配合 TeammateIdle、TaskCreated、TaskCompleted 等 Hooks，测试和静态检查可以接入任务生命周期，不达标直接阻止任务完成。

还有两处细节：新版 Claude Code 中，普通具名 Subagent 其实也能直接通信；部分较新模型默认不提供 Task 系列工具，团队成员就直接靠消息协调。

所以 Agent Teams 的核心不只是让 Agent 能互相发消息，而是把独立会话、成员管理、任务状态和质量控制整合成了一套完整机制。目前它仍处于 Experimental 阶段。

## 三、Antigravity Swarm：共享消息板与独立验证

Antigravity 的 /swarm 采用了另一种思路。启动 Swarm 后，当前会话变成 Coordinator（协调者），负责划定任务边界、创建 Worker、分配职责和验收结果，具体技术工作交给团队成员执行。

每个 Worker 同样有独立会话和上下文，但与 Claude Code 的独立 Mailbox 不同，Swarm 用的是一个公开的 Shared Message Board（共享消息板）。任务范围、禁止修改的内容、完成标准，以及成员间的提问、代码变更摘要和测试结果，都按顺序发布在同一个消息板上。成员之间通过 @name、@group、@all 公开交流，没有私下传话，整个协作过程对团队和用户完全可见。

三个机制拆开看：

**Sleep & Wake（事件驱动的休眠与唤醒）。** Worker 没有任务或正在等回复时进入休眠，期间不消耗模型 Token；被其他成员 @ 提及时自动唤醒继续执行。避免了 Agent 为了等消息反复空转调用模型。

**Verifier（独立验证机制）。** Coordinator 通常按每 2 到 4 个 Worker 配一个 Verifier 的比例，专门检查代码变更、运行测试，把发现的问题反馈给对应 Worker 修复。Worker 和 Verifier 还可以使用不同模型，实现跨模型的代码审查。

**Monitor（协作停滞监控）。** 当整个团队都进入等待状态、但任务还没完成时，Monitor 主动介入发消息唤醒相关成员，推动任务继续执行。

工作区默认共享，也可以给多个 Worker 分配独立的仓库副本（Git Worktree 隔离），减少并行改代码的冲突。它还提供 Graph 视图，能看到 Agent 之间的通信关系，也能回放整个团队的消息交互过程。过去只能看到 Agent 最终交付了什么，现在连它们如何讨论、协商、验证和修复问题，也变得可观测。

![](https://mmbiz.qpic.cn/mmbiz_png/PIWj1VguNosMLfA9BZmJkibYkRxSIOR8l6JTYe57aQ1iaf6FmKKzW1W8UWm4gTZe6c3CSCqoR5zIwzMa6WSLramwtvdsnYmdicc9tLWUuzibEHU/640?wx_fmt=png&from=appmsg)

图2 三种架构对照：组织形态、任务分配、通信机制、质量控制的四个切面

## 四、三条路线差在哪

| 维度 | Codex Subagents | Claude Code Agent Teams | Antigravity Swarm |
| --- | --- | --- | --- |
| 组织形态 | 主 Agent 父子委派 | Team Lead + Teammates | Coordinator + Worker + Verifier |
| 任务分配 | 下发 + followup\_task | 共享列表自主认领 | Coordinator 分派并验收 |
| 通信 | Mailbox / 消息投递 | 独立 JSON 收件箱 | 共享消息板，全程公开 |
| 调度 | 等待 / 恢复 / 中断 | 文件锁 + 依赖自动解除 | Sleep & Wake 事件驱动 |
| 质量控制 | 分角色配强模型审查 | Hooks 卡任务完成 | 独立 Verifier，跨模型验证 |
| 阶段 | V2 源码公开 | Experimental | Preview |

三家的重心一眼能分出来：Codex 偏重层级化任务委派与子 Agent 生命周期管理；Claude Code 偏重共享任务状态、自主认领和成员通信；Swarm 偏重共享消息板、事件驱动调度、独立验证和停滞监控。

三者不是谁取代谁的关系。Swarm 里依然有 Coordinator 负责整体协调，谈不上彻底去中心化。Antigravity 自己也同时保留了 Subagents、Swarm、Boost 和 Teamwork 等模式，分别对应独立子任务、并行开发、复杂问题的反复验证和长周期项目。**不同类型的任务需要不同的 Agent 组织方式，并不是所有事都值得拉起一个蜂群。**

## 五、撞上的都是分布式系统的老问题

上一篇把 Agent 编排系统类比成操作系统，从 Subagent、Agent Teams 一路看到 Swarm，会发现多 Agent 协作触及的几乎全是分布式系统里的经典设计：

| Agent 机制 | 分布式系统原型 |
| --- | --- |
| Subagent 委派 | 层级式任务调度 |
| Mailbox | 点对点消息传递 |
| Shared Message Board | 共享消息日志 |
| Shared Task List | 共享任务队列 |
| File Locking | 并发控制 |
| Sleep & Wake | 事件驱动调度 |
| Git Worktree | 工作空间隔离 |
| Verifier | 独立质量验证 |
| Monitor | 系统活性监控 |

![](https://mmbiz.qpic.cn/mmbiz_png/PIWj1VguNou9qqLiaSYp8r65IjRZ2e636RN7fVWqUKp419P6BOg3OS7XofQJWx1MRribWCQQztZrxdicBvGgj9DiaZ6uvnu0JWm9lbXvMs1HLNE/640?wx_fmt=png&from=appmsg)

 图3 Agent 机制与分布式系统原型一一对应；三个“不代表”是集成前必须过的检查

随着 Agent 数量增加，通信开销、资源竞争、状态一致性、任务依赖和故障恢复这些老问题会逐一冒出来。三个"不代表"不能想当然：任务认领加了锁，不代表代码修改实现了互斥；拥有独立的上下文窗口，不代表拥有独立的文件系统；多个 Worker 都汇报任务完成，也不代表集成后的代码能通过测试。

一旦任务依赖没正确解除，或者所有 Agent 都在互相等待回复，整个团队甚至可能直接陷入协作停滞。这些难题现在都还没被彻底解决：Agent Teams 处于 Experimental，Swarm 处于 Preview。

而且多 Agent 从来不是越多越好。面对高度耦合的任务，盲目增加 Agent 只会带来更高的通信开销、重复推理和 Token 消耗。

除了模型本身的能力和 Agent Harness 的打磨，如何组织多个拥有独立上下文、工具和推理能力的 Agent，并以可控成本实现可靠协作，正在成为 Coding Agent 非常关键的竞争方向。

让十个 Agent 同时写代码，和让十个 Agent 共同交付一个完整的项目，是两件完全不同的事。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PIWj1VguNosxzTqjClxKlIhyh62PQ5oNxv38uWibia6C8du1n2ews9CFWiaAQQeN1MCuEibZOwocJxl3dcuEIBHz1mZpRazz1B9Y8xcrObbtBCc/640?wx_fmt=png&from=appmsg)

图4 一张图回顾全文：三条路线的分工、通信与验收，以及它们撞上的分布式老问题

#CodingAgent #AI编程 #多智能体 #Subagent #Swarm #AgentTeams

预览时标签不可点

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/vgGymHXkYlHxHm5eWcF04Jiak4wbaPHuibiaRpMSS9cibMpn8zszwAmT9Oc2YYhJN1nowIDPnEgAddjclhcuDOaZtQ/0?wx_fmt=png)

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
推荐
，轻点两下取消推荐
分享
留言
收藏
听过
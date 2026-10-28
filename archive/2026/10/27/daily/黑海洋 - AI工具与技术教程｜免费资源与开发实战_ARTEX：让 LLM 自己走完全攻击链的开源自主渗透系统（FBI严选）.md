---
title: ARTEX：让 LLM 自己走完全攻击链的开源自主渗透系统（FBI严选）
url: https://blog.upx8.com/ARTEX-LLM
source: 黑海洋 - AI工具与技术教程｜免费资源与开发实战
date: 2026-10-27
fetch_date: 2026-10-28T07:48:02.376479
---

# ARTEX：让 LLM 自己走完全攻击链的开源自主渗透系统（FBI严选）

[![黑海洋](https://blog.upx8.com/logo.webp)
黑海洋
WIKI](https://blog.upx8.com/)

[首页](https://blog.upx8.com/)
[资源](https://blog.upx8.com/Free)
[安全](https://blog.upx8.com/os_security)
[开发](https://blog.upx8.com/code)
[资讯](https://blog.upx8.com/news)
[关于](/about.html)

在线工具

[极

**极简文本**
*txt.upx8.com*](https://txt.upx8.com/)
[I

**IP查询**
*ip.upx8.com*](https://ip.upx8.com/)
[哈

**哈希计算**
*blog.upx8.com*](https://blog.upx8.com/app/bs64/#hash)
[U

**USTD交易查询**
*18u.in*](https://18u.in)
[三

**三角洲辅助站**
*sjz.upx8.com*](https://sjz.upx8.com/)
[开

**开发者工具箱**
*tools.upx8.com*](https://tools.upx8.com/)

[首页](https://blog.upx8.com)
/
[安全](https://blog.upx8.com/os_security)
/
ARTEX：让 LLM 自己走完全攻击链的开源自主渗透系统（FBI严…

# ARTEX：让 LLM 自己走完全攻击链的开源自主渗透系统（FBI严选）

[安全](https://blog.upx8.com/os_security)
10-27
·
约 28 分钟
·
黑海洋
·

5,242
·
[1 条评论](#comments)

## ![ARTEX：让 LLM 自己走完全攻击链的开源自主渗透系统（FBI严选）](https://pic1.imgdb.cn/i/034mzCaE0WqI1nlgLFzAYc.png)

## 一、先给结论：它是什么，解决什么问题

ARTEX 是一套 **LLM 多 agent 驱动的自主渗透测试系统**。技术栈是 **Go 单体后端 + 内嵌 Next.js 前端（go:embed 打进同一个二进制）+ PostgreSQL**，Agent 能力由 `norma` SDK 提供（`agentcore` / `tool` / `permission` / `harness` / `memory` / `transcript`）。

一句话区分它和市面上其它工具：

* 传统扫描器（nuclei / xray / AWVS）：你给它一个域名，它按 POC 库打一轮，出一份报告。**流程是固定的。**
* 普通 AI 助手 + 工具：你一句我一句，**上下文一长就跑偏，走不了多步依赖链**。
* ARTEX：你划一个资产范围，系统自己派 planner 判断下一步该测什么，派 worker 去真机执行 Kali 命令 / Bash / HTTP，把结果写回图谱，再唤醒 planner 继续判断 —— **直到目标被证明或者没有新方向**。

它真正下功夫的地方不是"能调 LLM 跑命令"，而是解决了一个所有 Agent 系统都会撞上的工程难题：**事件驱动 + 每次唤醒都是全新会话，怎么保证一条有前后依赖的攻击链（发现注入点 → 取凭据 → 横向 → 提权）不乱序、不重复、不半路丢失。**

答案就是下面这套双图架构。

---

## 二、核心机制：理解这四个点，才算真懂 ARTEX

### 2.1 双图架构：把"目标是什么"和"测到什么程度"拆开

系统里有两张图，物理上都在 PostgreSQL，但语义完全独立：

| 图 | 范围 | 节点类型 | 回答什么 |
| --- | --- | --- | --- |
| **资产图** Asset Graph | **全局共享，跨任务同一份** | `root_domain` / `subdomain` / `ip` / `service` / `app` / `endpoint` | 目标世界长什么样 |
| **探索图** Exploration Graph | **每任务独立** | `goal` / `intent` / `fact` / `finding` / `hint` | 这次任务是怎么想、怎么推进的 |

探索图内部的边是**血缘链**：`spawns`（目标派生意图）、`derived_from`（事实派生新意图）、`yields`（意图产出事实）、`proves`（意图证实漏洞）。所以任何一个漏洞，都能往前倒推"它是从哪条事实、哪个意图一路派生出来的"。

两张图靠 **锚点表** `exploration_anchors(node_id, asset_id)` 连接。这一步是整个设计的枢纽：

* 从探索方向看：这条意图打的是哪些资产；
* 从资产反查：这个 endpoint 在本任务被哪些意图测过、得出过哪些事实。

于是"**资产测试覆盖度**"和界面里那张力导向的**资产覆盖图**（已测节点高亮）才成立。

```
flowchart LR
  subgraph EG["探索图（每任务独立 · 推进链）"]
    G["goal 目标"] -->|spawns| I1["intent 意图A"]
    I1 -->|yields| F1["fact 事实"]
    F1 -->|derived_from| I2["intent 意图B"]
    I2 -->|proves| FD["finding 漏洞"]
  end
  subgraph AG["资产图（全局共享 · 真值库）"]
    RD["root_domain"] --> SD["subdomain"] --> SV["service"] --> EP["endpoint"]
  end
  I1 -.anchor.-> SD
  F1 -.anchor.-> SV
  FD -.anchor.-> EP
```

一个容易忽略的工程取舍：**资产图的父子关系和去重 key 全部由程序计算，agent 只准提交原始信息**。这样做是因为 LLM 生成的资产关系必然有幻觉，让模型去算域名归属会污染整张真值库。

### 2.2 引擎闭环：图一变就唤醒 planner

引擎结构很简单：**每个任务一个 `plannerLoop` + N 个 worker goroutine**。N 就是「系统设置」里的 work agent 数量，默认 3。

闭环是这样转的：

1. worker 写回 fact / asset / finding，触发图变更（带 debounce 防抖）；
2. 引擎唤醒 planner；
3. planner 读态势（`graph_overview` 预取 + coverage/scope），派 0..N 条**意图**进 frontier 队列；
4. worker `claimNext` 领一条意图，取它 `asset_ids` 对应的原始资产作为初始信息；
5. worker 用真实工具（Kali / Bash / HTTP）执行，全程经记录代理留痕；
6. 结果写回双图 + 每步 activity，回到第 1 步。

关键细节：**大多数唤醒派 0 条意图**。这不是 bug，是收敛条件 —— 没有未覆盖的新方向，就说明任务该结束了。

### 2.3 planner 多轮共享 todolist：让攻击链在"无状态会话"里稳定推进

这是我认为 ARTEX 最有价值的一个设计。

问题背景：planner 是事件驱动的，**每次被唤醒都是一个全新会话，没有任何上下文记忆**。而真实攻击链天然是串行有依赖的。如果把整条链在一轮里全部并行派下去，结果就是乱套 —— 上一步的凭据还没拿到，横向的 worker 已经跑完了。

解法：planner 持有一份 **按任务保留、跨唤醒常驻的规划待办（todolist）**。

```
flowchart TB
  subgraph TODO["共享 todolist（按任务保留 · 跨唤醒常驻）"]
    T1["1 注入点 [已完成]"] -.前置满足.-> T2["2 取凭据 [进行中]"]
    T2 -.-> T3["3 横向 [待前置]"]
    T3 -.-> T4["4 提权 [待前置]"]
  end
  R1["第1轮 派意图①"] --> T1
  R2["第2轮 ①产出fact 派意图②"] --> T2
  R3["第3轮 ②产出fact 派意图③"] --> T3
```

每轮只对「前置步骤已完成、依赖的 fact 已存在」的下一步派意图，同时把已被 fact 满足的步骤标完成。**攻击链记录一次，按依赖逐步展开** —— 这样在无状态会话下依然不乱序、不重复。

### 2.4 worker 间的过程级信息交换：不让人白跑一遍

一次深入探索里，很多有价值的观察（某个报错原文、某段异常响应、某个隐藏参数）出现在 worker 的**执行过程中**，但它未必值得被写成正式 fact 污染图谱。

于是 worker 有三把工具：

* `search_all_worker_traces(q)`：在**本任务其他 work 的执行过程**里按关键字检索（自动排除自己这条意图的步骤），命中项带 `intent_id`；
* `list_worker_traces`：先看有哪些 work 跑过；
* `get_worker_trace(intent_id, step_ids=[...])`：取某个 work 具体几步的完整内容。

**信息以"执行过程"为粒度在 worker 之间流动，但边界不变** —— 每个 worker 仍然只做自己领到的那条意图。后面的 worker 能站在前面的肩膀上，不用把同一件事重跑一遍。

### 2.5 两个安全设计，决定了它敢不敢给你用

**拦截审批（guard / intercept）**：worker 的每个工具调用都要过审批门。内置规则里有一条特别值得说 —— 除了认 `DELETE` 方法，还专门拦路径里带 `/delete /del /remove /unlink /erase /destroy` 的 `GET/POST`。原因很实在：现实里大量应用的删除接口就是 `GET /api/user/delete?id=1`，只认 HTTP 方法根本拦不住。规则做了分隔符校验，`/delivery`、`/details`、`/delta` 不会被误拦。审批记录在全局「审批记录」、任务内「拦截审批」、对话审批卡片三处都可展开看调用详情。

**流量录制代理（MITM + CA）**：worker 的 Bash / HTTP 全程走本地代理留痕，默认监听 `127.0.0.1:8788`。漏洞可以关联**多条**流量证据，绑定时会拷出独立副本到证据库 —— 所以后来在流量列表点「清空全部」也不会带走已绑定的证据。这个代理默认只听本地，不要改成 `0.0.0.0`，那等于在公网摆一个开放代理。

---

## 三、功能清单：界面上到底有什么

| 模块 | 实际能力 |
| --- | --- |
| 仪表盘 | 总览 / Token 消耗 / 活动流 |
| 任务 | 创建、暂停、drain、执行过程（会话 / 工具调用逐条可看） |
| 探索链路 | 探索图可视化，看意图—事实—漏洞的血缘关系 |
| 发现 / 漏洞 | 级别、证据、处置状态；支持**手动复测** |
| 资产 | 域名 / 子域 / IP / 服务 / 端点 |
| 资产覆盖图 | 力导向布局，已测高亮，节点可折叠展开 |
| 流量录制 | MITM 抓包留痕、按 host 删除、清空全部（带索引压实） |
| 人在环路 | mainagent 对话，随时介入调整方向 |
| Agent 管理 | 预置 goals / planner / worker / mainagent / retester，可改提示词、LLM、预算、工具 |
| LLM 配置 | 多配置 + 激活切换，支持自定义 base\_url 与代理 |
| 拦截审批 | 工具调用前置审批，内置破坏性规则 + 可选模型兜底审批 |
| 通知推送 | 钉钉 / 飞书 / 企业微信 / 通用 Webhook / Telegram / 邮件六种渠道，实时与汇总两种模式，带投递历史和失败重发 |
| 资产同步 | 从 ScopeSentry 按项目/任务维度一键导入资产 |
| 漏洞复测 | 独立 retester agent 会话，结论三态：仍可复现 / 已修复 / 无法确认 |
| 技能 skills | `api-recon`、`playwright-cli`、`scopesentry`，目录热挂载 |
| MCP | 远程 MCP 支持 `http`（Streamable HTTP）与 `sse`（旧版） |
| 系统配置 | 代理、并发、命令拦截、版本与更新、通知 |

---

## 四、部署前你需要准备什么（项目介绍与完整部署教程）

四项，缺一个都跑不起来：

1. **PostgreSQL**（必需）。这是唯一强依赖，没有它连界面都进不去。
2. **LLM API Key**（探索必需）。`ANTHROPIC_API_KEY` 或 `OPENAI_API_KEY` 二选一，也可以在 UI 里配。支持自定义 `ARTEX_LLM_BASE_URL`，所以走中转站也行。
3. **Docker 或 Go 工具链**（二选一）。Docker 最省事；本地编译需要与 `go.mod` 声明匹配的 Go 版本（当前写的是 `go 1.26.3`）。
4. **Linux / macOS 优先**。`install.sh` 是 bash 脚本，Windows 建议直接上 Docker 或用 WSL。

> **划范围这件事先说清楚**：ARTEX 自己带了审批门和流量留痕，但你要跑它，资产范围得是你有权测试的。真机执行的是 Kali 命令、nmap、playwright，不是模拟器。

---

## 五、安装：三条能走通的路（以及两条走不通的）

### ⚠️ 先看这个坑，能省你半小时

🔒

这段内容已加密

解锁

---

## 十二、许可与作者的使用限制

代码是 **AGPL-3.0**：可以自由使用、修改、分发，但衍生作品必须同样以 AGPL-3.0 开源；**如果你改了它并以网络服务形式提供给用户，必须向这些用户公开完整源码**。

除了协议，作者在 README 里另加了一份"额外约定"，这块跟 AGPL 是两回事，用之前得知道它写了什么：只允许阅读、学习、研究源码，以及在本地隔离环境做原理验证；明确要求不要对线上系统发起实际测试，也不要用于生产环境和实网攻防。

也就是说：**作者把"能不能合法用"和"他用不用你"分开了** —— AGPL 不限制用途，但作者本人表态只接受学习和本地验证。这个态度在同类项目里比较少见，值得单独说一句。

---

## 十三、值不值得上手

**值得，如果你关心的是 Agent 工程本身。**

剥掉"渗透"这层外皮，ARTEX 实际上是一份相当完整的**长链路自主 Agent 参考实现**：

* 怎么在无状态会话里维持一条有依赖的多步计划（共享 todolist）；
* 怎么把"世界事实"和"推演过程"分成两张图，避免 LLM 幻觉污染真值库（双图 + 程序计算去重 key）；
* 怎么让并行 worker 交换过程级信息但不越界（trace 检索三件套）；
* 怎么给高风险工具调用上审批门，还顺手把 `GET /delete` 这种现实坑补上；
* 怎么做带租约的可靠投递、SSE 反代、一键更新带自动回滚。

这些东西换成"自动化运维 Agent""自动化应急响应 Agent""自动化代码审计 Agent"，架构一样能用。

**先别指望它开箱就能替你出渗透报告。** LLM 的判断力决定上限，3 个 worker 跑复杂目标容易在某个资产上打转，token 烧得比你预想快。第一轮的正确用法是：划一个**小范围**、盯着探索链路看它怎么想，把 planner 和 worker 的提示词按你的目标调一调，再放大。

**跑之前把范围划好。** 它会真的发请求、真的执行命令，审批门是最后一道闸，不是免死金牌。

---

*![ARTEX：让 LLM 自己走完全攻击链的开源自主渗透系统（FBI严选）](https://pic1.imgdb.cn/i/034mzF7Gu4Sd3LwJE8S4z4.png)*

*至发文前FBI已经抓获了32个用 ARTEX AI 发动攻击的黑客（这些都是攻击银行及政府机构的，还不算小萝卜头）！*

收藏

分享

报告错误

分享这篇文章

微信扫一扫

在手机上继续阅读

复制

扫码后直接打开这一页

[ARTEX](https://blog.upx8.com/tag/ARTEX/)

[上一篇
Work破甲包使用教程：用四个md文件改掉 AI 的人格](https://blog.upx8.com/Work-md-AI)
[下一篇
澳洲警告AI加剧网络安全威胁 黑客攻击规模与速度空前](https://blog.upx8.com/%E6%BE%B3%E6%B4%B2%E8%AD%A6%E5%91%8AAI%E5%8A%A0%E5%89%A7%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E5%A8%81%E8%83%81-%E9%BB%91%E5%AE%A2%E6%94%BB%E5%87%BB%E8%A7%84%E6%A8%A1%E4%B8%8E%E9%80%9F%E5%BA%A6%E7%A9%BA%E5%89%8D)

## 相关文档

* [FBI从iOS通知存储中提取Signal加密消息
  04-10](https://blog.upx8.com/FBI%E4%BB%8EiOS%E9%80%9A%E7%9F%A5%E5%AD%98%E5%82%A8%E4%B8%AD%E6%8F%90%E5%8F%96Signal%E5%8A%A0%E5%AF%86%E6%B6%88%E6%81%AF)
* [OpenClaw 本地模型方案：模型推荐 + vLLM 部署优化完整教程
  03-19](https://blog.upx8.com/OpenClaw-vLLM)
* [FBI正在调查Steam平台游戏中的恶意软件
  03-16](https://blog.upx8.com/FBI%E6%AD%A3%E...
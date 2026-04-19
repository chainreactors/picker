---
title: 基于多 Agent + Think-Act-Observe 的红队协调引擎 Ovogo
url: https://mp.weixin.qq.com/s/dVQRL6yhSZu3fuuMaJwmdQ
source: Doonsec's feed
date: 2026-04-18
fetch_date: 2026-04-19T04:46:37.220605
---

# 基于多 Agent + Think-Act-Observe 的红队协调引擎 Ovogo

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/4T1PVwJicwkic3iazUsetHwrLibkCwM2KYhsmUs0B7NuF14LWXWLpqPfNqhFWB3icn1n6tkTsCXZGTpPDxygcib2URZSfdFn0clJTPKz3ic2YmicC3c/0?wx_fmt=jpeg)

# 基于多 Agent + Think-Act-Observe 的红队协调引擎 Ovogo

atreasureboy
atreasureboy

泷羽Sec-Norsea

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

念天地之悠悠，独怆然而涕下。

> ```
>                  免责声明
> ```
>
>      本系列工具仅供安全专业人员进行已授权环境使用，此工具所提供的功能只为网络安全人员对自己所负责的网站、服务器等（包括但不限于）进行检测或维护参考，未经授权请勿利用工具中的功能对任何计算机系统进行入侵操作。利用此工具所提供的信息而造成的直接或间接后果和损>失，均由使用者本人负责。
>
> 工具集合：https://pan.quark.cn/s/f113bdb29fd7

## 一、什么是 Ovogo？

Ovogo 是一个 基于 AI Agent 的自主红队协调引擎，专为靶场环境和授权渗透测试设计。它不是简单的工具集合，而是一个具备完整思考和执行能力的 AI“红队队长”。

你只需要给它一个目标（URL、IP 或域名），它就能自主完成理解目标 → 制定计划 → 多 Agent 协同执行 → 动态调整策略 → 收集 Flag → 生成报告

## 二、功能介绍

Ovogo 的核心亮点在于高度自动化和智能化，主要功能包括：

* **自主攻击链规划**：基于 MITRE ATT&CK 框架，自动生成完整攻击路径
* 多 Agent 协同作战：同时运行侦察、扫描、利用、横向移动、Flag 收集等多个专业子 Agent
* **环境感知与智能绕过**：自动检测 WAF、EDR、沙箱等防护，集成 23 种主流绕过技术
* **实时动态调整**：根据执行结果持续观察、评估并调整攻击策略
* **Flag** 自动收集：在靶场环境中智能搜索并提取 Flag
* **完整报告生成**：自动汇总攻击链路、关键发现、利用过程，形成结构化报告
* **多 C2 框架支持**：深度集成 Havoc C2、Sliver C2 等主流红队框架

## 三、工作流程

1. **理解目标** — 接收渗透测试目标（URL / IP / 域名）
2. **环境感知** — 自动检测 WAF/EDR/沙箱防护，生成结构化绕过建议
3. **制定计划** — 基于 MITRE ATT&CK 框架自动生成攻击链
4. **并行分发** — 同时派遣多个专业子 Agent 执行侦察、扫描、利用
5. **防护感知利用** — 集成 Havoc C2 / Sliver C2 / APT28 三大框架的 23 种绕过技术
6. **监控进度** — 定时读取子 Agent 输出，评估进展，调整策略
7. **联动利用** — 将一个 Agent 的发现传递给另一个 Agent 利用
8. **收集 Flag** — 自动搜索、提取目标 Flag
9. **生成报告** — 汇总所有发现，形成完整攻击链记录

**与传统红队框架的本质区别：**

* 传统框架 = 脚本编排（if-then 流程固定，遇防护即失效）
* Ovogo = AI 自主决策 + 防护感知（LLM 每轮推理，动态检测防护并选择绕过技术）

---

## 四、完整架构全景图

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4T1PVwJicwk9k15Sz0cxnAMVFp3Uql00qlIAPqw8GcXe1ZMljb2nHa3uZibECZCeW10oBlUYBeLeyr0DbhJyEchIcNybsdYj80tGwKl3suuSc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/4T1PVwJicwk8lxWlafT9FcQ9QUCa23MjKKm0rsapj5CwCpkdK2RtGnNortu89ia3M6bX1icVdOOr2xYBCicpeamFRcCYkv3KQ24ibCxABSdfVbWo/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/4T1PVwJicwkicrKsIhhmG0ylgkia6rFthPdwYC2kvFatUxQcPXC826picQzQ1scSB4x2gQBY9qU9AO3Wr57bgvFM6ibPAvPNSRxvWHdmkThHn6iac/640?wx_fmt=png&from=appmsg)

---

## 五、核心模块详解

### 执行引擎：Think-Act-Observe

```
┌──────────────────────────────────────────────────────────────────┐
│                     RunTurn() 主循环                              │
│                                                                  │
│  ┌───────────┐    ┌──────────┐    ┌───────────┐    ┌──────────┐ │
│  │ Context   │ -> │ Streaming │ -> │  Tool     │ -> │ Loop /   │ │
│  │ Budget +  │    │ LLM Call  │    │  Batch    │    │ Return   │ │
│  │ Compact   │    │ (Think)   │    │ (Act/Obs) │    │          │ │
│  └───────────┘    └──────────┘    └───────────┘    └──────────┘ │
│       ↑                                                         │
│       │ 每 5 轮                                                  │
│  ┌────┴──────────┐                                             │
│  │ Critic 检查    │  15 项自动纠错清单                           │
│  └───────────────┘                                             │
│                                                                  │
│  并行调度: Promise.all (安全工具)  + 串行 (写操作)                │
│  软中断: ESC 暂停 → 用户介入 → 继续                              │
│  硬中断: Ctrl+C 取消                                              │
└──────────────────────────────────────────────────────────────────┘
```

每次 `runTurn()` 循环：

1. **上下文预算评估** — 检查 token 使用量，决定是否需要压缩
2. **自动压缩** — 超过 75% 时调用 LLM 摘要旧消息，保留最近 8 条原始消息
3. **Critic 注入** — 每 5 轮用 LLM 审查最近 24 条消息，发现失误立即纠正
4. **流式 API 调用** — 接收 LLM 的文本思考（Think）+ 工具调用（Act）
5. **工具批调度** — 读工具并行执行（Promise.all），写工具串行执行
6. **结果注入** — 工具结果作为 user 消息注入下一轮

### 状态机编排器

```
┌──────────────────────────────────────────────────────────────┐
│                    BattleOrchestrator                         │
│                                                              │
│  init → recon → vuln-scan → weapon-match → exploit           │
│         ↘          ↗          ↗         ↗                    │
│                          post-exploit → privesc → lateral    │
│                                            ↖        ↗        │
│                                              report → done   │
│                                                              │
│  PhaseMachine: 阶段状态追踪 + 允许转换约束                    │
│  TaskDAG:      任务依赖图 + 自动触发下游任务                   │
│  Supervisor:   LLM 决策引擎 (JSON 输出) + RoE 约束注入        │
│  Fallback:     规则降级决策 (LLM 失败时)                      │
│                                                              │
│ 启动: ovogogogo --orchestrator "对 target 进行渗透测试"       │
└──────────────────────────────────────────────────────────────┘
```

### 子 Agent 作战体系

```
┌─────────────────────────────────────────────────────────────────┐
│                    子 Agent 作战体系 (25+ 类型)                   │
│                                                                 │
│  Phase 1 — 侦察 + 漏洞探测 (并行开局)                            │
│  ├── recon          侦察总管 (内部: dns-recon / port-scan /     │
│  │                          web-probe / osint)                  │
│  └── vuln-scan      漏洞探测总管 (内部: web-vuln /              │
│                                   service-vuln / auth-attack)   │
│                                                                 │
│  Phase 2 — 漏洞检索                                             │
│  └── weapon-match   POC 库语义检索 (22W Nuclei PoC,             │
│                      BGE-M3 向量搜索)                            │
│                                                                 │
│  Phase 3 — 漏洞利用 + C2 (并行)                                  │
│  ├── manual-exploit  手工利用 (curl/python 精准打击 + 防护绕过)  │
│  ├── tool-exploit    工具利用 (MSF/sqlmap/searchsploit)          │
│  └── c2-deploy       C2 部署 (Metasploit/Sliver 监听 + payload)  │
│                                                                 │
│  Phase 4 — 靶机操作                                             │
│  ├── target-recon   靶机信息收集 (本机 + 内网)                   │
│  └── privesc        权限提升 (SUID/sudo/内核/计划任务/AMSI绕过)  │
│                                                                 │
│  Phase 5 — 内网横移                                             │
│  ├── tunnel         内网穿透 (chisel socks5 代理)                │
│  ├── internal-recon 内网资产发现 (proxychains + nmap)            │
│  └── lateral        横向移动 (MS17-010/PTH/凭证复用/AD攻击)      │
│                                                                 │
│  Phase 6 — Flag 收集                                            │
│  └── flag-hunter    全局 Flag 搜索收集 (6 层深度搜索)             │
│                                                                 │
│  Phase 7 — 报告                                                 │
│  └── report         渗透测试报告生成                              │
│                                                                 │
│  每个子 Agent: 独立 Engine | 专用 Prompt | tmux 面板 | 文件通信  │
└─────────────────────────────────────────────────────────────────┘
```

### 记忆与知识系统

```
┌─────────────────────────────────────────────────────────────────┐
│                     记忆 & 知识系统                              │
│                                                                 │
│  ┌───────────────────┐  ┌───────────────────┐                   │
│  │   语义记忆        │  │   情景记忆         │                   │
│  │   SemanticMemory  │  │   EpisodicMemory  │                   │
│  │                   │  │                   │                   │
│  │ 渗透知识持久化     │  │ 行动轨迹记录       │                   │
│  │ CVE利用/内网拓扑   │  │ "做了什么/成功失败" │                   │
│  │ 凭证/技术栈        │  │ Critic检查时注入   │                   │
│  │                   │  │                   │                   │
│  │ 存储: semantic.jsonl│ │ 存储: episodes.jsonl│                  │
│  └───────────────────┘  └───────────────────┘                   │
│                                                                 │
│  ┌───────────────────┐  ┌───────────────────┐                   │
│  │   实战知识库       │  │   文件记忆         │                  ...
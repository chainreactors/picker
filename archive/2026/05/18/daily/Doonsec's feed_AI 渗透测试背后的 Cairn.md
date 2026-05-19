---
title: AI 渗透测试背后的 Cairn
url: https://mp.weixin.qq.com/s/Z-R8KRdPbzA9kGERSLBUXQ
source: Doonsec's feed
date: 2026-05-18
fetch_date: 2026-05-19T06:02:21.989268
---

# AI 渗透测试背后的 Cairn

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/0zk3Ye7cp03dDyg9ecV6lQiajIiavSSNOupLLoJrzMzxHzSPRovCcU6IvPcHEloibRqPqYIaY7lZ8icf5KxK2KDOcL3ArALPXUvN8ZBcPRgbugw/0?wx_fmt=jpeg)

# AI 渗透测试背后的 Cairn

原创

攻防路
攻防路

攻防录

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

## 简介

Cairn 是 oritera 开源的 AI 通用状态空间搜索引擎。它把“从起点到目标，但路径未知”的问题建模成一张 Fact / Intent 图，再让多个 Agent 围绕这张图持续探索。

项目地址： https://github.com/oritera/Cairn

![](https://mmbiz.qpic.cn/mmbiz_png/0zk3Ye7cp01qT0PTxIwMqxFrDeKCS5qFoZds5Ob6HlaCHXVTS4ibHarsaah4jxjhsxvXYRucDeMgyVSPqoS0NNAQaib9Zn2ouiag9l3ssY0HxY/640?wx_fmt=png&from=appmsg)

AI 渗透测试只是 Cairn 已经验证过的第一个场景。它真正想抽象的是一类问题：起点明确，目标明确，中间路径未知。

这类系统可以用于 CTF、授权安全评估、漏洞研究、数学证明、复杂任务探索。

## 技术原理

Cairn 的核心不是给 Agent 预设“侦察员”“漏洞利用员”“报告员”这种角色，而是把探索过程放进一张共享图里。

图里只有三个核心对象：

| 概念 | 含义 | 作用 |
| --- | --- | --- |
| Fact | 已确认的客观事实 | 作为后续探索的踏脚石 |
| Intent | 还没执行的探索方向 | 让 Agent 知道下一步可以查什么 |
| Hint | 人或系统补充的策略提示 | 不进入因果图，只影响下一轮判断 |

Fact 像路标，Intent 像下一段路。Agent 不直接互相聊天，也不靠固定分工协作。它们都读同一张图，把自己的探索结果写回图里，后来的 Agent 再接着读。

这种方式对应 README 里提到的黑板架构和 stigmergy：多个执行者不直接通信，而是通过共享环境间接协作。

### 执行循环

每个 Worker 都执行同一套 OODA 循环：

| 阶段 | Cairn 里的动作 |
| --- | --- |
| Observe | 读取完整 Fact / Intent / Hint 图 |
| Orient | 判断当前状态离 goal 还有多远 |
| Decide | 生成新的 Intent，或认领已有 Intent |
| Act | 执行探索，写回新的 Fact |

任务类型只有三种：

| 任务 | 触发时机 | 输出 |
| --- | --- | --- |
| Bootstrap | 项目刚开始时，直接尝试推进整个问题 | Fact，必要时 Complete |
| Reason | 读全图，判断是否完成或提出新方向 | Complete / Intent / no-op |
| Explore | 认领一个 Intent 并执行 | 一个新的 Fact |

这个设计的重点是“少角色，多协议”。Agent 不需要知道自己是谁，只需要知道当前图是什么、目标是什么、自己能补哪块事实。

### 系统结构

Cairn 分成 Server 和 Dispatcher 两层。

| 组件 | 职责 |
| --- | --- |
| Cairn Server | 保存 Project、Fact、Intent、Hint，维护图一致性 |
| Dispatcher | 读取图、调度任务、管理容器、解析 Agent 输出 |
| Worker Container | 每个项目的隔离执行环境 |
| Agent Worker | Claude Code、Codex、Pi 等实际执行器 |

Server 不做推理，只做协议真相源。Dispatcher 才负责调度：选择任务、选择 Worker、启动容器内进程、把结构化结果写回 Server。

README 里的架构图可以概括成这样：

```
Cairn Server
  Facts / Intents / Hints
        ↓
Dispatcher
  Scheduling / Container / Protocol Writeback
        ↓
Worker Containers
  Claude Code / Codex / Pi
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0zk3Ye7cp00tiaiaqLe8ibRicicW8YjPEm3ib80lewdP1XVOR8GFToNpWHeTccicM8IJyzomWBc7z99rndmBnqFa1vg3VhibHTQRooY3Ll1y3icdhvNc/640?wx_fmt=png&from=appmsg)

### 为什么不固定角色

固定角色的多 Agent 系统容易遇到两个问题：

1. 角色边界写死后，任务变化时很难调整。
2. 某个角色漏掉的信息，其他角色未必能补回来。

Cairn 的做法是让任务从图里长出来。图上有什么 Fact，当前还有什么 Intent，目标是否已经满足，这些信息决定下一步该做什么。

| 设计方式 | 典型问题 | Cairn 的处理 |
| --- | --- | --- |
| 固定角色 | 角色边界僵硬 | Worker 不绑定角色 |
| 固定流程 | 未知路径容易卡死 | Intent 动态生成 |
| Agent 互聊 | 信息容易散落在对话里 | 所有结论落到 Fact 图 |
| 中心调度推理 | 调度器变成瓶颈 | Server 只维护一致性 |

### 快速上手

Cairn 需要 macOS 或 Linux、Python 3.12+、Docker。README 推荐用 Docker Compose 启动。

1. 克隆仓库。

```
git clone https://github.com/oritera/Cairn.git
cd Cairn
```

2. 拉取 Worker 容器镜像。

```
docker pull --platform=linux/amd64 ghcr.io/oritera/cairn-worker-container:latest
```

3. 使用 Docker Compose 启动。

```
docker pull ghcr.io/astral-sh/uv:python3.13-trixie
docker compose up --build
```

启动后，`cairn-server` 默认监听 8000 端口。数据会持久化到：

```
./datas/cairn/
```

4. 手动启动方式。

```
uv run --project cairn cairn serve
uv run --project cairn cairn dispatch --config dispatch.yaml
```

也可以只做启动健康检查：

```
uv run --project cairn cairn dispatch --config dispatch.yaml --startup-healthcheck-only
```

5. 配置 Worker。

运行前需要编辑 `dispatch.yaml`，填写 LLM endpoint 和 API key。配置里主要有四块：

| 配置块 | 作用 |
| --- | --- |
| `server` | Cairn Server 地址 |
| `runtime` | 调度间隔、全局并发、项目并发 |
| `tasks` | bootstrap / reason / explore 超时策略 |
| `workers` | Claude Code、Codex、Pi 等 Worker 配置 |

默认示例里，单个项目最多 4 个 worker，全局最多 8 个 worker，调度间隔是 3 秒。

## 使用场景

### 1. CTF 和靶场解题

任务示例：给定靶机地址和 flag 目标，让多个 Agent 并行探索端口、Web 服务、凭证、权限路径。

技术要点：不要把扫描输出直接塞满上下文。把结论写成 Fact，把下一步方向写成 Intent，原始日志放文件引用。

### 2. 授权安全评估

任务示例：在明确授权的内网或演练环境中，让 Agent 逐步确认攻击面、误配置、权限边界和可达路径。

技术要点：授权边界必须写进 origin、goal 或 Hint。不要让系统对未知外部目标自由探索。

### 3. 漏洞研究流程管理

任务示例：围绕某个组件，从复现条件、影响版本、触发路径、补丁差异逐步推进。

技术要点：Fact 只写已确认事实。猜测和方向放 Intent，人工判断放 Hint，避免把未证实结论写进图。

### 4. 复杂问题求解

任务示例：不是安全问题，而是数学证明、代码迁移、复杂调试，目标明确但路径不明确。

技术要点：把“状态空间搜索”抽出来用。Cairn 不要求任务一定是渗透测试，只要求有 origin、goal 和可验证的中间事实。

## 结尾

Cairn 值得关注的点，不是“又一个 AI 渗透测试 Agent”。它把 Agent 协作压缩成一套图协议：Fact 记录已经知道的事，Intent 记录下一步要探索的方向，Hint 承载人工判断。

这种设计更像给 Agent 铺路标。每个 Agent 不需要知道全局剧本，只要读图、补图、继续往目标推进。

往期推荐 📚

[对Auth/Waf 自动化bypass的burpsuite插件](https://mp.weixin.qq.com/s?__biz=MzY5ODAyOTAwMg==&mid=2247484955&idx=1&sn=f51bc8eeb37a4ffb74b57ba81e046d9a&scene=21#wechat_redirect)

[anything-analyzer：AI抓包分析器](https://mp.weixin.qq.com/s?__biz=MzY5ODAyOTAwMg==&mid=2247484875&idx=1&sn=2cf7e2e15f83e0e6619d940b77b3253c&scene=21#wechat_redirect)

[taste-skill：AI前端审美外挂](https://mp.weixin.qq.com/s?__biz=MzY5ODAyOTAwMg==&mid=2247484810&idx=1&sn=26bdcc11d8d2221d3d6d7694a78d2118&scene=21#wechat_redirect)

欢迎关注“攻防录”✨

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/7vAmdAO11X4lmHfibkjicia7MkfgkmAZCoKicD7poPsfAkjB9o6vqFNE8stLqAYa4gaHHLSmU42FMuYrNiab6mWBWTg/0?wx_fmt=png)

攻防录

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/7vAmdAO11X4lmHfibkjicia7MkfgkmAZCoKicD7poPsfAkjB9o6vqFNE8stLqAYa4gaHHLSmU42FMuYrNiab6mWBWTg/0?wx_fmt=png)

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
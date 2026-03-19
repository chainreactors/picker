---
title: Agent开发｜从0实现Agent（一）：50行代码实现Mini Claude Code（工具与执行篇）
url: https://mp.weixin.qq.com/s/1H-IJ7ChlP5jZ3r1zXBS9w
source: Doonsec's feed
date: 2026-03-18
fetch_date: 2026-03-19T04:16:18.142410
---

# Agent开发｜从0实现Agent（一）：50行代码实现Mini Claude Code（工具与执行篇）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/XkUCeyh2WibhwzAMxibjtZicxDrUgJR3HrcYUrgibneOD5Yvcu5TEvzyVF15KNjKgU8dcTeAJqknqK9UX4dzkpppXrWlIJQKEW3UpGHjgYTCft8/0?wx_fmt=jpeg)

# Agent开发｜从0实现Agent（一）：50行代码实现Mini Claude Code（工具与执行篇）

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

本系列文章将复现`learn-claude-code`项目，从0构建`nano Claude Code-like agent`。

手动实现一个类似Claude Code的Agent，学习Agent的内部工作原理和开发流程。

### 学习路线

学习路线：

```
第一阶段: 循环                       第二阶段: 规划与知识
==================                   ==============================
s01  Agent 循环              [1]     s03  TodoWrite               [5]
     while + stop_reason                  TodoManager + nag 提醒
     |                                    |
     +-> s02  Tool Use            [4]     s04  子智能体             [5]
              dispatch map: name->handler     每个子智能体独立 messages[]
                                              |
                                         s05  Skills               [5]
                                              SKILL.md 通过 tool_result 注入
                                              |
                                         s06  Context Compact      [5]
                                              三层上下文压缩

第三阶段: 持久化                     第四阶段: 团队
==================                   =====================
s07  任务系统                [8]     s09  智能体团队             [9]
     文件持久化 CRUD + 依赖图             队友 + JSONL 邮箱
     |                                    |
s08  后台任务                [6]     s10  团队协议               [12]
     守护线程 + 通知队列                  关机 + 计划审批 FSM
                                          |
                                     s11  自治智能体             [14]
                                          空闲轮询 + 自动认领
                                     |
                                     s12  Worktree 隔离          [16]
                                          任务协调 + 按需隔离执行通道

                                     [N] = 工具数量
```

课程目录：

| 课程 | 主题 | 格言 |
| --- | --- | --- |
| s01 | Agent 循环 | *One loop & Bash is all you need* |
| s02 | Tool Use | *加一个工具, 只加一个 handler* |
| s03 | TodoWrite | *没有计划的 agent 走哪算哪* |
| s04 | 子智能体 | *大任务拆小, 每个小任务干净的上下文* |
| s05 | Skills | *用到什么知识, 临时加载什么知识* |
| s06 | Context Compact | *上下文总会满, 要有办法腾地方* |
| s07 | 任务系统 | *大目标要拆成小任务, 排好序, 记在磁盘上* |
| s08 | 后台任务 | *慢操作丢后台, agent 继续想下一步* |
| s09 | 智能体团队 | *任务太大一个人干不完, 要能分给队友* |
| s10 | 团队协议 | *队友之间要有统一的沟通规矩* |
| s11 | 自治智能体 | *队友自己看看板, 有活就认领* |
| s12 | Worktree + 任务隔离 | *各干各的目录, 互不干扰* |

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

## 下载项目与环境安装

### Ubuntu22.04

在VMware虚拟机中安装Ubuntu22.04操作系统，作为基础环境。

### 基础环境安装

```
sudo apt update

sudo apt install net-tools
sudo apt install vim
sudo apt install curl
sudo apt install git
sudo apt install python3-pip

curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt-get install -y nodejs
```

### 下载项目

```
git clone https://github.com/shareAI-lab/learn-claude-code
cd learn-claude-code
pip install -r requirements.txt
```

### 配置大模型API

配置大模型API作为agent的基座：

```
cp .env.example .env
```

编辑`.env`文件：

```
# API Key (required)
# Get yours at: https://console.anthropic.com/
ANTHROPIC_API_KEY=sk-ant-xxx

# Model ID (required)
MODEL_ID=claude-sonnet-4-6

# Base URL (optional, for Anthropic-compatible providers)
# ANTHROPIC_BASE_URL=https://api.anthropic.com

# =============================================================================
#  Anthropic-compatible providers
#
#  Provider         MODEL_ID              SWE-bench  TB2     Base URL
#  ---------------  --------------------  ---------  ------  -------------------
#  Anthropic        claude-sonnet-4-6     79.6%      59.1%   (default)
#  MiniMax          MiniMax-M2.5          80.2%        -     see below
#  GLM (Zhipu)      glm-5                77.8%        -     see below
#  Kimi (Moonshot)  kimi-k2.5            76.8%        -     see below
#  DeepSeek         deepseek-chat        73.0%        -     see below
#                   (V3.2)
#
#  SWE-bench = SWE-bench Verified (Feb 2026)
#  TB2       = Terminal-Bench 2.0 (Feb 2026)
# =============================================================================

# ---- International ----

# MiniMax          https://www.minimax.io
# ANTHROPIC_BASE_URL=https://api.minimax.io/anthropic
# MODEL_ID=MiniMax-M2.5

# GLM (Zhipu)      https://z.ai
# ANTHROPIC_BASE_URL=https://api.z.ai/api/anthropic
# MODEL_ID=glm-5

# Kimi (Moonshot)  https://platform.moonshot.ai
# ANTHROPIC_BASE_URL=https://api.moonshot.ai/anthropic
# MODEL_ID=kimi-k2.5

# DeepSeek         https://platform.deepseek.com
# ANTHROPIC_BASE_URL=https://api.deepseek.com/anthropic
# MODEL_ID=deepseek-chat

# ---- China mainland ----

# MiniMax          https://platform.minimax.io
# ANTHROPIC_BASE_URL=https://api.minimaxi.com/anthropic
# MODEL_ID=MiniMax-M2.5

# GLM (Zhipu)      https://open.bigmodel.cn
# ANTHROPIC_BASE_URL=https://open.bigmodel.cn/api/anthropic
# MODEL_ID=glm-5

# Kimi (Moonshot)  https://platform.moonshot.cn
# ANTHROPIC_BASE_URL=https://api.moonshot.cn/anthropic
# MODEL_ID=kimi-k2.5

# DeepSeek (no regional split, same endpoint globally)
# ANTHROPIC_BASE_URL=https://api.deepseek.com/anthropic
# MODEL_ID=deepseek-chat
```

可以根据实际使用的模型填写，国内推荐使用`DeepSeek API`：

```
# API Key (required)
# Get yours at: https://console.anthropic.com/
ANTHROPIC_API_KEY=sk-xxxxxxxxxxxxxxxxxx

# Model ID (required)
MODEL_ID=deepseek-chat

# Base URL (optional, for Anthropic-compatible providers)
ANTHROPIC_BASE_URL=https://api.deepseek.com/anthropic
```

### 查看课程文档

```
cd web && npm install && npm run dev   # http://localhost:3000
```

![image-20260316114847122](https://mmbiz.qpic.cn/sz_mmbiz_png/XkUCeyh2Wibjmr1BBUDaK4KwPmLxd0n3UaXic8WlHjyDWAcoiavbeeawIHIQWYknkLtqRClxPIoGExVu8ic9dichVNPzVmb3Zicl9L21J9fyPPsg4/640?wx_fmt=png&from=appmsg)

访问`http://localhost:3000`：

![image-20260316114946886](https://mmbiz.qpic.cn/mmbiz_png/XkUCeyh2WibiazqIGLNE9TWdwExlSP2JjjVG8yJ546XuHIlwv1Gib44XPFTZMicxZV3IkkmX3HKzfOMnW26aYeyeooP01lvrT6thFgu1kYLPhbs/640?wx_fmt=png&from=appmsg)

即可打开官方课程文档。

## 基础知识

### 核心模式

所有 Agent 共享同一个循环：**调用模型、执行工具、回传结果**。生产级系统会在其上叠加策略、权限和生命周期层。

核心模式代码：

```
while True:
    response = client.messages.create(messages=messages, tools=tools)
    if response.stop_reason != "tool_use":
        break
    for tool_call in response.content:
        result = execute_tool(tool_call.name, tool_call.input)
        messages.append(result)
```

### Anthropic API

用户（user）请求格式：

```
response = client.messages.create(
    model=MODEL,           # 1. 指定模型
    system=SYSTEM,         # 2. 设置“系统提示词”
    messages=messages,     # 3. 提供“对话历史”
    tools=TOOLS,           # 4. （可选）定义“可用工具”
    max_tokens=8000,       # 5. 设置“最大回复长度”
)
```

它会构造如下请求：

```
{
  "model": "deepseek-chat",
  "system": "你是一个有用的AI助手，可以调用工具。",  // 系统提示词，设定AI的身份和规则
  "messages": [          // 对话历史，必须交替出现 user 和 assistant 的消息 [citation:8]
    {"role": "user", "content": "帮我看看当前目录有什么文件？"}
  ],
  "tools": [             // 可供AI使用的工具列表
    {
      "name": "bash",
      "description": "运行一个bash命令",
      "input_schem...
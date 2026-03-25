---
title: OpenClaw：技术解读和给 AI 应用开发的启示（2026）
url: https://arthurchiao.art/blog/openclaw-technical-notes-zh/
source: ArthurChiao's Blog
date: 2026-03-24
fetch_date: 2026-03-25T04:16:07.624067
---

# OpenClaw：技术解读和给 AI 应用开发的启示（2026）

# [ArthurChiao's Blog](https://arthurchiao.art/)

* [Home](/index.html)
* [Articles (EN)](/articles)
* [Articles (中文)](/articles-zh)
* [Categories](/categories)
* [About](/about)
* [Donate](/donate)
* [RSS](/feed.xml)

TOC

# OpenClaw：技术解读和给 AI 应用开发的启示（2026）

Published at 2026-03-24 | Last Update 2026-03-24

最近几个月 OpenClaw 大火，各种 Claw 大家多多少少都体验过了，
本文从技术角度尽量介绍一些不一样的东西，希望可以给大家一些参考和思考。

![](/assets/img/openclaw-technical-notes/openclaw-arch-2.png)

**Code and scripts used in this post**: [Github](https://github.com/ArthurChiao/arthurchiao.github.io/tree/master/assets/code/openclaw-technical-notes).

水平及维护精力所限，文中不免存在错误或过时之处，请酌情参考。
**传播知识，尊重劳动，年满十八周岁，转载请注明[出处](https://arthurchiao.art)**。

---

* [1 引言](#1-引言)
  + [1.1 技术演进：LLM -> Agent -> Assistant](#11-技术演进llm---agent---assistant)
  + [1.2 OpenClaw 是什么](#12-openclaw-是什么)
    - [官方自我介绍](#官方自我介绍)
    - [设计视角](#设计视角)
    - [技术视角](#技术视角)
  + [1.3 OpenClaw 不是什么？](#13-openclaw-不是什么)
* [2 ToyClaw：200 行 Python 代码实现一个 Claw](#2-toyclaw200-行-python-代码实现一个-claw)
  + [2.1 Code (by cursor with GPT-5.4)](#21-code-by-cursor-with-gpt-54)
  + [2.2 启动和基本对话测试](#22-启动和基本对话测试)
  + [2.3 Identity/Soul/User 测试](#23-identitysouluser-测试)
  + [2.4 User 测试](#24-user-测试)
  + [2.5 Skill 测试](#25-skill-测试)
  + [2.6 其他测试](#26-其他测试)
    - [查看 CPU 占用最高的几个进程](#查看-cpu-占用最高的几个进程)
    - [查看哪个进程在监听 `22` 端口](#查看哪个进程在监听-22-端口)
  + [2.7 小结](#27-小结)
* [3 OpenClaw 技术架构](#3-openclaw-技术架构)
* [4 OpenClaw 核心组件](#4-openclaw-核心组件)
  + [4.1 Agent](#41-agent)
    - [系统提示词](#系统提示词)
    - [Agent 类型: in-process vs. subprocess](#agent-类型-in-process-vs-subprocess)
  + [4.2 Skill](#42-skill)
    - [skill vs. tool](#skill-vs-tool)
    - [示例：`tripgenie` skill](#示例tripgenie-skill)
  + [4.3 定时任务](#43-定时任务)
  + [4.4 工作空间 (workspace)](#44-工作空间-workspace)
* [5 当我们在养龙虾时，我们在养什么](#5-当我们在养龙虾时我们在养什么)
  + [5.1 `AGENTS.md`：主 Agent 系统提示词](#51-agentsmd主-agent-系统提示词)
  + [5.2 BOOTSTRAP.md：启动提示词，用后即删](#52-bootstrapmd启动提示词用后即删)
  + [5.3 USER.md：Assistant 对 User 的理解和记录](#53-usermdassistant-对-user-的理解和记录)
  + [5.4 IDENTITY.md：Assistant 的身份](#54-identitymdassistant-的身份)
  + [5.5 SOUL.md：Assistant 的性格/气质](#55-soulmdassistant-的性格气质)
  + [5.6 TOOLS.md：Assistant 特定的环境信息，协助执行 tool](#56-toolsmdassistant-特定的环境信息协助执行-tool)
  + [5.7 Memory](#57-memory)
* [6 思考](#6-思考)
  + [6.1 万物皆可 SKILL](#61-万物皆可-skill)
  + [6.2 CLI 的世界？](#62-cli-的世界)
  + [6.3 安全](#63-安全)
  + [6.4 费用](#64-费用)
  + [6.5 toC 场景：要求精确输出格式](#65-toc-场景要求精确输出格式)
* [附录](#附录)
  + [Agent 系统提示词](#agent-系统提示词)
    - [`none` 模式](#none-模式)
    - [`minimal` 模式](#minimal-模式)
    - [`full` (default) 模式](#full-default-模式)
  + [Agent 类型: Pi-embedded vs. CLI](#agent-类型-pi-embedded-vs-cli)
    - [Pi-embedded runner](#pi-embedded-runner)
      * [Prompt：no dedicated prompt](#promptno-dedicated-prompt)
      * [流程](#流程)
    - [CLI runner](#cli-runner)
      * [Prompt](#prompt)
      * [流程](#流程-1)
  + [Task-specific / helpers 提示词](#task-specific--helpers-提示词)
    - [1. Subagent context prompt](#1-subagent-context-prompt)
    - [2. Heartbeat prompt (default)](#2-heartbeat-prompt-default)
    - [3. Skills section (in system prompt)](#3-skills-section-in-system-prompt)
    - [4. Memory Recall section (in system prompt)](#4-memory-recall-section-in-system-prompt)
    - [5. Safe external content – security warning](#5-safe-external-content--security-warning)
    - [6. LLM slug generator (session filename)](#6-llm-slug-generator-session-filename)
    - [7. SOUL.md / Project Context (in system prompt)](#7-soulmd--project-context-in-system-prompt)
  + [命令行](#命令行)
    - [TUI](#tui)
    - [CLI](#cli)
  + [Gateway verbose logging via config (equivalent to –verbose)](#gateway-verbose-logging-via-config-equivalent-to-verbose)

---

# 1 引言

## 1.1 技术演进：LLM -> Agent -> Assistant

![](/assets/img/openclaw-technical-notes/llm-agent-assisstant.jpg)

Image generated with Nano Banana (AI).

从技术的视角看，OpenClaw 这类产品并不是凭空出现的，而是大模型技术演进的一个自然结果。
如果把近几年的演进粗略分成三个阶段：

* 以 ChatGPT 为代表的大模型（LLMs），本质上都是一个**“语言推理引擎”**：
  + 它能**理解用户问题、具备世界知识、生成符合逻辑的回答**、做一定程度的分析和归纳，
  + 但它的**能力边界基本停留在对话框内**，和真实世界是完全隔离的。
* 接下来出现的是 Agent。相比 LLM，Agent 不再只是“想”和“答”，而是**能在某些场景开始“做”**：
  + 它会分解任务、规划步骤、调用工具、观察结果、修正错误与再次规划，从一次性回答升级为闭环执行。
  + 并且，**工具调用开始作为初期的“触角”延伸到真实世界**，例如查询天气、修改数据库。
* 以 OpenClaw 为代表的个人助手（本文接下来称为 Assistant），则是 **Agent 的进一步系统化和产品化**。
  + 它不仅有大模型的推理和 Agent 的任务编排和工具调用，**还拥有一台可以由它操控的电脑**（打开了 **`CLI`** 世界的大门）；
  + 换句话说，Assistant 不只是会拆解任务和调用几个 API 的 Agent，而是一个可以在即时通讯、
    文件系统、命令行、浏览器乃至业务系统之间灵活协作的助手，能完成**原本需要人在电脑上完成的事情**。

因此，OpenClaw 的价值不在于它是一个**更好用的对话式产品**，
而在于把 LLM、Agent runtime、工具体系、记忆机制、权限治理和多端交互等等整合成一个可长期协作的系统，能让 AI 真正解锁大量原本需要真人去做的工作。

## 1.2 OpenClaw 是什么

### 官方自我介绍

[OpenClaw 官网](https://openclaw.ai/)对自己的一句话介绍：

> **`The AI that actually does things`**.
>
> Clears your inbox, sends emails, manages your calendar, checks you in for flights.
> All from WhatsApp, Telegram, or any chat app you already use.

[官方技术文档](https://docs.openclaw.ai/)里的另一种介绍：

> **`Any OS gateway for AI agents`** across WhatsApp, Telegram, Discord, iMessage, and more.
>
> Send a message, get an agent response from your pocket. Plugins add Mattermost and more.

### 设计视角

两段官方介绍提到了但没有展开介绍的是：OpenClaw 是一个**个人助手**，这意味着：

1. 它有人设（**`identity`**）、
   性格/人格/语气（**`soul`**），以便于更好地服务该用户（**`user`**）；
2. 它设计上只服务一个用户（**`user`**），
   随着跟这个人的交互越来越频繁，也会越来越了解这个人；这进一步要求它要有记忆（**`memory`**）；
3. 它工作在用户的**个人设备/电脑上**，所有状态都存储在本地，甚至模型都用本地部署的；

### 技术视角

用技术一点的话说，OpenClaw 是一个面向**真实工作流**的 AI 助手。
它的关注点不只是“让模型回答得更聪明”，而是让模型能够在一个持续运行、可接入外部系统、具备权限边界和会话状态的环境里稳定工作。
更宽泛甚至可以说，OpenClaw 更接近一个 **AI 助手基础设施层**，而不是 AI 助手本身。

## 1.3 OpenClaw 不是什么？

* OpenClaw 不是另一个主打安全的本地聊天工具/本地部署模型；
* 不是在 chatbox 内有丰富 UI 交互的产品（e.g. 千问 Agentic Booking、Google Gemini）；

OpenClaw 重点是任务执行和系统协作，而不是把每一步中间结果都包装成一个精美的前端交互组件。
因此，从产品感知上看，它更偏向一个能干活的 Assistant，而不是一个强调展示层体验的 Assistant。

这也意味着，OpenClaw 并不追求非常强的前端呈现控制力。例如，连标准 markdown 的渲染支持都不全。
它的设计目标首先是执行任务、通用可扩展、安全，而不是富文本渲染、卡片编排或复杂 UI 交互。
所以如果你的目标是精确控制回答样式、深度定制消息渲染，或者依赖大量前端组件表达结果，
那么 OpenClaw 并不是最顺手的那类方案。

# 2 ToyClaw：200 行 Python 代码实现一个 Claw

为了理解 OpenClaw 的核心设计，我们首先自己来实现一个极简版的 ToyClaw。
基本功能：

1. 启动之后，支持命令行交互，类似 OpenClaw 的 `openclaw tui`；
2. 工作目录为 `/tmp/toyclaw/`，所有持久化的文件都放在这里；支持 USER.md SOUL.md IDENTITY.md AGENT.md 等；
3. 支持安装和使用 **`skills`**；
4. 支持执行 shell 命令，例如用户问当前占用 cpu 最多的几个进程是什么，要能执行 `ps` 之类的命令并返回最终答案；

用最简单的 python 实现上述功能，所有代码都放在 toyclaw.py。

> 根据以上需求 cursor 写出来的代码有五六百行，但其中一半多都是各种错误处理、防御编程代码、TUI 交互和提示词。
> 这些代码只依赖 python 内置的基本库。

## 2.1 Code (by cursor with GPT-5.4)

我们看一下最核心的代码：

系统提示词、人设、性格、用户描述等等初始化：

```
#!/usr/bin/env python3
"""ToyClaw: a tiny OpenClaw-like CLI assistant.

Everything lives in this single file on purpose:
- interactive TUI-ish REPL
- workspace rooted at /tmp/toyclaw
- context files: USER.md, SOUL.md, IDENTITY.md, AGENT.md
- skills installed as plain markdown files
- minimal shell tool support driven by an OpenAI-compatible chat API
"""

DEFAULT_FILE_CONTENTS = {
    "USER.md": textwrap.dedent(
        """\
        # USER.md

        Describe the human you are helping here.
        Examples:
        - name / nickname
        - language preference
        - working style
        - constraints to remember
        """
    ),
    "SOUL.md": textwrap.dedent(
        """\
        # SOUL.md

        Define the assistant's values, personality, and tone here.
        """
    ),
    "IDENTITY.md": textwrap.dedent(
        """\
        # IDENTITY.md

        Define the assistant's public identity here.
        Example:
        - name
        - vibe
        - style
        """
    ),
    "AGENT.md": textwrap.dedent(
        """\
        # AGENT.md

        Operating notes:
        - help the user directly
        - keep answers concise
        - use shell only when it materially helps
        - avoid destructive commands
        """
    ),
}
```

核心代码：

* 安装 skill
* 构建系统提示词、上下文/对话历史处理
* 执行 shell 命令
* 主循环

```
def install_skill(source: str) -> Path:
    parsed = urlparse(source)
    if parsed.scheme in {"http", "https"}:
        request = Request(source, headers={"User-Agent": "ToyClaw/0.1"})
        with urlopen(request, timeout...
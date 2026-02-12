---
title: Claude 高级技巧与安全配置CLAUDE.md、MCP、命令、技能与钩子 (Skills &amp; Hooks)
url: https://mp.weixin.qq.com/s/8yq_Q8JbnDPRWsltVgc9lw
source: Doonsec's feed
date: 2026-02-11
fetch_date: 2026-02-12T04:18:24.958259
---

# Claude 高级技巧与安全配置CLAUDE.md、MCP、命令、技能与钩子 (Skills &amp; Hooks)

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/UhfibIyPpmuMD1UqUBmqzC3rhb2uAyQib3iauFKEeNGdfHcXI8x6CibiaBEEywrDncPuZicfcKx9B9hcGv6ickWqovjuhpIhmibtgGHUuKuriboYT4IY/0?wx_fmt=jpeg)

# Claude 高级技巧与安全配置CLAUDE.md、MCP、命令、技能与钩子 (Skills & Hooks)

原创

Ti
Ti

TIPFactory情报工厂

![]()

在小说阅读器中沉浸阅读

# 1 安全守门员: 全局 CLAUDE.md

Claude Code 按以下顺序加载 `CLAUDE.md` 文件：

| **层级** | **位置** | **用途** |
| --- | --- | --- |
| **企业级** | `/etc/claude-code/CLAUDE.md` | 组织范围的策略 |
| **全局** | `~/.claude/CLAUDE.md` | 你对**所有**项目的标准 |
| **项目级** | `./CLAUDE.md` | 团队共享的项目指令 |
| **项目本地** | `./CLAUDE.local.md` | 个人项目的本地覆盖 |

全局文件适用于处理的每一个项目。全局文件可以配置的内容：

## 1.1 身份认证

示例：

```
## GitHub 账号
**始终**对所有项目使用 **YourUsername**：
- SSH: `git@github.com:YourUsername/<repo>.git`

## Docker Hub
已验证。用户名在 `~/.env` 中定义为 `DOCKER_HUB_USER`

## 部署
生产环境使用 Dokploy MCP。API 路径在 `~/.env` 中。
```

## 1.2 安全规则

```
## 绝对禁止事项
以下规则是绝对的：

### 严禁发布敏感数据
- 严禁将密码、API 密钥、Token 发布到 git/npm/docker。
- 在任何 commit 之前：验证不包含任何 Secrets。

### 严禁提交 .env 文件

- 严禁将 `.env` 提交到 git。
- 始终验证 `.env` 已列入 `.gitignore`。

### 严禁硬编码凭据

- 始终使用环境变量。
```

**为什么这很重要：Claude 会读取你的 .env** 。安全研究发现，Claude Code 会在未获明确许可的情况下自动读取 `.env`文件。正如 Backslash Security组织警告的内容：

> “如果不加限制，Claude 可能会读取 .env、AWS 凭据或 secrets.json，并通过‘有用的建议’将其泄露。”

你的全局 `CLAUDE.md` 建立了一个行为守门员 —— 即使 Claude 拥有访问权限，它也不会输出这些 Secrets。

# 2 新项目脚手架的全局规则

这是全局 `CLAUDE.md` 变成“项目工厂”的地方。你创建的每个新项目都会自动继承你的标准、结构和安全要求。在全局 CLAUDE.md 中加入脚手架规则，比如：在全局文件中添加“新项目设置 (New Project Setup)”部分：

```
## 新项目设置
创建任何新项目时，务必执行以下操作：

### 1. 必须创建的文件
- `.env` — 环境变量（严禁提交）
- `.env.example` — 带有占位符的模板
- `.gitignore` — 必须包含：.env, .env.*, node_modules/, dist/, .claude/
- `README.md` — 项目概述（引用环境变量，不要硬编码）

### 2. 标准目录结构
project-root/
├── src/         # 源代码
├── tests/       # 测试文件
├── .claude/     # Claude 配置
│   └── commands/# 自定义斜杠命令
└── scripts/     # 构建/部署脚本

### 3. Required .gitignore Entries
```

```
# Environment
.env
.env.*
.env.local
!.env.example

# Dependencies
node_modules/
vendor/
__pycache__/
.venv/

# Build outputs
dist/
build/
.next/
*.pyc

# Claude local files
.claude/settings.local.json
CLAUDE.local.md

# IDE
.idea/
.vscode/
*.swp

# OS
.DS_Store
Thumbs.db
```

```
### 4. Required CLAUDE.md Sections

每一个项目CLAUDE.md都需要：
```

```
# Project Name

## Overview
[What this project does]

## Tech Stack
- Language: [e.g., TypeScript]
- Framework: [e.g., Next.js]
- Database: [e.g., PostgreSQL]

## Commands
- `npm run dev` — Start development server
- `npm run build` — Build for production
- `npm test` — Run tests
- `npm run lint` — Check code style

## Architecture
[High-level overview of the codebase structure]

## Environment Variables
[List required env vars WITHOUT values]
```

为什么要做？GitHub - madison-hutson/claude-project-scaffolding: Ready-to-use project scaffolding with quality gates, testing, and Claude Code integration. Problem This Solves: LLM-assisted development fails by silently expanding scope, degrading quality, and losing architectural intent. This scaffold exists to make those failures impossible without explicit acknowledgement.

> “LLM 辅助开发失败的原因在于，它会在不知不觉中扩大范围、降低质量并失去架构意图。”

* • 每个项目都有不同的结构
* • 安全文件容易被遗忘（.gitignore、.dockerignore）
* • 错误处理不一致
* • 文档格式各不相同
* • 你浪费时间重新解释同样的要求。

GitHub - madison-hutson/claude-project-scaffolding: Ready-to-use project scaffolding with quality gates, testing, and Claude Code integration. Problem This Solves: LLM-assisted development fails by silently expanding scope, degrading quality, and losing architectural intent. This scaffold exists to make those failures impossible without explicit acknowledgement.

# 3 MCP服务器

MCP（模型上下文协议） 允许 Claude 与外部工具和服务进行交互。

添加MCP服务器：

```
# Add a server
claude mcp add <server-name> -- <command>

# List servers
claude mcp list

# Remove a server
claude mcp remove <server-name>
```

核心 MCP 服务器推荐

| **服务器** | **用途** | **安装命令** |
| --- | --- | --- |
| **Context7** | 实时文档访问 | `claude mcp add context7 -- npx -y @anthropic-ai/context7-mcp` |
| **Playwright** | 浏览器自动化测试 | `claude mcp add playwright -- npx -y @anthropic-ai/playwright-mcp` |
| **GitHub** | 仓库管理 | `claude mcp add github -- npx -y @modelcontextprotocol/server-github` |
| **Filesystem** | 扩展文件访问 | `claude mcp add fs -- npx -y @anthropic-ai/filesystem-mcp` |

具体到某一个MCP服务器，可以在Claude.md如下配置：

```
## Required MCP Servers

These MCP servers must be installed for full functionality:

### context7
Live documentation access for all libraries.
Install: `claude mcp add context7 -- npx -y @anthropic-ai/context7-mcp`

### playwright
Browser automation for testing.
Install: `claude mcp add playwright -- npx -y @anthropic-ai/playwright-mcp`
```

# 4 Context7 实时文档

Context7 是改变游戏规则的工具。它让 Claude 能够访问任何库的**最新**文档，解决了模型训练数据截止日期 (Knowledge Cutoff) 的问题。示例：

```
You: "Using context7, show me how to use the new Next.js 15 cache API"

Claude: *fetches current Next.js docs*
        *provides accurate, up-to-date code*
```

| Pattern | Example |
| --- | --- |
| 明确的 | “使用 context7，查找 Prisma 的 createMany 方法” |
| 研究 | “请查看 context7 以了解 React 服务器组件模式” |
| Debugging   调试 | “使用 context7 查找正确的 Tailwind v4 语法” |
|  |  |

### 4.1.1 添加到全局 CLAUDE.md

```
## Documentation Lookup

When unsure about library APIs or recent changes:
1. Use Context7 MCP to fetch current documentation
2. Prefer official docs over training knowledge
3. Always verify version compatibility
```

# 5 自定义命令和子代理

命令以 Markdown 文件的形式存储在 `.claude/commands/` 中，就是我们输入到`/`斜杠触发的这个。

示例：

```
---
description: Fix TypeScript errors
---

Run `npx tsc --noEmit` and fix any type errors.
For each error:
1. Identify the root cause
2. Fix with minimal changes
3. Verify the fix compiles

After fixing all errors, run the check again to confirm.
```

\*\*使用方法：`/fix-types`

## 5.1 子 agent

子代理在**隔离的上下文窗口**中运行——它们不会干扰您的主要对话。

> 每个子代理都在其独立的上下文窗口中运行。这意味着它可以专注于特定任务，而不会受到主要对话的“干扰”。

一些全局Commands可以用来触发子代理干活：

```
## Global Commands

Store these in ~/.claude/commands/ for use in ALL projects:

### /new-project
Creates new project with all scaffolding rules applied.

### /security-check
Scans for secrets, validates .gitignore, checks .env handling.

### /pre-commit
Runs all quality gates before committing.

### /docs-lookup
Spawns sub-agent with Context7 to research documentation.
```

# 6 单一用途的对话聊天很重要

这或许是最重要的部分。 **研究始终表明，混杂不同主题会严重降低准确性**参考：arxiv.org

> 随着上下文窗口中标记数量的增加，模型准确回忆信息的能力会下降。

* • **中间迷失问题**：LLMs对**上下文开头和结尾**的信息记忆效果最好，中间内容容易被遗忘。
* • **情境漂移**：当你转换话题时，先前的上下文就会变成**干扰后续推理的噪音** 。
* • **注意力预算**：“Transformer 模型需要 n² 个词元之间的成对关系。随着上下文的扩展，模型的‘注意力预算’就会变得捉襟见肘。”

可以在执行任务之间经常使用 `/clear` 来重置上下文窗口，尤其是在长时间会话期间，无关的对话会不断累积。

也可以使用子Agent隔离执行：

```
Spawn a sub-agent to research React Server Components.
Return only a summary of key patterns.
```

# 7 Skills & Hooks -- 强制执行

为什么 CLAUDE.md 规则会失效？

* • **上下文窗口压力** ：长时间的对话可能会使规则脱离主动关注范围。
* • **指令冲突** ：其他上下文可能会凌驾于您的规则之上。
* • **复制粘贴传播** ：即使 Claude 不编辑 `.env` ，它也可能将密钥复制到另一个文件。

```
PreToolUse hook blocking .env edits:
  → Always runs
  → Returns exit code 2
  → Operation blocked. Period.

CLAUDE.md saying "don't edit .env":
  → Parsed by LLM
  → Weighed against other context
  → Maybe followed
```

## 7.1 Hooks：确定性控制

钩子是 shell 命令，会在特定的生命周期节点执行。它们不是建议，而是每次都会运行的代码。

| **事件 (Event)** | **触发时机 (When It Fires)** | **使用场景 (Use Case)** |
| --- | --- | --- |
| `PreToolUse` | 任何工具执行之前 | 拦截/阻止危险操作 |
| `PostToolUse` | 工具执行完成之后 | 运行 Linter、格式化工具或测试 |
| `Stop` | Claude 完成响应时 | 回合结束时的质量把控 (Quality Gates) |
| `UserPromptSubmit` | 用户提交提示词 (Prompt) 时 | 验证或增强提示词内容 |
| `SessionStart` | 新会话开始时 | 加载上下文，进行初始化 |
| `Notification` | Claude 发送警报时 | 桌面通知 |

示例：禁止密码获取
在`~/.claude/settings.json`中添加：

```
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Read|Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "python3 ~/.claude/hooks/block-secrets.py"
          }
        ]
      }
    ]
  }
}
```

hook脚本：`~/.claude/hooks/block-secrets.py`

```
#!/usr/bin/env python3
"""
PreToolUse hook to block access to sensitive files.
Exit code 2 = block operation and feed stderr to Claude.
"""
import json
import sys
from pathlib imp...
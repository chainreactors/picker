---
title: 11733行代码复刻Claude Code！港大开源OpenHarness
url: https://mp.weixin.qq.com/s/OWMyT9fIQwcQUzxYWR__Zw
source: Doonsec's feed
date: 2026-04-11
fetch_date: 2026-04-12T04:43:22.338572
---

# 11733行代码复刻Claude Code！港大开源OpenHarness

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nX68dP9Wa1bVcRrTju8x1bsG45ymZEsicGAVFyHP8fSorLvJx6LXia4F3VkW6g1c20LBnGGdkZS4nOz8sFD3ZqFiciaA9AAgfwBKGydXNG3ZIicI/0?wx_fmt=jpeg)

# 11733行代码复刻Claude Code！港大开源OpenHarness

原创

我真tm厉害
我真tm厉害

黑客茶话会

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

AI AGENT 框架深度解析

# 11733行代码复刻Claude Code！港大开源OpenHarness狂揽3.9k星

2026年4月11日 | 黑客茶话会

51万行代码才能做到的事情，11733行就够了。

香港大学数据智能实验室（HKUDS）在4月1日开源了一个项目——OpenHarness，直接拿Claude Code开刀：用不足其1/44的代码量，复刻了98%的核心工具能力。

发布不到10天，GitHub Stars已经突破3.9k，登上Trending榜单，还引来了出版社的注意。

这到底是怎么做到的？

⚡ 数据先说话

11,733
行 Python 代码

98%
Claude Code 功能覆盖

1/44
Claude Code 体积

3.9k+
GitHub Stars（10天内）

**对比一句话：** Claude Code 源码泄漏时有51.2万行代码，OpenHarness用1.17万行就复刻了其98%的能力——代码量只有它的2.3%。

🧠 什么是"Harness"

这是理解OpenHarness的关键概念。

很多人把AI模型和AI Agent混为一谈，但其实是两层：

🧠 模型层（Model）

提供智能——理解、推理、生成。这是Claude、GPT-4、DeepSeek做的事。

🔧 Harness 层（执行基础设施）

提供"手、眼、记忆、安全边界"——工具调用、文件操作、记忆持久化、权限管控。这就是OpenHarness做的事。

官方定义："An Agent Harness is the complete infrastructure that wraps around an LLM to make it a functional agent. The model provides intelligence; the harness provides hands, eyes, memory, and safety."

翻译一下：模型是大脑，Harness是身体。没有Harness，再聪明的模型也只是个聊天机器人。

🏗️ 10个子系统，拆解清楚

OpenHarness的代码组织成10个清晰模块：

openharness/
├── engine/          # Agent Loop 核心引擎
├── tools/           # 43+ 内置工具
├── skills/          # 按需加载的知识技能
├── plugins/        # 插件系统
├── permissions/  # 权限控制
├── hooks/           # 生命周期钩子
├── commands/      # 54 个命令
├── mcp/             # MCP 协议客户端
├── memory/          # 持久记忆
├── coordinator/  # 多 Agent 协调
└── ui/              # React 终端 UI

🔥 5大核心能力拆解

1️⃣ Agent Loop 引擎

不是简单的while循环，而是状态机驱动的执行引擎。支持并行工具调用（自动分析依赖图）、流式处理、指数退避重试、Token预算管理和上下文自动压缩。

2️⃣ 43+内置工具

文件读写、Shell执行、代码搜索（Grep/Glob/LSP）、Web抓取、MCP协议、Notebook编辑……每个工具都有Pydantic类型校验和JSON Schema自描述，复刻了Claude Code 98%的工具能力。

3️⃣ 持久记忆系统

自动发现CLAUDE.md项目规范，MEMORY.md跨会话持久化（SQLite存储），智能上下文压缩：滑动窗口+分层摘要+重要性评分，动态Token预算管理。

4️⃣ 三级权限治理

**Strict（严格）**：所有危险操作人工确认 / **Auto（自动）**：信任操作自动放行，可疑操作询问 / **Full（全权）**：CI/CD场景全自动执行。支持pre/post工具钩子，路径级规则，命令白名单。

5️⃣ Swarm 多Agent协调

父子Agent模式，独立上下文和工具集，任务调度流程：分解→分配→并行执行→同步→合并→错误恢复。未来将集成ClawTeam，支持Agent间消息传递和共享状态。

🌐 模型中立：不绑定Anthropic

OpenHarness原生支持Claude，但通过环境变量可以接入任意OpenAI兼容端点：

| 模型提供商 | 支持 |
| --- | --- |
| Claude (Anthropic) | ✅ 原生 |
| DeepSeek / 通义千问 / Kimi | ✅ |
| Ollama（本地模型） | ✅ 离线 |
| Groq / SiliconFlow | ✅ |
| OpenRouter | ✅ |

一行环境变量切换模型，不用改任何代码。这让它成为真正意义上的"模型中立"Agent框架。

⚡ 5分钟上手

官方要求用uv包管理器（不支持pip直接安装）：

# 安装uv
pip install uv

# 初始化项目并安装OpenHarness
uv init my-agent && cd my-agent
uv add "hkuds/openharness[cli]"

# 设置API密钥
export ANTHROPIC\_API\_KEY=sk-...

# 一条命令启动
oh -p "检查这个仓库，列出Top 3优化建议"

**Skills系统：** 把.md技能文件放入`~/.openharness/skills/`，Agent就能按需加载。已有40+内置技能（commit、review、debug、test等），兼容Anthropic官方skills生态。

📊 测试覆盖：不只是demo项目

| 测试类型 | 数量 |
| --- | --- |
| 单元/集成测试 | 114 |
| CLI E2E 测试 | 6 |
| Harness E2E 测试 | 9 |
| React TUI 测试 | 3 + 4 |
| Skills + Plugins E2E | 12 |
| 总计 | 148 |

148个测试用例——这不是随手写的demo，是认真做工程的产品。

🎯 谁该用OpenHarness

📚 学习Agent底层原理

1.17万行清晰的Python代码，是学习Agent架构最好的教材。比读Claude Code的泄漏源码省力44倍。

🏠 本地私有化部署

支持Ollama离线模型，数据完全不出内网。金融、医疗、政务场景的理想选择。

🤖 CI/CD自动化

无头模式（headless）支持代码审查、测试生成、PR描述自动生成等任务，接入流水线一行命令搞定。

🔬 多Agent研究

内置Swarm协调机制，是研究多Agent协作系统的现成实验平台。

📌 结语

OpenHarness的意义不只是"复刻Claude Code"。它用极简的代码量，把AI Agent的基础设施完整拆解出来，告诉所有人：

✨ Agent的能力不在于模型有多聪明
✨ 而在于给模型配备了多强大的"身体"
✨ 而这个"身体"，其实可以很轻

同样来自HKUDS的Auto-Deep-Research已经在学界获得高度认可，这次的OpenHarness，节奏更快、工程更扎实。

如果你正在学Agent开发，或者想在本地跑一个完整的AI编程助手，OpenHarness值得认真看一看。

GitHub： https://github.com/HKUDS/OpenHarness

⊙ ⊙ ⊙

本文基于GitHub仓库、官方文档及公开技术文章整理。

不涉及未经授权的技术细节或敏感数据。

黑客茶话会

分享安全事件深度解读、攻防技术干货、AI工具生态分析

Copyright © 2026 黑客茶话会

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/XCnU3W0ibv6wxwenPYokRNMKjlj60e9AfziaFLIaibO8hjXTFKE3zKTKnst388z1Tz7Kia3KicOMOnicGh1fNiaH6uJxw/0?wx_fmt=png)

黑客茶话会

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/XCnU3W0ibv6wxwenPYokRNMKjlj60e9AfziaFLIaibO8hjXTFKE3zKTKnst388z1Tz7Kia3KicOMOnicGh1fNiaH6uJxw/0?wx_fmt=png)

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
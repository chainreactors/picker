---
title: Claude Code简介
url: https://mp.weixin.qq.com/s/RdJ576iOGiwMkuu3FxOh7g
source: Doonsec's feed
date: 2026-06-24
fetch_date: 2026-06-25T06:07:51.767328
---

# Claude Code简介

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/smrEGbtBXaX21Gnwicbj5iawCJFho8DCfpQ2g7ibIKKkVbnhAibBvdar4OMX93ng6raEzlicC49yho9sl90pWPNvfxDrXU1X1sQUD86F93J6EQpE/0?wx_fmt=jpeg)

# Claude Code简介

原创

信安路漫漫
信安路漫漫

信安路漫漫

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

Claude Code 是 Anthropic 公司推出的一款终端原生（Terminal-Native）AI 编程助手。

它不仅仅是一个聊天机器人或 IDE 插件，而是一个能够直接操作你文件系统、执行 Shell 命令、理解整个项目上下文的自主 Agent。你可以把它想象成一位坐在你终端里的资深结对编程伙伴。

# 🚀 核心定位：它是什么？

## 形态

命令行工具 (CLI)，直接在 Terminal/iTerm/PowerShell 中运行。

## 本质

基于 Claude 3.7 Sonnet (及后续模型) 的自主 Agent。

## 能力

+ 👀 全库视野：能读取和理解整个代码仓库的结构和内容（支持 200k+ 上下文）。
+ ✍️ 直接修改：可以直接创建、编辑、删除文件，而不仅仅是给出代码片段让你复制粘贴。
+ 🛠️ 执行命令：可以运行 npm install、git commit、pytest 等 Shell 命令。
+ 🔄 自主循环：遇到报错会自动分析日志、修改代码、重试，直到任务完成。

# 💡 核心功能与特点 (2026 最新版)

根据最新资料，Claude Code 已经进化到 2.1+ 版本，具备以下强大特性：

## 1. 真正的“全栈”操作能力

## 文件读写

claude "帮我把 src/utils.py 里的所有 print 替换为 logging" -> 它直接修改文件。

## 多文件协作

claude "添加一个用户登录功能" -> 它会自动创建路由、模型、模板、测试文件等多个文件，并建立关联。

## Git 集成

claude "提交刚才的修改并写一个清晰的 commit message" -> 它自动执行 git add, git commit。

## 2. 超长上下文与项目理解

支持 200k+ tokens 上下文，可以轻松吞下整个中型项目。

自动识别项目结构（如 Python 的 virtualenv, Node 的 node\_modules），智能忽略无关文件。

## 3. 自主调试与修复 (Self-Healing)

当你让它“修复这个 bug”时，它会：

* 运行测试复现 bug。
* 分析错误堆栈。
* 修改代码。
* 再次运行测试验证。
* 如果失败，重复上述步骤，直到成功。

## 4. 高度可定制与扩展

## Skills (技能)

2.1 版本新增，允许定义自定义指令集，让 Claude 记住你的编码规范或常用工作流。

## MCP (Model Context Protocol)

支持动态连接外部数据源和工具（如数据库、Jira、Slack）。

## Vim 模式

内置 Vim 键位支持，方便终端重度用户。

## 5. 安全与控制

## 权限确认

在执行危险操作（如删除文件、运行未知脚本）前，会暂停并请求用户确认。

## 沙箱机制

建议在 Docker 或受限环境中运行，防止意外破坏主机系统。

# 🆚 Claude Code vs. 其他工具

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 特性 | Claude Code | GitHub Copilot | Cursor | 传统 Chat (网页版) |
| 形态 | 终端 CLI | IDE 插件 | 独立 IDE   (VS Code Fork) | 网页浏览器 |
| 文件操作 | 直接修改 | 建议/补全 | 直接修改 | 仅文本输出 (需手动复制) |
| 命令执行 | 支持   (Run Shell) | 不支持 | 有限支持 | 不支持 |
| 项目视野 | 全库索引 | 当前文件/部分上下文 | 全库索引 | 需手动粘贴代码 |
| 自主性 | 高   (可循环调试) | 低 (被动补全) | 中 (Agent 模式) | 无 |
| 适用场景 | 复杂任务自动化  、脚本编写、重构 | 日常编码补全 | 沉浸式 AI 开发 | 简单问答、片段生成 |

# 🛠️ 如何使用？(快速入门)

## 1. 安装

需要 Node.js 18+ 环境：

```
npm install -g @anthropic-ai/claude-code或者使用 yarn yarn global add @anthropic-ai/claude-code
```

## 2. 认证

首次运行会引导你登录 Anthropic 账号：

claude

# 按提示打开浏览器授权

## 3. 基本命令示例

## 简单任务

```
claude "帮我写一个 Python 脚本，爬取 Hacker News 的前 10 条标题并保存为 JSON"
```

## 修复 Bug

```
claude "运行 pytest，如果有失败的测试，请分析原因并修复代码"
```

## 重构代码

```
claude "将 src/ 目录下所有使用 requests 的地方替换为 httpx，并确保异步兼容"
```

## 交互式会话

```
claude进入交互模式，可以连续对话 > 我想添加一个用户注册功能，需要哪些步骤？ > 好的，请先创建数据库模型...
```

# 💰 计费模式

基于 Anthropic API 用量 计费。

由于它能自主循环（可能多次读取文件、运行命令、重试），Token 消耗可能较快。

建议设置预算限制或在非关键任务中使用较小上下文窗口。

# ⚠️ 注意事项与最佳实践

## 代码审查

：虽然它很强大，但永远不要无条件信任 AI 生成的代码。务必 Review 它修改的文件和执行的命令。

## 版本控制

：在使用前确保 Git 工作区是干净的，方便随时 git revert。

## 敏感信息

：不要在包含 API Key、密码等敏感信息的目录中直接使用，或确保 .env 文件已被忽略。

## 明确指令

：指令越具体，结果越好。例如：“修复 bug”不如“运行 test\_login.py，修复导致 AssertionError 的问题”。

# 🌟 总结

Claude Code 是“AI Agent 编程”时代的标志性工具。

如果你只是需要代码补全，Copilot 足够。

如果你喜欢在 IDE 里和 AI 深度交互，Cursor 是很好的选择。

但如果你希望完全解放双手，让 AI 自主完成一个完整的开发任务（从读代码、改代码、跑测试到提交 Git），Claude Code 是目前最强大的选择。

它代表了未来编程的一种新范式：开发者从“写代码的人”转变为“定义目标和审核结果的人”。

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/Rzo6rPw2nBzeSE9F8n8h6enwOQRic7J3SE7afEypJIw6rfTP291hkrrVzeuGMOlj17RGwbv8wJibtdQnmamtGNmQ/0?wx_fmt=png)

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
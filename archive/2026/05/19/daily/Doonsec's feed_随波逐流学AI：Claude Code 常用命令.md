---
title: 随波逐流学AI：Claude Code 常用命令
url: https://mp.weixin.qq.com/s/3nJ1qA_TftfPdkdF90opew
source: Doonsec's feed
date: 2026-05-19
fetch_date: 2026-05-20T06:00:38.046566
---

# 随波逐流学AI：Claude Code 常用命令

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/xKia4GpOxoXVEdJJkK90P69eVAH8qvsZcmJqVBnFK4Ue2Gsu49jQmAxtGcsqauElkM6YYu1AHnuUDGlMZVme15U2cxOGNUAsW6RziaChaMyfY/0?wx_fmt=jpeg)

# 随波逐流学AI：Claude Code 常用命令

原创

长弓三皮
长弓三皮

长弓三皮

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/WTULWRVyhM355SQ3VwNKn1t4icEDiatRdCHBOz48XCyqG12bFkJiaXVQ9NSK8d4sQxdDWAAeBnE3vxI7Kv8L16ulQ/640?wx_fmt=gif&from=appmsg)

***随波逐流工作室—-探索前沿科技，分享最新软件。点击标题下蓝字“******长弓三皮******”关注，我们将为您提供有深度、有价值、有意思的阅读。***

*朋友们，现在只对常读和星标的公众号才展示大图推送，建议大家把长弓三皮“设为星标”，否则可能就看不到了啦！*

作者：随波逐流

![](https://mmbiz.qpic.cn/mmbiz_png/WTULWRVyhM3WyznugvYy71CFweUXJfda3ibXhwJxiaWbHNxxaJP1mKV6eWq1CO9BhQ7ibAMCnhVtrFUEQW4dkUMuA/640?wx_fmt=png&from=appmsg)

**Claude Cdoe安装**

Claude Code安装参看

《[随波逐流学AI：实战Claude Cdoe安装](https://mp.weixin.qq.com/s?__biz=MzU2NzIzNzU4Mg==&mid=2247491489&idx=1&sn=d0a2b5d59eda8d204000682dae19947d&scene=21#wechat_redirect)》

文章涉及到的软件安装可能需要访问github，如部分网友无法访问，我提供了国内下载地址：https://pan.quark.cn/s/ba582b0bb7d8

##

##

## Claude Code 常用命令

##

##

## 一、Claude Code 简介

Claude Code 是 Anthropic 推出的一款强大的 AI 编码助手，运行在终端环境中。它能够直接在项目目录中理解代码结构、编辑文件、执行命令，并支持持久化记忆、上下文压缩、后台任务、多模型切换等专业能力。

#### 智能代码分析

自动理解项目结构，提供精准的代码建议和优化方案

#### 持久化记忆

通过 CLAUDE.md 文件保持会话间的知识连续性

#### 多模型支持

支持 Sonnet、Opus、Haiku 等多种模型灵活切换

## 二、CLI 启动命令

CLI（Command Line Interface）命令用于启动 Claude Code 会话，控制会话的初始行为和配置。

2.1 基础启动命令

| 命令 | 描述 | 示例 |
| --- | --- | --- |
| `claude` | 启动交互式会话 | `claude` |
| `claude "query"` | 使用初始提示启动交互式会话 | `claude "explain this project"` |
| `claude -p "query"` | 通过 SDK 查询，然后退出 | `claude -p "explain this function"` |
| `claude --version` | 查看当前版本 | `claude --version` |
| `claude update` | 更新到最新版本 | `claude update` |

2.2 会话管理命令

| 命令 | 描述 | 示例 |
| --- | --- | --- |
| `claude -c` | 继续最近的对话 | `claude -c` |
| `claude -r "<session>"` | 按 ID 或名称恢复会话 | `claude -r "auth-refactor"` |
| `claude attach <id>` | 附加到后台会话 | `claude attach 7c5dcf5d` |
| `claude logs <id>` | 查看后台会话日志 | `claude logs 7c5dcf5d` |

2.3 身份验证命令

| 命令 | 描述 | 示例 |
| --- | --- | --- |
| `claude auth login` | 登录 Anthropic 账户 | `claude auth login --console` |
| `claude auth logout` | 登出账户 | `claude auth logout` |
| `claude auth status` | 显示身份验证状态 | `claude auth status` |

##

## 三、Slash Commands（斜杠命令）

Slash Commands 是在交互会话中以 `/` 开头输入的内置指令，用于控制会话状态、调整模型配置、执行代码审查等高频操作。

**提示：**在会话中输入 `/` 即可弹出所有可用命令的交互式列表，输入 `/` 后接字母可实时过滤。

3.1 会话管理类

| 命令 | 用途 | 关键说明 |
| --- | --- | --- |
| `/clear` | 清除对话历史 | 别名：`/reset`、`/new` |
| `/compact [说明]` | 压缩历史对话 | 可附加聚焦说明，保留关键上下文 |
| `/rewind` | 回滚对话到指定节点 | 别名：`/checkpoint` |
| `/branch [名称]` | 创建对话分支 | 别名：`/fork`，适合对比不同方案 |
| `/export [文件名]` | 导出当前对话 | 无文件名时弹出选择对话框 |

**选择策略：**上下文快用满但需保留项目背景时用 `/compact`；切换到完全不相关的新任务时用 `/clear`。

3.2 代码分析与质量类

| 命令 | 用途 | 适用场景 |
| --- | --- | --- |
| `/diff` | 打开交互式差异查看器 | 查看 git 未提交修改和逐轮操作 |
| `/security-review` | 分析安全风险 | PR 前快速安全自查 |
| `/simplify [聚焦]` | 并行代码审查并修复 | 代码复用性、质量与效率优化 |
| `/review` | 代码审查 | 全面代码质量检查 |
| `/refactor` | 重构代码 | 代码结构优化 |

3.3 上下文与资源管理

| 命令 | 用途 | 说明 |
| --- | --- | --- |
| `/context` | 可视化上下文使用情况 | 彩色网格展示，提供优化建议 |
| `/memory` | 编辑 CLAUDE.md 记忆文件 | 项目记忆与用户全局记忆 |
| `/init` | 初始化项目 | 生成 CLAUDE.md 项目知识库 |
| `/add-dir` | 添加工作目录 | 让 AI 访问更多文件夹 |

3.4 模型与配置类

| 命令 | 用途 | 说明 |
| --- | --- | --- |
| `/model` | 切换模型 | 支持 Sonnet、Opus、Haiku |
| `/config` | 交互式配置面板 | 主题、通知、自动更新等 |
| `/cost` | 查看 token 消耗 | 预估费用，控制成本 |
| `/doctor` | 环境诊断 | 检查 API、依赖、权限 |

3.5 代码操作类

| 命令 | 用途 | 说明 |
| --- | --- | --- |
| `/edit <文件路径>` | 打开文件编辑 | 交互式编辑指定文件 |
| `/run <命令>` | 执行 shell 命令 | 结果返回给 Claude |
| `/test` | 运行项目测试 | 自动检测测试框架 |
| `/lint` | 代码静态分析 | 检测代码质量问题 |
| `/format` | 格式化代码 | 自动代码格式化 |

##

##

## 四、工作模式介绍

Claude Code 提供三种工作模式，可通过 `Shift+Tab` 循环切换。

#### Default 默认模式

每次修改文件、执行命令都需要用户手动确认，安全性最高，适合初次使用或不确定操作后果的场景。

#### Auto-Accept 自动接受模式

文件修改会自动执行，无需确认，但 shell 命令仍然需要确认，适合重复性高、确定性强的编码工作。

#### Plan 计划模式

纯只读模式，不会修改任何文件、不会执行任何命令，只做分析、梳理结构、输出方案，适合阅读陌生代码、梳理架构。

##

## 五、实战示例

以下是几个常见的使用场景和命令组合示例，帮助您快速上手。

5.1 项目初始化与分析

`# 启动会话并初始化项目 claude /init # 分析项目结构 请帮我分析这个项目的架构和技术栈 # 压缩上下文，聚焦核心问题 /compact focus on the authentication module`

5.2 代码审查与优化

`# 查看当前变更 /diff # 运行测试 /test # 执行代码审查 /review # 安全审计 /security-review # 优化建议 /optimize focus on performance`

5.3 批量代码改造

`# 使用 batch 命令进行大规模代码迁移 /batch migrate src/ from CommonJS to ESM # 自动修复问题 /fix # 格式化代码 /format`

##

## 六、总结

Claude Code 的命令体系设计遵循"渐进式发现"的哲学，新手可以通过 `/help` 和 `/init` 快速上手，专家则可以通过键盘快捷键和自定义命令提升效率。掌握这些常用命令将显著提升您的 AI 辅助编程体验，让您能够更专注于创造性的工作。

建议从基础命令开始，逐步探索高级功能，结合实际项目需求选择合适的命令和工作模式。

参考文档：Claude Code CLI 官方文档

**公众号内输入**

**搜索  “公众号+题目标题”**

**可搜索到此文章**

![](https://mmbiz.qpic.cn/mmbiz_png/WTULWRVyhM0zic6S2ibB39fUwj77vFF6t86jMlgiaoj1ONX1qhodjatvxU72ZgAZPMURCTibgcb4FtLe486t6DXzgA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/WTULWRVyhM0sPwQYjg9rKJ7QZDZ55MPTkiagVPlIHfEtrQUhhUuyQ2fHglSq5ra51MgbUE7vOsUSS1U6z7AUoXA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/WTULWRVyhM0sPwQYjg9rKJ7QZDZ55MPTRZmQUsZYrzGQbrSAf1MyPtGynI7vicFviaDhItaGl9Ww3MarGBrhdEFg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/WTULWRVyhM0sPwQYjg9rKJ7QZDZ55MPTAx3YUQFnDiaZOJeflDbuQa4yukTklZic6HgPEZTAibCg1JIebRM4ynSEA/640?wx_fmt=png&from=appmsg)

你若喜欢，为“长弓三皮”点个赞和在看哦 ![](https://mmbiz.qpic.cn/mmbiz_gif/GtWwdCwkv7FoZELv8KXyj9QRscWJkKCzpmiaqCmVvWQp2PaS7NWwlHojLQz6HQoloicvjichnlSfTVVelMlM5YcSg/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/WTULWRVyhM3PtM3cWAzookibV6m0xYibfFpfiaHFXtoVxRnswM6plX72uEpkaHibPLBsJwyVkWFD4npLtkK7AFdq6w/0?wx_fmt=png)

长弓三皮

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/WTULWRVyhM3PtM3cWAzookibV6m0xYibfFpfiaHFXtoVxRnswM6plX72uEpkaHibPLBsJwyVkWFD4npLtkK7AFdq6w/0?wx_fmt=png)

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
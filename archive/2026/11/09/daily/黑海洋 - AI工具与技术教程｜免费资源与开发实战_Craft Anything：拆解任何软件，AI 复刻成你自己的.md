---
title: Craft Anything：拆解任何软件，AI 复刻成你自己的
url: https://blog.upx8.com/Craft-Anything-AI
source: 黑海洋 - AI工具与技术教程｜免费资源与开发实战
date: 2026-11-09
fetch_date: 2026-11-10T09:02:25.148890
---

# Craft Anything：拆解任何软件，AI 复刻成你自己的

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
[晴

**晴空图床**
*tp.776161.xyz*](https://tp.776161.xyz/)

[首页](https://blog.upx8.com)
/
[资源](https://blog.upx8.com/Free)
/
Craft Anything：拆解任何软件，AI 复刻成你自己的

# Craft Anything：拆解任何软件，AI 复刻成你自己的

[资源](https://blog.upx8.com/Free)
11-09
·
约 11 分钟
·
黑海洋
·

4,673

**Craft Anything** 出自 ArtCraft 团队，一句话定位：**看清任意网站、应用或游戏是怎么做的，再让 AI 给你造一个自己的版本；一个纯 Rust 写的开源净室引擎。**

把目标指给它，说清你想要什么，它就用真实的检查工具研究原作，让编码 agent 建一个新项目，把结果与原件比对，再反复收敛。

建库 9 天，**23,752 星、4,714 fork**。这个速度说明一件事：很多人心里都有"这个软件我能做得更好"的念头，缺的只是动手的第一步。

![网站项目页：步骤进度、相似度 93%、审批卡、检查清单](https://i0.wp.com/cdn.skyimg.net/up/2026/11/9/a836f8024e7405e0e3f755aefaafbf89.webp)

## 它解决什么问题

想复刻一个网站或小工具，通常卡在三处：

1. **看不清结构**：样式怎么排的、间距多少、交互逻辑是什么，靠猜。
2. **写不完成**：需求描述给 AI，它交付一个"看起来像但细节全错"的版本。
3. **验证不了**：改完不知道到底像不像，凭感觉。

Craft Anything 把这三步都变成可检查的流程：用工具读结构 → 让 agent 建项目 → **与原件比对** → 收敛。

关键点在于第三步。它说的"比对过，不是猜的"，是真的逐个尺寸量：**网页按三种屏宽检查，游戏跑它自己的自检，应用看它的运行。**

## 四步流程

指向一个目标，说清你要什么，按下 Start。然后：

| 步骤 | 做什么 |
| --- | --- |
| **研究** | 检查原件：各种宽度下的页面、代码、文件、怎么运行 |
| **构建** | 编码 agent 建新项目，用你指定的语言/框架/引擎（没指定就用合理默认） |
| **检查** | 构建成果与原件比对，列出还不一致的地方 |
| **就绪** | 打开、试玩或预览，或者继续提要求让它收敛 |

遇到该你拍板的地方，它会用大白话问你，而不是自作主张。

![Make 起始界面：选目标类型、地址、净室/深度模式、说需求](https://i0.wp.com/cdn.skyimg.net/up/2026/11/9/171df5ee88ac18c2f02537b538b9eadf.webp)

## 净室模式：这个设计值得单独说

默认是**净室（Clean room）**：**绝不读取原件内部的任何东西**——不读代码、不读文件、不读页面源码。

它只依据你能看到的东西工作：

* 你添加的图片
* 网站以访客身份呈现的样子（截图、可见文本、测量出的布局、颜色、字体与间距、展开的菜单）
* 你允许时截取的应用窗口画面

所有会往内部看的工具都会被拒绝，并告诉你如何开启深度模式。

这个设计意图很清楚：**它复现的是"外观和行为的证据"，不是抄源码。** 对想学怎么做的人来说，这反而更有价值——你得到的是一份基于观察的重新实现，而不是一份复制品。

**深度模式**则打开全部工具：程序代码和文件由内置引擎读取（装了 Ghidra 也会用它），网站的 JavaScript 会被读取、起始页面持续观察，构建方也能用这些能力。

切换方式有三种：标题栏或设置里点、执行 `settings_set deep_mode true`、单次 CLI 运行时加 `--deep`（或 `--clean-room`）。

## 引擎：314 个工具，纯 Rust

这是项目的技术底座，也是它区别于"套壳 AI 工具"的地方。

**一个纯 Rust 的逆向工程引擎，314 个工具**（引擎里 298 个，其余来自 AI 与设置层），覆盖：

原生程序 · .NET · Java · Android · Apple · Electron/JavaScript · 网站 · 固件 · 抓包 · 数据库 · 游戏文件

自带的解码器、反汇编器和反编译器**无需任何外部程序**即可工作。深度模式会全部用上，装了 Ghidra 时也会调用它。

引擎支撑三种前端：桌面应用（egui）、CLI、MCP 服务器。其中一部分还能以 **WebAssembly 跑在浏览器里**。

![进阶工作台：函数列表、伪 C、agent 对话、证据台账](https://i0.wp.com/cdn.skyimg.net/up/2026/11/9/9e4f206951aa5177f04eab1f26f5b529.webp)

## 两种模式，同一个引擎

**简单模式（默认）**：只问"你想做什么"。选一个网站/应用/游戏，描述它，按 Start。项目页显示四步进度、agent 正在做什么（用大白话）、提问卡和审批卡、结果有多像，以及打开结果或文件夹的按钮。底部输入框随时提改动要求。

"只看里面"功能会打开一个目标供你提问，但不构建任何东西（需深度模式）——相当于把它当逆向分析工具单独用。

**进阶模式**：完整工作台，包括所有工具（`Ctrl/Cmd+K`）、函数、字符串、伪 C、反汇编、十六进制、调用图、证据、未知项、任务、日志和 agent 控制台。

## 给 agent 用：每个工具都是 CLI 和 MCP

这一点对写自动化流程的人有用：**314 个工具每一个既是 CLI 子命令，又是 MCP 工具**，agent 不用打开应用就能研究目标或跑完整个重建。

```
craft-anything-cli commands                                   # 列出全部工具（按工具集分组）
craft-anything-cli mcp                                        # 作为 MCP 服务器供任意客户端调用
craft-anything-cli rebuild https://example.com "Recreate this website"
craft-anything-cli rebuild - "A snake game in Rust" --rounds 1
```

继续改已有项目：

```
craft-anything-cli rebuild https://example.com "Make the header blue" --continue-in "<项目文件夹>"
craft-anything-cli rebuild - "Add a contact form" --project-folder "<你的文件夹>" --existing edit
```

输出是带置信度、覆盖范围和局限性的证据记录；大结果先给摘要，再用 `core_evidence_browse` 分页读取。`craft-anything-cli setup` 把 Craft Anything 接到编码 agent 应用上。

纯研究不需要 AI，只有构建环节要。

## 安装

### 环境要求

* **Rust 1.97 或更新**（有依赖要求它，跑 `rustup update`）
* Debian / Ubuntu 跑桌面应用还要装依赖：

```
sudo apt-get install libxkbcommon-dev libwayland-dev libx11-dev libxrandr-dev libxi-dev libgl1-mesa-dev libgtk-3-dev
```

### 编译运行

```
git clone https://github.com/storytold/craft-anything && cd craft-anything
cargo run --release -p craft-anything                # 桌面应用
cargo install --path apps/craft-anything-cli         # 装 CLI
craft-anything-cli doctor                            # 检查安装、编码 agent 和引擎
```

`doctor` 会告诉你缺什么，先跑它再排查其他问题。

### 构建的前提：本机要有一个已登录的编码 agent

**Claude Code 是首选支持对象。** Craft Anything 运行你自己那份未经改动的 `claude` 程序，用你自己的登录；**它从不查看也不接触你的账号**，你对它的使用适用你和 Anthropic 自己的协议。

Codex 适配器已存在，但还没在真实安装上验证过。

提问和分析可以另选 Anthropic、OpenAI、OpenRouter 以及本地 OpenAI 兼容服务（设置 → AI）。

## 项目文件夹结构

新项目放在 `Documents/Craft Anything`（设置 → 通用里可改）。每个项目文件夹里有：

| 路径 | 内容 |
| --- | --- |
| `craft.json` | 请求、目标、状态和历史 |
| `capture/` | 从目标录到的内容 |
| `app/` | 生成的项目 |
| `checks/` | 每次与原件比对的结果 |
| `investigation.cany/` | 证据 |
| `inbox/` | 待回答问题 |

项目也能从你指定的文件夹开始（Start 下的「选择文件夹…」或 `--project-folder`）。如果那里已有文件，你要说明它们是什么：就是应用本身（构建方就地修改），还是作为起点的素材（应用建在旁边的 `app/` 里）。

## 当前状态：早期 alpha

作者列得很实在，没有过度包装。

**今天可用**

* 桌面应用（简单与进阶模式）、CLI、MCP 服务器
* 以 Claude Code 作构建方，面向网站/应用/游戏的 研究 → 构建 → 检查 → 收敛 流程
* 三种屏宽下的网站检查
* Unity、Unreal、Godot 的游戏重建
* 带 Ghidra 的深度模式
* 生成图片和 3D 模型（需自行开启，用你自己的 fal.ai 密钥）
* 插件（MCP 服务器，以及开启 `wasm-plugins` 选项的构建中的 WASM 组件）

**部分可用**

* 用 API 密钥和其他编码 agent 构建（已实现，尚未真机跑通）
* 应用和游戏的行为检查
* 少数引擎工具只用替身测过

**接下来**

* 第一次公开发布（Windows、macOS、Linux、FreeBSD 安装包和浏览器查看器已在 CI 配好）
* 之后的托管版

![贪吃蛇游戏项目完成态，可试玩](https://i0.wp.com/cdn.skyimg.net/up/2026/11/9/2732290ed4bdbc97eae3b65ba5a386ab.webp)

## 一个必须说清的边界

作者在 README 里写了「负责地使用」，这段不能省：

> 请在你拥有或获准检查的软件上使用 Craft Anything。它绝不绕过 DRM、登录或反作弊。

这两句划得很清楚：

1. **不做破解**。不绕 DRM、不绕登录、不绕反作弊。深度模式读的是本机上你自己装好的程序，不是远程破解别人的服务。
2. **重建是依据证据复现布局、风格与行为**，不是复制资产。agent 被要求不得复制 logo、照片或文本，除非你确认你拥有它们或已获授权。

翻译成实际操作：复刻别人的界面学结构没问题，把别人网站的 logo、图片、文案原样搬走不行。**能学怎么做，不能拿别人的东西当自己的。**

## 平台与许可

**开源协议**：MIT 或 Apache-2.0 双许可，任你选。Copyright (c) 2026 ArtCraft Team and the Craft Anything contributors。

随附的字体、图标、图片和其他资源各自保留其许可，每一项在 `ATTRIBUTION.md` 里列了作者、来源和许可。

注意：`docs/brand/` 里的 ArtCraft 名称、标志和 logo 是商标，**不在开源许可范围内**，分支和修改版必须移除它们。

**支持平台**：Windows（x64 / arm64 / x86，MSI + 便携版，有代码签名）、macOS（Universal，已签名公证）、Linux（AppImage / Flatpak / deb / rpm / tar.gz，x86\_64 + aarch64 + riscv64）、FreeBSD（x86\_64）、Web（WebAssembly 浏览器查看器）。

## 和 ArtCraft 其他应用的关系

Craft Anything 是 **Craft App Suite** 的一员，同一团队做了一整排开源创意工具：

PhotoCraft（图像编辑，支持真正的 PSD）· VectorCraft（矢量插画）· FilmCraft（视频剪辑调色）· LightCraft（照片库与 raw）· PdfCraft · EffectCraft（动效）· DesignCraft（排版出版）· FigCraft（界面设计与原型）· WordCraft · SoundCraft（音频）· DeckCraft（演示）· CADCraft · GridCraft（表格）· TextureCraft（3D 贴图）· MaterialCraft（程序化材质）

Craft Anything 在其中的定位不一样——其他是"做事工具"，它是"研究和复刻工具"。

## 适合谁

**适合**：

* 想学某个网站/应用怎么实现，需要一个能出证据的分析工具
* 手上有明确想复刻的东西，希望 AI 交付能对比验证的版本，而不是"感觉差不多"
* 想把研究/重建流程接进自己的 agent 工作流（MCP + CLI 齐全）
* 已经装了 Claude Code，愿意用 Rust 工具链编译

**不适合**：

* 想一键出成品、不愿碰 `cargo` 的人
* 期待它破解付费软件或绕过登录的人——设计上就不做
* 需要稳定生产工具的人：**早期 alpha**，今天能跑，明天接口可能改

## 参考链接

* [项目仓库](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL3N0b3J5dG9sZC9jcmFmdC1hbnl0aGluZw)
* [中文 README](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL3N0b3J5dG9sZC9jcmFmdC1hbnl0aGluZy9ibG9iL21haW4vUkVBRE1FLnpoLm1k)
* [全部工具清单 docs/tools.md](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL3N0b3J5dG9sZC9jcmFmdC1hbnl0aGluZy9ibG9iL21haW4vZG9jcy90b29scy5tZA)
* [Claude Code 接入说明](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL3N0b3J5dG9sZC9jcmFmdC1hbnl0aGluZy9ibG9iL21haW4vZG9jcy9jbGF1ZGUtY29kZS5tZA)
* [路线图](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL3N0b3J5dG9sZC9jcmFmdC1hbnl0aGluZy9ibG9iL21haW4vZG9jcy9ST0FETUFQLm1k)
* [最新发布](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL3N0b3J5dG9sZC9jcmFmdC1hbnl0aGluZy9yZWxlYXNlcy9sYXRlc3Q)
* [ArtCraft 官网](https://blog.upx8.com/go/aHR0cHM6Ly9nZXRhcnRjcmFmdC5jb20v)
* [Discord 社区](https://blog.upx8.com/go/aHR0cHM6Ly9kaXNjb3JkLmdnL2FydGNyYWZ0)

收藏

分享

报告错误

分享这篇文章

微信扫一扫

在手机上继续阅读

复制

扫码后直接打开这一页

[开源](https://blog.upx8.com/tag/%E5%BC%80%E6%BA%90/)
[AI](https://blog.upx8.com/tag/AI/)
[软件工具](https://blog.upx8.com/tag/%E8%BD%A...
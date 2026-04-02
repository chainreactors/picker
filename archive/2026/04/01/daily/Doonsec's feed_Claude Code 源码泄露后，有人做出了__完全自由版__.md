---
title: Claude Code 源码泄露后，有人做出了\"完全自由版\"
url: https://mp.weixin.qq.com/s/kprxkmSlKgIxsJbztLMSxA
source: Doonsec's feed
date: 2026-04-01
fetch_date: 2026-04-02T04:26:58.290672
---

# Claude Code 源码泄露后，有人做出了\"完全自由版\"

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/mAf9IMALLwjE2x4UgUKmysa5ys7vwuZx0GNhX4IocEZozyqeMIVnZEwDs51UwiaibLGicLmicjHyDibCG9C4r0z3mW5Ap2IA6cpVDLI2WpCaWxHs/0?wx_fmt=jpeg)

# Claude Code 源码泄露后，有人做出了"完全自由版"

原创

糖果LUA
糖果LUA

AI安全运营

![]()

在小说阅读器中沉浸阅读

# 实验性功能全部解锁，零遥测

> 一个干净的、可构建的 Claude Code 分支，移除了所有遥测、移除了安全提示的护栏，解锁了所有实验性功能。一个二进制文件，零回传。

---

## 背景：CLAUDE CODE 源码泄露

2026 年 3 月 31 日，Anthropic 的 Claude Code CLI 源码通过 npm 分发的 source map 意外公开。Claude Code 是一款终端原生的 AI 编程代理，被誉为目前业界最复杂的终端 AI Agent 实现之一。

基于这次源码泄露，开发者 paoloanzn 创建了 **free-code** 项目——一个彻底自由的 Claude Code 构建版本。

---

## 核心特点：三大改造

### 1️⃣ 移除所有遥测

官方版本的 Claude Code 会通过多种渠道"打电话回家"：

* OpenTelemetry/gRPC
* GrowthBook 分析
* Sentry 错误报告
* 自定义事件日志

**free-code 做了什么？**

* 所有出站遥测端点被死代码消除或存根化
* GrowthBook 功能标志评估仍可在本地工作（运行时功能门控需要），但不会回传
* 无崩溃报告，无使用分析，无会话指纹识别

### 2️⃣ 移除安全提示护栏

Anthropic 会在每次对话中注入系统级指令，这些指令超越了模型本身的安全约束：

* 硬编码的特定类别提示拒绝模式
* 注入的"网络风险"指令块
* 从 Anthropic 服务器推送的管理设置安全覆盖层

**free-code 做了什么？**
剥离了这些注入。模型自身的安全训练仍然适用——这只是移除了 CLI 包装在模型周围的额外提示级限制层。

### 3️⃣ 解锁所有实验性功能

Claude Code 附带了数十个通过 `bun:bundle` 编译时开关控制的功能标志。在公共 npm 版本中，大多数都是禁用的。

**free-code 做了什么？**
解锁了所有 45+ 个可以干净编译的标志，包括：

| 功能 | 作用 |
| --- | --- |
| **ULTRAPLAN** | Claude Code Web 上的远程多智能体规划（Opus 级别） |
| **ULTRATHINK** | 深度思考模式——输入 "ultrathink" 提升推理强度 |
| **VOICE\_MODE** | 按键说话语音输入和听写 |
| **AGENT\_TRIGGERS** | 用于后台自动化的本地 cron/触发器工具 |
| **BRIDGE\_MODE** | IDE 远程控制桥（VS Code、JetBrains） |
| **TOKEN\_BUDGET** | Token 预算跟踪和使用警告 |
| **BUILTIN\_EXPLORE\_PLAN\_AGENTS** | 内置探索/规划智能体预设 |
| **VERIFICATION\_AGENT** | 用于任务验证的验证智能体 |
| **BASH\_CLASSIFIER** | 分类器辅助的 bash 权限决策 |
| **EXTRACT\_MEMORIES** | 查询后自动记忆提取 |
| **HISTORY\_PICKER** | 交互式提示历史选择器 |
| **MESSAGE\_ACTIONS** | UI 中的消息操作入口点 |
| **QUICK\_SEARCH** | 提示快速搜索 |
| **SHOT\_STATS** | Shot 分布统计 |
| **COMPACTION\_REMINDERS** | 围绕上下文压缩的智能提醒 |
| **CACHED\_MICROCOMPACT** | 通过查询流的缓存微压缩状态 |

完整的功能标志审计（共 88 个标志）可以在项目的 FEATURES.md 中查看。

---

## 技术栈

* **运行时**

  : Bun
* **语言**

  : TypeScript
* **终端 UI**

  : React + Ink
* **CLI 解析**

  : Commander.js
* **Schema 验证**

  : Zod v4
* **代码搜索**

  : ripgrep（内置）
* **协议**

  : MCP、LSP
* **API**

  : Anthropic Messages API

---

## 如何安装

### 一键安装（推荐）

```
BASHcurl -fsSL https://raw.githubusercontent.com/paoloanzn/free-code/main/install.sh | bash
```

这个脚本会：

* 检查你的系统
* 如果需要，安装 Bun
* 克隆仓库
* 启用所有实验性功能进行构建
* 将 `free-code` 链接到你的 PATH

### 手动安装

```
BASH# 安装 Bun（如果你还没有）
curl -fsSL https://bun.sh/install | bash

# 克隆仓库
git clone https://github.com/paoloanzn/free-code.git
cd free-code

# 安装依赖
bun install

# 构建完整功能版本
bun run build:dev:full

# 运行
export ANTHROPIC_API_KEY="sk-ant-..."
./cli-dev
```

---

## 使用方法

```
BASH# 设置 API 密钥
export ANTHROPIC_API_KEY="sk-ant-..."

# 一键模式
free-code -p "这个目录里有什么文件？"

# 交互式 REPL（默认）
free-code

# 使用特定模型
free-code --model claude-sonnet-4-6-20250514

# 使用 Claude.ai OAuth 登录
free-code /login
```

---

## 构建选项

| 命令 | 输出 | 功能 | 备注 |
| --- | --- | --- | --- |
| `bun run build` | `./cli` | 仅 VOICE\_MODE | 类似生产的二进制文件 |
| `bun run build:dev` | `./cli-dev` | 仅 VOICE\_MODE | 开发版本戳 |
| `bun run build:dev:full` | `./cli-dev` | 所有 45+ 实验性标志 | 完整解锁构建 |
| `bun run compile` | `./dist/cli` | 仅 VOICE\_MODE | 替代输出目录 |

你还可以启用特定标志而不使用完整包：

```
BASH# 仅启用 ulraplan 和 ultrathink
bun run ./scripts/build.ts --feature=ULTRAPLAN --feature=ULTRATHINK

# 在开发构建之上启用特定标志
bun run ./scripts/build.ts --dev --feature=BRIDGE_MODE
```

---

## 系统要求

* **Bun**

  >= 1.3.11
* **macOS 或 Linux**

  （Windows 通过 WSL）
* **Anthropic API 密钥**

  （在环境中设置 `ANTHROPIC_API_KEY`）

---

## 去中心化备份

为了确保代码不会因为仓库被删除而消失，该项目通过 Filecoin 在 IPFS 上永久托管了完整副本：

* **CID**

  : `bafybeiegvef3dt24n2znnnmzcud2vxat7y7rl5ikz4y4yoglxappim54bm`
* **网关**

  : https://w3s.link/ipfs/bafybeiegvef3dt24n2znnnmzcud2vxat7y7rl5ikz4y4yoglxappim54bm

---

## 免责声明

原始的 Claude Code 源码归 Anthropic 所有。这个分支的存在是因为源码通过他们的 npm 分发公开暴露了。**请自行斟酌使用。**

---

## 核心价值

**free-code** 项目的核心价值在于：

1. **隐私保护**

   ：彻底移除了所有遥测和回传机制
2. **功能解锁**

   ：释放了官方版本禁用的 45+ 实验性功能
3. **自由控制**

   ：移除了额外的安全限制层，让用户拥有更多控制权
4. **去中心化**

   ：通过 IPFS 永久备份，确保代码不会消失

对于想要深入体验 Claude Code 全部功能、重视隐私保护的开发者来说，这是一个值得关注的项目。

---

**项目地址**: https://github.com/paoloanzn/free-code

---

## 去掉安全提示护栏的潜在风险

### 1. **恶意代码执行风险增加**

官方 Claude Code 在模型安全训练之外，额外添加了提示级限制：

* 硬编码的特定类别提示拒绝模式
* "网络风险"指令块
* 服务器推送的安全覆盖层

这些限制主要针对：

* 可能生成恶意代码的请求
* 网络攻击相关的提示
* 系统破坏性操作

**去掉后：** 模型仍然有基础安全训练，但"第二道防线"没了。如果有人故意诱导，可能会更容易让 AI 生成危险代码。

### 2. **权限决策更宽松**

free-code 移除了 `BASH_CLASSIFIER` 相关的安全限制，这意味着：

* 执行 shell 命令时的权限检查可能更宽松
* 危险操作（如 `rm -rf /`）的警告可能减少

### 3. **无审计追溯**

官方版本有遥测和会话记录，异常行为可以被追踪。free-code 零遥测：

* 无法追溯恶意使用
* Anthropic 无法监控滥用情况

---

## 但也要看到另一面

### 1. **模型本身仍有安全训练**

free-code 只是移除了 CLI 层的额外限制，Claude 模型自身的安全训练仍然生效：

* 不会主动生成恶意代码
* 对明显有害的请求仍有拒绝机制

### 2. **开发者责任**

free-code 明确声明"使用风险自负"，这意味着：

* 适合有一定技术判断力的开发者
* 不适合完全依赖 AI 自动执行危险操作的新手
* 需要用户自己审查生成的代码

### 3. **隐私与安全的权衡**

官方版本的遥测本身也有隐私争议：

* 你的代码、文件内容可能被上传
* 使用习惯被收集分析

free-code 做的是：用"用户自主判断"替代"平台强制管控"。

**适合使用：**

* 有经验的开发者，能判断代码安全性
* 需要高级功能（如 ULTRATHINK、VOICE\_MODE）
* 重视隐私，不希望任何数据回传

**不适合使用：**

* AI 编程新手
* 需要 AI 自动执行大量系统操作
* 无法判断生成代码是否安全

**最佳实践：**

* 生成代码后，先人工审查再执行
* 对危险操作（删除文件、修改系统配置）保持警惕
* 在测试环境中先验证

---

## 总结

去掉安全护栏确实**增加了风险**，但这个风险是**可控的**——前提是你有足够的技术判断力。这就像从"自动挡"换到"手动挡"：更自由，但也需要你自己把控方向。

对于技术成熟的开发者来说，这是一个值得尝试的选择；对于新手，建议先从官方版本开始。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/GibwsQ0cuT56QuCD7VUY4ibe7mGx7xRHwhuPIfeGGrLs3y9LwOQ0qjmm4amibTX3NibWeKP7jsSicCrXq6Czs3waALA/0?wx_fmt=png)

AI安全运营

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/GibwsQ0cuT56QuCD7VUY4ibe7mGx7xRHwhuPIfeGGrLs3y9LwOQ0qjmm4amibTX3NibWeKP7jsSicCrXq6Czs3waALA/0?wx_fmt=png)

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
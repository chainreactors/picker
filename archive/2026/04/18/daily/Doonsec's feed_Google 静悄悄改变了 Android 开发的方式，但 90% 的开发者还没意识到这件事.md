---
title: Google 静悄悄改变了 Android 开发的方式，但 90% 的开发者还没意识到这件事
url: https://mp.weixin.qq.com/s/ugjQFqwu1YTvkFC7ZAhqbg
source: Doonsec's feed
date: 2026-04-18
fetch_date: 2026-04-19T04:48:02.843467
---

# Google 静悄悄改变了 Android 开发的方式，但 90% 的开发者还没意识到这件事

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/RPq1g3ib528hw28BeNZ85hpJpiaB0OIG1cTvVMYF4xrhmdj8mIgtm7637EWjW0fNALiclWFAh7sHMhF8XU2MiaM3cmak5FbEUX5eAK3M7COY6Fk/0?wx_fmt=jpeg)

# Google 静悄悄改变了 Android 开发的方式，但 90% 的开发者还没意识到这件事

原创

0xSec笔记本
0xSec笔记本

0xSec笔记本

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 📢 免责声明

本文所述技术仅用于合法授权的安全研究、教学演示及防御机制开发。作者及发布平台不承担因读者误用、滥用本内容所导致的任何法律责任。请严格遵守《中华人民共和国网络安全法》及相关法律法规。

# 用 Claude Code 写了一段时间 Android的感悟

直到 Google 推出 Android CLI，我才意识到之前浪费了多少时间

#Android CLI  #LLM Agent 开发  #工具链底座

## 一、一个让我重复复盘的 bug

前段时间，我把一个中型 Android 项目的"加全面屏支持"任务完全交给了 Claude Code。
模型很流畅地给出了方案，代码看起来没问题，我合进去，CI 通过，上线。
然后 QA 反馈：某些 OEM 机型上状态栏出现了奇怪的黑边。

我花了几天排查，最后发现问题并不是低级逻辑错误，而是方案里混入了已经不算当前最佳实践的系统栏/insets 写法，同时也漏掉了 edge-to-edge 场景下和软键盘 / IME 相关的必要配置。这些问题在主流流程里不一定马上暴露，但一到特定系统版本、导航模式或 OEM 定制环境下，就会出问题。

模型并不蠢。它只是不知道当时的最新规范——因为这些改动发生在它的训练数据截止日期之后。

💡  这不是某一个模型独有的问题，而是所有 LLM 在 Android 场景里都会遇到的结构性限制：Android 生态碎片化严重，平台行为、官方推荐写法、Jetpack 方案和 OEM 兼容性又一直在变；如果模型没接上最新文档、发行说明和设备反馈，它就很容易给出“看起来对、其实已经过时”的实现。

这个背景，是理解 Android CLI 价值的起点：“在 Android 里，问题往往不只是“会不会写代码”，而是“知不知道这一刻什么写法才是对的”。”

## 二、Android 为什么是 AI Agent 的"地狱难度"

在深入 Android CLI 之前，我们需要先说清楚：为什么 Android 开发对 LLM Agent 来说比 Web 开发难得多？

原因不是 Kotlin 比 TypeScript 难写，而是 Android 的开发链路天然碎片化：

### ◆ 碎片一：SDK 管理是个黑洞

Android SDK 不是一个整体，它是几十个独立组件的集合：platform-tools、build-tools、platforms/android-35、系统镜像、NDK……每个组件有独立的版本号。
Agent 在描述环境时通常说 "需要 Android SDK"，但这句话毫无操作性。sdkmanager 的完整参数路径是：

```
⁠⁠⁠

sdkmanager "platforms;android-35""build-tools;34.0.0""system-images;android-35;google_apis;arm64-v8a"
```

一旦版本字符串错一个字符，就会静默失败或者下载错版本。Agent 很难每次都拼对。

### ◆ 碎片二：Gradle 构建系统的版本地狱

Gradle、AGP（Android Gradle Plugin）、Kotlin，三者的版本矩阵是有效的组合才能编译通过。AGP 8 和 AGP 9 的 DSL 写法有破坏性变化，但 LLM 的训练语料里两种写法都大量存在，模型无法判断应该用哪一套。

⚠️  AGP 9 废弃了 compile、provided、apk 等旧依赖关键字；新项目必须用 implementation / runtimeOnly。训练数据里两套写法并存，Agent 生成旧写法概率极高。

### ◆ 碎片三：设备配置是手工活

创建一个可用的 AVD（Android Virtual Device）涉及：选系统镜像（API 级别 + ABI + 变体）、配置硬件 profile、分配内存和存储。这些步骤在 Android Studio 里有 GUI 向导，但 Agent 在终端里得靠 avdmanager，参数极为繁琐：

```
⁠⁠⁠

avdmanager create avd \
  -n Pixel9_API35 \
  -k "system-images;android-35;google_apis;arm64-v8a"\
  --device "pixel_9"\
  --tag google_apis \
  --abi arm64-v8a
```

参数打错一个，整个命令静默不执行。

### ◆ 碎片四：最新规范永远在变

Edge-to-edge 全面屏、Navigation 3、Predictive Back Gesture、大屏适配……Android 每个版本都有破坏性的 UI/UX 规范变化。这些变化的文档在 developer.android.com 上实时更新，但任何 LLM 的训练数据都必然滞后。

💡  以上四个问题叠加的结果：哪怕你用最强的 LLM，在 Android 场景里平均要多消耗 40%-70% 的 Token 来处理这些"基础设施噪音"，且错误率居高不下。

## 三、Android CLI：一套专为 Agent 设计的基础设施

2026 年 4 月 16 日，Google 发布了 Android CLI Preview。官方的定位是：

> 💡  "为 Agent 工作流设计的 Android 工具套件——消除 Android 开发中的猜测，让 Agent 更高效、更可控，始终遵循最新最佳实践。"

它由三层组成，各司其职：

### ◆ 第一层：CLI 本体（命令层）

一个轻量级的可执行文件，把 Android 开发链路里最碎片化的操作收拢成语义清晰、机器可读的命令：

```
⁠⁠⁠

# ============================================================

# Android CLI 一键环境配置与项目创建完整流程

# 包含 SDK 安装、项目创建、模拟器管理、应用部署、文档查询、Skills 安装

# ============================================================

# -------------------------

# 1️⃣ SDK 管理

# -------------------------

android sdk install "platform-tools"

android sdk install "emulator"

android sdk install "platforms;android-35"

android sdk install "build-tools;34.0.0"

android sdk update

# -------------------------

# 2️⃣ 项目创建（官方模板）

# -------------------------

# 查看所有可用模板

android create --list

# 方法 1：在新目录下创建项目

mkdir ~/MyDemoProject

cd ~/MyDemoProject

android create --name=MyDemoApp empty-activity

# 方法 2：指定输出目录（避免目录冲突）

# android create --name=MyDemoApp -o ~/MyDemoProject empty-activity

# -------------------------

# 3️⃣ 设备管理

# -------------------------

# 创建模拟器

android emulator create --profile=medium_phone

# 列出可用模拟器

android emulator list

# 启动模拟器

android emulator start medium_phone

# -------------------------

# 4️⃣ 应用部署

# -------------------------

# 构建 APK（Gradle）

./gradlew assembleDebug

# 部署到默认模拟器

android run --apks=app/build/outputs/apk/debug/app-debug.apk

# 部署到指定设备（模拟器/真机）

android run --apks=app.apk --device=emulator-5554

# -------------------------

# 5️⃣ 文档查询

# -------------------------

# 搜索最新文档

android docs search "navigation 3 compose setup"

# 拉取文档内容

android docs fetch kb://navigation3-compose-guide

# -------------------------

# 6️⃣ Skill 管理

# -------------------------

# 查看已安装/可用 Skills

android skills list --long

# 安装 Navigation 3 Skill

android skills add --skill=navigation-3

# 安装 Edge-to-Edge Skill

android skills add --skill=edge-to-edge
```

这些命令有几个设计特点值得注意：

* •

  输出是结构化文本，方便 Agent 解析而非人眼阅读
* •

  错误信息明确指向可操作的修复方向
* •

  每个命令的副作用确定且可预期
* •

  支持 --dry-run 预览，不实际执行

### ◆ 第二层：Android Skills（知识层）

这是整个套件里设计最巧妙的部分，也是最容易被忽视的。

Skills 是 Markdown 格式的模块化指令集，本质上是专为 Android 场景定制的 SKILL.md 文件，放在 Agent 的上下文目录里，当提示词匹配特定条件时自动触发。

首批官方 Skills：

| Skill 名称 | 解决什么问题 | 触发场景示例 |
| --- | --- | --- |
| navigation3 | Navigation 3 的正确配置和迁移路径 | "帮我加导航，支持返回栈" |
| edge-to-edge | 全面屏适配的完整流程 | "加全面屏支持" |
| agp-9-migration | AGP 8→9 的 DSL 破坏性变化 | "升级 Gradle 版本" |
| xml-to-compose | XML 布局迁移到 Compose 的规范 | "把这个 XML 改成 Compose" |
| r8-analysis | R8 混淆配置分析和优化 | "打包后类找不到了" |

Skills 的运作机制：当 Agent 检测到提示词里出现"加全面屏支持"，它不需要自己摸索，而是直接执行 edge-to-edge Skill 里定义的步骤——修改 build.gradle、调整 MainActivity、更新主题配置。

💡  Skills 把"知道怎么做"变成了"自动就做了"。对于 AGP 升级、Compose 迁移这类有固定最佳实践的任务，这个机制能把 Agent 的正确率从 60% 直接拉到 95%+。

### ◆ 第三层：Android Knowledge Base（文档层）

通过 android docs 命令访问，覆盖四个来源的实时内容：developer.android.com、Firebase 文档、Google Developers、Kotlin 官方文档。

关键是"实时"两个字。Knowledge Base 在 Google 服务端持续更新，Agent 通过 CLI 查询时拿到的永远是最新版本，而不是训练数据里的快照。

回到我开头说的那个 bug——如果当时配合了 Android CLI，Agent 在写 Edge-to-edge 代码之前会先 android docs search "edge-to-edge android 15"，拿到最新的 WindowInsetsController 用法，那个三天的 bug 就不会存在。

## 四、它和 Claude Code / Gemini CLI / Android Studio 是什么关系？

这是最容易产生误解的地方，我直接给出判断：

### ◆ Android CLI vs Claude Code / Gemini CLI / Codex

这三者不是竞争关系，是不同层级的工具。

| 维度 | Claude Code / Gemini CLI | Android CLI |
| --- | --- | --- |
| 定位 | 通用 AI 编程 Agent，理解需求、生成代码 | Android 专用工具层，管理环境、执行操作 |
| 做什么 | "写一个登录页"，"重构这个类" | "安装 SDK"，"创建模拟器"，"查文档" |
| 知识来源 | 训练数据（有截止日期） | 实时 Knowledge Base + 官方模板 |
| 输出 | 代码文本 | 系统状态变更（文件、设备、SDK） |
| 关系 | 调用方 | 被调用的基础设施 |

正确的使用姿势是：Claude Code 作为"大脑"负责理解需求和生成代码，Android CLI 作为"手脚"负责执行环境相关的操作。

典型的协作流程：

```
⁠⁠⁠

你（对 Claude Code）: 帮我从零建一个支持 Navigation 3 和全面屏的 Android 项目

Claude Code 内部执行：
android init                              # 让自己先读 android-cli skill
android sdk install platforms/android-35  # 安装 SDK
android create --name=MyApp empty-activity-agp-9
android skills add navigation3 edge-to-edge
android docs search "navigation 3 setup"   # 查最新文档
android emulator create --profile=medium_phone
android emulator start medium_phone
./gradlew assembleDebug
android run --apks=app/build/outputs/apk/debug/app-debug.apk
```

全程不需要你手动介入环境配置。Agent 知道该调什么命令，Knowledge Base 保证文档是最新的，Skills 保证迁移步骤是正确的。

### ◆ Android CLI vs Android Studio

这是另一个常见的误解：有人以为 Android CLI 是 Android Studio 的替代品。

不是。它们解决的是完全不同的问题，适用于不同的阶段：

| 场景 | 推荐工具 | 理由 |
| --- | --- | --- |
| 环境初始化 / CI 配置 | Android CLI | 命令行，无 GUI 依赖，可脚本化 |
| 快速原型 / Agent 辅助开发 | Android CLI + Agent | Token 消耗低，操作确定性高 |
| UI 布局精调 | Android Studio | Layout Editor / Compose Preview 不可替代 |
| 交互式调试 | Android Studio | 断点、变量检查、堆栈追踪 |
| 性能 Profiling | Android Studio | CPU、内存、网络、电量全家桶 |
| 生产发布 / 签名打包 | Android Studio | GUI 引导，出错概率低 |
| 旧项目 AGP 迁移 | Android CLI Skills | Skills 覆盖标准迁移路径 |

💡  Google 的设计意图是：用 Android CLI 快速起步，在 Android Studio 里精细打磨。这是一个连续体，不是非此即彼的选择。

## 五、完整实战：从零到真机运行，跟着走一遍

以下是一个完整的、可复现的流程，从安装到跑起第一个 Navigation 3 项目。

### ◆ Step 0：安装 Android CLI

从 developer.android.com/tools/agents 下载，目前 Preview 免费。

```
⁠⁠⁠

# 下载（URL 以实际页面提供的为准）

https://developer.android.com/tools/agents/android-cli/archive?hl=zh-cn

```

```

```
# Linux版本下载
```

```
curl -fsSL https://dl.google.com/android/cli/latest/linux_x86_64/install.sh | bash
```

# 验证安装
android --version

# 保持更新（建议每次使用前跑一次）
android update
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RPq1g3ib528gNQmsz838fDnJFI7KQ96woPwt2hXw8r54iaRFBvuTcAIJABvhtpc72HQibwF7II5icyUibbFwmpF5FYmu1SMZh6BMLibnwbLNIYL84/640?wx_fmt=png&from=a...
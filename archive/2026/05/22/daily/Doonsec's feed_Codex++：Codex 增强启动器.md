---
title: Codex++：Codex 增强启动器
url: https://mp.weixin.qq.com/s/iWNR2pwgSsw0bvY6NRQmMw
source: Doonsec's feed
date: 2026-05-22
fetch_date: 2026-05-23T05:38:37.215906
---

# Codex++：Codex 增强启动器

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/0zk3Ye7cp02eo1Bjria6OmsIZSccDtqXicJkoIWXEBK88l6KEvPpkvCWELQ0wJWlFyzwlTRWKnlQTTSnMRtcVpZ0z5N6qBRzumpdeA7S8AX8Y/0?wx_fmt=jpeg)

# Codex++：Codex 增强启动器

原创

攻防路
攻防路

攻防录

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

Codex++ 是面向 Codex App 的外部增强启动器和管理工具。它不修改 Codex App 原始安装文件，而是通过外部 launcher 启动 Codex，再借助 Chromium DevTools Protocol 注入增强脚本。

项目地址：

https://github.com/BigPizzaV3/CodexPlusPlus

它主要处理几个 Codex 使用中的实际问题：API Key 模式下插件入口不可用、会话缺少删除按钮、中转配置切换麻烦、本地会话和 provider 状态不同步、需要导出或移动项目时操作成本偏高。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0zk3Ye7cp00FicglSco9zMia2rLtQfFeiaooLicWA7FRyycrj79zqoCGrNXCeyU4LyThQDiabsOCHEUic1DG8GNyBCibMqGYib8fv8kbcDSPfrs4y5s/640?wx_fmt=png&from=appmsg)

Codex++

## 技术原理

Codex++ 的设计重点是“外部增强”，不是直接改 Codex 安装包。

它的运行链路可以拆成四步：

1. `Codex++` 静默 launcher 先启动。
2. launcher 找到 Codex App，并以调试端口方式启动 Codex。
3. 后端通过 CDP 找到可注入的 Codex 页面。
4. 注入脚本在页面里增加菜单、按钮、状态检查和桥接调用。

仓库里的 `crates/codex-plus-core/src/cdp.rs` 会访问 `http://127.0.0.1:{debug_port}/json` 获取 CDP target，再挑选标题或 URL 中包含 Codex 的 page target。

桥接部分在 `crates/codex-plus-core/src/bridge.rs`。它通过 `Runtime.addBinding` 注册一个页面侧 binding，再用 `Page.addScriptToEvaluateOnNewDocument` 注入桥接脚本。页面里的增强脚本调用 bridge，后端再根据路径执行删除、导出、设置、状态检查、Zed 打开等操作。

| 模块 | 作用 | 位置 |
| --- | --- | --- |
| launcher | 启动 Codex、选择端口、启动 helper、执行注入 | `apps/codex-plus-launcher/` |
| core | CDP、bridge、设置、中转、更新、路由 | `crates/codex-plus-core/` |
| data | 会话删除、恢复、Markdown 导出、provider 同步 | `crates/codex-plus-data/` |
| manager | Tauri + React 管理界面 | `apps/codex-plus-manager/` |
| inject | 注入到 Codex 渲染端的增强脚本 | `assets/inject/renderer-inject.js` |

这种方式的好处是侵入性更低。Codex++ 不需要改 `app.asar`，也不往 Codex 安装目录写 DLL。风险主要在于 Codex App 页面结构变化后，注入脚本需要跟着更新。

## 痛点与解决

README 里举了两个直接场景。

API Key 模式下，Codex 原生插件入口会提示需要登录 ChatGPT，插件功能无法正常使用。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0zk3Ye7cp03bR7mV2RF8H35cPHDQtENBoCpGic7cGY5UIcFAL0VBb4SmibscV2JF8182LAqJsqfcVpBxicGhG9yxZrbPtJPdQjosPYJs4mRxSs/640?wx_fmt=png&from=appmsg)

API Key 模式下插件入口不可用

Codex 原生会话列表只有归档入口，没有真正的删除按钮。

![](https://mmbiz.qpic.cn/mmbiz_png/0zk3Ye7cp03sMU8gmqfGdPUtklzURpZ220Vsiao2wbKGRiaoVdpIaJXY4VeA4WzSCZjr2Q3Czkzcqqk8pVpKTutvAkGQLw89ODejweicNf1Bzo/640?wx_fmt=png&from=appmsg)

原生会话列表缺少删除能力

Codex++ 启动后，会在页面里增加 Codex++ 菜单，也会给会话列表补上删除、导出、移动等操作入口。

![](https://mmbiz.qpic.cn/mmbiz_png/0zk3Ye7cp009Qt8gMVc8Uh6qYRqMCic0YY2WB6n1R51SRj91Ka3U85J6rkiaaCYFfr4MbnXhMAwBLOnxDZ83hX21Na9ttViaVrweupXiax5RX0w/640?wx_fmt=png&from=appmsg)

Codex++ 解锁插件入口并添加删除按钮

从实现上看，删除能力不是简单隐藏一行 DOM。`codex-plus-data` 会识别本地 SQLite schema，对 Codex threads 相关表做删除，同时生成 undo token 和备份，便于回滚。

## 中转注入

中转注入适合已经在 Codex / ChatGPT 中完成官方账号登录，但希望把模型请求切到自定义兼容 API 的用户。

它的配置入口在管理工具的“中转注入”页面。流程比较直接：

1. 检测本机 `~/.codex/auth.json` 中的 ChatGPT 登录状态。
2. 添加中转配置，填写 Base URL 和 Key。
3. 选择当前配置并应用。
4. 从 `Codex++` 启动 Codex。

Codex++ 会写入 `~/.codex/config.toml`，生成类似配置：

```
model_provider = "CodexPlusPlus"

[model_providers.CodexPlusPlus]
name = "CodexPlusPlus"
wire_api = "responses"
requires_openai_auth = true
base_url = "https://example.com/v1"
experimental_bearer_token = "sk-..."
```

如果要切回官方登录态，在管理工具里清除 API 模式即可。代码里也会备份原有 `config.toml` 和 `auth.json`，再移除相关 API Key 配置。

这里需要注意一点：这类工具会读写 `~/.codex` 下的配置和登录状态。使用前最好确认自己理解中转服务来源、Key 存储位置和配置备份路径。

## 增强功能

Codex++ 的增强功能集中在日常使用细节上。

| 功能 | 说明 |
| --- | --- |
| 插件入口解锁 | 处理 API Key 模式下插件入口不可用的问题 |
| 会话删除 | 在会话列表中增加删除入口，并支持本地数据备份 |
| Markdown 导出 | 将 Codex 会话导出为 Markdown |
| 项目移动 | 修改会话对应的工作目录信息 |
| Timeline | 给长对话增加定位和跳转辅助 |
| 用户脚本 | 启动时注入自定义脚本 |
| Provider 同步 | 启动前同步本地会话 metadata |
| Zed 打开入口 | 识别远程 SSH 上下文后，从 Codex 跳转到 Zed Remote Development |
| 自动更新 | 通过 GitHub Release 检查并拉起安装器 |

顶部菜单会显示 `Codex++`，可以查看后端状态、打开设置面板、检查日志和诊断信息。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0zk3Ye7cp00cpfIULpCkuialU4pyoNacWzlbuyeU11klXnRt48AWo5h7ERWiaSFx2Ygh7yCmsUwCxCbT2gozMw8vN41kyzh3gicQwyXDuKM5HE/640?wx_fmt=png&from=appmsg)

Codex++ 设置面板

## 快速上手

Codex++ 通过 GitHub Release 发布安装包：

https://github.com/BigPizzaV3/CodexPlusPlus/releases

下载时按系统选择对应文件：

```
Windows：CodexPlusPlus-*-windows-x64-setup.exe
macOS Intel：CodexPlusPlus-*-macos-x64.dmg
macOS Apple Silicon：CodexPlusPlus-*-macos-arm64.dmg
```

安装后会出现两个入口：

1. `Codex++`

静默启动入口，不显示管理界面，只负责启动 Codex 并注入增强功能。

2. `Codex++ 管理工具`

Tauri 控制面板，用于启动、检查、修复、更新、配置中转注入、管理增强功能和用户脚本。

如果 Codex++ 菜单没有出现，优先确认自己是从 `Codex++` 入口启动，而不是直接打开原版 Codex。也可以打开管理工具的“诊断”和“日志”页面，看注入状态。

如果插件里显示后端连不上，可以先测试本地 helper：

```
Invoke-RestMethod -Method Post -Uri http://127.0.0.1:57321/backend/status -Body "{}" -ContentType "application/json"
```

如果接口正常，但页面仍超时，通常要重启 Codex++，或者查看日志里的 `renderer.script_loaded`、`bridge.request`、`bridge.response`。

## 开发结构

Codex++ 是 Rust workspace，前端管理工具使用 Tauri + React。

开发命令：

```
# 前端检查
cd apps/codex-plus-manager
npm install
npm run check
npm run vite:build

# Rust 检查
cd ../..
cargo fmt --check
cargo test
cargo build --release
```

主要目录：

```
apps/
  codex-plus-launcher/          静默启动入口
  codex-plus-manager/           Tauri 管理工具
assets/inject/
  renderer-inject.js            注入到 Codex 渲染端的增强脚本
crates/
  codex-plus-core/              启动、注入、配置、更新、安装、桥接等核心逻辑
  codex-plus-data/              会话数据、导出、Provider 同步
scripts/installer/
  windows/CodexPlusPlus.nsi     Windows NSIS 安装包
  macos/package-dmg.sh          macOS DMG 打包
```

## 使用场景

### 1. 用 API Key 或中转服务运行 Codex

任务示例：已经登录 ChatGPT，但希望把 Codex 模型请求切到兼容 API。

技术要点：通过中转注入写入 `CodexPlusPlus` provider。清除 API 模式时，工具会移除相关配置并切回官方登录模式。

### 2. 管理本地 Codex 会话

任务示例：删除不用的会话、导出重要会话、把会话移动到新的项目目录。

技术要点：增强脚本负责在页面加入口，后端通过 bridge 调用 `codex-plus-data` 处理本地 SQLite 和 rollout 文件。

### 3. 给 Codex 加用户脚本

任务示例：启动 Codex 时注入自己的前端脚本，给界面加快捷操作或小工具。

技术要点：用户脚本由管理工具统一开关，launcher 注入时会把脚本加入新文档执行列表。

### 4. 远程开发场景跳转 Zed

任务示例：在 Codex 里识别远程 SSH 上下文和文件路径后，直接用 Zed Remote Development 打开对应文件。

技术要点：注入脚本会尝试从页面状态、React props、文本路径等位置抽取 remote host 和 workspace root，再交给后端打开 Zed。

## 需要注意的点

第一，Codex++ 依赖 Codex App 的页面结构。Codex App 更新后，如果 DOM 或内部状态变了，注入脚本可能需要跟着适配。

第二，它会读写 `~/.codex/config.toml`、`~/.codex/auth.json` 和本地数据库。使用中转注入、会话删除、项目移动前，最好确认备份策略。

第三，macOS 包如果未签名或未公证，可能会被 Gatekeeper 拦截。README 里给出的处理方式是在“系统设置 - 隐私与安全性”中允许打开。

往期推荐 📚

[anything-analyzer：AI抓包分析器](https://mp.weixin.qq.com/s?__biz=MzY5ODAyOTAwMg==&mid=2247484875&idx=1&sn=2cf7e2e15f83e0e6619d940b77b3253c&scene=21#wechat_redirect)

[GPT-Image-2 提示词模板库](https://mp.weixin.qq.com/s?__biz=MzY5ODAyOTAwMg==&mid=2247484779&idx=1&sn=e68487ce016b54a7e6bdb920a04047a6&scene=21#wechat_redirect)

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
---
title: 渗透逆向利器 | 一款基于 MCP 协议的本地逆向分析工具
url: https://mp.weixin.qq.com/s/kW8nIZLMBoxtA_7vAxIy-Q
source: Doonsec's feed
date: 2026-11-15
fetch_date: 2026-11-16T08:46:25.442841
---

# 渗透逆向利器 | 一款基于 MCP 协议的本地逆向分析工具

# 渗透逆向利器 | 一款基于 MCP 协议的本地逆向分析工具

morluto
morluto

HACK之道

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

### 工具介绍

REA 是一款基于 MCP 协议的本地逆向分析工具，专为网络安全与渗透测试场景打造。支持 APK、原生二进制、Electron、.NET、固件等多类目标，可联动 Ghidra、Hopper、JADX 完成静态反编译与运行时行为捕获。依托 AI 智能体自动追踪调用链路，输出带完整证据链的分析结果，省去人工通读大量汇编的繁琐。适用于红队漏洞挖掘、二进制审计、安卓 App 逆向取证，所有分析在本地完成，兼顾效率与数据安全，助力安全研究人员快速拆解闭源程序，定位底层安全风险。

![](https://mmbiz.qpic.cn/mmbiz_png/HqolA1dQic6ibiaKdQGzpMxZ1CBnImLRHCjWIAUcwTYYLf69gicr6Fbl95ucdYKsvm4JdY2IX3xWI09GM0GzXO1MOgc01HpWeU8Nd5xV8Oibsic0k/640?wx_fmt=png&from=appmsg)

### 功能

> 在应用中看到一个想加入自己产品的功能？让智能体用 REA 调查它。即使没有源代码，智能体也可以检查应用、解释功能的工作方式、展示证据，并为你的项目实现类似功能。

## REA 的工作原理

**智能体通过 MCP 调用 REA，检查目标并追踪相关代码。REA 返回发现及对应证据。智能体据此提出后续问题、解释行为，或编写并测试实现。CLI 命令使用同样的工作流。**

![](https://mmbiz.qpic.cn/mmbiz_png/HqolA1dQic69IMm8Kib5cMLJFYLg9BQKacxibl4DO0WkNpsEISdLt94E6lvKiaOKMvAh4ceLINcicNKt5cHSBhuCNdvYkVTzVyicGsE0U1Y6uj91A/640?wx_fmt=png&from=appmsg)

## 可以分析什么

**REA 需要 Node.js 22.x（>=22.19）、24.x（>=24.11）或 26+，以及 npm。额外工具和主机支持取决于分析目标：**

| 目标 | REA 返回的内容 | 要求与指南 |
| --- | --- | --- |
| 原生二进制文件 | 伪代码、汇编、字符串、符号、调用和引用 | Hopper、Ghidra 或 IDA；原生分析 |
| 离线 ELF 布局 | 节、段、原始符号/重定位信息及静态防护机制候选项 | Linux x64 上由调用方提供的 pwntools；二进制诊断 |
| EVM 字节码 | 分派选择器、字节偏移、推断的参数和状态可变性 | Linux x64 上的本地原始字节/十六进制输入载体；离线 EVM 指南 |
| 已记录的 Linux 崩溃 | 原始 note 记录、每个已记录线程的寄存器/信号及可选的映射候选项 | Linux x64 上由调用方提供的 pwntools；可选的 GDB/pwndbg；已记录崩溃 |
| JavaScript / Electron | 模块、导入、source map、路由、IPC 和原生扩展关系 | Node.js 和 npm；应用分析 |
| 网站 | 页面结构、脚本、网络观察结果和按请求获取的截图 | Chrome 系浏览器；浏览器分析 |
| 已保存的网络捕获 | 请求、响应、可访问的载荷和来源位置 | HAR；原生 mitmproxy 捕获需要 Linux 上的 mitmdump；捕获指南 |
| .NET 程序集 | 元数据、CIL 指令、声明的原生依赖和构建对比 | 静态检查；托管代码指南 |
| Android APK | 清单声明、类、反编译的方法和引用 | Linux/macOS/Windows x64 上的无界面 JADX 和完整 JDK；Android 指南 |
| Android 设备 | 设备、软件包、进程、日志、转储、屏幕截图以及 APK/文件传输 | 调用方提供的 adb（模拟器或实体设备）；ADB 指南 |
| JEB 项目 | 引擎支持的项目单元、工件摘要和类型/方法的伪代码 | 由调用方启动、提供 MCP 的 JEB 客户端，通过 REA\_JEB\_MCP\_URL 选择；JEB 指南 |
| Android 资源 | 解码后的清单、字符串表、语言区域和版本信息 | 调用方提供的 Apktool 启动器；资源指南 |
| Flutter 应用 | Dart 快照哈希、按 ABI 的库摘要及引擎构建溯源 | 无（静态 APK 解析）；Flutter 指南 |
| 固件 | 区域、提取结果和转交原生分析的内容 | Linux 上的 Binwalk / Unblob；固件指南 |
| 软件包与资源 | 文件清单、摘要、plist、Apple bundle 结构和提取的资源 | 制品与 JavaScript 指南、Apple 应用 |
| 进程行为 | 终端输出、交互、退出和文件系统观察结果，以及运行对比 | 支持原生 PTY 的 Linux/macOS；进程捕获 |

 使用

使用

### 设置智能体

安装 Node.js 和 npm 后，运行：

```
npx rea-agents setup
```

选择智能体，检查计划中的变更并批准。设置流程会添加 REA 的 MCP 服务和匹配的工作流指引，并备份已有配置。完成后重启智能体。

设置流程支持 Claude Code、Codex、Cursor、Gemini CLI、Grok Build 和其他智能体。提供方配置和手动注册 MCP 的方法见安装与设置。

### 询问智能体

```
弄清 Notes 应用的搜索功能如何工作，展示证据，并为我的项目实现类似功能。
```

把 Notes 替换为目标应用，并描述你想了解的功能。

### 使用终端

检查已解包的 JavaScript/Electron 应用目录或 ASAR 文件：

```
npx -y rea-agents@latest analyze-javascript-application /absolute/path/to/app --json
```

结果包含模块、导入、Electron 边界及相关证据。将路径替换为你的目标路径，例如 Windows 上的 `"D:/apps/example"`。

如果需要经常使用，可以安装 `rea` 命令：

```
npm install --global rea-agentsrea --help
```

### 更新 REA

REA 更新较快，新版本经常包含错误修复。请保持安装的版本为最新。

通过 npm 安装的 CLI 使用：

```
rea update
```

要更新智能体注册和 skill，请运行更新命令输出的设置命令。

如果使用 `npx`，通过以下命令更新智能体设置：

```
npx rea-agents@latest setup
```

检查设置变更并重启智能体。单次 CLI 操作可使用 `npx rea-agents@latest`，后接所需命令。

项目地址

https://github.com/morluto/rea/

预览时标签不可点

阅读原文

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/GzdTGmQpRic1orFibqtmBJd06F33KoWTM6qEUAG7ZbwicA5MhTqx9stelHv8cMgibthiahUBTtgbPgn3ia2bYLpBElTQ/0?wx_fmt=png)

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
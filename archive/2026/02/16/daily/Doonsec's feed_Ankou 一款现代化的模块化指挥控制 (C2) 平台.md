---
title: Ankou 一款现代化的模块化指挥控制 (C2) 平台
url: https://mp.weixin.qq.com/s/PV0oGfl6rafyfi67f2-bmw
source: Doonsec's feed
date: 2026-02-16
fetch_date: 2026-02-17T04:16:21.448049
---

# Ankou 一款现代化的模块化指挥控制 (C2) 平台

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/libkMqMibKDtXe2DL7OW7BMscBHrVKHsrzTkZhIjqS3lpQZR9iblx8snGjkk5ktMRaC9LxOR72j9XlXQKM5ZQdYezg9eLYYtPHsnC1r9lW54iac/0?wx_fmt=jpeg)

# Ankou 一款现代化的模块化指挥控制 (C2) 平台

星夜AI安全
星夜AI安全

星夜AI安全

![]()

在小说阅读器中沉浸阅读

📌各位可以将公众号设为星标⭐

📌这样就不会错过每期的推荐内容啦~

📌这对我真的很重要！

![image](https://mmbiz.qpic.cn/mmbiz_png/SffY5ZO3R2lAVT6CicZmYO3GGZre7KEwxiaouHrUbg3rQ0UUVhEI7eDxct12pq4ITqI98fcU1rsJXlHib3VF1n4ew/640?wx_fmt=png&from=appmsg "image")

📌1. 本平台分享的安全知识和工具信息源于公开资料及专业交流，仅供个人学习提升安全意识、了解防护手段，禁止用于任何违法活动，否则使用者自行承担法律后果。

📌2. 所分享内容及工具虽具普遍性，但因场景、版本、系统等因素，无法保证完全适用，使用者要自行承担知识运用不当、工具使用故障带来的损失。

📌3. 使用者在学习操作过程中务必遵守法规道德，面对有风险环节需谨慎预估后果、做好防护，若未谨慎操作引发信息泄露、设备损坏等不良后果，责任自负。

Ankou 是一款现代化的模块化指挥控制平台，其设计目标是让操作人员能够快速上手，同时不牺牲专业能力。从传输中继到桌面客户端，每个组件都配备了便捷的快速启动脚本。您只需克隆代码库、配置植入密钥、执行提供的命令，即可立即开始体验。内置的 AI 助手降低了新手的入门门槛，同时也为经验丰富的团队提供了强大的能力倍增器，助力进行深入的目标分析。Ankou 内置了三个默认代理供团队定制使用——您也可以为团队创建全新的、前所未有的代理类型。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/s3lScxtIeTudbgr4cvNPx5ZCpBCmeUicXAibxZaXAaMursUno0YGJo3icXzWHxc2rU6dx7uwVDvGpKHLCeS3NrOlw/640?wx_fmt=png&from=appmsg)

---

## 核心架构概览

| 组件 | 描述 |
| --- | --- |
| **服务器 (`server/`)** | 这是一个基于 Go 的 API 与 WebSocket 中心，具备 GraphQL 架构、持久化任务、战利品存储、JWT 身份验证以及受 HMAC 保护的代理端点。首次运行 (`go run .`) 时会自动生成 TLS 证书、密钥和 SQLite 数据库。 |
| **幽灵中继 (`ghost-relay/`)** | 这是一个可丢弃的前端，支持多种传输协议（如 HTTPS、HTTP/3 QUIC、SSH、SMB/WebSocket），并将流量转发至服务器。每种协议都封装在一个 `accept_*.go` 模块中，因此添加新的传输协议就像复制模板一样简单。 |
| **代理 (`agents/<name>/`)** | 参考植入体（geist、phantasm、shade）展示了不同的传输堆栈和命令集。每个代理都负责 HMAC 签名、任务执行以及战利品回传。 |
| **客户端 (`frontend/`)** | 这是一个基于 Electron/Vite 的桌面应用程序，集成了实时仪表盘、监听器管理、文件系统浏览器、AI 助手面板和战利品视图。运行 `npm install && npm run electron` 即可启动。 |

这些组件协同工作，构建了一个分层的 C2 架构。该架构既能隐藏真正的服务器，又允许您独立地扩展传输层或代理行为。

---

## 核心特性

### 1. 模块化的传输、处理和代理类型

* **基于请求体的代理识别** - 代理在请求负载中声明其类型，使得无限种类的代理可以共享任意传输，而无需进行端口绑定。
* Ghost Relay 透明地转发流量，服务器根据请求体内容而非端口来路由代理类型。
* 通过 JSON 配置文件 (`server/agent_handlers/handler_*.json`) 即可添加新的处理程序。用户界面会立即更新，显示操作员可用的支持命令。
* 想要定制传输方案？参照 Ghost Relay 的新增传输指南操作，几分钟内就能获得一个可用于生产的模块。
* 所有这些特性都提供了一种简便的方法来构建自定义代理；在您的传输设置完成后，可以参考现有代理，围绕您的新处理程序和偏好的任何 TTP 来构建一个代理。
* 关于灵活的代理类型系统的详细信息，请参阅“基于请求体的代理识别”部分。

### 2. 人机交互式 AI 助手

* 客户端的 **AI 操作** 面板可以与任何兼容 OpenAI 的端点通信，确保所有目标数据都保留在您控制的主机上（例如 OpenAI、LM Studio、Ollama、OpenWebUI 等）。
* 您可以接入您最喜欢的本地或自托管 LLM；助手能够接收完整的命令输出历史，构建对目标的共同理解，并可以总结结果、标记异常、起草后续命令或监控关键工件，同时您始终保持完全的控制权。
* 引导式工作流程帮助经验不足的操作员掌握操作节奏：助手会解释上下文、推荐经过验证的命令、建议决策树并高亮常见的后续步骤。经验丰富的操作员则可以专注于更高层次的策略，利用 AI 快速筛选海量遥测数据、比较主机或在几秒内发现关键节点。
* 点击运行建议（使用 `<cmdankou>` 标签）允许您直接从聊天界面执行 AI 建议的命令，从而保持操作快速且可审计。
* 由于所有操作都通过 OpenAI 兼容层进行代理，因此无需修改 Ankou 的代码即可切换模型。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/s3lScxtIeTudbgr4cvNPx5ZCpBCmeUicXFwuSxMWOKUCxnmibY98Ot6Y4WaAdCOla7FibfxQOJDib6TOvsah1icicic1A/640?wx_fmt=png&from=appmsg)

### 3. AI 辅助的二进制多样化

* Ankou 的多态引擎会在保留全部功能的同时，重写植入程序的源代码结构。每次构建都会生成一个截然不同的二进制文件，从而降低跨攻击活动的可识别性。
* 多样化逻辑与命令映射集成，因此操作员无需为每个变体学习特殊的命令。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/s3lScxtIeTudbgr4cvNPx5ZCpBCmeUicXTjhLU5hEibszdudia07nPK7yJRNVnZXGnDfy1yGYoFcJS9IEPOCBibMKQ/640?wx_fmt=png&from=appmsg)

### 4. 操作员工作流程优化

* **文件系统与战利品浏览器** —— 在一个统一的界面中浏览远程目录、排队下载/上传以及标记战利品。战利品条目会在团队内部即时同步。
* **监听器编排** – 通过用户界面即可启动/停止 HTTPS 监听器，中继协调过程对用户透明。
* **GraphQL + WebSocket 管道** – 所有状态变更都会实时广播给已连接的客户端，确保操作员绝不会错过任何心跳、命令结果或战利品更新。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/s3lScxtIeTudbgr4cvNPx5ZCpBCmeUicX1ictWv5X26aXDJHcmnAcxibcgzU4ywuib7hKX3IvqbCxFEuIozibwswcVg/640?wx_fmt=png&from=appmsg)

### 5. 自动化剧本

* **“自动化”** 选项卡用于捕获可重复使用的剧本——例如快速分类、权限提升、横向移动——以便团队可以触发精心编排的工作流程，而无需每次都重新创建检查清单。
* 操作员只需点击一下即可重放经过验证的操作序列，从而节省时间；而 AI 助手则可以根据实时情报变化，在行动过程中动态调整剧本。

## 代理概览

| 代理 | 平台 | 语言 | 协议/传输 |
| --- | --- | --- | --- |
| **Geist** | Windows | Rust 与 Go | HTTP3/QUIC |
| **Phantasm** | Windows | Rust 与 Go | HTTPS |
| **Apparition** | Windows | Node.js (C 语言注入) | HTTPS |
| **Shade** | Linux | Go | SSH |
| **Wraith** | Linux | Rust | HTTP3/QUIC |

> 关于每个代理的设计、协议和任务模型的详细信息，请参阅代理目录。

---

## AI 后端配置（兼容 OpenAI）

AI 助手和多态引擎都支持 OpenAI API。您可以将 Ankou 指向任何兼容 OpenAI 的后端：

* 本地/自托管选项：例如 LM Studio、Ollama、OpenWebUI（通常默认情况下不需要 API 密钥）

默认设置与用法：

* **API 基础 URL** ：默认为 `http://localhost:11434/v1`（Ollama/LM Studio 可开箱即用）。
* **API 密钥** ：可选；仅在需要身份验证的提供商（如 OpenAI）时才需要。对于无需密钥的本地后端，请留空。
* AI 聊天面板和多态引擎共享这些设置，因此您只需配置一次即可重复使用。

---

## 快速入门（开箱即用）

* 安装最新版本的 Go 语言。
* 运行 `quickstart.py` 脚本。
* 请记录下您的注册密钥和代理 HMAC 密钥（`quickstart.py` 会以绿色打印这两个密钥；您也可以在 `ghost-relay/relay.config` 文件中找到代理 HMAC 密钥，其环境变量名为 `AGENT_HMAC_KEY`——构建代理时需要此密钥）。
* 运行或构建幽灵中继：

  ```
  cd ghost-relay
  go mod tidy
  go run .
  # 或者
  go build .
  ```
* 运行或构建 C2 服务器：

  ```
  cd server
  go mod tidy
  go run .
  # 或者
  go build .
  ```
* 进入任意代理目录，运行构建脚本，并根据您的中继和 C2 设置填写所需字段。

> **需要更多详细信息？** 请参阅完整指南：
>
> * 架构概述和快速入门
> * 添加新的代理、处理程序和监听器
> * 幽灵中继：添加新的传输方式# 构建独立桌面应用程序（若您倾向于自行构建而非使用我们的版本）

Ankou客户端能够打包为适用于Windows、Linux和macOS的独立桌面应用程序：

```
cd frontend
# 为Windows构建（NSIS安装程序 + 便携版.exe）
npm run dist:win
# 为Linux构建（AppImage + .deb包）
npm run dist:linux
# 为macOS构建（适用于Intel和Apple Silicon的DMG）
npm run dist:mac
# 为所有平台构建
npm run dist:all
```

若您不想自行构建，也可以直接使用npm运行该应用程序：

```
npm build
npm run electron
```

**构建输出**位于`frontend/release/`目录下：

* **Windows：**`Ankou C2-0.1.0-x64.exe`安装程序及便携版本。
* **Linux：**`Ankou C2-0.1.0-x64.AppImage`与`.deb`软件包。
* **macOS：**`Ankou C2-0.1.0-x64.dmg`（Intel架构）与`Ankou C2-0.1.0-arm64.dmg`（Apple Silicon架构）。

关于详细的构建说明、故障排除以及配置选项，请参阅`frontend/BUILD.md`文件。

---

# 路线图与贡献

我们正在积极推进以下方面的迭代：

* **将Geist和Phantasm代理集成至Rust**，以实现更小的体积、更强的能力，并做到开箱即用。
* **为Geist、Shade和Phantasm提供Golang基础模板**，使其功能更全面、更易于扩展。
* **提升执行效率**，以便您的工作更加轻松。
* **扩展开箱即用的C2协议功能支持**，这样您可以将我们的更多内容作为模板，用于创建出色的工具。

### 有特定的需求或想法吗？

欢迎在GitHub上提交issue，提出功能建议或初步构想——我们会优先考虑社区真正需要的想法。我们也非常欢迎您提交pull request；在开始之前，请先查阅上方链接的文档以获取指导。

---

# 常问问题

**问：我的代理注册请求返回HTTP 502错误。我遗漏了什么步骤吗？****答：** 监听器可能处于暂停状态。请打开桌面客户端，转到\*\*“监听器”**部分，找到您的代理应使用的监听器，然后点击**“恢复”\*\*按钮。当监听器状态显示为正在运行后，注册通常就会成功。如果问题依旧，请检查您在创建代理时，端点前是否缺少了必要的斜杠。

**问：如何提交反馈或提出功能建议？****答：** 请在GitHub上创建issue。请尽可能详细地描述问题——截图、日志或对工作流程的描述，将有助于我们确定优先级并快速响应。

**问：为什么每个代理都是单独的文件？****答：** 在使用Polyengine的过程中，我们发现向LLM提供单个文件能获得最佳结果。我们理解这会增加理解代码库的难度，但我们的目标是探索人工智能能力的边界。

关注微信公众号后台回复“**20260216** ”，即可获取项目下载地址

关注微信公众号后台回复**入群** 即可加入星夜AI安全交流群

## 圈子介绍

现任职于某头部网络安全企业攻防研究部，核心红队成员。2021-2023年间累计参与40+场国家级、行业级攻防实战演练，精通漏洞挖掘、红蓝对抗策略制定、恶意代码分析、内网横向渗透及应急响应等技术领域。在多次大型演练中，主导突破多个高防护目标网络，曾获“最佳攻击手”“突出贡献个人”等荣誉。

已产出的安全工具及成果包括：

* 多款主流杀软通杀工具（兼容卡巴斯基、诺顿、瑞星、360等终端防护，无感知运行，突破多引擎联合检测）
* XXByPassBehinder v1.1 冰蝎免杀生成器（定制化冰蝎免杀工具，绕过主流终端防护与EDR动态检测，支持自定义载荷）
* 哥斯拉二开免杀定制版（二开优化，深度免杀，突破终端防护与EDR检测，适配多场景植入）
* NeoCS4.9终极版（高级免杀加载工具，强化载荷注入与进程劫持，适配多系统版本，无兼容问题）
* WinDump\_免杀版（浏览器凭证窃取工具，支持Chrome/Edge/Firefox等主流浏览器，一键提取敏感数据，免杀过防护）\_
* \_DumpBrowser\_V1\_免杀版（浏览器凭证窃取工具，专攻浏览器密码、Cookie、历史记录提取，免杀性能拉满）
* fscan二开版（二开优化内网扫描工具，增强指纹精度、弱口令爆破与结果标准化输出，适配复杂内网）
* RingQ加载器二开版（二开优化免杀加载器，支持Shellcode内存执行，绕过各类终端防护与EDR检测）
* 多款免杀Webshell集合（覆盖PHP/JSP/ASPX，过主流WAF与终端防护，适配不同Web场景）
* 免杀360专属加载器（支持Shellcode内存执行，针对性绕过360全系防护检测，无感知运行）
* 一键Kill 火绒 defender 工具 **HDKiller**（包含源码）
* win11 一键kill 360工具 **InjectKill**（包含源码）
* win11 一键kill defender工具**win11\_df-killer**（包含源码）

后续将不断更新到内部圈子中 欢迎加入圈子 ![image](https://mmbiz.qpic.cn/mmbiz_jpg/SffY5ZO3R2nhghttp9mQhic3LJWsCj8Jb4QWibnjmRqic7M9W746srJZlLKQg6mmV7cKrwhWCOauLlJPzLzry0iaRQ/640?wx_fmt=jpeg&from=appmsg&watermark=1#imgIndex=7 "image")

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/SffY5ZO3R2kDRUZoVyoQSFNmAaYwluEFTjXAgQILjvqxkG8dwdfCP3ia9vzvl09Te62lH6VjoGcL2txzs1NZE4Q/0?wx_fmt=png)

星夜AI安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/SffY5ZO3R2kDRUZoVyoQSFNmAaYwluEFTjXAgQILjvqxkG8dwdfCP3ia9vzvl09Te62lH6VjoGcL2txzs1NZE4Q/0?wx_fmt=png)

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
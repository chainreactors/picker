---
title: SSHYard：免费开源的 SSH / SFTP 客户端，把 AI 助手放进终端里
url: https://blog.upx8.com/SSHYard-SSH-SFTP-AI
source: 黑海洋 - AI工具与技术教程｜免费资源与开发实战
date: 2026-11-06
fetch_date: 2026-11-07T08:00:38.407585
---

# SSHYard：免费开源的 SSH / SFTP 客户端，把 AI 助手放进终端里

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
SSHYard：免费开源的 SSH / SFTP 客户端，把 AI 助手放进终…

# SSHYard：免费开源的 SSH / SFTP 客户端，把 AI 助手放进终端里

[资源](https://blog.upx8.com/Free)
11-06
·
约 7 分钟
·
黑海洋
·

5,303

管几台服务器的人大概都有这个体验：终端开一个窗口，传文件再开一个 SFTP 窗口，看负载又得 ssh 进去敲 `top`。遇到 nginx 502，先查进程、再看配置、改完重启，来回切半天。

SSHYard 想把这些塞进一个窗口：**终端 + SFTP + 网络转发 + 备份 + AI 助手**，一款免费开源的原生桌面应用，支持 macOS、Windows 和 Linux。

![左侧主机列表 + 终端 + 右侧 AI 助手，AI 用表格汇报内存占用](https://i0.wp.com/cdn.skyimg.net/up/2026/11/6/c678caef13911e584c3d27ea714324f8.webp)

关键数据先说：**安装包 7–12 MB，原生绘制不走 WebView，AGPL-3.0 开源，无需注册账号，凭据本地加密。**

## 一句话说清它和别的 SSH 客户端有什么不同

市面上的 SSH 客户端大致分两类：终端模拟器（iTerm2、Windows Terminal）只管终端，SFTP 得另找工具；图形化客户端（Termius、FinalShell 一类）功能齐全但不少是 Electron 打包，体积上百 MB，且云同步意味着凭据要出门。

SSHYard 的差异点在两处：

1. **原生绘制**，不内置浏览器内核，所以安装包只有 7–12 MB。
2. **AI 助手贴着终端跑**，通过同一条 SSH 连接执行命令、编辑文件，而不是在另一个聊天窗口里给你复制粘贴建议。

## 核心功能

### 终端

* 多标签、分屏与终端搜索，支持真彩色、宽字符和输入法。
* **tmux、vim、htop 都能用鼠标操作**。
* 同一主机的多个面板共享一条连接，不重复建连。
* 断线后自动重连。

### SFTP 文件管理

* 远程文件面板就在终端旁边，**可以跟随终端的当前目录**。
* 内置编辑器，直接改远程文件，不用 `vi` 上去慢慢来。
* 支持拖放，整个文件夹也能传。
* 传输队列支持暂停、续传和重试。

![SFTP 双栏：左侧本地目录，右侧远程目录](https://i0.wp.com/cdn.skyimg.net/up/2026/11/6/7e2756525e210cae0cc76df153f0bf46.webp)

### 网络连接

* 多级跳板机。
* HTTP 与 SOCKS5 代理。
* 本地、远程和动态端口转发。

### 主机与凭据

* 从 SSH 配置文件导入，或直接输入 `user@host:port` 连接。
* 支持密码、OpenSSH / PEM / PuTTY 密钥与 SSH Agent。
* 可生成密钥并一键安装公钥。
* 凭据在本地加密保存。

### 备份与恢复

* 用密码加密备份主机、凭据、快捷指令和设置。
* 保存到本地、WebDAV、S3 兼容存储或 GitHub 私密 Gist。
* 支持手动或定时备份，可设置保留份数。
* 在另一台设备上恢复。

### 日常体验

* CPU、内存、磁盘、网络和延迟一目了然。
* 浅色与深色主题，可跟随系统。
* 五种界面语言（英、简中、繁中、日、韩）。

![系统监控面板：CPU、内存、网络各接口、磁盘](https://i0.wp.com/cdn.skyimg.net/up/2026/11/6/443b72469766c1e140a8bde2ac459c09.webp)

## AI 助手：能动手，但主动权在你

这是它最值得说清楚的部分，因为"AI 能操作服务器"听起来就让人紧张。SSHYard 的设计是把控制权切得很细。

**它怎么工作**：每台主机有独立的助手，助手能看到该主机的终端上下文，并通过**同一条 SSH 连接**执行命令、编辑文件。

**三种权限模式**：

| 模式 | 行为 |
| --- | --- |
| 询问 | 每次执行命令或修改文件前都征求你同意 |
| 自动审核 | 每个操作交给审核模型检查，模型允许才执行；要求确认或审核失败时转来问你 |
| 完全允许 | 必须由你明确开启 |

审核模型还能设**严格程度**：宽松 80%、标准 90%、严格 97%，对应决策模型判定操作安全所需的把握。

**用你自己的模型**：可接入任何支持 OpenAI 兼容 Chat Completions、OpenAI Responses 或 Anthropic Messages 接口的服务，包括自己部署的模型。终端输出和文件内容只发送给你选择的服务，**而且要先在该主机上得到你的同意**才能发。

![AI 助理设置：权限模式、审核模型、严格程度、模型服务商](https://i0.wp.com/cdn.skyimg.net/up/2026/11/6/ca1e9b36d86acfc63c92c02664485ae1.webp)

设置里还有两个实用开关：**终端上下文行数**（默认 200 行）决定 AI 能看到多少历史输出；**脱敏**在发送给模型前遮盖疑似私钥和令牌。

## 让 Claude Code / Codex 用你的主机

这个功能比较少见：开启「智能体接入」后，本机的 AI 智能体可以通过**开放 API、MCP 端点或 SSHYard Skill** 查看主机、建立 SSH 连接、执行命令。

* 为 Claude Code、Codex 一键配置 Skill。
* 每条命令记入 AI 审计日志（默认保留 90 天）。
* 重新生成令牌即可断开所有智能体。
* **默认关闭**，由你决定是否开启。

最关键的一句：**智能体拿到的是令牌，不是你保存的密码和密钥。** 凭据始终留在 SSHYard 内。

## 安全模型：四层，逐层说得清

1. **系统钥匙串**：只为 SSHYard 保存一把随机生成的 256 位主密钥，别无他物。
2. **本地加密凭据库**：密码、私钥、口令、快捷指令和 API 密钥都用这把主密钥加密，存在一个本地文件里。
3. **密封备份**：备份在本机完成压缩和加密，密钥由你的密码通过 **Argon2id** 派生，使用 **XChaCha20-Poly1305** 加密。
4. **你的存储**：WebDAV、S3 兼容存储和 GitHub Gist 只会收到加密后的文件，**备份密码本身从不保存**。

翻译成大白话：密码不上云、不进账号体系，系统只认你这台机器上的那把主密钥；备份出门前已经上锁，丢了备份文件也没用，除非对方知道你的备份密码。

## 规格一览

| 项目 | 内容 |
| --- | --- |
| 价格 | 免费 |
| 许可证 | GNU AGPL-3.0 |
| 平台 | macOS 12+（Apple 芯片与 Intel）、Windows、Linux（均含 x64 与 Arm64） |
| 界面 | 原生绘制，不使用 WebView |
| 安装包 | 约 7–12 MB |
| 语言 | English、简体中文、繁體中文、日本語、한국어 |
| 账号 | 无需注册 |
| 凭据 | 加密保存在本机 |
| AI 服务 | 任意 OpenAI 兼容 / OpenAI Responses / Anthropic 接口 |
| 智能体接入 | 开放 API、MCP 与 Skill，默认关闭 |

## 下载

当前版本 **0.0.19**，发布于 2026 年 11 月 6 日。全部构建产物都在 GitHub Releases，官方提供 SHA256SUMS 校验文件。

**macOS**（12 及以上，已签名并通过公证）

* [Apple 芯片 8.7 MB](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL0xpY295L3NzaHlhcmQvcmVsZWFzZXMvZG93bmxvYWQvdjAuMC4xOS9zc2h5YXJkLTAuMC4xOS1hcm02NC5kbWc)
* [Intel 10.0 MB](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL0xpY295L3NzaHlhcmQvcmVsZWFzZXMvZG93bmxvYWQvdjAuMC4xOS9zc2h5YXJkLTAuMC4xOS1hbWQ2NC5kbWc)

**Windows**（x64 / Arm64，无需管理员权限）

* [x64 安装程序 8.9 MB](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL0xpY295L3NzaHlhcmQvcmVsZWFzZXMvZG93bmxvYWQvdjAuMC4xOS9zc2h5YXJkLXNldHVwLTAuMC4xOS1hbWQ2NC5leGU)
* [x64 绿色版 ZIP 11.6 MB](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL0xpY295L3NzaHlhcmQvcmVsZWFzZXMvZG93bmxvYWQvdjAuMC4xOS9zc2h5YXJkLTAuMC4xOS13aW5kb3dzLWFtZDY0LXBvcnRhYmxlLnppcA)
* [Arm64 安装程序 7.6 MB](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL0xpY295L3NzaHlhcmQvcmVsZWFzZXMvZG93bmxvYWQvdjAuMC4xOS9zc2h5YXJkLXNldHVwLTAuMC4xOS1hcm02NC5leGU)
* [Arm64 绿色版 ZIP 10.4 MB](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL0xpY295L3NzaHlhcmQvcmVsZWFzZXMvZG93bmxvYWQvdjAuMC4xOS9zc2h5YXJkLTAuMC4xOS13aW5kb3dzLWFybTY0LXBvcnRhYmxlLnppcA)

**Linux**（.deb 安装包或 .tar.gz 压缩包）

* [x64 .deb 11.5 MB](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL0xpY295L3NzaHlhcmQvcmVsZWFzZXMvZG93bmxvYWQvdjAuMC4xOS9zc2h5YXJkXzAuMC4xOV9hbWQ2NC5kZWI)
* [x64 .tar.gz 11.6 MB](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL0xpY295L3NzaHlhcmQvcmVsZWFzZXMvZG93bmxvYWQvdjAuMC4xOS9zc2h5YXJkLTAuMC4xOS1saW51eC1hbWQ2NC50YXIuZ3o)
* [Arm64 .deb 10.5 MB](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL0xpY295L3NzaHlhcmQvcmVsZWFzZXMvZG93bmxvYWQvdjAuMC4xOS9zc2h5YXJkXzAuMC4xOV9hcm02NC5kZWI)
* [Arm64 .tar.gz 10.6 MB](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL0xpY295L3NzaHlhcmQvcmVsZWFzZXMvZG93bmxvYWQvdjAuMC4xOS9zc2h5YXJkLTAuMC4xOS1saW51eC1hcm02NC50YXIuZ3o)

其他：[全部下载与安装说明](https://blog.upx8.com/go/aHR0cHM6Ly9zc2h5YXJkLmNvbS96aC1oYW5zL2Rvd25sb2FkLw) · [更新日志](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL0xpY295L3NzaHlhcmQvcmVsZWFzZXMvdGFnL3YwLjAuMTk) · [SHA256SUMS](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL0xpY295L3NzaHlhcmQvcmVsZWFzZXMvZG93bmxvYWQvdjAuMC4xOS9TSEEyNTZTVU1T)

## 上手顺序

1. 装好打开，主机列表为空。
2. 从 SSH 配置导入，或点「+」输入 `user@host:port`。有密钥的选密钥类型，没有的可以让它生成并一键装公钥。
3. 连上后终端就是主界面，右键或顶部按钮开分栏：新终端、SFTP、系统监控。
4. 想用 AI：偏好设置 → AI 助理，先加一个模型服务商（填 API 地址和 Key），再选默认权限模式（建议先用「询问」）。
5. 想给 Claude Code 用：MCP / Skill 页面开启智能体接入并生成令牌，一键装 Skill。

## 适合谁

**适合**：手上有多台服务器、每天要在终端和文件之间来回切的人；受不了 Electron 客户端体积的人；想用 AI 搭把手但不愿意把私钥交给第三方云服务的人。

**要先想清楚**：

* **版本号还在 0.0.19**，属于早期阶段，接口和界面会变，生产环境主力工具建议先并行跑一段时间。
* **AI 功能要自备 API Key**，token 费用算你自己的，本地模型也能接但要有算力。
* **AGPL-3.0 不是随便用**：自己用没问题，改完对外提供服务要开源。
* 智能体接入一旦打开，等于给本机 AI 开了操作服务器的权限，令牌管理和审计日志要当正经事对待。

## 参考链接

* [官网（中文）](https://blog.upx8.com/go/aHR0cHM6Ly9zc2h5YXJkLmNvbS96aC1oYW5zLw)
* [GitHub 仓库 Licoy/sshyard](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL0xpY295L3NzaHlhcmQ)
* [下载页与安装说明](https://blog.upx8.com/go/aHR0cHM6Ly9zc2h5YXJkLmNvbS96aC1oYW5zL2Rvd25sb2FkLw)
* [v0.0.19 更新日志](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL0xpY295L3NzaHlhcmQvcmVsZWFzZXMvdGFnL3YwLjAuMTk)

收藏

分享

报告错误

分享这篇文章

微信扫一扫

在手机上继续阅读

复制

扫码后直接打开这一页

[安全](https://blog.upx8.com/tag/%E5%AE%89%E5%85%A8/)
[客户端](https://blog.upx8.com/tag/%E5%AE%A2%E6%88%B7%E7%AB%AF/)
[ssh](https://blog.upx8.com/tag/ssh/)
[免费开源](https://blog.upx8.com/tag/%E5%85%8D%E8%B4%B9%E5%BC%80%E6%BA%90/)
[AI](https://blog.upx8.com/tag/AI/)

[上一篇
OpenAI发布GPT-6 Cyber安全模型：漏洞挖掘和攻防边界管控能力跃升](https://blog.upx8.com/OpenAI%E5%8F%91%E5%B8%83GPT-6-Cyber-%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8AI%E8%83%BD%E5%8A%9B%E8%B7%83%E5%8D%87)
[下一篇
Ai抗议者闯入微软阿姆斯特丹数据中心工地](https://blog.upx8.com/%E6%8A%97%E8%AE%AE%E8%80%85%E9%97%AF%E5%85%A5%E5%BE%AE%E8%BD%AF%E9%98%BF%E5%A7%86%E6%96%AF%E7%89%B9%E4%B8%B9%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83%E5%B7%A5%E5%9C%B0)

## 相关文档

* [赵长鹏称币安可能遭遇史上最大规模加密货币盗窃案
  10-30](https://blog.upx8.com/%E8%B5%B5%E9%95%BF%E9%B9%8F%E7%A7%B0%E5%B8%81%E5%AE%89%E5%8F%AF%E8%83%BD%E9%...
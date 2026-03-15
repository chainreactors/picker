---
title: CyberStrikeAI 新增 WebShell 助手功能说明
url: https://mp.weixin.qq.com/s/E0tleX3mF4bLCjmLYxFgZA
source: Doonsec's feed
date: 2026-03-14
fetch_date: 2026-03-15T04:32:35.502329
---

# CyberStrikeAI 新增 WebShell 助手功能说明

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ufQ2xnAD33uIJzzibZMS0HmQ6YiaDK6lq6eN6icJICdwQic0opA0YPW7rc9ibpIwgEddGUmwgEFWwv30xGSFGnRHyFkQY6daKibtfAibSMhz9nR9I0/0?wx_fmt=jpeg)

# CyberStrikeAI 新增 WebShell 助手功能说明

原创

学安全也就图一乐
学安全也就图一乐

低调学安全

![]()

在小说阅读器中沉浸阅读

CyberStrikeAI 在现有 WebShell 管理（虚拟终端、文件管理）基础上，新增 **WebShell 助手** 功能。在每条 WebShell 连接下，可通过自然语言向 AI 下达指令，由 AI 在当前连接上执行命令、列目录、读写字件，并将对话历史按连接分别保存，便于多目标排查与后续复盘。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ufQ2xnAD33ul8FJfDHTF8ibF4c6Pay9gnjgNokicFGe6vfUd0Vw0kNiae2lCdictF78GgAGUB9MYNgo8wia5ducCjuob2vYbG87E3E9S3ASSK69E/640?wx_fmt=png&from=appmsg)

---

## 一、CyberStrikeAI 与 WebShell 管理

CyberStrikeAI 是一款 **AI 原生安全测试平台**，基于 Go 构建，集成 100+ 安全工具、智能编排引擎、角色化测试与 Skills 技能系统，支持通过对话完成漏洞发现、攻击链分析、知识检索与结果可视化，过程可审计、可追溯。

平台内的 **WebShell 管理** 支持添加与管理 WebShell 连接（兼容冰蝎、蚁剑等），包含 **常规的虚拟终端**（手动执行命令、命令历史、清屏等）和 **内置文件管理**（列目录、读写字件、上传下载、新建/删除/重命名等）。本次新增的 **WebShell 助手** 在此基础上，为每条连接提供独立的 AI 对话能力：用户用自然语言描述需求，AI 在当前选中的连接上调用相应能力并返回结果。虚拟终端、文件管理与 AI 助手可在同一界面按需切换使用。

---

## 二、WebShell 助手功能说明

使用入口：**WebShell 管理 → 选择一条连接 → AI 助手** 标签页。

助手根据当前选中的 WebShell 连接进行操作，支持以下四类能力；每条连接拥有独立的对话历史，在侧边栏可按连接查看与切换会话。

### 1. 执行命令（webshell\_exec）

用户可用自然语言请求在当前机器上执行命令，例如「执行 whoami」「查看当前用户 id」。
AI 通过 `webshell_exec` 在当前连接上执行对应命令，并将标准输出与错误信息返回至对话。适用于快速确认权限、环境信息等场景。

### 2. 列目录（webshell\_file\_list）

用户可请求列出指定路径的目录内容，例如「列出当前目录」「查看 /var/www 下有哪些文件」。
AI 通过 `webshell_file_list` 在当前连接上列出目录，并将结构整理后展示。适用于梳理站点目录、定位上传目录或配置文件。

### 3. 读文件（webshell\_file\_read）

用户可请求读取指定文件内容，例如「读取 config.php」「查看 /etc/passwd 前 20 行」。
AI 通过 `webshell_file_read` 在当前连接上读取文件并返回内容。适用于查看配置、密钥或进行简单的代码、日志分析。

### 4. 写文件（webshell\_file\_write）

用户可请求在指定路径写入内容，例如「在 /tmp 下创建 test.txt，内容为 hello」。
AI 通过 `webshell_file_write` 在当前连接上完成写入。适用于创建小脚本、测试文件或简单持久化与调试。

**说明：** 助手仅对「当前选中的 WebShell 连接」生效，不会与其他连接混淆；对话按连接维度持久化，便于多目标、多轮测试时的区分与回溯。

---

## 三、与虚拟终端、文件管理的区别

| 能力 | 虚拟终端 / 文件管理 | WebShell 助手 |
| --- | --- | --- |
| 操作方式 | 手动输入命令、点击界面 | 自然语言描述需求 |
| 适用场景 | 精确控制、逐条执行 | 快速试探、多轮追问、减少命令记忆 |
| 历史与上下文 | 命令历史、当前路径 | 按连接保存的对话与多轮上下文 |
| 多目标管理 | 需手动切换连接 | 切换连接即切换当前 Shell，会话随之切换 |

虚拟终端与文件管理适合需要精确控制的场景；WebShell 助手适合用自然语言描述意图、由 AI 在当前连接上执行并保留对话记录，便于复盘与报告编写。两者可配合使用。

---

## 四、使用步骤

1. **添加 WebShell 连接**
   在 Web 端进入 **WebShell 管理**，添加 Shell 地址、密码/密钥、类型（PHP/ASP/ASPX/JSP 或自定义）、请求方式、命令参数等（兼容冰蝎、蚁剑等）。添加后可点击 **测试连通性** 校验连接是否可用。
2. **打开 AI 助手**
   在左侧选中一条连接，切换到 **AI 助手** 标签页。
3. **输入需求**
   在输入框中用自然语言描述需求，例如「列出当前目录」「执行 whoami」「读取网站根目录下的 config.php」。
   AI 会在当前连接上调用相应工具（执行命令、列目录、读写字件），并将结果展示在对话中。
4. **多轮对话与多连接**
   同一连接下可连续多轮提问（如「再往上一级」「读取 db.php」）；切换连接即切换目标 Shell，侧边栏会展示该连接下的历史会话，可切换查看。
   连接与 AI 会话均持久化至 SQLite，服务重启后仍可继续使用。

---

## 五、总结

* **自然语言操作**：在当前 Shell 上执行命令、列目录、读写字件，无需记忆具体命令格式。
* **按连接隔离**：每条 WebShell 对应独立对话历史，多目标场景下不会混淆。
* **与现有能力统一**：与虚拟终端、文件管理、平台工具链处于同一界面，可按需切换使用。
* **可审计与追溯**：对话历史按连接保存，便于复现与报告。

WebShell 管理模块（虚拟终端、文件管理、AI 助手）后续会持续迭代，增加更多能力与体验优化，欢迎关注与反馈。

更多部署与配置说明见项目 README（中文 / English），

开源地址：https://github.com/Ed1s0nZ/CyberStrikeAI

欢迎 Star 与反馈。

---

*CyberStrikeAI · AI 原生安全测试平台 · WebShell 管理 + 虚拟终端 + 文件管理 + WebShell 助手*

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/KzNYA6icKe6ny3nDMkDelsYYnPJzRX2erWFEia2S7Bqqc7CjicEpJYQtId7a2jXKCial6Mw8ck8IFQEqmZnldrG2EQ/0?wx_fmt=png)

低调学安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/KzNYA6icKe6ny3nDMkDelsYYnPJzRX2erWFEia2S7Bqqc7CjicEpJYQtId7a2jXKCial6Mw8ck8IFQEqmZnldrG2EQ/0?wx_fmt=png)

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
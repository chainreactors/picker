---
title: AI 赋能 哥斯拉 MCP 插件：联动 Claude 打造红队 Webshell 自动化作战工具
url: https://mp.weixin.qq.com/s/do7uYAuHkyLr07tP4SahMw
source: Doonsec's feed
date: 2026-06-18
fetch_date: 2026-06-19T07:05:58.976655
---

# AI 赋能 哥斯拉 MCP 插件：联动 Claude 打造红队 Webshell 自动化作战工具

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/siavMjWic5FZWHyXIF8xWp1kzBA4dDPqbKrLiamB8HVbsFGZ51UAYAnBDwuwt3uDZicBRPgk9MNfEiaFkMbKNqDWRvDLaibD6VR5zsHAIk1xKAU3s/0?wx_fmt=jpeg)

# AI 赋能 哥斯拉 MCP 插件：联动 Claude 打造红队 Webshell 自动化作战工具

原创

Pop
Pop

RedTeam回忆录

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 基于 Godzilla 插件系统，通过 MCP 协议对接 Claude

---

## 🔥 核心

| 方案 | 依赖 | 说明 |
| --- | --- | --- |
| ✅ **本方案** | **Godzilla 插件（内置 MCP Server）+ Claude** | **一个 JAR 搞定，零依赖** |

---

## 🏗️ 架构

```
🖥️ Claude Desktop / Claude Code
    ↕  📡 MCP Protocol (HTTP :12306)
🦎 Godzilla Plugin (Java, 内置 MCP Server)
    ↕  🔌 Godzilla Core API
🎯 Webshell Sessions → 目标服务器
```

> 💡 MCP Server 直接内嵌在 Java 插件中，使用 JDK 自带的 com.sun.net.httpserver，完整实现 MCP 2024-11-05 协议规范。所有端口只监听 127.0.0.1，不对外暴露。

---

## 🛠️ MCP 工具清单（25 个）

### 🔗 连接管理

| 工具名 | 功能 |
| --- | --- |
| `godzilla_connect` | 连接 Webshell，获取 session\_id |
| `godzilla_test_connection` | 测试连接是否存活 |
| `godzilla_list_sessions` | 列出所有活跃会话 |
| `godzilla_disconnect` | 断开会话 |

### 📊 信息收集

| 工具名 | 功能 |
| --- | --- |
| `godzilla_server_info` | 服务器信息（OS/版本/架构/用户） |
| `godzilla_whoami` | 当前用户身份 |
| `godzilla_network_info` | 网络信息（IP/网卡/连接） |
| `godzilla_process_list` | 进程列表 |

### ⚡ 命令执行

| 工具名 | 功能 |
| --- | --- |
| `godzilla_exec_cmd` | 执行系统命令 |
| `godzilla_exec_code` | 执行自定义代码（PHP/JSP/ASP/ASPX） |

### 📁 文件操作

| 工具名 | 功能 |
| --- | --- |
| `godzilla_list_files` | 列出目录内容 |
| `godzilla_read_file` | 读取文件（返回 base64） |
| `godzilla_write_file` | 写入文件 |
| `godzilla_upload_file` | 上传本地文件到目标 |
| `godzilla_download_file` | 从目标下载文件 |
| `godzilla_delete_file` | 删除文件 |

### 🗄️ 数据库操作

| 工具名 | 功能 |
| --- | --- |
| `godzilla_db_connect` | 通过 Webshell 连接内网数据库 |
| `godzilla_db_query` | 执行 SQL 查询 |
| `godzilla_db_databases` | 列出所有数据库 |
| `godzilla_db_tables` | 列出表 |
| `godzilla_db_columns` | 获取表结构 |
| `godzilla_db_types` | 列出支持的数据库类型 |

> 📌 支持数据库：MySQL / PostgreSQL / MSSQL / Oracle / SQLite

### 👻 内存马管理

| 工具名 | 功能 |
| --- | --- |
| `godzilla_inject_memshell` | 注入内存马（Servlet/Filter/Listener/Valve） |
| `godzilla_list_memshells` | 列出已注入的内存马 |
| `godzilla_kill_memshell` | 清除内存马 |

---

## 🎯 使用场景

### 📍 场景一：快速信息收集

```
你：连一下 http://target.com/cmd.jsp 密码 pass JSP 类型
Claude：✅ 已连接，Windows Server 2012 R2，用户 SYSTEM

你：网络配置看一下
Claude：🌐 三个网卡，内网段 10.0.0.0/24、172.16.0.0/16

你：有没有杀软
Claude：🛡️ tasklist 未发现常见杀软进程

你：跑着什么服务
Claude：📦 Tomcat 9、MySQL 5.7、Redis 6.0
```

⏱️ 四个问题，三十秒，目标全貌出来。

### 📍 场景二：内网数据库渗透

```
你：通过 shell 连一下 192.168.1.100 的 MySQL，root/123456
Claude：✅ 已连接，MySQL 5.7.38

你：看看有哪些库
Claude：🗄️ webapp, crm, hr, mysql, information_schema...

你：crm 库有什么表
Claude：📋 customers, orders, payments, users...

你：users 表查一下有没有管理员
Claude：🔍 找到 role='admin' 的记录 3 条

你：config 表看看有没有敏感配置
Claude：🔑 发现 db_password=admin@123, api_key=sk-xxx...
```

💬 整个渗透链路，你就是在和 Claude 聊天。Claude 不只是把结果倒出来，会自动帮你标出敏感信息。

### 📍 场景三：翻文件找密码

```
你：把桌面文件列一下
Claude：📂 flag.txt, passwords.xlsx, backup.zip, notes.txt

你：notes.txt 读一下
Claude：🔑 VPN 账号 vpnuser/vpn@2024，域控 10.0.0.1

你：passwords.xlsx 下载到本地
Claude：✅ 已下载，24KB
```

### 📍 场景四：内存马注入

```
你：注入一个 Filter 内存马，URI /api/v2/auth，密码 rebeyond
Claude：👻 已注入，type: filter, uri: /api/v2/auth

你：看看现在有哪些内存马
Claude：📋 [Filter: /api/v2/auth (active)]
```

### 📍 场景五：exec\_code 执行自定义代码

| 目标类型 | 执行方式 |
| --- | --- |
| 🐘 PHP | ob\_start + eval，支持任意 PHP 代码 |
| 📄 ASP (VBScript) | ExecuteGlobal 动态执行 |
| 💎 ASPX (C#) | CSharpEvalCode eval 执行 |
| ☕ Java | 单行命令走 execCommand |

---

## 效果图：

我写的是让他对机器进行评估各位可以改提示词

![](https://mmbiz.qpic.cn/sz_mmbiz_png/siavMjWic5FZWRI98Khp8PySZ1D2Via18EPDReTUMMu4Q6dEdEicpwh7qQgWFEdOzxjNMgKug4qBbmrdHbCFLo6PnXClTjIyRXZrArPPzSzmVz8/640?wx_fmt=png&from=appmsg)

---

## 🔧 技术实现

| 组件 | 技术 | 说明 |
| --- | --- | --- |
| 🧱 插件框架 | Java 8+ | Godzilla 插件标准接口 |
| 🌐 HTTP Server | com.sun.net.httpserver | JDK 内置，零外部依赖 |
| 📡 MCP 协议 | JSON-RPC 2.0 over HTTP | Streamable HTTP Transport |
| 📝 JSON 处理 | Gson 2.10.1 | 打包进 JAR |
| 💻 目标语言 | Java/PHP/ASP/ASPX | 通过 Godzilla Payload 适配 |

---

## 📂 项目结构

```
godzilla-mcp-release/
├── plugins/
│   └── 📦 mcp-plugin-v10.jar     ← 就这一个文件
├── 🖱️ 一键配置Claude.bat         ← 双击配置
└── 📖 README.md                  ← 使用说明

发布包 283KB
```

---

## 🛡️ 安全声明

⚠️ 本工具仅供合法授权的安全研究和渗透测试使用。使用者需确保已获得目标系统的合法授权。未经授权的入侵行为属于违法行为，后果由使用者自行承担。

---

## 📥 工具下载

**💬**关注公众号** 回复 哥斯拉 获取工具下载**

---

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/siavMjWic5FZUiborU5CKEN5fBpNDSSjQ8rFubibvoonLDfTjkyCIPgqHeFsc1xToogAIGQiayreWtkjTNWMK4iciaz7kLSuYSBDeeVCCEt6sdoHYg/0?wx_fmt=png)

RedTeam回忆录

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/siavMjWic5FZUiborU5CKEN5fBpNDSSjQ8rFubibvoonLDfTjkyCIPgqHeFsc1xToogAIGQiayreWtkjTNWMK4iciaz7kLSuYSBDeeVCCEt6sdoHYg/0?wx_fmt=png)

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
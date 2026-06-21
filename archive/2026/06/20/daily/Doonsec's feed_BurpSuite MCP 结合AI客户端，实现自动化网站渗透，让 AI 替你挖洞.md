---
title: BurpSuite MCP 结合AI客户端，实现自动化网站渗透，让 AI 替你挖洞
url: https://mp.weixin.qq.com/s/GdNEEkuj0FxAeJu-hL9BMA
source: Doonsec's feed
date: 2026-06-20
fetch_date: 2026-06-21T06:46:02.860825
---

# BurpSuite MCP 结合AI客户端，实现自动化网站渗透，让 AI 替你挖洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LtibzcRx8GjV2OANlk2yQLiagA4pdNmxetqPYSbY1TDPdsGY3tjerXpq7YTyJSUgNiacf4t6yXibF3RL3KfGpTgb37QO0krDlrtiav8BUs0LloAo/0?wx_fmt=jpeg)

# BurpSuite MCP 结合AI客户端，实现自动化网站渗透，让 AI 替你挖洞

原创

W不懂安全
W不懂安全

W不懂安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

本文围绕 **Burp Suite**、**Burp Suite MCP** 与 **Cherry Studio** 三个核心组件，构建一个让 AI 直接参与 Web 渗透测试的联动环境。

## 1️⃣ 组件介绍

### 🔎 Burp Suite

由 PortSwigger 开发的 Web 安全测试综合平台，通过代理拦截 HTTP/HTTPS 流量，支持请求查看、修改、重放。在渗透测试中承担以下角色：

* 🌐 Web 流量捕获与分析
* ✏️ 参数篡改与漏洞验证
* 🔐 身份认证测试
* 🧭 越权检测
* 💥 通用 Web 漏洞挖掘

传统模式下，这些分析高度依赖人工操作——这正是引入 AI 的动力所在。

---

### 🔌 Burp Suite MCP

**MCP（Model Context Protocol）** 是一种连接 AI 模型与外部工具的协议。
Burp Suite MCP 在此扮演 **AI 与 Burp 之间的桥梁**，将 Burp 内的请求、响应、历史记录及测试上下文通过 MCP 接口暴露给 AI。

通过 MCP，AI 获得了直接「感知」和「操作」Burp 的能力：

* 📥 获取实时 HTTP 请求/响应
* 🔍 分析接口参数与返回内容
* ⚡ 辅助判断潜在漏洞
* 🧠 基于上下文生成测试思路
* ✅ 协助完成漏洞验证流程

它把传统「人 → 工具」的单向操作，升级为「AI ⇄ 工具」的双向协同。

---

### 💻 Cherry Studio

一个支持多模型接入的 AI 客户端，作为本地 AI Agent 的交互入口。在本环境中，它的职责是：

* 🧩 连接大语言模型
* ⚙️ 管理 MCP 服务
* 📤 向 Burp MCP 发送调用指令
* 📊 展现 AI 分析结果

**一句话分工：**

> Cherry Studio 负责调度 AI，Burp Suite 负责执行安全测试，Burp MCP 负责两者之间的数据通信。

---

## 2️⃣ AI 自动化渗透测试原理

核心逻辑：**通过 MCP 将大模型的分析能力与 Burp 的工具能力实时打通。**

### 📌 模式对比

**传统渗透测试流程：**

```
测试人员   ↓手动分析目标   ↓Burp 捕获流量   ↓人工判断漏洞   ↓手动验证
```

**引入 AI 后：**

```
安全目标   ↓Burp Suite 捕获请求   ↓Burp MCP 转换数据   ↓AI 模型分析上下文   ↓生成测试思路   ↓调用 Burp 完成验证   ↓返回结果
```

### 🎯 AI 的三大核心角色

1️⃣ **流量理解**
AI 解析 HTTP 请求/响应内容，识别接口结构、参数含义与潜在风险点。

2️⃣ **漏洞分析**
结合上下文与常见攻击面（SQLi、XSS、权限缺陷、逻辑漏洞等），输出有针对性的测试建议。

3️⃣ **测试辅助**
根据当前请求自动推导下一步测试动作，大幅减少重复性的信息整理与分析工作。

> ⚠️ AI 不是替代渗透测试人员，而是将海量重复劳动自动化，让人的精力聚焦在漏洞验证与攻击链构建上。

---

## 🔧 Burp Suite MCP 插件安装与配置

### 1. 插件安装步骤

1. 启动 Burp Suite，在上方工具栏中找到 **Extensions** 标签，点击进入。
2. 选择 **BApp Store** 子标签。
3. 在搜索框输入 `MCP`，会列出名为 **"MCP Server"** 的插件。
4. 点击右侧的 **Install** 进行下载安装。
   当按钮文字变为 **Reinstall**，且上方工具栏出现 **MCP** 标签时，即表示安装成功。

   > 📌 安装完成后，Burp Suite 工具栏会新增 `MCP` 选项卡。

---

### ![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtibzcRx8GjWcYruvnyXkPWTdFiazwFlhlItjnb6vdksBM7HaO7ic69vOHicv5AUxTPJabBWYUBqRuptHH9VBLhP6uTEAhGhmzXLEpPib0NZUT4g/640?wx_fmt=png&from=appmsg)

**### 2. MCP 配置界面功能说明

该页面用于控制 AI 客户端（如 Cherry Studio）如何连接 Burp Suite，以及 AI 能够调用哪些 Burp 功能。

---

#### ⚙️ Server Configuration（服务端配置）

* **Enabled**
  开启后，Burp Suite 启动 MCP 接口，Cherry Studio 等 AI 客户端即可通过该接口与 Burp 通信。
* **Enable tools that can edit your config**
  允许 AI 修改 Burp Suite 自身配置。
  ⚠️ 该权限可能影响代理、扫描等核心设置，存在一定风险，**通常保持关闭**。
* **Require approval for HTTP requests**
  控制 AI 是否需要人工确认才能发送 HTTP 请求。
  ✅ 开启后，AI 生成的测试请求会先经过用户确认，可有效避免误操作或大量异常请求。
* **Require approval for project data access**
  控制 AI 是否需要授权才能访问 Burp 项目数据。
  🔐 Burp 中保存了大量敏感测试信息（HTTP History、参数、响应内容等），开启后可以防止 AI 直接读取这些数据。

---

#### 📂 数据访问权限

* **Always allow HTTP history access**
  允许 AI 直接读取 HTTP 历史记录。
  ⭐ **这是 AI 分析 Web 流量的核心权限**，开启后 AI 可以获取 Burp 捕获的接口请求，辅助漏洞分析。
* **Always allow WebSocket history access**
  允许 AI 读取 WebSocket 通信数据。
  💡 如果目标存在实时通信功能可以开启；普通 Web 测试场景影响较小。
* **Filter config credentials**
  过滤配置中的敏感信息。
  🔏 开启后会隐藏密码、Token、密钥等内容，避免敏感凭证暴露给 AI。

---

#### 🎯 Auto-Approved HTTP Targets（自动批准目标）

用于配置允许 AI **免确认自动访问**的目标列表。

例如本地靶场：`localhost:8080`、`127.0.0.1`

> 💡 加入后，AI 对这些目标发送请求时无需重复确认。
> ⚠️ 实际测试中建议**只添加已获得明确授权的目标**。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtibzcRx8GjUSxF6jl5uvHVFuwWDibnzSNpGW40xoTvoLg4Ieo8DiaO7EibSpM4pe9KMcyOXpyl1VgZ8skKmia1eoicOmfKDOrUp5Dagf1QxmgUok/640?wx_fmt=png&from=appmsg)

#### 🔧 Advanced Options（高级选项）

* **Server host**
  设置 MCP Server 监听地址。
  默认：`127.0.0.1`，表示仅允许本机连接，安全性更高。
* **Server port**
  设置 MCP 服务端口。
  默认：`9876`，Cherry Studio 连接 Burp MCP 时需使用该地址。

> 🌐 **特殊场景**：如果 Burp Suite 安装在虚拟机中，而 AI 客户端（如 Cherry Studio）安装在本机，则 **Server host** 需修改为 `0.0.0.0`，以允许外部连接。

---

#### 📦 Installation（安装选项）

* **Install to Claude Desktop**
  自动写入 MCP 配置到 Claude Desktop（`claude_desktop_config.json`），让 Claude 可直接调用 Burp。
* **Extract server proxy jar**
  导出 MCP Server 插件文件 `mcp-proxy.jar`。
  🔧 如果不使用 Claude Desktop 或需要手动配置，可提取此 JAR 文件，然后手动加载。

  > 📥 **操作提示：**
  > 此处我们点击 **Extract server proxy jar**，导出 `mcp-proxy.jar`。

![](https://mmbiz.qpic.cn/mmbiz_png/LtibzcRx8GjXPYeibJ1bOkIrByVJiasaJehqNibgaE5N9gK2W41nMw0H6xuxBnPCSZ2JopB9jkYS2fH0ANgsZK1TEdmHBFbg6NRnVtuPibMf06Pk/640?wx_fmt=png&from=appmsg)

## 🔗 Cherry Studio 连接 Burp Suite MCP

### 1. 打开 AI 客户端

启动 **Cherry Studio**（其他支持 MCP 的 AI 客户端配置方式基本类似）。

### 2. 配置 MCP 服务器

进入 **MCP 服务器** 设置界面，新增一条配置。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtibzcRx8GjUyPKexEArX7r5icswzP8JwmzchnichDiaSga1vspZiazh4mv0XV7XO5ib15bztibObM9qAyGSLJeSAST797ufK1ibH3Du7KicFCoqCLx4/640?wx_fmt=png&from=appmsg)

参数如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtibzcRx8GjVOZKqa5cexicLvm5jckZ96sdvep7FD6ZVoCQ1PxEpPlbMpB59zCBAun03hLlib7hiaico20EOpxUbPAbxia0meMz18H51gv4c3clZo/640?wx_fmt=png&from=appmsg)

```
-jarC:\Program Files\mcp-proxy.jar--sse-urlhttp://127.0.0.1:9876
```

> ⚠️ **关键点**：将 `mcp-proxy.jar` 路径修改为你实际存放路径。

### 3. 保存并启动连接

* 点击 **保存** 配置
* 点击 **启动** 按钮

当状态栏出现类似 `Server version: x.x.x` 的版本号提示时，表示 Cherry Studio 已成功连接至 Burp Suite MCP 服务。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtibzcRx8GjUKaYHnYepc2bW6hJicxIFHrPY5VTN2pssZgsawAZD9AbVap1LpahcAB6vib2Wuicric8KeZ1EOKwKkkV4NSsibYAP3yJ5lLnVwVXaQ/640?wx_fmt=png&from=appmsg)

## 🧪 功能验证测试

进入 Cherry Studio 的对话界面，向 AI 发送一条测试指令，例如我发送的：

> “这是我部署的网站后台，现在我需要你使用burp，对 "http://xxx.com”进行......（要做什么），并找出安全问题，最后给我一份报告。

如果 AI 能正确响应并返回 Burp 中的请求数据，以及调用 Burp Suite 各种工具，说明整个链路已经打通，AI 可以正常调用 Burp Suite MCP 进行渗透测试辅助。

![](https://mmbiz.qpic.cn/mmbiz_png/LtibzcRx8GjWsTDap3AeRaONJhhhJacTcDibB23XibRgKkT2riaPYibaoEIIaOCfN6fCq7w2AVu7FssIBguTGictA3U5km2J9OBt4EicTejD3ibkd3E/640?wx_fmt=png&from=appmsg)

## 🎉 结语

至此，一个完整的 **"AI + Burp Suite" 自动化渗透测试环境** 已搭建完成。

在这套体系里，**Cherry Studio** 是 AI 的对话入口，**Burp MCP** 是连接 AI 与工具的桥梁，而 **Burp Suite** 则是真正执行安全测试的武器。三者联动后，测试人员只需用自然语言描述意图，AI 就能完成流量获取、参数分析、测试思路生成甚至部分验证工作。

> ⚡ 让 AI 替你处理海量的重复分析，而你，只需专注于真正的攻击链构建与漏洞研判。

这，就是未来渗透测试的工作方式。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Y4PrZUSw1T9GU9MhK80Q2QsthTRvcxtR5YUibqAQpedfvo4TopCYw1NlLwOWAzC5MXA2XZTqS84pSHdtFjVFNjw/0?wx_fmt=png)

W不懂安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Y4PrZUSw1T9GU9MhK80Q2QsthTRvcxtR5YUibqAQpedfvo4TopCYw1NlLwOWAzC5MXA2XZTqS84pSHdtFjVFNjw/0?wx_fmt=png)

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
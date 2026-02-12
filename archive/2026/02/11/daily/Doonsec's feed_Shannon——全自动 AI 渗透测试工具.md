---
title: Shannon——全自动 AI 渗透测试工具
url: https://mp.weixin.qq.com/s/6wmutbYVWobTC8wY-zyc4g
source: Doonsec's feed
date: 2026-02-11
fetch_date: 2026-02-12T04:18:47.533038
---

# Shannon——全自动 AI 渗透测试工具

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/qqiaD4wiajgFyP9IZYrhqMSZXGWj3RXs73ODDvALLmicVx7KCuVe3SCZYagKQvdKzvDpdjaDFc7cOp4ld9ibj8d5x9262rPedvepTfCZ0TKb9j0/0?wx_fmt=jpeg)

# Shannon——全自动 AI 渗透测试工具

一个人挺好
一个人挺好

一个人挺好 wa

![]()

在小说阅读器中沉浸阅读

## 项目地址：

https://github.com/KeygraphHQ/shannon

## 1. 项目概述

**Shannon** 是一款开源全自动 AI 渗透测试工具，旨在解决现代软件开发中的安全测试缺口问题。

![](https://mmbiz.qpic.cn/mmbiz_png/qqiaD4wiajgFyMJtVWJJdn3Ntxm19uUb37paJZDedZDYUqiau6DEdXc4jaoy9ibA93QqgOrWfexzp5tBcBWGTGPw9baKSJbo8IfibjaSkKWYcROY/640?wx_fmt=png&from=appmsg)

### 1.1 项目定位

表格

| 属性 | 描述 |
| --- | --- |
| **项目名称** | Shannon |
| **开发组织** | KeygraphHQ |
| **许可证** | AGPL-3.0 (Shannon Lite) |
| **GitHub Stars** | 17,000+ |
| **核心定位** | 全自动 AI 渗透测试工具 |
| **技术基础** | Anthropic Claude Agent SDK |

###

### 1.3 核心能力

* **白盒源代码分析**：深入理解应用架构、数据流和认证路径
* **黑盒动态利用**：通过内置浏览器执行真实攻击（注入、认证绕过等）
* **零误报策略**：严格执行"无利用，无报告"（No Exploit, No Report）原则
* **完全自主操作**：从 2FA/TOTP 登录到最终报告生成，全程无需人工干预

---

## 2. 核心特性

### 2.1 功能特性

表格

| 特性 | 描述 |
| --- | --- |
| **全自动操作** | 单命令启动，AI 处理从登录、浏览到报告的所有环节 |
| **渗透测试级报告** | 提供可复现的漏洞利用证明（PoC），消除误报 |
| **OWASP 漏洞覆盖** | 支持 Injection、XSS、SSRF、认证/授权缺陷等关键漏洞类型 |
| **代码感知测试** | 分析源代码指导攻击策略，结合动态利用验证真实风险 |
| **集成安全工具** | 集成 Nmap、Subfinder、WhatWeb、Schemathesis 等侦察工具 |
| **并行处理** | 多漏洞类型并行分析，缩短测试时间 |
| **高级认证支持** | 支持 2FA/TOTP、Google Sign-in 等复杂登录流程 |

### 2.2 技术亮点

* **证明式漏洞验证**：不仅发现潜在问题，而是通过实际执行攻击来验证漏洞可利用性
* **浏览器自动化**：使用真实浏览器进行点击、导航和攻击执行
* **数据流分析**：追踪用户输入到危险 sink 的完整路径
* **命令行集成**：结合浏览器自动化和命令行工具进行深度利用

---

## 3. 系统架构

Shannon 采用**多智能体架构**（Multi-Agent Architecture），模拟人类渗透测试专家的方法论，通过四个阶段完成安全测试：

plain

```
                    ┌──────────────────────┐
                    │    Reconnaissance    │
                    │    (侦察阶段)         │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────┴───────────┐
                    │          │           │
                    ▼          ▼           ▼
        ┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐
        │ Vuln Analysis   │ │ Vuln Analysis   │ │      ...        │
        │  (Injection)    │ │     (XSS)       │ │   (其他漏洞类型)  │
        │   漏洞分析阶段   │ │                 │ │                 │
        └─────────┬───────┘ └─────────┬───────┘ └─────────┬───────┘
                  │                   │                   │
                  ▼                   ▼                   ▼
        ┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐
        │  Exploitation   │ │  Exploitation   │ │      ...        │
        │  (Injection)    │ │     (XSS)       │ │                 │
        │   利用阶段       │ │                 │ │                 │
        └─────────┬───────┘ └─────────┬───────┘ └─────────┬───────┘
                  │                   │                   │
                  └─────────┬─────────┴───────────────────┘
                            │
                            ▼
                    ┌──────────────────────┐
                    │      Reporting       │
                    │      (报告阶段)       │
                    └──────────────────────┘
```

### 3.1 架构阶段详解

#### Phase 1: 侦察（Reconnaissance）

**目标**：构建完整的应用攻击面地图

**执行内容**：

* 源代码分析：理解技术栈、框架和架构
* 基础设施侦察：集成 Nmap、Subfinder 等工具
* 实时应用探索：通过浏览器自动化登录、点击和爬取
* 关联分析：将代码级洞察与实际行为关联

**输出**：详细的入口点、API 端点和认证机制地图

#### Phase 2: 漏洞分析（Vulnerability Analysis）

**目标**：并行识别潜在漏洞

**执行内容**：

* 并行执行：每个 OWASP 类别由专门的智能体处理
* 数据流分析：对 Injection、SSRF 等漏洞进行结构化追踪
* 假设生成：产出**假设的可利用路径**列表

**特点**：此阶段仅生成假设，不验证漏洞

#### Phase 3: 利用（Exploitation）

**目标**：将假设转化为实际证明

**执行内容**：

* 并行利用：各漏洞类型的专门利用智能体同时工作
* 真实攻击执行：使用浏览器自动化、命令行工具和自定义脚本
* **"无利用，无报告"政策**：无法成功利用的假设被标记为误报并丢弃

**关键原则**：只有通过实际攻击验证的漏洞才会进入报告阶段

#### Phase 4: 报告（Reporting）

**目标**：生成专业、可操作的渗透测试报告

**执行内容**：

* 数据整合：合并侦察数据和成功利用证据
* 噪音清理：移除幻觉或弱支持的发现
* PoC 生成：提供可复现的、复制粘贴式的漏洞利用代码
* 结构化输出：生成符合渗透测试标准的综合报告

---

## 4. 快速开始

### 4.1 前置条件

表格

| 需求 | 说明 |
| --- | --- |
| **Docker** | 容器运行时环境 |
| **AI 凭证** | Anthropic API Key 或 Claude Code OAuth Token（推荐 Anthropic） |

### 4.2 环境配置

**设置最大输出令牌数**（防止长报告生成时触发限制）：

bash

```
# 本地运行
exportCLAUDE_CODE_MAX_OUTPUT_TOKENS=64000

# Docker 运行（通过 -e 参数传递）
-eCLAUDE_CODE_MAX_OUTPUT_TOKENS=64000
```

### 4.3 安装步骤

bash

```
# 1. 克隆仓库
git clone https://github.com/KeygraphHQ/shannon.git
cd shannon

# 2. 配置 AI 凭证（二选一）

# 选项 A：环境变量
exportANTHROPIC_API_KEY="your-api-key"
# 或
exportCLAUDE_CODE_OAUTH_TOKEN="your-oauth-token"

# 选项 B：.env 文件
cat> .env <<'EOF'
ANTHROPIC_API_KEY=your-api-key
EOF

# 3. 构建容器
docker build -t shannon:latest .

# 4. 准备目标仓库
# 将目标应用代码放入 ./repos/ 目录
git clone https://github.com/your-org/your-app.git repos/your-app
```

### 4.4 运行渗透测试

bash

```
# 基础命令
./shannon start URL=https://your-app.com REPO=your-app

# 使用配置文件
./shannon start URL=https://your-app.com REPO=your-app CONFIG=./configs/my-config.yaml

# 自定义输出目录
./shannon start URL=https://your-app.com REPO=your-app OUTPUT=./my-reports
```

### 4.5 监控与停止

bash

```
# 查看实时日志
./shannon logs

# 查询特定工作流进度
./shannon query ID=shannon-1234567890

# 打开 Temporal Web UI 进行详细监控
open http://localhost:8233

# 停止所有容器（保留工作流数据）
./shannon stop

# 完全清理（移除所有数据）
./shannon stop CLEAN=true
```

---

## 5. 配置指南

### 5.1 配置文件结构

配置文件放置在 `./configs/` 目录，自动挂载到容器：

yaml

```
# configs/my-app-config.yaml

authentication:
login_type: form
login_url:"https://your-app.com/login"
credentials:
username:"test@example.com"
password:"yourpassword"
totp_secret:"LB2E2RX7XFHSTGCK"# 可选，支持 2FA

login_flow:
-"Type $username into the email field"
-"Type $password into the password field"
-"Click the 'Sign In' button"

success_condition:
type: url_contains
value:"/dashboard"

rules:
avoid:
-description:"AI should avoid testing logout functionality"
type: path
url_path:"/logout"

focus:
-description:"AI should emphasize testing API endpoints"
type: path
url_path:"/api"
```

### 5.2 配置参数说明

表格

| 配置项 | 类型 | 描述 |
| --- | --- | --- |
| `login_type` | string | 登录类型：form, oauth, sso 等 |
| `login_url` | string | 登录页面 URL |
| `credentials` | object | 用户名、密码、TOTP 密钥 |
| `login_flow` | array | 自然语言描述的登录步骤 |
| `success_condition` | object | 登录成功的判断条件 |
| `rules.avoid` | array | 避免测试的路径/功能 |
| `rules.focus` | array | 重点测试的路径/功能 |

### 5.3 本地应用测试

Docker 容器无法直接访问主机的 `localhost`，需使用 `host.docker.internal`：

bash

```
./shannon start URL=http://host.docker.internal:3000 REPO=your-app
```

---

## 6. 使用模式

### 6.1 单仓库应用

bash

```
git clone https://github.com/your-org/your-repo.git repos/your-app
./shannon start URL=https://your-app.com REPO=your-app
```

### 6.2 Monorepo 项目

bash

```
git clone https://github.com/your-org/monorepo.git repos/your-monorepo
./shannon start URL=https://your-app.com REPO=your-monorepo
```

### 6.3 多仓库应用（前后端分离）

bash

```
mkdir repos/your-app
cd repos/your-app
git clone https://github.com/your-org/frontend.git
git clone https://github.com/your-org/backend.git
git clone https://github.com/your-org/api.git

cd../..
./shannon start URL=https://your-app.com REPO=your-app
```

### 6.4 使用现有本地仓库

bash

```
cp-r /path/to/your-existing-repo repos/your-app
./shannon start URL=https://your-app.com REPO=your-app
```

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/AGUhPQZ04zyTvSBegohhPkdl4ZiaID39hGjT55M6GNVWWYfpt8Q146OaDEU4xQ0E4VtxLO4zfGia16VE6qHb001g/0?wx_fmt=png)

一个人挺好 wa

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/AGUhPQZ04zyTvSBegohhPkdl4ZiaID39hGjT55M6GNVWWYfpt8Q146OaDEU4xQ0E4VtxLO4zfGia16VE6qHb001g/0?wx_fmt=png)

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
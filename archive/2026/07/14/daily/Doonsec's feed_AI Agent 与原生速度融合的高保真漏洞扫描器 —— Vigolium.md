---
title: AI Agent 与原生速度融合的高保真漏洞扫描器 —— Vigolium
url: https://mp.weixin.qq.com/s/zc59bWR3OiatN7uIuWyjDw
source: Doonsec's feed
date: 2026-07-14
fetch_date: 2026-07-15T04:42:58.927370
---

# AI Agent 与原生速度融合的高保真漏洞扫描器 —— Vigolium

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/bhUibV7MPZlv281mQiaIBBkialbUvXGvukphwMlNvcH3fNibDX1wdSwX9tDxNaF0VC6l4pjZ1VCxJlEYDKP1FwXOcProskUicDZribYT0Y14ibthuo/0?wx_fmt=jpeg)

# AI Agent 与原生速度融合的高保真漏洞扫描器 —— Vigolium

原创

wolfsec
wolfsec

风铃Sec

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

声明：仅用于授权测试，用户滥用造成的一切后果和作者无关 请遵守法律法规！出于对安全考量本公众号发布的所有文章中的工具均建议放在虚拟机中运行！【无需回复关键字，文中第二部分0x02获取工具】

## 工具简介

**Vigolium** 是一个将 **AI Agent 与原生速度融合** 的高保真漏洞扫描器采用 Go 语言编写。该工具提供两种互补的扫描模式：**Native Scan**（原生扫描）和 **Agentic Scan**（智能体扫描），全面覆盖 OWASP Top 10 及更广泛的安全测试场景。

### 核心能力

| 能力 | 说明 |
| --- | --- |
| **235+ 扫描模块** | 144+ 主动扫描（模糊测试）+ 91+ 被动扫描（模式匹配），覆盖 Injection、访问控制、文件/路径、API/协议、框架特定、云/基础设施及带外攻击（OAST） |
| **Native Scan** | 快速、强大的确定性多阶段扫描，涵盖内容发现、浏览器 SPA 爬取、主动/被动审计 |
| **Agentic Scan** | AI 驱动的自主扫描，自动规划攻击、选择模块、生成自定义扩展、进行源码审计 |
| **OAST 技术** | 通过 interactsh 实现盲 XSS/SSRF/命令注入检测，自动载荷关联 |
| **语义感知变异** | 按语义类型（整数、UUID、JWT、邮箱）对参数分类并按意图变异 |
| **多阶段管道** | 外部信息收集 → 内容发现（Deparos）→ 浏览器/SPA 爬取（Spitolas）→ 审计，支持策略预设和扫描配置文件 |
| **价值感知变异** | 根据参数语义类型智能变异，提高漏洞检出率 |

### 技术亮点

* **原生 Go 构建**

  性能出色，支持并发 Worker 池 + 每主机限速 + 混合内存/磁盘/Redis 队列
* **内置 JS 引擎**

  支持 JavaScript/TypeScript 自定义模块和 Hook，无需重新编译
* **多会话认证**

  支持 CLI 内联、Session 文件、完整登录流程配置，自动测试 IDOR/BOLA
* **Burp Suite 集成**

  通过扩展转发 Burp 流量到 Vigolium Server
* **灵活输入**

  支持 URL、OpenAPI/Swagger、Postman、Burp Suite、cURL、Nuclei JSONL
* **报告生成**

  自动生成自包含 HTML 报告，支持静态报告导出

## 工具使用

### Native Scan 快速开始

```
# 扫描单个目标（默认平衡策略）
vigolium scan -t https://example.com

# 使用深度策略扫描
vigolium scan -t https://example.com --strategy deep

# 仅扫描指定模块
vigolium scan -t https://example.com -m xss-reflected,sqli-error

# 从 OpenAPI 规范扫描
vigolium scan -T openapi.yaml -I openapi

# 从文件管道读取 URL 批量扫描
cat urls.txt | vigolium scan

# 直接运行单个阶段
vigolium run discovery -t https://example.com

# 生成 HTML 报告
vigolium scan -t https://example.com --only discovery --format html -o report.html
```

---

### 认证扫描

```
# CLI 内联会话（name:Header:value）
vigolium scan -t https://example.com \
  --auth "admin:Cookie:session_id=abc123" \
  --auth "user:Cookie:session_id=xyz789"

# 从 YAML/JSON 文件加载会话
vigolium scan -t https://example.com --auth-file ./admin-session.yaml

# 自动登录流程（Cookie/JSON/Header 中提取 Token）
vigolium scan -t https://example.com --auth-file ./login-flow.yaml

# 添加自定义 Header
vigolium scan -t https://example.com -H "Authorization: Bearer token123"
```

---

### Agentic Scan

```
# Autopilot：AI 自主扫描
vigolium agent autopilot -t https://example.com

# 指定源码目录 + 聚焦认证绕过
vigolium agent autopilot -t https://example.com --source ./src --prompt "focus on auth bypass"

# 差异扫描：对比代码变更
vigolium agent autopilot -t https://example.com --diff main...feature/auth

# 指定强度预设
vigolium agent autopilot -t https://example.com --intensity deep

# Swarm：AI 引导的定向扫描
vigolium agent swarm -t https://example.com/api/users --vuln-type sqli

# Swarm：全范围扫描
vigolium agent swarm -t https://example.com --discover

# 源码审计
vigolium agent audit --source ./src --mode deep

# 使用 piolium 驱动
vigolium agent audit --driver=piolium --source ./src --mode balanced
```

---

### Server 模式

```
# 启动 API 服务器（带认证）
vigolium server -k my-secret-key

# 启用透明 HTTP 代理（记录流量）
vigolium server -k my-key --ingest-proxy-port 9003

# 自动扫描接收到的流量
vigolium server -k my-key --scan-on-receive

# 向运行中的服务器导入流量
cat urls.txt | vigolium ingest -s http://localhost:9002

# 导入 OpenAPI 规范
vigolium ingest -s http://localhost:9002 -i api.yaml -I openapi
```

---

### JavaScript 引擎

```
# 执行内联 JavaScript
vigolium js --code 'let r = vigolium.http.get(TARGET); console.log(r.status)' -t https://example.com

# 运行 JS 文件（带超时）
vigolium js --code-file ./my-script.js -t https://example.com --timeout 60s

# 列出加载的扩展
vigolium ext ls

# 浏览 API 文档及代码示例
vigolium ext docs --example

# 安装入门脚本
vigolium ext preset
```

**JS 认证会话示例：**

```
// 创建持久会话（共享 Cookie 池）
let session = vigolium.http.session();
session.post(
"https://app.example.com/login",
JSON.stringify({ user: "admin", pass: "secret" }),
  { headers: { "Content-Type": "application/json" } }
);
session.get("https://app.example.com/dashboard"); // Cookie 自动发送

// 自动登录 + Token 提取
let authed = vigolium.http.login({
url: "https://app.example.com/api/auth",
method: "POST",
body: JSON.stringify({ username: "admin", password: "pass" }),
extract: [{ source: "json", path: "$.token", apply_as: "Authorization: Bearer {value}" }]
});

// IDOR/BOLA 多会话测试
let results = vigolium.http.authTest({
sessions: { admin: adminSession, user: userSession },
requests: [{ method: "GET", url: "https://app.example.com/api/users/1" }]
});
```

## 工具获取

为方便使用，提供构建好的 **vigolium** 工具包（含源码）：

> **🔗 下载链接**：https://pan.quark.cn/s/94dd0a7927a6
>
> **📁 文件名**：`vigolium`

下载后解压即可使用，包含完整可执行文件和相关依赖。

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qGTEdaLg0HmibOdP6ibKTOYNXKuEdbPFJKnX0Z54TIaWXmS6apnB5FYRgZVtWlzvTJK3lQzuxEHTa5kCSibf2eXZw/0?wx_fmt=png)

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
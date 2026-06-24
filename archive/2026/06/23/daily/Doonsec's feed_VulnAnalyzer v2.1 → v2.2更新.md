---
title: VulnAnalyzer v2.1 → v2.2更新
url: https://mp.weixin.qq.com/s/YgTkzNNvzo9UEYIdADa5bQ
source: Doonsec's feed
date: 2026-06-23
fetch_date: 2026-06-24T06:01:46.127617
---

# VulnAnalyzer v2.1 → v2.2更新

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/lVicKnyEkagLU4XMbJjLznA0GYd5mYnJiav30cnl4icXDT2sB3VibvY4jicfChia43ZKWRVxzvN9Wr7MVs3L3kup0jehxuhicQnxXcCv2PEic5UgBxk/0?wx_fmt=jpeg)

# VulnAnalyzer v2.1 → v2.2更新

原创

斯诺克视野
斯诺克视野

卡布奇诺的派对

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

## VulnAnalyzer v2.1 → v2.2 更新日志

### 一、新增漏洞检测能力

#### 1. SSTI（服务端模板注入）检测

* **覆盖引擎**

  ：Jinja2、Twig、Freemarker、Velocity、Thymeleaf、Pebble、Nunjucks、EJS、Smarty、Blade
* **检测模式**

  ：

+ 模板引擎 API 调用（`render_template_string`、`compile`、`process` 等）+ 用户数据
+ 模板语法表达式（`{{...}}`、`${...}`、`#{...}`、`th:text`）+ 用户变量名
+ 参数中包含 SSTI 探测载荷（`{{config.__class__}}` 等）→ CRITICAL 级别
+ URL 参数引用模板文件路径（`?template=index.twig`）

* **CWE/OWASP**

  ：CWE-94 / A03:2021

#### 2. XSS 污染链追踪

* 检测完整的 source→sink 数据流：`URLSearchParams → params.get() → ... → innerHTML`
* 当 DOM 数据源与 DOM 写入点出现在同一作用域（相距 < 1000 字符）时标记为 HIGH 级别
* **新增 XSS source 检测**

  ：`URLSearchParams`、`new URL()`、`window.location.search/hash/href`

#### 3. 链式 SSRF 检测

* 检测 `fetch(profileMeta.dataUrl)` 模式——第一个 API 响应字段被直接用于第二个 fetch
* 标记为 HIGH 级别，含详细验证指导

#### 4. 缺失错误处理检测

* 检测 async 函数缺少 `try/catch` → MEDIUM
* 检测 `fetch()` 调用缺少 `.catch()` → LOW

### 二、用户体验改进

#### 行号定位

* 以前：`"location": "source offset 432"`（晦涩的字符偏移量）
* 现在：`"location": "第2行 第13列"` + `"source_line": "const x = params.get('userId');"`
* 前端新增行号徽章 `2:13` 和代码预览区域

### 三、前端更新

* 新增 SSTI PoC 载荷（Jinja2、Twig、Freemarker、Velocity、Thymeleaf、Smarty）
* 新增 `.line-badge` 和 `.code-preview` 样式
* 每个发现的详情中直接展示源代码行

> 当安全研究员需要快速审查一段代码或一个网站的攻击面时，商业扫描器太重、手工审计太慢——我们需要一个介于两者之间的轻量级工具。这就是 VulnAnalyzer 诞生的原因。 https://github.com/kabuqin/VulnAnalyzer.git

---

## 它能做什么？

VulnAnalyzer 是一个基于 Python + Flask 构建的 Web 安全分析平台，核心能力是**两件事**：

1. **静态代码分析** — 粘贴一段 HTTP 请求、HTML 页面或后端源码，瞬间给出漏洞信号
2. **自动化网站扫描** — 输入目标 URL，自动爬取页面、提取表单和参数、逐页分析安全问题

不需要安装 Burp Suite，不需要配置复杂的扫描策略，打开浏览器就能用。

---

## 为什么造这个轮子？

市面上已经有 OWASP ZAP、Burp Suite、Nuclei 等成熟的扫描工具，但它们各有痛点：

| 工具 | 痛点 |
| --- | --- |
| Burp Suite | 商业版昂贵，社区版功能受限，Java 环境笨重 |
| OWASP ZAP | 启动慢，UI 复杂，对新手不友好 |
| Nuclei | 依赖 YAML 模板，无法做源码级分析 |
| 手工审计 | 准确但效率极低 |

VulnAnalyzer 的定位很明确：**一个能快速启动、能分析源码、能自动爬网站、能给出修复建议的轻量工具**。它不追求零误报（那是商业扫描器的战场），而是追求"5 分钟内让你知道该关注哪些地方"。

---

## 架构设计

整个项目只有 4 个核心文件，不到 3000 行代码：

```
VulnAnalyzer/
├── app.py                 # Flask 服务器 + SSE 流式推送
├── vuln_analyzer.py       # 漏洞检测引擎（2000+ 行，核心）
├── crawler.py             # 网站爬虫 + 表单/参数提取
└── static/
    └── index.html         # 单文件前端 UI
```

### 检测引擎：vuln\_analyzer.py

这是项目的心脏。它采用**纯静态分析**策略——不发送任何攻击载荷，不执行任何代码，只通过正则匹配和模式识别来发现潜在的安全信号。

```
# 检测引擎的核心流程
defanalyze(text, source_name, enabled_types=None):
    message=parse_http_message(text)   # 解析 HTTP 消息结构
    html=FormParser()                  # 解析 HTML 表单/DOM
    html.feed(text)
    params=extract_params(message, text) # 提取所有参数

    # 并行运行 12 个分析器
    findings.extend(analyze_xss(text, html, message, params))
    findings.extend(analyze_sql_injection(text, params))
    findings.extend(analyze_uploads(html, message, text))
    findings.extend(analyze_ssrf(text, params, html))
    findings.extend(analyze_command_injection(text, params))
    # ... 更多分析器
```

每个分析器独立运行，最后通过去重和风险排序合并结果。这种设计让添加新的检测规则变得极其简单——写一个 `analyze_xxx()` 函数就行。

### 爬虫：crawler.py

爬虫采用**广度优先搜索**策略，核心设计考量：

* **智能去重** — 去除 URL fragment（`#section`）后再比较，避免重复爬取
* **资源过滤** — 自动跳过 `.jpg`、`.css`、`.js` 等静态资源
* **表单提取** — 解析每个页面的 `<form>` 标签，记录输入字段和类型
* **参数发现** — 从 URL query string 中提取参数名和值
* **进度回调** — 通过 `on_progress` 回调实时通知上层

### 前端：纯原生 HTML + CSS + JS

没有 React，没有 Vue，没有构建步骤。一个 `index.html` 搞定全部 UI：

* CSS Grid 布局，暗色主题
* SSE（Server-Sent Events）实现实时扫描进度
* 发现卡片支持按风险等级、漏洞类型过滤
* CWE 编号可点击跳转到官方页面
* `Ctrl+Enter` 快捷键触发分析

---

## 能检测什么？

### 通用漏洞（12 类）

| 类型 | 典型检测信号 | 参考标准 |
| --- | --- | --- |
| **XSS** | DOM sink（innerHTML、eval）、模板表达式、缺少 CSP | CWE-79 |
| **SQL 注入** | 字符串拼接 SQL、数据库错误信息泄露 | CWE-89 |
| **命令注入** | os.system、subprocess、shell 元字符 | CWE-78 |
| **路径遍历** | `../` 序列、文件路径参数名 | CWE-22 |
| **SSRF** | URL 构造 API、私有 IP 引用 | CWE-918 |
| **XXE** | XML DOCTYPE、外部实体声明 | CWE-611 |
| **文件上传** | 缺少 accept 过滤的 file input | CWE-434 |
| **开放重定向** | redirect/next/return 参数 | CWE-601 |
| **CORS 错误配置** | 通配符 Origin、Credentials + Wildcard | CWE-942 |
| **敏感信息泄露** | API Key、密钥、信用卡号、堆栈跟踪 | CWE-200 |
| **授权绕过** | 敏感路由无鉴权、角色参数直控 | CWE-285 |
| **安全头缺失** | 缺少 CSP、HSTS、X-Frame-Options 等 | CWE-693 |

### Java 专项（13 类）

当输入被识别为 Java 源码时，自动启用额外的检测规则，覆盖：

* JDBC/JPA/MyBatis SQL 注入
* Runtime.exec / ProcessBuilder 命令注入
* ObjectInputStream / XStream 反序列化
* 弱加密算法（DES、ECB、MD5）
* 硬编码密钥和 IV
* Spring Security 错误配置
* SpEL 表达式注入
* 不安全的类反射加载

---

## 实战演示

### 场景 1：分析一个登录表单

粘贴以下 HTML：

```
<formaction="/login"method="post">
  <inputname="user">
  <inputtype="password"name="pass">
</form>
```

VulnAnalyzer 秒级返回：

```
[LOW] Sensitive Exposure — Password field without autocomplete restriction
       CWE-522 | OWASP A02:2021
       ✓ 设置 autocomplete='current-password' 或 'new-password'
```

### 场景 2：分析一个 HTTP 请求

```
POST/api/search?q=test&sort=nameHTTP/1.1
Host: shop.example.com
Content-Type: application/x-www-form-urlencoded

category=electronics&limit=20
```

检测结果可能包含：

* **SQL Injection**（Medium）— `sort` 参数名暗示 ORDER BY 拼接风险

### 场景 3：扫描整个网站

输入目标 URL → 自动爬取 → 逐页分析 → SSE 实时推送进度到前端：

```
› Initializing scan of https://example.com...
› Starting crawl of https://example.com
› Crawling page 1: https://example.com/
› Crawling page 2: https://example.com/about
› Crawl complete: 12 pages, 3 forms, 8 params
› Analyzing page 1/12: https://example.com/
› ...
› Scan complete! Found 23 issues.
```

---

## 每条发现都包含什么？

VulnAnalyzer 不只是告诉你"这里有漏洞"，它给出一套完整的上下文：

```
{
  "type": "SQL Injection",
  "risk": "high",
  "confidence": "medium",
  "location": "query parameter 'id'",
  "evidence": "Parameter name suggests database-backed filtering",
  "verification": "确认服务端使用了参数化查询...",
  "cwe": "CWE-89",
  "owasp": "A03:2021",
  "tags": ["input-validation", "database"]
}
```

* **Location** — 漏洞在哪里
* **Evidence** — 为什么认为有问题
* **Verification** — 怎么进一步验证（防御性指导，不含攻击代码）
* **CWE / OWASP** — 标准化分类引用
* **Tags** — 便于过滤和分组

---

## 5 分钟上手

```
# 克隆或下载项目
cd VulnAnalyzer

# 安装依赖（只需要两个）
pip install flask requests

# 启动
python app.py

# 打开浏览器访问
# http://127.0.0.1:5000
```

也支持命令行模式：

```
# 分析单个文件
python vuln_analyzer.py request.txt --pretty

# 输出 Markdown 报告
python vuln_analyzer.py response.http --format markdown -o report.md

# 只关注高危以上
cat page.html | python vuln_analyzer.py --min-risk high

# SARIF 格式（可导入 GitHub / VS Code）
python vuln_analyzer.py src.java --format sarif -o results.sarif
```

---

## 设计哲学

### 1. 静态优先，零副作用

VulnAnalyzer 永远不会向目标发送攻击载荷。它只做**信号分析**——"这里有一个模式，看起来像是漏洞信号，请你手动验证"。这使得它对生产环境完全安全。

### 2. 宁可误报，不可漏报

启发式检测必然带来误报，但通过 `confidence`（置信度）和 `risk`（风险等级）两个维度来帮你判断优先级。一个 `critical` + `high confidence` 的发现，值得你立刻关注；一个 `info` + `low confidence` 的信号，可以留到以后看。

### 3. 防御性输出

每个发现都附带 `verification` 字段，告诉你如何从防御角度验证和修复。它不会生成可用的 exploit，因为这是一个帮助防御者的工具。

---

## 性能参考

| 场景 | 耗时 |
| --- | --- |
| 单段代码分析 | 50 ~ 150 ms |
| 单页面爬取 + 分析 | 1 ~ 3 s |
| 30 页完整网站扫描 | 2 ~ 5 min |
| 内存占用 | 50 ~ 100 MB |

---

## 未来可以做什么？

当前版本已经覆盖了常见的 Web 漏洞类别，但仍有很大的扩展空间：

* **JavaScript 渲染支持** — 集成 Playwright/Selenium 处理 SPA 应用
* **认证扫描** — 支持 Cookie / JWT 注入后扫描需要登录的页面
* **WebSocket 分析** — 检测和 fuzz WebSocket 消息
* **CI/CD 集成** — 作为 GitHub Action 或 Git Hook 自动运行
* **协作功能** — 团队共享扫描结果，跟踪漏洞修复状态
* **自定义规则** — 支持 YAML/JSON 格式的自定义检测规则

VulnAnalyzer 不是要替代 Burp Suite 或 Nuclei，而是填补"手工复制粘贴代码到在线工具"和"启动完整扫描器"之间的空白。它的价值在于：

* **安全工程师**：快速审查代码片段，在 code review 阶段就发现问题
* **开发者**：提交代码前自查，减少安全债
* **学生/研究者**：理解漏洞检测的原理，学习安全分析器的实现方式

工具只是辅助，最终的安全判断永远在人。

---

*VulnAnalyzer v2.2 | 仅用于授权安全测试 | Educational Use Only*

公众号后台回复【2912】获取

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/lVicKnyEkagK2ibTjaBexSWkshoEWsC1nvoOmOrHOhKt7VfNENlBOgrOXrf2n3Eibdz3lTPWxp4ckl3u4HjdUiaNgQzCKWsZicG0OjCHic30tm4eo/0?wx_fmt=png)

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
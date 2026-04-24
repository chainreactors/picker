---
title: 100+ 工具 + AI Agent，CyberStrikeAI 重塑安全测试方式
url: https://mp.weixin.qq.com/s/lIPKwZUr1jyRoCKzRz5xvw
source: Doonsec's feed
date: 2026-04-23
fetch_date: 2026-04-24T04:49:20.024273
---

# 100+ 工具 + AI Agent，CyberStrikeAI 重塑安全测试方式

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/4T1PVwJicwkibYRMiaUz1k9NVJdNia0E6ESNkZHM5fbX8wcfpKeEn2MEogFricwCwAvf6T7K773QMN2vGl53iblf3YwZF9kgWZkGL6uaUiaCGaqQw0/0?wx_fmt=jpeg)

# 100+ 工具 + AI Agent，CyberStrikeAI 重塑安全测试方式

原创

Ed1s0nZ
Ed1s0nZ

泷羽Sec-Norsea

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

可堪孤馆闭春寒，杜鹃声里斜阳暮。

```

```

```

```

> ```
> 免责声明
> ```
>
> 本系列工具仅供安全专业人员进行已授权环境使用，此工具所提供的功能只为网络安全人员对自己所负责的网站、服务器等（包括但不限于）进行检测或维护参考，未经授权请勿利用工具中的功能对任何计算机系统进行入侵操作。利用此工具所提供的信息而造成的直接或间接后果和损>失，均由使用者本人负责。
>
> 工具集合：https://pan.quark.cn/s/f113bdb29fd7

## 一、什么是 CyberStrikeAI？

`CyberStrikeAI` 是一款AI 原生安全测试平台，采用 `Go` 语言开发。它将 100+ 款主流安全工具与智能编排引擎相结合，通过 AI Agent 和 MCP 协议，实现从自然语言指令到漏洞发现、攻击链分析、知识检索和结果可视化的端到端自动化。

平台支持角色化测试、技能系统和完整的生命周期管理，为安全团队提供可审计、可追溯、可协作的测试环境。简单来说，`CyberStrikeAI` 让 AI 真正具备了自主安全测试能力，从对话式指令开始，即可驱动完整的安全测试流程。

相比传统的手动测试方式，`CyberStrikeAI`的优势在于：它不仅仅是工具的堆砌，而是通过AI协调这些工具，形成了一个**可审计、可追溯、可协作**的完整测试生态。对于初学者来说，这意味着你可以快速学习安全测试知识；对于专业人士来说，这意味着效率翻倍提升。

## 二、功能介绍CyberStrikeAI

功能丰富且覆盖面广，主要包括以下方面：

* **AI 决策引擎**：兼容 OpenAI 格式的大模型（GPT、Claude、DeepSeek 等），支持智能决策和工具调用

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4T1PVwJicwkib4Ma1TDmhaiamXmIeUJ1NYeSBOJSyMI6UseZYX0IQ5tqUM7hv6U14geJsaS2RP8hUBBFIbwK0iczojSPXo8PaGPjA5MZWpUnHNc/640?wx_fmt=png&from=appmsg)

* **原生 MCP 协议支持**：实现 HTTP、stdio、SSE 等多种传输方式，支持外部 MCP 联邦

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4T1PVwJicwkicHXHQ4YtNvK5SEEfxKeib8SaGibLpgxcKZia0LxDJDLicnsRAVZ06PxfWAhZ85SiayLpuREy9kwBnnFibLics3KFibtEsLTV0sX8aXia1o/640?wx_fmt=png&from=appmsg)

* **100+ 预置工具**：覆盖全杀伤链，包括网络扫描、Web 攻击、漏洞扫描、子域枚举、云安全、容器安全、后渗透等多个领域

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4T1PVwJicwk9BzPMgIMiaMmYNWVartCH680mZFYOicyVpJhN8aiciaQrKBCRMuBqqeicZpWmGGFQMEefoicq0VB4CKw6WKBaAbmncuyKlcnKUmheoA/640?wx_fmt=png&from=appmsg)

* **角色化测试**：内置多种预定义安全角色（如渗透测试、CTF、Web 应用扫描等），可自定义提示词和工具限制

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4T1PVwJicwkicxiajRvIdvRcbrrSzQN4iaeoA3S1JqkQwyZl17tiaSGpllBruTYHTpRvicsPEpo4s5emaKrax0wNalAt8lMKQt7obsKRyicib0Nk6JI/640?wx_fmt=png&from=appmsg)

* **多 Agent 协同**：支持单 Agent ReAct 和多 Agent 模式（Deep、Plan-Execute、Supervisor 等编排方式）

![](https://mmbiz.qpic.cn/mmbiz_png/4T1PVwJicwk870rgWpOGtnMBoozeyibiaK0KygZwZd1icm9RmYib74LQf9b1XTwqNz2krH1ic0JBkfUDNrefDmIQRiaT7lib87Yn9ALQW1h9Dd8zjk8/640?wx_fmt=png&from=appmsg)

* **技能系统**：模块化 Skill 设计，包含 20+ 领域样本（SQLi、XSS、API 安全等）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4T1PVwJicwk8dJicjbvoVcUxA2Ia0NP5cHw1t9mweCZ3VpnIKcoyvOUamn8oeVvU19v313CP3QBuACpSk6ekxgGtKfYk3ntakA4tfyiaiaAkGkI/640?wx_fmt=png&from=appmsg)

* **知识库（RAG）**：支持嵌入向量检索、后处理重排序和可配置预算

![](https://mmbiz.qpic.cn/mmbiz_png/4T1PVwJicwkibM9mWU70VibBqDQdxiaWZbuBRjSqskXnYj3Toib4sibZdGFEOoEeh7FbbvCWAduWq68ZzMibxFDnaODnIkrSVg7YS7C17SzLO40qoY/640?wx_fmt=png&from=appmsg)

* **WebShell 管理**：支持多种类型 WebShell 的虚拟终端、文件管理及 AI 辅助测试

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4T1PVwJicwkicVS57SJ8DHRyFRH62etiaXiasvfMoXSeVibe0gT4ECvtG41hQOB1XICJE4HgOXQGQLpZMeaDJePcJm68FXlc4ds6R9O1BS4K8ORo/640?wx_fmt=png&from=appmsg)

* **漏洞管理**：CRUD 操作、严重程度跟踪、状态流转和统计分析

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4T1PVwJicwkicWqVicVK0NxDTq8bmP4wWEIu1Ob62gycz3gzn9ZlZxzZ3ib4Fc9cicxB4WbO04D9rpK4lTrOVnB03n6ckabuq4icnfO3icJ3kCOxx0/640?wx_fmt=png&from=appmsg)

* **批量任务管理**：支持任务队列创建和顺序执行

![](https://mmbiz.qpic.cn/mmbiz_png/4T1PVwJicwk86ZNROCc0NOhx7NoDo3SB6FLibufN9xS9Gk2Ol8GKCwEuFyjkmNnNaaYcVIHCggze7fcIsMh68Kcg1eCk7lNza5YUNFxgcW1e4/640?wx_fmt=png&from=appmsg)

* **可视化界面**：密码保护的 Web 控制台、攻击链图、风险评分、历史审计等

![](https://mmbiz.qpic.cn/mmbiz_png/4T1PVwJicwk978xKfUYRQ4n2LG9Lib5YI6Ze62BzN7nKk2HUWAN8wkyHQyxCN0eJxLOR8hlFXy811Akmp3Xib3iaBbuyZplwibFkqA3iarVvOuicB4/640?wx_fmt=png&from=appmsg)

这些功能使平台既适合自动化测试，也支持人工深度介入。

## 三、框架架构CyberStrikeAI

采用模块化、高扩展性的架构设计：

* **核心语言**：Go（后端主框架） + Python（部分工具支持）
* **AI 引擎**：兼容 OpenAI 协议的大模型 + 多 Agent 编排（CloudWeGo Eino）
* **工具系统**：100+ YAML 定义的工具配方，支持动态扩展
* **MCP 实现**：原生支持多种传输协议和外部联邦
* **数据存储**：SQLite + 大结果分页压缩 + 可搜索归档
* **知识库**：嵌入向量检索 + 可选 Eino Compose 索引管道
* **安全机制**：密码保护、审计日志、工具沙箱、超时控制等

平台强调可观测性和可扩展性，适合团队协作和二次开发。

## 四、如何使用快速上手步骤：

1. 克隆仓库

   ```
   git clone https://github.com/Ed1s0nZ/CyberStrikeAI.git
   cd CyberStrikeAI
   ```
2. 一键部署（推荐）

   ```
   chmod +x run.sh && ./run.sh
   ```
3. 首次配置

* 打开 http://localhost:8080
* 在设置中配置 OpenAI 兼容的 API Key 和模型
* 设置登录密码

4. 安装必要安全工具（可选，根据需求选择）

* Ubuntu/Debian：sudo apt install nmap sqlmap nuclei httpx gobuster 等
* macOS：使用 brew 安装对应工具

5. 启动后通过 Web 控制台或 API 进行测试

平台支持 Docker 部署和手动编译，升级可使用 upgrade.sh 脚本。

## 五、其他重要特性

### 完整的漏洞生命周期管理

系统不仅发现漏洞，还让你能够创建、分类、跟踪和管理漏洞。每个漏洞都可以设置严重程度（Critical/High/Medium/Low/Info）、当前状态（Open/Confirmed/Fixed）和解决期限。这对于团队协作和合规性报告至关重要。

### 审计日志与可追溯性

所有的操作——包括AI决策、工具调用、用户行为——都被完整记录在SQLite数据库中。这意味着你可以回放任何一个测试过程，查看AI为什么做出某个决定，这对安全审计和知识学习都极其宝贵。

### Skills系统与知识积累

CyberStrikeAI借鉴了Claude Agent Skills的概念，支持将可复用的测试流程打包成Skills。你可以创建一个"SQL注入检测技能"、"API安全审计技能"等，在不同的任务中复用。这形成了一个不断积累的知识资产库。

### 无缝升级

项目提供了一个智能升级脚本`upgrade.sh`，能够无缝升级到新版本，同时保留你的配置文件和数据。对于长期运维来说，这是一个重大的便利。

> 项目地址：https://github.com/Ed1s0nZ/CyberStrikeAI

## 学习交流群

刚加入网络安全行业的小白，可以加入学习交流群，大家一起互相学习，互相进步，不会的难题大家一起学习，一起攻克。

想要进学习交流群的师傅们，可以扫描下方二维码添加好友，我再拉你进群（Ps：防止广告进群）。

![](https://mmbiz.qpic.cn/mmbiz_jpg/IkpoxULsr9dEclFnKnAAurt1AlnO1HBLiaRymULG1ibJJhXlNjMH1rd1SgQQWIyFBVTRMteWWfiby3FCWfpB7n2oA/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/IkpoxULsr9fbWSl52zKqe5AN711UM8IFNbS9rZLM7reGeUZs0XqdtM8X5L5mdRibicHpxmu3iaPGct9UztVKAT6AA/0?wx_fmt=png)

泷羽Sec-Norsea

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/IkpoxULsr9fbWSl52zKqe5AN711UM8IFNbS9rZLM7reGeUZs0XqdtM8X5L5mdRibicHpxmu3iaPGct9UztVKAT6AA/0?wx_fmt=png)

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
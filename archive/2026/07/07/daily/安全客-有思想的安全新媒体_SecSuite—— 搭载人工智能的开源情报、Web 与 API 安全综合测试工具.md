---
title: SecSuite—— 搭载人工智能的开源情报、Web 与 API 安全综合测试工具
url: https://www.anquanke.com/post/id/315743
source: 安全客-有思想的安全新媒体
date: 2026-07-07
fetch_date: 2026-07-08T05:03:55.726008
---

# SecSuite—— 搭载人工智能的开源情报、Web 与 API 安全综合测试工具

首页

阅读

* [安全资讯](https://www.anquanke.com/news)
* [安全知识](https://www.anquanke.com/knowledge)
* [安全工具](https://www.anquanke.com/tool)

活动

社区

学院

安全导航

内容精选

* [专栏](/column/index.html)
* [精选专题](https://www.anquanke.com/subject-list)
* [安全KER季刊](https://www.anquanke.com/discovery)
* [360网络安全周报](https://www.anquanke.com/week-list)

# SecSuite—— 搭载人工智能的开源情报、Web 与 API 安全综合测试工具

阅读量**19988**

发布时间 : 2026-07-07 22:27:24

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

![]()

一款由TheSecuredAnalyst项目团队开发的全新开源安全平台SecSuite现已正式发布。该工具集开源情报侦查、Web漏洞扫描、API安全检测、合规性核查与AI智能分析能力于一体，是一套统一化综合安全工具套件。

项目开源仓库托管于GitHub，仓库地址：53cur3dL34rn/security-suite。本工具面向安全从业人员、渗透测试工程师与红队人员打造，采用模块化可扩展架构，支持完全离线运行本地大模型。

# **版本核心组件**

SecSuite v0.1.0内置11套开源情报模块、6款Web安全扫描器、4套API安全检测工具，全部功能可通过统一命令行界面（CLI）调用，亦可基于FastAPI搭建的REST程序接口调用。

平台支持三类AI推理后端：Ollama（纯本地离线推理）、Anthropic Claude、OpenAI GPT。依托AI能力，工具可自动关联多源风险线索、生成管理层精简报告、提供大模型交互式漏洞修复指引，是目前功能完整性领先的开源安全综合套件之一。

工具主打轻量化部署，全流程一键部署脚本大幅降低使用门槛：Linux/macOS环境执行setup.sh、Windows环境执行setup.ps1，脚本自动完成Python环境、全部依赖库、Ollama 框架及本地大模型部署；Windows端安装无需管理员权限。

# **SecSuite全生命周期安全检测能力一览**

![]()

# **核心特色：AI 交互式漏洞修复引擎**

SecSuite 最具实战价值的功能为 AI 修复引擎（调用命令：secsuite ai remediate）。

区别于传统工具仅输出静态检测报告，该模块完成目标扫描、识别全部风险项后，依托本地大模型交互式引导运维人员逐项修复漏洞。

针对每一类风险（例如无认证 Redis 服务暴露），AI 会生成三段可直接执行的 Shell 指令：【风险核查命令】【漏洞修复命令】【修复结果验证命令】，操作人员可实时执行、修改或跳过对应指令。

该功能打通了 “漏洞发现 — 漏洞修复” 的工作链路，以往该流程需要多款独立工具配合完成。关键优势：整套推理流程依托 Ollama 部署的通义千问 2.5、LLaMA 3.2 等本地大模型运行，所有扫描数据、账号凭证、业务基础设施信息不会流出本地隔离环境。

# **API安全检测模块（apisec）**

apisec 模块专门针对 REST 接口设计，可导入 OpenAPI/Swagger 接口文档并对全部接口开展系统性安全检测，下设三类子模块覆盖主流攻击面：

接口检测子模块：检测垂直 / 水平越权访问（BOLA/IDOR）、SQL/NoSQL/ 命令注入、参数批量赋值漏洞、敏感信息泄露；

鉴权检测子模块：鉴权绕过、身份认证缺陷、JWT 签名漏洞（含 none 算法攻击、过期时间 exp 字段缺失检测）、接口限流缺失；

模糊测试子模块：向接口传入边界极值、注入载荷、畸形请求体，触发程序崩溃、敏感数据外泄等异常。

通过secsuite serve命令可启动 REST 服务端，将全部检测能力封装为标准化 HTTP 接口，可无缝接入 CI/CD 流水线、安全编排平台，也可通过 curl、Python 脚本开发自研自动化工具。

# **Web 扫描核心能力**

工具演示案例中，对example.com站点扫描可精准识别站点启用 SSLv3 协议，判定存在 POODLE 漏洞（CVE-2014-3566）。

内置 SSL/TLS 实时审计模块可快速识别废弃协议、弱加密套件、证书链异常，官方测试场景中单站点审计耗时不足 1 秒。

同时集成 XSS、SQL 注入扫描、字典目录爆破、基于 Nuclei 模板的通用漏洞检测，完整覆盖 Web 应用主流攻击面。

# **工具架构分层设计**

SecSuite 采用三层解耦架构：

交互层：基于 Typer 开发的 CLI 命令行 + FastAPI 构建的 REST 接口；

核心调度层：目标资产建模、缓存管理、通用 HTTP 客户端、报告导出引擎；

扫描插件层：各类安全检测模块化插件。

# **配套运维功能**

报告导出：支持 JSON、CSV、HTML、Markdown 四种格式；

定时任务调度：兼容 Cron 定时扫描，自动留存历史检测记录；

SIEM 日志输出：支持 CEF/LEEF 标准日志格式，对接 Splunk、Elasticsearch、Syslog 日志体系。

Shodan、VirusTotal、Anthropic、OpenAI 所需API密钥均为选填项。核心检测功能可完全脱离第三方密钥，仅依靠Ollama本地AI模型运行，适用于物理隔离内网、网络管控严苛的环境。

# **发布说明**

SecSuite v0.1.0现已上线GitHub开源仓库，仓库地址：53cur3dL34rn/security-suite。

本工具仅供安全从业人员在获得正式授权前提下开展渗透测试、红队演练与安全风险评估。

全部第三方 API、AI大模型对接功能均为可选组件；模块化架构支持团队仅启用与测评范围匹配的插件，按需轻量化部署。

信息来源：cybersecuritynews.com

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/315743](/post/id/315743)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [渗透测试](/tag/%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=184300)

[安全客](/member.html?memberId=184300)

这个人太懒了，签名都懒得写一个

* 文章
* **16**

* 粉丝
* **0**

### TA的文章

* ##### [【FDE前沿部署工程师】全国百城上岗计划二期来啦！](/post/id/315682)

  2026-07-07 23:19:12
* ##### [RedAmon：串联侦察、漏洞利用与后渗透的 AI 安全工具](/post/id/315747)

  2026-07-07 22:58:08
* ##### [SecSuite—— 搭载人工智能的开源情报、Web 与 API 安全综合测试工具](/post/id/315743)

  2026-07-07 22:27:24
* ##### [恶意Skills利用扫描规避技术攻击Claude Code和Codex](/post/id/315737)

  2026-07-07 16:59:30
* ##### [T3MP3ST 安全框架：集成 35 款工具，将 AI 代码智能体转化为零日漏洞挖掘器](/post/id/315732)

  2026-07-07 16:53:40

### 相关文章

* ##### [RedAmon：串联侦察、漏洞利用与后渗透的 AI 安全工具](/post/id/315747)

  2026-07-07 22:58:08
* ##### [T3MP3ST 安全框架：集成 35 款工具，将 AI 代码智能体转化为零日漏洞挖掘器](/post/id/315732)

  2026-07-07 16:53:40
* ##### [一款完全离线的自主渗透测试智能体AIRecon](/post/id/315678)

  2026-06-26 15:23:49
* ##### [新开源网络安全平台CyberSentinel AI v3.0 正式亮相](/post/id/315663)

  2026-06-23 11:36:49
* ##### [Splunk AI Toolkit曝高危漏洞：CVSS 9.1，可远程执行任意系统命令](/post/id/315618)

  2026-06-18 20:00:10
* ##### [HPE发布Aruba OS高危漏洞预警 可未授权重置密码](/post/id/315148)

  2026-03-13 10:34:00
* ##### [GitLab发布紧急安全更新 修复高危XSS与API拒绝服务漏洞](/post/id/315155)

  2026-03-13 10:33:13

### 热门推荐

文章目录

![](https://p0.qhimg.com/t11098f6bcd5614af4bf21ef9b5.png)

安全KER

* [关于我们](/about)
* [联系我们](/note/contact)
* [用户协议](/note/protocol)
* [隐私协议](/note/privacy)

商务合作

* [合作内容](/note/business)
* [联系方式](/note/contact)
* [友情链接](/link)

内容需知

* [投稿须知](https://www.anquanke.com/contribute/tips)
* [转载须知](/note/repost)
* 官网QQ群：568681302

合作单位

* [![安全KER](https://p0.ssl.qhimg.com/t01592a959354157bc0.png)](http://www.cert.org.cn/)
* [![安全KER](https://p0.ssl.qhimg.com/t014f76fcea94035e47.png)](http://www.cnnvd.org.cn/)

Copyright © 北京奇虎科技有限公司 三六零数字安全科技集团有限公司 安全KER All Rights Reserved [京ICP备08010314号-66](https://beian.miit.gov.cn/)[![](https://icon.cnzz.com/img/pic.gif)](https://www.cnzz.com/stat/website.php?web_id=1271278035 "站长统计")

微信二维码

**X**![安全KER](https://p0.ssl.qhimg.com/t0151209205b47f2270.jpg)
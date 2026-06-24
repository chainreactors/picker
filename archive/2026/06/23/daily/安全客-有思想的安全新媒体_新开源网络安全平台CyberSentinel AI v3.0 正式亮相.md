---
title: 新开源网络安全平台CyberSentinel AI v3.0 正式亮相
url: https://www.anquanke.com/post/id/315663
source: 安全客-有思想的安全新媒体
date: 2026-06-23
fetch_date: 2026-06-24T05:59:27.772186
---

# 新开源网络安全平台CyberSentinel AI v3.0 正式亮相

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

# 新开源网络安全平台CyberSentinel AI v3.0 正式亮相

阅读量**27425**

发布时间 : 2026-06-23 11:36:49

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

一款名为 **CyberSentinel AI v3.0** 的新开源网络安全平台正式亮相，成为自主安全工具领域的重要进展。该平台融合了 **33 款真实渗透测试与威胁情报工具**，并搭载与提供商无关的 AI 引擎，支持 Claude、GPT-4o、OpenRouter，以及通过 Ollama 实现的完全离线本地推理。

与仅能提出命令建议的传统 AI 安全助手不同，CyberSentinel AI 能够在隔离的 Kali Linux Docker 沙箱中**真正执行工具**——包括 Nmap、SQLMap、Nikto、Nuclei 和 OWASP ZAP——并由 AI 对结果进行实时分析。

该平台在 GitHub 上以 `3sk1nt4n/cybersentinel-ai` 发布，完全运行于本地基础设施，**无需任何云服务依赖**。

# 架构：七大容器化服务

平台通过 Docker Compose 部署，共包含七个容器化服务：

* Next.js 前端

（端口 3000）：提供流式聊天界面

* FastAPI 后端

（端口 8000）：负责 AI 路由、意图分类与工具编排

* Kali 沙箱容器

在完全隔离的环境中执行安全扫描，防止危险操作波及宿主系统

* Neo4j

用于攻击面与 MITRE ATT&CK 技术知识图谱映射

* ChromaDB

基于 MITRE、CIS 和 NIST 框架的 RAG（检索增强生成）引擎

* Elasticsearch + Kibana

ELK Stack SIEM，预置安全事件数据，用于日志分析训练

该平台的**自主执行模型**允许 AI 自动分类用户意图、自主选择合适工具，并支持**最多同时并发运行五个工具**，最终综合输出统一分析报告——这是向实用安全自动化迈出的重要一步。

# 33款安全工具，覆盖六大功能类别

| 类别 | 工具数量 | 主要工具 |
| --- | --- | --- |
| 实时扫描器 | 11 款 | Nmap、Nikto、Nuclei、SQLMap、Subfinder、OWASP ZAP、SSL/TLS 分析、DNS 侦察、WHOIS、HTTP 头部检测、Ping/Traceroute |
| 威胁情报 API | 5 款 | Shodan、VirusTotal、AbuseIPDB、AlienVault OTX、NVD/CISA KEV |
| SIEM 集成 | 3 款 | ELK Stack、Splunk、Wazuh |
| AI 检测 | 5 款 | Zeek 分析器、IOC 提取器、日志分析器、威胁检测、电子邮件钓鱼分析器 |
| 威胁狩猎 | 4 款 | YARA 规则、Sigma 规则、Snort/Suricata 规则、SIEM 查询生成器 |
| 合规框架 | 5 款 | MITRE ATT&CK、MITRE ATLAS、NIST/CIS、HIPAA/PCI-DSS、SOC 2/FedRAMP |

# 核心亮点

**会话中途切换 AI 提供商**是 CyberSentinel 的突出特性之一。用户可在 Anthropic Claude、OpenAI GPT-4o、OpenRouter（支持 100+ 模型）与本地运行的 Ollama（默认模型 `qwen2.5:7b`）之间随时切换，**且不会丢失任何对话上下文**。所有 API 密钥均为可选，平台可以 Ollama 作为默认推理引擎实现完全离线运行。

**实时威胁情报**动态拉取自 NVD、CISA KEV、EPSS、AlienVault OTX 和 Abuse.ch，无需手动更新即可保持漏洞上下文的持续更新。

# 安全防护机制

平台内置多重安全保障措施：

* 输入/输出过滤

屏蔽提示词注入（Prompt Injection）、SSRF 攻击和系统提示词泄露

* 沙箱隔离

所有扫描均在独立容器内执行

* 法律警告

项目明确提示，未经授权的扫描行为属于违法行为

# 系统要求

* 必须安装

Docker Desktop

* 最低内存

8 GB RAM

* 首次构建

约需下载 4–5 GB 镜像及模型数据

* 后续启动

约 30 秒内完成

CyberSentinel AI v3.0 实现了**自主 AI 与真实安全工具的深度融合**，为安全研究人员和红队提供了一套完全自托管、无云依赖的替代性平台，是安全自动化领域值得关注的实践性进展。

信息来源：https://cybersecuritynews.com/cybersentinel-ai-with-33-security-tools/

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/315663](/post/id/315663)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [人工智能](/tag/%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD)
* [渗透测试](/tag/%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95)
* [漏洞挖掘](/tag/%E6%BC%8F%E6%B4%9E%E6%8C%96%E6%8E%98)

**+1**0赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=184300)

[安全客](/member.html?memberId=184300)

这个人太懒了，签名都懒得写一个

* 文章
* **7**

* 粉丝
* **0**

### TA的文章

* ##### [新开源网络安全平台CyberSentinel AI v3.0 正式亮相](/post/id/315663)

  2026-06-23 11:36:49
* ##### [Weaxor勒索软件又添Linux平台变种](/post/id/315628)

  2026-06-22 15:11:07
* ##### [「文科生AI黑客松」专访：社会工作专业范心怡，和她那个会夸人的电子穿搭闺蜜](/post/id/315622)

  2026-06-22 10:05:30
* ##### [Splunk AI Toolkit曝高危漏洞：CVSS 9.1，可远程执行任意系统命令](/post/id/315618)

  2026-06-18 20:00:10
* ##### [不写代码，照样赢！全国首届文科生AI黑客松圆满落幕](/post/id/315595)

  2026-06-03 20:27:26

### 相关文章

* ##### [科技云报到：“龙虾”入笼：为何金融行业不敢“养”？](/post/id/315234)

  2026-03-27 10:44:02
* ##### [利润仅$200？Anthropic 最新研究揭示 AI 自动挖掘 0-day 的真实经济账](/post/id/313896)

  2025-12-19 14:36:30
* ##### [芯云一体安全可信，超融合重塑智能时代未来](/post/id/313229)

  2025-11-18 16:36:43
* ##### [一文读懂香港金融科技周：DART将带领香港金融科技驶向何方？](/post/id/313039)

  2025-11-05 18:35:34
* ##### [人工智能可能修复帮助传播了 15 年的漏洞](/post/id/308401)

  2025-06-12 15:19:33
* ##### [浅析新型网络犯罪DeepSeek AI实战应用](/post/id/305102)

  2025-03-18 10:38:20
* ##### [360SRC x Hacking Group丨「奇御」AI安全技术沙龙议题征集！](/post/id/302279)

  2024-11-28 17:43:31

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
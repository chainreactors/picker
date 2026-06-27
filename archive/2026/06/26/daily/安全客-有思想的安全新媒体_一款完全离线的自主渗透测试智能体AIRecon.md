---
title: 一款完全离线的自主渗透测试智能体AIRecon
url: https://www.anquanke.com/post/id/315678
source: 安全客-有思想的安全新媒体
date: 2026-06-26
fetch_date: 2026-06-27T05:50:23.894242
---

# 一款完全离线的自主渗透测试智能体AIRecon

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

# 一款完全离线的自主渗透测试智能体AIRecon

阅读量**20148**

发布时间 : 2026-06-26 15:23:49

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

AIRecon 是一款完全离线运行的自主渗透测试智能体，它将自托管的 Ollama 大语言模型与 Kali Linux Docker 沙箱相结合，能够自动化完成端到端的安全评估，且全程不向云端暴露任何数据。该工具由研究人员 pikpikcu 开发，旨在消除使用 GPT-4 或 Claude 等商业 API 模型所带来的高昂成本——这类递归式侦察工作流在单次会话中可能需要发起数千次 LLM 调用。

# PART.01 颠覆传统模式

商业化的 AI 安全工具会将目标情报发送到外部服务器，并要求持续购买 API 订阅。AIRecon 彻底颠覆了这一模式：所有工具输出、漏洞报告和会话数据都保留在操作者本机之上。

它原生集成 Caido 代理，内置五种功能：list（列表）、replay（重放）、automate（自动化，使用 §FUZZ§ 标记）、findings（发现）和 scope（范围管理）。这使其尤其适合在严格数据合规政策下工作的漏洞赏金猎人和红队人员。

# PART.02 四阶段自动化流程

AIRecon 通过四个自动化阶段来组织每次 engagements（安全评估任务），每个阶段都有明确的目标、推荐的工具以及自动转换条件。阶段约束是有意设计为”软性”的——智能体被引导但不会被强制阻断。检查点机制如下：每 5 次迭代触发阶段评估，每 10 次触发自我评估，每 15 次触发上下文压缩。

完整技术栈包括：Kali 沙箱、浏览器自动化、自定义模糊测试器、Schemathesis API 模糊测试以及用于静态源码分析的 Semgrep SAST。

# PART.03本地安全知识库

AIRecon 的一项突出功能是其可选的 airecon-dataset 配套组件，可将约 109 万条安全记录索引到本地 SQLite FTS5 数据库中，涵盖 CVE 漏洞、红队技术、CTF 解题报告、Nuclei 模板和漏洞赏金载荷——全部完全离线可用。

LLM 在尝试不熟悉的技术之前，会自主调用 dataset\_search，将其决策建立在真实索引数据之上，而非纯粹依靠”幻觉”臆测。会话记忆持久化存储在 `~/.airecon/memory/airecon.db` 中，保存的内容包括发现项、WAF 绕过模式、工具可靠性评分以及针对单个目标的攻击链发现，这些都会影响未来的行为。

# PART.04 模型配置要求

AIRecon 要求模型原生支持工具调用（tool-calling）和扩展思考（`<think>` 块）。强烈不建议使用参数量低于 8B 的模型，因为它们频繁出现幻觉、编造 CVE 以及不可靠的工具调用。推荐配置如下：

| 模型 | 显存需求 | 适用场景 |
| --- | --- | --- |
| Qwen3.5 122B | 48+ GB | 最佳质量，最可靠 |
| Qwen3.5 35B | 20 GB | 推荐大多数用户使用 |
| Qwen3.5 35B (MoE) | 16 GB | 更低显存占用 |
| Qwen3.5 9B | 6 GB | 最低可用配置 |

# PART.05 内置技能与扩展

AIRecon 自带 57 个内置技能文件和 289 个”关键词→技能”自动映射，覆盖最常见的攻击技术。社区维护的 airecon-skills 仓库额外提供了 57 个基于命令行的实战手册，适用于 CTF、漏洞赏金和渗透测试任务。

此外还支持 MCP 服务器集成（通过 `~/.airecon/mcp.json` 配置），允许智能体将外部工具（如自定义 XSS 生成器或专有 API 扫描器）动态暴露为第一等公民的智能体工具。

# PART.06 安装与 Google Colab 支持

从 GitHub 安装需要 Python 3.12+、Docker 20.10+ 以及一个运行中的 Ollama 实例，一条命令即可完成：

```
bashcurl -fsSL https://raw.githubusercontent.com/pikpikcu/airecon/refs/heads/main/scripts/install.sh | bash
```

对于本地显存不足的操作者，AIRecon 支持通过 Cloudflare 隧道连接 Google Colab T4 GPU，让免费层级的 Colab 会话来提供模型服务，而 AIRecon 的 TUI 界面在本地运行。

免费的 T4 GPU（15 GB 显存）可运行 qwen3.5:9b，但单次会话上限为 12 小时，不适合超出该时长的深度自主侦察任务。

信息来源：cybersecuritynews.com

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/315678](/post/id/315678)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [渗透测试](/tag/%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95)
* [漏洞挖掘](/tag/%E6%BC%8F%E6%B4%9E%E6%8C%96%E6%8E%98)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=184300)

[安全客](/member.html?memberId=184300)

这个人太懒了，签名都懒得写一个

* 文章
* **9**

* 粉丝
* **0**

### TA的文章

* ##### [一款完全离线的自主渗透测试智能体AIRecon](/post/id/315678)

  2026-06-26 15:23:49
* ##### [360纳米Work Box全国渠道伙伴招募正式启动](/post/id/315669)

  2026-06-25 10:58:52
* ##### [新开源网络安全平台CyberSentinel AI v3.0 正式亮相](/post/id/315663)

  2026-06-23 11:36:49
* ##### [Weaxor勒索软件又添Linux平台变种](/post/id/315628)

  2026-06-22 15:11:07
* ##### [「文科生AI黑客松」专访：社会工作专业范心怡，和她那个会夸人的电子穿搭闺蜜](/post/id/315622)

  2026-06-22 10:05:30

### 相关文章

* ##### [新开源网络安全平台CyberSentinel AI v3.0 正式亮相](/post/id/315663)

  2026-06-23 11:36:49
* ##### [利润仅$200？Anthropic 最新研究揭示 AI 自动挖掘 0-day 的真实经济账](/post/id/313896)

  2025-12-19 14:36:30
* ##### [记一所中学的的SQL报错注入](/post/id/297649)

  2024-09-03 16:06:03
* ##### [sign加密小程序漏洞挖掘](/post/id/299052)

  2024-08-29 03:21:11
* ##### [那些你需要知道的关于DORA的知识](/post/id/297784)

  2024-07-10 19:33:03
* ##### [攻防演练场景下的漏洞挖掘与治理 | 安全范儿沙龙开启](/post/id/297265)

  2024-06-14 16:04:34
* ##### [字节跳动安全范儿技术沙龙\*第13期：漏洞攻防安全](/post/id/293892)

  2024-03-13 13:50:49

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
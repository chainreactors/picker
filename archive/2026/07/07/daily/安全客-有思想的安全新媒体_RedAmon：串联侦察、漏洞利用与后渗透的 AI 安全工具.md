---
title: RedAmon：串联侦察、漏洞利用与后渗透的 AI 安全工具
url: https://www.anquanke.com/post/id/315747
source: 安全客-有思想的安全新媒体
date: 2026-07-07
fetch_date: 2026-07-08T05:03:53.937284
---

# RedAmon：串联侦察、漏洞利用与后渗透的 AI 安全工具

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

# RedAmon：串联侦察、漏洞利用与后渗透的 AI 安全工具

阅读量**18541**

发布时间 : 2026-07-07 22:58:08

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

一款全新开源攻击性安全平台 RedAmon 重构自动化渗透测试流程，将**资产侦察、漏洞利用、后渗透操作、AI 漏洞分级研判、自动化代码修复**整合为一套端到端完整流水线，最终可自动生成附带修复代码的 GitHub 合并请求（PR）。

RedAmon 是基于 Docker 构建的模块化容器化渗透测试框架，无需在本地主机直接安装各类安全工具。

![]()

该平台架构依托六大核心模块：并行化资产侦察流水线、AI 智能体调度器、攻击面图谱、跨会话情报演化图谱 EvoGraph、CypherFix 漏洞修复引擎，以及支持 500 余项配置参数的项目设置引擎。其完整杀伤链流程可概括为：资产侦察 → 漏洞利用 → 后渗透操作 → AI 漏洞研判 → 代码修复智能体 → 提交 GitHub 合并请求。

# **资产侦察模块**

RedAmon 的侦察流水线可在 Kali Linux 容器内并行调度 40 余款行业主流安全工具，包含 Subfinder、Amass、Naabu、Masscan、Nuclei、Katana、FFuf、Arjun 等。所有工具输出数据统一汇入共享 Neo4j 知识图谱，图谱内置17类实体节点、20 余种关联关系，数分钟内即可为 AI 智能体构建结构完整、全域连通、可检索查询的可视化攻击面，省去传统工具数小时的数据整理耗时。

专属 AI 安全测试模块「AI Gauntlet」专门针对大模型 / AI 业务面开展拓展侦察，集成四款红队专用工具 garak、PyRIT、Giskard、promptfoo，对探测到的接口端点开展安全检测，覆盖提示注入、模型越狱、数据泄露等风险，检测结果统一映射至 OWASP 大模型安全规范与 MITRE-ATLAS 大模型攻防框架。

# **核心自主AI智能体**

RedAmon 的核心是基于 LangGraph 搭建、采用 ReAct（推理 + 行动）模式的自主智能体。智能体按顺序执行三大阶段：信息搜集阶段、漏洞利用阶段、后渗透阶段，通过运行在沙箱隔离 Kali 环境中的模型上下文协议（MCP）服务，可调用 14 款以上安全工具：

Metasploit：漏洞载荷执行

Hydra：凭证暴力破解

Playwright：浏览器自动化测试

完整 Kali 命令行环境，预装 70 余款命令行安全工具

平台内置「分队并行模式（Fireteam）」，主根智能体可拆分出多支专业子智能体同步作业，例如同时执行：Hydra 校验账号密码策略、通过权限提升链路验证 CVE 漏洞利用路径、全域扫描前端跨站脚本（XSS）漏洞。

# **自动化漏洞修复引擎CypherFix**

绝大多数攻击性安全工具仅止步于漏洞发现，而 RedAmon 搭载双智能体修复流水线 CypherFix 实现漏洞闭环处置：

漏洞研判智能体：针对 Neo4j 图谱执行 9 套预设图查询语句，聚合数百条扫描结果、自动去重，并根据漏洞可利用难度完成风险分级；

代码修复智能体：拉取目标代码仓库，依托 11 款代码分析工具遍历源码，通过循环推理迭代生成针对性修复代码，自动创建 GitHub 合并请求，交由人工审核合并。

# **人机协同与访问管控**

该框架设计上并非完全无人自主运行，配套**工具确认机制**实现人机介入管控：执行高风险操作（Nmap 大规模扫描、Metasploit 漏洞载荷、Hydra 暴力破解等）前会暂停智能体流程，在交互界面弹出「允许 / 拒绝」操作弹窗，人工确认后方可继续。

支持上传《授权测试范围文档（RoE）》一键配置全项目操作约束；内置目标防护机制，框架底层永久拦截政府、军工、教育类域名，杜绝违规扫描。

# **开发团队与模型兼容**

RedAmon 由具备 15 年企业级 AI 智能体系统研发经验、AWS 认证 AI 平台架构师萨穆埃莱・詹皮耶里（Samuele Giampieri）主导开发维护；协同开发者瑞泰什・戈希尔（Ritesh Gohil）任职 Workday 网络安全工程师，拥有 7 年渗透测试实战经验，累计发布 11 个通用漏洞编号（CVE）。

框架兼容主流大模型服务商：OpenAI（GPT-5）、Anthropic（Claude Opus 4.6）、亚马逊 Bedrock，以及适配 Ollama 的本地离线模型，单项目可动态切换 400 余款大模型，项目开源仓库托管于 GitHub。

信息来源：cybersecuritynews.com

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/315747](/post/id/315747)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [渗透测试](/tag/%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95)
* [漏洞挖掘](/tag/%E6%BC%8F%E6%B4%9E%E6%8C%96%E6%8E%98)

**+1**0赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=184300)

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

* ##### [SecSuite—— 搭载人工智能的开源情报、Web 与 API 安全综合测试工具](/post/id/315743)

  2026-07-07 22:27:24
* ##### [T3MP3ST 安全框架：集成 35 款工具，将 AI 代码智能体转化为零日漏洞挖掘器](/post/id/315732)

  2026-07-07 16:53:40
* ##### [一款完全离线的自主渗透测试智能体AIRecon](/post/id/315678)

  2026-06-26 15:23:49
* ##### [新开源网络安全平台CyberSentinel AI v3.0 正式亮相](/post/id/315663)

  2026-06-23 11:36:49
* ##### [利润仅$200？Anthropic 最新研究揭示 AI 自动挖掘 0-day 的真实经济账](/post/id/313896)

  2025-12-19 14:36:30
* ##### [记一所中学的的SQL报错注入](/post/id/297649)

  2024-09-03 16:06:03
* ##### [sign加密小程序漏洞挖掘](/post/id/299052)

  2024-08-29 03:21:11

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
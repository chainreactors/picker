---
title: AI赋能威胁情报核武器！一键打通CTI到检测的完整闭环
url: https://mp.weixin.qq.com/s/Pt6g6UuIK-SyHy-VtyA5Lw
source: Doonsec's feed
date: 2026-07-30
fetch_date: 2026-07-31T05:28:51.625990
---

# AI赋能威胁情报核武器！一键打通CTI到检测的完整闭环

![cover_image](http://mmbiz.qpic.cn/sz_mmbiz_jpg/x5l8unjI0UqQTc7kr8RkAmKQqAActZDicicyeU4icSVD8q1icMOU1Igozy2RssroiaRN6NzCeviaiaJjCMEib2r0UzIPc0tb1Jy1rWo7joOavh7Lfko/0?wx_fmt=jpeg)

# AI赋能威胁情报核武器！一键打通CTI到检测的完整闭环

棉花糖糖糖
棉花糖糖糖

棉花糖网络安全工具箱

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

安全规范免责声明：本文仅做技术分享，使用者需遵守当地法律法规，禁止用于任何未授权的渗透测试或攻击行为。

## 重点导读简介

AdversaryGraph是一款自托管的AI辅助威胁情报到检测（CTI-to-Detection）工作台。该工具将威胁报告、IOC证据、CVE漏洞上下文、恶意软件分析结果、资产清单和验证遥测数据转化为可审查的ATT&CK/ATLAS映射和检测工程工单。平台支持多工作区管理，提供31个独立工作区，每个工作区配备模块级API/UI授权控制。

## 重点导读核心功能

### PART 01AI报告分析

平台集成AI辅助报告摄取引擎，支持从文本、PDF、DOCX和TXT格式中自动提取威胁情报。分析结果与ATT&CK框架关联，生成结构化的检测规则建议。

### PART 02Threat Radar

威胁雷达模块提供产品安全CTI早期预警能力，覆盖CVE、KEV、PoC、零日漏洞、供应链安全、硬件风险等多维信号源。系统提供产品暴露评分、案例图谱、PSIRT/Hunt/IR/Detection工作流，支持保存资产注册表与证据标签的CVE/TTP/IOC详情页面。资产评估结合被动OSINT、隔离MCP基础安全Nmap服务发现、有限Web姿态检查、验证TLS和只读DNS姿态、经签名/速率限制的Nuclei网络模板、本地CVE候选、所有权感知发现合并、可审计MCP工具跟踪和治理AI审查。

### PART 03威胁狩猎

威胁狩猎模块支持可证伪假设、有限范围、ATT&CK映射、遥测需求、版本化查询计划、保存发现、审查处置、可审计Threat Radar交接。来自存储报告或狩猎上下文的多提供商AI建议支持Enterprise ATT&CK。AI可起草假设、计划、查询、发现摘要和结果摘要，但不创建证据、执行查询或做出生命周期和处置决定。

### PART 04威胁狩猎查询库

平台提供经过审查的Sigma/YARA-L示例库，从有限Git支持馈送索引社区规则，支持字段化搜索和自动完成、溯源和ATT&CK链接、跨十种格式的确定性IOC到查询生成、一键创建规范狩猎草案。

### PART 05统一RAG

统一混合RAG系统覆盖标准化IOC、CVE、ATT&CK/TTP、攻击者、攻击者部门/地区/技术观测、活动、报告、知识、Threat Radar信号、威胁狩猎、证据图和消毒资产记录。系统支持增量数据库协调、有限单跳扩展跨允许列表存储关系、实时公司空间清单或保存业务档案作为私有请求上下文、PostgreSQL全文加pgvector搜索、引用绑定AI答案、过期分析员确认的Navigator提案。

### PART 06MCP服务器

平台提供有界的分析员面向MCP服务器，用于经认证的只读/咨询情报搜索、实体检索、接地答案和Navigator提案，无需自动平台变更。独立的私有扫描MCP服务仅由API用于授权资产评估。

### PART 07ATT&CK/ATLAS Navigator

内置Navigator支持攻击者、活动、部门覆盖和对比叠加层可视化。

### PART 08IOC库

IOC库提供调查透视、病毒总查询和馈送管理功能。

### PART 09CVE库

CVE库与NVD和CISA KEV同步，存储CVSS评分/CWE/CPE，提供严格APT-TTP-IOC-CVE关联。

### PART 10资产攻击面映射

资产攻击面映射功能支持从CMDB、扫描器、云、CSV、JSON和主机名/IP清单导入，使用严格的`namespace:value`标签标注产品、供应商、依赖、技术、部门、CVE、TTP、风险和暴露。

### PART 11恶意软件分析

恶意软件分析工作流由隔离的MalwareGraph服务支持，提供静态分类、字符串提取、解包/反混淆支持、调试器风格审查和AI摘要。

### PART 12攻击模拟

攻击模拟模块支持TTP优先实验室场景、真实被攻击服务器遥测、SIEM转发、连贯AI辅助杀伤链演练和攻击链图审查。平台区分两种遥测模式：真实实验室遥测由批准Docker实验室fixtures生成；合成AI遥测为SIEM解析器/规则练习生成，不验证真实漏洞行为。

### PART 13证据到检测图

证据到检测图功能保留从证据到已验证检测结果的完整推理链：证据→声明→行为→ATT&CK技术→必需遥测→检测候选→检测规则→验证场景→SIEM结果→分析员决策。该图帮助分析员了解什么是已证明的、什么是推断的、需要什么遥测、存在什么检测、什么已验证、什么仍需审查。AI生成的图节点和边为草稿，经分析员审查后生效。

### PART 14可观测性

可观测性仪表板提供API请求指标、近期跟踪、脱敏日志尾、Prometheus兼容指标和健康/自检视图。

## 重点导读核心架构

```
Evidence -> Claim -> Behavior -> ATT&CK Technique -> Required Telemetry
  -> Detection Candidate -> Detection Rule -> Validation Scenario
  -> SIEM Result -> Analyst Decision
```

系统采用有界AI架构设计，AI生成内容均为辅助输出，非证据或自主决策。所有AI生成内容需经分析员审查后生效。平台分离分析员面向MCP和私有扫描MCP服务，确保资产评估的安全隔离。

## 重点导读部署架构

平台采用Docker Compose部署，默认配置将公共UI和参考文档绑定到localhost，API、Redis、恶意软件分析服务和实验室fixtures位于内部Compose网络。本地配置存储在`.env`文件，持久化数据库默认位置为`${ADVERSARYGRAPH_DB_DIR:-./data/postgres}`。

部署要求：
- Docker和Docker Compose环境
- 推荐16GB以上内存
- 100GB以上存储空间

AI功能为可选配置，分析员可使用本地Ollama服务或经批准的云端OpenAI兼容端点。

## 重点导读项目地址

本公众号非项目作者，仅做技术分享。

```
https://github.com/anpa1200/threatmapper
```

## 广告时间

**低价考证包括但不限于CISP系列、PMP等等国内网安证书、网络安全交流群请关注公众号后点菜单栏的找棉花糖。**

**糖心会员站，网络安全必备网站，包括在线内网靶场、web靶场、src靶场、应急响应靶场，以及各种网安资料、教程、方案模版、以及超级多在线工具，99元包年！详细介绍：**[棉花糖会员站介绍(26年4月26日版本) ：在线内网靶场、网安资料方案、在线工具全能资源站](https://mp.weixin.qq.com/s?__biz=MzkyOTQzNjIwNw==&mid=2247493656&idx=1&sn=ef2aad19a122c739055604331f93f34c&scene=21#wechat_redirect)**，看完介绍百分百心动！**

![棉花糖会员站介绍图1](https://mmbiz.qpic.cn/mmbiz_png/x5l8unjI0UpXicmteDiaRvpe3RC3MibHK3a4MtuvtpCHUicsDEojJB4pLXgWd7PTLA86fibvK7HJDz8EwUJvYiavrvuKuHs57K5oymxdPibZbs7WSk/640?from=appmsg)

![棉花糖会员站介绍图2](https://mmbiz.qpic.cn/mmbiz_png/x5l8unjI0UrO39kjfIRNYorW4LCG7oNZqUOQ87ZF1mWbbDkIVmic401rVmiaDYbHaC42CY0mFTRbf2yvaIUXEwQlkhk58a32PASZ11T7FqcKU/640?from=appmsg)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/x5l8unjI0UrCSxv33ws9W4q7NCsLZiaWAQPkO1Tr0E81AlzPiah3DzibhDxWLTTViaTb8BXvSoRhkkJ3hqFMlfrhIxlSZ8CWyBib5lyyLQyJ36Wo/0?wx_fmt=png)

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
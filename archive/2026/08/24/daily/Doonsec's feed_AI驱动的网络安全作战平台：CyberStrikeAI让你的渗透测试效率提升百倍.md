---
title: AI驱动的网络安全作战平台：CyberStrikeAI让你的渗透测试效率提升百倍
url: https://mp.weixin.qq.com/s/3Ig2uCxY95ICkKGFdgV_LQ
source: Doonsec's feed
date: 2026-08-24
fetch_date: 2026-08-25T02:58:03.270229
---

# AI驱动的网络安全作战平台：CyberStrikeAI让你的渗透测试效率提升百倍

# AI驱动的网络安全作战平台：CyberStrikeAI让你的渗透测试效率提升百倍

棉花糖糖糖
棉花糖糖糖

棉花糖网络安全工具箱

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

郑重声明：本文仅作技术研究用途。使用 CyberStrikeAI 前，请确保目标系统为你所有或已获得明确授权。未授权使用本工具属于违法行为。

## 重点导读概述

CyberStrikeAI 是由 404Starlink 团队开发的 AI 原生网络安全作战系统，基于 Go 语言构建，集成了 Eino 驱动的智能代理、MCP 原生工具生态、RAG 知识检索体系、可视化工作流引擎以及攻击链建模分析模块。该平台为授权安全测试提供了一个完整的可审计工作空间，覆盖从侦察到后渗透的全链路操作。

## 重点导读核心架构

### PART 01技术栈

* **语言与框架**：Go 1.25+，Gin Web 框架，Eino 编排框架
* **多模型支持**：OpenAI Compatible API，可配置多个 AI 渠道
* **知识检索**：向量检索 + Reranking + 查询改写
* **数据持久化**：SQLite
* **协议支持**：MCP（Model Context Protocol）

### PART 02目录结构

```
├── cmd/            # 服务器与 MCP stdio 入口
├── internal/       # 核心模块
│   ├── agent/      # 智能代理
│   ├── multiagent/ # 多代理编排
│   ├── mcp/        # MCP 协议实现
│   ├── c2/         # C2 命令控制
│   ├── attackchain/# 攻击链建模
│   └── knowledge/ # 知识库检索
├── web/            # 前端界面
├── tools/          # 工具配方（100+）
├── roles/          # 角色配置
├── skills/         # Agent Skills
├── agents/         # 多代理编排配置
└── plugins/        # Burp Suite 插件、浏览器扩展
```

## 重点导读核心功能

### PART 03智能代理与编排

系统支持单代理执行、Deep 模式、Plan-Execute 模式以及 Supervisor 多代理模式。Graph 工作流支持将代理、工具、条件节点、审批节点和输出节点组合成可复用流程。

### PART 04MCP 工具生态

支持 HTTP、stdio、SSE、外部联邦和动态工具发现。工具执行具备以下特性：Worker 并发执行、有界等待、可通过 execution\_id 恢复轮询、取消支持、每服务器熔断、并发限制和统一输出上限。

### PART 05安全工具库

预置 100+ 工具，覆盖完整攻击链：

* **网络扫描**：nmap、masscan、rustscan、arp-scan、nbtscan
* **Web 扫描**：sqlmap、nikto、dirb、gobuster、feroxbuster、ffuf、httpx
* **漏洞扫描**：nuclei、wpscan、wafw00f、dalfox、xsser
* **子域名枚举**：subfinder、amass、findomain、dnsenum、fierce
* **云安全**：prowler、scout-suite、cloudmapper、pacu、terrascan、checkov
* **容器安全**：trivy、clair、docker-bench-security、kube-bench、kube-hunter
* **后渗透**：linpeas、winpeas、mimikatz、bloodhound、impacket、responder

### PART 06知识库

结合查询改写、向量检索、Reranking 和结果后处理。视觉分析模块独立调用视觉模型处理截图、验证码和 UI 界面。

### PART 07治理与审计

* 人工审核机制：审批模式、工具白名单、审计代理审查
* 平台 RBAC：多用户、系统角色、自定义角色、范围权限、所有权分配
* 结果治理：存储代理看到的工具结果副本，保护恢复路径，限制历史输出大小

### PART 08资产管理

支持域名、IP、端口、服务的标准化与去重。XLSX/CSV 导入导出、高级过滤器、保存视图、所有权和业务元数据、跨页批量维护、重复合并、扫描覆盖率追踪、关联漏洞和风险状态。

### PART 09漏洞管理

提供严重等级分类、生命周期跟踪、过滤和统计功能。

### PART 10项目与会话管理

会话管理支持分组、固定、重命名和批量组织。项目与攻击链功能连接跨会话事实、风险评分、图形视图和逐步回放。

### PART 11机器人集成

支持个人微信、企业微信、钉钉、飞书、Telegram、Slack、Discord、QQ 机器人。

### PART 12WebShell 管理

提供连接管理、虚拟终端、文件操作和 AI 辅助工作流。

### PART 13内置 C2

提供监听器、加密信标、会话、任务队列、载荷辅助工具和实时事件。

## 重点导读界面预览

### PART 14系统仪表盘

![System Dashboard Light](https://mmbiz.qpic.cn/mmbiz_png/x5l8unjI0Urpcam4qSnMfyZhiaiacX5YoqJiboJOZWOPLdskXBLBsAlTJuDYCAP0GE7IhjtLe3zQyahZUNSSDz3d5LNdQ0UrEUEQk0wLLoDeco/640?from=appmsg)

System Dashboard Light

![System Dashboard Dark](https://mmbiz.qpic.cn/sz_mmbiz_png/x5l8unjI0Uomvk4cCb85tibdprArSKZibMp9uevFBFSMJB7ynzSMQce5bQ1ear2ZurGKKhZ9YjjN8d4w3QexxV4O5SibmXNrQBcApmqp0cGFfQ/640?from=appmsg)

System Dashboard Dark

### PART 15核心功能界面

![Web Console](https://mmbiz.qpic.cn/mmbiz_png/x5l8unjI0UqcicianX6icJyib11TFUDh40ibV4cQJ9op9M7ibdicfX0Oeia04JKM2fia8M7Q1cFl0MPzzUvlJQcRN8vmkibLibEqVFcpkEo4rVehtBxthg/640?from=appmsg)

Web Console

![Task Management](https://mmbiz.qpic.cn/sz_mmbiz_png/x5l8unjI0UoEPvGDsmuO6BrhE49CkXYrDGKWylgyibbrsbzV7sic5mGB370cgTHBLvCFIAgICjcFibYxCAy0fdshFoFrsyXERhcw63E3ItfokU/640?from=appmsg)

Task Management

![Vulnerability Management](https://mmbiz.qpic.cn/mmbiz_png/x5l8unjI0Uqn9k37JMAiblr7jpGOKbTyV5xnwNtO64DA34W7icN1q5zwvyqpVsREkiaBrEuVh2j7QEjU3t0OYYzE5rLDDcvIxicwoK1UokO8Sfo/640?from=appmsg)

Vulnerability Management

![WebShell Management](https://mmbiz.qpic.cn/mmbiz_png/x5l8unjI0UrqtTbZkQ3NMamBTRAgdvWkd6MTLMdjGicZVEDkicM7mibWKJBRaDgvON4Z9M32hMfQHbeLfDozR0Fy13KGRLdeDqiafMzh8X6yZ50/640?from=appmsg)

WebShell Management

![MCP Management](https://mmbiz.qpic.cn/sz_mmbiz_png/x5l8unjI0UoNWpFc3INY2V7a1ic6eicNuDibRpDKprEd10byLwCr8L80lkEgnoTJqCvjda6blyLyrmvlO7LV2JxM1chTboWHia9dcZRHqIKtLGA/640?from=appmsg)

MCP Management

![Knowledge Base](https://mmbiz.qpic.cn/mmbiz_png/x5l8unjI0UoxvvmY57JwwicZoa3rYUI7LibY2QsPZgOnF72ZQfrHcf2jPNmodnykGZa8vMsh2aOgAVVghicibY7icjOLdFenkzm9fPtHb7EByf2s/640?from=appmsg)

Knowledge Base

![Skills Management](https://mmbiz.qpic.cn/mmbiz_png/x5l8unjI0UqOXUFAnvXl4BfvUIicbNvg4cuAMe7IDZkb4f4cibMnv7coUJibZtDqhL9VStTN4S05VBeR02gMwkfvNNXMDgfia31B3LxFvZ24cVs/640?from=appmsg)

Skills Management

![Agent Management](https://mmbiz.qpic.cn/mmbiz_png/x5l8unjI0Uoh6Tz8Wf5T3YiahmnB0VJfZiaKshW2NpBNYzf5iakz6cdAFJ3R5oGCz0xzmOibB9mXo83EfaA7BJAxjfGzwQUvpRHWqLiaWTw8AdjQ/640?from=appmsg)

Agent Management

![Role Management](https://mmbiz.qpic.cn/mmbiz_png/x5l8unjI0Upj2KkT6Wicu6eEoMvEvuv49k8dAaAvBPWnuuPOiaqHJBkgI2hGUZBv1icLytVWS48SOib6rbWRnZ3fzQOQicck5yJsFVCWg53dCqKc/640?from=appmsg)

Role Management

![System Settings](https://mmbiz.qpic.cn/mmbiz_png/x5l8unjI0UowWc3RHEgFGfohqvSicVQopwEnh9zViaEw1REZic2FNL2o1G7XDjSH1rFDic8zDSCUMcPP6NibH9H5WVxegTuhxvFFyBRQYym3eQ18/640?from=appmsg)

System Settings

### PART 16扩展集成

![MCP stdio Mode](https://mmbiz.qpic.cn/mmbiz_png/x5l8unjI0UoxtqIcLaaIDGQuSWy9rTe8oN7Ve6E1CDWwLlRMhD35JEicS6GhcialZjzmor1ibeScgtKs55bcbROooibMT4PrjLN2vkujdibVkGQ0/640?from=appmsg)

MCP stdio Mode

![Burp Suite Plugin](https://mmbiz.qpic.cn/sz_mmbiz_png/x5l8unjI0UpiboBlxg9aAAwhf4yrmYQKmoQXKN6hyWw0NRAmnImz9iaur75oaUns9iapViabibfcmMaDI3ecvPRCA52QdTz7VLSjMRwPibVib1p93E/640?from=appmsg)

Burp Suite Plugin

### PART 17攻击链视图

![Attack Chain](https://mmbiz.qpic.cn/mmbiz_png/x5l8unjI0Urd5BXGorwQvq2Cmyjjs99SZTZCp3iccMYlibAWHwTdaZych1Z4plryasibnkZ2ic73jUh11mKg5oG6ZKy09ZpoXaC7zmPLXibvMOWw/640?from=appmsg)

Attack Chain

## 重点导读快速部署

### PART 18环境要求

* Go 1.25+
* Python 3.10+

### PART 19启动命令

```
bashgit clone https://github.com/Ed1s0nZ/CyberStrikeAI.git
cd CyberStrikeAI
chmod +x run.sh && ./run.sh
```

`run.sh` 脚本自动完成以下操作：检查验证 Go 和 Python 环境、创建 Python 虚拟环境、安装 Python 依赖、下载 Go 依赖、构建项目、启动服务器。

### PART 20升级

```
bashchmod +x upgrade.sh && ./upgrade.sh --yes
```

本地 `tools/`、`roles/`、`skills/` 目录会被保留。

## 重点导读插件生态

### PART 21Burp Suite 插件

位置：`plugins/burp-suite/cyberstrikeai-burp-extension/`
构建输出：`plugins/burp-suite/cyberstrikeai-burp-extension/dist/cyberstrikeai-burp-extension.jar`

### PART 22浏览器扩展

支持 Chrome 和 Edge。捕获 DevTools 网络流量并发送至 CyberStrikeAI 进行 AI 辅助安全测试。
安装路径：`chrome://extensions/` → 加载已解压 → F12 → CyberStrikeAI 标签
构建输出：`plugins/browser-extension/cyberstrikeai-browser-extension/dist/cyberstrikeai-browser-extension.zip`

## 重点导读多代理编排

系统内置多个专业代理配置：

* recon.md - 侦察代理
* vulnerability-triage.md - 漏洞分类代理
* engagement-planning.md - 行动规划代理
* attack-surface-enumeration.md - 攻击面枚举代理
* penetration.md - 渗透代理
* privilege-escalation.md - 权限提升代理
* lateral-movement.md - 横向移动代理
* persistence-maintenance.md - 持久化代理
* cleanup-rollback.md - 清理回滚代理
* reporting-remediation.md - 报告修复代理

编排器支持三种模式：Orchestrator（标准编排）、Orchestrator-Plan-Execute（计划执行）、Orchestrator-Supervisor（监督模式）。

## 重点导读配置说明

最小配置示例：

```
yamlserver:
  host: "127.0.0.1"
  port: 8080
ai:
  default_channel: openai-main
  channels:
    openai-main:
      provider: openai_compatible
      api_key: "${OPENAI_API_KEY}"
      base_url: "https://api.openai.com/v1"
      model: "your-model"
```

## 重点导读项目信息

本公众号非项目作者，仅做技术分享。

本文介绍的项目开源地址如下：

```
https://github.com/Ed1s0nZ/CyberStrikeAI
```

## 广告时间

**低价考证包括但不限于CISP系列、PMP等等国内网安证书、网络安全交流群请关注公众号后点菜单栏的找棉花糖。**

**糖心会员站，网络安全必备网站，包括在线内网靶场、web靶场、src靶场、应急响应靶场，以及各种网安资料、教程、方案模版、以及超级多在线工具，99元包年！详细介绍：**[棉花糖会员站介绍(26年4月26日版本) ：在线内网靶场、网安资料方案、在线工具全能资源站](https://mp.weixin.qq.com/s?__biz=MzkyOTQzNjIwNw==&mid=2247493656&idx=1&sn=ef2aad19a122c739055604331f93f34c&scene=21#wechat_redirect)**，看完介绍百分百心动！**

![棉花糖会员站介绍图1](https://mmbiz.qpic.cn/mmbiz_png/x5l8unjI0UqK8XkJiarGltuZ9Aiaq9Hmy7dntF4sp9icBoS3PVKatSmqcic4h71Micltmz19bD7ibKQBMe05UVoPaia7pWGiaibQYKicammOP4WSwVqjA/640?from=appmsg)

![棉花糖会员站介绍图2](https://mmbiz.qpic.cn/sz_mmbiz_png/x5l8unjI0Uphuicztom623FGubpmYJk75rO6BEsBAjkD0j0yaA8adbjbVqqaJ8P83VLWF2SPXtLZVoXOnjVudic4sVJXcx9oE4cjvib2czpx34/640?from=appmsg)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/x5l8unjI0UrCSxv33ws9W4q7NCsLZiaWAQPkO1Tr0E81AlzPiah3DzibhDxWLT...
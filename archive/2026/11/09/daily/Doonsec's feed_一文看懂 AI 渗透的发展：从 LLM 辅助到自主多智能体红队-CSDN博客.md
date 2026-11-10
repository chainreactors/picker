---
title: 一文看懂 AI 渗透的发展：从 LLM 辅助到自主多智能体红队-CSDN博客
url: https://mp.weixin.qq.com/s/84pN30qSLYTgzX3INqjD_g
source: Doonsec's feed
date: 2026-11-09
fetch_date: 2026-11-10T09:00:45.714854
---

# 一文看懂 AI 渗透的发展：从 LLM 辅助到自主多智能体红队-CSDN博客

# 一文看懂 AI 渗透的发展：从 LLM 辅助到自主多智能体红队-CSDN博客

原创

网络安全民工
网络安全民工

网络安全民工

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

> **为了规避商业产品风险，本文讨论的是开源Ai渗透产品**

## 前言：

### （一）、AI渗透的几种技术路线

* AI 自主渗透平台：能够自主规划攻击路径、调用工具、验证漏洞和生成报告。
* AI Agent 安全平台：采用多智能体架构，将侦察、漏洞分析、利用验证等任务交给不同 Agent。
* AI 辅助渗透工具：通过 LLM 提升传统扫描器、渗透工具和安全工作流的效率。
* AI 红队与自动化攻击平台：模拟真实攻击者，开展持续自动化红队测试。
* AI 安全运营平台：结合攻击面管理、漏洞验证、风险分析和整改闭环。

### （二）、AI 渗透技术在过去三年经历了明显的范式变化

* 2023：LLM 辅助渗透。 AI 帮助安全人员理解漏洞、生成命令、分析结果，仍以人工操作为主。
* 2024：AI 安全测试与红队自动化。 开始系统化测试大模型本身，出现任务拆解、攻击策略和多轮交互。
* 2025：自主渗透 Agent 爆发。 AI 开始接管信息收集、工具调用、漏洞验证和攻击链执行。
* 2026：多 Agent、白盒分析与工程化。 重点转向自主执行、真实漏洞验证、MCP 工具生态、CI/CD 集成和持续安全测试。

## 一、AI 渗透发展时间轴

### （一）、2023 年：LLM  辅助渗透萌芽——人主导、AI 辅助

1. **2023-02-27｜PentestGPT**

   > 仓库创建：2023-02-27｜首次 PyPI 发布：2023-06-15｜最近可确认代码提交：2026-07-14
   >
   > 早期代表性 LLM 渗透项目。通过任务树、上下文管理和交互式推理辅助渗透人员完成测试流程。

   GitHub 仓库：https://github.com/GreyDGL/PentestGPT?utm\_source=chatgpt.com ·

   PyPI 发布记录：https://pypi.org/project/pentestgpt/?utm\_source=chatgpt.com
2. **2023-04-28｜Promptfoo**

   > 仓库创建：2023-04-28｜最近更新：2026-11-07｜最新 Release：0.125.1（2026-10-25）
   >
   > 从 Prompt 和模型评估工具发展为 LLM 应用、Agent、RAG 的安全测试与红队框架，支持自动化测试和 CI/CD。

   GitHub 仓库：https://github.com/promptfoo/promptfoo?utm\_source=chatgpt.com ·

   Release：https://github.com/promptfoo/promptfoo/releases?utm\_source=chatgpt.com
3. **2023-05-10｜NVIDIA garak**

   > 仓库创建：2023-05-10｜最近代码提交：2026-11-07｜最新 Release：v0.17.1（2026-10-16）
   >
   > 面向大模型漏洞扫描，覆盖 Jailbreak、提示词注入、数据泄露、错误信息生成等风险。

   GitHub 仓库：https://github.com/NVIDIA/garak?utm\_source=chatgpt.com

阶段判断：**AI 开始理解渗透任务，但主要还是“人操作工具，AI 提供建议”**。

### **（二）、2024 年：AI 红队与多步攻击研究——**自动化测试、任务规划

1. **2024-02-22｜Microsoft PyRIT**

   > 首次公开发布：2024-02-22｜后续版本持续演进，2026 年版本记录见项目文档
   >
   > Microsoft 开源的生成式 AI 风险识别工具，支持多轮攻击、目标适配、转换器、评分器和测试记忆管理。

   GitHub 仓库：https://github.com/microsoft/PyRIT?utm\_source=chatgpt.com ·

   Microsoft 首发公告：https://www.microsoft.com/en-us/security/blog/2024/02/22/announcing-microsofts-open-automation-framework-to-red-team-generative-ai-systems/?utm\_source=chatgpt.com
2. **2024-02-29｜AgentDojo**

   仓库创建：2024-02-29｜最近可确认代码提交：2026-06-02

   重点不是完整渗透平台，而是研究使用工具的 LLM Agent 如何受到提示词注入攻击，以及防御机制如何评估。

   GitHub 仓库：https://github.com/ethz-spylab/agentdojo?utm\_source=chatgpt.com

阶段判断：**AI 安全开始从普通漏洞检测扩展到模型、Agent、工具调用和提示词攻击。**

### （三）、2025 年：自主 AI 渗透平台集中出现——Agent 自主执行

1. **2025-01-06｜PentAGI**

   > 仓库创建：2025-01-06｜首次 Alpha：2025-01-07｜最近代码提交：2026-10-22｜最新 Release：v2.2.0（2026-10-05）
   >
   > 多 Agent 自主渗透系统，采用研究、开发、执行等角色分工，集成安全工具、记忆系统、知识存储和 Docker 执行环境。

   GitHub 仓库：https://github.com/vxcontrol/pentagi?utm\_source=chatgpt.com ·

   Release：https://github.com/vxcontrol/pentagi/releases?utm\_source=chatgpt.com
2. **2025-03-31 / 04｜CAI（Cybersecurity AI）**

   > 仓库创建：2025-03-31｜公开发布：2025-04｜最后公开开源版本：0.5.10（2025-12）｜归档：2026-08-28
   >
   > 面向 AI 网络安全攻防的通用框架，支持 Agent、工具、模型和安全研究工作流。注意：该仓库现已归档，不再维护。

   GitHub 仓库
3. **2025-07-10｜HexStrike AI**

   > 仓库创建：2025-07-10｜最近可确认代码提交：2026-08-03
   >
   > 通过 MCP 将 AI Agent 与 150+ 安全工具连接，强调工具发现、参数优化、任务编排和自动化执行。它更接近安全工具编排层，而非独立完成所有工作的完整渗透引擎。

   GitHub 仓库：https://github.com/0x4m4/hexstrike-ai?utm\_source=chatgpt.com
4. **2025-08-05｜Strix**

   > 仓库创建：2025-08-05｜最近代码提交：2026-11-06｜最新 Release：v1.7.0（2026-10-05）
   >
   > 面向 Web 和 API 应用的 AI 渗透工具，结合浏览器、代码理解、多 Agent 协作和漏洞验证，强调发现并证明真实漏洞。

   GitHub 仓库：https://github.com/usestrix/strix?utm\_source=chatgpt.com
5. **2025-09-27｜Shannon**

   > 仓库创建：2025-09-27｜最近代码提交：2026-11-06｜最新 Release：v3.5.0（2026-10-27）
   >
   > 以白盒 Web/API 渗透为核心，通过源码分析发现攻击面，再利用运行环境执行验证。2026 年持续扩展代码分析、报告、CI/CD 和工作区能力。

   GitHub 仓库：https://github.com/KeygraphHQ/shannon?utm\_source=chatgpt.com ·

   Release：https://github.com/KeygraphHQ/shannon/releases?utm\_source=chatgpt.com
6. **2025-05｜DeepTeam**

   > 首次公开 Release：2025-05-23｜最近 Release：v1.0.10（2026-10-16）｜仓库更新记录：2026-10-23
   >
   > 专门测试 LLM、RAG 和 AI Agent 的红队框架，覆盖 Jailbreak、提示词注入、多轮攻击和隐私泄露等场景。

   GitHub 仓库：https://github.com/confident-ai/deepteam?utm\_source=chatgpt.com ·

   PyPI 发布记录：https://pypi.org/project/deepteam/?utm\_source=chatgpt.com

阶段判断：**从“AI 给出建议”走向“AI 自主规划、调用工具、验证漏洞、输出结果”。**

### （四）、2026 年：多 Agent、白盒与工程化——自主红队与持续验证

1. **2026-07-02｜T3MP3ST**

   > 仓库创建：2026-07-02｜最近可确认代码提交：2026-09-08
   >
   > 将现有 AI 编码 Agent 包装成红队执行框架，尝试复用 Claude Code、Codex、Ollama 等现有 Agent 或本地模型，组织侦察、利用和报告流程。

   GitHub 仓库：https://github.com/elder-plinius/T3MP3ST?utm\_source=chatgpt.com
2. **2026 年持续演进｜Shannon 3.x、PentAGI 2.x、Strix 1.x**

   > 代表性方向包括白盒分析与动态验证融合、多 Agent 角色协作、模型适配、沙箱隔离、会话恢复、CI/CD、自动化报告和持续测试。

阶段判断：**竞争重点逐步从“能否调用工具”转向“能否稳定完成攻击链、产出可信证据并融入安全运营”。**

## 二、主要项目发布时间与最近更新时间汇总

以下按首次公开时间排序。日期尽量采用仓库创建日、官方发布公告或 Release 记录；“最近更新”优先指可核实的代码提交或正式版本，而不是第三方网站抓取页面的刷新时间。

| 项目 | 首次公开/创建 | 最近可核实更新 | 项目定位 |
| --- | --- | --- | --- |
| PentestGPT | 2023-02 | 2026-07 代码提交 | AI 辅助/自主渗透 |
| Promptfoo | 2023-04 | 2026-11-07 | LLM 红队 |
| garak | 2023-05 | 2026-11-07 | LLM 漏洞扫描 |
| PyRIT | 2024-02 | 2026-09 版本记录 | AI 红队框架 |
| AgentDojo | 2024-02 | 2026-06-02 | Agent 攻防基准 |
| PentAGI | 2025-01 | 2026-10-22 | 自主多 Agent 渗透 |
| CAI | 2025-03 | 2026-08-28 归档 | 安全 AI 框架 |
| DeepTeam | 2025-05 | 2026-10-23 | LLM/Agent 红队 |
| HexStrike AI | 2025-07 | 2026-08-03 | MCP 安全工具编排 |
| Strix | 2025-08 | 2026-11-06 | 自主应用渗透 |
| Shannon | 2025-09 | 2026-11-06 | 白盒 AI 渗透 |
| T3MP3ST | 2026-07 | 2026-09-08 | 多 Agent 红队编排 |

> 需要特别注意： PentestGPT 的 GitHub 仓库创建时间、PyPI 发布时间不是同一个日期；CAI 已归档；T3MP3ST 的仓库最近代码提交与第三方页面刷新时间也不是一回事。不能用“网页显示最近更新”替代 Git Commit 时间。

## 三、AI 渗透技术演进路线——从  Copilot  到 Autonomous Pentester

**2023｜AI Copilot——人操作，AI 辅助**

> 理解任务、解释命令、生成 POC、分析扫描结果。

**2024｜AI Red Team——AI 规划，自动测试**

> 多轮攻击、任务拆解、提示词注入、攻击效果评分。

**2025｜Autonomous Pentest Agent——AI 规划，Agent 执行**

> 多 Agent、MCP、工具调用、攻击链编排、漏洞验证。

**2026+｜AI Security Operations——自主测试，持续闭环**

> 白盒+黑盒融合、攻击图谱、风险量化、自动复测、持续验证。

## 四、值得重点研究的项目及可借鉴模块

| 项目 | 最值得拆解的能力 | 借鉴价值 |
| --- | --- | --- |
| PentestGPT | 任务树、交互式推理、上下文管理 | 渗透任务规划 |
| PentAGI | 多 Agent 分工、记忆、执行沙箱 | 云端指挥中心与本地执行 |
| CAI | 安全 Agent 框架、轨迹记录、评估 | Agent 运行时与效果评测 |
| HexStrike AI | MCP 工具封装、工具路由 | Skill/Tool/MCP 生态 |
| Strix | 浏览器 Agent、漏洞验证、报告 | Web/API 自主渗透 |
| Shannon | 源码分析、攻击面推导、动态利用 | 白盒与黑盒融合 |
| T3MP3ST | 复用外部编码 Agent、红队编排 | 模型解耦与本地化部署 |
| PyRIT / DeepTeam | AI 应用攻击、攻击策略和评分 | AI 大模型风险评估 |

## 五、AI 渗透平台整体技术格局

### （一）、第一梯队：自主渗透平台

**1、Strix：自主发现、利用验证、PoC**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T0ibbhsCmribQpdxgwibUe9lxx7npPic3YqNDtFnPwOhH6oZdYfky9FjqGLNMu0gl6LvnaGzia1NFEAKCeBC6PlndIHetrYicjRX68TobR9prg1lM/640?wx_fmt=png&from=appmsg)

**2、Shannon：白盒代码分析 + 动态验证**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T0ibbhsCmribRQCnjrdHR91fG9fvCKqOzYiaq58tW0dXAdttgm3z7R3rpKVC1Gia6AyEjia7I2I6BjV0lBZDZp3LdFaVsdgQrUNY0ArTLX5ZmiaOU/640?wx_fmt=png&from=appmsg)

**3、PentAGI：多 Agent + 工具编排**

![](https://mmbiz.qpic.cn/mmbiz_png/T0ibbhsCmribT7picxNGyOjQick4ImXA6BRyzA66dDTu74y4DufDK7aTHzZPlBoPoOpM3N3rB5wcVCBhkD2FJXIgbZMyJPiaEtVypZnzv0ziaTpRo/640?wx_fmt=png&from=appmsg)

**4、PentestGPT：LLM 推理 + 渗透任务规划**

![](https://mmbiz.qpic.cn/mmbiz_png/T0ibbhsCmribQ1ibKUkXR39dqVSVb9FL783X2cBx3IRkpmqU9TC7m3nK3khyX7of7P5ReeDFQicRKhTtUqGlAYYNo3BqibMtiahrGJq6k7I5SBU8Y/640?wx_fmt=png&from=appmsg)

### **（二）、第二梯队：AI 红队与工具编排**

* HexStrike AI：MCP + 大量安全工具。
* CAI：模块化网络安全 Agent 框架。
* CyberStrikeAI：AI 原生安全执行平台。
* RedAmon：AI 红队自动化。
* T3MP3ST：多 Agent 红队框架。

### （三）、第三梯队：AI 安全测试与辅助工具

* promptfoo：AI 应用红队测试。
* garak：大模型漏洞扫描。
* Osmedeus：自动化攻击面工作流。
* hackingBuddyGPT：LLM 辅助主机渗透。

> 参考的开源项目排行榜包括 DeepCyber AI Pentesting Landscape、AI Pentest Tools Leaderboard 和 Awesome AI Pentesting。它们对项目范围的定义并不完全一致，因此本报告将采用广义 AI 渗透技术生态口径。

## 六、GitHub 重点项目 Top 30

下面按研究价值、社区热度和技术相关性整理。

### A. 自主 AI 渗透平台

| 序号 | 项目 | 参考 Star | 核心定位 |
| --- | --- | --- | --- |
| 1 | Strix | 60k+ | 自主 Web/API 渗透 |
| 2 | Shannon | 47k+ | 白盒 AI 渗透 |
| 3 | PentAGI | 22k+ | 多 Agent 自主渗透 |
| 4 | PentestGPT | 15k+ | LLM 渗透任务规划 |
| 5 | HexStrike AI | 11k+ | MCP 安全工具编排 |
| 6 | Cybersecurity AI (CAI) | 9k+ | 模块化安全 Agent |
| 7 | RedAmon | 3k+ | AI 红队自动化 |
| 8 | METATRON | 4k+ | 离线本地 AI 渗透 |
| 9 | Raptor | 3k+ | 进攻性安全自动化 |
| 10 | CyberStr...
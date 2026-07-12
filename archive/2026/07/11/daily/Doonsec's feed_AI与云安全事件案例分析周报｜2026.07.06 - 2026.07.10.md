---
title: AI与云安全事件案例分析周报｜2026.07.06 - 2026.07.10
url: https://mp.weixin.qq.com/s/iZ6TjBxIOQbnJoEF374MvA
source: Doonsec's feed
date: 2026-07-11
fetch_date: 2026-07-12T05:10:15.874720
---

# AI与云安全事件案例分析周报｜2026.07.06 - 2026.07.10

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/mAopIKtZvYuCU4nO7gjXu6bbvPeiaYSnaIiaL761jaWPyjugvQ4VlBT4yKicBMxH93j1qphLiaDpIk082MS2VZvEZYyAzPdSam5QRxTZjbrhMNI/0?wx_fmt=jpeg)

# AI与云安全事件案例分析周报｜2026.07.06 - 2026.07.10

原创

星云实验室
星云实验室

绿盟科技研究通讯

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/mAopIKtZvYuvt6f7WZIKdLcLIKwakNnO1ibz4nZvGTwEwnmV2EmzyjmEvVDaTUGSChGVKEtooicanticgCwDEfcZ76bGsyOI2MxxLhLdK76S9E/640?wx_fmt=gif&from=appmsg)

本周重点集中在 AI Agent 执行边界、AI 编排平台暴露、云身份钓鱼与开发者供应链。

事件一

GhostApproval：AI 编码助手符号链接审批绕过可将恶意仓库变成本地主机入口

事件简介

* 事件概述：Wiz 披露 GhostApproval 攻击模式，指出 Amazon Q Developer、Claude Code、Augment、Cursor、Google Antigravity、Windsurf 等 AI 编码助手在处理恶意仓库内符号链接时，可能把用户批准的“普通项目文件”写入真实敏感目标，例如 ~/.ssh/authorized\_keys、~/.zshrc 或 AI 工具配置。攻击者只需让 Agent 执行“初始化项目”“按 README 设置工作区”等常见动作，即可能获得 SSH 持久化、shell 启动执行或本地凭证读取能力。
* 事件时间：2026-07-09 公开报道，Wiz 于 2026-07-08 发布研究
* 事件链接：https://thehackernews.com/2026/07/ghostapproval-symlink-flaws-could-let.html
* 影响范围：

+ 影响使用 Amazon Q Developer、Claude Code、Augment、Cursor、Google Antigravity、Windsurf 处理不可信仓库的开发者
+ 风险资产包括 SSH 登录文件、shell 启动脚本、AI 工具配置、本地云 CLI 凭证和 AWS 等云身份材料
+ Amazon Q Developer、Cursor、Google Antigravity 已有修复或更新；Augment、Windsurf 仍需规避不可信仓库；Claude Code 对风险归类存在分歧

* 技术分类归属：自治代理层 / AI 供应链层 / 开发者主机身份层 / 公有云身份层
* 事件标签：云AI融合

事件背景与回顾

* 事件背景与架构形态：符号链接本身是传统 Unix 文件系统能力，但 AI 编码助手把“仓库内容”“自然语言指令”“文件写入动作”和“用户审批 UI”串成新的执行链。GhostApproval 的关键不在 symlink 新颖，而在审批窗口只展示表面路径，没有展示最终解析后的真实目标路径。
* 时间线：Wiz 向相关厂商报告后，于 2026-07-08 公开 GhostApproval；2026-07-09 The Hacker News 报道并列出各工具修复状态。该问题与 W26 的 Amazon Q MCP 投毒、Claude Code 幽灵仓库和前周 Bash 旧技巧绕过同属“repo-carried behavior”风险家族。

事件根因深度分析

![](https://mmbiz.qpic.cn/mmbiz_png/mAopIKtZvYujXYOjCS5nwPUIrtNbZCECE2zogSO5dDiaV63sZ9c0zREoeCk88v42dgicsRes2ykcYhcofxxSLZmLS7ZLkGQkic9PJCgPt5NibRI/640?wx_fmt=png&from=appmsg)

* 基础设施与云配置错误：开发者工作站通常同时持有 SSH、GitHub、AWS CLI、容器注册表等身份材料，AI Agent 一旦可跨项目边界写文件，就能绕过传统“仓库沙箱”的心理边界。
* AI 供应链与存储缺陷：恶意仓库不需要直接携带明显恶意二进制，只需携带符号链接、README 指令和看似合理的配置文件名，就可把普通开源仓库变成 Agent 执行载体。
* 前沿算法/工程逻辑缺陷：审批 UI 展示的是 Agent 请求写入的逻辑路径，而不是文件系统最终落点，导致“人类在环”被错误上下文欺骗。
* 复合依赖与应急响应缺陷：同一问题横跨 IDE 插件、命令行 Agent、文件系统解析、权限 UI 和本地凭证管理，修复需要多家厂商同步改写路径解析与审批逻辑。
* 边界防御与分层隔离缺陷：多数 Agent 默认拥有开发者用户权限，缺少只读仓库模式、出项目目录写入阻断、敏感路径二次确认和容器化隔离。

VERIZON DBIR 事件分类

* System Intrusion
* Privilege Misuse

攻击路径与 MITRE ATT&CK 技术映射

| 技术 ID | 技术/子技术名称 | 实际利用方式 |
| --- | --- | --- |
| T1195.001 | Supply Chain Compromise: Software Dependencies and Development Tools | 恶意仓库携带 symlink 与指令诱导 AI 编码助手执行文件写入 |
| T1204.002 | User Execution: Malicious File | 用户批准看似无害的项目文件修改，实际写入敏感系统文件 |
| T1546.004 | Event Triggered Execution: Unix Shell Configuration Modification | 将载荷写入 `.zshrc` 等 shell 启动文件实现后续执行 |
| T1098.004 | Account Manipulation: SSH Authorized Keys | 写入攻击者 SSH 公钥以获得免密登录入口 |
| T1552.001 | Unsecured Credentials: Credentials In Files | 通过 Agent 文件访问能力接触云 CLI 凭证和本地密钥 |

事件二

Langflow 多漏洞遭利用：AI Agent 编排平台成为算力、凭证和二阶段载荷入口

事件简介

* 事件概述：CISA 将 Langflow CVE-2026-55255 加入 KEV，并要求联邦机构紧急修复；该漏洞是 /api/v1/responses 端点的 IDOR，允许已认证攻击者访问其他用户 flow，读取敏感数据并消耗资源。与此同时，Sysdig 观测到针对 Langflow 的野外利用，攻击目标包括代码执行、二阶段 implant 投递、AI 主机算力滥用和 LLM / 云密钥窃取；旧漏洞 CVE-2025-3248 也被 JadePuffer 勒索活动利用。
* 事件时间：2026-07-08
* 事件链接：https://www.bleepingcomputer.com/news/security/cisa-orders-feds-to-prioritize-patching-langflow-auth-bypass-flaw/
* 影响范围：

+ 影响暴露在公网或弱访问控制下的 Langflow AI Agent / workflow 编排平台
+ 风险资产包括 Langflow flows、PostgreSQL 数据库、LLM API key、云访问密钥、GPU/CPU 算力和后续 implant 落地环境
+ 本周相关风险覆盖 CVE-2026-55255、CVE-2025-3248、CVE-2026-33017、CVE-2026-5027 等多条 Langflow 攻击面

* 技术分类归属：编排层 / 自治代理层 / 云基础设施层 / 凭证暴露
* 事件标签：云AI融合

事件背景与回顾

* 事件背景与架构形态：Langflow 是用于构建 AI Agent 与可执行 pipeline 的可视化框架，具备拖拽式节点编排和 REST API 调用能力。它一旦暴露在公网，攻击者拿到 flow、数据库或执行入口后，天然可以顺着 LLM 密钥、云密钥和算力资源继续扩展。
* 时间线：Sysdig 于 2026-06-25 观测 CVE-2026-55255 野外利用；2026-07-08 BleepingComputer 报道 CISA KEV 紧急修复要求。CISA 同期也提示 CVE-2025-3248 已被 JadePuffer 等勒索相关活动利用。

  事件根因深度分析
* 基础设施与云配置错误：AI 编排平台经常为方便调试暴露 API、Web UI 或测试环境，若认证、对象级授权和公网访问控制不足，flow 级别 IDOR 会直接变成数据与执行入口。
* AI 供应链与存储缺陷：Langflow flows 往往保存 prompt、节点配置、工具调用参数、数据库连接和 LLM key；攻击者读取 flow 等同于读取 AI 应用供应链蓝图。
* 前沿算法/工程逻辑缺陷：Agent 编排平台把“模型调用、工具调用、数据访问、代码执行”统一抽象成 flow，权限边界若仍按普通 Web 应用设计，会低估执行链组合风险。
* 复合依赖与应急响应缺陷：同一平台连续出现 IDOR、缺失认证、代码注入、路径穿越等问题，说明漏洞修复不是单点补丁，而是需要重审暴露面和运行时最小权限。
* 边界防御与分层隔离缺陷：AI 主机若同时持有云 key、数据库凭证和外网访问，一次 Langflow 打点即可变成算力劫持、凭证窃取与二阶段载荷投递。

VERIZON DBIR 事件分类

* System Intrusion
* Credential Abuse

攻击路径与 MITRE ATT&CK 技术映射

| 技术 ID | 技术/子技术名称 | 实际利用方式 |
| --- | --- | --- |
| T1190 | Exploit Public-Facing Application | 利用公网暴露的 Langflow API 或 Web 服务进入 AI 编排环境 |
| T1078 | Valid Accounts | 借已认证身份或弱认证访问其他用户 flow |
| T1059 | Command and Scripting Interpreter | 通过 flow 执行能力或二阶段 loader/dropper 实现命令执行 |
| T1552.001 | Unsecured Credentials: Credentials In Files | 从 flow、数据库或环境变量中提取 LLM / 云访问密钥 |
| T1496 | Resource Hijacking | 滥用被攻陷 AI 主机的计算资源运行 botnet、implant 或勒索前置任务 |

事件三

Forg365：AI 辅助 PhaaS 平台将 Microsoft 365 钓鱼、OAuth 与会话持久化产品化

事件简介

* 事件概述：ZeroBEC 披露 Forg365 钓鱼即服务平台，该平台面向 Microsoft 365 账号窃取，集成 AiTM、device-code phishing、AI 辅助诱饵生成、OAuth app 配置、SMTP 配置、token/cookie 管理和后渗透操作。攻击者可用 AI 在同一控制面内生成更贴合业务场景的钓鱼邮件，再通过 ForgCookie 浏览器扩展持续刷新 Microsoft SSO cookie，从而维持对受害者 Microsoft 服务的访问。
* 事件时间：2026-07-09
* 事件链接：https://www.bleepingcomputer.com/news/security/new-forg365-phishing-platform-uses-ai-to-target-microsoft-365-accounts/
* 影响范围：

+ 影响使用 Microsoft 365、Entra ID、OAuth device-code flow 和第三方邮件安全网关的企业
+ 攻击基础设施涉及 Amazon SES、SendGrid 资源、Cloudflare Pages 和 Gophish
+ 风险资产包括 Microsoft 365 账号、SSO cookie、OAuth grants、邮箱规则、会话 token 和云协作数据

* 技术分类归属：公有云身份层 / 应用层 / AI 社工生成 / SaaS 会话持久化
* 事件标签：云AI融合

事件背景与回顾

* 事件背景与架构形态：Forg365 将原本分散的钓鱼链条平台化：邮件生成、落地页、device-code 引导、AiTM 代理、cookie 刷新、OAuth 应用和账号情报面板在同一后台完成。AI 功能不是单纯写邮件，而是降低定制诱饵和平台构建成本。
* 时间线：ZeroBEC 于 2026-07-09 发布分析，BleepingComputer 同日报道。该平台被认为与 Kali365、Sneaky2FA 等 PhaaS 形态存在功能相似性，但公开材料尚未确认直接关联。

事件根因深度分析

![](https://mmbiz.qpic.cn/mmbiz_jpg/mAopIKtZvYtbBggicJNPJXJFap9GpCGjv20JWRx1cZYEicDPboJfhURS7BXJLDx89R5feLsaGibCrz5d1jKyicXzuUYmFUyKrg18tiaAJXCU5Ato/640?wx_fmt=jpeg&from=appmsg)

* 基础设施与云配置错误：企业若默认允许 device-code flow、缺少条件访问约束、OAuth grant 审批和异常 broker 活动监控，会让钓鱼链绕过传统密码拦截。
* AI 供应链与存储缺陷：攻击者把 Amazon SES、SendGrid、Cloudflare Pages 等合法云服务嵌入投递链，提高邮件送达率和基础设施可信度。
* 前沿算法/工程逻辑缺陷：AI 生成内容使钓鱼诱饵更快适配行业、岗位和业务上下文，降低批量定制成本。
* 复合依赖与应急响应缺陷：一次账号失陷后，需要同时撤销 token/session、清理 OAuth grants、检查 mailbox rules、审计新设备登录和 Microsoft Authentication Broker 活动。
* 边界防御与分层隔离缺陷：Microsoft 365 会话 cookie 和 OAuth 权限一旦被接管，可继续访问 SharePoint、OneDrive、Teams、邮件和内部文档。

VERIZON DBIR 事件分类

* Social Engineering
* Credential Abuse

攻击路径与 MITRE ATT&CK 技术映射

| 技术 ID | 技术/子技术名称 | 实际利用方式 |
| --- | --- | --- |
| T1566 | Phishing | AI 辅助生成 Microsoft 365 钓鱼邮件与业务诱饵 |
| T1528 | Steal Application Access Token | 通过 AiTM、device-code flow 和 cookie 管理窃取会话与访问 token |
| T1098.005 | Account Manipulation: Device Registration | 诱导受害者授权攻击者控制的设备或应用 |
| T1114 | Email Collection | 失陷后访问邮箱、规则和账户情报面板 |
| T1567 | Exfiltration Over Web Service | 通过 SaaS 会话将邮件、文档和协作数据带出 |

事件四

Injective SDK npm 供应链投毒：GitHub 贡献者账号失陷后发布钱包窃密包

事件简介

* 事件概述：Injective Labs SDK 项目的 GitHub 仓库被攻击者通过合法贡献者账号入侵，并向 npm 发布恶意版本 @injectivelabs/sdk-ts 1.20.21。该版本在开发者调用生成或导入钱包密钥相关函数时窃取 mnemonic seed phrase 和 private key，并通过伪装成合法基础设施的 HTTP POST 外传。该包每周下载量约 5 万，并进一步影响 17 个关联包和大量依赖链。
* 事件时间：2026-07-09
* 事件链接：https://www.bleepingcomputer.com/news/security/injective-sdk-on-npm-infected-with-cryptocurrency-wallet-stealer/
* 影响范围：

+ 影响使用 Injective SDK 构建钱包、交易机器人、DEX、DeFi 应用和支付工具的开发者
+ 恶意版本 @injectivelabs/sdk-ts 1.20.21 曾被下载约 310 次，另有 17 个关联包被固定到该恶意 SDK 版本
+ 风险资产包括钱包私钥、助记词、开发者本地密钥、CI/CD 环境变量和链上资金

* 技术分类归属：开发者供应链层 / npm 包管理 / 凭证窃取 / CI/CD 生态
* 事件标签：云

事件背景与回顾

* 事件背景与架构形态：攻击者不是直接投放仿冒包，而是入侵合法 GitHub 贡献者账号，修改真实项目并发布真实包的新版本。恶意逻辑不在安装阶段立即触发，而是在钱包密钥函数被调用时激活，提高静态检查和安装期监控难度。
* 时间线：攻击者于 2026-06-08 左右提交可疑变更并发布恶意版本；项目方数分钟内发现并回滚，随后发布干净版本 1.20.23；2026-07-09 BleepingComputer 汇总 Socket、Ox Security、StepSecurity 的分析。

事件根因深度分析

* 基础设施与云配置错误：发布链依赖 GitHub 账号、npm token 和项目维护权限，若贡献者账号缺少强 MFA、最小权限和发布审批，单点失陷即可影响真实包。
* AI 供应链与存储缺陷：虽然该事件不直接利用 AI，但命中 npm、GitHub 和开发者 SDK 供应链；同...
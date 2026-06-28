---
title: 全球智能体安全版图：主要国际厂商的方案、理念与部署路径
url: https://mp.weixin.qq.com/s/8JUByLu3OmYN8Lly58Te5g
source: Doonsec's feed
date: 2026-06-27
fetch_date: 2026-06-28T06:10:16.466880
---

# 全球智能体安全版图：主要国际厂商的方案、理念与部署路径

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibANIaIJODOk2TXxI3mgEmbOmpA5NIibLNbxibHbIFeqszgfKHNtnZ368mCxAzn08eMuZdEBpr0Tficnn4G2hUnKp7ibZk9SV6SteACUXfr6McgE/0?wx_fmt=jpeg)

# 全球智能体安全版图：主要国际厂商的方案、理念与部署路径

dimu
dimu

AI简化安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibANIaIJODOmygeg7kUia347iabcpNSyIb33V8LKzTZ022icqc6xNAAohhlp5Aic3EoKul5pNNH2vwkpiaIORo1b4DDTF53koD46543SBMqticJwS0/640?from=appmsg)

过去一年，企业对生成式 AI 的安全关注主要集中在提示词注入、越狱、敏感数据泄露和模型幻觉。但随着 AI Agent 开始连接数据库、SaaS、API、MCP Server、浏览器、终端和业务系统，风险已经从“回答错了”升级为“真的去执行了”。

智能体安全的核心问题也变成了三句话：

* • 这个 Agent 是谁？
* • 它能访问什么？
* • 它每一步行动是否被授权、被记录、可阻断？

因此，国际主流厂商正在从四个方向布局：云平台原生护栏、安全平台运行时防护、身份治理、AI 资产与暴露面管理。

![](https://mmbiz.qpic.cn/mmbiz_jpg/ibANIaIJODOlxE5rzrtva79FMNucbnmfwnhfGtQktysL5hPia8PqHa9Jan7XUCxJBeQ9F0pmCziajaYgam0Yg6ULahfGmTM7JniaTxQU0kPictc8/640?from=appmsg)

## 一、智能体安全为什么成为独立赛道？

传统 AI 安全更关注模型输入输出：有没有恶意提示词、有没有泄露敏感数据、有没有生成违规内容。智能体安全则进一步关注“行动链条”：Agent 是否调用了不该调用的工具、是否带着过高权限访问系统、是否把外部网页里的恶意指令当成任务、是否把人类身份和 Agent 行为混在一起。

这意味着企业不能只部署一个提示词过滤器，而需要建立一套围绕 Agent 生命周期的控制体系：

* • 身份层：每个 Agent 都应有身份、所有者、权限和生命周期。
* • 网关层：模型调用、工具调用、MCP 请求要经过统一控制点。
* • 运行时层：检测提示词注入、越权工具调用、数据外泄和异常动作。
* • 暴露面层：盘清模型、数据集、推理端点、插件、Agent 框架和云权限。
* • 治理层：把用例、审批、风险、审计和合规证据纳入流程。

一句话：Agent 的价值在于能自主行动，Agent 的风险也来自自主行动。

## 二、国际主要厂商方案速览

![](https://mmbiz.qpic.cn/mmbiz_jpg/ibANIaIJODOkQyfj6HibrReicy5mTwIdfBqVAACRLcFnCgga7U8217MMAYX1V4K3UOLRvorWsnibMBM5riaClBVibgZXHt9GAwy1ZibIRem5rN2SUQ/640?from=appmsg)

### 1. Microsoft：把 Agent 纳入 Defender、Purview 与 Foundry 体系

微软的核心理念是“把 AI Agent 当作企业安全资产纳入统一安全运营”。它不是单点做一个 AI 防火墙，而是把 Agent 的开发、运行、数据治理和威胁检测放进 Microsoft Security 体系。

关键产品与能力：

* • Microsoft Foundry 安全与合规[1]
* • Microsoft Defender for Cloud AI Security Posture[2]
* • Microsoft Purview 管理 Agent 365 数据安全与合规[3]
* • Foundry Guardrails、Prompt Shields、Abuse Detection、Defender XDR、Sentinel 联动

部署方式：主要通过 Azure 订阅、Microsoft Defender Portal、Purview Portal 开启能力。适合已经使用 Azure AI Foundry、Copilot Studio、Microsoft 365、Defender XDR、Sentinel 的大型企业。

适用场景：企业内部 Agent 管理、Copilot 类应用治理、敏感数据防泄露、SOC 统一告警关联。

### 2. AWS：以 AgentCore + Guardrails 构建“可执行边界”

AWS 的核心理念是“Agent 可以自治，但工具调用必须被确定性策略控制”。Amazon Bedrock AgentCore 强调框架无关、模型无关，可以支持 LangGraph、CrewAI、LlamaIndex、Strands Agents 等不同智能体框架。

关键产品与能力：

* • Amazon Bedrock AgentCore[4]
* • AgentCore Policy[5]
* • Amazon Bedrock Guardrails[6]
* • AgentCore Runtime、Gateway、Identity、Observability

部署方式：通过 AgentCore Gateway 拦截工具调用，用 Cedar 策略或自然语言生成策略控制 Agent 可以访问哪些工具、执行哪些动作。Bedrock Guardrails 可在网关边界对输入、输出、工具调用进行检测与阻断。

适用场景：云上自研 Agent、业务流程自动化、跨工具调用授权、需要策略即代码的企业。

### 3. Google Cloud：Model Armor 作为 AI 与 Agent 的运行时护栏

Google Cloud 的核心理念是“在提示词、响应、工具交互路径上做内联检测和阻断”。Model Armor 是 Google Cloud 面向生成式 AI 与 Agentic AI 的运行时安全服务。

关键产品与能力：

* • Google Cloud Model Armor[7]
* • Model Armor 集成文档[8]
* • Gemini Enterprise Agent Platform 配置 Model Armor[9]

部署方式：可以通过 Gemini Enterprise Agent Platform 内联启用，也可以通过 REST API 接入任意模型和基础设施。支持模板级策略和项目级 baseline 策略，用于检测提示词注入、越狱、PII 泄露、恶意 URL、违规内容等。

适用场景：Google Cloud、Vertex AI、Gemini 生态中的 Agent 应用，以及需要多模型运行时护栏的企业。

### 4. Palo Alto Networks：Prisma AIRS 做统一 AI 运行时安全平台

Palo Alto Networks 的核心理念是“Discover、Assess、Protect”，即先发现 AI 资产和 Agent，再评估风险，最后做实时防护。Prisma AIRS 已经从 AI Runtime Security 扩展到 AI Agent Security。

关键产品与能力：

* • Prisma AIRS[10]
* • Prisma AIRS Agent Security[11]
* • Prisma AIRS 文档[12]

核心能力包括 Agent 发现、Agent 身份验证、AI Runtime Firewall、AI Runtime API、AI Red Teaming、AI Model Security、AI Posture Management。

部署方式：支持网络内联拦截、API 嵌入式检测、云账号接入、模型扫描、自动化红队测试。适合多云、多团队、多 Agent 平台并存的大型企业。

适用场景：AI 资产治理、Agent 运行时防护、MCP 风险监测、模型上线前安全评估。

### 5. Cisco：AI Defense 强调网络层内联防护

Cisco 的核心理念是“把 AI 安全嵌入企业网络和安全云”。Cisco 收购 Robust Intelligence 后，将其算法红队、AI Firewall 等能力整合进 Cisco AI Defense。

关键产品与能力：

* • Cisco AI Defense[13]
* • Cisco AI Defense Data Sheet[14]
* • Robust Intelligence is now part of Cisco[15]

部署方式：Cisco 强调网络层可见性和内联防护，不一定要求开发团队改代码或接入 SDK。它可发现 AI 资产，评估模型风险，并在生产环境中用 guardrails 阻断恶意输入、危险输出和 Agent 特定威胁。

适用场景：大型网络环境、云流量治理、MCP Server 检测、AI 应用上线前红队验证。

### 6. CrowdStrike：把终端作为 Agent 安全控制点

CrowdStrike 的核心理念是“AI 在哪里执行，安全就在哪里生效”。它认为很多 Agent 最终会在终端、浏览器、SaaS、云工作负载中触发命令、脚本、文件访问和网络连接，因此端点是关键控制面。

关键产品与能力：

* • Falcon AI Detection and Response[16]
* • CrowdStrike Secure Your AI[17]
* • Charlotte AI AgentWorks[18]

部署方式：依托 Falcon 传感器、Falcon 控制台和安全云，发现 Shadow AI、监控 Agent 行为、阻断提示词攻击和敏感数据泄露，并将 AI 事件与终端、身份、云、威胁情报关联。

适用场景：SOC、终端与浏览器侧 Agent 监测、企业员工使用 GenAI 工具治理、自建安全 Agent 工作流。

### 7. CyberArk 与 Okta：把 Agent 当作“新型非人身份”

身份安全厂商的判断非常明确：Agent 不是普通应用，也不是普通 API Key，而是一类新的机器身份、非人身份和委托身份。

CyberArk 的方案：

* • CyberArk Secure AI Agents[19]
* • CyberArk Secure AI Agents 文档[20]

CyberArk 的核心理念是身份优先、最小权限、零常驻权限。AI Agent Gateway 位于 Agent 与 MCP Server / 工具之间，控制 Agent 何时、以什么权限访问数据库、SaaS、API 和内部资源。

Okta 的方案：

* • Okta for AI Agents[21]
* • Okta for AI Agents GA[22]

Okta 的核心理念是把 Agent 注册为 Universal Directory 中的一等身份，支持发现、登记、授权、短期令牌、访问审查、审计和 kill switch。

部署方式：通常通过身份目录、Agent 注册、短期凭证、MCP / API 访问代理、访问审查流程落地。适合已经有成熟 IAM、PAM、IGA 体系的企业。

适用场景：Agent 访问数据库、工单系统、CRM、ERP、代码仓库、云控制台等高权限资源时。

### 8. Wiz 与 Tenable：从暴露面管理看 Agent 风险

Wiz 和 Tenable 的共同思路是：不要只看单个提示词，而要看 Agent 所在的云环境、身份权限、数据暴露、配置错误和攻击路径。

Wiz 方案：

* • Wiz AI-SPM[23]
* • Wiz AI Agent Security Best Practices[24]

Wiz 将 AI 服务、模型、数据、SDK、云资源和身份权限纳入 Security Graph，做 AI-BOM、AI-SPM、攻击路径分析和修复工作流。

Tenable 方案：

* • Tenable 收购 Apex Security 相关公告[25]
* • Tenable One[26]

Tenable 通过 AI Aware 与 Apex Security 能力，补强 Shadow AI、AI 使用治理、策略执行和 AI 暴露面管理。

部署方式：以云账号接入、资产发现、配置扫描、权限分析、暴露面建模为主。适合已经使用 CNAPP、CSPM、Exposure Management 的企业。

适用场景：云上 AI 资产盘点、AI 服务误配置治理、Agent 过度授权、训练数据和推理端点暴露风险分析。

### 9. IBM：从治理、合规与生命周期角度管理 Agent

IBM 的核心理念是“可信 AI 需要治理系统，而不仅是安全检测”。watsonx.governance 面向 AI 资产、风险、合规、策略和审计，适合监管强、流程重的大型组织。

关键产品与能力：

* • IBM watsonx.governance[27]
* • Agentic AI governance, evaluation and lifecycle[28]
* • Agent monitoring and security metrics in watsonx.governance[29]

部署方式：围绕 AI use case 建立登记、评估、审批、监控、合规报告和安全指标面板，并与 Guardium AI Security 等能力联动。

适用场景：金融、保险、政企、制造等需要 AI 合规审计、模型治理、Agent 决策可追溯的行业。

### 10. HiddenLayer、Check Point / Lakera、NVIDIA：专精型运行时与模型安全能力

这一类厂商更偏“技术组件”或“专精安全层”，常作为大型平台之外的补强。

HiddenLayer：

* • HiddenLayer AI Security Platform[30]
* • 重点能力：AI Discovery、AI Supply Chain Security、Model Scanning、AI Runtime Security、Agentic and MCP Protection。

Check Point / Lakera：

* • Check Point AI Guardrails / Lakera Guard 文档[31]
* • 重点能力：提示词注入检测、数据泄露防护、工具调用检测、Off-Task Action、Tool Allow/Deny List。

NVIDIA NeMo Guardrails：

* • NVIDIA NeMo Guardrails[32]
* • NeMo Guardrails 文档[33]
* • 重点能力：开发者可编程护栏，支持输入、输出、检索、对话、执行、工具调用验证，可作为 Python 库、API Server、容器或 Kubernetes 微服务部署。

适用场景：自研 Agent、模型供应链扫描、MCP 工具调用防护、低代码接入 AI 防火墙、开发阶段安全嵌入。

## 三、怎么选型：四类企业对应四种路线

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibANIaIJODOlNt8TOUUaFeocOKWEKRmHbmWkmRNhraPzDTbm9R2Hkm22f0JgIPyNC5UgWnQXZLjvjyLyRicQUNkGhgG05hHEzRN06eTO7bUjU/640?from=appmsg)

如果企业主要在 Azure、AWS、Google Cloud 上建设 AI 应用，优先看云平台原生能力：Microsoft Defender / Purview / Foundry、Amazon Bedrock AgentCore、Google Model Armor。

如果企业已经有成熟安全平台，希望统一管控多云、多模型、多 Agent，优先看 Palo Alto Prisma AIRS、Cisco AI Defense、CrowdStrike Falcon AIDR。

如果最大风险是 Agent 拿着高权限访问数据库、SaaS、MCP 工具和内部 API，优先看 CyberArk、Okta 这类身份优先方案。

如果企业处在 AI 资产爆发期，还不知道有多少模型、数据集、API Key、推理端点和 Agent，优先看 Wiz、Tenable、HiddenLayer 这类 AI-SPM、暴露面管理和模型供应链安全能力。

## 四、一个更现实的落地架构

企业级智能体安全通常不会是单一产品解决，而是组合架构：

1. 1. 云平台原生能力负责“在哪里运行就在哪里守住基础安全”。
2. 2. 身份平台负责“Agent 到底是谁、能访问什么、何时吊销”。
3. 3. AI 网关负责“模型调用和工具调用统一过策略”。
4. 4. 运行时安全负责“攻击发生时能检测和阻断”。
5. 5. 暴露面管理负责“持续发现影子 AI、误配置和攻击路径”。
6. 6. 治理平台负责“用例、风险、审批、审计和合规报告”。

这也解释了为什么市场上不同厂商看似都在讲 Agent Security，但切入点并不相同：云厂商从开发和运行平台切入，安全平台厂商从流量和运行时切入，身份厂商从非人身份切入，CNAPP / Exposure Management 厂商从资产和攻击路径切入。

## 五、结语：给自治系统上刹车、方向盘和行车记录仪

Agent 的价值在于可以自主规划、调用工具、完成任务。但对企业安全来说，自主性越强，越需要边界。

未来的智能体安全不会只是一个“提示词过滤器”，而会形成一套组合架构：

* • 身份层：每个 Agent 都有身份、所有者和生命周期。
* • 权限层：访问工具和数据时使用短期、最小权限。
* • 网关层：所有模型调用、工具调用、MCP 请求经过统一控制点。
* • 运行时层：检测提示词注入、数据泄露、越权工具调用和异常行为。
* • 治理层：记录用途、风险、审批、审计和合规证据。

一句话总结：智能体安全不是阻止企业使用 Agent，而是让 Agent 在可见、可控、可审计的轨道上释放生产力。

---

## 参考链接

`[1]` Microsoft Foundry 安全与合规: *https://learn.micro...
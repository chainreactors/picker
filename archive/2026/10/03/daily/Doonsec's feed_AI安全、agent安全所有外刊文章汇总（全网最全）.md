---
title: AI安全、agent安全所有外刊文章汇总（全网最全）
url: https://mp.weixin.qq.com/s/OxELrrHM9uhNOAdFThlL4w
source: Doonsec's feed
date: 2026-10-03
fetch_date: 2026-10-04T07:36:30.181581
---

# AI安全、agent安全所有外刊文章汇总（全网最全）

# AI安全、agent安全所有外刊文章汇总（全网最全）

原创

小猫信安
小猫信安

小猫信安

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/a4nfIUib3hYJicib3iae38hLAqF7VNGxETMlJJxYnvMDHwg4icJ4xlKTY0Unku4O8pNmTItPEac4L4kqs5p8ia98RQAeicbgZhIf5oTf9r5Unggyo0/640?wx_fmt=png&from=appmsg)

> 温馨提示：文章字体最小号阅读最佳
>
> 请善用curl+f搜索

## 目录

```
威胁框架与标准综述与系统化研究攻击研究通过工具进行提示词注入工具投毒与供应链权限提升与过度授权数据外泄与隐私间接提示词注入跨插件攻击针对 Agent 的后门攻击Agent 欺骗与操控越狱与护栏绕过防御研究权限与访问控制运行时监控与沙箱输入/输出校验形式化验证与分析评估与红队测试基准测试与数据集工具与框架Agent Skill 规范行业报告与博客文章
```

---

## 威胁框架与标准

* ```
  OWASP Agentic AI Threats and Mitigations（OWASP 代理式 AI 威胁与缓解）： https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/OWASP Top 10 for LLM Applications（OWASP LLM 应用前 10 大风险）： https://owasp.org/www-project-top-10-for-large-language-model-applications/OWASP Agentic Skills Top 10 (AST10)（OWASP Agentic Skills 前 10 大风险）： https://owasp.org/www-project-agentic-skills-top-10/MITRE ATLAS™（ATLAS 威胁地图）： https://atlas.mitre.org/NIST AI Risk Management Framework（NIST AI 风险管理框架）： https://www.nist.gov/artificial-intelligence/ai-risk-management-frameworkNIST SP 800-218A: Secure Software Development for AI（NIST AI 安全软件开发）： https://csrc.nist.gov/pubs/sp/800/218/a/finalEU AI Act（欧盟 AI 法案）： https://artificialintelligenceact.eu/Anthropic Responsible Scaling Policy（Anthropic 负责任扩展政策）： https://www.anthropic.com/index/anthropics-responsible-scaling-policyIETF draft-klrc-aiagent-auth-01: AI Agent Authentication and Authorization（AI Agent 身份认证与授权草案）： https://datatracker.ietf.org/doc/draft-klrc-aiagent-auth/IETF draft-niyikiza-oauth-attenuating-agent-tokens-00: Attenuating Authorization Tokens for Agentic Delegation Chains（Agent 委托链授权令牌削弱草案）： https://datatracker.ietf.org/doc/draft-niyikiza-oauth-attenuating-agent-tokens-00/Certifying Ghosts: How Cybersecurity AI Agents Break the EU Cyber Resilience Act（网络安全 AI Agent 如何突破 EU Cyber Resilience Act）： https://arxiv.org/abs/2607.07109综述与系统化研究Connecting the Dots in Agentic AI Security: A Cross-Dimensional Threat Taxonomy, Evaluation Maturity, and Open Challenges（连接各类 Agentic AI 安全研究点）： https://arxiv.org/abs/2609.23894Trustworthy Agentic AI: Failure Modes, Mitigation Strategies, and a Lifecycle Framework for Autonomous LLM Systems（可信 Agentic AI：失效模式、缓解策略与生命周期框架）： https://arxiv.org/abs/2609.22712Attack Success Rate Is Not a Number: On Measurement Validity in Agentic AI Security Evaluation（攻击成功率并非数字：Agentic AI 安全评估的有效性研究）： https://arxiv.org/abs/2609.25173A Survey on LLM-based Autonomous Agents: Common Attacks and Defenses（LLM 自主 Agent 攻击与防御综述）： https://arxiv.org/abs/2402.09283Agent Security Bench (ASB): Formalizing and Benchmarking Attacks and Defenses in LLM-based Agents（Agent 安全 benchmark）： https://arxiv.org/abs/2410.02644Security of AI Agents（AI Agent 安全）： https://arxiv.org/abs/2406.08689Not All Agents Are Created Equal: A Survey on Software-use Agent Security（并非所有 Agent 都一样：软件使用型 Agent 安全综述）： https://arxiv.org/abs/2502.02761A Survey on the Honesty of Large Language Models（大语言模型诚实性综述）： https://arxiv.org/abs/2409.18786A Comprehensive Study of Jailbreak Attack versus Defense for Large Language Models（大语言模型越狱攻击与防御综述）： https://arxiv.org/abs/2402.13457Prompt Injection Attacks and Defenses in LLM-Integrated Applications（LLM 集成应用中的 Prompt Injection 攻击与防御）： https://arxiv.org/abs/2310.12815The Emerged Security and Privacy of LLM Agent: A Survey with Case Studies（LLM Agent 的安全与隐私综述与案例研究）： https://arxiv.org/abs/2407.19354Self-Evolving Agents: A Survey（自进化 Agent 调研）： https://arxiv.org/abs/2504.01641Safety in Self-Evolving LLM Agent Systems: Threats, Amplification, and Case Studies（自进化 LLM Agent 系统安全）： https://arxiv.org/abs/2606.23075From Thinker to Society: Security in Hierarchical Autonomy Evolution of AI Agents（从思考者到社会：分层自治 AI Agent 安全）： https://arxiv.org/abs/2603.07496Characterizing Faults in Agentic AI: A Taxonomy of Types, Symptoms, and Root Causes（Agentic AI 故障分类）： https://arxiv.org/abs/2603.06847Security Considerations for Multi-agent Systems（多 Agent 系统安全考量）： https://arxiv.org/abs/2603.09002The Attack and Defense Landscape of Agentic AI: A Comprehensive Survey（Agentic AI 攻击与防御全景综述）： https://arxiv.org/abs/2603.11088Taming OpenClaw: Security Analysis and Mitigation of Autonomous LLM Agent Threats（OpenClaw 安全分析与缓解）： https://arxiv.org/abs/2603.11619OpenClaw as Language Infrastructure: A Case-Centered Survey of a Public Agent Ecosystem in the Wild（OpenClaw 作为语言基础设施的案例调查）： https://www.preprints.org/manuscript/202603.1060AgenticCyOps: Securing Multi-Agentic AI Integration in Enterprise Cyber Operations（企业网络运营中的多 Agent 安全框架）： https://arxiv.org/abs/2603.09134MCP-in-SoS: Risk Assessment Framework for Open-Source MCP Servers（开源 MCP Server 的系统风险评估框架）： https://arxiv.org/abs/2603.10194SoK: The Attack Surface of Agentic AI — Tools, and Autonomy（Agentic AI 攻击面综述）： https://arxiv.org/abs/2603.22928Toward Secure LLM Agents: Threat Surfaces, Attacks, Defenses, and Evaluation（面向安全 LLM Agent 的威胁面、攻击、防御与评估）： https://arxiv.org/abs/2606.10749Data Agents Under Attack: Vulnerabilities in LLM-Driven Analytical Systems（数据 Agent 遭遇攻击）： https://arxiv.org/abs/2606.08661Agents That Know Too Much: A Data-Centric Survey of Privacy in LLM Agents（知道太多的 Agent：面向数据中心的隐私调查）： https://arxiv.org/abs/2606.26627Security Engineering of OpenClaw: Analyzing Attack Surface Expansion and Trust-Boundary Violations（OpenClaw 的安全工程分析）： https://arxiv.org/abs/2606.15008LLM Agents Security Duality: A Comprehensive Survey of Self-Security and Empowered Cybersecurity（LLM Agent 安全二象性综述）： https://arxiv.org/abs/2606.28450Agent Security Meets Regulatory Reality: A Practitioner Systematization of Autonomous-Agent Threats and Controls in Regulated Financial Systems（Agent 安全与监管现实结合）： https://arxiv.org/abs/2606.29142Security and Privacy in Agentic AI: Grand Challenges and Future Directions（Agentic AI 安全与隐私的重大挑战与未来方向）： https://arxiv.org/abs/2607.06608Trust but Verify? Uncovering the Security Debt of Autonomous Coding Agents（信任但验证？揭示自治编码 Agent 的安全债务）： https://arxiv.org/abs/2607.12428Agent Skill Security: Threat Models, Attacks, Defenses, and Evaluation（Agent Skill 安全：威胁模型、攻击、防御与评估）： https://arxiv.org/abs/2607.13987The Ethics of Autonomous AI Agents for Offensive Security（用于攻击性安全的自治 AI Agent 的伦理问题）： https://arxiv.org/abs/2607.20255The Chronos Vulnerability: A Taxonomy of Temporal Persistence and Memory-Based Deception in Agentic AI（Chronos 漏洞：Agentic AI 中时间持久化与记忆欺骗分类）： https://arxiv.org/abs/2607.19433Engineering Trustworthy Agentic AI for Critical Systems（关键系统中的可信 Agentic AI 工程）： https://arxiv.org/abs/2607.18548Agent Security Needs Redefinition through a Holistic Framework（Agent 安全需要整体框架重定义）： https://arxiv.org/abs/2607.22024An Empirical Study of Model Context Protocol Applications（MCP 应用实证研究）： https://arxiv.org/abs/2607.25635Security of World-Model-Based Embodied AI: A Lifecycle of Threats, Defenses, and Evaluation（基于世界模型的具身 AI 安全）： https://arxiv.org/abs/2607.28226From Monoliths to Swarms: A Study of Attack Surface Evolution in the Transition to Multi-Agent Web Systems（从单体到群体：多 Agent Web 系统攻击面演进研究）： https://arxiv.org/abs/2608.00202The Vulnerability With No CVE: Managing Persistent Gaps Between Mandate and Authority in AI Coding Agents（没有 CVE 的漏洞：管理 AI 编码 Agent 的授权与职责差异）： https://arxiv.org/abs/2608.05884On Understanding, Identifying, and Mitigating Vulnerabilities in Agentic Large Language Models（理解、识别与缓解 Agentic LLM 漏洞）： https://arxiv.org/abs/2608.10530When Agents Act on Web3: An Attack-Surface Survey of MCP, Skills, and Tool Calling（Agent 参与 Web3 时的攻击面研究）： https://arxiv.org/abs/2608.17275A2ABreak: Systematic Security Analysis of the A2A Protocol（A2A 协议系统安全分析）： https://arxiv.org/abs/2609.10871When Passing Tests Hides Vulnerabilities: An Empirical Study of Silent Failures in Agentic Systems（测试通过掩盖漏洞：Agentic 系统沉默失败实证研究）： https://arxiv.org/abs/2609.10548Trustworthy Agentic AI: A Comprehensive Cybersecurity and Systems Survey on Threat Landscapes, Defense Architectures, and Open Challenges（可信 Agentic AI：威胁、架构与开放挑战的全面综述）： https://arxiv.org/abs/2609.13731Authorization Architectures ...
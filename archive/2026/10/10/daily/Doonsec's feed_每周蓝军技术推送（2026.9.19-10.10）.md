---
title: 每周蓝军技术推送（2026.9.19-10.10）
url: https://mp.weixin.qq.com/s/f9PVBtI_caYEopnAyuEQaw
source: Doonsec's feed
date: 2026-10-10
fetch_date: 2026-10-11T08:00:19.102331
---

# 每周蓝军技术推送（2026.9.19-10.10）

# 每周蓝军技术推送（2026.9.19-10.10）

原创

天元实验室
天元实验室

M01N Team

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/uZT6kWW1jCk5Ml9CgYSLdF7u0ZK2OgFibgCXs6NRHwOviav7uP8lDFHKkY7Jwb4SAGf8UCjaNl2In5nTSfGV4ypibo7zU0RdCMC8Y9zOhabB6c/640?wx_fmt=png&from=appmsg)

**内网渗透**

研究使用重叠片段技术突破令牌长度限制，实现大尺寸令牌外带

https://portswigger.net/research/smashing-the-token-limit

**终端对抗**

分析攻击者滥用新型RMM工具，通过带OpenAction的恶意PDF投递VBS载荷

https://isc.sans.edu/diary/rss/33400

ClickFix攻击演变，利用DNS TXT记录与浏览器缓存预取隐藏恶意载荷

https://www.darkreading.com/cyberattacks-data-breaches/clickfix-attacks-evolve-better-hide-malicious-payloads

HollowGraph：无需独立C2服务器，调用微软Graph API通过受害者M365日历收发指令与数据

https://www.dugganusa.com/post/this-iranian-malware-has-no-c2-server-to-block-the-command-channel-is-a-meeting-invite-in-your-own

**漏洞相关**

CVE-2026-21589：Atlassian多产品任意文件读取漏洞，已观测到在野扫描攻击

https://isc.sans.edu/diary/rss/33406

CVE-2026-88771、CVE-2026-88772：Citrix NetScaler零日漏洞，已发现存在在野利用

https://unit42.paloaltonetworks.com/netscaler-zero-days-exploited/

CVE-2026-42016、CVE-2026-42018、CVE-2026-82329：在野链式利用，未授权接管Artifactory植入后门

https://www.wiz.io/blog/artifactory-under-attack-in-the-wild-exploitation-of-cve-2026-42016-cve-2026-4201

CVE-2026-66804：分析Windows悬空COM对象注册导致权限提升的漏洞利用技术

https://projectzero.google/2026/09/windows-dangling-com.html

Fragnesia新变种：通过Open vSwitch清除skb共享标记，实现无特权本地提权

https://blog.doyensec.com/2026/09/17/ovs.html

CVE-2026-39987：公开marimo漏洞手工编写的利用方式，披露攻击链检测特征

https://www.sysdig.com/blog/machine-speed-hold-the-ai-hand-rolled-marimo-cve-2026-39987-exploit

BlueMoon：串联Chrome与Windows零日漏洞的新型漏洞利用套件

https://www.proofpoint.com/us/blog/threat-insight/once-bluemoon-multiple-state-aligned-threat-actors-rapidly-adopt-novel-exploit

百万美元沙箱挑战赛曝出两处Linux内核网络栈缺陷，可确定性导致宿主机崩溃与内核内存泄漏

https://www.securityweek.com/1-million-sandbox-challenge-uncovers-linux-kernel-flaws/

分析大型厂商的漏洞快速修复系统，为厂商紧急补丁能力建设提供参考

https://projectzero.google/2026/10/emergency-patching.html

**人工智能和安全**

opencode-chat-replay.py、hermes\_forensic\_extract.py：提取两款AI编程代理的操作痕迹完成取证重建

https://isc.sans.edu/diary/rss/33410

AgentCorruption：AWS Bedrock AgentCore已修补漏洞，单提示可接管企业全云环境舰队

https://www.darkreading.com/cloud-security/agentcorruption-aws-environments-at-risk-single-prompt

分析AWS AgentCore Harness默认配置缺陷，提示注入可窃取凭据并给出加固步骤

https://unit42.paloaltonetworks.com/securing-aws-agentcore-harness-credentials/

AISI开展AI安全测试时，被测AI代理自主发起未授权供应链攻击与社工操作

https://www.aisi.gov.uk/blog/incident-report-unsanctioned-agent-behaviour-during-cyber-testing

Anthropic复盘发现Claude突破测试隔离环境，未授权访问三家机构生产系统

https://www.anthropic.com/news/investigating-incidents-cybersecurity-evals

Google GTIG研究AI时代漏洞发现趋势，披露少数AI编排框架存在在野利用漏洞

https://cloud.google.com/blog/topics/threat-intelligence/vulnerability-discovery-and-exploitation-trends-in-the-ai-era

自主AI代理实时动态选择攻击路径入侵零售站点，窃取超60万张信用卡数据

https://gambit.security/blog-posts/autonomous-ai-agents-online-retailers-25-a-company

验证AI代理仅凭漏洞传闻即可快速挖掘对应利用代码，探讨开源安全响应改进方向

https://anil.recoil.org/notes/rumour-is-the-exploit

分析AI可自动化网络攻击环节，探讨攻防两端利用AI强化安全的可行路径

https://blog.gregbrockman.com/the-defenders-window

Scan for Good：结合Gemini系列模型与人工研究员，扫描公网高危暴露点

https://www.wiz.io/blog/scan-for-good-critical-ai-exposures

研究大模型沙箱逃逸网络限制方法，利用DNS欺骗、CDN IP共享实现突破（厂商授权红队演练，仅少数尝试成功）

https://www.perplexity.ai/hub/blog/escaping-space-part-i

PageBreak：谷歌自研AI安全代理，用于测试Web应用安全，解决大模型扫描高误报问题

https://blog.google/security/agentic-hacks-real-proofs-inside-googles-pagebreak-project/

https://bughunters.google.com/blog/pagebreak-real-world-findings

Model Inversion：识别PR的AI生成属性，路由至对立大模型交叉检测高危代码漏洞

https://www.greptile.com/blog/model-inversion

对比多款开源AI代码安全校验框架，梳理代码执行验证等核心差异维度

https://semgrep.dev/blog/2026/comparing-open-source-ai-code-security-harnesses

AISI测评主流开源大模型网安能力，验证其安全对齐易被剥离，使用成本远低于闭源模型

https://www.aisi.gov.uk/blog/how-far-behind-the-frontier-are-leading-open-weight-models-on-cyber

BOTS v3基准：测试多款大模型基于Splunk完成安全事件调查的性能

https://defensebench.ai/benchmarks/botsv3

分析AI代理LOBL行为引发的告警噪声问题，提出基于信号置信度关联的检测方案

https://jvehent.org/2026/09/22/detection-fidelity-ai-agents.html

提出语义恶意软件场景检测方案，设计标准化遥测、类Sigma规则及演练体系

https://detect.fyi/detection-engineering-in-the-era-of-semantic-malware-663cee8cda7b

Numbat：开源智能体端侧防护套件，使用CEL表达式实现52条行为检测规则，可自动生成新规则

https://www.perplexity.ai/hub/blog/securing-agents-across-perplexity-s-client-endpoints-with-numbat

guard-skills：面向编码AI代理的质量门禁，可捕获AI生成的代码、测试与文档失效模式

https://github.com/amElnagdy/guard-skills

promptzero：Claude透明API代理，在数据流出本地前匿名化PII与敏感数据

https://github.com/openbashok/promptzero

prempti：基于Falco构建，为AI编码代理提供安全策略与运行可见性的防护层

https://github.com/falcosecurity/prempti

destructive\_command\_guard：拦截AI代理执行危险命令，支持白名单配置与CI文件扫描的防护工具

https://github.com/Dicklesworthstone/destructive\_command\_guard

mantis：栈无关模块化工具，支持AI编码代理自主查找、复现、修补漏洞

https://github.com/google/mantis

defending-code-reference-harness：可自定义自主扫描框架，集成多环节能力保障源代码安全

https://github.com/anthropics/defending-code-reference-harness

datadog-saist：AI原生静态代码检测工具，拉取API检测提示无需Datadog认证

https://github.com/DataDog/datadog-saist

Claude Security：依托Mythos 5.1扫描代码追溯数据流，识别漏洞并生成可审核补丁

https://claude.com/product/claude-security

socbench：面向网络安全运营场景的大模型代理公开测试基准框架

https://github.com/DeepTempo/socbench

RAMPART：基于pytest原生实现的智能体AI应用安全测试框架

https://github.com/microsoft/RAMPART

llm-observer-proxy-go：搭载嵌入式Bifrost数据平面的运行域LLM观测代理

https://github.com/xxyyue/llm-observer-proxy-go

研究AI代理最小权限管控方案，提出专属身份、访问控制与工具绑定等落地安全机制

https://www.microsoft.com/en-us/security/blog/2026/07/16/least-privilege-for-ai-agents-identity-access-and-tool-binding/

Skill Poisoning攻击：伪造AI代理技能插件，诱导AI后台自动下载投放恶意软件

https://ministryofcyberaffairs.com/news/skill-poisioning-turning-ai-agents-into-malware-droppers-warns-china-s-national-cert-66b8bba4-9ffd-4583-a6c7-122e8149e0e8

**云安全**

Unit 42分析攻击者利用Web3基础设施结合开源供应链攻击入侵企业云环境

https://unit42.paloaltonetworks.com/web3-cloud-supply-chain-attacks/

OperTraitor：审计Kubernetes Operator权限，识别过度RBAC风险，加固非人类身份安全

https://unit42.paloaltonetworks.com/agentic-ai-kubernetes-operator-risks/

CiliumHound：BloodHound OpenGraph扩展，生成Cilium网络策略图谱用于审计排查缺口

https://specterops.io/blog/2026/09/17/ciliumhound-graphing-kubernetes-network-policies/

研究使用FleetDM+Osquery+YARA组合，实现K8s环境大规模内存恶意代码狩猎

https://holdmybeersecurity.com/2026/07/14/hunting-malware-and-malicious-mcps-in-memory-on-kubernetes-with-fleetdm-osquery-yara/

分析Scaleway云IAM信任边界，梳理攻击者持被盗凭据接管账户的攻击路径

https://cyber.zorgenkind.eu/posts/Mapping-Scaleway-IAM/

分析AWS通过托管策略处置泄露IAM凭证，详述GitHub密扫与CloudTrail监控方案

https://unit42.paloaltonetworks.com/detecting-exposed-aws-iam-credentials/

设计行为聚类模型从云审计日志映射身份角色，通过标准SQL实现持续威胁检测

https://unit42.paloaltonetworks.com/behavioral-clustering-map-to-cloud-identities/

披露谷歌GFile未授权访问利用方案，借助AI预测隐藏路径获取敏感文件

https://bughunters.google.com/blog/breaking-into-googles-gfile-for-100k

针对150余家机构AWS根账号的密码喷洒攻击，给出SCP等云侧防护方案

https://securitylabs.datadoghq.com/articles/aws-root-user-bruteforce-campaign

分析四种Azure Blob存储勒索手法，附带检测事件码与红队模拟技术

https://securitylabs.datadoghq.com/articles/azure-blob-storage-ransomware-four-methods/

Zapocalypse：针对Zapier的攻击链，本可发布任意JS在所有用户会话中运行，官方已披露并修复

https://www.token.security/blog/zapocalypse-the-attack-chain-that-could-have-hijacked-zapier

基于多代理Swarm架构改造云影子资产扫描器，生成多格式安全报告与修复指令

https://aws.plainenglish.io/adding-strands-security-agents-to-shadow-asset-scanner-60c236c84b7e

梳理AWS EKS各层取证数据源，提供节点凭据泄露、容器逃逸的检测查询方法

https://www.synacktiv.com/en/publications/aws-eks-forensics-data-sources-and-investigation-tooling.html

分析Hugging Face入侵事件复盘，指出Tailscale并未阻断该次入侵，建议改用短时效OIDC令牌替代可复用auth key

https://tailscale.com/blog/hugging-face-intrusion

分析AWS持久化滥用合法身份特性，给出关联身份凭据的检测处置方法

https://www.rapid7.com/blog/post/dr-investigating-aws-persistence-mechanisms

AWS Continuum：推理多源异构数据，覆盖代码漏洞发现到修复，含STRIDE威胁建模预览能力

https://aws.amazon.com/blogs/security/introducing-aws-continuum-security-at-machine-speed

分析GCP日志导出时serviceData字段被剔除，引发安全检测静默失效问题

https://permiso.io/blog/gcp-servicedata-officially-deprecated-actively-dangerous

分析Salesforce云平台攻击面，提供对应MITRE ATT&CK战术的狩猎查询方法

https://securitylabs.datadoghq.com/art...
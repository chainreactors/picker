---
title: AI安全专题周报（20260911）
url: https://blog.netlab.360.com/aian-quan-zhuan-ti-zhou-bao-5/
source: 360 Netlab Blog - Network Security Research Lab at 360
date: 2026-09-11
fetch_date: 2026-09-12T06:48:33.748528
---

# AI安全专题周报（20260911）

[![360 Netlab Blog - Network Security Research Lab at 360](https://blog.netlab.360.com/content/images/2019/02/netlab-brand-5.png)](https://blog.netlab.360.com)

* [Botnet](https://blog.netlab.360.com/tag/botnet/)
* [DNSMon](https://blog.netlab.360.com/tag/dnsmon/)
* [DDoS](https://blog.netlab.360.com/tag/ddos/)
* [PassiveDNS](https://blog.netlab.360.com/tag/pdns/)
* [Mirai](https://blog.netlab.360.com/tag/mirai/)
* [DTA](https://blog.netlab.360.com/tag/dta/)

# AI安全专题周报（20260911）

* [![NOTOn1y](/content/images/size/w100/2026/08/2f35bd757c0c0fcb537ee47e8fa31171.jpg)](/author/on1y/)

#### [NOTOn1y](/author/on1y/)

11 Sep 2026
• 52 min read

[Share](#/share)

**报告编号：**TIC-202609-AI02

**报告周期：**2026年9月5日—9月11日

## 一、报告概述

基于360威胁情报中心对本期公开网络安全素材的整理与分析，本周AI安全风险主要集中在AI智能体自动化攻击、生成式AI辅助社会工程、AI平台跨账号数据泄露、模型网关与推理组件漏洞、隐蔽提示攻击以及AI代理本地数据窃取等方向。相关事件显示，AI正从辅助单点任务向编排完整攻击流程发展，同时AI平台、模型组件、代理配置和连接应用也形成新的高价值攻击面。

**报告重点内容涵盖：**

**· AI辅助攻击与欺诈：**数百个AI智能体被用于编排PaperCut全球攻击，攻击者还使用AI生成邮件模板实施高管冒充和虚假发票欺诈。

**· AI平台与代理数据风险：**ChatGPT沙箱隔离问题形成跨账号隐蔽通道，信息窃取恶意软件开始收集AI工具令牌、MCP配置、提示历史和项目数据。

**· 模型与工具链安全：**LiteLLM漏洞链可导致云环境失陷，PuzzleMask可通过纯文本散文隐藏恶意提示，Ollama解码组件存在整数溢出风险，对抗性AI活动正进一步走向自主化。

───────────────────────────────────

## 二、本周重点安全事件

### （一）数百个AI智能体编排PaperCut全球攻击

**事件名称：**26秒攻陷11家机构：一场由数百个AI智能体编排的PaperCut全球攻击行动

**发布日期：**2026-09-10

**发布机构：**奇安信威胁情报中心

**威胁概述：**

奇安信威胁情报中心援引GreyNoise披露，一场由数百个AI智能体编排的全球攻击行动利用PaperCut NG/MF漏洞CVE-2026-81578和CVE-2026-82078，在无需认证的情况下实现远程代码执行。攻击者随后转储LSASS进程内存与注册表凭据，通过传递哈希或noPac漏洞链横向移动，并利用DCSync获取域凭据。素材显示，该行动在26秒内攻陷11家机构，涉及教育、零售、房地产、政府和医疗等行业。

**IOC指标：**

**· CVE：**CVE-2026-81578, CVE-2026-82078, CVE-2021-42278, CVE-2021-42287, CVE-2023-27350

**· IP：**45.142.193.132, 45.158.196.75

**· MD5：**528cd4e69ecfa5191adbcf6ef28667bf, ce870a91e8d27e8f663f0687abc60b04, a6437ac3d6798090a218520985d36a3f, fc92dfafa7aa741c5f2b9cbcf75d1d19, 974decb9ff4c8f9ccb0937c96d513347

**· URL：**http://45.142.193.132:8000/lsa\_collect.exe, http://45.142.193.132:8089/agent5.exe

**STIX详情：**

```
{
  "type": "bundle",
  "id": "bundle--efd1c3ca-29ca-40d8-ba02-1a0e29e68b0f",
  "spec_version": "2.1",
  "objects": [
    {
      "type": "campaign",
      "spec_version": "2.1",
      "id": "campaign--5c1cece8-9cd5-481d-baa3-163ffa76ed63",
      "name": "PaperCut NG/MF全球攻击行动",
      "created": "2026-09-10T10:57:49Z",
      "modified": "2026-09-10T10:57:49Z",
      "description": "由数百个AI智能体编排，针对PaperCut NG/MF两个在野漏洞发动的全球性大规模攻击行动",
      "x_evidence": "GreyNoise最新披露的一起针对PaperCut NG/MF的全球性攻击行动",
      "x_confidence": 0.95
    },
    {
      "type": "intrusion-set",
      "spec_version": "2.1",
      "id": "intrusion-set--7600e39f-054b-4768-a076-e877bb025429",
      "name": "疑似俄语背景攻击者",
      "created": "2026-09-10T10:57:49Z",
      "modified": "2026-09-10T10:57:49Z",
      "description": "通过OpenAI Codex作为智能体运行框架、DeepSeek模型作为实际执行模型，编排数百个AI智能体执行攻击的攻击者",
      "x_evidence": "一名疑似俄语背景的攻击者利用IP地址45.142.193.132...发动了一场全球性的大规模攻击行动",
      "x_confidence": 0.9
    },
    {
      "type": "infrastructure",
      "spec_version": "2.1",
      "id": "infrastructure--09774ad3-dc7f-4340-94d7-b7d8f9a28eb7",
      "name": "PaperCut NG/MF",
      "created": "2026-09-10T10:57:49Z",
      "modified": "2026-09-10T10:57:49Z",
      "description": "受攻击的打印管理软件",
      "x_evidence": "PaperCut是广泛部署于学校、企业、政府机构和托管服务商的打印管理软件；其中NG和MF为自托管的Java Web应用",
      "x_confidence": 0.97
    },
    {
      "type": "identity",
      "spec_version": "2.1",
      "id": "identity--704c127a-a16b-45d2-add8-0ce7a6953064",
      "name": "GreyNoise",
      "created": "2026-09-10T10:57:49Z",
      "modified": "2026-09-10T10:57:49Z",
      "description": "披露并持续跟踪此次全球性攻击行动的威胁情报机构",
      "x_evidence": "GreyNoise最新披露的一起针对PaperCut NG/MF的全球性攻击行动",
      "x_confidence": 0.99
    },
    {
      "type": "vulnerability",
      "spec_version": "2.1",
      "id": "vulnerability--a22d0a23-d8ce-4e20-b933-47d716b9497c",
      "name": "CVE-2026-81578",
      "created": "2026-09-10T10:57:49Z",
      "modified": "2026-09-10T10:57:49Z",
      "description": "PaperCut NG/MF Web管理接口关键功能缺失身份验证漏洞",
      "x_evidence": "CVE-2026-81578让攻击者无需任何凭据即可修改系统配置",
      "x_confidence": 0.96
    },
    {
      "type": "vulnerability",
      "spec_version": "2.1",
      "id": "vulnerability--e90e2ec7-cba0-456e-a0c1-0afb503584f1",
      "name": "CVE-2026-82078",
      "created": "2026-09-10T10:57:49Z",
      "modified": "2026-09-10T10:57:49Z",
      "description": "PaperCut NG/MF数据库连接工具组件不安全的动态类加载漏洞",
      "x_evidence": "被篡改的配置（数据库驱动类名）随即触发CVE-2026-82078，使服务器加载并执行攻击者指定的Java代码",
      "x_confidence": 0.96
    },
    {
      "type": "intrusion-set",
      "spec_version": "2.1",
      "id": "intrusion-set--621f44bf-281b-4e7e-8bee-8b144badbdc2",
      "name": "Clop",
      "created": "2026-09-10T10:57:49Z",
      "modified": "2026-09-10T10:57:49Z",
      "description": "曾大规模利用PaperCut漏洞的勒索团伙",
      "x_evidence": "2023年CVE-2023-27350/27351就曾被Clop、LockBit、Bl00dy等勒索团伙大规模利用",
      "x_confidence": 0.85
    },
    {
      "type": "intrusion-set",
      "spec_version": "2.1",
      "id": "intrusion-set--4f62692a-2660-4ace-8c04-a322a2a3c243",
      "name": "LockBit",
      "created": "2026-09-10T10:57:49Z",
      "modified": "2026-09-10T10:57:49Z",
      "description": "曾大规模利用PaperCut漏洞的勒索团伙",
      "x_evidence": "2023年CVE-2023-27350/27351就曾被Clop、LockBit、Bl00dy等勒索团伙大规模利用",
      "x_confidence": 0.85
    },
    {
      "type": "intrusion-set",
      "spec_version": "2.1",
      "id": "intrusion-set--238b5866-ac2c-4cf7-a489-55fa3ffbf3fb",
      "name": "Bl00dy",
      "created": "2026-09-10T10:57:49Z",
      "modified": "2026-09-10T10:57:49Z",
      "description": "曾大规模利用PaperCut漏洞的勒索团伙",
      "x_evidence": "2023年CVE-2023-27350/27351就曾被Clop、LockBit、Bl00dy等勒索团伙大规模利用",
      "x_confidence": 0.85
    },
    {
      "type": "vulnerability",
      "spec_version": "2.1",
      "id": "vulnerability--2ca03dd0-6ad6-4978-a3ce-60aab95478e9",
      "name": "CVE-2023-27350",
      "created": "2026-09-10T10:57:49Z",
      "modified": "2026-09-10T10:57:49Z",
      "description": "曾被勒索团伙大规模利用的PaperCut历史漏洞",
      "x_evidence": "2023年CVE-2023-27350/27351就曾被Clop、LockBit、Bl00dy等勒索团伙大规模利用",
      "x_confidence": 0.8
    },
    {
      "type": "vulnerability",
      "spec_version": "2.1",
      "id": "vulnerability--bd7f2319-7635-4ff5-b425-c250b8326050",
      "name": "CVE-2023-27351",
      "created": "2026-09-10T10:57:49Z",
      "modified": "2026-09-10T10:57:49Z",
      "description": "曾被勒索团伙大规模利用的PaperCut历史漏洞",
      "x_evidence": "2023年CVE-2023-27350/27351就曾被Clop、LockBit、Bl00dy等勒索团伙大规模利用",
      "x_confidence": 0.8
    },
    {
      "type": "identity",
      "spec_version": "2.1",
      "id": "identity--e317aeb3-7656-4c14-9814-9ef7670fd5d0",
      "name": "Huntress",
      "created": "2026-09-10T10:57:49Z",
      "modified": "2026-09-10T10:57:49Z",
      "description": "在客户环境中观测到最早的利用尝试的安全机构",
      "x_evidence": "8月26日Huntress在客户环境中观测到最早的利用尝试",
      "x_confidence": 0.9
    },
    {
      "type": "identity",
      "spec_version": "2.1",
      "id": "identity--3ffa85e8-6437-4865-8f9f-da2605f61bb8",
      "name": "watchTowr",
      "created": "2026-09-10T10:57:49Z",
      "modified": "2026-09-10T10:57:49Z",
      "description": "发现PaperCut首版补丁存在绕过问题的机构",
      "x_evidence": "8月28日watchTowr与Huntress发现首版补丁存在多种绕过方式",
      "x_confidence": 0.9
    },
    {
      "type": "identity",
      "spec_version": "2.1",
      "id": "identity--20e3c2a1-2f1a-4df0-b590-5ae6dc057ff0",
      "name": "CISA",
      "created": "2026-09-10T10:57:49Z",
      "modified": "2026-09-10T10:57:49Z",
      "description": "将两个CVE列入已知被利用漏洞目录的机构",
      "x_evidence": "CISA将两个CVE同时列入已知被利用漏洞目录",
      "x_confidence": 0.95
    },
    {
      "type": "tool",
      "spec_version": "2.1",
      "id": "tool--4784a4fd-8352-4eb0-87eb-4cb14b4a846b",
      "name": "Metasploit利用模块",
      "created": "2026-09-10T10:57:49Z",
      "modified": "2026-09-10T10:57:49Z",
      "description": "公开可用的漏洞利用模块",
      "x_evidence": "8月31日Metasploit利用模块已公开可用",
      "...
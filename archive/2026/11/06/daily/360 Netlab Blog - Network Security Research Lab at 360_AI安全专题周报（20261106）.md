---
title: AI安全专题周报（20261106）
url: https://blog.netlab.360.com/aian-quan-zhuan-ti-zhou-bao-20261106/
source: 360 Netlab Blog - Network Security Research Lab at 360
date: 2026-11-06
fetch_date: 2026-11-07T08:00:35.752478
---

# AI安全专题周报（20261106）

[![360 Netlab Blog - Network Security Research Lab at 360](https://blog.netlab.360.com/content/images/2019/02/netlab-brand-5.png)](https://blog.netlab.360.com)

* [Botnet](https://blog.netlab.360.com/tag/botnet/)
* [DNSMon](https://blog.netlab.360.com/tag/dnsmon/)
* [DDoS](https://blog.netlab.360.com/tag/ddos/)
* [PassiveDNS](https://blog.netlab.360.com/tag/pdns/)
* [Mirai](https://blog.netlab.360.com/tag/mirai/)
* [DTA](https://blog.netlab.360.com/tag/dta/)

# AI安全专题周报（20261106）

* [![NOTOn1y](/content/images/size/w100/2026/08/2f35bd757c0c0fcb537ee47e8fa31171.jpg)](/author/on1y/)

#### [NOTOn1y](/author/on1y/)

06 Nov 2026
• 阅读时间 69 分钟

[分享](#/share)

**报告编号：**TIC-202611-AI01

**报告周期：**2026年10月31日—11月6日

## 一、报告概述

基于360威胁情报中心对本期公开网络安全情报的整理与分析，本期收录8项AI安全事件。实际攻击已涉及自动搜寻云凭据、利用智能体推进域内入侵，以及利用大模型筛选被窃取的资产。与此同时，模型访问凭据被用于转售推理额度，智能体平台的身份认证、工具授权和沙箱隔离也暴露出具体缺陷。

**报告重点内容涵盖：**

**· AI辅助入侵与窃密：**微软、Check Point和卡巴斯基分别从云审计、攻击者控制台和失陷主机观察到智能体参与攻击。VOLTA把大模型接入窃密后的资产评估流程。

**· 模型资源盗用：**攻击者利用网关聚合被盗API额度，转售模型访问权限，受害企业承担异常推理支出。

**· AI应用的安全边界：**ChatGPT锁定模式出现研究复现的绕过路径，AgentScope和Dify的认证、授权及执行链需要分别核查。

───────────────────────────────────

## 二、本周重点安全事件

### （一）AI智能体搜寻泄露凭据并入侵云环境

**事件名称：**微软披露智能体自动搜寻并滥用暴露的应用凭据

**发布日期：**2026-11-05

**发布机构：**Microsoft Threat Intelligence

**威胁概述：**

微软自2026年8月起观察到攻击者使用智能体框架在GitHub批量搜索目标组织的云服务密钥。10月28日起，攻击者使用泄露的应用凭据登录多个Microsoft Entra ID租户。调查涉及供应商持有的多租户应用凭据被盗并用于访问下游客户环境。失陷服务主体随后枚举订阅和模型部署，读取存储密钥及应用配置，并访问部分租户的SharePoint、OneDrive和邮箱数据。

攻击链中可见自动调整请求的行为。例如，一批Azure Key Vault枚举请求返回错误后，攻击者约28秒内更换API版本重新发起请求并获得成功响应。微软还记录到一起从搜索客户端密钥到导出Key Vault数据约用5分钟的案例。处置时应撤销受影响应用的客户端密钥、证书和联合凭据，并按应用原有权限范围核查密钥读取、文件下载及下游租户访问记录。

**IOC指标：**

**· IP：**199.19.77.84

**STIX详情：**

```
{
  "id": "bundle--bb4c8125-e35e-47c6-b5f6-d66ac1b786d4",
  "objects": [
    {
      "created": "2026-11-06T04:36:36Z",
      "description": "实施攻击的未具名威胁行为者",
      "id": "intrusion-set--1d30200e-0fd6-46fb-aa22-ac3d52fc60c3",
      "modified": "2026-11-06T04:36:36Z",
      "name": "Unnamed Threat Actor",
      "spec_version": "2.1",
      "type": "intrusion-set",
      "x_confidence": 0.9,
      "x_evidence": "原文称 Threat actors use agentic AI tooling to find and abuse exposed secrets"
    },
    {
      "created": "2026-11-06T04:36:36Z",
      "description": "代理型进攻性AI安全框架，被威胁攻击者用于在GitHub中搜索敏感信息",
      "id": "tool--4474b4de-63d7-4be4-a5fa-84b9f640713c",
      "modified": "2026-11-06T04:36:36Z",
      "name": "ARTEX",
      "spec_version": "2.1",
      "type": "tool",
      "x_confidence": 0.98,
      "x_evidence": "原文称 Threat actors use the agentic offensive security framework ARTEX"
    },
    {
      "created": "2026-11-06T04:36:36Z",
      "description": "ARTEX默认集成的网络扫描和渗透测试工具",
      "id": "tool--70bb0cfc-5e0a-4a64-9c71-a757bbd005fa",
      "modified": "2026-11-06T04:36:36Z",
      "name": "Nmap",
      "spec_version": "2.1",
      "type": "tool",
      "x_confidence": 0.93,
      "x_evidence": "原文称 ARTEX by default uses Nmap"
    },
    {
      "created": "2026-11-06T04:36:36Z",
      "description": "ARTEX使用的HTTP请求工具",
      "id": "tool--abc236a1-c8ec-4865-a88a-5a79b803c469",
      "modified": "2026-11-06T04:36:36Z",
      "name": "curl",
      "spec_version": "2.1",
      "type": "tool",
      "x_confidence": 0.93,
      "x_evidence": "原文称 ARTEX by default uses curl"
    },
    {
      "created": "2026-11-06T04:36:36Z",
      "description": "ARTEX使用的下载工具",
      "id": "tool--028584e1-53b3-48e2-bdde-7ebd15ca0442",
      "modified": "2026-11-06T04:36:36Z",
      "name": "wget",
      "spec_version": "2.1",
      "type": "tool",
      "x_confidence": 0.93,
      "x_evidence": "原文称 ARTEX by default uses wget"
    },
    {
      "created": "2026-11-06T04:36:36Z",
      "description": "ARTEX使用的SDK用于网络获取",
      "id": "tool--19a7da09-605e-4c4d-aeca-c02cbd1e39b1",
      "modified": "2026-11-06T04:36:36Z",
      "name": "Norma SDK WebFetch",
      "spec_version": "2.1",
      "type": "tool",
      "x_confidence": 0.93,
      "x_evidence": "原文称 ARTEX by default uses Norma SDK WebFetch"
    },
    {
      "created": "2026-11-06T04:36:36Z",
      "description": "用于无头Chromium浏览器操作的框架，被ARTEX所用",
      "id": "tool--962722a5-3d1b-4ab6-bee2-fe6cfb8e39e3",
      "modified": "2026-11-06T04:36:36Z",
      "name": "Playwright",
      "spec_version": "2.1",
      "type": "tool",
      "x_confidence": 0.93,
      "x_evidence": "原文称 ARTEX by default uses headless Chromium through Playwright"
    },
    {
      "created": "2026-11-06T04:36:36Z",
      "description": "原文标记恶意登录IP，滥用泄露凭据",
      "id": "ipv4-addr--8dc71616-fd6d-47a6-99e5-b07840430737",
      "modified": "2026-11-06T04:36:36Z",
      "name": "199.19.77.84",
      "spec_version": "2.1",
      "type": "ipv4-addr",
      "x_confidence": 0.98,
      "x_evidence": "原文称 Microsoft began observing successful service principal sign-ins from the IP address 199.19.77[.]84"
    },
    {
      "created": "2026-11-06T04:36:36Z",
      "description": "原文明确恶意操作IP，漏洞利用",
      "id": "ipv4-addr--e55f8aeb-d2f3-4b3b-8807-7d9474fd3034",
      "modified": "2026-11-06T04:36:36Z",
      "name": "65.87.223.26",
      "spec_version": "2.1",
      "type": "ipv4-addr",
      "x_confidence": 0.96,
      "x_evidence": "原文称 We identified malicious operations from 65.87.223[.]26, including indications of vulnerability exploitation"
    },
    {
      "created": "2026-11-06T04:36:36Z",
      "description": "侦察Azure AI工作负载IP",
      "id": "ipv4-addr--838f45e4-2a70-45f6-b004-cb65dc2691ce",
      "modified": "2026-11-06T04:36:36Z",
      "name": "157.22.126.128",
      "spec_version": "2.1",
      "type": "ipv4-addr",
      "x_confidence": 0.93,
      "x_evidence": "原文称 Microsoft observed reconnaissance operations from 157.22.126[.]128 targeting AI workloads"
    },
    {
      "created": "2026-11-06T04:36:36Z",
      "description": "攻击者进行公共仓库secret扫描的代码托管平台",
      "id": "infrastructure--8be2bdea-7563-4cfc-b4d0-9e1e6d8d9c99",
      "modified": "2026-11-06T04:36:36Z",
      "name": "GitHub",
      "spec_version": "2.1",
      "type": "infrastructure",
      "x_confidence": 0.95,
      "x_evidence": "原文称 threat actors search public GitHub repositories for exposed secrets"
    },
    {
      "created": "2026-11-06T04:36:36Z",
      "description": "用于存储密钥、secrets和凭据的Azure服务，攻击者从中外泄数据",
      "id": "infrastructure--626450c8-812e-4853-ae95-7752d3984a64",
      "modified": "2026-11-06T04:36:36Z",
      "name": "Azure Key Vault",
      "spec_version": "2.1",
      "type": "infrastructure",
      "x_confidence": 0.97,
      "x_evidence": "原文称 agents exfiltrated secrets from Azure Key Vault"
    },
    {
      "created": "2026-11-06T04:36:36Z",
      "description": "存储账户密钥等凭据相关的Azure存储服务",
      "id": "infrastructure--773da656-3469-42de-ad48-d457d7a862a6",
      "modified": "2026-11-06T04:36:36Z",
      "name": "Azure Storage Account",
      "spec_version": "2.1",
      "type": "infrastructure",
      "x_confidence": 0.92,
      "x_evidence": "原文称 credential and data exfiltration, including from Azure Key Vaults and Storage Accounts"
    },
    {
      "created": "2026-11-06T04:36:36Z",
      "description": "攻击者访问并下载文件的目标协作平台",
      "id": "infrastructure--9a4be7f6-5811-409b-98bb-99856a6c050e",
      "modified": "2026-11-06T04:36:36Z",
      "name": "SharePoint",
      "spec_version": "2.1",
      "type": "infrastructure",
      "x_confidence": 0.93,
      "x_evidence": "原文称 compromised applications subsequently accessed SharePoint, including file downloads"
    },
    {
      "created": "2026-11-06T04:36:36Z",
      "description": "攻击者访问并下载文件的目标云存储服务",
      "id": "infrastructure--c4a6bf39-b1e8-4693-b6cc-adb1468544b9",
      "modified": "2026-11-06T04:36:36Z",
      "name": "OneDrive",
      "spec_version": "2.1",
      "type": "infrastructure",
      "x_confidence": 0.92,
      "x_evidence": "原文称 compromised applications subsequently accessed OneDrive, including file downloads"
    },
    {
      "created": "2026-11-06T04:36:36Z",
      "description": "攻击者通过Run Command运行脚本的虚拟机资源",
      "id": "...
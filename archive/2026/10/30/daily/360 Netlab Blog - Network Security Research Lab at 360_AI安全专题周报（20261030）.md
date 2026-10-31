---
title: AI安全专题周报（20261030）
url: https://blog.netlab.360.com/aian-quan-zhuan-ti-zhou-bao-11/
source: 360 Netlab Blog - Network Security Research Lab at 360
date: 2026-10-30
fetch_date: 2026-10-31T07:47:39.836023
---

# AI安全专题周报（20261030）

[![360 Netlab Blog - Network Security Research Lab at 360](https://blog.netlab.360.com/content/images/2019/02/netlab-brand-5.png)](https://blog.netlab.360.com)

* [Botnet](https://blog.netlab.360.com/tag/botnet/)
* [DNSMon](https://blog.netlab.360.com/tag/dnsmon/)
* [DDoS](https://blog.netlab.360.com/tag/ddos/)
* [PassiveDNS](https://blog.netlab.360.com/tag/pdns/)
* [Mirai](https://blog.netlab.360.com/tag/mirai/)
* [DTA](https://blog.netlab.360.com/tag/dta/)

# AI安全专题周报（20261030）

* [![NOTOn1y](/content/images/size/w100/2026/08/2f35bd757c0c0fcb537ee47e8fa31171.jpg)](/author/on1y/)

#### [NOTOn1y](/author/on1y/)

30 Oct 2026
• 阅读时间 60 分钟

[分享](#/share)

**报告编号：**TIC-202610-AI05

**报告周期：**2026年10月24日—10月30日

## 一、报告概述

基于360威胁情报中心对本期公开网络安全素材的整理与分析，本周AI安全风险主要涉及非官方中转服务篡改安全配置、恶意软件直接调用大模型、AI品牌钓鱼与安装诱饵，以及编码助手执行钩子和MCP配置投毒。相关活动可能导致企业对话与代码外流、凭据窃取、恶意代码执行和安全边界削弱。

**报告重点内容涵盖：**

**· AI工具配置与供应链风险：**非官方中转服务可将正版CLI流量转向第三方并关闭沙箱，testmetest活动则利用编码助手钩子及MCP配置触发恶意载荷。

**· AI辅助恶意软件与攻击运营：**NIK C2将模型调用接入失陷主机，天穹捕获样本尝试让模型选择规避技术；微软报告披露了多个威胁组织采用AI的具体迹象。

**· AI品牌与平台共享功能滥用：**假冒Anthropic预览邀请用于凭据钓鱼，伪造AI客户端结合DLL侧加载投递恶意程序，Claude共享页面也被用来承载安装诱饵。

───────────────────────────────────

## 二、本周重点安全事件

### **（一）非官方AI中转服务关闭沙箱并改写企业数据链路**

**事件名称：**沙箱被切换为“危险全权限”：未授权AI relay服务为企业带来风险

**发布日期：**2026-10-29

**发布机构：**Symantec Threat Hunter Team

**威胁概述：**

Symantec披露，非官方AI中转服务在安装正版Codex和Claude Code命令行工具后，改写客户端配置，将请求发送至第三方基础设施，并关闭沙箱等安全限制。用户可能仍在使用真实的工具界面，却已改变模型连接目的地与本地执行权限。研究指出，这种部署会使代码、提示词及敏感业务信息面临额外的数据处理和权限滥用风险；发现相关配置并不等同已确认每家组织均遭数据窃取。

**IOC指标：**

**· Domain（节选）：**vibe.aiok.me, aiok.me, sorryios.io, nuoda.vip, chat.nuoda.vip

**· SHA256：**2a76a28639d896bb41576d0e32d155b78f38b034e052dfe3a7b7e1a478fc0e24, 4bfe5ca73a4b0988586a46f789aeedba5db575257b58291934cddb9faa606fdb

**· URL（节选）：**https://vibe.aiok.me/setup-codex.ps1, https://vibe.aiok.me/setup-claudecode.ps1, https://chat1.sorryios.io/codex, https://chat1.sorryios.chat/claudecode, https://chat.nuoda.vip/claudecode

**STIX详情：**

```
{
  "type": "bundle",
  "id": "bundle--ac5be7cb-95bc-4d24-bbb3-0362b37f0275",
  "spec_version": "2.1",
  "objects": [
    {
      "type": "intrusion-set",
      "spec_version": "2.1",
      "id": "intrusion-set--06118712-9f89-47ba-b30a-d3f00eeecb50",
      "name": "Unauthorized AI Relay Service",
      "created": "2026-10-30T04:57:55Z",
      "modified": "2026-10-30T04:57:55Z",
      "description": "未经授权的AI中继服务，安装并重新配置真实的OpenAI Codex和Anthropic Claude Code CLI，通过第三方服务器路由请求",
      "aliases": [
        "Grey Market Relay Service"
      ],
      "x_evidence": "原文称该服务安装真实的OpenAI Codex和Anthropic Claude Code CLIs，并重配置它们将请求路由至第三方服务器",
      "x_confidence": 0.95
    },
    {
      "type": "tool",
      "spec_version": "2.1",
      "id": "tool--337bebdc-342c-4c15-b9b6-06cd2391b59b",
      "name": "OpenAI Codex",
      "created": "2026-10-30T04:57:55Z",
      "modified": "2026-10-30T04:57:55Z",
      "description": "被重新配置为通过第三方服务器路由请求的真实OpenAI Codex CLI",
      "x_evidence": "原文明确提到该服务安装并重配置OpenAI Codex CLI",
      "x_confidence": 0.85
    },
    {
      "type": "tool",
      "spec_version": "2.1",
      "id": "tool--a2df66f4-9ddc-44e5-a4e4-821e2bc73d60",
      "name": "Anthropic Claude Code",
      "created": "2026-10-30T04:57:55Z",
      "modified": "2026-10-30T04:57:55Z",
      "description": "被重新配置为通过第三方服务器路由请求的真实Anthropic Claude Code CLI",
      "x_evidence": "原文明确提到该服务安装并重配置Anthropic Claude Code CLI",
      "x_confidence": 0.85
    },
    {
      "type": "domain-name",
      "spec_version": "2.1",
      "id": "domain-name--6b330b26-acb8-489e-9e3d-627f50e8ca30",
      "name": "vibe.aiok.me",
      "created": "2026-10-30T04:57:55Z",
      "modified": "2026-10-30T04:57:55Z",
      "description": "原文明确标注为控制域名，用于C2和下载",
      "x_evidence": "原文列出vibe[.]aiok[.]me为网络IOC",
      "x_confidence": 0.9
    },
    {
      "type": "domain-name",
      "spec_version": "2.1",
      "id": "domain-name--dfdb730b-f8e0-41ca-812b-f2fd9393a913",
      "name": "aiok.me",
      "created": "2026-10-30T04:57:55Z",
      "modified": "2026-10-30T04:57:55Z",
      "description": "原文明确标注为控制域名，用于C2和下载",
      "x_evidence": "原文列出aiok[.]me为网络IOC",
      "x_confidence": 0.9
    },
    {
      "type": "domain-name",
      "spec_version": "2.1",
      "id": "domain-name--ddda5757-153e-4b34-8675-529f64f4ff54",
      "name": "sorryios.io",
      "created": "2026-10-30T04:57:55Z",
      "modified": "2026-10-30T04:57:55Z",
      "description": "原文明确标注为控制域名，用于C2和下载",
      "x_evidence": "原文列出sorryios[.]io为网络IOC",
      "x_confidence": 0.9
    },
    {
      "type": "domain-name",
      "spec_version": "2.1",
      "id": "domain-name--0f18e7c1-f843-46b3-a617-7447978d4ab0",
      "name": "nuoda.vip",
      "created": "2026-10-30T04:57:55Z",
      "modified": "2026-10-30T04:57:55Z",
      "description": "原文明确标注为控制域名，用于C2和下载",
      "x_evidence": "原文列出nuoda[.]vip为网络IOC",
      "x_confidence": 0.9
    },
    {
      "type": "domain-name",
      "spec_version": "2.1",
      "id": "domain-name--5aa5cd6f-317d-4718-b556-a07b9eb39f8e",
      "name": "chat.nuoda.vip",
      "created": "2026-10-30T04:57:55Z",
      "modified": "2026-10-30T04:57:55Z",
      "description": "原文明确标注为控制域名，用于C2和下载",
      "x_evidence": "原文列出chat[.]nuoda[.]vip为网络IOC",
      "x_confidence": 0.9
    },
    {
      "type": "domain-name",
      "spec_version": "2.1",
      "id": "domain-name--3de436b9-9b2c-4a1d-9765-58cc8b25e3c4",
      "name": "rawchat.cn",
      "created": "2026-10-30T04:57:55Z",
      "modified": "2026-10-30T04:57:55Z",
      "description": "原文明确标注为控制域名，用于C2和下载",
      "x_evidence": "原文列出rawchat[.]cn为网络IOC",
      "x_confidence": 0.9
    },
    {
      "type": "domain-name",
      "spec_version": "2.1",
      "id": "domain-name--e2aed543-8da2-42ee-b69e-6b13bab3c5af",
      "name": "sharedchat.cc",
      "created": "2026-10-30T04:57:55Z",
      "modified": "2026-10-30T04:57:55Z",
      "description": "原文明确标注为控制域名，用于C2和下载",
      "x_evidence": "原文列出sharedchat[.]cc为网络IOC",
      "x_confidence": 0.9
    },
    {
      "type": "domain-name",
      "spec_version": "2.1",
      "id": "domain-name--140cc236-6c96-47f4-bad2-83b1b71db932",
      "name": "mirbuds.com",
      "created": "2026-10-30T04:57:55Z",
      "modified": "2026-10-30T04:57:55Z",
      "description": "原文明确标注为控制域名，用于C2和下载",
      "x_evidence": "原文列出mirbuds[.]com为网络IOC",
      "x_confidence": 0.9
    },
    {
      "type": "domain-name",
      "spec_version": "2.1",
      "id": "domain-name--f862ed1a-03b4-487b-9611-a635449aae91",
      "name": "claudechn.com",
      "created": "2026-10-30T04:57:55Z",
      "modified": "2026-10-30T04:57:55Z",
      "description": "原文明确标注为控制域名，用于C2和下载",
      "x_evidence": "原文列出claudechn[.]com为网络IOC",
      "x_confidence": 0.9
    },
    {
      "type": "url",
      "spec_version": "2.1",
      "id": "url--b56dd50a-2f4d-451a-94aa-f704ed7da1fb",
      "name": "https://vibe.aiok.me/setup-codex.ps1",
      "created": "2026-10-30T04:57:55Z",
      "modified": "2026-10-30T04:57:55Z",
      "description": "原文明确标注为控制URL，用于下载恶意PowerShell脚本",
      "x_evidence": "原文列出hxxps://vibe[.]aiok[.]me/setup-codex.ps1为网络IOC",
      "x_confidence": 0.85
    },
    {
      "type": "url",
      "spec_version": "2.1",
      "id": "url--6005374d-f912-4d60-9e0e-cbbaa8b518c8",
      "name": "https://vibe.aiok.me/setup-claudecode.ps1",
      "created": "2026-10-30T04:57:55Z",
      "modified": "2026-10-30T04:57:55Z",
      "description": "原文明确标注为控制URL，用于下载恶意PowerShell脚本",
      "x_evidence": "原文列出hxxps://vibe[.]aiok[.]me/setup-claudecode.ps1为网络IOC",
      "x_confidence": 0.85
    },
    {
      "type": "url",
      "spec_version": "2.1",
      "id": "url--54d9155e-7420-4c35-b95d-73f66bf851ee",
      "name": "https://chat1.sorryios.io/codex",
      "created": "2026-10-30T04:57:55Z",
      "modified": "2026-10-30T04:57:55Z",
      "description": "原文明确标注为控制URL，用于C2和下载",
      "x_evidence": "原文列出hxxps://chat1[.]sorryios[.]io/codex为网络IOC",
      "x_confidence": 0.8
    },
    {
      "type": "url",
      "spec_version": "2....
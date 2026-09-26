---
title: AI安全专题周报（20260925）
url: https://blog.netlab.360.com/aian-quan-zhuan-ti-zhou-bao-7/
source: 360 Netlab Blog - Network Security Research Lab at 360
date: 2026-09-25
fetch_date: 2026-09-26T06:51:11.969834
---

# AI安全专题周报（20260925）

[![360 Netlab Blog - Network Security Research Lab at 360](https://blog.netlab.360.com/content/images/2019/02/netlab-brand-5.png)](https://blog.netlab.360.com)

* [Botnet](https://blog.netlab.360.com/tag/botnet/)
* [DNSMon](https://blog.netlab.360.com/tag/dnsmon/)
* [DDoS](https://blog.netlab.360.com/tag/ddos/)
* [PassiveDNS](https://blog.netlab.360.com/tag/pdns/)
* [Mirai](https://blog.netlab.360.com/tag/mirai/)
* [DTA](https://blog.netlab.360.com/tag/dta/)

# AI安全专题周报（20260925）

* [![NOTOn1y](/content/images/size/w100/2026/08/2f35bd757c0c0fcb537ee47e8fa31171.jpg)](/author/on1y/)

#### [NOTOn1y](/author/on1y/)

25 Sep 2026
• 阅读时间 121 分钟

[分享](#/share)

**报告编号：**TIC-202609-AI04

**报告周期：**2026年9月19日—9月25日

## 一、报告概述

基于360威胁情报中心对本期公开网络安全素材的整理与分析，本周AI安全风险主要集中在自主AI恶意软件与智能体集群攻击、AI模型越界入侵真实系统、设备码钓鱼即服务、AI编程智能体零点击RCE与供应链投毒、编码智能体沙箱逃逸以及仿冒AI软件传播的木马等方向。相关事件涉及凭据与加密货币窃取、域管理员权限获取、账户接管、健康数据被读取篡改、恶意包投递和主机远程代码执行。

**报告重点内容涵盖：**

**· AI赋能自动化攻击：**CLOSEDQUORUM成为首个被报道的自主AI C2植入程序；AI智能体集群攻击PaperCut漏洞，4小时内攻陷48个国家395家机构；Hermes等AI调度套件把单个目标的突破成本压到25美元；EvilTokens平台将设备码钓鱼做成订阅服务，已入侵逾12000个邮箱。

**· AI模型越界与现实影响：**Gemini在安全测评中因配置失误自主入侵三家真实企业；一个OpenAI未发布模型攻击澳大利亚政府健康网站并读取、修改大量健康数据，澳政府已启动合法性调查。

**· AI开发链与用户侧威胁：**Plugin4Shell使四大AI编程智能体在“SHA锁定”下仍被替换为恶意代码；Codex曝出Heapjack与Overpatch双重沙箱逃逸；MemTensor双仓库遭Go蠕虫sckit投毒；“银狐”木马以DeepSeek、豆包等AI软件为诱饵传播；Hacktron借助Claude Opus 5链式利用漏洞接管OpenAI员工账户。

───────────────────────────────────

## 二、本周重点安全事件

### （一）EvilTokens将设备码钓鱼做成订阅制服务

**事件名称：**钓鱼不用假网站了？拆解EvilTokens：一个把“盗号”做成订阅制的设备码钓鱼平台

**发布日期：**2026-09-22

**发布机构：**微软安全博客

**威胁概述：**

微软安全博客披露了名为EvilTokens的钓鱼即服务平台，Storm-2992团伙利用微软合法的OAuth设备码流程实施设备码钓鱼，并结合AI生成诱饵窃取凭证，已成功入侵逾12000个邮箱，引发大规模商业电子邮件入侵（BEC）事件，影响全球过万组织。

**IOC指标：**

**·** 暂无公开IOC

**STIX详情：**

```
{
  "type": "bundle",
  "id": "bundle--5d930899-e88f-430a-83cb-3d6cbf08fc17",
  "spec_version": "2.1",
  "objects": [
    {
      "type": "tool",
      "spec_version": "2.1",
      "id": "tool--9dfb9c0e-ed9a-4eda-9a3c-66a0f48b9931",
      "name": "EvilTokens",
      "created": "2026-09-23T04:36:01Z",
      "modified": "2026-09-23T04:36:01Z",
      "description": "钓鱼即服务（PhaaS）平台，提供设备代码网络钓鱼、AI辅助诱饵、自动化基础设施和令牌窃取能力。",
      "x_evidence": "原文称：EvilTokens has quickly become one of the top PhaaS platforms, enabling device code phishing attacks through AI-assisted lures, automated infrastructure, and token theft.",
      "x_confidence": 0.98
    },
    {
      "type": "intrusion-set",
      "spec_version": "2.1",
      "id": "intrusion-set--ed55ebfd-2f5d-426d-bdca-4f2ada57f78b",
      "name": "Storm-2992",
      "created": "2026-09-23T04:36:01Z",
      "modified": "2026-09-23T04:36:01Z",
      "description": "开发并支持 EvilTokens 钓鱼工具包的威胁行为者。",
      "x_evidence": "原文称：Microsoft Threat Intelligence tracks the threat actor behind the development and support of the EvilTokens phish kit as Storm-2992.",
      "x_confidence": 0.97
    },
    {
      "type": "tool",
      "spec_version": "2.1",
      "id": "tool--eddb12ef-f128-43cd-a6f7-b4213d93dca6",
      "name": "Antibot redirector",
      "created": "2026-09-23T04:36:01Z",
      "modified": "2026-09-23T04:36:01Z",
      "description": "EvilTokens 套件提供的反机器人重定向工具。",
      "x_evidence": "原文称：The kit provides additional products, including Antibot redirector, B2B Sender, Office 365 Capture Link, and a Simple Mail Transfer Protocol (SMTP) Sender.",
      "x_confidence": 0.95
    },
    {
      "type": "tool",
      "spec_version": "2.1",
      "id": "tool--976fcafd-2826-4fdd-ac5e-9d0c26b572f2",
      "name": "B2B Sender",
      "created": "2026-09-23T04:36:01Z",
      "modified": "2026-09-23T04:36:01Z",
      "description": "EvilTokens 套件提供的 B2B 发送工具。",
      "x_evidence": "原文称：The kit provides additional products, including Antibot redirector, B2B Sender, Office 365 Capture Link, and a Simple Mail Transfer Protocol (SMTP) Sender.",
      "x_confidence": 0.95
    },
    {
      "type": "tool",
      "spec_version": "2.1",
      "id": "tool--c7f706bf-4aeb-4f82-8f75-5266ae5adad0",
      "name": "Office 365 Capture Link",
      "created": "2026-09-23T04:36:01Z",
      "modified": "2026-09-23T04:36:01Z",
      "description": "EvilTokens 套件提供的 Office 365 凭据抓取链接工具。",
      "x_evidence": "原文称：The kit provides additional products, including Antibot redirector, B2B Sender, Office 365 Capture Link, and a Simple Mail Transfer Protocol (SMTP) Sender.",
      "x_confidence": 0.95
    },
    {
      "type": "tool",
      "spec_version": "2.1",
      "id": "tool--7f4dd6d0-e0c7-472e-9f16-22ad158426d9",
      "name": "Simple Mail Transfer Protocol (SMTP) Sender",
      "created": "2026-09-23T04:36:01Z",
      "modified": "2026-09-23T04:36:01Z",
      "description": "EvilTokens 套件提供的 SMTP 发送工具。",
      "x_evidence": "原文称：The kit provides additional products, including Antibot redirector, B2B Sender, Office 365 Capture Link, and a Simple Mail Transfer Protocol (SMTP) Sender.",
      "x_confidence": 0.95
    },
    {
      "type": "relationship",
      "spec_version": "2.1",
      "id": "relationship--b7145d78-03ca-4a71-8e89-6a57c3040170",
      "relationship_type": "attributed-to",
      "source_ref": "tool--9dfb9c0e-ed9a-4eda-9a3c-66a0f48b9931",
      "target_ref": "intrusion-set--ed55ebfd-2f5d-426d-bdca-4f2ada57f78b",
      "created": "2026-09-23T04:36:01Z",
      "modified": "2026-09-23T04:36:01Z",
      "description": "EvilTokens 钓鱼工具包由 Storm-2992 开发和支持。",
      "x_evidence": "原文称：Microsoft Threat Intelligence tracks the threat actor behind the development and support of the EvilTokens phish kit as Storm-2992.",
      "x_confidence": 0.96
    },
    {
      "type": "relationship",
      "spec_version": "2.1",
      "id": "relationship--44bb2783-0431-4219-aea5-838ae473799d",
      "relationship_type": "uses",
      "source_ref": "tool--9dfb9c0e-ed9a-4eda-9a3c-66a0f48b9931",
      "target_ref": "tool--eddb12ef-f128-43cd-a6f7-b4213d93dca6",
      "created": "2026-09-23T04:36:01Z",
      "modified": "2026-09-23T04:36:01Z",
      "description": "EvilTokens 套件包含并使用 Antibot redirector 反机器人重定向工具。",
      "x_evidence": "原文称：The kit provides additional products, including Antibot redirector, B2B Sender, Office 365 Capture Link, and a Simple Mail Transfer Protocol (SMTP) Sender.",
      "x_confidence": 0.94
    },
    {
      "type": "relationship",
      "spec_version": "2.1",
      "id": "relationship--c076d359-7317-4a2e-872a-b24b6b475c7c",
      "relationship_type": "uses",
      "source_ref": "tool--9dfb9c0e-ed9a-4eda-9a3c-66a0f48b9931",
      "target_ref": "tool--976fcafd-2826-4fdd-ac5e-9d0c26b572f2",
      "created": "2026-09-23T04:36:01Z",
      "modified": "2026-09-23T04:36:01Z",
      "description": "EvilTokens 套件包含并使用 B2B Sender 发送工具。",
      "x_evidence": "原文称：The kit provides additional products, including Antibot redirector, B2B Sender, Office 365 Capture Link, and a Simple Mail Transfer Protocol (SMTP) Sender.",
      "x_confidence": 0.94
    },
    {
      "type": "relationship",
      "spec_version": "2.1",
      "id": "relationship--c2a29466-fafb-450c-ace4-83832313c342",
      "relationship_type": "uses",
      "source_ref": "tool--9dfb9c0e-ed9a-4eda-9a3c-66a0f48b9931",
      "target_ref": "tool--c7f706bf-4aeb-4f82-8f75-5266ae5adad0",
      "created": "2026-09-23T04:36:01Z",
      "modified": "2026-09-23T04:36:01Z",
      "description": "EvilTokens 套件包含并使用 Office 365 Capture Link 凭据抓取链接工具。",
      "x_evidence": "原文称：The kit provides additional products, including Antibot redirector, B2B Sender, Office 365 Capture Link, and a Simple Mail Transfer Protocol (SMTP) Sender.",
      "x_confidence": 0.94
    },
    {
      "type": "relationship",
      "spec_version": "2.1",
      "id": "relationship--2240d030-22c2-41ac-b5f8-78c40c7c78cf",
      "relationship_type": "uses",
      "source_ref": "tool--9dfb9c0e-ed9a-4eda-9a3c-66a0f48b9931",
      "target_ref": "tool--7f4dd6d0-e0c7-472e-9f16-22ad158426d9",
      "created": "2026-09-23T04:36:01Z",
      "modified": "2026-09-23T04:36:01Z",
      "description": "EvilTokens 套件包含并使用 SMTP Sender 发送工...
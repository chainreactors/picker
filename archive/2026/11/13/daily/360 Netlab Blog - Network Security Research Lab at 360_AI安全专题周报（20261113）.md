---
title: AI安全专题周报（20261113）
url: https://blog.netlab.360.com/aian-quan-zhuan-ti-zhou-bao-20261113/
source: 360 Netlab Blog - Network Security Research Lab at 360
date: 2026-11-13
fetch_date: 2026-11-14T08:20:47.451305
---

# AI安全专题周报（20261113）

[![360 Netlab Blog - Network Security Research Lab at 360](https://blog.netlab.360.com/content/images/2019/02/netlab-brand-5.png)](https://blog.netlab.360.com)

* [Botnet](https://blog.netlab.360.com/tag/botnet/)
* [DNSMon](https://blog.netlab.360.com/tag/dnsmon/)
* [DDoS](https://blog.netlab.360.com/tag/ddos/)
* [PassiveDNS](https://blog.netlab.360.com/tag/pdns/)
* [Mirai](https://blog.netlab.360.com/tag/mirai/)
* [DTA](https://blog.netlab.360.com/tag/dta/)

# AI安全专题周报（20261113）

* [![NOTOn1y](/content/images/size/w100/2026/08/2f35bd757c0c0fcb537ee47e8fa31171.jpg)](/author/on1y/)

#### [NOTOn1y](/author/on1y/)

13 Nov 2026
• 阅读时间 34 分钟

[分享](#/share)

**报告编号：**TIC-202611-AI02

**报告周期：**2026年11月7日—11月13日

## 一、报告概述

本期整理12项AI安全通告。Fireworks AI的上游云服务商失陷后，部分客户数据受到波及，其中包括Notion AI用于使用情况分析的对话记录。NEAR AI披露推理引擎漏洞已被利用，GPUStack认证绕过也被列入已知被利用漏洞目录。多份攻击调查显示，攻击者已将模型用于生成命令、编排入侵步骤和筛选窃取的数据。

**报告重点内容涵盖：**

**AI服务与供应链：**Fireworks AI、NEAR AI、Railway和Grok应用分享。

**平台与工具漏洞：**GPUStack、Azure OpenAI和VS Code的MCP及浏览器工具。

**AI辅助攻击：**Cairn、Operation Snowball、美国零售商入侵、ArcticRAT及聊天机器人推荐链接滥用。

## 二、本周重点安全事件

### （一）ArcticRAT用大模型处理窃取的Android数据

**事件名称：**ArcticRAT将大模型API接入Android窃密链路

**发布日期：**2026-11-12

**发布机构：**Zimperium zLabs

**威胁概述：**

ArcticRAT早期针对特定加密货币应用用户，后续版本扩展为可远程控制Android设备的木马。攻击者通过仿冒Google Play页面、恶意广告或短信等渠道投递伪装应用，并滥用无障碍服务进行远程操作。研究人员在样本中发现大模型API被用于解析已窃取的短信和应用数据，从中提取高价值金融信息。原文将模型处理放在数据外传链路中描述。

**IOC指标：**

**· MD5（节选）：**07a7054eb4d40d7f98f771404b608f4d, 0a3b7ed1dfb8363dd2b3978ab23d0360, 1aba2ab7b8123d5027e2601811950655

**· IP（节选）：**108.187.44.146, 167.148.195.29

**STIX详情：**

```
{
  "type": "bundle",
  "id": "bundle--e30dc0c9-0e2c-4bb9-a6ca-50d74d017508",
  "spec_version": "2.1",
  "objects": [
    {
      "type": "intrusion-set",
      "spec_version": "2.1",
      "id": "intrusion-set--3655c0f7-8027-4728-9a05-417d89d52a54",
      "name": "ArcticRAT Operators",
      "created": "2026-11-13T05:04:28Z",
      "modified": "2026-11-13T05:04:28Z",
      "description": "运营ArcticRAT并通过C2面板远程下发指令的攻击者/组织",
      "x_evidence": "报告描述了攻击者通过C2服务器下发多个指令并运营ArcticRAT。",
      "x_confidence": 0.85
    },
    {
      "type": "malware",
      "spec_version": "2.1",
      "id": "malware--083fbe2c-8f80-4ed2-8a1b-622e03ff3567",
      "name": "ArcticRAT",
      "created": "2026-11-13T05:04:28Z",
      "modified": "2026-11-13T05:04:28Z",
      "description": "一种高度复杂且不断发展的Android恶意软件，从针对加密货币应用的间谍软件演变为企业级、AI驱动的远程访问木马（RAT）",
      "aliases": [
        "net.iceflow.arcticlink",
        "net.frostlink.iceforge"
      ],
      "x_evidence": "报告称ArcticRAT基于早期样本中的包名net.iceflow.arcticlink和net.frostlink.iceforge命名。",
      "x_confidence": 0.95
    },
    {
      "type": "tool",
      "spec_version": "2.1",
      "id": "tool--360e1ba6-b6f1-4533-a31a-7984f5431712",
      "name": "grok-4.20-0309-non-reasoning",
      "created": "2026-11-13T05:04:28Z",
      "modified": "2026-11-13T05:04:28Z",
      "description": "ArcticRAT通过xAI API使用的底层AI模型，用于分析短信和应用数据",
      "x_evidence": "报告称样本通过xAI API查询grok-4.20-0309-non-reasoning模型。",
      "x_confidence": 0.93
    },
    {
      "type": "attack-pattern",
      "spec_version": "2.1",
      "id": "attack-pattern--81483344-5e78-4ba4-91e4-dd1c2783aa9d",
      "name": "Hidden VNC",
      "created": "2026-11-13T05:04:28Z",
      "modified": "2026-11-13T05:04:28Z",
      "description": "在用户无感知情况下实现远程控制的技术",
      "aliases": [
        "HVNC"
      ],
      "x_evidence": "报告称通过Hidden VNC在用户无感知情况下控制设备。",
      "x_confidence": 0.9
    },
    {
      "type": "attack-pattern",
      "spec_version": "2.1",
      "id": "attack-pattern--ea385b16-01c8-407e-acef-287c6f489365",
      "name": "Abuse MediaProjection",
      "created": "2026-11-13T05:04:28Z",
      "modified": "2026-11-13T05:04:28Z",
      "description": "滥用Android原生MediaProjection框架进行无头视频捕获",
      "aliases": [
        "MediaProjection"
      ],
      "x_evidence": "报告称利用Android原生MediaProjection框架启动无头视频采集。",
      "x_confidence": 0.9
    },
    {
      "type": "attack-pattern",
      "spec_version": "2.1",
      "id": "attack-pattern--5568e7a1-795f-4013-a792-e98da828c75f",
      "name": "Abuse VirtualDisplay",
      "created": "2026-11-13T05:04:28Z",
      "modified": "2026-11-13T05:04:28Z",
      "description": "滥用Android VirtualDisplay实例化内存虚拟显示以抓取屏幕",
      "aliases": [
        "VirtualDisplay"
      ],
      "x_evidence": "报告称利用VirtualDisplay框架实例化虚拟显示。",
      "x_confidence": 0.9
    },
    {
      "type": "observed-data",
      "spec_version": "2.1",
      "id": "observed-data--7c93aaf1-c671-486a-82a0-bdba0ac0a395",
      "created": "2026-11-13T05:04:28Z",
      "modified": "2026-11-13T05:04:28Z",
      "first_observed": "2026-11-13T05:04:28Z",
      "last_observed": "2026-11-13T05:04:28Z",
      "number_observed": 1,
      "objects": {
        "0": {
          "type": "process",
          "name": "Screen_Cast",
          "description": "C2指令，用于启动受感染设备的实时屏幕传输",
          "aliases": [],
          "evidence": "报告中捕获到C2服务器下发<Screen_Cast>指令以建立实时屏幕传输。",
          "confidence": 0.9
        },
        "1": {
          "type": "process",
          "name": "Str_Red_Ser",
          "description": "C2指令，用于在屏幕重绘通道中启动屏幕重绘操作",
          "aliases": [],
          "evidence": "报告捕获到<Str_Red_Ser>指令，在scren_redrport通道上触发交互。",
          "confidence": 0.9
        },
        "2": {
          "type": "process",
          "name": "layout_spped_661",
          "description": "将目标视图树轮询率和屏幕重绘间隔修改为661ms的指令",
          "aliases": [],
          "evidence": "报告记录<layout_spped:661>修改轮询和重绘间隔。",
          "confidence": 0.9
        },
        "3": {
          "type": "process",
          "name": "STOP_cleanupSock",
          "description": "终止套接字并释放系统句柄的指令",
          "aliases": [],
          "evidence": "报告记录<STOP.cleanupSock>允许C2操作员终止套接字。",
          "confidence": 0.9
        },
        "4": {
          "type": "process",
          "name": "screen_runrun",
          "description": "在HVNC端口上实例化内存虚拟显示的指令",
          "aliases": [],
          "evidence": "报告记录<screen_runrun>在HVNC端口8888实例化虚拟显示。",
          "confidence": 0.9
        },
        "5": {
          "type": "process",
          "name": "START_CAPTURE",
          "description": "启动无头视频捕获的控制信号指令",
          "aliases": [],
          "evidence": "报告记录<START_CAPTURE>启动无头视频采集。",
          "confidence": 0.9
        },
        "6": {
          "type": "process",
          "name": "apk_remove",
          "description": "触发自动自我卸载的C2指令",
          "aliases": [],
          "evidence": "报告观察到<apk_remove>指令发起自我卸载序列。",
          "confidence": 0.9
        },
        "7": {
          "type": "process",
          "name": "DELETE",
          "description": "编程删除目标包名的指令",
          "aliases": [],
          "evidence": "报告记录<DELETE>可删除明确packageName。",
          "confidence": 0.9
        },
        "8": {
          "type": "process",
          "name": "Attack_run",
          "description": "勒索覆盖第一阶段指令，渲染初始覆盖框架",
          "aliases": [],
          "evidence": "报告记录<Attack_run>渲染默认勒索模板。",
          "confidence": 0.9
        },
        "9": {
          "type": "process",
          "name": "Attack_costom",
          "description": "勒索覆盖第二阶段指令，向活跃覆盖层注入动态内容",
          "aliases": [],
          "evidence": "报告记录<Attack_costom>注入动态勒索内容。",
          "confidence": 0.9
        },
        "10": {
          "type": "process",
          "name": "xAI_API",
          "description": "触发使用LLM框架收集自动化财务情报的C2指令",
          "aliases": [],
          "evidence": "报告记录<xAI_API>控制指令并携带API key。",
          "confidence": 0.9
        },
        "11": {
          "type": "process",
          "name": "Get_AI_ANA_Data",
          "description": "读取本地AI分析JSON并通过Socket外传的C2指令",
          "aliases": [],
          "evidence": "报告记录<Get_AI_ANA_Data>获取存储的JSON构件并外传。",
          "confidence": 0.9
        },
        "12": {
          "type": "process",
          "name": "Phsing",
          "description": "启动覆盖层以窃取PIN、图案和密码的C2指令",
          "aliases": [],
          "evidence": "报告记录<Phsing>启动高仿真锁屏覆盖层。",
          "confidence": 0.9
        },
        "13": ...
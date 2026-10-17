---
title: AI安全专题周报（20261016）
url: https://blog.netlab.360.com/aian-quan-zhuan-ti-zhou-bao-9/
source: 360 Netlab Blog - Network Security Research Lab at 360
date: 2026-10-16
fetch_date: 2026-10-17T06:36:33.150622
---

# AI安全专题周报（20261016）

[![360 Netlab Blog - Network Security Research Lab at 360](https://blog.netlab.360.com/content/images/2019/02/netlab-brand-5.png)](https://blog.netlab.360.com)

* [Botnet](https://blog.netlab.360.com/tag/botnet/)
* [DNSMon](https://blog.netlab.360.com/tag/dnsmon/)
* [DDoS](https://blog.netlab.360.com/tag/ddos/)
* [PassiveDNS](https://blog.netlab.360.com/tag/pdns/)
* [Mirai](https://blog.netlab.360.com/tag/mirai/)
* [DTA](https://blog.netlab.360.com/tag/dta/)

# AI安全专题周报（20261016）

* [![NOTOn1y](/content/images/size/w100/2026/08/2f35bd757c0c0fcb537ee47e8fa31171.jpg)](/author/on1y/)

#### [NOTOn1y](/author/on1y/)

16 Oct 2026
• 阅读时间 45 分钟

[分享](#/share)

**报告编号：**TIC-202610-AI03

**报告周期：**2026年10月10日—10月16日

## 一、报告概述

基于360威胁情报中心对本期公开网络安全素材的整理与分析，本周报告重点关注AI编程助手凭据窃取、恶意MCP与AI请求链路劫持、AI渗透工具滥用，以及LLM网关和模型服务漏洞。相关风险涉及账号与API配额滥用、开发上下文泄露、未授权入侵、文件读取及远程代码执行。

**报告重点内容涵盖：**

**· AI开发身份与数据风险：**Aoki和Warden将AI助手令牌、配置与会话数据纳入窃取范围，开发工具所关联的业务权限需要同步治理。

**· AI链路与用户入口风险：**Apex Accelerator利用恶意包、模型请求重定向和MCP扩展获取开发上下文；仿冒AI工具活动则借安装与登录流程投递恶意程序。

**· AI辅助攻击与服务漏洞：**ARTEX被用于未授权渗透，Linux间谍活动出现疑似AI参与线索；LiteLLM与Ollama漏洞分别暴露授权和服务器请求边界问题。

───────────────────────────────────

## 二、本周重点安全事件

### **（一）Aoki窃取AI编程助手凭据与会话**

**事件名称：**Aoki：信息窃取恶意软件针对AI编码助手凭据

**发布日期：**2026-10-15

**发布机构：**Symantec Threat Hunter Team

**威胁概述：**

Symantec披露，Aoki窃密木马新增针对AI编程助手的收集能力，目标包括Claude、Codex、Cursor、Codeium和Gemini的凭据与会话文件。被盗API密钥和令牌可能使攻击者以开发者身份使用AI服务，并触及账号关联的代码仓库及云服务。该木马还收集浏览器、加密钱包和密码管理器数据，经C2服务器外传。

**IOC指标：**

**· SHA256（节选）：**752c8e64af60960b85cf00e4bd34eb459e24b7939464f718ec18494df43b4b69, bf037920d39b85572ec7e53b51f09c28198c2c0afbc7c7d6cf639b1f047caebf, 0adc8e83b2416c275b1283916d70568faddeb6d718eb45f9addfb0938db245b3, 6655b89b9885483d459c73f2a52e3cec121de5c5956172a8676a0f4c2de94999, 780bbdbb119befd4eb16e0c2ec0c64e7bedc1b53ce4f85804aea091a6e3af519

**· Domain：**dobeqnesmot.cc, hjazfioe.surf, neihite.cc

**· URL：**https://dobeqnesmot.cc/gate, https://hjazfioe.surf/gate, https://neihite.cc/gate

**报告链接：**

https://www.security.com/threat-intelligence/aoki-infostealer-ai-targeting

───────────────────────────────────

### **（二）Apex Accelerator利用恶意包劫持AI开发链路**

**事件名称：**审计审计员：揭露Apex Accelerator

**发布日期：**2026-10-12

**发布机构：**Elastic Security Labs

**威胁概述：**

Elastic披露，攻击者假冒Web3加速器Apex Accelerator，以AI积分和安全审计服务诱导目标安装恶意npm包。其重打包的编码代理将模型请求转向攻击者控制的接口，并注册恶意MCP服务器，使提示词、对话上下文、代码片段及工具输出暴露。攻击链还包含跨平台恶意软件投递和凭据窃取。

**IOC指标：**

**· SHA256（节选）：**985829083f3937df6c82419216f7697afae0caac8efca6257a756066fe2c0abb, 5ee7145061f05779f7f6f9b72e216713d17d53e183a92f408bfbbc44f2bfb95d, 42a760b15fea7c9af718ee45386c1c3ea1bec9e30c95d16c287bcc8b2efdc72e, 127ae4cad80b6605157ca2a1feada8a235e16aacc5d2119337a98115a4e13274, 20f0a401676292d4ae34932e61f34afa97bcfc47ee517cda2afeb7222264a193

**· Domain（节选）：**apexaccs.org, arena.apexaccs.org, token.apexaccs.org, vrf.apexaccs.org, arena.apexfdn.xyz

**· URL（节选）：**https://vrf.apexaccs.org/api/v1/vrf, https://arena.apexaccs.org/api/llm/v1/chat/completions, https://arena.apexaccs.org/api/llm/v1, https://arena.apexaccs.org/api/copilot/mcp, https://arena.apexaccs.org/dashboard/pilot

**报告链接：**

https://www.elastic.co/security-labs/threat-command/apex-accelerator-malicious-npm-packages

───────────────────────────────────

### **（三）疑似AI辅助间谍活动攻击政府Linux基础设施**

**事件名称：**AI驱动的间谍活动针对政府Linux基础设施

**发布日期：**2026-10-15

**发布机构：**Palo Alto Networks Unit 42

**威胁概述：**

Unit 42披露了一起针对政府及关联基础设施的Linux间谍活动。攻击者利用Web shell、SysGoRAT及反向Shell收集凭据、横向移动和窃取数据库信息。研究人员在脚本中发现对话式注释和推理痕迹，认为存在大模型生成代码或AI代理参与的迹象；这些线索不能单独证明攻击全程自主执行。

**IOC指标：**

**· IP（节选）：**45.88.188.140, 198.23.185.234, 138.68.244.146, 185.21.136.6, 72.61.89.179

**· IP:Port：**104.194.158.65:443

**· Domain：**magento.ink, solidmonpe.com, wibu-bau-bawang.online, beraskencur.site

**· SHA256（节选）：**2bf7992e6260c1a98c709fa98ec766fb9f27692f338b30b43ac821b824fd849e, 27d799ceadb570bfca890d4c2572314afe57eecf14083d30409da15afdfc4704, d73186cea6cf2cf3d48c09139a9d15521365aab675787b4e7a6f81767331c9fd, 9e45830171eb607cf2c0fc80f5cc9cc3db39bb937032136990383a595f6f151e, c527b94e3d21824a674face4cd9d862e536b60ccbf54573839e3360f99188343

**· CVE：**CVE-2025-55182, CVE-2021-4034

**STIX详情：**

```
{
  "type": "bundle",
  "id": "bundle--135b0aa2-2e02-48a2-8ee1-73a82756b76b",
  "spec_version": "2.1",
  "objects": [
    {
      "type": "intrusion-set",
      "spec_version": "2.1",
      "id": "intrusion-set--c9b98851-01c9-4e64-9031-a8162e5e963b",
      "name": "CL-UNK-1211",
      "created": "2026-10-16T04:46:22Z",
      "modified": "2026-10-16T04:46:22Z",
      "description": "针对政府实体和国家附属基础设施的未明身份攻击团伙或攻击集群。",
      "aliases": [
        "UNK"
      ],
      "x_evidence": "原文：Unit 42 identified a campaign targeting government entities and state-affiliated infrastructure... We track this activity as CL-UNK-1211；并称 UNK 表示尚未确定归属的集群。",
      "x_confidence": 0.95
    },
    {
      "type": "malware",
      "spec_version": "2.1",
      "id": "malware--7403585e-c5e5-4322-938e-84cd1fa77e06",
      "name": "SysGoRAT",
      "created": "2026-10-16T04:46:22Z",
      "modified": "2026-10-16T04:46:22Z",
      "description": "攻击者开发的定制跨平台远程访问木马（RAT），使用 Go 编写。",
      "aliases": [
        "sys-control-client",
        "pip2.7",
        "ea_install",
        "semanage"
      ],
      "x_evidence": "原文：The attackers deployed a custom-developed, multi-platform remote access Trojan (RAT) written in Go... We named this malware SysGoRAT；并列出重命名 sys-control-client、pip2.7、ea_install、./semanage。",
      "x_confidence": 0.95
    },
    {
      "type": "tool",
      "spec_version": "2.1",
      "id": "tool--0ed72f37-c812-43f0-b3b3-de4cb9596741",
      "name": "Global Socket",
      "created": "2026-10-16T04:46:22Z",
      "modified": "2026-10-16T04:46:22Z",
      "description": "解决 NAT 和防火墙遍历问题的框架，被攻击者滥用。",
      "aliases": [
        "GSocket"
      ],
      "x_evidence": "原文：The attackers misused Global Socket... They deployed the framework’s binary, gs-netcat.",
      "x_confidence": 0.9
    },
    {
      "type": "vulnerability",
      "spec_version": "2.1",
      "id": "vulnerability--ed292df4-768d-4ad2-be5e-71428943744c",
      "name": "CVE-2021-4034",
      "created": "2026-10-16T04:46:22Z",
      "modified": "2026-10-16T04:46:22Z",
      "description": "用于本地权限提升的漏洞，PwnKit 对应 CVE-2021-4034。",
      "aliases": [
        "PwnKit"
      ],
      "x_evidence": "原文：PwnKit, a self-contained exploit for CVE-2021-4034 — in an attempt to gain root privileges.",
      "x_confidence": 0.95
    },
    {
      "type": "vulnerability",
      "spec_version": "2.1",
      "id": "vulnerability--ae00d943-95b5-444c-aacc-5b73c498a602",
      "name": "CVE-2025-55182",
      "created": "2026-10-16T04:46:22Z",
      "modified": "2026-10-16T04:46:22Z",
      "description": "攻击者扫描并利用的漏洞，React2Shell 对应 CVE-2025-55182。",
      "aliases": [
        "React2Shell"
      ],
      "x_evidence": "原文：attackers deployed a custom vulnerability scanner written in Go that scans for servers vulnerable to CVE-2025-55182 (React2Shell).",
      "x_confidence": 0.95
    },
    {
      "type": "tool",
      "spec_version": "2.1",
      "id": "tool--df37a32c-3e63-401a-a309-b071b820e251",
      "name": "LinPEAS",
      "created": "2026-10-16T04:46:22Z",
      "modified": "2026-10-16T04:46:22Z",
      "description": "用于检查本地权限提升路径的开源工具。",
      "x_evidence": "原文：They started by deploying and executing an open-source tool called LinPEAS to check for local privilege escalation paths.",
      "x_confidence": 0.9
    },
    {
      "type": "tool",
      "spec_version": "2.1",
      "id": "tool--4ffa69b0-663a-4213-89c8-63f68f2bb117",
      "name": "revsocks",
      "created": "2026-10-16T04:46:22Z",
      "modified": "2026-10-16T04:46:22Z",
      "description": "开源反向 SOCKS5 隧道工具。",
      "x_evidence": "原文：The attackers deployed the open-source tool revsocks, a reverse SOCKS5 tunneling tool with SSL/TLS and proxy support.",
      "x_confidence": 0.9
    },
    {
      "type": "tool",
      "spec_version": "2.1",
      "id": "tool--4fbf752a-ab14-4cd0-8f13-2f8336962...
---
title: AI安全专题周报（20261023）
url: https://blog.netlab.360.com/aian-quan-zhuan-ti-zhou-bao-10/
source: 360 Netlab Blog - Network Security Research Lab at 360
date: 2026-10-23
fetch_date: 2026-10-24T06:46:43.493711
---

# AI安全专题周报（20261023）

[![360 Netlab Blog - Network Security Research Lab at 360](https://blog.netlab.360.com/content/images/2019/02/netlab-brand-5.png)](https://blog.netlab.360.com)

* [Botnet](https://blog.netlab.360.com/tag/botnet/)
* [DNSMon](https://blog.netlab.360.com/tag/dnsmon/)
* [DDoS](https://blog.netlab.360.com/tag/ddos/)
* [PassiveDNS](https://blog.netlab.360.com/tag/pdns/)
* [Mirai](https://blog.netlab.360.com/tag/mirai/)
* [DTA](https://blog.netlab.360.com/tag/dta/)

# AI安全专题周报（20261023）

* [![NOTOn1y](/content/images/size/w100/2026/08/2f35bd757c0c0fcb537ee47e8fa31171.jpg)](/author/on1y/)

#### [NOTOn1y](/author/on1y/)

23 Oct 2026
• 阅读时间 82 分钟

[分享](#/share)

**报告编号：**TIC-202610-AI04

**报告周期：**2026年10月17日—10月23日

## 一、报告概述

基于360威胁情报中心对本期公开网络安全素材的整理与分析，本周AI安全风险集中在AI网关供应链投毒、模型与云计费资源劫持、AI编码工具凭据泄露、智能体辅助入侵，以及AI应用组件漏洞。相关事件涉及恶意安装包投递、第三方模型API密钥暴露、跨租户应用凭据滥用、未授权模型调用及代码注入。

**报告重点内容涵盖：**

**· AI供应链与开发凭据风险：**LiteLLM恶意安装包可在Python启动时执行窃密载荷；OpenCode Console安全事件则使关联的第三方模型服务密钥面临泄露风险。

**· AI资源与云身份滥用：**Skynet代理指令显示攻击者试图借用暴露模型驱动攻击；云计费账户劫持活动通过钓鱼与外部项目绑定，让受害者承担未授权AI调用费用。

**· AI辅助入侵与应用漏洞：**ARTEX被用于加速供应链及云环境攻击，BUGSTER与日本API攻击调查提供了AI参与的具体证据；Stable Diffusion WebUI模型加载组件被披露存在代码注入风险。

───────────────────────────────────

## 二、本周重点安全事件

### **（一）LiteLLM 1.107.0安装包遭投毒，窃取凭据并植入后门**

**事件名称：**LiteLLM 再次被劫持：恶意 1.107.0 Wheels 窃取凭证并加载远程代码

**发布日期：**2026-10-21

**发布机构：**JFrog Security Research

**威胁概述：**

JFrog披露，LiteLLM 1.107.0的恶意wheel安装包加入了Python启动钩子，可在应用尚未导入LiteLLM时执行凭据窃取，并提供每小时检查一次的远程代码加载通道。受影响范围还包括对应的官方Docker镜像。恶意载荷收集云服务及AI开发环境中的秘密信息；JFrog在10月22日更新称厂商已控制事件，受污染的发布版本和镜像已被下架。

**IOC指标：**

**· SHA256：**1bbcb1443bc962e45f5aad53fe3d2c30600e0379715fb6c664cdd3ac126c339e

**· URL：**http://www.litellm.dev/healthcheck, https://raw.githubusercontent.com/letters9813/pythonclient-test/main/domain.txt

**· Domain：**www.litellm.dev, litellm.dev

**STIX详情：**

```
{
  "type": "bundle",
  "id": "bundle--28dc2217-11a4-401a-9de4-d646be87843b",
  "spec_version": "2.1",
  "objects": [
    {
      "type": "intrusion-set",
      "spec_version": "2.1",
      "id": "intrusion-set--deae4bd0-74e5-406c-b2e7-5d725af5d1f9",
      "name": "Unknown Attacker",
      "created": "2026-10-21T16:27:25Z",
      "modified": "2026-10-21T16:27:25Z",
      "description": "当前 litellm 1.107.0 供应链攻击的未知幕后攻击者；目前无证据将其与 TeamPCP 关联。",
      "x_evidence": "原文称“The new 1.107.0 compromise uses different payloads and infrastructure. No evidence currently links it to TeamPCP or the earlier access path”。",
      "x_confidence": 0.85
    },
    {
      "type": "infrastructure",
      "spec_version": "2.1",
      "id": "infrastructure--1431aa5b-3b83-498d-90a7-8609eabfa33f",
      "name": "litellm",
      "created": "2026-10-21T16:27:25Z",
      "modified": "2026-10-21T16:27:25Z",
      "description": "被滥用的 LLM 接口/代理 Python 库；恶意 1.107.0 wheel 被注入三个启动文件并发布到 PyPI 和 Docker Hub。",
      "x_evidence": "原文称 LiteLLM 是“a widely used Python interface and proxy for large language model providers”，并描述“malicious litellm 1.107.0 wheels”。",
      "x_confidence": 0.95
    },
    {
      "type": "malware",
      "spec_version": "2.1",
      "id": "malware--8ddd10d2-950b-45be-82c1-6120bffc0a67",
      "name": "privcollect",
      "created": "2026-10-21T16:27:25Z",
      "modified": "2026-10-21T16:27:25Z",
      "description": "由 cook.py 解码启动的凭证窃取恶意软件，收集 SSH/GPG/云/AI 开发凭据、环境变量和 LiteLLM 数据库信息。",
      "x_evidence": "原文称“The decoded program identifies itself as privcollect”，并描述其收集范围。",
      "x_confidence": 0.95
    },
    {
      "type": "url",
      "spec_version": "2.1",
      "id": "url--20dba1d4-75c4-4d04-a774-b3e669648f78",
      "name": "http://www.litellm.dev/healthcheck",
      "created": "2026-10-21T16:27:25Z",
      "modified": "2026-10-21T16:27:25Z",
      "description": "privcollect 加密窃取数据的回传 URL。",
      "x_evidence": "原文 IoC 列表包含“Exfiltration URL: hxxp[:]//www[.]litellm[.]dev/healthcheck”。",
      "x_confidence": 0.95
    },
    {
      "type": "domain-name",
      "spec_version": "2.1",
      "id": "domain-name--fd4da841-95ee-4e7d-b1e3-a03fd8727193",
      "name": "www.litellm.dev",
      "created": "2026-10-21T16:27:25Z",
      "modified": "2026-10-21T16:27:25Z",
      "description": "本次攻击的恶意外传域名。",
      "x_evidence": "原文 IoC 列表包含“Exfiltration domain: www[.]litellm[.]dev”。",
      "x_confidence": 0.95
    },
    {
      "type": "domain-name",
      "spec_version": "2.1",
      "id": "domain-name--e63020fd-4b33-4ffa-8d5a-773a84ab6e8c",
      "name": "litellm.dev",
      "created": "2026-10-21T16:27:25Z",
      "modified": "2026-10-21T16:27:25Z",
      "description": "攻击者注册的 LiteLLM 相似域名。",
      "x_evidence": "原文称“Registration records show that litellm[.]dev was created on October 13, 2026”。",
      "x_confidence": 0.95
    },
    {
      "type": "url",
      "spec_version": "2.1",
      "id": "url--0ad0f2ef-bd57-4e5a-b832-9135498c40fe",
      "name": "https://raw.githubusercontent.com/letters9813/pythonclient-test/main/domain.txt",
      "created": "2026-10-21T16:27:25Z",
      "modified": "2026-10-21T16:27:25Z",
      "description": "C2 死信 URL，用于获取 domain.txt。",
      "x_evidence": "原文 IoC 列表包含“C2 dead-drop URL: hxxps[:]//raw[.]githubusercontent[.]com/letters9813/pythonclient-test/main/domain.txt”。",
      "x_confidence": 0.95
    },
    {
      "type": "domain-name",
      "spec_version": "2.1",
      "id": "domain-name--99f0bac6-7a41-4f2d-85a1-5d6d775b0c9e",
      "name": "raw.githubusercontent.com",
      "created": "2026-10-21T16:27:25Z",
      "modified": "2026-10-21T16:27:25Z",
      "description": "死信 URL 的托管域名，用于托管 domain.txt。",
      "x_evidence": "死信 URL 本身包含 raw.githubusercontent.com。",
      "x_confidence": 0.9
    },
    {
      "type": "infrastructure",
      "spec_version": "2.1",
      "id": "infrastructure--ace1609a-9b86-4010-ba33-535e8f88d66f",
      "name": "PyPI",
      "created": "2026-10-21T16:27:25Z",
      "modified": "2026-10-21T16:27:25Z",
      "description": "恶意 litellm 1.107.0 wheel 的发布平台。",
      "x_evidence": "原文称“PyPI has since removed the compromised 1.107.0 release”。",
      "x_confidence": 0.95
    },
    {
      "type": "infrastructure",
      "spec_version": "2.1",
      "id": "infrastructure--aba9630b-b9ed-4834-aaca-864d194ba4f8",
      "name": "Docker Hub",
      "created": "2026-10-21T16:27:25Z",
      "modified": "2026-10-21T16:27:25Z",
      "description": "恶意 litellm/litellm:1.107.0 镜像的发布平台。",
      "x_evidence": "原文称“Docker Hub has since removed the affected image and all affected tags”。",
      "x_confidence": 0.95
    },
    {
      "type": "infrastructure",
      "spec_version": "2.1",
      "id": "infrastructure--c25c65d3-6957-4abb-a6a9-7e4a78674de1",
      "name": "letters9813/pythonclient-test",
      "created": "2026-10-21T16:27:25Z",
      "modified": "2026-10-21T16:27:25Z",
      "description": "GitHub 仓库，用于托管 domain.txt 死信 URL。",
      "x_evidence": "原文 IoC 列表包含“Dead-drop repository: letters9813/pythonclient-test”。",
      "x_confidence": 0.9
    },
    {
      "type": "observed-data",
      "spec_version": "2.1",
      "id": "observed-data--175c2020-bf1a-44e8-a328-99820d399f08",
      "created": "2026-10-21T16:27:25Z",
      "modified": "2026-10-21T16:27:25Z",
      "first_observed": "2026-10-21T16:27:25Z",
      "last_observed": "2026-10-21T16:27:25Z",
      "number_observed": 1,
      "objects": {
        "0": {
          "type": "file",
          "name": "cook.pth",
          "description": "恶意 wheel 中的 Python 启动钩子文件，位于 purelib 下，内容为 import cook。",
          "aliases": [],
          "evidence": "原文称“The first file, cook.pth, contains only: import cook”。",
          "confidence": 0.95
        },
        "1": {
          "type": "file",
          "name": "cook.py",
          "description": "恶意启动文件，包含 Base64 编码、zlib 压缩的 privcollect 程序。",
          "aliases": [],
          "evidence": "原文称“cook.py launches the privcollect credential stealer”。",
          "confidence": 0.95
        },
        "2": {
          "type": "file",
          "name": "sitecustomize.py",
          "description": "恶意 Py...
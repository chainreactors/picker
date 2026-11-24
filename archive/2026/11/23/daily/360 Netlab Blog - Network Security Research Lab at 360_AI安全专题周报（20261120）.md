---
title: AI安全专题周报（20261120）
url: https://blog.netlab.360.com/aian-quan-zhuan-ti-zhou-bao-20261120/
source: 360 Netlab Blog - Network Security Research Lab at 360
date: 2026-11-23
fetch_date: 2026-11-24T11:48:15.651715
---

# AI安全专题周报（20261120）

[![360 Netlab Blog - Network Security Research Lab at 360](https://blog.netlab.360.com/content/images/2019/02/netlab-brand-5.png)](https://blog.netlab.360.com)

* [Botnet](https://blog.netlab.360.com/tag/botnet/)
* [DNSMon](https://blog.netlab.360.com/tag/dnsmon/)
* [DDoS](https://blog.netlab.360.com/tag/ddos/)
* [PassiveDNS](https://blog.netlab.360.com/tag/pdns/)
* [Mirai](https://blog.netlab.360.com/tag/mirai/)
* [DTA](https://blog.netlab.360.com/tag/dta/)

# AI安全专题周报（20261120）

* [![NOTOn1y](/content/images/size/w100/2026/08/2f35bd757c0c0fcb537ee47e8fa31171.jpg)](/author/on1y/)

#### [NOTOn1y](/author/on1y/)

23 Nov 2026
• 阅读时间 50 分钟

[分享](#/share)

**报告编号：**TIC-202611-AI03

**报告日期：**2026年11月14日—11月20日

## **一、报告概览**

本期整理7项AI安全事件与研究。微软agent-framework遭供应链投毒，恶意GitHub仓库将项目说明和启动钩子变成编码助手的执行入口；Kokoro发布者账号接管研究则暴露了模型更新链的身份恢复风险。攻击侧，非洲证券交易所调查发现疑似AI生成的凭证搜寻工具，Google披露补丁差分与自动利用链的新观测。设备码钓鱼及CyberStrikeAI工作区案例进一步表明，授权范围、工具审批和实际执行结果需要分别核查。

**报告重点内容涵盖：**

开发与模型供应链：agent-framework恶意版本、GitHub仓库配置投毒、Kokoro发布者账号接管。

AI辅助攻击：非洲证券交易所凭证搜寻、exploit\_agent自动化漏洞分析与利用。

智能体权限治理：设备码授权滥用、CyberStrikeAI工具审批关闭后的连续执行。

## **二、本周重点安全事件**

### **（一）微软agent-framework遭供应链投毒**

**事件名称：**恶意Python包利用.pth启动钩子窃取云与CI/CD凭证

**发布日期：**2026-11-18

**发布机构：**JFrog Security Research、Wiz、Elastic Security Labs

**威胁概述：**

微软agent-framework在PyPI发布的1.26.1、1.26.2版本被植入凭证窃取代码，两个恶意版本随后被隔离或移除。载荷通过site-packages中的.pth文件挂接Python初始化流程，即使业务代码没有导入该框架，后续启动解释器也可能触发。样本收集环境变量、云端令牌和开发工具凭据，1.26.2还扩展至GitHub Actions的OIDC场景，使用固定webhook地址外传。不同研究对发布链路的描述存在差异，现有证据不足以认定微软源代码仓库或整个构建环境失陷。受影响方应先隔离环境并处置启动钩子，重建运行环境，撤销可能暴露的凭据，同时排查镜像、锁文件及依赖缓存中的恶意版本。

**IOC指标：**

**· SHA256（节选）：**d27fa34414e6201d5e03e559ef634f020057554d7b3f4898dd5d7cd3e989e110, 3d20a8bc91351a9a16b6db243b848ceca0206b7a8623b02d2af553a9c9f7e0a9

**· URL：**https://webhook.site/d381fd80-ec62-42ad-8f5c-d1b15103c9bb

上述URL为被滥用的特定收集端点，不能据此将webhook.site整站认定为恶意。

**STIX详情：**

```
{
  "type": "bundle",
  "id": "bundle--e6195b08-663e-4649-9770-5cf4b7d0dd80",
  "spec_version": "2.1",
  "objects": [
    {
      "type": "intrusion-set",
      "spec_version": "2.1",
      "id": "intrusion-set--4a719314-d1a0-4b70-8d8e-55ab7ce9e3ef",
      "name": "Unattributed PyPI Supply Chain Actor",
      "created": "2026-11-18T16:24:35Z",
      "modified": "2026-11-18T16:24:35Z",
      "description": "未归因至已知威胁组，通过供应链投毒方式投毒合法 agent-framework 包并发布至 PyPI，窃取 Azure 身份、CI/CD 令牌及 AI 开发者机密。",
      "x_evidence": "原文结论：'We have not attributed this attack to a known threat group.' 攻击者本地重新打包并发布恶意版本。",
      "x_confidence": 0.95
    },
    {
      "type": "malware",
      "spec_version": "2.1",
      "id": "malware--bac8b5b5-3b66-474d-bad3-1695d6f49c8f",
      "name": "agent-framework",
      "created": "2026-11-18T16:24:35Z",
      "modified": "2026-11-18T16:24:35Z",
      "description": "被攻击者投毒并在本地重新打包发布至 PyPI 的 Python 包，恶意版本为 1.26.1 和 1.26.2。",
      "x_evidence": "原文：'The attacker repacked the clean wheel locally and published versions 1.26.1 and 1.26.2 with a .pth startup hook'。",
      "x_confidence": 0.95
    },
    {
      "type": "malware",
      "spec_version": "2.1",
      "id": "malware--35c2808d-08bc-42f2-991c-5a386ec68969",
      "name": "agent_framework_meta",
      "created": "2026-11-18T16:24:35Z",
      "modified": "2026-11-18T16:24:35Z",
      "description": "被注入恶意代码的模块名，在 1.26.1 版本中通过 __init__.py 触发 _telemetry._start()。",
      "x_evidence": "原文：'the agent-framework wheel installs a small stub module named agent_framework_meta'，且攻击者在 1.26.1 中修改其 __init__.py。",
      "x_confidence": 0.9
    },
    {
      "type": "url",
      "spec_version": "2.1",
      "id": "url--bcd728c1-a11f-4980-b1f5-82ae981451ab",
      "name": "https://webhook.site/d381fd80-ec62-42ad-8f5c-d1b15103c9bb?t=telemetry",
      "created": "2026-11-18T16:24:35Z",
      "modified": "2026-11-18T16:24:35Z",
      "description": "原文明确标注为窃密数据外传 URL，通过 HTTPS POST 接收序列化监控数据。",
      "x_evidence": "原文：'Plaintext webhook.site exfiltration ... hxxps[:]//webhook[.]site/d381fd80-ec62-42ad-8f5c-d1b15103c9bb ... sends an HTTPS POST to ?t=telemetry'。",
      "x_confidence": 0.95
    },
    {
      "type": "attack-pattern",
      "spec_version": "2.1",
      "id": "attack-pattern--b5db4edb-a256-4616-98b4-ddb09a9ed135",
      "name": "PyPI Supply Chain Compromise",
      "created": "2026-11-18T16:24:35Z",
      "modified": "2026-11-18T16:24:35Z",
      "description": "攻击者在本地重新打包合法 agent-framework wheel 并发布至 PyPI，投毒版本为 1.26.1 和 1.26.2。",
      "x_evidence": "原文：'Rather than compromising Microsoft's build pipeline, the attacker repacked the clean wheel locally and published versions 1.26.1 and 1.26.2 with a .pth startup hook'。",
      "x_confidence": 0.9
    },
    {
      "type": "attack-pattern",
      "spec_version": "2.1",
      "id": "attack-pattern--6e943eb1-c88f-4bae-a276-5ad708aad56d",
      "name": "Python .pth Startup Hook Execution",
      "created": "2026-11-18T16:24:35Z",
      "modified": "2026-11-18T16:24:35Z",
      "description": "利用 site-packages 中 .pth 文件以 import 开头的行在 Python 启动时自动执行恶意代码。",
      "x_evidence": "原文：'During CPython initialization, site.py scans site-packages for .pth files and passes any line starting with import to exec() before sitecustomize or user scripts run.'",
      "x_confidence": 0.95
    },
    {
      "type": "attack-pattern",
      "spec_version": "2.1",
      "id": "attack-pattern--b7aaa425-b7bb-443e-beb7-542ccf3ee1c6",
      "name": "Credential and Secret Harvesting",
      "created": "2026-11-18T16:24:35Z",
      "modified": "2026-11-18T16:24:35Z",
      "description": "收集环境变量中的 Azure、AWS、GitHub、OpenAI 等凭据，读取 35 个 glob 模式目标文件，并查询 Azure 元数据服务获取 OAuth2 令牌。",
      "x_evidence": "原文：'On startup, _collect() records the hostname, username, working directory, and sys.argv[:20], then sweeps os.environ for 31 case-insensitive substrings covering Azure, AWS, GitHub, OpenAI...' 及 'evaluates 35 glob patterns'。",
      "x_confidence": 0.95
    },
    {
      "type": "attack-pattern",
      "spec_version": "2.1",
      "id": "attack-pattern--8e99899e-7ec3-45e2-806f-b3b81409a599",
      "name": "Exfiltration via HTTPS POST",
      "created": "2026-11-18T16:24:35Z",
      "modified": "2026-11-18T16:24:35Z",
      "description": "将收集的数据序列化为 JSON，经 zlib 压缩、Base64 编码后通过 HTTPS POST 发送至攻击者指定的 webhook.site URL。",
      "x_evidence": "原文：'It serializes the harvested data to JSON, compresses it with zlib, Base64-encodes the result with no encryption, and sends an HTTPS POST to ?t=telemetry'。",
      "x_confidence": 0.95
    },
    {
      "type": "observed-data",
      "spec_version": "2.1",
      "id": "observed-data--33dc2c55-b227-4c5d-a5d3-f5a9230c4061",
      "created": "2026-11-18T16:24:35Z",
      "modified": "2026-11-18T16:24:35Z",
      "first_observed": "2026-11-18T16:24:35Z",
      "last_observed": "2026-11-18T16:24:35Z",
      "number_observed": 1,
      "objects": {
        "0": {
          "type": "file",
          "name": "agent_framework_meta/__init__.py",
          "description": "被添加恶意调用的文件，SHA-256: c275ccbe520ef3c0f02dc6a35389e427f9f1b4e0b12e140cd7bf7179ce143f02。",
          "aliases": [],
          "evidence": "原文：'They appended a silent _telemetry._start() call to agent_framework_meta/__init__.py'，IOC 表给出该哈希。",
          "confidence": 0.95
        },
        "1": {
          "type": "file",
          "name": "agent_framework_meta.pth",
          "description": "1.26.1 版本中添加的启动钩子文件，内容为 import agent_framework_meta，SHA-256: 21f28e8517a10ffe431f8d68f5875c85eca4001ae6d118322b0a41873998eb5e。",
          "aliases": [],
          "evidence": "原文：'added a 28-byte agent_framework_meta.pth file to the root of site-packages containing import agent_framework_meta'，IOC 表给出哈希。",
          "confidence": 0.95
        },
        "2": {
          "type": "file",
          "name": "af_runtime_diag.pth",
          "description": "1.26.2 版本中使用的启动钩子文件，SHA-256: 325e7e9f0ec94e41ad1a1b7a3f18a6b8b5bffece2e2b97b8d3369eb967452f93。",
          "aliases": [],
          "evidence": "原文：'In 1.26.2, the attacker restored the cl...
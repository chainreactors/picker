---
title: AI安全专题周报
url: https://blog.netlab.360.com/aian-quan-zhuan-ti-zhou-bao-6/
source: 360 Netlab Blog - Network Security Research Lab at 360
date: 2026-09-18
fetch_date: 2026-09-19T07:01:34.905494
---

# AI安全专题周报

[![360 Netlab Blog - Network Security Research Lab at 360](https://blog.netlab.360.com/content/images/2019/02/netlab-brand-5.png)](https://blog.netlab.360.com)

* [Botnet](https://blog.netlab.360.com/tag/botnet/)
* [DNSMon](https://blog.netlab.360.com/tag/dnsmon/)
* [DDoS](https://blog.netlab.360.com/tag/ddos/)
* [PassiveDNS](https://blog.netlab.360.com/tag/pdns/)
* [Mirai](https://blog.netlab.360.com/tag/mirai/)
* [DTA](https://blog.netlab.360.com/tag/dta/)

# AI安全专题周报

* [![NOTOn1y](/content/images/size/w100/2026/08/2f35bd757c0c0fcb537ee47e8fa31171.jpg)](/author/on1y/)

#### [NOTOn1y](/author/on1y/)

18 Sep 2026
• 阅读时间 65 分钟

[分享](#/share)

**报告编号：**TIC-202609-AI03

**报告周期：**2026年9月12日—9月18日

## 一、报告概述

基于360威胁情报中心对本期公开网络安全素材的整理与分析，本周AI安全风险主要集中在AI知识库与推理服务漏洞、Agent Skill和软件包供应链攻击、AI编程助手会话劫持、非官方AI中转服务数据泄露、AI驱动的移动端威胁以及ChatGPT品牌钓鱼等方向。相关事件涉及远程代码执行、凭据与源代码窃取、恶意包投递、敏感对话留存和账户凭证盗取。

**报告重点内容涵盖：**

**· AI应用与Agent生态安全：**QAnything未授权文件写入漏洞可导致Root RCE，vLLM聊天模板漏洞可造成资源耗尽，Skill链路还面临路径逃逸、供应链投毒和代码后门风险。

**· AI开发与软件供应链风险：**攻击者劫持AI编程助手会话传播Shai-Hulud蠕虫，GemStuffer活动则利用大量恶意RubyGems包执行代码、窃取凭据和外传数据。

**· AI数据与用户侧威胁：**非官方AI中转站截获并出售明文数据，RatHat针对移动端银行凭证，攻击者还利用ChatGPT订阅付款提醒实施钓鱼。

───────────────────────────────────

## 二、本周重点安全事件

### （一）QAnything任意文件写入可导致Root RCE

**事件名称：**无需认证！本地知识库QAnything任意文件写入漏洞可提权至Root RCE（CVE-2026-88533）

**发布日期：**2026-09-18

**发布机构：**360漏洞研究院

**威胁概述：**

360漏洞研究院披露，QAnything存在未授权任意文件创建漏洞CVE-2026-88533。未经身份认证的攻击者可访问文件上传接口，通过特制文件名实施路径遍历，将文件写入非预期目录。在官方Docker部署场景中，攻击者可在服务重启后执行代码并获得root权限。

**IOC指标：**

**· CVE：**CVE-2026-88533

**STIX详情：**

```
{
  "type": "bundle",
  "id": "bundle--1e1eb052-5326-43c0-bd42-b62d47625c1f",
  "spec_version": "2.1",
  "objects": [
    {
      "type": "intrusion-set",
      "spec_version": "2.1",
      "id": "intrusion-set--f84e7e80-cef4-4132-99be-9348e2278e03",
      "name": "Unauthenticated Remote Attacker",
      "created": "2026-09-18T07:28:02Z",
      "modified": "2026-09-18T07:28:02Z",
      "description": "攻击链主体；未经身份认证、无需登录即可远程访问目标服务的攻击者。",
      "x_evidence": "原文称“未经身份认证的远程攻击者可通过网络访问目标服务并利用该缺陷”，且攻击链主体为未经身份认证的远程攻击者。",
      "x_confidence": 0.9
    },
    {
      "type": "tool",
      "spec_version": "2.1",
      "id": "tool--fed225a9-6eea-414d-b92d-50dcb71365b6",
      "name": "QAnything",
      "created": "2026-09-18T07:28:02Z",
      "modified": "2026-09-18T07:28:02Z",
      "description": "存在未授权任意文件创建漏洞的本地知识库软件；受影响版本：v1.4.x ≤ 受影响版本 ≤ v2.0.0。",
      "x_evidence": "原文称“QAnything 被披露存在未授权任意文件创建漏洞（CVE-2026-88533）”，并列出“影响范围: QAnything v1.4.x ≤ 受影响版本 ≤ v2.0.0”。",
      "x_confidence": 0.98
    },
    {
      "type": "vulnerability",
      "spec_version": "2.1",
      "id": "vulnerability--1ebde131-8ed9-4bfc-b6c5-48a38f4bb60d",
      "name": "CVE-2026-88533",
      "created": "2026-09-18T07:28:02Z",
      "modified": "2026-09-18T07:28:02Z",
      "description": "QAnything 未授权任意文件创建漏洞；CVSS 3.1 评分 9.8；可导致未经认证 root 权限代码执行。",
      "x_evidence": "原文明确标注“漏洞编号 CVE-2026-88533”及“CVSS 3.1 9.8”，并说明可导致未授权 root 权限代码执行。",
      "x_confidence": 0.99
    },
    {
      "type": "attack-pattern",
      "spec_version": "2.1",
      "id": "attack-pattern--870f706f-4d58-45e6-be77-b1bfed48cf4f",
      "name": "Path Traversal",
      "created": "2026-09-18T07:28:02Z",
      "modified": "2026-09-18T07:28:02Z",
      "description": "漏洞类型，导致任意文件创建；对文件名解码和基础处理后未充分约束路径分隔符、上级目录引用及绝对路径。",
      "x_evidence": "原文称“漏洞类型 路径遍历”，并指出“未对路径分隔符、上级目录引用及绝对路径进行充分约束”。",
      "x_confidence": 0.95
    },
    {
      "type": "tool",
      "spec_version": "2.1",
      "id": "tool--55d0c9c3-4429-468c-a234-222dddbde19d",
      "name": "Docker",
      "created": "2026-09-18T07:28:02Z",
      "modified": "2026-09-18T07:28:02Z",
      "description": "官方部署场景使用的容器技术；官方 Docker 部署中后端进程默认以 root 权限运行。",
      "x_evidence": "原文称“官方 Docker 部署场景中，后端进程以 root 权限运行”。",
      "x_confidence": 0.9
    },
    {
      "type": "tool",
      "spec_version": "2.1",
      "id": "tool--823cc120-0442-49f8-ae24-baac0f188764",
      "name": "Python",
      "created": "2026-09-18T07:28:02Z",
      "modified": "2026-09-18T07:28:02Z",
      "description": "攻击者结合其启动加载机制，在后端服务重启后触发代码执行。",
      "x_evidence": "原文称“攻击者可进一步结合 Python 启动加载机制，在后端重新启动后触发 root 权限代码执行”。",
      "x_confidence": 0.9
    },
    {
      "type": "infrastructure",
      "spec_version": "2.1",
      "id": "infrastructure--c41da074-97aa-458e-8bd2-7e53c4698df6",
      "name": "QAnything Port 8777",
      "created": "2026-09-18T07:28:02Z",
      "modified": "2026-09-18T07:28:02Z",
      "description": "目标服务默认端口 8777；在可被攻击者网络访问时成为初始访问入口。",
      "x_evidence": "原文临时修复方案提及“QAnything 默认 8777 端口”，并指出应限制该端口避免服务直接暴露。",
      "x_confidence": 0.95
    },
    {
      "type": "relationship",
      "spec_version": "2.1",
      "id": "relationship--04f27030-9331-4725-a84f-aeae1715371f",
      "relationship_type": "targets",
      "source_ref": "intrusion-set--f84e7e80-cef4-4132-99be-9348e2278e03",
      "target_ref": "tool--fed225a9-6eea-414d-b92d-50dcb71365b6",
      "created": "2026-09-18T07:28:02Z",
      "modified": "2026-09-18T07:28:02Z",
      "description": "未经身份认证的远程攻击者通过网络访问并针对目标 QAnything 服务。",
      "x_evidence": "原文称“未经身份认证的远程攻击者可通过网络访问目标服务”及“目标 QAnything 服务”。",
      "x_confidence": 0.95
    },
    {
      "type": "relationship",
      "spec_version": "2.1",
      "id": "relationship--ff6a9c7c-54f9-4ff8-9d47-bcde06fef595",
      "relationship_type": "uses",
      "source_ref": "intrusion-set--f84e7e80-cef4-4132-99be-9348e2278e03",
      "target_ref": "attack-pattern--870f706f-4d58-45e6-be77-b1bfed48cf4f",
      "created": "2026-09-18T07:28:02Z",
      "modified": "2026-09-18T07:28:02Z",
      "description": "攻击者使用路径遍历技术，通过特制文件名利用漏洞。",
      "x_evidence": "原文称“攻击者在无需身份认证的情况下，可通过公开的知识库及文件上传接口提交特制文件名”，漏洞类型为路径遍历。",
      "x_confidence": 0.9
    },
    {
      "type": "relationship",
      "spec_version": "2.1",
      "id": "relationship--10c73b77-f229-460a-9b91-8304870b1cef",
      "relationship_type": "exploits",
      "source_ref": "intrusion-set--f84e7e80-cef4-4132-99be-9348e2278e03",
      "target_ref": "vulnerability--1ebde131-8ed9-4bfc-b6c5-48a38f4bb60d",
      "created": "2026-09-18T07:28:02Z",
      "modified": "2026-09-18T07:28:02Z",
      "description": "攻击者利用 CVE-2026-88533 实现任意文件创建。",
      "x_evidence": "原文称“未经身份认证的远程攻击者可通过网络访问目标服务并利用该缺陷”。",
      "x_confidence": 0.95
    },
    {
      "type": "relationship",
      "spec_version": "2.1",
      "id": "relationship--99f3daed-128a-4963-ad12-3cb0deb31fb3",
      "relationship_type": "exploits",
      "source_ref": "attack-pattern--870f706f-4d58-45e6-be77-b1bfed48cf4f",
      "target_ref": "vulnerability--1ebde131-8ed9-4bfc-b6c5-48a38f4bb60d",
      "created": "2026-09-18T07:28:02Z",
      "modified": "2026-09-18T07:28:02Z",
      "description": "路径遍历攻击技术利用 CVE-2026-88533 实现任意文件创建。",
      "x_evidence": "原文将漏洞类型标注为“路径遍历”，并关联“CVE-2026-88533 QAnything 未授权任意文件创建漏洞”。",
      "x_confidence": 0.95
    },
    {
      "type": "relationship",
      "spec_version": "2.1",
      "id": "relationship--95844be3-9698-4ae7-bb94-7a300f1b7276",
      "relationship_type": "targets",
      "source_ref": "vulnerability--1ebde131-8ed9-4bfc-b6c5-48a38f4bb60d",
      "target_ref": "tool--fed225a9-6eea-414d-b92d-50dcb71365b6",
      "created": "2026-09-18T07:28:02Z",
      "modified": "2026-09-18T07:28:02Z",
      "description": "CVE-2026-88533 影响 QAnything 本地知识库软件。",
      "x_evidence": "原文称“QAnything 被披露存在未授权任意文件创建漏洞（CVE-2026-88533）”。",
      "x_confidence": 0.99
    },
    {
      "type": "relationship",
      "spec_version": "2.1",
      "id": "relationship--7a1fbe31-ffd2-4d4e-9326-016a0e59cd92",
      "relationship_type": "uses",
      "source_ref": "tool--fed225a9-6eea-414d-b92d-50dcb71365b6",
      "target_ref": "tool--55d0c9c3-4429-468c-a234-222dddbde19d",
      "created": "2026-09-18T07:28:02Z",
      "modified": "2026-09-18T07:28:02Z",
      "description": "QAnything 官方部署场景使用 Docker 容器技术，且后端进程默认以 root 权限运行。",
      "x_evidence": "原文称“官方 Docker 部署场景中，后端进程以 root 权限运行”。",
      "x_confidence": 0.9
  ...
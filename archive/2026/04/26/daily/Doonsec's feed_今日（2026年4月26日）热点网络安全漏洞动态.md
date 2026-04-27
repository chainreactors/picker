---
title: 今日（2026年4月26日）热点网络安全漏洞动态
url: https://mp.weixin.qq.com/s/yk3Na1rZNQq8d0ck-cs45A
source: Doonsec's feed
date: 2026-04-26
fetch_date: 2026-04-27T05:05:49.590866
---

# 今日（2026年4月26日）热点网络安全漏洞动态

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/RwAbCjh555v4svfONicO18qzL5oqUb6p8CUYYjELjszKHxzfjoibXonMfoYicapXZdJTmcvqCT92MXsL0NQKzAotoTZOM44gnlhd24B2VPsgkA/0?wx_fmt=jpeg)

# 今日（2026年4月26日）热点网络安全漏洞动态

奇安信 CERT

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**日期：**2026-04-26　　**威胁等级：****High****来源：**Kaspersky · Black Hat Asia · CISA KEV · Microsoft MSRC

## 一、概要

截至2026年4月26日早间，本日热度最高的漏洞主要来自**Black Hat Asia 2026**会议披露及近期威胁情报。焦点是**PhantomRPC**（Windows RPC架构权限提升漏洞），由Kaspersky研究员Haidar Kabibo于4月24日披露，引发全球安全社区热议；同期**Microsoft Defender零日系列**（BlueHammer、RedSun、UnDefend）仍在活跃利用，**SharePoint Spoofing零日**（CVE-2026-32201）作为4月Patch Tuesday在野利用漏洞持续发酵。

## 二、高危漏洞详情

### PhantomRPC：Windows RPC架构权限提升（今日热度最高）

**无CVE / 无官方补丁**本地权限提升Black Hat Asia 2026

**受影响产品：**所有Windows版本（包括客户端和服务器版），影响Windows RPC运行时（rpcrt4.dll）。

**影响：**本地权限提升至SYSTEM级别。低权限进程（例如NT AUTHORITY\NETWORK SERVICE）可伪造RPC服务器，拦截高权限客户端的RPC调用，利用RpcImpersonateClient API冒充客户端安全上下文，实现从低权限服务账户直接提升至SYSTEM/Administrator权限。无需内存破坏，属于**架构设计缺陷**。

**热度原因：**4月24日Black Hat Asia 2026由Kaspersky研究员Haidar Kabibo正式披露（4月25日媒体大量报道），提供5种具体利用路径PoC和审计工具。Microsoft早在2025年9月收到报告，但评估为"moderate"严重性，**拒绝分配CVE、不计划立即修补**，引发安全社区强烈不满。该漏洞暴露Windows RPC根本设计弱点，潜在攻击向量几乎无限，适用于gpupdate.exe、Microsoft Edge启动、DHCP/WDI服务等多种场景。X平台和安全论坛昨日讨论量激增，被视为"改变权限提升方式"的新型技术。

**修复建议：**无官方补丁（Microsoft已关闭案例）；启用ETW-based RPC监控（Event ID 1的RPC\_S\_SERVER\_UNAVAILABLE错误+高模拟级别）；尽可能启用被禁用的服务（如TermService）以占用合法端点；严格限制SeImpersonatePrivilege（仅授予必需进程）；使用Kaspersky GitHub上的PhantomRPC审计工具（github.com/KasperskyOS-community/phantom-rpc）扫描可利用模式；部署监控规则评估整体风险。

### Microsoft Defender零日系列：BlueHammer + RedSun + UnDefend（持续活跃）

**CVSS 7.8~9.0 High/Critical**仍处活跃利用

**受影响产品：**Microsoft Defender Antimalware Platform（所有支持版本）。

**影响：**

* **BlueHammer**

  （CVE-2026-33825，已修补）：权限提升至SYSTEM。
* **RedSun**

  ：触发Defender警报后实现侦察和手动命令执行。
* **UnDefend**

  ：DoS攻击（阻止Defender接收签名更新或导致防病毒停止工作），结合其他漏洞可执行任意程序。

**热度原因：**同一研究员Chaotic Eclipse（GitHub Nightmare-Eclipse）因不满Microsoft漏洞处理流程，于4月初公开BlueHammer，后续连续披露RedSun和UnDefend。Huntress威胁情报公司在4月10-16日检测到真实利用活动（包括FunnyApp.exe、undef.exe），PoC已在GitHub公开。4月20日前后中文媒体（iThome等）持续跟进，形成"第三款Defender零日"话题，热度居高不下。

**修复建议：**立即更新Microsoft Defender到**4.18.26030.3011或更高版本**（Windows Security > Virus & threat protection > Protection updates > Check for updates）；BlueHammer已通过4月Patch Tuesday修补，RedSun和UnDefend建议持续监控Microsoft后续补丁；开启Microsoft Defender for Endpoint高级防护；隔离可疑进程；监控Defender警报和EICAR测试文件触发。

### CVE-2026-32201：Microsoft SharePoint Server 欺骗漏洞（Patch Tuesday余热）

**Spoofing 欺骗**在野利用零日

**受影响产品：**Microsoft SharePoint Server（2016、2019、Subscription Edition）。

**影响：**欺骗漏洞（Spoofing），未授权攻击者通过网络进行欺骗，可查看敏感信息并修改已披露信息（影响机密性和完整性）。

**热度原因：**4月Patch Tuesday确认的**在野利用零日**，CISA等机构关注度高，与Defender零日同期讨论，成为企业管理员重点关注对象。

**修复建议：**立即应用**2026年4月Patch Tuesday安全更新**（通过Windows Update或Microsoft Update Catalog）；优先更新SharePoint服务器；避免通过预览窗格打开可疑文档；启用SharePoint高级威胁防护（ATP）。

## 三、总体修复提醒

* **优先级：**

  PhantomRPC（无补丁，架构级缺陷）和SharePoint Spoofing零日（在野利用）为最高优先；Defender零日系列（RedSun/UnDefend）需持续跟进Microsoft后续补丁。
* **PhantomRPC专项：**

  下载Kaspersky审计工具（github.com/KasperskyOS-community/phantom-rpc）扫描可利用模式；启用ETW RPC监控；收紧SeImpersonatePrivilege权限分配。
* **通用防护：**

  启用EDR/XDR、限制SeImpersonatePrivilege非必要授予、监控RPC异常事件；SharePoint管理员检查最新Patch Tuesday更新状态。
* **持续关注：**

  建议定期查看Microsoft Security Response Center和CISA KEV最新页面获取实时更新。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4ic3Dr2nTQbrt9ZdsEIxjK36YibkxgDHpwdDIFJvShiaib2ia3lzIIVqEeDNDEib9WNuZ1IdcjgUWIWGWKw/0?wx_fmt=png)

奇安信 CERT

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4ic3Dr2nTQbrt9ZdsEIxjK36YibkxgDHpwdDIFJvShiaib2ia3lzIIVqEeDNDEib9WNuZ1IdcjgUWIWGWKw/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过
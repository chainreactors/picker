---
title: 今日（2026年5月1日）热点网络安全漏洞动态
url: https://mp.weixin.qq.com/s/LmGpBQH7k4z7FNnlSdlSgw
source: Doonsec's feed
date: 2026-05-01
fetch_date: 2026-05-02T04:57:56.232328
---

# 今日（2026年5月1日）热点网络安全漏洞动态

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/RwAbCjh555vO8H1T6Zb4ica0wJ5y9xXAmFQnankJ5ncRErMws39FnCj3E1bMnF4pTbU6iaSWYoic3icHMqO2ibKcultsjz6mnHXutaCI8XX6nOTk/0?wx_fmt=jpeg)

# 今日（2026年5月1日）热点网络安全漏洞动态

奇安信 CERT

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**日期：**2026-05-01　　**威胁等级：****Critical****来源：**CISA KEV · KnownHost · Tenable · Microsoft MSRC

## 一、概要

2026年4月30日至5月1日最新高热度漏洞：**cPanel & WHM 认证绕过**（CVE-2026-41940，Critical，已在野零日利用，PoC公开，CISA要求5月3日前修补）；**Tenda 4G300路由器命令注入**（CVE-2026-7469，Critical）；**n8n XML节点原型污染RCE**（CVE-2026-42232/42231，Critical）；以及**Microsoft Defender零日系列**持续活跃利用。以上漏洞均有新进展，建议立即处置。

## 二、高危漏洞详情

### CVE-2026-41940：cPanel & WHM 认证绕过（最高优先级）

**CVSS Critical**已在野零日利用 · KEV

**受影响产品：**WebPros cPanel & WHM（WebHost Manager）、WP Squared（WordPress Squared）所有未修补版本。

**影响：**缺失认证关键功能，允许**未认证远程攻击者**绕过登录流程，直接获得控制面板未授权访问，可导致服务器完全接管、数据窃取或进一步恶意操作。

**热度原因：**2026年4月28-30日披露后，**已在野零日利用**（PoC已公开）；托管商KnownHost确认在披露前已观察到成功利用尝试，最早可追溯至2月23日；cPanel作为大量网站主机控制面板影响广泛；CISA已加入KEV目录，要求联邦机构在**5月3日前**完成修补。

**修复建议：**立即升级到cPanel官方修复版本（参考4月28日安全更新）；检查release notes并应用补丁；临时措施：限制控制面板公网暴露、使用强WAF规则阻挡异常登录流量、启用双因素认证；修补后验证登录流程。

### CVE-2026-7469：Tenda 4G300 路由器命令注入

**CVSS Critical**4月30日披露

**受影响产品：**Tenda 4G300 路由器，固件版本 US\_4G300V1.0Mt\_V1.01.42\_CN\_TDC01 等特定版本。

**影响：**通过操纵 `/goform/DelFil` 中的 `delflag` 参数，允许远程攻击者**执行任意命令**，可完全控制路由器并横向渗透内网。

**热度原因：**2026年4月30日左右在最新CVE列表中高调出现，公开利用代码已可用；IoT/路由器设备常被大规模扫描利用，尤其在固件更新滞后的场景下，热度快速上升。

**修复建议：**尽快升级到Tenda最新固件版本（如有）；临时缓解：禁用远程管理、将设备置于隔离网络、监控异常流量；建议更换不支持及时更新的旧设备。

### CVE-2026-42232 & CVE-2026-42231：n8n XML节点原型污染 RCE

**CVSS Critical**原型污染 RCE

**受影响产品：**n8n（工作流自动化工具）受影响版本（XML Node 和 XML Webhook Body Parser 组件）。

**影响：**原型污染漏洞，可导致**远程代码执行（RCE）**。攻击者通过恶意XML输入污染原型，实现代码执行，可完全接管n8n自动化平台。

**热度原因：**最近在Tenable最新CVE列表中被标记为高危；n8n作为流行开源/自托管自动化平台，广泛用于DevOps和业务流程，RCE风险高；原型污染漏洞易被自动化攻击利用。

**修复建议：**升级n8n到最新安全版本；临时措施：严格验证和净化XML输入、使用沙箱环境运行工作流、限制Webhook暴露；启用输入验证和WAF防护。

### Microsoft Defender 零日系列持续活跃利用

**CVSS 7.8~9.0**持续活跃利用

**受影响产品：**Microsoft Defender（本地权限提升相关漏洞，包括BlueHammer CVE-2026-33825等）。

**影响：**访问控制粒度不足，导致本地授权攻击者**权限提升**；多个Defender零日（BlueHammer、RedSun、UnDefend等）在野利用，部分仍待完全修补，整体可实现权限提升+持久化+侦察。

**热度原因：**4月中下旬至近期，研究者和威胁行为者公开/利用多个Defender零日PoC；CISA已将相关漏洞加入KEV；Defender作为默认端点保护工具，其自身漏洞易引发连锁反应，社区讨论热度持续。

**修复建议：**应用Microsoft最新累积更新（包括4月Patch Tuesday及后续紧急补丁）；隔离受影响系统、监控权限异常行为、使用EDR工具检测利用迹象；未打全补丁前考虑临时禁用部分Defender功能（风险自评估）。

### 其他近期KEV新增活跃利用漏洞

**SimpleHelp**（CVE-2024-57726 CVSS 9.9、CVE-2024-57728）：低权限用户可创建高权限API密钥或遍历文件，已在勒索软件/僵尸网络中使用，CISA要求**5月8日前**修补。

**Samsung MagicINFO 9 Server 路径遍历**（CVE-2024-7399）：已活跃利用。

**D-Link DIR-823X 命令注入**（CVE-2025-29635）：旧设备但利用活跃。

## 三、总体修复提醒

* **最高优先：**

  cPanel CVE-2026-41940（5月3日KEV截止，零日利用）和n8n RCE（立即打补丁）；Tenda路由器检查并隔离。
* **紧急行动：**

  cPanel用户立即应用4月28日补丁；检查KnownHost等托管商公告；SimpleHelp用户在5月8日前完成修补。
* **通用防护：**

  限制控制面板和物联网设备公网暴露；启用WAF/零信任；监控异常登录和权限行为；建议持续关注CISA KEV目录和厂商安全公告。

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
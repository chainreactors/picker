---
title: CISA 将 Cisco、Chromium V8、Fortinet 和 Citrix NetScaler 漏洞添加到其已知被利用漏洞目录中
url: https://mp.weixin.qq.com/s/2BJIlsWq8idNksSwsY86DQ
source: Doonsec's feed
date: 2026-09-11
fetch_date: 2026-09-12T06:46:55.056376
---

# CISA 将 Cisco、Chromium V8、Fortinet 和 Citrix NetScaler 漏洞添加到其已知被利用漏洞目录中

# CISA 将 Cisco、Chromium V8、Fortinet 和 Citrix NetScaler 漏洞添加到其已知被利用漏洞目录中

爱拍照的老李
爱拍照的老李

爱拍照的老李

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**导****读**

美国网络安全和基础设施安全局 (CISA) 将 Cisco、Google Chromium V8、Fortinet 和 Citrix NetScaler 的漏洞添加到其已知被利用漏洞目录中。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/PaFY6wibdwyLhhsbYySX8WiaxFvu7dNtYrn8onKg4Hflqh1M2Hp4KZ9CsLa2yYwv7GoAqphibibD4LBKm7lbA8mkkb0rh0dHGUXo6bkXvAqCGMs/640?wx_fmt=jpeg&from=appmsg)

美国网络安全与基础设施安全局（CISA）将以下漏洞新增至其已知被利用漏洞（KEV）目录：

CVE-2025-25249 Fortinet多款产品基于堆的缓冲区溢出漏洞

CVE-2026-19490 CitrixNetScaler存在通过替代路径或通道绕过身份验证的漏洞

CVE-2026-87491 谷歌Chromium V8越界写入漏洞

CVE-2026-20079 思科防火墙管理中心存在通过替代路径或通道绕过身份验证的漏洞

CVE-2026-20079（CVSS 评分为10.0）是一个身份验证绕过漏洞。该漏洞存在于思科安全防火墙管理器（Cisco Secure FMC）的网页界面中，未经过身份验证的远程攻击者可利用此漏洞绕过身份验证，发送特制的HTTP请求以执行脚本，从而有可能获得底层操作系统的root权限。

CVE-2026-87491（CVSS 评分为 8.8）CVE-2026-87491 是 2026 年第七个被主动利用的 Chrome 零日漏洞。该漏洞影响 V8——谷歌开源的高性能 JavaScript 和 WebAssembly 引擎，也是 Chrome 的 JavaScript 和 WebAssembly 引擎。攻击者可通过特制的 HTML 页面利用该越界写入漏洞，并在 Chrome 沙箱内执行任意代码。谷歌已在 Chrome 153.0.8010.36 及更高版本中修复了此问题。

“谷歌知道在野外存在针对 CVE-2026-87491 的漏洞利用程序。” 该安全公告中写道。

CVE-2025-25249（通用漏洞评分系统分值为8.1分）是存在于Fortinet FortiOS和FortiSwitchManager中的堆缓冲区溢出漏洞。该漏洞存在于cw\_acd守护进程中，未经身份验证的远程攻击者可通过发送特制数据包执行任意代码或命令。该漏洞目前正被野外广泛利用，包括针对已被攻陷的FortiGate设备部署PivotC2远程访问木马的攻击。

CVE-2026-19490（CVSS 评分为 9.3）是一处身份验证绕过漏洞。该漏洞影响 Citrix NetScaler ADC 和 NetScaler Gateway，允许未授权的远程攻击者通过 SAML HTTP 重定向绑定绕过身份验证，从而可能未经授权访问受保护的服务。该漏洞已被纳入美国网络安全与基础设施安全局（CISA）的已知被利用漏洞目录，表明其已在野外被主动利用。

根据《第22-01号约束性操作指令：降低已知被利用漏洞的重大风险》要求，联邦政府跨部门机构必须在截止日期前修复已识别的漏洞，以保护其网络免受利用目录中这些缺陷的攻击。

专家还建议私营组织审查目录并解决其基础设施中的漏洞。

美国网络安全与基础设施安全局（CISA）要求联邦机构在2026年9月22日前修复Windows系统的相关漏洞，其余漏洞则要求在2026年9月12日前解决。

新闻链接：

https://securityaffairs.com/198850/security/u-s-cisa-adds-cisco-google-chromium-v8-fortinet-and-citrix-netscaler-flaws-to-its-known-exploited-vulnerabilities-catalog.html

**![](https://mmbiz.qpic.cn/mmbiz_jpg/AnRWZJZfVaGC3gsJClsh4Fia0icylyBEnBywibdbkrLLzmpibfdnf5wNYzEUq2GpzfedMKUjlLJQ4uwxAFWLzHhPFQ/640?wx_fmt=jpeg)**

扫码关注

爱拍照的老李

**讲述普通人能听懂的安全故事**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz/AnRWZJZfVaF2RjjiaFU5rh9gjoyybDu9EvVnCYlqGSXDTZyuDbPbic33rGMe0dfB3HAicVkh6kdgo7T3OAOGwOtYw/0?wx_fmt=png)

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
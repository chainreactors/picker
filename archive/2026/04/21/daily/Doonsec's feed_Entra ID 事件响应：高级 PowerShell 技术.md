---
title: Entra ID 事件响应：高级 PowerShell 技术
url: https://mp.weixin.qq.com/s/6N0gL5PzKMFsAwKhBr5vpw
source: Doonsec's feed
date: 2026-04-21
fetch_date: 2026-04-22T04:40:24.806772
---

# Entra ID 事件响应：高级 PowerShell 技术

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/h4gtbB74nSjbkFWW7f4hRLuddibIMkmrehotO5AHibqDLYDPY8dGgFfko0HBhiap0uGZC34Fm0ujSu8Pwql5d39E2av23UCt2k7SibOfcHZtaKo/0?wx_fmt=jpeg)

# Entra ID 事件响应：高级 PowerShell 技术

cyberdom
cyberdom

securitainment

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

| 原文链接 | 作者 |
| --- | --- |
| https://cyberdom.blog/entra-id-incident-response-advanced-powershell-techniques/ | cyberdom |

Microsoft Entra ID 的 CFIR (云取证与事件响应) 为检测、调查和响应身份威胁提供了坚实的蓝图。然而，真正掌握这一体系，离不开合适的工具与正确的方法。PowerShell 正是在这里大显身手。

本文将深入探讨 PowerShell 如何赋能安全团队，充分发挥 Entra ID CFIR 的全部潜力。从自动化事件响应工作流，到识别入侵的细微迹象，PowerShell 脚本能够将繁杂的日志与告警转化为可操作的情报。

无论是资深安全专家，还是刚踏上身份防御之路的新手，这份实战指南都将助力安全团队打通理论与实践之间的壁垒，让 Entra ID CFIR 的实施更智能、更高效、更有力。

## Entra ID 事件响应矩阵

该矩阵专为使用 Microsoft Entra ID 的事件响应人员设计，提供结构化且实用的框架。它将常见的身份相关攻击场景与 MITRE ATT&CK 技术进行对应，帮助安全团队理解攻击者行为、识别日志来源，并开展有针对性的调查。

该矩阵具有多重用途：

* **将攻击映射至行业标准：**

  采用 MITRE ATT&CK 可确保团队与工具之间术语统一、理解一致。
* **明确调查重点：**

  针对每个事件场景，重点标注了用于揭露证据的关键 Entra ID 日志类型和数据来源。
* **指导检测与调查：**

  指出在上述日志中应关注哪些迹象、异常或规律。
* **支持自动化：**

  通过列出各场景所对应的 PowerShell 模块，引导事件响应人员使用有效的命令集以程序化方式采集和分析数据。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/h4gtbB74nSialCzEIDwpo9S91PykRpjJD7Go3Z2CGqtCObAs1yJ9Gh92AahNf1eYKLhSKNhH6y4sKv3icdAWGFjUtKSvNkJSXrSduTrRKJoo8/640?wx_fmt=png&from=appmsg)

## PowerShell IR

在 Entra ID 调查场景中，首选的 PowerShell 工具是 **Microsoft Entra PowerShell 模块**（`Microsoft.Entra`）。该模块专为 Entra ID 身份与访问管理数据交互而设计，提供最全面、最新的 cmdlet，可满足事件响应的各项需求。

以下是优先选择 Microsoft Entra PowerShell 模块的主要原因：

## Entra ID 事件响应矩阵

* 该模块可直接访问关键日志，包括登录日志、审计日志和角色分配，这些均是取证调查的核心数据。
* 它基于 Microsoft Graph API 构建，确保与 Entra ID 最新功能及安全数据完全兼容。
* 该模块支持细粒度的查询与过滤，可对可疑活动展开有针对性的调查，涵盖高风险登录、OAuth 授权许可、令牌盗窃及权限提升等场景。
* 该模块与事件响应和威胁狩猎的自动化脚本工作流无缝集成。
* 该模块替代了已弃用的 AzureAD 和 MSOnline 模块，与 Microsoft 当前及未来的技术路线图保持一致。

此外，若需访问更广泛的 Microsoft 365 审计数据，尤其是跨服务的统一审计日志，**Exchange Online PowerShell 模块**的 `Search-UnifiedAuditLog`cmdlet 依然极具价值，可作为 Entra ID 专项查询的有效补充。

如需进行现代化、灵活的 Graph API 访问，也可在 Entra 工作流中同时使用或嵌入 **Microsoft Graph PowerShell SDK**（`Microsoft.Graph`模块），尤其适用于高级场景。

**Detect-MultipleFailedSignins.ps1**脚本利用 Microsoft Graph 登录日志，检测多次登录失败后紧随其后出现的成功登录行为。

该脚本通过 Microsoft Graph 分析 Microsoft Entra ID (Azure AD) 登录日志，识别连续发生三次或三次以上登录失败、随后立即出现成功登录的用户。此类模式可能是账户遭到入侵或暴力破解攻击的迹象。

![](https://mmbiz.qpic.cn/mmbiz_png/h4gtbB74nSjsMu37mAGfpmfpgGnbZCA2FxERzEmlxj4t7b1w0ia8FrIiazSNyJ39Ar4GFnreLEyYkYBp4EicpMhSBQGBwq0C7lj9R35afmhib3Q/640?wx_fmt=png&from=appmsg)

---

Detect-NewCountrySignins.ps1 脚本分析过去 30 天的登录日志，并报告从新国家/地区登录的用户。

该脚本通过检测 Microsoft Entra ID 登录日志，识别用户从此前从未访问过的新国家/地区登录的情况。它分析过去 30 天内的成功登录记录，当用户最新的登录来源于其历史登录记录中未曾出现的国家/地区时，将自动发出警报。

![](https://mmbiz.qpic.cn/mmbiz_png/h4gtbB74nSjibOP9bZVDbjMLh4Dqd8VU08rsLNYRicpIqoRYGAG6ZsspK4L9QYzwxf3CaMQdaCFNtPfQvTuOgP5ggFPhaJw3Cicy4YIPG4UbQQ/640?wx_fmt=png&from=appmsg)

---

Get-SuspiciousOAuthConsents.ps1 脚本分析 Microsoft Entra ID 中的 OAuth 应用程序授权许可情况。

该脚本分析 Microsoft Entra ID 中的 OAuth 应用程序授权许可，识别潜在的可疑或未经授权的应用程序授权行为，帮助安全团队发现可能存在的基于 OAuth 的攻击——即用户可能已向恶意应用程序授予访问权限的情况。

![](https://mmbiz.qpic.cn/mmbiz_png/h4gtbB74nSiaPNFicl5bjDQSfHpgickMAJc2BWNj1VcbmZBUMtY5oFoYeCBzV47RNpqd4ule3nrWAL51iaqjB2Ob3ClcbO1WuguxRyACb7kpkek/640?wx_fmt=png&from=appmsg)

---

Get-SignInTimeline.ps1 脚本生成 Entra ID (Azure AD) 登录活动的完整时间线。

该脚本检索并分析 Microsoft Entra ID 登录日志，构建身份验证活动的详细时间线，为整个组织的登录模式提供全面视图，涵盖位置、设备、风险级别及身份验证方式等关键信息。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/h4gtbB74nShbNvjvDRqpHz46KiaWWFzPAGAK94ad89d53pibkiaiagvpdwoU3reQfJXeExkelqcaelsSYbAe4eHhMbJ2mS2ZnklVVsvqCcibiaTtM/640?wx_fmt=png&from=appmsg)

Detect-LegacyAuthSignIns.ps1 脚本识别 Microsoft Entra ID 中使用旧版身份验证协议的成功登录行为。

该脚本监控并检测 Microsoft Entra ID 中使用旧版身份验证协议的成功登录。旧版身份验证存在安全风险，因为它绕过了多重身份验证和条件访问策略等现代安全功能。

---

> 免责声明：本博客文章仅用于教育和研究目的。提供的所有技术和代码示例旨在帮助防御者理解攻击手法并提高安全态势。请勿使用此信息访问或干扰您不拥有或没有明确测试权限的系统。未经授权的使用可能违反法律和道德准则。作者对因应用所讨论概念而导致的任何误用或损害不承担任何责任。

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/hoiaQy7WhTCOSzVJlQkf89Vd656PRcKTQzzdNktnMJbmEYjZwfCOG7Y5qIwOvnIPVEPXAKzWb9D4t5SdUCy4gCg/0?wx_fmt=png)

securitainment

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/hoiaQy7WhTCOSzVJlQkf89Vd656PRcKTQzzdNktnMJbmEYjZwfCOG7Y5qIwOvnIPVEPXAKzWb9D4t5SdUCy4gCg/0?wx_fmt=png)

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
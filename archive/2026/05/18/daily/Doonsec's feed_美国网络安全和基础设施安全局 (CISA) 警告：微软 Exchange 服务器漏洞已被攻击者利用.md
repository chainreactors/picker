---
title: 美国网络安全和基础设施安全局 (CISA) 警告：微软 Exchange 服务器漏洞已被攻击者利用
url: https://mp.weixin.qq.com/s/grRRPmFUY6TLDIWEHeJdaA
source: Doonsec's feed
date: 2026-05-18
fetch_date: 2026-05-19T06:01:10.154115
---

# 美国网络安全和基础设施安全局 (CISA) 警告：微软 Exchange 服务器漏洞已被攻击者利用

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BicXBAdicJy7O36b13lHLEXDfmdHhcvt2XreibicIdR24MpaLc7aNXC5cky9YVUjDUYKl8FibiaW79ZWibqgtBa7ypy3Kdpic2ibpZGsQFPNMEJK7iak8/0?wx_fmt=jpeg)

# 美国网络安全和基础设施安全局 (CISA) 警告：微软 Exchange 服务器漏洞已被攻击者利用

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

美国网络安全和基础设施安全局 (CISA) 就新披露的 Microsoft Exchange Server 漏洞发出新的警告，该漏洞已在现实世界的攻击中被利用，这引起了依赖本地电子邮件基础设施的组织的担忧。

漏洞CVE-2026-42897 是一个跨站脚本 (XSS) 漏洞，会 影响 Microsoft Exchange Server，特别是 Outlook Web Access (OWA) 中的漏洞。

根据官方公告，该问题发生在网页生成过程中。在某些交互条件下，该问题可能会被触发，从而允许攻击者在受害者的浏览器中执行任意 JavaScript 代码。

该漏洞已于 2026 年 5 月 15 日被添加到 CISA 的已知利用漏洞 (KEV) 目录中，表明已确认该漏洞在实际环境中被积极利用。

遵循约束性操作指令 (BOD) 22-01 的联邦机构和组织必须在 2026 年 5 月 29 日之前解决该问题。

## **微软 Exchange Server 漏洞利用**

安全研究人员指出，Exchange 等企业电子邮件平台中的 XSS 漏洞尤其危险，因为它们可以被利用来劫持已认证的会话。

在实践中，攻击者可以诱骗用户点击精心构造的链接，从而在用户的浏览器会话中执行恶意脚本。

这可能导致凭证被盗、邮箱被访问或进一步的内部安全受到威胁。

尽管微软尚未公开将该漏洞与勒索软件活动联系起来，但CISA将该漏洞纳入KEV目录强烈表明威胁行为者对此表现出浓厚的兴趣。

由于 Exchange 服务器在处理敏感通信和凭证方面发挥着重要作用，因此它们历来都是攻击者的高价值目标。

该漏洞属于 CWE-79 类，这是一类众所周知的 Web 安全漏洞，涉及在网页生成过程中对输入进行不适当的中和处理。

尽管 XSS 是一种常见的漏洞类型，但由于输入验证不一致和 Web 应用程序行为复杂，它仍然被广泛利用。

CISA敦促各组织立即应用供应商提供的缓解措施和安全更新。

如果补丁尚未发布或无法应用，建议各机构遵循微软概述的其他缓解策略，或考虑停止使用受影响的系统，直到这些系统得到安全保护。

安全团队还应监控 Exchange 服务器日志，以发现可疑活动，包括异常的身份验证模式、意外的脚本执行或Outlook Web Access 会话中的异常用户行为。

最新警告凸显了一个更广泛的趋势，即攻击者正积极针对企业协作工具，尤其是那些暴露在互联网上的工具。

由于 Exchange Server 仍在企业中广泛部署，未修补的漏洞可能很快成为更深层次网络入侵的入口。

强烈建议各组织优先考虑修补漏洞，并审查其面向互联网的 Exchange 服务，以降低被利用的风险。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKJ7zaD2SCDB9F4cHqDTEwJ6wULzhqNKntCMGN2NHYIx7TEicwiaxRTcQaBahVjqwpL96mEw0LBVMRAA/0?wx_fmt=png)

安全圈的那点事儿

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKJ7zaD2SCDB9F4cHqDTEwJ6wULzhqNKntCMGN2NHYIx7TEicwiaxRTcQaBahVjqwpL96mEw0LBVMRAA/0?wx_fmt=png)

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
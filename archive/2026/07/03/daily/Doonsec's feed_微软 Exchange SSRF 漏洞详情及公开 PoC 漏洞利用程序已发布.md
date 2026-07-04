---
title: 微软 Exchange SSRF 漏洞详情及公开 PoC 漏洞利用程序已发布
url: https://mp.weixin.qq.com/s/Lewk8FZcrFv4umdbw1W_kw
source: Doonsec's feed
date: 2026-07-03
fetch_date: 2026-07-04T05:40:28.884118
---

# 微软 Exchange SSRF 漏洞详情及公开 PoC 漏洞利用程序已发布

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/BicXBAdicJy7MiasKZbpS3icIRzUmqxBciaSBRenOgRjGnbcyMtNsclibwlm4M39gq8UBRWMsyFMaPmdEu0vWPXNgicALZFRHEVbaNqqRCZodibeQns/0?wx_fmt=jpeg)

# 微软 Exchange SSRF 漏洞详情及公开 PoC 漏洞利用程序已发布

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

HawkTrace 的安全研究人员披露了 Microsoft Exchange 中一个高危服务器端请求伪造 (SSRF) 漏洞的技术细节，该漏洞的跟踪编号为 CVE-2026-45504。

该漏洞的 CVSS 评分为 8.8，允许经过身份验证的低权限用户从易受攻击的 Exchange 服务器读取任意文件，这给依赖本地部署的企业带来了严重的担忧。

Microsoft Exchange 被广泛用于企业电子邮件、日历和协作。由于它在处理敏感通信方面发挥着核心作用，因此任何允许未经授权访问数据的漏洞都可能造成重大影响。

在这种情况下，问题在于 Exchange 在附件预览期间以及与 SharePoint 服务集成时如何处理外部 URL。

根据 HawkTrace 的分析，该漏洞源自 OneDriveProUtilities 组件，具体存在于 TryTwice 和 GetWacUrl 等函数中。

这些函数发出 HTTP 请求以检索WOPI（Web 应用程序开放平台接口）数据和文档预览的访问令牌。

## **Exchange SSRF 漏洞已公开 PoC 漏洞利用**

核心问题是用户控制的输入未经充分验证就直接传递给了 WebRequest.CreateHttp。

攻击始于经过身份验证的用户使用Exchange Web Services (EWS)创建特制的引用附件。

此附件包含一个指向攻击者控制服务器的 ProviderEndpointUrl。当受害者访问或预览此附件时，Exchange 服务器会向攻击者的服务器发起后端请求，以检索 WOPI 元数据。

攻击者随后会返回一个恶意的 WebApplicationUrl 值。该响应不会返回标准的 HTTP 或 HTTPS URL，而是包含一个文件 URI，例如 file:///C:/Windows/win.ini。

通常情况下，Exchange 添加的额外查询参数会破坏文件路径。然而，研究人员演示了一种使用片段字符 (#) 的简单绕过方法。

通过返回类似 file:///C:/Windows/win.ini# 的有效负载，可以忽略片段之后附加的所有内容，从而使系统能够正确处理本地文件路径。

因此，Exchange 在不知情的情况下向本地文件系统执行 FileWebRequest 请求，并将文件内容返回给攻击者。

这实际上将 SSRF 漏洞变成了任意文件读取原理，从而可以访问敏感的系统文件，例如配置数据、凭据和内部服务信息。

问题的根本原因是 WOPI 端点返回的 URL 缺少协议验证。Exchange 信任响应，并且没有限制诸如 file:// 之类的非 HTTP 协议，而这些协议在这种情况下是绝对不允许的。

这种信任边界违规行为使攻击者能够从受控的外部请求转向内部文件访问。

HawkTrace 还在GitHub 上发布了一个公开的概念验证 (PoC) 漏洞利用程序，演示了如何在实际场景中利用该漏洞。

PoC 通过设置恶意服务器、向 Exchange 进行身份验证并请求任意文件（例如系统 hosts 文件）来自动执行此过程。

此次披露凸显了复杂企业软件中与SSRF漏洞相关的持续风险。即使需要身份验证，低权限访问加上不正确的输入验证也可能导致重大数据泄露。

为缓解此问题，各组织应应用微软提供的安全更新，并限制 Exchange 服务器向不受信任的端点发出出站请求。

对 URL 方案进行正确验证，特别是阻止 file:// 和类似协议，对于防止漏洞利用至关重要。

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
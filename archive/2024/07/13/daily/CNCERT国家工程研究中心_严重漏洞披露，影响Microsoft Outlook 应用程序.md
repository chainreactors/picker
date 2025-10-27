---
title: 严重漏洞披露，影响Microsoft Outlook 应用程序
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247545830&idx=3&sn=7afd7f19afbfb2fe3fec0538fafc4127&chksm=fa938527cde40c318a0e9cfabe671a96083f396ab3cc529b0bad0368159bb2d2737e6e36f22e&scene=58&subscene=0#rd
source: CNCERT国家工程研究中心
date: 2024-07-13
fetch_date: 2025-10-06T17:43:41.982925
---

# 严重漏洞披露，影响Microsoft Outlook 应用程序

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176nqbSSxR1qo9Y4e5L2EyiasqAtIKNP7iapL0UhP1dO3e6b25Bgg3QWL8aYCOFIiagkoMlwBYhkVzAJGg/0?wx_fmt=jpeg)

# 严重漏洞披露，影响Microsoft Outlook 应用程序

网络安全应急技术国家工程中心

安全研究人员发现了一个严重漏洞 CVE-2024-38021，该漏洞影响大多数 Microsoft Outlook 应用程序。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/QmbJGbR2j6yBERDWREPLRfvyULWJsyu7QM2ibX5Miczs5l7TQtTDlvEib2V5398SvKjPtGIJbegpE4QPUAnGG1VZw/640?wx_fmt=jpeg&from=appmsg&wxfrom=13)

该零点击远程代码执行 (RCE) 漏洞现已被 Microsoft 修补，并且不需要任何身份验证，这与之前发现的 CVE-2024-30103 不同，后者至少需要 NTLM 令牌。

如果被利用，CVE-2024-38021 可能会导致数据泄露、未经授权的访问和其他恶意活动。微软已将此漏洞评为“重要”，并指出了可信和不可信发件人之间的区别。

对于受信任的发件人来说，该漏洞是零点击的，但对于不受信任的发件人，则需要一键用户交互。

Morphisec 发现了该漏洞，并于 7 月 9 日发布了相关公告，他敦促微软将该漏洞重新归类为“严重”，以反映更高的估计风险并确保采取足够的缓解措施。

该安全公司同意微软的观点，认为此 RCE 比 CVE-2024-30103 更复杂，因此不太可能立即利用。但是，将其与另一个漏洞结合起来可以简化攻击。

事件时间线始于 2024 年 4 月 21 日，当时 Morphisec 向微软报告了该漏洞。该漏洞于 2024 年 4 月 26 日得到确认，并于 2024 年 7 月 9 日由微软作为补丁星期二更新的一部分进行了修补。

为了降低风险，务必使用最新补丁更新所有 Microsoft Outlook 和 Office 应用程序。此外，实施强大的电子邮件安全措施（例如禁用自动电子邮件预览和教育用户了解打开来自未知来源的电子邮件的风险）也至关重要。

此外，Morphisec 表示，通过 EDR 和自动移动目标防御 (AMTD) 确保整个安全堆栈的全面覆盖将进一步降低风险并提供针对已知和未知攻击的端点保证。

原文来源：E安全

“投稿联系方式：010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176n1NvL0JsVSB8lNDX2FCGZjW0HGfDVnFao65ic4fx6Rv4qylYEAbia4AU3V2Zz801UlicBcLeZ6gS6tg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mrRug7icLIhX4EvNQjNgGRibia7K9qOLTR5PDfQiaUesU9xge7pnF8iciaxVC3JVkNqHA2pvQDnrM0hDVQ/0?wx_fmt=png)

网络安全应急技术国家工程中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mrRug7icLIhX4EvNQjNgGRibia7K9qOLTR5PDfQiaUesU9xge7pnF8iciaxVC3JVkNqHA2pvQDnrM0hDVQ/0?wx_fmt=png)

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
---
title: 影响 300 万款苹果 iOS / macOS 应用，CocoaPods 平台漏洞披露
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247545731&idx=2&sn=e2bc79fca8c76db4162bae1b4ffd26c4&chksm=fa938542cde40c54f53688c64def68778dfe9ec56dae030498f6f9fb8d9d15197283675a4ff0&scene=58&subscene=0#rd
source: CNCERT国家工程研究中心
date: 2024-07-09
fetch_date: 2025-10-06T17:46:14.503601
---

# 影响 300 万款苹果 iOS / macOS 应用，CocoaPods 平台漏洞披露

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176m3VIeoMC11ImHuNLddiaSV2v4rCHY8wUqPSg37Cich6sePEXRPQ6ZzAYtZ9fTwOkrFicG2XfhjbFCoA/0?wx_fmt=jpeg)

# 影响 300 万款苹果 iOS / macOS 应用，CocoaPods 平台漏洞披露

网络安全应急技术国家工程中心

最近，Objective-C 和 Swift 的著名依赖管理器 CocoaPods 的关键漏洞被曝光，使数百万 macOS 和 iOS 设备上的应用程序面临供应链攻击风险，可能会对一些苹果用户造成伤害。

![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3ibxXCMBvobgCKmWuAOBcoCWHB2Uvd2mvWQoJ6a4XrygyJ6N5YXuWPUh9zSNVXWhtED1fyU5OLpyXA/640?wx_fmt=jpeg&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

问题出现在 CocoaPods 迁移到 Trunk 服务器时，导致数千个软件包无人认领，攻击者可以利用公共 API 获取 pod 和 CocoaPods 源代码中的电子邮件地址。（CocoaPods 被广泛用于管理 macOS 和 iOS 开发中的第三方库，可以自动化集成和解析，是一个广受欢迎的省时工具，因此被利用的风险很大。）

然而，这些无人认领的软件包被暴露了近十年，直到 2023 年 10 月才被修补。

Trunk 服务器作为 CocoaPods 基础设施的重要组成部分，负责管理 CocoaPods 库文件的分发和托管，对于库的版本控制、用户验证和发布流程至关重要。相关的安全问题可能会损害 CocoaPods 库的完整性，使攻击者能够向流行的数据包中注入有害代码。

发现的关键漏洞包括：

* CVE-2024-38366 (CVSS 10.0)，该漏洞影响电子邮件验证工作流程，可在 Trunk 服务器上执行任意代码。因此，合法软件包可能会被篡改或替换，给用户带来重大风险。
* CVE-2024-38368 (CVSS 9.3) ，该漏洞利用了「认领 Pods」功能，攻击者可以控制无人认领的软件包。这反过来又可以篡改源代码，对流行的应用程序进行未经批准的修改。
* CVE-2024-38367 (CVSS 8.2)，该漏洞也涉及电子邮件验证，其中潜在的良性链接允许攻击者将用户重定向到恶意域，从而导致账户面临被接管或令牌被盗的风险。

由于许多流行应用程序都依赖于 CocoaPods，此类漏洞威胁到整个 iOS 和 macOS 生态系统。利用这些漏洞的攻击者可以向合法应用程序注入恶意代码，通过可信渠道分发恶意软件，并破坏用户数据。

虽然 CocoaPods 已经修补了这些漏洞，但有关这些漏洞如何被利用的细节尚未澄清。开发人员已被敦促审查安全实践并更新依赖项，以降低未来再次被利用的风险。

据了解，这并不是 CocoaPods 第一次受到审查。2023 年初，安全研究人员发现了一个允许攻击者劫持子域的漏洞。最近发现的漏洞强调了依赖管理器和软件开发中安全性的重要性，安全研究人员需要积极主动地应对可能影响用户数据和应用程序的潜在漏洞。

**参考资料：**
https://www.spiceworks.com/it-security/endpoint-security/news/critical-cocoapods-vulnerability-macos-ios-apps-supply-chain-attacks/

原文来源：FreeBuf

“投稿联系方式：010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176n1NvL0JsVSB8lNDX2FCGZjW0HGfDVnFao65ic4fx6Rv4qylYEAbia4AU3V2Zz801UlicBcLeZ6gS6tg/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

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
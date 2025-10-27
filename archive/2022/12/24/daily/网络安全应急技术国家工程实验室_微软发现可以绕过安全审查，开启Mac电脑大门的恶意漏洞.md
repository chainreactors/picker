---
title: 微软发现可以绕过安全审查，开启Mac电脑大门的恶意漏洞
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247533470&idx=3&sn=f63b902421452faf93a29151d0aa018b&chksm=fa93f55fcde47c490f3bf02a6545daa5f0c593d614deb358da2ffc6e89bd8303b5a5cddfa3a1&scene=58&subscene=0#rd
source: 网络安全应急技术国家工程实验室
date: 2022-12-24
fetch_date: 2025-10-04T02:26:13.846512
---

# 微软发现可以绕过安全审查，开启Mac电脑大门的恶意漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176nq1AmeUibe5dWiat6g4Eu31UHgdNLfxA7famRsT2frUdnRggMRIV6CmrDbNwtYr0RuehCHC93h96JQ/0?wx_fmt=jpeg)

# 微软发现可以绕过安全审查，开启Mac电脑大门的恶意漏洞

网络安全应急技术国家工程中心

**摘要：**微软发现编号CVE-2022-42821的“Achilles”漏洞，能让攻击者绕过苹果Gatekeeper安全机制，而在Mac电脑上执行恶意应用程序，建议Mac电脑用户更新作业系统至macOS Monterey 12.6.2、macOS Big Sur 11.7.2及macOS Ventura 13以完成修补。

![](https://mmbiz.qpic.cn/mmbiz_png/QmbJGbR2j6yrMqPsXuHEpfoGqvSKdg9jBia1hFzbkd8kRib9jMgJVZ4vzxdvWXYzJjL6XsXhtE4aTUSavzko9Esw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

微软安全威胁情报小组（Microsoft Security Threat Intelligence）发现macOS有项漏洞，能让攻击者绕过Gatekeeper安全机制，而在Mac电脑上执行恶意应用程序。苹果已经释出新版macOS作业系统予以修补。

据悉，微软是在7月发现编号CVE-2022-42821的漏洞，它可使用应用程序绕过macOS Gatekeeper提供的应用执行限制。Gatekeeper功能是确保只有受信赖的应用程序可以在Mac装置上执行。本漏洞可为恶意程序开启Mac电脑大门，再协助提升攻击活动成功率。微软也将此漏洞为“Achilles”。

微软解释，Gatekeeper会检查所有从网络下载的应用程序，确认应用程序是否具备（苹果核准的）开发人员签章以及经过苹果公证，应用程序必须通过检查才能开启，否则Gatekeeper就会封锁应用程序执行并通知使用者（如下图所示）。

![](https://mmbiz.qpic.cn/mmbiz_png/QmbJGbR2j6yrMqPsXuHEpfoGqvSKdg9jS1bicdTic0GTrzHWWTmwvCDTznXITtYYTvSQMNwFrSkDUub7dCcDXRibA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

Gatekeeper的作业原理是检查苹果浏览器Safari在应用程序下载时赋予的扩充属性，其中com.apple.quarantine储存下载档案来源资讯，以及提供Gatekeeper处理档案的指示。

研究人员发现，透过设定非常严格的存取控制清单（Access Control List，ACL），可使Safari（或其他应用程序）无法设定扩充属性，包括Gatekeeper相关的com.apple.quarantine。结果就能使Gatekeeper无法在用户从网络下载执行恶意程序时发挥把关的作用。

研究人员并在概念验证中设计了滥用这项漏洞的方法，建立假路径及储存经改造的ACL的假AppleDouble档案，成功使Gatekeeper使用了这个档案，因而造成了Gatekeeper绕过的结果。

这项漏洞影响macOS 12 Monterey、macOS 11 Big Sur等版本。经过微软通报，苹果已经释出macOS Monterey 12.6.2、macOS Big Sur 11.7.2及macOS Ventura 13解决漏洞。

微软并提醒，macOS的安全功能封闭模式（Lockdown Mode）无法防范Achilles漏洞攻击。这功能是Ventura以后加入，用于保护特定高风险人士可能遭国家或进阶黑客执行零点击远端程序码攻击。微软呼吁Mac电脑用户，不论是否开启封闭模式都必须安装更新。

原文来源：E安全

“投稿联系方式：010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176n1NvL0JsVSB8lNDX2FCGZjW0HGfDVnFao65ic4fx6Rv4qylYEAbia4AU3V2Zz801UlicBcLeZ6gS6tg/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

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
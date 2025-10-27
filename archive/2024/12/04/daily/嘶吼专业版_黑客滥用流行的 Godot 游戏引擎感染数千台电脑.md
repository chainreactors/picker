---
title: 黑客滥用流行的 Godot 游戏引擎感染数千台电脑
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247580048&idx=2&sn=e05509c65eae9352cc6b8c92744366ba&chksm=e91469aade63e0bc17fec18ae5e3baf4ef115ff82ae81bbc919874ff833cc0ecaa66d44e2a6c&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2024-12-04
fetch_date: 2025-10-06T19:39:15.172764
---

# 黑客滥用流行的 Godot 游戏引擎感染数千台电脑

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2icIdkO0eXJMTRtvibI8qV1iag3w5sdOic4Xnm0zmALVY7kbAU7ev9NtfhGAsZic4xpJaicK6S3sG9FYyHA/0?wx_fmt=jpeg)

# 黑客滥用流行的 Godot 游戏引擎感染数千台电脑

胡金鱼

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

黑客利用新的 GodLoader 恶意软件，广泛使用 Godot 游戏引擎功能，在短短三个月内逃避检测并感染了 17,000 多个系统。

Check Point Research 在调查攻击时发现，威胁者可以使用此恶意软件加载程序来针对所有主要平台（包括 Windows、macOS、Linux、Android 和 iOS）的游戏玩家。它还利用 Godot 的灵活性及其 GDScript 脚本语言功能来执行任意代码，并使用游戏引擎 .pck 文件（打包游戏资产）绕过检测系统来嵌入有害脚本。

一旦加载，恶意制作的文件就会触发受害者设备上的恶意代码，使攻击者能够窃取凭据或下载其他有效负载，包括 XMRig 加密矿工。

该矿工恶意软件的配置托管在 5 月份上传的私人 Pastebin 文件中，该文件在整个活动期间被访问了 206,913 次。

至少自 2024 年 6 月 29 日起，网络犯罪分子一直在利用 Godot Engine 执行精心设计的 GDScript 代码，从而触发恶意命令并传播恶意软件。VirusTotal 上的大多数防病毒工具仍未检测到这种技术，可能仅在短短的时间内就感染了超过 17,000 台计算机。

Godot 拥有一个充满活力且不断发展的开发者社区，他们重视其开源性质和强大的功能。超过 2,700 名开发者为 Godot 游戏引擎做出了贡献，而在 Discord、YouTube 和其他社交媒体平台等平台上，Godot 引擎拥有大约 80,000 名关注者，他们可以随时了解最新消息。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icIdkO0eXJMTRtvibI8qV1iagNIxDMxL2MQDZET7ysI5ibvJFmjU0LkHO0ibhcdD9VctUAOXeKscCY4Gg/640?wx_fmt=png&from=appmsg)

攻击链

攻击者通过 Stargazers Ghost Network 传播 GodLoader 恶意软件，这是一种恶意软件分发即服务 (DaaS)，使用看似合法的 GitHub 存储库掩盖其活动。

2024 年 9 月至 10 月期间，他们使用由超过 225 个 Stargazer Ghost 帐户控制的 200 多个存储库，将恶意软件部署到目标系统，利用潜在受害者对开源平台和看似合法的软件存储库的信任。

在整个活动过程中，Check Point 在 9 月 12 日至 10 月 3 日期间检测到针对开发人员和游戏玩家的四次独立攻击浪潮，诱使他们下载受感染的工具和游戏。

虽然安全研究人员只发现了针对 Windows 系统的 GodLoader 样本，但他们还开发了 GDScript 概念验证漏洞利用代码，展示了恶意软件如何轻松地用于攻击 Linux 和 macOS 系统。

Stargazer Goblin 是这些攻击中使用的 Stargazers Ghost Network DaaS 平台背后的恶意分子，Check Point 于 2023 年 6 月首次观察到在暗网上推广此恶意软件分发服务。但是，它可能至少从 2022 年 8 月起就一直活跃，自这项服务推出以来，收入超过 100,000 美元。

Stargazers Ghost Network 使用 3,000 多个 GitHub“ghost”帐户创建了数百个存储库的网络，这些存储库可用于传播恶意软件（主要是 RedLine、Lumma Stealer、Rhadamanthys、RisePro 和 Atlantida Stealer 等信息窃取程序）以及 star、fork 和订阅这些恶意代码库，将它们推送到 GitHub 的趋势部分并增加其明显的合法性。

随后，Godot Engine 维护者和安全团队成员发送声明说：“该漏洞并非 Godot 特有。Godot Engine 是一个带有脚本语言的编程系统。例如，它类似于 Python 和 Ruby 运行时，用任何编程语言都可以编写恶意程序。”

Godot 不为“.pck”文件注册文件处理程序。这意味着恶意分子始终必须将 Godot 运行时与 .pck 文件一起发送。用户始终必须将运行时与 .pck 一起解压到同一位置，然后执行运行时。除非存在其他操作系统级漏洞，否则恶意分子无法创建“一键漏洞利用”。如果使用这样的操作系统级漏洞，那么由于运行时的大小，Godot 将不是一个特别有吸引力的选择。这类似于用 Python 或 Ruby 编写恶意软件，恶意分子必须将 python.exe 或 ruby.exe 与其恶意程序一起发送。

参考及来源：https://www.bleepingcomputer.com/news/security/new-godloader-malware-infects-thousands-of-gamers-using-godot-scripts/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icIdkO0eXJMTRtvibI8qV1iagdIXbHaH2F8q1p7RVcx6IB67Nc3tbyLaKDh8tgR25L4sjtjDLYndrVw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icIdkO0eXJMTRtvibI8qV1iagAU3KTOlloV0xAKpvsict667JrbeRmVwOXemrN0riaAocRrupib02YzsicA/640?wx_fmt=png&from=appmsg)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

嘶吼专业版

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

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
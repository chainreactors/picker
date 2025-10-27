---
title: 警惕：OTP被绕过！大规模短信窃取活动感染了113个国家的Android设备
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247546121&idx=2&sn=a464dacc2cd14677dfbd2d00d240ce5e&chksm=fa9383c8cde40ade93011f450adaf18bc57adcb0aa68b1f0f547172c94f756bdad9a3e201bfb&scene=58&subscene=0#rd
source: CNCERT国家工程研究中心
date: 2024-08-01
fetch_date: 2025-10-06T18:05:59.281703
---

# 警惕：OTP被绕过！大规模短信窃取活动感染了113个国家的Android设备

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176nOibnP9AsqErf6zoibLYbeJkIJo8zibyHNcy6734nVIBBQPQELC6HZ770mxx8woc0n2liak1hJZAl2zQ/0?wx_fmt=jpeg)

# 警惕：OTP被绕过！大规模短信窃取活动感染了113个国家的Android设备

网络安全应急技术国家工程中心

全球移动设备和应用安全知名企业Zimperium, Inc.于7月29日发布最新研究报告，称其发现了一个针对Android设备的大规模短信窃取活动，该活动自2022年2月以来已发现超过10.7万个恶意软件样本，针对113个国家的不同行业安卓用户开展了针对性攻击活动。该公司的安全实验室zLabs团队的研究表明，攻击者不断改进技术以绕过一次性口令（OTP）等安全措施，对企业和个人用户构成重大威胁。这些恶意软件不仅窃取短信，还能盗取敏感信息，包括OTP，为进一步的网络钓鱼和社会工程攻击提供便利。报告强调了企业需要强大的移动安全解决方案，以抵御恶意软件的侵害，并提高对潜在威胁的可见性。同时，解决这一挑战还需要多层次的方法，包括先进的检测技术、用户教育和意识提升。

![](https://mmbiz.qpic.cn/mmbiz_jpg/0KRmt3K30icXE7bp4Rke1Agk8icZutTyFNAZtN7FG93BC7ich8wHu7aeou655ewhpAbibR14S9yDxoP2nbqticuoyWQ/640?wx_fmt=jpeg&from=appmsg&wxfrom=13&tp=wxpic)

Zimperium的研究人员发现了这一行动，并自 2022 年 2 月以来一直在追踪它。他们报告说，发现了至少 107,000 个与该活动相关的不同的恶意软件样本。

这项针对全球Android设备的恶意活动利用数千个 Telegram 机器人来感染设备以窃取短信的恶意软件，并窃取600多种服务的一次性2FA口令 (OTP)。

网络犯罪分子的动机是经济利益，很可能使用受感染的设备作为身份验证和匿名中继。

恶意活动规模

![](https://mmbiz.qpic.cn/mmbiz_png/0KRmt3K30icXE7bp4Rke1Agk8icZutTyFNIAIYSEWibLCqazm0R3avibyGJGHvicUPuPyeQTqsicfOa2mJ4ZKrsz4biag/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

![](https://mmbiz.qpic.cn/mmbiz_png/0KRmt3K30icXE7bp4Rke1Agk8icZutTyFNd63oZxnVw6LwVZURBoicdJGyTpdaIeyfARRPUPxb4SoW6LsFN3YIAMg/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

感染过程

感染目标设备共有一个阶段，各个步骤协同配合。

![](https://mmbiz.qpic.cn/mmbiz_jpg/0KRmt3K30icXE7bp4Rke1Agk8icZutTyFNibyA2SDhUaaVqIl1ayib9OicL3ZNuITYFO680FkjejRYtOibtOiacSh6b9w/640?wx_fmt=jpeg&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

![](https://mmbiz.qpic.cn/mmbiz_png/0KRmt3K30icXE7bp4Rke1Agk8icZutTyFNRhq60YNLhv5Hdicc1iaPYYibMGo0nEKs150Kw1ficGwyzxIEYBgRn3mgicw/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

Telegram诱捕

短信窃取程序通过恶意广告或自动与受害者通信的Telegram机器人进行分发。

在第一种情况下，受害者会被引导至模仿Google Play的页面，报告夸大的下载次数以增加合法性并创造虚假的信任感。

在 Telegram上，机器人承诺向用户提供适用于 Android平台的盗版应用程序，并在用户分享APK文件之前要求用户提供电话号码。

Telegram 器人使用该号码生成新的APK，从而实现个性化跟踪或未来的攻击。

![](https://mmbiz.qpic.cn/mmbiz_jpg/0KRmt3K30icXE7bp4Rke1Agk8icZutTyFNXtFHlOTOEbsib3QfDw4sms4CjCfGpb96IbeYwgMiciaiaXMB7fEcdMy00A/640?wx_fmt=jpeg&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

Telegram机器人向受害者发送短信窃取程序来源：Zimperium

Zimperium表示，该行动使用2,600个Telegram机器人来推广各种Android APK，这些 APK由 13 个命令和控制 (C2) 服务器控制。

此次攻击活动的受害者主要位于印度和俄罗斯，巴西、墨西哥和美国的受害者数量也相当可观。

赚取经济回报

虽然研究者无法确定此次攻击活动背后的确切动机，但根据他我们的研究，研究者确实知道其中存在经济利益考量。研究者观测到一些平台，这些平台接受各种付款方式，包括加密货币，这是网络犯罪分子常用的一种隐藏用户身份的方法。

Zimperium发现该恶意软件将捕获的 SMS 消息传输到网站“fastsms.su”的特定API 端点。

该网站允许访问者购买外国“虚拟”电话号码，用于匿名化以及对在线平台和服务进行身份验证。

![](https://mmbiz.qpic.cn/mmbiz_jpg/0KRmt3K30icXE7bp4Rke1Agk8icZutTyFNJuOUPbHCeXm6CyhxiblF9r62NfkZSuxQuwPibSKiaGgq7um4UrUaicfVCQ/640?wx_fmt=jpeg&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)
快速短信网站

来源：BleepingComputer

受感染的设备很可能在受害者不知情的情况下被该服务主动使用。

请求的Android SMS 问权限允许恶意软件捕获帐户注册和双因素身份验证所需的 OTP。
![](https://mmbiz.qpic.cn/mmbiz_jpg/0KRmt3K30icXE7bp4Rke1Agk8icZutTyFNQMwXZWoWmYbHGuS3a6Ob6Lj4R96GuaysXRLwEAEAicTXcUbNficQu1hA/640?wx_fmt=jpeg&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

恶意软件将短信泄露到Fast SMS站点

来源：Zimperium

BleepingComputer系Fast SMS服务询问Zimperium 调查结果，但截至本文发表尚未收到回复。对于受害者来说，这可能会导致他们的移动账户产生未经授权的费用，同时他们还可能涉嫌通过其设备和号码进行非法活动。

结论及建议

Zimperium 的研究团队认为，移动恶意软件的泛滥和数据窃取的便利性，如短信和一次性口令（OTP），对个人和组织构成了重大威胁。研究团队发现了大量的恶意软件样本和多种感染媒介，表明威胁形势复杂且不断演变。恶意应用程序窃取敏感信息，包括OTP，突显了对强大企业移动安全解决方案的迫切需求。被盗凭证可能被用作进一步欺诈活动的起点，例如创建虚假账户进行网络钓鱼或社会工程攻击。

研究团队给出了三点建议，一是需要采取多层次的方法来解决移动安全问题，包括先进的检测技术和用户教育。二是企业需要实施强大的移动安全解决方案，以保护自身免受恶意软件和网站的侵害，并提高对潜在威胁的可见性。三是强化用户对移动安全的认识和教育，以提高整体的网络安全防护水平。

关于Zimperium

Zimperium, Inc. 作为全球移动设备和应用安全的领导者，致力于提供实时的设备保护，以应对Android、iOS和Chromebook设备上的已知和未知威胁。公司成立之初，就意识到传统的终端安全技术已不足以应对日益严峻的移动安全挑战。因此，Zimperium团队创新性地开发了基于机器学习的z9引擎，这一技术突破使得移动设备能够免受设备、网络、网络钓鱼和应用程序攻击的侵害。z9引擎的卓越之处在于其能够检测100%的零日移动漏洞，且无需依赖更新，避免了基于云的检测可能带来的延迟和限制，这是其他移动安全供应商所无法比拟的。Zimperium的这一创新不仅重新定义了移动安全，也为移动设备用户提供了一个更为安全和可靠的保护环境。

**参考资源：**

1.https://www.zimperium.com/blog/unmasking-the-sms-stealer-targeting-several-countries-with-deceptive-apps/

2.https://www.bleepingcomputer.com/news/security/massive-sms-stealer-campaign-infects-android-devices-in-113-countries/

原文来源：网空闲话plus

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
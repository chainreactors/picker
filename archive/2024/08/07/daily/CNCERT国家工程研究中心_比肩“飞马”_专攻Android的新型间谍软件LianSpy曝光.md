---
title: 比肩“飞马”:专攻Android的新型间谍软件LianSpy曝光
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247546220&idx=3&sn=f106be1865368716f6743b0b68ebf827&chksm=fa9383adcde40abba89cfc53b1e4f4b10ecf99ba9f089acdf2eec74b4e60d5ffc79f6ea23104&scene=58&subscene=0#rd
source: CNCERT国家工程研究中心
date: 2024-08-07
fetch_date: 2025-10-06T18:04:50.962104
---

# 比肩“飞马”:专攻Android的新型间谍软件LianSpy曝光

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176lsPeECN1yxChvqJWdrXMNPgsbsNz9ktqku3mA4h1D3gIPWerbnb2ywx0Cl6NtpcHluOStjkF6AUg/0?wx_fmt=jpeg)

# 比肩“飞马”:专攻Android的新型间谍软件LianSpy曝光

网络安全应急技术国家工程中心

俄罗斯网络安全公司卡巴斯基研究人员发现了一种之前从未见过的间谍软件，该软件针对俄罗斯的Android用户，并且可能会部署到其他地区。这个被称为LianSpy的恶意软件至少自2021年以来就一直活跃，但由于其“复杂的规避技术”，直到今年春天才被发现和分析。卡巴斯基告诉俄罗斯媒体，他们在俄罗斯发现了10个间谍软件目标，但拒绝透露受害者是谁。研究人员表示，这不是大规模间谍活动，而是间谍软件操作员感染了特定目标。该工具的开发者和购买者目前仍不得而知。卡巴斯基称，攻击者只使用公共服务（例如俄罗斯Yandex Disk云服务）而不是私人基础设施来窃取被盗数据和存储配置命令，因此很难“确定哪个黑客组织是这些攻击的幕后黑手”。研究人员在8月5日发布的报告中表示：“全球实践表明，这种复杂的网络间谍活动往往是由与民族国家行为者有关的团体煽动的。”

![](https://mmbiz.qpic.cn/mmbiz_jpg/0KRmt3K30icXyNZgemnabtTsbJET3d2b2hPjAwhMjiaGc4nStYhIUGX7JrVfz8geUM8WDfVHdFuzy2RMic7UwK33g/640?wx_fmt=jpeg&from=appmsg&wxfrom=13&tp=wxpic)

这是一款后漏洞利用恶意软件

卡巴斯基研究员Dmitry Kalinin本周在一篇博文中写道：“LianSpy是一种后漏洞利用的木马，这意味着攻击者要么利用漏洞获取Android设备的权限，要么通过物理访问受害者的设备来修改固件。目前尚不清楚攻击者在前一种情况下可能利用了哪种漏洞。”

LianSpy是快速增长的间谍软件工具列表中的最新一款。同类软件包括广泛部署的产品，例如NSO集团的Pegasus Software 和Intellexa联盟的Predator。近年来，研究人员发现了这些恶意软件实例，这些恶意软件针对的是iPhone和Android智能手机用户。这些工具的主要购买者和用户通常是政府和情报机构，他们希望监视异见人士、政治对手和其他感兴趣的人。

在许多情况下（例如去年的Operation Triangulation iOS 间谍软件活动），移动间谍软件工具的提供者利用Android和iOS 中的零日漏洞在目标设备上投放和/或运行恶意软件。在其他情况下，包括去年被称为BadBazaar的Android间谍软件工具和2022年被称为SandStrike 的另一个间谍工具，威胁行为者通过官方移动应用商店中流行应用程序的假冒版本分发间谍软件。

Lianspy已经活动了三年

卡巴斯基研究人员于2024年3月首次偶然发现LianSpy，并很快确定其背后的实体自2021年7月以来一直在使用该间谍软件工具。他们的分析表明，攻击者很可能以系统应用程序和金融应用程序的形式分发恶意软件。

与某些所谓的零点击间谍软件工具不同，LianSpy的运行能力在一定程度上取决于用户交互。恶意软件启动时，首先检查其是否具有在受害者设备上执行任务所需的权限。如果没有所需的权限，恶意软件会提示用户提供权限。当LianSpy获得权限后，它会注册所谓的Android 广播接收器来接收和响应系统事件，如启动、电池电量不足和网络变化。卡巴斯基研究人员发现 LianSpy 使用经过修改的名称（“mu”而不是“su”）的超级用户二进制文件来尝试获取受害者设备的root访问权限。卡巴斯基官员表示，这表明威胁行为者在通过其他方式首先获得设备访问权限后投放了恶意软件。

“启动后，恶意软件会将其图标隐藏在主屏幕上，并使用root权限在后台运行，”Kalinin写道。“这使它能够绕过Android状态栏通知，这些通知通常会提醒受害者智能手机正在使用摄像头或麦克风。”

LianSpy都能干些什么？

LianSpy会伪装成系统应用程序或金融服务，例如支付宝数字支付应用程序。如果间谍软件作为系统应用程序运行，它会自动获得进一步利用所需的权限；否则，它会请求屏幕覆盖、通知、后台活动、联系人和通话记录的权限。

一旦激活，该间谍软件就会将其图标隐藏在主屏幕上，并使用管理员权限在后台运行。该间谍软件通过拦截通话记录、向攻击者的服务器发送已安装应用程序列表以及记录智能手机屏幕（主要是在 Messenger 活动期间）来悄无声息地秘密监视用户活动。研究人员表示，攻击者似乎对受害者的银行数据不感兴趣。

目前尚不清楚黑客如何使用他们获得的数据，但他们确保将这些数据安全地存储在他们的服务器上。为此，他们使用了一种加密方案，只有威胁者才能解密被盗信息。

由于用于过滤通知的关键短语部分为俄语，并且LianSpy的一些默认配置包括俄罗斯流行的消息应用程序的软件包名称，因此研究人员将这款间谍软件引向了俄罗斯。然而，“这款间谍软件采用的非常规方法也可能适用于其他地区。”这表明该恶意软件专门针对俄罗斯用户，但其也可对其它地区用户有效。

LianSpy的主要功能是悄悄监视用户活动，方法是拦截通话记录、记录设备屏幕（尤其是用户发送或接收消息时）以及枚举受害者设备上安装的所有应用程序。恶意软件背后的威胁行为者没有使用私有基础设施与恶意软件通信或存储收集的数据。相反，攻击者一直在使用公共云平台和pastebin服务来实现这些功能。

卡巴斯基在有关该恶意软件的技术报告中表示：“威胁者利用 Yandex Disk 窃取数据并存储配置命令。受害者数据被上传到一个单独的 Yandex Disk文件夹中。”

据卡巴斯基称，LianSpy的一个有趣之处是该恶意软件如何在受感染的设备上利用其root权限。LianSpy不会利用其超级用户身份完全控制设备，而是仅使用足够多的功能以悄无声息的方式执行其任务。“有趣的是，root权限的使用是为了防止被安全解决方案检测到，”安全供应商表示。卡巴斯基研究人员还发现LianSpy使用对称和非对称密钥来加密其窃取的数据，这使得受害者身份无法识别。

Kalinin表示，除了收集通话记录和应用程序列表等标准间谍手段外，它还利用root权限进行秘密屏幕录制和规避。与以经济为目的的间谍软件不同，LianSpy专注于捕获即时消息内容，这表明它是一种有针对性的数据收集操作。

2023年6月，卡巴斯基发现了另一起间谍活动，名为“三角测量行动”，该活动利用了Apple设备中的两个漏洞。该活动自2019年以来一直活跃，通过发送带有恶意附件的iMessage来攻击目标。

防范建议

卡巴斯基在其博文中给出了防范此类间谍软件的建议。

(1）只从官方商店和目录下载应用程序，但请记住，间谍软件甚至可能渗透到这些商店和目录中。

(2）定期更新您的操作系统——并非所有恶意软件都能适应新的安全功能。

(3）使用来自可信开发商的知名应用程序。避免使用即时通讯和其他服务的替代客户端，因为它们可能包含恶意代码。

(4）使用卡巴斯基：防病毒和VPN及时检测LianSpy等间谍软件。

(5）如果仍然没有可靠的保护，请使用间谍软件检测工具TinyCheck 。

(6）仅授予应用程序运行所需的权限。

**参考资源：**

1.https://www.securitylab.ru/news/550817.php

2.https://therecord.media/android-spyware-kaspersky-russian-targets

3.https://www.darkreading.com/mobile-security/sophisticated-android-spyware-targets-users-in-russia

4.https://www.kaspersky.com/blog/new-spy-for-android-smartphones-lianspy/51923/

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
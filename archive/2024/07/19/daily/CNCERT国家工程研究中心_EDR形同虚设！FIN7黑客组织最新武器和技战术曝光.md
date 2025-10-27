---
title: EDR形同虚设！FIN7黑客组织最新武器和技战术曝光
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247545902&idx=3&sn=4b92f556eb0f88a19116d169cd7ed542&chksm=fa9382efcde40bf9c2bbfac04452c68ac8040c1947bb7d442e450ecce30d1dc17b5f2331f2d1&scene=58&subscene=0#rd
source: CNCERT国家工程研究中心
date: 2024-07-19
fetch_date: 2025-10-06T17:42:15.743986
---

# EDR形同虚设！FIN7黑客组织最新武器和技战术曝光

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176ll0qqBicuM5SRQlDotjm1Wf8DTjhZ764q0OmTWWgR2f1ta3IeFUlDLnkn99IubNxyCa4icfQyS8Hvg/0?wx_fmt=jpeg)

# EDR形同虚设！FIN7黑客组织最新武器和技战术曝光

网络安全应急技术国家工程中心

著名的FIN7黑客组织被发现正在销售其定制的“AvNeutralizer”工具，该工具能够通过终止企业网络中的端点防护软件来逃避检测。FIN7是一个自2013年以来活跃的俄罗斯黑客组织，最初专注于通过黑客攻击组织和窃取借记卡及信用卡信息进行金融诈骗。随后，他们转向勒索软件领域，并与DarkSide和BlackMatter等勒索软件即服务(RaaS)平台有关联。FIN7以其复杂的网络钓鱼和工程攻击而闻名，包括冒充BestBuy发送恶意USB密钥和开发定制恶意软件及工具。他们还创建了一个名为Bastion Secure的假冒安全公司，以招募渗透测试人员和开发人员进行勒索软件攻击，而申请者并不知道他们的工作将如何被使用。

SentinelOne的最新报告显示，FIN7创建的“AvNeutralizer”（也称为AuKill）工具最初在2022年被BlackBasta勒索软件操作中发现。该工具被用来终止安全软件，使得勒索软件能够更轻易地执行。研究人员发现，除了BlackBasta外，还有五个其他勒索软件操作使用了这个工具，显示出该工具的广泛传播。FIN7还更新了AvNeutralizer，利用Windows ProcLaunchMon.sys驱动程序使进程挂起，从而使它们无法正常工作。这使得该工具能够终止包括Windows Defender和Sophos、SentinelOne、Panda、Elastic和Symantec等产品在内的任何防病毒/EDR软件。研究人员警告说，FIN7的持续创新和工具开发，以及其软件的销售，使其成为全球企业的重大威胁。FIN7使用多个别名与其他网络犯罪实体合作，使得归因更加困难，并展示了其先进的操作策略。

![](https://mmbiz.qpic.cn/mmbiz_jpg/0KRmt3K30icWXhHFJaWTb6S4agA4mJwkia1icGEH8iaQQKIJSJEicfHOxkNa1q1V5Isb1aX5ibLX5UavtLp8NFlicBgCg/640?wx_fmt=jpeg&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

兜售攻击武器

SentinelOne 的最新研究揭露了 FIN7 最近在地下犯罪论坛上的活动，该组织在论坛上以各种假名推销其工具和服务。在这些工具中，该组织最引人注目的是销售一种名为 AvNeutralizer（也称为 AuKill）的高度专业化的工具，该工具旨在禁用大多数安全解决方案。

![](https://mmbiz.qpic.cn/mmbiz_jpg/0KRmt3K30icWXhHFJaWTb6S4agA4mJwkiaqceiaSeBhUByYXdDDgm21EJWxVUMMuZAwrvbp8Xsb7W48xhQN17xH4Q/640?wx_fmt=jpeg&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

来源：sentinelone.com

AvNeutralizer 工具的广告出现在多个不同的论坛上，使用不同的用户名，售价从 4,000 美元到 15,000 美元不等。研究人员表示，该工具被各种勒索软件组织广泛采用，表明它不再是单个威胁行为者行动的专属。

研究人员发现了几个用户名，包括“goodsoft”、“lefroggy”、“killerAV”和“Stupor”，这些用户名表明该组织与 FIN7 网络犯罪集团有关联，共同推广其工具和服务，例如名为“PentestSoftware”的后漏洞利用框架。

![](https://mmbiz.qpic.cn/mmbiz_jpg/0KRmt3K30icWXhHFJaWTb6S4agA4mJwkiaqsKptpA40hX3DIqn5icMjMKTZsRQb047vZRl9vxzibTicp7NcOHdvOTZw/640?wx_fmt=jpeg&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

来源：sentinelone.com

该组织在不同论坛上使用多重身份似乎是一种掩盖其真实身份同时维持其非法活动的策略。

攻击武器工具包

### FIN7网络犯罪集团成功实施复杂的网络攻击行动依赖于一套多功能工具包，最新发现和披露的主有要以下五种。

### 1. Powertrash

Powertrash是一个高度混淆的PowerShell脚本，用于反射性地加载内存中的嵌入PE文件，使黑客能够隐秘地执行后门负载。FIN7在其入侵活动中广泛使用 Powertrash以逃避防御。研究人员通过分析大量样本开发了一个基于PowerShell 抽象语法树（AST）的解包器，用于处理混淆代码和自动提取负载。

### 2. Diceloader

Diceloader，又名Lizar 和IceBot，是一个最小化的后门，使攻击者能够建立 C2通道。通过发送位置独立代码（或 shellcode）模块，该后门可以直接在内存中加载并通过加密通道将输出返回给攻击者。Diceloader通常通过Powertrash加载器部署，攻击者使用一个称为“远程系统客户端”的UI客户端与Diceloader C2 服务器交互并控制受害者。

### 3. SSH-based Backdoor

在调查 Diceloader C2 基础设施时，研究人员发现了一个用于托管有效载荷的开放目录网络服务器。该服务器上有两个 Powertrash 加载器用于交付 Diceloader，还有基于 OpenSSH 和 7zip 的原生工具，这些工具用于在被攻击系统上保持持久性。安装脚本通过反向 SSH 隧道连接到攻击者的服务器，并设置为计划任务，以便在系统重启后仍能保持持久性。

### 4. Core Impact

Core Impact是一个渗透测试工具，提供了大量商业级漏洞利用程序，适合 FIN7 的兴趣。该框架生成位置独立代码（PIC）植入物，通过运行时的 XOR 解密来逃避静态检测。FIN7通过Powertrash在其活动中传送Core Impact加载器，并开发了解包器以提取植入物配置。

### 5. AvNeutralizer

AvNeutralizer是FIN7自2022年4月开始开发的专门工具，用于篡改安全解决方案。该工具以定制构建的形式交付给买家，针对特定的安全解决方案进行篡改。AvNeutralizer的版本逐渐更新，并利用弱版本的Process Explorer驱动程序漏洞，进行跨进程操作以篡改安装在系统上的安全解决方案。最新版本增加了新技术，能够篡改某些受保护进程的特定实现，并在勒索软件入侵中使用。

分析显示该组织从2021年初开始从Carbanak过渡到使用Diceloader（也称为Lizar）恶意软件，这表明了其恶意软件演变的时间表。此外，FIN7还被发现将Core Impact等渗透测试工具纳入其武器库，这些工具通常用于复杂的网络攻击。

FIN7的基础设施包括Diceloader的命令和控制服务器，这些服务器在不同国家和托管提供商中被发现。研究人员还发现了一个暴露的服务器，揭示了该组织使用SSH后门进行秘密文件泄露，这表明了其在网络渗透中的隐蔽性。

该组织还开发并销售如AvNeutralizer这样的专门工具，这些工具在地下犯罪论坛上非常受欢迎。AvNeutralizer是一种用于终止安全软件的工具，使得勒索软件攻击更难以被检测和防御。FIN7的这些活动不仅增强了其在其他网络犯罪分子中的影响力，也展示了其技术专长。

对抗EDR的新技术

AvNeutralizer使用超过10种不同的用户模式和内核模式技术来篡改安装在系统上的安全解决方案，以逃避终端点安全解决方案（EDR）的检测和保护措施。大多数这些技术已经有文档记录，例如通过易受攻击的RTCore64.sys驱动程序移除PPL保护，沙箱化受保护进程，利用Restart Manager API和Service Control Manager API等。然而，SentinelOne发现了一种全新的技术，利用了先前在野外未见的Windows内置驱动能力。

AvNeutralizer利用一系列驱动程序和操作步骤，在某些特定实现的受保护进程中创建失败，最终导致拒绝服务的情况。它结合了ProcLaunchMon.sys和更新版本的Process Explorer驱动程序（版本17.02），后者已经针对跨进程操作滥用进行了强化，并且当前没有被Microsoft的WDAC列表所阻止。

以下是成功实现受保护进程实施拒绝服务条件的步骤：

将Process Explorer驱动程序PED.sys（17d9200843fe0eb224644a61f0d1982fac54d844）放置在C:\Windows\System32目录下，并连接到\.\PROCEXP152设备。

加载C:\Windows\System32\drivers\ProcLaunchMon.sys驱动程序，它在系统驱动程序目录中可用，并连接到\.\com\_microsoft\_idna\_ProcLaunchMon设备。

通过与ProcLaunchMon驱动程序交互，配置新的TTD（Time-Travel Debugging）监控会话。

将目标受保护进程的PID添加到TTD监控会话中，导致新生成的子进程被挂起（IOCTL: 0x228034）。

使用procexp驱动程序杀死目标受保护进程的所有非保护子进程（在更新版本的Process Explorer驱动程序中仍允许）。

受保护进程尝试重新启动其子进程，但这些进程由于内核挂起而导致通信失败，并最终崩溃。

![](https://mmbiz.qpic.cn/mmbiz_jpg/0KRmt3K30icWXhHFJaWTb6S4agA4mJwkia6pHYKJBOj6Pux4TZcrBOficJ3DTSbjOF5VOrWRpjngvCfGCficyMbyWw/640?wx_fmt=jpeg&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

AvNeutralizer工作流

这些操作显示了AvNeutralizer如何利用多种复杂的技术手段，利用系统内置的驱动能力和更新的进程探测器驱动版本，以绕过和破坏受保护进程的实施。这些方法使得安全解决方案在面对AvNeutralizer时难以有效检测和防御，对于攻击者来说具有显著的操作灵活性和成功性。

小结

SentinelOne的调查揭示了FIN7作为一个网络威胁组织的显著特点：适应性、持久性和持续发展。该组织通过采用自动化攻击方法，如自动SQL注入攻击，针对面向公众的服务器，展示了其在网络攻击领域的先进性和创新能力。

AvNeutralizer工具的开发与商业化

FIN7在地下犯罪论坛中开发并商业化了如AvNeutralizer等专用工具，这些工具不仅增强了该组织的影响力，也使其在网络犯罪领域中的地位更加突出。AvNeutralizer是一种专门设计用于终止安全软件的工具，使得勒索软件攻击更难以被检测和防御。

技术专长与规避安全措施

FIN7的不断创新，尤其是在规避安全措施方面的复杂技术，进一步展示了其技术专长。该组织通过使用多个假名和与其他网络犯罪实体的合作，使得追踪和归因其行动变得更加困难，这反映了其高级的运营策略。

呼吁进一步的研究与防范

SentinelOne希望这项研究能够激发更多的努力，以更深入地了解FIN7的策略，并开发有效的缓解措施。随着FIN7不断演变其攻击手段，网络安全社区需要保持警惕，加强合作，共同应对这一不断增长的威胁。通过持续的研究和信息共享，可以更好地保护企业和组织免受FIN7等高级持续威胁(APT)组织的侵害。

**参考资源：**

1.https://www.sentinelone.com/labs/fin7-reboot-cybercrime-gang-enhances-ops-with-new-edr-bypasses-and-automated-attacks/

2.https://thecyberexpress.com/fin7-gang-elude-edr-and-automate-attacks/

3.https://www.bleepingcomputer.com/news/security/notorious-fin7-hackers-sell-edr-killer-to-other-threat-actors/

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
---
title: JanaWare勒索软件通过定制的Adwind RAT攻击土耳其用户
url: https://mp.weixin.qq.com/s/uoD4h4ibnla1LfxfJjvuOw
source: Doonsec's feed
date: 2026-04-20
fetch_date: 2026-04-21T04:45:30.154068
---

# JanaWare勒索软件通过定制的Adwind RAT攻击土耳其用户

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/BicXBAdicJy7NJjQ5REMXY11aWsvCZFdhoPeD9QrcBIZCTa5dILoTTymZO96vxfkLOHnZmVsVFYwiaaDVKftgC5zz0GHVR2usD8cfibbceKj6Qo/0?wx_fmt=jpeg)

# JanaWare勒索软件通过定制的Adwind RAT攻击土耳其用户

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

最新分析的名为“JanaWare”的勒索软件活动利用定制版的 Adwind 远程访问木马 (RAT) 攻击土耳其用户。

该攻击活动结合了隐蔽的投放技术、地理限制和多态恶意软件，以逃避检测并保持长期活动。

研究人员发现，JanaWare 专门针对位于土耳其的系统而设计。该恶意软件通过检查系统语言、区域设置和外部 IP 地址来实施严格的地理围栏控制。

只有当系统符合土耳其区域指标时才会执行，从而大大降低了受全球安全分析的影响。

遥测和样本分析表明，该活动至少从 2020 年就开始了，最近一次采集的样本是在 2025 年 11 月。

尽管行动持续进行，但由于其局部目标定位和使用混淆技术，该行动一直相对不为人知。

Acronis TRU 团队发现了一个利用定制版 Adwind（Java RAT）变种的威胁集群。

受害者主要包括家庭用户和中小企业。与索要高额赎金的大型勒索软件团伙不同，JanaWare 的运营者采用的是高规模、低成本的策略，赎金通常在 200 美元到 400 美元之间。

## **基于网络钓鱼的感染链**

攻击始于网络钓鱼邮件，诱骗用户点击恶意链接。这些链接通常会将受害者重定向到托管在谷歌云端硬盘上的恶意程序，导致下载恶意Java归档（JAR）文件。

该恶意软件一旦通过 Java 程序 (javaw.exe) 执行，便会在系统中建立立足点。端点检测与响应 (EDR) 遥测数据揭示了清晰的执行链：

* Outlook 发起了钓鱼邮件攻击。
* Chrome浏览器打开了一个恶意Google云端硬盘链接。
* 下载并执行 JAR 文件。
* 基于 Adwind 的有效载荷会部署勒索软件模块。

这种方法与受害者在公共论坛上的报告相符，证实了社会工程学的广泛应用。

JanaWare 使用多层混淆技术来阻碍分析。研究人员发现，它结合使用了 Stringer 和 Allatori 等公开工具以及自定义类加载器，从而增加了逆向工程的难度。

![](https://mmbiz.qpic.cn/mmbiz_png/BicXBAdicJy7MSa9znicSLekicuTwdwiaGc2ySSKiayD8TM7W2kvRicWnZl893lADaDYTw9r4AJhoCRvibfmkA8BZBrVRwkbv6ycVVHqUoqQ86S0ahc/640?wx_fmt=png&from=appmsg)

该恶意软件的一个关键特征是其多态行为。它利用名为“FilePumper”的组件修改自身的JAR文件，插入随机数据，从而为每次感染生成唯一的文件哈希值。这种技术能够有效地绕过基于特征码的检测系统。

此外，该恶意软件还包含硬编码的配置数据，包括命令与控制 (C2) 基础设施、身份验证令牌和用于匿名通信的 TOR 网络设置。

## **勒索软件的执行和影响**

在确认受害者位于土耳其后，该恶意软件会使用 PowerShell 命令关闭安全防御系统。这些操作包括：

* 禁用 Microsoft Defender 和安全通知。
* 删除卷影副本以防止恢复。
* 禁用 Windows 更新和勒索软件防护。
* 干扰已安装的杀毒软件。

该恶意软件随后会下载一个基于 Java 的勒索软件模块，该模块使用 AES 加密算法对所有驱动器上的文件进行加密。与 C2 服务器的通信通过 Tor 网络进行，这使得追踪和恢复变得十分困难。

![](https://mmbiz.qpic.cn/mmbiz_png/BicXBAdicJy7NXWapVDcebITN6tRGn9dcU3pSjFHuxOOibW46B8RuDz2JSn3o0mibiaE32hymW6gCUqiadPiaMBFcrgDy0vyrnPKbnWX5fOVWtG1p8/640?wx_fmt=png&from=appmsg)

加密系统会收到一封用土耳其语写的勒索信，指示受害者通过 qTox 或基于 Tor 的 .onion 网站联系攻击者。

该通知文件名包含一句土耳其语短语，意思是“重要通知”，这强化了该活动的区域性重点。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BicXBAdicJy7PqcJuvF0v7SlayJfTvQduy65S8MxqmP4fB8LmKZ2EPCSyVeibSia9gGucQX2XQxtXibia9eEcJKWd8icEUkH22Lf0ibKP9o0ZVQMa2s/640?wx_fmt=png&from=appmsg)

JanaWare 展示了规模较小、地域性强的勒索软件攻击如何能够持续多年而不被发现。它结合了定向投放、地理围栏和模块化设计，使攻击者能够在保持灵活性的同时悄无声息地进行攻击。

安全专家警告说，此类攻击凸显了一种日益增长的趋势：局部勒索软件威胁在避免引起全球关注的同时，利用特定用户群体。

## **妥协ioc**

| MD5 Hash | Description |
| --- | --- |
| 4f0444e11633a331eddb0deeec17fd69 | Adwind RAT |
| b2d5bbf7746c2cb87d5505ced8d6c4c6 | Ransomware module (JanaWare) |

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
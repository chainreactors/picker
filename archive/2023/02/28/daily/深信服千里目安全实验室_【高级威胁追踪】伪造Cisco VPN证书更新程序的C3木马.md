---
title: 【高级威胁追踪】伪造Cisco VPN证书更新程序的C3木马
url: https://mp.weixin.qq.com/s?__biz=Mzg2NjgzNjA5NQ==&mid=2247517560&idx=1&sn=50b465098f4294b5bcea69eadbcb20d7&chksm=ce460e68f931877e4c9bed04be82947c7c576cc38c23e59d856bcac7757dd0b63858c4434dcb&scene=58&subscene=0#rd
source: 深信服千里目安全实验室
date: 2023-02-28
fetch_date: 2025-10-04T08:16:53.886731
---

# 【高级威胁追踪】伪造Cisco VPN证书更新程序的C3木马

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/w8NHw6tcQ5xGyNZ2Paib7Gw5e0AohMCpSIxqsqaCvhgvRMFTNa5jHibcibycJECXQ01LsEEzumv1RPAC4OLOiaYGtA/0?wx_fmt=jpeg)

# 【高级威胁追踪】伪造Cisco VPN证书更新程序的C3木马

原创

深瞻情报实验室

深信服千里目安全技术中心

**概述**

攻击者通过钓鱼邮件、社会工程或企业应用漏洞伪造企业应用更新程序针对特定的目标企业进行定向攻击，是 APT 攻击的一种常用手段，也曾被用于针对目标企业的定向勒索攻击活动当中，**近期深信服蓝军 APT 研究团队日常运营中发现一例伪造 Cisco VPN 证书更新程序的攻击样本，该攻击样本会执行一种新型的 C3 木马通信程序，免杀隐藏性非常强。**

C3 是一种自定义控制命令工具，由 WithSecure 安全实验室开发并维护，该工具允许红队快速开发和利用自定义的命令和控制通道，同时提供与现有攻击工具包的集成，可极大的提高 C2 工具的免杀能力，该工具曾被用于 DarkSide 勒索病毒攻击活动，未来有可能会被应用到更多的 APT 攻击或定向勒索攻击活动当中，深信服 APT 研究团队一直在关注全球**攻击者使用的各种新型的攻击手段、攻击武器与全球最新的攻击事件，针对这款 C3 木马样本进行了相关的分析。**

**分析**

1.该攻击样本同样使用 OneNote 文档加载执行木马程序，受害者双击该 OneNote 文档之后，显示安装 Cisco 数字签名的更新程序，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5xGyNZ2Paib7Gw5e0AohMCpSViamRhuQZVibJVSB9X4JTibvibNibNZLV4tac94Oic5dByicAfGIECGR5IzIA/640?wx_fmt=png)

2.使用解析工具对 OneNote 文档进行解包之后，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5xGyNZ2Paib7Gw5e0AohMCpSSjDcYnaiaNYvPj1BAuia1bfBNPJpBvFhtmMhLMS0U7icEHCoNRtoxFtibw/640?wx_fmt=png)

OneNoteAttachments 里面附带一个 Cisco-CertificatePkg.cpl 程序。

3.动态调试 Cisco-CertificatePkg.cpl，会在内存中解密出一层 ShellCode 代码，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5xGyNZ2Paib7Gw5e0AohMCpSI8kRVibIy3HpN4gDY9DCEV43uvcgunddpOLxvXYtdjQ1DgHNOrzAgicQ/640?wx_fmt=png)

4.ShellCode 代码会在内存中解密出一个 Payload 加载程序，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5xGyNZ2Paib7Gw5e0AohMCpS5pAOPmCzXeQT0CibOwcia0IaZsew06iaHQMTN9uaHEJ48J5yTmkweibCicg/640?wx_fmt=png)

5.Payload 加载程序执行之后会在内存中解密出核心 Payload，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5xGyNZ2Paib7Gw5e0AohMCpSEOyIWh3n9UDrxqvZRiaUXM53ic4JDF4VIBia0tqD1kCa8BjExHWvP4SKQ/640?wx_fmt=png)

6.解密出来的另一个 Payload，就是一个 C3 木马，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5xGyNZ2Paib7Gw5e0AohMCpSYfFZOPm1auibHC33UH2mQTQ3lS99edjfP0RnSrcV1RqKbXer0ZNQjwA/640?wx_fmt=png)

7.调用该 C3 木马 StartNodeRelay 函数，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5xGyNZ2Paib7Gw5e0AohMCpSTticaWgDqsuszKpUKpZFnOXib8NW6gXr3qiauOQO6Rkye0ib6WethaLpUw/640?wx_fmt=png)

8.该样本与 Azure 服务总线集成，通过 Azure 服务总线进行通信，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5xGyNZ2Paib7Gw5e0AohMCpSHLyZOVvAnsRVWmOtFFoht2lmQibCKnibC9uLWzsY6QwRdfJ0fwNSFRHw/640?wx_fmt=png)

9.与远程服务器通信 URL 地址，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5xGyNZ2Paib7Gw5e0AohMCpSHCw0OBFDicia8t7QQrkwRDKoRcqiarOKdmib3PcDibQqk4nytz1ItPvP1ug/640?wx_fmt=png)

样本基本上就分析完毕了，该样本使用了最近比较活跃的利用 OneNote 文件的攻击手法，同时利用 C3 工具对 C2 网络通信进行了自定义，攻击者在样本层面和流量层面都使用了相应的免杀逃逸技术。

**总结**

攻击者一直在寻找新的攻击手法和攻击技术，以逃避安全厂商各种安全产品的检测，包含终端安全产品，网端安全产品、云端安全产品等，**这是一场猫捉老鼠的游戏，也是一个持续对抗升级的过程，安全厂商需要持续关注和研究全球攻击者使用的最新的一些攻击手法和攻击技术，才能更好的保障客户的安全。**

深信服APT研究团队专注全球高级威胁事件的跟踪与分析，拥有一套完善的自动化分析溯源系统以及外部威胁监控系统，能够快速精准的对 APT 组织使用的攻击样本进行自动化分析和关联，同时积累并完善了几十个 APT 以及网络犯罪威胁组织的详细画像，并成功帮助客户应急响应处置过多个 APT 及网络犯罪威胁组织攻击事件，未来随着安全对抗的不断升级，威胁组织会研究和使用更多新型的 TTP，深信服APT研究团队会持续监控，并对全球发现的新型安全事件进行深入分析与研究。

**ioc**

**HASH**

6887cf122d9409d86f09bf8ea900844214c8c07f74daa680582b2b4c69cf35b8

23920a9337e02e4f8ee01aaeae91b172dab1c3a1028c2f55d4098fe1b2e4ff7f

**参考链接**

https://labs.withsecure.com/publications/hunting-for-c3

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5xUEmJGibg2JE8nVwwxzibBrJTEzuyfhPTuTZeyvTviay6rzGOGrHkAO45vyyibnV1FZThckmmfFfM6BA/0?wx_fmt=png)

深信服千里目安全技术中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5xUEmJGibg2JE8nVwwxzibBrJTEzuyfhPTuTZeyvTviay6rzGOGrHkAO45vyyibnV1FZThckmmfFfM6BA/0?wx_fmt=png)

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
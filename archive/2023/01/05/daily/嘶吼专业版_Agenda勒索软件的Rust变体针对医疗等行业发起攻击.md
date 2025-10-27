---
title: Agenda勒索软件的Rust变体针对医疗等行业发起攻击
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247556011&idx=3&sn=e231f59a27cef78e9dd0632247e0aa60&chksm=e915cb91de6242878fa4a18e8821e9ec02587e11a9ee8233a57c2b78b4f2d0ed0348edd554ff&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2023-01-05
fetch_date: 2025-10-04T03:05:05.647826
---

# Agenda勒索软件的Rust变体针对医疗等行业发起攻击

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ibR2vSLibcFv8TmXTcicFBvZTOIFQKWC1ENuicic2oZ6FPOBruegr5GPS9SqlxSYcNgia5FSKntZzRJvaQ/0?wx_fmt=jpeg)

# Agenda勒索软件的Rust变体针对医疗等行业发起攻击

gejigeji

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

今年，各种勒索软件即服务组织相继在Rust中开发了他们的勒索软件版本，这其中就包括Agenda。Agenda的Rust变体瞄准了一些重要行业。我们将在本文中介绍Rust变体的工作原理。今年，BlackCat、Hive和RansomExx等勒索软件即服务（RaaS）组织开发了Rust版本的勒索软件，Rust是一种跨平台语言，可以更容易地为Windows和Linux等不同的操作系统定制恶意软件。在这篇文章中，我们介绍了另一个已经开始使用这种语言的勒索软件组织Agenda(也称为Qilin)。

根据我们在过去一个月的观察，Agenda勒索软件的活动包括在其泄露网站上发布许多公司的信息。攻击者不仅声称他们能够侵入这些公司的服务器，还威胁要公布他们的文件。勒索软件组织在其泄漏网站上发布的公司位于不同的国家，主要属于制造业和IT行业，总收入超过5.5亿美元。

最近，我们发现了一个用Rust语言编写的Agenda勒索软件样本，检测结果为Ransom.Win32.Agenda.THIAFBB。值得注意的是，同样的勒索软件最初是用Go语言编写的，以针对泰国和印度尼西亚等国家的医疗和教育部门而闻名。攻击者通过使用泄露的账户和唯一的公司ID等机密信息作为附加的文件扩展名，为目标受害者自定义了之前的勒索软件二进制文件。Rust变体还使用了间歇性加密，这是当今攻击者用于更快加密和逃避检测的新兴策略之一。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibR2vSLibcFv8TmXTcicFBvZTx4xicxiaxX3vnBMSncuvPGr2Ea3RFhibiapMwY0h9lx7pPmE8rmJyGvpjg/640?wx_fmt=png)

VirusTotal中二进制文件的提交详细信息，包括提交日期和上传地区

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibR2vSLibcFv8TmXTcicFBvZTRD9GfbeyZQdpZ3z65VNiaY5n9MvjEmKS0wicjoFuHibicl5cdmszRoKyibA/640?wx_fmt=png)

BinText上显示二进制文件使用的Rust模块/函数的字符串

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibR2vSLibcFv8TmXTcicFBvZTM9FX0UpRcHibbsQwLtbnia1k9aYmpwq2Nj3O2ibRIQcOPmLVkGDf9HdZg/640?wx_fmt=png)技术分析

执行时，Rust二进制文件会提示以下错误，要求将密码作为参数传递。这个命令行特性类似于用Golang编写的Agenda勒索软件二进制文件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibR2vSLibcFv8TmXTcicFBvZTG1MMhvLsibXIfVKuR8rEsvbZxnpSxUXzp4GtBx0TbhBU3xsJ563TVyA/640?wx_fmt=png)

执行示例时的错误提示

在以“-password”作为参数并结合虚拟密码“agenda apass”执行示例时，勒索软件示例将从终止各种进程和服务开始运行其恶意例程。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibR2vSLibcFv8TmXTcicFBvZT1SmUhNJYEPKW6F00CgUps51IVKP7sibicxibAbYHYHXlMOBicd4tFP6pjg/640?wx_fmt=png)

终止应用程序和服务

针对我们分析的样本，勒索软件将扩展名“MmXReVIxLV”附加到加密文件中。它还在命令提示符上显示活动日志，包括已加密的文件和运行时间。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibR2vSLibcFv8TmXTcicFBvZTiakRQEg70HWIt4f38G90SRMib7GdknZ4Dwibnet7S4KzhBhficavlj3TOw/640?wx_fmt=png)

加密文件示例

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibR2vSLibcFv8TmXTcicFBvZT957EMdSC2jG9tWnIdte19e0R5V3EG4IpgxClHrn6yAEpFRHSjU3SoA/640?wx_fmt=png)

加密文件中的日志

然后，勒索软件将继续在其加密的每个目录上释放其勒索通知。正如其勒索说明中所观察到的，用于执行勒索软件的密码也将用作登录勒索软件组支持聊天网站的密码。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibR2vSLibcFv8TmXTcicFBvZTiaONMsibmLAMwv628SEGiawAZJdLdyvib3bLickNEibtmchSiclVldWf1rlxg/640?wx_fmt=png)

勒索通知

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibR2vSLibcFv8TmXTcicFBvZTM9FX0UpRcHibbsQwLtbnia1k9aYmpwq2Nj3O2ibRIQcOPmLVkGDf9HdZg/640?wx_fmt=png)勒索软件分析

不同于Agenda的Golang变体，它接受10个参数，Rust变体只接受3个参数：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibR2vSLibcFv8TmXTcicFBvZTSTmMKJ87qgUwSzVhiaE5fmdqHjqXW6L0p5X95mxQr0PFJ3hmiaVblHnQ/640?wx_fmt=png)

Agenda勒索软件Rust变体使用的参数

Rust变体在二进制文件中也包含硬编码配置，就像以前在Golang中编译的示例一样。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibR2vSLibcFv8TmXTcicFBvZTByh4ic3jZiaKIVvvsGX6p7wSAj4Un5zFibXPrDFx75kpgiaTklTibmKEo7g/640?wx_fmt=png)

包含配置的二进制文件内的函数

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibR2vSLibcFv8TmXTcicFBvZTgcAqvcOdlF21VzbFicU8xRIS9XWFpTVGg1dHHCdqrh56UVQmoEU0zJw/640?wx_fmt=png)

包含配置的字符串

它还在其配置中添加了-n、-p、fast、skip和step标志，这些标志在Golang变体配置中不存在，仅通过命令行参数使用。经过进一步分析，我们了解到这些标志用于间歇性加密。这种策略使勒索软件能够根据标志的值对文件进行部分加密，从而更快地加密受害者的文件。这种策略在勒索软件攻击者中越来越流行，因为它可以让他们更快地加密，并避免严重依赖于读/写文件操作的检测。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibR2vSLibcFv8TmXTcicFBvZTUbFQ6Wpr6PHmXtYKiaVicybNfjyYgODJkvHY6efEaxIo5pWeewhhbOWQ/640?wx_fmt=png)

用于间歇加密的标志

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibR2vSLibcFv8TmXTcicFBvZThzBibAoqGvWAx2SPC66SVpEprdZB825RJaFvS1crRXGhnEhml3LukSg/640?wx_fmt=png)

用于间歇加密的标志

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibR2vSLibcFv8TmXTcicFBvZTibOIrCe5x9SesPuyjiczpaic4f2kgsd0ksqA5Qia0lCX0zJxiadHEmwicsew/640?wx_fmt=png)

Agenda勒索软件Golang变体接受的命令行参数

我们试图使用其配置中的一些标志来模拟其加密行为。对于这个模拟，我们使用一个填充“a”作为内容的虚拟文件。

对于快速模式：

值：1

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibR2vSLibcFv8TmXTcicFBvZTibS8q6ibFeNHojuQ4VT7hM7G5U0jByicowzbBoHAuuIAKT0vzsQAXr18A/640?wx_fmt=png)

快速标志设置为1

加密字节：1\*0x200000h，其中1是快速标志中设置的值

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibR2vSLibcFv8TmXTcicFBvZTP09RDwLEmdwqfg9AgV7bbpAr8wFOp8WRlGjOrPAPOqrfWCGiaSMkXdA/640?wx_fmt=png)

0x200000h字节加密

对于N-P模式：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibR2vSLibcFv8TmXTcicFBvZTc2YIibaTzqZ29cATMEeAXLT8FibeyCvR2AgibCJ1zeMoMYPZicLyCsKSOg/640?wx_fmt=png)

标志设置为 n = 1; p = 1

总大小=88082336字节，加密的字节数= 1 \* 0x200000,h，其中1是n标志中设置的值，跳过的字节数= 880818字节(整个文件的1%)，其中1是p标志中设置的值。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibR2vSLibcFv8TmXTcicFBvZTZl8ON8MibQMibsqibtRKSsQNbPCZpLSF0Jjp1XBb1nlicKemObzsYzVKEg/640?wx_fmt=png)

加密字节的0x200000h

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibR2vSLibcFv8TmXTcicFBvZTdHxTmbYyWWgIfW4FISuXg85kCnd6MfZuFUxibuXdfvoyaHtHdJlBaUA/640?wx_fmt=png)

880818字节（相当于文件的1%）加密

除了用于不同加密模式的附加标志之外，Rust变体还将AppInfo包括在要终止的服务列表中。它禁用了用户帐户控制（UAC），这是一项Windows功能，有助于防止恶意软件以管理权限执行，从而导致无法以管理权限运行其他应用程序。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibR2vSLibcFv8TmXTcicFBvZTEh3mJV8Rl6icdeVANOO5MboH5FguXoZVxibSwvCQUmqkRlppyZWMqK3A/640?wx_fmt=png)

使用与service\_CONTROL\_stop等效的参数0x01停止服务的函数

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibR2vSLibcFv8TmXTcicFBvZTvl41fzSoTRMmmYOfX1rkpnXTnrY0RDxIP5v2Cegf1XAhtzwIkfbteg/640?wx_fmt=png)

用于使用等同于SERVICE\_DISABLED的参数0x04禁用服务的函数

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibR2vSLibcFv8TmXTcicFBvZTQdCb7xeyHdnl7901JhkQs7VRlpSbq4jcA17z0ZWia0wlSUTqrAlQXvw/640?wx_fmt=png)

禁用AppInfo服务后，无法运行具有管理权限的应用程序

众所周知，Agenda勒索软件还可以为每个受害者部署自定义的勒索软件，我们已经看到，它的Rust变体有一个分配的空间，用于在其配置中添加帐户，主要用于权限升级。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibR2vSLibcFv8TmXTcicFBvZTC44kgtR1NP39jf6iablJvGXwNhQZ8ssIN0ibe0icRcnR7dgX4icopzrM7w/640?wx_fmt=png)

在Agenda勒索软件的Rust变体配置中分配的帐户

要附加在加密文件上的文件扩展名在其配置中是硬编码的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibR2vSLibcFv8TmXTcicFBvZTT1Sp6og5e1c1o0eWPYd2iaTK7hibR6E5oplOSg2GiakmYdx4zJdVpGZNg/640?wx_fmt=png)

要附加的文件扩展名

然而，与之前的Golang变体不同，攻击者在Rust变体的配置中不包括受害者的凭据。后者的这一特性不仅可以阻止其他研究人员访问勒索软件的聊天支持网站，还可以在外部提供样本时访问攻击者的对话。它还可以防止来自受害者之外的其他人的主动信息。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibR2vSLibcFv8TmXTcicFBvZTjiaJuJJUthtOloK67nV40VRBPSC0DBwO32yxaCcHMYTey79w4FQlKhw/640?wx_fmt=png)

Agenda勒索软件聊天支持网站

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibR2vSLibcFv8TmXTcicFBvZTM9FX0UpRcHibbsQwLtbnia1k9aYmpwq2Nj3O2ibRIQcOPmLVkGDf9HdZg/640?wx_fmt=png)总结

Agenda是一个新兴的勒索软件家族，最近一直针对医疗保健和教育行业等关键部门。目前，它的攻击者似乎正在将他们的勒索软件代码迁移到Rust，因为最近的样本仍然缺乏在用Golang变体编写的原始二进制文件中看到的一些特征。Rust语言在攻击者中越来越受欢迎，因为它更难分析，而且反病毒引擎的检测率较低。

参考及来源：https://www.trendmicro.com/en\_us/research/22/l/agenda-ransomware-uses-rust-to-target-more-vital-industries.html

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibR2vSLibcFv8TmXTcicFBvZTvhEacZorsdO2GFo35o834HUlcBLAvWFxicBiao2uovtpI0j2ERBoiaIQQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibR2vSLibcFv8TmXTcicFBvZToAZ7eQFVAl02R4IFPJic5Uxl2xzNgDW8ppG7d55QASpwSQ87lKt5seg/640?wx_fmt=png)

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
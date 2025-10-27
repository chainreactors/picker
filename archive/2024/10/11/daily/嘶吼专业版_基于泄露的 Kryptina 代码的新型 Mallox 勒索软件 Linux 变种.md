---
title: 基于泄露的 Kryptina 代码的新型 Mallox 勒索软件 Linux 变种
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247578317&idx=2&sn=1dcc49298f8e4f331aa6d29db8e29d37&chksm=e91462f7de63ebe14c34b6f5fbbb26be37dcec7e345948fd90e85f9583c694fee0d2220438a0&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2024-10-11
fetch_date: 2025-10-06T18:53:42.318942
---

# 基于泄露的 Kryptina 代码的新型 Mallox 勒索软件 Linux 变种

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2icAdh8xnicSc1Av7wVq5sXOpYxR8H6xnaiaSiapP6mxzOIibK8eg6X0WjrfcSktE9eFoyBvo3QZpzsp8A/0?wx_fmt=jpeg)

# 基于泄露的 Kryptina 代码的新型 Mallox 勒索软件 Linux 变种

胡金鱼

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

Mallox 勒索软件行动的附属机构（也称为 TargetCompany）被发现使用稍微修改过的 Kryptina 勒索软件版本攻击 Linux 系统。

SentinelLabs 表示，此版本与其他针对 Linux 的 Mallox 变体不同，例如 Trend Micro 研究人员去年 6 月描述的变体，这突显了勒索软件生态系统的策略转变。此外，这再次表明，之前只针对 Windows 的恶意软件 Mallox 正在将 Linux 和 VMWare ESXi 系统纳入其攻击范围，标志着该行动的重大演变。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icAdh8xnicSc1Av7wVq5sXOpQkuIPW0ZOK5zDuqn0GzSJnbc6PGYveorcgPiauYn5eBcEZib2TGibzjnQ/640?wx_fmt=png&from=appmsg)从 Kryptina 到 Mallox

Kryptina 于 2023 年底作为针对 Linux 系统的低成本（500-800 美元）勒索软件即服务 (RaaS) 平台推出，但未能在网络犯罪社区引起关注。

2024 年 2 月，其所谓的管理员使用别名“Corlys”在黑客论坛上免费泄露了 Kryptina 的源代码，据推测这些源代码被有意获得可运行的 Linux 变体的随机勒索软件参与者获取。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icAdh8xnicSc1Av7wVq5sXOpaqPXriaP0SDiapXFoNbgmkBGPhcyFvUOwZBrRU9IP30k6keUp0CWcTCQ/640?wx_fmt=png&from=appmsg)

威胁者泄露源代码

在 Mallox 的一家附属公司遭遇操作失误并暴露其工具后，SentinelLabs 发现 Kryptina 已被该项目采用，其源代码被用于构建重新命名的 Mallox 有效载荷。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icAdh8xnicSc1Av7wVq5sXOpCX7gQUuce85eV7zSZaDu3MRGz6KFpj3cfj8F9fQzYPjToebFFWOibnA/640?wx_fmt=png&from=appmsg)

暴露服务器上的 Kryptina 源代码

重新命名的加密器名为“Mallox Linux 1.0”，使用 Kryptina 的核心源代码、相同的 AES-256-CBC 加密机制和解密例程，以及相同的命令行构建器和配置参数。

这表明 Mallox 附属公司仅修改了外观和名称，删除了赎金记录、脚本和文件上对 Kryptina 的引用，并将现有文档转置为“精简”形式，其余部分保持不变。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icAdh8xnicSc1Av7wVq5sXOpsMaia1hIicsGqYbdJtfAXcUicnbjibPw0SVHibkiaWS30aiaL1miaEaG6xxEUg/640?wx_fmt=png&from=appmsg)

Mallox Linux 1.0 勒索信

除了 Mallox Linux 1.0 之外，SentinelLabs 还在威胁者的服务器上发现了各种其他工具，包括：

**·**合法的卡巴斯基密码重置工具 (KLAPR.BAT)

**·**CVE-2024-21338 漏洞利用，Windows 10 和 11 上的权限提升漏洞

**·**权限提升 PowerShell 脚本

**·**基于 Java 的 Mallox 有效载荷投放器

**·**包含 Mallox 有效载荷的磁盘映像文件

**·**14 个潜在受害者的数据文件夹

目前，尚不确定 Mallox Linux 1.0 变体是由单个附属机构、多个附属机构还是所有 Mallox 勒索软件运营商与 Linux 变体一起使用。

参考及来源：https://www.bleepingcomputer.com/news/security/new-mallox-ransomware-linux-variant-based-on-leaked-kryptina-code/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icAdh8xnicSc1Av7wVq5sXOpNQUsb0u2EvbSYJOjY9BCMibwgt5bPiaDGicqTB3MxtgN4PSt4A1I5287Q/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icAdh8xnicSc1Av7wVq5sXOpWIE4uW9DNpW2CaumSdVpteO9a8FN5dyicOmpYAc5hfNicnWgTc9bTfbQ/640?wx_fmt=png&from=appmsg)

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
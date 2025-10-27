---
title: PoorTry Windows 驱动程序进化为功能齐全的 EDR 擦除器
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247577728&idx=1&sn=332a991d402015de6d8488d207838dd3&chksm=e91460bade63e9ace8aa6a5696ab90b5d3f93c6eec403ec7665422c0583566d1faed0a5351f0&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2024-08-30
fetch_date: 2025-10-06T18:05:41.196386
---

# PoorTry Windows 驱动程序进化为功能齐全的 EDR 擦除器

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ibt9cHnHKXpMLEM9cjKiaCg8ZaVLyKcyAJJ3CvIicj6OicOjmWAH22ciagQX5Ubd0af57xQJI5tzqu7VA/0?wx_fmt=jpeg)

# PoorTry Windows 驱动程序进化为功能齐全的 EDR 擦除器

胡金鱼

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

多个勒索软件团伙用来关闭端点检测和响应 (EDR) 解决方案的恶意 PoorTry 内核模式 Windows 驱动程序已演变为 EDR 擦除器，删除了对安全解决方案的运行至关重要的文件，并使恢复变得更加困难。

尽管 Trend Micro 自 2023 年 5 月以来就警告过 Poortry 上添加了此功能，但 Sophos 现已确认在野外看到了 EDR 擦除攻击。

PoorTry 从 EDR 停用器演变为 EDR 擦除器，代表了勒索软件参与者在策略上非常激进的转变，他们现在优先考虑更具破坏性的设置阶段，以确保在加密阶段获得更好的结果。

PoorTry，也称为“BurntCigar”，于 2021 年开发，作为内核模式驱动程序，用于禁用 EDR 和其他安全软件。

该套件被多个勒索软件团伙使用，包括 BlackCat、Cuba 和 LockBit，最初引起人们注意是因为其开发人员找到了通过 Microsoft 的认证签名流程对其恶意驱动程序进行签名的方法。其他网络犯罪团伙，如 Scattered Spider也被发现使用该工具实施以凭证盗窃和 SIM 卡交换攻击为重点的入侵。

在 2022 年和 2023 年期间，Poortry 不断发展，优化其代码并使用 VMProtect、Themida 和 ASMGuard 等混淆工具来打包驱动程序及其加载器（Stonestop）以进行逃避检测。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibt9cHnHKXpMLEM9cjKiaCg8HNpfTvnM57pcRIJnt26bmvWd4pypsUd0HFNhFibS8eI7ciaYcTWxRwjA/640?wx_fmt=png&from=appmsg)Evolution to a wiper

Sophos 的最新报告基于 2024 年 7 月的 RansomHub 攻击，该攻击利用 Poortry 删除关键的可执行文件 (EXE)、动态链接库 (DLL) 和安全软件的其他重要组件。

这确保了 EDR 软件无法被防御者恢复或重新启动，从而使系统在攻击的后续加密阶段完全不受保护。该过程从 PoorTry 的用户模式组件开始，识别安全软件的安装目录以及这些目录中的关键文件。

然后，它会向内核模式组件发送请求，系统地终止与安全相关的进程，然后删除它们的关键文件。

这些文件的路径被硬编码到 PoorTry 上，而用户模式组件支持按文件名或类型删除，这使其具有一定的操作灵活性，可以覆盖更广泛的 EDR 产品。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibt9cHnHKXpMLEM9cjKiaCg8rtqPFjZ2ElMbJUVyp67Qq6xwaTtwyicBhlZCAHdbY6AKWjpTOXruynA/640?wx_fmt=png&from=appmsg)

按文件类型删除功能

该恶意软件可以进行微调，只删除对 EDR 操作至关重要的文件，从而避免在攻击风险较高的第一阶段产生不必要的噪音。

Sophos 还指出，最新的 Poortry 变体采用签名时间戳操纵来绕过 Windows 上的安全检查，并使用 Tonec Inc. 的 Internet Download Manager 等其他软件的元数据。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibt9cHnHKXpMLEM9cjKiaCg8zUA4RM5iczeBBJGBFZ4d8wib9AvPNbzE5eDN5NHIURzfIXhL6MKrMCRw/640?wx_fmt=png&from=appmsg)

驱动程序属性

攻击者采用了一种被称为“证书轮盘”的策略，他们部署使用不同证书签名的相同有效载荷的多个变体，以增加至少一个成功执行的机会。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibt9cHnHKXpMLEM9cjKiaCg8NaOhScFJq5ukl7gYuQOHxZb5wQHicercwV2OjWfSv5uJac461Mtxe9g/640?wx_fmt=png&from=appmsg)

随着时间的推移，用于签署 Poortry 驱动程序的各种证书

尽管人们努力追踪 PoorTry 的演变并阻止其生效，但该工具的开发人员已经表现出了适应新防御措施的非凡能力。

EDR 擦除功能使该工具在应对攻击方面比防御者更具优势，但也可能为在加密前阶段检测攻击提供新的机会。

参考及来源：https://www.bleepingcomputer.com/news/security/poortry-windows-driver-evolves-into-a-full-featured-edr-wiper/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibt9cHnHKXpMLEM9cjKiaCg8vuVGHhJsh7qfQFuWribfeXalBDibP1fBGhvv6xBpdapkEibFN7xwrG8iaA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icEjy5ZrpCcgr4BicXicPv08DSsrgibDcJQpvwkZoO4OqdIpJNhj6TO5xV0ic0AnVf7f2kcPnNevQlTtQ/640?wx_fmt=png)

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
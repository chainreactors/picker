---
title: 新的 DroidBot Android 恶意软件针对 77 个银行加密应用程序
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247580391&idx=1&sn=2bdac2222c560e9b5607fbdcb854f116&chksm=e9146addde63e3cb11d73bc8e2f025fd4c2e18886e4150c631b0a062b509c2570c7fc6fbdf9f&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2024-12-25
fetch_date: 2025-10-06T19:38:57.290438
---

# 新的 DroidBot Android 恶意软件针对 77 个银行加密应用程序

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ic0EAbdYOEIdHpa8fkhBaULEBStgsAPdg15Pu8Toibb6B80f4ZCEt5EkJMcezucmRVMELPtMS9HTpg/0?wx_fmt=jpeg)

# 新的 DroidBot Android 恶意软件针对 77 个银行加密应用程序

胡金鱼

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

一种名为“DroidBot”的新 Android 银行恶意软件试图窃取英国、意大利、法国、西班牙和葡萄牙超过 77 个加密货币交易所和银行应用程序的凭据。

据发现新 Android 恶意软件的 Cleafy 研究人员称，DroidBot 自 2024 年 6 月以来一直活跃，并作为恶意软件即服务 (MaaS) 平台运行，该工具的售价为每月 3,000 美元。至少有 17 个附属组织已被发现使用恶意软件构建器来针对特定目标定制其有效负载。

尽管 DroidBot 缺乏任何新颖或复杂的功能，但对其僵尸网络之一的分析显示，英国、意大利、法国、土耳其和德国有 776 种独特的感染，表明存在重大活动。此外，Cleafy 表示，该恶意软件似乎正在大力开发，有迹象表明试图扩展到包括拉丁美洲在内的新地区。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ic0EAbdYOEIdHpa8fkhBaULWtS6cUreFjdMz9NnMnbd8ONt3oPpYcC7S4yyj1crvfnvpctcdHiajMw/640?wx_fmt=png&from=appmsg)DroidBot MaaS 操作

DroidBot 的开发人员似乎是土耳其人，他们为附属公司提供了进行攻击所需的所有工具。这包括恶意软件构建器、命令和控制 (C2) 服务器以及中央管理面板，他们可以从中控制操作、检索被盗数据和发出命令。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ic0EAbdYOEIdHpa8fkhBaULiblYicZ5kIR5mu7Fd7LQmdgfBxiaekvEkynoQdyImxeblNkpGmJ8B8bYQ/640?wx_fmt=png&from=appmsg)

创作者声称 DroidBot 在 Android 14 上运行良好

多个附属机构在同一 C2 基础设施上运行，并为每个组织分配了唯一的标识符，使 Cleafy 能够识别 17 个威胁组织。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ic0EAbdYOEIdHpa8fkhBaULwmTRIR7ZlKrwxvMxcnCfW9OghY7UVyKVlqn0ZDI64xDB4uuQxSc04w/640?wx_fmt=png&from=appmsg)

从样本配置中提取的附属机构

有效负载构建器允许附属机构自定义 DroidBot 以针对特定应用程序、使用不同的语言并设置其他 C2 服务器地址。关联公司还可以访问详细文档、恶意软件创建者的支持以及定期发布更新的 Telegram 频道。

总而言之，DroidBot MaaS 操作使缺乏经验或低技能的网络犯罪分子的进入门槛相当低。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ic0EAbdYOEIdHpa8fkhBaULic5mnkb8khZibzyI30IGU3lz4Wiar4SMibPADoJvoTjTJtcSVrP2uDUw2w/640?wx_fmt=png&from=appmsg)

管理面板为附属公司提供完全控制

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ic0EAbdYOEIdHpa8fkhBaULWtS6cUreFjdMz9NnMnbd8ONt3oPpYcC7S4yyj1crvfnvpctcdHiajMw/640?wx_fmt=png&from=appmsg)冒充流行应用程序

DroidBot 通常伪装成 Google Chrome、Google Play 商店或“Android Security”来欺骗用户安装恶意应用程序。然而，在所有情况下，它都会充当试图从应用程序窃取敏感信息的特洛伊木马。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ic0EAbdYOEIdHpa8fkhBaUL8VsmicaV7gCB2K7F4Q7icYGYWX6gIN3rxxmgbVHVYticEiaT0icVNKUAYiaA/640?wx_fmt=png&from=appmsg)

DroidBot 的屏蔽应用程序

该恶意软件的主要特征是：

**·**按键记录 – 捕获受害者输入的每一次按键。

**·**覆盖 – 在合法的银行应用程序界面上显示虚假的登录页面。

**·**短信拦截 – 劫持传入的短信，特别是那些包含用于银行登录的一次性密码 (OTP) 的短信。

**·**虚拟网络计算 – VNC 模块使附属机构能够远程查看和控制受感染的设备、执行命令以及使屏幕变暗以隐藏恶意活动。

DroidBot 操作的一个关键方面是滥用 Android 的辅助功能服务来监控用户操作，并代表恶意软件模拟滑动和点击。因此，如果用户安装了请求奇怪权限的应用程序（例如辅助功能服务），应该立即产生怀疑并拒绝该请求。

在 DroidBot 试图窃取凭证的 77 个应用程序中，一些突出的应用程序包括 Binance、KuCoin、BBVA、Unicredit、Santander、Metamask、BNP Paribas、Credit Agricole、Kraken 和 Garanti BBVA。

为了减轻这种威胁，建议 Android 用户仅从 Google Play 下载应用程序，在安装时仔细检查权限请求，并确保 Play Protect 在其设备上处于活动状态。

参考及来源：https://www.bleepingcomputer.com/news/security/new-droidbot-android-malware-targets-77-banking-crypto-apps/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ic0EAbdYOEIdHpa8fkhBaULxMVmuiae7wPZ5dXzWR8FsrwGAPJhqdtnAMaq2oDSCB1ocSLA2SUlDUQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ic0EAbdYOEIdHpa8fkhBaUL3kl5PypBDZftquAR6cmC9dLrw372dFSVfjWsskV08L44l4y8YFobFQ/640?wx_fmt=png&from=appmsg)

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
---
title: Google Play、Apple App App Store应用程序被发现窃取加密钱包
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247581038&idx=1&sn=384640170fe0870e0583a717748bc8ef&chksm=e9146d54de63e442da671c77a9d6be2709bd6611b46e83350c9176246d2a14da1f9b57001420&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2025-02-08
fetch_date: 2025-10-06T20:38:25.358471
---

# Google Play、Apple App App Store应用程序被发现窃取加密钱包

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o28ib0T3x1toYu7uk1a4DGlmg8hqecRNp6yxCZlSzq9dVOgmO4VJzteicqRIQfgmycKnDZ4fMECrqwYg/0?wx_fmt=jpeg)

# Google Play、Apple App App Store应用程序被发现窃取加密钱包

胡金鱼

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

Google Play商店和Apple App Store上的Android和iOS应用程序包含一个恶意软件开发套件（SDK），旨在使用OCR偷窃器窃取加密货币钱包恢复短语。该活动被称为“ SparkCat”，其名称（“ Spark”）是受感染应用程序中恶意SDK组件之一的名称（“ Spark”）。

Kaspersky解释说：“我们发现Android和iOS应用程序具有恶意的SDK/框架，这些应用程序嵌入了窃取加密货币钱包恢复短语，其中一些可以在Google Play和App Store上找到。”

从Google Play下载了被感染的应用程序超过242,000次，这是在App Store中找到偷窃器的第一个已知案例。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28ib0T3x1toYu7uk1a4DGlmg9dPibU8Uia9NgVRIoK4tTEJiaJtG6vBI8W4SUBe6e7aT2icJHua3pThViaw/640?wx_fmt=png&from=appmsg)Spark SDK窃取用户的加密货币

被感染的Android应用程序上的恶意SDK利用了称为“ Spark”的恶意Java组件，该组件伪装成分析模块。

它使用GitLab上存储的加密配置文件，该文件提供命令和操作更新。在iOS平台上，该框架具有不同的名称，例如“ gzip”，“ googleappsdk”或“ stat”。另外，它使用一个称为“ IM\_NET\_SYS”的基于锈的网络模块来处理与命令和控制（C2）服务器的通信。

该模块使用Google ML Kit OCR从设备上的图像中提取文本，试图找到可用于在攻击者设备上加载加密货币钱包的恢复短语，而无需知道密码。

它（恶意组件）会根据系统的语言加载不同的OCR模型，以区分图片中的拉丁语，韩语和日本角色。然后，SDK沿路径 / API / E / D / U将有关设备的信息上传到命令服务器，并在响应中接收一个调节恶意软件后续操作的对象。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28ib0T3x1toYu7uk1a4DGlmgY7EvhuiaMyUIJ9niaqavWmK14CbU3huYGibXvYLVgCQh53WOIibKgp4oXg/640?wx_fmt=png&from=appmsg)

用于连接到命令和控制服务器的URL

该恶意软件通过使用不同语言的特定关键字来搜索包含秘密的图像，而这些关键字是每个区域（欧洲，亚洲等）的变化。虽然某些应用程序显示针对区域，但它们在指定地理区域之外工作的可能性也不能排除在外。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28ib0T3x1toYu7uk1a4DGlmg9dPibU8Uia9NgVRIoK4tTEJiaJtG6vBI8W4SUBe6e7aT2icJHua3pThViaw/640?wx_fmt=png&from=appmsg)

据发现，有18个受感染的Android和10个iOS应用程序，其中许多应用程序在各自的应用商店中仍然可用。Android Chatai应用程序是由卡巴斯基感染的一个应用程序，该应用程序安装了超过50,000次。该应用已不再在Google Play上可用。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28ib0T3x1toYu7uk1a4DGlmgibqNgbImoOMQ4jrNFQOJKPKyJic94U3cE2Ga4KewRtX38l0icGiahruW3Q/640?wx_fmt=png&from=appmsg)

在Google Play上下载的应用程序

如果用户在设备上安装了这些应用程序中的任何一个，建议立即卸载它们，并使用移动防病毒工具扫描任何残留物。除此之外，用户最好还应考虑重置。

参考及来源：https://www.bleepingcomputer.com/news/mobile/google-play-apple-app-store-apps-caught-stealing-crypto-wallets/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28ib0T3x1toYu7uk1a4DGlmglERBpxfjic4bqZ6rSMDyw6qhFjWOR2YhhiaTMrPlxMiamvrEC7iawD7KCQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28ib0T3x1toYu7uk1a4DGlmgQxeVtbbFMT3hmaZmkPAnvpsia0Sl1Uz6Z5iaw0LQXbiadafJd59t5rNicg/640?wx_fmt=png&from=appmsg)

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
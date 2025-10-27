---
title: TrickMo 恶意软件使用假锁屏窃取 Android PIN
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247578536&idx=2&sn=34aa6e9a59ffeffecc24eaebaf012c30&chksm=e9146392de63ea84ee5b27e19f88294024c5ba0a52c891d16a6f5ce430cc8b53f865d486c95c&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2024-10-19
fetch_date: 2025-10-06T18:53:54.504357
---

# TrickMo 恶意软件使用假锁屏窃取 Android PIN

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o28uyfnoZvSN5BNK9u8vBDw6d59kDORggSmoFdMrR1Wbk3QChojDKN6V9uHrhvk8M3zdicEThBgnVXA/0?wx_fmt=jpeg)

# TrickMo 恶意软件使用假锁屏窃取 Android PIN

胡金鱼

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

TrickMo Android 银行木马的 40 个新变种已在野外被发现，与 16 个植入程序和 22 个不同的命令和控制 (C2) 基础设施相关，具有旨在窃取 Android PIN 的新功能。

Zimperium 是在 Cleafy 之前发布的一份报告调查了当前流通的一些（但不是所有）变种之后报告了这一情况。

TrickMo 于 2020 年首次由 IBM X-Force 记录，但据悉其至少从 2019 年 9 月起就被用于针对 Android 用户的攻击。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28uyfnoZvSN5BNK9u8vBDw6TrhDEZfOaler1t2sFbFEBnDRSMHVomZ58yBvJz7Adk8HibRVV6eeeiaw/640?wx_fmt=png&from=appmsg)假锁屏窃取 Android PIN

TrickMo 新版本的主要功能包括一次性密码 (OTP) 拦截、屏幕录制、数据泄露、远程控制等。该恶意软件试图滥用强大的辅助服务权限来授予自己额外的权限，并根据需要自动点击提示。

作为一种银行木马，它为用户提供各种银行和金融机构的网络钓鱼登录屏幕覆盖，以窃取他们的帐户凭据并使攻击者能够执行未经授权的交易。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28uyfnoZvSN5BNK9u8vBDw6X47DFR5bhZiaL64Nq4psWRiaP8qkiaPU6cphNKZmnEOKs2KnrXL5jiah1g/640?wx_fmt=png&from=appmsg)

攻击中使用的银行覆盖层

Zimperium 分析师在剖析这些新变体时还报告了一个新的欺骗性解锁屏幕，模仿真正的 Android 解锁提示，旨在窃取用户的解锁图案或 PIN。

欺骗性用户界面是托管在外部网站上的 HTML 页面，并在设备上以全屏模式显示，使其看起来像合法屏幕。

当用户输入解锁图案或 PIN 码时，页面会将捕获的 PIN 码或图案详细信息以及唯一的设备标识符（Android ID）传输到 PHP 脚本。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28uyfnoZvSN5BNK9u8vBDw6w8icODGex5NmH15ia6ictIeMNQiciapWKMdqg55yv4KhccD8pJDnw3qYsSQ/640?wx_fmt=png&from=appmsg)

TrickMo 显示的假 Android 锁屏

窃取 PIN 允许攻击者通常在深夜在设备未受到主动监控时解锁设备，以实施设备欺诈。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28uyfnoZvSN5BNK9u8vBDw6TrhDEZfOaler1t2sFbFEBnDRSMHVomZ58yBvJz7Adk8HibRVV6eeeiaw/640?wx_fmt=png&from=appmsg)受害者分布

由于 C2 基础设施安全不当，Zimperium 确定至少有 13,000 名受害者受到该恶意软件的影响，其中大多数位于加拿大，在阿拉伯联合酋长国、土耳其和德国也发现了大量受害者。

根据 Zimperium 的说法，这个数字相当于“几台 C2 服务器”，因此 TrickMo 受害者的总数可能更高。

据安全研究员分析表明，每当恶意软件成功窃取凭据时，IP 列表文件就会定期更新，在这些文件中已经发现了数百万条记录，表明威胁者访问了大量受感染的设备和大量敏感数据。

Cleafy 此前曾向公众隐瞒了妥协的迹象，因为配置错误的 C2 基础设施可能会将受害者数据暴露给更广泛的网络犯罪社区，但 Zimperium 现在选择将所有内容发布到这个 GitHub 存储库上。

然而，TrickMo 的目标范围十分广泛，涵盖银行以外的应用程序类型（和帐户），包括 VPN、流媒体平台、电子商务平台、交易、社交媒体、招聘和企业平台。

TrickMo 目前通过网络钓鱼进行传播，因此为了最大限度地降低感染的可能性，人们应避免不认识的人通过短信或直接消息发送的 URL 下载 APK。

Google Play Protect 可识别并阻止 TrickMo 的已知变体，因此确保其在设备上处于活动状态对于防御恶意软件至关重要。

参考及来源：https://www.bleepingcomputer.com/news/security/trickmo-malware-steals-android-pins-using-fake-lock-screen/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28uyfnoZvSN5BNK9u8vBDw6cdczrrL2bzIxXqCI0vY2vntGHicQh3FnvPEC1c08bjTFttQWwyjFWPQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28uyfnoZvSN5BNK9u8vBDw6zoCkWWdjDaRJibe0zdXP6SQjUpicwF3HmfxB3MJBmNX2GCT5Qtq3EnGw/640?wx_fmt=png&from=appmsg)

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
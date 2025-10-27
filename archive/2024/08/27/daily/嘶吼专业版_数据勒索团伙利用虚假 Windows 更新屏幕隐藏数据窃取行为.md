---
title: 数据勒索团伙利用虚假 Windows 更新屏幕隐藏数据窃取行为
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247577675&idx=1&sn=484f1f09dd872c849af57ec7502129cf&chksm=e9146071de63e967cc0a605592b849d0fb44b7327dba266e59ad6cd8b6eee944f7065a3fae49&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2024-08-27
fetch_date: 2025-10-06T18:06:36.531880
---

# 数据勒索团伙利用虚假 Windows 更新屏幕隐藏数据窃取行为

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2icGXtXwjQ1pEjhGo4h3WqIAWRG7kfbSuKUuSZU0Ne6IhYBPT3LmTHYf0KDH7yMfYzaTtY70mDKeJA/0?wx_fmt=jpeg)

# 数据勒索团伙利用虚假 Windows 更新屏幕隐藏数据窃取行为

胡金鱼

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

近日，一个名为 Mad Liberator 的新数据勒索团伙瞄准了 AnyDesk 用户，并运行虚假的 Microsoft Windows 更新屏幕来分散注意力，同时从目标设备窃取数据。

该行动于 7 月开始出现，虽然观察该活动的研究人员没有发现任何涉及数据加密的事件，但该团伙在其数据泄露网站上指出，他们使用 AES/RSA 算法来锁定文件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icGXtXwjQ1pEjhGo4h3WqIAe1DaIGCyHW4VHv9dfjUEa3EqOy59fxzVxtSae1ks7HjIxfZTl3dUBg/640?wx_fmt=png&from=appmsg)

Mad Liberator“关于”页面

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icGXtXwjQ1pEjhGo4h3WqIAzia0Xwhqp5HKWfzX1iagbbOonOlIgH9vWnwxC1XVMATys5AHEsqSOEbw/640?wx_fmt=png&from=appmsg)

# 针对 AnyDesk 用户

在网络安全公司 Sophos 的一份报告中，研究人员表示，Mad Liberator 攻击始于使用 AnyDesk 远程访问应用程序与计算机进行未经请求的连接，该应用程序在管理公司环境的 IT 团队中很受欢迎。

目前尚不清楚威胁者如何选择其目标，但有一种理论是，Mad Liberator 会尝试潜在的地址（AnyDesk 连接 ID），直到有人接受连接请求，但该说法尚未证实。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icGXtXwjQ1pEjhGo4h3WqIAf5c5JskP3eljUoXeHtJEdic4ViazL7v9VleHiaib3hSnsEqPZrT79DEZdQ/640?wx_fmt=png&from=appmsg)

AnyDesk 上的连接请求

一旦连接请求被批准，攻击者就会在受感染的系统上放置一个名为 Microsoft Windows Update 的二进制文件，该二进制文件会显示一个虚假的 Windows Update 启动画面。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icGXtXwjQ1pEjhGo4h3WqIAgmxNAK8Giaf5YRDzncmBCjj6tX9vic8tnDFWxI5S2XlByhGJUxYxfNmA/640?wx_fmt=png&from=appmsg)

伪造的 Windows 更新启动画面

该诡计的唯一目的是分散受害者的注意力，同时威胁者使用 AnyDesk 的文件传输工具从 OneDrive 帐户、网络共享和本地存储中窃取数据。在虚假更新屏幕期间，受害者的键盘被禁用，以防止破坏数据泄露过程。

安全研究人员发现，Mad Liberator 的攻击持续了大约四个小时，在数据泄露后阶段，它没有进行任何数据加密。但它仍然在共享网络目录上留下勒索信，以确保在企业环境中获得最大程度的可见性。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icGXtXwjQ1pEjhGo4h3WqIACfdMia9DmlicyjlGy1a6hVOxraeR92zD947wJ2JYmRthg1jLPG9azcXw/640?wx_fmt=png&from=appmsg)

被入侵的设备被泄露勒索信

安全研究人员指出，在 AnyDesk 连接请求之前，它没有看到 Mad Liberator 与目标互动，也没有记录任何支持攻击的网络钓鱼尝试。

关于 Mad Liberator 的勒索过程，威胁者在其暗网上声明，他们首先联系被入侵的公司，并表示如果满足他们的金钱要求，他们就会“帮助”他们修复安全问题并恢复加密文件。

如果受害公司在 24 小时内没有回应，他们的名字就会被公布在勒索门户网站上，并有七天的时间联系威胁者。

在发出最后通牒后的五天内，如果受害者没有支付赎金，所有被盗文件都会被公布在 Mad Liberator 网站上，目前该网站已列出了九名受害者。

参考及来源：https://www.bleepingcomputer.com/news/security/new-mad-liberator-gang-uses-fake-windows-update-screen-to-hide-data-theft/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icGXtXwjQ1pEjhGo4h3WqIADkibSx32onRusxCT1ybHSQYONCXRxOmYGCfaUdMbZxkMgz09wsQeFlQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icGXtXwjQ1pEjhGo4h3WqIAoykwJc2SL0tqhcXNFTaDrUoJCXK6mp0aAfnr0gNqa8mNWLibujUibTUA/640?wx_fmt=png&from=appmsg)

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
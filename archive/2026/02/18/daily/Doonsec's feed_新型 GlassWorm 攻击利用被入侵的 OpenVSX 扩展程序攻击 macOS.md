---
title: 新型 GlassWorm 攻击利用被入侵的 OpenVSX 扩展程序攻击 macOS
url: https://mp.weixin.qq.com/s/yws2xELVg3mKt4hq2fXSuw
source: Doonsec's feed
date: 2026-02-18
fetch_date: 2026-02-19T04:21:11.527039
---

# 新型 GlassWorm 攻击利用被入侵的 OpenVSX 扩展程序攻击 macOS

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/qvpgicaewUBkrOhnIEU2qdibGwPST8b6krIibWSROQQ0T1ZZDTOGP7CfCe5jficwRcayicQ9MhZLaicvVvoYbhv5PsoQ/0?wx_fmt=jpeg)

# 新型 GlassWorm 攻击利用被入侵的 OpenVSX 扩展程序攻击 macOS

Rhinoer
Rhinoer

犀牛安全

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/qvpgicaewUBkrOhnIEU2qdibGwPST8b6kriaohsa3aAXdYKDmbFNuOTro3xMBqym2zicTtM7v94ia98rDial1o4pVHjA/640?wx_fmt=png&from=appmsg)

一种名为 GlassWorm 的新型恶意软件攻击通过被入侵的 OpenVSX 扩展程序，专门窃取 macOS 系统中的密码、加密钱包数据以及开发人员凭据和配置。

攻击者获得了合法开发者（oorzc）的帐户访问权限，并将带有 GlassWorm 有效载荷的恶意更新推送至四个已被下载 22,000 次的扩展程序。

GlassWorm攻击最早出现于10月下旬，它利用“不可见”的Unicode字符隐藏恶意代码，窃取加密货币钱包和开发者账户信息。该恶意软件还支持基于VNC的远程访问和SOCKS代理。

随着时间的推移和多波攻击，GlassWorm 不仅影响了微软官方的 Visual Studio Code 应用商店，还影响了其针对不受支持的 IDE 的开源替代方案 OpenVSX。

在之前的攻击活动中，GlassWorm 展现出了进化的迹象，盯上了 macOS 系统，其开发者正在努力为 Trezor 和 Ledger 应用添加替代机制。

Socket 安全团队发布的一份新报告描述了一项新的攻击活动，该活动利用木马技术入侵以下扩展程序：oorzc.ssh-tools v0.5.1oorzc.i18n-tools-plus v1.6.8oorzc.mind-map v1.0.61oorzc.scss-to-css-compile v1.3.4

恶意代码于1月30日推送，Socket报告称这些扩展程序在过去两年中一直无害。这表明oorzc账户很可能是被GlassWorm攻击者入侵的。

研究人员表示，此次攻击活动专门针对 macOS 系统，从 Solana 交易备忘录中提取指令。值得注意的是，俄语系统未被攻击，这可能暗示了攻击者的来源。

![](https://mmbiz.qpic.cn/mmbiz_png/qvpgicaewUBkrOhnIEU2qdibGwPST8b6krTJsAM0yYh187Sz9bFoG4fXKkjVkxbppSe4qapUfF7ibocjdbRURZ7vg/640?wx_fmt=png&from=appmsg)

GlassWorm 会加载一个 macOS 信息窃取程序，该程序通过 LaunchAgent 在受感染的系统上建立持久性，从而能够在登录时执行。

它会收集 Firefox 和 Chromium 浏览器的数据、钱包扩展和钱包应用程序、macOS 钥匙串数据、Apple Notes 数据库、Safari cookie、开发者密钥以及本地文件系统中的文档，并将所有内容泄露到攻击者位于 45.32.150[.]251 的基础架构中。

![](https://mmbiz.qpic.cn/mmbiz_png/qvpgicaewUBkrOhnIEU2qdibGwPST8b6kr5tj9hIxJkFffeI2sZiavfKBPa2WYjTEpxDEbEdaDpjDoIGRM0dR69ibA/640?wx_fmt=png&from=appmsg)

Socket 将这些软件包报告给了 Open VSX 平台的运营商 Eclipse 基金会，安全团队确认了未经授权的发布访问权限，撤销了令牌，并删除了恶意版本。

唯一的例外是oorzc.ssh-tools，由于发现了多个恶意版本，它已从 Open VSX 中完全移除。

目前市面上受影响的扩展程序版本是干净的，但下载了恶意版本的开发者应该对系统进行全面清理，并轮换所有密钥和密码。

信息来源：BleepingComputer

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/qvpgicaewUBlHBkILqQuaxKrXKhgz0ZMBz6S8ME08fAF1vUqLQlYxwYIVWh5bsgnAictt45YVfMuqzAic2QZd6Siag/0?wx_fmt=png)

犀牛安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qvpgicaewUBlHBkILqQuaxKrXKhgz0ZMBz6S8ME08fAF1vUqLQlYxwYIVWh5bsgnAictt45YVfMuqzAic2QZd6Siag/0?wx_fmt=png)

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
---
title: 新型macOS窃密软件伪装苹果崩溃报告框架，窃取浏览器凭据
url: https://mp.weixin.qq.com/s/SULZH1huDJwVaygrt3WG6A
source: Doonsec's feed
date: 2026-07-14
fetch_date: 2026-07-15T04:43:25.981227
---

# 新型macOS窃密软件伪装苹果崩溃报告框架，窃取浏览器凭据

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX3KBdxpS17OeuMmic7fdAicPuQcEPgumoBSgib9Declibe2uZONQT3Ut7qZZK8ay9jPwO1YGvpu6nkV0Q7j8vuicu8Vx0I6vaZbc2qM/0?wx_fmt=jpeg)

# 新型macOS窃密软件伪装苹果崩溃报告框架，窃取浏览器凭据

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![FreeBuf](https://mmbiz.qpic.cn/mmbiz_gif/icBE3OpK1IX1piafdTo4RZuh09FGofibbEz0hrzvPKkbxTicaficrBmpsZu4QxqYe1ubCsAmlpzGyxVheibXf3FK3FRDEyib3Ttg9E1cHmWBf5R1mU/640?wx_fmt=gif)

![文章配图](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX2KjAJkoSkb9py0YuicW6OEntuCibbY29x8vwgA3HhVFoBvFePxNJfDbkTKtTFMrWZkicnW5ibVuPyQMibO5msWdr2rrIvicAxWib67Io/640?wx_fmt=jpeg)

CrashStealer是一款原生C++开发的macOS信息窃取器，它伪装成苹果内置的崩溃报告工具，用于窃取浏览器凭据、加密货币钱包、密码管理器数据和钥匙串内容，然后将所有数据加密并外泄至远程命令与控制服务器。

Part01

发现与技术概览

2026年5月初，Jamf在VirusTotal上首次发现了一个可疑样本，它看起来像是一款尚在开发中的信息窃取器。到7月初，野外检测证实该恶意软件已成熟并开始活跃部署，研究人员遂将其正式命名为CrashStealer进行追踪。

与通常基于AppleScript释放器或轻量级Objective-C封装构建的常见macOS窃密软件不同，CrashStealer完全用原生C++编写，核心围绕一个名为MacOSData的内部类，这使其与Atomic（AMOS）、MacSync和Phexia等家族区别开来，尽管目标相似。

Part02

初始访问与伪装机制

初始访问始于一个名为“Werkbit Setup”的磁盘映像，其中包含一个应用程序包，该包使用合法的开发者ID签名并附有经过公证的票据，使其能够在首次启动时绕过Gatekeeper。

![macOS窃密软件伪装苹果崩溃报告](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX15mQNk7rr1BGf8jMa1Ml61rJRtqPkFXiabaSNDia6zZnSiajv3ibf3qXMiaB2UKRQDsa5xCIRic6LgWMnQqUk9UOnCMtJPcVQ6O43Vw/640?wx_fmt=jpeg)

这很不寻常：连磁盘映像容器本身也经过了签名，这在恶意DMG活动中十分罕见。一旦打开，释放器会悄悄从GitHub托管的服务器中获取一个混淆的shell脚本，解码多层Base64编码的命令，并下载实际负载，该负载伪装成“CrashReporter.app”，带有苹果的包标识符com.apple.crashreporter和对应的图标。

Part03

攻击能力与持久化分析

一旦运行，CrashStealer会通过dscl在本地验证受害者的登录密码，解锁钥匙串，并分析已安装的安全工具，然后开始收集数据。其收集范围十分广泛：

* Chromium系列浏览器（Chrome、Brave、Edge、Opera、Vivaldi）和Firefox的凭据存储
* 约80个加密货币钱包扩展，涵盖Ethereum、Solana、Cosmos、TON及其他生态系统
* 14个密码管理器，包括1Password、Bitwarden和LastPass
* 用户的登录钥匙串以及对Documents和Downloads目录的广泛文件系统侦察

这种广度反映了现代macOS窃密软件领域的常见模式，即针对加密货币的凭据窃取已成为主要目标。

CrashStealer在技术上的独特之处在于，它通过苹果的CommonCrypto框架使用客户端AES-256-GCM加密来加密暂存的数据，然后将其打包成ZIP归档，并通过libcurl外泄。这种操作安全级别在常见的基于AppleScript的窃密软件中并不常见。

这种加密优先的方法，加上控制流平坦化、分层反调试检查等反分析措施，反映了macOS恶意软件家族在技术手段上专业化的大趋势。整个行业的研究人员都指出，随着macOS威胁从机会主义脚本演变为结构化、业务化运作，这种转变已愈发明显。

![macOS窃密软件伪装苹果崩溃报告](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX2YibibML1ORNQ3SmH8HPLibOzCEy7HrJjzpxP55OibKJd3wRpiciaKqs2DWobcs0oxVNm0K3ib5ibKMEfjQ5frgYYEtVEN6I1H7uQWSvk/640?wx_fmt=jpeg)

为了实现持久化，CrashStealer会复制自身并进行临时重签名，然后安装一个名为com.apple.crashreporter.helper的LaunchAgent，以便在重启后继续运行，将苹果模仿主题延续到持久化层。

Jamf还将该活动关联到一个实时操作面板和多个基础设施域名，表明CrashStealer是一个更大规模、多平台行动的一部分，而非孤立的工具。

这一发现进一步证明了macOS信息窃取器正在迅速缩小与Windows同类产品在复杂度上的差距，2025年至2026年间，检测数量和技术复杂度均大幅攀升。

参考来源：

New macOS Stealer Mimics Apple’s Crash Report Framework to Steal Browser Credentials

https://cybersecuritynews.com/macos-stealer-mimics-apples-crash-report/

**推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX3M5qLVTGP6jiaibktDcXOic6E1x1CNbVhdStkk8micFrCq9q4Hp2oH9WnQ229S3ziaeHPACAgicCRKZjic3pV1CTArGRs1KdhccugdUw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651342454&idx=1&sn=30ae51eba566ed3187493e4e817d3124&scene=21#wechat_redirect)

###

###

###

###

###

###

###

###

###

###

###

###

###

###

###

### **电报讨论**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX38DqtZUv5FjJ2NibZ3wlLba7jpicoInsIGFnVouGN6kbudJyTf7yhkPM5z8JBrkOVNnialq3PeHX0JzJ9vkBXoUwAdicH70OSf4Wc/640?wx_fmt=png&from=appmsg)

![扫码加入AI安全交流群](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX3vp7Nh5SN03lJzkelia9oMl3rDgBcDgQuSu66GUobMfu7PibWYZsgcVfAuZ1aAVwMiatGia3JO3kthfNotNqKQC8uiaS9Za2ky2BVI/640?wx_fmt=png)

![下载FreeBuf知识大陆APP](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0d7KoyEHYsPfbgBgXYQmHS9EgIpOAxfibDrVp8uYPQd3yzGxCrUKcoiajc9NX5KNwMKmib2nnrSsnDa8POob7G5mibuxwMMez0bfI/640?wx_fmt=png)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

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
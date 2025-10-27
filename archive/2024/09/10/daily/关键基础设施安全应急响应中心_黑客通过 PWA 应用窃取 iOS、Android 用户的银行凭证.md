---
title: 黑客通过 PWA 应用窃取 iOS、Android 用户的银行凭证
url: https://mp.weixin.qq.com/s?__biz=MzkyMzAwMDEyNg==&mid=2247545718&idx=4&sn=e7e6095f757729b1a5577a56ddf635cb&chksm=c1e9bf27f69e363168d7c018fa57f174f88219e85a42a411fc170fbb9b595f60cebf35924dca&scene=58&subscene=0#rd
source: 关键基础设施安全应急响应中心
date: 2024-09-10
fetch_date: 2025-10-06T18:28:25.212969
---

# 黑客通过 PWA 应用窃取 iOS、Android 用户的银行凭证

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGoguWwHVes7qFjvRfF8YWP2jj8lXI1iaOfzBszYh9tjtBFwFmlDUBr3ibLV4hXKZYg4qEfDHTJzGU0MyQ/0?wx_fmt=jpeg)

# 黑客通过 PWA 应用窃取 iOS、Android 用户的银行凭证

关键基础设施安全应急响应中心

近期，安全研究人员发现威胁者开始使用渐进式 Web 应用程序冒充银行应用程序并窃取 Android 和 iOS 用户的凭据。

渐进式 Web 应用程序 (PWA) 是跨平台应用程序，可以直接从浏览器安装，并通过推送通知、访问设备硬件和后台数据同步等功能提供类似原生的体验。

在网络钓鱼活动中使用此类应用程序可以逃避检测，绕过应用程序安装限制，并获得设备上危险权限的访问权限，而无需向用户提供可能引起怀疑的标准提示。

该技术于 2023 年 7 月在波兰首次被发现，而同年 11 月发起的后续活动则针对捷克用户。

网络安全公司 ESET 报告称，它目前正在追踪两个依赖这种技术的不同活动，一个针对匈牙利金融机构 OTP Bank，另一个针对格鲁吉亚的 TBC Bank。

然而，这两起攻击活动似乎是由不同的威胁分子发起的。其中一个组织使用不同的命令和控制 (C2) 基础设施来接收被盗凭证，而另一个组织则通过 Telegram 记录被盗数据。

# **感染链**

ESET 表示，这些活动依靠多种方法来接触目标受众，包括自动呼叫、短信（短信网络钓鱼）以及 Facebook 广告活动中精心制作的恶意广告。

在前两种情况下，网络犯罪分子会用虚假消息诱骗用户，称他们的银行应用程序已过时，出于安全原因需要安装最新版本，并提供下载钓鱼 PWA 的 URL。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ib5aZ2jnToWLicWJaLsa8IOlkYAicLOmqLS1o3RESpwFaayKFWofOwicwibTOGd2dySYky6XcjuWMC32Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

PWA 活动感染流程

在社交媒体上发布恶意广告的情况下，威胁分子使用冒充的银行官方吉祥物来诱导合法感，并宣传限时优惠，例如安装所谓关键应用更新即可获得金钱奖励。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ib5aZ2jnToWLicWJaLsa8IOlgRvK0aT1iaWp5jNLGNDKEcyB7VYTTk3oDic4owVTHwHqLlTzHO7p3RuQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

网络钓鱼活动中使用的恶意广告之一

根据设备（通过 User-Agent HTTP 标头验证），点击广告会将受害者带到虚假的 Google Play 或 App Store 页面。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ib5aZ2jnToWLicWJaLsa8IOl8o0Ob9L2U7VE3kDEAVsE6zZKu6icHryMpoRxYDeH7G3PfibW6vheQ9iaQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

虚假的 Google Play 安装提示（左）和进度（右）

点击“安装”按钮会提示用户安装一个伪装成银行应用程序的恶意 PWA。在某些情况下，在 Android 上，恶意应用程序以 WebAPK（由 Chrome 浏览器生成的原生 APK）的形式安装。

网络钓鱼应用程序使用官方银行应用程序的标识符（例如，看似合法的登录屏幕徽标），甚至将 Google Play Store 声明为该应用程序的软件来源。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ib5aZ2jnToWLicWJaLsa8IOlkQ60etY7WZ8bXSibd4qfNbpiccLaHJLd4hibBLcj389OTETkpjiceYQ6QA/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

恶意 WebAPK（左）和钓鱼登录页面（右）

# **在移动设备上使用 PWA 的吸引力**

PWAs 旨在跨多个平台运行，因此攻击者可以通过单一网络钓鱼活动和有效载荷瞄准更广泛的受众。

不过，其主要好处在于可以绕过谷歌和苹果对官方应用商店之外的应用安装限制，以及可能提醒受害者注意潜在风险的“从未知来源安装”警告提示。

PWAs 可以紧密模仿原生应用的外观和感觉，尤其是在 WebAPK 的情况下，图标上的浏览器徽标和应用内的浏览器界面都是隐藏的，因此几乎不可能将其与合法应用程序区分开来。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ib5aZ2jnToWLicWJaLsa8IOlNcpHKDepJeB8Mc55mN1BN5SVTapZYslcgGbvSgM2Mnt6GD7roNPJSA/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

PWA（左）和合法应用程序（右）

WebAPK 难以区分，因为它们的图标中没有 Chrome 徽标。这些 Web 应用可以通过浏览器 API 访问各种设备系统，例如地理位置、摄像头和麦克风，而无需从移动操作系统的权限屏幕请求这些权限。

最终，攻击者可以在无需用户交互的情况下更新或修改 PWA，从而允许动态调整网络钓鱼活动以获得更大的成功。

滥用 PWAs 进行网络钓鱼是一种危险的新兴趋势，随着越来越多的网络犯罪分子意识到其潜力和优势，这种趋势可能会发展到新的程度。

**参考及来源：**

https://www.bleepingcomputer.com/news/security/hackers-steal-banking-creds-from-ios-android-users-via-pwa-apps/

原文来源：嘶吼专业版

“投稿联系方式：sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogvC8qicuLNlkT5ibJnwu1leQiabRVqFk4Sb3q1fqrDhicLBNAqVY4REuTetY1zBYuUdic0nVhZR4FHpAfg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogvgetLSfCMn2pt4xU0Fs6mWM4P98FUya5sz3BvAIzZam7WzZ5aA1kWkKBicptwLzVRicaqAhZ1pceiaA/0?wx_fmt=png)

关键基础设施安全应急响应中心

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogvgetLSfCMn2pt4xU0Fs6mWM4P98FUya5sz3BvAIzZam7WzZ5aA1kWkKBicptwLzVRicaqAhZ1pceiaA/0?wx_fmt=png)

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
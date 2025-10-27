---
title: 慢雾：X 账号安全排查加固指南
url: https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247500113&idx=1&sn=565d07ddee32d31b1e5d3271281e7c3f&chksm=fddebfd6caa936c02a5600ff8c266caf7d4798b41c4d1600aea03ce5c6b9433c3e107bd9c041&scene=58&subscene=0#rd
source: 慢雾科技
date: 2024-08-01
fetch_date: 2025-10-06T18:05:29.045941
---

# 慢雾：X 账号安全排查加固指南

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/qsQ2ibEw5pLZHvGplVZ74mmVhWQwnJrw2eaWxr7Pdmw6wX75U8yoLXd7UFFkcfS67h3QYKgpiaZIicLbmW0pje06g/0?wx_fmt=jpeg)

# 慢雾：X 账号安全排查加固指南

原创

慢雾安全团队

慢雾科技

By: 耀

##

## **背景概述**

近期 Web3 项目方/名人的 X 账号被盗并被用于发送钓鱼推文的事件频发，黑客善于利用各种手段盗取用户账号，较为常见的套路如下：

* 诱导用户点击假冒的 Calendly/Kakao 会议预约链接，从而窃取用户账号的授权或控制用户的设备；
* 私信诱骗用户下载带木马的程序（假冒游戏、会议程序等），木马除了会盗取私钥/助记词之外，可能还会窃取 X 账号权限；
* 利用 SIM Swap 攻击，窃取依赖手机号的 X 账号权限。

慢雾安全团队协助解决了多起类似事件，如 7 月 20 日，TinTinLand 项目方 X 账号被盗，攻击者置顶了一条含有钓鱼链接的推文。在慢雾安全团队的协助下，TinTinLand 及时解决了账号被盗问题，并对 X 账号进行了授权审查和安全加固。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZHvGplVZ74mmVhWQwnJrw24jmh1FhqbNOFCDwQ43SwSsgvfgjh9zK0sqP8ZIslRCxPKU6QDmY9tQ/640?wx_fmt=png&from=appmsg)

考虑到屡屡出现受害者，许多用户对于如何增强 X 账号安全性不太了解，慢雾安全团队将在本文为大家讲解如何对 X 账号做授权排查和安全设置，以下是具体操作步骤。

## **授权排查**

我们以 Web 端为例，打开 x.com 页面后，点击侧边栏的“More”，找到“Settings and privacy”选项，这里主要用于设置账号的安全和隐私。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZHvGplVZ74mmVhWQwnJrw2RibbicXcpVxGL5fE0PJjXh2bNE0mFwWW78X1wJGicgXzPffT1pQ0SjnDQ/640?wx_fmt=png&from=appmsg)

 ![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZHvGplVZ74mmVhWQwnJrw2V6CqUNGL92YxBaPoz2u36Urxv0HZISic1LIvT1gq4s06UhWRL0H6PfQ/640?wx_fmt=png&from=appmsg)

进入“Settings”栏目后，选择“Security and account access”以对账号的安全和授权访问进行设置。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZHvGplVZ74mmVhWQwnJrw2rluecSoTo2vAlWGW5Mhcqh822Gia5icqnwN7xjSfFMX1MwqdTlcPdohQ/640?wx_fmt=png&from=appmsg)

**查看授权过的应用**

很多钓鱼方式是利用用户误点击授权应用链接，导致把 X 账号的发推权限授权出去，随后账号被用于发送钓鱼信息。

排查方法：选择“Apps and sessions”栏目，查看账号授权给了哪些应用，如下图，演示账号授权给了这 3 个应用。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZHvGplVZ74mmVhWQwnJrw2Y329tG5oGoibrKiaKLT9NbpmvjzfFtsWXUVjqfr0BoDghzCPpKRib1a1w/640?wx_fmt=png&from=appmsg)

选择具体的应用后可以看到相对应的权限，用户可通过“Revoke app permissions”移除权限。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZHvGplVZ74mmVhWQwnJrw2NFC5MloMh0c9VhG0FWCrOJIiaibzcCZ9jsHXZQOvz9AKdDyria8gSEdag/640?wx_fmt=png&from=appmsg)

**查看委托情况**

排查方法：Settings → Security and account access → Delegate

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZHvGplVZ74mmVhWQwnJrw2pSwwLU2bxOH0EUu0pIk7IssQrJiaWcYbEU7zHVAbB13WfJQpUsbnia6A/640?wx_fmt=png&from=appmsg)

如果发现当前账号开启了允许邀请管理，那么需要进入“Members you’ve delegated”查看当前账号共享给了哪些账号，在不需要共享后应第一时间取消委派。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZHvGplVZ74mmVhWQwnJrw2icPbbCVBCEtc4DfXDRmvQX65Wm0hndtSmlI1KfGfp7YbSQwXMSdAQUw/640?wx_fmt=png&from=appmsg)

**查看异常登录日志**

如果用户怀疑账号被恶意登录，可以通过排查登录日志来查看异常登录的设备，日期和地点。

排查方法：Settings → Security and account access → Apps and sessions → Account access history

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZHvGplVZ74mmVhWQwnJrw28ePYIOH3VUlC3ebLo4Uxp8nqpxa4c9WKLFRujvZEclHOTa8K30oHuA/640?wx_fmt=png&from=appmsg)

如下图，进入 Account access history 可以查看登录设备的型号，登录日期，IP 和地区，如果发现异常登录信息，则说明账号可能被盗了。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZHvGplVZ74mmVhWQwnJrw2RUbZ4bcxiaP0rjoTw3ibEuGhQC8ctcCT6aKfsNiaAdLslrWpzbcAomE5g/640?wx_fmt=png&from=appmsg)

**查看登录设备**

如果 X 账号被盗后发生恶意登录，用户可以通过查看当前账号的登录设备，然后将恶意登录的设备踢下线。

排查方法：选择“Log out the device shown”，将账号从某个设备注销退出。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZHvGplVZ74mmVhWQwnJrw2Xts64ibcmk2NsPWcIgONd2eiaj6h0icOqWdAtPHiasA2vLHGFeAMdv984A/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZHvGplVZ74mmVhWQwnJrw2WEEORjUufMg5MuXcwFVzIQT8icafC0XUeodAHPIr1KRokgsp7ibvNW8A/640?wx_fmt=png&from=appmsg)

## **安全设置**

###

### **2FA 验证**

用户可以通过开启 2FA 验证，为账号开启双重验证保险，避免密码泄漏后账号直接被接管的风险。

配置方法：Settings → Security and account access → Security → Two-factor authentication

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZHvGplVZ74mmVhWQwnJrw2U8DAmwdibE4CQU5MUYRgicVzXgCRnFhzmrqvsScWcgF5iaJzicYDXKiaLVg/640?wx_fmt=png&from=appmsg)

可以设置如下 2FA 来增强账号的安全性，如短信验证码、身份验证器和安全密钥。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZHvGplVZ74mmVhWQwnJrw2D2icJttFTq1LtCKciaGEEGoAW6paUHoKtZrJYQgEmgTgrwrHZS45IwLw/640?wx_fmt=png&from=appmsg)

**额外的密码保护**

除了设置账号密码和 2FA 外，用户还可以开启额外的密码保护来进一步增强 X 账号安全性。

配置方法：Settings → Security and account access → Security → Additional password protection

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZHvGplVZ74mmVhWQwnJrw22Ihibv02hJMW8pR1wDDlzquh0mMynyMmqibzdnI8R5Vuu88KlUwMFNFg/640?wx_fmt=png&from=appmsg)

##

## **总结**

定期检查授权应用和登录活动是确保账号安全的关键，慢雾安全团队建议用户定期根据排查步骤对 X 账号进行授权排查，从而加强账号的安全性，降低被黑客攻击的风险。如果发现账号被黑，请立即采取措施，修改账号密码，进行授权排查，撤销可疑授权，并对账号进行安全增强设置。

**往期回顾**

[TonConnect SDK 的 Origin 伪造风险分析](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247500083&idx=1&sn=236a3bc7285c68e9636e231d5704a629&chksm=fddebfb4caa936a27719caf94d384e21d77b40ed876748f218ae8568504632200abe713c15e9&scene=21#wechat_redirect)

[黑暗森林之狡诈的网络钓鱼](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247500063&idx=1&sn=5c6890de082e290cd8b2ca660e7afb40&chksm=fddebf98caa9368efcb2f31f9e5dad3ae3a06a33a851587ab0d2bb983f136ff1fd4fcab5b0ff&scene=21#wechat_redirect)

[Web3 安全入门避坑指南｜钱包被恶意多签风险](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247500038&idx=1&sn=00ff98cee22c817942d2e1bce4f8db46&chksm=fddebf81caa93697ba13a1ad0f8eb3baab0c739926912e671c3ac4d81b18467feee1bffae095&scene=21#wechat_redirect)

[慢雾(SlowMist) 为香港浸会大学金融课程获奖者提供“慢雾网络安全奖”](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247500008&idx=1&sn=fa9a8c6b1d89653d784131884f958cce&chksm=fddebe6fcaa93779e7cc92cace20762718781c556b5b6bf15226a693d2b68459b35e637fd06c&scene=21#wechat_redirect)

[慢雾：公链安全审计指南全面升级，并新增 Layer2 安全审计方法](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247499970&idx=1&sn=949d5a2fa1ce82709818e8fcc37ccad0&chksm=fddebe45caa9375310a4fccccd715ec76bb09b9ccfd7f0e692ae3dbca35b1ffdd6fec7138722&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLazKt6yZQQvqiccDeUu8Togv4VUdq4r7iak19Hta2pfbzPrGohPNR71WxPKrBoK9nyibPVL7ssCuW3yA/640?wx_fmt=png)

**慢雾导航**

**慢雾科技官网**

*https://www.slowmist.com/*

**慢雾区官网**

*https://slowmist.io/*

**慢雾 GitHub**

*https://github.com/slowmist*

**Telegram**

*https://t.me/slowmistteam*

**Twitter**

*https://twitter.com/@slowmist\_team*

**Medium**

*https://medium.com/@slowmist*

**知识星球**

*https://t.zsxq.com/Q3zNvvF*

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbCKRaQNEUrvPEphjODejx61A2PcXPPj3dFegU3unrp2nr60oBfYXAZDj99nIXojoia9p6UDy4iaqQw/0?wx_fmt=png)

慢雾科技

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbCKRaQNEUrvPEphjODejx61A2PcXPPj3dFegU3unrp2nr60oBfYXAZDj99nIXojoia9p6UDy4iaqQw/0?wx_fmt=png)

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
---
title: 【安全圈】能伪造通话界面，FakeCall恶意软件变种在安卓手机中传播
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065627&idx=3&sn=926f2a6b02eef61e44cd08f8b9f22c6f&chksm=f36e631bc419ea0d1c7712878321bfaa133b49e743351111cb64d7c9e7e24dcf2e222e84435f&scene=58&subscene=0#rd
source: 安全圈
date: 2024-11-01
fetch_date: 2025-10-06T19:17:56.036716
---

# 【安全圈】能伪造通话界面，FakeCall恶意软件变种在安卓手机中传播

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljSIHBZf6MFQjP0Qt7BmMfFLRibGyIEGibFicAjuxDz1rYVowSeya7cMLZ0Qdg9NmKR5Z6j7piaJG5X0g/0?wx_fmt=jpeg)

# 【安全圈】能伪造通话界面，FakeCall恶意软件变种在安卓手机中传播

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

恶意软件

据Hackread消息，Zimperium's zLabs 的网络安全研究人员发现了 FakeCall 恶意软件的一个新变种，能够诱导受害者拨打诈骗电话，导致身份信息被窃取。

FakeCall 是一种语音钓鱼类型的网络钓鱼恶意软件，一旦安装，就能完全控制住安卓系统手机。而最新的变种还具备了几项新功能：选择性上传特定图像、远程控制屏幕、模拟用户操作、捕获和传输实时视频以及远程解锁设备，这些功能可以捕获敏感文件或用户个人照片。

FakeCall 恶意软件通常从受到攻击的网站或钓鱼邮件中渗透到设备，并请求成为默认呼叫处理程序的权限， 如果获得许可，恶意软件就会获得大量权限。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljSIHBZf6MFQjP0Qt7BmMfF6QRWS62SArpNMPJTgq6lsx0jVsVMWFwGKFPRGhEaibuvHDTsRgC0QDg/640?wx_fmt=jpeg&from=appmsg)攻击链路

根据 Zimperium 与 Hackread分享的博文，攻击者在攻击过程中使用了一种名为 "电话监听器服务 "的功能，这项服务是恶意软件的重要组成部分，使其能够操纵设备的通话功能，从而拦截和控制所有来电和去电，并窃取敏感信息，如一次性密码（OTP）或账户验证码。

恶意软件还能操纵设备显示屏，显示虚假的通话界面，诱骗受害者提供敏感信息。它还可以操纵通话记录来隐藏其恶意活动并控制通话时间。攻击者可以利用这些功能欺骗受害者，使其泄露敏感信息并进一步造成经济上的损失。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljSIHBZf6MFQjP0Qt7BmMfFLtXANH8R8ZC5RGb0Bd9pTB5xQ3lgnObZs14jw3cD8iaPes7BvCHrsOQ/640?wx_fmt=jpeg&from=appmsg)伪造的呼叫界面

此外，该恶意软件还利用安卓辅助功能服务捕获屏幕内容并操纵设备显示屏，在模仿合法手机应用的同时创建欺骗性用户界面。 通过监控来自Stock Dialer 应用程序的事件，并检测来自系统权限管理器和系统 UI 的权限提示。在检测到特定事件时，该恶意软件可以绕过用户同意授予的权限，让远程攻击者控制受害者的设备 UI，从而模拟用户交互并精确操纵设备。

目前谷歌已经调查了受 Scary 恶意软件模仿影响到的应用程序，并表示Google Play 上的所有应用程序都受到保护，不受新变体的影响。为了防范此类恶意软件，建议用户从可信来源下载应用程序，谨慎处理权限请求，并使用具有设备检测功能的移动安全软件。

参考来源：New “Scary” FakeCall Malware Captures Photos and OTPs on Android

***END***

阅读推荐

[【安全圈】2024年9月涉及国内的数据泄露](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065600&idx=1&sn=6d6cbb7552c7286176e5f195fe943183&chksm=f36e6300c419ea1640df39c2a4844793d126205df0f9ee8316581a6a33207a99027d6109ef62&scene=21#wechat_redirect)

[【安全圈】互联网大厂主页疑似遭到篡改？](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065600&idx=2&sn=672e3a8c2a44ab141de706841b2e06db&chksm=f36e6300c419ea16523d84e6bd13e79994f97970c0273b66079a7a14b51d8ab98b488cebb666&scene=21#wechat_redirect)

[【安全圈】非法获取上亿条公民个人信息，一科技公司员工获刑](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065600&idx=3&sn=25fdbf80a473e8ffe0114247ae89cc99&chksm=f36e6300c419ea16094cd436661e031038ce662208961a0ecee58cfdbae007ea3ffd4fb42221&scene=21#wechat_redirect)

[【安全圈】因健身应用轨迹，贴身保镖恐泄露美国总统位置信息](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065600&idx=4&sn=15b26bfc0c1a2d1c033683e786adb151&chksm=f36e6300c419ea16ee1da5f7563c5d408f9256a5f5921f5dc1f7d0b5d668cfaf54a7b7b21876&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

安全圈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

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
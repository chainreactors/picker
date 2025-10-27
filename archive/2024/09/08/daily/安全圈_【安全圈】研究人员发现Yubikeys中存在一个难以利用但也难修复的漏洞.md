---
title: 【安全圈】研究人员发现Yubikeys中存在一个难以利用但也难修复的漏洞
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064191&idx=4&sn=2fe0d56663512b21ba1785d9a22bcd38&chksm=f36e65ffc419ece95bd1e15cc3b1eb19a4fe27400937238106b5b34bde708be50cd7af470869&scene=58&subscene=0#rd
source: 安全圈
date: 2024-09-08
fetch_date: 2025-10-06T18:24:51.346683
---

# 【安全圈】研究人员发现Yubikeys中存在一个难以利用但也难修复的漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliayAgNUicp8k6tBdiaTt9Ne0tbR5flENEHRuVANdZO2mmb8KMJb0VMxbSqNcTo67xIdrBdTZAdpybAA/0?wx_fmt=jpeg)

# 【安全圈】研究人员发现Yubikeys中存在一个难以利用但也难修复的漏洞

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=png&from=appmsg "微信图片_20230927171534.png")

**关键词**

安全漏洞

Yubikeys 是使用最广泛的双因素身份验证 （2FA） 硬件工具之一，某些版本容易受到侧信道攻击。

NinjaLab 的安全专家兼联合创始人 Thomas Roche 发现 YubiKey 5 系列设备包含一个加密漏洞，当攻击者获得对它们的临时物理访问权限时，它们很容易被克隆。

虽然漏洞无法修复，但也很难被利用。

## 了解如何使用 Yubikey

Yubikeys 是由 Yubico 开发的基于 USB 的物理安全设备，在登录在线帐户时增加了一层额外的保护。它们通常用于 2FA，除了密码外，还需要物理设备才能访问您的帐户。

Yubikeys 被许多安全专家认为是多因素身份验证 （MFA） 最安全的硬件选项之一，特别是因为它们通常支持 Fast Identity Online 2 （FIDO2） 标准。

FIDO2 身份验证由 FIDO 联盟和万维网联盟 （W3C） 联合开发，基于公钥加密，比基于密码的身份验证更安全，并且更能抵抗网络钓鱼和其他攻击。

## 14 年未被注意到的侧信道漏洞

在执行他称为 EUCLEAK 的侧信道攻击时，Roche 在许多 YubiKey 产品使用的加密库中发现了一个漏洞，该漏洞允许他克隆这些设备。

侧信道攻击是一种入侵尝试，旨在利用设备或系统的物理特性来提取敏感信息。

研究人员指出，侧信道漏洞是最大的安全元件制造商之一英飞凌科技公司提供的库中的加密漏洞，14 年来一直没有引起注意，并进行了大约 80 次最高级别的通用标准认证评估。

研究人员在公布他的经历结果之前联系了 Yubiso。

## 受影响的 Yubikey 设备

在公开公告中，Yubico 承认了该漏洞，并指定受影响的设备是：

* YubiKey 5 系列5.7 之前的版本
* YubiKey 5 FIPS 系列 5.7 之前的版本
* YubiKey 5 CSPN 系列 5.7 之前的版本
* YubiKey Bio 系列 5.7.2 之前的版本
* 5.7 之前的 Security Keys 系列
* YubiHSM 2 2.4.0 之前的版本
* YubiHSM 2 FIPS 2.4.0 之前的版本

较新的版本不受影响。

## 复杂的 Yubikey 漏洞利用场景

主要制造商表示，该漏洞的严重性为“中等”。

这部分是因为它相对难以利用。罗氏使用价值 11,000 欧元的材料来执行 EUCLEAK 攻击，并可以物理访问该设备——这两个标准可能令人望而却步。

Roche 提供了一个典型的攻击场景，可以成功利用 Yubikey 漏洞：

1. 攻击者窃取了受 FIDO 保护的受害者应用程序帐户的登录名和密码（例如，通过网络钓鱼攻击）
2. 攻击者在有限的时间内对受害者的设备进行物理访问，而受害者没有注意到
3. 由于被盗受害者的登录名和密码（对于给定的应用程序帐户），攻击者在执行侧信道测量时，根据需要多次向设备发送身份验证请求
4. 攻击者悄悄地将 FIDO 设备归还给受害者
5. 攻击者对测量结果执行侧信道攻击，并成功提取链接到受害者应用程序账户的椭圆曲线数字签名算法 （ECDSA） 私钥
6. 攻击者可以在 FIDO 设备或受害者没有注意到的情况下登录受害者的应用程序帐户。换句话说，攻击者为受害者的应用程序账户创建了 FIDO 设备的克隆。只要合法用户不撤销其身份验证凭证，此克隆就会授予对应用程序账户的访问权限。

***END***

阅读推荐

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGyliaz0aAPfSKT3CQcTKrPtCxqXbJamRHkE9mKriasvCEOJ07ydg7Umd9dAxOQDviaZSRfLGRh5EYtnzDA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliaz0aAPfSKT3CQcTKrPtCxqldiaHOapkXapQJn5JTVy1zhXrv184q4sT1S0vy2tySkVupibHHVcEcXg/640?wx_fmt=jpeg)[【安全圈】LiteSpeed 曝出严重漏洞，致使超 600 万 WordPress 网站遭攻击](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064175&idx=2&sn=3f54fca5e0c49722e56e0d3e226be408&chksm=f36e65efc419ecf927842317d91613e7ac1e5b84ddc1ca57b670d4bf60ebfac80f95a068fc18&scene=21#wechat_redirect)

[【安全圈】网络身份证是强制，会影响正常上网？公安部详细回应](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652063868&idx=2&sn=e0e51cc3262a54328e4fee1482c882f1&chksm=f36e643cc419ed2a36eb00a524a91605bcd28b782d15ab7fb662c206140dca0df3a38bac1c1a&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliaz0aAPfSKT3CQcTKrPtCxqKzURpYTic1eAo8eAuDEmMXeJE90lQNibZPiafo12ljibfLM3PBtvMbUyEg/640?wx_fmt=jpeg)[【安全圈】黑客背刺同行，向对方发送信息窃取软件](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064175&idx=3&sn=2d49306130a302f0793dc7e75949ba07&chksm=f36e65efc419ecf9398617670f784c5315357caccba465d5c7416103122a2bbe8c9aa5989866&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliaz0aAPfSKT3CQcTKrPtCxqIe8hNDmDbprVdazmq3FdOGr8vPXw46oB6HKkEX1HAPeGZcvXYqOpqg/640?wx_fmt=jpeg)[【安全圈】被警方逮捕后，Telegram创始人首次公开发声：更安全，更强大](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064175&idx=4&sn=85aec69b16d8c398a97f5c096f282e77&chksm=f36e65efc419ecf9a827d0f895e4aedc4af0a87a08a0b686c42263d02477d04ded8127c11e2c&scene=21#wechat_redirect)

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
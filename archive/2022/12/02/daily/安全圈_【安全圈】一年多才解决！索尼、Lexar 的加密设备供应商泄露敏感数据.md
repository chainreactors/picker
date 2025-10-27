---
title: 【安全圈】一年多才解决！索尼、Lexar 的加密设备供应商泄露敏感数据
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652026116&idx=3&sn=37c197ee72a95e116ec89cd5f1a867b0&chksm=f36f9944c4181052e58eff107549df91978e0db79496090be0504a86c1b2c9a2bb33fdd0e1f3&scene=58&subscene=0#rd
source: 安全圈
date: 2022-12-02
fetch_date: 2025-10-04T00:18:03.546842
---

# 【安全圈】一年多才解决！索尼、Lexar 的加密设备供应商泄露敏感数据

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGylgU7AQyHMBto7BXAPaYHNSA8j3UmibPDQVHNvCEq3NTAbR5kOlLY1wXr7phSZRz0Iia3fgWT80AsbDw/0?wx_fmt=jpeg)

# 【安全圈】一年多才解决！索尼、Lexar 的加密设备供应商泄露敏感数据

安全圈

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGylgU7AQyHMBto7BXAPaYHNSAib1svM50ppMoI1q5WiafHthfeLK5U1oZup9icyDPnia6MicatveFtibaG79g/640?wx_fmt=jpeg)

**关键词**

Sony、Lexar

当用户购买 Sony、Lexar 或 Sandisk USB 密钥或其它任何存储设备时，都会附带一个加密解决方案，以确保数据安全。

据悉，该方案由第三方供应商 ENC Security 开发，然而 近日Cybernews 研究小组披露，该公司在一年多时间里一直在泄露其配置和证书文件。

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGylgU7AQyHMBto7BXAPaYHNSA9VyRHNiacYpn8RIKwuGibD7bK2tHNTngwic8cd0SicQBh97XjvkCGib5Ddg/640?wx_fmt=jpeg)

随着事件发酵，ENC Security 迅速做出回复，声称泄露事件原因是第三方供应商的错误配置，在收到通知后已立刻修复漏洞。

ENC Security 是一家位于荷兰的公司，在全球拥有 1200 万用户，通过其流行 DataVault 加密软件提供“军用级数据保护”解决方案。

**Cybernews 发现安全问题**

从 Cybernews 披露的内容来看， 泄漏服务器内的数据主要包括销售渠道的简单邮件传输协议（SMTP）凭证、单一支付平台的 Adyen 密钥、电子邮件营销公司的 Mailchimp API 密钥、许可支付 API 密钥、HMAC 消息验证码以及以 .pem 格式存储的公共和私人密钥。

2021 年 5 月 27 日到 2022 年 11 月 9日 ，一年多的时间里，任何人都可以公开访问这些数据，直到 Cybernews 向 ENC Security 披露该漏洞后，该服务器才被关闭。

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGylgU7AQyHMBto7BXAPaYHNSAzZ4icEKpbun09Rm2bam9Qf5GGxYtAT2NicF0H8XhTIgibMv0v6pSY5p4g/640?wx_fmt=jpeg)

举个简单的例子，攻击者可能通过销售沟通渠道向客户发送假发票或通过可信的电子邮件地址传播恶意软件来欺骗客户。

此外，由于 Mailchimp API 密钥允许攻击者发送大规模营销活动并查看、收集线索，对攻击者来说无疑具有更大价值。不仅如此，勒索软件运营商也能够利用 .pem 文件里面的密钥开展未经授权的访问，甚至是服务器被接管。Vareikis 一再强调，泄漏一年多的数据对威胁者来说不亚于一个“金矿”。

**ENC Security 公司回应**

在收到并仔细分析 Cybernews 研究小组报告后，ENC Security 迅速采取措施，解决安全问题。ENC Security 发言人表示，公司始终认真对待数据的安全和保护，每一个安全问题都会被彻底研究并采取适当的措施进行补救，必要时也会通知客户进一步加强安全。

ENC Security 也曾出现其它安全事件

Cybernews 研究小组的发现与 2021 年 12 月研究人员 Sylvain Pelissier 的发现一样令人担忧。

去年，Pelissier 演示了在 ENC Security  DataVault 加密软件中发现的几个漏洞，这些漏洞可能允许攻击者在未经检测的情况下，获取用户密码并修改 vault 中的文件。不止于此，DataVaul 软件还使用了“计算工作量不足的密码哈希”，这可能会让攻击者暴力破解用户密码。

当时，ENC Security 承认 DataVault 软件 6 和 7.1 及其衍生版本易受攻击，不久后通过发布升级解决了漏洞。

Vareikis 告诫用户，一些“超级”安全公司喜欢使用类似“军用级”加密等词汇，过度夸大产品能力，进行虚假宣传，对于这种宣传，用户应当始终持怀疑态度。

来源：FreeBuf

***END***

阅读推荐

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGylgU7AQyHMBto7BXAPaYHNSAwL9kicakIzxHhgHqEjbLbmlHvu3Bpbic8LaLIhqpWUttB0Gqkk5MqzuA/640?wx_fmt=jpeg)

# [【安全圈】应对挑战！元宇宙可能成为 2023 年网络攻击的主要途径](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652025972&idx=1&sn=cfd884abb5e3cff179335b50d5ae4257&chksm=f36f9834c41811223cb03635656355deb905e0bbd1ffecd465c1d8c5c8c49f2ec0e3ac8983bd&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGylgU7AQyHMBto7BXAPaYHNSA53Ze5jYAPN0ziapYZJrlnkd3NtbGlQESPXaP0hb9tPj148OViac0U1pQ/640?wx_fmt=jpeg)

# [【安全圈】以威胁国家安全为由，美国禁止销售中兴、海康威视等电信和监控设备](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652025972&idx=2&sn=de6f5b320d1bb645cf46765afd15e72d&chksm=f36f9834c41811227599b505a054256c6c54bd53a64ffe1640df99aa5e5f685b166cbc07d982&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGylgU7AQyHMBto7BXAPaYHNSAmXyvUCX17HIorpmFE0ooiabBbr2QmINq3lx2Ro3iaCKbb209AJUVgiaTw/640?wx_fmt=jpeg)

# [【安全圈】宏碁电脑存在驱动程序漏洞，启动过程中可部署恶意软件](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652025972&idx=3&sn=78efb6a0d35bca6db75a1112c7b97976&chksm=f36f9834c4181122f57ef00f80ef6cfcfdf4687b239883c7e2a98f741b92bc78ec8108e3d1b5&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGylgU7AQyHMBto7BXAPaYHNSAVQb4juM2yhB7iaMu6skKY12c1WLqp2QYy1ZKibj008VHEkjSIWMSSYEg/640?wx_fmt=jpeg)

# [【安全圈】新攻击利用Windows安全绕过 0 day 漏洞投放恶意软件](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652025972&idx=4&sn=d652e648e5bb3117ca53f7bf0aa96cb1&chksm=f36f9834c41811225ffaef84ae60e9f5b6e8d6752f864fa26a5717d7a745bdc621faadd67446&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

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
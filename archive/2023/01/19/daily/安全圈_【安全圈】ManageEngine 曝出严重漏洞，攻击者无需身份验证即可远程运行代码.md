---
title: 【安全圈】ManageEngine 曝出严重漏洞，攻击者无需身份验证即可远程运行代码
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652029924&idx=1&sn=ab547df73b4cfdd2405bade9fcf6ca5b&chksm=f36fefa4c41866b20226cfbe5d0534d62b885ad74f7f219a16a2d8e53328e3d54e43f89d0b27&scene=58&subscene=0#rd
source: 安全圈
date: 2023-01-19
fetch_date: 2025-10-04T04:17:56.140376
---

# 【安全圈】ManageEngine 曝出严重漏洞，攻击者无需身份验证即可远程运行代码

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGyliaLAngoF0AzBMb3CFtrVSkxJVyf74UggZxnZdUF9AV9YTVUKiaVX6o1nhBoMS1Q8O993rT93QywL9g/0?wx_fmt=jpeg)

# 【安全圈】ManageEngine 曝出严重漏洞，攻击者无需身份验证即可远程运行代码

安全圈

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGyljsJVJHhaCOeUkoze16FrNjE24yjZVib01Tl7diaq0PGm6wazJMuo3K51rsrhdiagwEDicqXQtmMQlIJQ/640?wx_fmt=jpeg)

**关键词**

漏洞

IT之家 1 月 17 日消息，来自 Horizon3 Attack Team 的网络安全研究人员公布了一个概念验证 (PoC) 漏洞，这一漏洞存在于诸多 VMware 产品中。

据介绍，CVE-2022-47966 漏洞可允许攻击者无需身份验证即可在 ManageEngine 服务器中远程执行代码，而这些服务器在之前的某个时间点启用了基于 saml 的单点登录（SSO）协议，因此关闭该功能也无法解决任何问题。

研究人员指出，易受攻击的端点使用了一种名为 Apache Santuario 的过时第三方依赖项，就是这个原因导致攻击者可以通过 NT AUTHORITY\SYSTEM 身份远程执行代码，从而完全控制系统。

目前来看，这个漏洞很容易被利用，并且是攻击者在网上“'spray and pray”的有利方式。研究人员警告说，该漏洞允许作为 NT AUTHORITY\SYSTEM 远程执行代码，基本上可以使攻击者完全控制该系统”。

“如果用户确定他们的信息被泄露了，就需要进行额外的调查，以确定攻击者所造成的损害。一旦攻击者获取到对端点的系统级访问权限，攻击者就可能开始通过 LSASS 转储凭据或者利用现有的公共工具来访问存储的应用程序凭据，以进行横向转移。”

IT之家提醒，目前 Zoho 已经发布了相应的补丁，有需要的用户请尽快下载。

值得一提的是，研究人员通过 Shodan 搜索未打补丁的端点后依然发现了“数千个”易受攻击的 ManageEngine 产品、ServiceDesk Plus 和 Endpoint Central 实例，希望大家提高警惕。

目前，业内还没有关于 CVE-2022-47966 被恶意利用的报告，但如果 IT 管理员选择无视这一漏洞，则早晚会出现受害者。

***END***

阅读推荐

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGylghZXxV8UdubcwzGYPwHUfzwZMVBFLcSCMQ8jsHsnsiaZYszzsua7Gr4BV7gPhPzH8Du63fcMCfRxA/640?wx_fmt=jpeg)[【安全圈】倒卖信息10万余条 安徽全椒警方破获一侵犯公民个人信息案](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652029906&idx=1&sn=b66273f638164f656756690090f60d56&chksm=f36fef92c418668472274157abcd4433c096512998abcd989785bd2bf93ce248b6132f6b4f66&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ibias7xAsaLBuzW9sPX2ItESic0ZkrbWIoy68qVBib1O4ibXBzfoBpxHYFndXpaHh3c0gX7ZrR7EhLAkg/640?wx_fmt=jpegwxfrom=5wx_lazy=1wx_co=1)[【安全圈】雷朋眼镜制造商被网络犯罪分子盗走2.72亿美元，缘于背后的一起杀猪盘](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652029906&idx=2&sn=0d82f704bc4eca74dcc3380390f644e3&chksm=f36fef92c418668405d225391b100bfa5d65c0eacc05f8ace61f9e5cb2d70ad0a301faf0a45b&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGylghZXxV8UdubcwzGYPwHUfzYUbPxJUsK9Z2M9aqgyyhqwg5pOPk6JG8XVC2M44zhibp5TwqHjyNqtw/640?wx_fmt=jpeg)[【安全圈】历时500多天，滴滴出行被放出来了](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652029906&idx=3&sn=0138b6bf288913f87aeac45d40e2ac31&chksm=f36fef92c4186684aa9168f18053f54f0b20d049ec715d5f35413d6574bbccc8da6456f04c2e&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylghZXxV8UdubcwzGYPwHUfzaY1ib9Mn6du02qhR73oKSicY1kko7rApZQy5Y3v8ZeZMsNOaxZAXVUag/640?wx_fmt=png)[【安全圈】数字情报公司Cellebrite1.7TB数据泄露](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652029906&idx=4&sn=f39c924fb301c47679e7d33ea803bd38&chksm=f36fef92c41866845c79b966890b6c7e72a76c7847a6a7141da28c57185c43e80dd4fb59f4a4&scene=21#wechat_redirect)

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
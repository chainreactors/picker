---
title: 【安全圈】Fortinet VPN已修复的缓冲区溢出零日漏洞，可执行任意代码
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652029924&idx=4&sn=7f882b1b2a8760c9911800eebb3782d1&chksm=f36fefa4c41866b22955936529e3f96cb8a9b2b588cd47f271a7f26d2c4a450762717e023502&scene=58&subscene=0#rd
source: 安全圈
date: 2023-01-19
fetch_date: 2025-10-04T04:17:58.352252
---

# 【安全圈】Fortinet VPN已修复的缓冲区溢出零日漏洞，可执行任意代码

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGyliaLAngoF0AzBMb3CFtrVSkxuqEyibL4ibukfWFht9dHW50eWtp9rHYrAlxecibKiaJGy2qSQyctBt5O0w/0?wx_fmt=jpeg)

# 【安全圈】Fortinet VPN已修复的缓冲区溢出零日漏洞，可执行任意代码

安全圈

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGyljsJVJHhaCOeUkoze16FrNjE24yjZVib01Tl7diaq0PGm6wazJMuo3K51rsrhdiagwEDicqXQtmMQlIJQ/640?wx_fmt=jpeg)

**关键词**

漏洞

在最近的网络安全观察中发现，Fortinet公司上个月已解决的 FortiOS SSL-VPN 中的一个零日漏洞，被不知名的攻击者利用在针对政府和其他大型组织的攻击中。该漏洞利用的复杂性表明它是高级攻击者，而且它高度针对政府或与政府相关的目标。

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGyliaLAngoF0AzBMb3CFtrVSkxBkN6ny6BajdWba14DicesmwvWPTQqTawzkIiaoJn5hM7jYUFkbOZSQicw/640?wx_fmt=png)

安全研究人员在对感染链进行分析时发现，最终目标是部署一个为 FortiOS 修改的通用 Linux 植入物，该植入物能够破坏 Fortinet 的IPS入侵防御系统模块，并与远程建立连接以下载其他恶意软件并执行命令。

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGyliaLAngoF0AzBMb3CFtrVSkxkSsbUoggLHIqvB2BNiavqa9fcJO3L8HkV7cnz7RG8vx4boMWdODFI5w/640?wx_fmt=png)

此外，作案手法揭示了使用混淆来阻止分析以及使用“高级功能”来操纵 FortiOS 日志记录和终止日志记录进程以保持未被发现。

攻击者还会搜索 FortiOS 中的事件日志 elog 文件，在内存中解压后，搜索攻击者指定的字符串，将其删除，然后重建日志，以此来隐藏攻击行为。

极牛攻防实验室研究人员表示，利用该漏洞需要深入了解 FortiOS 和底层硬件，并且攻击者拥有对 FortiOS 的不同部分进行逆向工程的能力。

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
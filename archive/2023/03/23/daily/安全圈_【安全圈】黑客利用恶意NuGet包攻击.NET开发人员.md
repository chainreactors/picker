---
title: 【安全圈】黑客利用恶意NuGet包攻击.NET开发人员
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652031634&idx=4&sn=5d307df654d046f0bf5b88b5de729708&chksm=f36fe6d2c4186fc4f3b290462c39823528843507eb78a8144f969120441d77a258e7a4331065&scene=58&subscene=0#rd
source: 安全圈
date: 2023-03-23
fetch_date: 2025-10-04T10:23:12.277601
---

# 【安全圈】黑客利用恶意NuGet包攻击.NET开发人员

![cover_image](https://mmbiz.qlogo.cn/mmbiz_jpg/aBHpjnrGylg8PwZL29AibicqVTypKpzzLkFxiaXMrok2mCbHPkbDm3KzVCr8TJic7Kn1vgpBBAa23KFfOibEZ2iabhjA/0?wx_fmt=jpeg)

# 【安全圈】黑客利用恶意NuGet包攻击.NET开发人员

安全圈

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGylgSxa9I02IBd3bgLEhwfJCeRibw3LEjMujeAhD2CvyiaVCZJVHGHODbkPx3pViaX0sAibZsDun6sicUzdQ/640?wx_fmt=jpeg)

**关键词**

黑客

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylg8PwZL29AibicqVTypKpzzLkjofibRXPg42w6k8Sm1CNOP9EXPmp85ibExIrqU1Cotu6rPFmnqDHliaHw/640?wx_fmt=png)

威胁攻击者通过 NuGet 存储库提供的加密货币窃取程序瞄准并感染 .NET 开发人员，并通过打字抓取模拟多个合法软件包。

根据 JFrog 安全研究人员 Natan Nehorai 和 Brian Moussalli 的说法，其中三个在一个月内被下载了超过150000次，他们发现了这个正在进行的活动。虽然大量下载可能表明大量 .NET 开发人员的系统遭到破坏，但也可以解释为攻击者试图使其恶意 NuGet 包合法化。JFrog 安全研究人员表示：“前三个软件包的下载次数令人难以置信——这可能表明攻击非常成功，感染了大量机器。  ”

“然而，这并不是攻击成功的完全可靠指标，因为攻击者可能会自动夸大下载计数（使用机器人）以使软件包看起来更合法。”威胁行为者在创建 NuGet 存储库配置文件时还使用了域名仿冒来冒充使用 NuGet .NET 程序包管理器的 Microsoft 软件开发人员的帐户。

***END***

阅读推荐

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGylia5hKib3cekyj7UTNhjtKlqvgj1UsH6229rYGOfbDele2ALm9vbqy7pAtEsp7AXaVlSWEcQ1h1Jbibw/640?wx_fmt=jpeg)[【安全圈】“扫码送礼品”实为窃取个人信息！九江一特大跨省犯罪团伙落网](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652031607&idx=1&sn=ab12fc9b78ff8feafdf483ee638159c5&chksm=f36fe637c4186f21ccf5ad5855c3d8913ffb0d6021ab456d59fe661b06979b9d2dd0880c210c&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGylia5hKib3cekyj7UTNhjtKlqvUs0R275gkEL7KnL8bVntv62FAMYBVgZ2EFUcOXzDqnmZ3A23lmm9xw/640?wx_fmt=jpeg)[【安全圈】决不妥协！法拉利被黑客入侵后拒绝支付赎金](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652031607&idx=2&sn=4a9f8f0af4e3382232a8fec0cbc1bdd7&chksm=f36fe637c4186f218767cb4ec9758c17863e5ae6192ae8e94c8aaf9c825eb86db8069fae1c7a&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGylg8PwZL29AibicqVTypKpzzLkhH7xqFRJ4FsunMP6tbSP4L5qdffNB0vicbaYNrSG768eHanOslSia7Vg/640?wx_fmt=jpeg)[【安全圈】ChatGPT Plus 服务存在 BUG：支付页面会随机曝光用户注册邮箱](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652031607&idx=3&sn=a23ede213d8a5ecf00ecd797f9ac9e38&chksm=f36fe637c4186f2138927f4bd0849fdc8ce0b14b8568f41caeef955dcc2e8d1b34f0104c62de&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGylg8PwZL29AibicqVTypKpzzLkKib1f9bjAQtv2DvBAibwibr3WJDWOTLOELEuWNfRDyhAL1zeDpKfWeo4w/640?wx_fmt=jpeg)[【安全圈】俄罗斯黑客利用 Outlook 漏洞窃取 NTLM 哈希](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652031607&idx=4&sn=446f23d3fdddc39b79f53ad2e8c8523f&chksm=f36fe637c4186f213283c3cb2cffe7c9b8e9e27f9db35c73e6f802fba3decdac770f66297ca5&scene=21#wechat_redirect)

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
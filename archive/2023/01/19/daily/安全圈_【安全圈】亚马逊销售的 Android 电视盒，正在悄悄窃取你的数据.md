---
title: 【安全圈】亚马逊销售的 Android 电视盒，正在悄悄窃取你的数据
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652029924&idx=2&sn=561b62afa7a14cca208d8d06223e1260&chksm=f36fefa4c41866b2694703ff3baf804a8e4df3bd2ae1b4a17ab4386d6d0588fdbe9cc3d9c9bd&scene=58&subscene=0#rd
source: 安全圈
date: 2023-01-19
fetch_date: 2025-10-04T04:17:56.874338
---

# 【安全圈】亚马逊销售的 Android 电视盒，正在悄悄窃取你的数据

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGyliaLAngoF0AzBMb3CFtrVSkxkU3EvMVNtpUczpSPFzNjic855H1iaYibPwfMibdLedRyhG7SHy6GQCX7Lw/0?wx_fmt=jpeg)

# 【安全圈】亚马逊销售的 Android 电视盒，正在悄悄窃取你的数据

安全圈

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGyljsJVJHhaCOeUkoze16FrNjE24yjZVib01Tl7diaq0PGm6wazJMuo3K51rsrhdiagwEDicqXQtmMQlIJQ/640?wx_fmt=jpeg)

**关键词**

恶意软件

安全研究员 Daniel Milisic 发现他在亚马逊上购买的 T95 Android 电视盒感染了复杂的预装恶意软件。

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGyliaLAngoF0AzBMb3CFtrVSkxQfEoueCnqLicTibe2CbSxqdjXZ5hicLpKEth1l2NWegtOQGPVMRKWia3icw/640?wx_fmt=jpeg)

这款 Android 电视盒型号可在亚马逊和全球速卖通上以低至 40 美元的价格购买。

该设备配备了 Android 10（带有可用的 Play 商店）和 Allwinner H616 处理器。Milisic 在其固件中发现了预加载的恶意软件。

Milisic 购买了 T95 Android 电视盒来运行 Pi-hole，这是一个 Linux 网络级广告和互联网跟踪器拦截应用程序。

运行 Pi-hole 后，他注意到该盒子正在到达与恶意软件活动相关的地址。

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGyliaLAngoF0AzBMb3CFtrVSkxL63r80FBkrRLwJibewGhvacpoLn1H9FSugIfITu7tdbFSf0uNzt7tpA/640?wx_fmt=jpeg)

“在搜索完成后，专家试图删除该恶意软件。在使用 tcpflow 和 nethogs 监控流量的恶意软件层之上发现了有问题的进程/APK，然后将其从 ROM 中删除。但有些无法追踪的恶意软件已经深深地嵌入到 ROM 中。它是非常复杂的恶意软件，其运行方式类似于 CopyCatin。

该设备使用使用测试密钥签名的 Android 10 操作系统。专家还发现它具有可通过以太网端口访问的 Android 调试桥 (ADB)。

设备固件中嵌入的恶意代码类似于 Android CopyCat恶意软件。专家指出，他测试的所有 AV 产品都无法检测到威胁。

Milisic 还设计了一个技巧来阻止恶意软件使用 Pi-hole 将命令和控制服务器 YCXRL.COM 的 DNS 更改为 127.0.0.2。

他还创建了一个 iptables 规则，将所有 DNS 重定向到 Pi-hole，因为恶意软件/病毒/任何无法解析的东西都会使用外部 DNS。

通过这样做，C&C 服务器最终会攻击 Pi-hole 网络服务器，而不是将我的登录名、密码和其他 PII 发送到 Linode（在撰写本文时目前 为 139.162.57.135）。

请注意，Milisic 提出的解决方案并没有删除恶意代码或禁用它，它只是消除了它对其操作的干扰。

为了确定 s T95 Android 电视盒是否已被感染，研究人员建议检查是否存在名为：

> `/data/system/Corejava`

和一个名为

> `/data/system/shared_prefs/open_preference.xml`？

Milisic 无法测试来自同一供应商或型号的其他设备以确定它们的固件是否也被感染。

最后，米利西奇总结道：“不要相信 AliExpress 或亚马逊上的廉价 Android 盒子，它们的固件带有测试密钥签名。他们正在窃取您的数据（除非您可以查看 DNS 日志）并且不留痕迹！”

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
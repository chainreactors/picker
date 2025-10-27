---
title: 【安全圈】朝鲜黑客创建经过安全验证的恶意软件攻击macOS系统
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066112&idx=4&sn=5b9242cdb5d2263f743eae03dcbe82d0&chksm=f36e7d00c419f41651171aad9c644ce17a7b061075eb069737ae2c80576eb4d36c322befe171&scene=58&subscene=0#rd
source: 安全圈
date: 2024-11-22
fetch_date: 2025-10-06T19:17:04.988303
---

# 【安全圈】朝鲜黑客创建经过安全验证的恶意软件攻击macOS系统

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylggLicm6zgDUAd59I5kicYGLSLiaNGQdBU3qyvV32jZKaMTcMczzA4UiclYibrWRE0ziapYV1Ziaxsh0nPsw/0?wx_fmt=jpeg)

# 【安全圈】朝鲜黑客创建经过安全验证的恶意软件攻击macOS系统

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

恶意软件

据BleepingComputer消息，朝鲜黑客正使用 Flutter 创建的木马记事本应用程序和扫雷游戏来攻击苹果 macOS 系统，这些应用程序具有合法的苹果开发人员 ID 签名和公证。

这些暂时经过了苹果安全检查的应用涉及窃取加密货币，与朝鲜黑客长期在金融盗窃方面的兴趣一致。根据发现该活动的 Jamf Threat Labs 的说法，该活动看起来更像是一场绕过 macOS 安全的实验，而不是一场成熟且高度针对性的操作。

从 2024 年 11 月开始，Jamf 在 VirusTotal 上发现了多个应用程序，这些应用程序对所有 AV 扫描似乎完全无害，但展示了“第一阶段”功能，连接到与朝鲜行为者相关的服务器。

这些应用程序均使用谷歌的 Flutter 框架为 macOS 构建，该框架使开发人员能够使用以 Dart 编程语言编写的单个代码库为不同的操作系统创建本地编译的应用程序。

Jamf研究人员表示，攻击者在基于 Flutter 的应用程序中嵌入恶意软件并非闻所未闻，但却是第一次看到攻击者使用它来攻击 macOS 设备。

由于嵌入在动态库 （dylib） 中，该库由动态库 （dylib） 在运行时加载，使用这种方法不仅为恶意软件开发者提供了更多功能，而且还使恶意代码更难检测。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylggLicm6zgDUAd59I5kicYGLSpA1ibdO4icicT7OHsHXx84nsiallVI3ef2wChVynW7HfGlhzibrVbJZL2icA/640?wx_fmt=jpeg&from=appmsg)Flutter 应用程序布局

在进一步分析其中一款名为 New Updates in Crypto Exchange （2024-08-28）的应用程序时，Jamf 发现 dylib 中的混淆代码支持 AppleScript 执行，使其能够执行从命令和控制 （C2） 服务器发送的脚本。该应用程序打开了一个适用于 macOS 的扫雷游戏，其代码可在 GitHub 上免费获得。

Jamf 发现的 6 个恶意应用程序中有 5 个具有用合法的开发人员 ID 签名，并且恶意软件已通过公证，这意味着这些应用程序被苹果的自动化系统扫描并被认为安全。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylggLicm6zgDUAd59I5kicYGLSBCdNoS1Zzgd5u4OicteiaAS319BquAxnMgW3IwIfQA8VbT9JNghon0uA/640?wx_fmt=jpeg&from=appmsg)经过安全签名、带有木马的扫雷游戏

Jamf 还发现了两款基于 Golang 和 Python 变体的应用，两者都向一个已知的与朝鲜有关联的域 "mbupdate.linkpc[.]net "发出网络请求，并具有脚本执行功能。

目前苹果已经撤销了 Jamf 发现的应用程序签名，因此这些应用如果加载到最新的 macOS 系统上将无法绕过 Gatekeeper 防御。

然而，目前尚不清楚这些应用程序是否曾经用于实际操作，或者仅用于“在野”测试中，以评估绕过安全软件的技术。

参考来源：North Korean hackers create Flutter apps to bypass macOS security

***END***

阅读推荐

[【安全圈】苹果手机72小时不用会自动锁死？](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066097&idx=1&sn=6b2503a2e569d80705cada518019361e&chksm=f36e7d71c419f4675e3986754fc7b32cd6d7589cac2505e25c84a51ded871da048608e7fe980&scene=21#wechat_redirect)

[【安全圈】涉嫌强迫用户共享数据，印度对Meta处以2500万美元罚款](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066097&idx=2&sn=1a5dd1ca6f2eb61c32d863fb63f4c5f8&chksm=f36e7d71c419f4677edcbb49aa84592cb0b2db6ffdfe051b4cad624bd7567c52e9f0ba1802fd&scene=21#wechat_redirect)

[【安全圈】苹果发布紧急安全更新修复WebKit引擎中的漏洞 黑客已经利用漏洞展开攻击](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066097&idx=3&sn=0e0cc754f2cdc596b5f8419a8fa6f7a5&chksm=f36e7d71c419f467daf3ea8cddb360e80ba1bf2d4166d38a18b9e3f18237b4be22f6661fe72a&scene=21#wechat_redirect)

[【安全圈】越来越多的国家正在为“黑客”松绑？](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066097&idx=4&sn=4c89dea98b272ff7dffa7f78d293c288&chksm=f36e7d71c419f467dbcdf3ea7de6e01f01c01afb2d854b3a7651a5f21daec878f96818777f10&scene=21#wechat_redirect)

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
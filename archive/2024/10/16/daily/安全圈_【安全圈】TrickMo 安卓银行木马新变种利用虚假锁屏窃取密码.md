---
title: 【安全圈】TrickMo 安卓银行木马新变种利用虚假锁屏窃取密码
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065256&idx=3&sn=db9a05a7cb472260591425ee387b49ef&chksm=f36e61a8c419e8be43d4f3953b52b2ac31136bd4bd05c846f86a8083c861da3244bea490f740&scene=58&subscene=0#rd
source: 安全圈
date: 2024-10-16
fetch_date: 2025-10-06T18:54:12.199485
---

# 【安全圈】TrickMo 安卓银行木马新变种利用虚假锁屏窃取密码

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljhP5K1N0lvmFx8KzoW6LVPn5yiciaEkpicHdeibNDI7U30BUwl5zs3mgO8SPdb5Am0FiakHt452qjSkYQ/0?wx_fmt=jpeg)

# 【安全圈】TrickMo 安卓银行木马新变种利用虚假锁屏窃取密码

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=png&from=appmsg "微信图片_20230927171534.png")

**关键词**

木马病毒

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljhP5K1N0lvmFx8KzoW6LVPBWOsH7O11ryx7HIN1yiactgrH6lGpB0q0pZ0X18dibMX9R3BhZs4sicHw/640?wx_fmt=jpeg&from=appmsg)

近期，研究人员在野外发现了 TrickMo Android 银行木马的 40 个新变种，它们与 16 个下载器和 22 个不同的命令和控制（C2）基础设施相关联，具有旨在窃取 Android 密码的新功能。

Zimperium 和 Cleafy 均报道了此消息。

TrickMo 于 2020 年首次被 IBM X-Force 记录在案，但人们认为它至少从 2019 年 9 月开始就被用于攻击安卓用户。

## 新版 TrickMo 利用虚假锁屏窃取安卓密码

新版 TrickMo 的主要功能包括一次性密码（OTP）拦截、屏幕录制、数据外渗、远程控制等。

该恶意软件试图滥用强大的辅助功能服务权限，为自己授予额外权限，并根据需要自动点击提示。

该银行木马能够向用户提供各种银行和金融机构的钓鱼登录屏幕覆盖，以窃取他们的账户凭据，使攻击者能够执行未经授权的交易。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljhP5K1N0lvmFx8KzoW6LVPOuSoPGWSgIvrZ0iciaq6PjjBteV2ZKXkRdGiagSfKz0caluHHqR8MHkyw/640?wx_fmt=jpeg&from=appmsg)

攻击中使用的银行业务覆盖，来源：Zimperium

Zimperium 分析师在剖析这些新变种时还报告了一种新的欺骗性解锁屏幕，它模仿了真正的安卓解锁提示，旨在窃取用户的解锁模式或 PIN 码。

Zimperium解释称：欺骗性用户界面是一个托管在外部网站上的HTML页面，以全屏模式显示在设备上，使其看起来像一个合法的屏幕。

当用户输入解锁模式或 PIN 码时，页面会将捕获的 PIN 码或模式详情以及唯一的设备标识符（Android ID）传输到 PHP 脚本。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljhP5K1N0lvmFx8KzoW6LVPInJ2OynPYBdTokKCtVNs0cJtAE0z4kfoTznxhiaRwGtM2XQrmGtaHkA/640?wx_fmt=jpeg&from=appmsg)

TrickMo 展示的伪造安卓锁屏，来源：Zimperium

通过窃取 PIN 码，攻击者可以在设备不受监控时（可能是在深夜）解锁设备，从而在设备上实施欺诈。

## 暴露的受害者

由于 C2 基础设施的安全防护不当，Zimperium 还能够确定至少有 13000 名受害者受到了该恶意软件的影响，其中大部分位于加拿大，还有相当数量的受害者位于阿拉伯联合酋长国、土耳其和德国。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljhP5K1N0lvmFx8KzoW6LVPbOBo5MQ7NBoL7ruFbnPrUgvwkfnQ2gdPzN2TZtNVlBA6FQRIXQ73VA/640?wx_fmt=jpeg&from=appmsg)

TrickMo 受害者热图，来源：Zimperium

据 Zimperium 称，这一数字与 “多个 C2 服务器 ”相对应，因此 TrickMo 受害者的总数可能更高。另外，分析发现，每当恶意软件成功渗出凭证时，IP列表文件就会定期更新。在这些文件中，研究人员发现了数以百万计的记录，这表明被入侵的设备数量庞大，威胁行为者访问了大量敏感数据。

由于 C2 基础设施配置不当，可能会将受害者数据暴露给更广泛的网络犯罪社区，Cleafy 此前一直未向公众公布入侵指标。Zimperium 现在选择在 GitHub 存储库中发布所有信息。

然而，TrickMo 的目标范围似乎足够广泛，涵盖了银行以外的应用程序类型（和账户），包括 VPN、流媒体平台、电子商务平台、交易、社交媒体、招聘和企业平台。

由于 C2 基础设施配置不当，可能会将受害者数据暴露给更广泛的网络犯罪社区，Cleafy 此前一直未向公众公布入侵指标，但 Zimperium 现在选择在 GitHub 存储库中发布所有信息。

据悉，TrickMo 目前是通过网络钓鱼传播的，因此为了尽量减少感染的可能性，应避免从不认识的人通过短信或直接消息发送的 URL 下载 APK。

Google Play Protect 可以识别并阻止 TrickMo 的已知变种，因此确保它在设备上处于激活状态对于抵御恶意软件至关重要。

参考来源：TrickMo malware steals Android PINs using fake lock screen (bleepingcomputer.com)

***END***

阅读推荐

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylhIRRy7YakD1vW3pJqde1NQ7pIUBOYAGjnqOxaCAlkWibiasCCka7gzEKBVG066crBWJrBoBZicTdj3A/640?wx_fmt=png)[【安全圈】这就很有意思：谷歌似乎要让Android系统可以直接运行Linux软件](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065207&idx=1&sn=2483fecda412b57897dd5eaeca451bb2&chksm=f36e61f7c419e8e10e4736ff24a84340716e928688e4c23e957ca00f9097420f4f638d6ed427&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhIRRy7YakD1vW3pJqde1NQl6P9CYibZKkVPzMwKOxMhrPOADqYv3tz0t7pMr5Vnic3Se9d0OsLt9rw/640?wx_fmt=jpeg)[【安全圈】威胁升级！伊朗APT34组织针对阿联酋及海湾关键基础设施发动攻击](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065207&idx=2&sn=5d2a6ee8cad3c1a93fd0258350d9c10e&chksm=f36e61f7c419e8e16198b5842f83c4e50a87fc6d753fd51721b9b6f94fe5110bdf922327062e&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhIRRy7YakD1vW3pJqde1NQrR7QBledFKCkumUyPAXEhwlOFhBE8xh8cgBr2ibNibUmWCV6H268vpEg/640?wx_fmt=jpeg)[【安全圈】低成本恶意软件泛滥，能窃取多个浏览器存储的个人数据](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065207&idx=3&sn=5d89471d200697e40710c3a07232eba7&chksm=f36e61f7c419e8e1fdafbc003a558fb38d81c13aa33f44924c31ae747de0cc821fab24d0b293&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylhIRRy7YakD1vW3pJqde1NQdWLuKxqSOWhq1k8icH495NM4o8sicq4X6u97uwWdCzZlHEokWaC8xibmQ/640?wx_fmt=png)[【安全圈】一种名为 perfctl 的 Linux 恶意软件在过去 3 - 4 年瞄准配置错误的 Linux 服务器](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065207&idx=4&sn=461cec5353ae7f3583dde92f719b667f&chksm=f36e61f7c419e8e1775062eeab2eaf3ee8fcd24f2acde0f36dc0d98247d87a50bb28f0ff15bb&scene=21#wechat_redirect)

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
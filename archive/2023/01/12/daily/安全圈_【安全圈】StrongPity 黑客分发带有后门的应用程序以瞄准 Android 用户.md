---
title: 【安全圈】StrongPity 黑客分发带有后门的应用程序以瞄准 Android 用户
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652029704&idx=2&sn=a96c38dea4b96176edb61245d8f0cd8e&chksm=f36fef48c418665e6bf377825ff4667dd02af3a6c3bde8aaeb3099ae32b00834b3c7d2b281a8&scene=58&subscene=0#rd
source: 安全圈
date: 2023-01-12
fetch_date: 2025-10-04T03:40:01.522006
---

# 【安全圈】StrongPity 黑客分发带有后门的应用程序以瞄准 Android 用户

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGylg7we0iaX56CjTnibV5yCpQ4XRltW7nrR4NkKkv9w77PbianbQfXd0uqDAoiaNbay16w4bMicHXnT5N6Rw/0?wx_fmt=jpeg)

# 【安全圈】StrongPity 黑客分发带有后门的应用程序以瞄准 Android 用户

安全圈

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGyljTLQCV26ymfwSjaUUfbvribzO4ObBJcvsl0EsuPKuJLAoEZQGmmmj90iaV6SwpxCPUZ8cicOJGBoMLA/640?wx_fmt=jpeg)

**关键词**

恶意软件

名为StrongPity的高级持续性攻击 (APT) 组织通过一个冒充名为Shagle的视频聊天服务的虚假网站，以木马化版本的 Telegram 应用程序瞄准 Android 用户。

“一个模仿 Shagle 服务的山寨网站被用来分发 StrongPity 的移动后门应用程序，”ESET 恶意软件研究员 Lukáš Štefanko在一份技术报告中说。“该应用程序是开源 Telegram 应用程序的修改版本，使用 StrongPity 后门代码重新打包。”

StrongPity，也被称为 APT-C-41 和 Promethium，是一个从 2012 年开始活跃的网络间谍组织，其大部分行动集中在叙利亚和土耳其。卡巴斯基于 2016 年 10 月首次公开报告了该组织的存在。

此后，该组织的活动范围扩大到涵盖非洲、亚洲、欧洲和北美的更多目标，入侵利用水坑攻击和网络钓鱼来激活杀伤链。

StrongPity 的主要特征之一是它使用假冒网站，这些网站声称提供各种软件工具，只是为了诱骗受害者下载受感染的应用程序版本。

2021 年 12 月，Minerva Labs披露了一个三阶段攻击序列，该序列源于看似良性的 Notepad++ 安装文件，安装后将后门上传到受感染的主机上。

同年，专家观察到StrongPity 首次部署了一款 Android 恶意软件，它能够入侵叙利亚电子政府门户网站并将官方 Android APK 文件替换为流氓文件。

ESET 的最新发现突出了一种类似的作案手法，该作案手法旨在分发更新版本的 Android 后门有效荷载，该后门有效荷载能够记录电话呼叫、跟踪设备位置并收集 SMS 消息、通话记录、联系人列表和文件。

此外，授权恶意软件可访问权限使其能够从各种应用程序（如 Gmail、Instagram、Kik、LINE、Messenger、Skype、Snapchat、Telegram、Tinder、Twitter、Viber 和微信）中窃取信息。

此次后门功能隐藏在 2022 年 2 月 25 日左右可供下载的合法版本的 Telegram Android 应用程序中。也就是说，虚假的 Shagle 网站目前不再活跃。

也没有证据表明该应用程序已在官方 Google Play 商店中发布。目前尚不清楚潜在受害者是如何被引诱到假冒网站的。

Štefanko 指出：“恶意域名是在同一天注册的，因此山寨网站和假冒的 Shagle 应用程序可能从那天起就可以下载了。”

攻击的另一个值得注意的方面是 Telegram 的篡改版本使用与正版 Telegram 应用程序包名称相同，这意味着后门变体无法安装在已经安装 Telegram 的设备上。

Štefanko 说：“这可能意味攻击者首先诱导受害者，并迫使他们从设备上卸载 Telegram（如果安装了 Telegram），或者该活动的重点是很少使用 Telegram 进行通信的国家。”

***END***

阅读推荐

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGyljTLQCV26ymfwSjaUUfbvribm8le5UnfibToEkDbkq4FczF5wap6ggOAiavmzA8UQxh2RT78tKJo6gAw/640?wx_fmt=jpeg)[【安全圈】违规给“挖矿”企业融资24亿元！肖毅案细节曝光](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652029660&idx=1&sn=07d732660245c513a705259742933590&chksm=f36fee9cc418678a0505b1b0ce08c64ece3fc64e17f848f339cacc93d68ef4afbbab3f70074f&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGyljTLQCV26ymfwSjaUUfbvribq7sticL2Z2JJKKbL8UrRQnuXYakX51X9sc3pNN3Ik9s9gxFV4fd8Oiaw/640?wx_fmt=jpeg)[【安全圈】俄罗斯黑客再度出击，美国重要核实验室被攻击](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652029660&idx=2&sn=c925de26844684f4ce65a1949c0e66f3&chksm=f36fee9cc418678a154e985cabb4a4bb5659c054412d101ae43babfd3d3b647c9bba63c55a35&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGyljTLQCV26ymfwSjaUUfbvrib1CSaJiba5y8X61FtV4OZVcL6a67cqCm690FyI6TR7Viar9ym1m9bhS2Q/640?wx_fmt=jpeg)[【安全圈】英国多所学校数据遭大规模泄露，教育行业成勒索软件的主目标](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652029660&idx=3&sn=6b9f19120750421a34bea8321b06e611&chksm=f36fee9cc418678aef9f7ba35e795827b91756017c55addc392d83bc3ada9fac6b706e17213c&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGyljTLQCV26ymfwSjaUUfbvribRzl8rWTOB2OBNmYudH1W3hbuY89lPegWPiczowAY8iav9EIAg7EpY0Aw/640?wx_fmt=png)[【安全圈】国内一城市发布元宇宙三年行动计划](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652029660&idx=4&sn=90aae98b466ce05549d091ef2429c196&chksm=f36fee9cc418678a9b55855b48f4210534035e9dce4d8cc9f3243ae69b6cf5c59f46c37e5205&scene=21#wechat_redirect)

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
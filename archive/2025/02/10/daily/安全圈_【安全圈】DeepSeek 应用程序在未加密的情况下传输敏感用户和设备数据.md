---
title: 【安全圈】DeepSeek 应用程序在未加密的情况下传输敏感用户和设备数据
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067721&idx=1&sn=fd6e5278ffdaa6a2bc2cd75bf7489edf&chksm=f36e7bc9c419f2df4d8a72f54ec4dc4cdfd3621f7189b92a33134a7d7146e22426def0ebbe41&scene=58&subscene=0#rd
source: 安全圈
date: 2025-02-10
fetch_date: 2025-10-06T20:37:04.293162
---

# 【安全圈】DeepSeek 应用程序在未加密的情况下传输敏感用户和设备数据

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylj1oOYoHUQm0a2cy9I03m1lcKQr3nQdH1nTQdWyvphNWuyA74teaialeUBDUwx8zqEZeE2cojV7jnQ/0?wx_fmt=jpeg)

# 【安全圈】DeepSeek 应用程序在未加密的情况下传输敏感用户和设备数据

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

DeepSeek

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylj1oOYoHUQm0a2cy9I03m1l4Oqyv7MRbeD4SzkRQp6dPBvWJvQzXuIp0qmAbluucAOicUxvf9rpZoA/640?wx_fmt=other&from=appmsg)

对苹果 iOS 操作系统 DeepSeek 移动应用程序的最新审计发现了明显的安全问题，其中最主要的是它在互联网上发送敏感数据而不进行任何加密，使其容易受到拦截和操纵攻击。

该评估来自 NowSecure，它还发现该应用程序未能遵守最佳安全实践，并且收集了大量用户和设备数据。

该公司表示：“DeepSeek iOS 应用程序在互联网上发送一些移动应用程序注册和设备数据，且没有加密。这会使互联网流量中的任何数据都面临被动和主动攻击。”

拆解还揭示了在对用户数据进行加密时存在的几个实施缺陷。其中包括使用不安全的对称加密算法 ( 3DES )、硬编码加密密钥以及重用初始化向量。

此外，数据还会被发送到由云计算和存储平台Volcano Engine管理的服务器，该平台由运营 TikTok 的中国公司字节跳动所有。

NowSecure 表示：“DeepSeek iOS 应用程序全面禁用了应用程序传输安全 (ATS)，这是一种 iOS 平台级保护，可防止敏感数据通过未加密的通道发送。由于此保护被禁用，该应用程序可以（并且确实）通过互联网发送未加密的数据。”

尽管这款人工智能聊天机器人服务在全球多个市场的 Android 和 iOS 应用商店排行榜上名列前茅，但这一发现仍加剧了人们对其 的担忧。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylj1oOYoHUQm0a2cy9I03m1l1HeicGh7O82MrdnOcIKgVhAtMdWia1zhJmV6ic66DicFMBzTA0XmwUD0hQ/640?wx_fmt=other&from=appmsg)

网络安全公司 Check Point 表示，它观察到威胁行为者利用 DeepSeek、阿里巴巴 Qwen 和 OpenAI ChatGPT 的人工智能引擎开发信息窃取程序、生成未经审查或不受限制的内容以及优化脚本以进行大规模垃圾邮件分发的案例。

该公司表示：“由于威胁行为者利用越狱等先进技术绕过保护措施，开发信息窃取程序、金融盗窃和垃圾邮件分发，组织迫切需要针对这些不断演变的威胁实施主动防御，以确保对人工智能技术的潜在滥用采取强有力的防御措施。 ”

本周早些时候，美联社透露，DeepSeek 的网站配置为将用户登录信息发送给中国移动，中国移动是一家已被禁止在美国运营的国有电信公司。

该应用程序与TikTok非常相似，与中国有关联，这促使美国立法者推动在全国范围内禁止在政府设备上使用 DeepSeek，因为它存在向北京提供用户信息的风险。

值得注意的是，包括澳大利亚、意大利、荷兰、台湾和韩国在内的多个国家和地区，以及美国和印度的政府机构（例如国会、美国国家航空航天局、海军、五角大楼和德克萨斯州）均已禁止在政府设备中使用 DeepSeek。

DeepSeek 人气的爆炸式增长也使其面临恶意攻击，中国网络安全公司 XLab向《环球时报》透露，上个月底，该服务遭受了来自 Mirai 僵尸网络hailBot和RapperBot 的持续分布式拒绝服务 (DDoS) 攻击。

与此同时，网络犯罪分子正抓紧 时间利用 DeepSeek 的狂热来建立相似的页面，传播恶意软件、虚假投资骗局和欺诈性加密货币计划。

来源：https://thehackernews.com/2025/02/deepseek-app-transmits-sensitive-user.html

***END***

阅读推荐

[【安全圈】韩某某投敌叛变，48小时内被国安抓捕归案](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067706&idx=1&sn=7f31eb8f0f2b9706fa2bb95c56de54b9&scene=21#wechat_redirect)

[【安全圈】慧与Office 365 邮件服务遭攻击，至少 16 名员工隐私数据泄露](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067706&idx=2&sn=3fed7e8c8d5ff870c7d74733e568e26f&scene=21#wechat_redirect)

[【安全圈】微软示警 ASP.NET 重大安全漏洞，超3000公开密钥恐致服务器沦陷](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067706&idx=3&sn=42ec007bcefb5e73b814bbd77c03cb62&scene=21#wechat_redirect)

[【安全圈】曝英国要求苹果留“后门”：允许其检索全球任何用户上传到云端的所有内容](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067706&idx=4&sn=932d329534a041f36ccec808cef39b2e&scene=21#wechat_redirect)

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
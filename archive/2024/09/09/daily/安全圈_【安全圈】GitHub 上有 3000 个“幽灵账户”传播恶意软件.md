---
title: 【安全圈】GitHub 上有 3000 个“幽灵账户”传播恶意软件
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064249&idx=3&sn=be5b899e0bea8af3b290b45b6e5ef67f&chksm=f36e65b9c419ecafca6755f32b32c1b766aa4b099e2fed984e8a28f7e5d61de2cdfd0cc7797d&scene=58&subscene=0#rd
source: 安全圈
date: 2024-09-09
fetch_date: 2025-10-06T18:24:22.257081
---

# 【安全圈】GitHub 上有 3000 个“幽灵账户”传播恶意软件

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhQV8P7VwvC6C2P0u35FEU8nbWu8SQfzy7icL3ySzxRCJuLHibTs9Xr5ETGzrDnvPjw8gd8f5ykO81w/0?wx_fmt=jpeg)

# 【安全圈】GitHub 上有 3000 个“幽灵账户”传播恶意软件

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=png&from=appmsg "微信图片_20230927171534.png")

**关键词**

恶意软件

Check Point Research 最近曝光了一个新的分发即服务 (DaaS) 网络，称为 Stargazers Ghost Network，该网络至少在一年前就在 GitHub 上传播恶意软件。由于这些账户也执行正常活动，因此用户并未意识到这些账户正在执行恶意活动。

![](https://mmbiz.qpic.cn/mmbiz_png/AnRWZJZfVaHPK1GoY0vCUh4zb9B0lGym6MibYEib4iaCL9RxWO5S8v3IuPBwJKskHCcswS7QE7PKWI4LpyGDZUzuQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

这些幽灵账户针对的是那些想要增加 YouTube、Twitch 和 Instagram 粉丝的用户，通过 Discord 频道向 GitHub 存储库分发恶意链接。由于恶意链接指向已加星标和验证的内容，其他用户会认为这些存储库是合法的。然而，高星标数量让 Check Point 研究人员意识到这些账户很可疑。

![](https://mmbiz.qpic.cn/mmbiz_png/AnRWZJZfVaHPK1GoY0vCUh4zb9B0lGymC3UH7ib1iaEh0ReS1dqphVwCiaVSttiaTvVaicYRJulE0LS186PrAg6jDvA/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**恶意软件通过密码加密的档案发布进行分发**

“在短短的监控期内，我们发现了 2,200 多个发生‘幽灵’活动的恶意存储库。在 2024 年 1 月左右的一次活动中，该网络传播了 Atlantida 窃取程序，这是一个新的恶意软件家族，可窃取用户凭据和加密货币钱包以及其他个人身份信息 (PII)。这次活动非常有效，因为在不到四天的时间内，超过 1,300 名受害者感染了 Atlantida 窃取程序。”Check Point Research 报告中写道。

通过使用三个 GitHub 帐户协同工作，Stargazers Ghost Network 成功避开了 GitHub 的检测。当攻击者将包含钓鱼下载链接的 README.md 文件附加到外部存储库的发布版本时，攻击就开始了。

一个帐户提供钓鱼存储库模板，而另一个帐户提供钓鱼图像模板。然后，第三个帐户将恶意软件作为发布版本中受密码保护的存档提供，有时攻击就是在这里检测到的，然后第三个帐户被 GitHub 禁止。如果发生这种情况，攻击者就会使用第一个帐户中的新链接再次发起攻击。

### **暗网赚钱**

研究人员还发现了该计划的另一部分——利用幽灵账户在暗网上赚钱。CheckPoint 估计，2024 年 5 月中旬至 6 月中旬的恶意活动为 Stargazers Ghost Network 带来了约 8,000 美元的收入。Check Point 估计，该计划在整个生命周期内带来了约 100,000 美元的收入。

2023 年 7 月 8 日，Terefos 团队发现 Stargazers Ghost Network 在暗网上发布了横幅广告。网络犯罪分子可以“雇佣”幽灵账户，获得 GitHub 上的各种服务，包括加星标、关注、分叉和关注账户和存储库。

这些服务的价格各不相同，例如加星标 100 个账户需 10 美元，而为受信任的账户提供“陈旧”存储库则需 2 美元。除了广告横幅，网络犯罪分子还使用了另一种典型的营销策略：折扣。在 Stargazers Ghost Network 上花费超过 500 美元的威胁行为者可以获得服务折扣。

### **GitHub 采取行动**

在了解到这 3,000 个幽灵账户后，GitHub 采取行动阻止恶意软件的传播。

Check Point 的研究人员认为，幽灵账户在许多其他平台上运作，包括 YouTube、Discord、Instagram 和 Facebook。由于这些渠道还可用于通过帖子、存储库、视频和推文分发链接和恶意软件，Check Point 认为这些账户的运作方式类似于 GitHub 计划，这意味着这很可能只是一种新策略的开始。

Check Point 报告总结道：“未来的幽灵账户可能会利用人工智能 (AI)模型来生成更具针对性和多样性的内容，从文本到图像和视频。通过考虑目标用户的回复，这些由人工智能驱动的账户不仅可以通过标准化模板来推广网络钓鱼材料，还可以通过针对真实用户的需求和互动量身定制的响应来推广网络钓鱼材料。恶意软件传播的新时代已经到来，我们预计这些类型的操作将更频繁地发生，这使得区分合法内容和恶意材料变得越来越困难。”

***END***

阅读推荐

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliayAgNUicp8k6tBdiaTt9Ne0txpDfbyrQfVvE85QeUc8SNTTibheOUsR1V6fbGDu83akQoZrZgafh3iaw/640?wx_fmt=jpeg)[【安全圈】在针对中国贸易公司的攻击中发现新的跨平台恶意软件KTLVdoor](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064191&idx=1&sn=c35045938e79877d30f89b03edd0e1fb&chksm=f36e65ffc419ece90013b87874cd7798d71ec90c368fa3cd01b9772d200a1c28a3c179a97067&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGyliayAgNUicp8k6tBdiaTt9Ne0tbbeNaiaibcj5iaaFCJEXMpjtdKHpdBSUK8WFXxhkFSbSHrX7OAwRnusiaw/640?wx_fmt=png)[【安全圈】微软发布Windows Server 2025新预览版调整时间炸弹 请用户尽快更新](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064191&idx=2&sn=1780528b58dfe68e94e96232787e9eac&chksm=f36e65ffc419ece9293ed88aae76bc78264cee9a48b12a868f4e30df06954de3b8f8450e3392&scene=21#wechat_redirect)

[【安全圈】网络身份证是强制，会影响正常上网？公安部详细回应](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652063868&idx=2&sn=e0e51cc3262a54328e4fee1482c882f1&chksm=f36e643cc419ed2a36eb00a524a91605bcd28b782d15ab7fb662c206140dca0df3a38bac1c1a&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliayAgNUicp8k6tBdiaTt9Ne0tvzZWFaB7j9wbQry52n6LyxZvqejZTWhJa9MYQoq3FX8eRwZ0YbpzbQ/640?wx_fmt=other)[【安全圈】Microchip Technology 确认员工数据被盗](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064191&idx=3&sn=54a0ddf43c0026e259668f2618ca0c2b&chksm=f36e65ffc419ece9b6366cf6730df99dce0a26885d6310c52bb5b820f8dc05ebbd72ed362f38&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgTTuYibxDr5sTw6UZTOEkmzZuc9frHlJKxcK8vXZWV0YCun5qJwtzScxfSAgubKEncsnD45RuqELg/640?wx_fmt=jpeg&from=appmsg)[【安全圈】研究人员发现Yubikeys中存在一个难以利用但也难修复的漏洞](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064191&idx=4&sn=2fe0d56663512b21ba1785d9a22bcd38&chksm=f36e65ffc419ece95bd1e15cc3b1eb19a4fe27400937238106b5b34bde708be50cd7af470869&scene=21#wechat_redirect)

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
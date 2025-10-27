---
title: 【安全圈】俄罗斯黑客组织 Romcom 利用 0day 漏洞攻击 Firefox、Tor 用户
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066334&idx=4&sn=11465e70e7b110f53a2339d3dae91a21&chksm=f36e7e5ec419f74854a25fa61ed147efd22e98ef5b6de5c23de7bd687f6e2459303cbc314c3a&scene=58&subscene=0#rd
source: 安全圈
date: 2024-11-30
fetch_date: 2025-10-06T19:16:37.554529
---

# 【安全圈】俄罗斯黑客组织 Romcom 利用 0day 漏洞攻击 Firefox、Tor 用户

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylg4kbtk0IKFiboTvHdnHibVXNFasQSS6m5ia4iawSkniadfTRsTPwRDiaOdqEWoR7W6DnOEeMbaibK92xwjQ/0?wx_fmt=jpeg)

# 【安全圈】俄罗斯黑客组织 Romcom 利用 0day 漏洞攻击 Firefox、Tor 用户

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

黑客

一个俄罗斯黑客组织Romcom利用两个此前未知的漏洞攻击 Windows PC 上的 Firefox 和 Tor 浏览器用户。

防病毒提供商 ESET 将该攻击描述为潜在的“大规模活动”，其目标是欧洲和北美的用户。

俄罗斯黑客通过一个恶意网页传播黑客攻击，这些网页似乎伪装成虚假新闻机构。如果易受攻击的浏览器访问该页面，它可以秘密触发软件漏洞，在受害者的电脑上安装后门。

ESET 警告称，用户无需与该网页进行任何交互。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgacxE7EloOtv9ibibZtiasrhjMvknc9DPcrAVNmJvk9W92LDN6PiaU1A9AicBjbjllxbk4PiaY3EPeaJ9Q/640?wx_fmt=png&from=appmsg)

目前尚不清楚黑客如何传播恶意网页链接。但第一个漏洞（称为CVE-2024-9680）可导致 Firefox 和 Tor 浏览器在正常受限制的进程中运行恶意代码。

黑客利用 Windows 10 和 11 中的第二个漏洞（称为CVE-2024-49039）发动攻击，以便在浏览器之外和操作系统上执行更多恶意代码。秘密下载并安装一个能够监视 PC 的后门，包括收集文件、截屏以及窃取浏览器 cookie 和保存的密码。

Mozilla、Tor 和 Microsoft 都已修补了漏洞。Tor 浏览器基于 Firefox。Mozilla 于 10 月 8 日私下报告了此问题，这两款浏览器都在第二天修补了此漏洞。与此同时，Microsoft于 11 月 12 日修补了另一个漏洞。

如果用户未能及时打补丁，黑客仍可继续利用该攻击。ESET 提供的遥测数据显示，某些国家可能有多达 250 名用户遭遇过该攻击，攻击始于 10 月，甚至可能更早。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgacxE7EloOtv9ibibZtiasrhjwoMdBoNlNwwibKLF4yBWJibCxjdWWv32EW17y8IYQKbI2NQcOpASlg1g/640?wx_fmt=png&from=appmsg)

ESET将这些攻击与一个名为“RomCom”的俄罗斯黑客组织联系起来，该组织一直专注于网络犯罪和间谍活动。

ESET追踪了该组织一系列的攻击活动：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgacxE7EloOtv9ibibZtiasrhjnyTCc2qStiaFXEWRicLYpeJdD6VxXfY5ibrwQeicrdpzlZ6RGBWfceBslA/640?wx_fmt=png&from=appmsg)

将两个0day漏洞串联起来，RomCom 便可以利用无需用户交互的漏洞进行攻击。这种复杂程度表明威胁组织有意愿并有手段获得或开发隐身能力。

详细技术报告：

https://www.welivesecurity.com/en/eset-research/romcom-exploits-firefox-and-windows-zero-days-in-the-wild/

Mzoilla官方漏洞公告：

https://blog.mozilla.org/security/2024/10/11/behind-the-scenes-fixing-an-in-the-wild-firefox-exploit/

***END***

阅读推荐

[【安全圈】实习生向模型投毒事件后续：字节跳动起诉该实习生索赔800万元](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066267&idx=1&sn=60295481f95c5dd47afc5777c65fc240&scene=21#wechat_redirect)

[【安全圈】国际执法机构成功捣毁一个盗版视频网站，月收入高达2.5亿欧元（约合人民币19.12亿元）](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066267&idx=2&sn=7e668b534b3cc494ee46de09126e4051&scene=21#wechat_redirect)

[【安全圈】微软可能窃取你的Word、Excel文件以训练人工智能模型？](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066267&idx=3&sn=60edc9444015bfe02212ba3d2d549432&scene=21#wechat_redirect)

[【安全圈】Bootkitty——首个针对Linux的UEFI引导程序恶意软件](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066267&idx=4&sn=2e12d00121b83ddf62b939eea70ced2a&scene=21#wechat_redirect)

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

阅读原文

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
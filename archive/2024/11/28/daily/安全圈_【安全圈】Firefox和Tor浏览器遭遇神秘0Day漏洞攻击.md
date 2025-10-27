---
title: 【安全圈】Firefox和Tor浏览器遭遇神秘0Day漏洞攻击
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066249&idx=3&sn=c16dd8113efa3f879e94a0128384f7be&chksm=f36e7d89c419f49fb3a2915184568b4a51c1bcf58da2b60b496d622047008b653b429485ab28&scene=58&subscene=0#rd
source: 安全圈
date: 2024-11-28
fetch_date: 2025-10-06T19:20:35.777304
---

# 【安全圈】Firefox和Tor浏览器遭遇神秘0Day漏洞攻击

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhqDPOFswIOmibtyefhG5bOOic6nz3LWWyqhDb8KPa0wToLL8j56wZmDB0FKKSGCfdzh13GSqYic6DSA/0?wx_fmt=jpeg)

# 【安全圈】Firefox和Tor浏览器遭遇神秘0Day漏洞攻击

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

网络攻击

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhqDPOFswIOmibtyefhG5bOOqhusLMzbeFGOpib4CEn6qEAeWgyqMsnBm7bfJ3G7VLvzeSCuSQ5ibdzA/640?wx_fmt=jpeg&from=appmsg)

近日，俄罗斯某APT组织被发现利用两个以前未知的漏洞攻击Windows PC上的Firefox和Tor浏览器用户。安全厂商ESET指出，这些零日漏洞攻击可能造成“广泛传播”，主要针对欧洲和北美的用户。

俄罗斯黑客通过一个伪装成假新闻组织的恶意网页进行传播。如果易受攻击的浏览器（Firefox和Tor浏览器 ）访问该页面，它可以秘密触发软件漏洞在受害者的PC上安装后门。最关键的是，ESET警告称，这个过程无需与网页进行互动。

目前，尚不清楚是如何传播包含恶意软件的网页链接。但第一个漏洞（编号：CVE-2024-9680），可以导致Firefox和Tor浏览器运行恶意计算机代码。

黑客还将攻击与Windows 10和11中的第二个漏洞（编号：CVE-2024-49039）链接起来，在浏览器和操作系统上执行更多的恶意计算机代码，最终实现秘密下载并安装一个后门。该后门能够监视PC，包括收集文件、截取屏幕截图以及窃取浏览器cookie和保存的密码。

目前，Mozilla、Tor和微软已经修补了这些漏洞。这两个浏览器于10月9日修复了该漏洞，微软在11月12日修补了另一个漏洞，并建议用户及时更新。

如果用户未能修补漏洞，黑客可以继续利用漏洞发起此类攻击。ESET的杀毒产品数据显示，自10月份（可能更早）以来，某些国家已有超过250家企业用户可能遇到了这些攻击。

虽然还没有掌握确凿的证据，但ESET认为该攻击的幕后是名为“RomCom”俄罗斯APT组织，后者专注于网络犯罪和间谍活动。这也是RomCom继2023年6月滥用微软CVE-2023-36884 漏洞后，第二次被发现利用关键零日漏洞，策划具有威胁性的攻击活动。

参考来源：https://www.pcmag.com/news/russian-hackers-used-zero-day-attack-to-hit-firefox-tor-users

***END***

阅读推荐

[【安全圈】微软又全球宕机11小时，多项核心服务无法使用](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066233&idx=1&sn=c19f13229d6729fcaba6459e32b28d5a&scene=21#wechat_redirect)

[【安全圈】慎用，知名压缩工具7-Zip存在严重漏洞](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066233&idx=2&sn=778f80b7b5c35162dd41acacfbd17148&scene=21#wechat_redirect)

[【安全圈】微软给Windows 11添加新选项允许打开任意文件夹最终都在新选项卡中打开](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066233&idx=3&sn=eda307d1af237cfd16d170e9ffa459af&scene=21#wechat_redirect)

[【安全圈】Ubuntu 20.04 LTS版即将5年主流结束 除非订阅ESM否则明年4月将无法更新](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066233&idx=4&sn=0490cbd0d910ca903dcdf33af3bd1057&scene=21#wechat_redirect)

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
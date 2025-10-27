---
title: 【安全圈】PyPI Python 库“aiocpa”发现通过 Telegram Bot 泄露加密密钥
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066334&idx=3&sn=adb8550b6cc0709a29ae8645c49f3da1&chksm=f36e7e5ec419f74850b83281a36bf791424cf12f6f7b6fe34fdd417ef029e6c397fd31ffa995&scene=58&subscene=0#rd
source: 安全圈
date: 2024-11-30
fetch_date: 2025-10-06T19:16:36.428412
---

# 【安全圈】PyPI Python 库“aiocpa”发现通过 Telegram Bot 泄露加密密钥

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgacxE7EloOtv9ibibZtiasrhjIWSaD9WU5fRYVHGoBcJFKkktu51XXYT3co7W9PtMTjpTZ9PNJajdeA/0?wx_fmt=jpeg)

# 【安全圈】PyPI Python 库“aiocpa”发现通过 Telegram Bot 泄露加密密钥

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

PyPI

Python 软件包索引（PyPI）软件仓库的管理员已经隔离了 “aiocpa ”软件包，因为该软件包在新的更新中包含了通过 Telegram 外泄私钥的恶意代码。

该软件包被描述为同步和异步 Crypto Pay API 客户端。该软件包最初于 2024 年 9 月发布，迄今已被下载 12100 次。

将 Python 库隔离后，客户端就无法继续安装，其维护者也无法对其进行修改。

网络安全机构Phylum上周分享了软件供应链攻击的细节，该机构称，软件包的作者在PyPI上发布了恶意更新，同时在GitHub的库中保持清洁，试图逃避检测。

目前还不清楚最初的开发者是恶意更新的幕后黑手，还是他们的证书被其他威胁行为者泄露。

恶意活动的迹象首次出现在 0.1.13 版本的库中，其中包括对 Python 脚本 “sync.py ”的修改，该脚本的目的是在安装软件包后立即解码并运行一段混淆代码。

Phylum说：“这个特殊的blob被递归编码并压缩了50次，”Phylum补充说，它被用来使用Telegram机器人捕获并传输受害者的Crypto Pay API令牌。

值得注意的是，Crypto Pay 被宣传为基于 Crypto Bot（@CryptoBot）的支付系统，允许用户接受加密货币支付，并使用 API 向用户转账。

这一事件意义重大，尤其是因为它凸显了在下载软件包之前扫描其源代码的重要性，而不仅仅是检查其相关的软件仓库。

“正如这里所证明的那样，攻击者可以在向生态系统分发恶意软件包的同时，故意维护干净的源代码库，”该公司表示，并补充说，“这次攻击提醒我们，软件包之前的安全记录并不能保证其持续的安全性。”

软件包 aiocpa 已正式从 PyPI 软件源中删除。

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
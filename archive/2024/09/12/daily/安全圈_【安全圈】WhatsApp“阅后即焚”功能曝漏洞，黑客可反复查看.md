---
title: 【安全圈】WhatsApp“阅后即焚”功能曝漏洞，黑客可反复查看
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064335&idx=2&sn=ae95b2ac3eb9fe50dc11b71ae2308f86&chksm=f36e660fc419ef19c976b3738d066d4b60f7f036f183ba48fbafaed13f5584b33c4080e6a1cb&scene=58&subscene=0#rd
source: 安全圈
date: 2024-09-12
fetch_date: 2025-10-06T18:29:16.589574
---

# 【安全圈】WhatsApp“阅后即焚”功能曝漏洞，黑客可反复查看

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgRicbQ6VzsjWRPfpanbuyeSdz8TMdaN88LIDPGLP7pvUYbg2kzkQTLXaNZialHCSmTN503SiaO9k9zQ/0?wx_fmt=jpeg)

# 【安全圈】WhatsApp“阅后即焚”功能曝漏洞，黑客可反复查看

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=png&from=appmsg "微信图片_20230927171534.png")

**关键词**

安全漏洞

据BleepingComputer消息，全球拥有20亿用户的即时通讯工具 WhatsApp最近修复了一个十分重要的隐私漏洞，该漏洞能允许攻击者多次查看用户发送的“阅后即焚”（View once）内容。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgRicbQ6VzsjWRPfpanbuyeSymEfA1hn8NEVg66Z3oDiagnNxHSZOwTsxnsov9LNkSsDHC4OpcCesEA/640?wx_fmt=jpeg&from=appmsg)

WhatsApp的“阅后即焚”于3年前推出，允许用户发送只能浏览一次的照片、视频和语音消息，且接收者无法转发、分享、复制或截取消息。

但这其中有一个Bug，Zengo X 研究团队发现，“阅后即焚” 功能可用于向收件人的所有设备发送加密媒体消息，包括桌面端，即使这些消息在桌面端无法显示。这些消息与普通消息几乎完全相同，但包含一个指向 WhatsApp 网络服务器（"blob store"）托管的加密数据 URL 以及解密密钥。

研究人员称，这些消息在下载后不会立即从 WhatsApp 的服务器中删除，且某些版本的“阅后即焚 ”消息还包含无需下载即可查看的低质量预览。

此外，“阅后即焚 ”消息与常规消息类似，但带有一个“View once”值为“true”的标记，攻击者仅需将“true“改为” false“，就可绕过此隐私功能 ，下载、转发和共享这些“阅后即焚 ”消息。

Zengo X 据称是第一个向 WhatsApp母公司Meta 详细报告这一漏洞的组织，但在此之前该漏洞可能至少 已经暴露了1年。BleepingComputer甚至已观察到两款谷歌浏览器插件（其中一个已于 2023 年发布）能够便捷地实现反复查看并共享“阅后即焚 ”消息。

目前Meta已表示对漏洞进行了修复，但这背后所反映出的更深层次问题也引发了人们的忧虑，即这些科技巨头所谓的为用户着想的隐私措施可能仅仅是个”空壳“，其本质上仍然漏洞百出。

***END***

阅读推荐

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgkUguUn2Zr2jE7dxoVOPckLPdj78V4glicW8B5l0wYOEZDiaUNPm6kFmfU1qSpspg793icvkdGzG1bw/640?wx_fmt=jpeg)[【安全圈】全国首例！三名程序员在虚拟币钱包中植入“后门”，窃取上万条用户密码](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064313&idx=1&sn=f0e564b32de7f9a8451a7838cd09ce68&chksm=f36e6679c419ef6f89e6896804adff9e1368a071fdeda74e84abab8a9f3a1fbff730d6cd9350&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljUASPgGc31ibGFF8QlWO2bDVRTmG60tLcehoiaraLcyb9sHGOuavM5GxCJMTSegsHe0rNJzoDG9Cww/640?wx_fmt=jpeg&from=appmsg)[【安全圈】美国一 AI 公司因非法收集面部数据被罚超 3000 万欧元](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064313&idx=2&sn=1a2768fa4fc1c00cdb0d5257c8f13ab0&chksm=f36e6679c419ef6f6aabf549f51379c2bdefb5b3097e8d633c0b1971d029fc37b4b0f41e6637&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgkUguUn2Zr2jE7dxoVOPckwO49EEhAmZlicZuPyaMTV5V0Ot6L28ujkfcMaic2GwicQtMLqtcgJhymw/640?wx_fmt=jpeg)[【安全圈】McAfee 识别出 280 多个虚假安卓应用，可能会窃取加密货币钱包](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064313&idx=3&sn=779efcc08939bdd90510ded9e796ed50&chksm=f36e6679c419ef6f32af6ed70d1c1bc2cf9c6ec712a4762d0fbf5fab5a13b9ec9c822a19b1d6&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgkUguUn2Zr2jE7dxoVOPckGjKj87HLbicfdk2VICtNmbsstdWXUibE5L8tO1tM7K4x5iavP9AVefLUg/640?wx_fmt=jpeg)[【安全圈】黑客背刺同行，向对方发送信息窃取软件](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064313&idx=4&sn=0aa1c34198f22da1fad88f018223ddf9&chksm=f36e6679c419ef6f6509c94daed8b8325067c714e4eb88049e1be19548527e03aa43c500eb0a&scene=21#wechat_redirect)

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
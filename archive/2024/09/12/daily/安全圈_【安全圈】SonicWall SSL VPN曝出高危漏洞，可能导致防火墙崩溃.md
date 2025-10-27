---
title: 【安全圈】SonicWall SSL VPN曝出高危漏洞，可能导致防火墙崩溃
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064335&idx=3&sn=ef8069d8946623ebc55c3e93a45ad582&chksm=f36e660fc419ef19327e756dcb04ba4ac776b959972bfb8b560427de7fae57d06333410a3ea0&scene=58&subscene=0#rd
source: 安全圈
date: 2024-09-12
fetch_date: 2025-10-06T18:29:17.631449
---

# 【安全圈】SonicWall SSL VPN曝出高危漏洞，可能导致防火墙崩溃

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgRicbQ6VzsjWRPfpanbuyeSZYQxSUOGfaakzSGiaox8GOKCYpqzr97zIuHCQpHuXAZy7Zpjic8m35Cw/0?wx_fmt=jpeg)

# 【安全圈】SonicWall SSL VPN曝出高危漏洞，可能导致防火墙崩溃

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=png&from=appmsg "微信图片_20230927171534.png")

**关键词**

安全漏洞

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgRicbQ6VzsjWRPfpanbuyeSghpkShLDicgAkHpFf2ENSJ8SGJTpeiaZzgxyNsAYowYDNWHvXqYc05jA/640?wx_fmt=jpeg&from=appmsg)

近日，有黑客利用 SonicWall SonicOS 防火墙设备中的一个关键安全漏洞入侵受害者的网络。

这个不当访问控制漏洞被追踪为 CVE-2024-40766，影响到第 5 代、第 6 代和第 7 代防火墙。SonicWall于8月22日对其进行了修补，并警告称其只影响防火墙的管理访问界面。

然而，SonicWall上周五（9月6日）透露，该安全漏洞还影响了防火墙的SSLVPN功能，且已被黑客用以网络攻击。该公司提醒客户尽快为受影响的产品打上补丁，但没有透露有关野外利用的详细信息。

Arctic Wolf的安全研究人员认为这些攻击与Akira勒索软件背后的运营者有所关联，他们试图以SonicWall设备为目标，获得对目标网络的初始访问权。

Arctic Wolf高级威胁情报研究员Stefan Hostetler表示：在每个实例中，被攻击的账户都是设备本身的本地账户，而不是与微软活动目录等集中式身份验证解决方案集成在一起。此外，所有被入侵账户的 MFA 都被禁用，受影响设备上的 SonicOS 固件属于已知易受 CVE-2024-40766 影响的版本。

同时，网络安全机构Rapid7也在最近的事件中发现了针对SonicWall SSLVPN账户的勒索软件组织，但其表示将CVE-2024-40766与这些事件联系起来的证据仍然是间接的。

Arctic Wolf 和 Rapid7 复制了 SonicWall 的警告，并敦促管理员尽快升级到最新的 SonicOS 固件版本。

## 联邦机构被勒令在 9 月 30 日前打补丁

本周一（9月9日），CISA将此关键访问控制漏洞添加到其已知漏洞目录中，并命令联邦机构在 9 月 30 日之前的三周内，按照约束性操作指令 (BOD) 22-01 的规定，确保其网络中存在漏洞的 SonicWall 防火墙的安全。

SonicWall 缓解建议将防火墙管理和 SSLVPN 访问限制为可信来源，并尽可能禁止互联网访问。管理员还应为所有使用 TOTP 或基于电子邮件的一次性密码 (OTP) 的 SSLVPN 用户启用多因素身份验证 (MFA)。

在网络间谍和勒索软件攻击中，攻击者经常以 SonicWall 设备和设备为目标。例如，包括HelloKitty和FiveHands在内的多个勒索软件团伙也利用SonicWall的安全漏洞初步访问了受害者的企业网络。

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
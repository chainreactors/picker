---
title: 【安全圈】Steam 平台上的 PirateFi 游戏被发现安装了密码窃取恶意软件
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067859&idx=3&sn=22a5fdac878492e3eb605cf3133cb536&chksm=f36e7453c419fd45ec3f7a4da4066239d4bf96bc365dcafd96e9890106ae8d2315d875641329&scene=58&subscene=0#rd
source: 安全圈
date: 2025-02-18
fetch_date: 2025-10-06T20:40:02.193286
---

# 【安全圈】Steam 平台上的 PirateFi 游戏被发现安装了密码窃取恶意软件

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgzlicSCH250mZoyPsJvSY3zodY6BartqibtsoW6s5GdMHLCSxPgmtpcekkp8iajO9GicYiaw1ibQcfyI2w/0?wx_fmt=jpeg)

# 【安全圈】Steam 平台上的 PirateFi 游戏被发现安装了密码窃取恶意软件

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

黑客、恶意软件

一款名为PirateFi的免费游戏在Steam商店中被发现向不知情的用户分发Vidar信息窃取恶意软件。

这款游戏在Steam目录中存在了近一周，从2月6日至2月12日，期间被最多1500名用户下载。分发服务已向可能受影响的用户发送通知，建议他们出于谨慎考虑重新安装Windows系统。

**Steam上的恶意软件**

PirateFi由Seaworth Interactive于上周在Steam上发布，并获得了正面评价。该游戏被描述为一款设定在低多边形世界中的生存游戏，涉及基地建设、武器制作和食物收集。

然而，Steam本周早些时候发现该游戏包含恶意软件，但未具体说明恶意软件的类型。

通知中写道：“该游戏的开发者账户上传了包含疑似恶意软件的版本。”

“您在这些版本活跃期间在Steam上玩了PirateFi，因此这些恶意文件很可能已在您的电脑上运行，”服务警告称。

建议受影响用户运行全系统扫描，使用最新的杀毒软件，检查是否有不认识的新安装软件，并考虑重新格式化操作系统。

受影响用户还在PirateFi的Steam社区页面上发布了警告，告知其他用户不要启动游戏，因为他们的杀毒软件已将其识别为恶意软件。

SECUINFRA Falcon Team的Marius Genheimer获取了通过PirateFi分发的恶意软件样本，并确认其为Vidar信息窃取者的一个版本。

“如果您是下载了这款‘游戏’的玩家之一：请认为您的浏览器、电子邮件客户端、加密货币钱包等保存的凭据、会话cookie和秘密已被窃取，”SECUINFRA建议道。

建议更改所有可能受影响账户的密码，并在可能的情况下激活多因素身份验证保护。

根据动态分析和YARA签名匹配，识别为Vidar的恶意软件被隐藏在一个名为Pirate.exe的文件中，作为有效载荷（Howard.exe）与InnoSetup安装程序打包在一起。

Genheimer告诉BleepingComputer，威胁行为者多次修改了游戏文件，使用各种混淆技术，并更改了用于凭据窃取的命令与控制服务器。

研究人员认为，PirateFi名称中的web3/区块链/加密货币引用是故意为之，旨在吸引特定的玩家群体。

Steam未公布受PirateFi恶意软件影响的用户数量，但从游戏页面的统计数据来看，最多可能有1500人受到影响。

恶意软件入侵Steam商店并不常见，但并非前所未有。2023年2月，Steam用户曾被恶意的Dota 2游戏模式 targeting，这些模式利用Chrome n-day漏洞在玩家电脑上执行远程代码。

2023年12月，当时流行的独立策略游戏《Slay the Spire》的一个模组被黑客入侵，注入了一个名为‘Epsilon’的信息窃取者投放器。

Steam引入了额外的措施，如基于短信的验证，以保护玩家免受未经授权的恶意更新，但PirateFi的案例表明，这些措施还不够充分。

***END***

阅读推荐

[【安全圈】利用App盗取数百万条个人信息，江西一公司负责人获刑！](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067846&idx=1&sn=21a4530ad00ec5af97103e9590e7dce0&scene=21#wechat_redirect)

[【安全圈】PostgreSQL漏洞与BeyondTrust零日漏洞被联合利用](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067846&idx=2&sn=cd94ea7cada0daf8d439805d2653a055&scene=21#wechat_redirect)

[【安全圈】黑客利用智能合约漏洞盗取价值950万美元以太币](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067846&idx=3&sn=4a1a9e96de810a8e68ea6951a76de7f0&scene=21#wechat_redirect)

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
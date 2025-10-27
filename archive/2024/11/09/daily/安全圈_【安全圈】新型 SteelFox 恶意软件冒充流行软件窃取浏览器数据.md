---
title: 【安全圈】新型 SteelFox 恶意软件冒充流行软件窃取浏览器数据
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065786&idx=4&sn=1999eecd13825fe3129c7713dfe36b47&chksm=f36e63bac419eaacc03506b346d45cd70cace1afa85326b8fb2f4a4d0885ed6b84e1e21cf620&scene=58&subscene=0#rd
source: 安全圈
date: 2024-11-09
fetch_date: 2025-10-06T19:19:13.601201
---

# 【安全圈】新型 SteelFox 恶意软件冒充流行软件窃取浏览器数据

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylg5ZQcZEq3ZdBoKh2Wq7BR9vgKafMG93lib28J9iasHqAOxgzicYEm7ErZMNawcib2Ow3MoI6ogVzfsaQ/0?wx_fmt=jpeg)

# 【安全圈】新型 SteelFox 恶意软件冒充流行软件窃取浏览器数据

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

恶意软件

SteelFox 恶意软件通过伪造激活工具、窃取信用卡数据和部署加密矿工来打击软件盗版者。了解影响全球用户的这一新威胁，以及如何保护自己免受这一复杂网络犯罪活动的侵害。

Securelist 的网络安全研究人员发现了一种新型恶意软件，这种恶意软件通过在线论坛、torrent 跟踪器和博客传播，冒充福昕 PDF 编辑器、AutoCAD 和 JetBrains 等合法软件。

研究人员称其为 “SteelFox”，该恶意软件的主要目标是那些参与下载盗版软件和虚假软件激活工具（破解版）的Microsft Windows用户。

该活动始于 2023 年 2 月，通过伪造软件激活工具将加密货币挖掘和数据窃取功能结合在一起。到目前为止，该恶意软件已经感染了全球 11,000 多名用户。

根据 Securelist 在发布前与 Hackread.com 分享的博文，SteelFox 是一个全功能的 “犯罪软件包”，可以从受感染的设备中提取敏感数据，包括信用卡信息、浏览历史和登录凭证。它还会收集系统信息，如安装的软件、运行的服务和网络配置。

恶意软件的初始攻击载体是虚假的软件激活程序，这些程序在在线论坛和洪流跟踪器上被宣传为可以免费激活合法软件。安装后，恶意软件会创建一个服务，即使在重启后也会留在系统中，并使用易受攻击的驱动程序来提高其权限。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylg5ZQcZEq3ZdBoKh2Wq7BR9BQY7A8yOonN5hJfl1pIWH705Z4zYcdgH3Y2icGv8RmolmaStHdb3d1Q/640?wx_fmt=jpeg&from=appmsg)恶意程序广告（通过 Securelist）

该恶意软件通过多阶段攻击链运行，首先是一个需要管理员权限的驱动程序。执行后，它会将自己安装为 Windows 服务，并使用 AES-128 加密来隐藏其组件。该恶意软件通过利用易受攻击的驱动程序实现系统级访问，并通过 SSL pinning 实现 TLS 1.3，以便与其命令服务器进行安全通信。

“SteelFox “高度复杂地使用了现代C++语言和外部库，这赋予了该恶意软件强大的威力。TLSv1.3 和 SSL pinning 的使用确保了安全通信和敏感数据的采集。

全球影响

SteelFox似乎并不针对特定的个人或组织，而是在更大范围内感染尽可能多的用户。该恶意软件已经感染了 10 多个国家的用户，其中包括以下国家：

* 阿联酋
* 印度
* 巴西
* 中国
* 俄罗斯
* 埃及
* 阿尔及利亚
* 墨西哥
* 越南
* 斯里兰卡

KnowBe4 的安全意识倡导者 James McQuiggan 强调了企业谨慎对待软件下载来源的重要性。他还强调了通过网络安全意识计划培训员工的必要性。

“SteelFox下载器的双重功能–同时提供软件 “破解 ”和恶意软件–表明了网络犯罪分子使用的复杂工具，并使用过时的驱动程序进行权限升级，这凸显了企业确保实施补丁的迫切需要。”

詹姆斯解释说：“企业必须确保验证软件来源，保持最少的用户权限访问控制，并利用端点保护来检测可疑的安装行为。”

“此外，更重要的是，确保向用户提供网络安全意识计划，让他们了解未经验证的软件（如开源软件或这些常见的应用程序）的危险性。允许 IT 管理软件解决方案安装和监控所有应用程序，”他建议说。

防范SteelFox

为避免成为SteelFox的受害者，用户应只从官方渠道下载软件，并使用可靠的安全解决方案，以检测和防止受感染软件的安装。此外，用户在点击不明来源的链接或下载附件时应谨慎，因为这些链接或附件往往会被用来传播恶意软件。

***END***

阅读推荐

[【安全圈】Windows 10 将于明年 10 月停止支持 对你我有何影响](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065766&idx=1&sn=20737c81521c2b60c2ae6e68bd85cf08&chksm=f36e63a6c419eab0559b56523c0815b5e760666eb51eaa8a0579237fda5bd619c529c56f24fe&scene=21#wechat_redirect)

[【安全圈】谷歌云将在2025年底强制实施多因素身份验证](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065766&idx=2&sn=60b2502195278b934474b1c4a7fc49bd&chksm=f36e63a6c419eab08fb88d51ccdbf0cb4bfe5081e8ccfe502ee69577918cb1ada38f8721c993&scene=21#wechat_redirect)

[【安全圈】黑客可以随意访问EA公司7亿用户账号](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065766&idx=3&sn=bcdf6497f31db93acd068fb24f76e293&chksm=f36e63a6c419eab04b707515e3ec637038e1f931dd74f1640728e7904bece00c01cfe82fde69&scene=21#wechat_redirect)

[【安全圈】Schneider Electric 在报告黑客索赔后调查安全“事件”](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065766&idx=4&sn=792c2e0aa0defbba125b9aeffcfd1210&chksm=f36e63a6c419eab0a561defb5b66ec4b27a9cf4821a910f2d64455a2cb15fdd063a65f35cf94&scene=21#wechat_redirect)

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
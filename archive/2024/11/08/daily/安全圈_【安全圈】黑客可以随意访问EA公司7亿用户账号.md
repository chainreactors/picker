---
title: 【安全圈】黑客可以随意访问EA公司7亿用户账号
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065766&idx=3&sn=bcdf6497f31db93acd068fb24f76e293&chksm=f36e63a6c419eab04b707515e3ec637038e1f931dd74f1640728e7904bece00c01cfe82fde69&scene=58&subscene=0#rd
source: 安全圈
date: 2024-11-08
fetch_date: 2025-10-06T19:20:02.085606
---

# 【安全圈】黑客可以随意访问EA公司7亿用户账号

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylh59qJDyCI8MyoWRIDeKfkMRbqHJnHibib8hoHiaQFCHEe3H9vp7Lfb2R6ENRVzibYKWBcIGKe4WIQuKg/0?wx_fmt=jpeg)

# 【安全圈】黑客可以随意访问EA公司7亿用户账号

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

安全漏洞

据Cyber News消息，游戏开发人员兼白帽 Sean Kahler 发现了一个影响 Electronic Arts （EA） 帐户系统的漏洞，可以在未经授权的情况下访问任何EA用户帐户（目前EA用户有大约7亿），包括游戏统计数据。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylh59qJDyCI8MyoWRIDeKfkMMlMXeXZaKtk1dyXX5FrU5ZkrtWSFXSVV9ia7mW2czvJAp2YeDrzBHEQ/640?wx_fmt=jpeg&from=appmsg)

该漏洞最开始是由Kahler 在“某个游戏的可执行文件”中找到硬编码凭证后，在 EA 的开发人员测试环境中获得了特权访问令牌。

在扫描了暴露的文档并四处探查后，Kahler 发现了一个带有暴露 API（应用程序编程接口）的内部服务，从而揭开了漏洞的面纱。EA 的内部 API 允许修改被称为 "角色 "的玩家配置文件。Kahler 最初将 EA 帐户状态更改为“禁止”，从而阻止了用户登录游戏。该 API 还允许将 Steam 帐户链接到另一个用户的 EA 帐户。

Kahler 意识到，既然可以将自己的链接账户转移到任何我想要的 EA 账户，那不就可以登录到该链接账户，从而登录到任何 EA 账户了吗？同样，通过使用 Xbox 帐户并将其转移到他人的 EA 帐户，可以使用控制台登录对方的游戏，如《战地 2042》，且不需要验证或密码。

因此，黑客可以利用这一漏洞来窃取用户名和游戏数据，并通过将他们的 Xbox 角色移动到受害者的帐户来登录其他人的帐户。暴露的 API 允许更改用户名、禁止帐户、阻止玩家访问游戏或在没有用户交互的情况下绕过禁令。

Kahler 于 2024 年 6 月 16 日负责任地向 EA 披露了漏洞，对方确认了该漏洞并指定了严重性，并在7 月 7 日至 10 月 8 日期间陆续通过5个补丁修复了漏洞。

参考来源：Whitehat finds flaw that gave unauthorized access to over 700 million EA accounts

***END***

阅读推荐

[【安全圈】Ollama AI模型发现六大漏洞，能导致DoS攻击、模型中毒](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065749&idx=1&sn=b8878258d3b73972d34180a4f45b9858&chksm=f36e6395c419ea83933909751917712797ee725716d53445c905e31288295910cc4fae20086d&scene=21#wechat_redirect)

[【安全圈】德国大型药品批发商遭勒索攻击，欲扰乱超6000家药房供应](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065749&idx=2&sn=d5382d9df68bd0a24d91a977ff18d8d0&chksm=f36e6395c419ea830bbe5f67aa0efba15583dc17a4f01f0bcf375e1810e75abc8c6025aad501&scene=21#wechat_redirect)

[【安全圈】黑客攻击意大利政府核心部门](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065749&idx=3&sn=95609299638b6b94edb1006b1589f9e2&chksm=f36e6395c419ea832e64c39dc60436fa7e2efd302434a8c7fbc922005839ada55ca55c84a2bb&scene=21#wechat_redirect)

[【安全圈】谷歌在Gemini对话AI机器人中增加盲文本水印 可以用来检测内容由AI生成](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065749&idx=4&sn=6e7a08939bc1fa5bc0f516088d6be4c8&chksm=f36e6395c419ea830fe214a47a37b257668ca9ae62ab4e5fca65bf8374f3c0e376ce592fa8b3&scene=21#wechat_redirect)

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
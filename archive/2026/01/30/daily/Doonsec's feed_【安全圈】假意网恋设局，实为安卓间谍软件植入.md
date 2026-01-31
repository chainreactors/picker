---
title: 【安全圈】假意网恋设局，实为安卓间谍软件植入
url: https://mp.weixin.qq.com/s/JIKGn2Xnd--_P9dLMfN4Ig
source: Doonsec's feed
date: 2026-01-30
fetch_date: 2026-01-31T04:02:25.909564
---

# 【安全圈】假意网恋设局，实为安卓间谍软件植入

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljgSmB9m0MJslT2lQTzcI48b6NmXCd2yJmqKkjpIAylZ5Z4d1hndSOrGyLnoEZE1AKBIPZWxFNO2Q/0?wx_fmt=jpeg)

# 【安全圈】假意网恋设局，实为安卓间谍软件植入

安全圈

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

间谍软件

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljgSmB9m0MJslT2lQTzcI48trNWWn8MTvAHYbn4XhzlzWZcrpV19MR3rEAV3bibdicdwsUDbn4tICyw/640?wx_fmt=jpeg&from=appmsg)ESET 研究人员发现了一起针对巴基斯坦用户的安卓间谍软件攻击活动，该活动以**网恋诈骗**为诱饵。攻击者通过一款伪装成聊天工具的恶意应用实施攻击，这款应用会将对话流量转接到 WhatsApp，而在浪漫伪装的背后，其核心目的是窃取受感染设备中的数据。ESET 将该恶意软件命名为**GhostChat**。

该威胁团伙似乎正在开展范围更广的监控行动，包括通过**ClickFix 攻击**攻陷受害者电脑，以及通过**WhatsApp 设备链接攻击**获取受害者的 WhatsApp 账户访问权限。

这些关联攻击活动均以仿冒巴基斯坦政府机构的网站为诱饵，受害者需从非官方渠道手动下载并安装 GhostChat。该应用从未在 Google Play 上架，且默认启用的 Google Play Protect 会对其进行拦截。

ESET 研究员卢卡斯・斯特凡科表示：“此次攻击采用了一种我们在同类骗局中前所未见的欺骗手段 ——GhostChat 中的虚假女性资料会显示为‘锁定’状态，需要输入密码才能查看。但实际上，这些密码是硬编码在应用中的，这只是一种社会工程学策略，目的是让潜在受害者产生‘获得专属访问权限’的错觉。”

这款恶意应用盗用了一款正规约会软件的图标，却不具备任何相应功能，仅作为移动设备上的诱捕工具和监控程序。受害者登录后，会看到 14 个女性资料列表，每个资料都关联一个带有巴基斯坦国家代码的 WhatsApp 号码。使用本地号码能让资料看起来更像是巴基斯坦本地人，从而增加骗局的可信度。当用户输入所谓的解锁码后，应用会将其重定向至 WhatsApp，与该号码开始聊天，而这些号码实际上由威胁团伙控制。

在受害者使用该应用的过程中，甚至在登录之前，**GhostChat 间谍软件就已在后台运行**。它会监控设备活动，并将敏感数据发送至命令与控制（C2）服务器。GhostChat 还支持持续监控：它会设置内容观察者跟踪新生成的图片，并在图片出现时立即上传；同时，它会运行一个定时任务，每五分钟检查一次新文档，以实现对数据的持续收集。

此次攻击活动与一个更庞大的基础设施相关联，该基础设施还支持基于 ClickFix 的恶意软件投放和 WhatsApp 账户攻陷。这些攻击均依赖仿冒网站、冒充政府机构，以及基于二维码的设备链接方案，同时针对桌面端和移动端用户。**ClickFix**是一种社会工程学攻击手段，它通过看似合法的指示，诱使受害者手动执行恶意代码。

除了利用 ClickFix 的桌面端攻击，该基础设施还支持针对 WhatsApp 用户的移动端专项攻击。受害者被诱导加入一个声称与巴基斯坦国防部相关的虚假社群频道，并被要求扫描二维码，将其安卓或苹果设备链接至 WhatsApp 网页版或桌面端。这种名为**GhostPairing**的攻击方式，能让攻击者获取受害者的聊天记录和联系人信息，获得与合法用户完全相同的账户可见性和控制权，从而暴露所有私人通信内容。

***END***

阅读推荐

[【安全圈】抖音崩了](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652073915&idx=1&sn=b745a686b245684c9bdd345d1b77afb8&scene=21#wechat_redirect)

[【安全圈】恶意 VS Code 扩展"ClawdBot Agent"伪装AI助手传播木马](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652073915&idx=2&sn=3ed01239d8e66b938f373a2a52c32bc0&scene=21#wechat_redirect)

[【安全圈】PyTorch "安全"模式被严重RCE漏洞攻破，可执行任意代码](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652073915&idx=3&sn=ad2665e9be5ec05d1f5f1bcdabcfa2d4&scene=21#wechat_redirect)

[【安全圈】Chrome 发布安全更新，修复后台 Fetch API 漏洞](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652073915&idx=4&sn=cc70511df2d49f4ff6dd41538bf3b02a&scene=21#wechat_redirect)

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
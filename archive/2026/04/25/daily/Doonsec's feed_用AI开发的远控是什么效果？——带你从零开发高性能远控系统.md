---
title: 用AI开发的远控是什么效果？——带你从零开发高性能远控系统
url: https://mp.weixin.qq.com/s/flhZhvGBfH0jJikqTKJGpA
source: Doonsec's feed
date: 2026-04-25
fetch_date: 2026-04-26T04:56:32.415374
---

# 用AI开发的远控是什么效果？——带你从零开发高性能远控系统

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/IRUJvvhticxQ9Ua4aibryN3yvMM8RY99NQsQdBricunZSEPjydCiaYian3WBvPpkBh3NBkEicEPdprPh4Alic72JO2Bnpj8cBoY0SXmYw4xNLLDtF8/0?wx_fmt=jpeg)

# 用AI开发的远控是什么效果？——带你从零开发高性能远控系统

原创

安全研究员
安全研究员

CppGuide

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

经过将近一年半的准备，最近打算做一个新的尝试：

计划出开办一个新的编程训练营，带着大家用AI从零开发一套远控类软件，功能对标银孤远控，但性能和稳定性将大幅度优于银孤。包含常见的插件管理、远程终端、远程屏幕、键盘记录、文件管理、代理转发等功能，程序整体框架、网络通信框架、通信协议等全部从零设计，由于AI的赋能，主控和被控支持Windows/Linux/MAC均存在可能性。

成品效果演示：

![](https://mmbiz.qpic.cn/mmbiz_png/IRUJvvhticxSPw166ThDzdD7wUKicUQ5kDBlWmoOcWfrY1xLmQEyENaauSEy2gsXptGCx07wicNekUC3ibUgelVBZGrZrUPabRoibc1oNboiadVTo/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/IRUJvvhticxRWzZvYZkdph6r7ydQC8lQhosmODnQB3P93dboXoL1bKsqvqB4Y3ic5SYYT9NmKS7tdeYoxJZg7nmibzG68gic3CGYVqibUhk0AFYo/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/IRUJvvhticxTCSeaWhibL1XP7FtZamhlvSic5ibnSIiaSUXyibkaCRQK7gtnozJv2wGhicENoN6BK4cLKiaPTFYhJ6aicHEOPe4A0UsnQmOBFTibXgLtc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/IRUJvvhticxQJ74z8d98qnjwz6TeDKic29ggWlDNtsk8ibVGQ8frY6FA8oy2Ap3ckNmctcVyb3Qkwia4Luwaib9Qr65pQZde2BmGt6BH7IBEjmM0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/IRUJvvhticxQX74Rpug0TjvwLic6r8OHs0B6aHYvIDnwDIG0GRzDibZzC1ugpTMVoadCvwb0NKkkxCy2QTFX5NwKv8LxD9kmfq7CzS7wwcFTjA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/IRUJvvhticxSH9X9nv2bO1oW6lTYZZhpTLvq6oZuv5uPaGWukOfOdiakfHPiaXN6uk1iafzEohiaCoOf70yOiccjD2uogwYIoftrX0I5YxIbAtZw0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/IRUJvvhticxRmSgf5KUGE5VI5zAxaQmSTiabadfjC8T00QGNfHpdsZF2icIgTe6GJP7A0V0ZSicgibVEOQ8UXGyvZSEOOnHrgha3O8hyZU255z28/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/IRUJvvhticxRqSOUrExgqUDYH84p4FIWds1ibKu9ve28IkIpNFa1QQqIqLYXVpfzV7iazeH7lrr8qBG2RCB1fSQON8pf1kOGe2XYianoYMMkd4Y/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/IRUJvvhticxSQfKMaGiawwD5PYSoL6K4aSaZ7X9eOD0jJic4ibppjTWeLZoQLDNmwc0WqR8oj7CibSLdaRLBick7jU88zACaKyEoibdeCG6zZHdJbY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/IRUJvvhticxTkUB0JyXdibTCjJtPFLMBg4hzmJKUACN17x3ayCv67ePurlszdSTz7HibYiaKpCuemlicJsskhIdNUHCfnXXK3ZspCTB7dR6lb7kg/640?wx_fmt=png&from=appmsg)

为什么我会选择开发一个远控：

1. 工作生活需要，目前市面上诸如向日葵、TeamViewer类的套件，并没有好用便宜的产品；

2. 由于目前AI的加持，很多代码开发细节可以直接交由AI来做，开发者不再需要花大量精力去关注开发细节，所以从代码驱动型转为产品驱动型更容易，每个人都可以利用AI做出自己的产品，这也是我将个人技术产品化的一次尝试；

3. 自己从零开发，代码可控，功能可控，可自由扩展。

在这个训练营中，你不仅能学习实用开发技能，同时将实战如何使用AI进行中大型项目开发，最重要的，你会深刻的体会到，AI时代程序员们应该掌握哪些知识和能力才能提高职场竞争力，避免被AI淘汰。

开营时间

目前训练营筹备中，考虑功能点非常多，计划采用直播加录播形式。预计五一劳动节之后开营。

报名方式

目前预报名阶段，现在报名特惠价 1300，开营后恢复原价2500。

有兴趣的同学，可以私聊微信cppxiaofang预约名额，加微信请备注“训练营报名”，名额有限，无备注或备注不对不加。

本项目仅用于学习研究，合理合法使用，不涉及免杀，所有报名同学需要签署不滥用协议。黑产和非法用途勿扰。

以下是功能模块列表（计划目标）：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/IRUJvvhticxSw2d9QMXjgU2OLXoL0vjIdgW26UTDbjxkh31738spTNgfxLoRy76pB4xF1maAQIbicIM25avy2VoIuOEF9Wh3HDk1LwRWxTMxI/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/IRUJvvhticxRxaf1VlXHpAHw4icMyHjL99US9F6WQ7ytBBsMYEExibpSFufniaRBbAPthfLYqEWPHFzaczS7qcpSLPewiceVuV5XhQp1xZtCkGII/640?wx_fmt=png&from=appmsg)

计划实现的效果：

这套系统不是功能的堆砌，所有模块都融入大量设计模式和设计思想，并结合小方从业十余年做商业客户端软件和高性能服务器的经验，从零开发。无论从源码和功能都是非常优秀的。

目标：

1. 源码交付，所有模块从零开发，代码风格和格式整齐划一，注释量不低于代码总量百分之三十；
2. 各模块职责分工明确，易于扩展和维护，以通信协议为例，所有的网络解包和装包操作使用统一的入口和出口，在通信层可以随意替换协议格式和增加加密、压缩等处理；
3. 对占用资源做到极致化考虑，内存和CPU使用率低，支持几百客户端稳定在线和功能操作；
4. 新增和扩展插件容易，插件只需要专注于自己的逻辑，框架已经完全处理好插件升级、传输和启用等功能，新增插件无需修改主控和被控任何代码。
5. 所有远控功能均在被控用户明确授权的情况下开启，无隐藏功能，无后门。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/GSweNIrkicYvM1mIwPctlYONEDKJwUfRZ57uAkVR59MpX1cVnmmnyPZ5O9OCuys78Sy6fOEncwfgWpgCo9Tibeag/0?wx_fmt=png)

CppGuide

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/GSweNIrkicYvM1mIwPctlYONEDKJwUfRZ57uAkVR59MpX1cVnmmnyPZ5O9OCuys78Sy6fOEncwfgWpgCo9Tibeag/0?wx_fmt=png)

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
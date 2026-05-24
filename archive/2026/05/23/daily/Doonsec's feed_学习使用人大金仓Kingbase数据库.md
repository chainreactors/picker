---
title: 学习使用人大金仓Kingbase数据库
url: https://mp.weixin.qq.com/s/-flp9CGxDGYP_ekFOFu7-A
source: Doonsec's feed
date: 2026-05-23
fetch_date: 2026-05-24T05:55:24.936055
---

# 学习使用人大金仓Kingbase数据库

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/3YDEbeC7QUglADyg8H11QibJ0zgXcaUb25CJpiaHG4Y4nEWNuVhaTGbeNZNB0GuPUmibX82ZgBoak9qH08cLUiaU3XBpWAKQfiaF0IqIskaXzDicE/0?wx_fmt=jpeg)

# 学习使用人大金仓Kingbase数据库

原创

梦之核
梦之核

核点点

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

本周在调试一个代码开源的知识库系统，默认使用的是postgresql数据库，在安装的过程中产生了一种想法，能否用人大金仓Kingbase数据库软件替代postgresql数据库软件？

基于这样的想法，从人大金仓官方网站上开始学习kingbase。

通过咨询千问，得知人大金仓数据库（KingbaseES）与postgresql之间有着非常紧密的“血缘关系”，简单的说，Kingbase是在开源数据库postgresql的基础上深度开发和优化而来的国产数据库，保持最大程度的兼容postgresql的生态。可以把Kingbase理解成postgresql的一个“企业级国产增强版”，如果具备postgresql的使用经验，几乎可以零成本过渡到Kingbase的日常开发和运维中。

从人大金仓官方网站下载Kingbase的docker镜像，按照文档配置docker并启动，便可以快速的体验Kingbase数据库。

将知识库系统配置的原postgresql数据库连接信息修改成kingbase的信息，启动知识库系统，经过测试，知识库系统能够正常启动和使用，在kingbase数据库中可以验证到数据表正常创建和数据的正常写入。

基于这样的体验，大致可以得出结论，如果原系统使用的是postgresql数据库，那么可以完整的迁移到人大金仓Kingbase数据库，实现数据库软件的替代。

另外通过查看人大金仓Kingbase数据库的文档，发现还能兼容oracle、mysql、sqlserver数据库，基本上覆盖了常用的数据库迁移需求，为此，对人大金仓Kingbase产生了极大的兴趣，也就意味着可以使用人大金仓Kingbase数据库完成许多系统的数据库替代。

![](https://mmbiz.qpic.cn/mmbiz_png/3YDEbeC7QUiamHL0TuncCsAfpp9PMjqbmbOz89Etodg2rKR2XuxiawlK4aMPhEDLNPa99o5y861icYhRGJG8B4Ux9hnkvwGYUIC11TGW5G8KYE/640?wx_fmt=png&from=appmsg)

在学习人大金仓Kingbase数据库方面，主要是观看官方社区KCA视频合集，下载文档进行学习，如数据库的安装和启停，KSQL命令行工具等等，快速的对Kingbase系统性的了解，后面还要更加仔细的学习，今天还把许多文档下载下来。

接下来有新的软件开发任务的时候，决定使用Kingbase，作为一款国产的，并且通过国测测评的数据库产品，值得使用。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/SX1T8B6d6kzpFXDpn6H2UjiaSKR1boMF3KjAPReBZlpEfYIp83icLTJU4gib6dKd1yOH9fiaoTCuXNic1wcM5iaq9dpQ/0?wx_fmt=png)

核点点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/SX1T8B6d6kzpFXDpn6H2UjiaSKR1boMF3KjAPReBZlpEfYIp83icLTJU4gib6dKd1yOH9fiaoTCuXNic1wcM5iaq9dpQ/0?wx_fmt=png)

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
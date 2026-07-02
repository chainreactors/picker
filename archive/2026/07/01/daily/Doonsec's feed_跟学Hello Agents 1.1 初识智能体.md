---
title: 跟学Hello Agents 1.1 初识智能体
url: https://mp.weixin.qq.com/s/MrLgW5oDzRBDt_Ony3lIxg
source: Doonsec's feed
date: 2026-07-01
fetch_date: 2026-07-02T05:52:48.126878
---

# 跟学Hello Agents 1.1 初识智能体

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/TmfJFw8PQ0Jptu85SruzJxqr9jTgyOgqKawj7FdBqebwN5gYTUFDhBUX6TvIs8GWW6zKUibqiann9TLGBOMtXhEskBWAcRO5W7JibKRLQr7aiac/0?wx_fmt=jpeg)

# 跟学Hello Agents 1.1 初识智能体

原创

LIch
LIch

Licharsec

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

假期开始写点记录，跟着系统的学一下，不然学的太分散了，没有深度。找了个感兴趣的Agent项目学习，这个项目比较经典同时有介绍，觉得很适合。

## 核心一 如何调用自定义功能

开始介绍基础的定义，然后要完成的内容是一个天气预报Agent，回顾一下各章节提纲

![](https://mmbiz.qpic.cn/sz_mmbiz_png/TmfJFw8PQ0Iodbp2kWW0Qwhibjrz66Qrsqc95GI0WEdqsctB71pethQer5Kknxma8iaAuEReIl6UNZIkaiaamaqMY2Qfoh6pzMTtM0ibr5ZIPXM/640?wx_fmt=png&from=appmsg)

总结一下核心收获，智能体如何调用的函数，是通过交互协议的格式约束，再通过代码进行正则匹配出Action行为，通过行为去调用对应的函数功能

![](https://mmbiz.qpic.cn/sz_mmbiz_png/TmfJFw8PQ0JUjHXyQqzPZMkIQ1gia6zgEiby5qicA1kEuGOlpUVPvMfbvbbkGvTqhtaJQKhsyPJiblHUpEta96IqZsmf5wuJ0t5p09Cf4YJQEicQ/640?wx_fmt=png&from=appmsg)

# 核心二 如何输出符合交互内容

通过拆分思维提示以及多轮循环进行可控范围内运行

![](https://mmbiz.qpic.cn/sz_mmbiz_png/TmfJFw8PQ0KhFDjhRP2QM9eGibznBgqYq7d2cg41aDH4pHBUibicSdzHNAnd1bSC1pqjUgeqcpOdibia3C4k595aSVT7yuslmmxXlNvibibpxC1NvQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/TmfJFw8PQ0Khibibyia1khRQKqDBOPsqhicfsC1hYHMF1tWnGFx8wVgekvXxRGUfN5D3uhVCAuDEPOY7G2tCic9XXyaQ1tdI6lTSZfGDfD76icU1w/640?wx_fmt=png&from=appmsg)

# 自我思考 工具的调用途径问题

项目里给的是自定义函数来实现一些功能，所以在写函数的时候给的模版就是直接写成一个json格式，然后根据action正则提取对应的键值。

![](https://mmbiz.qpic.cn/mmbiz_png/TmfJFw8PQ0Koa0l3J9OzKRkJ91GIfllJQaTMm0A8vgQmN3PuAJrn9tawFsDPVleNRs5To8m4LtaX3bQvP6icAhQJY3uXr5DMledgibl0Eqmvc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/TmfJFw8PQ0IJyuYbLt3d5HTGzG5tHvzDrN6NkguPaicqMB6nfDLicpftqmt5EMEZoUdE2EOgSDCia9GFNuAcUprVOQ53ic76TdjDlKnN93SV5eI/640?wx_fmt=png&from=appmsg)

这里自己想着把写的SPiderx爆破放进去，但因为是个项目工具，所以不适合直接调用，然后写成一个工具一个项目分开的结构，改了一下工具函数使用，这样更清晰加了一个描述

![](https://mmbiz.qpic.cn/sz_mmbiz_png/TmfJFw8PQ0KMRSh4oShtInfvRfYJzwYWOWED3C9t388upibc6FM67Gn4zrHLKerWh55u6cAshOCyguelsStHOXG1PQjXDCOp8DEYQKn9ianVs/640?wx_fmt=png&from=appmsg)

然后写一个tool.json记录可以调用的工具列表

![](https://mmbiz.qpic.cn/mmbiz_png/TmfJFw8PQ0J5UOSBDDA4FzJC8ceVSzcAqdOMEfGQ5GkYgYWPLY2raOWNzriantEYBrjQGg0ddHavZWsNk7ibRHHnpibfIvYkz9B9ibJ7v5sZgG8/640?wx_fmt=png&from=appmsg)

再加了一个工具类加载对应的函数，不过这里不会用的AI写，总感觉怪怪的，把所有模块都一次先导入了。

![](https://mmbiz.qpic.cn/mmbiz_png/TmfJFw8PQ0Lb2RIdgtNrpLqAflfG9OM4cEicO70htUW2GibdU79EnDtBvx0UtPL7gqGXnrACpGkGqQDDhcr476haHebBvSz5LewOFunmPibcss/640?wx_fmt=png&from=appmsg)

第一章主要就实现了简略的一个Agent调用天气预报，产生了一个小疑问

1.写的这些自定义函数和mcp什么区别?

了解了一下

![](https://mmbiz.qpic.cn/mmbiz_png/TmfJFw8PQ0IMrbV09v6k1XgF5VYVibd1zsSN8tSRVT381rNzuW3X95JeZDnevnyIU59L7siaMic8TyIAn7YaA8EYiaMvOuGu07zYtuBcicIAqYM4/640?wx_fmt=png&from=appmsg)

下一次的内容为下一章节以及看看能不能自己优化一下把加载工具写成mcp格式，自己拓展一下，不知道是太久没写还是开发基础太弱，总感觉函数代码一写长自己就遗忘前面写的....

预览时标签不可点

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/JKnIzkTkBfPNgKsicaKUQw7mKKPPyvhjF4icfeg8mweyaoSUPtGibkjhl2nF1iaaxKvPYztNHvgEPtKGpv1QCIHkrA/0?wx_fmt=png)

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
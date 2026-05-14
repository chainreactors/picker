---
title: SRC实战 | Host碰撞还能碰到吗？到底该如何挖？单靠Host碰撞打榜某众测第二
url: https://mp.weixin.qq.com/s/BS0zQcffy3IgZHNTpAOSOA
source: Doonsec's feed
date: 2026-05-13
fetch_date: 2026-05-14T05:42:57.167401
---

# SRC实战 | Host碰撞还能碰到吗？到底该如何挖？单靠Host碰撞打榜某众测第二

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/6mEJuibtxKvPSDwus99xRAZcjj4ic6a6klqmChXv8d8Fmn5SsYUNibcI0C61jIIicqpOZlibPg7o9hhB2fCiaLmvQJaIKGiaCVCdAPicNpHONK2YYUc/0?wx_fmt=jpeg)

# SRC实战 | Host碰撞还能碰到吗？到底该如何挖？单靠Host碰撞打榜某众测第二

原创

安全艺术
安全艺术

安全艺术

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

*注：公众号已开启留言功能，师傅们有啥想讨论的直接留言就行哈。*

# 0x00 交代下背景

上周有师傅私信说想了解下Host碰撞咋打的。

![](https://mmbiz.qpic.cn/mmbiz_png/6mEJuibtxKvNBhqdchHREQ09ibibPSA7g5r41dDk3A8v1BXARO65rTNn7CCac99Nicach8X6ClnS7X4OdKzic6S8Ln1aELCNH1gtDbLEdelMFL0w/640?wx_fmt=png&from=appmsg)

攻防间隙抽个时间简单分享下吧，还是以实战为主，拿上个月的众测为例，靠着host碰撞打到第二名。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6mEJuibtxKvPiasLnldia15DxtzXJS7M49VBYs8PxIcZhcxQbPiaeuweibPBdcBsTO8bpF5ooVZKm32rE4d7icgPgg61Y7QHicjjJWTwHgo9npC2mg/640?wx_fmt=png&from=appmsg)

# 0x01 直接上干货

原理啥的不多说了，个人还是喜欢实战为主，挖不到漏洞的原理烂熟于心也没用，哈哈。

我的打法主要分两种情况：

第一是情况比较常见，直接收集目标域名和IP进行碰撞完事，很多工具都能实现，比如ARL。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6mEJuibtxKvOpzqKm9XY0My9ccKOdbq2CiaWC8Pvwz0uhsujwk7WnDictz8F4ickq97jDWicpGS7SnqoribpBdlBAdbJj2KkNpFuQvvqMYINviaVJU/640?wx_fmt=png&from=appmsg)

第二种情况就是用常见内网域名字典拼接目标域名。

举例：

yapi拼接xxx.com

minio拼接xxx.com

harbor拼接xxx.com

apollo拼接xxx.com

confluence拼接xxx.com

superset拼接xxx.com

......

碰撞成功后利用比较简单了，改系统host文件或者用burp自带的dns绑定都行。

注：以上两种情况不要局限于跑一次就完事了，紧盯目标单位，建议每天都碰撞一次，因为实战发现碰撞出的网站并不是一直都开着的，很多都是临时开着的。总而言之，多多碰撞，才有惊喜。

# 0x02 我的实战小成果

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6mEJuibtxKvMq7VYWn1ib9Dl2acwJmaQiaC7kJBwiaNWuT4rWJ3gfq274ic3BsENGwjZJ9mleanSzToE7VsV9NgM7347qFr1avta4c5N4Y3ZDXgo/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6mEJuibtxKvNfZYaDgtW8sNCQlNZzRxT885gibibw7wINWVMjNrTJttibDSrMw0BicicILIoxxgFvquwNrDATqY2oat7r0HdInBbGnMGXr4vaMgicQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6mEJuibtxKvMxE1X2PcN2ynEfT2nkA3pn22ecjCgwfkhx5jQpsjdMZodhZia4PuBaGgWzkEnmPme4aOFoocKnuBlvzGibFN1srYy514CNYjvgo/640?wx_fmt=png&from=appmsg)

# 0x02 我的实战小圈子

感兴趣的师傅们可以回复"**dddd**"获取联系方式，无意勿扰哈，谢谢。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6mEJuibtxKvPaS6qoDSUI1JSasHC4Le1WHuOcaAJ5TzqBA1U9s9iaglS5aXEUOSLS1rrIq13fPvegn2YErKPqYkhgHPvyO8icNXUGXkpb2q22A/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2Oo4NY9fLLoomQgld6ia6hfpRbrvGyVibgUgzOauMBthcywVUOU2bSRtSyjunLPVQNqRAO2YKH85bPMg/0?wx_fmt=png)

安全艺术

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2Oo4NY9fLLoomQgld6ia6hfpRbrvGyVibgUgzOauMBthcywVUOU2bSRtSyjunLPVQNqRAO2YKH85bPMg/0?wx_fmt=png)

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
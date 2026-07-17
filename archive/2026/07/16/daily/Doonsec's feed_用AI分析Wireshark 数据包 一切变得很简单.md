---
title: 用AI分析Wireshark 数据包 一切变得很简单
url: https://mp.weixin.qq.com/s/AYxik2PgkiDOEmLvvmzv8w
source: Doonsec's feed
date: 2026-07-16
fetch_date: 2026-07-17T04:58:54.050764
---

# 用AI分析Wireshark 数据包 一切变得很简单

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6OrHemEOukhorZciagFLlaP5RGatEteq3ADOVRF5Gqhy1paibV0LJVbHXpA6E4rKwvoiabhicUW692nD4NTg7BZZenXEgMSCeVCUQY/0?wx_fmt=jpeg)

# 用AI分析Wireshark 数据包 一切变得很简单

黑白之道

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 网络抓包是运维重要环节，能帮助我们分析当前的网络环境存在的异常。因此，`Wireshark`也被大家所熟知。

在之前的文章中，我们也讲到过Wireshark的入门使用和高级玩法。大家可以在历史文章中查看。现在AI的介入，能否为新手提供更便捷的流量分析呢？让我们一起试试吧！

![图片](https://mmbiz.qpic.cn/mmbiz_png/1N1JeeKBorfBue46Pn2ibRbFzUocwqmssXJUQPAxjxeDu2bHlyCucjgKVX5Mn7ELzGSPGBDE4Xuc5SFvCG43UV1YviaicjyGWibRNDTWUOqCdFs/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=0)

运行`Wireshark`后，我们开始捕获数据包。在捕获过程中，我们可以进行网络访问和其他操作。![图片](https://mmbiz.qpic.cn/mmbiz_png/1N1JeeKBordZhew184CAZCibvODoxby08cyfn5IJKOBYA4anMkAq3rTHiaxc6JgHhfV89WrVjCW6WwbfuOJuUcmKV69wDnaohGXe4aVgzwM4U/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=1)抓获完成后，保持数据包。
接下来，让我们通过AI工具claude来分析。![图片](https://mmbiz.qpic.cn/mmbiz_png/1N1JeeKBorfDibd5OaUA3rxjsAS98UDsQTeN0GnTWeTxNib3gRfb15wmZJI1dslBAb3ujPqY2ceWk7XC1MibhDe6a2ntWrzQuWrujgj9epwGTE/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=2)接下来，让我们一起来看看对数据包的分析结果吧。![分析到的设备](https://mmbiz.qpic.cn/mmbiz_png/1N1JeeKBorddGOC55rA9jyKJlg9WvTDKRfzmmt6wZn67U9R5GlOeWuk0p8gwbuAjV5mf6ze4Ngw1yNn6QMELdvHo7BsMf2Y03jQx2JUVv1o/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=3)

分析到的设备

![协议分析](https://mmbiz.qpic.cn/mmbiz_png/1N1JeeKBordibvkBLShUlMj1Xibwd6PpYwEvuuONmjcyQ8bnGbn14FHkKV1VXYWjesuwbBuibKEm6JkPycXVdGqzIfG7WfkBJC5HqZZWVMx4Ww/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=4)

协议分析

![登录HTTP网页时，获取到了账号和密码](https://mmbiz.qpic.cn/sz_mmbiz_png/1N1JeeKBoretBD4TJtYwpRfLMXLLmGC2L93FU32SpXdfHXtUjbKvmh0GU2mspeoUJX4wthyEzErb4WHx2vFgLLyRWGgmJLvWlRrATOoJQUQ/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=5)

登录HTTP网页时，获取到了账号和密码

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/1N1JeeKBoretkoKBbeOmaxkA0AzLRJEn5HDicYHiaOGL6hRicdkZuXLVZVic19bxuiajvOjkDbQUMnLZv0agQa6KtqlBWEqf2ibTnFe4MEqQGsN5E/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=6)![图片](https://mmbiz.qpic.cn/mmbiz_png/1N1JeeKBorc0ZMQdpyicJ8Bjj4ISZs9jxgTYJqPCMOTZBzzYibicEx3kxLVI1rqBn59c0G2bwK0KSbQUibg92liaAjib9CqsXXQ4ZISUCYXY7Wko0/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=7)![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/1N1JeeKBorfDJibyqtyOBibl423MUMERmeKftEtt8Y8MAkpSMCV8pswkxYJKiavQy5yiby6gbu6icj9LtIkb2x9GKa4kSATavXwaNrHlDu3cNJicI/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=8)如上，我们接入AI工具，可以轻松的对抓到的包进行数据分析。让小白也能轻松玩转流量分析，感兴趣的小伙伴快去试试吧！

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/3xxicXNlTXLicpdp8GZxicJpcFIZglvakzYRZiaqt6W61hfgibjeymOgiaGqRsgNvgWIacMj7Gk4PIZ4o2NtW1zb9P6Q/0?wx_fmt=png)

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
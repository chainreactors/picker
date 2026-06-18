---
title: 补充：Hermes的应用（十二）：Hermes Desktop中SSH Tunnel配置过程
url: https://mp.weixin.qq.com/s/g_NwPjk3F6lKYsN3xSvCeA
source: Doonsec's feed
date: 2026-06-17
fetch_date: 2026-06-18T06:46:54.467589
---

# 补充：Hermes的应用（十二）：Hermes Desktop中SSH Tunnel配置过程

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2PhZXrB0gN4zpk50xqepzjAzLZ5iaSXVuzumP0lUBzn0uhNLcictwCtdicuKxaN33ORJt0eSoYAd0kUkVqNQ3C8Wy4mk14EXELogfniahRHp2BE/0?wx_fmt=jpeg)

# 补充：Hermes的应用（十二）：Hermes Desktop中SSH Tunnel配置过程

原创

MicroPest
MicroPest

MicroPest

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

在《[Hermes的应用（十二）：Hermes Desktop中SSH Tunnel配置过程](https://mp.weixin.qq.com/s?__biz=MjM5NDcxMDQzNA==&mid=2247490780&idx=1&sn=747a69b0e792aa8bd60ea0a6952b6981&scene=21#wechat_redirect)》中我介绍了SSH Tunnel的连接过程，有网友朋友连接后，在连接kali的Hermes端的大模型出现了问题，我再延伸下。

1、我们的Hermes Desktop客户端程序是在windows下运行，首先建立c:\users\administrator\.hermes目录以及其下的.env文件，其内容只有一行，如下图（以我的为例，api-key）：

![](https://mmbiz.qpic.cn/mmbiz_png/2PhZXrB0gN7mBVbibR6owS7jUdIRM66WAicpuwwDVxVkJRY7etpyI5szZAjbFAmTny17dc49OzHMhgdN4bWyUATyGSqbzdUFiajxEuHphX9dq0/640?wx_fmt=png&from=appmsg)

2、在Hermes Desktop程序中提供商这里，设置如下：

![](https://mmbiz.qpic.cn/mmbiz_png/2PhZXrB0gN737fNbXOZxlzC6h9LEkBP93Qax8ibsdibzjibuxy21v7yF2BBoMA8cjAwJCzNy3PXZNa5ZNUkrIzjBokCaZzpw4TTPln5Odofnms/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2PhZXrB0gN7dr2g488ADh3qAibSibK8q9ZUtE4HrKO51FEbqWEoFiaIyO6uIgkYUYVLAygUly8ia0T5aHJGnfIfzxAstr7bTasUe6IzZW5llzgQ/640?wx_fmt=png&from=appmsg)

在模型这里设置如下：

![](https://mmbiz.qpic.cn/mmbiz_png/2PhZXrB0gN7ejP3wMFJu3MJRbKHj4f5obA87ia1rEiacYx4mXNM2ZqZMgzTiaEt2x0MTTQfjxaRpC5EBvmGK5yv0aiapgo7JR2vxXqCibgFxYuicg/640?wx_fmt=png&from=appmsg)

3、重启Hermes Desktop程序后，你会发现：

![](https://mmbiz.qpic.cn/mmbiz_png/2PhZXrB0gN6iafWfunfAjciaZ88BEpKb3kia82iabdu3qdJUZkibJicJAib9DosLS9J6rbc3QbvRCicoCl9cviamPKjoNqYNSJfj33IPERe1icEVoJ6AQ/640?wx_fmt=png&from=appmsg)

虽然这里出现错误提示：Missing OPENAI\_API\_KEY — required by the active provider.     不用管它，这句提示曾误导了我一段时间。

现在，你可以正常工作了。

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/2hnvgPYNzpI857XC5Kft3W5TyR4cickrqaIUibKveibjF4531l9HGGu8dISFz0Yr6OUkCHfulChWC2acVmh4b39dg/0?wx_fmt=png)

MicroPest

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/2hnvgPYNzpI857XC5Kft3W5TyR4cickrqaIUibKveibjF4531l9HGGu8dISFz0Yr6OUkCHfulChWC2acVmh4b39dg/0?wx_fmt=png)

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
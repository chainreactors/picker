---
title: 【免杀攻防】基于Golang的图片隐写免杀
url: https://mp.weixin.qq.com/s/VJu8AMUtG8U0gcoRotWNUA
source: Doonsec's feed
date: 2026-01-31
fetch_date: 2026-02-01T04:23:28.628746
---

# 【免杀攻防】基于Golang的图片隐写免杀

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/v94hWOZcBpyhqpnLtJZsEGfuUuTmSqZYoqD4dAuajOib9jfvxLEBJOG84BvT7icYOzSYKTTRF0FxWVU7wZq4m9yQ/0?wx_fmt=jpeg)

# 【免杀攻防】基于Golang的图片隐写免杀

原创

平凡安全
平凡安全

平凡安全

![]()

在小说阅读器中沉浸阅读

**「你可以不屠龙，但不能不磨剑」**

## **「前言」**

网络安全技术学习，承认⾃⼰的弱点不是丑事，只有对原理了然于⼼，才能突破更多的限制。

拥有快速学习能力的安全研究员，是不能有短板的，有的只能是大量的标准板和几块长板。

知识⾯，决定看到的攻击⾯有多⼴；知识链，决定发动的杀伤链有多深。

## **「基于Golang的图片隐写免杀」**

首先介绍我们的免杀思路是通过将恶意代码（Shellcode）进行隐写处理，嵌入到图片文件中。随后，将用于拉取并执行该Shellcode的程序伪装成正常的图片文件，当目标用户打开“图片”时，实际会触发隐藏的恶意行为，实现上线目的。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/v94hWOZcBpxzRDhtD30bs9ehrjwqSRg3EOdmPpcdQcicrchTnIEpV2pXJv3YWibd2cBXF4JniaYc8T3Gdy3JNNtog/0?wx_fmt=png)

平凡安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/v94hWOZcBpxzRDhtD30bs9ehrjwqSRg3EOdmPpcdQcicrchTnIEpV2pXJv3YWibd2cBXF4JniaYc8T3Gdy3JNNtog/0?wx_fmt=png)

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
---
title: 【钓鱼攻防】浅谈制作免杀excel文档钓鱼
url: https://mp.weixin.qq.com/s/_hnxh-3bRCXJlbRCp9HmHQ
source: Doonsec's feed
date: 2026-01-24
fetch_date: 2026-01-25T03:50:41.341635
---

# 【钓鱼攻防】浅谈制作免杀excel文档钓鱼

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/v94hWOZcBpyhqpnLtJZsEGfuUuTmSqZYoqD4dAuajOib9jfvxLEBJOG84BvT7icYOzSYKTTRF0FxWVU7wZq4m9yQ/0?wx_fmt=jpeg)

# 【钓鱼攻防】浅谈制作免杀excel文档钓鱼

原创

平凡安全
平凡安全

平凡安全

![]()

在小说阅读器中沉浸阅读

**「上班让人感到最可怕的地方是，它居然让我因为盼着退休而期待衰老，而不是好好珍惜剩余人生里最年轻的每一天。」**

## **「前言」**

网络安全技术学习，承认⾃⼰的弱点不是丑事，只有对原理了然于⼼，才能突破更多的限制。

拥有快速学习能力的安全研究员，是不能有短板的，有的只能是大量的标准板和几块长板。

知识⾯，决定看到的攻击⾯有多⼴；知识链，决定发动的杀伤链有多深。

## **「1、CSV注入之RCE」**

CSV公式注入(CSV Injection)是一种会造成巨大影响的攻击向量，攻击这可以向Excel文件中注入可以输出或以CSV文件读取的恶意攻击载荷，当用户打开Excel文件时，文件会从CSV描述转变为原始的Excel格式，包括Excel提供的所有动态功能，在这个过程中，CSV中的所有Excel公式都会执行，当该函数有合法意图时，很易被滥用并允许恶意代码执行。

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
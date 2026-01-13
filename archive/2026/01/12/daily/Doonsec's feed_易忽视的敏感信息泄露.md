---
title: 易忽视的敏感信息泄露
url: https://mp.weixin.qq.com/s/b9fPdO_Bbpzdpc67uzkwKg
source: Doonsec's feed
date: 2026-01-12
fetch_date: 2026-01-13T03:27:02.951018
---

# 易忽视的敏感信息泄露

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ib9b5DLqe7gQ0QRBHOnjELSZoicjuWZGbicu4Ssg3JdMVictA2ibmR3LoAr4PgzSQY8Q8fYO98rx1Ohic7maBic6ht2cw/0?wx_fmt=jpeg)

# 易忽视的敏感信息泄露

原创

pippybear

安全无界

![]()

在小说阅读器中沉浸阅读

声明：请勿利用文章内的相关技术从事非法测试，如因此产生的一切不良后果与文章作者和本公众号无关。

写了2期的burp小脚本，终于又回到了搞事情上，不过这次要讲的内容思路其实很简单，几乎是有手就行，但是却又很容易被忽略掉，所以就有了本文，目标是之前的一次授权红蓝对象。话不多说直接上正文。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ib9b5DLqe7gQ0QRBHOnjELSZoicjuWZGbicUTHaJzDHBqvsiabw96Ac6Cu1A1xV5AKBnR0LtgVny5Qytr5BA0sAuSw/640?wx_fmt=png&from=appmsg)

乍一看目标，就有点像各个公司的官网或者首页系统，也就是功能不多，而且基本挂的都是静态页面。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ib9b5DLqe7gQ0QRBHOnjELSZoicjuWZGbicsLCmqpyemUG1GlPlUSiaoNKd62tZt6qIKn60v0FysBzKgxJia9C9KziaQ/640?wx_fmt=png&from=appmsg)

遇到形如这些的系统，基本上大部分大黑阔在做红蓝对抗或者大规模检查时，就会很快的点击过一下基本功能就直接跳过了，有些时候那就错过这妥妥的敏感信息啦。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ib9b5DLqe7gQ0QRBHOnjELSZoicjuWZGbicgBZf9g8IVv5RoPMicN8Tv1h3Ifda82OnabktXfhD3nJx34yyMu7xggg/640?wx_fmt=png&from=appmsg)

这里思路就很简单，点击基本信息，UI上看到的是这个样子的，虽然有姓名和手机号，但是也不构成三要素。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ib9b5DLqe7gQ0QRBHOnjELSZoicjuWZGbic0XibhYnzM30Vl8HqPqoOrhB93NYy8DSWXX6uqGIUKq4ibD80PNKohDIA/640?wx_fmt=png&from=appmsg)

但是，API给你的结果可就大不一样了，不仅姓名、手机包括身份证ID以及其他敏感信息都直接未脱敏响应出来了，而且也可以直接遍历ID。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ib9b5DLqe7gQ0QRBHOnjELSZoicjuWZGbicmBfqW5iagwbo3oh8VXuDzvXIxiasDN9E2lRp2XMicQicKrQU7dykUicCpoA/640?wx_fmt=png&from=appmsg)

所以，看到类似的这种站点，可以停下来多看看API的响应结果，当然也可以写一个小插件来提醒自己，防止错过送来的大洞（虽然这种出现的几率不大，但是有时候也会有，所以不要被习惯带走了漏洞，有些时候很多漏洞反而出乎意料的简单粗暴）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ib9b5DLqe7gQ0QRBHOnjELSZoicjuWZGbicFBYzZcsG7Aicc43oCgu0QPVnfiaUcjd6wKo9QyQ4EQEt7xwgsCqSdBhw/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/ib9b5DLqe7gRWFX6SiaQE368qzz3ruUmbnpAzmoIcmWYrXOnic1DzRllicgLMZ3NZ49q4CG4Tq7mmIkL8oyibfLfMqw/0?wx_fmt=png)

安全无界

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/ib9b5DLqe7gRWFX6SiaQE368qzz3ruUmbnpAzmoIcmWYrXOnic1DzRllicgLMZ3NZ49q4CG4Tq7mmIkL8oyibfLfMqw/0?wx_fmt=png)

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
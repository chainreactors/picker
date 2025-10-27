---
title: 【电子取证】GPS数据轨迹
url: https://mp.weixin.qq.com/s?__biz=MzAwNDcwMDgzMA==&mid=2651044863&idx=2&sn=58d3aa13bceb52610650b047c7782d3e&chksm=80d0f40eb7a77d188a8a2869dd31f0f9c4cff8ee3ed2832a954dbf75cfc3ae0f30a78662e0fe&scene=58&subscene=0#rd
source: 电子物证
date: 2023-02-07
fetch_date: 2025-10-04T05:52:27.803621
---

# 【电子取证】GPS数据轨迹

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/dDhDhftpRFsxAm7KW73dFEh8NZoaT8nunN1CKeNaGyibYux0YyuVDleaNGYhkoc7w7eibpNjCboQBQqLDtibDfRrA/0?wx_fmt=jpeg)

# 【电子取证】GPS数据轨迹

电子物证

以下文章来源于Th0r安全
，作者达达

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM5HPm2axJYtYJLnANlwalWdJoJC1pECko6Qqmtp6iaEBNg/0)

**Th0r安全**
.

深耕网络安全行业，文章内容涵盖安全开发，病毒分析，电子取证，内网渗透，WEB渗透等安全相关知识

## 前言

电子取证当中，我们有时候会碰到关于GPS的情况，弄清楚GPS的取证相关知识点，可以帮助更好的判断。

参考书籍:<<电子数据取证>>

## 正文

在这之前，我们要先下载好，两个工具，工欲善其事必先利其器。

一个就是我们经常使用的FTK IMAGER

![](https://mmbiz.qpic.cn/mmbiz_png/GIRBFLSfaJJc4jPyunwYA83EBiavOoQUCyHOG6kAMqzkhaEIlfASm48UehAP1RCEADXRE71c4RUOcFWEkZA2xGA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

另一个就是Google earth pro

![](https://mmbiz.qpic.cn/mmbiz_png/GIRBFLSfaJJc4jPyunwYA83EBiavOoQUCiajxjo7oqRGc6jt1gwmuK4XbbJbKo99XCx4toTcZU7bc6nEV76mAJlA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

![](https://mmbiz.qpic.cn/mmbiz_png/GIRBFLSfaJJc4jPyunwYA83EBiavOoQUCjLSKJ1G2CIKyS5A8ibvrcLO5WPic4Y2HcOPAw5PyNrCKVNBib2ucbtMicg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

在开始之前，我们要简单了解一个文件格式GPX。

GPS交换格式(GPX)是一种轻量级的XML数据格式，用于通过互联网在应用程序Web服务之间交换GPS数据(航点、航线和航迹).

航点可能是用户录入的，想要未来导航到达的位置，也可能是用户录入时所在是位置。，并不意味着用户曾经到达某个特定的地点。

![](https://mmbiz.qpic.cn/mmbiz_png/GIRBFLSfaJJc4jPyunwYA83EBiavOoQUCdIKkRrXpgnv1W5LJrjtcCJ30mJ809d7Km0nCmH3L7Cbiaibye2gDQhVw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

航线:

如果用户希望以特定顺序导航一系列航点，那么就形成一条航线。

航迹点是GPS设备记录的它曾经到达的位置的信息。

![](https://mmbiz.qpic.cn/mmbiz_png/GIRBFLSfaJJc4jPyunwYA83EBiavOoQUC79Xq8U7iaEZAacV3zzY8kcHexdTuxRksGhcYZKdaTGQT52mP78b2mVQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

在一个GPX文件中，这些数据是比较大的，所以需要借助软件来帮助更好的取证判断。

我们这里用一个从GPS上导出的镜像文件来分析。

打开FTK

![](https://mmbiz.qpic.cn/mmbiz_jpg/GIRBFLSfaJJc4jPyunwYA83EBiavOoQUCfqfGPicZBwUbjDRz9ibwTLXB1wdmbq8KuLT4q4NgxEog0TZpj2WsNiaaw/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

导入之后，打开目录。

![](https://mmbiz.qpic.cn/mmbiz_png/GIRBFLSfaJJc4jPyunwYA83EBiavOoQUCF9hWQjdyT7SI9awymeuzbaTepultSTMaaTLeZOv2icngP6le1YFtH3g/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

打开GPX，导出一个文件。

![](https://mmbiz.qpic.cn/mmbiz_jpg/GIRBFLSfaJJc4jPyunwYA83EBiavOoQUCgr0HH6WDrs1ucnRrdhXG6cLIRDemZ5rCfWjWDibvg2SgPkjzyQMBueQ/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

用Google earth导入

![](https://mmbiz.qpic.cn/mmbiz_jpg/GIRBFLSfaJJc4jPyunwYA83EBiavOoQUC9jib8mbezdBNvkBk6wFlaNsLE5rzo2XIfhBIibiaRTBOF1M7lTYMfbwnA/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

可以在Tracks中找到详细的跟踪记录。

![](https://mmbiz.qpic.cn/mmbiz_png/GIRBFLSfaJJc4jPyunwYA83EBiavOoQUCz5nqpCNy8nn0nwk5TnwpYRicbjo2cwkCjDzkcG2EY6bOJBbNt1iaZMsw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

可以通过点击下面的按钮，模拟踪迹。

![](https://mmbiz.qpic.cn/mmbiz_png/GIRBFLSfaJJc4jPyunwYA83EBiavOoQUCkEHVAiamasukowm0jTZs03MmiaMA1A8oyUe2vA3PDGletAxo7C9xglicA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

![](https://mmbiz.qpic.cn/mmbiz_jpg/GIRBFLSfaJJc4jPyunwYA83EBiavOoQUCmJVyrYlyHPvosdJxicITMCEuv5aaRIKianmGhGn4gKQJaIKiaB1Urckpw/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

这样子我们就能知道该GPS的使用者的踪迹了。判断踪迹也可以通过我们之前说的注册表中的WIFI连接记录来知道。

来源：[Th0r安全](https://mp.weixin.qq.com/s?__biz=Mzg3ODY3MzcwMQ==&mid=2247490640&idx=1&sn=7c79f71a1452b569f196f238dea6d254&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/dDhDhftpRFvypLIddOk8EJNwFmGv5sw40Ty0d9OMXUbicPtzt610wXiaf0l7HdpW9JXT9OZf3JbuNh3FvUPJnAKQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/dDhDhftpRFuouuxbQ44msKkdjic0C8WOQrHEN6rex1hiblHTTIpApR8safvHvB9zXorQTMStvvyN2zO8xjOJd5vg/0?wx_fmt=png)

电子物证

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/dDhDhftpRFuouuxbQ44msKkdjic0C8WOQrHEN6rex1hiblHTTIpApR8safvHvB9zXorQTMStvvyN2zO8xjOJd5vg/0?wx_fmt=png)

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
---
title: 【探究】APK中第三方打包APPID解密过程
url: https://mp.weixin.qq.com/s?__biz=MzAwNDcwMDgzMA==&mid=2651045164&idx=2&sn=c38176caec0fc1ac05b8f3df2242f4a7&chksm=80d0f2ddb7a77bcbe7e810a6169a34facb1c7e387e472175a0b7827f85023c5dcd71f2dd31cb&scene=58&subscene=0#rd
source: 电子物证
date: 2023-03-08
fetch_date: 2025-10-04T08:55:54.267414
---

# 【探究】APK中第三方打包APPID解密过程

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/dDhDhftpRFtpOWyJMpaamd2JUvQApZwbylMhxIv9JtoV5nQBUicyDm4lPxZmmQZlu7Ibp44KJ8DRy6QjwyKSOng/0?wx_fmt=jpeg)

# 【探究】APK中第三方打包APPID解密过程

电子物证

![](https://mmbiz.qpic.cn/mmbiz_jpg/mTA5icOvVGeeIeicfA4LtvGBa8N0G5Ayb6Xghu0N3ibI2wG6LjkpXE9icfplxeynDcFJiaoQUJOicLFZVfnCBSxOdJqg/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

![](https://mmbiz.qpic.cn/mmbiz_jpg/mTA5icOvVGeeIeicfA4LtvGBa8N0G5Ayb6bLtI4iaia0A4y8OALNfWw2mgXVViby1ADw8erEU2x3p6gvxToNX30aDDg/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

![](https://mmbiz.qpic.cn/mmbiz_jpg/mTA5icOvVGeeIeicfA4LtvGBa8N0G5Ayb6PJ9SlVVuINor833QNKXBIxicvqVM2riaTUqfSLbbSw4riaibtq3YEyCwDw/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

![](https://mmbiz.qpic.cn/mmbiz_jpg/mTA5icOvVGeeIeicfA4LtvGBa8N0G5Ayb6bn7nux3lcLW9QrxzCpPhJpY25d0drxoBlmmHfHicuZKqqUSfay8Lk2Q/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

![](https://mmbiz.qpic.cn/mmbiz_jpg/mTA5icOvVGeeIeicfA4LtvGBa8N0G5Ayb6qh507SXViaHdicpqULFpKnAbGpibKgibOkGibeyXepc9KicJa7SlvqcZP1QA/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

![](https://mmbiz.qpic.cn/mmbiz_jpg/mTA5icOvVGeeIeicfA4LtvGBa8N0G5Ayb60JiaTqsZsX9sU1Vaiag1zNgCYGNgMlLABUibnmF8fImxgaq6W7OIs3Atg/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

![](https://mmbiz.qpic.cn/mmbiz_jpg/mTA5icOvVGeeIeicfA4LtvGBa8N0G5Ayb60Kn9zuVic0lLM6zg9eDjhuR5uHJWfSCgoTmRZia4oNMpFIPQZQrTr2lQ/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

转自：[网络安全与取证研究](https://mp.weixin.qq.com/s?__biz=Mzg3NTU3NTY0Nw==&mid=2247485298&idx=1&sn=6bf3684015ee308199778f0f48dd378c&scene=21#wechat_redirect)

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
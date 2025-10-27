---
title: 【培训】Osint开源情报练习 #002
url: https://mp.weixin.qq.com/s?__biz=MzI2MTE0NTE3Mw==&mid=2651148736&idx=2&sn=ebee4c79a769e10968179969c634d83a&chksm=f1af26fac6d8afec43791f1e2d2945b5e030bab5b7a6d0c003eff48d2af4aa4bbae72ead9e03&scene=58&subscene=0#rd
source: 丁爸 情报分析师的工具箱
date: 2025-01-30
fetch_date: 2025-10-06T20:11:14.134753
---

# 【培训】Osint开源情报练习 #002

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/B0AKMb5va5xiao1Zh0Q2B5XgBp90R5wJpAAKCgwgR3ArOR27aL1cPkYWchZwqpFRsjtviaHPHFTcmNUNOByAbQ7g/0?wx_fmt=jpeg)

# 【培训】Osint开源情报练习 #002

丁爸 情报分析师的工具箱

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ATxWOmBMQ2la9HcxSqzEm9FcMBnUx4hEqVibTGkfGPTfiajaqAibF57xRD6cHDDA8FSfpVIZzdlPzibXTSxnwcF6xg/640?wx_fmt=jpeg&from=appmsg)

#

# **O****sint开源情报练习****#002**

欢迎参加OSINT开源情报练习#002!

## **一、****任务简报**

这是一张海岛上度假村的照片。请依据你在途中找到的信息来判断：

a) 度假村的名字是什么？

b) 这个岛的坐标是多少？

c) 拍摄照片时相机朝向哪个方向？

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ATxWOmBMQ2m5a9A4nrH5LWIiawibJIiaCbFZ7oWcLtiaaibMfAxAX9ZGTFIueUUrx1Uaiaqns05nlf0iaiaV7T2aHp4IJA/640?wx_fmt=png&from=appmsg)

练习级别：

对于初学者：中等

对于专家：简单

## 二、**步骤分析**

### **1.图片反查**

在处理这种图片中信息含量极少的类型时，我们最常采用的第一步措施便是在尽可能多的图像搜索引擎中进行图片反查，最常用的有Yandex、Bing（必应）以及Google（谷歌）。此处笔者已在Google游览器安装Reverse Image Search插件，该插件可以直接选择在不同的引擎中进行反查，此处便以此插件作为演示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ATxWOmBMQ2m5a9A4nrH5LWIiawibJIiaCbFqAR5E5PZomzE3BIBz2LL0z4RWCwZz7cgiabN0EVdlthEVJmwsz8AUyA/640?wx_fmt=png&from=appmsg)

如图，目前笔者的插件提供四个不同的搜索引擎反查，我们依次打开四个链接。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ATxWOmBMQ2m5a9A4nrH5LWIiawibJIiaCbFCwUp76qGjZnA6EW5qKWyMgJicK4ib82jdDvtungcFr50K1nyZZZSQdGQ/640?wx_fmt=png&from=appmsg)

最后我们在谷歌的反查中发现，反查提供的结果中，欧安度假村（Oan Resort）的图片与我们的目标图片高度吻合，我们点进该链接中进行查看。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ATxWOmBMQ2m5a9A4nrH5LWIiawibJIiaCbF588J7ONQj2ll7KYmyt7z7XXM1g0DdT4nBy6GvF1515SQLDmGhDzswQ/640?wx_fmt=png&from=appmsg)

可以发现，该度假村官网使用的照片，就是我们的目标图片，所以可以确定，图片所拍摄的就是欧安度假村。

此时，我们已经解决了第一个问题——度假村的名字是什么？

### 2. **位置确定**

此时我们继续游览刚才打开的度假村官网，查找是否有有用信息。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ATxWOmBMQ2m5a9A4nrH5LWIiawibJIiaCbF5R0M7yYIicQxeAGz7ibpBgIPNEb1QKflr09sIxQYLycypW5lficx0hMbg/640?wx_fmt=png&from=appmsg)

在官网的About（关于）项下方，我们可以看到官网提供了欧安度假村的Google地球定位视频，但是并没有提供具体的坐标信息，但是没关系，我们可以自己去查找。我们到Google Map中查询度假村的名字。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ATxWOmBMQ2m5a9A4nrH5LWIiawibJIiaCbF1jCSDVYakxX86lGXoMMtj2qoHoU77jdiaCChicKTUhpu0pMjKkx6e8bQ/640?wx_fmt=png&from=appmsg)

查询出来后，直接点击右键，就可以看到该度假村的坐标位置：7.362979448751061, 151.75640722585283。此时，我们完成了第二个问题——这个岛的坐标是多少？

### **3.相机朝向确定**

为方便观察，我们复制该坐标到谷歌地球中进行查看。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ATxWOmBMQ2m5a9A4nrH5LWIiawibJIiaCbF2xUiaN3Zj4XGnsC5rdgOHVVMgWa6ngtAL9dHo5icuycpIOVRQ3k90GbA/640?wx_fmt=png&from=appmsg)

然后我们再拉近距离，利用鼠标右键调整角度，根据参照物找到与目标图片相同的视角。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ATxWOmBMQ2m5a9A4nrH5LWIiawibJIiaCbFCNTcs0h98VzlNvOZKVVqibhYr7EekAribicIS5FibrKRIgvBHWEoiboozdw/640?wx_fmt=png&from=appmsg)

然后根据此时谷歌地球右上角的指南针可以看出，我们现在是面向西北。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ATxWOmBMQ2m5a9A4nrH5LWIiawibJIiaCbFjCqujgZcticavL09K3iaib1UtEgNhUyBEZ8TkYNppPCPTkHPK0Ep8zarg/640?wx_fmt=png&from=appmsg)

到此，我们就完成了第三个问题——拍摄照片时相机朝向哪个方向？

如若想了解更多信息，请后台私信！

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ATxWOmBMQ2lk4uX1sbrjO14weuRNoNKgwiafo3Ak1jCRRU87yEPibHfEoicORW7EkxiaOwjrtCicialoMytL7HrErl8Q/640?wx_fmt=jpeg&from=appmsg)

长按识别下面的二维码可加入星球

里面已有万余篇资料供给下载

越早加入越便宜

繼費五折優惠

![](https://mmbiz.qpic.cn/mmbiz_jpg/B0AKMb5va5zKJ6IvDm7zH8uGKMLmpkqKYLbkAVHcDIy1pTdjbsOlqh0GOYj7RhhMsfCLtUtWfwEicsFibUicCMwnw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

![](https://mmbiz.qpic.cn/mmbiz_jpg/B0AKMb5va5weznr59sOFnfjlug4lPdXGst2Ppk4z9iaENOniczwktxLNyvXJU4y0ibGic51MrKtiaicscLW3JbrYhauA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/B0AKMb5va5w5ib3A8u3qXrGBlL51p19Mq3tzhYE148ajGRI4EDI1dmreicLUw8y7p3Qo1wiagVOS7A9smNVr6LyicA/0?wx_fmt=png)

丁爸 情报分析师的工具箱

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/B0AKMb5va5w5ib3A8u3qXrGBlL51p19Mq3tzhYE148ajGRI4EDI1dmreicLUw8y7p3Qo1wiagVOS7A9smNVr6LyicA/0?wx_fmt=png)

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
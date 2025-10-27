---
title: 【安全圈】超 2000 万的安装量，Google Play 已成恶意广告程序温床
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652022133&idx=2&sn=9d77f787022af7f333e74bc4a8ced1ec&chksm=f36f8935c4180023758717d381dd9ea8e44b5bcc3c563fb5d6d5a062cf7981275559dd63f955&scene=58&subscene=0#rd
source: 安全圈
date: 2022-10-27
fetch_date: 2025-10-03T21:01:40.643818
---

# 【安全圈】超 2000 万的安装量，Google Play 已成恶意广告程序温床

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGylhChmtOQr2zsYya7AXiav1ADWBfEtPZMBGHAdmTvLnow2uHBw6WswSciafs5nJCGhMCkOb03xMbqjVQ/0?wx_fmt=jpeg)

# 【安全圈】超 2000 万的安装量，Google Play 已成恶意广告程序温床

安全圈

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGylhChmtOQr2zsYya7AXiav1AD4avQXDETguH2lI9qM5otIpcesLdUtNvkQ4YngwBurQkpiaticMajRQfw/640?wx_fmt=jpeg)

**关键词**

Googelplay

McAfee的安全研究人员发现，GooglePlay官方商店里有16个恶意点击的应用程序，安装次数超过2000万次。其中一个名为DxClean的应用程序的安装次数更是超过500万次，搞笑的是，其用户评级竟然还有4.1分(满分5分)。

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhChmtOQr2zsYya7AXiav1ADfpZHWT1SBsUdDBtp47dwtGTyBDKIgGnhjetuDe70aYmtUYUhxhMstQ/640?wx_fmt=png)

这类伪装成应用程序的广告软件，常常表现为在不可见的框架中或在后台加载广告并点击它们，为背后的攻击者创造收入。

最近，McAfee移动研究小组发现了潜入GooglePlay的新Clicker恶意软件。McAfee发表的报告中说:"总共有16个以前在GooglePlay上的应用程序被证实有恶意的有效载荷，大约有2000万次安装。"

攻击者将恶意点击代码隐藏在较为实用的应用软件中，如手电筒(Torch)、QR阅读器、 Camara、单位转换器和任务管理器。

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGylhChmtOQr2zsYya7AXiav1AD7caX0u9JH6fZWQNACuSOPzTq8hk2zU3icVy7UmJho7xSxHmK8XdwLOg/640?wx_fmt=jpeg)

恶意点击程序通过FCM消息（Firebase Cloud Messaging）传播，当应用程序收到符合某些条件的FCM消息时，相关功能就会在后台启动。FCM消息包括多种信息，比如要调用的函数和要传递的参数。"

通常情况下，这些功能会指示设备在后台访问网站，同时模仿用户的行为。这可能会消耗大量的网络流量和电力，同时通过在用户不知情的情况下点击广告为攻击者创造利润。

专家们在这些点击器应用程序中发现了两段代码，一个是"comclickcas"库，用于实现自动点击功能，第二个是"com.liveposting"库，作为一个代理，运行隐藏的广告软件服务。

目前安全公司分享了McAfee专家报告的所有16个Clicker应用程序，并且已从GooglePlay中删除。“Clicker恶意软件以非法广告收入为目标，可以破坏移动广告生态系统。恶意行为被巧妙地隐藏起来，难以被用户发现。”

最后，安全专家建议安装并激活一个安全软件，这样用户可及时了解设备上存在的任何移动安全威肋的通知。及时删除这些恶意应用程序，不仅可以延长电池使用时间，也可以大大减少流量的消耗，保护用户个人信息和数据安全。

来源：FreeBuf

***END***

阅读推荐

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGylhChmtOQr2zsYya7AXiav1ADtWlLibhEsBTvSDEML0FmjGS7ljfkkkcUkKL1Hc27lKicyibc3KibX27iaLg/640?wx_fmt=jpeg)

# [【安全圈】墨西哥拒绝美国,购买中企设备后遭黑客袭击](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652021962&idx=1&sn=9ccb1031c073d49809c21ca5abb775ed&chksm=f36f888ac418019c5c475ebd519338b87199fe16dc46a8352b703cff4a76f815dd8def5d6885&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGylhChmtOQr2zsYya7AXiav1ADhEJUSybGgJX75iaFQIvBMmkOh8Y3fXDaQdEmEZyZHfFqHzlugoICKxg/640?wx_fmt=jpeg)

# [【安全圈】超市巨头遭网络攻击，支付系统一度中断！](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652021962&idx=2&sn=288731eff0da8846abeef323aa092583&chksm=f36f888ac418019c1a5c3befe8f81f22e8475503776a7420481ed83d18156a18604e111eaf1b&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGylhChmtOQr2zsYya7AXiav1ADwIZzu4xq0JPZR4oCBcUBaxc37fsB55gtu8IqX7U7Ka1UsqmUwicNztg/640?wx_fmt=jpeg)

# [【安全圈】涉195万用户信息!新加坡一电商平台数据遭泄露！](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652021962&idx=3&sn=e0fb1f9c53451e2776aa528b4f1a67f7&chksm=f36f888ac418019c5eec53c9d90c7eddf15f60f7e479aa3a4dad5882b7e46c4bef084f156538&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGylhChmtOQr2zsYya7AXiav1ADib8wZlL7jSJYVJMYjBF2plEbYOibSdvqibkQwK9E8ILULpiciagNuzFY1tA/640?wx_fmt=jpeg)

# [【安全圈】拥有两个名称的新勒索组织正针对全球多家公司](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652021962&idx=4&sn=d76bf864a4340dfeeb443b290afc2c07&chksm=f36f888ac418019ca56e5d6df0f86e3be935f4bc9da43147334b5e1026b1d2af27038263c802&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

安全圈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

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
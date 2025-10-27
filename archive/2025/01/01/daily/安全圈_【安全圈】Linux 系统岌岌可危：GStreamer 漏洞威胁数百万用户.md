---
title: 【安全圈】Linux 系统岌岌可危：GStreamer 漏洞威胁数百万用户
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067033&idx=2&sn=6bf70d067d0bebdf78e4045b13df4439&chksm=f36e7899c419f18fa333cb25b0da58cc1c4c85067efbaaa4f07d75759489fcedb137e123cdf0&scene=58&subscene=0#rd
source: 安全圈
date: 2025-01-01
fetch_date: 2025-10-06T20:08:02.385306
---

# 【安全圈】Linux 系统岌岌可危：GStreamer 漏洞威胁数百万用户

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliaibIy800sLiaj9ibq6rYbMktRFTDibfrqtWX7k1wibOFNBiaCdKC0Bnfdicdc9s8Qae5ZBrsicO6c3K5Jiatg/0?wx_fmt=jpeg)

# 【安全圈】Linux 系统岌岌可危：GStreamer 漏洞威胁数百万用户

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

安全漏洞

GitHub 安全实验室的安东尼奥-莫拉莱斯（Antonio Morales）最近发布了一份报告，公布了 GStreamer 中的 29 个漏洞，GStreamer 是一个开源多媒体框架，广泛应用于 Ubuntu、Fedora 和 openSUSE 等 Linux 发行版。GStreamer 支持广泛的多媒体功能，包括音频和视频解码、字幕解析和媒体流。它与 Nautilus、GNOME Videos 和 Rhythmbox 等关键应用程序的集成使其成为许多系统的重要组件，也成为网络攻击者的诱人目标。

莫拉莱斯在报告中解释说：“GStreamer 是一个大型库，包括 300 多个不同的子模块。在这项研究中，我决定只关注 Ubuntu 发行版默认包含的’Base’和’Good’插件。”这些插件支持 MP4、MKV、OGG 和 AVI 等流行编解码器，因此特别容易被利用。

在已发现的 29 个漏洞中，大多数是在 MP4 和 MKV 格式中发现的。以下是一些最值得注意的漏洞：

* CVE-2024-47537：isomp4/qtdemux.c.中的越界（OOB）写入。
* CVE-2024-47538: vorbis\_handle\_identification\_packet 中的堆栈缓冲区溢出。
* CVE-2024-47607：gst\_opus\_dec\_parse\_header 中的堆栈缓冲区溢出。
* CVE-2024-47615: gst\_parse\_vorbis\_setup\_packet 中的 OOB 写入。
* CVE-2024-47539：convert\_to\_s334\_1a 中的 OOB 写入。

这些漏洞包括 OOB 写入、堆栈缓冲区溢出和空指针取消引用，所有这些漏洞都可能允许攻击者执行任意代码、导致系统崩溃或外泄敏感信息。

GStreamer 在桌面环境和多媒体应用程序中的广泛使用凸显了这些漏洞的严重性。莫拉莱斯称：“该库中的关键漏洞可以打开许多攻击载体。例如，恶意制作的媒体文件可以利用这些漏洞入侵用户系统。”

为了发现这些漏洞，莫拉莱斯采用了一种新颖的模糊方法。由于大型媒体文件的大小和复杂性，传统的覆盖引导模糊器在处理大型媒体文件时往往会遇到困难。莫拉莱斯选择了一种定制方法：他说：“我从头开始创建了一个输入语料生成器，”他介绍说，该技术生成了 400 多万个测试文件，专门用于发现 MP4 和 MKV 解析器中的罕见执行路径。

我们敦促开发人员和用户尽快更新到最新的 GStreamer 补丁版本。

***END***

阅读推荐

[【安全圈】大众集团80万电动汽车车主个人数据被泄露](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067016&idx=1&sn=6603384db2288a2926a144a8eac4bf06&scene=21#wechat_redirect)

[【安全圈】大量Chrome扩展程序遭黑客攻击，60万用户数据危险](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067016&idx=2&sn=c6d0c4c40675a96032fc8819d5d12bc5&scene=21#wechat_redirect)

[【安全圈】WPA3协议存在安全漏洞，黑客可获取WiFi密码](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067016&idx=3&sn=8a2de7555b1f2f62a08ba91e461c72ba&scene=21#wechat_redirect)

[【安全圈】亚太地区恐在2025年面临更多深度伪造、量子攻击威胁](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067016&idx=4&sn=166b595d367a5786467ef6200b20dc4c&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

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
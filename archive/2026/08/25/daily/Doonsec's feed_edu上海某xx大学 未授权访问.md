---
title: edu上海某xx大学 未授权访问
url: https://mp.weixin.qq.com/s/cwBevFfFrgMLnhf6L9Ywmw
source: Doonsec's feed
date: 2026-08-25
fetch_date: 2026-08-26T03:03:22.721328
---

# edu上海某xx大学 未授权访问

# edu上海某xx大学 未授权访问

zkaq- zbs
zkaq- zbs

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

# 本文由掌控安全学院 - zbs  投稿

**来****Track安全社区投稿~**

**千元稿费！还有保底奖励~（https://bbs.zkaq.cn）**

## 先利用在社区学习到的知识：

我在信息搜集时使用的hunter语法：domain=”edu.cn”&&web.body=”注册”

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoLjtgRaJiasibNPzy325BFyakUiaicXSnMKSCa2CibBPFIS7LOgK390XYPrgOgo9U7TMvWWxfialYubdubezXNCB5Ym2cBGfNjWaYtOk/640?wx_fmt=png&from=appmsg)
为什么要这样搜？ 因为往往有注册功能的网站登录后可以有更多的功能点接口，权限也会上升为用户

比如这里登录后，才能访问网站：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoISIOicQMAFic9kOicRpz2rkWohH9T28tCSibKJuD6zeV6uQibibYOTt0DdOiaibEYqMkCho6OrZLxlusLiatfHvIk1nFOk7M92TtdOW04c/640?wx_fmt=png&from=appmsg)
思路：传参点测sql注入、有回显内容可以测xss、文件上传点测测、框架看一下有无通用、逻辑漏洞想到的都试试
我比较菜鸡，没在这里找到什么漏洞，但是不要放弃，可以试试目录扫描：
这里用到老师推荐的findsomething插件：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoJgicIjZkUDe4Picvoo6k48xcvG6pRArLGEyl7BjRo3TzkYphOj28XqaMTJ1ZZTaoHGP9qZsTF5KsCfAVqMzuBz90BG5Shvq0Er4/640?wx_fmt=png&from=appmsg)
这些都是新的资产-接口，可以一个个访问看看
这里找到一处/advixxx，是班主任的管理后台，但是对用户没有鉴权，可以未授权访问：

![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoKgANEib3XKKia7R6WG0nxLq0NrqQTJUZHuMcGnJNnYhEIZA5iaW5kQLAIzatiaw6Vuic5cQP6R64J49YL7bGFznvAl6ibmNuBONZEOw/640?wx_fmt=png&from=appmsg)
里面可以看到资金流水等敏感信息：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoKwftuonReO4BTnuZkfYP6NPCR2hKSIM0FzYMVxARwUU8snWiaSQuf4NjLKw7AptBlwFy34RVUspvgr4QvuACpQOfpgFkhb32iaw/640?wx_fmt=png&from=appmsg)
对于这种信息泄露，利用bp抓包看看请求包和相应包，往往会有更多的数据、收获：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoJOHwcZfITebLZ0AeibYwDRoqhh9D9a42m9TZ9WXFGI2MGocjiaU0Vb5ccpicppibygC6yfzygCNZzKVetrH0gjDeNQkApiaOj7VdkE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoJWzW2NviaqrBwPrMA1fficiaMQicWrFDo8SC2IibMTEqGH4ibmyyFwP4OGR2mvicic39OEG4b93Bb3XTaFGHCy2MqNYVgfJXZkuRZ6edE/640?wx_fmt=png&from=appmsg)
而且未授权访问还会暴露更多的接口，比如这里：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoI8IcK9q3IVJDW29rOiaKb8xI5fq783x4Rn5XYuEfcVuniaZibaPp0VaJ2tmfCrGWmspNCcNJpIZthLmnsDWBnnNAY6thEiaXwfOGo/640?wx_fmt=png&from=appmsg)
找到一处网站管理员的后台接口，并且用的是wordpress框架，这里可以用用kali的wpscan工具扫一下，说不定会有惊喜：

![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoJWtt1UpxJXtiaBwquTSibXN1r5cic1Z9yliaaZlPicHRX6PJsRibibStm7tB4AAcpyUUb3V9J6wkDWC2ibeyF572v4DibtO3iat6oI8IcC4/640?wx_fmt=png&from=appmsg)

申明：本公众号所分享内容仅用于网络安全技术讨论，切勿用于违法途径，

所有渗透都需获取授权，违者后果自行承担，与本号及作者无关，请谨记守法.

![图片](https://mmbiz.qpic.cn/mmbiz_gif/BwqHlJ29vcqJvF3Qicdr3GR5xnNYic4wHWaCD3pqD9SSJ3YMhuahjm3anU6mlEJaepA8qOwm3C4GVIETQZT6uHGQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=10)

**没看够~？欢迎关注！**

**分享本文到朋友圈，可以凭截图找老师领取**

上千**教程+工具+交流群+靶场账号**哦

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcrpvQG1VKMy1AQ1oVvUSeZYhLRYCeiaa3KSFkibg5xRjLlkwfIe7loMVfGuINInDQTVa4BibicW0iaTsKw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=11)

**分享后扫码加我！**

**回顾往期内容**

[零基础学黑客，该怎么学？](http://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247487576&idx=1&sn=3852f2221f6d1a492b94939f5f398034&chksm=fa686929cd1fe03fcb6d14a5a9d86c2ed750b3617bd55ad73134bd6d1397cc3ccf4a1b822bd4&scene=21#wechat_redirect)

[网络安全人员必考的几本证书！](http://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247520349&idx=1&sn=41b1bcd357e4178ba478e164ae531626&chksm=fa6be92ccd1c603af2d9100348600db5ed5a2284e82fd2b370e00b1138731b3cac5f83a3a542&scene=21#wechat_redirect)

[文库｜内网神器cs4.0使用说明书](http://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247519540&idx=1&sn=e8246a12895a32b4fc2909a0874faac2&chksm=fa6bf445cd1c7d53a207200289fe15a8518cd1eb0cc18535222ea01ac51c3e22706f63f20251&scene=21#wechat_redirect)

[记某地级市护网的攻防演练行动](https://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247543747&idx=1&sn=c7745ecb8b33401ae317c295bed41cc8&token=74838194&lang=zh_CN&scene=21#wechat_redirect)

[手把手教你CNVD漏洞挖掘 + 资产收集](https://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247542576&idx=1&sn=d9f419d7a632390d52591ec0a5f4ba01&token=74838194&lang=zh_CN&scene=21#wechat_redirect)

[【精选】SRC快速入门+上分小秘籍+实战指南](http://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247512593&idx=1&sn=24c8e51745added4f81aa1e337fc8a1a&chksm=fa6bcb60cd1c4276d9d21ebaa7cb4c0c8c562e54fe8742c87e62343c00a1283c9eb3ea1c67dc&scene=21#wechat_redirect)

## [代理池工具撰写 | 只有无尽的跳转，没有封禁的IP！](http://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247503462&idx=1&sn=0b696f0cabab0a046385599a1683dfb2&chksm=fa6bb717cd1c3e01afc0d6126ea141bb9a39bf3b4123462528d37fb00f74ea525b83e948bc80&scene=21#wechat_redirect)

![图片](https://mmbiz.qpic.cn/mmbiz_gif/BwqHlJ29vcqJvF3Qicdr3GR5xnNYic4wHWaCD3pqD9SSJ3YMhuahjm3anU6mlEJaepA8qOwm3C4GVIETQZT6uHGQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=12)

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
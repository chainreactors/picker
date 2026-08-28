---
title: 某公司某系统超级管理员密码重置通杀
url: https://mp.weixin.qq.com/s/hgiBKiUIvM4mfsI_hn7vLw
source: Doonsec's feed
date: 2026-08-27
fetch_date: 2026-08-28T13:34:47.221959
---

# 某公司某系统超级管理员密码重置通杀

# 某公司某系统超级管理员密码重置通杀

zkaq- 腾风起
zkaq- 腾风起

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

# 本文由掌控安全学院 - 腾风起  投稿

**来****Track安全社区投稿~**

**千元稿费！还有保底奖励~（https://bbs.zkaq.cn）**

故事的起因是在挖edu的时候，意外发现某站点系统存在接口泄露，并且此接口可直接实现超级管理员密码重置，查ico找到用这个系统的站点，发现均存在此漏洞。

### 如何查ico找到相同系统站点

跟江月老师学的，首先打开系统站点，F12或者鼠标右键检查，然后刷新页面，在网络这里找到\*.ico文件，把这个图片存到某个地方
![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoJTZCFtOtaBqQ29Glc0wQPykXMXDjC1wIHo7wpubJBcJqVGu4SuGAA19KKe59a74sX7Av8hoArOaZ9bPadG64RicAeVqLJMMqSg/640?wx_fmt=png&from=appmsg)
然后打开hunter等测绘平台，图标查询查ico，也可以直接粘贴地址
![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoILFrZoNrNFmjntSgK1w9myccM9ItsaCicNswYD0F9p4Vt9o40UawYshhibKicia3rOncGibicqRXX9ic4mst2E8NiaEC6tNnufPCvia6Z0/640?wx_fmt=png&from=appmsg)
还有一种查的更全的方法，就是找某系统独一无二的静态资源，因为icon可能会被换掉，多看看hunter等查询语法
这套系统查icon查到六百多
![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoIyOkSkwUHPicQDauC3HWg3sMLXwAeiacuVhOdrhDYqwdHHSoHmI5Y3ecw2LrS00z5AoJNHUqrRIQic745sKpDERUxUMSjGORfQicc/640?wx_fmt=png&from=appmsg)

### 漏洞挖掘

我们打开此站，对于一些功能点正常测试，听江月老师讲的，会经常翻js，在这个站点的js中，jsrouterscan等插件发现的接口没有跑出什么东西，我比较笨，一点点翻一点点看的，在这里发现了三个接口，都危害极大，可以重置域名，重置配置，这里只演示重置管理员密码这个接口，因为这个还没修可能，所以打码打的厉害一点哈
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoJIl9X0VendUR8Lia7V9nWIjU7oL9Iibz3ptNdmEk6XrnPqQwQuuswOrTL8wMH2qwKVb4nAYAHibM9NmBNMgzBaLSptiaQeeIpLlSc/640?wx_fmt=png&from=appmsg)
拼接这个path地址访问，把/login换成这个地址

![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoJKlxzpl8PGgEcxj334zJcZVbBZ6FUP9CdaicookiaNNAY0sWEqaiajzMpQEh0hibaT5mIZAB3Hgd4uOaz1SIBGmHVl3g7CNq0l3M0/640?wx_fmt=png&from=appmsg)
登录成功
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoI11jom6MN7ZHLicfCQYPV2I8a4GpRhwicq67Uk63SOrxBTYrY9VWoKTZAib50rWEMxuj8SGhSmk198OeKuAUubukdHZQE9uodwJI/640?wx_fmt=png&from=appmsg)
数据极大，我们安分守己，超级管理员权限肯定是最大了，我个人觉得 还是不要再做别的操作为好，希望大家都耐心一点，用江月老师的话说，不要放过任何一个细节，每一个报文也都要仔细看。感谢大家的观看。

此漏洞评定为高危，同时已经提交cnvd

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ianpxKPnLHoKZEwIOTK02RnIbicPtcyicuwtJbFrb1j8dicHr8mFDicUZLSKSg4xBVswFPB6rpUicuFlyjIlicUhO6pD2pRLTrdj1qII94MGga2krQ/640?wx_fmt=jpeg&from=appmsg)

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
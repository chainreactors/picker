---
title: 总是被忽略的目录遍历到shell以及云权限
url: https://mp.weixin.qq.com/s/mrg9Jj65qVGf3EhgpF7URw
source: Doonsec's feed
date: 2026-04-25
fetch_date: 2026-04-26T04:58:40.289625
---

# 总是被忽略的目录遍历到shell以及云权限

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ianpxKPnLHoI0jKgRovSiaJ8ic2tnwjJN1GYdh871Cj3Gla8tYkibQZXzWicfMVibRyA3NJVicMafQzqPuxljBSR0XEPknZhryADPvgo0V9qdMebhQ/0?wx_fmt=jpeg)

# 总是被忽略的目录遍历到shell以及云权限

原创

zkaq - jingyii
zkaq - jingyii

掌控安全EDU

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

码领资料

获网安教程

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcrpvQG1VKMy1AQ1oVvUSeZYhLRYCeiaa3KSFkibg5xRjLlkwfIe7loMVfGuINInDQTVa4BibicW0iaTsKw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=0)

![图片](https://mmbiz.qpic.cn/mmbiz_png/b96CibCt70iaaJcib7FH02wTKvoHALAMw4fchVnBLMw4kTQ7B9oUy0RGfiacu34QEZgDpfia0sVmWrHcDZCV1Na5wDQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=1)

# 本文由掌控安全学院 - **jingyii 投稿**

**来****Track安全社区投稿~**

**千元稿费！还有保底奖励~（  https://bbs.zkaq.cn   **）****

# 一、前言

 某证书站严重案例

# 二、正文

    问大师傅借了个门户账密，想着对于我这种初探门径的多一本证书总是好的

从下向上寻，第二个系统便看到了一个 IOC 师生服务热线，当然里面已经没什么功能点了，很多服务早就关闭了，可能有师傅已经打过这个系统吧

![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoJRDr2dx5qhMibkVDvYbFL3VtDUwmibRs250FT3KkTRLRTeeJ3Bqe0mW3ZkEWY4h15UZEMMNsKWxZNuG1ws0nL9HSW658zTq6wsE/640?wx_fmt=png&from=appmsg)

随手点开了雪瞳给了一点惊喜，尤为是 download?id= 的出现，看到了一丝可能

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoIB49AwO9vPcXozvh5KpSSSGNggj7V4fHktJRkXKsNvU9xTKOwJraHawLmS5fqfMBFo8Tygl6RQvbuWsBFQHjFn8SkA3d0icFVA/640?wx_fmt=png&from=appmsg)

    对 78 个路径爆破后，转而还是看向了

/server/voicemailRecord/download?id=

    从 1-10000 进行尝试

![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoILFVYvibnqrFhy34KliaoNQfpUxibQzqCqUN11gw2icRnwJfgdhGic2sofHeFxJC3O3oUnFjDT7J5te6t7uK52UHc728fMjeLofMD4/640?wx_fmt=png&from=appmsg)

有了路径，访问了好几个文件，都是学工与学生的通话记录，当前算不上什么危害了也就，一筹莫展

把路径删一删试试呢？惊喜

这里已经修复，用别的图代替一下，出现了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoLqN1t9jMJUdAGERThNoRjt92UCTtlCQicVtHgdicY1PTKFQIrT6ics6jbNlRd6DRYYIHVk5Pw2PyHgdYib3g60m9LWEXgsyTjWa0c/640?wx_fmt=png&from=appmsg)

在里面找到了多份敏感信息，包括身份证，发票之类的，也就打包交了，证书是有了

# 三、意外之喜

翻了翻去，正欲撤退，偶然翻到一个文件 后缀为 .账号，过于敏感，厚码展示

服务器账密 数据中台账密等信息，瞠目结舌

![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoJia1JjlfAmwBIa8ibFODE4GmeCWeibozcdbDqAKwUIUr9xqerpaCtceAOackRjZcEa92nJnGeSvLI9uNS3Md5icGlbPYwuNVJzSU4/640?wx_fmt=png&from=appmsg)

毕竟这个系统还有工单二字，猜测是在交付时误留的文件

登录仍然可以登录的某几个系统，系统中多处 order by 注入不提，sfz 已有几十万余

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoKYsHMgyN8ibx8ZPHkMaorcLibfUZv0WtygY6ZSWDLaaznbmvqicOFe1f3FMCEfvac0gIYnSrcQF1ZnicCe7FDHUJab82tvQb0YdBo/640?wx_fmt=png&from=appmsg)

下面的这个系统用的jeecg-boot，也是存在历史 nday 路径遍历和任意 sql 语句的执行

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoIqdg7Q3ibc2T2ibibfY3JMSGwL6nLycKZkHJ4TFUqLWUYwFrH3QYb1IB7iba63RtzZ4r8mVwcx2LTkibIVk1BqsJW7icQoSw2DwlP3w/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoLzm52AI5umq7X64l63zlPMd7zuJkEFWusOfxa9HWJibf3KusvmMOZjuicLf3piboQcZwTwX49pvBxgzon4ia7tq2KXvLwdHRqysG4/640?wx_fmt=png&from=appmsg)

后 ssh 登录了主机

下载到了一份源码，若依框架，其他的部分都是小洞

但是拿到了 ak sk

![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoKBGBWfcN2gKDfqbuaX8MqR8nib99CwfSzKYqeybuAT3QJy6gHsJMqbNHNqe8SD2nBPc6kVCR8NEQZgCQLDZV1uqJJ9ydB2Sicos/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoJfyS75FbsKhYoUEvoS76PCVD5PaIaicLWdkxYM8gOEX4QA3PLfJt26le4YWOFASqVh08ItxnXX9QYMtvic1iaorJ1hIVkahXdDj8/640?wx_fmt=png&from=appmsg)

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

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/BwqHlJ29vcq98SadiaYm6GqwrAZjdeXAuLrl5ATlxIMCiabYgjLJ1M1gcLHicsRuISeqtAuLaSfRtBULuibjDBcLsg/0?wx_fmt=png)

掌控安全EDU

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
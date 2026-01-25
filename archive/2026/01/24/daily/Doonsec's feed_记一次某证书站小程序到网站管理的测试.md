---
title: 记一次某证书站小程序到网站管理的测试
url: https://mp.weixin.qq.com/s/ve0ByZIQKbbNiEBN7OEyzw
source: Doonsec's feed
date: 2026-01-24
fetch_date: 2026-01-25T03:54:59.883211
---

# 记一次某证书站小程序到网站管理的测试

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BwqHlJ29vcp9TJicGdcOYNcBf2FWuZMHsmxRlukLonTJccbxC6NWchKE7z0JouNF4bGev2H1RaOb9YvhNxguFGw/0?wx_fmt=jpeg)

# 记一次某证书站小程序到网站管理的测试

原创

zkaq-mike123
zkaq-mike123

掌控安全EDU

![]()

在小说阅读器中沉浸阅读

扫码领资料

获网安教程

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcrpvQG1VKMy1AQ1oVvUSeZYhLRYCeiaa3KSFkibg5xRjLlkwfIe7loMVfGuINInDQTVa4BibicW0iaTsKw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=0)

![图片](https://mmbiz.qpic.cn/mmbiz_png/b96CibCt70iaaJcib7FH02wTKvoHALAMw4fchVnBLMw4kTQ7B9oUy0RGfiacu34QEZgDpfia0sVmWrHcDZCV1Na5wDQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=1)

# 本文由掌控安全学院 - **mike123**投稿

**来****Track安全社区投稿~**

**千元稿费！还有保底奖励~（ https://bbs.zkaq.cn  **）****

# 一、前提提要

来到一个证书站的小程序

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcp9TJicGdcOYNcBf2FWuZMHsia9svUKE4qvsU6RyherwIPxzcb0JIrUk9sIvoEBibfibcnibUIhgnBXnbA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcp9TJicGdcOYNcBf2FWuZMHsCtM75xkP5UqK1yvw1vUQ9v3zy585PduYZYbbs53SYFCmTvh73yExow/640?wx_fmt=png&from=appmsg)

二、站点测试

登录框测试的话首选的一般都是弱口令 先登陆抓包怎么传密码

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcp9TJicGdcOYNcBf2FWuZMHsNpHhg2DdrMHwH5mRjzNNicQgEm4CpJDoNBecBhGGGIdN2EwIDE8Xa0Q/640?wx_fmt=png&from=appmsg)

这里看到是明文传输 那直接试试字典跑一下 最后也是跑出一组弱口令 账号密码都是一样的 进入后台

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcp9TJicGdcOYNcBf2FWuZMHsXYFL1BaF8tCkvtdZfokUWO0jibC2iaqEE1qt7hicILOic1DSibalJ7XARBg/640?wx_fmt=png&from=appmsg)

进入后台点几下然后观察一下数据包 这里我点击我的时候抓到一个这样的包

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcp9TJicGdcOYNcBf2FWuZMHs44Ajmib29SABUXYL5BV5s5S5p5Y0BO8jIf9dcOysDWMb3H4cRYuyibibQ/640?wx_fmt=png&from=appmsg)

看到id很多师傅都会很兴奋

这里我置空一下看看情况

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcp9TJicGdcOYNcBf2FWuZMHsGs9KmIVf6a8z4WhmtQgzCmcmWgI9COpbpj7EcYHA7D152icT5gB8G4w/640?wx_fmt=png&from=appmsg)

什么都没显示 那我添加个1呢 一般来说1有很大可能是管理的id

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcp9TJicGdcOYNcBf2FWuZMHsxG3NmwaFdgWGjcWPkpfBMVR8f90jTsFAGGtdv5RBLDcylTfXTzPkyg/640?wx_fmt=png&from=appmsg)

不出所料 1是管理的id

我这里直接替换数据包然后看看是什么个情况

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcp9TJicGdcOYNcBf2FWuZMHsJesic8YABuPsX0VvpvpPG5lUCx04UhWeApdtzYicsbxlof7vvYkzJ4QQ/640?wx_fmt=png&from=appmsg)

这是普通账户的

我更改1以后的

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcp9TJicGdcOYNcBf2FWuZMHsFWgQGRxXpJxpsedSicH3IfNU3KQb04yCdaU31OE1xSTXdWzJ80SlCbQ/640?wx_fmt=png&from=appmsg)

可以看到是多了很多功能 但是我点了几下都找不到危害点 这时候产生疑问 改成1后的数据包有很多菜单

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcp9TJicGdcOYNcBf2FWuZMHsJgkPEn48QsU8XjMLthcsUawMAfnpCLLPwNjqt0Pb6eMSXIG1kMaoWQ/640?wx_fmt=png&from=appmsg)

但是为啥我这个小程序点了半天都没找到呢 有可能是删除了 然后看了一下返回包 很像web端的管理菜单 这时候就在想是不是有web端呢 然后就去扫了下该站的目录

使用dirsearch成功扫到了web端的登录口

https://xxxedu.cn/xxx /#/login

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcp9TJicGdcOYNcBf2FWuZMHs8kicRUdicgFj0dJJJjJLic2OgseaZib4rIOxuJmbb2GrAZictWN8ndibZTTg/640?wx_fmt=png&from=appmsg)

奇怪的是我用小程序爆出来的弱口令一直显示密码错误 抓包发现不是同一个登录接口

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcp9TJicGdcOYNcBf2FWuZMHsE9DNNVGqboCibIIUuicAEsSL2lbyicpxFYU6VftPiafE7hTBRP1Hz2H9Ew/640?wx_fmt=png&from=appmsg)

这时候跑了弱口令也是没一个能进去 那我们如何测试web呢

这里我们来看两个数据包 分别是小程序登录返回的数据包和web登陆返回的数据包

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcp9TJicGdcOYNcBf2FWuZMHsBtqcflOahuEuibXaXasS4BSvQhNmowN7FqFjICtzv4LJOia2uLQh1GrA/640?wx_fmt=png&from=appmsg)

细心的师傅应该发现了 格式非常像 我们如果替换掉小程序登录的结果 是否能进去web端呢 这里我也是这样尝试的

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcp9TJicGdcOYNcBf2FWuZMHsGTEEYvY0WhymiaCtP5LRplnu1tsU2uXpibOewEkg0ciaJHL7bNQoVBHkA/640?wx_fmt=png&from=appmsg)

这里已经进去了 但是一直没有菜单

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcp9TJicGdcOYNcBf2FWuZMHsmkzpu8ycdvWtdeF27d1sQrPnyurmGLeHpmWnA793r65JcXibHpjLvpA/640?wx_fmt=png&from=appmsg)

可以看到路径有个#号 感觉像vue框架 这里使用VueCrack工具看看路由情况

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcp9TJicGdcOYNcBf2FWuZMHsG4B2cdegpyXa3JiaCFFhSsfze5DGjvNNiaEJ38fyI6J7auXBtNVYKibFg/640?wx_fmt=png&from=appmsg)

发现特别多路由 这里点了几下

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcp9TJicGdcOYNcBf2FWuZMHsibaza3icgrrYXjdianHXOL5r0MOEZQEaq7QQlLY6jiaIRl8Y5KSjd6tp9Q/640?wx_fmt=png&from=appmsg)

这种配置只要能创建 在edu中就已经可以中危了 达到了证书获取的条件 然后又点到一个路由

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcp9TJicGdcOYNcBf2FWuZMHsRoDC39hWCg21vT59gIlnuFUbCPfokxZknuxA3olXvibzvZDhNMZc1tg/640?wx_fmt=png&from=appmsg)

人员管理的界面都没鉴权 这里直接重置管理的密码然后重新登录

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcp9TJicGdcOYNcBf2FWuZMHsVxR9a8OvwadGcSiaJ0VNHibe2brj6NgNhlhsPmxn8q02icbomygFmx6tA/640?wx_fmt=png&from=appmsg)

直接进入管理帐号了

点击人员编辑会抓到这个包

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcp9TJicGdcOYNcBf2FWuZMHs7wDMIeUafBwF83amHJNRN8VQj7e7ibSa8icGU1KVuM3kfJkJEGfpTBfQ/640?wx_fmt=png&from=appmsg)

此时id我们都能知道了

由于返回包泄露了密文密码 edu是收的 理论上这21w用户的密码都能泄露 最后打包上去也是拿下一个10分漏洞

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcp9TJicGdcOYNcBf2FWuZMHsdSFWj8JUQVFvaKe3Pic0wnw5znXVhsib6gOBOwt1dxgXNM7urpnyhDPw/640?wx_fmt=png&from=appmsg)

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
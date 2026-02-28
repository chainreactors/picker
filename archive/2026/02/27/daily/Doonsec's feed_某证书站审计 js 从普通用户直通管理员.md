---
title: 某证书站审计 js 从普通用户直通管理员
url: https://mp.weixin.qq.com/s/jklgEOAIm45jh9H5hRRNwg
source: Doonsec's feed
date: 2026-02-27
fetch_date: 2026-02-28T03:58:00.856933
---

# 某证书站审计 js 从普通用户直通管理员

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BwqHlJ29vcqxLuDWVwYg2pa48TtJUCzVQeTQOmcLFCSmgwsMU8owzb8ibgkv6BYtpyaAMt4ZibK5hAlhdyVjYxfQ/0?wx_fmt=jpeg)

# 某证书站审计 js 从普通用户直通管理员

原创

zkaq - bielang
zkaq - bielang

掌控安全EDU

![]()

在小说阅读器中沉浸阅读

扫码领资料

获网安教程

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcrpvQG1VKMy1AQ1oVvUSeZYhLRYCeiaa3KSFkibg5xRjLlkwfIe7loMVfGuINInDQTVa4BibicW0iaTsKw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=0)

![图片](https://mmbiz.qpic.cn/mmbiz_png/b96CibCt70iaaJcib7FH02wTKvoHALAMw4fchVnBLMw4kTQ7B9oUy0RGfiacu34QEZgDpfia0sVmWrHcDZCV1Na5wDQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=1)

# 本文由掌控安全学院 - **bielang 投稿**

**来****Track安全社区投稿~**

**千元稿费！还有保底奖励~（ https://bbs.zkaq.cn **）****

# 一、前言

某日新上了一个证书站点，挖掘了一下午，交完报告觉得稳了，第二天传来噩耗，没人家 手速快，全部重复：

于是重新打点，有了下文

# 二、正文

某日新上了一个

开局的权限：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcqxLuDWVwYg2pa48TtJUCzVrln1shWP6gj31DGn3jAs0e0YdibSJxibZbfGypRNg5zGFK8oYybXjkKg/640?wx_fmt=png&from=appmsg)

里面的功能点都很少，查看数据包得知鉴权方式为：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcqxLuDWVwYg2pa48TtJUCzV1Ah4JJ2E62g4802EW9pOh5icxN6dqBGAqxeAN76ddMc305hbCPbNiaZA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcqxLuDWVwYg2pa48TtJUCzVjyamNiccke2eCFgmAt9Ljbl6IUzDgFASfia9sQMbnpdf4O7cLsBPprAg/640?wx_fmt=png&from=appmsg)

```
logintoken=xxxxxxx
```

每一个功能点都点开看看，然后看一下数据包：

发现并没有什么有价值的数据包，但是后台插件 xiayue（推荐，有权限时候这玩意就是好用）给我扫出来一个未授权:

重放：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcqxLuDWVwYg2pa48TtJUCzVEEPicYMIvZabnOPUntxaDO2DYOf4uFWIHYZRlVKSEIiaibzJf9SE210LA/640?wx_fmt=png&from=appmsg)

虽然回显了用户 id 和用户密码 123456 以及鉴权字段`logintoken`，但是事情真的这么简单吗？尝试登录发现并不行，替换`logintoken`也不行，因为`logintoken` 还做了一个时间戳的检验：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcqxLuDWVwYg2pa48TtJUCzV6pLvN9dBKQ6geGKM9cJiamxQdM6EVlbaEwsFic4l8a07ppUsc3iajkXJA/640?wx_fmt=png&from=appmsg)

可以看到最近的一个都是 11.12 日的，已过期很久了。

隔了一天，我提交的另外三个洞 都重复了，只能继续看这个，然后我开始手工看接口：

先看了当前这个接口能不能检索到：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcqxLuDWVwYg2pa48TtJUCzVm5Nt9vbyVOmdwyvbpknarDyFXYOI99fBxUicwJWd3S3upcqzh8XBMtA/640?wx_fmt=png&from=appmsg)

然后跟一下其他的接口，跟了好几个，都没用，全是垃圾接口。

发现这个 js 中中文注释是比较多的，所以直接检索“**管理**”：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcqxLuDWVwYg2pa48TtJUCzVEnt0yVkd0MXeFNqib0BgSLibdib0NOTbiar8L7ycGRXXyDLFOg17FNogeQ/640?wx_fmt=png&from=appmsg)

看见一个`加载管理员列表`**:**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcqxLuDWVwYg2pa48TtJUCzVmzLtaOr2s1ibSxkxZtl5xCym273TtibRBrGHydAUdpFbOAR89VnUyPYw/640?wx_fmt=png&from=appmsg)

非常的贴心，全都注释的明明白白的，构造表单查询：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcqxLuDWVwYg2pa48TtJUCzVFcbc05L2deC3peSwgtOEUJqnTIg9thNKpyI9PhUVhnz0ibPoib0DkV5A/640?wx_fmt=png&from=appmsg)

只要鉴权字段就行了，查询出全部的用户。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcqxLuDWVwYg2pa48TtJUCzVxLicficRhg3pibGHbWtuGHPvGRPc04xHlVFpG3WtuTc7DYPA4VODbsd1w/640?wx_fmt=png&from=appmsg)

密码为 123456 的全都登不上去。

解密 md5 加密的密码：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcqxLuDWVwYg2pa48TtJUCzVqRBAl7ZWiaFMlaSJgJaZjhZbVObsaT7EZ5yOrgF0LR62qibN6NiakCuzg/640?wx_fmt=png&from=appmsg)

能成功登录，但是呢，是一个测试账户，权限还是和开局一样，没有卵用。。。。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcqxLuDWVwYg2pa48TtJUCzVP9SK0v9N2SkfCWANsiaTB5r0ribZVsKTuYjhvQaqnHibIlxfFLNY2MKTQ/640?wx_fmt=png&from=appmsg)

继续看 js,添加管理员：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcqxLuDWVwYg2pa48TtJUCzVF83A4XKK1iaebzgaxONmpeTKmiaG0UiblmpQPrmnoVwDaibwS5j6HXoTUQ/640?wx_fmt=png&from=appmsg)

构造表单：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcqxLuDWVwYg2pa48TtJUCzVDy04M7ekIfvHtIFNOG4886cfbiav4yHcBiaibb3fLHl6A8jzpDq9wibAibw/640?wx_fmt=png&from=appmsg)

已经把上面的 字段都填好了后发现还是缺少字段，怎么办呢？我直接把 js 复制给 ai,一把梭哈：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcqxLuDWVwYg2pa48TtJUCzV3nb0kpIQArxfZmzw69CBfCDRQfib22puD7Ln85GUOaFIrA7RKAic7eFg/640?wx_fmt=png&from=appmsg)

给了我一个 job 字段：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcqxLuDWVwYg2pa48TtJUCzVsGz3447kgR9qZ8brebkW26JzPXgcImUmc5zD68kQpHPwjzCXXhJJcg/640?wx_fmt=png&from=appmsg)

信息完整，但是部门不对，回到之前哪个数据包中：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcqxLuDWVwYg2pa48TtJUCzVR2OBnb3HmXRJoKGibu7pTdZSZ7A3RhSbh9MiciaaOrrfp7sa2DaA6IEsw/640?wx_fmt=png&from=appmsg)

随便找一个，注册成功，以为结束了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcqxLuDWVwYg2pa48TtJUCzVIDiaxzNzBR1WpWWW7InfFlaToNibnN4tQDBemEugoKxMLiaMibAEhhavYA/640?wx_fmt=png&from=appmsg)

尝试登陆：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcqxLuDWVwYg2pa48TtJUCzV34guysQDWAMnonBq7TttQScXU7XQqGUlHkNzCJIgIoYC5iaCN7Cyl2g/640?wx_fmt=png&from=appmsg)

nmlgb，没法，再去看 js：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcqxLuDWVwYg2pa48TtJUCzVMvMH1QopKW2Gsn5uBPic9tRgKlEKO55QW5vb8qtcibEHRCoOOAj6OWEQ/640?wx_fmt=png&from=appmsg)

难道是没有启用吗？

在构造一个表单呢：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcqxLuDWVwYg2pa48TtJUCzVgwuguEWJ5sT3bAqnN4AicxUJ2jRqvTQy1ZWicIVY2mibbialf5wJZljgvQ/640?wx_fmt=png&from=appmsg)

lid 值 从哪里来呢，当然是之前的哪个获取所有用户的数据包中：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcqxLuDWVwYg2pa48TtJUCzVZnia6iah84RBX3XrB3B15I5lkmjuDJhYibP1Ttuy08ibUNEdlmxdmKic5pA/640?wx_fmt=png&from=appmsg)

启用成功，还是登录不了，难道是注册的用户权限的问题？

再审 js:

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcqxLuDWVwYg2pa48TtJUCzV9JrKxIDSfnuO50WTBSL6iaGfIRrZLLvhMakX9BZeymTfkuHZYBgicnbw/640?wx_fmt=png&from=appmsg)

再次构造表单：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcqxLuDWVwYg2pa48TtJUCzVibufdrv98gdJYp05jdVmyChow1eIPcUoIcUua4xh3hiagrGj4C1gp3Kw/640?wx_fmt=png&from=appmsg)

改成一个领导的权限，依旧登录失败。

不得不放弃该账号的操作了，开局有一个通过 cas 传递的账号，那我直接更改他的 roleid：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcqxLuDWVwYg2pa48TtJUCzVMBgC08scl4CibkTXfy6T6HrBKkZOO97YcqicUtTLia4Yg0lrkLE6tbAIQ/640?wx_fmt=png&from=appmsg)

改成了领导的，发现只多了一个功能点，没用。本来想找一个能够更改密码的接口，直接改别人的密码登录的，但是没有找到这个接口，且当前账户的密码我也未知。那只能改之前的那个测试账户的 roleid 了，但是有一个问题就是我不知道哪一个 id 值对应管理员的用户，尝试 fuzz:

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcqxLuDWVwYg2pa48TtJUCzVYeM9MJCGONWQ7ib4ZCWBe4znBDFdRTAE0awToPicY8gT8EEcfB6W8cfQ/640?wx_fmt=png&from=appmsg)

最后发现居然是 0：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcqxLuDWVwYg2pa48TtJUCzVIRID7sBmxOjBicM1HvUIiaF7ENib2BK1icl4tRvQjVgFqJNUE7uK5HeYtA/640?wx_fmt=png&from=appmsg)

登录：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcqxLuDWVwYg2pa48TtJUCzVpB4ibgvnonKwduT9hlPaBiciczflMKAmKpKjpHYdxXNjoqKrpsdPQjLxQ/640?wx_fmt=png&from=appmsg)

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

## [代理池工具撰写 | 只有无尽的跳转，没有封禁的IP！](http://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247503462...
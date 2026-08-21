---
title: 微信小程序存在任意用户登陆
url: https://mp.weixin.qq.com/s/c5MEegwI629ZJA0CCR3ZXA
source: Doonsec's feed
date: 2026-08-20
fetch_date: 2026-08-21T03:01:01.372969
---

# 微信小程序存在任意用户登陆

# 微信小程序存在任意用户登陆

zkaq- 郑居中
zkaq- 郑居中

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

# 本文由掌控安全学院 - 马小芳  投稿

**来****Track安全社区投稿~**

**千元稿费！还有保底奖励~（https://bbs.zkaq.cn）**

## 微信小程序存在任意用户登陆

```
在登录小程序时，都会遇到是否一键登录或或授权，方便用户的登录，但是在方便的同时也意味着存在一些可利用的漏洞
漏洞成因：泄露session_key的值
```

### 复现步骤

1. 在登陆时，弹出这个页面时

   ![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoIpD2R1p4UDAUOib9ton3nnfM0vdB4bwHzZnibn6VvX8QpoPBLmHnarmeQ2IiaSk5t8qwSEFWjQyNlxxEOvib9cYQJrRfmLW7jqeas/640?wx_fmt=png&from=appmsg)
2. 抓包，观察数据包的内容

   ![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoJWnkd3aNib65D357eeos34AKx5C0sDWqLKfw4JN9xJcibCZLwW8URhNmbUSzrbFOWnho3fFbgGsDcbzR9BxEHfep27ZDOzeDx5c/640?wx_fmt=png&from=appmsg)

   会发现有mobile值（密文）和iv值（随机数），拿到密文，肯定时想到解密，想要解密就必须知道密文，iv，session\_key，这三个缺一不可，得到两个了，想办法得到第三个session\_key
3. 仔细观察数据包的回显，在下一个数据包的回显中，拿到session\_key。

   ![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoIf4KNWlUbnlYGib5aetOHfE83pjvjJgC6JiaHKS1bp89FBVj2Fse0ugluVtGZBXMcsWiaeAgxtlacpYGwibOQeSFQBxnhWqTyzsuk/640?wx_fmt=png&from=appmsg)
4. 使用工具微信一键登录解密，即可得到明文信息

   ![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoJcskLV4yh3YhkRIZMGPEMKxuwdTY9YE6icyYg1I7CUYL4aRq3QB7AYibb2k8fOiaNGkVydk3K9W0ZF0sibVKt0Qo40ESIwmcNsZOU/640?wx_fmt=png&from=appmsg)
5. 将明文中的手机号修改为其他的手机号，再进行加密，替换以前的密文，即可实现任意用户登录

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoI8TH7pSgPw2f1NQCCRo6gCQ5DbqZ5LhdXxW7DqfibxS8SuBvvD8lVoJYjOBWfrj1M28oiamPp8FxkX0WbgAVue5tYPCicOibxgtcs/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoIttib3auAicZDLhibShvF6FmYqD3giaYoteZibbxiaUdQYgAQzd4WzSxHsZ1r5McCNgEXSX9oE6sWLCzx8TRQicgrfVibicrP7dPgXHicPk/640?wx_fmt=png&from=appmsg)

注意：iv值是随机的，每次必须重新抓包，工具我放在附件了

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
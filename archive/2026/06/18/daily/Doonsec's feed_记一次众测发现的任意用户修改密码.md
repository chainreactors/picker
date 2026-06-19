---
title: 记一次众测发现的任意用户修改密码
url: https://mp.weixin.qq.com/s/9lEqwsbZLD9KcqT3rgO2rw
source: Doonsec's feed
date: 2026-06-18
fetch_date: 2026-06-19T07:06:28.225837
---

# 记一次众测发现的任意用户修改密码

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ianpxKPnLHoIF2wbOswmoYujOzgRVEMAicEqHS0ricWbygTru8tHicj5NHgYAyxQfNKicm0tTcrvR3clC11zfWNE2gz7eVdltFK9icvGRM6tuQeEk/0?wx_fmt=jpeg)

# 记一次众测发现的任意用户修改密码

zkaq -郑居中
zkaq -郑居中

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

# 本文由掌控安全学院 - **zkaq -郑居中 投稿**

**来****Track安全社区投稿~**

**千元稿费！还有保底奖励~（https://bbs.zkaq.cn）**

# 0x1 前言

某次众测，在测试过程中，发现平台在用户身份验证机制上的关键缺陷，导致仅需获取目标用户的用户名和手机号，即可实现任意用户密码的修改。这一问题显然暴露了平台在身份认证设计中的重大安全隐患。

这一漏洞的利用门槛相对较低，攻击者可以通过社会工程学或公开信息获取目标用户的基本信息，然后直接发起攻击，劫持用户账户。漏洞的影响不仅局限于个人隐私和账户安全，还可能对整个平台的核心业务和用户信任造成严重威胁

# 0x2 漏洞案列

通过fofa找到资产中的一个采购平台。
![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoJLjHEziaoHrChu6s23cSEeXsOhpAs2GY9xdTqC2fu5KxaYAQJNpv2LLYhkw1C2oK9COJwc0YFh9JmvhzV2Xll0CYDdBtavPAf8/640?wx_fmt=png&from=appmsg)

在修改密码处，需要身份验证码。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoITsYB9Qh2iaXUjLzIBxUJUNWHGen23wbib7y3AIQv6JmDz6ZpTV9NF1YyhujHYCicMWgpHiaVNKRjqnMGFyn8bTYP7BG3xbAANdSE/640?wx_fmt=png&from=appmsg)

测试过后发现在身份验证中，要求手机号和用户账号要保持一直。但是我们现在没有账号，在主页中也没有发现注册的功能点，开始分析js文件，观察findsomething插件，看是否存在注册接口。

给大家推荐一个比较好用的插件，配合findsomething简直无敌了。

findsomething点击复制url

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoLqBQTabnJicUk9icTDTJ0iaLEhycgYXwPDo2Vflgyic9wtQp1uwxWWDP3KiahedhNOKJda4NMEO6bxvqFDvTJ3TbBdI3d4y9yGjk9w/640?wx_fmt=png&from=appmsg)

将复制的url粘贴到这个里面，点击openurls，该插件就会将所有的url在当前浏览器中，都跑一边。

下载地址： https://github.com/htrinter/Open-Multiple-URLs

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoL0LTxQsf6W9czbcrxIaDaxba1vIniccZKGlECnrAraaE5T1uZNQ5KcYQdm0a0AMvON3wibF0BthXH0IfaKhhwpwbHr5wHiaVawhA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoIB7mRHXCEmIcribPvTsZ8NW6Oh7Bd1iafmaoCbIFBXfXnaUgPIV13icmd1p3VY3VOn5SEveW0smBNNDhJOGHtIibEW8Yic645kDiaoc/640?wx_fmt=png&from=appmsg)

但是缺点也很明显，findsomething插件复制出来的的url，都是自动拼接到根路径。
如：https://baidu.com/aooucth
而网站真正的路径可能前面存在固定路径，如：https://baidu.com/固定路径/aooucth 这样的，遇到这种问题，还需要师傅们自己拼接，或者通过burp爆破。

再次这个网站就是这样的，在findsomething，发现/page/supplier/register/register.html,直接拼接会跳转到主页，在固定路径后拼接就可注册了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoKlLmv0LmRYQnQMXqAqCvYibxM08hkNcYibLic0rDMBialzDGkZicfhKAKiar3ibRI36L6ujQ3JxEZP4NgHesA9ib6wWsViagTHKMcWugnM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoI6a4QIDMXEGZkcTQH0UqqHnneXfjDibkNwYB4zqVqdj5PV4licKCSDTyW9rlPkXTdheAOibPb094AOIFnQyoB6BL8sKr90KUV6hg/640?wx_fmt=png&from=appmsg)
正常注册账号后，忘记密码处，输入正确的账号和手机号，获取数据包。

![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoLghPTksGibnFVOCaOibdQfjT5WNscFpxsBRpb4TS5BfFIgDfzu3tF9nicHg9z9exxYClauLEeDicBbESdtu8h167nqrXNNLibkrQKQ/640?wx_fmt=png&from=appmsg)
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoIlXfFR9qD6FWUficr6eNvjic8IW8lNvHibfcOcDbKa6OJbMToTfeT1usW41k74eOwaU4IvBa91asyac4LIjo4ScB3Zxa89pMFEmc/640?wx_fmt=png&from=appmsg)
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoJYrAMGo63h2e8fLbib77UkoOjCPmUvMB48oO9NcyvXYibU2f0BsuoIXTP8PiaYwibCSJheKPbia3sBFffpZ7SgD4yCx3Icbvom8J4Q/640?wx_fmt=png&from=appmsg)
发现在数据包中，并没有验证验证码的对错，输入正确的绑定关系的账号和手机号，直接返回一个result值。
只需要将账号和手机号比对正确，就会获取到一个 result，页面跳转到
https:/xxx/pass.html?id=xxxxx6xxxxxxxxxxxxxx

![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoL6Va2R5aYR8JE7Ro2icPR0wyBCCVyelKOCWZkCMUHbC8pUiasttejibbiaRB0bTc268SGIRNnO4Cjj2WGZgPGR7CtZj6gcDXhTx5w/640?wx_fmt=png&from=appmsg)

此时大家都能想到该id值，就是修改用户密码的关键，只要获取到用户名和手机号就可以无需验证码修改了。
在下面的链接替换其中的 id 值，即可无需验证码修改对应账号的密码。
而且我还发现，这个 result 值永久不会变化，只要获取到受害者的 result 值，，即使对方修改密码后，我们也可再次修改，无论何时都可修改受害者密码。

# 漏洞横向

理论是可以的，然后我们现在就是像如何获取受害者的账号和手机号呢？

登陆后拿到cookie，再次将findsomething的接口报一遍，刚好泄露用户联系方式。
在https://xxxx/。。。。/getAnnouncement 接口泄露人员的联系方式和邮箱。

![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoJn7QhOQ0HiaG9YJdu8IK29v4vrYk6uFFheTJwYa9V2VVCibZ1mCt9UeVea7TeDsWguiav4eWAfsk6W0g9QPzMBzT0eUoI4UStPl4/640?wx_fmt=png&from=appmsg)
然后根据姓名和手机号进行爆破，运气也是好炸天了。

![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoIc4ETMVF2ZoRJEJ83Az9BYQopDRA80DGQOIj1eoMCibzFWuSooSmr8b0mtp98B1s90jeUj8O5VARqB3Hz9ezpAyfVfNKZP9iaSo/640?wx_fmt=png&from=appmsg)
替换id值后，也确实可以修改用户的密码，在这里就没有修改，众测嘛，证明危害即可，不能影响正常的业务。

```
申明：本公众号所分享内容仅用于网络安全技术讨论，切勿用于违法途径，

所有渗透都需获取授权，违者后果自行承担，与本号及作者无关，请谨记守法.

![图片](https://mmbiz.qpic.cn/mmbiz_gif/BwqHlJ29vcqJvF3Qicdr3GR5xnNYic4wHWaCD3pqD9SSJ3YMhuahjm3anU6mlEJaepA8qOwm3C4GVIETQZT6uHGQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=15)

没看够~？欢迎关注！

分享本文到朋友圈，可以凭截图找老师领取

上千教程+工具+靶场账号哦

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcrpvQG1VKMy1AQ1oVvUSeZYhLRYCeiaa3KSFkibg5xRjLlkwfIe7loMVfGuINInDQTVa4BibicW0iaTsKw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=16)

 分享后扫码加我！

回顾往期内容

Xray挂机刷漏洞

零基础学黑客，该怎么学？

网络安全人员必考的几本证书！

文库｜内网神器cs4.0使用说明书

代码审计 | 这个CNVD证书拿的有点轻松

【精选】SRC快速入门+上分小秘籍+实战指南

## 代理池工具撰写 | 只有无尽的跳转，没有封禁的IP！

![图片](https://mmbiz.qpic.cn/mmbiz_gif/BwqHlJ29vcqJvF3Qicdr3GR5xnNYic4wHWaCD3pqD9SSJ3YMhuahjm3anU6mlEJaepA8qOwm3C4GVIETQZT6uHGQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=17)

点赞+在看支持一下吧~感谢看官老爷~

你的点赞是我更新的动力
```

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
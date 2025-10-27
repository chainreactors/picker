---
title: 通过FUZZ技术获取万元赏金
url: https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247494500&idx=1&sn=3216252e5a64609ece001bcc5f53e086&chksm=e8a5e107dfd26811f0319f69432dd91c9cc62fc4c6f615b4854f423a863477806695a78c10d5&scene=58&subscene=0#rd
source: 迪哥讲事
date: 2024-05-05
fetch_date: 2025-10-06T17:16:22.791317
---

# 通过FUZZ技术获取万元赏金

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/YmmVSe19Qj5lP3Z8uEcjUn1HI7f3YVwKCprVPcIp01fnv1740jMkTMGYXfKzCHm9ZxxAeUsuvaDWbiba08weFtg/0?wx_fmt=jpeg)

# 通过FUZZ技术获取万元赏金

迪哥讲事

以下文章来源于网络安全之旅
，作者小乳酸

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM7gOV6xA1v0ib4icvlDwJKiaNEF55z4Lmmd6utIs1DGLFnbA/0)

**网络安全之旅**
.

记录自己网络安全成长之路以及各种奇思妙想，欢迎广大热爱网络安全人士一起交流共勉。

## 0x01 前言

      下午，一个老朋友发来一批资产让我找个有效漏洞，原因是厂商弄活动，提交有效漏洞可获取其奖品，那个奖品对朋友很有吸引力。

## 0x02 漏洞背景

      一个后台系统，称其为https://manager.target.com。

## 0x03 漏洞挖掘过程

      目标站点如下图所示，可以看到不仅要用户名密码，还需要正确的手机号，以及验证码才可登录。

## ![](https://mmbiz.qpic.cn/mmbiz_png/pOOKGW9VicEoiaSyElorta0w0ibEzZAiaJuvxicFrAYlg3tRfVib3iapYgkylJ2eHsicyG3g3hgibq85WcoXDvaz8F68icfg/640?wx_fmt=png)

      对目标站点进行目录探测，未发现有用接口。进一步对其目录探测，使用wfuzz对https://manager.target.com/进行探测，

wfuzz -w dict/test.txt https://manager.target.com/h5FUZZ也无果。至于为什么这样设置目录探测，因为在日常渗透中，我发现大多数h5站点登录都无需验证码，可能是方便手机端用户登录吧。

wfuzz -w dict/test.txt https://manager.target.com/h5-FUZZ，发现https://manager.target.com/h5-mobile返回302状态码，

其跳转到https://manager.target.com/h5-mobile/，发现页面空白，通过burp发现其加载了js文件。

从app.js文件发现mobileapi/login接口。从chunk.js文件中找到其参数。

![](https://mmbiz.qpic.cn/mmbiz_png/pOOKGW9VicEoiaSyElorta0w0ibEzZAiaJuvQzgP9ibqfoGU8avTKOK6dTXKibDs3qOzuqKHExWHVCGEWicEGnX5ySDpw/640?wx_fmt=png)

构造post报文进行登录，返回账户密码错误，使用burp对其进行暴力破解，成功爆破出一组账号，返回一个token值。eyJadGadad1UxMiJ9.eyJsb2dpbl91c2VyX2tlfasdcLTYwYzasdsgzLThkM2Y5NDdiN2FiNSJ9.Mnp7HxlGHdadseN9wmW5vKMe19ffYRGwMYl4WeJJBkAEdj-d6h2HGF0oadqqwasm-brXrvG5q2p5rQ。

将其token值拼接在头部，构造post报文，访问https://manager.target.com/mobileapi/get/orderall(app.js中提取出来的接口）,发现还是返回状态码401，怀疑是token头部字段问题，使用字典对token进行暴力破解，burp暴力破解模块设置如下图所示，其token常用的字段为token,access-token,Authenticator等。

![](https://mmbiz.qpic.cn/mmbiz_png/pOOKGW9VicEoiaSyElorta0w0ibEzZAiaJuvBiaMu5SGO8SO7RIroUh3JglBSxQe8DIoetG8soHmGL3ciaco4PwdHJoQ/640?wx_fmt=png)

发现头部身份认证字段为access-token。其返回了大量用户订单。

![](https://mmbiz.qpic.cn/mmbiz_png/pOOKGW9VicEoiaSyElorta0w0ibEzZAiaJuvxeHZwKE0EsZjibWtIFxPnJFGe1ylJ1RCFKHSDjWghhmqUuvrHzFhibSw/640?wx_fmt=png)

## 0x04 厂商反馈

      漏洞交给了朋友提交，十分钟就得到了厂商反馈，本来以为算高危，厂商给了个严重，良心厂商。

如果你是一个长期主义者，欢迎加入我的知识星球，我们一起往前走，每日都会更新，精细化运营，微信识别二维码付费即可加入，如不满意，72 小时内可在 App 内无条件自助退款
前面有同学问我有没优惠券，这里发放100张100元的优惠券,用完今年不再发放

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj7N5nMaJbtnMPVw96ZcVbWfp6SGDicUaGZyrWOM67xP8Ot3ftyqOybMqbj1005WvMNbDJO0hOWkCaQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj5jYW8icFkojHqg2WTWTjAnvcuF7qGrj3JLz1VgSFDDMOx0DbKjsia5ibMpeISsibYJ0ib1d2glMk2hySA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

## 往期回顾

[dom-xss精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247488819&idx=1&sn=5141f88f3e70b9c97e63a4b68689bf6e&chksm=e8a61f50dfd1964692f93412f122087ac160b743b4532ee0c1e42a83039de62825ebbd066a1e&scene=21#wechat_redirect)

[年度精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487187&idx=1&sn=622438ee6492e4c639ebd8500384ab2f&chksm=e8a604b0dfd18da6c459b4705abd520cc2259a607dd9306915d845c1965224cc117207fc6236&scene=21#wechat_redirect)

[Nuclei权威指南-如何躺赚](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487122&idx=1&sn=32459310408d126aa43240673b8b0846&chksm=e8a604f1dfd18de737769dd512ad4063a3da328117b8a98c4ca9bc5b48af4dcfa397c667f4e3&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试设置功能IV](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486973&idx=1&sn=6ec419db11ff93d30aa2fbc04d8dbab6&chksm=e8a6079edfd18e88f6236e237837ee0d1101489d52f2abb28532162e2937ec4612f1be52a88f&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试注册功能以及相关Tips](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486764&idx=1&sn=9f78d4c937675d76fb94de20effdeb78&chksm=e8a6074fdfd18e59126990bc3fcae300cdac492b374ad3962926092aa0074c3ee0945a31aa8a&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4k2mXPm8xlXujVgicTGvZbcictoGLuPERQn9lRPAKkKUB5ut9XMicric8PxLRmSOq0tT5LuGuD1WemBQ/0?wx_fmt=png)

迪哥讲事

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4k2mXPm8xlXujVgicTGvZbcictoGLuPERQn9lRPAKkKUB5ut9XMicric8PxLRmSOq0tT5LuGuD1WemBQ/0?wx_fmt=png)

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
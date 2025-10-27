---
title: 27200美元赏金！安全研究员披露Facebook、Instagram双因素身份验证漏洞
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458493266&idx=2&sn=235736dba6bc7ec0d726a21754ba6044&chksm=b18e91d886f918ce6609c86f32d28f15abe1cf05e71e455b1886a598b1fdc97bcbf02b0aafc7&scene=58&subscene=0#rd
source: 看雪学院
date: 2023-02-03
fetch_date: 2025-10-04T05:35:10.965491
---

# 27200美元赏金！安全研究员披露Facebook、Instagram双因素身份验证漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HnIIRLfPJb8T8NMAe0AwvibpV0vOvcSXnYia7u6zABVQYNM0gqdFpcice6s92cJAqzibRXPiayeEv1Sag/0?wx_fmt=jpeg)

# 27200美元赏金！安全研究员披露Facebook、Instagram双因素身份验证漏洞

看雪学苑

看雪学苑

近日，一名来自尼泊尔的安全研究员Gtm Mänôz，披露了一个影响Instagram和Facebook的双因素身份验证漏洞。在向Meta报告此漏洞后，其将一笔27200美元的赏金收入了囊中。

双因素身份验证(2FA)是目前常见的一种保护用户账户安全的手段。它是一种需要提供两个身份验证因素以确认身份的身份验证过程，用户需要用两种方式（用户所知道的和用户所拥有的，例如密码和手机收到的验证码）证明自己的身份才能获得账户访问授权。

据悉，该漏洞存在于Facebook母公司Meta用于确认手机号码和电子邮件地址的组件中。Gtm Mänôz注意到，该组件未对验证码做时间和失败次数校验，这使得攻击者在获知受害者的手机号码后，能够暴力破解验证码。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HnIIRLfPJb8T8NMAe0AwvibHlVt8PtIE86yPd1PGE7v1cr5lwBnWY3RjJHicWEIwwTjccyhRxrG0Sw/640?wx_fmt=jpeg)

而一旦攻击者成功试出正确的验证码，受害者的电话号码就会与攻击者使用的账户绑定，同时受害者账户的双因素身份验证也会被停用。攻击者在此之后就能够通过钓鱼等方式取得受害者密码，接过受害者账户控制权限。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HnIIRLfPJb8T8NMAe0Awvibr8Qb7xGRLXNEvAX3qGvBVMGuqJNM8pvVhSaZWH7iagA7nODWzyohy5Q/640?wx_fmt=jpeg)

黑客攻击成功后，用户会收到Facebook官方发送的一封电子邮件，通知其电话号码在Facebook上被其他人注册及验证。

根据Gtm Mänôz博客时间线，其于2022年9月14日向Meta报告了这个漏洞，IT巨头Facebook则于2022年10月17日完成了修复，其表示并未发现此漏洞有被滥用的迹象。Meta为Gtm Mänôz的漏洞发现及报告奖励了27200美元。

博客链接：*https://medium.com/pentesternepal/two-factor-authentication-bypass-on-facebook-3f4ac3ea139c*

编辑：左右里

资讯来源：Meta

转载请注明出处和本文链接

**每日涨知识**

安全测试（security tests）

安全测试能够验证控制在正常运行。这些测试包括自动扫描、工具辅助渗透测试和手动测试安全性。安全测试应该定期进行，需要关注保护机构的每个关键安全控件。

﹀

﹀

﹀

![](https://mmbiz.qpic.cn/mmbiz_jpg/Uia4617poZXP96fGaMPXib13V1bJ52yHq9ycD9Zv3WhiaRb2rKV6wghrNa4VyFR2wibBVNfZt3M5IuUiauQGHvxhQrA/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8E9S6vNnUMRCOictT4PicNGMgHmsIkOvEno4oPVWrhwQCWNRTquZGs2ZLYic8IJTJBjxhWVoCa47V9Rw/640?wx_fmt=gif)

**球分享**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8E9S6vNnUMRCOictT4PicNGMgHmsIkOvEno4oPVWrhwQCWNRTquZGs2ZLYic8IJTJBjxhWVoCa47V9Rw/640?wx_fmt=gif)

**球点赞**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8E9S6vNnUMRCOictT4PicNGMgHmsIkOvEno4oPVWrhwQCWNRTquZGs2ZLYic8IJTJBjxhWVoCa47V9Rw/640?wx_fmt=gif)

**球在看**

![](https://mmbiz.qpic.cn/mmbiz_gif/1UG7KPNHN8FxuBNT7e2ZEfQZgBuH2GkFjvK4tzErD5Q56kwaEL0N099icLfx1ZvVvqzcRG3oMtIXqUz5T9HYKicA/640?wx_fmt=gif)

戳“阅读原文”一起来充电吧！

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/1UG7KPNHN8EGLfh77kFmnicd9WOic2ibvhCibFdB4bL4srJCgo2wnvdoXLxpIvAkfCmmcptXZB0qKWMoIP8iaibYN2FA/0?wx_fmt=png)

看雪学苑

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1UG7KPNHN8EGLfh77kFmnicd9WOic2ibvhCibFdB4bL4srJCgo2wnvdoXLxpIvAkfCmmcptXZB0qKWMoIP8iaibYN2FA/0?wx_fmt=png)

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
---
title: 35个Chrome扩展被劫持，黑客攻击细节披露
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458587938&idx=2&sn=8632d3bdf0ba63f40ad769149d031f97&chksm=b18c23a886fbaabe048f0a103741ca0996bc074753ef3020f8e23546b6680b71989fee85add5&scene=58&subscene=0#rd
source: 看雪学苑
date: 2025-01-03
fetch_date: 2025-10-06T20:09:49.633038
---

# 35个Chrome扩展被劫持，黑客攻击细节披露

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FVzNwDWrTVic9ZOChjQcCJd5pibGUmg4WUgxuq0cVXVe7fERkDP0IKFXbvUE8icJcX76O2K1iap3USlQ/0?wx_fmt=jpeg)

# 35个Chrome扩展被劫持，黑客攻击细节披露

看雪学苑

看雪学苑

近期，网络安全领域发生了一起严重的黑客攻击事件，至少35个Chrome扩展被黑客劫持。此次攻击的目标包括了知名网络安全公司Cyberhaven的扩展，显示出攻击者的技术手段相当高明。

攻击始于2024年12月5日，黑客通过精心设计的钓鱼邮件，冒充Google发送警告，声称开发者的Chrome扩展违反了Chrome Web Store的政策，可能会被移除。邮件中包含一个看似合法的“政策违规”链接，实则指向一个钓鱼网站，目的是诱骗开发者交出对Chrome扩展的控制权。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FVzNwDWrTVic9ZOChjQcCJd88fbey6K5PibVUFjjhqictLNsgeFGJfCfIurt8efqEcT0J8CpdF25VsQ/640?wx_fmt=png&from=appmsg)

攻击中使用的网络钓鱼电子邮件

这些钓鱼邮件使用了诸如supportchromestore.com、forextensions.com、chromeforextension.com等域名，模仿Google的官方通知，诱使开发者点击链接并授权一个名为“Privacy Policy Extension”的恶意OAuth应用。这个应用请求权限管理Chrome Web Store扩展，一旦授权，攻击者就能通过受害者的账户发布恶意更新。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FVzNwDWrTVic9ZOChjQcCJdbYoiaVz1xSWpwkiak1NiaNibTUeiaS3ibYoIaPOq02IZMO5ONAuCfQFicJMew/640?wx_fmt=png&from=appmsg)

恶意身份验证请求

Cyberhaven在事后的分析中指出，即使员工开启了Google Advanced Protection并有多重身份验证（MFA），但在OAuth授权流程中并未触发MFA提示，导致攻击者得以绕过这些安全措施。攻击者一旦获得权限，就会在扩展中注入恶意文件，如‘worker.js’和‘content.js’，这些文件包含窃取Facebook账户数据的代码。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FVzNwDWrTVic9ZOChjQcCJdxSrOhzDQpJKllxZDaNXZfn8NTngUnDrNGY1C6IREs01VEmvDFWZOXA/640?wx_fmt=png&from=appmsg)

权限审批提示

受影响的扩展被重新发布到Chrome Web Store，而用户在不知情的情况下安装了这些恶意更新。攻击者的目标是Facebook商业账户，他们试图通过窃取的用户数据进行直接支付、散布虚假信息或将访问权限出售给他人。

此次事件再次提醒开发者和用户，网络安全威胁无处不在，即使是专业的安全公司也可能成为攻击目标。用户需要保持警惕，及时更新软件，避免点击不明链接。

资讯来源：bleepingcomputer

转载请注明出处和本文链接

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
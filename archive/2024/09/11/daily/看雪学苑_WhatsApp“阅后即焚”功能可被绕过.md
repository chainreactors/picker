---
title: WhatsApp“阅后即焚”功能可被绕过
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458572382&idx=4&sn=f3a859c26f0d231625c94e25670dac4b&chksm=b18de6d486fa6fc2e904042fddbe97f0fbb5e470d61197a34d1c9379a6d7bc2721f0ce289b44&scene=58&subscene=0#rd
source: 看雪学苑
date: 2024-09-11
fetch_date: 2025-10-06T18:29:04.185316
---

# WhatsApp“阅后即焚”功能可被绕过

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Hljwtk29mb9ibibYBFsn2qhX7IJnmFTh9scNS8Ficyz9s4fic3JKFzpDvEia5lPuHicOLErmPtxSXhjRMA/0?wx_fmt=jpeg)

# WhatsApp“阅后即焚”功能可被绕过

看雪学苑

看雪学苑

WhatsApp是一个拥有超过20亿用户的即时通讯应用。而在最近，安全公司Zengo的研究员披露WhatsApp的“阅后即焚”功能存在严重漏洞。——该功能本意是让用户发送的消息只能被查看一次，以保护用户隐私不外泄，但实际上却可以被轻易绕过。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Hljwtk29mb9ibibYBFsn2qhXHD226OJCM2wDRCDrv7n6kyickM0hXZHm7aFKeZwX0dcLOHzDNIOfsDw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Hljwtk29mb9ibibYBFsn2qhXN3DneckiaP4oQn61zPRCMdRUjGegnyXfnmResvbrDNjclSryiaaHrHUA/640?wx_fmt=png&from=appmsg)

研究员发现，WhatsApp的“阅后即焚”功能实际上是发送加密的媒体消息到接收者的所有设备上，这些消息与正常的消息几乎相同，但包含了加密数据的URL和解密密钥。此外，“阅后即焚”消息还设置了一个“view once”标志为“true”。然而，攻击者可以通过设置这个“view once”标志为“false”来绕过这个功能，从而允许消息被下载、转发和分享。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Hljwtk29mb9ibibYBFsn2qhXvcmXNv8D9JklmVfACA6hwvdUea4JVSiaq7Mxmyo2DGEsgQjC8ERuqyg/640?wx_fmt=png&from=appmsg)

Zengo团队表示他们发现这一漏洞已被在野利用一年多。他们在GitHub上找到了一些代码示例，包括一个修改后的Android客户端和一个Chrome扩展，这些代码可以让攻击者轻易地绕过这个限制。

由于该漏洞已得到证实可被利用，Zengo团队决定放弃通常的90天等待期，而改为直接公开此漏洞。他们在8月26日就此问题通知了WhatsApp，并通过Meta的漏洞赏金计划提交了报告。

 “……唯一比没有隐私更糟糕的是虚假的隐私感，在这种情况下，用户被误导以为某些形式的通信是私有的，但事实却并非如此。目前，WhatsApp的‘阅后即焚’功能就是一种虚假的隐私感，应该要么彻底修复，要么放弃。” Zengo团队强调道。

据悉，WhatsApp目前已确认此问题并积极进行修复，将在测试成功后推出新版本。

编辑：左右里

资讯来源：zengo

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
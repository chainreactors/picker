---
title: 三十多年历史的RADIUS网络协议被发现可绕过身份验证
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458563327&idx=2&sn=4735f9b8dccb61b2de4ee701183bf077&chksm=b18d827586fa0b63ebb4083479186d204a5c71c0ccf6e6b303979a50988b4e4c1a1d54dd4168&scene=58&subscene=0#rd
source: 看雪学苑
date: 2024-07-12
fetch_date: 2025-10-06T17:43:54.889888
---

# 三十多年历史的RADIUS网络协议被发现可绕过身份验证

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EQpXR3mibibqEQU4dF9tmOg4icXXhL7WwibyG5libVcZfDicalNsZcWtqp5dT6dicrrfdkLghuqIxjeeT0w/0?wx_fmt=jpeg)

# 三十多年历史的RADIUS网络协议被发现可绕过身份验证

看雪学苑

看雪学苑

近日，微软公司和加州大学等机构的安全研究员们披露了一个影响互联网连接和应用的漏洞，该漏洞被命名为“Blast-RADIUS”，存在于远程用户拨号认证服务协议中（RADIUS，一个于1991年开发的网络协议，距今已有三十多年历史）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EQpXR3mibibqEQU4dF9tmOg4SWnhBXXkl6yquCjxqmBcRPC418xJwZSln1BicXZKwAwYDulHuJQbaVQ/640?wx_fmt=png&from=appmsg)

据了解，RADIUS协议是一种用于管理网络访问的轻量级认证协议。它是一个允许用户连接到网络的集中式授权、认证和计费管理的客户端-服务器协议，广泛应用于各种互联网应用和服务，如VPN、Wi-Fi、家庭互联网连接以及企业网络的交换机和路由器。

研究人员披露，该漏洞（CVE-2024-3596）源于RADIUS协议缺乏身份验证和完整性检查，使得攻击者可以修改这些数据包而不被检测到。他们已经发现一种利用MD5哈希算法的方法，可以伪造所需的凭证。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EQpXR3mibibqEQU4dF9tmOg4X5IvuvZ5eZmSwQj2V39XoP9V3DZVn2B1UJx7ufISJFKDSoVl2Yn8ibg/640?wx_fmt=png&from=appmsg)

黑客利用弱加密哈希MD5伪造RADIUS服务器的身份验证响应，可导致中间人攻击，使攻击者能够访问客户端和服务器之间的受保护通信。假如黑客成功渗透网络并获得至少部分访问权限，那么通过利用Blast-RADIUS漏洞，黑客可以升级到能够登录任何使用RADIUS进行认证的设备，或者分配自己任意的网络权限。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EQpXR3mibibqEQU4dF9tmOg4b5yc99PpKf64eKTGMxiavqJGCfnViau9mQmm5Eq6KibicdWm0o0D3vDcjg/640?wx_fmt=png&from=appmsg)

好消息是，尽管该漏洞已经存在30年，但实际利用漏洞的可能性较低，因为攻击必须在RADIUS数据包在客户端和服务器之间传输时发生。然而也要注意到，BlastRADIUS是一个影响所有符合标准的RADIUS客户端和服务器的基本设计缺陷。因此，使用该协议的组织和互联网服务提供商（ISP）最好及时进行更新修复。

论文链接：https://www.blastradius.fail/pdf/radius.pdf

编辑：左右里

资讯来源：blastradius

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
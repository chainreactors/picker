---
title: ​研究者揭露微软 Windows 内核的操作系统降级漏洞
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458579476&idx=3&sn=a068c8f37e67f44576894bd4525a3be6&chksm=b18dc29e86fa4b886b74ef63e071b4feff13d277532cea3a21cbf0f7168a31fde1eb79d4f282&scene=58&subscene=0#rd
source: 看雪学苑
date: 2024-10-30
fetch_date: 2025-10-06T18:52:39.377105
---

# ​研究者揭露微软 Windows 内核的操作系统降级漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GWQXsxtiaCpMQvg1R6csm5e8xKvOImuM3xMZ2oJZwg0STKesHX5uHI9xLSnyHrfpg2DXV3CK0HUPA/0?wx_fmt=jpeg)

# ​研究者揭露微软 Windows 内核的操作系统降级漏洞

看雪学苑

看雪学苑

近期，SafeBreach Labs的研究人员揭露了一种名为“Windows Downdate”的新型攻击技术，该技术能够操纵Windows 11系统在更新时降级关键系统组件，使部分漏洞修复补丁失效。这一攻击原理最初于2024年8月在Black Hat USA 2024上披露，现在更多细节被公布。

“Windows Downdate”技术利用了一个名为“ItsNotASecurityBoundary”的驱动程序签名强制（DSE）绕过漏洞，**允许攻击者加载未签名的内核驱动程序，并将经过验证的安全目录替换为恶意版本。**例如，攻击者可以针对“ci.dll”等关键组件，将其降级到易受攻击的状态，从而获得内核级权限。这项技术是“虚假文件不变性”（FFI）新漏洞的一部分，利用了关于文件不可变性的错误假设，允许通过清除系统工作集来修改“不可变”文件。

研究人员概述了在具有不同级别虚拟化安全（VBS）保护的Windows系统中可利用漏洞的步骤，并发现了多种禁用VBS关键功能的方法，包括凭证防护和受管理程序保护的代码完整性（HVCI）等功能，甚至首次使用了UEFI锁。攻击者可以对关键操作系统组件进行自定义降级，暴露以前修补过的漏洞，使系统容易被利用。

这种攻击技术对企业构成了重大威胁，允许攻击者加载未签名的内核驱动程序、启用自定义rootkit以解除安全控制、隐藏进程并保持隐蔽性。为降低风险，企业应及时更新系统，打上最新的安全补丁，同时部署有效的端点检测和响应（EDR）解决方案，以检测和响应恶意活动，防止未经授权的访问和数据泄露。此外，使用UEFI锁定和“强制”标志启用VBS还能提供额外的保护。

资讯来源：thehackernews.com

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
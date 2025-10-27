---
title: 谷歌浏览器“SymStealer”漏洞：可窃取用户敏感文件
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458492659&idx=2&sn=a63c0f35e0b19a057d9fbe52e437b144&chksm=b18eae7986f9276feb843b5b5ea16ac6b6234be576b2224b8390c71020f6bf3bf6e68dde9ff2&scene=58&subscene=0#rd
source: 看雪学院
date: 2023-01-17
fetch_date: 2025-10-04T04:03:35.407376
---

# 谷歌浏览器“SymStealer”漏洞：可窃取用户敏感文件

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EsP0xyQOicAHbxq8yLjXa2FcbVsG12R9rGoYTxXMiaITAVX110ohLe4fyPVQOrv2lS6p3y3y2ELvww/0?wx_fmt=jpeg)

# 谷歌浏览器“SymStealer”漏洞：可窃取用户敏感文件

看雪学苑

看雪学苑

近期，网络安全公司Imperva的红队披露了一个名为“SymStealer”的漏洞（CVE-2022-3656），据称影响超过25亿Google Chrome以及基于Chromium的浏览器用户。此漏洞允许攻击者窃取敏感文件，如加密钱包和云提供商凭据。

据悉，Chrome是目前使用最广泛的浏览器，市场占有率为65.52％。另外两个排名前6的浏览器Opera和Edge也都基于Chromium，这使Chromium的市场占有率超过了70％。Chromium的流行有诸多好处，如兼容性和安全审计。但这也增加了跨浏览器漏洞的可能性。

符号链接（symlink，也称symbolic link）是一种指向另一个文件或目录的文件类型。它允许操作系统将链接的文件或目录视为位于符号链接的位置，这可以用于创建快捷方式、重定向文件路径或以更灵活的方式组织文件。然而，如果符号链接处理不当，它们也可能引入漏洞。

在Imperva向Google披露的漏洞中，问题就源自浏览器在处理文件和目录时与符号链接交互的方式。具体而言，浏览器没有正确检查符号链接是否指向非法访问的位置，导致允许窃取敏感文件。这个问题通常称之为符号链接跟随（symbolic link following）。

实际的攻击场景中，攻击者可能会伪造一个提供新加密钱包服务的虚假网站。该网站会欺骗用户通过下载他们的“恢复”密钥来创建新钱包。

> 许多加密钱包和其他在线服务要求用户下载“恢复（recovery）”密钥才能访问其帐户。这些密钥作为一种备份，防止用户因任何原因（例如忘记密码）而无法访问其帐户。用户通常会下载这些密钥，然后将其上传回网站，以验证其对帐户的所有权。

然而这些密钥实际上却是一个包含符号链接到用户计算机上敏感文件或文件夹（如云提供商凭据）的zip文件。当用户解压并将 “恢复”密钥上传回网站时，符号链接将被处理，攻击者就此获得对敏感文件的访问权限。而用户甚至都可能没有意识到任何不对劲，因为该网站可能被设计成看起来十分的合法正规，下载和上传“恢复”密钥的过程可能看起来很正常。

Google已经确认了这个漏洞并发布了修复补丁。为了防范这个漏洞，用户最好更新到最新版本的Chrome或基于Chromium的浏览器，以确保自己的文件不会被盗取。

此外，用户应该尽量避免在网上下载可疑文件，特别是那些来自不可信网站的文件。如果用户不确定文件是否可信，可以使用杀毒软件来检查文件是否受损或包含恶意软件。另外，用户也可以使用一些浏览器扩展来防御这个漏洞，例如防篡改保护之类的扩展。

编辑：左右里

资讯来源：Imperva

转载请注明出处和本文链接

**每日涨知识**

特洛伊木马（trojan horse）

一种恶意代码对象，看起来是个善意的程序(如游戏或简单的实用程序)。它公开执行"覆盖"功能，而且还带有未知的有效载荷，如病毒。

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
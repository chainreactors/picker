---
title: ImageMagick：隐藏在网上图像背后的漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247556983&idx=1&sn=6d82fa0da6bbbeab07a1ba623f56f2ee&chksm=e915cf4dde62465b1cc58f2364765a1d318ec8c5e435b4c69e7e3ffb9877567ec2217b2795f8&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2023-02-04
fetch_date: 2025-10-04T05:43:35.242048
---

# ImageMagick：隐藏在网上图像背后的漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o29VwC7PK34uZcxX7x73nNWtNCgsxSYouTdGpaygqoGU6deVfhaYF6FdIJ16QT3WJkMyzaHBZCejUw/0?wx_fmt=jpeg)

# ImageMagick：隐藏在网上图像背后的漏洞

布加迪

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

ImageMagick是一种免费开源软件套件，用于显示、转换和编辑图像文件。它可以对200多种格式的图像文件进行读写操作，因此它在全球网站上很常见，因为我们总是需要为用户的个人资料和目录等内容处理图片。

Ocelot团队在最近的一次高级持续性威胁（APT）模拟活动中发现，ImageMagick在一个基于Dupal的网站中被用于处理图像，因此该团队决定尝试找出该组件中的新漏洞，随后下载了最新版本的ImageMagick（当时是7.1.0-49）。结果发现了两个零日漏洞：

  CVE-2022-44267：ImageMagick 7.1.0-49很容易受到拒绝服务攻击。当它解析PNG图像（比如为了调整大小）时，转换进程可能会等待stdin输入。

  CVE-2022-44268：ImageMagick 7.1.0-49很容易受到信息泄露攻击。当它解析PNG图像（比如为了调整大小）时，生成的图像可能嵌入了任意远程文件的内容（如果ImageMagick二进制代码拥有读取权限）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29VwC7PK34uZcxX7x73nNWtpNN3lj8X7X8TTIAOokkeClI4bpHibHqX1MPjQURxgTpLMYPxK7JTWGA/640?wx_fmt=png)
   如何触发漏洞利用？

攻击者需要使用ImageMagick将恶意图像上传到网站，以便远程利用上述漏洞。

Ocelot团队非常感谢ImageMagick的志愿者团队，他们及时地验证并发布了所需的补丁：

https://github.com/ImageMagick/ImageMagick/commit/05673e63c919e61ffa1107804d1138c46547a475

这篇博文解释了这些漏洞的技术细节。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29VwC7PK34uZcxX7x73nNWtpNN3lj8X7X8TTIAOokkeClI4bpHibHqX1MPjQURxgTpLMYPxK7JTWGA/640?wx_fmt=png)
   CVE-2022-44267：拒绝服务

ImageMagick：7.1.0-49

当ImageMagick解析PNG文件时，比如在收到图像后的调整大小操作中，转换进程可能会因无法处理其他图像而等待stdin输入，导致拒绝服务攻击。

不法分子可以制作PNG或使用现有的PNG，并添加文本块类型（比如tEXt）。这种类型有关键字和文本字符串。如果关键字是字符串“profile”（不带引号），那么ImageMagick将把该文本字符串解释为文件名，并将内容作为原始资料加载。如果指定的文件名是“-”，ImageMagick将尝试从标准输入读取内容，可能会让进程永远等待。

漏洞利用路径执行：

上传图像以触发ImageMagick命令，比如“convert”

ReadOnePNGImage（coders/ png.c: 2164）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29VwC7PK34uZcxX7x73nNWtO0rE8zDR1Xd1FNXicic1OBUM1icl4LPcr0Sj45icxe0XZxrbfelFAd5HFA/640?wx_fmt=png)

图1

读取“tEXt”文本块：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29VwC7PK34uZcxX7x73nNWtWeGw2FeN9lKFXicNO5QsES6ZPKt5rrlpgKaKk1IbjkeMmaiaHiaWHffuQ/640?wx_fmt=png)

图2

SetImageProfile（MagickCore / property.c: 4360）：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29VwC7PK34uZcxX7x73nNWtpN5e7iaIXP8dkV5WG4j6ZHNDMOYjFRtq38lqcMUWJvicUH7GYlaXfyibQ/640?wx_fmt=png)

图3

检查关键字是否等于“profile”：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29VwC7PK34uZcxX7x73nNWtMkGA32yQOGstC7vaTwpaC2Ss0aV7cO5Ehp1Ziaor6r0ZIsmO7w95mhw/640?wx_fmt=png)

图4

在第4720行将文本字符串复制为文件名，在第4722行保存内容：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29VwC7PK34uZcxX7x73nNWt7ySEqoiaozPydZh6BKxib15gXCCKMI8R6FTm14BbE7OEjpIAllpk6h2w/640?wx_fmt=png)

图5

FileToStringInfo将内容存储到string\_info->datum（MagickCore/string.c:1005）：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29VwC7PK34uZcxX7x73nNWtyx2KibsW2010ENj7WvfLSGWObZzYPe1J8AV3RliaVAGibiaLLEtpZEqoHQ/640?wx_fmt=png)

图6

FileToBlob（MagickCore/blob.c:1396）：将stdin分配给文件名作为“-”，导致进程永远等待输入：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29VwC7PK34uZcxX7x73nNWtt9ZqYWnSdicyJPiciaCZpyD1Ao7jskO4v8P2uSqSeNz4AlDLNFo3QVtEQ/640?wx_fmt=png)

图7

概念验证（PoC）：恶意PNG文件：

89504e470d0a1a0a0000000d49484452000000010000000108000000003a7e9b550000000b49444154789c63f8ff1f00030001fffc25dc510000000a7445587470726f66696c65002d00600c56a10000000049454e44ae426082

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29VwC7PK34uZcxX7x73nNWtxs7hZXO9U13icHCKM3Uics4OfiaOeVWm3K0wRlAyJ7zucutpfu9kic2sdQ/640?wx_fmt=png)

图8

证据：恶意图像文件：OCELOT\_output.png

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29VwC7PK34uZcxX7x73nNWtRojfB5NoH7vBELqryDLicEdlg27IA0KzWic3NyxuJouAJNpp7rsyScOw/640?wx_fmt=png)

图9

Stdin输入永远等待：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29VwC7PK34uZcxX7x73nNWt6LicNGRaFpq57f8qb08xINpVV020bJ3JVjeoyxuktwZD6VNJiaVcQSvw/640?wx_fmt=png)

图10

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29VwC7PK34uZcxX7x73nNWtpNN3lj8X7X8TTIAOokkeClI4bpHibHqX1MPjQURxgTpLMYPxK7JTWGA/640?wx_fmt=png)
   CVE-2022-44268：任意远程泄漏

ImageMagick：7.1.0-49

当ImageMagick解析PNG文件时，比如在调整大小操作中，生成的图像可能嵌入了来自网站的任意远程文件的内容（如果magick二进制代码拥有读取权限）。

不法分子可以制作PNG或使用现有的PNG，并添加文本块类型（比如tEXt）。这种类型有关键字和文本字符串。如果关键字是字符串“profile”（不带引号），那么ImageMagick将把文本字符串解释为文件名，并将内容作为原始资料加载，然后攻击者可以下载大小调整后的图像，该图像随带远程文件的内容。

漏洞利用路径执行：

上传图像以触发ImageMagick命令，比如“convert”

ReadOnePNGImage（coders/ png.c: 2164）：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29VwC7PK34uZcxX7x73nNWtFicQgwp0BOEm1iavE0zImlDm9N0DkQhciaLRnz9KeWPPKFCBzichibYZKbA/640?wx_fmt=png)

图11

读取tEXt文本块：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29VwC7PK34uZcxX7x73nNWt5CPREkcYK9R4jHU9XumMBoTJCvA6kdjibMAtbOicFcBPBQgxARpbjQ6g/640?wx_fmt=png)

图12

SetImageProfile（MagickCore / property.c: 4360）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29VwC7PK34uZcxX7x73nNWtbvfEpeansNhWAX4ZLRaw6XaS7zSqybic1BYJXamqot1EDFfDzd3PHFA/640?wx_fmt=png)

图13

检查关键字是否等于“profile”：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29VwC7PK34uZcxX7x73nNWt19bn5E5ddb2Wc5T4FnJxz5vROL8zLN7Jqg3s42BxC5oicXFDfSzQtWA/640?wx_fmt=png)

图14

在第4720行将文本字符串复制为文件名，在第4722行保存内容：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29VwC7PK34uZcxX7x73nNWtLVGjl0rP0PjknBicPQibFc5jggUdt2YMUXiblo7qq84GXRuMRpgNxq3aw/640?wx_fmt=png)

图15

FileToStringInfo将内容存储到string\_info->datum（MagickCore/string.c:1005）：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29VwC7PK34uZcxX7x73nNWtq5YWHcOv77lzaoGF5dVfEaNffrfyqVdAYQSFXzKTZ4et6iaDmVINBTA/640?wx_fmt=png)

图16

如果提供了一个有效（且可以访问）的文件名，内容将返回给调用者函数（FileToStringInfo）， StringInfo对象将返回给SetImageProperty函数，将blob保存到生成的新图像中，这要感谢SetImageProfile函数：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29VwC7PK34uZcxX7x73nNWtK1Q9V2gDrNYKH27trxsRyBFGFrLseeo8iawh0EiauW2srjYSDsGkfIFQ/640?wx_fmt=png)

图17

这个新图像可供攻击者下载，其中嵌入了任意网站文件内容。

PoC：恶意PNG内容泄露“/etc/passwd”文件：

89504e470d0a1a0a0000000d4948445200000001000000010100000000376ef9240000000a49444154789c636800000082008177cd72b6000000147445587470726f66696c65002f6574632f70617373776400b7f46d9c0000000049454e44ae426082

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29VwC7PK34uZcxX7x73nNWtGvyibfqw1dsVjXJt69yNlI66iadXb469qM1ogibouFHJQiba9booIMgF5g/640?wx_fmt=png)

图18

证据：

通过profile->datum变量，/etc/passwd的内容存储在图像中：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29VwC7PK34uZcxX7x73nNWtpfuWe5dAPMXyrRR5gD8x4219GaUrMNX6nB7LbsL5ibiaiaxQAap28XNBA/640?wx_fmt=png)

图19

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29VwC7PK34uZcxX7x73nNWtciankYVN4I1v4r1DUdlzpGWiafIvibLPZcJYm5xwWQOLaicC2niccekwGxA/640?wx_fmt=png)

图20

/etc/passwd内容的十六进制表示，内容从图像中提取：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29VwC7PK34uZcxX7x73nNWtBnaElAZZBLE7XryfycK5rqSDqMiab4O493Ea6mJKjxG2c0UpictGfxPg/640?wx_fmt=png)

图21

来自网站中/etc/passwd的内容，在生成的图像中收到：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29VwC7PK34uZcxX7x73nNWtTCl2CuSiay6Q9icicq3RrlMLJdJmKFgbvcrGFN7zfBuYKrGLX13eDobnw/640?wx_fmt=png)

图22

显示漏洞利用的视频：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29VwC7PK34uZcxX7x73nNWtJibLaibrnQ1LvTngAOSPViaFdMGBRLPibmaVHzGicG3j2J2ECyY6XBrs9oA/640?wx_fmt=png)

图23

参考及来源：https://www.metabaseq.com/imagemagick-zero-days/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29VwC7PK34uZcxX7x73nNWt6SJZ5Leicu7MlwB6vmapQaZWiaibbFYibJBmKkhTY2jR81fWLO0P0Y23EQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icEjy5ZrpCcgr4BicXicPv08DSsrgibDcJQpvwkZoO4OqdIpJNhj6TO5xV0ic0AnVf7f2kcPnNevQlTtQ/640?wx_fmt=png)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

嘶吼专业版

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

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
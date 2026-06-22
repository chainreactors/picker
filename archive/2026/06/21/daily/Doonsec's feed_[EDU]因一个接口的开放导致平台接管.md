---
title: [EDU]因一个接口的开放导致平台接管
url: https://mp.weixin.qq.com/s/0zEHtcunYN4Vi7vzMBdWPg
source: Doonsec's feed
date: 2026-06-21
fetch_date: 2026-06-22T07:14:16.491639
---

# [EDU]因一个接口的开放导致平台接管

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Qzel5kQIPbAoIb4IwRx0ClWRPicV4LJWWrpfXkoELDWHOvY5aRPhdGz49QIAhAxuPXlyd2K9JKXibY2Kzia84iaFZX9F9vZFzzRwFicU11icyz7cs/0?wx_fmt=jpeg)

# [EDU]因一个接口的开放导致平台接管

原创

略懂安全的三秋
略懂安全的三秋

略懂安全的三秋

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

无问AI远超通用大模型，在网络安全问题理解、代码生成、安全研究分析及其他复杂场景上是你的最佳选择。

链接：https://www.wwlib.cn/index.php/

如果积分不够用可以使用我的积分码，即可领取100积分

兑换链接：https://www.wwlib.cn/index.php/gift

******WUWEN\_FxWhkLkyuiU01gOL0y******

![](https://mmbiz.qpic.cn/mmbiz_jpg/Qzel5kQIPbCKIiav1hKrhJ4P01lK5CibF0kRaeNcQXyzPWj5WJacYYAsDkMR5ehAaliaS1YwibEWXkicvrDOcvxYToxFL5l03HM789NuvKkYPVnw/640?wx_fmt=jpeg)

开局登录框起手

这里试了几个弱口令组合都没登录成功，于是尝试绕过验证码也没有成功，所以爆破这条路是到头了。

查看插件

![](https://mmbiz.qpic.cn/mmbiz_jpg/Qzel5kQIPbBdfYN6Y5Bk53WY7SP7heKbuicy4DWa9aCLKCoWPnXYMTMDaYCnlc113ibLd2HSHVNQ19rYoG3xwOnEAwAqMR6kicdyPGbNT1rnHI/640?wx_fmt=jpeg)

72个接口不是很多，但还是要遍历一下

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Qzel5kQIPbBiaR82P9YbjyE1a1DeyXer39EicWNIblC3rsYTTgpFnWdQe8XGnDBcZQ8M5EcLM4fpRwK7ZpQ3w3CsxvEw0N0QiaZ1OEyv5dEib0M/640?wx_fmt=jpeg)

开启了Django但没什么信息泄露

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Qzel5kQIPbChy7aqja6CE5qIRFuMZgGSFllrTw7z6QyEd08dYmnGnOM8exjiawmiazQaMABLhcibqUH31CBNicy7wWwTic2FO3u5SThEcR3IMQic4/640?wx_fmt=jpeg)

注册接口到是有点东西

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Qzel5kQIPbDLqHYfDjagJIFkrd2df13ejtS4nPXQswiafCAb6MP0x4a1HBWW44SkxmbrUQIWJc5t0JpVdwFhfRbRl1oppFgN6LNzZXeic1dcc/640?wx_fmt=jpeg)

缺少点东西，不用想就是注册信息了

老生常谈根据登录包构造注册包，又根据响应包补注册包，于是就有

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Qzel5kQIPbALaj9KypU1xfKCIrw334mqINXHcjk4ibKy5MFy3gN9laicC2mZw81FaOATvicztKFnOIOt6Hj9dDNnucINOiakLDLJZoWvafvl4YQ/640?wx_fmt=jpeg)

因为我注册过来，所以就不请求了。

使用注册的账号登录

![](https://mmbiz.qpic.cn/mmbiz_jpg/Qzel5kQIPbCQhjuBYb4ibaE6f9bRSWqnG6V0cQ6Zs99Fxoc8fo3IGuSJcabQpcJv02djYewDWvZIBW6gcmkIlHRd2wYxbm8HM009mr4IjJu4/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/Qzel5kQIPbDfFslXr9MmFaiaEQZSOGstN2soeq9rKONGln0xka6qhP93byn5gaZ5Llt9SwMicK8XewPUTqkI8diaEkXEZa3V7RVq0NMvzZgiamo/640?wx_fmt=jpeg)

这期比较水和少

`由于传播、利用本公众号所提供的信息而造成``的任何直接或者间接的后果及损失，均由使用``者本人负责，公众号略懂安全的三秋不``为此承担任何责任，一旦造成后果请自行承担！`

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Qzel5kQIPbCLibpoeKyUIrykBCCd4Ix1Q2SVIyIsc7IGsL6y2kJktXuMpEpkOprEoL5TVjNdLBTeiaVESIo318WKeepXDXS0sfibQPxG3maGhU/0?wx_fmt=png)

略懂安全的三秋

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Qzel5kQIPbCLibpoeKyUIrykBCCd4Ix1Q2SVIyIsc7IGsL6y2kJktXuMpEpkOprEoL5TVjNdLBTeiaVESIo318WKeepXDXS0sfibQPxG3maGhU/0?wx_fmt=png)

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
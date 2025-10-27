---
title: PWA网络钓鱼，针对Android、iOS金融欺诈活动
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247546595&idx=2&sn=dc479608ee5cc480a5de3fc5bc5fddad&chksm=fa938022cde4093444d803c02901c42926265bd3b9ffa696409dada3ab24526fc69f9f5b6d2d&scene=58&subscene=0#rd
source: CNCERT国家工程研究中心
date: 2024-08-27
fetch_date: 2025-10-06T18:08:23.575581
---

# PWA网络钓鱼，针对Android、iOS金融欺诈活动

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176liaa98w4YwicjzOGLbBhuIm4wqEjoV8HdyWm2RZytz2aX7xl3QGmUBuy1GH4ppMxhHaE71ryiaVvReQ/0?wx_fmt=jpeg)

# PWA网络钓鱼，针对Android、iOS金融欺诈活动

网络安全应急技术国家工程中心

![](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176liaa98w4YwicjzOGLbBhuIm4XdggN0RevA4QKIgic5HIxLpGzicTQBAZVM5EXhbNLPQFx1VWViaPiaJt6g/640?wx_fmt=jpeg&from=appmsg)

在捷克共和国、匈牙利和格鲁吉亚的金融欺诈活动中，最近发现了一种复杂的移动网络钓鱼技术。

这种网络钓鱼方法利用渐进式Web应用程序PWA，提供类似本机应用程序的体验，主要在Android和iOS设备上出现。

**01、 iOS和Android上的PWA网络钓鱼**

这种新型的网络钓鱼技术之所以能够实施，是利用PWA的工作特性诱导用户下载并运行恶意软件，而无需用户明确允许第三方手机应用的安装。

在iOS上，网络钓鱼网站冒充知名应用程序的登录页面，并指示受害者将PWA添加到他们的主屏幕。

在登录页面建立之前，某个威胁通过修改PWA的清单文件，使得PWA能够独立运行，并且其行为与普通的移动应用相似。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QmbJGbR2j6xysVJRYEicwI0bOHdQjWRja8ban1gdjKrxCabNPgRtzuSZA79UwZLz0G4Z5XzE9zUibYOHIS05WzQA/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

PWA工作原理的简化图

来源：ESET

在Android设备上，当用户在浏览器中确认了自定义的弹出窗口后，PWA会被安装。这会导致用户静默地安装Web Android包工具包（WebAPK）。

WebAPK是一种特殊类型的APK，即标准的Android应用程序文件，可以被视为PWA的升级版本。这种升级是因为Chrome浏览器从PWA生成原生Android应用程序。

**02、针对银行的金融欺诈活动**

在2023年11月，ESET观察到针对几家捷克银行、匈牙利OTP银行和格鲁吉亚TBC银行的移动网络钓鱼活动，在这些活动中，攻击者使用了一种特定的技术，并且这种技术是与标准的网络钓鱼传递技术一起使用的。

这些网络钓鱼活动使用了三种不同的URL传递机制：

语音呼叫传送：自动呼叫警告用户过时的银行应用程序，并要求用户在数字键盘上选择一个选项。按下正确的按钮后，将通过短信发送网络钓鱼URL。

短信发送：带有网络钓鱼链接的短信被莫名其妙地发送到捷克的电话号码。

恶意广告投放：在Instagram和Facebook等Meta平台上发布号召性用语的广告，例如为下载更新用户提供优惠。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QmbJGbR2j6xysVJRYEicwI0bOHdQjWRja3lbhVib8NIqw8CI4EKsjLMiac7bhnVibjPIErN1zJNHRkMoubhEJtkEAg/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

PWA 网络钓鱼流

来源：ESET

2024年3月，研究人员首次发现了控制网络钓鱼应用的C2服务器。服务器中的数据表明，3月之前可能并未运行。

根据C2服务器和后端基础设施的分析，研究人员得出结论，至少有两个不同的威胁行动者在操作这些网络钓鱼活动。

ESET目前已经通知了被这些网络钓鱼活动针对的银行。

原文来源：E安全

“投稿联系方式：sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176n1NvL0JsVSB8lNDX2FCGZjW0HGfDVnFao65ic4fx6Rv4qylYEAbia4AU3V2Zz801UlicBcLeZ6gS6tg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mrRug7icLIhX4EvNQjNgGRibia7K9qOLTR5PDfQiaUesU9xge7pnF8iciaxVC3JVkNqHA2pvQDnrM0hDVQ/0?wx_fmt=png)

网络安全应急技术国家工程中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mrRug7icLIhX4EvNQjNgGRibia7K9qOLTR5PDfQiaUesU9xge7pnF8iciaxVC3JVkNqHA2pvQDnrM0hDVQ/0?wx_fmt=png)

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
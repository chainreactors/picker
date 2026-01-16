---
title: 0117.我是如何发现 Google 表单漏洞的（重复内部漏洞 - 已修复）
url: https://mp.weixin.qq.com/s/TRJ79gWpK6ySL8eWSCNlfQ
source: Doonsec's feed
date: 2026-01-15
fetch_date: 2026-01-16T03:26:55.235358
---

# 0117.我是如何发现 Google 表单漏洞的（重复内部漏洞 - 已修复）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/yKTOKd3ibs980XSUEAxXyYOB9wUZ0R7Pt5iaJkaxPc8yic00Q4u059gwHWZqbVB7XXAzRK96QibmHpw0X8kDKnv8uw/0?wx_fmt=jpeg)

# 0117.我是如何发现 Google 表单漏洞的（重复内部漏洞 - 已修复）

原创

Qadhafy Muhammad
Qadhafy Muhammad

Rsec

![]()

在小说阅读器中沉浸阅读

本文章仅用网络安全研究学习，请勿使用相关技术进行违法犯罪活动。

声明：本文搬运自互联网，如你是原作者，请联系我们！

类型：Google漏洞

![](https://mmbiz.qpic.cn/mmbiz_png/yKTOKd3ibs980XSUEAxXyYOB9wUZ0R7PtHm9gbmlxxibaYDEYribCvGibia82FrulfdAiaQicNFFvMPgW6NRVXQyez8AA/640?wx_fmt=png&from=appmsg)

**Google 表单**是一款简单易用的基于 Web 的应用程序，用于**创建表单、调查问卷和测验**。它可以帮助用户：

* 高效地收集信息或反馈
* 实时存储和分析结果
* 与他人安全地合作

我于 2025 年 11 月 1 日凌晨 12 点 24 分发现了*谷歌表单*的一个漏洞。当时我只是在做实验，试图找到*谷歌产品*中的一个漏洞。这个漏洞是在*谷歌表单*中发现的，请问这个漏洞的具体情况是什么？

在开始之前，让我先向大家介绍一下如何控制*谁可以发布文件或表单*。我发现的问题*与编辑者可以更改权限和共享的*设置有关。您可以在这里找到有关发布权限工作原理的更多详细信息。

![](https://mmbiz.qpic.cn/mmbiz_jpg/yKTOKd3ibs980XSUEAxXyYOB9wUZ0R7PtmvTqa9XGEbibCUMSpEWuhia6qkJoT9VX1AqqQM3ZrWnkDegw92saeGXA/640?wx_fmt=other&from=appmsg)

https://support.google.com/docs/answer/183965?hl=en&co=GENIE.Platform%3DDesktop#zippy=%2Ccontrol-who-can-publish-a-file

概念***验证***

如果在编辑器视图中创建 Google 表单，并授予“拥有链接的任何人”访问权限，则编辑者在这种情况下可以执行两种操作：

1. 编辑者可以编辑、删除和发布表单。
2. 编辑者可以编辑和删除表单，但不能发布表单。

为什么这些条件会有所不同？
这是由于“*编辑可以更改权限和共享*”选项的*选中*或*取消选中*状态造成的。

![](https://mmbiz.qpic.cn/mmbiz_jpg/yKTOKd3ibs980XSUEAxXyYOB9wUZ0R7PtVibUB2UM50yMHhJzbpZQbFeo379kIUAg9Q6tECzYZs0CxzdannN8f1A/640?wx_fmt=other&from=appmsg)

从下图可以看出，当“*编辑者可以更改权限和共享*”选项未选中时，它属于第二种情况：*编辑者可以编辑表单，但不能发布它。*

![](https://mmbiz.qpic.cn/mmbiz_jpg/yKTOKd3ibs980XSUEAxXyYOB9wUZ0R7PtzJozr9qYSP6z3Hic8F6DhcfHG1jUMraUfQd8ARblLSrnqaWEwJUy4qQ/640?wx_fmt=other&from=appmsg)

取消勾选“*编辑者可以更改权限和共享*”选项后，我复制了我创建的 Google 表单的 URL。当我将其粘贴到另一个 Chrome 账户并尝试发布时，发现：

“表单所有者已禁用分享功能”，并且发布按钮也被禁用。这是因为 Google 表单的所有者取消选中了 *“编辑者可以更改权限和分享”选项。*

![](https://mmbiz.qpic.cn/mmbiz_jpg/yKTOKd3ibs980XSUEAxXyYOB9wUZ0R7Pt1efN3l0ibbetYpQo61W62D22iaeJj8wny2qLrhw9MwsUicTfCAqkAR27g/640?wx_fmt=other&from=appmsg)

我不是按钮的所有者，我该如何激活它？

![](https://mmbiz.qpic.cn/mmbiz_jpg/yKTOKd3ibs980XSUEAxXyYOB9wUZ0R7PtANM3BRF9BtqQXqJRrV0nqbPpaopXMXNECMqjvvDY16Q07bMibWibRS9w/640?wx_fmt=other&from=appmsg)

启用按钮其实很简单。我只需在浏览器的“检查元素”中将按钮元素从“禁用”更改为“***启用***”即可。这样一来，我就能够***绕过编辑者可以编辑和删除表单但不能发布表单的限制，从而即使我不是表单所有者***，即使发布按钮最初是***禁用的***，我也可以发布 Google 表单。

![](https://mmbiz.qpic.cn/mmbiz_png/yKTOKd3ibs980XSUEAxXyYOB9wUZ0R7PttOMHJB0sbu83ZibGE3JWYJ41NRxhicLeJlE0iaDQ9OYu1bDw6icjHUaLQg/640?wx_fmt=png&from=appmsg)

Google 关闭了此漏洞报告，我的报告状态也被关闭了，可能是因为引发了太多的争论。

我记得，11月6日这个漏洞还没修复，但11月7日下午，他们就修复了，而且没有通知我。是我主动跟进的，所以他们才回复了我。

对于 Google 表单的更新，现在任何拥有链接的人都可以编辑和发布表单，即使“***编辑者可以更改权限和共享***”选项***未选中或已选中***。

我的意思是，当一个 Google 表单处于“编辑者可以更改权限和共享”选项未选中或选中，并且任何拥有链接的人都可以编辑和发布该表单时，我认为这种修复方式有点奇怪。

> 验证视频
>
> https://youtu.be/TA-FHvXIgoU

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/yKTOKd3ibs98K2tqBAticMskicyUAjtQoicZSdgKiaj1G5KGKOyd7A6paRrrHhz2JVvU3RLRsboI6MibP7Nl68yVAyTw/0?wx_fmt=png)

Rsec

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/yKTOKd3ibs98K2tqBAticMskicyUAjtQoicZSdgKiaj1G5KGKOyd7A6paRrrHhz2JVvU3RLRsboI6MibP7Nl68yVAyTw/0?wx_fmt=png)

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
---
title: 0164.我是如何通过 XSS 和开放重定向发现账户盗用 (ATO) 的
url: https://mp.weixin.qq.com/s/D3FVRT6QtmaSVL9DZk8Bdg
source: Doonsec's feed
date: 2026-05-21
fetch_date: 2026-05-22T06:00:34.140746
---

# 0164.我是如何通过 XSS 和开放重定向发现账户盗用 (ATO) 的

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/MW9pCm89Bus2FwjeJIUiaZicyNq5mArJT5RiadFlXQImRGLZDXjKEhFCrlBh8Fcvj1SJnt3jcJy9PQ7xic0WVgiaRsx6PXJbcsGajqaA8YaKxmyI/0?wx_fmt=jpeg)

# 0164.我是如何通过 XSS 和开放重定向发现账户盗用 (ATO) 的

原创

JEETPAL
JEETPAL

Rsec

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

本文章仅用网络安全研究学习，请勿使用相关技术进行违法犯罪活动。

声明：本文搬运自互联网，如你是原作者，请联系我们！

类型：重定向、XSS

大家好，

今天，我想分享一下我发现通过 XSS 和开放重定向漏洞进行账户盗用 (ATO) 的经历。让我们马上开始吧！

因此，狩猎从随机选择一个程序开始，我们称之为 example.xyz. 这是一个加密平台。

我开始逐个枚举子域名，检查是否存在任何可能的子域名被接管的情况，但一无所获。

我使用 Wayback URL 从 example.xyz 获取之前的 URL，然后开始手动查找。我访问了注册页面并开始注册流程。在注册过程中，我注意到一个名为 callbackUrl 的参数。

```
https://example.xyz/sign-in?callbackUrl=
```

我决定使用开放重定向有效负载来测试这个参数。

```
https://example.xyz/sign-in?callbackUrl=https://example.xyz@evil.com
```

这个开放重定向有效。登录后，我被重定向到了 evil.com。但这还不足以达到更高的影响，最高可以达到 P3/P4，所以我决定测试 XSS。我尝试了多种 payload，但标签

```
<>
```

 都被过滤掉了。因此，我决定使用不同的 payload，例如：

```
javascript:alert(document.cookie)
```

这次成功了，我能够使用会话 cookie 弹出警报。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MW9pCm89Buu9ic1yVIO9SqAiaic26CvljGJPKAAT0GPCl9er57E2OmhDAZ8aCXOtHBEd2QCLHISsbYQG8kbQCdAaF1E3hibCzF5zdr1hGtPVutc/640?wx_fmt=png&from=appmsg)

之后我准备了一份报告提交给项目组。几天后，我收到了项目经理的回复。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MW9pCm89BuuxAqqo2mOlg0mXynZgdxVKfrUfqHic0Fk5mNYyDsQS9FrK4viaPib2BiblW3ibva4aeBfcxpYfvJAlNYBicnQicASaWPxjH0Fkiav63lE/640?wx_fmt=png&from=appmsg)

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
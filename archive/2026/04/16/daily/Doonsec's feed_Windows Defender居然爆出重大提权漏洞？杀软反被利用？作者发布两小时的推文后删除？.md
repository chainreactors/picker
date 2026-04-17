---
title: Windows Defender居然爆出重大提权漏洞？杀软反被利用？作者发布两小时的推文后删除？
url: https://mp.weixin.qq.com/s/ZRLkJi15du8ceOEoS8JM1Q
source: Doonsec's feed
date: 2026-04-16
fetch_date: 2026-04-17T04:47:11.821466
---

# Windows Defender居然爆出重大提权漏洞？杀软反被利用？作者发布两小时的推文后删除？

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/1ibFic8ns5ft4tywxnGO7SfTLdibM5sAnsmAicYvvnfx761wHNHvElM3l1DgibTgLiczydEmLQX2QQQEeWIHzNSodDGsYdypPNxB3b2MIrfIyDUw8/0?wx_fmt=jpeg)

# Windows Defender居然爆出重大提权漏洞？杀软反被利用？作者发布两小时的推文后删除？

kernel
kernel

Relay学安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

起初看推文的时候发现作者发布了一个Windows Defender的提权漏洞。

我刚将漏洞复现完，作者就把推文删了哈哈.....

![](https://mmbiz.qpic.cn/mmbiz_png/1ibFic8ns5ft7cBIyVib6vlCj6iaw9qkAVqIRb5ic31SNib3gpHocnMviajlGmJY09vWpraRTPeSSqMTNjAbuiaBIxLnYKNIkoib9J1Fc2AB290aDbFY/640?wx_fmt=png&from=appmsg)

好在POC还没删，POC还正热乎着。

```
https://github.com/Nightmare-Eclipse/RedSun
```

看到的大家快保存吧。

根据作者的介绍漏洞成因如下:

当 Windows Defender 意识到某个恶意文件带有“云标签（cloud tag）”时，出于某种极其愚蠢且搞笑的原因，这个本该保护系统的杀毒软件竟然觉得：**把这个它发现的恶意文件重新写回原始位置是个好主意。**

这段 PoC 正是利用了这种行为，通过劫持该过程来覆盖系统文件，从而获取管理员权限。

如下利用成功，需要注意的是利用的时候打开Windows Defender的实时保护即可。

![](https://mmbiz.qpic.cn/mmbiz_png/1ibFic8ns5ft5Q6xqFK39ticMQibopytm9KtkCdBicmMGFJYGSq14DBWib77dibgrbUFvTibyTlRhHxicAUL8PYdFgDM2QlmyoXvVVQxvovo911MtRhs/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/ia1z64qxm2mpPRMsd41M9uicNibC4x9CcHwRJtfuZbnD1wnhcWEjPFdlbfttC11glYMUlVdThSmtYDiadAtHzZx3Pg/0?wx_fmt=png)

Relay学安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ia1z64qxm2mpPRMsd41M9uicNibC4x9CcHwRJtfuZbnD1wnhcWEjPFdlbfttC11glYMUlVdThSmtYDiadAtHzZx3Pg/0?wx_fmt=png)

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
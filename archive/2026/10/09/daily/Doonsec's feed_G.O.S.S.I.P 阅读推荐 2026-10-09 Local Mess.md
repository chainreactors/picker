---
title: G.O.S.S.I.P 阅读推荐 2026-10-09 Local Mess
url: https://mp.weixin.qq.com/s/v_ZB_f3YDKn23YkQwJaFlQ
source: Doonsec's feed
date: 2026-10-09
fetch_date: 2026-10-10T07:56:14.058492
---

# G.O.S.S.I.P 阅读推荐 2026-10-09 Local Mess

# G.O.S.S.I.P 阅读推荐 2026-10-09 Local Mess

原创

G.O.S.S.I.P
G.O.S.S.I.P

安全研究GoSSIP

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

10月的第一期阅读推荐，我们来给大家介绍2026年USENIX Security会议的Distinguished Paper Award Winner论文——*Bridges to Self: Silent Web-to-App Tracking on Mobile via Localhost*

![](https://mmbiz.qpic.cn/mmbiz_png/eQ0Wf6rqolUic1OVZtcg2nhsfMOnH2C8WJXQPD1ke7nmibtSbF0mia8u9HVXV2uicskGyKFaibKZxM0qWGpHtJ65ocrJrVianr01RV2f9Z8vQLIMk/640?wx_fmt=png&from=appmsg)

大家还记得【[G.O.S.S.I.P 阅读推荐 2025-06-06 127.0.0.1 窃听风暴](https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247500229&idx=1&sn=88babd5c24e47474dab239b716401442&scene=21#wechat_redirect)】这篇文章吗？今天的论文推荐其实就是当时的研究工作的后续：来自西班牙、荷兰和比利时的研究人员（去年我们还在羡慕他们的男足国家队，今年我们已经在羡慕他们的男足国家队在世界杯上取得的好成绩了）把研究成果投稿到了USENIX Security 2026（并且拿奖拿到手软，如下图），那让我们具体关注下论文里面有什么更为重要的细节。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eQ0Wf6rqolW8eP1miaDLQWxKibDBiaR4l7fWNiaoyoxhuoicsELJOWsyRgFfXaRUO8nhJlYJLPtOGic1fM5Iy39SYRvORqdjAjKwSP228BmezOeE8/640?wx_fmt=png&from=appmsg)

首先还是回顾下这项研究：在Android平台上，让一个拥有`INTERNET`权限的APP在本地网络地址（也就是127.0.0.1或者就叫做`localhost`）的特定端口上提供服务，然后让**浏览器上运行的脚本和`localhost`的这个端口进行通信**，由于`localhost`在浏览器的同源策略访问控制中一般来说默认是可信的，网站上的脚本就可以通过`localhost`特定端口去获取手机上的APP发送的信息。

![](https://mmbiz.qpic.cn/mmbiz_png/eQ0Wf6rqolXTS5C36I5sIZK8vjQuialEy5iaSK6PNpVs7ibjLATsDEQNIYfwichOVv0kgdKBXtcIduBZww0OXrBAKs0rMcvARa0D3xrPcYod8Eo/640?wx_fmt=png&from=appmsg)

这种通信模式带来的问题是什么呢？研究人员发现，Meta和Yandex这些美国和俄国的互联网大厂让旗下的APP（包括Facebook、Instagram、Yandex Maps、Yandex Navigator、Yandex Search、Yandex Browser等）偷偷在本地Android系统上通过`localhost`特定的端口提供服务，另一方面则通过各种手段让许多第三方网站的网页集成他们开发的JavaScript脚本（Meta Pixel 和 Yandex Metrica）。这两件事情完成之后，当用户访问某个第三方网站，**这些脚本就会立即尝试和本地特定端口通信**，通过APP提供的数据来打破浏览器的种种隔离和匿名化防护，获得大量用户的隐私数据！

![](https://mmbiz.qpic.cn/mmbiz_png/eQ0Wf6rqolV1RUDBpOVT63sQ2sh928Gpa8gCnWsbnribAp9miacYMAmdzSdv8XM7JveZL3A9ZBicXibiaxFIfzD0jj6qR0ooH2y4vJy3h9mmA1y0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eQ0Wf6rqolWLESmBrOn7Vr25LzA3mb9579mWSXxrvK1omXdj6HDrs6c7a3UkHKtBnibM4IN4yyDr3SStZiaPa3OQUibvz0TVickGicnsF5zmwY0o/640?wx_fmt=png&from=appmsg)

这里面最搞笑的一点，是Yandex Metrica脚本通过和`yandexmetrica[.]com`这个域名通信来欲盖弥彰，因为Yandex在DNS解析记录里面把域名的解析记录指向127.0.0.1，然后Yandex还在自己的APP里面把`yandexmetrica[.]com`对应的证书也放进去了，在APP里面启动了一个迷你版的TLS服务器，让脚本显得好像是“通过和`yandexmetrica[.]com`进行TLS通信”，而实际上是和本地的APP进行通信。可是，可是，你在本地启动TLS服务器你就得把`yandexmetrica[.]com`的私钥放在本地啊……攻击者只需要拿到对应的APP就提取到了`yandexmetrica[.]com`的TLS证书私钥……

当然还有个很重要的问题——为什么在iOS上没有发现同类问题（从技术层面上此类问题也应该可能存在于iOS平台），作者对此进行了一些推测：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eQ0Wf6rqolVaG5VtJxY4QeHoJa9yDYkzLRnZ7NQjXrCjrHCPI37vqD9wIREaddU7VppH3WesnmicG3VbdvhHsQ5A0B2O4OV5ysfAbEK06kW4/640?wx_fmt=png&from=appmsg)

当然，我们还是会很好奇，这个研究只是针对了欧美进行了调研，那神秘的东方到底有没有类似的安全问题呢？

---

> 论文：https://www.usenix.org/system/files/usenixsecurity26-vlummens.pdf

预览时标签不可点

不喜欢

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EibxMcqx9KdafugxDicBiaW3cb1gyTuWooDCJjH1ibu8aibOiapYLq8BJMwNbIeUK1t0japdvmdqTfCxhg/0?wx_fmt=png)

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
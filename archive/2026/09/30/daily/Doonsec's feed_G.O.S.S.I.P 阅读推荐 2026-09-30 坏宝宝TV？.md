---
title: G.O.S.S.I.P 阅读推荐 2026-09-30 坏宝宝TV？
url: https://mp.weixin.qq.com/s/3BlX41yc5gjHaVfWzIa5OQ
source: Doonsec's feed
date: 2026-09-30
fetch_date: 2026-10-01T07:56:48.639750
---

# G.O.S.S.I.P 阅读推荐 2026-09-30 坏宝宝TV？

# G.O.S.S.I.P 阅读推荐 2026-09-30 坏宝宝TV？

原创

G.O.S.S.I.P
G.O.S.S.I.P

安全研究GoSSIP

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

国庆假期马上就要到了，大家是出去人挤人还是宅在家里面刷手机呢？不知道有多少人会在家里面看电视度过国庆佳节，这种假期模式可能已经是30年前的时尚了。不过智能电视的出现，或多或少又给大家提供了一些回到大屏幕（相对手机小屏幕）面前的理由。今天我们介绍一篇DIMVA 2026的研究论文，作者在文中对东芝、三星和LG的智能电视以及相关的HbbTV（混合广播宽带电视）机制的安全性进行了分析：

![](https://mmbiz.qpic.cn/mmbiz_png/eQ0Wf6rqolWJgTmtSjRYlV2EJXj3tic73Qn4wiciaQO6SZJ22RwKOzxvPpiaWibiaYTMPod3fNIdibwND7htrO8PfzXzbvJMGeqgTSZPV7bHdfFefc/640?wx_fmt=png&from=appmsg)

这篇论文的核心研究内容针对的是HbbTV（Hybrid Broadcast Broadband TV，混合广播宽带电视），一个从2010年开始就制定的标准，它的特点是把传统的电视广播信号传输和现代的网络数据传输结合在一起，而且**HbbTV 不需要在本地安装应用程序，因为数字内容已经成了电视信号的一部分**（~~这样就更方便在电视信号里面插入广告了~~）。目前HbbTV协会已经有了很多成员单位（下图里面你知道多少？好像除了Amazon、BBC和几个电视厂商以外，就没几个认识的了）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eQ0Wf6rqolW1fcBw8TSKbKqxUzqF5mUOedoyxtsHXxKEOoQnvTQ8yiaawHqHu1iaDH7W3quZib5A8YjqBgnwteVkVuJVTINBCq16WOPKmONk3s/640?wx_fmt=png&from=appmsg)

为了支持“不安装APP就~~投放广告~~支持数字内容”的特性，HbbTV要求提供两组API（当然都是需要和智能电视厂商深度结合），一类是针对智能电视的浏览器的特定的JavaScript API，另一类是HbbTV本身的管理API，包括Application Management API、Configuration and Settings API和Media Playback API。当然，引入这些API必然也会引入相关的风险，G.O.S.S.I.P早在2022年就指出过这类问题——【[G.O.S.S.I.P 阅读推荐 2022-10-14 EvilScreen](https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247492914&idx=1&sn=52403a2177409a69c74574c49ccaee5a&scene=21#wechat_redirect)】，而直到今天仍然还存在大量API的权限检查不严格的情况。攻击者利用这些接口，可以实现DoS、内容篡改、钓鱼等攻击，也可以把智能电视变成跳板，来攻击同一个局域网内部的其他设备：

![](https://mmbiz.qpic.cn/mmbiz_png/eQ0Wf6rqolX2Fk0BpRwcOHodCPX1hk5x0GKHL5ibaFctd3vpsSRsjGmr8uDgWUuL5sFqTLRmCpa8JdAjl9OQUzjiaQxLQdfVibklFyy3GNxsTA/640?wx_fmt=png&from=appmsg)

作者在论文第六章里面具体介绍了如何基于HbbTV的特性来对智能电视进行多种实际的攻击。在第一种攻击中，由于HbbTV本身是支持基本的电视信号的，那么攻击者可以利用电视信号（DVB stream）这一路缺乏认证的特点，伪造视频流注入，让智能电视播放恶意视频哈哈哈。而第二种攻击则是利用了支持HbbTV的智能电视能够接收一个HTML文件并且运行（只需在header中把Content-Type设置为`application/vnd.hbbtv.xhtml+xml`）的特点，给智能电视注入一个恶意HTML然后把它变成web server加以控制。不过这两个攻击的具体细节在论文中并没有详细介绍，作者只是给了一个HbbTV Attack Toolkit（开源，https://github.com/SecPriv/HbbTV-attack-toolkit 可获取代码）

作者实际评测了Toshiba TV（2021，运行Android系统）、Samsung TV（2017，运行Tizen系统）和LG TV（2024，运行webOS系统），发现这些电视的最大问题首先是里面的浏览器非常古老，比如Toshiba的电视用的是Chrome 55.0.2883.91（问题是谁叫你测试2021年的电视啊……），而且它们的最新固件也基本上就停在Android 11这种 ~~霍乱时期的爱情~~ 疫情时期的系统（2020年发布），所以对它们进行攻击基本上是水到渠成（如下表）：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eQ0Wf6rqolV1aAECNhyCibyfKxgn4daTcRLrHHcHaE7LMZc9aTDaPdqEoIicbUMia2SjMcbYIXeWiakSrMESceuaptMcthAE7tvsB0abXdE1opM/640?wx_fmt=png&from=appmsg)

最后，不得不感叹在欧洲做安全研究就好像木心先生的那首诗《从前慢》

*记得早先少年时
大家诚诚恳恳
说一句 是一句
清早上火车站
长街黑暗无行人
卖豆浆的小店冒着热气
从前的日色变得慢
车，马，邮件都慢
一生只够爱一个人
从前的锁也好看
钥匙精美有样子
你锁了 人家就懂了*

祝大家有一个愉快的国庆节！

---

> 论文：https://martina.lindorfer.in/files/papers/hbbtv\_dimva26.pdf

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
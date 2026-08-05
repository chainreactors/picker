---
title: 拆解 SecOC：安全报文如何生成？新鲜值、同步报文工程要点
url: https://mp.weixin.qq.com/s/ymfADddQGLNIqWAlY-g6XA
source: Doonsec's feed
date: 2026-08-04
fetch_date: 2026-08-05T04:55:32.754529
---

# 拆解 SecOC：安全报文如何生成？新鲜值、同步报文工程要点

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaDIiakN55zLGiaYW4VsEUo1csFf6gAnhSkkjeFnJNL80NOtBrYibdtibVTlYibbAo5KfCib086wlgRQwzAt8JqYzNk4JwYQN4FsEGo44/0?wx_fmt=jpeg)

# 拆解 SecOC：安全报文如何生成？新鲜值、同步报文工程要点

谈思实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaAf3Eh4RynoftF7dz1NtAd2SYNXWsm8EaWOewRjSXxcCjicH0t59JtNOypwHKjHNlxV8CeJft7puVrzuEzoHibdHGKJ2Bhcc4iajI/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247575811&idx=2&sn=55c140dd2df955df133478463dd59bbf&scene=21#wechat_redirect)

**01**

**SecOC模块介绍**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaBoBibbFicUzTl3Hia7ozDDDvuw8SxCuI44xkrG2C6seRwbf2d12Libgfvoj0XXibDa9FpF5yX2lzSsiabAh4HamA59ZAO826iawpoXmw/640?wx_fmt=png&from=appmsg)

Integration of the SecOC BSW

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaCkrhs75V2xuVEiaFkBU2GZbfiaWx4CbLY7l2QdKmjT4FdcVxDYCCy9ljZyzehYx81txtvM8zicU1RWGGaBCicn5oZNdAZG8OArQCc/640?wx_fmt=png&from=appmsg)

Transformation of an Authentic I-PDU in a Secured I-PDU by SecOC

从图上可以看出SecOC模块与PduR模块进行报文信息交互，同时调用CSM模块进行加解密。

**1.1数据流分析**

**1.1.1数据接收**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaCFStIKHrnK22npxctpfBFEW9oHTI5zjZW3yxKructqLLFySXaPWIuotAeYWmoqAYG6FQgRdAwSQhwicIyxjTLTiahVU0fg4rGVQ/640?wx_fmt=png&from=appmsg)

以CanIf接收为例，CanIf收到报文后，调用PduR\_CanIfRxIndication通知到PduR,PduR随后调用SecOC\_RxIndication将原始数据传给SecOC模块，当SecOC模块校验完成后，将校验结果和处理过后的数据再次传递给PduR模块。

**1.1.2数据发送**

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaAyacn8kNYnJyDURH7ibEydPDbLh5npEmlc42WMic3SRvytUib0Ar2KpSYgABVKWMXZAHlWq8XcbyTKgBOqgcj71geKg8lZeHzeOM/640?wx_fmt=png&from=appmsg)

以CanIf发送为例，Com模块调用PduR\_ComTransmit准备发送报文，然后PduR模块通过SecOC\_Transmit对需要发送的数据进行处理，然后通过调用PduR\_SecOCTransmit将处理后的数据发送给PduR模块，这个时候PduR模块就可以通过CanIf\_Transmit将数据发送出去了。

**02**

**Pdu组成**

上面我们说过，SecOC模块会对数据进行认证+Counter，因此其Pdu内容的组成肯定与普通报文不同。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBKqmYh5lz1zkJjxfJCHRUO5NNibN3Hfic4NziabWojSVuObSnaj0qS3rEDeh0lQUy4YTInGVm93rMhjtMVKLEsNoo9nTmc4tQcwI/640?wx_fmt=png&from=appmsg)

Secured I-PDU contents

从上图可以看出Pdu的内容由原数据+新鲜值+认证信息(如MAC)组成。

**2.1 新鲜值(Freshness Value)**

**2.1.1 新鲜值的介绍**

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBLWttXl7Y6v7QqM5Kic99LhAFytibNrnw2eYCSMDwaEnegqShMTMKjeicicUvthDhQqo842z0AHFGhft4ufzcVC2jr64hxb7Oj7wk/640?wx_fmt=png&from=appmsg)

由上图可以看出新鲜值由：trip counter、reset counter、message counter、reset flag组成，各个部分的含义如下所示。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaA3xXZRV54ExMArMiaX6OhxUsIUwnIUvicbl3kkp5SVLTVkKoGczpNPPHmhZfvM8m2H0Mog7AickGIgRoHT7sPHxsokmQEpVbf8YQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaAyhAUvllK2TtGGGSLNVfGTZGKYRzctsmfElhzxfIIwmLQOdRkmW2DqyC90VOaN442IpCgjEhotcquqGMlUEfCBrohvWlExP6c/640?wx_fmt=png&from=appmsg)

Behavior example of freshness value (TripCnt, RstCnt, MsgCnt, ResetFlag)

对于主节点来说

1. 在上电的时候TripCnt增加了1，随后本次上电周期保持不变;
2. ResetCnt在TripCnt增加的时候复位，然后周期性增加

对于从节点而言

1. TripCnt在接收到同步报文后发生变化，其值同步到和主节点保持一致，随后本次上电周期保持不变;
2. ResetCnt在每次收到同步报文时都同步到和主节点保持一致。
3. MsgCnt在每次成功发送报文后增加，同时在RstCnt增加的时候清零。

**2.2 同步报文**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaCynWGqhSOG6NXWKibkgylhJuNx0NG9micUWwtPMMzbia99JwneRnw6viaZQWYwX7aUTiaB6RYwcFLxuSiaCIRQKOoXdwicd0l8cqSDSE/640?wx_fmt=png&from=appmsg)

Format of the synchronization message (TripResetSyncMsg)

同步报文也是需要添加认证信息的。

**2.2.1 主节点的处理**

主节点上电后从NVM中读取到上次的值作为TripCnt初始值,同时设置ResetCnt为1.当TripCnt增加的时候，FvM模块会调用NvM模块将变化后的TripCnt存储到EE。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaA7gwhM15LVWzhqnBYjZEOyia40uSoaR2Evow3Yt5XkRPs723yX24myCGVpcPX0lXqhkw8rXgeCV369E6Gq1jfhtCCAXcjRp5b0/640?wx_fmt=png&from=appmsg)

Transmission Timing of Synchronization Message

**2.2.2 从节点的处理**

从节点上电后也通过NvM模块读取上一次的TripCnt值作为初始值。当接收到同步报文后，需要进行对同步报文中的新鲜值的数值的大小进行校验，校验通过后，再进行信息安全校验，校验通过后更新从节点的值。关于数值大小校验一般是如下几个条件(具体项目参照不同的OEM的需求)：

* 同步报文中主节点的TripCnt值大于从节点的TripCnt值，此时校验通过;
* 如果条件1不满足，那么需要满足从节点的TripCnt和同步报文中的TripCCnt的偏差在一定范围内，那么认为也是校验通过的。

**2.3 实际报文中对于新鲜值的裁剪**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaDpPN3ye5TcblWtnIXQIOG0p87cFX9HBJ5nSRKw5ibJ4kI4yvDwUqvtUiaccyzx8vI5F7ic8Kpz7gy1ztciaup1tvSiaagkbp6JUq54/640?wx_fmt=png&from=appmsg)

由于新鲜值和MAC都很长，而目前常用的CANFD最多也只能传输64个字节，因此为了提高数据的传输效率，需要对新鲜值和MAC值进行截断填充到报文中，具体报文的的定义跟随项目定义。

**2.4 同步报文的发送时机**

如上所述，主节点在上电初始化后就要尽快发出第一帧同步报文，然后周期性发送报文。但是假如从节点由于如busoff等掉线后又重新恢复了，此时怎么办呢？它要一直等着主节点发送同步报文么？当然不是，一般当从节点启动后(具体看整车厂要求)，如果在给定时间时间内没有收到同步报文，那么就要主动发送同步请求报文。当其从busoff恢复后，也是同样的道理。同步请求的报文一般是不需要加密的，具体可参见各个项目的要求。

来源：汽车电子嵌入式软件分享

**end**

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJlH8rNickiaaHhLM4PaibcicFO9usS5xIOrWYjZibuvwV8g9DwnI6xZ4RvHg/640?wx_fmt=jpeg&from=appmsg)

**谈思汽车媒体门户**

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9hgqzDyib0J4ico1LVFEZ2QnqGKQhnxdoZeiaZAHaGnnTnFGDvlfibtd8h389z8H20gh1icn8yhxrx8yw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkyODQzMDI3Mw==&mid=2247549590&idx=1&sn=b5ea25965c057d1ca2913d900f77799d&scene=21#wechat_redirect)

**精品活动推荐**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaAI8KMQg42koBCmQ8xCYRUVtiaem7dsJtOqV3DGOX6iaYEHyxflLz2KpKog3fHia0MOsJl0uRNIdyy32iaibZKpdT4LKv907eGCWcdA/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247572036&idx=3&sn=2410465a682d6b6c1f8b801eb583cdae&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaAf3Eh4RynoftF7dz1NtAd2SYNXWsm8EaWOewRjSXxcCjicH0t59JtNOypwHKjHNlxV8CeJft7puVrzuEzoHibdHGKJ2Bhcc4iajI/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247575811&idx=2&sn=55c140dd2df955df133478463dd59bbf&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaA7BGa1vwHmHNlluBv83nX42cOwngUmsgRicQ6oyhxN3HmOsFIml2sUM8Yibk5GELQqiaFLt2dVzmf01r90xrW0vMWGpJX7zOsmkM/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247575659&idx=3&sn=1b3acb3a33e0fc992b67b37bc4d04a0e&scene=21#wechat_redirect)

**AutoSec系列沙龙**

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkP4bDWQkLJvELA6L8vJsCRctQMTiasyhKEkb1ujgIjlGBVx91jbsQ29g/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247548574&idx=1&sn=11f37456b4f45c0fdbf795c21e201c03&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkO7zMw9U0oRCldUrRpcKyGwogwoUbpTJXic56yibibZ6Wqzr6C2P6iaFJWQ/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247551934&idx=2&sn=50785b76c512a88b30455fc1e8fa188c&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkVh6Z43iczWWhmnKMicdo0WU9VCzDFa2N2eiaJIogkxsLEEFt8wJ6W0CUA/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247557132&idx=2&sn=2e44d4c2d77a2eec377d0553442d2c1b&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw80qwJ0DQGXJ8KiakP0yVicGI8mlMKIokicyytiaYrN6BIBOybqkYX7KSXwbia50cic232dG7BnYibKqHasA/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247561775&idx=1&sn=948a9e7f8d4fbed363c6a6a5479cd39e&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkfxA4GZice84BsCR4zGV0oqJXpEjUsUpGKcFcCx1BiaDYDQU4cT3nTtpA/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247561260&idx=2&sn=0ca6395502487515a921f32288b7e8df&scene=21#wechat_redirect)

**专业社群**

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJnASqAJY7fLYIeMGl8fHu4aPXusCVuX2qAYkrb9bQMRGEBvSghHETaQ/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247535223&idx=1&sn=e30e07a44accd5b0e9ada3d8b537f977&scene=21#wechat_redirect)

**部分入群专家来自：**

**新势力车企：**

特斯拉、理想、极氪、小米、零跑汽车、阿维塔汽车、智己汽车、小鹏、岚图汽车、蔚来汽车、吉祥汽车、赛力斯......

**外资传统主流车企代表:**

大众中国、大众酷翼、奥迪汽车、宝马、福特、戴姆勒-奔驰、通用、保时捷、沃尔沃、现代汽车、日产汽车、捷豹路虎、斯堪尼亚......

**内资传统主流车企：**

吉利汽车、上汽乘用车、长城汽车、上汽大众、长安汽车、北京汽车、东风汽车、广汽、比亚迪、一汽集团、一汽解放、东风商用、上汽商用......

**全球领先一级供应商：**

博世、大陆集团、联合汽车电子、安波福、采埃孚、科世达、舍弗勒、霍尼韦尔、大疆、日立、哈曼、华为、百度、联想、...
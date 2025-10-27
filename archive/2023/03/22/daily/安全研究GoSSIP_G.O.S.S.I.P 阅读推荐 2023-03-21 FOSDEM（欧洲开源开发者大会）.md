---
title: G.O.S.S.I.P 阅读推荐 2023-03-21 FOSDEM（欧洲开源开发者大会）
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247494611&idx=1&sn=116a45210e1b8dcf17ff5a16026ea7d7&chksm=c063c50af7144c1c99db1ca7306e1512c4f85398a8686527069a48c82dffd7443f5ab8243c95&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2023-03-22
fetch_date: 2025-10-04T10:16:12.158494
---

# G.O.S.S.I.P 阅读推荐 2023-03-21 FOSDEM（欧洲开源开发者大会）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/uicdfzKrO21EFs4oPbkiaibdOlEwss031f4Lm1tBO3rib0Ujziaw8uq71x0iaGBg07XAic4pIxLaLLlXkC2ibXSTge7Vmw/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2023-03-21 FOSDEM（欧洲开源开发者大会）

原创

G.O.S.S.I.P

安全研究GoSSIP

今天脱离学术圈，去工业界看看一些生产实践内容（趁着AI还没取代码农）。我们要围观是2月初在布鲁塞尔召开的欧洲开源开发者大会（Free and Open source Software Developers’ European Meeting，FOSDEM）

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EFs4oPbkiaibdOlEwss031f4ZcU9ichxDJP4URe23JkBNibQUEGdm1p5cGwUYWDSxkuzGwJZ1SUn5oDQ/640?wx_fmt=png)

作为一个工业界主导的开源活动，在FOSDEM上能够看到很多可能是学术研究社区觉得不那么“novel”但是非常实用的内容，而且丰富多彩（实际上整个活动召开期间一共有35个房间用来召开各种议题、讨论），比如庆祝“开源”这个名词诞生（1998年2月3日在加州Palo Alto会议上确定使用open source而不是free software）25周年的talk (https://fosdem.org/2023/schedule/event/celebrating\_25\_years\_of\_open\_source/)；介绍NASA中开源项目使用的talk (https://fosdem.org/2023/schedule/event/nasa/)，大家都熟悉下面这幅图里面的传奇女程序员玛格丽特·汉密尔顿吧！

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EFs4oPbkiaibdOlEwss031f4ibY7ChzQR1a9ibEaxvMsT4SzrtLZDpiaKzSQ28Unia2Wxm3OsyedZDE7ibg/640?wx_fmt=png)

---

整个FOSDEM主题非常多，我们不可能一一介绍，大家可以访问下面的网址去选择自己感兴趣的内容。这里面有非常多计算机系统和安全相关的session，我们来走马观花地看看。

> https://fosdem.org/2023/schedule/rooms/

首先介绍的就是Security track (https://fosdem.org/2023/schedule/track/security/)，这个track里面从偏密码学的Elliptic curves in FOSS (https://fosdem.org/2023/schedule/event/security\_elliptic\_curves\_in\_foss/) 和Kerberos PKINIT: what, why, and how (to break it) (https://fosdem.org/2023/schedule/event/security\_kerberos\_pkinit/) 到偏实际代码安全的IntelOwl Project (https://fosdem.org/2023/schedule/event/security\_intelowl/) 和 Where does that code come from? (https://fosdem.org/2023/schedule/event/security\_where\_does\_that\_code\_come\_from/)，大家可以各取所需。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EFs4oPbkiaibdOlEwss031f48r8PQJ5cqFCrhxs40wiceaNm6Nv8H33vpzMaFMDeCwuFZK7qxSDI4SA/640?wx_fmt=png)

接下来带大家去看的是机密计算（confidential computing）track (https://fosdem.org/2023/schedule/track/confidential\_computing/)，可以看出来这个方面是最近的热点，里面有非常多的主题（两天的活动时间都排满了），关注TEE、SGX等研究内容的小伙伴必须围观：

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EFs4oPbkiaibdOlEwss031f4gicvxWMumzAO1T4ncdvjyyLveZRUegWG4uRWFyFyniaESHd8amMZrOCA/640?wx_fmt=png)

---

在Kernel、Microkernel和底层的Bootloader方面，本次活动有三个track：

* Kernel devroom (https://fosdem.org/2023/schedule/track/kernel/)
* Microkernel and Component-based OS devroom (https://fosdem.org/2023/schedule/track/microkernel\_and\_component\_based\_os/)
* Open Source Firmware, BMC and Bootloader devroom(https://fosdem.org/2023/schedule/track/open\_source\_firmware\_bmc\_and\_bootloader/)

这里面要着重推荐一个Don’t blame devres - devm\_kzalloc() is not harmful, Use-after-free bugs in drivers and what to do about them (https://fosdem.org/2023/schedule/event/devm\_kzalloc) 的报告：

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EFs4oPbkiaibdOlEwss031f4Dm5ENAZc1WbdiaPViazd42CC7lluZ9oia5PoIvug2vCPtCVeQsCq9KqFA/640?wx_fmt=png)

---

最后要给大家介绍三个工具开发的track：

* Binary Tools devroom (https://fosdem.org/2023/schedule/track/binary\_tools/)
* LLVM devroom (https://fosdem.org/2023/schedule/track/llvm/)
* Emulator Development devroom (https://fosdem.org/2023/schedule/track/emulator\_development/)

在binary tools这个track里面，很多工具都被知名Linux网站LWN推荐（详见 https://lwn.net/Articles/924133 的介绍），同时也有知名的逆向分析工具Radare2这个项目的开发历程和下一步展望的 The state of r2land (https://fosdem.org/2023/schedule/event/bintools\_radare2/)

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EFs4oPbkiaibdOlEwss031f4L33G2qm2QsmH2bkyuWc2VUvibx6ngNhNrYgzpY2ZiaichekgRCvDvJOdw/640?wx_fmt=png)

但是编辑部的私人喜好里面，却强烈推荐给大家的是模拟器开发这个track里面的内容，因为实际上emulator开发是非常体现极客精神的一种活动——对古老的计算平台的复原，让现代计算机能够运行那些历史上的代码，是不是有一种上帝的感觉！

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EFs4oPbkiaibdOlEwss031f4e42Sw9z5gFCJWG1t46qpR6pFGJ6ib8bKMcLWh2At8HhPbGibtubgs0Qg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EFs4oPbkiaibdOlEwss031f4CZILuic2tGickC0cVfiamvSXrsYUxRHCibpiaFv3mXuu12zel9Wx10y6cXw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EFs4oPbkiaibdOlEwss031f4daCicH5qPE7buoibRIwWvLcCZyrEJiaB17uOnVYkt3PuiaKtpKq3go8u2Q/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EFs4oPbkiaibdOlEwss031f4ZricIvOatbQXBlznPy9GhNvSQ7L0iasuCoSRWtdUzIQuR0OvwFFSDuyQ/640?wx_fmt=png)

欸呀呀好喜欢这种开源的氛围，希望开源社区在下一个25年能够发展得越来越好！！！

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EibxMcqx9KdafugxDicBiaW3cb1gyTuWooDCJjH1ibu8aibOiapYLq8BJMwNbIeUK1t0japdvmdqTfCxhg/0?wx_fmt=png)

安全研究GoSSIP

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
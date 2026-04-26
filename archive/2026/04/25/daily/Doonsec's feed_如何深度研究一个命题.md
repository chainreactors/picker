---
title: 如何深度研究一个命题
url: https://mp.weixin.qq.com/s/RpOdV_2tIckA1HcfSr3agQ
source: Doonsec's feed
date: 2026-04-25
fetch_date: 2026-04-26T05:02:26.164236
---

# 如何深度研究一个命题

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/LjdkpgSF7Pck0KU9JqsxLvQqRzOqNvygvWElhdyGckGjnIfR3bzGEH5KSBDsXbTuVyribuA9YPd9hEWJiaich5d8Q24LGqRp99Y803jWibxAun8/0?wx_fmt=jpeg)

# 如何深度研究一个命题

原创

hyang0
hyang0

生有可恋

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

之前介绍过**横纵分析法，是使用AI skill研究问题的方法。**

[使用横纵分析法进行深度研究](https://mp.weixin.qq.com/s?__biz=Mzk0MTI4NTIzNQ==&mid=2247497671&idx=1&sn=cfc81d91b13ff4501cfc30487b782f64&scene=21#wechat_redirect)

很多AI工具都出了以深度研究为卖点的功能。比如早期的chatgpt、grok3都推出了自己的深度研究。目前grok4比较拉，页面也看不到深度研究入口了。同样我们以一个题目进行探索，比如要研究“系统高可用设计标准”。

首先试试 chatgpt 的深度研究工具：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LjdkpgSF7Pd1d7VKQpOnNcmu9s9rS65V80FSQQXDUrPe17cxbCOhGWzBXiaGqoJhiaomQueafica3tpvPQRnFrhyerFOabob5CeEYgs3OHkObY/640?wx_fmt=png&from=appmsg)

深度研究提示词：

系统的高可用有哪些设计标准？高可用设计核心原则是什么，有哪些度量标准？如何落地。

![](https://mmbiz.qpic.cn/mmbiz_png/LjdkpgSF7Pcv2LpX42wnLxicYZC1Q5cd7icFwuUgsQic2S6ksTgpsUHNSIfzso40SicMo8SELkZqj8FPic8BTZwcibYUCVpL5l0kHQN4Vib7hZxW18/640?wx_fmt=png&from=appmsg)

等待的同时，也可以让 Qclaw 试试。目前 AI agent 的研究能力普遍比原生的模型要强，如果你在模型中问不出你想要的就应该试试使用 AI agent。这里没有调用**横纵分析法 skill，直接使用QClaw原生的web搜索功能。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LjdkpgSF7PdaeTicfWbVl9C2ZCuJicWADgAKoyrxeW5xMbeZpGH7A3Uv3vljkeQv06jibB0rBkGuZcTXaDj46cDj8F8vyBsKft8MgbtYuHz3yE/640?wx_fmt=png&from=appmsg)

当报告出来后，你还可以让 agent 将参考的文献内容下载下来。

提示词：

系统的高可用有哪些设计标准？高可用设计核心原则是什么，有哪些度量标准？如何落地。以 markdown 格式出一份研究报告。

参考的文章内容，下载到 ha-design 项目目录中

如果 token 用爆了，可以切换到自己的 coding plan，我用的是火山的 coding plan，每月¥39，现在内置 glm-5.1，比较顶。推荐火山模型没有什么好处，它的消费券不能叠加，邀请码没什么用。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LjdkpgSF7PeksIPWO82cVUjm2icfkynEgZLMOQSBjT7sV6jiacC8sLcf4vRp2T1Pe8Ij7zTzu8SicgcNmrfgq06TsofLdNqVxDWtghsuH0MpWU/640?wx_fmt=png&from=appmsg)

关于高可用的文献：

* **JavaGuide《高可用系统设计指南》**
* **CSDN《教你读懂高可用/SRE》**
* 字节跳动《异构场景下的高可用建设实践》
* Microsoft Azure《可靠性目标定义策略》
* 阿里《高可用架构建设实践经验》《阿里云卓越架构框架》
* `Google SRE Book` 书籍版权原因没有下载

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LjdkpgSF7Perxljpyh3EukHsFJo0e4HUUQjU5hIzhTGB4Bx2WLGtW7HGibfknZnLjpnB6dDjicNVW6ySfLMVmQsSuCTwJLVqLA08DDznrYthM/640?wx_fmt=png&from=appmsg)

chatgtp 的深度研究号称是博士级别的研究能力，发起请求后可用不用一直等着。chatget 研究完后后可以查看分析报告，并将报告下载下来。

深度研究历时22分钟，引用35篇文章，对于做研究或写稿的人来说还是很有参考价值的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LjdkpgSF7PeH3WdEtpVZS6t5efR2YuGEAdOib4xfyUgDjxOgwQJNcekssp4TZiaQTraBvNOAOWwjzhKlzyLtE3RptQ0y9TK8sGK67G4SIRrBs/640?wx_fmt=png&from=appmsg)

全文完。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/ulAibOLeecVtlibejT79OV1CEtDxRdopU4ZpHTLW4EDibaYb0p30STPSN6c6ZLX3qIB67IrbuElJkFgNRJfW1Fg3g/0?wx_fmt=png)

生有可恋

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ulAibOLeecVtlibejT79OV1CEtDxRdopU4ZpHTLW4EDibaYb0p30STPSN6c6ZLX3qIB67IrbuElJkFgNRJfW1Fg3g/0?wx_fmt=png)

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
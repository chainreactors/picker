---
title: SDC2024议题聚焦 | Rust 的安全幻影：语言层面的约束及其局限性
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458577983&idx=1&sn=91770ab97d6f2b826adc5e143e7e5483&chksm=b18ddcb586fa55a30db3c97d660b48765d5d16d32ae9b780fec7ac95756380fd7864a5ce4098&scene=58&subscene=0#rd
source: 看雪学苑
date: 2024-10-11
fetch_date: 2025-10-06T18:52:27.441903
---

# SDC2024议题聚焦 | Rust 的安全幻影：语言层面的约束及其局限性

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8E8yCSsWgGmmeNjMBnyleQMbZexnaun8gemznfdqPodPTAebvAx4mUfjT9VELpBgMO3ianibBFFBOpQ/0?wx_fmt=jpeg)

# SDC2024议题聚焦 | Rust 的安全幻影：语言层面的约束及其局限性

SDC2024

看雪学苑

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8E8yCSsWgGmmeNjMBnyleQMqd8TWubKBmm8DEWI2hZUNRcEsbVk6F8z2B8WT8KveNFfS203N8VQUA/640?wx_fmt=png&from=appmsg)

**·****SDC2024 议题预告** **·**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8E8yCSsWgGmmeNjMBnyleQMmTOEjlRa93alu4icOXGFzBktib87FTMquYtByJIicNgQrGnQ1qFFzP13Q/640?wx_fmt=gif&from=appmsg)

***0****1***

**Rust 的安全幻影：**

**语言层面的约束及其局限性**

本议题深入分析了 Rust 编程语言的编译二进制文件及其现有的安全问题。Rust 语言的安全机制源自于其背后的约束，Rust约束不仅是语言设计的核心，也是其安全性的重要保障。然而，这些约束并非无懈可击。

在现实场景中， Rust 的所有权、借用和生命周期在某些特定情况下可能导致安全隐患。比如，错误的约束规则、约束不完整或超出约束范围的代码，都会在不经意间使得安全问题浮出水面。议题将通过具体案例来探讨这些特征在实际应用中的表现。同时，引入【Rust 编译期】和【用户使用期】的概念，通过这两个阶段的划分来进一步辅助识别 Rust 安全性的局限性与挑战。

***0****2***

**演讲嘉宾**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8E8yCSsWgGmmeNjMBnyleQMy6VPNzkJZqa7kibLVdnvyBjAq9h3vtqUicFxfBPIJsXMq8DzfjiaiapgFQ/640?wx_fmt=jpeg&from=appmsg)

**陈浩**

奇安信天工实验室安全研究员，主要负责二进制漏洞挖掘相关工作。

***0****3***

**听众收获**

1. 了解Rust语言的安全机制，包括其背后的约束和安全性保障；

2. 识别Rust安全性的局限性，包括其所有权、借用和生命周期在某些特定情况下可能导致的安全隐患；

3. Rust安全问题的案例分析；

4. 提高安全意识和编程技能，更好地使用Rust编程语言开发安全的应用程序。

***0****4***

**报名参会**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8E8yCSsWgGmmeNjMBnyleQMczR6BvI0uYj0GzJgciaXu8TMkoE8BloxC52RXuWzwSohnEoFmAWiahIw/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8E8yCSsWgGmmeNjMBnyleQMicEz9gBb1CY6jOTbT5iaZ4aj5bdYA9jn2eX7WLqWH4Jcmiamt6YlrAtfQ/640?wx_fmt=jpeg&from=appmsg)

更多议题细节，欢迎来峰会现场聆听

![](https://mmbiz.qpic.cn/mmbiz_jpg/Uia4617poZXP96fGaMPXib13V1bJ52yHq9ycD9Zv3WhiaRb2rKV6wghrNa4VyFR2wibBVNfZt3M5IuUiauQGHvxhQrA/640?wx_fmt=other)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8E8yCSsWgGmmeNjMBnyleQM3RL8BOp4A7HB4KxODJcKiazfkqjNFAglfWrT2tIVfpZPKt4bHibAmm5w/640?wx_fmt=gif&from=appmsg)

**球分享**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8E8yCSsWgGmmeNjMBnyleQM3RL8BOp4A7HB4KxODJcKiazfkqjNFAglfWrT2tIVfpZPKt4bHibAmm5w/640?wx_fmt=gif&from=appmsg)

**球点赞**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8E8yCSsWgGmmeNjMBnyleQM3RL8BOp4A7HB4KxODJcKiazfkqjNFAglfWrT2tIVfpZPKt4bHibAmm5w/640?wx_fmt=gif&from=appmsg)

**球在看**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8E8yCSsWgGmmeNjMBnyleQMoAOAibJiavDbQkKhYjiaKLE18wWnYWhCOicGeokTrfM6RKmv0s1ibDBRRQA/640?wx_fmt=gif&from=appmsg)

点击阅读原文查看更多

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/1UG7KPNHN8EGLfh77kFmnicd9WOic2ibvhCibFdB4bL4srJCgo2wnvdoXLxpIvAkfCmmcptXZB0qKWMoIP8iaibYN2FA/0?wx_fmt=png)

看雪学苑

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1UG7KPNHN8EGLfh77kFmnicd9WOic2ibvhCibFdB4bL4srJCgo2wnvdoXLxpIvAkfCmmcptXZB0qKWMoIP8iaibYN2FA/0?wx_fmt=png)

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
---
title: 内存安全编码强化Android系统安全
url: https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247518525&idx=1&sn=527b5cd12121cefa54ccac0c26c32ba9&chksm=c144fb80f633729634a0b87b8c507d48b31734fd50c70fbbe7e022a677becae62c0bcd119ef7&scene=58&subscene=0#rd
source: 数世咨询
date: 2024-10-01
fetch_date: 2025-10-06T18:53:17.227271
---

# 内存安全编码强化Android系统安全

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Y9btpvDIDqo4QGLCrLnXyJuAEtBhrFIKQzFXjAiao6TDBQg2H48r0CuawEJFwP26oH3tbLdtgN0fXPksFU26ABw/0?wx_fmt=jpeg)

# 内存安全编码强化Android系统安全

数世咨询

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Y9btpvDIDqo4QGLCrLnXyJuAEtBhrFIKE3MXjZibbujAodibUYuPRzmU4zBalQxQ2cu1jlNef6h8Qr4ULicVgxEnA/640?wx_fmt=jpeg&from=appmsg)

自从Google开始转向使用Rust语言来开发Android系统的新功能以来，系统中出现的内存错误数量大幅减少。

在过去的五年里，Android系统中与内存相关漏洞的数量显著减少，这一成果主要得益于Google采用的安全设计理念。这种理念的核心在于大量新编码工作中广泛应用了Rust等内存安全的编程语言。

缓冲区溢出和释放后使用错误等内存安全问题在Android系统中的影响已大幅降低，目前仅占所有漏洞的24%。这一数据相比2019年的76%有明显下降。截至今年前几个月的数据统计，发现与Android内存相关的漏洞共计36个，约为去年数量的一半，与其在2019年高达223个漏洞的情况大相径庭。

**01**

**“安全设计”理念的回报**

在9月25日的一篇博文中，来自Google Android和安全团队的研究人员指出，这一进展应归功于他们的安全编码实践，这是一种旨在优先考虑使用如Rust等内存安全编程语言的新代码开发的安全设计方法。研究人员解释道：“基于我们所掌握的知识，很明显，我们不需要完全放弃或重写所有的现有内存不安全代码。相反，Android项目的重点是使互操作性既安全又便捷，这是我们在内存安全之旅中的主要目标之一。”

内存安全漏洞长期以来一直是应用程序软件漏洞的大头，其占比通常超过60%，并且预计这一比例将继续保持在高位。这类漏洞的危害性远超其他类型的缺陷。以2022年为例，与内存相关的错误在所有已识别的Android漏洞中仅占36%，然而，它们却是操作系统中最严重问题的86%，在已确认遭利用的Android漏洞中占比高达78%。

在编程领域，广泛使用的语言如C和C++允许开发人员直接操作内存，这为软件编码错误留下了空间。相比之下，像Rust、Go和C#这样的内存安全语言提供了自动的内存管理和内置的安全检查功能，这些功能帮助预防了常见的内存相关错误。即使是美国网络安全和基础设施安全局（CISA）甚至白宫等机构，都对使用非内存安全语言带来的安全风险增加以及解决这些问题所需的大量成本表示担忧。尽管向内存安全语言的转变正在逐步推进，但许多人预计完全迁移现有的代码库到内存安全的代码可能需要数年甚至数十年的时间。

**02**

**渐进的过渡**

谷歌选择采用内存安全的编程语言（如Rust）来实现Android新功能，同时基本保留现有代码基础。两位Google研究员指出，这种转变导致近年来使用非内存安全语言的新项目开发速度减缓，而基于内存安全的开发活动则呈现增长趋势。

自Android 12起，Google便开始向Rust支持过渡，并在Android开源项目中逐步增加对该编程语言的使用。到了Android 13，操作系统中的大部分新代码已经转向使用内存安全语言编写。谷歌当时明确表示，他们的目标并非将所有C和C++代码替换为Rust，而是计划随着时间的推移，逐渐实现这一转换。

在早先的一篇博文中，Google的安全工程团队表达了一种观点：“将C++改造为一种具备严格内存安全保障的语言是不现实的。”尽管如此，Google并未放弃对C和C++的投入，而是继续投资于提高这些语言内存安全的工具，以此来支持公司庞大的、基于C++编写的代码库。

特别值得一提的是，Google注意到，涉及内存相关的错误在Android系统漏洞中的比例有所减少。这一变化不仅得益于该公司越来越多地采用如Rust这样的内存安全编程语言，而且旧的漏洞随着时间的推移自然减少也是原因之一。研究人员指出，与新编写的代码相比，五年前的Android代码中相同数量的代码段往往具有较低的漏洞密度。

研究人员说：“问题主要在于新代码，因此需要从根本上改变我们开发代码的方式”。

\* 本文为陈发明编译，原文地址：
https://www.darkreading.com/application-security/memory-safe-code-adoption-android-safer
注：图片均来源于网络，无法联系到版权持有者。如有侵权，请与后台联系，做删除处理。

— 【 THE END 】—

🎉 大家期盼很久的#**数字安全交流群**来了！快来加入我们的粉丝群吧！

🎁 **多种报告，产业趋势、技术趋势**

这里汇聚了行业内的精英，共同探讨最新产业趋势、技术趋势等热门话题。我们还有准备了专属福利，只为回馈最忠实的您！

👉 扫码立即加入，精彩不容错过！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqqPJv9p5ibKIhJXQjWHJmSlibSdib80Llfp8mlV0ibf7m47jyaVeGoFeorddtIuxS5liafTJRKHeSdLnaQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

😄嘻嘻，我们群里见！

更多推荐

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqp72VD8Ft2xAxulKkNQzCpMYmic4xkqp3ky3wcian32ndo3MuLV2dqL6RgqTfITGP0SsmRzibUBftDFg/640?wx_fmt=png&from=appmsg)](http://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247514213&idx=1&sn=fa2d0412dbbce05ec48a9df909b7cfd3&chksm=c144cad8f63343ce0f383fc9d885c2c7ddcb3f3871270abea4c274775307858d350f60db3b54&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqqXZatwW85WHD0ggOUzguusylfEicp7y64ic36rtZXpLGPKXds2NvBpuExtgAMicK0LB71waZTVKfpPw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247513359&idx=1&sn=2f3bd51b24862de02cca6078688bafeb&chksm=c144c7b2f6334ea415adac810ce4803cdb3cd5e5ba194ff394b7278ebbb48cc830c8d405427a&token=824343009&lang=zh_CN&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqo4QGLCrLnXyJuAEtBhrFIKVsI37oeicK5Dicx7JibKicdfOQa7mc117xz0J42ibvAewtA9ltZCpxdBV1Q/640?wx_fmt=png&from=appmsg)](http://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247496165&idx=1&sn=8eebdc4bc446705fc36c513df9834080&chksm=c1448358f6330a4e6bfeaa03b49f59489b3b1a57d33fa7713cbe07773e8ab9a6d82615ca8e03&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Y9btpvDIDqqibHKn3xia71ylibsqm32we7KaKfENSmicZKZf0dT3Jic5QicvIicKsBUZxyTt9FvqFNVAKV5ILVE5se9AQ/0?wx_fmt=png)

数世咨询

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Y9btpvDIDqqibHKn3xia71ylibsqm32we7KaKfENSmicZKZf0dT3Jic5QicvIicKsBUZxyTt9FvqFNVAKV5ILVE5se9AQ/0?wx_fmt=png)

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
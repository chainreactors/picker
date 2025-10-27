---
title: 本地防御绕过，一款通过调用Windows系统白名单文件执行PowerShell命令的工具
url: https://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247498948&idx=1&sn=062edba0bbb40b2214670da48083f3c2&chksm=fa595229cd2edb3f14fa2a6119ee09eb114d414f86bd884fc4943bfdffb7999900037466b378&scene=58&subscene=0#rd
source: dotNet安全矩阵
date: 2025-02-18
fetch_date: 2025-10-06T20:39:56.643893
---

# 本地防御绕过，一款通过调用Windows系统白名单文件执行PowerShell命令的工具

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YiczKSznEcepYxrkAyv2WgKswGC46xVib2nkjGSeG4pXuObs7pruibEm5bBsHXn8I7iaPHdeePvDADU7w/0?wx_fmt=jpeg)

# 本地防御绕过，一款通过调用Windows系统白名单文件执行PowerShell命令的工具

原创

专攻.NET安全的

dotNet安全矩阵

Sharp4BreakStart.exe 是一款利用了 Windows 系统的白名单机制，通过生成并执行 VBScript 脚本来启动 PowerShell 指令的工具。由于该工具能够绕过某些基于签名的安全防护，成为了渗透测试者和红队成员在执行任务时的重要工具。本文将详细介绍 `Sharp4BreakStart.exe` 的工作原理、基本用法、应用场景以及潜在的安全风险。

**01. 工具基本介绍**

Sharp4BreakStart.exe 是一款巧妙利用 Windows 系统的白名单机制的工具。它通过将命令编译为 VBScript 脚本，然后使用系统白名单文件启动 PowerShell 指令。

此工具可以绕过某些安全防护，执行指定命令或脚本，比如启动 PowerShell 命令或其他程序。由于其利用了 Windows 系统内的白名单文件，这使得它能够绕过部分基于签名的安全检测。

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8gCOsRWBfquZ6F6Qs5uexSc7X2f0VYxRlHGpzxhqf0ib3SxnLYhHFTXK8cwtAZKauWOyBtSvjGP5g/640?wx_fmt=jpeg&from=appmsg)

**02. 工具工作原理**

Sharp4BreakStart.exe 的工作原理是在目标系统上生成并执行一个 VBScript 脚本。该脚本在执行时启动 PowerShell，并通过指定命令启动目标程序或脚本。由于生成的 VBScript 脚本与 Windows 系统的白名单文件关联，这使得它能够在不被大多数防病毒软件或安全防护工具检测的情况下执行。

## 2.1 通过VBS启动PS

VBScript 是一种脚本语言，`Sharp4BreakStart.exe` 通过生成 VBScript 脚本来启动 PowerShell，这种方式能够轻松绕过一些基于文件扩展名或脚本源的安全检测。

## 2.2 利用系统白名单文件

Windows 系统中的白名单文件是指由操作系统或微软签名的文件，这些文件在执行时往往不会被安全软件拦截。`Sharp4BreakStart.exe` 的一个关键特点就是它利用了这些文件，通过编译成 VBScript 并借助白名单文件的机制启动 PowerShell 指令。

**03. 工具实战用法**

因为 VBScript 脚本被认为是合法的、已知的 Windows 系统功能之一，所以它不太可能被某些安全防护系统标记为恶意。

使用 `Sharp4BreakStart.exe` 非常简单。其基本用法如下：

```
```
Sharp4BreakStart.exe calc.exe
```
```

该命令会启动 Windows 自带的计算器应用 `calc.exe`。用户只需要将需要启动的程序名称作为参数传递给 `Sharp4BreakStart.exe`，工具将会自动生成相应的 VBScript 并通过 PowerShell 执行该程序。

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1YiczKSznEcepYxrkAyv2WgKsk7h4AeV8CNfrVyJaTxehUcwwBibwutrKQPlr18erS9drFmAXDe0D2hw/640?wx_fmt=png&from=appmsg)

综上所述，`Sharp4BreakStart.exe` 是一款利用 Windows 系统白名单文件启动 PowerShell 指令的工具。通过将命令转化为 VBScript 脚本并借助白名单文件机制，该工具能够绕过部分安全检测，并执行任意命令或程序。文章涉及的工具已打包在星球，感兴趣的朋友可以加入自取。

**04. 技术精华内容**

从漏洞分析到安全攻防，我们涵盖了 .NET 安全各个关键方面，为您呈现最新、最全面的 .NET 安全知识，下面是公众号发布的精华文章集合，推荐大伙阅读！

[![图片](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8TQhCZMggf71ffibqISJ8f5naPJacnjn0roDyxxnAibmuwDJq2p1GTBpicZhnM9o9gTIu9S9ia8Uqwtw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&retryload=1&tp=webp)](https://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247497498&idx=2&sn=00900a0c29c85b41fe6a586d7e5c3571&scene=21#wechat_redirect)

[![图片](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y9tl26Kh2sQYI9guTCflSwQP8Gs9z7iamicOvlQv4UYzjwd378D03h7yEYFtZ6xA74qicInoed7qpBWg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247495167&idx=1&sn=9280c55fdc7c9146e549be470cf9f120&chksm=fa594312cd2eca04bfe8fd1fd3890b389d9c700b9b69d897f919addac399bab4f4d2e55f6b4f&scene=21#wechat_redirect)

[![图片](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibQ6VpnKYXPqfmHnyJHzHxOeP3ichLEiafhGiawd8mjkHYBalO37fN8QQkNdic1hjjY2Nvw2Bib6UvibDRA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247490722&idx=2&sn=c9807daa5548e139a0c67303cb26882a&chksm=fa5ab24fcd2d3b59a85be03e69c655ffd644e8458bc2ec3f572da4b40b43e5003fda756f35b4&scene=21#wechat_redirect)

[![图片](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibQ6VpnKYXPqfmHnyJHzHxOjWgak8cI7Mic1wTt3YSKqsbLl9rPe0cF9WGtOEuiceLreTNtNVib6IKlw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247490703&idx=2&sn=e7db1ff662e5b41d9a1806fbdf33e204&chksm=fa5ab262cd2d3b7470f029b9a07d1dd3611e63be910b01a601144efe7d84b5f016f488a354cf&scene=21#wechat_redirect)

[![图片](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibQ6VpnKYXPqfmHnyJHzHxO8jJ97qqWlY6XR03DqSnutcHFYibDtVG5Y2wEaK4p2bzEicZblY4oQyGg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247490700&idx=2&sn=e8a865ada7c743e77fb9e953c5da74b1&chksm=fa5ab261cd2d3b7736387eddfc8524a378a1604552d0c9b55476646f9e8275f48818aab8acad&scene=21#wechat_redirect)

[![图片](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibQ6VpnKYXPqfmHnyJHzHxOe1viaia4aoFceunsUdIna4DPbmemW1EqlBMrovOoE6bdAFF3iaApxz5qA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247488736&idx=2&sn=d24aaa297c51eb620ccdf67af513086d&chksm=fa5aba0dcd2d331bbb22f3f5657199d718c90efed42fcb9cb67ec23d342f887c117e4858f1cb&scene=21#wechat_redirect)

**05. 加入安全社区**

目前dot.Net安全矩阵星球已成为中国.NET安全领域最知名、最专业的技术知识库之一，超 **1200+** 成员一起互动学习。星球主题数量近 **600+**，精华主题 230+，PDF文档和压缩包 300+ 。从Web应用到PC端软件应用，无论您是初学者还是经验丰富的开发人员，都能在这里找到对应的实战指南和最佳实践。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y9AiaXibTRdEnEfYuQx76FjZVjmyEWtIaDuDePFFmyRqggiaq2k47pLoib9GZtUCOhaP40WPlhvbiaKZVg/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

## 20+专栏文章

星球文化始终认为授人以鱼不如授人以渔！星球整理出**20+**个专题栏目涵盖 **.NET安全 点、线、面、体等知识范围**，助力师傅们实战攻防！其中主题包括.NET  内网攻防、漏洞分析、内存马、代码审计、预编译、反序列化、WebShell免杀、命令执行、工具库等等。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8xRheDpQ7NsESosdNZUopa90SJRuwnLy9uZV4icrXiaZlJPQlYJWXTw8HCrF9oTcE3DDgrdFnXo2BA/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

## 海量资源和工具

截至当前，dot.Net安全矩阵星球社区汇聚了 **600+** 个实用工具和高质量PDF学习资料。这些资源涵盖了攻防对抗的各个方面，在实战中能够发挥显著作用，为对抗突破提供强有力的支持。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8xRheDpQ7NsESosdNZUopaqVZW8XsALVA4FNiaj32q8npN82VSeqSKb4fQvLiczFNs0099VRFVQwPA/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8xRheDpQ7NsESosdNZUopa63ZXbX3YXLwoeNnjStcRtTbU9hoe6ecO5hhkj2apG1I6tKlkpz5GaQ/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

## 专属成员交流群

我们还有多个成员专属的**内部星球陪伴群**，加入的成员可以通过在群里提出问题或参与论的方式来与其他成员交流思想和经验。此外还可以通过星球或者微信群私聊向我们进行提问，以获取帮助迅速解决问题。

![图片](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8xRheDpQ7NsESosdNZUopaAiaouHb6HYza539m9v0ykDoD2JezaArDZBPlJInuabf6XsduzVcjZ0Q/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

## 已入驻的大咖们

星球汇聚了各行业安全攻防技术大咖，并且每日分享.NET安全技术干货以及交流解答各类技术等问题，社区中发布很多**高质量的.NET安全资源**，可以说市面上很少见，都是干货。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibEfvTKP231YekyMbc9jeicFuh0aAYDSicAg36pkFaC2P1KW0L5NV1HOssmysrPnrP1fzr2rFOmy8lA/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

## 欢迎加入我们

dotNet安全矩阵星球从创建以来一直聚焦于.NET领域的安全攻防技术，定位于高质量安全攻防星球社区，也得到了许多师傅们的支持和信任，通过星球深度连接入圈的师傅们，一起推动.NET安全高质量的向前发展。**星球门票后期价格随着内容和质量的不断沉淀会适当提高，因此越早加入越好！**

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8xRheDpQ7NsESosdNZUopag09JtYcKpucjZPAlfeqC1ovcQvhrkemAzbURDaVF3InmpQshiatDnyQ/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8uc3CokHvGlrE00icPjW7AdTgEXkDtRT81Bbiaibx9gpMD6thAiawO5vz0icNlUzrzaOf6g044Tnzv3sQ/0?wx_fmt=png)

dotNet安全矩阵

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8uc3CokHvGlrE00icPjW7AdTgEXkDtRT81Bbiaibx9gpMD6thAiawO5vz0icNlUzrzaOf6g044Tnzv3sQ/0?wx_fmt=png)

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
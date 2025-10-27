---
title: .NET 实战中指定任意进程绕过UAC的工具
url: https://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247498077&idx=1&sn=04b717db56927d9b13c5b8ecdbd3ab3f&chksm=fa5957b0cd2edea67eaad3351471d3667a75fd70ebd1081a5c87395b2a6a42c4f784e48e5607&scene=58&subscene=0#rd
source: dotNet安全矩阵
date: 2025-01-09
fetch_date: 2025-10-06T20:10:55.637443
---

# .NET 实战中指定任意进程绕过UAC的工具

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8Db8KbC6Q8iclZNYFiazrmanaFPoEgnbsI5icaSN13LwAf3K72jLfrW5NGxurJ51wfetrib48wkyBoqw/0?wx_fmt=jpeg)

# .NET 实战中指定任意进程绕过UAC的工具

原创

专攻.NET安全的

dotNet安全矩阵

此文所提供的信息只为网络安全人员对自己所负责的网站、服务器等进行检测或维护参考，未经授权请勿利用文章中的技术资料对任何计算机系统进行入侵操作。利用此文所提供的信息而造成的直接或间接后果和损失，均由使用者本人负责。本文所提供的工具仅用于学习，禁止用于其他方面。

Sharp4UACPlus.exe 是一款专门设计用于内网渗透过程中绕过用户帐户控制（UAC）的实用工具，它是 **Sharp4UACPASS.exe** 的优化升级版本。在红队活动中，UAC常常成为提升权限的一个阻碍，而 Sharp4UACPlus.exe 通过提升当前用户权限，能够轻松绕过这一限制，执行高权限操作，为渗透测试和后续操作提供便利。

01

Sharp4UACPASS 背景介绍

**1.1 主题背景介绍**

前两周，我们发布了 Sharp4UACPASS.exe 这款绕过UAC的工具，此工具无需以管理员身份运行，直接双击即可使用。运行后，工具会弹出一个交互式 cmd.exe 窗口，为渗透测试或本地权限提升提供便利，原文请参考：

[.NET 一款内网实战中绕过UAC的神器](https://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247497663&idx=3&sn=b2c03aaa2ab108cf4daa61206df259eb&scene=21#wechat_redirect)

工具在星球发布后，有多位师傅们还希望能启动指定的进程，实战中避开对cmd.exe的依赖，有关主题思想火花的碰撞和交流讨论如下图所示。

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Yiclo9umXySkaJo4nf8WqSFmaJkNzXhkKibC49XMd6RNLxdU3aLWE578797H1Yhs77U7bf59U5rmicBw/640?wx_fmt=png&from=appmsg)

因此有必要对工具进行升级优化。

02

Sharp4UACPlus 基本介绍

**2.1 工具背景介绍**

与前代工具 Sharp4UACPASS.exe 相比，Sharp4UACPlus.exe 不仅继承了其强大的功能，还新增了**自定义启动任意进程**的能力。无论是启动cmd命令行，还是运行特定程序或脚本，这款工具都能胜任，极大地增强了工具的灵活性和适用性。

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8Db8KbC6Q8iclZNYFiazrman81t78o5I4autdficwV5p6libm7kiaoX8OIlX2ENMRB7lCWZD2OlMh7ibmw/640?wx_fmt=jpeg&from=appmsg)

**2.2 工具使用方法**

通过 Sharp4UACPlus.exe.config 配置文件实现操作流程的个性化定制，无需修改工具源代码。在 <appSettings> 节点中设置要执行的目标程序或脚本路径。具体代码如下所示。

```
```
<appSettings>
    <add key="ExecPath" value="C:\Windows\System32\winver.exe" />
</appSettings>
```
```

ExecPath：指定目标进程的物理路径。例如，启动 Windows 版本信息窗口，可以设置为 C:\Windows\System32\winver.exe。

如果需要运行脚本，可以指定脚本解释器路径并附加脚本文件路径，例如：

```
```
<add key="ExecPath" value="C:\Windows\System32\cmd.exe /c C:\path\to\script.bat" />
```
```

双击或者在cmd下运行 Sharp4UACPlus.exe，工具会根据配置文件中的设置自动启动指定的进程或脚本，并以高权限运行，如下图所示。

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8Db8KbC6Q8iclZNYFiazrman8ppIlVKZIs4IJCDWTXzPAsqfpXDD2by9OBtiaNE9y2g7EeVzy8gIEnw/640?wx_fmt=png&from=appmsg)

综上，Sharp4UACPlus.exe 是一款高效的 UAC 绕过工具，通过简易配置和灵活的自定义进程启动功能，为内网渗透和红队活动提供了强大的支持。文章涉及的工具已打包在星球，感兴趣的朋友可以加入自取。

03

公众号安全技术精华内容

**3.1 .NET 精华回顾**

从漏洞分析到安全攻防，我们涵盖了 .NET 安全各个关键方面，为您呈现最新、最全面的 .NET 安全知识，下面是公众号发布的精华文章集合，推荐大伙阅读！

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8A7Qhn1ssuqNzv0iceS7ZhOuZ0AO4P1eFeG2xTdR2V6GWibiaxO2RenUJzrwOfvsdqofibI6H2uY0CLQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](https://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247497429&idx=2&sn=a07599921eeb651ce005f57ed350be5e&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8TQhCZMggf71ffibqISJ8f5naPJacnjn0roDyxxnAibmuwDJq2p1GTBpicZhnM9o9gTIu9S9ia8Uqwtw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&retryload=1&tp=webp)](https://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247497498&idx=2&sn=00900a0c29c85b41fe6a586d7e5c3571&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y9tl26Kh2sQYI9guTCflSwQP8Gs9z7iamicOvlQv4UYzjwd378D03h7yEYFtZ6xA74qicInoed7qpBWg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247495167&idx=1&sn=9280c55fdc7c9146e549be470cf9f120&chksm=fa594312cd2eca04bfe8fd1fd3890b389d9c700b9b69d897f919addac399bab4f4d2e55f6b4f&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibQ6VpnKYXPqfmHnyJHzHxOeP3ichLEiafhGiawd8mjkHYBalO37fN8QQkNdic1hjjY2Nvw2Bib6UvibDRA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247490722&idx=2&sn=c9807daa5548e139a0c67303cb26882a&chksm=fa5ab24fcd2d3b59a85be03e69c655ffd644e8458bc2ec3f572da4b40b43e5003fda756f35b4&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibQ6VpnKYXPqfmHnyJHzHxOjWgak8cI7Mic1wTt3YSKqsbLl9rPe0cF9WGtOEuiceLreTNtNVib6IKlw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247490703&idx=2&sn=e7db1ff662e5b41d9a1806fbdf33e204&chksm=fa5ab262cd2d3b7470f029b9a07d1dd3611e63be910b01a601144efe7d84b5f016f488a354cf&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibQ6VpnKYXPqfmHnyJHzHxO8jJ97qqWlY6XR03DqSnutcHFYibDtVG5Y2wEaK4p2bzEicZblY4oQyGg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247490700&idx=2&sn=e8a865ada7c743e77fb9e953c5da74b1&chksm=fa5ab261cd2d3b7736387eddfc8524a378a1604552d0c9b55476646f9e8275f48818aab8acad&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibQ6VpnKYXPqfmHnyJHzHxOe1viaia4aoFceunsUdIna4DPbmemW1EqlBMrovOoE6bdAFF3iaApxz5qA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247488736&idx=2&sn=d24aaa297c51eb620ccdf67af513086d&chksm=fa5aba0dcd2d331bbb22f3f5657199d718c90efed42fcb9cb67ec23d342f887c117e4858f1cb&scene=21#wechat_redirect)

04

欢迎加入.NET 安全矩阵星球

**4.1 .NET 安全社区**

目前dot.Net安全矩阵星球已成为中国.NET安全领域最知名、最专业的技术知识库之一，超 **1200+** 成员一起互动学习。星球主题数量近 **600+**，精华主题 230+，PDF文档和压缩包 300+ 。从Web应用到PC端软件应用，无论您是初学者还是经验丰富的开发人员，都能在这里找到对应的实战指南和最佳实践。

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y9AiaXibTRdEnEfYuQx76FjZVjmyEWtIaDuDePFFmyRqggiaq2k47pLoib9GZtUCOhaP40WPlhvbiaKZVg/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**4.2 20+个专栏文章**

星球文化始终认为授人以鱼不如授人以渔！星球整理出**20+**个专题栏目涵盖 **.NET安全 点、线、面、体等知识范围**，助力师傅们实战攻防！其中主题包括.NET  内网攻防、漏洞分析、内存马、代码审计、预编译、反序列化、WebShell免杀、命令执行、工具库等等。

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8xRheDpQ7NsESosdNZUopa90SJRuwnLy9uZV4icrXiaZlJPQlYJWXTw8HCrF9oTcE3DDgrdFnXo2BA/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

**4.3 星球海量的工具**

截至当前，dot.Net安全矩阵星球社区汇聚了 **600+** 个实用工具和高质量PDF学习资料。这些资源涵盖了攻防对抗的各个方面，在实战中能够发挥显著作用，为对抗突破提供强有力的支持。

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8xRheDpQ7NsESosdNZUopaqVZW8XsALVA4FNiaj32q8npN82VSeqSKb4fQvLiczFNs0099VRFVQwPA/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8xRheDpQ7NsESosdNZUopa63ZXbX3YXLwoeNnjStcRtTbU9hoe6ecO5hhkj2apG1I6tKlkpz5GaQ/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

**4.4 星球专属成员群**

我们还有多个成员专属的**内部星球陪伴群**，加入的成员可以通过在群里提出问题或参与论的方式来与其他成员交流思想和经验。此外还可以通过星球或者微信群私聊向我们进行提问，以获取帮助迅速解决问题。

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8xRheDpQ7NsESosdNZUopaAiaouHb6HYza539m9v0ykDoD2JezaArDZBPlJInuabf6XsduzVcjZ0Q/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

**4.5 入驻星球的大咖们**

星球汇聚了各行业安全攻防技术大咖，并且每日分享.NET安全技术干货以及交流解答各类技术等问题，社区中发布很多**高质量的.NET安全资源**，可以说市面上很少见，都是干货。

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibEfvTKP231YekyMbc9jeicFuh0aAYDSicAg36pkFaC2P1KW0L5NV1HOssmysrPnrP1fzr2rFOmy8lA/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

**4.6 欢迎加入我们**

dotNet安全矩阵星球从创建以来一直聚焦于.NET领域的安全攻防技术，定位于高质量安全攻防星球社区，也得到了许多师傅们的支持和信任，通过星球深度连接入圈的师傅们，一起推动.NET安全高质量的向前发展。**星球门票后期价格随着内容和质量的不断沉淀会适当提高，因此越早加入越好！**

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8xRheDpQ7NsESosdNZUopag09JtYcKpucjZPAlfeqC1ovcQvhrkemAzbURDaVF3InmpQshiatDnyQ/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

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
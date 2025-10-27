---
title: 举一反三 ，通过 Sharp4SuoPoc 从原理上复现  Visual Studio 投毒事件的来龙去脉
url: https://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247498340&idx=1&sn=f9aecfc3de35b8fac05e7e7d352da9e4&chksm=fa595489cd2edd9f317b3ce1a2e10a23a2a5c3c3fc4a16daa713ac76716cec8ef519e525b37a&scene=58&subscene=0#rd
source: dotNet安全矩阵
date: 2025-01-21
fetch_date: 2025-10-06T20:10:59.861062
---

# 举一反三 ，通过 Sharp4SuoPoc 从原理上复现  Visual Studio 投毒事件的来龙去脉

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y9PFDpDvKwTXJc0F7cwmEa4yiaqCVhv19OYTKgRezM6cqvzdibiaVVPfex6opJHjpHLudAcly4uVmKtA/0?wx_fmt=jpeg)

# 举一反三 ，通过 Sharp4SuoPoc 从原理上复现 Visual Studio 投毒事件的来龙去脉

原创

专攻.NET安全的

dotNet安全矩阵

![](https://mmbiz.qpic.cn/mmbiz_gif/NO8Q9ApS1YibJO9SDRBvE01T4A1oYJXlTBTMvb7KbAf7z9hY3VQUeayWI61XqQ0ricUQ8G1FykKHBNwCqpV792qg/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp)

在近期的网络安全事件中，一款提权工具被发现植入了后门，攻击者利用 Visual Studio 项目的 .suo 文件作为隐蔽的攻击媒介。由于 .suo 文件通常是隐藏的配置文件，且安全研究人员对其内容关注较少，因此成为了攻击者利用的一个漏洞。

**01. 相关背景介绍**

.suo 文件是 Visual Studio 中用于存储用户自定义设置和状态的文件，通常用于保存项目的用户环境配置，如调试设置、编辑器状态等。攻击者利用 .suo 文件的隐蔽性，可以在项目打开时执行恶意代码，从而实现反向连接、权限提升等攻击行为。

此次攻击事件被初步归因于东南亚地区的 APT 组织——海莲花。该组织因其高隐蔽性和高技术水平而著名，长期以来专门针对政府机构、军事单位以及高价值目标进行精准打击。

为了防止类似的攻击事件发生，安全研究人员开发了专门的工具来分析 .suo 文件，防止通过 .suo 文件引入的恶意代码对项目和开发者造成损害，详情请大家阅读上一篇文章[《拒绝 Github 投毒，通过 Sharp4SuoBrowser 分析 Visual Studio 隐藏文件》](https://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247498230&idx=1&sn=1e5e2aea22eaa89ab48881c6176108fc&scene=21#wechat_redirect)

**02. **工具**实战操作**

Sharp4SuoPoc.exe 是一款专门用于创建恶意 .suo 文件的工具。该工具可以将恶意命令嵌入到 .suo 文件中，导致当 Visual Studio 打开项目时，自动执行指定的命令。此工具能够帮助安全研究人员了解如何利用 .suo 文件作为攻击媒介，从而采取有效的防护措施。

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y9PFDpDvKwTXJc0F7cwmEa4hiabzrs3NXRQuXHFibgqzHCLf4csRJI1AcSKCP75n9T2LdHMu8z2Itdw/640?wx_fmt=jpeg&from=appmsg)

## 2.1 工具用法

以下是使用 Sharp4SuoPoc.exe 工具的基本步骤，首先，你需要一个正常的 .suo 文件，通常可以从现有的 Visual Studio 项目中获取。这个文件包含了项目的默认配置信息。这里以 Sharp4VSSuo1 项目为例，隐藏的.suo文件具体的路径如下所示。

```
```
\.vs\Sharp4VSSuo1\v16\.suo
```
```

随后将这个.suo文件重命名为original.suo，这样做的目的在于名称方便管理。

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8BMpj9YFSbJMRoY97L1hdPPlDyVwHQd4Kxhibib0VI0w0KxSTYXQySkicVLXu5CQ9loueiaLBUmBft2w/640?wx_fmt=png&from=appmsg)

接着，使用 Sharp4SuoPoc.exe 工具，并传入命令参数。以下是一个命令示例。

```
```
Sharp4SuoPoc.exe original.suo handle.suo cmd /c start winver
```
```

生成的 handle.suo 文件会包含恶意命令，当 .suo 文件被打开时会执行启动 winver.exe 进程，如下图所示。

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8BMpj9YFSbJMRoY97L1hdPNms53JOq6AmyuxgNfgW9Ys5cdNYTRCAvI0xqvTmPMWibozfpJ6bFSXQ/640?wx_fmt=png&from=appmsg)

然后，将生成的 handle.suo 文件复制到 Visual Studio 安装目录下的 .suo 文件存储路径，例如 vs\Sharp4VSSuo1\v16 目录。

最后，在 Visual Studio 中打开 Sharp4VSSuo1 项目，此时指定的命令会被自动执行，命令会弹出 Windows 版本信息窗口，如下图所示。

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y9PFDpDvKwTXJc0F7cwmEa4aAeNvt4PwVsVOEcWKjWnXaicS6SgicZAC0Pc5wpJuK49ibUotkNH6OLyQ/640?wx_fmt=png&from=appmsg)

## 2.2 防护措施

防止这种通过 .suo 文件的攻击，开发者和安全团队可以批量在项目中采取使用 Sharp4SuoBrowser.exe 这样的工具来分析 .suo 文件，确保文件中没有被植入恶意代码。

另外，确保 .suo 文件始终被隐藏，并且限制对其的访问权限。对于不需要的 .suo 文件，可以删除。

## 2.3 小结

防止这种通过 .suo 文件的攻击，开发者和安全团队可以批量在项目中采取使用 Sharp4SuoBrowser.exe 这样的工具来分析 .suo 文件，确保文件中没有被植入恶意代码

综上，通过 Sharp4SuoPoc.exe 展示了如何利用 .suo 文件这一被忽视的配置文件作为攻击渠道。在面对类似攻击时，开发者和安全团队应当提高警惕，采取必要的安全措施，保护自己的工作环境免受这种隐蔽攻击的威胁，文章涉及的工具已打包在星球，感兴趣的朋友可以加入自取。

**03. 技术精华内容**

从漏洞分析到安全攻防，我们涵盖了 .NET 安全各个关键方面，为您呈现最新、最全面的 .NET 安全知识，下面是公众号发布的精华文章集合，推荐大伙阅读！

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8TQhCZMggf71ffibqISJ8f5naPJacnjn0roDyxxnAibmuwDJq2p1GTBpicZhnM9o9gTIu9S9ia8Uqwtw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&retryload=1&tp=webp)](https://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247497498&idx=2&sn=00900a0c29c85b41fe6a586d7e5c3571&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y9tl26Kh2sQYI9guTCflSwQP8Gs9z7iamicOvlQv4UYzjwd378D03h7yEYFtZ6xA74qicInoed7qpBWg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247495167&idx=1&sn=9280c55fdc7c9146e549be470cf9f120&chksm=fa594312cd2eca04bfe8fd1fd3890b389d9c700b9b69d897f919addac399bab4f4d2e55f6b4f&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibQ6VpnKYXPqfmHnyJHzHxOeP3ichLEiafhGiawd8mjkHYBalO37fN8QQkNdic1hjjY2Nvw2Bib6UvibDRA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247490722&idx=2&sn=c9807daa5548e139a0c67303cb26882a&chksm=fa5ab24fcd2d3b59a85be03e69c655ffd644e8458bc2ec3f572da4b40b43e5003fda756f35b4&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibQ6VpnKYXPqfmHnyJHzHxOjWgak8cI7Mic1wTt3YSKqsbLl9rPe0cF9WGtOEuiceLreTNtNVib6IKlw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247490703&idx=2&sn=e7db1ff662e5b41d9a1806fbdf33e204&chksm=fa5ab262cd2d3b7470f029b9a07d1dd3611e63be910b01a601144efe7d84b5f016f488a354cf&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibQ6VpnKYXPqfmHnyJHzHxO8jJ97qqWlY6XR03DqSnutcHFYibDtVG5Y2wEaK4p2bzEicZblY4oQyGg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247490700&idx=2&sn=e8a865ada7c743e77fb9e953c5da74b1&chksm=fa5ab261cd2d3b7736387eddfc8524a378a1604552d0c9b55476646f9e8275f48818aab8acad&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibQ6VpnKYXPqfmHnyJHzHxOe1viaia4aoFceunsUdIna4DPbmemW1EqlBMrovOoE6bdAFF3iaApxz5qA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247488736&idx=2&sn=d24aaa297c51eb620ccdf67af513086d&chksm=fa5aba0dcd2d331bbb22f3f5657199d718c90efed42fcb9cb67ec23d342f887c117e4858f1cb&scene=21#wechat_redirect)

**04. 加入安全社区**

目前dot.Net安全矩阵星球已成为中国.NET安全领域最知名、最专业的技术知识库之一，超 **1200+** 成员一起互动学习。星球主题数量近 **600+**，精华主题 230+，PDF文档和压缩包 300+ 。从Web应用到PC端软件应用，无论您是初学者还是经验丰富的开发人员，都能在这里找到对应的实战指南和最佳实践。

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y9AiaXibTRdEnEfYuQx76FjZVjmyEWtIaDuDePFFmyRqggiaq2k47pLoib9GZtUCOhaP40WPlhvbiaKZVg/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

## 20+专栏文章

星球文化始终认为授人以鱼不如授人以渔！星球整理出**20+**个专题栏目涵盖 **.NET安全 点、线、面、体等知识范围**，助力师傅们实战攻防！其中主题包括.NET  内网攻防、漏洞分析、内存马、代码审计、预编译、反序列化、WebShell免杀、命令执行、工具库等等。

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8xRheDpQ7NsESosdNZUopa90SJRuwnLy9uZV4icrXiaZlJPQlYJWXTw8HCrF9oTcE3DDgrdFnXo2BA/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

## 海量资源和工具

截至当前，dot.Net安全矩阵星球社区汇聚了 **600+** 个实用工具和高质量PDF学习资料。这些资源涵盖了攻防对抗的各个方面，在实战中能够发挥显著作用，为对抗突破提供强有力的支持。

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8xRheDpQ7NsESosdNZUopaqVZW8XsALVA4FNiaj32q8npN82VSeqSKb4fQvLiczFNs0099VRFVQwPA/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8xRheDpQ7NsESosdNZUopa63ZXbX3YXLwoeNnjStcRtTbU9hoe6ecO5hhkj2apG1I6tKlkpz5GaQ/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

## 专属成员交流群

我们还有多个成员专属的**内部星球陪伴群**，加入的成员可以通过在群里提出问题或参与论的方式来与其他成员交流思想和经验。此外还可以通过星球或者微信群私聊向我们进行提问，以获取帮助迅速解决问题。

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8xRheDpQ7NsESosdNZUopaAiaouHb6HYza539m9v0ykDoD2JezaArDZBPlJInuabf6XsduzVcjZ0Q/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

## 已入驻的大咖们

星球汇聚了各行业安全攻防技术大咖，并且每日分享.NET安全技术干货以及交流解答各类技术等问题，社区中发布很多**高质量的.NET安全资源**，可以说市面上很少见，都是干货。

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibEfvTKP231YekyMbc9jeicFuh0aAYDSicAg36pkFaC2P1KW0L5NV1HOssmysrPnrP1fzr2rFOmy8lA/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

## 欢迎加入我们

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
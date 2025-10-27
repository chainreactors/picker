---
title: 扫描 .NET 中的敏感信息，通过 Sharp4FindKeyPlus 获取 machineKey 和数据库密码
url: https://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247498914&idx=1&sn=e420daf3c1f4536bf59e82a80411ce93&chksm=fa59524fcd2edb598dbfab15b98e8b17faa2a78fcc3b834b64eb883f66091dba442140d0b834&scene=58&subscene=0#rd
source: dotNet安全矩阵
date: 2025-02-14
fetch_date: 2025-10-06T20:36:34.316827
---

# 扫描 .NET 中的敏感信息，通过 Sharp4FindKeyPlus 获取 machineKey 和数据库密码

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8ZHZQsw4xAAZvNXjNeMWrwEJHSh8T41Z6HbZK1qYKIgEjzNb9xojSic131dfjfLcyiaATLhtIW8d8w/0?wx_fmt=jpeg)

# 扫描 .NET 中的敏感信息，通过 Sharp4FindKeyPlus 获取 machineKey 和数据库密码

原创

专攻.NET安全的

dotNet安全矩阵

![图片](https://mmbiz.qpic.cn/mmbiz_gif/NO8Q9ApS1YibJO9SDRBvE01T4A1oYJXlTBTMvb7KbAf7z9hY3VQUeayWI61XqQ0ricUQ8G1FykKHBNwCqpV792qg/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp)

在实际操作中，很多 .NET Web 项目配置数据并不总是保存在根目录下的 web.config 文件中。为了更好地满足这种需求，Sharp4FindKeyPlus.exe 能够自动扫描项目目录及其子目录中的多种文件格式，提取潜在的敏感信息。特别是对于 machineKey 的提取，方便后续进行 ViewState 反序列化漏洞攻击。因此，Sharp4FindKeyPlus.exe 成为红队人员和渗透测试团队必不可少的工具之一。

**01. 工具背景介绍**

Sharp4FindKeyPlus.exe 工具的产生源于dot.Net安全矩阵星球微信群群友们的需求：该群友提醒可以在此基础上再加上对machineKey的提取

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8ZHZQsw4xAAZvNXjNeMWrwDyLUtdf4utwwTjyZIyvS6La3YFIlmoOCnfzpts1YeOJHmmOBr4sT3Q/640?wx_fmt=png&from=appmsg)

machineKey 是 .NET Web 应用用来进行加密和验证的关键元素，尤其是在处理 ViewState 数据的序列化和反序列化时。通过获取 machineKey，攻击者可以执行 ViewState 反序列化漏洞攻击，从而获取敏感数据或执行其他恶意操作。

**02. 工具基本介绍**

Sharp4FindKeyPlus.exe 通过扫描项目目录中的配置文件，能够高效地提取出 .NET Web 应用中的敏感信息，显示提取到的数据库连接信息，包含服务器地址、数据库名、用户名、密码等。

此版本最重要是提取到的 machineKey，可用于后续的 ViewState 反序列化攻击。

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8ZHZQsw4xAAZvNXjNeMWrwuqcHtnPcocvuYof7jaUbMvyCia6yUmkW9l74xkIgyZJyC0c3sxOBuAA/640?wx_fmt=jpeg&from=appmsg)

**03. 工具实战用法**

Sharp4FindKeyPlus.exe 的操作非常简单，使用者只需要通过命令行运行即可，工具就会自动扫描并提取其中的敏感信息。

```
```
Sharp4FindKey.exe
```
```

运行该命令后，工具将开始扫描当前路径下的所有子目录和文件，扫描完成后，工具将在控制台中输出提取到的所有敏感信息。

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8ZHZQsw4xAAZvNXjNeMWrwlduhgy8P7NZExn6wYcuC4404JHOcU36nhww393gpOhVlJSib2AICibiaA/640?wx_fmt=png&from=appmsg)

图上已经寻找到包含数据库连接信息和 machineKey 的配置信息，具体内容如下所示。

```
```
<machineKey validationKey="02EFF2E15D7B1A82607716CBB9105205BE39A0BF05766CCC7B4E50F7D02B1DDBDDEA9D83503A82DA93E814F10CF1F892362ECF92DC432E2DE7E036D9A7DE92BA" decryptionKey="2729CB46EDF38EBD9E2BF62BC20706BA21B844442EB95777FA73B4DC84C3603A" validation="HMACSHA256" decryption="AES" compatibilityMode="Framework45" />-
```
```

综上所述，**Sharp4FindKeyPlus.exe** 是一款能够自动扫描配置文件并提取其中的敏感信息，尤其是数据库连接字符串和 machineKey。无论是进行渗透测试、Web 安全审计，还是为红队演练提供支持，都是不可或缺的强力工具。文章涉及的工具已打包在星球，感兴趣的朋友可以加入自取。

**04. 技术精华内容**

从漏洞分析到安全攻防，我们涵盖了 .NET 安全各个关键方面，为您呈现最新、最全面的 .NET 安全知识，下面是公众号发布的精华文章集合，推荐大伙阅读！

[![图片](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8TQhCZMggf71ffibqISJ8f5naPJacnjn0roDyxxnAibmuwDJq2p1GTBpicZhnM9o9gTIu9S9ia8Uqwtw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&retryload=1&tp=webp)](https://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247497498&idx=2&sn=00900a0c29c85b41fe6a586d7e5c3571&scene=21#wechat_redirect)

[![图片](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y9tl26Kh2sQYI9guTCflSwQP8Gs9z7iamicOvlQv4UYzjwd378D03h7yEYFtZ6xA74qicInoed7qpBWg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247495167&idx=1&sn=9280c55fdc7c9146e549be470cf9f120&chksm=fa594312cd2eca04bfe8fd1fd3890b389d9c700b9b69d897f919addac399bab4f4d2e55f6b4f&scene=21#wechat_redirect)

[![图片](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibQ6VpnKYXPqfmHnyJHzHxOeP3ichLEiafhGiawd8mjkHYBalO37fN8QQkNdic1hjjY2Nvw2Bib6UvibDRA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247490722&idx=2&sn=c9807daa5548e139a0c67303cb26882a&chksm=fa5ab24fcd2d3b59a85be03e69c655ffd644e8458bc2ec3f572da4b40b43e5003fda756f35b4&scene=21#wechat_redirect)

[![图片](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibQ6VpnKYXPqfmHnyJHzHxOjWgak8cI7Mic1wTt3YSKqsbLl9rPe0cF9WGtOEuiceLreTNtNVib6IKlw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247490703&idx=2&sn=e7db1ff662e5b41d9a1806fbdf33e204&chksm=fa5ab262cd2d3b7470f029b9a07d1dd3611e63be910b01a601144efe7d84b5f016f488a354cf&scene=21#wechat_redirect)

[![图片](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibQ6VpnKYXPqfmHnyJHzHxO8jJ97qqWlY6XR03DqSnutcHFYibDtVG5Y2wEaK4p2bzEicZblY4oQyGg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247490700&idx=2&sn=e8a865ada7c743e77fb9e953c5da74b1&chksm=fa5ab261cd2d3b7736387eddfc8524a378a1604552d0c9b55476646f9e8275f48818aab8acad&scene=21#wechat_redirect)

[![图片](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibQ6VpnKYXPqfmHnyJHzHxOe1viaia4aoFceunsUdIna4DPbmemW1EqlBMrovOoE6bdAFF3iaApxz5qA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247488736&idx=2&sn=d24aaa297c51eb620ccdf67af513086d&chksm=fa5aba0dcd2d331bbb22f3f5657199d718c90efed42fcb9cb67ec23d342f887c117e4858f1cb&scene=21#wechat_redirect)

**05. 加入安全社区**

目前dot.Net安全矩阵星球已成为中国.NET安全领域最知名、最专业的技术知识库之一，超 **1200+** 成员一起互动学习。星球主题数量近 **600+**，精华主题 230+，PDF文档和压缩包 300+ 。从Web应用到PC端软件应用，无论您是初学者还是经验丰富的开发人员，都能在这里找到对应的实战指南和最佳实践。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y9AiaXibTRdEnEfYuQx76FjZVjmyEWtIaDuDePFFmyRqggiaq2k47pLoib9GZtUCOhaP40WPlhvbiaKZVg/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

## 20+专栏文章

星球文化始终认为授人以鱼不如授人以渔！星球整理出**20+**个专题栏目涵盖 **.NET安全 点、线、面、体等知识范围**，助力师傅们实战攻防！其中主题包括.NET  内网攻防、漏洞分析、内存马、代码审计、预编译、反序列化、WebShell免杀、命令执行、工具库等等。

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
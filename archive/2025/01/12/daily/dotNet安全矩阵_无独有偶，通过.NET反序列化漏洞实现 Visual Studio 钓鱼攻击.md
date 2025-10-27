---
title: 无独有偶，通过.NET反序列化漏洞实现 Visual Studio 钓鱼攻击
url: https://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247498152&idx=3&sn=a45de16edbca5168f73ea7ed4ffeca36&chksm=fa595745cd2ede53cd0f763edff055aeced78d85bdeea1f2be5fd2d80d72a65ed86e0df928f3&scene=58&subscene=0#rd
source: dotNet安全矩阵
date: 2025-01-12
fetch_date: 2025-10-06T20:09:18.131538
---

# 无独有偶，通过.NET反序列化漏洞实现 Visual Studio 钓鱼攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8Db8KbC6Q8iclZNYFiazrmanYSJzkYh9t0DvGcVWMVvia8GLcDtz0oKTiajNbJH7IcicfRSbic28qNqxqw/0?wx_fmt=jpeg)

# 无独有偶，通过.NET反序列化漏洞实现 Visual Studio 钓鱼攻击

原创

专攻.NET安全的

dotNet安全矩阵

近期，网络安全从业人员间流传着一个引起广泛关注的事件：某提权工具被植入后门，导致工具使用者的身份信息和敏感数据遭到泄露。根据现有的信息，初步判断此次攻击背后可能是东南亚某APT组织——海莲花（Lotus Blossom）所为。

Visual Studio（VS）是微软开发的集成开发环境（IDE），广泛应用于软件开发，尤其是.NET平台应用程序的开发。然而，正因为其广泛的使用，攻击者往往利用开发工具的弱点进行精准的网络攻击。

此次攻击的基本原理是攻击者向受害者的Visual Studio工程中投递了一个恶意 .suo 文件，该文件为项目隐藏文件，每次打开工程后都会对该文件做一次覆盖写入操作，因此具有非常强的隐蔽性。

无独有偶，黑客还可以通过一种新的攻击方式，利用Visual Studio项目文件（如 .sln 或 .csproj 文件）中的资源文件（.resx），成功发起定向攻击。这种攻击方式的特点在于，攻击者不需要直接编译项目代码，而是通过打开项目文件来触发攻击。

01

新的攻击方法概述

攻击者通过将恶意载荷嵌入到Visual Studio的资源文件（.resx文件）中，并将该文件添加到项目中。当开发人员打开Visual Studio项目文件（如 .sln 或 .csproj 文件）时，Visual Studio会自动加载该资源文件。此时，恶意的反序列化载荷将被触发，从而执行攻击者的代码。

这种攻击方式依赖于.NET的反序列化漏洞。攻击者利用对象的反序列化机制，将恶意构造的对象嵌入到 .resx 文件中。一旦项目被打开，恶意的对象将在项目加载时被反序列化，并执行预定的恶意操作。

**1.1 资源文件内容**

在此攻击中，攻击者会将恶意代码作为一个二进制数据块（通常使用base64编码）嵌入 .resx 文件中的 data 元素。例如，以下是恶意 .resx 文件的一部分：

```
```
<data name="test" mimetype="application/x-microsoft.net.object.binary.base64">
  <value>AAEAAAD/////AQAAAAAAAAAMAgAAAElTeXN0ZW0sIFZlcnNpb249NC4wLjAuMCwgQ3VsdHVyZT1uZXV0cmFsLCBQdWJsaWNLZXlUb2tlbj1iNzdhNWM1NjE5MzRlMDg5BQEAAACEAVN5c3RlbS5Db2xsZWN0aW9ucy5HZW5lcmljLlNvcnRlZFNldGAxW1tTeXN0ZW0uU3RyaW5nLCBtc2NvcmxpYiwgVmVyc2lvbj00LjAuMC4wLCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPWI3N2E1YzU2MTkzNGUwODldXQQAAAAFQ291bnQIQ29tcGFyZXIHVmVyc2lvbgVJdGVtcwADAAYIjQFTeXN0ZW0uQ29sbGVjdGlvbnMuR2VuZXJpYy5Db21wYXJpc29uQ29tcGFyZXJgMVtbU3lzdGVtLlN0cmluZywgbXNjb3JsaWIsIFZlcnNpb249NC4wLjAuMCwgQ3VsdHVyZT1uZXV0cmFsLCBQdWJsaWNLZXlUb2tlbj1iNzdhNWM1NjE5MzRlMDg5XV0IAgAAAAIAAAAJAwAAAAIAAAAJBAAAAAQDAAAAjQFTeXN0ZW0uQ29sbGVjdGlvbnMuR2VuZXJpYy5Db21wYXJpc29uQ29tcGFyZXJgMVtbU3lzdGVtLlN0cmluZywgbXNjb3JsaWIsIFZlcnNpb249NC4wLjAuMCwgQ3VsdHVyZT1uZXV0cmFsLCBQdWJsaWNLZXlUb2tlbj1iNzdhNWM1NjE5MzRlMDg5XV0BAAAAC19jb21wYXJpc29uAyJTeXN0ZW0uRGVsZWdhdGVTZ...
</value>
</data>
```
```

上面的 base64 编码的值代表着攻击者构造的恶意对象，这些对象会在反序列化时执行特定的命令或载荷。

**1.2 整体执行过程**

通过将恶意构造的对象注入到 .resx 文件中，攻击者可以在开发者打开项目文件时触发反序列化过程，执行恶意代码，具体执行步骤可参考如下。

## 构造恶意 .resx 文件

攻击者首先构造一个恶意的 .resx 文件，该文件包含一个 data 元素，其中嵌入了恶意的反序列化对象。为了确保反序列化漏洞能够成功触发，恶意对象通常会以 application/x-microsoft.net.object.binary.base64 类型进行编码，构造好的载荷如下图所示。

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8Db8KbC6Q8iclZNYFiazrmanIiac4XMlHU7lF9QpmhbTC6F7nyUVDQic2XH89Kk9nRs3YMVHKuIWEHMw/640?wx_fmt=png&from=appmsg)

## 将恶意文件添加到项目

攻击者将该恶意 .resx 文件添加到目标项目的资源目录中，并修改 .sln 或 .csproj 文件，使得该资源文件能够在打开项目时被加载。

## 触发反序列化漏洞

一旦受害者打开该项目文件，Visual Studio会自动加载 .resx 资源文件，并执行反序列化操作。这时，恶意的反序列化对象将被激活，并执行攻击者预设的恶意代码。例如，攻击者可以通过反序列化漏洞执行远程代码、窃取敏感信息，甚至完全控制受害者的机器。

02

资源文件加载工具

攻击者并不需要对目标项目文件进行复杂的修改，只需在项目中插入恶意资源文件或修改项目配置文件，攻击就能够成功触发，我们已经在星球给出了概念性的验证项目 Sharp4VS2022RCE，如下图所示。

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8Db8KbC6Q8iclZNYFiazrmanOibzgKL8jLGl1FyHfMMR2653Z765b4p21cFEC5MjGxuYY2ATMQR8QBQ/640?wx_fmt=jpeg&from=appmsg)

当受害者打开 Sharp4VS2022RCE 项目时，Visual Studio会自动加载该资源文件，并触发反序列化漏洞，进而执行攻击者事先设置好的反序列化 payload，导致系统被控制。

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8Db8KbC6Q8iclZNYFiazrman66LAM3xJ70wUicnXbpc5WMZtUr7LyicwJA0IMYuEY163Mm3vIiamQhOdA/640?wx_fmt=png&from=appmsg)

综上，这类针对Visual Studio的反序列化攻击通过将恶意对象嵌入到 .resx 资源文件中，利用安全研究人员在打开项目时的反序列化漏洞执行恶意代码。作为网络安全人员，我们需要对这种隐蔽的攻击方式保持警惕，并采取有效的防范措施，以保护我们的代码和数据免受威胁。文章涉及的工具已打包在星球，感兴趣的朋友可以加入自取。

03

公众号安全技术精华内容

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

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y9AiaXibTRdEnEfYuQx76FjZVjmyEWtIaDuDePFFmyRqggiaq2k47pLoib9GZtUCOhaP40WPlhvbiaKZVg/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

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

dotNet安全矩阵星球从创建以来一直聚焦于.NET领域的安全攻防技术，定位于高质量安全攻防星...
---
title: 一种通过 .NET 启动 cmd.exe 的新方法
url: https://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247498306&idx=3&sn=d5276b7bf7380ce889dc125627631a94&chksm=fa5954afcd2eddb9766ec4e35c05e11ccf9f4e97162811fc15396171a733e0531e29cabee253&scene=58&subscene=0#rd
source: dotNet安全矩阵
date: 2025-01-19
fetch_date: 2025-10-06T20:09:06.234353
---

# 一种通过 .NET 启动 cmd.exe 的新方法

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y81ssibGribdYSOgqyk7F9eL250nFl7g5Vj653EskXtlibNrThRNWZrIIXUpELKia4mH6sPCucAibCyzibQ/0?wx_fmt=jpeg)

# 一种通过 .NET 启动 cmd.exe 的新方法

原创

专攻.NET安全的

dotNet安全矩阵

![](https://mmbiz.qpic.cn/mmbiz_gif/NO8Q9ApS1YibJO9SDRBvE01T4A1oYJXlTBTMvb7KbAf7z9hY3VQUeayWI61XqQ0ricUQ8G1FykKHBNwCqpV792qg/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp)

Sysnative 路径是Windows操作系统中一个非常有用的特性，它解决了32位应用程序在64位系统中访问系统目录时的路径重定向问题。通过利用这一特性，红队渗透时可以实现一些新的功能和绕过防御，如启动64位CMD等。

**01. 相关背景介绍**

最近正在看日志目录下的 System.evtx 文件，该文件的绝对地址如下所示，使用Everything发现确实存在。

```
```
C:\Windows\System32\winevt\Logs\System.evtx
```
```

但是，当用 .NET 默认的 File.Exists 方法去判断时，却得到的结果是false，这个结果显然不符合预期，如下图所示。

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y81ssibGribdYSOgqyk7F9eL2LhibPribRVTGRnFmJuTYddau4rwQO9cpgTiaNib9d3QM2sXxicL8Vq1ibI1Q/640?wx_fmt=png&from=appmsg)

接着，将该问题发到dot.Net安全矩阵专属成员群里和朋友们互动，大家大概从权限、被占用、路径等问题去讨论交流，如下图所示。

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y81ssibGribdYSOgqyk7F9eL2RD8pldxsEPqIs2KYOa3AZHOutcXmJrL06bD8tKKUYBscJ0eVia1RicZw/640?wx_fmt=png&from=appmsg)

经过研究后，发现是由于 Windows 系统下的 Sysnative路径造成的。

**02. Sysnative路径**

Sysnative是一个特殊的虚拟路径，仅在64位Windows操作系统中存在，并且仅对32位应用程序可见。

当32位应用程序尝试访问C:\Windows\Sysnative时，系统会自动将其重定向到实际的64位系统目录C:\Windows\System32。

这一特性使得32位应用程序能够无缝访问64位系统目录中的资源，解决了路径重定向带来的问题。另外，Sysnative 路径在Windows Vista 版本后已默认提供，详情如下图所示。

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y81ssibGribdYSOgqyk7F9eL2IUd8ON5SrnlYNIZIwuSouRwFJQjZKibvXORfQw748iaQBGicE2pec4TZA/640?wx_fmt=png&from=appmsg)

**03. 实战对抗用法**

利用Sysnative路径，我们可以实现一种启动CMD的新方法。传统上，32位应用程序启动CMD通常是通过访问 C:\Windows\System32\cmd.exe

实际上会被重定向到C:\Windows\SysWOW64\cmd.exe，即32位CMD，然而，通过指定C:\Windows\Sysnative\cmd.exe，32位应用程序可以成功启动64位CMD。

以下是一个简单的 .NET 代码示例，展示了如何使用 Sysnative 路径启动CMD进程。

```
```
using System.Diagnostics;

class Program
{
    static void Main()
    {
        Process.Start("C:\\Windows\\Sysnative\\cmd.exe");
    }
}
```
```

这段代码将在64位Windows操作系统上成功启动一个64位的CMD。这对于需要执行64位命令或脚本的32位应用程序来说，是一个非常有用的技巧。

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y81ssibGribdYSOgqyk7F9eL2RMemfBgkWicr2hmRuUmeEjh1u7TF1NibjuXjNbbdeibvkoXYmoTlzCrPQ/640?wx_fmt=png&from=appmsg)

**04. 更改IIS运行配置**

当32位应用程序尝试访问C:\\Windows\\System32时，实际上会被重定向到C:\\Windows\\SysWOW64，这是因为System32目录包含了64位系统文件，而SysWOW64包含了32位系统文件。

IIS 10可以配置为以32位或64位模式运行应用程序，因此，如果应用程序池配置为 [ 启用32位应用程序 ]，则在该池下运行的所有应用程序都将作为32位进程运行，具体的配置如下所示。

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y81ssibGribdYSOgqyk7F9eL2vib7ibpsVVTqJZmoicRt4mVL9tecI8D5lGK3FT2anuNt7CYQc2x1kRjUA/640?wx_fmt=png&from=appmsg)

如果IIS 10中通过 aspx 调用 C:\\Windows\\Sysnative\\cmd.exe不成功的话，通常与应用程序池的位数配置有关，否则会正常启动，如下图所示。

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y81ssibGribdYSOgqyk7F9eL2muV1KXl5ic2YXpEmqadV6KcdvyCJXMTXAQqQfLgOhdcBPs2jXf2Ob5g/640?wx_fmt=png&from=appmsg)

**05. 应用场景讨论**

Sysnative路径的这一特性引起了群友们广泛的讨论和关注。开发者们开始探索其在各种场景下的应用，包括但不限于计划任务、LOLBIN、兼容性。

1. 在计划任务中使用Sysnative路径可以确保即使任务是由32位程序触发的，也能执行64位的命令或脚本。

2. 在渗透测试中，攻击者可以利用Sysnative路径绕过某些安全限制，执行系统自带的64位工具。

3. 对于需要在32位和64位系统上同时运行的程序，Sysnative路径提供了一种统一的方式来访问系统目录中的文件。

然而，需要注意的是，Sysnative路径是一个非公开的特性，其未来可用性可能会受到Windows更新的影响。因此，在依赖这一特性时，开发者应谨慎考虑其潜在的风险和不确定性。

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y81ssibGribdYSOgqyk7F9eL2NNySrrmMMkG2glSN89pniahiaojGmNdTF6vS0GJHaajVJfQuUD6ujJWQ/640?wx_fmt=jpeg&from=appmsg)

文章涉及的概念性验证工具已打包在星球，感兴趣的朋友可以加入自取。

**06. 技术精华内容**

从漏洞分析到安全攻防，我们涵盖了 .NET 安全各个关键方面，为您呈现最新、最全面的 .NET 安全知识，下面是公众号发布的精华文章集合，推荐大伙阅读！

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8TQhCZMggf71ffibqISJ8f5naPJacnjn0roDyxxnAibmuwDJq2p1GTBpicZhnM9o9gTIu9S9ia8Uqwtw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&retryload=1&tp=webp)](https://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247497498&idx=2&sn=00900a0c29c85b41fe6a586d7e5c3571&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y9tl26Kh2sQYI9guTCflSwQP8Gs9z7iamicOvlQv4UYzjwd378D03h7yEYFtZ6xA74qicInoed7qpBWg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247495167&idx=1&sn=9280c55fdc7c9146e549be470cf9f120&chksm=fa594312cd2eca04bfe8fd1fd3890b389d9c700b9b69d897f919addac399bab4f4d2e55f6b4f&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibQ6VpnKYXPqfmHnyJHzHxOeP3ichLEiafhGiawd8mjkHYBalO37fN8QQkNdic1hjjY2Nvw2Bib6UvibDRA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247490722&idx=2&sn=c9807daa5548e139a0c67303cb26882a&chksm=fa5ab24fcd2d3b59a85be03e69c655ffd644e8458bc2ec3f572da4b40b43e5003fda756f35b4&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibQ6VpnKYXPqfmHnyJHzHxOjWgak8cI7Mic1wTt3YSKqsbLl9rPe0cF9WGtOEuiceLreTNtNVib6IKlw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247490703&idx=2&sn=e7db1ff662e5b41d9a1806fbdf33e204&chksm=fa5ab262cd2d3b7470f029b9a07d1dd3611e63be910b01a601144efe7d84b5f016f488a354cf&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibQ6VpnKYXPqfmHnyJHzHxO8jJ97qqWlY6XR03DqSnutcHFYibDtVG5Y2wEaK4p2bzEicZblY4oQyGg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247490700&idx=2&sn=e8a865ada7c743e77fb9e953c5da74b1&chksm=fa5ab261cd2d3b7736387eddfc8524a378a1604552d0c9b55476646f9e8275f48818aab8acad&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibQ6VpnKYXPqfmHnyJHzHxOe1viaia4aoFceunsUdIna4DPbmemW1EqlBMrovOoE6bdAFF3iaApxz5qA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247488736&idx=2&sn=d24aaa297c51eb620ccdf67af513086d&chksm=fa5aba0dcd2d331bbb22f3f5657199d718c90efed42fcb9cb67ec23d342f887c117e4858f1cb&scene=21#wechat_redirect)

**07. 加入安全社区**

目前dot.Net安全矩阵星球已成为中国.NET安全领域最知名、最专业的技术知识库之一，超 **1200+** 成员一起互动学习。星球主题数量近 **600+**，精华主题 230+，PDF文档和压缩包 300+ 。从Web应用到PC端软件应用，无论您是初学者还是经验丰富的开发人员，都能在这里找到对应的实战指南和最佳实践。

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y9AiaXibTRdEnEfYuQx76FjZVjmyEWtIaDuDePFFmyRqggiaq2k47pLoib9GZtUCOhaP40WPlhvbiaKZVg/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

## 7.1 20+专栏文章

星球文化始终认为授人以鱼不如授人以渔！星球整理出**20+**个专题栏目涵盖 **.NET安全 点、线、面、体等知识范围**，助力师傅们实战攻防！其中主题包括.NET  内网攻防、漏洞分析、内存马、代码审计、预编译、反序列化、WebShell免杀、命令执行、工具库等等。

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8xRheDpQ7NsESosdNZUopa90SJRuwnLy9uZV4icrXiaZlJPQlYJWXTw8HCrF9oTcE3DDgrdFnXo2BA/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

## 7.2 海量资源和工具

截至当前，dot.Net安全矩阵星球社区汇聚了 **600+** 个实用工具和高质量PDF学习资料。这些资源涵盖了攻防对抗的各个方面，在实战中能够发挥显著作用，为对抗突破提供强有力的支持。

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8xRheDpQ7NsESosdNZUopaqVZW8XsALVA4FNiaj32q8npN82VSeqSKb4fQvLiczFNs0099VRFVQwPA/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8xRheDpQ7NsESosdNZUopa63ZXbX3YXLwoeNnjStcRtTbU9hoe6ecO5hhkj2apG1I6tKlkpz5GaQ/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

## 7.3 专属成员交流群

我们还有多个成员专属的**内部星球陪伴群**，加入的成员可以通过在群里提出问题或参与论的方式来与其他成员交流思想和经验。此外还可以通过星球或者微信群私聊向我们进行提问，以获取帮助迅速解决问题。

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8xRheDpQ7NsESosdNZUopaAiaouHb6HYza539m9v0ykDoD2JezaArDZBPlJInuabf6XsduzVcjZ0Q/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

## 7.4 已入驻的大咖们

星球汇聚了各行业安全攻防技术大咖，并且每日分享.NET安全技术干货以及交流解答各类技术等问题，社区中发布很多**高质量的.NET安全资源**，可以说市面上很少见，都是干货。

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibEfvTKP231YekyMbc9jeicFuh0aAYDSicAg36pkFaC2P1KW0L5NV1HOssmysrPnrP1fzr2rFOmy8lA/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

## 7.5 欢迎加入我们

dotNet安全矩阵星球从创建以来一直聚焦于.NET领域的安全攻防技术，定位于高质量安全攻防星球社区，也得到了许多师傅们的支持和信任，通过星球深度连接入圈的师傅们，一起推动.NET安全高质量的向前发展。**星球门票后期价格随着内容和质量的不断沉淀会适当提高，因此越早加入越好！**

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8xRheDpQ7NsESosdNZUopag09JtYcKpucjZPAlfeqC1ovcQvhrkemAzbURDaVF3InmpQshiatDnyQ/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/NO8...
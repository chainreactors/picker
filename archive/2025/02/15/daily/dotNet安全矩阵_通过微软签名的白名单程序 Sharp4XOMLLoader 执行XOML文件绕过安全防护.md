---
title: 通过微软签名的白名单程序 Sharp4XOMLLoader 执行XOML文件绕过安全防护
url: https://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247498923&idx=1&sn=4e6c1ea22c62d8d700b3beada14bbfe2&chksm=fa595246cd2edb501712ff22ee94bbe46fe3f7235f4eed102051bb3dac1fbdb01c7e23126717&scene=58&subscene=0#rd
source: dotNet安全矩阵
date: 2025-02-15
fetch_date: 2025-10-06T20:37:07.067688
---

# 通过微软签名的白名单程序 Sharp4XOMLLoader 执行XOML文件绕过安全防护

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8ZHZQsw4xAAZvNXjNeMWrwULztlthzRniaJpYKGPnSWIP8ibIXetchc8pDeGYpiaTZEnKnwVeJ3ia1JA/0?wx_fmt=jpeg)

# 通过微软签名的白名单程序 Sharp4XOMLLoader 执行XOML文件绕过安全防护

原创

专攻.NET安全的

dotNet安全矩阵

![图片](https://mmbiz.qpic.cn/mmbiz_gif/NO8Q9ApS1YibJO9SDRBvE01T4A1oYJXlTBTMvb7KbAf7z9hY3VQUeayWI61XqQ0ricUQ8G1FykKHBNwCqpV792qg/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp)Sharp4XOMLLoader.exe是一款用于执行嵌入在XOML中.NET代码的工具。由于该程序自带微软的数字签名，能够有效的绕过杀毒软件的监控，执行潜在的恶意代码，同时，该技术利用了XOML的合法性以及系统中对白名单程序的高度信任，使得恶意代码的执行更加隐蔽，难以被检测和阻止。

**01. 详解XOML文件**

XOML文件是一种基于XML的文件格式，专用于定义和描述 WF 中的工作流程。通过XOML文件，可以指定WF工作流的结构、活动及其行为，而无需在.cs文件中编写大量的代码。
通常一个典型的XOML文件和WPF里的XAML文件基本一致，以下是一段XOML文件的示例代码，主要展示了一个简单的顺序工作流程。包括以下几个主要部分。

```
```
<SequentialWorkflowActivity x:Class="MyWorkflow" x:Name="foobarx"
 xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
 xmlns="http://schemas.microsoft.com/winfx/2006/xaml/workflow">
  <SequentialWorkflowActivity Enabled="False">
  </SequentialWorkflowActivity>
</SequentialWorkflowActivity>
```
```

SequentialWorkflowActivity是.NET早期的版本中XOML文件的根元素，定义了一个顺序工作流程。顺序工作流程意味着各个活动将按照它们在文件中的顺序依次执行。

x:Class属性指定了工作流程的类名：MyWorkflow，x:Name属性为工作流程实例指定了一个名称叫foobarx。xmlns 和 xmlns:x 用于声明XAML和工作流程相关的命名空间，这是为了确保XOML文件中的元素和属性能够正确地映射到.NET Framework中的类型和成员。

值得一提的是，XOML文件通过`xml<x:Code>`标签，可以在XOML文件中直接嵌入.NET代码，从而在工作流程执行过程中启动winver.exe进程。具体如下所示。

```
```
<x:Code>
      Object test = System.Diagnostics.Process.Start("cmd.exe", "/c winver");
</x:Code>
```
```

因为程序自带微软签名，如果把winver.exe换成启动恶意木马的进程，通过该工具能够绕过反病毒软件的监控，执行恶意代码。

**02. 工具实战操作**

Sharp4XOMLLoader.exe 便是这样一款执行 XOML中的 Shellcode 的工具。因为程序自带微软签名，因此通过该工具能够绕过反病毒软件的监控，执行恶意代码。

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8ZHZQsw4xAAZvNXjNeMWrwsf8XfKoSmsc7MttOEQaP6TU3kkgIIialIEhVjFBmsCia0ETzjJ08M2fg/640?wx_fmt=png&from=appmsg)

## 2.1 工具用法

只需替换掉base64编码的Shellcode即可，Sharp4XOMLLoader 工具允许通过命令行传递参数来加载并执行 XOML 文件，命令如下所示。

```
```
Sharp4XOMLLoader.exe /debug:- Shellcode.xoml
```
```

其中的 /debug:- 参数用于指定不生成其他附属调试文件，确保执行过程的隐蔽性，shellcode.xoml: 是包含了要执行的 shellcode 的 XOML 文件，执行完成后返回了运行成功后的cmd.exe。

如下图所示："Microsoft Windows [版本 10.0.19045.4780](c) Microsoft Corporation。保留所有权利。"

![图片](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8HibppicvjAs3FBwutvmB8d3eEtYnoOkxnL9pwFqJJ5iclCtku9IKibsG9ib3tVPzPAV1bYIaobdaze3A/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**03. 加载器原理分析**

当 Sharp4XOMLLoader.exe 编译 XOML 文件时，依赖于内部的编译器组件和多个辅助类来完成整个编译流程。这些组件和方法共同作用，最终将 XOML 文件编译成可执行的 .NET 程序集。打开dnspy.exe，在调试参数处输入 1.xoml

当 Sharp4XOMLLoader.exe 编译 XOML 文件时，依赖于内部的编译器组件和多个辅助类来完成整个编译流程。这些组件和方法共同作用，最终将 XOML 文件编译成可执行的 .NET 程序集。打开dnspy.exe，在调试参数处输入 1.xoml

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8ZHZQsw4xAAZvNXjNeMWrwsks1EkdLNO3icF7joxEzs0Xp6rDfY3ul7MVcCKibPtibia3nrPqXeibibgJw/640?wx_fmt=png&from=appmsg)

AppDomain.CreateInstanceAndUnwrap 方法在独立的 AppDomain 中创建 WorkflowCompilerInternal 的对象。这种方法可以隔离编译过程，确保编译操作不会影响其他应用程序域的状态。

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8ZHZQsw4xAAZvNXjNeMWrwhPORVAiczF6mpj9kMK5QdVkqpMwf5taNfo4jHbsNkD9SjXX3zxm4icJQ/640?wx_fmt=png&from=appmsg)

其实，workflowCompilerInternal.Compile 方法是实际执行编译的核心步骤，parameters 包含了编译所需的配置和选项，files 则是待编译的 XOML 文件。随后，通过GenerateLocalAssembly方法编译生成了一个临时的dll文件，通常路径位于：

```
```
@C:\Users\User\AppData\Local\Temp\oi0a1mun\1.dll
```
```

接着，XomlCompilerHelper.InternalCompileFromDomBatch 方法被调用，用于处理 XOML 文件的具体编译，如下图所示。

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8ZHZQsw4xAAZvNXjNeMWrwmR6HkZVM6CgYsfXpSsOZibaAHw44hylgNz7ICiaCRTt7prmicfGBRH2Cg/640?wx_fmt=png&from=appmsg)

最终，Sharp4XOMLLoader.exe 经过一系列的方法调用触发命令执行，从而启动winver.exe进程。如下图所示。

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8ZHZQsw4xAAZvNXjNeMWrwiaUicP6rek9NsRYgrxjPOz99K28K52kEBg8xcMnhtXogLsibdwb707mOw/640?wx_fmt=png&from=appmsg)

综上所述，Sharp4XOMLLoader.exe工具凭借微软数字签名的掩护，巧妙地绕过安全防线，执行XOML文件内嵌的.NET恶意代码。其利用XOML的合法身份及系统对信任程序的宽松态度，实现了恶意行为的高度隐蔽性。文章涉及的工具已打包在星球，感兴趣的朋友可以加入自取。

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

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibEfvTKP231YekyMbc9jeicFuh0aAYDSicA...
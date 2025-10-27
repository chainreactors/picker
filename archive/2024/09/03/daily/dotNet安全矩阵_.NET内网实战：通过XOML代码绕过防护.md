---
title: .NET内网实战：通过XOML代码绕过防护
url: https://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247494961&idx=2&sn=8cf5ab24af4dff58b334065e332c870b&chksm=fa5943dccd2ecacaaf9164584040cef3bab12aadef84fd1216b444c98ad6ba9fcd9bcae5f667&scene=58&subscene=0#rd
source: dotNet安全矩阵
date: 2024-09-03
fetch_date: 2025-10-06T18:26:14.631712
---

# .NET内网实战：通过XOML代码绕过防护

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8g70WSk5ibViagFgQ8Sj8tUmtDsrXMxdn8rVS4KJFKM0wicTPoAiawTq8nxalJHazYRH3bmeflxx9Fdw/0?wx_fmt=jpeg)

# .NET内网实战：通过XOML代码绕过防护

原创

专攻.NET安全的

dotNet安全矩阵

01

阅读须知

此文所节选自小报童《.NET 内网实战攻防》专栏，主要内容有.NET在各个内网渗透阶段与Windows系统交互的方式和技巧，对内网和后渗透感兴趣的朋友们可以订阅该电子报刊，解锁更多的报刊内容。

02

基本介绍

本文内容部分节选自小报童《.NET 通过执行XOML文件代码绕过安全防护》，完整的文章内容请加入小报童后订阅查看。现在限时只需59元，永久买断！目前已有200+位朋友抢先预定，我们会长期更新，对.NET内网安全的朋友们请尽快订阅该报刊！

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8g70WSk5ibViagFgQ8Sj8tUmibUQfUWQZ5W0xE1l8NhyFXqIEWfVzQoO8Mva0OIiaT46sdarawHXI16g/640?wx_fmt=png&from=appmsg)

03

编码实现

在红队活动往往需要考虑如何在实际环境中绕过防御机制，启动木马进程。今天，我们将深入探讨一种较少被提及但非常有趣的技术—利用XOML执行.NET代码。由于该程序自带微软的数字签名，它能够绕过杀毒软件的监控，执行潜在的恶意代码。该技术利用了XOML的合法性以及系统中对白名单程序的高度信任，使得恶意代码的执行更加隐蔽，难以被检测和阻止。

## 3.1 XOML文件是什么

XOML文件是一种基于XML的文件格式，专用于定义和描述Windows Workflow Foundation (WF) 中的工作流程。通过XOML文件，可以指定WF工作流的结构、活动及其行为，而无需在.cs文件中编写大量的代码。

通常一个典型的XOML文件和WPF里的XAML文件基本一致，以下是一段XOML文件的示例代码，主要展示了一个简单的顺序工作流程。包括以下几个主要部分

```
<SequentialWorkflowActivity x:Class="MyWorkflow" x:Name="foobarx"
 xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
 xmlns="http://schemas.microsoft.com/winfx/2006/xaml/workflow">
  <SequentialWorkflowActivity Enabled="False">
  </SequentialWorkflowActivity>
</SequentialWorkflowActivity>
```

上述XML代码中，<SequentialWorkflowActivity> 是.NET早期的版本中XOML文件的根元素，定义了一个顺序工作流程。顺序工作流程意味着各个活动将按照它们在文件中的顺序依次执行。

x:Class属性指定了工作流程的类名：MyWorkflow，x:Name属性为工作流程实例指定了一个名称叫foobarx。xmlns和xmlns:x用于声明XAML和工作流程相关的命名空间，这是为了确保XOML文件中的元素和属性能够正确地映射到.NET Framework中的类型和成员。

值得一提的是，XOML文件通过<x:Code>标签，可以在XOML文件中直接嵌入.NET代码，从而在工作流程执行过程中启动winver.exe进程。具体如下所示。

```
<x:Code>
      Object test = System.Diagnostics.Process.Start("cmd.exe", "/c winver");
 </x:Code>
```

## 3.2 调试分析

当编译 XOML 文件时，依赖于内部的编译器组件和多个辅助类来完成整个编译流程。这些组件和方法共同作用，最终将 XOML 文件编译成可执行的 .NET 程序集。打开dnspy.exe，在调试参数处输入 1.xoml。

首先使用 AppDomain.CreateInstanceAndUnwrap 方法在独立的 AppDomain 中创建 WorkflowCompilerInternal 的对象。

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8g70WSk5ibViagFgQ8Sj8tUm8SLwOa6wgx9kKlQN9PGc4GAsc1icVcR4sRn79LkGj72JWGMTibwVGpfg/640?wx_fmt=other&from=appmsg)

接着，XomlCompilerHelper.InternalCompileFromDomBatch 方法被调用，用于处理 XOML 文件的具体编译，如下图所示。

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8g70WSk5ibViagFgQ8Sj8tUmiaybGgQZfBAjo4pUgC43daV2MHtw4ia1ZyIRKC8HVFv2eibzqCbxyaOBg/640?wx_fmt=other&from=appmsg)

最终，Sharp4XOMLLoader 通过 Activator使用反射机制创建该类型的实例，并将其作为 Activity 对象返回，从而触发.NET代码执行启动winver.exe。如下图所示。

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8g70WSk5ibViagFgQ8Sj8tUmcge9HfELSmLTYTrHVH0B35o0viavLiaiaT13AIqPPl87CBtVyHP1R3hJw/640?wx_fmt=other&from=appmsg)

综上，凭借微软数字签名的掩护，巧妙地绕过安全防线，执行XOML文件内嵌的.NET恶意代码。其利用XOML的合法身份及系统对信任程序的宽松态度，实现了恶意行为的高度隐蔽性。

04

**欢迎加入.NET 电子报刊**

我们的小报童电子报刊【.NET内网安全攻防】也开始运营，引入小报童也是为了弥补知识星球对于轻量级阅读支持的不足，为用户读者提供更佳的阅读体验。如果您对阅读体验的需求比较高，那么可以订阅这个专栏。

本次电子报刊《.NET 内网安全攻防》专栏，内容主要有.NET在各个内网渗透阶段与Windows系统交互的方式和技巧，可细分为以下8个方向。

```
1） .NET 安全防御绕过
2） .NET 本地权限提升
3） .NET 内网信息收集
4） .NET 内网代理通道
5） .NET 内网横向移动
6） .NET 目标权限维持
7） .NET 数据传输外发
8） .NET 目标痕迹清理
```

原价899，现在限时只需59元，永久买断！目前已有200+位朋友抢先预定，我们会长期更新，初步计划保持每周更新1-2篇新内容，对.NET内网安全的朋友们请尽快订阅该报刊！![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibeicvDNVldcXTgRnFUFTwOqfTleogJThU7kCaZJuuU2BLVLYluu6CFV7BX458AxBcd93ickZ0rmOqQ/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

每增加五十人涨价10元，抓紧订阅，超值！订阅后请关注公众号：dotNet安全矩阵，发送订单截图和您的微信号，邀请您加入专属交流群。感兴趣的朋友，可以点击链接：https://xiaobot.net/p/dotNetAttack，或者扫描下方海报微信二维码加入即可，订阅后小报童定时会将最新内容通过微信推送给您。

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8g70WSk5ibViagFgQ8Sj8tUmOzzGX6ic8Cs2icOPBHibOcQLqsC73tF9H9cl8JkU0DIOYj6hXicXyCfoeg/640?wx_fmt=jpeg&from=appmsg)

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
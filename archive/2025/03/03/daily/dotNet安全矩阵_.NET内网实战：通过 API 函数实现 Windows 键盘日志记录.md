---
title: .NET内网实战：通过 API 函数实现 Windows 键盘日志记录
url: https://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247499035&idx=1&sn=8698ae938bdaabdebb9271616ae4ab84&chksm=fa5953f6cd2edae09eb5e8f15567550f4f56eb459e73fb4afe3870ea23c0838084e51c6fe9ca&scene=58&subscene=0#rd
source: dotNet安全矩阵
date: 2025-03-03
fetch_date: 2025-10-06T21:56:37.730396
---

# .NET内网实战：通过 API 函数实现 Windows 键盘日志记录

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y9pqv2licn4Pp8qgoheytreD621QVaM8SmyGFAWFTXamvsKNtXObOicjkS7qXUUb6k6dImeFbfYHxng/0?wx_fmt=jpeg)

# .NET内网实战：通过 API 函数实现 Windows 键盘日志记录

原创

专攻.NET安全的

dotNet安全矩阵

01

阅读须知

此文所节选自小报童《.NET 内网实战攻防》专栏，主要内容有.NET在各个内网渗透阶段与Windows系统交互的方式和技巧，对内网和后渗透感兴趣的朋友们可以订阅该电子报刊，解锁更多的报刊内容。

02

基本介绍

本文内容部分节选自小报童《.NET 通过伪造文件时间戳实现痕迹清理》，完整的文章内容请加入小报童后订阅查看。现在限时只需59元，永久买断！目前已有300+位朋友抢先预定，我们会长期更新，对.NET内网安全的朋友们请尽快订阅该报刊！

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y9pqv2licn4Pp8qgoheytreDsMjOupOReficArfLksuV3IUiaEzZmCCSV48Pz1JbtFeoT6CiaDvuQZiatw/640?wx_fmt=png&from=appmsg)

03

原理分析

在红队渗透测试中，信息收集是最重要的初期阶段之一。通过精确地获取目标系统上的信息，红队能够识别潜在的攻击路径，并为后续的攻击提供有价值的数据。在这其中，键盘记录器（Keylogger）作为一种常见的攻击手段，可以有效地收集用户输入的信息，帮助攻击者获取目标用户的敏感数据，如登录凭据、系统操作命令等.

## 3.1 钩子

钩子（Hook）是一种 Windows 操作内置的监控和拦截机制，通过程序拦截和处理操作系统或应用程序中的特定事件或消息，钩子通常用于监视和修改系统行为，可以获取或改变事件流，而无需直接修改目标程序的源代码。在系统中，钩子可以用于监控键盘、鼠标、窗口消息等各种系统事件

## 3.2 API

SetWindowsHookEx 函数用于安装钩子。此函数主要用于创建钩子链，允许应用程序拦截和处理事件，具体函数的签名如下所示。

```
```
[DllImport("user32.dll", CharSet = CharSet.Auto, SetLastError = true)]
private static extern IntPtr SetWindowsHookEx(int idHook, Program.LowLevelKeyboardProc lpfn, IntPtr hMod, uint dwThreadId);
```
```

当事件发生时，系统会调用此回调函数。参数 hMod 表示钩子句柄，如果安装钩子成功，返回一个钩子句柄，否则返回 IntPtr.Zero。

CallNextHookEx 函数用于将事件传递给下一个钩子或钩子链中的下一个处理程序。这是钩子处理链的一部分，用于确保事件能够继续传递到其他钩子或系统， 具体函数的签名如下所示。

```
```
[DllImport("user32.dll", CharSet = CharSet.Auto, SetLastError = true)]
private static extern IntPtr CallNextHookEx(IntPtr hhk, int nCode, IntPtr wParam, IntPtr lParam);
```
```

如果是 WH\_KEYBOARD\_LL，则为键盘事件的类型。返回值取决于钩子的实现。一般来说，将返回下一个钩子的处理结果.

## 3.3 调用钩子

这里重点介绍一下方法体内调用的 WriteFile 函数，主要目的是在监听键盘事件时，处理不同的按键输入并将其写入文件。ToWrite 变量是输入的按键名称，首先不记录 Shift 键， 对于 **Return**（回车键）按键，输出换行符， 对于 **OEMPeriod**（句号键）按键，输出句号字符。代码如下所示。

```
```
if (ToWrite  "ShiftKey") { /* 不记录 Shift 键 */ }
else if (ToWrite  "Return") { appendText = Environment.NewLine; }
else if (ToWrite == "Space") { appendText = " "; }
else if (ToWrite == "OEMPeriod") { appendText = "."; }
```
```

最终，决定好要记录的字符 appendText 后，使用 File.AppendAllText 方法将字符追加到指定的文件中，运行时如下图所示。

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y9pqv2licn4Pp8qgoheytreDFpptulgaJPKlaKcb37zQXoicKGMo4IjYbcrzu7FsZLjkDfy62JzCrYA/640?wx_fmt=other&from=appmsg)

综上，键盘记录在渗透测试中的作用不可忽视，不仅能帮助攻击者获取目标用户的敏感数据，还能为进一步的攻击提供丰富的信息。在信息收集阶段，键盘记录器作为一个有效的工具，能够监控用户输入并记录下来，包括登录凭证、系统命令、敏感信息等。想要了解完整或者更多的内网安全方向的文章，可以移步订阅小报童《.NET 内网实战攻防》电子报刊。

04

**欢迎加入.NET 电子报刊**

我们的小报童电子报刊【.NET内网安全攻防】也开始运营，引入小报童也是为了弥补知识星球对于轻量级阅读支持的不足，为用户读者提供更佳的阅读体验。如果您对阅读体验的需求比较高，那么可以订阅这个专栏。

本次电子报刊《.NET 内网安全攻防》专栏，内容主要有.NET在各个内网渗透阶段与Windows系统交互的方式和技巧，可细分为以下8个方向。

```
1） .NET 安全防御绕过
2） .NET 本地权限提升
3） .NET 内网信息收集
4） .NET 内网代理通道
5） .NET 内网横向移动
6） .NET 目标权限维持
7） .NET 数据传输外发
8） .NET 目标痕迹清理
```

原价899，现在限时只需59元，永久买断！目前已有280+位朋友抢先预定，我们会长期更新，初步计划保持每周更新1-2篇新内容，对.NET内网安全的朋友们请尽快订阅该报刊！![图片](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibeicvDNVldcXTgRnFUFTwOqfTleogJThU7kCaZJuuU2BLVLYluu6CFV7BX458AxBcd93ickZ0rmOqQ/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

每增加五十人涨价10元，抓紧订阅，超值！订阅后请关注公众号：dotNet安全矩阵，发送订单截图和您的微信号，邀请您加入专属交流群。感兴趣的朋友，可以点击链接：https://xiaobot.net/p/dotNetAttack，或者扫描下方海报微信二维码加入即可，订阅后小报童定时会将最新内容通过微信推送给您。

![图片](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1YibXibiaRyFPI439dFybReKxQoa5OnhetdDKdnd36lG844cFIWNaib1adpRCXOJbRb6mVicfic8tLqXl9Pw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

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
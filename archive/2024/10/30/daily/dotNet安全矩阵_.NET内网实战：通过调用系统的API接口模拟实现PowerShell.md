---
title: .NET内网实战：通过调用系统的API接口模拟实现PowerShell
url: https://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247496302&idx=2&sn=7df2bd29f289ba8cf5a08de3f86dab70&chksm=fa595c83cd2ed595a5c3fc39d2b5edea9e8e5341e231ee28196a1fb558e28a5d934af96ccb81&scene=58&subscene=0#rd
source: dotNet安全矩阵
date: 2024-10-30
fetch_date: 2025-10-06T18:53:01.040300
---

# .NET内网实战：通过调用系统的API接口模拟实现PowerShell

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y9smyGZn3Nv0QdoibXiaLjdHMtftMvdvEoegj7grlBYEUobXqwCLtyWm9jcPpYMM5IVyibRh198FcsAQ/0?wx_fmt=jpeg)

# .NET内网实战：通过调用系统的API接口模拟实现PowerShell

原创

专攻.NET安全的

dotNet安全矩阵

01

阅读须知

此文所节选自小报童《.NET 内网实战攻防》专栏，主要内容有.NET在各个内网渗透阶段与Windows系统交互的方式和技巧，对内网和后渗透感兴趣的朋友们可以订阅该电子报刊，解锁更多的报刊内容。

02

基本介绍

本文内容部分节选自小报童《.NET 通过调用API模拟实现PowerShell》，完整的文章内容请加入小报童后订阅查看。现在限时只需59元，永久买断！目前已有220+位朋友抢先预定，我们会长期更新，对.NET内网安全的朋友们请尽快订阅该报刊！

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y9smyGZn3Nv0QdoibXiaLjdHM2CKCNRdvFyKM1sN0cOhS3wwDVwOFzacox5kiaZicpTTrlIFLKTFq5rFw/640?wx_fmt=png&from=appmsg)

03

原理分析

在红队内网渗透中，PowerShell 常常被用于执行各种任务，然而也常常受到安全工具的监控。因此，寻找和开发一个能够有效规避检测的 PowerShell 替代工具是非常有意义的。本文将介绍一种实现PowerShell进程的思路，能够在保持 PowerShell 强大功能的同时，规避检测工具的监控。

## 3.1 Invoke-Expression

Invoke-Expression 是 PowerShell 中的一个强大命令，用于执行一个字符串内容中包含的命令、表达式或脚本。通过 Invoke-Expression，可以将字符串参数中的内容当作实际的 PowerShell 命令来执行，具体语法如下所示。

```
Invoke-Expression [-Command] <String> [<CommonParameters>]
```

-Command: 表示需要执行的字符串内容，可以是一个完整的命令或脚本。比如，启动 Windows 自带的计算器，命令如下所示

```
Invoke-Expression "calc"
```

作用是将 "calc" 这一字符串视为实际命令并执行，相当于直接输入 calc。如下图所示。

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y9smyGZn3Nv0QdoibXiaLjdHM4sUnn3qdsBYWiaPiblDwwlkEXzEdV50KwicribhMRM2woicZ0OGd1lZ2B2g/640?wx_fmt=other&from=appmsg)

## 3.2 AddScript

PowerShell.AddScript 是 .NET API 提供的接口，用于将 PowerShell 脚本添加到一个 PowerShell 对象的脚本管道中,可以动态生成 PowerShell 脚本内容并在程序执行时运行,例如 Invoke-Expression，并通过 Invoke() 方法获取whoami执行的结果，具体代码如下所示。

```
```
powerShell.AddScript("Invoke-Expression 'whoami'");
Collection<PSObject> results = powerShell.Invoke();
foreach (PSObject result in results)
{
    Console.WriteLine(result.ToString());
}
```
```

上述代码中，首先通过 PowerShell.Create() 创建一个新的 PowerShell 对象，用于封装 PowerShell 脚本引擎，允许我们在.NET中执行 PowerShell 脚本。

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y9smyGZn3Nv0QdoibXiaLjdHMnrFV6iaywdqFQiagVEUfanViaLlcOtHKTX4vIaMh8n5CKGqKZcjXXYX5w/640?wx_fmt=other&from=appmsg)

综上，可以利用PowerShell.AddScript 和 Invoke-Expression完成一个小型的PowerShell替代工具，因此能够有效规避一些安全防护软件对于 PowerShell.exe 进程的检测规则，便于黑客更加隐蔽的执行任务。想要了解完整或者更多的内网安全防御绕过方向的文章，可以移步订阅小报童《.NET 内网实战攻防》电子报刊。

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

原价899，现在限时只需59元，永久买断！目前已有240+位朋友抢先预定，我们会长期更新，初步计划保持每周更新1-2篇新内容，对.NET内网安全的朋友们请尽快订阅该报刊！![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibeicvDNVldcXTgRnFUFTwOqfTleogJThU7kCaZJuuU2BLVLYluu6CFV7BX458AxBcd93ickZ0rmOqQ/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

每增加五十人涨价10元，抓紧订阅，超值！订阅后请关注公众号：dotNet安全矩阵，发送订单截图和您的微信号，邀请您加入专属交流群。感兴趣的朋友，可以点击链接：https://xiaobot.net/p/dotNetAttack，或者扫描下方海报微信二维码加入即可，订阅后小报童定时会将最新内容通过微信推送给您。

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y9smyGZn3Nv0QdoibXiaLjdHMJWGxJp9ibViaKvSS55M4ic9858VervRwVGM7aMfSmP5ibCZc8dv30ZPC1Q/640?wx_fmt=jpeg&from=appmsg)

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
---
title: .NET内网实战：通过 Sysnative 虚拟路径绕过安全防护启动 cmd 进程
url: https://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247498948&idx=2&sn=b67e25fe8d738c38288c2d1d8de22384&chksm=fa595229cd2edb3f8de025a602769351ab9a6a2f964f6230dd9fe318d76256c762252864f2a7&scene=58&subscene=0#rd
source: dotNet安全矩阵
date: 2025-02-18
fetch_date: 2025-10-06T20:39:58.183578
---

# .NET内网实战：通过 Sysnative 虚拟路径绕过安全防护启动 cmd 进程

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YiczKSznEcepYxrkAyv2WgKswGC46xVib2nkjGSeG4pXuObs7pruibEm5bBsHXn8I7iaPHdeePvDADU7w/0?wx_fmt=jpeg)

# .NET内网实战：通过 Sysnative 虚拟路径绕过安全防护启动 cmd 进程

原创

专攻.NET安全的

dotNet安全矩阵

01

阅读须知

此文所节选自小报童《.NET 内网实战攻防》专栏，主要内容有.NET在各个内网渗透阶段与Windows系统交互的方式和技巧，对内网和后渗透感兴趣的朋友们可以订阅该电子报刊，解锁更多的报刊内容。

02

基本介绍

本文内容部分节选自小报童《.NET 通过 Sysnative 虚拟路径绕过安全防护启动cmd进程》，完整的文章内容请加入小报童后订阅查看。现在限时只需59元，永久买断！目前已有300+位朋友抢先预定，我们会长期更新，对.NET内网安全的朋友们请尽快订阅该报刊！

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1YiczKSznEcepYxrkAyv2WgKscskKqXPuuYrJ06hTgVMibiceSRcN1dxIhlg34LHS8vO15YnNFokC6ibvQ/640?wx_fmt=png&from=appmsg)

03

原理分析

Sysnative 路径是Windows操作系统中一个非常有用的特性，解决了32位应用程序在64位系统中访问系统目录时的路径重定向问题。通过利用这一特性，红队渗透时可以实现一些新的功能和绕过防御，如启动64位CMD等。

## 3.1 基本介绍

在 64 位 Windows 操作系统中，System32 目录并不包含 32 位系统文件，而 32 位的系统文件则存放在 SysWOW64 目录中。这是为了区分和管理不同位数的程序和其对应的系统文件，如下图所示。

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YiczKSznEcepYxrkAyv2WgKsNib0qJunEHrgjYtPVf2Kb3pRzym5g4d8QzDNbJ7nByrhd9dUxfcCZLQ/640?wx_fmt=other&from=appmsg)

对于 32 位应用程序来说，访问 System32 目录时会被重定向到 SysWOW64 目录，为了解决这一问题，Windows 从Vista 版本后开始提供了一个虚拟路径 Sysnative，它指向 System32 目录，但仅对 32 位应用程序可见。

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YiczKSznEcepYxrkAyv2WgKsaibItJvUOjTRvpkicZ4f9Cyc6fmOxmEjogImkXkO8dcRKcHjvhdx4SvQ/640?wx_fmt=other&from=appmsg)

## 3.2 使用方法

在 64 位的 Windows 操作系统上，32 位应用程序可以通过 Sysnative 路径来访问 64 位的系统文件。例如： C:\Windows\Sysnative\cmd.exe - 这是 32 位应用程序访问 64 位的 cmd.exe 的路径。

利用Sysnative路径，我们可以实现一种启动CMD的新方法，在 32 位应用程序中运行时启动64 位版本的 cmd.exe，具体代码如下所示。

```
```
using System.Diagnostics;
class Program
{
    static void Main()
    {
        Process.Start("C:\\Windows\\Sysnative\\cmd.exe");
    }
}
```
```

这段代码将在64位Windows操作系统上成功启动一个64位的CMD。这对于需要执行64位命令或脚本的32位应用程序来说，是一个非常有用的技巧，如下图所示

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YiczKSznEcepYxrkAyv2WgKsH46WuicC93a2JmQhuquiajUOBuvBOhwZTC8mvX2OvDtGwnDMiaDz2kMHw/640?wx_fmt=other&from=appmsg)

## 3.3 IIS下应用

IIS 10可以配置为以32位或64位模式运行应用程序，因此，如果应用程序池 [ 启用32位应用程序 ] 项配置为 True，则在该池下运行的所有应用程序都将作为32位进程运行，将上述控制台里的.NET代码写在单个ASPX页面，再访问 123.aspx 时便可顺利启动cmd.exe进程，如下图所示

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YiczKSznEcepYxrkAyv2WgKsnnjRWFsx8ibhwQKTZI1VGN9BqSlSiaGIeyzwPY8NJcicQMjwLPtWa3NZQ/640?wx_fmt=other&from=appmsg)

如果 IIS 10中通过 aspx 调用 C:\\Windows\\Sysnative\\cmd.exe不成功的话，通常与应用程序池的位数配置有关，否则会正常启动。

综上，这一特性引起了群友们广泛的讨论和关注，在渗透测试中，攻击者可以利用Sysnative路径绕过某些安全限制，或者在权限维持阶段，通过在计划任务中使用Sysnative路径可以执行64位的命令或脚本。想要了解完整或者更多的内网安全方向的文章，可以移步订阅小报童《.NET 内网实战攻防》电子报刊。

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
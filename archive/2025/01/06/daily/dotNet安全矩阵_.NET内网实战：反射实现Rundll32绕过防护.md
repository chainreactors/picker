---
title: .NET内网实战：反射实现Rundll32绕过防护
url: https://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247497978&idx=1&sn=5015baab61df83837a10ea3d468e1b26&chksm=fa595617cd2edf01bdc78dee43caf18f1c290c64393ffbb10eea2fe83e3e1677f4c19e7d15fc&scene=58&subscene=0#rd
source: dotNet安全矩阵
date: 2025-01-06
fetch_date: 2025-10-06T20:09:29.795436
---

# .NET内网实战：反射实现Rundll32绕过防护

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Yicicto87ibBgvX9QjdHEia894t6swAx2BDgvpR2iavwFn6ic6MTlk6CllPDGShOwIHeT52oPf63IkQhsvA/0?wx_fmt=jpeg)

# .NET内网实战：反射实现Rundll32绕过防护

原创

专攻.NET安全的

dotNet安全矩阵

01

阅读须知

此文所节选自小报童《.NET 内网实战攻防》专栏，主要内容有.NET在各个内网渗透阶段与Windows系统交互的方式和技巧，对内网和后渗透感兴趣的朋友们可以订阅该电子报刊，解锁更多的报刊内容。

02

基本介绍

本文内容部分节选自小报童《.NET 通过反射技术实现Rundll32功能绕过安全防护》，完整的文章内容请加入小报童后订阅查看。现在限时只需59元，永久买断！目前已有280+位朋友抢先预定，我们会长期更新，对.NET内网安全的朋友们请尽快订阅该报刊！

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Yicicto87ibBgvX9QjdHEia894teZrzJfIdmbmV6SgVLNXYGMocEpPtVF4VusLMgoGXiaqauGQvD2EmgSg/640?wx_fmt=png&from=appmsg)

03

原理分析

在攻防对抗中，攻击者常利用 .NET 提供的反射技术，通过动态加载外部 DLL 并调用其中的任意方法，实现灵活且隐蔽的恶意代码执行。这种技术无需提前绑定目标代码，能够有效规避静态检测，同时模仿类似 rundll32.exe 的行为，进一步提高攻击链的隐匿性。比如通过加载 Sharp4Library.dll 的组件并动态调用其方法，攻击者可以轻松实现任意指令执行，为渗透测试和实际攻击提供强大的支持。

## 3.1 rundll32

rundll32.exe 是一个位于 Windows 系统 C:\Windows\System32 目录中的可执行文件。主要功能是通过加载C或C++编译的动态链接库中指定的函数来执行某些特定任务。在实际使用中， 以下是 rundll32.exe 基本的用法：

```
```
rundll32.exe <DLL路径>,<函数名> [参数]
```
```

比如，调用 Shell32.dll 中的 Control\_RunDLL 函数打开 Windows控制面板，具体命令如下所示。

```
```
rundll32.exe shell32.dll,Control_RunDLL desk.cpl
```
```

因此，系统管理员可以通过 rundll32.exe 在脚本中执行系统相关任务，如批量管理控制面板功能。

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Yicicto87ibBgvX9QjdHEia894ticwJyM0ZqcYiaUHuG6FZKbTylfezfSyDraJWrUibXHlSNAtJctHttUh0A/640?wx_fmt=other&from=appmsg)

## 3.2 .NET反射技术

反射是 .NET 提供的一种强大功能，可以在运行时动态获取类型信息（类、方法、属性、字段等），并进行实例化、调用方法或修改字段值。.NET 中反射的核心类都位于 System.Reflection 命名空间。

.NET反射一般有以下几个步骤，首先通过 Assembly 类加载程序集，通常需要提供一个绝对的物理路径，并且使用LoadFrom或者LoadFile载入，具体代码如下所示。

```
```
using System.Reflection;
Assembly assembly = Assembly.LoadFrom("Sharp4Library.dll");
Assembly assembly = Assembly.LoadFile(@"C:\Path\To\Sharp4Library.dll");
```
```

接着，通过GetMethod、Invoke 方法进行调用，代码如下所示

```
```
MethodInfo method = type.GetMethod("Run");
method.Invoke(null, new object[] { arg1, arg2 });
object result = method.Invoke(instance, new object[] { arg1, arg2 });
```
```

## 3.3 实现rundll32功能

通过 .NET 的反射机制，主要实现动态加载指定路径的 DLL 文件，调用 DLL 中的指定命名空间、类和方法，并传递自定义参数，实现复杂的功能调用，具体代码如下所示。

```
```
using System;
using System.IO;
using System.Linq;
using System.Reflection;

class Program
{
    public static void Main(string[] args)
    {
        string fullPath = args[0];
        string namespaceName = args[1];
        string className = args[2];
        string methodName = args[3];
        string[] methodArgs = args.Length > 4 ? args.Skip(4).ToArray() : new string[0];
        StdLoad(fullPath, namespaceName, className, methodName, methodArgs);
    }
}
```
```

上述代码中，通过从加载的 Assembly 对象中提取所有类型的命名空间，并去重后转换为数组 var namespaces。接着，再利用反射机制调用指定类型的指定方法。

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Yicicto87ibBgvX9QjdHEia894t64QbRO9pNQcQyFWclziaZzUDRibHeuUsiaKkAXt0pGXtDkVPzicwpM9skw/640?wx_fmt=other&from=appmsg)

通过以下命令调用上述 DLL 的功能， 执行后将弹出计算器，具体命令如下所示

```
```
 Sharp4Rundll32.exe Sharp4Library.dll Sharp4Library Class1 Run cmd.exe /c calc
```
```

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Yicicto87ibBgvX9QjdHEia894tcQ6rPqtU0XianUjibh95WuJJNkyNLKRNicTGpj9cvbGwOs7s2eq1J5T7g/640?wx_fmt=other&from=appmsg)

综上，通过 .NET 的 Assembly.LoadFile 和反射机制，可以实现动态加载和调用 DLL 的功能。这种技术不仅能够满足动态扩展和模块化开发的需求，还能在特定场景下替代 rundll32.exe 的功能。想要了解完整或者更多的内网安全方向的文章，可以移步订阅小报童《.NET 内网实战攻防》电子报刊。

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

原价899，现在限时只需59元，永久买断！目前已有280+位朋友抢先预定，我们会长期更新，初步计划保持每周更新1-2篇新内容，对.NET内网安全的朋友们请尽快订阅该报刊！![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibeicvDNVldcXTgRnFUFTwOqfTleogJThU7kCaZJuuU2BLVLYluu6CFV7BX458AxBcd93ickZ0rmOqQ/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

每增加五十人涨价10元，抓紧订阅，超值！订阅后请关注公众号：dotNet安全矩阵，发送订单截图和您的微信号，邀请您加入专属交流群。感兴趣的朋友，可以点击链接：https://xiaobot.net/p/dotNetAttack，或者扫描下方海报微信二维码加入即可，订阅后小报童定时会将最新内容通过微信推送给您。

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1YibXibiaRyFPI439dFybReKxQoa5OnhetdDKdnd36lG844cFIWNaib1adpRCXOJbRb6mVicfic8tLqXl9Pw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

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
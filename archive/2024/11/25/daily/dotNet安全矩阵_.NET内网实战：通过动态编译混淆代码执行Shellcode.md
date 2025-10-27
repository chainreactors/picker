---
title: .NET内网实战：通过动态编译混淆代码执行Shellcode
url: https://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247496868&idx=1&sn=086918413912fb2d458b885b4ef7b36a&chksm=fa595a49cd2ed35f7c824e981f1b937ed1fc725ada05083e40abca7c120bf1f087a2949104b1&scene=58&subscene=0#rd
source: dotNet安全矩阵
date: 2024-11-25
fetch_date: 2025-10-06T19:15:03.375215
---

# .NET内网实战：通过动态编译混淆代码执行Shellcode

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y9JlPQ9pp3r4U7uctkB21k4AvMAxn37t9On9lqopXDgk60H3qp2Zy8icdNb94PmENo0JSKaXsy4xiaA/0?wx_fmt=jpeg)

# .NET内网实战：通过动态编译混淆代码执行Shellcode

原创

专攻.NET安全的

dotNet安全矩阵

01

阅读须知

此文所节选自小报童《.NET 内网实战攻防》专栏，主要内容有.NET在各个内网渗透阶段与Windows系统交互的方式和技巧，对内网和后渗透感兴趣的朋友们可以订阅该电子报刊，解锁更多的报刊内容。

02

基本介绍

本文内容部分节选自小报童《.NET 通过隐藏任务计划实现权限持久化》，完整的文章内容请加入小报童后订阅查看。现在限时只需59元，永久买断！目前已有240+位朋友抢先预定，我们会长期更新，对.NET内网安全的朋友们请尽快订阅该报刊！

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y9JlPQ9pp3r4U7uctkB21k41mFeB2vsypeCZpia3YsekWqApAcnfSSVD4g6C46w5Gtce1XgwciaAN1A/640?wx_fmt=png&from=appmsg)

03

原理分析

在红队行动中，常常需要规避各种防御机制以成功启动木马进程。今天，我们将深入探讨一种相对冷门但非常有趣的技术：通过 .NET 动态编译结合代码混淆，实现对 shellcode 的隐秘执行。

## 3.1 VirtualAlloc函数

VirtualAlloc 是 Windows API 中用于内存分配的函数，常用于分配和保护进程的虚拟内存空间。在.NET中可以通过 P/Invoke 调用的非托管函数，具体代码如下所示。

```
```
[DllImport("kernel32.dll", SetLastError = true, ExactSpelling = true)]
private static extern UInt32 VirtualAlloc(
    UInt32 lpStartAddr,        // 内存的起始地址
    UInt32 size,               // 要分配的内存大小（以字节为单位）
    UInt32 flAllocationType,   // 分配类型（如 MEM_COMMIT 或 MEM_RESERVE）
    UInt32 flProtect           // 内存保护属性（如 PAGE_EXECUTE_READWRITE）
);
```
```

因此，在.NET里通过[DllImport("kernel32.dll", SetLastError = true, ExactSpelling = true)] 特性声明 Windows API。DllImport 提供了SetLastError 、ExactSpelling 两个选项，当 SetLastError 设置为 true时， 表示是否返回 GetLastError 的错误代码。

## 3.2 CreateThread函数

CreateThread 也是 Windows API 提供的函数，用于在目标进程中创建一个新的线程。通常在.NET里调用的方式如下所示。

```
```
[DllImport("kernel32.dll", SetLastError = true)]
private static extern IntPtr CreateThread(
    UInt32 lpThreadAttributes,  // 线程的安全属性
    UInt32 dwStackSize,         // 线程的初始堆栈大小
    UInt32 lpStartAddress,      // 线程的起始地址（函数指针）
    IntPtr param,               // 传递给线程的参数
    UInt32 dwCreationFlags,     // 创建标志
    ref UInt32 lpThreadId       // 接收线程 ID
);
```
```

通常与动态内存分配和 shellcode 执行结合使用，尤其是在渗透测试或恶意代码中，用于将 shellcode 注入到目标进程并执行。

## 3.3 动态编译技术

安全对抗阶段，有时我们需要在运行时动态编译代码并执行，.NET平台提供的CSharpCodeProvider 是一个编译服务的类，用于与底层的编译器交互，可以动态创建、编辑和编译代码。

```
```
public static object function1(string code, string namespacename, string classname, string functionname, bool isstatic, params object[] args)
{
    object returnval = null;
    Assembly asm = BuildAssembly(code);
    object instance = null;
    Type type = null;
    if (isstatic)
    {
        type = asm.GetType(namespacename + "." + classname);
    }
    else
    {
        instance = asm.CreateInstance(namespacename + "." + classname);
        type = instance.GetType();
    }
    MethodInfo method = type.GetMethod(functionname);
    returnval = method.Invoke(instance, args);
    return returnval;
}
```
```

上述代码中，通过 Type.GetMethod() 获取指定的方法信息，然后使用 MethodInfo.Invoke() 调用方法，不过做了一次判断，对于静态方法，调用时不需要实例，对于实例方法，需传入已创建的对象实例。

通过调用function1(code, "Namespace", "Program", "run", false, null); 实现动态编译执行，此处的 "run" 便是需要调用的方法名称，"Program" 是类的名称。运行后成功启动本地计算器进程，如下图所示

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y9JlPQ9pp3r4U7uctkB21k4BtII8SpQOVOKB5TEHOffNA3XCwUZ792bZEDSca9uc1IzVbo26vlDsg/640?wx_fmt=other&from=appmsg)

综上所述，通过动态编译.NET代码实现线程注入的思路，其主要功能是接收经过 Base64 编码的 shellcode 字符串，并将其注入到本地线程中，从而执行恶意代码。想要了解完整或者更多的内网安全方向的文章，可以移步订阅小报童《.NET 内网实战攻防》电子报刊。

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

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y9smyGZn3Nv0QdoibXiaLjdHMJWGxJp9ibViaKvSS55M4ic9858VervRwVGM7aMfSmP5ibCZc8dv30ZPC1Q/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

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
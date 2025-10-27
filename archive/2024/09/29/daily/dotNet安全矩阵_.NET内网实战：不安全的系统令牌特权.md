---
title: .NET内网实战：不安全的系统令牌特权
url: https://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247495620&idx=1&sn=aa00a0d1f8bb2269ff7b606039484958&chksm=fa594129cd2ec83fb548863ffb6af450870aef4544f872a71e2b3eaa00a0cee89ab9df33b53e&scene=58&subscene=0#rd
source: dotNet安全矩阵
date: 2024-09-29
fetch_date: 2025-10-06T18:23:42.864261
---

# .NET内网实战：不安全的系统令牌特权

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibTRic7PgrT4472YFHDrrOLlcq46LOia2TU0dCjiabPcq7p43twm9h7LJMnr9HonnwVYgBKdGJMmiauUg/0?wx_fmt=jpeg)

# .NET内网实战：不安全的系统令牌特权

原创

专攻.NET安全的

dotNet安全矩阵

01

阅读须知

此文所节选自小报童《.NET 内网实战攻防》专栏，主要内容有.NET在各个内网渗透阶段与Windows系统交互的方式和技巧，对内网和后渗透感兴趣的朋友们可以订阅该电子报刊，解锁更多的报刊内容。

02

基本介绍

本文内容部分节选自小报童《.NET 不安全的令牌特权-SeImpersonatePrivilege 》，完整的文章内容请加入小报童后订阅查看。现在限时只需59元，永久买断！目前已有220+位朋友抢先预定，我们会长期更新，对.NET内网安全的朋友们请尽快订阅该报刊！

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1YibTRic7PgrT4472YFHDrrOLl5W52HKMe0lj87t1auDeRjMZqCUjjs9PZf6w7mfeicicL9ncIRTQJMSpg/640?wx_fmt=png&from=appmsg)

03

原理分析

在 Windows 操作系统中，用户和进程可以拥有不同的权限，这些权限控制着能够执行的操作范围。如果当前进程获取到本地用户或者系统服务账户启用了一些不安全的权限，那么有可能会完成权限提升。SeImpersonatePrivilege 是一种特殊的权限，允许进程以其他用户的身份执行操作。

## 3.1 用户身份运行程序

当在Windows系统桌面下使用管理员组的用户打开 cmd 而不以管理员身份运行时，cmd 以当前用户的权限级别启动，默认不具备 SeImpersonatePrivilege 权限，执行命令 whoami /priv 查看当前用户或进程所具有的权限，如下图所示

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibTRic7PgrT4472YFHDrrOLlib9eK6SZAmETBKSR7pBRiafgicJaTyj9MoBibjeTJiaibVrI4iaKNgJ1MevHQ/640?wx_fmt=other&from=appmsg)

从图上显示当前管理员组用户Ivan1ee，虽然是管理员权限，但被分配了Medium Mandatory Level，该组是Windows 安全模型中的一种强制级别，限制用户对系统敏感部分的访问，从而减少潜在的恶意操作。因此，当应用程序尝试执行需要更高权限的操作时，Windows 会根据用户的 Mandatory Level 进行检查。如果用户的级别不足，则会提示用户以管理员身份运行程序。

## 3.2 管理员身份运行程序

当用户需要以高权限运行程序时，通常在Windows窗口下右键点击 cmd，选择以管理员身份运行。再次输入 whoami /priv 可以看到很多的特权名，如下图所示。

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibTRic7PgrT4472YFHDrrOLlb0QlyyyU9YwyeTo66JQDgTj2MSIMdhdlZJkmpxA1VDndPTFw1dCQfw/640?wx_fmt=other&from=appmsg)

默认分配此权限的用户组分别是本地管理员组的成员(Administraotrs)、本地服务账户（Local Service、Network Service）、服务控制管理器启动的服务，由此得知，.NET应用程序池在NetWork Service账户下运行的IIS均具备此权限。

## 3.3 编程实现

下面将详细解析一个 .NET 类 PrivilegeChecker，其主要功能是检查当前进程是否具备 SeImpersonatePrivilege 权限。

在PrivilegeChecker类的开头，使用 DllImport 特性导入了三个 Windows API 函数，OpenProcessToken 用于打开指定进程的访问令牌，以便获取权限信息。GetTokenInformation 函数可以获取指定令牌的不同类型的信息，例如权限列表。LookupPrivilegeValue 函数用于查找特权名称对应的 LUID（本地唯一标识符），通过它可以确认权限的启用状态。具体代码如下所示。

```
```
[DllImport("advapi32.dll", SetLastError = true)]
private static extern bool OpenProcessToken(IntPtr ProcessHandle, uint DesiredAccess, out IntPtr TokenHandle);
[DllImport("advapi32.dll", SetLastError = true)]
private static extern bool GetTokenInformation(IntPtr TokenHandle, TOKEN_INFORMATION_CLASS TokenInformationClass, IntPtr TokenInformation, uint TokenInformationLength, out uint ReturnLength);
[DllImport("advapi32.dll", CharSet = CharSet.Auto)]
private static extern bool LookupPrivilegeValue(string lpSystemName, string lpName, out LUID lpLuid);
```
```

接着，通过 OpenProcessToken 获取当前进程的访问令牌。如果调用失败，抛出异常。具体代码如下所示。

```
```
public static bool IsSeImpersonatePrivilegeEnabled()
{
    IntPtr zero = IntPtr.Zero;
    try
    {
        if (!OpenProcessToken(Process.GetCurrentProcess().Handle, 8U, out zero))
        {
            throw new Win32Exception(Marshal.GetLastWin32Error());
        }
    }
```
```

04

WebShell实战

所以很多工具在桌面用户下运行工具，需要首先绕过UAC或者以管理员身份运行此工具，但是在在IIS里通过webshell运行，根本不需要考虑UAC的绕过，这个特权很厉害噢。比如IIS服务管理器的进程w3wp.exe默认就具备了该权限，如下图所示。

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibTRic7PgrT4472YFHDrrOLlRxL0eFTyKM5yhmgfQ4oLzQicCDARnuZXQKVXjIKHjdhbMCFlaxGF66A/640?wx_fmt=other&from=appmsg)

这样看，通过 IIS 进程（如 w3wp.exe）启动的 cmd 可以在一定情况下运行其他软件，而不受 UAC 限制。这是因为 IIS 进程在具有 SeImpersonatePrivilege 权限的上下文中运行，可以模拟令牌。

综上，曾有前辈说，当你拥有 SeImpersonatePrivilege 权限时，你就是SYSTEM。想要了解完整或者更多的内网安全防御绕过方向的文章，可以移步订阅小报童《.NET 内网实战攻防》电子报刊。

05

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

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1YibTRic7PgrT4472YFHDrrOLlcTgKtwgm9cngTJDUib6AO9siaC7WXl6f8Jk1QZbYcib76QcIOBTicMDRhQ/640?wx_fmt=png&from=appmsg)

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
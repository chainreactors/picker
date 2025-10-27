---
title: .NET内网实战：通过进程管道执行CMD命令
url: https://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247494406&idx=3&sn=a64a4e93a057d59abb5e0ffc93a4bb3b&chksm=fa5945ebcd2eccfd283106211bd11e2571a4a00b78f97dda08e9d65df52eb1362ab6465253a3&scene=58&subscene=0#rd
source: dotNet安全矩阵
date: 2024-08-13
fetch_date: 2025-10-06T18:06:50.611818
---

# .NET内网实战：通过进程管道执行CMD命令

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Yicib5jic9GbpwRHsGAoNx7RelER8vGELRsZamp5AAjh73VVAD1CHgkYVsQkJDDpx9KBkLZu9bghs8nw/0?wx_fmt=jpeg)

# .NET内网实战：通过进程管道执行CMD命令

专攻.NET安全的

dotNet安全矩阵

01

阅读须知

此文所节选自小报童《.NET 内网实战攻防》专栏，主要内容有.NET在各个内网渗透阶段与Windows系统交互的方式和技巧，对内网和后渗透感兴趣的朋友们可以订阅该电子报刊，解锁更多的报刊内容。

02

基本介绍

本文内容部分节选自小报童《.NET 通过进程管道执行CMD命令》，完整的文章内容请加入小报童后订阅查看。现在限时只需59元，永久买断！目前已有170+位朋友抢先预定，我们会长期更新，对.NET内网安全的朋友们请尽快订阅该报刊！

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Yicib5jic9GbpwRHsGAoNx7RelaMYkz9xSsXEf6czBJRicM1oCfsTibib6rd0aicSGZcPGhRickiatwvFFe5mQ/640?wx_fmt=png&from=appmsg)

03

编码实现

通过Windows API中的SetHandleInformation、CreatePipe、CreateProcess以及OpenProcess等函数实现任意命令执行并在黑屏上显示命令执行后的结果，可以在内网渗透阶段规避安全防护设备的拦截和告警，因此这种技术对于红队活动是非常有利的。

## 3.1 创建管道

使用CreatePipe函数创建一个管道，我们知道在Windows系统编程中，管道是一种重要的进程间IPC通信机制，允许数据在进程之间单向或双向流动。而CreatePipe函数是Windows API的一部分，创建一个匿名管道，该管道具有读端和写端。

```
[DllImport("kernel32.dll")]
private static extern bool CreatePipe(out IntPtr hReadPipe, out IntPtr hWritePipe, ref UnmanagedExecute.SECURITY_ATTRIBUTES lpPipeAttributes, uint nSize);
UnmanagedExecute.CreatePipe(out hStdOutRead, out hStdOutWrite, ref saHandles, 0U);
```

由于管道是匿名的，因此只能用于由同一父进程创建的进程之间的通信。

## 3.2 进程初始化

随后，使用DllImport属性从kernel32.dll库中导入SetHandleInformation函数。.NET调用SetHandleInformation函数的代码如下所示

```
[DllImport("kernel32.dll", SetLastError = true)]
private static extern bool SetHandleInformation(IntPtr hObject, UnmanagedExecute.HANDLE_FLAGS dwMask, UnmanagedExecute.HANDLE_FLAGS dwFlags);
```

然后，初始化了PROCESS\_INFORMATION和STARTUPINFOEX结构体。PROCESS\_INFORMATION用于接收新创建进程的信息，如进程句柄和主线程句柄。具体代码如下所示。

```
IntPtr hDupStdOutWrite = IntPtr.Zero;
IntPtr hStdOutRead;
IntPtr hStdOutWrite;
UnmanagedExecute.PROCESS_INFORMATION pInfo = default(UnmanagedExecute.PROCESS_INFORMATION);
UnmanagedExecute.STARTUPINFOEX siEx = default(UnmanagedExecute.STARTUPINFOEX);
siEx.StartupInfo.cb = Marshal.SizeOf<UnmanagedExecute.STARTUPINFOEX>(siEx);
IntPtr lpValueProc = IntPtr.Zero;
IntPtr hSourceProcessHandle = IntPtr.Zero;
siEx.StartupInfo.hStdError = hStdOutWrite;
siEx.StartupInfo.hStdOutput = hStdOutWrite;
```

上述代码中，siEx.StartupInfo结构体的hStdError和hStdOutput成员都设置为hStdOutWrite句柄，这意味着新进程的标准输出和标准错误都将重定向到hStdOutWrite指定的句柄。

经过上面的配置后我们通过调用API函数CreateProcess 创建进程，此函数用于创建一个新的进程，允许程序通过指定父进程ID和命令来启动一个新的进程。具体代码如下所示

```
siEx.StartupInfo.dwFlags = STARTF_USESHOWWINDOW | STARTF_USESTDHANDLES;
siEx.StartupInfo.wShowWindow = SW_HIDE;

var ps = new SECURITY_ATTRIBUTES();
var ts = new SECURITY_ATTRIBUTES();
ps.nLength = Marshal.SizeOf(ps);
ts.nLength = Marshal.SizeOf(ts);

bool ret = CreateProcess(null, command, ref ps, ref ts, true, EXTENDED_STARTUPINFO_PRESENT | CREATE_NO_WINDOW, IntPtr.Zero, null, ref siEx, out pInfo);
```

新进程创建后，调用SafeFileHandle封装了 hStdOutRead 句柄，结合StreamReader从管道读取新进程输出的Stream流数据，最后，通过do语句循环不断的读取输出数据，直到子进程完全退出管道中无数据为止。

综上，通过使用 Windows API 函数如 CreateProcess、OpenProcess 和 DuplicateHandle实现父子进程间的数据交互，主要在处理子进程输出时，通过创建管道并使用 StreamReader 实时读取数据，使得用户可以即时获取子进程的执行结果。想要了解完整或者更多的内网安全防御绕过方向的文章，可以移步订阅小报童《.NET 内网实战攻防》电子报刊。

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

原价899，现在限时只需59元，永久买断！目前已有170+位朋友抢先预定，我们会长期更新，初步计划保持每周更新1-2篇新内容，对.NET内网安全的朋友们请尽快订阅该报刊！![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibeicvDNVldcXTgRnFUFTwOqfTleogJThU7kCaZJuuU2BLVLYluu6CFV7BX458AxBcd93ickZ0rmOqQ/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

每增加五十人涨价10元，抓紧订阅，超值！订阅后请关注公众号：dotNet安全矩阵，发送订单截图和您的微信号，邀请您加入专属交流群。感兴趣的朋友，可以点击链接：https://xiaobot.net/p/dotNetAttack，或者扫描下方海报微信二维码加入即可，订阅后小报童定时会将最新内容通过微信推送给您。

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibIAgFshlvm5mdSHoPlq9MrsmJiaSCvnl9Bmv31XRC3m2ibEXg4ehRH4g8XPLicZomicJXN2faEicDWTag/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

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
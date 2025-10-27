---
title: .NET内网实战：通过傀儡进程执行Shellcode
url: https://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247493629&idx=1&sn=83235ca782ed28b7faaa18e2fe1919bb&chksm=fa594910cd2ec00688c18a740d98a9c7d75cca2190fb168285bc95facdfd0a20a854ef4d6bc1&scene=58&subscene=0#rd
source: dotNet安全矩阵
date: 2024-07-29
fetch_date: 2025-10-06T17:41:17.592853
---

# .NET内网实战：通过傀儡进程执行Shellcode

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Yib0Y9dkVCH34QoFqiaaZ738KSYOdVN1cY4GJbuVecNt4ucGj72SO1E2DaA8blHIuXAoaJQlEUJ9icQA/0?wx_fmt=jpeg)

# .NET内网实战：通过傀儡进程执行Shellcode

原创

专攻.NET安全的

dotNet安全矩阵

01

阅读须知

此文所节选自小报童《.NET 内网实战攻防》专栏，主要内容有.NET在各个内网渗透阶段与Windows系统交互的方式和技巧，对内网和后渗透感兴趣的朋友们可以订阅该电子报刊，解锁更多的报刊内容。

02

基本介绍

本文内容部分节选自小报童《.NET 通过创建系统影子账户实现权限维持》，完整的文章内容请加入小报童后订阅查看。现在限时只需49元，永久买断！目前已有160+位朋友抢先预定，我们会长期更新，对.NET内网安全的朋友们请尽快订阅该报刊！

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Yib0Y9dkVCH34QoFqiaaZ738KPKtGP1D91FMs56C42MDdQ8iaHhg5h5lmHFXlibZfGXWmmyky5e50B0ug/640?wx_fmt=png&from=appmsg)

03

编码实现

在 Windows 操作系统中，简单来说，傀儡进程就是攻击者通过一系列技术操作，将原本正常的进程转化为执行恶意任务的傀儡。通常借助ZwQueryInformationProcess、ReadProcessMemory和ResumeThread等API函数来实现这个技术。

## 3.1 相关函数

ZwQueryInformationProcess函数用于获取指定进程的信息，如进程ID、父进程信息等，ReadProcessMemory函数用于从指定进程的内存中读取数据，ResumeThread函数表示当暂停计数递减至零时，恢复线程的执行。在.NET平台下调用该函数的代码如下所示。

```
DllImport("kernel32.dll", SetLastError = true)]
static extern bool ReadProcessMemory(IntPtr hProcess, IntPtr lpBaseAddress, [Out] byte[] lpBuffer, int dwSize, out IntPtr lpNumberOfBytesRead);
```

## 3.2 实现傀儡进程

要成功构建傀儡进程，关键在于两点：首先是选择合适时机向内存写入Shellcode，其次则是精准地修改进程的执行流程。在.NET环境中调用相关函数的核心代码示例如下。

```
public PROCESS_INFORMATION StartProcess(string path)
{
STARTUPINFO startInfo = new STARTUPINFO();
PROCESS_INFORMATION procInfo = new PROCESS_INFORMATION();
uint flags = CreateSuspended | DetachedProcess | CreateNoWindow;
if (!CreateProcess((IntPtr)0, path, (IntPtr)0, (IntPtr)0, true, flags, (IntPtr)0, (IntPtr)0,  ref  startInfo, out procInfo))
throw new SystemException("[x] 创建进程失败!");
return procInfo;
}
```

首先通过调用CreateProcess函数来创建一个新的进程，并设置处于挂起状态，随后，读取该进程中特定模块的内存地址。接着，使用ZwCreateSection函数来创建一个进程间共享的内存区域，这个区域允许不同的进程间共享数据。

```
public bool CreateSection(uint size)
{
    LARGE_INTEGER liVal = new LARGE_INTEGER();
    size_ = round_to_page(size);
    liVal.LowPart = size_;
    var status = ZwCreateSection(ref section_, GenericAll, (IntPtr)0, ref liVal, PageReadWriteExecute, SecCommit, (IntPtr)0);
    return nt_success(status);
}
```

最终，调用ResumeThread函数，激活并恢复主线程的执行，使进程按照预设的包含Shellcode的代码运行执行。

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Yib0Y9dkVCH34QoFqiaaZ738K2X4QL5YFPHicvl25UNyxRNsyzeUpWor0aEx96Pg9hW3ocCMglJCDNbg/640?wx_fmt=other&from=appmsg)

综上，傀儡进程是通过篡改某进程的内存数据来实现的，具体做法是在内存中写入Shellcode，并操纵进程的执行流程，使其转而执行恶意的Shellcode。这样一来，虽然进程的外壳看似未变，但内部执行的操作却已完全替换。想要了解更多内网安全防御绕过方向的文章，可以移步订阅小报童《.NET 内网实战攻防》电子报刊。

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

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Yib0Y9dkVCH34QoFqiaaZ738Kz9ziafiaEWnUkJYNk4SiajHbD8J6skkR0jK9ecycszmxP827PTibRx0jvA/640?wx_fmt=jpeg&from=appmsg)

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
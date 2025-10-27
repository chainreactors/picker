---
title: .NET 技术 | 调用系统API创建Windows服务
url: https://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247497381&idx=1&sn=4c2a31360b1963c2a343bd95ecc749f5&chksm=fa595848cd2ed15e1e5de87f7b28cf3294f8bc779b7076908bb8c61404128565cca43aaf9382&scene=58&subscene=0#rd
source: dotNet安全矩阵
date: 2024-12-11
fetch_date: 2025-10-06T19:41:31.252025
---

# .NET 技术 | 调用系统API创建Windows服务

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y990ZibCu931ibTOj3vcyYnyQx0KmY5S6yAibnbhz8xylk2dARhEbs8DPZzDpzjZIoeJLVH3vFxabUkg/0?wx_fmt=jpeg)

# .NET 技术 | 调用系统API创建Windows服务

原创

专攻.NET安全的

dotNet安全矩阵

01

阅读须知

此文所提供的信息只为网络安全人员对自己所负责的网站、服务器等（包括但不限于）进行检测或维护参考，未经授权请勿利用文章中的技术资料对任何计算机系统进行入侵操作。利用此文所提供的信息而造成的直接或间接后果和损失，均由使用者本人负责。本文所提供的工具仅用于学习，禁止用于其他方面

02

SCM函数基本介绍

在Windows操作系统中，Services服务是以后台进程的形式运行的，通常以高权限启动并运行。因此，红队经常利用.NET框架，通过创建和管理Windows服务来实现权限维持。

## 2.1 SCM函数原型

OpenSCManager是Windows API中的一个核心函数，用于打开服务控制管理器 (Service Control Manager, SCM) 数据库。服务控制管理器是Windows操作系统中管理服务的组件。通过这个函数，我们可以获取一个句柄，用于后续操作（如创建、查询、启动或停止服务）。函数原型如下所示。

```
```
[DllImport("advapi32.dll", CharSet = CharSet.Auto, SetLastError = true)]
private static extern IntPtr OpenSCManager(string machineName, string databaseName, uint dwAccess);
```
```

OpenSCManager函数需要提供三个参数，machineName: 指定目标计算机名称，databaseName: 指定要打开的数据库名称。dwAccess: 指定所需的访问权限，例如SC\_MANAGER\_CREATE\_SERVICE (值为2U)，允许创建系统服务，详细的权限说明如下所示。

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y990ZibCu931ibTOj3vcyYnyQQib418oOLibdGwscHXGZjstQAyROibMEt071MYiabmbXkKVVwwE6icobQgw/640?wx_fmt=png&from=appmsg)

当成功时，返回一个非零值 (IntPtr)，表示服务控制管理器数据库的句柄，如果遇到失败：返回IntPtr.Zero，可以通过调用Marshal.GetLastWin32Error获取详细的错误信息。

## 2.2 使用SCM函数

以下是一个使用OpenSCManager函数打开本地服务控制管理器并创建服务的完整示例，具体代码如下所示。

```
```
using System;
using System.Runtime.InteropServices;

class Program
{
    [DllImport("advapi32.dll", CharSet = CharSet.Auto, SetLastError = true)]
    private static extern IntPtr OpenSCManager(string machineName, string databaseName, uint dwAccess);

    const uint SC_MANAGER_CREATE_SERVICE = 0x2;

    static void Main()
    {
        // 打开服务控制管理器
        IntPtr scmHandle = OpenSCManager(null, null, SC_MANAGER_CREATE_SERVICE);

        // 检查返回值是否为零
        if (scmHandle == IntPtr.Zero)
        {
            int errorCode = Marshal.GetLastWin32Error();
            Console.WriteLine($"Failed to open SCM. Error Code: {errorCode}");
            return;
        }

        Console.WriteLine("Successfully opened the Service Control Manager.");

        // 后续逻辑：创建服务、启动服务等
        // ...

        // 记得关闭句柄（如果需要）
    }
}
```
```

上述代码，通过P/Invoke调用OpenSCManager函数，打开服务管理器的句柄，OpenSCManager是服务管理的起点，其返回的句柄直接影响后续操作的成功与否。使用时需注意提供正确的权限和参数，避免运行时错误。

03

CreateService基本介绍

成功获取SCM句柄后，可以通过调用CreateService函数创建一个新的系统服务，函数的原型如下所示。

```
```
[DllImport("Advapi32.dll")]
public static extern IntPtr CreateService(
    IntPtr serviceControlManagerHandle,
    string lpSvcName,
    string lpDisplayName,
    Program.SERVICE_ACCESS dwDesiredAccess,
    uint dwServiceType,
    uint dwStartType,
    uint dwErrorControl,
    string lpPathName,
    string lpLoadOrderGroup,
    IntPtr lpdwTagId,
    string lpDependencies,
    string lpServiceStartName,
    string lpPassword);
```
```

通常，创建服务时，需要提供服务的名称、显示名称、启动类型和服务路径等关键信息，详细参数列表如下所示。

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y990ZibCu931ibTOj3vcyYnyQ1Ept6oDj9ubhxXsLyhn5dHNBXqT9t5SSsibgcARZaXpEicRg5MGZDqWQ/640?wx_fmt=png&from=appmsg)

以下代码演示如何创建服务，服务创建失败，会返回IntPtr.Zero，需要处理错误，具体代码如下所示。

```
```
string serviceName = "MyService";
string serviceDisplayName = "My Custom Service";
string binPath = @"C:\Path\To\YourService.exe";

IntPtr serviceHandle = Program.CreateService(
    scmHandle,
    serviceName,
    serviceDisplayName,
    SERVICE_ACCESS.SERVICE_ALL_ACCESS,
    16U,
    2U,
    1U,
    binPath,
    null,
    IntPtr.Zero,
    null,
    null,
    null);

if (serviceHandle == IntPtr.Zero)
{
    throw new Exception("Failed to create service.");
}
```
```

04

工具实现

攻击者通过 Sharp4Stay.exe 工具，利用 OpenSCManager 和 CreateService 函数打开服务控制管理器数据库、创建系统服务以及启动服务等这些步骤，实现目标权限维持。

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y990ZibCu931ibTOj3vcyYnyQyDq1aia6AvlSJF8A1Hqial0am2QwpMibtt78sHBcmh17kUsNVKLeucohw/640?wx_fmt=jpeg&from=appmsg)

因为图片过长，不便于文章展示，因此通过隐藏部分用法达到缩短图片长度，不便之处请读者朋友们谅解。文章涉及的工具已打包在星球，感兴趣的朋友可以加入自取。

05

推荐阅读

从漏洞分析到安全攻防，我们涵盖了.NET安全各个关键方面，为您呈现最新、最全面的.NET安全知识，下面是公众号发布的精华文章集合，推荐大家阅读！

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8A7Qhn1ssuqNzv0iceS7ZhOuZ0AO4P1eFeG2xTdR2V6GWibiaxO2RenUJzrwOfvsdqofibI6H2uY0CLQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](https://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247497195&idx=1&sn=cf64ddd96482f7e25aa18fcc7283afdb&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8TQhCZMggf71ffibqISJ8f5naPJacnjn0roDyxxnAibmuwDJq2p1GTBpicZhnM9o9gTIu9S9ia8Uqwtw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&retryload=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247493952&idx=4&sn=db68011fb075c1d02268811163646b53&chksm=fa5947adcd2ecebbb1ca6659f289a5e344e37d1136fe0bd9272b5578e4c71bb19bb250e934d3&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y9tl26Kh2sQYI9guTCflSwQP8Gs9z7iamicOvlQv4UYzjwd378D03h7yEYFtZ6xA74qicInoed7qpBWg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247495167&idx=1&sn=9280c55fdc7c9146e549be470cf9f120&chksm=fa594312cd2eca04bfe8fd1fd3890b389d9c700b9b69d897f919addac399bab4f4d2e55f6b4f&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibQ6VpnKYXPqfmHnyJHzHxOeP3ichLEiafhGiawd8mjkHYBalO37fN8QQkNdic1hjjY2Nvw2Bib6UvibDRA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247490722&idx=2&sn=c9807daa5548e139a0c67303cb26882a&chksm=fa5ab24fcd2d3b59a85be03e69c655ffd644e8458bc2ec3f572da4b40b43e5003fda756f35b4&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibQ6VpnKYXPqfmHnyJHzHxOjWgak8cI7Mic1wTt3YSKqsbLl9rPe0cF9WGtOEuiceLreTNtNVib6IKlw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247490703&idx=2&sn=e7db1ff662e5b41d9a1806fbdf33e204&chksm=fa5ab262cd2d3b7470f029b9a07d1dd3611e63be910b01a601144efe7d84b5f016f488a354cf&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibQ6VpnKYXPqfmHnyJHzHxO8jJ97qqWlY6XR03DqSnutcHFYibDtVG5Y2wEaK4p2bzEicZblY4oQyGg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247490700&idx=2&sn=e8a865ada7c743e77fb9e953c5da74b1&chksm=fa5ab261cd2d3b7736387eddfc8524a378a1604552d0c9b55476646f9e8275f48818aab8acad&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibQ6VpnKYXPqfmHnyJHzHxOe1viaia4aoFceunsUdIna4DPbmemW1EqlBMrovOoE6bdAFF3iaApxz5qA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247488736&idx=2&sn=d24aaa297c51eb620ccdf67af513086d&chksm=fa5aba0dcd2d331bbb22f3f5657199d718c90efed42fcb9cb67ec23d342f887c117e4858f1cb&scene=21#wechat_redirect)

06

欢迎加入.NET安全星球

为了更好地应对基于.NET技术栈的风险识别和未知威胁，dotNet安全矩阵星球从创建以来一直聚焦于.NET领域的安全攻防技术，定位于高质量安全攻防星球社区，也得到了许多师傅们的支持和信任，通过星球深度连接入圈的师傅们，一起推动.NET安全高质量的向前发展。 星球门票后期价格随着内容和质量的不断沉淀会适当提高，因此越早加入越好！

    目前dot.Net安全矩阵星球已成为中国.NET安全领域最知名、最活跃的技术知识库之一，从.NET Framework到.NET Core，从Web应用到PC端软件应用，无论您是初学者还是经验丰富的开发人员，都能在这里找到对应的安全指南和最佳实践。

星球汇聚了各行业安全攻防技术大咖，并且每日分享.NET安全技术干货以及交流解答各类技术等问题，社区中发布很多高质量的.NET安全资源，可以说市面上很少见，都是干货。

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1YibzerwUbGOupPoJgYlZNMo1gg58eGoicPibjMBKkEo1zOia6zOyeupYasZZ9DTFvJVvzJQTEuhKrvTsA/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8DlZsGiaRRGghficKFQt58Ueoynsb0my3uzMAb7VwM5bgtnb4nbl4c9xdEjGraUXic6pO0p38xmWiaRQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibQ6VpnKYXPqfmHnyJHzHxOc2SogKzZ16SD7dpzF3v81kia4ZAx5QU5ibnNibEo8kZZSJgrficz4Ckxwg/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

星球文化始终认为授人以鱼不如授人以渔！加入星球后可以跟星主和嘉宾们一对一提问交流，20+个专题栏目涵盖了点、线、面、体等知识面，助力师傅们快速成长！其中主题包括.NET Tricks、漏洞分析、内存马、代码审计、预编译、反序列化、webshell免杀、命令执行、C#工具库等等。![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YiccvW0LwqSx3grm4bgM0fz01qCxrYGBR94wibZ7sk1zIO9DzCgviab9vmUic8qmvynXhSM8LxFhGG97w/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

    我们倾力打造专刊、视频等配套学习资...
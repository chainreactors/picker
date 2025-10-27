---
title: 通过 Sharp4Tokenvator 实现本地权限提升
url: https://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247498493&idx=3&sn=d4029c2b542db791a7c4a70127b369fc&chksm=fa595410cd2edd069e4d76454b7789a94293ccb94a2ca643ad9f8b6bb7689ce4f47c1adf7a35&scene=58&subscene=0#rd
source: dotNet安全矩阵
date: 2025-01-28
fetch_date: 2025-10-06T20:10:40.767846
---

# 通过 Sharp4Tokenvator 实现本地权限提升

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibKNCffFFT7ozQS3EUtqEia7O2q2PuVe9l5SYHPDdP7vaXI8riak7e4FbvXQibBIiaz7iaIpal6tDoKgUg/0?wx_fmt=jpeg)

# 通过 Sharp4Tokenvator 实现本地权限提升

原创

专攻.NET安全的

dotNet安全矩阵

![](https://mmbiz.qpic.cn/mmbiz_gif/NO8Q9ApS1YibJO9SDRBvE01T4A1oYJXlTBTMvb7KbAf7z9hY3VQUeayWI61XqQ0ricUQ8G1FykKHBNwCqpV792qg/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp)

命名管道是进程间通信中常用的一种机制，它提供了高效、安全的双向数据传输能力，尤其适用于同一台计算机上的多个进程之间通信，甚至可以通过网络与远程计算机进行数据交换。在 .NET 中，NamedPipeServerStream 类是实现命名管道服务器端的核心工具，支持多客户端连接、双向通信以及灵活的安全配置。

接下来，我们将深入了解其核心构造函数、常用属性与方法，并通过示例代码展示如何创建一个简单的命名管道服务器。

**01. 管道访问配置**

在Windows操作系统中，通过命名管道实现进程间通信是一种常见的技术。而在权限提升场景下，命名管道常用于客户端与服务端通信，同时为实现令牌模拟提供支持。

在 .NET 中通常使用 PipeSecurity 类为管道设置访问控制规则，用于管理命名管道的访问控制列表（ACL）。通过这个类，可以为命名管道配置精细化的安全权限，从而控制哪些用户或用户组能够访问管道，以及他们可以执行的操作。

最常用的方法是 AddAccessRule，用于向命名管道的访问控制列表中添加一条新的访问规则。

以下代码展示了如何使用 PipeSecurity 和 PipeAccessRule 配置管道的访问权限。

```
```
using System;
using System.IO.Pipes;
using System.Security.AccessControl;

class Program
{
    static void Main()
    {
        PipeSecurity pipeSecurity = new PipeSecurity();
        pipeSecurity.AddAccessRule(new PipeAccessRule(
            "Everyone",
            PipeAccessRights.ReadWrite,
            AccessControlType.Allow));
        using (NamedPipeServerStream namedPipeServerStream = new NamedPipeServerStream(
            "TestPipe",
            PipeDirection.InOut,
            1,
            PipeTransmissionMode.Message,
            PipeOptions.None,
            128,
            128,
            pipeSecurity))
        {
            Console.WriteLine("管道已创建，等待客户端连接...");
            namedPipeServerStream.WaitForConnection();
            Console.WriteLine("客户端已连接！");
        }
    }
}
```
```

何使用 PipeSecurity 和 PipeAccessRule不过，在生产环境中，应限制对管道的访问，仅允许特定用户组使用。例如，可以使用管理员组。

```
```
pipeSecurity.AddAccessRule(new PipeAccessRule("Administrators", PipeAccessRights.FullControl, AccessControlType.Allow));
```
```

**02. 命名管道服务器**

NamedPipeServerStream 是 .NET 提供的命名管道服务器端实现类，用于实现进程间通信。允许创建一个命名管道服务器，以便客户端通过管道名称连接，并与服务器进行数据交换。

命名管道是双向通信的一种机制，可以用于同一台计算机上的不同进程之间通信，或者通过网络与远程计算机通信，具体使用代码如下所示。

```
```
public NamedPipeServerStream(
    string pipeName,
    PipeDirection direction,
    int maxNumberOfServerInstances = NamedPipeServerStream.MaxAllowedServerInstances,
    PipeTransmissionMode transmissionMode = PipeTransmissionMode.Byte,
    PipeOptions options = PipeOptions.None,
    int inBufferSize = 0,
    int outBufferSize = 0,
    PipeSecurity pipeSecurity = null
)
```
```

上述代码中，pipeName 表示管道名称，客户端需要通过该名称连接。direction 参数表示管道的方向，可以是 In（只读）、Out（只写）或 InOut（读写）。

具体实际的用法，可以参考如下代码展示了如何创建一个简单的命名管道服务器。

```
```
using System;
using System.IO;
using System.IO.Pipes;
using System.Text;

class Program
{
    static void Main()
    {
        string pipeName = "TestPipe";
        using (NamedPipeServerStream pipeServer = new NamedPipeServerStream(
            pipeName,
            PipeDirection.InOut,
            NamedPipeServerStream.MaxAllowedServerInstances,
            PipeTransmissionMode.Message,
            PipeOptions.Asynchronous))
        {
            Console.WriteLine($"管道已创建: {pipeName}");
            Console.WriteLine("等待客户端连接...");

            pipeServer.WaitForConnection();
            Console.WriteLine("客户端已连接");

            byte[] message = Encoding.UTF8.GetBytes("Hello from server");
            pipeServer.Write(message, 0, message.Length);
            Console.WriteLine("消息已发送");

            byte[] buffer = new byte[256];
            int bytesRead = pipeServer.Read(buffer, 0, buffer.Length);
            string receivedMessage = Encoding.UTF8.GetString(buffer, 0, bytesRead);
            Console.WriteLine($"收到客户端消息: {receivedMessage}");
        }
    }
}
```
```

**03. 工具实战操作**

Sharp4Tokenvator 便是这样一款基于命令管道实现的 Windows 令牌访问工具，主要用于模拟低权限用户到高权限用户。通过工具，用户可以借助系统中高权限进程的令牌，创建新的进程并以高权限运行，从而实现权限提升。

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibKNCffFFT7ozQS3EUtqEia7FUAwocSInIT0CbaWxwPL1zV5aZNFt52Hz52PkREa8ibllRlJjmJzxRw/640?wx_fmt=jpeg&from=appmsg)

## 3.1 工具用法

以下是使用 Sharp4Tokenvator.exe 工具的基本步骤，使用工具提供的Steal\_Token 命令接口，利用目标进程的令牌模拟高权限用户并执行命令。

```
```
Steal_Token /Process:3576 /Command:cmd.exe
```
```

其中，3576为目标进程PID，如下图所示。

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1YibKNCffFFT7ozQS3EUtqEia7RnwUsmRUF5vqaVKXGXOhZhaWkbQDz8jxoRRs36cVRvD16blKocolzA/640?wx_fmt=png&from=appmsg)

综上，Sharp4Tokenvator是一个强大的令牌操作工具，其基于.NET的实现使其在Windows系统中具有高度的灵活性和适用性，文章涉及的工具已打包在星球，感兴趣的朋友可以加入自取。

**04. 技术精华内容**

从漏洞分析到安全攻防，我们涵盖了 .NET 安全各个关键方面，为您呈现最新、最全面的 .NET 安全知识，下面是公众号发布的精华文章集合，推荐大伙阅读！

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8TQhCZMggf71ffibqISJ8f5naPJacnjn0roDyxxnAibmuwDJq2p1GTBpicZhnM9o9gTIu9S9ia8Uqwtw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&retryload=1&tp=webp)](https://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247497498&idx=2&sn=00900a0c29c85b41fe6a586d7e5c3571&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y9tl26Kh2sQYI9guTCflSwQP8Gs9z7iamicOvlQv4UYzjwd378D03h7yEYFtZ6xA74qicInoed7qpBWg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247495167&idx=1&sn=9280c55fdc7c9146e549be470cf9f120&chksm=fa594312cd2eca04bfe8fd1fd3890b389d9c700b9b69d897f919addac399bab4f4d2e55f6b4f&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibQ6VpnKYXPqfmHnyJHzHxOeP3ichLEiafhGiawd8mjkHYBalO37fN8QQkNdic1hjjY2Nvw2Bib6UvibDRA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247490722&idx=2&sn=c9807daa5548e139a0c67303cb26882a&chksm=fa5ab24fcd2d3b59a85be03e69c655ffd644e8458bc2ec3f572da4b40b43e5003fda756f35b4&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibQ6VpnKYXPqfmHnyJHzHxOjWgak8cI7Mic1wTt3YSKqsbLl9rPe0cF9WGtOEuiceLreTNtNVib6IKlw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247490703&idx=2&sn=e7db1ff662e5b41d9a1806fbdf33e204&chksm=fa5ab262cd2d3b7470f029b9a07d1dd3611e63be910b01a601144efe7d84b5f016f488a354cf&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibQ6VpnKYXPqfmHnyJHzHxO8jJ97qqWlY6XR03DqSnutcHFYibDtVG5Y2wEaK4p2bzEicZblY4oQyGg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247490700&idx=2&sn=e8a865ada7c743e77fb9e953c5da74b1&chksm=fa5ab261cd2d3b7736387eddfc8524a378a1604552d0c9b55476646f9e8275f48818aab8acad&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibQ6VpnKYXPqfmHnyJHzHxOe1viaia4aoFceunsUdIna4DPbmemW1EqlBMrovOoE6bdAFF3iaApxz5qA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247488736&idx=2&sn=d24aaa297c51eb620ccdf67af513086d&chksm=fa5aba0dcd2d331bbb22f3f5657199d718c90efed42fcb9cb67ec23d342f887c117e4858f1cb&scene=21#wechat_redirect)

**05. 加入安全社区**

目前dot.Net安全矩阵星球已成为中国.NET安全领域最知名、最专业的技术知识库之一，超 **1200+** 成员一起互动学习。星球主题数量近 **600+**，精华主题 230+，PDF文档和压缩包 300+ 。从Web应用到PC端软件应用，无论您是初学者还是经验丰富的开发人员，都能在这里找到对应的实战指南和最佳实践。

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y9AiaXibTRdEnEfYuQx76FjZVjmyEWtIaDuDePFFmyRqggiaq2k47pLoib9GZtUCOhaP40WPlhvbiaKZVg/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

## 20+专栏文章

星球文化始终认为授人以鱼不如授人以渔！星球整理出**20+**个专题栏目涵盖 **.NET安全 点、线、面、体等知识范围**，助力师傅们实战攻防！其中主题包括.NET  内网攻防、漏洞分析、内存马、代码审计、预编译、反序列化、WebShell免杀、命令执行、工具库等等。

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8xRheDpQ7NsESosdNZUopa90SJRuwnLy9uZV4icrXiaZlJPQlYJWXTw8HCrF9oTcE3DDgrdFnXo2BA/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

## 海量资源和工具

截至当前，dot.Net安全矩阵星球社区汇聚了 **600+** 个实用工具和高质量PDF学习资料。这些资源涵盖了攻防对抗的各个方面，在实战中能够发挥显著作用，为对抗突破提供强有力的支持。

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8xRheDpQ7NsESosdNZUopaqVZW8XsALVA4FNiaj32q8npN82VSeqSKb4fQvLiczFNs0099VRFVQwPA/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8xRheDpQ7NsESosdNZUopa63ZXbX3YXLwoeNnjStcRtTbU9hoe6ecO5hhkj2apG1I6...
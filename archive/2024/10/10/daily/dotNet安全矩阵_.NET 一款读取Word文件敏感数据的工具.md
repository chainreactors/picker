---
title: .NET 一款读取Word文件敏感数据的工具
url: https://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247495880&idx=3&sn=06cdfc43d9a1d014ccaf9674e857cdf9&chksm=fa595e25cd2ed733522eb3cee1772895ecfd310d6db435bc87ccf30777bc60066eb564fc9db6&scene=58&subscene=0#rd
source: dotNet安全矩阵
date: 2024-10-10
fetch_date: 2025-10-06T18:53:49.617928
---

# .NET 一款读取Word文件敏感数据的工具

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y9M4REibpm76wTYNDGxNkc7aXibt2OAXJ2ibUjoaV5ib35kM4XYxJ2dZ3gRHrSEbT9Gj97bX26aETDgeQ/0?wx_fmt=jpeg)

# .NET 一款读取Word文件敏感数据的工具

原创

专攻.NET安全的

dotNet安全矩阵

01

阅读须知

此文所提供的信息只为网络安全人员对自己所负责的网站、服务器等（包括但不限于）进行检测或维护参考，未经授权请勿利用文章中的技术资料对任何计算机系统进行入侵操作。利用此文所提供的信息而造成的直接或间接后果和损失，均由使用者本人负责。本文所提供的工具仅用于学习，禁止用于其他方面

02

基本介绍

Sharp4ReadWord.exe 是一款专为红队活动设计的工具，能够自动化地读取 Microsoft Word 文档内容，在企业内网环境中批量收集信息，快速查找敏感数据。

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y9M4REibpm76wTYNDGxNkc7a5Cwj6BB6fhqd3F3tHoukkUNx9KPVSqOE6I4YGTmuTd1uU1JXiadkr0w/640?wx_fmt=jpeg&from=appmsg)

03

使用方法

Sharp4ReadWord.exe 主要用于打开和读取指定的 Word 文档，支持指定文档路径及密码。

## 3.1 读取未加密的文档

在命令行中可以通过以下方式使用此工具，读取没有密码保护的文档，命令如下所示。

```
Sharp4ReadWord.exe 1.docx
```

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y9M4REibpm76wTYNDGxNkc7aBsm1Xe8cXJAvicicicsIyeoFWeEnWENb4oWfSanW8nJORIEecqSeA7qTA/640?wx_fmt=png&from=appmsg)

## 3.2 读取有密码保护的文档

当需要读取多个文档或逐一批量操作多个文件时，可以将这些命令封装成批处理脚本，在内网环境中批量处理并搜索特定关键字或敏感数据，通过指定-password参数解密，具体命令如下所示。

```
Sharp4ReadWord.exe 1.docx -password 123456
```

04

原理解析

Sharp4ReadWord.exe 其核心功能通过 for 循环处理用户输入的参数。-checkPassword 选项用于标记是否需要检测文档密码，-password 选项用于输入文档密码，具体代码如下所示。

```
```
if (args.Length == 0)
    {
        PrintHelpMenu();
        return;
    }

    string docFullPath = Path.GetFullPath(args[0]);
    string docName = Path.GetFileName(docFullPath);
    bool checkPassword = false;
    string documentPassword = null;

    // 处理命令行参数
    for (int i = 1; i < args.Length; i++)
    {
        if (string.Equals(args[i], "-checkPassword", StringComparison.OrdinalIgnoreCase))
        {
            checkPassword = true;
        }
        else if (string.Equals(args[i], "-password", StringComparison.OrdinalIgnoreCase) && i + 1 < args.Length)
        {
            documentPassword = args[i + 1];
            i++;
        }
    }
```
```

随后，通过 IsProcessRunning("winword") 检查系统中是否有正在运行的 Word 进程，如果 Word 程序已运行，调用 GetActiveObject("Word.Application") 获取当前活动的 Word 实例，并禁用弹窗警告 (DisplayAlerts) 以静默方式打开文档。

```
```
 if (isWordRunning)
        {
            Console.WriteLine("OPSEC WARNING: Microsoft Word is currently running...Using existing Winword Application\n");
            wordApp = (Application)Marshal.GetActiveObject("Word.Application");
            if (wordApp == null)
            {
                throw new Exception("Failed to get active Word application");
            }
            wordApp.DisplayAlerts = WdAlertLevel.wdAlertsNone;
            isWordOpen = true;
        }
        else
        {
            Console.WriteLine("Microsoft Word is not running...Using New COM Winword Application. \n");
            wordApp = new Application();
            if (wordApp == null)
            {
                throw new Exception("Failed to create new Word application");
            }
            wordApp.Visible = false;
            wordApp.DisplayAlerts = WdAlertLevel.wdAlertsNone;
            isWordOpen = false;
        }
```
```

上述代码，如果 Word 未运行，则使用 new Application() 创建一个新的 Word 应用实例，并设置为不可见 (Visible = false)，防止弹出窗口暴露操作痕迹。

综上，Sharp4ReadWord.exe 是一款非常实用的内网文档批量读取工具，通过检测系统进程状态、支持密码验证，并使用 COM 对象进行 Word 操作，实现了高效、便捷的信息收集。工具已经打包在星球，感兴趣的朋友可以加入自取。

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

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y9ZQNibdZiazX...
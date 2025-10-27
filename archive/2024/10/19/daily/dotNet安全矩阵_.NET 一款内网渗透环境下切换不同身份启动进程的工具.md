---
title: .NET 一款内网渗透环境下切换不同身份启动进程的工具
url: https://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247496071&idx=3&sn=219b08b40cb36c10269661e2f089d269&chksm=fa595f6acd2ed67ceeca2235f5b1796e45689dff604107b5d2c163dc209933ec275ba39f77ae&scene=58&subscene=0#rd
source: dotNet安全矩阵
date: 2024-10-19
fetch_date: 2025-10-06T18:53:15.226680
---

# .NET 一款内网渗透环境下切换不同身份启动进程的工具

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Yib5CJlFmEOTeruxSS2L8gEiagbvAVXg2ImGquJibUesf1Be19b20jHAsy0icA28icIjXzKoHiayOD2baLQ/0?wx_fmt=jpeg)

# .NET 一款内网渗透环境下切换不同身份启动进程的工具

原创

专攻.NET安全的

dotNet安全矩阵

01

阅读须知

此文所提供的信息只为网络安全人员对自己所负责的网站、服务器等（包括但不限于）进行检测或维护参考，未经授权请勿利用文章中的技术资料对任何计算机系统进行入侵操作。利用此文所提供的信息而造成的直接或间接后果和损失，均由使用者本人负责。本文所提供的工具仅用于学习，禁止用于其他方面

02

基本介绍

Sharp4UserId.exe 是一款专为红队设计的工具，通过指定的账户和密码，以不同身份启动新进程，赋予进程对应的权限，从而实现内网提权或降权。还可以通过添加 --bypass-uac 参数绕过 UAC，以管理员身份启动高权限进程。

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Yib5CJlFmEOTeruxSS2L8gEianJf84xbRJQD2tcvGx4azhI0gkOiazvkzCXWODOdw67VIgXejI0RpV1Q/640?wx_fmt=jpeg&from=appmsg)

03

使用方法

Sharp4UserId.exe 在已知用户账户和密码的情况下，可以以该用户的身份启动高权限进程，例如管理员账户。也可以使用普通用户启动新进程以限制其访问权限。

```
Sharp4UserId.exe Admin 123456 "cmd /c whoami /all"
```

例如，以普通用户Admin 运行命令 cmd /c whoami /all，如下图所示。

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Yib5CJlFmEOTeruxSS2L8gEiaKiaTlWUAP1k0d1bsqa1xJnEZ550rMus4x1xMnBhXZSB8jicSkh0qDN8Q/640?wx_fmt=png&from=appmsg)

另外，添加 --bypass-uac 参数，可以在高权限账户下绕过 UAC。

```
Sharp4UserId.exe Admin 123456 "cmd /c whoami /all" --bypass-uac
```

04

原理解析

工具首先使用 ParseCommonProcessesInCommandline 方法解析命令行参数，并设置 startupinfo 结构体的相关字段。startupinfo 结构体是 Windows API 中用于指定启动进程的窗口设置和控制台信息的结构体，具体代码如下所示。

```
```
string text = this.ParseCommonProcessesInCommandline(cmd);
int logonProvider = 0;
int num = 0;
RunasCs.STARTUPINFO startupinfo = default(RunasCs.STARTUPINFO);
startupinfo.cb = Marshal.SizeOf(startupinfo);
startupinfo.lpReserved = null;
RunasCs.ProcessInformation processInformation = default(RunasCs.ProcessInformation);
this.RunasSetupStdHandlesForProcess(processTimeout, remote, ref startupinfo, out this.hOutputWrite, out this.hErrorWrite, out this.hOutputRead, out this.socket);
```
```

随后，使用 WindowStationDACL 类为当前会话添加访问控制列表 (ACL)，使指定的用户拥有访问权限。这一步将用户的会话桌面名称 (text2) 赋值给 startupinfo.lpDesktop，确保启动的进程在该用户的桌面环境中运行。

```
```
this.stationDaclObj = new WindowStationDACL();
string text2 = this.stationDaclObj.AddAclToActiveWindowStation(domainName, username, logonType);
startupinfo.lpDesktop = text2;
```
```

接着，通过 EnablePrivilege 方法启用 SeAssignPrimaryTokenPrivilege 权限，确保能够在指定的用户上下文中创建进程，代码如下所示。

```
```
private void RunasCreateProcessAsUserW(
    string username,
    string domainName,
    string password,
    int logonType,
    int logonProvider,
    string commandLine,
    bool forceUserProfileCreation,
    bool userProfileExists,
    ref RunasCs.STARTUPINFO startupInfo,
    ref RunasCs.ProcessInformation processInfo,
    ref int logonTypeNotFiltered)
{
    this.GetUserEnvironmentBlock(zero2, username, forceUserProfileCreation, userProfileExists, out zero3);
    AccessToken.EnablePrivilege("SeAssignPrimaryTokenPrivilege", WindowsIdentity.GetCurrent().Token);
    AccessToken.EnableAllPrivileges(zero2);

    if (!RunasCs.CreateProcessAsUser(
            zero2,
            null,
            commandLine,
            IntPtr.Zero,
            IntPtr.Zero,
            true,
            134218752U,
            zero3,
            Environment.GetEnvironmentVariable("SystemRoot") + "\\System32",
            ref startupInfo,
            out processInfo))
    {
        throw new RunasCsException("CreateProcessAsUser", true);
    }
}
```
```

最后，通过CreateProcessAsUser 以特定用户身份启动新进程的关键方法，允许工具在指定用户的上下文中运行所需的命令。

综上，Sharp4UserId.exe 是一款强大的红队工具，通过创建特定用户上下文进程实现灵活的权限控制。通过深入了解其代码实现与用法，可以在红队活动中更高效地切换权限，以适应不同场景需求。工具已经打包在星球，感兴趣的朋友可以加入自取。

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
...
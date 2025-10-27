---
title: .NET 一款通过虚拟键盘绕过UAC的工具
url: https://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247495465&idx=1&sn=4cca2bb0b9c92c93161e88d8f0b019a0&chksm=fa5941c4cd2ec8d2a908e2bd960e64158f63753c8f60f7a0824de16245f4409916debff5fbf2&scene=58&subscene=0#rd
source: dotNet安全矩阵
date: 2024-09-24
fetch_date: 2025-10-06T18:27:50.637762
---

# .NET 一款通过虚拟键盘绕过UAC的工具

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YicbkHOYUFtfAaVDIvxnbLnAaadDgjdNoibibbrmGFV2nNNPXGdnSjiaaYYbVPuicmouviaQNrVRnaqQYDg/0?wx_fmt=jpeg)

# .NET 一款通过虚拟键盘绕过UAC的工具

原创

专攻.NET安全的

dotNet安全矩阵

01

阅读须知

此文所提供的信息只为网络安全人员对自己所负责的网站、服务器等（包括但不限于）进行检测或维护参考，未经授权请勿利用文章中的技术资料对任何计算机系统进行入侵操作。利用此文所提供的信息而造成的直接或间接后果和损失，均由使用者本人负责。本文所提供的工具仅用于学习，禁止用于其他方面

02

基本介绍

Sharp4UAC是一款通过控制Windows虚拟键盘，实现在不弹出 UAC 提示的情况下，以管理员权限启动新的进程，从而绕过了 UAC 限制。这种技术常用于高级持久性威胁和渗透测试中，尤其是在需要提升权限的场景下。

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YicbkHOYUFtfAaVDIvxnbLnA45BVibucaZaplhHtjLPBRSb2M1DYHGG5iawLfwcXQ2mqicKSKicBibB6TzA/640?wx_fmt=jpeg&from=appmsg)

03

使用方法

比如默认情况下当前的用户进程没有以管理员权限运行，属于普通用户权限。这种进程只能访问属于中等或低级别的资源，不能修改系统范围内的设置或执行高权限操作。

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8P8gy09FzIjLrrsDjBHVoFwFvtwRAuonq1BcxmYFD4gMj4hOWiaiamIpjf3wCNicsmrQcOzQPL0VEKQ/640?wx_fmt=png&from=appmsg)

图中命令返回 Mandatory Label\Medium Mandatory Level 并附带 S-1-16-8192 时，表示当前进程运行在中等完整性级别，表示没有以管理员权限运行，属于普通用户权限。

随后，Sharp4UAC 通过 PowerShell.exe 调用 uiAccessPlease 方法，以管理员身份运行新的 PowerShell 进程，具体命令如下所示。

```
```
add-type -path C:\Users\Ivan1ee\Desktop\Sharp4UAC.dll
```
```

上面的命令首先加载 Sharp4UAC.dll，然后调用 uiAccessPlease 方法，启动一个以管理员权限运行的 PowerShell 实例。再次输入 whoami /all 命令返回 Mandatory Label\High Mandatory Level  S-1-16-12288，表示具备了管理员权限。如下图所示。

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8P8gy09FzIjLrrsDjBHVoFYZVrj6QiciaPtiaIRVc4HgO76aOA5nzbqSj1MoPF7GQux9K6aEmkD25gA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8P8gy09FzIjLrrsDjBHVoFBSkpRG5kabNr0exnkAxnT1FovDZwKicLVEfcw24e38iaiad7UuEBn4MHA/640?wx_fmt=png&from=appmsg)

因此，该工具适用于渗透测试、红队活动以及其他需要静默权限提升的场景。例如，当测试人员试图绕过 UAC 限制、执行高权限操作时，Sharp4UAC可以帮助实现目标，而不会在用户界面中弹出权限提示。

04

原理解析

Sharp4UAC 核心机制是使用 uiAccessPlease 方法的核心功能是通过操作系统自带的辅助工具—如虚拟键盘 (osk.exe) 来提升进程的权限，首先，使用 Windows API 获取 osk.exe 的进程句柄和进程令牌。这是因为 osk.exe 在某些系统中默认以高权限运行

```
```
int TokenIntegrityLevel = 25;
TrollUAC.STARTUPINFO si = default(TrollUAC.STARTUPINFO);
si.cb = (uint)Marshal.SizeOf<TrollUAC.STARTUPINFO>(si);
TrollUAC.PROCESS_INFORMATION pi = default(TrollUAC.PROCESS_INFORMATION);
int oskPID = TrollUAC.spawn("C:\\windows\\system32\\osk.exe");
IntPtr hProcess = TrollUAC.OpenProcess(TrollUAC.ProcessAccessFlags.QueryLimitedInformation, true, oskPID);
```
```

接着，复制 osk.exe 的进程令牌，并设置其完整性级别，以便新进程能继承高权限。这一步通过 DuplicateTokenEx 和 SetTokenInformation 函数实现。

```
```
TrollUAC.DuplicateTokenEx(hToken, 983551U, ref sa, 2, 1, ref DuplicatedToken);
TrollUAC.SetTokenInformation(DuplicatedToken, TokenIntegrityLevel, tokenMandatoryLabel, Marshal.SizeOf<TrollUAC.TOKEN_MANDATORY_LABEL>(tokenMandatoryLabel) + TrollUAC.GetLengthSid(sidPtr));
```
```

然后，工具创建使用 CreateProcessAsUser 创建新进程并执行脚本，具体代码如下所示。

```
```
TrollUAC.SpitFile("C:\\users\\public\\troll.vbs");
TrollUAC.CreateProcessAsUser(DuplicatedToken, null, "cscript.exe //NOLOGO c:\\users\\public\\troll.vbs", ref sa, ref sa, true, 0U, IntPtr.Zero, null, ref si, out pi);
```
```

综上，Sharp4UAC是一款非常有效的 UAC 绕过工具，通过利用高权限进程来提升权限，并执行用户指定的脚本或命令。它的实现方式不仅规避了 UAC 弹窗，同时提供了一种简便而隐蔽的方式来获得管理员权限。工具已经打包在星球，感兴趣的朋友可以加入自取。

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

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y9ZQNibdZiazXl9zhxh3wB9n5LXcwJqbvQywJQLsckcGGV6NNWLITK1VkDV2CPeahvyUbPNPCRATEmA/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co...
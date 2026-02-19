---
title: Impacket 开发指南：第二部分 - 系统中的 RPC 发现与安全机制解析
url: https://mp.weixin.qq.com/s/vWVirHHfVVuEioXkjb2Xbw
source: Doonsec's feed
date: 2026-02-18
fetch_date: 2026-02-19T04:15:36.460834
---

# Impacket 开发指南：第二部分 - 系统中的 RPC 发现与安全机制解析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/h4gtbB74nSiaibfUN7zIHo2tGQdPgRh1yz0ibKBSyYGAshq7EAz3DRJNyUJuVu7mb8Z9JQgrdgWNRofwmkoSjl7kia32BuMYeJKyeIuaArvczgM/0?wx_fmt=jpeg)

# Impacket 开发指南：第二部分 - 系统中的 RPC 发现与安全机制解析

CICADA8
CICADA8

securitainment

![]()

在小说阅读器中沉浸阅读

| 原文链接 | 作者 |
| --- | --- |
| https://cicada-8.medium.com/impacket-developer-guide-part-2-finding-rpc-on-the-system-and-some-words-about-in-security-7df65acbd621 | CICADA8 |

# ![Impacket Developer Guide Part 2](https://mmbiz.qpic.cn/mmbiz_png/h4gtbB74nSjWKawg9GI1yFqphKc4TDFVvrTlCAkGgDULZ5e4Pu8POB2xO4AZwleWDYns2srib8FrI5fqjicUibFA0hlkPduGJyLR1a7zytW3PE/640?wx_fmt=png&from=appmsg)

大家好，我叫 Michael Zhmailo，是 CICADA8 团队的渗透测试专家。

这是关于使用 Impacket 进行开发的系列文章的延续。在上一部分中，我们了解了 RPC 的工作原理，学习了基本概念，还创建了一个客户端和服务器。

在这一部分中，我将向你介绍一些工具，它们可以帮助你在系统上找到正在运行的 RPC 服务器，同时我们还会探讨一些 RPC 服务器的安全问题。

如果你想学习 RPC 基础知识，请先阅读第一部分。

## 探索系统上的 RPC 服务器

总体而言，有以下几种方法可以找到 RPC 服务器及其方法：

* 查找和探索 IDL 文件；
* 从 epmapper 服务获取信息；
* PE 文件分析；
* 被动探索。

让我们从最后一种方法开始。

### 被动探索

该方法基于这样一个事实：特定服务器提供的 RPC 方法早已被人熟知和研究。而且，已经提供了调用这些方法所需的封装器。例如，要研究潜在的有趣功能，你可以参考 WindowsRpcClients 仓库，然后选择你感兴趣的 RPC 方法所在的文件。

![被动探索示例](https://mmbiz.qpic.cn/sz_mmbiz_png/h4gtbB74nShOoODkMKBg8BAIcaeYHHjWiagBRhIPP0IZJyaD0cGbrH2uWMnP31PKkSia4RtlQKmko8KOW2L1gYFozibp9aL1LibXlzREdejqwRk/640?wx_fmt=png&from=appmsg)

被动探索示例

例如，在这个案例中，我们可以看到 *lsaiso.exe*内部有一个 RPC 服务器，在 UUID 为 *57cce375-4430-47a6-bb96-2cad0d2fd140*的接口内有一个方法 *BCryptIumSignHash()*。

这种方法对于研究知名的 RPC 接口非常有用。甚至有一个已知接口的列表：

* 端点 `\\pipe\lsarpc`上有：LSARPC (*12345778-1234-abcd-ef00-0123456789ab*)、LSA Directory Services (*3919286a-b10c-11d0-9ba8-00c04fd92ef5*)；
* `\\pipe\samr`

  — SAMR (*12345778-1234-abcd-ef00-0123456789ac*)；
* `\\pipe\atsvc`

  — Task Scheduler (*1ff70682-0a51-30e8-076d-740be8cee98b*)；
* `\\pipe\winreg`

  — Windows Remote Registry (*338cd001-2244-31f1-aaaa-900038001003*)；
* `\\pipe\svcctl`

  — Service Control Manager (*367abb81-9844-35f1-ad32-98f038001003*)；
* `\\pipe\srvsvc`

  — Service Control Manager (*4b324fc8-1670-01d3-1278-5a47bf6ee188*)；
* 以及其他......

此外，你可以在 MSDN 上找到特定协议的文档。例如，我们可以查看 MS-EVEN 协议，发现它通过 *82273FDC-E32A-18C3-3F78-827929DC23EA*接口运行，并且我们需要通过 *pipeeventlog*连接到此 RPC 服务器。

![连接详情](https://mmbiz.qpic.cn/sz_mmbiz_png/h4gtbB74nSjebp8egUa7tQU4DcDcUEeU3CMv9JVO3EslXTiaJeyI2ObVY41niabrCqqInPF5vrVW5dN8Eosc6Qiakibtia5RaibguiaSSP6xOibic28U/640?wx_fmt=png&from=appmsg)

连接详情

文档中还包含可与此 RPC 服务器一起使用的方法、结构和类的描述。

![MS-EVEN 函数](https://mmbiz.qpic.cn/sz_mmbiz_png/h4gtbB74nSh6yNHyR66qics3jVL2lu7ficEHyygunicKcYZZqh8FTC65gl6GpGLicFHu00A8YHoyic7yiaIibltM2iboJibKHR3s0UpITzW9mLg32Rhg/640?wx_fmt=png&from=appmsg)

MS-EVEN 函数

如果服务器使用动态端点，文档中也会有相关说明。例如，MS-DRSR 就是这样做的。

![MS-DRSR 动态端点文档](https://mmbiz.qpic.cn/sz_mmbiz_png/h4gtbB74nSjq1kwRqRERr6pcBITXliaPuN8x8uw9HicFPxGjAV5Kstce9O7zVvHJbnpUiaqqtYeMbIXk9Kh739FAGlpyMzlhJrVWSCsncjK0rY/640?wx_fmt=png&from=appmsg)

MS-DRSR 动态端点文档

### PE 文件分析

这种方法稍微复杂一些，但我们后面要讨论的大多数工具都使用了它。简而言之，它基于在特定文件中检测正在运行的 RPC 服务器。其主要指标是导入了 *rpcrt4.dll\_，或者使用了特殊的 RPC 函数，如*RpcStringBindingCompose()*。如果我们更详细地看，在正在运行的 RPC 服务器的 PE 文件的*.data\_ 节中，有一个符号 \_GlobalRpcServer\_，它是一个描述此 RPC 服务器的复杂结构体 *RPC\_SERVER\_T*。

![RPC\_SERVER\_T 结构体示例](https://mmbiz.qpic.cn/mmbiz_png/h4gtbB74nShGQRBvvVbDeLGnECz3yz144ibmtXPAVXvueVXOWG9alPE64yzxBAtgIicKVAcvUI3ZJELKRvX6SpAugQTgVKwUh98l1K0jkEibZo/640?wx_fmt=png&from=appmsg)

RPC\_SERVER\_T 结构体示例

一旦你找到了 RPC\_SERVER\_T，就可以继续研究 RPC 服务器的接口了。接口以 *RPC\_INTERFACE\_T*结构体的形式呈现。

![RPC\_INTERFACE\_T 结构体示例](https://mmbiz.qpic.cn/sz_mmbiz_png/h4gtbB74nSgGawHuicn3YLLSUxSYib17dnujPeDQEib4D1Shgm26VTIUALdiaNRqNItibf8BmNwXojc1ariafmaa7EWG7Y0ZMcgb22oL4XpDCvbGI/640?wx_fmt=png&from=appmsg)

RPC\_INTERFACE\_T 结构体示例

然后剩下的就是正确解析这个结构体，研究所有标志位和一些负责安全的参数，最后探索可用的 RPC 方法。值得注意的是，RPC 方法的名称通常通过 PDB 文件提取。你可以在这篇博客中找到对这些结构体的详细分析和研究。

有很多工具可以以这种方式分析 PE 文件，稍后我会列出它们。现在让我们进入下一种查找 RPC 服务器的方法。

### 从 epmapper 服务获取信息

你可能还记得，如果 RPC 服务器使用动态端点，它必须向 Endpoint Mapper 服务注册自己，否则客户端将无法连接到它。我们可以查询 EpMapper 服务，找出特定 RPC 接口正在监听的端点。这是一种相当简单的方法，因为它涉及使用现成的 WINAPI 调用，即 RpcMgmtEpEltInqBegin() 用于开始检查 EpMapper 中的端点列表，以及 RpcMgmtEpEltInqNext() 用于获取列表中的下一个元素。

我们可以自己编写工具，但其他人已经为我们完成了这项工作。以下是我推荐的三个工具：

* PortQry — 由微软工程师开发；

```
PortQry.exe -n <HostName> -e 135
```

![epmapper 探索](https://mmbiz.qpic.cn/mmbiz_png/h4gtbB74nShELc2WW2Lnr2Hfvyp5cAPLp3f1qZFRFbhcGFOBy7kjBwOy6LPLWcSHp6dUIQ0ibMev0HvuysfOsmia1d9sJbuIibApnuQNRGialKk/640?wx_fmt=png&from=appmsg)

epmapper 探索

* RPCDump — 通过 C++ 进行转储；
* rpcdump.py — 通过 Python 进行转储。

请注意，这只能获取使用 EpMapper 的 RPC 服务器的信息。如果 RPC 服务器不使用动态端点，EpMapper 中将没有关于它的信息。

### 查找和探索 IDL 文件

正如我所说，IDL 文件是 RPC 服务器的一种文档。IDL 文件描述了 RPC 服务器提供的方法，包含了接收的参数和返回值的信息。你可以很容易地在网上找到 IDL 文件。例如，使用以下 Github 搜索。

![IDL 文件搜索](https://mmbiz.qpic.cn/sz_mmbiz_png/h4gtbB74nSia6kuRghqPTJlKc6WzPnnK3WjEvicUGbdMticGKmRMH9rTTO1QgbAedvAVkHEarojx5RUj26ia5qKp0EWM1pwibMc9omxd4cKDPvZQ/640?wx_fmt=png&from=appmsg)

IDL 文件搜索

特定 RPC 接口的 IDL 文件通常也由 Windows 开发人员自己分发。因此，一旦确定了你想要研究的 RPC 协议，可以尝试搜索其 IDL 文件。我还想向你推荐 idl\_scraper 工具，它可以批量分析大量 IDL 文件，将所有信息生成 CSV 文件：RPC 接口名称、UUID 值、可用方法名称和接受的参数。这对于模糊测试（Fuzzing）非常有用。

![idl\_scraper 输出示例](https://mmbiz.qpic.cn/mmbiz_png/h4gtbB74nSiaD8XhXOP9MJZFwVkvLz4dd3Nyukoicp64xk4oMiabsnV1ibx5Xf0vv8xnbXKRXiaMMWqiaJNkmcTfwPotUGkLzeL8e2CVz99lWSelg/640?wx_fmt=png&from=appmsg)

idl\_scraper 输出示例

### 更多方法

如果你关注 ETW 事件、WireShark 流量和 ProcMon 日志，就可以调查和检测 RPC 服务器的异常行为。例如，有一些工具如 RpcInvestigator、rpc\_visibility 和 RPCMon 可以帮助使用 ETW 来调查 RPC。

### 通用工具

我们已经学习了在系统上查找和调查 RPC 的基本方法。如你所见，一切都相当简单。因此，有很多不同的工具可以使 RPC 研究更加容易。让我们从提供良好 GUI 界面并能给出系统上 RPC 服务器相当完整概览的工具开始。

* RPCView — 通过 *GlobalRpcServer*分析工作，支持 RPC 接口的反编译，可以解析特殊的 RPC 注册标志（Registration Flags），这些标志可能会影响客户端连接时 RPC 服务器的行为。这些标志非常重要，我们稍后会详细讨论。例如，有一个标志 \_RPC\_IF\_ALLOW\_LOCAL\_ONLY\_，它会导致远程客户端无法连接到 RPC 服务器，只允许本地连接。

![RPCView](https://mmbiz.qpic.cn/sz_mmbiz_png/h4gtbB74nSjNVicdB63cYFPtxdYXheKrY2MiavTS8RlhicJPZIgXUd5abOBlmAy5g8UcxP0ulV5R83PpnrB94zXP5omVa07qKlK0Y1adz50T1g/640?wx_fmt=png&from=appmsg)

RPCView

* rpv + rpv-web — 拥有美观的图形界面，分别显示 RPC 和 DCOM 服务器，显示 RPC 方法的 OpNum（操作编号。每个 RPC 方法都有自己的 Opnum，可以通过 Opnum 而不是名称来调用该方法）以及附加符号文件后的方法名称。

![rpv 图形界面](https://mmbiz.qpic.cn/mmbiz_png/h4gtbB74nSiav0z81LGpw48I8KgGCfgbQyWxd2PEIShqFAXVK59M9rRcCCtVM8J1ZIUrW7hegB20HSgYW8nJuvOkUgREGaW1iaj38LdXichIIM/640?wx_fmt=png&from=appmsg)

rpv 图形界面

* RpcInvestigator — 我认为这是最方便的工具之一。它支持动态创建连接到各种 RPC 服务器的客户端，还有一个消费者（Consumer）用于提取和分析与 RPC 相关的 ETW 事件。

![RpcInvestigator 图形界面](https://mmbiz.qpic.cn/mmbiz_png/h4gtbB74nShmOib2aRut5M6sM9eJdIZPemDvOq9mfkOcgdm4ZWlJJXvl1hudOu4yvLgs9M0pSOJ4B4ibQUYDXEvCQwBibR124jMzZibEekfGKa8/640?wx_fmt=png&from=appmsg)

RpcInvestigator 图形界面

* RpcEnum — 该工具集成了 Hydra 反编译器以及 Neo4j 数据库，可以跟踪特定 RPC 方法调用的函数。

![RpcEnum](https://mmbiz.qpic.cn/sz_mmbiz_png/h4gtbB74nSjU1ThHwbP0HGedqWMmPH7yJIDCUicNyUmUInPfKPlSdREoiaozWs2PKeKrLOCN512hbb1fUI3g2kLSW5Tqk7nYD3k8QXkz4mSUU/640?wx_fmt=png&from=appmsg)

RpcEnum

然而，如果你希望自动化你的研究，可以看看以下这些工具。

* NtObjectManager — 支持许多用于处理 RPC 的 Powershell cmdlet。让我们看看最基本的几个：

```
# Get information about RPC in the PE File
C:\>'C:\Windows\System32\efssvc.dll'|Get-RpcServer

Name       UUID                                 Ver Procs EPs Service Running
---------------------------------
efssvc.dll df1941c5-fe89-4e79-bf10-463657acf44d 1.0530   EFS     False
efssvc.dll 04eeb297-cbf4-466b-8a2a-bfd6a2f10bba 1.070   EFS     False

# Get more information about a specific RPC procedure
C:\>$rpcinterfaces='C:\Windows\System32\efssvc.dll'|Get-RpcServer
C:\>$rpcinterfaces[0].Procedures[0]

Name                     : EfsRpcOpenFileRaw
Params                   : {_hProcHandle, FC_BIND_CONTEXT - NdrContextHandleTypeReference - IsOut, IsSimpleRef, FC_C_WSTRING - NdrConformantStringTypeReference - MustSize, MustFree, IsIn, IsSimpleRef, FC_LONG
- NdrSimpleTypeReference - IsIn, IsBasetype}
ReturnValue              : FC_LONG - NdrSimpleTypeReference - IsOut, IsReturn, IsBasetype
Handle                   : FC_BIND_PRIMITIVE - NdrSimpleTypeReference - IsIn
RpcFlags                 : 0
ProcNum                  : 0
StackSize                : 40
HasAsyncHandle           : False
DispatchFunctio...
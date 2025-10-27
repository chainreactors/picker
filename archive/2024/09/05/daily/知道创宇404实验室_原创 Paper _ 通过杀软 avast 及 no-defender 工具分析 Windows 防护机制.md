---
title: 原创 Paper | 通过杀软 avast 及 no-defender 工具分析 Windows 防护机制
url: https://mp.weixin.qq.com/s?__biz=MzAxNDY2MTQ2OQ==&mid=2650984694&idx=1&sn=7ba5d62b933542ac64cecc692e8fc282&chksm=807992c4b70e1bd2f0588c7c9f865cc4200bce4a37f718e61a4d8c85eaaf9bd84e6498ad191a&scene=58&subscene=0#rd
source: 知道创宇404实验室
date: 2024-09-05
fetch_date: 2025-10-06T18:27:01.026083
---

# 原创 Paper | 通过杀软 avast 及 no-defender 工具分析 Windows 防护机制

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/3k9IT3oQhT12gYOMHmfMeISpj5ibEGHxlLrSuVqUWibTHkoiaIb6alBZrtIfakPXKhHUDuc8LIqoVLHicWHKiaibT4GA/0?wx_fmt=jpeg)

# 原创 Paper | 通过杀软 avast 及 no-defender 工具分析 Windows 防护机制

原创

404实验室

知道创宇404实验室

**作者：******知道创宇404实验室****

**时间：**2024年9月4日****

**1 前言**

参考资料

近几年随着 Windows 越来越重视系统安全，Windows Defender 已经从最开始的杀毒软件发展为如今的端点检测和响应软件(EDR)，并成为 Windows 安全体系的一部分；从系统安全的角度来看，Windows 不建议用户关闭或停用 Defender；从安全研究的角度来看，由于 Defender 提供的默认关闭策略无法完全停止该软件运行，可以说的上是 Windows 「不允许」用户关闭 Defender，这常常就会阻碍和影响对恶意软件的调试分析。

2024年6月，安全研究员 es3n1n 在 Github 分享了开源工具 no-defender，其利用 Windows 安全防护的第三方杀毒软件接管机制，通过逆向分析 Avast 杀毒软件提取出关键组件，编写 hook 代码修改关键组件的执行逻辑，从而实现完全关闭 Defender 软件。

本文将结合 no-defender 源码和 Avast 杀毒软件，研究学习 no-defender 的源码和实现原理。

本文实验环境：

```
Windows10 专业版22H2 19045.2364
Visual Studio 2022
Avast 24.7.9311.0
no-defender master
```

****2 关闭Defender的方案****

参考资料

随着 Defender 软件在 Windows 安全体系中发挥着越来越关键的作用，Windows 系统逐步加码停用 Defender 的难度，导致互联网上大量的关闭 Defender 的方案都存在局限性或直接失效了，我们这里对其进行简单梳理：

1. 关闭实时保护：临时关闭「实时保护」功能，Defender 将自动择机恢复；
2. 添加排除文件夹：在 Defender 中配置排除文件夹，扫描和实时保护将绕过该文件夹；
3. 组策略关闭Defender：在 `组策略-计算机配置-管理模板-Windows组件-Microsoft Defender 防病毒` 选择 `关闭 Microsoft Defender防病毒-已启动`，目前已无效；
4. 注册表关闭Defender：在 `注册表-HKEY_LOCAL_MACHINE-SOFTWARE-Policies-Microsoft-Windows Defender` 项添加名为 `DWORD DisableAntiSpyware=1`，目前已无效；
5. 服务停止Defender：在 `Services` 中配置 Defender 进程为 `禁用`，目前已无效；
6. 安全模式下损坏Defender二进制：在 Defender 关闭防篡改后进入安全模式，修改 Defender 的二进制程序(如`C:\ProgramData\Microsoft\Windows Defender\platform\4.18.2211.5-0\MsMpEng.exe`)的所有者，并重命名为 `MsMpEng.exe.bak`，可永久关闭 Defender；
7. 第三方杀毒软件接管：安装第三方杀毒软件后，Defender 将自动退出。

> 有些方案能够关闭 Defender，但随后会由 Windows Security Center 自动启动 Defender 进程，这种仍视为无效；
> 由于操作系统版本、Dedenfer版本均会影响其内部的策略，各方案的适用情况难以确定，本文以 `Windows10 专业版22H2 19045.2364` 测试为准。

Windows Defender 正常工作示意图：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT12gYOMHmfMeISpj5ibEGHxlviakXqdqFAT4vy1YibdR3Kz8TGkDWVsm8OXj7VodcxQ589zoKqRUbM0Q/640?wx_fmt=png&from=appmsg)

使用「安全模式下损坏Defender二进制」的方案可以永久关闭 Defender，但这种方案具有一定的侵入性和破坏性，而使用「第三方杀毒软件接管」的方案则需要进一步确认该杀毒软件是否提供了完全关闭的功能。

实际上早在 2016 年就有安全研究者分享开源软件 YourAV 工具，该工具通过模仿杀毒软件行为，在安全中心注册了一个杀毒软件，随后 Defender 就会自动退出，达到了关闭 Defender 的目的；但由于近年 Windows 安全体系的层层加码，目前杀毒软件必须经由微软继续签名认证，同时还需使用未公开的 API 和安全中心进行消息同步，导致 YourAV 这种方案也失效了。

****3 no-defender概要****

参考资料

no-defender 工具可以说是 YourAV 工具的一个接力，既然目前需要微软签名和未公开的 API，那就直接从第三方杀毒软件(Avast)中逆向分析并提取出来，通过 hook 修改杀毒软件的运行逻辑，调用在安全中心(Windows Security Center)注册杀毒软件的逻辑，同样 Defender 就会自动关闭退出。

no-defender 工具提供的程序如下：

```
win_x64
├── no-defender-loader.exe  // no-defender服务配置工具
├── no-defender-loader.pdb
├── powrprof.dll            // no-defender的hook实现
├── powrprof.pdb
├── wsc.dll                 // avast的wsc通信核心组件
└── wsc_proxy.exe           // avast的wsc通信程序
```

按照 README 运行工具如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT12gYOMHmfMeISpj5ibEGHxlBJj6C5cSmBeCLqicF4VgWfnnHoKbZogwHkWPiaE7kicJoD7Y7ibVkThSWA/640?wx_fmt=png&from=appmsg)

在安全中心中可以看到 no-defender 已经注册成功，Defender 自动退出如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT12gYOMHmfMeISpj5ibEGHxlNgP25leVxS2bicpARoJtgFoQVhV6Qlu4Jwr6xibo7W8gnX8fCt1xOyPA/640?wx_fmt=png&from=appmsg)

由于 no-defender 在一定程度上影响了 Windows 的安全策略，Github 官方于 2024.06.08 对 no-defender 仓库发出 DMCA 下架政策，删除了仓库所有数据内容，如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT12gYOMHmfMeISpj5ibEGHxllSga4FxsgDkQIibC2nTHSbkRbMiaxQLh3B430iay30YumPKYa28JGuQvA/640?wx_fmt=png&from=appmsg)

通过 no-defender 工具的源码我们可以清晰的理解其执行流程，但要进一步理解其原理则需要从 Avast 逆向分析开始说起。

****4 Avast的wsc机制****

参考资料

Avast是位于捷克布拉格的 AVAST Software a.s. 公司于1988年首次发行的杀毒软件，软件名取自「Anti-Vzzirus-Advanced-Set」，即「高级杀毒软件」；其提供家用用途的免费版本以及企业和专业用户的付费版本，被全球用户广泛使用。

在 Avast 官网下载程序并安装，如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT12gYOMHmfMeISpj5ibEGHxl8XTU9TbZqDibBRvOYn9Bu9x35wm2T07ZFDgVXILWmJqJQL7uzL7Wicrg/640?wx_fmt=png&from=appmsg)

安装完毕后可以在安全中心中看到 Avast 已经接管了杀毒软件功能，Defender 自动退出，如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT12gYOMHmfMeISpj5ibEGHxlandKja1Jw6EDCib0TnAibpdww0dJE6x2sZl9YKcfHBfDicHs5wW22Qwww/640?wx_fmt=png&from=appmsg)

Windows操作系统和安全防护软件之间的协同工作，得益于安全中心(Security Center)服务，如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT12gYOMHmfMeISpj5ibEGHxl0mRn1vPuBqmbf6FVptqHKfUqgTRMTue6lmeDevlfN4Isj6Uhcd9EjA/640?wx_fmt=png&from=appmsg)

安全防护软件通过 `wscsvc` 服务提供的 API 向 Windows 系统通知、报告自身的运行状态，随后由 Windows 系统调整安全策略，以保证持续的安全防护功能；`wscsvc` 服务除了能够注册防病毒软件，还可以注册防火墙、防间谍等软件。

在 Avast 的软件实现中，将与 `wscsvc` 服务通信的部分封装为一个单独的服务 `AvastWscReporter`，如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT12gYOMHmfMeISpj5ibEGHxlvXjK70v1zzzg36R12yGfZTsU6OhjNxjO48VpaA0W7abAO8cKnktVnA/640?wx_fmt=png&from=appmsg)

那么我们可以整理出 Avast 和 Windows 安全中心的通信关系如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT12gYOMHmfMeISpj5ibEGHxlYicYP1HkTOIhnqJGVj3aDy0X5JI6HMmemdHA1jekqqG98r9QnkOVQnQ/640?wx_fmt=png&from=appmsg)

根据服务路径找到其关键文件 `wsc_proxy.exe` 和 `wsc.dll` 如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT12gYOMHmfMeISpj5ibEGHxlyjOZH4jBzKiaHhoLOYATjZ8Hht5ibOFUl6RYJYemibZZA4ZhKXMzMfXqQ/640?wx_fmt=png&from=appmsg)

也就是说如果我们可以复用 `wsc_proxy.exe` 和 `wsc.dll` 程序，那么就可以向 Windows 安全中心注册任意的杀毒软件软件，从而关闭 Defender 软件。

****5 wsc.dll****

参考资料

首先分析 `wsc_proxy.exe` 程序，其逻辑非常简单，主函数中只有加载 `wsc.dll` 文件并调用 `run()` 函数的逻辑，如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT12gYOMHmfMeISpj5ibEGHxl4VNY0Yre0piaYg2osWzSC4qfcbxA85Da3H7xlskYUJvNCVUCRjfx82g/640?wx_fmt=png&from=appmsg)

随后跟入 `wsc.dll` 程序，在该动态链接库的 `dllmain()` 函数中仅完成一些初始化的工作，其导出函数如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT12gYOMHmfMeISpj5ibEGHxlibay5RCbhhQzvrhUsxomIpnWMdoEb1xicoibibSHicDgNQ8y2UDkvFxEPTA/640?wx_fmt=png&from=appmsg)

而核心逻辑主要在 `run()` 函数下，跟入函数 `run() => sub_18004A2E0() => sub_180048000()/service_proc()`，可以看到 `wsc.dll` 首先对一些文件对象(如：`\\wsc.log` 和 `WscReporter` 等)进行初始化，如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT12gYOMHmfMeISpj5ibEGHxlxqM6nlbVB0Eibiccgafn3UsCo219shyLkia0GGt79k1mXskTZ1037KKYg/640?wx_fmt=png&from=appmsg)

随后在 `sub_180194020()` 函数对 `ASW*` 文件对象进行初始化，若文件打开失败则返回错误 `sd is not loaded` 并退出，如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT12gYOMHmfMeISpj5ibEGHxlG2icicvFb6oQqPeKLJmib5mJDa0WnboUpagibInP3yTPMgKHiahrzTjNAHg/640?wx_fmt=png&from=appmsg)

在一切准备就绪后，调用 `StartServiceCtrlDispatcherW` 系统启动服务，绑定的服务主函数为 `sub_180047800()/service_proc()`，如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT12gYOMHmfMeISpj5ibEGHxlssLNxC4f5Tj5Ip2iaxbrWbbxm5ocRr9lHyvyeolmicKtI9DOCFiaDmU0g/640?wx_fmt=png&from=appmsg)

跟入服务主函数 `sub_180047800()/service_proc()` 中，其主要逻辑为首先使用 `CreateThread()` 系统调用启动了 `sub_18002CB20()` 线程，随后使用 `RpCServerRegisterIfEx` 系统调用注册启动了 RPC 服务器，如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT12gYOMHmfMeISpj5ibEGHxlI25uks8Gibq4RDQ29xwnsOntvjibdVCic0hZxpJEn16EO1JE3HURf2REA/640?wx_fmt=png&from=appmsg)

首先我们来分析 RPC 服务器，根据 `_RPC_SERVER_INTERFACE_T` 定义逆向分析 `unk_1802BE3C0` 结构体，可找到 RPC 处理函数 `sub_18002A590()`：

```
typedef struct _RPC_SERVER_INTERFACE_T {
    UINT                     Length;
    RPC_IF_ID                InterfaceId;
    RPC_IF_ID                TransferSyntax;
    (RPC_DISPATCH_TABLE*)    DispatchTable;
    UINT                     RpcProtseqEndpointCount;
    PRPC_PROTSEQ_ENDPOINT_T  RpcProtseqEndpoint;
    RPC_MGR_EPV PTR_T        DefaultManagerEpv;
    (MIDL_SERVER_INFO*)      InterpreterInfo;
    UINT                     Flags ;
} RPC_SERVER_INTERFACE_T, PTR_T PRPC_SERVER_INTERFACE_T;
```

当接收到 RPC 请求后将调用该函数 `sub_18002A590()/s_wscrpc_update()`，该函数读取请求字符串并将其转换为二进制格式，随后通过 `sub_18002B0D0()` 存入 `qword_1803E3098` 队列中，然后设置 `hHandle` 多线程信号量如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT12gYOMHmfMeISpj5ibEGHxl2xWpOicYB04bMITjjctHyLTw7YxfCrjLszcdhzWu2ScmNAmJHrvayJw/640?wx_fmt=png&from=appmsg)

而 `sub_18002CB20()` 线程则用于实际处理队列中的任务，跟入到 `sub_18002CB20() => sub_18002A090()/queue_worker()` 线程内部，`while(1)` 循环中首先等待 `hHandle` 多线程信号量，当接收到信号量后从 `qword_1803E3098` 队列中获取任务，如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT12gYOMHmfMeISpj5ibEGHxlfSHfIiatcfQT3eGqYq1tyicDQQicpfRdgW0Sq0xxJHqA2jx4aOCS8ibFIA/640?wx_fmt=png&from=appmsg)

获取到任务后，调用 `sub_180029FB0()/process_item()` 处理该任务，其...
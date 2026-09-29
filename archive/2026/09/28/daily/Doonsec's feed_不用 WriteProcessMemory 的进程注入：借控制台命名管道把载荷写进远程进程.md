---
title: 不用 WriteProcessMemory 的进程注入：借控制台命名管道把载荷写进远程进程
url: https://mp.weixin.qq.com/s/5QW-qf3C0YcT9sutgZW4JQ
source: Doonsec's feed
date: 2026-09-28
fetch_date: 2026-09-29T07:38:43.056931
---

# 不用 WriteProcessMemory 的进程注入：借控制台命名管道把载荷写进远程进程

# 不用 WriteProcessMemory 的进程注入：借控制台命名管道把载荷写进远程进程

TwoSevenOneT
TwoSevenOneT

赛博生存指南

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

> 原文：https://www.zerosalarium.com/2026/09/edr-evasion-process-injection-without-WriteProcessMemory.html
> 作者：Two Seven One Three（@TwoSevenOneT）
> 发布时间：2026-09-26
> 翻译模型：GLM-5.3

编者按：zerosalarium（@TwoSevenOneT）的新作，本仓库第二次译介这位作者，上一篇是 2026-06 的《EDRChoker：通过限速遥测流量绕过防御》。远程进程注入的标配四件套是 OpenProcess → VirtualAllocEx → WriteProcessMemory → CreateRemoteThread，中间两步是 EDR 用户态 hook 与内核回调盯得最紧的地方。本文的替代思路：把载荷写进一个交互式控制台子进程（`netsh.exe` / `nslookup.exe`）的 hStdInput。那本来就是一根命名管道，父进程对它调 `WriteFile` 再正常不过，写进去的数据会原样落进子进程内存。之后用 `VirtualProtectEx` 补上执行权限、劫持线程改 RIP，整条链路一次都不碰 `VirtualAllocEx` 和 `WriteProcessMemory`。载荷只需避开三个坏字符，也不需要以挂起状态创建子进程。作者同步开源了 PoC 仓库 InjectSetConsole，文末「译者补充」逐段过了这份源码——哪里写得讲究、哪里是概念验证的通病，一并说清。

## I. 引子

在针对目标的红队项目或渗透测试中，你大概率会用到远程进程注入来执行载荷。正因为这套手法出现得太频繁，EDR（Endpoint Detection and Response）对相关 API 盯得非常紧。

本文介绍一种向远程进程注入代码的新做法，全程不依赖大名鼎鼎的 `WriteProcessMemory` 和 `VirtualAllocEx`。

在我跟一堆 EDR 许可证搏斗的那段时间，我发现 SensePost 的两位实力派研究员 Max Hirschberger 和 Ogulcan Ugur 已经独立想到了类似的点子并发了文章；顺着他们的工作，我又找到了 modexp 探索过一条相近路线的研究。说实话，这几位做得都比我好。

不过，我对两点始终不满意：一是必须在初始化阶段把进程挂起，二是 `lpCommandLine` 和 `lpEnvironment` 得改成奇奇怪怪的格式。于是我放下这些路线，转而研究出一套新的注入技术，也就是下面要讲的这套。

欢迎在 X 上找我，看我最近在琢磨的渗透测试与红队技巧：Two Seven One Three (@TwoSevenOneT)[https://x.com/TwoSevenOneT]

## II. 主体

### 1. 远程进程注入技术概览

进程注入是一种重要的规避与持久化技术：攻击者强迫一个合法、受信的 Windows 进程替自己运行任意代码。

在经典的远程线程注入或 PE 注入流程里，注入方进程要先通过 `OpenProcess` 拿到目标应用（比如 `explorer.exe` 或 `svchost.exe`）的句柄，再用 `VirtualAllocEx` 在目标的虚拟地址空间里划一块专属缓冲区。

内存备好后，攻击者调用 `WriteProcessMemory` 把恶意载荷拷进远程进程的内存空间。

接着用 `CreateRemoteThread` 或其他办法创建一个线程，让它的 RIP 指向刚写入 shellcode 的那块内存。这种跨进程动作天然绕过常规边界防御，还继承了宿主进程的访问权限，所以 EDR 解决方案会通过用户态 hook 和内核回调对 `WriteProcessMemory` 严加监视和审查。各家 EDR 平台都把跨进程内存修改视为高严重级遥测事件，逼得现代威胁行为者不断寻找能绕开传统内存操作签名的替代方案。

大多数远程注入技术都遵循这个通用公式：

```
[OpenProcess/CreateProcess] + [VirtualAllocEx] + [WriteProcessMemory] + [某种把线程 RIP 重定向到新写入 shellcode 的方法]
```

### 2. 用 Windows 命名管道向远程进程写任意载荷

打开一个交互式控制台程序，它带一个名为 `conhost.exe` 的子进程；你在里面敲命令时，这些命令的内容存在哪儿？

答案：存在这个程序的内存里。

为了演示，我写一个小程序：用 `CreateProcess` 创建子进程，然后往子进程的 hStdInput 写数据。

我拿控制台程序 `nslookup.exe` 举例：

![代码：创建子进程并向其控制台写入数据](https://mmbiz.qpic.cn/sz_mmbiz_png/JpU6JH8dicqVHHv6J19libpEvvHh5seBibftaGfUJfmv19qcjC90pgXlYaG8xTeGo1iavyNmjhqGRZ4yxPCXbbyC6GvmmE8GO5Xzp16P7BopKSY/640?wx_fmt=png&from=appmsg)

当我对子进程的 hStdInput 调用 `WriteFile` 时，被写入的数据就存进了子进程的内存。

![Process Hacker 显示：写入 hStdInput 的数据位于子进程内存](https://mmbiz.qpic.cn/sz_mmbiz_png/JpU6JH8dicqVVbsM4IGXUJQ52BCbVSvFZGSXYUZc1H4oBTrPX16WkUGuJ5S8VXfjHMEKwwKSPIA1oF5nJNY73ULvicEWVPpmP6RoZx3W2Dr1c/640?wx_fmt=png&from=appmsg)

那么思路就来了：用 hStdInput 这根命名管道把载荷写进另一个进程，而不是对子进程调 `WriteProcessMemory`。

但有个问题：Windows 控制台界面只能显示有限的可读字符，而写命名管道本质上就是调 `WriteFile`。理论上，我们应该能往 hStdInput 写入控制台显示不了的字节。实践检验一下，我有下面这个二进制数组：

![待写入子进程的原始载荷二进制数组](https://mmbiz.qpic.cn/mmbiz_png/JpU6JH8dicqUwLNRkvgQTuTLvWgLSppDgUNd1icTko7p1xTMxVcqzliacv4ZHFlhhUIksgicgz4312dfLibgj5YYunwJoYPuaL82m23wUibPbePC8/640?wx_fmt=png&from=appmsg)

写入命名管道之后：

![原始载荷成功写入子进程内存，全程未用 WriteProcessMemory](https://mmbiz.qpic.cn/sz_mmbiz_png/JpU6JH8dicqVk3TrnKH6TpCicLKnXfZ961xu4QLKnnzsbTh24ZDceibGqRUovM0DjhRLrZQJtnYYGaV5m2sT4ATvuG9EGzAMVdp90W9XaLbLVE/640?wx_fmt=png&from=appmsg)

这证明：几乎任何我们想要的文件，都能写进一个控制台进程的内存里。

### 3. 经控制台命名管道的远程进程注入

基于上述信息，要不用 `VirtualAllocEx` 和 `WriteProcessMemory` 把载荷注入远程进程，主要步骤如下：

* 选一个交互式控制台程序。我找到两个合适的：`netsh.exe` 和 `nslookup.exe`。
* 调用 `CreateProcess`，拿到子进程 hStdInput 的句柄。
* 对 hStdInput 调 `WriteFile`，把载荷写进子进程。
* 在子进程内存里定位新写入的载荷。
* 用 `VirtualProtectEx` 给定位到的内存区域加上执行权限。
* 劫持一个线程，把它的 RIP 重定向到上述地址。

用 `WriteFile` 写 hStdInput 时，载荷必须避开几个在 Windows 控制台里有特殊含义的坏字符：

* 0x0D：回车符（CR），ASCII 与 Unicode 里的控制字符。
* 0x0A：换行符（LF），控制字符。
* 0x1A：SUB（替换字符），按 Ctrl+Z 产生，历史上用作 EOF（End-of-File）标记。

生成载荷时必须避开这些字符，否则子进程会把载荷当成命令、按普通命令去执行，结果是「Command not found」之类的输出，原始载荷也就不再留在进程内存里了。

要在子进程内存里定位新写入的载荷，我在载荷开头放一段特征字符序列，称之为 marker（标记）。搜索这个 marker，就能确定载荷的位置。重定向 RIP 时，要在 marker 所在地址上加 marker 的大小：

```
RIP = marker_addr + sizeof(marker)
```

我写了一个 PoC，完整跑通上述六步，完成 shellcode 的远程注入与执行，效果如下：

![InjectSetConsole 运行成功](https://mmbiz.qpic.cn/mmbiz_png/JpU6JH8dicqWy0wMckUd2GfvgFPOiaY2jwYiavXv3clxsWG0yQficfaHHsOZpCsFCIQcoWLFZpgZmdHllCLJraibbbgTtaFRQHSox6ofd7gsibOS4/640?wx_fmt=png&from=appmsg)

![InjectSetConsole 运行成功后的进程树](https://mmbiz.qpic.cn/sz_mmbiz_png/JpU6JH8dicqV38rAKTeqbESicf5FghmUbq40EEPkGia5Q2pVKSFmvzdjb6gVLiaicKxiaiaYGwStctHPTGHQNcpsTbvkbjs4ZC7wyQicb6WZicb6EEb0/640?wx_fmt=png&from=appmsg)

此前已有研究者拿这套技术实测过多款 EDR，所以这里不再放我自己的测试结果。

演示视频：https://youtu.be/DCUnbj\_usPM

### 4. 防御

这套控制台命名管道注入技术彻底甩开了 `VirtualAllocEx` 和 `WriteProcessMemory`，因此监控重心应放在：对远程进程使用 `VirtualProtectEx` 的行为，以及命名管道上的读写操作。

## III. 结语

红队项目或渗透测试里用到的多数远程注入技术都依赖 `VirtualAllocEx` + `WriteProcessMemory` 这对 API 组合，EDR 对它们的监视自然非常严密。

与传统路线不同，控制台命名管道注入不用 `VirtualAllocEx` 和 `WriteProcessMemory`，而是利用命名管道上的读写操作，以及控制台程序把交互命令存进内存的方式。除此之外，这套技术还有几个额外优点：

* 不需要 `CreateProcess` 以挂起状态启动进程。
* 不会让子进程的 `lpCommandLine` 或 `lpEnvironment` 出现异常格式。

载荷或 shellcode 能用的字符几乎不受限制，需要避开的坏字符很少。

因此，传统的监控手段无法可靠地检测和阻止这套技术。防御方应该把注意力放在控制台程序存放命令的那块内存区域上，监控 `VirtualProtectEx` 的使用，并跟踪命名管道上的读写操作。

本文作者：Two Seven One Three

## 参考资源

* 原文（Zero Salarium 博客）：https://www.zerosalarium.com/2026/09/edr-evasion-process-injection-without-WriteProcessMemory.html
* PoC 源码仓库（InjectSetConsole）：https://github.com/TwoSevenOneT/InjectSetConsole
* PoC 演示视频：https://youtu.be/DCUnbj\_usPM
* 作者 X 主页：https://x.com/TwoSevenOneT

## 译者解读

这篇文章的巧妙之处，在于把「写远程内存」这个高危动作换了一件完全合法的外衣。控制台子进程的 hStdInput 本质是一根命名管道，父进程往子进程的标准输入里写数据，是操作系统设计里最天经地义的行为之一，shell 和无数父进程每秒都在做。EDR 可以给 `WriteProcessMemory` 挂 hook、给跨进程内存写挂内核回调，却很难对「父进程写子进程 stdin」这种动作做什么文章，因为误报面大到不可用。

这套思路也不是孤例。本仓库之前译介过 Module Stomping——把 shellcode 踩进 file-backed DLL 的 `.text` 段，《DEF CON 34 从加载器到内核》工坊篇里三款 EDR 对其集体沉默。命名管道注入与它是一个哲学：不对抗检测，让写入动作本身获得合法语义。一个藏在合法模块的代码段里，一个借道子进程的 console 输入缓冲。检测方要回答的问题从「谁写了远程内存」变成「这次写是否合法」，后者在用户态几乎没法回答。

链路后半段并没有消失，只是换了地方。`VirtualProtectEx` 对远程进程加可执行权限仍是必经步骤，Elastic 的 `suspicious_memory_protection_change` 一类规则、调用栈检测（本仓库 DEF CON 34 篇有展开）直接适用，这也是原文 Defense 小节点名的重点。管道读写的监控没有现成的公开 ETW provider，现实落点是 Sysmon 的管道事件（Event 17/18）与对象句柄审计——配套 PoC 用的是 `CreatePipe` 匿名管道（底层实现就是随机命名的管道实例），监控语义与显式命名的管道不完全一样，这点在文末的源码评估里有展开。载荷本身则躺在 console 输入缓冲区里，一块本不该有可执行内容、内容也不是合法命令历史的区域，Moneta 这类属性驱动的内存扫描器（见本仓库《Moneta 内存隐蔽与误报》篇）原则上能把它捞出来。

只避开 0x0D / 0x0A / 0x1A 三个字节，对现代 shellcode 几乎不构成负担。位置无关的 shellcode 里这三个字节本来就少见，真碰上用编码器过一遍就行。对比走 ROP 链或自定义协议解析时的字符约束，这差不多是白送的条件。

和前作比一下：SensePost 与 modexp 的同类思路研究，要么要在初始化时挂起进程，要么让 `lpCommandLine` / `lpEnvironment` 变形。挂起创建的进程、异常的命令行格式，都是 Sysmon EID 1 的现成狩猎字段。本文用「正常创建 + 写 stdin」绕开了这两个副作用，OPSEC 上确实更干净。

至于这套技术对 2026 年的商业 EDR 还剩多少实效，原文没有给出自己的测试数据（作者只说前人测过），要验证只能自己动手复现。

## 译者补充：PoC 源码评估

作者同步开源了 PoC 仓库 InjectSetConsole（C++，约 330 行有效代码）。上面解读里说的检测面，这份源码里能看到具体长什么样，逐段过一遍。

先核实对应关系。README 链回本文和同一个演示视频；`rawData` 数组开头 25 字节是 `0x61×3, 0x62×3, 0x63×3, 0x64×3, 0x65×3, 0x66×4, 0x67×3, 0x6A×3`，长度 25 = 0x19，与 README「替换 shellcode 从偏移 0x19 开始」、代码里劫持 RIP 的 `(*result) + 0x19` 三方吻合。载荷数组开头的注释把作者意图写得很直白：

```
//msfvenom -p windows/x64/exec CMD="notepad.exe" -e x64/zutto_dekiru -b '\x0a\x0d\x1a' -f hex
// bad chars are 0x0a, 0x0d, 0x1a
//Execute code at offset 0x19
//Need marker to search from remote memory
unsignedchar rawData[368] = {
0x61, 0x61, 0x61, 0x62, 0x62, 0x62, 0x63, 0x63, 0x63, 0x64, 0x64, 0x64,
0x65, 0x65, 0x65, 0x66, 0x66, 0x66, 0x66, 0x67, 0x67, 0x67, 0x6A, 0x6A,
0x6A, 0x48, 0xB8, 0x30, 0xAC, 0x10, 0x28, 0x03, 0xD6, 0x03, 0x02, 0xDB,
    ... // shellcode from offset 0x19
};
```

仓库分三个文件：`InjectSetConsole.cpp` 是主流程（管道创建、`CreateProcess`、写载荷、找 marker、改保护、劫持线程，六步在 `main()` 里顺序排开）；`PipeExchange.h` 是管道读写辅助，`ReadFromPipe` 用 `PeekNamedPipe` 先探可用字节再 `ReadFile`，非阻塞；`InjectHelp.h` 装着三个核心函数——远程特征扫描、主线程定位、RIP 改写。管道部分是 MSDN 标准重定向模式：`CreatePipe` 两根管道，`SetHandleInformation` 关掉父进程侧两端的继承标志，`STARTUPINFO` 挂 `STARTF_USESTDHANDLES`，`CreateProcess` 以 `CREATE_NEW_CONSOLE` + `bInheritHandles = TRUE` 拉起子进程。

### 写得讲究的三处

`FindPatternInRemoteProcess` 的扫描过滤规矩：从 `lpMinimumApplicationAddress` 扫到 `lpMaximumAppli...
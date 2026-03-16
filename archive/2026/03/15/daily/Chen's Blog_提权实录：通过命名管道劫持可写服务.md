---
title: 提权实录：通过命名管道劫持可写服务
url: https://gh0st.cn/archives/2026-03-16/1
source: Chen's Blog
date: 2026-03-15
fetch_date: 2026-03-16T04:33:25.428688
---

# 提权实录：通过命名管道劫持可写服务

[![Author Avatar](/assets/avatar.jpg)](/)

# EvilChen

 [About Me](/about) | [My Friends](/friends)

# 提权实录：通过命名管道劫持可写服务

March 16, 2026

# 提权实录：通过命名管道劫持可写服务

## 前言

本文在分析某 Windows 应用的服务组件时，发现其创建的命名管道访问控制配置宽松，允许低权限用户连接并发送指令，从而触发高权限的终止任意进程操作（`taskkill`）。进一步分析发现，被终止的服务会自动重启，而其可执行文件的权限配置错误，允许 Everyone 组读写。结合这两个缺陷，可构造一条完整的本地提权利用链。

## 漏洞挖掘过程

### 命名管道

#### 关于命名管道

命名管道（Named Pipe）是 Windows 操作系统提供的一种进程间通信（IPC）机制，允许不同进程（包括跨会话、跨权限级别）通过一个带名称的管道进行双向或单向数据交换。命名管道具有全局可见的名称（通常位于 `\pipe\` 命名空间下，如 `\\.\pipe\KeyServicePipe`），支持多客户端连接，并可通过安全描述符（Security Descriptor） 设置访问控制列表（ACL），以限制哪些用户或组可以读取、写入或创建连接。

命名管道常被用作高权限服务与低权限客户端之间的通信通道。然而，若开发者未正确配置管道的 ACL（例如允许 Everyone 或 Authenticated Users 具有写权限），攻击者就可以作为客户端向服务端发送消息，从而使得服务执行敏感操作（如启动/终止进程、读取文件等），以此构成权限提升或远程代码执行的风险。

#### 发现命名管道

发现命名管道及查看其对应的 ACL 策略可以借助 [Sysinternals Suite](https://learn.microsoft.com/en-us/sysinternals/downloads/sysinternals-suite) 内的 `pipelist` 和 `accesschk`。这里[0cat](https://github.com/0cat-r)向我推荐了一款可视化友好的工具：[Pipetap](https://github.com/sensepost/pipetap)。通过查看 `Pipelist` 发现存在一个 ACL 策略为 Everyone 可写的命名管道：`KeyServicePipe`。

![CleanShot 2026-01-04 at 16.11.27@2x](/images/2026-03-16/CleanShot%202026-01-04%20at%2016.11.27@2x.png)

该命名管道对应的进程也是以 `System` 权限运行着，完全符合我们挖掘提权的条件。

![CleanShot 2026-01-12 at 19.44.25@2x](/images/2026-03-16/CleanShot%202026-01-12%20at%2019.44.25@2x.png)

#### 进程终止逻辑

根据命名管道服务进程定位到其可执行文件，接着通过 IDA 进行[一键导出反编译代码](https://github.com/gh0stkey/FuncExporter)。配合着 AI 进行分析，很容易就定位到相关信息。

首先是入口接收到信息并根据不同的偏移量解析客户端所发送过来的消息，根据这些偏移量得知消息包含 2 个部分：消息头和消息体，消息头为 12 个字节。

![CleanShot 2026-01-12 at 16.20.29@2x](/images/2026-03-16/CleanShot%202026-01-12%20at%2016.20.29@2x.png)

其次是消息头的逻辑，我们可以看见其有三个部分，每个部分刚好 4 字节（DWORD）。三个部分分别为：会话 ID、消息类型、消息体长度。这些信息也是基于后续的调试输出所得知。读到消息类型后，会判断消息类型的范围必须在 1-37 之间。

![CleanShot 2026-01-12 at 16.23.31@2x](/images/2026-03-16/CleanShot%202026-01-12%20at%2016.23.31@2x.png)

最后就进入消息分发，根据不同的消息类型进行分发。不同的消息类型对应不同的处理逻辑，在这里实际上踩了个坑，正常跟进向下的逻辑 Map 寻找，而实际上在服务创建的构造函数内就已经定义好了：`sub_424FF0(v5, 消息类型, 消息处理函数)`。

![CleanShot 2026-01-12 at 17.01.45@2x](/images/2026-03-16/CleanShot%202026-01-12%20at%2017.01.45@2x.png)

关键问题逻辑就是其作为命名管道服务端有一个消息接收分发机制，根据消息类型来进行消息的分发。如图所示，当消息类型为 `24` 时则进入消息进入 `sub_4216B0` 函数处理。

在 `sub_4216B0` 函数内本质上就是获取消息体进行处理，最重要的就行消息体的 `+4` 字节偏移位，其为 PID（这里做了强转换，因此无法进行命令注入）。PID 首先用于 `TASKLIST` 命令进行命令查找。

![CleanShot 2026-01-12 at 19.25.22@2x](/images/2026-03-16/CleanShot%202026-01-12%20at%2019.25.22@2x.png)

只有当指定的 PID 进程存在时才会接着向下走，走到 `TASKKILL` 命令，根据 PID 强制关闭进程。至此，我们就发现了一条低权限进程通过命名管道以 `System` 权限进行 `TASKKILL` 任意进程的路径。

![CleanShot 2026-01-12 at 19.39.38@2x](/images/2026-03-16/CleanShot%202026-01-12%20at%2019.39.38@2x.png)

### 系统服务

#### 关于系统服务

Windows 服务（Windows Service）是 Windows 操作系统中一种在后台持续运行的程序，无需用户交互即可执行特定任务。如果服务在配置时没有做好权限的 ACL 配置则会导致三类风险：可修改服务二进制文件、可修改服务注册表项、可修改服务本身，易被攻击者利用实现本地权限提升或恶意篡改服务配置与运行逻辑。

#### 可修改服务二进制文件

这里直接借助 [SharpUp](https://github.com/GhostPack/SharpUp) 来进行一键分析：`SharpUp.exe check ModifiableServiceBinaries`。发现有很多服务的可执行文件是可以修改的，但是要配合攻击链路，就需要满足被 `TASKKILL` 强制终止进程后，还会自动重启的。这里测试出来发现 `KeyAgent` 服务满足这一逻辑。

![CleanShot 2026-01-12 at 19.49.29@2x](/images/2026-03-16/CleanShot%202026-01-12%20at%2019.49.29@2x.png)

## 利用链构建

利用链构建比较简单，先启动独立的线程不断的循环尝试将恶意文件 `EvilAgent.exe` 替换目标服务的合法可执行文件 `KeyAgent.exe`，同时作为客户端连接命名管道 `\\.\pipe\KeyServicePipe` 并发送构造好的 KillProcess 消息触发命名管道服务进程执行 `TASKKILL` 命令终止 `KeyAgent.exe` 进程，最后借助 `KeyAgent.exe` 服务自动重启特性加载恶意文件，完成本地权限提升的利用链构建。

![mermaid-diagram-2026-01-12-203558](/images/2026-03-16/mermaid-diagram-2026-01-12-203558.png)

`EvilAgent.exe` 是 [SystemGap](https://github.com/Rvn0xsy/SystemGap) 项目里的 `SystemGapAll`。其同样也借助命名管道实现高低权限进程间的通信，低权限向高权限发送要执行的命令，高权限执行并把结果返回给低权限。

![4cd75d3600f7dd104be96cb3fd87d56a](/images/2026-03-16/4cd75d3600f7dd104be96cb3fd87d56a.png)

## 总结

本提权利用链的成功构建，关键在于命名管道访问控制配置不当与服务可执行文件权限配置错误这两个缺陷的组合利用，在实战过程中发现这也类似的问题也很多，是个值得关注的攻击面。最后，在此特别感谢 [@倾旋](https://payloads.online/) 在漏洞挖掘过程中提供的协助。

[INDEX](https://gh0st.cn/ "Back to Index")  ·  [>>](https://gh0st.cn/archives/2025-12-26/1 "PREV: 黑盒视角下的 WebView 漏洞面探索")

</> Copyright © Chen's Blog (GH0ST.CN) 2016-2021
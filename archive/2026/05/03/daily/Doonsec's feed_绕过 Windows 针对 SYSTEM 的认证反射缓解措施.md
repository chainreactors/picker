---
title: 绕过 Windows 针对 SYSTEM 的认证反射缓解措施
url: https://mp.weixin.qq.com/s/X8lJPZMzfbwpLno2T0EvUw
source: Doonsec's feed
date: 2026-05-03
fetch_date: 2026-05-04T05:26:34.169089
---

# 绕过 Windows 针对 SYSTEM 的认证反射缓解措施

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/h4gtbB74nSia3nN9bJL4t4PNGKRSibx2kstPnWEyf3GnWaJWKUzaD4jnhviaiaiaocfJkjOrqt6XXS1sLRN8Vb0ox6sCQCshR3NCicpp3Ixsxqkibc/0?wx_fmt=jpeg)

# 绕过 Windows 针对 SYSTEM 的认证反射缓解措施

Guillaume André
Guillaume André

securitainment

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

| 原文链接 | 作者 |
| --- | --- |
| https://www.synacktiv.com/publications/bypassing-windows-authentication-reflection-mitigations-for-system-shells-part-1.html | Guillaume André |

> 一年前，认证反射 ( authentication reflection ) 类漏洞作为一种强大的攻击向量重新浮出水面 —— 包括我们在内的多位安全研究员共同促成了 CVE-2025-33073 的发现。这一逻辑漏洞使得攻击者几乎可以在无需任何用户交互的情况下接管任何一台 Windows 机器。在我们发布分析文章以及 Microsoft 推出官方补丁之后，我们仍然感觉到问题的根本原因尚未被真正触及。

> 这篇分为两部分的博客文章将记录我们绕过这些加固措施的过程，而这一过程也让我们发现了两个全新的认证反射漏洞。在第一部分中，我们将奠定研究的基础、阐述方法论，并披露我们发现的第一个漏洞：一个通过 NTLM 反射实现的、极为简单的本地权限提升。

## 引言

### CVE-2025-33073

CVE-2025-33073 是一个严重的认证反射漏洞，可在 Windows 系统上导致远程命令执行 ( RCE )。这一类漏洞的原理是：迫使某台机器上的客户端向受攻击者控制的服务器发起认证，然后再将该认证转发到同一台机器上的某个服务，从而冒用该客户端的身份。在深入阅读本文之前，**强烈建议**先阅读我们对 CVE-2025-33073 的详细分析,以便充分理解其中的技术细节。不过，该漏洞内部机制的关键要点仍简要回顾如下：

* 在向某个目标发起认证时，可以在目标名称之后以 base64 形式追加附加目标信息 ( additional target information )。
* 在构造认证 blob ( NTLM 或 Kerberos ) 之前，LSASS 会从目标名称中剥离这些附加数据。例如，使用目标名称 `srv11UWhRCAAAAAAAAAAAAAAAAAAAAAAAAAAAAwbEAYBAAAA`会让 LSASS 为 `srv1`生成认证 blob。在本系列文章中，我们将这种机制称为 CMTI ( CredMarshalTargetInfo ) 技术。
* `srv11UWhRCAAAAAAAAAAAAAAAAAAAAAAAAAAAAwbEAYBAAAA`

  同时也是一条合法的 DNS 记录。此外，在 Active Directory 环境中，默认情况下域用户就能添加 DNS 记录。
* 当我们迫使一个特权服务 ( 例如以 `NT AUTHORITY\SYSTEM`身份运行的 LSASS ) 向由此类 DNS 记录指向的服务器发起认证时，NTLM 和 Kerberos 这两种认证包都会出现一些颇为有趣的行为：
* 对于 NTLM，由于经过净化处理后的目标名称与机器名相同，因此会触发 NTLM 本地认证。又因为带有附加目标信息的 DNS 记录指向的是受控 IP 地址，我们可以将 NTLM 本地认证转发至该机器，从而冒用特权服务的身份。
* 对于 Kerberos，由于目标名称已被净化，因此用于申请服务票据 ( ST ) 的 SPN 会是 `CIFS/SRV1`。同样地，因为带有附加目标信息的 DNS 记录指向受控 IP 地址，客户端会将 `AP-REQ`发送到我们的服务器，然后再将其转发到同一台机器，以冒用特权服务的身份。
* 认证包内部存在多种机制，用于推断初始客户端是否以 `NT AUTHORITY\SYSTEM`身份运行，但关键之处在于：一旦转发成功，我们便在目标机器上拥有了一条以 `NT AUTHORITY\SYSTEM`身份认证的 SMB 会话，这已足以将该机器彻底攻陷。

### 补丁

为了缓解该漏洞，Microsoft 决定修改 SMB 客户端 ( `mrxsmb.sys`),使其拒绝连接到名称中包含附加目标信息的目标。从一开始，这种缓解方式就让我们觉得有些奇怪：倘若以某种方式发现了另一种技术，可以让受控服务器收到 NTLM 本地认证或 Kerberos `AP-REQ`,那么该漏洞岂不是又被重新引入了！于是我们决定核实这是否真的可行。

首先，我们将描述本次研究中所遵循的、通用且具有迭代性的绕过方法论。随后，我们将立刻通过披露发现的第一个漏洞来对该方法论进行示范：一个通过 NTLM 反射实现的、极为简单的本地权限提升。

## 方法论

### 原理

要绕过一项缓解措施，最重要的是先彻底搞清楚它到底做了什么。同样，要找到漏洞的变种，就必须深入理解原始漏洞。在我们的案例中，这一步并不困难，因为一年前向 Microsoft 报告该漏洞时，我们就已经做过这样的分析。

接下来的目标是尽可能多地构想出在补丁覆盖范围之外的、理论上的攻击场景。在这一阶段，场景是否可行并不重要：它们只需要不被补丁所影响即可。

最后，每一种攻击策略都需要根据多项标准进行评估：可行性、前置条件等等。除了攻击实际是否可行这一点之外，大多数标准都比较主观，取决于个人偏好。在本次研究中，我们选择遵循以下规则：

* 攻击至少应能在最新版本的 Windows 11 或 Windows Server 2025 上奏效 ( 以满足 bounty 资格要求 )。
* 攻击应能在默认配置下奏效。
* 攻击不应需要任何用户交互。
* 攻击应能导致 RCE 或 LPE 二者之一。

如果某种攻击策略满足上述全部预设标准，则将其选中并进行测试。这一通用的绕过方法论可以用下图来概括：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/h4gtbB74nSgzoNQ1wF2RZBKCoyfSwY0nfpibKezt29icicjyyLicJoTEywYP3LibO2e4tLp2VzZq3ysk6BWYjObnnhzHd7vjAvQcVFgOn3JMnibFU/640?wx_fmt=png&from=appmsg)

通用绕过方法论示意图。

### 改用其他客户端协议

由于补丁仅作用于 SMB 客户端，我们不妨尝试改用其他客户端协议来强制触发认证。事实上，CMTI 技术与 SMB 协议本身并无关联，理论上可以应用于任何使用 NTLM 或 Kerberos 认证的协议。除了 SMB 之外，还有两种协议可用于强制认证，只是各自的前置条件门槛不同:RPC ( 包括 DCOM ) 与 HTTP。

#### RPC

RPC 强制认证通常借助 DCOM 来触发，所使用的小技巧由 James Forshaw 在 10 年前 进行了说明。然而自 2022 年 10 月起，DCOM 客户端在认证时所采用的认证级别始终不会低于 `RPC_C_AUTHN_LEVEL_PKT_INTEGRITY`,这意味着在向 SMB 转发时会协商签名。

我们可以将转发目标改为 HTTP，因为 HTTP 不支持完整性机制 ( 在 HTTPS 上的 channel binding 除外 )。然而，默认情况下 Windows 机器并不会暴露任何可被用于攻陷该机器的 HTTP 服务器，这并不符合我们「默认配置」这一标准。确实存在一些众所周知的、可能导致机器 ( 或域 ) 被攻陷的 HTTP 服务，例如 ADCS 的 Web Enrollment 或 SCCM 的 AdminService，但我们想要的是一个能在不安装任何特定角色或软件的 Windows 机器上奏效的利用方式。因此，我们决定放弃这条思路。

值得一提的是，这一攻击策略已被 @decoder\_it 探索过，并最终促成了 CVE-2026-26119 的发现 —— 该漏洞针对 Windows Admin Center 的 HTTP 服务进行攻击。

#### HTTP

HTTP 强制认证主要通过 `WebClient`服务来实现 —— 该服务实现了一个 WebDAV 客户端。要让一台机器通过 WebDAV ( 也即 HTTP ) 进行认证，该服务必须处于运行状态。这在 Windows 工作站上并非默认情况;虽然存在一些将其启动起来的方法，但都需要用户交互，因而不符合我们的标准。在 Windows 服务器上，该服务甚至根本就没有安装。

此外，Windows 上至少大多数 HTTP 客户端都会在生成认证 blob 之前将目标名称转换为小写，这使得 CMTI 技术无法奏效，因为它依赖于 base64 编码的数据 ( 而 base64 是大小写敏感的 )。

基于上述原因，我们同样决定放弃这条路线。

### 在目标名称上做文章

另一种可能性是继续使用 SMB 作为被转发的客户端及转发目标，但寻找其他方式迫使客户端向受控服务器发起认证，同时保持攻击中的本地认证特性。

#### 向 localhost 发起认证

我们的第一个想法是尝试强制让认证目标指向 localhost。当目标名称为 `localhost`( 或本地 IP 地址 ) 时，NTLM 认证包会发起 NTLM 本地认证，我们便可以将其转发到 SMB 服务。唯一的难点在于：如何强制 SMB 客户端连接到我们的 SMB 服务器，而非默认的那个。此外，这意味着影响范围将仅限于 LPE，但这仍然符合我们的标准。

#### 寻找另一种 Kerberos 强制认证原语

另一条显而易见的攻击思路是寻找一种能够替代 CMTI 的技术，使我们能够收到任意服务的 `AP-REQ`消息。事实上，目前并不存在专门用于阻止 Kerberos 反射攻击的缓解措施 ( 通信完整性或机密性除外 )。主要挑战在于：如何针对任意服务、向任意 IP 地址强制发起 Kerberos 认证，因为 Kerberos 与域名之间存在着紧密的耦合。

因此我们最终选定了上述两个攻击思路。将我们的通用绕过方法论应用到 CVE-2025-33073 上，可得到下图：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/h4gtbB74nSgZZvdLfibRzlAMRfjo4LrH2SqXeGG5TLYsfZiayibH7n4qjVWqyO6gYFnUakEGvdxibnIxdWRmoL5x2I0ZnPOQ7LE8PaqtZVG2p9c/640?wx_fmt=png&from=appmsg)

应用于 CVE-2025-33073 的绕过方法论。

## 本地反射

### SMB 客户端的任意连接端口

在我们沿着这条思路深入研究的过程中，James Forshaw 此前发表的一篇博客立刻浮现在我们脑海中。在那篇文章里，他描述了对一项老旧技术的改进，该技术利用远程 SMB 服务器来延迟对文件数据的访问，从而推迟对虚拟内存的读取。这项改进利用了一个相对较新的功能 —— 该功能在 Windows 11 24H2 和 Windows Server 2025 中引入，允许在连接 SMB 共享时指定一个任意端口。这正是我们所需要的！

任何 Windows 系统的用户都可以使用这一新功能。例如，要在 12345 端口上挂载远程 SMB 共享，可以执行以下命令：

```
C:\> net use \\192.168.56.3\share /tcpport:12345
```

在实现层面，为引入这一功能，Microsoft 同时修改了用户态和内核态的多个组件。要建立到远程共享的连接，需要调用 WNetAddConnection4W 函数，并在 `lpUseOptions`参数中传入一个未公开文档的数据缓冲区。该缓冲区是以下结构体的数组：

```
structUSE_OPTION
{
  DWORD OptionType;
  DWORD Size;
  BYTE OptionData[];
};
```

目前，`OptionType`已实现的取值有四种：

* `TraP`

  :传输 ( transport ) 参数。该选项类型中，除其他内容外，还包含用于 SMB 连接的任意 TCP 端口。
* `DefC`

  :延迟连接 ( deferred connection ) 参数。
* `ComP`

  :压缩 ( compression ) 参数。
* `BloN`

  :NTLM 阻断 ( NTLM blocking ) 参数。

`Size`参数等于 `USE_OPTION`头部大小 ( 8 字节 ) 加上实际选项数据大小。

在本次研究中，我们仅对传输参数对应的数据结构进行了逆向分析：

```
structTRANSPORT_USE_OPTION
{
  DWORD TransportType;
  BOOLEAN SkipCertCheck;
  WORD TcpPort;
  WORD QuicPort;
  WORD RdmaPort;
  DWORD PortTypes;
};
```

其中 `TransportType`字段的取值如下：

* 1 表示 TCP。
* 2 表示 QUIC。

`PortTypes`字段是以下数值的组合：

* 1 表示 TCP。
* 2 表示 QUIC。
* 4 表示 RDMA。

存放于 `lpUseOptions`中的数据会被传递给 `ntlanman!LmCreateEABufferForUseOptions`函数。该函数解析输入缓冲区，并构造一个新的缓冲区，稍后通过 FSCTL 提交至内核。最终，SMB 客户端会接收到该缓冲区，并在 `mrxsmb!MRxSmbSetNetUseSpecifiedTransportInfo`中对其进行解析，以判断是否需要在替代端口上建立连接。

有趣的是，在谈到这一功能时，James 还提到：

> 我个人认为，默认开启它是一个错误，未来还会回来给 Windows 制造麻烦。

事实证明，他一如往常地说对了。

![](https://mmbiz.qpic.cn/mmbiz_png/h4gtbB74nSjnv0icQypVfCCB0gRzyBOibOicCmIBAfnJhafQvm0RGiaicuLsnf9U3oERffzvheiaDoLSfjCpcAH6KB6WC6LicsrKqxI5T6agxR6x2o/640?wx_fmt=png&from=appmsg)

默认开启这一功能是一个错误。

因此，攻击思路是：在本地搭建一个监听非 445 端口的 SMB 服务器，然后强制让一个特权服务向其发起认证。然而，我们随即遇到了下面这个问题：如何告诉特权服务必须连接到我们位于自定义端口上的服务器，而不是默认的 445 端口？事实上，要强制一个服务向任意 SMB 共享发起认证，我们通常会让它以 UNC 语法 ( `\\IP\SHARE`) 提供一个文件路径，并尝试打开该文件。而 UNC 语法并不允许指定端口 ( WebDAV 共享除外 )。此外，`net use`仅作用于当前用户会话：出于显而易见的安全原因，某个用户不能访问另一个用户已认证的 SMB 会话。

### SMB 多路复用

事实证明，这其实根本不是问题！官方规范 MS-SMB2 ( 第 3.2.4.2 节 ) 写道：

> 如果正在建立一条新会话，客户端**可以**复用现有连接，使多个会话在同一连接上多路复用。如果不复用现有连接，客户端可以为新会话建立一条新连接。

换言之，**SMB 区分 TCP 连接与已认证会话**:多个已认证的会话可以共用同一条 TCP 连接作为传输通道。此外，Windows 的 SMB 客户端会复用 TCP 连接。

### 本地权限提升

整个利用策略主要分为两个步骤：

1. 在本地 12345 端口启动一个 SMB 服务器，并将其挂载。这会让 SMB 客户端建立一条到我们这个共享的 TCP 连接，并将其保持打开，以便后续复用。需要注意的是，这一步并不需要持有有效凭证：本地共享可以配置为接受指定凭证 ( 例如 `user:user`),然后再调用 `net use`用相同的凭证完成认证。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/h4gtbB74nShHIaz8ustAiafpzibTGsPIUvvCDcrrkSLCJRyWrDVCc71GXxI63U0HlS7xOwYZeYQ9LJlY8K8Ks1fVX0wlxGYA05KbF3ibxYz8dE/640?wx_fmt=png&from=appmsg)

NTLM 本地反射的步骤一。

1. 迫使一个特权服务 ( 例如 LSASS ) 向先前所挂载的同一共享发起认证。这里必须使用相同的共享路径，以便 SMB 客户端复用之前在挂载该共享时所建立的同一条 TCP 连接。该服务会向我们自定义的 SMB 服务器发起认证，而 NTLM 本地认证会被转发到机器自身真正的 SMB 服务上，最终得到一条特权 SMB 会话，从而将该机器攻陷。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/h4gtbB74nSha0MRicZFAmRiby1ics8x7e8vNXF8PZ7klvWFu4qwMsBJJ1E6NDHsP01hHXde6SlbyZyTSMBlI3UcaCwjOjCv3bjrE7eiahTsz3RQ/640?wx_fmt=png&from=appmsg)

NTLM 本地反射的步骤二。

为构建一个可用的 PoC，我们使用了以下工具：

* Impacket 的 `smbserver.py`:用于在自定义端口上启动一个 SMB 服务，接收特权的 NTLM 本地认证 blob，并将其转交给中继服务器。我们对其做了少量修改，以便在挂载共享所用的同一条 TCP 连接上解析后续接收到的特权认证 blob。
* Impacket 的 `ntlmrelayx.py`:用于将特权认证 blob 转发到机器自身真正的 SMB 服务，并以 `NT AUTHORITY\SYSTEM`身份执行命令。
* `net.exe`

  :用于在指定 TCP 端口上挂载自定义的 SMB 共享。
* `PetitPotam.exe`

  :用于强制 LSASS 向自定义 SMB 服务发起认证。我们对其做了少...
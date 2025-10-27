---
title: 如何从 Parallels Desktop虚拟机中逃逸
url: https://www.4hou.com/posts/BXP2
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2023-06-12
fetch_date: 2025-10-04T11:44:51.909586
---

# 如何从 Parallels Desktop虚拟机中逃逸

如何从 Parallels Desktop虚拟机中逃逸 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

[![](https://www.4hou.com/sihou/images/new4hou/newlogoss.png)](https://www.4hou.com)

* [首页](https://www.4hou.com)
* [企业中心](https://www.4hou.com/corp/newindex)
* [产业研究院](https://www.4hou.com/real-time)

![](https://www.4hou.com/sihou/images/new4hou/search-icon.png)

[投稿](https://www.4hou.com/contribute)

[登录](https://www.4hou.com/login)
  |
[注册](https://www.4hou.com/register)

* 导读 ▾
* [活动](https://www.4hou.com/newticket)
* [专题](https://www.4hou.com/category/special)
* [图谱](https://www.4hou.com/atlas/index)
* [报告](https://www.4hou.com/new-report-info)
* [嘶票](https://www.4hou.com/tickets)
* [嘶货](https://www.4hou.com/shop)
* [企业查询](https://www.4hou.com/corp/new-search-company)
* [招聘](https://www.4hou.com/recruit)![](https://www.4hou.com/sihou/images/1561626446625934.png)

* [新闻](https://www.4hou.com/category/news)
* [行业](https://www.4hou.com/category/industry)
* [趋势](https://www.4hou.com/category/observation)
* [访谈](https://www.4hou.com/category/people)
* [漏洞](https://www.4hou.com/category/vulnerable)
* [WEB安全](https://www.4hou.com/category/web)
* [业务安全](https://www.4hou.com/category/business)
* [系统安全](https://www.4hou.com/category/system)
* [内网渗透](https://www.4hou.com/category/penetration)
* [勒索软件](https://www.4hou.com/category/typ)
* [安全工具](https://www.4hou.com/category/tools)

# 如何从 Parallels Desktop虚拟机中逃逸

xiaohui
[漏洞](https://www.4hou.com/category/vulnerable)
2023-06-11 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)190874

收藏

导语：本文会详细介绍最新发现的两个漏洞，一个是plist注入（CVE-2023-27328），另一个是竞态条件（CVE-202 3-27327），这两个漏洞可以用来从GuestParallels Desktop虚拟机中逃脱。

本文会详细介绍最新发现的两个漏洞，一个是plist注入（CVE-2023-27328），另一个是竞态条件（CVE-202 3-27327），这两个漏洞可以用来从GuestParallels Desktop虚拟机中逃脱。在这篇文章中，我将对研究结果进行分解。

Parallels Desktop 被称为 macOS 上最强大的虚拟机软件。可以在 Mac 下同时模拟运行 Win、Linux、Android 等多种操作系统及软件而不必重启电脑，并能在不同系统间随意切换。

最新版的 Parallels Desktop 18 (PD18) 完美支持最新的 macOS Ventura、Monterey 和 Windows 11、Win10，并充分优化！可不重启直接在 Mac 系统上运行 Linux 和 Windows 应用软件、游戏、使用诸如 Office 办公软件、VisualStudio、AutoCAD 等工具。

**Toolgate & Parallels工具**

Parallels Desktop使用名为“Parallels ToolGate”的半虚拟PCI设备,用于Guest操作系统和主机操作系统之间的通信。

Toolgate是Parallels中用于Guest和主机之间通信的协议，由于其庞大的攻击面和相对不成熟的安全态势，因此它是一个寻找漏洞的好地方。

在x86 Guest上，通过将TG\_REQUEST结构的物理地址写入特定的I/O端口，从Guest向主机发送Toolgate请求。

请求结构包括一个操作码（request）、一个由主机更新以指示请求状态的状态字段（status）、可选的内联数据（如果InlineByteCount>0）和TG\_BUFFER结构的可选列表（如果BufferCount>0）。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230523/1684856693512584.png "1684856693512584.png")

Parallels Tools是一种可以安装在Guest中的软件（类似于VirtualBox guest Additions或VMWare Tools），它添加了各种有用的功能，如共享文件夹、共享剪贴板以及在虚拟机中拖放。

Parallels Tools还为userland进程添加了一个通道，用于发出Toolgate请求。在Linux上，这是一个在/proc/driver/prl\_tg创建的proc条目，由prl\_tg内核模块创建和管理，在Windows上，它是一个位于\\的命名管道。\管道\平行工具管道。Parallels Tools还包含各种userland进程和服务，这些进程和服务使用此通道来促进这些有用的功能。

重要的是，用户和进程可以使用Parallels Tools创建的通道向主机发送哪些Toolgate消息是有限制的，这是由prl\_tg内核模块强制执行的。具体来说，操作码（又名请求字段）必须大于TG\_Request\_SECURED\_MAX的值，该值定义为0x7fff，否则对proc条目的写入将失败，并出现EINVAL。我们可以在这里看到这方面的代码：

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230523/1684856706166820.png "1684856706166820.png")

正如注释所建议的，只有那些处理文件系统操作的Toolgate操作码小于这个阈值。这意味着，如果我们想发送与文件系统相关的Toolgate请求，我们必须绕过此检查。

**共享应用程序**

共享应用程序是一个Parallels功能，它允许在Guest应用程序中打开Mac上的文件，反之亦然。它还允许将文件扩展名和URL方案与Guest应用程序相关联。

Parallels通过监控Guest中启动的新应用程序，然后在新应用程序启动时向主机发送Toolgate请求，来处理将运行Guest应用程序“同步”到主机的操作。主机通过创建和启动“辅助”应用程序来处理这些消息，这些应用程序与Guest中的应用程序具有相同的名称和图标。这些辅助应用程序在运行时会显示在Mac dock中，并且在不运行时可用于从dock或Launchpad启动Guest中的相应应用程序。

此同步过程如下：

1.Parallels Tools检测到在Guest中启动了应用程序；

2.它向主机发送一个Toolgate请求（TG\_request\_FAVRUNAPPS，操作码0x8302），通知它已启动具有给定名称和图标的应用程序；

3.如果此Guest应用程序已经存在一个辅助应用，则启动该辅助应用程序并完成操作；

4.如果辅助应用程序不存在，则在~/Applications (Parallels)/

5.应用程序bundle（Unix/linux系统中的一种可执行文件。用户可以在终端中使用./\*\*\*（文件名）.bundle命令使其运行）是根据一个模板创建的，该模板是使用Guest提供的信息填写的。作为Toolgate请求的一部分，Guest发送的信息包括应用程序名称、描述和图标等。这些信息被写入到新应用程序bundle中的几个文件中，包括Info.plist，它是应用程序bundle中的（XML）文件，其中包括有关bundle的元数据，Info.plist可用来构建任意数据，这些数据在运行时是可访问的，Info.plist是每个bundle的专属配置，Info.plist文件中的keys和values描述了许多要应用于该bundle的行为以及配置选项；

6.新的辅助应用程序已启动，因此它显示在dock中；

辅助应用程序包含一个名为WinAppHelper的二进制文件，该二进制文件直接从模板中复制，并作为应用程序bundle的入口点存在。当应用程序运行时，该二进制文件将解析应用程序bundle中特定于Parallels的配置文件（例如AppParams.pva），并向相应的Guest虚拟机发送消息以启动相关应用程序（如果该应用程序尚未运行）。

 Info.plist模板的片段如下所示，它取自hypervisor二进制文件。突出显示的占位符将被Guest提供的输入替换。

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230523/1684856730134401.png "1684856730134401.png")

假设主持人正在接受Guest的输入，并使用它来填写Info.plist模板，重要的是要对来自guest的所有输入进行适当的转义或净化，因此不可能将XML注入plist并修改辅助应用程序的行为。研究发现，除了URL方案和文件扩展名这两个字段之外，Guest提供的所有字段都完成了转义。这允许注册Guest应用程序将分别处理的文件扩展名和URL方案。

这意味着我们可以发送自己的Toolgate请求（操作码0x8302），告诉主机创建一个带有恶意URL方案或文件扩展名的辅助应用程序。在上述示例中，研究人员选择了利用Info.plist中的URL方案，这些方案是在CFBundleURLSchemes数组中未加注释的情况下编写的。

创建CFBundleURLSchemes数组的相关模板如下所示：

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230523/1684856748194679.png "1684856748194679.png")

%1被替换为Guest提供的URL方案，每个方案都封装在标记中，随后将完成的模板插入Info.plist 模板中。

代码形式如下所示：

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230523/1684856765178622.png "1684856765178622.png")

可以滥用的一种方法是使用LSEnvironment项设置DYLD\_INSERT\_LIBRARIES环境变量。这可以用来强制辅助二进制文件（WinAppHelper）在执行时加载任意dylib。研究人员确实花了一段时间寻找Info.plist 的其他特性，发现可以在不需要第二个漏洞的情况下利用它们。

例如，如果我们提供以下字符串作为URL方案：

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230523/1684856783133747.png "1684856783133747.png")

它被包装在

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230523/1684856802144658.png "1684856802144658.png")

现在，当执行WinAppHelper时，它将加载我们选择的dylib。如果我们可以利用现有的dylib来做一些有趣的事情，或者在磁盘上的某个地方创建我们自己的dylib，那么我们可以使用它在主机上执行代码。

**获取文件写入**

为了在没有用户交互的情况下完成在主机上执行代码的目标，我需要找到一种方法，将受控的dylib写入主机的已知位置。不幸的是，辅助应用程序bundle中没有可以被我们完全控制的文件（包括例如应用程序图标）。共享文件夹似乎是一个查找漏洞的好地方，可以让我们实现目标。

Parallels中的共享文件夹实际上是使用Toolgate实现的，它具有用于文件管理各个方面的操作码，包括打开、读取和写入文件。共享文件夹文件系统内核模块（prl\_fs）在Guest中发生文件系统操作时，将相关的Toolgate指令写入主机，然后主机执行请求的操作。

如上所述，所有这些操作码都被Parallels Tools创建的通信通道所禁止，这意味着要发送与文件系统相关的操作码，我们需要加载自己的内核模块才能完成，不幸的是，这需要root权限。为了做到这一点，我们使用了现有的prl\_tg代码，并进行了一些修改以删除安全检查。

一旦我们可以向Toolgate写入任意消息，就可以使用TG\_REQUEST\_FS\_L\_open（0x223）操作码打开共享文件夹中的文件。在hypervisor中，文件路径是通过将Guest提供的文件路径附加到主机上配置的共享文件夹路径来构建的。在处理打开请求时，有一些安全检查，以确保Guest不能打开主机共享文件夹路径之外的文件，包括：

检查文件路径是否包含..，这应该已经被Guest标准化了；

检查文件是否是指向共享外部的符号链接；

打开构造的路径并检查生成的文件是否在主机上的共享文件夹之外，这是使用fcntl的F\_GETPATH选项完成的。

如果任何一项检查失败，Parallels将拒绝打开该文件，并将向Guest返回一个漏洞。检查本身看起来不错，但问题是在进行安全检查和实际打开文件之间存在检查到使用时间（TOCTOU）的机会。这意味着，如果我们在安全检查之后，但在打开之前，快速将路径从普通文件切换到指向主机上共享外部路径的符号链接，那么系统管理程序将为我们打开主机上符号链接的目标。

之后，我们可以使用对Toolgate的后续调用来简单地读取或写入打开的文件。换句话说，这使我们能够读取或写入主机上的任何文件，前提是主机进程具有权限。

但如果共享文件夹文件系统为我们做这件事，为什么我们还需要Toolgate请求呢？理论上，只需使用共享文件夹中的文件执行竞争，而无需发送手动Toolgate请求，就可以利用此漏洞。然而，在实践中，试图仅通过文件系统操作来利用这种竞争会在prl\_fs内核模块中触发一个漏洞，从而导致系统崩溃。

**综合分析**

第一个漏洞允许我们在主机上加载任何dylib，第二个漏洞使我们能够在主机文件系统的任何位置写入任意文件（假设Parallels进程具有权限）。因此，我们可以创建一个恶意的dylib，将其写入主机上的已知位置，并强制辅助应用程序加载它，这将使我们在没有用户交互的情况下执行代码。

我们可以使用下面的代码编译成一个dylib，它将在加载dylib时弹出一个计算器。

![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230523/1684856823127158.png "1684856823127158.png")

**总结**

这个链可以被任何具有提升权限的代码从任何Guest操作系统中利用，这些权限是使用编写任意Toolgate请求所需的权限指令所必需的。如果安装了Parallels Tools，那么plist注入漏洞可以以较低的权限利用，但文件写入漏洞仍然需要加载我们自己的内核模块，以绕过安全限制，并发送与文件系统相关的Toolgate请求。

总的来说，Parallels是一个有趣的目标。根据我和其他人发现的漏洞，它比VirtualBox和VMWare等更不成熟，其中必定还有很多漏洞。

本文翻译自：https://pwn.win/2023/05/08/parallels-escape.html如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?7IGnJTPk)

#### 你可能感兴趣的

* [![]()

  Salesloft: GitHub账户遭入侵 导致Drift令牌被盗并引发大规模Salesforce数据窃取](https://www.4hou.com/posts/33NQ)
* [![]()

  TP-Link确认路由器存在未修复零日漏洞](https://www.4hou.com/posts/YZ8p)
* [![]()

  黑客借助HexStrike-AI工具可快速利用新型漏洞](https://www.4hou.com/posts/PGyn)
* [![]()

  黑客利用Sitecore零日漏洞部署WeepSteel侦察恶意软件](https://www.4hou.com/posts/RXAR)
* [![]()

  Docker Desktop严重漏洞可让攻击者劫持Windows主机](...
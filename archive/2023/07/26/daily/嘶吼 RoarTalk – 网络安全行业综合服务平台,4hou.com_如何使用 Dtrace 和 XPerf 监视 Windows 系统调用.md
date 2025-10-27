---
title: 如何使用 Dtrace 和 XPerf 监视 Windows 系统调用
url: https://www.4hou.com/posts/9AOJ
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2023-07-26
fetch_date: 2025-10-04T11:53:42.595055
---

# 如何使用 Dtrace 和 XPerf 监视 Windows 系统调用

如何使用 Dtrace 和 XPerf 监视 Windows 系统调用 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 如何使用 Dtrace 和 XPerf 监视 Windows 系统调用

walker
[技术](https://www.4hou.com/category/technology)
2023-07-25 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)128526

收藏

导语：在本文中，我们讨论在 Windows 中监视系统调用的一些核心方法。

监视系统调用 (syscall) 和分析系统行为可以帮助您调试产品并提高其性能、安全性和合规性。然而，由于缺乏内置工具以及需要逆向工程和应用程序行为分析的专业知识，监视 Windows 中的系统调用面临着挑战。

在本文中，我们讨论在 Windows 中监视系统调用的一些核心方法。

**监控 Windows 中的系统调用：查看内容以及原因**

系统调用是一种使程序能够从操作系统内核请求各种类型的服务和任务的机制。系统调用为用户级程序访问系统资源提供了一种安全且受控的方式，而不会影响操作系统 (OS) 的稳定性或安全性。当执行请求的操作时，系统调用在用户模式和内核模式之间转移控制。

系统调用是ring-0/ring-3隔离的标准部分。让我们仔细看看。

**在操作系统中，有两种代码环境：**

以完全权限运行的内核代码（环 0）

以有限权限运行的用户代码（环 3）

在这些环境之间，有一个系统调用接口。

环 0 和环 3 之间的划分（内核级别和用户级别）是观察应用程序行为和原始操作的最佳点。当代码达到系统调用级别时，应用程序无法混淆其操作。例如，如果用户级代码秘密调用CreateFile()函数，您仍然可以通过监视系统调用来检测到这一点，因为您将看到 NtCreateFile 系统调用的执行。

**对于大多数流行的体系结构，包括 x86、AMD64、ARM64 和 PowerPC，处理系统调用的方法是相同的：**

在用户级别， 一组系统 API 充当系统调用的包装器。

在内核级别，内核 API 实现系统调用的处理程序并由内核驱动程序使用。

在某些体系结构中，系统调用称为系统服务。

**Windows 中系统调用的常见示例包****括：**

文件输入/输出 (I/O) 操作，例如读取或写入文件

流程管理，例如创建新流程或终止现有流程

内存管理，例如分配内存

进程间通信，例如在进程之间发送或接收消息

设备驱动程序操作，例如向硬件设备发送命令

为什么您的开发人员需要监视系统调用？

Windows 系统调用监控对于研究多层软件和分析具有混淆代码的应用程序的行为至关重要。使用这种方法，您可以确定特定应用程序的行为方式，而无需分析应用程序每个级别的代码。

**监控系统调用的常见原因包括：**

调试—— 跟踪应用程序中的问题，确定其根本原因，并快速修复错误。

性能优化——识别瓶颈并优化有问题的代码部分以提高整体性能。

安全——检测可疑的、潜在的恶意行为，并采取措施阻止其发生。

合规性——通过分析应用程序访问和使用特定类型数据的方式，确保应用程序符合相关要求。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230714/1689303045161386.png "1689301828654866.png")

然而，在实践中应用这种方法面临着多重挑战。它需要深入了解操作系统的细节以及逆向工程和应用程序行为分析的利基知识。在下一节中，我们将根据 Apriorit 专家的经验，讨论开发人员在尝试监视 Windows 中的系统调用时可能面临的关键问题。

**Windows 中的系统调用监控挑战**

与 Linux 具有用于监视任何进程中的系统调用的strace工具相比，Windows 由于安全原因没有用于此任务的内置工具。然而，在 Windows XP 之前，任何需要监视或控制用户级代码的软件（例如防病毒软件）都可以在两个表中设置挂钩：

系统服务描述符表（SSDT）

影子系统服务描述符表（影子SSDT）

这些表包含指向处理特定系统调用的内核函数的指针。

在 SSDT 和 Shadow SSDT 中设置挂钩会导致大量冲突和不稳定，导致 Windows 声誉受损，并使其看起来像一个不可靠的操作系统。除此之外，rootkit 和病毒还能够在 SSDT 和 Shadow SSDT 中设置挂钩。这就是为什么微软被迫阻止对这些表的访问，并且从Windows XP开始，实施了PatchGuard，也称为内核补丁保护。从那时起，系统监控工具只能为一小部分内核事件设置回调，这使得系统调用的监控变得非常具有挑战性。

下面，我们讨论如何监视 Windows 中的系统调用，并解释一种安全有效的方法来分析 Windows 中的程序行为。

**使用 XPerf 监控 Windows 系统调用**

在 Windows XP 中，Microsoft 引入了Windows 事件跟踪 (ETW)机制，用于XPerf工具使用的详细事件日志记录。后者现在是Windows Performance Toolkit的一部分。

一般来说，微软将 ETW 回调放置在整个 Windows 子系统中，以便能够跟踪低级事件。使用 ETW，您可以获取系统事件，因此 XPerf 对于监视系统调用也可能很有用。

让我们看看如何使用 XPerf 来监视 Windows 中的系统调用。

首先，我们查询 ETW 提供者，看看是否有与系统调用相关的内容：

```
logman.exe query providers
```

在我们从 XPerf 收到的信息中，没有任何看起来像系统调用的内容。转到 TraceView 并监视名称如 Microsoft-Windows-Kernel-\* 的内核提供程序事件，也为我们带来了各种类型的内核事件，但没有有关系统调用的结果。

下一个可能性是使用SystemTraceProvider 一个跟踪内核事件的内核提供程序。将这个提供程序的 GUID 添加到 TraceView 后，我们仍然没有结果。

为了寻找设置挂钩的可能替代方案，我们尝试了不同的方法来监视 Windows 中的系统调用，包括通过虚拟机管理程序挂钩 SSDT 函数以及使用 Windows 事件跟踪的未记录部分。

**使用 Syscall Monitor 和 InfinityHook 监控 Windows 系统调用**

为了寻找替代解决方案，我们决定研究一下记录较少的监控系统调用的方法。

免责声明：以下操作仅用于研究目的。

**在研究了几种可能性之后，我们在 GitHub 上发现了两个有前途的项目：**

系统调用监视器

无限钩

让我们从测试 Syscall Monitor 工具开始。该项目使用虚拟机扩展通过虚拟机管理程序挂钩 SSDT 功能。该方法本身有效，使得监视 Windows 中的系统调用成为可能。不幸的是，作者决定实现该工具作为ProcessMonitor的替代品。因此，Syscall Monitor 的能力有限，只能监控一小部分系统调用：

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230714/1689303046136041.png "1689301853136677.png")

总而言之，Syscall Monitor 是一个很好的工具，可以帮助您开始研究 SSDT 挂钩，但如果您想监视图形设备接口 (GDI) 系统调用等内容，则该工具就没用了。

现在，让我们继续测试 InfinityHook 工具的使用。根据该工具的描述，在使用它之前，您需要了解ETW的基础知识。

为了监视 Windows 中的系统调用，InfinityHook 在系统调用处理程序的内核代码中使用 ETW 跟踪的未记录部分。值得注意的是，该项目无法轻松地开箱即用，我们必须在设法运行代码之前实现一些细微的更改。然而，结果我们得到了 BSOD：

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230714/1689303047198994.png "1689301874212198.png")屏幕截图 2. 使用 InfinityHook 工具的结果

从上面的屏幕截图中可以看到，我们收到一条错误消息，内容为“停止代码：KERNEL\_SECURITY\_CHECK\_FAILURE”。此消息意味着内核补丁保护已被触发。显然，最新版本的 Windows 保护内核 ETW 提供程序回调免受修改，因此为了监视 Windows 系统调用，我们需要禁用 PatchGuard。

在 Windows 10 中禁用 PatchGuard 的一种方法是使用EfiGuard项目。按照 GitHub 的说明，我们使用软盘映像启动 Windows 10 的 VMWare 实例，用于此类研究和实验：

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230714/1689303047916492.png "1689301891795005.png")

屏幕截图 3. 使用 EfiGuard 工具的结果

我们尝试了几种不同的驱动程序签名强制绕过方法，但结果仍然相同 - 我们仍然遇到由内核补丁保护触发的 BSOD。经过进一步调查，我们确定 EfiGuard 在不同的 Windows 版本上成功运行 - 具体来说，Windows 10 版本 1511。

然后，我们创建了一个新的 VMWare 映像，并在其上安装了 Windows 10 build 1511，并尝试使用 EfiGuard 再次禁用 PatchGuard。这一次，我们的尝试成功了，我们终于成功运行了InfinityHook项目。InfinityHook 使用DbgPrint()
函数打印有关来自驱动程序的系统调用的信息。因此，我们需要使用DebugView工具来查看其日志。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230714/1689303047207471.png "1689301918153365.png")屏幕截图 4. InfinityHook 中的系统调用监控结果

**从上面的截图可以看出，InfinityHook提供了以下数据：**

系统调用索引

EPROCESS值

系统调用的堆栈指针

索引超过 4000 的系统调用是 GDI 调用。为了正确地将索引映射到系统调用的名称，您需要知道与您的计算机运行的内核版本相关的系统调用索引。您还可以尝试使用互联网上提供的系统调用表之一进行进一步研究。

然而，由于这种方法需要额外的努力，我们尝试寻找一种更方便、更安全的方法来监视 Windows 中的系统调用。在下一节中，我们将详细讨论如何使用 DTrace 来监视 Windows 系统调用。

**使用 DTrace 监控 Windows 系统调用**

DTrace是一个动态跟踪框架，允许开发人员在用户模式和内核模式下实时分析系统行为。该框架最初由 Sun Microsystems 为 Solaris 操作系统开发，后来移植到其他类 Unix 操作系统，例如macOS和 Linux。

目前，微软还支持DTrace，使开发人员和软件研究人员能够监控从Windows 10 Build 1903开始的64位平台上的系统调用。但是，该工具只能捕获64位进程的痕迹。

GitHub 上的DTrace on Windows页面包含有关如何安装它的易于遵循的说明，因此我们将在概述中省略这部分。

默认情况下，系统将 DTrace 放置在C:\Program Files\DTrace文件夹中。要使用它，您需要以管理员身份运行以下命令：

```
dtrace -ln syscall:::
```

运行此命令后，DTrace 应打印系统中可用于监视的系统调用列表。

注意：每个系统调用都会打印两次，因为您可以监视系统调用参数及其返回值。

接下来，运行以下用D语言编写的脚本继续进行系统调用监控：

```
syscall:::   /pid == 9140/    {  printf ("%s called\n", execname);    }
```

这个特定的脚本打印 PID = 9140 的进程的所有系统调用。通过更改 PID，您可以监视您感兴趣的任何其他进程的系统调用。

将脚本保存为 test.d 文件，然后您可以使用简单的命令运行它：

```
Dtrace -s test.d
```

要了解其工作原理，让我们运行记事本脚本。我们收到以下结果：

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230714/1689303048220435.png "1689302094981386.png")

屏幕截图 5. 使用 DTrace 监控记事本系统调用

您可以随时按Ctrl+C停止使用 DTrace 监视 Windows 系统调用。

要了解有关使用 DTrace 脚本和可能的系统监控方法的更多信息，您可以探索 Microsoft 在 DTrace GitHub 页面上提供的示例。

**结论**

监视系统调用可以提供有关应用程序行为和性能的宝贵见解，从而帮助开发人员创建更可靠、更高效、更安全的应用程序。要监视 Windows 中的系统调用，可以使用 Microsoft 官方支持的 DTrace 实现。

本文翻译自：https://www.apriorit.com/dev-blog/reverse-engineering-monitoring-syscalls-windows如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?Q7UpSCoE)

#### 你可能感兴趣的

* [![]()

  新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)
* [![]()

  ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)
* [![]()

  Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)
* [![]()

  NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)
* [![]()

  前瞻对抗｜这大概是首次，AI挖出了Linux内核可利用0day](https://www.4hou.com/posts/6MAV)
* [![]()

  攻防速写｜一条微...
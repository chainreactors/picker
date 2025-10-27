---
title: 以 Roshtyak 后门为例介绍恶意软件的自保护、逃逸等技巧（二）
url: https://www.4hou.com/posts/mX9E
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-12-12
fetch_date: 2025-10-04T01:14:04.160842
---

# 以 Roshtyak 后门为例介绍恶意软件的自保护、逃逸等技巧（二）

以 Roshtyak 后门为例介绍恶意软件的自保护、逃逸等技巧（二） - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 以 Roshtyak 后门为例介绍恶意软件的自保护、逃逸等技巧（二）

luochicun
[技术](https://www.4hou.com/category/technology)
2022-12-11 19:33:10

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)126540

收藏

导语：Roshtyak包含设置自定义向量异常处理程序的检查，并有意触发各种异常，以确保它们都按预期得到处理。

**异常检查**

此外，Roshtyak包含设置自定义向量异常处理程序的检查，并有意触发各种异常，以确保它们都按预期得到处理。

Roshtyak使用RtlAddVectoredExceptionHandler设置了一个向量异常处理程序。此处理程序包含针对所选异常代码的自定义处理程序。顶级异常处理程序也使用SetUnhandledExceptionFilter注册。不应该在目标执行环境中调用此处理程序(任何有意触发的异常都不应该通过向量异常处理程序)。因此，这个顶级处理程序只包含一个对TerminateProcess的调用。有趣的是，Roshtyak还使用ZwSetInformationProcess使用ProcessDefaultHardErrorMode类来设置SEM\_FAILCRITICALERRORS。这确保了即使异常以某种方式被传递到默认异常处理程序，Windows也不会显示标准漏洞消息框，这可能会提醒受害者发生了可疑的事情。

当一切都设置好之后，Roshtyak开始生成异常。第一个异常是由一条popf指令生成的，后面直接跟着一条cpuid指令(如下所示)。popf指令弹出的值被精心设计为设置漏洞标志，而该标志又会引发一个单步异常。在物理设备上，异常会在cpuid指令之后立即触发。然后，自定义向量异常处理程序将接管并将指令指针从标记为无效指令的 C7 B2 操作码中移走。但是，在许多管理程序下，不会引发单步异常。这是因为 cpuid 指令强制 VM 退出，这可能会延迟跟踪标志的效果。如果是这种情况，处理器将在尝试执行无效操作码时引发非法指令异常。如果向量异常处理程序遇到这样的异常，它就知道它是在管理程序下运行的。 Palo Alto Networks 的一篇文章描述了这种技巧的一种变体。

![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221019/1666160718591019.png "1666160718591019.png")

基于异常的检查使用 popf 和 cpuid 来检测管理程序

另一个异常是使用双字节int 3指令(CD 03)生成的。这条指令后面是垃圾操作码。这里的 int 3 引发一个断点异常，该异常由向量异常处理程序处理。向量异常处理程序实际上并没有做任何处理异常的事情，这很有趣。这是因为默认情况下，Windows 在处理两个字节的 int 3 指令时，会将指令指针留在两个指令字节之间，指向 03 字节。当从这个 03 字节反汇编时，垃圾操作码突然开始变得有意义。我们认为这是对一些急于求成的调试器的检查，这些调试器可能会将指令指针“修复”到03字节之后的指针。

此外，向量异常处理程序检查线程的 CONTEXT 并确保寄存器 Dr0 到 Dr3 为空。如果不是，则使用硬件断点调试进程。虽然这种检查在恶意软件中比较常见，但 CONTEXT 通常是通过调用 GetThreadContext 之类的函数来获取的。此时，恶意软件开发者利用 CONTEXT 作为参数传递给异常处理程序，因此他们不需要调用任何额外的 API 函数。

**大型可执行映射**

下一次检查很有趣，主要是因为我们不确定它真正应该检查什么。首先，Roshtyak创建一个大小为0x386F000的大型PAGE\_EXECUTE\_READWRITE映射。然后它将这个映射映射到自己的地址空间9次。在这之后，它将映射设置为0x42 (inc edx的操作码)，除了最后六个字节，它们被四个inc ecx指令和jmp dword ptr [ecx]填充。接下来，它将映射视图的9个基址放入一个数组中，后面是单个ret指令的地址。最后，它将ecx指向这个数组并调用第一个映射视图，这将导致依次调用所有映射视图，直到最后的ret指令。返回后，Roshtyak 验证 edx 恰好增加了 0x1FBE6FCA 倍 (9 \* (0x386F000 - 6))。

![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221019/1666160736127869.png "1666160736127869.png")

大映射段的结尾，jmp dword ptr [ecx] 指令应该跳转到下一个映射视图的开头

我们最好的猜测是，这是另一个反模拟器检查。例如，在某些模拟器中，映射段可能没有完全实现，因此写入映射视图的一个实例的指令可能不会传播到其他八个实例。另一种理论是，这种检查可以用于请求模拟器可能无法提供的大量内存。毕竟，所有视图的总和几乎是标准32位用户模式地址空间的一半。

**中止检测过程**

这个技巧滥用 NtCreateThreadEx 中未记录的线程创建标志来检测 Roshtyak 的主进程何时被外部挂起（这可能意味着附加了调试器）。这个标志实际上允许线程即使在PsSuspendProcess被调用时也能继续运行。这与另一个滥用线程挂起计数器是带符号的8位值这一事实的技巧相结合，这意味着它的最大值为127。Roshtyak生成两个线程，其中一个线程持续挂起另一个线程，直到达到挂起计数器的限制。在此之后，第一个线程会定期挂起另一个线程，并检查对 NtSuspendThread 的调用是否继续失败并显示 STATUS\_SUSPEND\_COUNT\_EXCEEDED。如果没有，则该线程必须被外部挂起并恢复，这将使挂起计数器保持在 126，因此对 NtSuspendThread 的下一次调用将成功。如果没有得到这个漏洞代码，那么Roshtyak就会停止使用TerminateProcess。Secret Club在一篇博文中详细描述了这一技巧。我们相信这就是Roshtyak的作者得到这个技巧的原因。值得一提的是，Roshtyak只在Windows版本18323 (19H1)及以后的版本中使用了这种技术，因为在之前的版本中没有实现无文档记录的线程创建标志。

**间接注册表写入**

Roshtyak 执行许多可疑的注册表操作，例如，设置 RunOnce 项以实现持久性。由于可能会监控对此类密钥的修改，因此 Roshtyak 试图绕过监控。它首先生成一个随机注册表项名称，并使用 ZwRenameKey 将 RunOnce 项临时重命名为随机名称。重命名后，Roshtyak 会在临时密钥中添加一个新的持久性条目，然后最终将其重命名为 RunOnce。这种写入注册表的方法很容易被检测到，但它可能会绕过一些简单的基于挂钩的监控方法。

同样，Roshtyak 使用多种方法来释放文件。除了对 NtDeleteFile 的明显调用之外，Roshtyak 还可以通过在对 ZwSetInformationFile 的调用中设置 FileDispositionInformation 或 FileRenameInformation 来有效地释放文件。然而，与注册表修改方法不同的是，这似乎不是为了逃避检测而实现的。相反，如果对NtDelete文件的初始调用失败，Roshtyak将尝试这些替代方法。

**检查 VBAWarnings**

VBAWarnings 注册表值控制用户打开包含嵌入 VBA 宏的文档时 Microsoft Office 的行为方式。如果此值为 1，则意味着“启用所有宏”，则默认执行宏，甚至不需要任何用户交互。这是沙盒的常见设置，旨在自动触发恶意文档。另一方面，此设置对于普通用户来说并不常见，他们通常不会随意更改设置，使自己更容易受到攻击（至少他们中的大多数人不会）。因此，Roshtyak 使用此检查来区分沙箱和普通用户，如果 VBAWarnings 的值为 1，则拒绝进一步运行。有趣的是，这意味着无论出于何种原因以这种方式降低安全性的用户都不会受 Roshtyak 的影响。

**命令行清除**

Roshtyak 的核心是用非常可疑的命令行执行的，例如RUNDLL32.EXE SHELL32.DLL,ShellExec\_RunDLL REGSVR32.EXE -U /s "C:\Users\\AppData\Local\Temp\dpcw.etl."。这些命令行看起来不是特别合法，因此 Roshtyak 试图在执行期间隐藏它们。它通过清除从各种来源收集的命令行信息来做到这一点。它首先调用 GetCommandLineA 和 GetCommandLineW 并清除两个返回的字符串。然后它会尝试清除 PEB->ProcessParameters->CommandLine 指向的字符串（即使它指向一个已经被清除的字符串）。由于 Roshtyak 经常在 WoW64 下运行，它还调用 NtWow64QueryInformationProcess64 来获取指向 PEB64 的指针，以清除通过遍历这个“第二个”PEB 获得的 ProcessParameters->CommandLine。虽然清除命令行可能是为了让 Roshtyak 看起来更合法，但完全清除任何命令行也是极不寻常的。 Red Canary 研究人员在他们的博客文章中注意到了这一点，他们提出了一种基于这些可疑的空命令行的检测方法。

![11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221019/1666160751380694.png "1666160751380694.png")

Roshtyak 的核心流程，如 Process Explorer 所示，注意可疑的空命令行。

**附加技巧**

除了到目前为止描述的技巧之外，Roshtyak 还使用了许多其他恶意软件中常见的不太复杂的技巧。这些包括：

使用 ThreadHideFromDebugger 隐藏线程，并使用 NtQueryInformationThread 验证线程是否真的被隐藏了；

在 ntdll 中修补 DbgBreakPoint；

使用 GetLastInputInfo 检测用户活动情况；

检查来自 PEB 的字段（BeingDebugged、NtGlobalFlag）；

检查来自 KUSER\_SHARED\_DATA 的字段（KdDebuggerEnabled、ActiveProcessorCount、NumberOfPhysicalPages）；

检查所有正在运行的进程的名称（一些通过哈希比较，一些通过模式比较，一些通过字符分布比较）；

哈希所有加载模块的名称，并根据硬编码的黑名单检查它们；

验证主进程名不需要太长时间，而且与沙盒中使用的已知名称不匹配；

使用cpuid指令检查hypervisor信息和处理器标志；

使用没有纪录的 COM 接口；

根据硬编码的黑名单检查用户名和计算机名；

正在检查是否存在已知的沙盒诱饵文件；

根据硬编码的黑名单检查自己的适配器的 MAC 地址；

检查 ARP 表中的 MAC 地址（使用 GetBestRoute 填充它并使用 GetIpNetTable 来检查它）；

使用 ProcessDebugObjectHandle、ProcessDebugFlags 和 ProcessDebugPort 调用 ZwQueryInformationProcess；

检查显示设备的 DeviceId（使用 EnumDisplayDevices）；

检查 \\.\PhysicalDrive0 的 ProductId（使用 IOCTL\_STORAGE\_QUERY\_PROPERTY）；

检查虚拟硬盘（使用 NtQuerySystemInformation 和 SystemVhdBootInformation）；

检查原始 SMBIOS 固件表（使用 NtQuerySystemInformation 和 SystemFirmwareTableInformation）；

设置 Defender 排除项（针对路径和进程）；

删除与恶意软件使用的进程名相关的IFEO注册表项；

**混淆**

我们展示了许多旨在防止 Roshtyak 在不良执行环境中触发的反分析技巧。就单个技巧来说，都很容易被修复或识别。分析 Roshtyak 之所以困难的原因，是所有这些技巧被组合起来了，同时被重度混淆和多层包装。这使得静态研究反分析技巧并弄清楚如何通过所有检查以使 Roshtyak 自行解包变得非常困难。此外，即使是主要的有效载荷也收到了相同的混淆，这意味着静态分析 Roshtyak 的核心功能也需要大量的去混淆。

接下来，我们将介绍Roshtyak使用的主要混淆技术。

![13.1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221019/1666160762615369.png "1666160762615369.png")

来自Roshtyak的随机代码片段，可以看到，这种混淆使得Hex-Rays反编译器的原始输出实际上难以理解

**control flow flatterning(控制流平坦化)**

控制流扁平化是 Roshtyak 采用的最引人注目的混淆技巧之一。它以一种不同寻常的方式实现，使 Roshtyak 函数的控制流图具有独特的外观（见下文）。控制流扁平化的目标是混淆各个代码块之间的控制流关系。

控制流由一个 32 位控制变量引导，该变量跟踪执行状态，识别要执行的代码块。这个控制变量在每个函数开始时被初始化以引用起始代码块（通常是一个 nop 块）。然后在每个代码块的末尾修改控制变量，以识别应该执行的下一个代码块。修改是使用一些算术指令执行的，例如 add、sub 或 xor。

有一个调度程序使用控制变量将执行路由到正确的代码块中。这个调度程序由if/else块组成，这些块被循环链接到一个循环中。每个调度程序块接受控制变量，并使用算术指令屏蔽它，以检查是否应该将执行路由到它所保护的代码块中。有趣的是，从代码块到调度程序循环有多个入口点，使控制流图在 IDA 中呈现锯齿状外观。

使用包含 imul 指令的特殊代码块执行分支。它依赖于前一个块来计算分支标志。使用 imul 指令将该分支标志与一个随机常数相乘，并将结果与新的控制变量相加、替换或异或。这意味着在分支块之后，控制变量将识别两个可能的后续代码块中的一个，这取决于为分支标志计算的值。

![14.1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221019/1666160785242034.png "1666160785242034.png")

用控制流扁平化混淆的函数的控制流图

**函数激活项**

Roshtyak 的混淆函数需要一个额外的参数，我们称之为激活密钥。此激活密钥用于解密所有局部常量、字符串、变量等。如果使用漏洞的激活密钥调用函数，则解密会产生垃圾明文，这很可能导致Roshtyak陷入控制流分配器内部的无限循环中。这是因为调度程序使用的所有常量（控...
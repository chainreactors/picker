---
title: 网络协议模糊测试之旅——剖析MicrosoftIMAP客户端协议（下）
url: https://www.4hou.com/posts/8YOg
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2023-05-29
fetch_date: 2025-10-04T11:37:04.594814
---

# 网络协议模糊测试之旅——剖析MicrosoftIMAP客户端协议（下）

网络协议模糊测试之旅——剖析MicrosoftIMAP客户端协议（下） - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 网络协议模糊测试之旅——剖析MicrosoftIMAP客户端协议（下）

luochicun
[技术](https://www.4hou.com/category/technology)
2023-05-28 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)153573

收藏

导语：在本博客中，我们记录了审核和模糊测试MicrosoftInternet消息访问协议(IMAP)客户端协议的过程。本文，我们会详细介绍实践中遇到的一些挑战。

上一篇文章主要讲的是理论上的可能性，本文，我们会详细介绍实践中遇到的一些挑战。

**挑战1：可扩展存储引擎缓存清理**

WindowsMail利用统一的存储数据库将电子邮件数据（例如电子邮件地址和消息）保存在本地文件系统中。此数据库位于路径%LOCALAPPDATA%\Comms\UnistoreDB\store.vol。可扩展存储引擎(ESENT)使用专有的二进制格式为其数据结构构建数据库。这种二进制格式可以使用像ESEDatabaseView这样的工具来查看。使用ESENT的好处是它有一个缓存机制，可以最大限度地高性能访问数据。这种缓存机制是我们遇到的第一个障碍。

在后台，缓存缓冲区根据系统服务启动UserDataService时初始化的ESENT参数JET\_paramVerPageSize分配一个大小。默认缓存大小为0x2000，必须与页面大小粒度对齐。但是，这在WTF模糊器模块的上下文中成为一个问题。

问题是，当缓存缓冲区已满时，ESENT将工作项排队以清除缓存缓冲区。工作项是程序可以提交给线程池的子例程。工作项是异步执行的，并且调度程序系统会根据系统资源的可用性发出警报。遗憾的是，这是一个复杂的机制，WTF模糊器无法模拟。因此，fuzzer模块将在上下文切换时退出，当它碰到线程API（例如，KERNELBASE!QueueUserWorkItem）时退出。让模糊器超越上下文切换是对CPU时间的浪费。这就是为什么你应该在每个WTF模糊器模块中找到类似的断点处理程序的原因：

![133.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220807/1659865659786106.png "1659865659786106.png")

在上下文切换期间停止模糊器模块的断点处理程序

当发生意外的上下文切换时，开发者必须了解它发生的原因并实施解决方法以达到所需的代码路径。这可以通过分析WTF模糊器生成并由0vercl0k的Symbolizer后处理的覆盖跟踪日志来完成。下图显示了在上下文切换处停止的覆盖跟踪日志示例：

![14.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220807/1659865691100903.png "1659865691100903.png")

通过Symbolizer生成的覆盖跟踪日志示例

这里没有复杂的技巧来分析覆盖跟踪日志。我们只需进行回溯以定位模块或函数转换（即modA!funcnameX->modB!funcnameY）以发现上下文切换的原因。通常，我们将模块文件加载到IDAPro中以统计研究和理解底层代码。有时，执行静态代码分析可能还不够，尤其是当代码包含IDAPro无法自动解析的虚函数调用时。相反，你可以使用TTD来解析虚函数调用或探索执行的代码。

![15.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220807/1659865729175357.png "1659865729175357.png")

覆盖跟踪日志揭示了上下文切换的原因

上图显示ESENT!CGPTaskManager::ErrTMPost+0xd4调用KERNELBASE!QueueUserWorkItem，本质上是在线程池队列中放置一个可执行线程，而ESENT!CGPTaskManager::ErrTMPost是从ESENT!VER::VERSignalCleanup派生的。在深入分析该函数后，在TTD的帮助下，我们确定了ESENT!VER::VERSignalCleanup的目的是将当前缓冲区缓存大小与通过JET\_paramVerPageSize指定的默认缓存大小进行比较。它调用QueueUserWorkItem来执行缓存清理线程，ESENT！VER::VERIRCECleanProc，如果当前缓存缓冲区被填满，最终会导致上下文切换。因此，我们面临的挑战是找到一种方法来防止触发清理程序。

我们首先想到的是，最简单的解决方法是将默认缓存大小从0x2000增加到其最大大小0x10000。从技术上讲，数据库引擎的配置设置可以根据MSDN文档使用API JetSetSystemParameter进行调整。但是，我们无法通过使用外部程序来更改驻留在隔离的系统服务进程空间中的设置来实现这一目标。

![16.1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220807/1659865811963064.png "1659865811963064.png")

![16.2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220807/1659865836107272.png "1659865836107272.png")

![16.3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220807/1659865853166653.png "1659865853166653.png")

清单3：显示系统主机服务集数据库引擎配置设置的调用堆栈

查看清单3中的调用堆栈，然后我们考虑通过劫持UserDataService并在数据库引擎配置设置发生之前在ESENT.dll中的特定偏移处调整硬编码的默认缓存大小来解决此问题。我们决定试一试。

劫持服务DLL很简单。我们可以定位到目标服务注册表项，定义如下：

HKEY\_LOCAL\_MACHINE\SYSTEM\CurrentControlSet\Services\UserDataSvc\Parameters

ServiceDLL=%SystemRoot%\System32\userdataservice.dll

当ServiceDLL条目调整为我们自定义的服务DLL文件时，它将变成：

HKEY\_LOCAL\_MACHINE\SYSTEM\CurrentControlSet\Services\UserDataSvc\Parameters

ServiceDLL=c:\userdatasvc\UserDataSvcProxy.dll

自定义服务DLL导出两个强制模型函数，ServiceMain和SvchostPushServiceGlobals。修改上述注册表项后，系统服务将加载自定义服务DLL，该DLL执行模型ServiceMain函数。模型ServiceMain函数将在ESENT.dll中的特定偏移处修补JET\_paramVerPageSize。打补丁后，它会将执行传递给UserDataService导出的初始ServiceMain函数，并像往常一样继续它的初始例程。

![17.1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220807/1659865866811246.png "1659865866811246.png")

![17.2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220807/1659865881152265.png "1659865881152265.png")

![17.3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220807/1659865890140757.png "1659865890140757.png")

清单4：显示自定义服务DLL劫持UserDataService的调用堆栈

设置完后，我们针对新的快照映像运行模糊器模块，并加载了自定义服务DLL，该DLL应将缓存大小调整为0x10000。但不幸的是，它仍然hits=清理过程。因此，我们需要找出另一种解决方法。

我们查看了ESENT!VER::VERSignalCleanup，但意识到该函数不返回调用函数的值，这使我们相信函数例程并不关心这个清理过程是否成功执行。最重要的是，它似乎不跟踪任何可能导致ESENT中意外行为的全局状态或事件。考虑到这些，我们决定跳过这个清理过程，只需设置一个断点来模拟这个函数，即在命中断点时立即返回到调用者，如下图所示：

![18.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220807/1659865925558669.png "1659865925558669.png")

跳过ESENT!VER::VERSignalCleanup以避免上下文切换

这样，我们的模糊器模块可以在清理过程之外执行，而无需点击上下文切换！但是，需要注意的是，这可能会大大增加快照映像内的内存使用量。但这不应该给我们带来任何潜在的问题，因为一旦完成模糊测试迭代，快照映像就会恢复到其原始状态。换句话说，悬空缓存缓冲区可以忽略不计。

**挑战2：加载一个卸载的DLL并执行分页内存**

如果你熟悉软件模拟，就会明白让模拟器的行为像本机计算机一样是不可能的。同样的事情也适用于WTF模糊器。当出现这种限制时，我们需要找到解决方法。但根据面临的限制的复杂性，有些解决办法可能很简单，有些解决办法就像调整快照映像一样简单。

我们遇到的下一个问题是，当WTF尝试从文件系统加载已卸载的DLL文件时会发生上下文切换。同样，我们通过分析覆盖跟踪日志和一些代码片段确定了问题的根本原因，如下图所示。从覆盖跟踪日志中，我们可以看出CoCreateInstanceAPI是从MCCSEngineShared!Decode2047Header+0xfe调用的。此COMAPI负责加载在类ID中指定的COM对象，在本例中为CLSID\_CMultiLanguage。此类ID对应于C:\WINDOWS\SYSTEM32\mlang.dll。

![19.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220807/1659866004233507.png "1659866004233507.png")

加载卸载的DLL文件

有了这些信息，我们手动将COM对象DLL注入目标进程，将映像转储为新的快照，并对其进行测试。结果，它超越了MCCSEngineShared!Decode2047Header，但我们遇到了另一个问题。

![20.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220807/1659866013373244.png "1659866013373244.png")

由内存访问错误导致的另一个上下文切换

查看上图中的覆盖跟踪日志后，我们意识到发生了从用户模式exsmime!CMimeReader::FindBoundary到内核模式nt!MiUserFault的异常代码执行转换。我们的经验表明，模拟器可能已命中保留的内存地址或换出到页面文件的内存地址。这是一种常见的Windows内存管理机制，出于性能原因将不经常使用的内存保留在页面文件中。为了验证这一点，我们使用WinDbg调试器加载内存转储并检查在exsmime!CMimeReader::FindBoundary+0x4f处指定的代码，如图10所示。

![21.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220807/1659866021904148.png "1659866021904148.png")

调用虚函数时的内存访问错误

它从虚函数表中调用虚函数，但虚函数的目的地exsmime!CHdrContentType::value是通过TTD快照确定的，如下图所示：

![22.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220807/1659866029182663.png "1659866029182663.png")

使用TTD确定虚函数的目的地址

为了解决这个内存访问问题，我们运行了lockmem实用程序，它确保指定进程的每个可用内存区域都将保留在内存中，因此它不会被写入页面文件，这会在访问时引发页面错误。为获得最佳结果，始终建议执行完整的内存转储，以避免其他不可预见的内存访问问题。当你对内核模式组件进行模糊测试时，此技巧特别有用。

**挑战3： 注册表挂钩**

Windows注册表是一个分层数据库，用于存储Windows操作系统和应用程序的低级设置。该数据库将注册表配置单元的信息保存在文件系统中。也就是说，注册表操作在一定程度上涉及到I/O操作。由于模拟器都不支持这些操作，因此我们需要复制这些功能。

在撰写本文时，WTF提供了一个fshook子系统来复制I/O操作，但不提供注册表挂钩（此后是reghook）。显然，我们不能为reghook重用fshook，因为它们是不同的API，但我们可以将fshook中的一些实现调整为reghook。例如，我们可以重用fshook和RegHandleTable\_t类中的伪句柄算法。fshook和reghook之间的关键区别在于如何模拟预期内容（(即用于I/O操作的文件内容和用于注册表操作的注册表数据）。例如，对于reghook，如果注册表操作要打开一个新句柄，则调用RegOpenKeyAPI来打开特定注册表项的句柄。其对应的钩子处理程序将API调用重定向到本机。换句话说，本机设备将尝试使用本机API打开注册表项，如果注册表项存在，则返回句柄。打开的句柄对本机有效，但对作为内存转储的客户机无效。因此，应该生成一个伪句柄并将其映射到本机句柄。

重申一下，当前的regook实现是不完整的，并且没有针对其他目标进行全面测试。但是扩展现有的regook以支持其他注册表API应该相当简单。

**奇特的RFC822.SIZE案例**

在部署和分发模糊器模块后，我们开始收集模糊器收集的有趣输入。从那里，我们开始生成代码跟踪，并使用Lighthouse插件将其加载到IDAPro中以进行进一步分析。

我们首先对InternetMail.dll进行逆向工程，以找到操纵变异输入的代码，特别是模糊器提供给目标的ResponseParams。此时，FETCH响应中的一个有趣的ResponseParams，RFC822.SIZE，立即引起了我们的注意。经查，RFC822.SIZE是FETCH命令的属性之一，表示消息的大小。简单地说，它告诉电子邮件客户端到达客户端的整个电子邮件消息的大小，包括电子邮件标题、内容和附件。

有趣的是...
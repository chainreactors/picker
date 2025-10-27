---
title: 基于云的恶意软件传播：GuLoader的技术迭代过程
url: https://www.4hou.com/posts/yAXg
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2023-06-22
fetch_date: 2025-10-04T11:44:49.436161
---

# 基于云的恶意软件传播：GuLoader的技术迭代过程

基于云的恶意软件传播：GuLoader的技术迭代过程 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 基于云的恶意软件传播：GuLoader的技术迭代过程

xiaohui
[技术](https://www.4hou.com/category/technology)
2023-06-21 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)124094

收藏

导语：GuLoader是一个著名的基于shellcode的下载程序，已被用于大量攻击，主要用于传输各类恶意软件。

![微信截图_20230603211328.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230621/1687312280114658.png "1685802322129646.png")

GuLoader又称CloudEyE，是一种 Visual Basic Script (VBS) 下载程序，用于在受感染的计算机上传播远程访问木马，最早于2019年被首次发现。GuLoader是一个著名的基于shellcode的下载程序，已被用于大量攻击，主要用于传输各类恶意软件。GuLoader已经活跃了三年多，目前仍在进一步开发中。最新版本集成了新的反分析技术，这使得检测变得越来越困难。新的GuLoader样本在VirusTotal上接收零检测，确保其恶意有效负载也未被检测到。

GuLoader的有效负载是完全加密的，包括PE标头。这允许攻击者使用知名的公共云服务存储有效负载，绕过安全保护，并保持有效负载长时间可供下载。

早期版本的GuLoader是作为包含加密shellcode的VB6应用程序实现的。目前，最常见的版本是基于VBScript和NSIS安装程序。VBScript变体将shellcode存储在远程服务器上。

**GuLoader介绍**

“封装”和“加密”服务是专门为抵抗安全产品而设计的。GuLoader是攻击者用来逃避安全检测的最重要途径。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230621/1687312281193381.png "1685802437178632.png")

过去6个月内使用GuLoader的攻击次数

除了代码加密之外，GuLoader还利用了许多其他技术，包括反调试和沙盒逃避技术。GuLoader的一个显著特征是加密的有效负载被上传到远程服务器。潜在的攻击者会获得一个高度保护的基于shellcode的加载程序，该加载程序从远程服务器下载负载，然后解密并在内存中运行它，而不会将解密的数据释放到硬盘驱动器中。

尽管谷歌努力阻止GuLoader加密的恶意负载，但在大多数情况下，GuLoader仍然从谷歌硬盘下载负载。下图显示了GuLoader在过去一个月使用的不同托管服务的统计数据。

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230621/1687312281206522.png "1685802449146250.png")

GuLoader在2023年3月至4月期间使用的不同托管服务

有分析表明，GuLoader目前被用来传播以下恶意软件：

```
Formbook
XLoader
Remcos
404Keylogger
Lokibot
AgentTesla
NanoCore
NetWire
```

早期的GuLoader样本设法避免了安全产品的检测，但后来不同的安全解决方案都能够检测到它。然而，在网络安全供应商不断提高同时，GuLoader的开发人员也在继续改进他们的产品。

**技术细节**

GuLoader的早期版本是作为包含加密shellcode的VB6应用程序实现的。shellcode执行加载加密有效负载、解密和从内存启动它的主要功能。

目前，最常见的版本是基于VBScript和NSIS安装程序(Nullsoft Scriptable Install System)。

**VBScript变体**

在2022年底介绍的早期版本中，shellcode存储在VBScript中。

新版本的一个显著特点是加密的shellcode托管在云服务(通常是Google Drive)上。VBScript本身只包含一个小的混淆的PowerShell脚本和大量的垃圾代码。这使得GuLoader样本保持非常低的检测率。

以下是使用GuLoader的VBS变体的感染链示例：

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230621/1687312282193051.png "1685802463487376.png")

使用GuLoader的VBS变体的感染链

让我们考虑一个SHA256 5fcfdf0e241a0347f9ff9caa897649e7fe8f25757b39c61afddbe288202696d5的示例。在2023年3月3日上传到VirusTotal (VT)时，它从未被检测到：

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230621/1687312282829507.png "1685802480212882.png")

上传两天后，59家供应商中只有17家将此样本标记为恶意样本。

在撰写本文时，指定的样本上传到VT已有3周，下载GuLoader shellcode和下载恶意负载(Remcos)的url仍然很活跃：

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230621/1687312283100797.png "1685802496123444.png")

让我们来看看GuLoader VBScript的内部。它包含许多伪随机注释和一些无用的命令。清理之后，我们得到的代码是这样的：

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230621/1687312284206856.png "1685802511552157.png")

清理过的GuLoader vbscript

这段代码的目的是调用PowerShell解释器，并将“pa0”变量中收集的脚本代码作为参数传递给它。

如果我们在添加省略和连字符后查看“pa0”变量的内容，我们会得到以下脚本：

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230621/1687312285784485.png "1685802549675568.png")

GuLoader混淆了PowerShell脚本

我们看到这个新脚本包含函数“Gothites9”，它实现了从第二个字符开始以3的步长剪切传递的字符串。因此，命令“$Tjene0=Gothites9'OIUlEDiXSa'；”的结果是“IEX”。

字符串$Parrotb以相同的方式转换。从位置2开始，从该字符串中每隔三个字符获取一个字符串，该字符串是另一个PowerShell脚本：

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230621/1687312285153774.png "1685802563116367.png")

删除第一层混淆后的GuLoader PowerShell脚本

该脚本可以通过使用IEX命令(如果操作系统是32位)调用，也可以作为参数传递给从SysWOW64文件夹调用的PowerShell解释器(如果操作系统是64位)。这是因为GuLoader shellcode必须在32位进程中运行。

可以看到，脚本代码包含指向Google Drive的URL。

但是，生成的脚本仍然严重混淆。脚本以一个用于解码字符串的函数开始：

![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230621/1687312286149805.png "1685802617337405.png")

GuLoader PowerShell脚本中的编码字符串

有趣的是，嵌套脚本中的所有行都以编码形式存储，除了包含URL的行。

脚本去混淆后，我们得到以下代码：

![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230621/1687312286643958.png "1685802632664277.png")

GuLoader PowerShell脚本去混淆

现在我们可以看到，脚本分配了2个内存区域，将数据从链接下载到Google Drive，并将其保存到临时文件“%APPDATA%\Umig.For”中。接下来，使用BASE64对下载文件的内容进行解码。解码数据的前654个字节被释放在第一个存储区域（本例中为“$Gamme2483”），其余的被释放在第二个存储区域中（本例为“$Nulstille”）。前654个字节包含一个混淆的shellcode，它旨在解密第二个复制区域，其中包含加密形式的shellcode的主要部分。

通过使用CallWindowsProc回调函数将控制权转移到解密器，该函数还接收加密shellcode的地址和NtProtectVirtualMemory函数的地址作为参数。

**基于NSIS安装程序的变体**

与VBS变体不同，基于NSIS的样本包含GuLoader shellcode，尽管是以加密的形式。这允许安全研究人员在沙盒中运行示例并查看GuLoader的行为，即使沙盒没有连接到互联网。静态分析NSIS脚本和加密shellcode也是可能的。

在上传到VirusTotal后，此类样本现在可以被检测到。

![11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230621/1687312287462103.png "1685802645910091.png")

基于NSIS安装程序的GuLoader变体的检测率

我们不会详细描述这种变体，因为在 GuLoader: The NSIS Vantage Point一文中已经对其进行了分析。

**GuLoader shellcode**

NSIS和VBS变体都使用相同版本的shellcode。与以前的GuLoader版本一样，shellcode实现了大量的反分析技术：

沙盒逃避技术包括：

扫描内存中与vm相关的字符串；

使用CPUID指令检查虚拟化环境位是否开启；

使用RDTSC结合CPUID 测量时间；

搜索QEMU相关文件：C:\Program files\QEMU ga\QEMU-ga.exe和C:\Program files\qga\qga.exe；

使用EnumWindows API函数统计Windows的数量；

使用EnumDeviceDrivers API函数检查是否存在与vm相关的驱动程序；

使用MsiEnumProductsA和MsiGetProductInfoA枚举已安装的软件；

反调试技术：

挂钩函数DbgBreakPoint 和DbgUiRemoveBreakIn ，以防止调试器附加；

从使用ThreadHideFromDebugger调用NtSetInformationThread函数的调试器中隐藏主线程ThreadInformation类值；

了解了GuLoader shellcode所使用的技术，在动态分析过程中使用调试器可以很容易地绕过它们。然而，在新版本中，我们遇到了一种使调试和静态分析都非常困难的技术。

**一种新的反分析技术**

从2022年底开始，GuLoader shellcode使用了一种新的反分析技术，它通过故意抛出大量异常并在将控制权转移到动态计算地址的向量异常处理程序中处理它们来打破代码执行的正常流程。

为了抛出异常，代码使用int3指令。可以实现一个脚本，将int3指令自动替换为跳转到正确地址的指令：

![12.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230621/1687312288166305.png "1685802660190481.png")

用jmp指令替换int3指令

该技术在《恶意软件分析：GuLoader剖析揭示新的反分析技术和代码注入冗余》一文中首次被公开。然而，在新版本中，这项技术得到了改进。shellcode开始使用三种不同的模式来抛出异常并中断正常的代码执行流程。

访问无效内存地址导致访问冲突

这种模式非常简单。首先，作为数学运算的结果，其中一个寄存器被设置为零值。然后shellcode尝试将数据写入由该寄存器寻址的内存：

![13.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230621/1687312288140588.png "1685802673513287.png")

访问无效内存地址引发访问违规异常

导致访问违规异常(0xC0000005)。该异常在GuLoader中由注册的VEH处理，该VEH计算新地址以继续执行shellcode。所使用的数字和导致计算零值的数学运算总是不同的。

**设置陷阱标志以引发单步异常**

GuLoader使用以下指令组合来设置EFALGS寄存器中的TF：

![14.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230621/1687312289130062.png "1685802703136064.png")

设置陷阱标志以引发单步异常

乍一看，这段代码中发生了什么并不清楚。然而，如果我们计算寄存器EDI中的值，则得到值0x100。接下来的几个指令的组合旨在推动EFLAGS并将TF (陷阱标志)位设置为“1”。然后，将堆栈中修改后的值设置回EFLAGS寄存器。

当在EFLAGS寄存器中设置了Trap标志但未附加调试器时，处理器会在执行下一条指令后生成单步异常（0x80000004）。在GuLoader中，注册的VEH在这种情况下被调用。但是，如果附加了调试器，则不会调用GuLoader的VEH，并且执行路径错误。

GuLoader shellcode中的代码块总是不同的，可以使用寄存器的各种组合。在无效内存地址的情况下，使用的数字和导致在EFLAGS寄存器中计算值0x100来设置TF的数学运算总是不同的。

**使用int3引发断点异常**

使用int3作为指令进行反分析技术已经在以前版本的GuLoader中实现。然而，它仍然被用于GuLoadershellcode的各个部分。当CPU在没有调试器的情况下遇到int3指令时，它会生成断点异常（0x80000003），并调用已注册的VEH。但是，如果附加了调试器，则控制将转移到调试器的中断处理程序，该中断处理程序通常会暂停程序的执行。int3指令后面通常是随机字节，这些字节会破坏shellcode的正常执行：

...
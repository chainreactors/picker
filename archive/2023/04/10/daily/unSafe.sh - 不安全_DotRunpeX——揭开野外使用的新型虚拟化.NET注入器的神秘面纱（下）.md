---
title: DotRunpeX——揭开野外使用的新型虚拟化.NET注入器的神秘面纱（下）
url: https://buaq.net/go-157767.html
source: unSafe.sh - 不安全
date: 2023-04-10
fetch_date: 2025-10-04T11:29:30.101300
---

# DotRunpeX——揭开野外使用的新型虚拟化.NET注入器的神秘面纱（下）

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/d706940b957ca35dc002ee68950c00dd.jpg)

DotRunpeX——揭开野外使用的新型虚拟化.NET注入器的神秘面纱（下）

导语：本研究的主要主题是对两个版本的DotRunpeX注入器进行深入分析，对比它们之间的相似之处，并介绍用于分析新版本的DotRunpeX的PoC技术，因为它是由自定义版本的KoiVM .NET pr
*2023-4-9 12:0:0
Author: [www.4hou.com(查看原文)](/jump-157767.htm)
阅读量:21
收藏*

---

导语：本研究的主要主题是对两个版本的DotRunpeX注入器进行深入分析，对比它们之间的相似之处，并介绍用于分析新版本的DotRunpeX的PoC技术，因为它是由自定义版本的KoiVM .NET protector.虚拟化传播的。

![微信截图_20230319161953.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230319/1679225376385362.png "1679225376385362.png")

**新版DotRunpeX完整的技术分析**

为了分析dotRunpeX的新版本，使用了示例SHA256:“44a11146173db0663a23787bffbb120f3955bc33e60e73ecc798953e9b34b2f2”。这个示例是一个用.NET编写的64位可执行文件“.exe”，受KoiVM保护。版本信息与旧版本的DotRunpeX的情况相同，并且在CPR分析的所有示例中都是一致的。CPR可以再次注意到ProductName – RunpeX.Stub.Framework 。

![33.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230319/1679225407276730.png "1679225407276730.png")

新DotRunpeX版本的信息

在dnSpyEx中打开示例并导出入口点函数\_sb()方法后，CPR可以立即确认此新版本的DotRunpeX受到KoiVM虚拟程序的保护。尽管大多数IL代码都是虚拟化的，但CPR仍然可以发现P/Invoke定义的CreateProcess方法的调用，该方法以某种方式创建一个处于挂钩状态的进程——通常用于代码注入技术“Process Hollowing”。

![34.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230319/1679225422163176.png "1679225422163176.png")

创建挂钩的流程作为Process Hollowing技术的一部分

在进一步研究了.NET元数据(特别是ImplMap表)中剩余的内容之后，找出了定义为P/Invoke并很可能被这个示例使用的其他方法，CPR得到了比旧版本dotRunpeX更令人兴奋的发现。显然，该示例不仅执行代码注入，还执行加载和与驱动程序通信。

![35.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230319/1679225448984720.png "1679225448984720.png")

ImplMap表——DotRunpeX的新版本

CPR立即注意到的下一个是使用了与旧版本相同的资源名——BIDEN\_HARRIS\_PERFECT\_ASSHOLE——它包含要注入的加密有效负载。资源名称在CPR分析的所有样本中都是一致的。很明显，解密例程隐藏在代码虚拟化之后，但通过猜测，他们可以得到一个简单的异或解密例程，它使用了一个表示开发者秘密愿望的密码——I\_LOVE\_HENTAIU2。

![36.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230319/1679225551212378.png "1679225551212378.png")

使用密码“I\_LOVE\_HENTAIU2”对.NET资源进行简单异或解密

不过，由于DotRunpeX仍处于开发阶段，并添加了新功能，使用该注入器的最新示例改变了解密方案（不再是简单的XOR），从而省略了嵌入式有效负载的静态提取。

如上所述，IL代码受到KoiVM虚拟程序的保护，因此为了继续分析，CPR需要想出一些方法来处理受保护的代码，并在合理的时间内从中获得一些有意义的东西。首先，CPR想到的是使用一个名为OldRod的公开开源KoiVM去虚拟程序。这个工具完全适用于KoiVM的普通版本。它的开发方式甚至要优于KoiVM原始版本的一些简单修改（例如VMEntry类中方法的签名修改或默认#Koi流名称的修改）。

不过，CPR正在处理一个自定义版本的KoiVM，它以一种不那么容易被发现的方式修改了保护程序。KoiVM的原始实现定义了119个用于虚拟化代码的常量变量。这些常量用于定义寄存器、标志、操作码等。这些常量的指定值用于正确执行虚拟化代码，也是去虚拟化过程所需的。

![37.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230319/1679225569850354.png "1679225569850354.png")

KoiVM的原始实现定义了119个常量

在使用普通版本的KoiVM时，在constants类内已编译的、受保护的示例中，生成的常量以完全相同的顺序显示为字段，并带有升序标记值。在编译后的二进制文件中，常量及其对应的标记的顺序是OldRod所依赖的。

![38.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230319/1679225582160969.png "1679225582160969.png")

OldRod源代码——常量的自动检测

尽管OldRod工具是一个非常好用的工具，并且可以在通过配置文件(——config选项)提供自定义常量映射时处理常量的自定义顺序，但找出这些常量的正确映射并不像听起来那么简单。有时，当一个常量的顺序是手工修改时，通过分析它们在代码中的使用来正确地映射它们可能并不难。但更糟糕的是，它们以一种非常有效的方式被打乱，使得正确的映射非常困难，以至于认为这种方法无法在合理的时间内获得一些结果。

![39.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230319/1679225595179102.png "1679225595179102.png")

OldRod源代码——常量的自动检测

通过精确的代码分析和通过适当的处理程序映射常量期间的一些困难时刻，CPR还是能够完全去虚拟化代码。不过，就算有了完全去虚拟化的代码，但还是一个不能完全运行的.NET程序集，它仍然被ConfuserEx混淆器混淆了。

下图是与驱动程序例程相关的完全去虚拟化和去混淆的代码。

驱动程序装载/卸载：

![40.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230319/1679225610394166.png "1679225610394166.png")

负责加载/卸载驱动程序的虚拟化和非虚拟化代码

与procexp设备的通信：

![41.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230319/1679225622919247.png "1679225622919247.png")

负责与procexp设备通信的去虚拟化和去混淆的代码

为了讲解方便，本文不讨论去虚拟化和去混淆的过程。

通常，当不可能在合理的时间内对代码进行反虚拟化时，CPR仍然没有其他选择。第一个选项(处理虚拟化代码时非常常见的方法)是使用调试器、DBI(动态二进制检测)、挂钩和WIN API跟踪进行动态分析。当CPR处理dotnet代码时，另一种方法可能是使用一些来自.NET内部世界的知识进行PoC。CPR决定将这两种方法结合起来，从而开发出了一种非常有效的新工具。

为了获得更多关于代码功能的信息，CPR从使用x64dbg的动态分析方法开始。正如CPR之前指出的，包含P/Invoke定义的方法的ImplMap表似乎是在调试器中设置断点的一个很好的起点。通过自动解析P/Invoke定义的方法并将其转换为x64dbg脚本，CPR开发了第一个工具，称为“ImplMap2x64dbg”。

**ImplMap2x64dbg**

使用dnfile模块正确解析.NET可执行文件及其元数据的Python脚本，此工具创建一个x64dbg脚本，用于在.NET可执行文件的已定义ImplMap (P/Invoke)方法上设置断点。

![42.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230319/1679225632198786.png "1679225632198786.png")

使用" ImplMap2x64dbg "处理DotRunpeX示例将生成x64dbg脚本：

![43.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230319/1679225644133211.png "1679225644133211.png")

CPR主要关注某些WIN/NT API，如CreateProcessW、NtWriteVirtualMemory、CreateFileA、CreateFileW、NtLoadDriver、NtQuerySystemInformation和DeviceIoControl，因为它们是与驱动程序和进程注入例程相关的有趣API。

我们能看到的第一个有趣的WIN API调用是CreateFileW，它用于在路径C:\Users\XXX\AppData\Local\Temp\Иисус.sys中创建一个文件。

![44.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230319/1679225699355260.png "1679225699355260.png")

CreateFileW用于创建文件“Иисус.sys”

如果CPR检查创建的文件Иисус.sys（俄语翻译为“jesus.sys”），就会立即发现它是一个有效的进程资源管理器驱动程序，版本为16.43。

![45.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230319/1679225710922267.png "1679225710922267.png")

创建的文件“Иисус.sys”是有效的进程资源管理器驱动程序，版本16.43

CPR可以看到负责加载此驱动程序的例程NtLoadDriver，其中参数指向DriverServiceName–\Registry\Machine\System\CurrentControlSet\Services\TaskKill，它指定了驱动程序注册表项的路径。

![46.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230319/1679225723132620.png "1679225723132620.png")

NtLoadDriver用于通过其关联的注册表项加载procexp驱动程序

![47.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230319/1679225734105991.png "1679225734105991.png")

驱动程序注册表项“\registry\Machine\System\CurrentControlSet\Services\TaskKill”的内容

挂钩到进程资源管理器设备如下。

![48.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230319/1679225743198704.png "1679225743198704.png")

获取进程资源管理器设备的句柄

DotRunpeX 逃避杀毒软件技术之一是在进程资源管理器驱动程序（procexp.sys）的帮助下阻止一个硬编码的反恶意软件服务列表。使用进程资源管理程序驱动程序背后的原因是，反恶意软件服务通常作为受保护的进程运行，更具体地说是作为PPL，以避免由恶意活动引起的系统保护失效。有可能滥用procexp驱动程序的易受攻击版本来关闭受保护进程的对象句柄。一旦关闭了足够多的句柄，特定的受保护进程将被终止。CPR分析的所有示例都滥用了该驱动程序的16.43版本，这也是最新的易受该技术攻击的版本。

为了获得有关对象句柄的信息，DotRunpeX使用具有指定SystemInformationClass 0x10的NT API NtQuerySystemInformation，该SystemInformationClass0x10指向未记录的结构[SYSTEM\_HANDLE\_information]。通过这种方式，它可以找到属于受保护进程的所有句柄。

![49.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230319/1679225784595319.png "1679225784595319.png")

NtQuerySystemInformation用于获取未记录的结构SYSTEM\_HANDLE\_INFORMATION

为了处理受保护进程的对象句柄，DotRunpeX使用WIN API DeviceIoControl将IOCTL直接发送给易受攻击的procexp驱动程序。IOCTL“2201288708”（IOCTL\_CLOSE\_HANDLE）在RDX寄存器中，处理此请求的procexp驱动程序例程负责关闭指定进程的某些对象句柄，无论指定进程是否受到保护。一旦关闭了足够多的对象句柄，反恶意软件服务就会被终止。

![50.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230319/1679225802123204.png "1679225802123204.png")

DeviceIoControl用于发送IOCTL“2201288708”以关闭受保护进程的对象句柄

我们还可以看到寄存器R8 (lpInBuffer)指向关闭对象句柄所需的数据。该数据结构可以定义如下：

![51.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230319/1679225813280867.png "1679225813280867.png")

让我们比较一下DotRunpeX示例使用的procexp驱动程序版本（版本16.43，2021.8.17编译）和最新版本的proceexp驱动程序（版本17.02，2022.11010编译）。CPR可以立即发现添加的修复代码，该代码负责禁用关闭受保护进程的对象句柄的可能性。

![52.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230319/1679225823184978.png "1679225823184978.png")

16.43与17.02版本进程资源管理器驱动程序之间的比较

这种使用进程资源管理器驱动程序关闭受保护流程的对象句柄的技术可以随时上网查找到，并且是名为Backstab的开源项目的一部分，进程资源管理器驱动程序17.0以上的版本已经被修复。

在阻止特定的受保护进程后，Process Hollowing将使用WIN API CreateProcessW以挂钩状态启动进程（在本例中为C:\Windows\Microsoft.NET\Framework\v4.0.30319\InstallUtil.exe），并直接使用NT API NtWriteVirtualMemory将DotRunpeX的嵌入式有效负载写入新创建的远程进程。

事实证明，通过一种专注于本机层和WIN/NT API的某些使用的动态分析方法，CPR对这种可用于自动化和大规模处理的虚拟化dotnet注入器获得了一些有趣的发现：

每个DotRunpeX示例都有一个要注入的特定恶意软件家族的嵌入式有效负载；

每个DotRunpeX示例都有一个嵌入式procexp驱动程序来终止受保护的进程；

虚拟化代码背后很可能隐藏着某种配置，它指定了process Hollowing的目标进程、要阻止的受保护进程列表（反恶意软件服务），以及其他有趣的可配置内容；

除此之外，CPR可以利用.NET内部世界的知识来实现一些自动化。当谈论dotnet时，CPR可以立即想到由.NET运行时管理的代码。越来越多的事情正在被管理，其中特别重要的就是所谓的“内存管理”。dotnet中的内存类型有堆栈和.NET堆。在网络世界中，CPR不需要为内存分配/释放而烦恼，因为这些例程是由.NET运行时和...
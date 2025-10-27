---
title: 以 Roshtyak 后门为例介绍恶意软件的自保护、逃逸等技巧（一）
url: https://buaq.net/go-138376.html
source: unSafe.sh - 不安全
date: 2022-12-04
fetch_date: 2025-10-04T00:28:29.939301
---

# 以 Roshtyak 后门为例介绍恶意软件的自保护、逃逸等技巧（一）

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

![](https://8aqnet.cdn.bcebos.com/5c5b4828eb10ce17252c88a4b2ce1341.jpg)

以 Roshtyak 后门为例介绍恶意软件的自保护、逃逸等技巧（一）

导语：本文就以 Roshtyak 后门为例
*2022-12-3 12:0:0
Author: [www.4hou.com(查看原文)](/jump-138376.htm)
阅读量:26
收藏*

---

导语：本文就以 Roshtyak 后门为例介绍恶意软件的自保护、杀软逃逸技巧。Raspberry Robin于2021年9月首次被发现，通过受感染的USB设备传播。

恶意软件开发者通常会使用各种技巧使分析工作变得更加困难。这些技巧包括使逆向工程复杂化的混淆技巧、逃避沙箱的反沙箱技巧、绕过静态检测的打包技巧等。多年来，各种恶意软件在野外使用的无数欺骗手段都记录了这一点。然而，尽管有许多可用的技巧，但在典型的恶意软件中很少实现这些技巧。

本文就以 Roshtyak 后门为例介绍恶意软件的自保护、杀软逃逸技巧。Raspberry Robin于2021年9月首次被发现，通过受感染的USB设备传播。本文的主题是一个我们称为 Roshtyak 的后门，它不是典型的恶意软件。 Roshtyak 反分析设计很多。有些是众所周知的，有些是我们从未见过的。从技巧角度来看，Roshtyak 的自我保护非常有趣。 Roshtyak 属于我们见过的反分析最成功的的恶意软件之一。我们希望通过发布我们对恶意软件及其保护技巧的研究和分析，帮助其他研究人员识别和应对类似的技巧，并强化他们的分析环境，使他们对所描述的绕过技巧加强防护。

Roshtyak 是 Raspberry Robin 使用的 DLL 后门，一种通过受感染的可移动驱动器传播的蠕虫，Raspberry Robin今年非常流行。

Red Canary 的研究人员于 2022 年 5 月发布了对 Raspberry Robin 的首次分析。6 月，赛门铁克发布了一份报告，描述了一次挖矿/剪贴板劫持操作，据报道，这让攻击者至少赚了170万美元。赛门铁克没有将恶意操作与 Raspberry Robin 联系起来。尽管如此，根据我们的分析，其幕后组织是Raspberry Robin。该评估基于我们分析中观察到的 C&C 重叠、以及很多与其他恶意软件相似性。Cybereason、微软和思科在 2022 年 7 月/8 月发布了进一步的报告。微软报告说，Raspberry Robin 感染导致了 DEV-0243（又名 Evil Corp）勒索行为。虽然我们无法确认此连接。尽管如此，我们仍然有理由相信挖矿软件有效载荷并不是 Raspberry Robin 感染被货币化的唯一方式。最近的其他报道也暗示了 Raspberry Robin 和 Evil Corp 之间可能存在的联系。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221019/1666160263938668.png "1666160263938668.png")

尽管发表了如此多的报道，但关于 Raspberry Robin 仍有许多未知数。恶意软件背后的最终目标是什么？谁负责运营 Raspberry Robin ？它是如何变得如此流行的？不幸的是，我们没有所有这些问题的答案。但是，我们可以回答我们多次看到的一个重要问题：在高度混淆的 DLL（或我们称之为 Roshtyak）中隐藏了哪些功能？为了回答这个问题，我们对 Roshtyak 示例进行了完全逆向工程。

**Roshtyak介绍**

Roshtyak 包含多达 14 层保护层，每层都经过高度混淆并服务于特定目的。一些工件表明这些层最初是 PE 文件，但被转换为只有以前的层知道如何解密和加载的自定义加密结构。许多反调试器、反沙盒、反虚拟机和反仿真器检查遍布各个层。如果其中一项检查成功检测到分析环境，那么将采取四个操作中的一个。

恶意软件调用自己的TerminateProcess，以避免显示任何进一步的恶意行为，并保持后续层的加密。

Roshtyak是故意撞车的。这与终止自身具有相同的效果，但由于Roshtyak的混淆特性，可能无法立即清楚崩溃是有意的还是因为一个漏洞。

恶意软件故意进入无限循环。由于循环本身位于混淆代码中并且跨越数千条指令，因此可能很难确定循环是否在为攻击做准备。

最有趣的情况是恶意软件通过解包和加载虚假有效负载来绕过成功检查，这发生在第八层，它加载了几十个反分析检查。每个检查的结果都用于修改全局变量的值。在第 8 层的数据段加密了两个有效载荷。真正的第 9 层和伪造的有效载荷，只有在执行所有检查后，全局变量与预期值匹配时，才会解密真正的第九层。如果检测到分析环境，则全局变量的值将与预期值不同，从而导致 Roshtyak 解包并执行虚假有效负载。

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221019/1666160272208590.png "1666160272208590.png")

Roshtyak 的混淆导致即使是相对简单的函数也变得很大。如果想在合理的时间范围内对其进行逆向工程，就需要一些自定义的反混淆工具。

虚假有效载荷是一个 BroAssist（又名 BrowserAssistant）广告软件示例。我们认为，这个虚假的有效载荷旨在误导恶意软件分析师认为该示例没有实际情况那么有趣。当逆向工程师专注于快速解包示例时，整个示例可能看起来“只是”一个混淆的广告软件（而且是一个非常古老的广告软件），这可能会导致分析师对深入挖掘失去兴趣。事实证明，这些虚假的有效载荷恶作剧可能非常有效。从下面的屏幕截图中可以看出，它欺骗了至少一名研究人员，该研究人员漏洞地将 Raspberry Robin 蠕虫归因于虚假的 BrowserAssistant 有效载荷。

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221019/1666160283108177.png "1666160283108177.png")

这表明，鉴于 Roshtyak 的设计和复杂性，犯这样的漏洞是多么容易。

**复杂的混淆技巧**

现在让我们直接详细介绍 Roshtyak 采用的一些有趣的规避技巧。

**段寄存器**

在执行的早期，Roshtyak 更喜欢使用不需要调用任何导入函数的检查。如果其中一项检查成功，则示例可以安静地退出，而不会生成任何可疑的 API 调用。下面是 Roshtyak 检查 gs 段寄存器行为的示例。该检查被设计为隐形的，周围的垃圾指令使其容易被忽视。

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221019/1666160294125477.png "1666160294125477.png")

只有带下划线的指令是有用的

此检查背后的第一个想法是检测单个执行。在上面的代码片段之前，cx 的值被初始化为 2。在弹出ecx指令之后，Roshtyak检查cx是否仍然等于2。这将是预期的行为，因为该值应该在正常情况下通过堆栈和 gs 寄存器传播。但是，单个事件会重置 gs 选择器的值，这会导致最后弹出一个不同的值到 ecx 中。

但这项检查还有更多内容。作为上述两个 push/pop 对的副作用，gs 的值暂时更改为 2。在此检查之后，Roshtyak 进入一个循环，计算迭代次数，直到 gs 的值不再是 2。 gs 选择器在线程上下文切换后也会被重置，因此循环本质上是计算迭代次数，直到发生上下文切换。 Roshtyak 多次重复此过程，求出结果的平均值，并检查它是否属于裸机执行环境的合理范围。如果示例在虚拟机管理程序或模拟器中运行，则平均迭代次数可能会超出此范围，这使 Roshtyak 能够检测到不需要的执行环境。

Roshtyak 还检查 cs 段寄存器的值是 0x1b 还是 0x23。此时，0x1b 是在原生 x86 Windows 上运行时的预期值，而 0x23 是在 WoW64 中运行时的预期值。

**通过随机 ntdll gadget注入 APC**

Roshtyak从独立的进程中执行一些功能。例如，当它与它的C&C服务器通信时，它会生成一个新的看似无害的进程，如regsvr32.exe。通过使用共享段，它将通信模块注入到新进程的地址空间中。被注入的模块通过APC注入执行，使用的是NtQueueApcThreadEx。

有趣的是，ApcRoutine 参数（标记要安排执行的目标例程）并不指向注入模块的入口点。相反，它指向 ntdll 中看似随机的地址。仔细一看，我们发现这个地址不是随机选择的，而是 Roshtyak 扫描了 ntdll 的代码段来查找pop r32;retgadget(不包括pop，因为旋转堆栈是不可取的)，并随机选择一个作为ApcRoutine。

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221019/1666160306120124.png "1666160306120124.png")

随机弹出 r32； ret gadget 用作 APC 注入的入口点

查看 ApcRoutine 的调用约定可以理解发生了什么。 pop 指令使堆栈指针指向 NtQueueApcThreadEx 的 SystemArgument1 参数，因此 ret 指令有效地跳转到 SystemArgument1 指向的任何位置。这意味着通过滥用这个gadget，Roshtyak 可以将 SystemArgument1 作为 APC 注入的入口点。这混淆了控制流并使 NtQueueApcThreadEx 调用看起来更合法。如果有人挂钩此函数并检查 ApcRoutine 参数，它指向 ntdll 代码段的事实可能足以让他们相信该调用不是恶意的。

**检查组合写入内存的读/写性能**

在接下来的检查中，Roshtyak 分配一个带有 PAGE\_WRITECOMBINE 标志的大内存缓冲区。该标志应该修改缓存行为以优化顺序写入性能，不过这是以读取性能和可能的内存排序为代价的。 Roshtyak 使用它来检测它是否在物理设备上运行。它进行了一项实验，首先写入分配的缓冲区，然后从分配的缓冲区中读取，同时使用一个单独的线程作为计数器来测量读写性能。该实验重复 32 次，只有在大多数情况下写性能至少是读性能的6倍时，才会通过检查。如果检查失败，Roshtyak就会故意选择漏洞的RC4密钥，从而导致无法正确地解密下一层。

**隐藏shellcode**

有趣的是，注入的 shellcode 也被隐藏了。当 Roshtyak 准备代码注入时，它首先创建一个大段并将其作为 PAGE\_READWRITE 映射到当前进程中。然后，它用随机数据填充该段，并将 shellcode 放置在随机数据内的随机偏移处。由于 shellcode 只是一个相对较小的加载器，后面跟着看起来是随机的打包数据，所以整个段看起来像随机数据。

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221019/1666160316137912.png "1666160316137912.png")

共享区段内字节的直方图。注意，它看起来几乎是随机的，最可疑的符号是空字节的轻微过度表示。

然后该段从当前进程中取消映射，并映射到目标进程中，在目标进程中使用上述 APC 注入技巧执行该段。添加随机数据是为了隐藏 shellcode 的存在。仅从目标进程的内存转储来看，该段可能看起来充满了随机数据并且不包含任何有效的可执行代码。即使有人怀疑该段中间某处的实际有效代码，也不容易找到它的确切位置。

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221019/1666160329148628.png "1666160329148628.png")

共享段中 shellcode 的开始。可能很难确定确切的起始地址，因为它通常是从奇数bt指令开始的。

**Ret2Kernel32**

Roshtyak特别注意清理自己的攻击痕迹。每当不再需要某个字符串或某段内存时，Roshtyak 就会清除或释放它，以试图清除尽可能多的证据。 Roshtyak 的图层也是如此。每当一层完成其工作时，它就会在将执行传递到下一层之前进行自我释放。但是，该层不能简单直接地自我释放。如果它在当前正在执行的内存区域上调用 VirtualFree，整个进程将会崩溃。

因此，Roshtyak 通过在层转换期间执行的 ROP 链来释放层以避免此问题。当一个层即将退出时，它会在堆栈上构造一个 ROP 链并返回其中。下面可以看到这样一个 ROP 链的示例。该链首先返回 VirtualFree 和 UnmapViewOfFile 以释放上一层的内存。然后，它返回到下一层。下一层的返回地址设置为 RtlExitUserThread，以保障执行安全。

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221019/1666160340564142.png "1666160340564142.png")

一个简单的 ROP 链，由 VirtualFree -> UnmapViewOfFile -> next layer -> RtlExitUserThread 组成。

**MulDiv漏洞**

MulDiv是一个由kernel32.dll导出的函数，它接受三个32位有符号整数作为参数。它将前两个参数相乘，将乘法结果除以第三个参数，并返回最后的结果四舍五入到最接近的整数。虽然这可能看起来是一个足够简单的函数，但在微软的实现中有一个古老的符号扩展漏洞。这个漏洞现在被认为是一个功能，可能永远不会被修复。

Roshtyak 知道该漏洞并通过调用 MulDiv(1, 0x80000000, 0x80000000) 来测试它的存在。在真实的 Windows 设备上，这会触发漏洞并且 MulDiv 漏洞地返回 2，即使正确的返回值应该是 1，因为 (1 \* -2147483648) / -2147483648 = 1。这允许 Roshtyak 检测不复制漏洞的模拟器.例如，这成功检测到 Wine，有趣的是，它包含一个不同的漏洞，这使得上述调用返回 0。

**篡改存储在堆栈中的返回地址**

还有一些用来混淆函数调用的技巧。如上一节所示，Roshtyak喜欢使用ret指令调用函数。下一个技巧与此类似，因为它也操作堆栈，因此可以使用 ret 指令跳转到所需的地址。

为了实现这一点，Roshtyak 扫描当前线程的堆栈，寻找指向前一层代码段的指针，与其他层不同，这一层没有使用 ROP 链技巧释放。它用它想要调用的地址替换所有这些指针。然后它让代码多次返回，直到 ret 指令遇到一个被劫持的指针，将执行重定向到所需的地址。

本文翻译自：https://decoded.avast.io/janvojtesek/raspberry-robins-roshtyak-a-little-lesson-in-trickery/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

![](https://www.4hou.com/captcha/flat?WOODGX0H)

#### 你可能感兴趣的

* [![](https://img.4hou.com/images/1290aea80e20e22ba9d08e0199cfcfab.png)

  以 Roshtyak 后门为例介绍恶意软件的自保护、逃逸等技巧（一）](https://www.4hou.com/posts/kM0r)
* [![](https://img.4hou.com/images/3764cd8a6d5ca3a3651a7fc37b051d63.jpg)

  DarkKomet synaptics 病毒应急响应事件复盘](https://www.4hou.com/posts/MBv1)
* [![](https://img.4hou.com/images/WX20221201-100422@2x.png)

  Warzone RAT恶意软件通过不断调试.NET部署多阶段攻击](https://www.4hou.com/posts/2JBA)
* [![](https://img.4hou.com/images/1668666974646856.png)

  SaaS蔓延：含义、危害、现状及缓解方案](https://www.4hou.com/posts/XVzo)
* [![](https://img.4hou.com/images/d3ca6f9f3b6a265a045ec46084e2b341.jpeg)

  如何恢复网络令牌](https://www.4hou.com/posts/QL8M)
* [![](https://img.4hou.com/images/WX20221128-095238@2x.png)

  Windows App 运行控制机制 Smart App Control 的内部安全架构分析（下）](https://www.4...
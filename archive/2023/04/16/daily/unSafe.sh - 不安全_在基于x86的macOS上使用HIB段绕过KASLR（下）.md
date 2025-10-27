---
title: 在基于x86的macOS上使用HIB段绕过KASLR（下）
url: https://buaq.net/go-158792.html
source: unSafe.sh - 不安全
date: 2023-04-16
fetch_date: 2025-10-04T11:31:37.484548
---

# 在基于x86的macOS上使用HIB段绕过KASLR（下）

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

![](https://8aqnet.cdn.bcebos.com/fc5f659b021bace0480e39aa409ff1ea.jpg)

在基于x86的macOS上使用HIB段绕过KASLR（下）

导语：本文我们将介绍XNU(苹果macOS
*2023-4-15 12:0:0
Author: [www.4hou.com(查看原文)](/jump-158792.htm)
阅读量:18
收藏*

---

导语：本文我们将介绍XNU(苹果macOS使用的内核)的实现细节，它可以消除许多内核漏洞中对专用信息泄露漏洞的需要。

**确定当前CPU**

虽然这不是一个真正的“技巧”，但为了匹配dblmap中的正确结构地址，有必要识别当前CPU编号。每个内核都有自己的GDT(在dblmap中)，因此可以使用sgdt指令来确定当前的CPU。然后可以循环，直到看到“正确的”GDT。

需要执行此操作的一个示例是在使用有效负载填充 LDT 之后，任务需要在正确的内核上执行，然后有效负载才会出现在 dblmap 中该内核的 LDT 中。

**使用 dblmap 简化实际的漏洞利用**

为了提供一个演示 dblmap 实用性的具体示例，我们将展示如何通过使用 dblmap 而不是其过度复杂的多个泄漏原语构造来大大简化我们的 Pwn2Own 2021 内核漏洞利用。 GitHub 上提供了此变体的源代码以及完整的 Safari 到内核链的其余部分。

bug/exploit 的完整细节在之前的一篇文章中已经介绍过：1.我们对已释放的内核缓冲区进行任意写入操作；2.没有内核信息泄露。

我们可以使用包含 OSObject 指针的新 OSArray 的后备存储轻松回收已释放的内核缓冲区。这些是 C++ 对象，因此破坏数组中的内核数据指针以指向假对象应该足以通过虚拟调用劫持控制流。

多亏了dblmap，我们可以将已知的数据放在已知的内核地址。这意味着我们可以在LDT中构造伪内核对象及其虚函数表，而不需要真正的内核文本或数据泄漏。

![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220821/1661059691810227.png "1661059691810227.png")

为了简单起见，我们选择CPU 0作为“正确”的CPU，它的LDT对应于内核中的master\_ldt符号。

现在我们已经能够劫持内核控制流，我们需要研究调用时的寄存器状态，以及如何将其转换为对dblmap函数的有用调用。

**被劫持的内核调用网站的参数控制**

在这种情况下，将生成一个损坏的OSArray的副本，我们首先能够在OSArray::initWithObjects()中劫持控件，它被传递给包含损坏对象的备份存储。遍历损坏的支持存储，并为每个对象调用taggedRetain()虚函数。

调用的第一个参数自然是this指针，它将指向LDT中的假对象；

第二个参数是“tag” ，它将是&OSCollection::gMetaClass；

没有明确的第三个参数，但我们仍然可以查看函数是如何编译的，并确定调用网站的rdx（根据调用约定的第三个参数）中可能包含的内容。

它恰好在count++操作期间使用，这意味着它将等于假对象在已损坏数组中的索引加1。换句话说，如果破坏数组中第i个索引的对象，对应调用的第三个参数将是i+1。这让我们可以控制第三个参数，只要它是一个相对较小的非零整数。

由于第二个参数 &OSCollection::gMetaClass 是 OSMetaClass 的一个实例，一个 C++ 对象，它的第一个字段是虚函数表。使用第三个参数8调用memcpy()会相对简单，它会将虚函数表复制到LDT中。然后可以使用i386\_get\_ldt()读出虚函数表，这将导致文本泄漏。

然后，我们可以使用OSSerializer::serialize()将带有受控制的this参数的调用转换为带有3个受控制参数的任意函数调用(假设可以满足LDT限制)。这可能足以获得足够的泄漏，以消除对LDT的依赖，并从那里继续利用。

**在 LDT 中设置任意位**

hibernate\_page\_bitset() 函数的签名是：

![11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220821/1661059718182373.png "1661059718182373.png")

第二个布尔参数set决定函数是设置位还是清除位。在我们的例子中，它将为真，因为&OSCollection::gMetaClass是非零的。

第三个参数page指定要设置或清除的位。如前所述，我们可以将其设为任何小的非零整数。

第一个参数是LDT中的假对象，它的结构如下:

![12.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220821/1661059728204453.png "1661059728204453.png")

简而言之，它是一个可变大小的位图数组，其中每个位图都与一个位索引范围相关联。

由于我们控制了伪结构和位索引，因此调用这个函数允许我们在LDT中设置任意位。

应该注意的是，dblmap 中 LDT 的内存内容是短暂的，如果当前任务（进程/线程）被抢占，它们就变得无关紧要。

当一个新任务开始在CPU上执行时，如果它有一个LDT，它将被复制到dblmap中，覆盖现有的已损坏的内容。同样，当重新调度被抢占的任务(具有先前损坏的LDT)时，复制到dblmap中的LDT来自堆分配结构，从而有效地消除了损坏。

在本文的示例中，你基本上可以忽略这个细节，因为失败不会有任何惩罚或崩溃，如果需要的话，我们可以重新执行被劫持的bitset调用。另外，OSArray::initWithObjects()在一个循环中遍历已损坏的后台存储，这意味着我们可以劫持数组中每个插槽的虚拟调用，并在一次传递中多次调用bitset函数。我们不需要每次设置一个位时都来回切换到用户空间，这意味着经过的时间更少，我们的任务被抢占的机会也就越低。

另一种选择是破坏 LDT 中的前 3 个描述符之一。这些是硬编码的，不能用 i386\_set\_ldt() 修改：

![13.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220821/1661059740113710.png "1661059740113710.png")

由于它们预计不会更改，因此每次在 CPU 上执行新任务时不会重置这些条目。任何 dblmap 的 LDT（每个 CPU 一个）中对这 3 个描述符的任何损坏都将在抢占期间持续存在。

**构建调用门**

在LDT中设置比特听起来很强大，但我们实际上可以用它做什么？

请记住，有两种类型的描述符:用于内存区域的代码/数据描述符和系统描述符。LDT中唯一允许的系统描述符是调用门。正如英特尔手册所述:调用门有助于在不同权限级别之间进行程序控制的受控传输。

它们主要由3个方面定义：

1.访问门所需的权限级别；

2.目标代码段选择器；

3.目标入口点；

二进制格式：

![14.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220821/1661059749142443.png "1661059749142443.png")

当从用户空间（ring3）通过呼叫门进行远程呼叫时，大致会发生以下情况：

1.检查权限（调用门描述符的 DPL 字段必须为 3）；

2.目标代码段描述符的 DPL 字段成为新的权限级别；

3.使用新的权限级别从 TSS 中选择一个新的堆栈指针；

4.将旧的ss 和 rsp 推入新堆栈；

5.将旧的cs和rip推入新堆栈；

6.从调用门选择器和入口点设置cs和rip。

构造一个可以被ring3 (DPL为3)访问的调用门，并为64位内核代码(0x8)指定代码段选择器，这将允许我们对指定的任何地址执行远程调用，如ring0。

滥用调用门来利用内核漏洞之前已经被证明过，但是在 32 位 Windows 的上下文中，当时SMEP、SMAP和页表隔离并未受到关注。

**泄露kernel slide**

当我们触发远程调用时，Supervisor Mode Execution Prevention (SMEP)阻止我们跳转到用户空间中的可执行代码。页表仍然处于用户模式，其中唯一映射的内核空间页用于dblmap。这就留下了跳到\_\_HIB文本部分中的现有代码的唯一选项。

我们将远程调用指向ks\_64bit\_return()的中间，它包含以下指令序列:

![15.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220821/1661059764170864.png "1661059764170864.png")

请记住，我们拥有完全的寄存器控制(rsp除外，它将是内核堆栈)，因此对r15解引用的第一条指令将给我们一个任意的读原语。我们只需将r15适当地设置为要读取的地址，进行远程调用，在返回到用户空间时，r15将包含解除引用的数据。

这可能导致从dblmap中泄漏一个函数指针，从而暴露kernel slide。具体来说，我们可以从idt64\_hndl\_table0中泄漏ks\_dispatch()指针。

这里有一点需要注意的是，从远程调用返回通常是通过远返回指令 retf 完成的，而不是 iretq 中断返回。 堆栈布局将与预期略有不同：

![16.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220821/1661059775186302.png "1661059775186302.png")

rflags 将从旧的 rsp 中设置，而 rsp 将使用旧的 ss 填充，而 ss 将从之后发生在堆栈上的任何内容中填充。这意味着：

在进行远程调用之前，可以通过将RSP设置为Rflags值来“恢复”Rflags；

从旧的ss中设置RSP是没有问题的，我们可以自己恢复RSP；

加载到ss的堆栈上的下一个值将是一个内核指针，这将是一个无效的选择器，并将触发一个异常。然而，这个异常将发生在中断返回后的ring3中，所以我们可以简单地使用预期的Mach异常处理行为来捕获它。

可以使用thread\_set\_exception\_ports()来为EXC\_BAD\_ACCESS注册一个异常端口。我们生成一个线程来等待异常消息，然后用包含正确的ss选择器的消息内容来响应，从而允许远程调用线程继续。

**控制页表，控制一切**

kernel slide不仅显示内核基址的虚拟地址，而且还显示其物理地址。这为我们提供了CPU 0的LDT的物理地址，或者换句话说，就是受控数据的物理地址。

这为我们提供了一个非常强大的工具：如果我们重构调用门以跳转到mov cr3指令，我们将立即获得任意的ring0代码执行。

我们所需要做的就是确保我们正确地设置了我们的伪页表（驻留在 LDT 中）：

1.mov cr3后面指令的虚拟地址应该映射到传入LDT的shellcode的物理地址；

2.内核堆栈应该是可映射和可写的（对于 CPU 0，这是 \_\_HIB 段中的符号 master\_sstk）；

3.根据经验，这是不必要的，但是为了安全起见，应该映射GDT(对于CPU 0，符号master\_gdt)。

注意，这只适用于CPU 0，它的LDT静态分配在\_\_HIB段中。其他 CPU 的 LDT 从内核堆分配，虚拟别名插入到 dblmap 的页表中。这些堆分配的物理地址不能直接从kernel slide中推断出来。

**内核Shellcode**

由于对 LDT 描述符的限制，我们传入LDT的shellcode将由任意6字节的块组成。如果我们使用 2 个字节进行短跳转（EB + 偏移量），这会留下 4 个任意字节的块。

虽然理论上这已经结束了，但在“正常”页表状态下更容易获得不受限制的shellcode执行。为了实现这一目标，一个简单的解决方案是使用受限制的shellcode禁用SMEP和SMAP(它们只是CR4寄存器中的位)，然后返回到用户空间。然后，我们可以像以前一样触发一个被劫持的虚拟内核调用，但这一次跳转到用户空间中的任意shellcode。

一个小细节是每个CPU都有控制寄存器，所以只有在执行LDT shellcode的CPU上才会禁用SMEP和SMAP。

另一个实现细节是如何干净地返回到用户空间，这将需要恢复原始页表。我们通过让shellcode执行以下操作来实现：

1.从 dblmap 读取 cpshadows[i].cpu\_ucr3 到 rax；

2.修改堆栈以形成有效的 iretq 布局；

3.跳转到 ks\_64bit\_return() 执行 cr3 切换（来自 rax），然后执行 iretq；

我们介绍了 dblmap 如何大大降低 KASLR 的功效，提供几个有趣的内核调用目标、主机走私内核 shellcode 等。

本文翻译自：https://blog.ret2.io/2022/08/17/macos-dblmap-kernel-exploitation/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

![](https://www.4hou.com/captcha/flat?1FlHVKCB)

#### 你可能感兴趣的

* [![](https://img.4hou.com/images/2960a0e0b6ce6ae3e13497961092a24e.png)

  在基于x86的macOS上使用HIB段绕过KASLR（下）](https://www.4hou.com/posts/jJJR)
* [![](https://img.4hou.com/images/28904374-e683a822a78d8ffe.jpg)

  【技术原创】Java利用技巧——Jetty Servlet型内存马](https://www.4hou.com/posts/YXG2)
* [![](https://img.4hou.com/images/微信截图_20230412094032.png)

  在基于x86的macOS上使用HIB段绕过KASLR（上）](https://www.4hou.com/posts/gXXY)
* [![](https://img.4hou.com/images/微信图片_20230411132833.png)

  Nexus安卓木马分析报告](https://www.4hou.com/posts/m0Zp)
* [![](https://img.4hou.com/images/c808a4a9afca5f2de89bb29dc527ae81.png)

  以 SingPass 应用为例分析 iOS RASP 应用自保护的实现以及绕过方法（下）](https://www.4hou.com/posts/6Vy9)
* [![](https://img.4hou.com/images/b6ba67bb4b7e1d9c0a9c35a6ae8e976a.png)

  DotRunpeX——揭开野外使用的新型虚拟化.NET注入器的神秘面纱（下）](https://www.4hou.com/posts/17xj)

![]()

文章来源: https://www.4hou.com/posts/jJJR
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)
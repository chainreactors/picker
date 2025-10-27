---
title: 睡眠混淆绕过Windows CFG检测保护机制
url: https://mp.weixin.qq.com/s?__biz=MzUzMDUxNTE1Mw==&mid=2247500458&idx=1&sn=05dbf86a29362fde50890b3599c9c0b8&chksm=fa521714cd259e02f97dd60181f8d007f3fc36fbcb17ce5b7ca4efff6ef4f3be5377678c1e88&scene=58&subscene=0#rd
source: 山石网科安全技术研究院
date: 2023-03-23
fetch_date: 2025-10-04T10:23:23.545608
---

# 睡眠混淆绕过Windows CFG检测保护机制

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Gw8FuwXLJnSCjDJQ1pYlOsvmUzD9CH25sbRTeibqBStfDgxVesYHAC4WQzPmRkTQGM1exZf5O5arVeiam3V21SOQ/0?wx_fmt=jpeg)

# 睡眠混淆绕过Windows CFG检测保护机制

原创

x1a0

山石网科安全技术研究院

**0****1**

**CFG&kCFG‍‍‍‍‍‍‍‍**

# 控制流防护(CFG)及其在内核中的实现称为kCFG，是Microsoft的控制流完整性（CFI）版本。CFG的工作原理是检查在使用CFG编译的模块的应用程序内部的间接函数调用，此外，从Windows10 1703版本开始，Windows内核已使用kCFG进行编译，但是为了启用kCFG，需要启用VBS（基于虚拟化的安全）。

# 为了提高用户的效率，受CFG保护的间接调用使用位图来进行验证，其中一组位指示目标是否"有效"还是"无效"。如果目标进程中加载的模块中的函数的起始位置，则该目标被视为"有效"。这意味着位图代表整个进程地址空间，使用CFG编译的每个模块在位图中都有自己的一组位，具体取决于它在内存中的加载位置，如ASLR，Windows仅在每次引导时随机化地址空间，因此此位图通常在所有进程之间共享，从而节省大量内存。

通常，在非常高的级别上，间接用户模式函数调用被传递给一个guard\_check\_icall函数（或在其他情况下传递到guard\_dispatch\_icall）。然后该函数取消引用function\_guard\_check\_icall\_fptr并执行指向指针的跳转。该指针是指向函数LdrpValidateUserCallTargetES（或其他情况下的LdrpValidateUserCallTarget）的指针。

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSCjDJQ1pYlOsvmUzD9CH25HqfQHBbkkrTvYFmicibqBx1Vuyut8TRRla6k39JWdkLuq38IsMmLpR9A/640?wx_fmt=png)

执行一系列按位操作和汇编函数，结果是检查位图来确定间接函数调用中的函数是否是位图中的有效函数，无效的函数将导致进程终止。

kCFG有一个非常类似的实现，间接函数调用由kCFG检查，最值得注意的是，这打破了[nt!HalDispatchTable+0x8]的原语，漏洞利用人员和研究人员通过调用nt!KeQueryIntervalProfile，在64位系统上对[nt!HalDispatchTable+0x8]进行间接调用，在内核的上下文中执行代码。

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSCjDJQ1pYlOsvmUzD9CH25WRwPfGBD3jdsW5scsDZGI8qKIPGaQPmGD10olbCxyDy1b5X3txrQqg/640?wx_fmt=png)

kCFG使用了和CFG略有不同的修改，即位图被存储在变量nt!guard\_icall\_bitmap内，从外，nt!\_guard\_dispatch\_icall启动了验证目标的例程，不需要其他函数调用。

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSCjDJQ1pYlOsvmUzD9CH25hiclQ4jsPNRhxfPjwrkMlhlCFiaLPr6BeXZkpPOLylPcVS4H5SBldcoQ/640?wx_fmt=png)

CFG缓解了在漏洞开发生命周期的某个时刻，一个函数指针可能被覆盖，来指向一个不同的函数指针，这可能对漏洞利用人员有利（如VirtualProtect）。

CFG是一种前向边缘CFI缓解，这意味着它不考虑ret指令，这是一种后向边缘情况，由于CFG不检查返回地址，CFG可以通过利用信息泄露来进行绕过，这可能会使用解析线程环境块（TEB）等操作泄露堆栈，利用这些知识，就有可能在堆栈上覆盖一个函数的返回地址，从而达到恶意的目的。

后面还有一些CFG的一些不足之处，模块利用导入地址表（IAT）来进行导入，如WindowsAPI函数，这些IAT表本质上是特定模块内的虚拟地址，指向WindowsAPI函数。

IAT默认是只读的，一般不能修改，由于其只读状态，Microsoft认为这些函数是"安全的"，这意味着CFG/kCFG并不保护这些函数，如果漏洞利用者能够修改，或在IAT中添加一个恶意条目，就有可能调用一个用户定义的指针。

此外，漏洞开发人员可以利用额外的操作系统功能来执行代码，根据设计，CFG/kCFG只验证一个函数是否从位图指示的位置开始，而不是验证一个函数是否是它所声称的，如果能够在CFG/kCFG位图中找到更多标记为有效的函数，就有可能用另一个函数的指针覆盖一个函数的指针，以"代理"代码执行，例如，这可能会导致类型混淆攻击，即一个不同的的函数正在用原来预期的参数和对象运行。

kCFG只有在启用VBS时才会启用，kCFG的一个有趣特点是，即使VBS没有被启用，kCFG的调度函数和例程仍然存在，函数调用仍然通过它们传递，无论是否启用VBS，kCFG都会对虚拟地址的"高"位进行逐位检查，以确定一个地址是否是符号扩展的（也被称为内核模式地址），如果检测到一个用户模式地址，无论HVCI是否被启动，kCFG都会导致KERNEL\_SECURITY\_CHECK\_FAILURE的错误检查，这是防止内核模式代码调用用户模式代码的一种缓解措施，这也是一种绕过DEP的潜在技术。

**0****2‍**

**分析&实现‍‍‍‍‍‍‍‍**

恶意软件使用的"睡眠混淆"技术，睡眠混淆的目标是通过在睡眠时隐藏在读/写内存空间中来保护恶意软件不被内存扫描发现，这也是有效的，因为内存扫描是资源密集型的，因此通常只针对可执行区域进行内存扫描。

睡眠混淆的实现使用CreateTimerQueueTimer设置了异步的计时器，每个都是一个接一个的执行，并做了下面的工作：

·将恶意软件的可执行内存区域设置为读/写

·加密内存区域

·等待一个特定的时间段

·解密内存区域

·将内存设置为读/执行

这一切都是因为CreateTimerQueueTimer使用一个回调例程，在每个定时器完成后执行一个给定的函数，回调例程发生在恶意软件的内存空间之外，因此即使内存被设置为读/写，也可以被执行。

如果编译并运行了带有CreateTimerQueueTimer的程序在没有开CFG的前提下会正常运行，如果在编译时启用了CFG（/guard:cf），并运行的话，将会触发CFG。

这是因为CreateTimerQueueTimer指向的回调例程是NtContinue，它在一个特殊的函数列表中，在启用CFG时不能间接调用，在这种情况下，是由我们的定时器触发的调用。由于现在恶意软件很少在自己的进程中运行，几乎都是被注入或加载到一个"正常"的进程中，而这些进程大多在编译时启用了CFG，但是在这里我们发现微软似乎给我们留了一线生机。

来自MSDN：[SetProcessValidCallTargets]为CFG提供了有效的间接调用目标的列表，并指定是否应该标记为有效。

CFG实际不是为了阻止在这里所讨论的攻击类型而建立的，而是为了通过使Use-After-Free和ROP链更加困难来阻止漏洞利用的，因此，如果处于"正常"的代码代码执行情况下，很容易采取给定的内存位置将其设置为有效目标，将此函数添加到项目中并启动启动项目。

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSCjDJQ1pYlOsvmUzD9CH25lFdDgVyACKIpnic4NManBPPHWVl3FBibzXicSJIuaAhusHyV6FwOLrQ7Q/640?wx_fmt=png)

通过逆向分析KernelBase，让我们看看SetProcessalidCallTargets做了什么。

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSCjDJQ1pYlOsvmUzD9CH25Uo5nHfVzDiasno3m6ATQzfiawRrqPJF6xfPF1oHtic7nPm39T9A0EVI9Q/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSCjDJQ1pYlOsvmUzD9CH25kwJrYqqMfOIEC42Pe9uSmQC2NOokQFNPt4FkVovUCWTvs6DdbHsTMQ/640?wx_fmt=png)

在SetProcessValidCallTarget的内部只是简单的调用了SetProcessValidCallTargetsSection函数，在SetProcessValidCallTargetsSection内部则是调用了NtSetInformationVirtualMemory函数，通过分析这是一个系统调用，系统调用号为0x19E。这里SetProcessValidCallTarget需要五个参数，x64调用会将前四个参数传递给寄存器RCX、RDX、R8和R9，最后一个参数则是放入堆栈中。

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSCjDJQ1pYlOsvmUzD9CH25lsEDCIbibf3iaQqDlb8ZXpWbDjo9dicznuCiaUlmZMVSNy1ZSuPWcicCDrQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSCjDJQ1pYlOsvmUzD9CH25jtccWq72HEnTgdSLhmYglgsiap9hAuia0pf4K4b75AxTjLwEI2I8jsgw/640?wx_fmt=png)

在这里，我们看到RCX是0XFFFFFFFFFFFF，在这种情况下，它代表了当前进程的句柄。RDX指向0x00007FF96372D000，是ntdll.dll的基址，也就是我们正在修改的DLL。R8是0x0000000000080000，是ntdll中可执行区域的大小。R9是0x0000000000000001，我们要修改的内存位置的数量。

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSCjDJQ1pYlOsvmUzD9CH25DicBbsuKRTM7glVzA0GyoO100Rk1zQkMLiblgyia9DR3slImDhmNkx5ibQ/640?wx_fmt=png)

我们现在需要弄清楚CFG\_CALL\_TARGET\_INFO结构是如何设置和存储的。

首先，值为0x790的RCX被移到RAX，然后RAX被推到RSP+0x48的栈中。这是我们的CFG\_CALL\_TARGET\_INFO结构中的第一个值，即到NtContinue的偏移量。

接下来，0x1被推到RSP +0x50的堆栈中。 0x1是CFG\_CALL\_TARGET\_VALID标志的值，我们把它作为第二个值传入。

最后，一个指向结构开头的指针，RSP+0x48被移到RAX，然后作为RSP+0x20推送到堆栈。这是x64中传递给函数的第五个参数的标准位置。指针指向内存位置0x00000071110FF678，我们需要记住这个位置，因为后面会出现。

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSCjDJQ1pYlOsvmUzD9CH25LeUQp3m9z3gChSBYV6jaG9nkMW85amLV5KTCTSf2lTMC2SJc23NibHQ/640?wx_fmt=png)

截图中是NtSetInformationVirtualMemory的必要参数。由于我们得到的是一个无效参数的错误，让我们通过整个调用来看看syscall上的寄存器和堆栈是什么样的。

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSCjDJQ1pYlOsvmUzD9CH25aZxhe1DTP70icg5hJWhfllZKgP0QVDBsEbic4QkXwltaTcd51gcTaT2A/640?wx_fmt=png)

RCX表示的是本地进程句柄。RDX是0x2，与VmCfgCallTargetInformation的VIRTUAL\_MEMORY\_INFORMATION\_CLASS枚举匹配。R8是0x1，是我们要修改的内存条目数，R9是0x00000071110FF570，这是一个指向MEMORY\_RANGE\_ENTRY结构的内存指针，有两个条目，从我们之前的参数看应该很熟悉。 首先是ntdll的基址，位于0x00007FF96372D000。 第二个是我们之前作为第三个参数传递给SetProcessValidCallTargets的可执行区域的大小。

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSCjDJQ1pYlOsvmUzD9CH25DqbKkYAGiaJOPTWjBbTVUjmTKDqwsFxqWrfBqQm1NvLo6oyhxekYFCQ/640?wx_fmt=png)

让我们看一下堆栈，在RSP+0x20处，也就是我们基于堆栈的NtSetInformationVirtualMemory参数的开始，我们看到两个条目，这与现有的NtSetInformationVirtualMemory文档中的最后两个参数相匹配。 第一个堆栈参数是一个指向内存区域的指针，0x00007FF961489E80，MSDN说这是一个变量缓冲区，取决于被查询的信息类；第二个是缓冲区的大小。

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSCjDJQ1pYlOsvmUzD9CH2544cUJ2zicsCibbKfnYOmlfpMA3vf6DDEsgOib059RFGCjKGGiawY3VnAzA/640?wx_fmt=png)

让我们去看看第五个参数所指向的内存位置，0x00000071110FF580，看看它存了什么。

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSCjDJQ1pYlOsvmUzD9CH2569zHIBfydba31Z452MgABxunPS6bpJE7G2ck0LrEr0eoHWdQmb2LwQ/640?wx_fmt=png)

这是我们需要弄清的新结构在内存中的位置。 首先，我们有0x1，可以认为它指的是所传递的偏移量的数量。 第二个值，0x00000071110FF5E8，似乎是一个指向另一个内存位置的指针，目前被设置为零。第三个值，0x00000071110FF678，也是一个指针。这个应该很熟悉，因为它是一个指针，指向之前为我们的CFG\_CALL\_TARGET\_INFO结构预留的内存，我们将其传递给SetProcessValidCallTargets。这意味着这将是我们新结构中的第三个值。 最后，我们有16个字节的0，让我们跨过系统调用，看看这些值是否有变化。

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSCjDJQ1pYlOsvmUzD9CH25DxUcRCZqret7OC9cVHcHckDzOXdsDHYyoUYiaIYZwL6diaibj6ibooHeiag/640?wx_fmt=png)

唯一的变化是位于0x00000071110FF5E8的第二个参数的值，它从0变成了1。这表明它是一个指向数值的指针

这里就是我们的新结构：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSCjDJQ1pYlOsvmUzD9CH25R03C3L5xurqqdHFrjZN2xM9mFtxTecpU5Jm6jygrwhjk5bxqB1ZCmg/640?wx_fmt=png)

这里是我们的新函数，将一个内存位置标记为对CFG有效。

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSCjDJQ1pYlOsvmUzD9CH25rNvhe7b0tMeGv0EOW3PibcBMylW4nxwFibTXhSEROGlyT9IsNNtmicS2Q/640?wx_fmt=png)

最后，让我们看看它是否有效呢。

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSCjDJQ1pYlOsvmUzD9CH25Y4fibOic7Dl0L7y3wfmL2icGAWJUZewOIsr8pkR7vJKXWvlw9fNWkJ2mw/640?wx_fmt=png)

参考链接：

https://docs.microsoft.com/en-us/windows/win32/api/memoryapi/nf-memoryapi-setprocessvalidcalltargets

https://docs.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwsetinformationvirtualmemory

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSZmibNONzibea8WkcAFcdQcXicIYgWuvOtR8HqlqJ68Avib679FBGHYqxRibldppr6etXJxxWRrlBToiaw/0?wx_fmt=png)

山石网科安全技术研究院

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSZmibNONzibea8WkcAFcdQcXicIYgWuvOtR8HqlqJ68Avib679FBGHYqxRibldppr6etXJxxWRrlBToiaw/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过
---
title: 使用伪造对象绕过Intel CET
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247552359&idx=3&sn=68f39f97b781ffd24ce5765cf170d5f4&chksm=e915dd5dde62544be36df51303adc9dea02565c5a9946260e9da2cfda8e91a48c6061273c748&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2022-10-19
fetch_date: 2025-10-03T20:16:49.844774
---

# 使用伪造对象绕过Intel CET

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ic0PRaz05OScZQR3ytItW78ThWEDv0qS4gPCg6nPu1eCYG7gdnjNbibCQLXojBJibWtvW2UrpcGYfag/0?wx_fmt=jpeg)

# 使用伪造对象绕过Intel CET

xiaohui

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ic0PRaz05OScZQR3ytItW78sia4RruMcwib4meDeOjdJ2VXfE4tnKY7M6DY9JNJXHGibCoWfww3xeBiaA/640?wx_fmt=png)

虽然数据执行保护（DEP）旨在阻止来自特定内存区域的纯代码注入攻击，但道高一尺魔高一丈，攻击者已经不再注入整个代码的有效负载了，而是重新利用DEP允许的内存页面中的多个代码块，称为ROP gadget。这些代码块取自目标应用程序中现有的代码，并链接在一起，以形成所需的攻击者有效负载，或仅按页禁用DEP，以允许运行现有代码有效负载。

为了永久阻止ROP攻击，Intel开发了一种新的硬件强制控制流完整性缓解措施，称为控制强制技术（CET），大约两年前首次在Windows系统上发布。

我们会在本文中简要介绍CFI缓解措施的工作原理，包括CET，以及如何利用Counterfeit Object-Oriented Programming (COOP) 在最新Windows版本上有效绕过Intel CET。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ic0PRaz05OScZQR3ytItW78KqGUxAgyGNMy2AB9W1EstvkIoBBXGpb8UhqXbgrsDcR5cfLktO4JRw/640?wx_fmt=png)Forward-Edge和Backward-Edge CFI

控制流完整性机制可以分为两大类：Forward-Edge和Backward-Edge。

与Microsoft CFG4一样，Forward-EdgeCFI通过使用经过验证的函数地址来保护间接函数调用。例如，如果我们用ROPgadget地址重写CALL [rax]指令中解引用的指针，CFG将通过发出异常来阻止我们的攻击。

相反，像Intel的CET5这样的Backward-EdgeCFI通过将函数的返回地址与存储在Shadow Stack上的以前保存的地址版本进行比较来保护函数的返回地址。如果原始返回地址在内存被攻击期间被重写了，则地址对照（ address comparison）将不可避免地失败，应用程序将被终止。考虑到基于ROP的攻击在没有“CALL”指令的情况下执行“RET”指令，运行线程的堆栈和影子堆栈（shadow stack ）值不匹配，因此像CET这样的Backward-EdgeCFI有效地阻止了这种攻击技术。

Intel CET旨在通过间接分支跟踪（IBT）通过影子堆栈和COP/JOP缓解ROP攻击。然而，由于后一种技术尚未在Windows上实现，因此在本文中，我们将把“Intel CET”作为仅启用影子堆栈的实现。

CET当前的实现方式非常无效，因为渲染器进程通常会被利用。尽管CET在浏览器上还没有得到广泛的执行，但我们应该期待它在未来的每一个进程中都得到执行。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ic0PRaz05OScZQR3ytItW78KqGUxAgyGNMy2AB9W1EstvkIoBBXGpb8UhqXbgrsDcR5cfLktO4JRw/640?wx_fmt=png)伪造对象

Felix Schuster在2015年提出了一种名为伪面向对象编程（COOP）的新代码重用技术。不过该技术尚未在野外或公开利用被发现。我们写这篇博文的目的是试图利用这种理论方法，并在概念验证中加以实现，以绕过Intel CET。

该技术背后的主要思想是伪造，即用攻击者控制的有效负载在内存中生成新的对象，并通过目标应用程序或加载库中已经存在的虚拟函数将它们链接在一起。

伪对象中包含的每个虚拟函数称为vfgadget，负责执行一个小任务。与ROP类似，vfgadget可以执行诸如将值填充到寄存器中之类的任务。然而，当组合在一起时，多个vfgadget可以执行更高级的操作。

由于目前没有专门的工具可以发现vfgadget，所以可以通过自定义脚本(如idpython)找到它们，使用类似于ROP gadget发现的过程。

由于vfgadget是从CFG有效函数池中选取的，我们可以将它们标记为合法的，一旦我们劫持了其中一个函数的间接调用，它们的执行就不会被CFG阻止。

此外，一个有趣的推论是Intel CET不会被触发，因为我们不会在顺序调用vfgadget的过程中损坏任何函数返回地址。

一个典型的COOP有效载荷从一个充当COOP主要功能的基本vfgadget开始。我们在本文称之为Looper。一旦攻击者在内存中集成了伪造对象，Looper vfgadget就会遍历由攻击者精心安排的其他vfgadget数组，这些vfgadget将被逐个调用。通过以这种方式对齐伪对象中的vfgadget，我们将能够以可控的方式调用有效的虚拟函数。

Looper运行后，它可以调用其他负责执行特定操作的vfgadget，如Argument Loaders Invoker和Collector。这些vfgadget将定期存储在Looper访问的数组中。

Argument Loader vfgadget通过将值加载到给定寄存器中来填充该寄存器。要加载的值将存储在伪对象中，位于假对象开始处的偏移位置。

一旦寄存器被一个或多个参数加载器填充，就可以调用Invoker vfgadget来简单地执行目标API的函数指针。

Collector是一种gadget，用于检索寄存器中已存在的值，并将其保存回攻击者的伪造对象即作为从调用的API返回的值。

下图总结了迄今为止讨论的COOP攻击策略。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ic0PRaz05OScZQR3ytItW78dfFFau22zmPQvFRTjJ5vcAHFL2siaSdzlk7PiaaxoiaOSnxYh02KvsicFg/640?wx_fmt=png)

COOP攻击流

我们可以根据不同的vfgadget的可用性和想要执行的API来安排和混合它们。

为了更好地理解COOP攻击，让我们从分析主vfgadget Looper开始。以下汇编代码提供了Looper COOP vfgadget的简化版本：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ic0PRaz05OScZQR3ytItW788KbBSiaicU4BT1FDzT64GAvvPuEzFoeqmpEES4L5h20J6b8Hx6icf0ianQ/640?wx_fmt=png)

Looper Gadget相关的ASM代码

在第一行中，RCX持有this9指针，我们将伪对象的开头加载到RBX中，该伪对象位于RCX的偏移量0x40处。由于伪对象中的所有项目都将以偏离此指针的偏移量为准，因此我们需要确保在劫持程序流之前保存其值（即通过破坏vtable）。

然后，COOP有效负载基址被解引用到RAX中，RAX指向被调用的第一个vfgadget。一旦调用返回，一个新的vfgadget将从前一个gadget的偏移量0x20处加载，如果RBX的内容不为零，则会进行新的循环迭代。

当在内存中写入伪造对象时，我们需要预先对齐每个vfgadget以匹配Looper偏移量，类似于下面的布局：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ic0PRaz05OScZQR3ytItW78PVsYcbqCpzleDR48epFROWyib62hpUxic2knQMBol02nm8qUviaxuIcKA/640?wx_fmt=png)

内存中的COOP缓冲区

这样，00000227`26cd8900是COOP有效负载的基址，它存储在‘this’指针（RCX）的偏移量0x40处。从前面的代码清单中，我们注意到在\_loopstart例程的第一行，指针被解引用到RAX中，而RAX又指向第一个vfgadget。在下一次循环迭代中，Looper通过在前一个循环的偏移量0x20处加载指针来重复相同的任务，并最终调用第二个vfgadget。

当利用真实的目标浏览器时，建议依赖Looper vfgadget，因为它比其他vfgadget提供了更多的控制和稳定性。但是，为了简洁起见，我们在编写易受攻击的应用程序时只使用了一个Invoker vfgadget，它只接受一个参数。

在介绍了COOP的基本理论之后，让我们继续开发一个由CET编译的概念验证应用程序，该应用程序是我们为展示COOP攻击而开发的。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ic0PRaz05OScZQR3ytItW78KqGUxAgyGNMy2AB9W1EstvkIoBBXGpb8UhqXbgrsDcR5cfLktO4JRw/640?wx_fmt=png)与COOP绕过CET影子堆栈

我们编写的易受攻击的应用程序是用CET和CFG以及默认启用的DEP编译的。

首先，为了验证CET是否真的被强制执行，我们在printf上放置一个断点，检查调用堆栈，覆盖返回地址并恢复执行。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ic0PRaz05OScZQR3ytItW78pnTnx4m5mLDcKfDFN3hJ0zwuq6o3pLZZwjF449M25Nw8KzCkiaZUFhw/640?wx_fmt=png)

验证CET的执行

当收到一个涉及无效返回地址的Shadow Stack异常提示，就代表CET被启用了。

由于CET是一种硬件强制缓解，为了触发上述漏洞，我们至少需要一个英特尔虎湖( Tiger Lake )十一代酷睿 CPU。

为了模拟浏览器漏洞，我们可以利用执行应用程序时自动触发的应用程序中的类型混淆漏洞来获得RIP控制。

当我们点击该漏洞的触发器时，vtable指针会被我们的输入损坏，导致我们可以控制的间接调用。然后我们劫持vtable，使其指向第一个（也是唯一一个）vfgadget所在的COOP缓冲区。如上所述，为了简洁起见，我们没有使用带有嵌套vfgadget的Looper，而是选择使用一个同时具有Invoker和Argument Loader组件的gadget。

作为该漏洞自动利用的一部分，为了获取vfgadget的‘this’指针，我们泄漏了堆栈指针，并将‘this’指针作为堆栈的静态偏移量进行检索。

一旦我们获得了‘this’指针地址，我们就准备好要调用的WindowsAPI的地址及其参数。这是通过在伪对象内以所需偏移量写入Windows API地址和参数来实现的。

在更详细地研究COOP有效负载之前，让我们先通过不带任何参数运行PoC来理解它的语法。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ic0PRaz05OScZQR3ytItW78buG0RCbWFvSIEibaSTyu2GLJJLATeSMibCOmkgQpicfWmTia40eqic7CKtw/640?wx_fmt=png)

获取PoC的语法

应用程序接受四个参数：一个指向伪造对象（COOP）缓冲区的指针、vfgadget地址、Windows API地址及其参数。该助手显示了两个简单的用例，但可以将其扩展为调用任何CFG允许的API（如果应用程序是用它编译的）。

由于Windows DLL将在随机基址加载，因此需要预先计算所需的API地址。

让我们首先检查与vfgadget相关的对象的C++代码，然后从编译的二进制文件探索其相应的程序集：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ic0PRaz05OScZQR3ytItW78uxl2qQQgdic59esN2kwe5sLQFzIUK7rtY8R3yBHBeT78pE5xU00e14A/640?wx_fmt=png)

我们从中派生vfgadget的' trigger '方法

项目中的OffSec类包含一个触发器方法，它充当一个C风格的函数指针，我们可以使用它来调用任何我们喜欢的API。然后，在主程序例程中实例化“OffSec”类，以便将其与方法一起加载到内存中。

仔细查看反汇编程序中的Invoker可以发现一些有趣的方面。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ic0PRaz05OScZQR3ytItW78ZQpthiaEIibuibRrHXGRgnCMibtBpDBqwlvZHQEBE1h95QbAicLgL0SbJFw/640?wx_fmt=png)

调用程序vfgadget

从第二行到第四行，RCX引用的‘this’指针首先存储在堆栈中，然后移动到RAX中。接下来，从RAX偏移量0x10处的值被解引用并移动到RAX中。此值将是驻留在伪对象中的API函数指针。然后，在第7行和第8行，第一个函数参数从‘this’指针偏移量0x8处解引用，并移到RCX中。

我们很快就会发现，一旦我们从命令行提交了参数，易受攻击的应用程序就会处理这些偏移。

在介绍了攻击链的主要构建块之后，让我们尝试通过传递四个参数来运行PoC，以获得代码执行：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ic0PRaz05OScZQR3ytItW78EGHHFKsAnj5rjbLic0U1DxSvweWmiaicsiaxtiaUqoX1h83Zx72hoMgfNwA/640?wx_fmt=png)

运行带有所有参数的PoC应用程序

通过上述命令，我们提供了以下参数：00001e000000作为伪对象的存储缓冲区，5086014001000000作为Invoker vfgadget，40610fecfb7f0000是WinExec内存地址。作为最后一个参数，我们传递WinExec字符串参数。请注意，所有内存地址都是以little-endian格式传递的。

一旦启动，应用程序立即停止，允许我们将调试器附加到它。在这样做之前，我们启动Process Explorer以验证二进制文件实际上在启用Intel CET的情况下运行。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ic0PRaz05OScZQR3ytItW78m0mXkvP2b8xiagPJA2JcCL8jAUibLlLibPSjT4EQX5fY79WBwfDxVQrMQ/640?wx_fmt=png)

验证是否已使用Process Explorer启用CET

在“堆栈保护”栏下，Process Explorer确认仅对CET兼容模块强制执行CET，这意味着将对使用CET编译的任何模块强制执行缓解。附加调试器后，我们将断点放置到主函数中唯一的间接调用，然后继续执行。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ic0PRaz05OScZQR3ytItW78kFvYWpAzI5L4mcRicDV3XrWk2bXN6QicPa1oJHxfsia3d4k2ZXLQzJibmA/640?wx_fmt=png)

间接调用时中断

我们在main+0x3d2处放置了一个断点，并验证了在该地址确实有一个间接调用。接下来，我们将转储位于静态地址0x1e0000的伪造对象的内容，该地址包含指向位于0000000 1400186a0的vfgadget的指针。

在main+0x3d2是类型混淆错误引发的地方，允许我们控制RIP。一旦到达断点，我们就检查驻留在COOP缓冲区中的值，它应该是第一个Invoker vfgadget。我们让应用程序继续运行，并验证我们确实达到了断点。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ic0PRaz05OScZQR3ytItW78ia003EIwrmm4Xzq5Sh6zhIU6ibklXttqz9HhYGJz0AJrrs2rCAmbhy3A/640?wx_fmt=png)

登录第一个COOP vfgadget

在跟踪到CFG ldrpdispatchusercalltarget例程之后，我们跳转到Invoker vfgadget ' OffSec::trigger '，证明我们已经控制了程序的执行流。然后我们继续在vfgadget中进行跟踪：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ic0PRaz05OScZQR3ytItW783Zdp2R5LCUomj0W8aw6ZtcsX6wnlM3sOONyRR5obYwZfs3dFeF3j2w/640?wx_fmt=png)

将 ‘this’ 指针移动到RAX中

在上面的清单中，Invoker首先将‘this’指针从RCX保存到堆栈中，我们还验证它是否指向COOP缓冲区的底部。在最后一条指令中， ‘this’ 指针被加载到RAX中，RAX将用作调用API及其参数的引用：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ic0PRaz05OScZQR3ytItW78mKEicqqm99cxLJiaRVTBVel80maMkDkZKqS9kwbibicGvRQiaGLrDFu2bSA/640?wx_fmt=png)

通过‘this’ 指针加载WinExec参数

首先，在偏移量0x10处，我们可以看到WinExec地址被加载到RAX中，然后，在三条指令之后，命令参数被检索到偏移量0x8处。

如果执行继续，我们将再次调用LdrpDispatchUserCallTarget，它依次将执行分派给WinEx...
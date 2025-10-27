---
title: 利用直接 SYSCALL 调用禁用 Control Flow Guard，绕过终端防护软件的检测
url: https://www.4hou.com/posts/8Yzm
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-12-13
fetch_date: 2025-10-04T01:16:43.014132
---

# 利用直接 SYSCALL 调用禁用 Control Flow Guard，绕过终端防护软件的检测

利用直接 SYSCALL 调用禁用 Control Flow Guard，绕过终端防护软件的检测 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 利用直接 SYSCALL 调用禁用 Control Flow Guard，绕过终端防护软件的检测

gejigeji
[新闻](https://www.4hou.com/category/news)
2022-12-12 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)181523

收藏

导语：在这篇文章中，我们将演示如何使用直接的SYSCALL来禁用控制流保护(CFG)。CFG是一种内置在Windows中的漏洞缓解安全控制。

在这篇文章中，我们将演示如何使用直接的SYSCALL来禁用控制流保护(CFG)。CFG是一种内置在Windows中的漏洞缓解安全控制。

禁用CFG允许攻击者使用睡眠混淆技术来逃避检测。此外，我们还将介绍逆向工程未记录结构的基础知识。随着检测和避免检测越来越依赖于低级操作系统概念，这项技能将继续与安全社区相关。

已有很多关于“睡眠混淆（sleep obfuscation）”技术的讨论。睡眠混淆的目的是通过在睡眠时隐藏在读/写内存空间中来保护恶意软件免受内存扫描。这是有效的，因为内存扫描是资源密集型的，因此通常只针对可执行区域。

最近，一位安全研究员@C5pider在GitHub上发布了一个名为Ekko的概念验证工具。该工具以一种易于理解的方式实现了一种公共睡眠混淆方法，该方法首先由@peterwintrsmith 引入，我们会在本文中参考使用。

这种睡眠混淆的实现使用CreateTimerQueueTimer设置异步计时器。它们一个接一个地执行，完成以下任务:

将恶意软件可执行内存区域设置为读/写；

加密内存区域；

等待特定的时间段；

解密内存区域；

将内存设置回读取/执行。

这一切都有效，因为 CreateTimerQueueTimer 使用回调例程在每个计时器完成时执行给定函数。回调例程发生在恶意软件的内存空间之外，因此即使内存设置为只读/写也可以执行。

**进入控制流保护**

如果你使用这种或类似的执行方法，你会遇到一个阻碍：Microsoft 的 Control Flow Guard (CFG)。

CFG是一种包含在Windows中的反利用技术(从Windows 8.1开始)，它可以防止任意代码在程序中间接执行。这可以阻止尝试禁用数据执行保护 (DEP) 或将包含恶意代码的只读/只写缓冲区设置为可执行的攻击。

如果你编译并运行 Ekko，它将正常工作；但是，如果你在启用 CFG (/guard:cf) 的情况下编译它并尝试运行它，你将触发 CFG，并且该过程将快速结束。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220831/1661938520202699.png "1661938520202699.png")

控制流保护错误

这是因为CreateTimerQueueTimer指向的回调例程是NtContinue，它位于一个特殊的函数列表中，在启用CFG时不能间接调用该函数。间接函数调用是从程序调用堆栈外的另一个函数发起的调用。在本例中，由计时器触发的调用。下面是不允许的函数调用的完整列表和解释。

由于恶意软件现在很少运行在自己的“Evil.exe”进程中，它几乎总是会被注入或加载到一个“已知良好”进程中，而这些进程中的大多数都是用CFG启用编译的。作为恶意软件开发者，我们需要弄清楚如何绕过或禁用NtContinue 的 CFG。[SetProcessValidCallTargets]为CFG提供了一个有效的间接调用目标列表，并指定它们是否应该被标记为有效。

CFG 实际上并不是为了阻止我们在这里讨论的攻击类型而构建的。它的存在使得Use-After-Free和ROP链接更加困难，从而阻止利用。因此，在“正常”代码执行情况下，很容易获取给定的内存位置并将其设置为有效的目标。将该函数添加到Ekko项目中，在启动 Ekko 之前在 NtContinue 上调用该函数。

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220831/1661938529157118.png "1661938529157118.png")

![2.2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220831/1661938538162942.png "1661938538162942.png")

Ekko 在启用 CFG 的情况下运行

太棒了！问题解决了。现在让我们看看 SetProcessValidCallTargets 的底层发生了什么，看看它是否调用了 NT API。

**使用SYSCALL进行测试**

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220831/1661938547515756.png "1661938547515756.png")

来自 SetProcessValidCallTargets 的 NtSetInformationVirtualMemory

在底层，SetProcessValidCallTargets正在调用NtSetInformationVirtualMemory。不幸的是，这个SYSCALL的文档比较少见，但我们最终还是找到了一篇文章，当尝试实现该研究时，调用 NtSetInformationVirtualMemory 会返回“无效参数”错误。

该研究针对的是x86进程，它需要不同于x64的结构，这导致了无效参数错误。

有了前面的运行函数，所以让我们在调试器中遍历它，看看我们是否可以绘制出它如何成功地将参数传递给 x64 进程的 NtSetInformationVirtualMemory。

SetProcessValidCallTargets 接受五个参数。 X64 调用约定将前四个参数传递给寄存器 RCX、RDX、R8 和 R9。最后一个参数将被推入堆栈。

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220831/1661938556143868.png "1661938556143868.png")

SetProcessValidCallTargets参数

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220831/1661938564148314.png "1661938564148314.png")

SetProcessValidCallTargets寄存器

在这里，我们看到 RCX 是 0XFFFFFFFFFFFFFFFF，在这种情况下，它表示当前进程的句柄。 RDX 指向 0x00007FF96372D000，ntdll.dll 的基地址，也就是我们正在修改的 DLL。 R8 为 0x0000000000080000，ntdll 中可执行区域的大小。 R9 是 0x00000000000000001，我们正在修改的内存位置的数量。

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220831/1661938572858002.png "1661938572858002.png")

设置堆栈参数

我们现在需要弄清楚 CFG\_CALL\_TARGET\_INFO 结构是如何设置和存储的。

相关区域在上面的截图中被突出显示。

首先，将值为0x790的RCX移动到RAX，然后将RAX推入RSP + 0x48处的堆栈。这是CFG\_CALL\_TARGET\_INFO结构中的第一个值，NtContinue的偏移量。

接下来，0x1被推送到RSP +0x50处的堆栈。0x1是作为第二个值传入的CFG\_CALL\_TARGET\_VALID标志的值。

最后，指向结构开头的指针，RSP + 0x48 被移动到 RAX，然后作为 RSP + 0x20被推入堆栈。这是在 x64 中传递给函数的第五个参数的标准位置。指针指向内存位置 0x00000071110FF678，我们需要记住这个位置，因为它稍后会出现。

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220831/1661938580188310.png "1661938580188310.png")

NTSetInformationVirtualMemory

NtSetInformationVirtualMemory所需的参数全部来自这里。

因为我们得到了一个无效的参数错误，让我们一步一步地遍历整个调用，看看在SYSCALL中寄存器和堆栈是什么样子的。

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220831/1661938589493757.png "1661938589493757.png")

SYSCALL中的寄存器

本地进程句柄仍然是用RCX的形式表示。RDX是0x2，与VmCfgCallTargetInformation 的 VIRTUAL\_MEMORY\_INFORMATION\_CLASS 枚举相匹配。R8是0x1，我们正在修改的内存条目的数量，R9是0x00000071110FF570，它是指向 MEMORY\_RANGE\_ENTRY 结构的内存指针，其中两个条目在我们之前的参数中出现过。

首先是ntdll的基地址0x00007FF96372D000。

第二个是我们之前作为第三个参数传递给 SetProcessValidCallTargets 的可执行区域的大小。

![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220831/1661938597593207.png "1661938597593207.png")

内存中的MEMORY\_RANGE\_ENTRY结构

**定义未记录的结构**

到目前为止，一切看起来都很好。让我们看看堆栈。

在RSP+0x20, NtSetInformationVirtualMemory是从基于堆栈的参数开始的，我们看到两个条目，它们与现有 NtSetInformationVirtualMemory 文档中的最后两个参数匹配。

第一个堆栈参数是一个指向内存区域的指针，0x00007FF961489E80, MSDN说这是一个依赖于查询的信息类的变量缓冲区，第二个是缓冲区的大小。

![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220831/1661938604203031.png "1661938604203031.png")

SYSCALL时的堆栈

我们立即看到与上述博客的差异。 0x28（40字节）比之前研究的0x10要大。

让我们转到第五个参数0x00000071110FF580所指向的内存位置，看看它是什么样子的。

![11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220831/1661938613889248.png "1661938613889248.png")

内存指针处的 40 个字节

这是我们需要弄清楚的新结构在内存中的位置。

首先，我们有0x1，可以放心地假设它指的是传递的偏移量的数量。

第二个值0x00000071110FF5E8似乎是指向另一个内存位置的指针，该位置目前被设置为0。

第三个值0x00000071110FF678也是一个指针。这应该看起来很熟悉，因为它是一个指向先前为我们传递给 SetProcessValidCallTargets 的 CFG\_CALL\_TARGET\_INFO 结构预留的内存的指针。这意味着这将是我们新结构中的第三个值。

最后，我们有 16 个字节的零。

让我们跳过SYSCALL，看看这些值是否发生了变化。

![12.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220831/1661938623105511.png "1661938623105511.png")

 系统调用后值的变化

唯一改变的值是 0x00000071110FF5E8 处的第二个参数的值，它从0更改为1。这表明它是一个指向数值的指针，我们称之为ULONG，因为它是NT调用的常见类型。

这是我们的新结构：

![13.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220831/1661938632180300.png "1661938632180300.png")

新结构

这是我们将内存位置标记为对 CFG 有效的新函数：

![14.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220831/1661938641376030.png "1661938641376030.png")

新函数

让我们看看它是否有效。

![15.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220831/1661938651830810.png "1661938651830810.png")

使用NtSetInformationVirtualMemory使用CFG执行Ekko

**总结**

我们已经介绍了如何使用直接SYSCALL禁用给定内存位置的 CFG。

一旦被利用，CFG 通常不会起到任何保护作用。

完整的PoC代码可以在Icebreaker的GitHub上找到。

本文翻译自：https://icebreaker.team/blogs/sleeping-with-control-flow-guard/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?PRJS4Z3S)

#### 你可能感兴趣的

* [![]()

  ​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)
* [![]()

  新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)
* [![]()

  新型NPM包利...
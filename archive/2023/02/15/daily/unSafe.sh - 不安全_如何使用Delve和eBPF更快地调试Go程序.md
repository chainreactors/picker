---
title: 如何使用Delve和eBPF更快地调试Go程序
url: https://buaq.net/go-149373.html
source: unSafe.sh - 不安全
date: 2023-02-15
fetch_date: 2025-10-04T06:36:06.054807
---

# 如何使用Delve和eBPF更快地调试Go程序

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

![](https://8aqnet.cdn.bcebos.com/50ac3a724b7a31b99522559073c8f015.jpg)

如何使用Delve和eBPF更快地调试Go程序

前言此文章将解释如何使用 Delve 跟踪 Go 程序，以及 Delve 如何利用 eBPF 在后台优化效率和速度。Delve 的目标是为开发人员提供愉快且高效
*2023-2-14 21:33:17
Author: [www.cnxct.com(查看原文)](/jump-149373.htm)
阅读量:29
收藏*

---

[![](https://image.cnxct.com/2023/02/delve-debug_2x-800x400.png)](https://image.cnxct.com/2023/02/delve-debug_2x.png)

### 前言

此文章将解释如何使用 [Delve](https://github.com/go-delve/delve) 跟踪 Go 程序，以及 Delve 如何利用 eBPF 在后台优化效率和速度。Delve 的目标是为开发人员提供愉快且高效的 Go 调试体验。因此，本文重点介绍了我们如何优化函数跟踪子系统，以便您可以更快地检查程序并找到根本原因分析。Delve 的跟踪实现有两个不同的后端，一个是基于 ptrace 的，另一个使用 eBPF。如果您不熟悉任何这些术语，请不要担心，我会随着解释一起说明。

### 什么是程序跟踪？

跟踪是一种允许开发人员在执行时看到程序正在做什么的技术。与典型的调试技术相反，这种方法不需要直接用户交互。最知名的跟踪工具之一是 [strace](https://strace.io/)，它允许开发人员在执行期间查看程序的系统调用。

尽管上述的 strace 工具对于了解系统调用很有用，但 Delve trace 命令允许您洞察 "用户空间" 中 Go 程序的情况。这种 Delve 跟踪技术允许您跟踪程序中的任意函数，以便查看这些函数的输入和输出。

此外，您还可以使用此工具了解程序的控制流，而无需交互式调试会话的开销，因为它还会显示正在执行该函数的 Goroutine。对于高度并发的程序，这可能是获得程序执行洞察力的更快方法，而无需启动完整的交互式调试会话。

### 如何使用 Delve 跟踪 Go 程序

Delve 允许您通过调用 dlv trace 子命令来跟踪 Go 程序。该子命令接受一个正则表达式，并将执行您的程序，在与正则表达式匹配的每个函数上设置跟踪点，并实时显示结果。

以下是示例程序：

```
package main

import "fmt"

func foo(x, y int) (z int) {
        fmt.Printf("x=%d, y=%d, z=%d\n", x, y, z)
        z = x + y

        return
}

func main() {
        x := 99
        y := x * x
        z := foo(x, y)

        fmt.Printf("z=%d\n", z)
}
```

程序跟踪将给出以下输出：

```
$ dlv trace foo

> goroutine(1): main.foo(99, 9801)

x=99, y=9801, z=0

>> goroutine(1): => (9900)

z=9900

Process 583475 has exited with status 0
```

如您所见，我们在正则表达式中提供了 `foo`，它在这种情况下与主包中同名的函数匹配。以`>`为前缀的输出表示被调用的函数，并显示调用函数的参数，而以`>>`为前缀的输出表示从函数返回并与其相关联的返回值。所有输入和输出行均以在该时刻执行的 Goroutine 作为前缀。

默认情况下，`dlv trace` 命令使用基于 ptrace 的后端，但添加 `--ebpf` 标志将启用基于 eBPF 的实验性后端。使用上面的示例，如果我们要像以下方式调用 trace 子命令：

```
$ dlv trace –ebpf foo
```

我们将收到类似的输出。但是，背后发生的情况要大大不同并且更加高效。

### ptrace低效率

默认情况下，Delve 会使用 ptrace 系统调用来实现跟踪功能。ptrace 是一个系统调用，允许程序观察和操纵同一台机器上的其他程序。实际上，在 Unix 系统上，Delve 使用这个 ptrace 功能来实现调试器提供的许多低级功能，例如读写内存、控制执行等。

虽然 ptrace 是一个有用和强大的机制，但它存在固有的效率低下。首先，ptrace 是一个系统调用，意味着我们必须跨越用户空间/内核空间边界，这增加了每次使用函数时的开销。这是由于我们必须调用 ptrace 的次数越多，开销就越大。考虑前面的示例，以下是使用 ptrace 实现跟踪的大致步骤概述：

1. 使用 `ptrace(PT_ATTACH)` 启动程序并附加调试器。
2. 使用 `ptrace` 在匹配所提供的正则表达式的每个函数处设置断点，并在被跟踪的进程的可执行内存中插入断点指令。
3. 另外，在该函数的每个返回指令处设置断点。
4. 再次使用 `ptrace(PT_CONT)` 继续程序。
5. 此步骤可能涉及多次`ptrace`调用，因为我们需要读取函数入口的CPU寄存器、堆栈上的内存以及如果必须取消指针引用的堆上的内存。
6. 再次使用`ptrace(PT_CONT)`继续程序。
7. 在函数返回时遇到断点，通过读取变量，可能涉及到更多的`ptrace`调用，以读取寄存器和内存。
8. 再次使用`ptrace(PT_CONT)`继续程序。
9. 直到程序结束。

显然，函数的参数和返回值越多，每次停止就越昂贵。所有调试器花费在进行 `ptrace` 系统调用的时间，我们跟踪的程序都处于暂停状态，没有执行任何指令。从用户的角度来看，这使得程序的运行速度比原本要慢得多。现在，对于开发和调试来说，这也许不是什么大问题，但是时间是宝贵的，我们应该尽量快速地完成事情。程序在跟踪过程中的运行速度越快，你就能越快找到问题的根本原因。

现在的问题是，我们如何使其更好呢？在下一节中，我们将讨论新的基于 eBPF 的后端，以及它如何改进这种方法。

### eBPF 为何比 ptrace 更快

一个最大的速度和效率改进是避免大量的系统调用开销。这是 eBPF 发挥作用的地方，因为我们可以在函数入口和出口设置 uprobes，并将小 eBPF 程序附加到它们上。Delve 使用 Cilium eBPF Go 库加载和与 eBPF 程序交互。

每次触发 probe 时，内核将调用我们的 eBPF 程序，然后在它完成后继续主程序。我们编写的小 eBPF 程序将处理函数入口和出口中列出的所有步骤，但不会有所有的系统调用上下文切换，因为程序直接在内核空间中执行。我们的 eBPF 程序可以通过 eBPF 环形缓冲区和映射数据结构与用户空间中的调试器通信，使 Delve 能够收集所需的所有信息。

这种方法的优点是，我们正在跟踪的程序需要暂停的时间大大减少。在触发 probe 时运行我们的 eBPF 程序比在函数入口和出口处调用多个系统调用要快得多。

### 使用eBPF调试与跟踪步骤

这里再概括一遍使用 eBPF 跟踪调试的流程：

1. 启动程序并使用 `ptrace(PT_ATTACH)` 附加到进程上。
2. 在内核中加载所有需要跟踪的函数的 uprobes。
3. 使用 `ptrace(PT_CONT)` 继续执行程序。
4. 在函数入口和出口触发 uprobes。每当 probe 被触发，内核部分将运行我们的 eBPF 程序，该程序获取函数的参数或返回值，并将其发送回用户空间。在用户空间中，从 eBPF 环形缓冲区读取函数参数和返回值。
5. 重复此过程直到程序结束。

通过使用这种方法，Delve 可以比使用默认的 ptrace 实现更快地跟踪程序。现在，你可能会问，为什么不将这种方法默认使用？事实上，未来很有可能会成为默认方法。但目前，仍在进行开发，以改进这种基于 eBPF 的后端并确保它与基于 ptrace 的后端具有平衡性。然而，您仍然可以在执行 `dlv trace` 时使用 `--ebpf` 标志来使用它。

为了给出一个使用不同跟踪方法的程序的效率差异的大致数字，我测量了另一个程序的运行情况，如下所示：

```
Program execution: 23.7µs

With eBPF trace: 683.1µs

With ptrace tracing: 2.3s
```

数字本身就是最好的证明！

### 为什么不使用uretprobe

如果您熟悉 eBPF、uprobes / uretprobes，您可能会问为什么我们对一切都使用 uprobes，而不是仅使用 uretprobes 捕获返回参数。关于此的解释相当复杂，但简短版本是，Go 运行时在执行 Go 程序过程中需要多次检查调用堆栈。当 uretprobes 附加到函数时，它们将该函数的返回地址覆盖在堆栈上。当 Go 运行时检查堆栈时，它会找到该函数的意外返回地址，最终会导致程序致命退出。为了解决这个问题，我们只需使用 uprobes，并利用 Delve 的能力检查程序的机器指令来在每个函数的返回指令处设置探测器。

### Delve使用eBPF更快地调试Go代码

Delve的总体目标是帮助开发人员尽快地找到Go代码中的错误。为此，我们利用最新的方法和技术，并试图推动调试器可以完成的范围。 Delve在内部利用eBPF来最大化效率和速度。用户空间跟踪是任何工程师工具箱中的重要工具，我们的目标是使其高效易用。

#### 原文：

[How debugging Go programs with Delve and eBPF is faster](https://developers.redhat.com/articles/2023/02/13/how-debugging-go-programs-delve-and-ebpf-faster)

[![知识共享许可协议](https://www.cnxct.com/attachments/88x31.png)](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh)CFC4N的博客 由 [CFC4N](https://www.cnxct.com) 创作，采用 [知识共享 署名-非商业性使用-相同方式共享（3.0未本地化版本）许可协议](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh)进行许可。基于<https://www.cnxct.com>上的作品创作。转载请注明转自：[如何使用Delve和eBPF更快地调试Go程序](https://www.cnxct.com/how-debugging-go-programs-delve-and-ebpf-faster-zh_cn/)

文章来源: https://www.cnxct.com/how-debugging-go-programs-delve-and-ebpf-faster-zh\_cn/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)
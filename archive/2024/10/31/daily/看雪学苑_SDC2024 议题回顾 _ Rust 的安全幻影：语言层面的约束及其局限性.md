---
title: SDC2024 议题回顾 | Rust 的安全幻影：语言层面的约束及其局限性
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458579888&idx=1&sn=6ee6350ecda2740e1d51c63b9fc1288c&chksm=b18dc33a86fa4a2c4252ae8a5dd9f7349fd6d565b31624b58ca9c70c88e111492c2a2022df2d&scene=58&subscene=0#rd
source: 看雪学苑
date: 2024-10-31
fetch_date: 2025-10-06T18:54:27.944882
---

# SDC2024 议题回顾 | Rust 的安全幻影：语言层面的约束及其局限性

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EarBb1XmLBhgH7C3dzu9gbgfx89q2Ca48pXztw7NvbcXBdqm4351ypBA4hibZabm7BVE7j5hyvftQ/0?wx_fmt=jpeg)

# SDC2024 议题回顾 | Rust 的安全幻影：语言层面的约束及其局限性

SDC2024

看雪学苑

“

Rust 语言的安全机制源自于其背后的约束，Rust约束不仅是语言设计的核心，也是其安全性的重要保障。然而，这些约束并非无懈可击。在现实场景中， Rust 的所有权、借用和生命周期在某些特定情况下可能导致安全隐患。

”

一起来回顾下陈浩在SDC2024 上发表的议题演讲：《Rust 的安全幻影：语言层面的约束及其局限性》

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EarBb1XmLBhgH7C3dzu9gb6gpJzY6tTXbF6OpqCdjUKOAEZnOD13ia8sAe3dp3kxiboZcGtpZ3qOlg/640?wx_fmt=jpeg&from=appmsg)

**【陈浩：奇安信天工实验室安全研究员】**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8EarBb1XmLBhgH7C3dzu9gb54gPGMibcVPxWBEMiacVScHvnrx6ERdWW1xI7u6Gx5opQd2c7Ms048Zw/640?wx_fmt=gif&from=appmsg)

**一**

**Rust介绍**

Rust语言自其发布以来就备受人们关注，作为一门现代的系统级编程语言，Rust在安全性方面引起了人们的极大兴趣。它与其他语言相比，引入了一系列创新的安全特性，旨在帮助开发者编写更可靠、更安全的软件。在这个基础上，许多大厂开始纷纷在自己的项目中引入Rust，比如`Cloudflare`的`pingora`，Rust版的git -- `gitxoide`，连微软都提到要将自家的win32k模块用rust重写，足以见得其火爆程度。

之所以人们对Rust那么充满兴趣，除了其强大的语法规则之外，Rust提供了一系列的安全保障机制也让人非常感兴趣，其主要集中在以下几个方面：

* **内存安全：**Rust通过使用所有权系统和检查器等机制，解决了内存安全问题。它在编译时进行严格的借用规则检查，确保不会出现数据竞争、空指针解引用和缓冲区溢出等常见的内存错误。
* **线程安全：**Rust的并发模型使得编写线程安全的代码变得更加容易。它通过所有权和借用的机制，确保在编译时避免了数据竞争和并发问题，从而减少了运行时错误的潜在风险。
* **抽象层安全检测：**Rust提供了强大的抽象能力，使得开发者能够编写更加安全和可维护的代码。通过诸如模式匹配、类型系统、trait和泛型等特性，Rust鼓励使用安全抽象来减少错误和提高代码的可读性。

Rust强大的编译器管会接管很多工作，从而尽可能的减少各种内存错误的诞生。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8EarBb1XmLBhgH7C3dzu9gb54gPGMibcVPxWBEMiacVScHvnrx6ERdWW1xI7u6Gx5opQd2c7Ms048Zw/640?wx_fmt=gif&from=appmsg)

**二**

**Rust不会出现漏洞吗？**

在 Rust 的各类机制下，开发人员在编译阶段被迫做了相当多的检查工作。同时在 Rust 的抽象机制下，整体的开发流程得到了规范，理论上应该是很难再出现漏洞了。然而，安全本质其实是人，**错误本质上是由人们的错误认知引发的。**即便是在 Rust 的保护之下，人们也是有可能犯错，从而导致新的问题的出现。对于这种场景，我们可以用一种宏观的方法论来概括，那就是**认知偏差。**这里可以用一个图来大致描述一下这个认知偏差：

![](https://mmbiz.qpic.cn/mmbiz_png/9EP6QFMcTmSPQyjCzntic6eQhpsa8LVgrlAUJ18JlEGwgrjoUlmb0FCIufm4oC7WzrzLoRo95JxIibSrUrn3zSYQ/640?wx_fmt=png&from=appmsg)

换句话说，在使用Rust开发中，人们认为Rust能够提供的防护和Rust实际上提供的防护，这两者存在一定的差异。具体来说，可以有一下几种场景：

* Rust 检查时，能否防护过较为底层的操作状态？
* Rust 自身特性是否会引入问题？
* Rust 能否检查出作为mod 或者 API被其他人调用时，也能完全保护调用安全吗？

为了能够更好的了解认知差异，接下来我们就介绍几种比较典型的 Rust 下容易出现的漏洞。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8EarBb1XmLBhgH7C3dzu9gb54gPGMibcVPxWBEMiacVScHvnrx6ERdWW1xI7u6Gx5opQd2c7Ms048Zw/640?wx_fmt=gif&from=appmsg)

**三**

**案例一：对操作系统行为的认知错误**

在进行开发过程中，Rust 通常会需要与操作系统底层进行交互。然而在这些操作过程中，本质上是对**底层的API**或者对**底层操作系统**的操作，此时考察的是开发者对于操作系统的理解。而Rust编译器的防护机制并无法直接作用于这些底层的操作系统对象，从而会导致错误的发生。

一种常见的认知偏差就是**默认操作系统提供的特性**，比如说接下来要提到的**特殊字符过滤规则。**

**1、BatBadBut（CVE-2024-24576）**

在2024年4月，安全研究员RyotaK公开了一种他发现现有大部分高级语言中常见的漏洞类型，取名为`BatBadBut`，其含义为**batch文件虽然糟糕，但不是最糟糕的。**

> batch files and bad, but not the worst

*在Windows下，想要执行bat文件就必须要启动一个cmd.exe，所以执行的时候通常会变成*`cmd.exe /c test.bat`。

每个高级语言在Windows平台下需要创建新的进程的时候，最终都会调用Windows的API`CreateProcess`。为了防止命令注入，它们大多数会对参数进行一定的限制，然而**Windows平台下的CreateProcess存在一定的特殊行为**，使得一些常见的过滤手段依然能够被绕过。作者给了一个nodejs的例子，在nodejs中，当进行进程创建的时候，通常是这样做的：

![](https://mmbiz.qpic.cn/mmbiz_png/9EP6QFMcTmSPQyjCzntic6eQhpsa8LVgrFOUicZVXGbicanmnVUVxrm9epb6tv71HxbowO3L9eMrjyJc3uxNlNmzA/640?wx_fmt=png&from=appmsg)

这种做法通常是没问题的，此时由`CreateProcess`创建的进程为`echo`，参数为后续的两个参数。同时，这个调用过程中伴随的如下的过滤函数，会将`"`过滤成`\"`

![](https://mmbiz.qpic.cn/mmbiz_png/9EP6QFMcTmSPQyjCzntic6eQhpsa8LVgrvWzDLJwibpwXo3IAJbmPGbLqHP9DKJTn7icCwLVTe4F7wtgc2hVcVn8A/640?wx_fmt=png&from=appmsg)

此时，上述的指令会形成如下的指令：

![](https://mmbiz.qpic.cn/mmbiz_png/9EP6QFMcTmSPQyjCzntic6eQhpsa8LVgr3ra0l5xVss8P3va4mzvl1GpGMQiaMJDFq931kT1aIRTeWBRcB4kVVjA/640?wx_fmt=png&from=appmsg)

然而，当遇到如下代码的时候，情况会发生变化：

![](https://mmbiz.qpic.cn/mmbiz_png/9EP6QFMcTmSPQyjCzntic6eQhpsa8LVgrk3CJEQD5Mr6CWibicnIia9rDDJOZczPfd5neicJDnLuo7CqxMdibbWq8cmA/640?wx_fmt=png&from=appmsg)

因为 Windows 并没有办法直接的启动一个bat文件，所以实际上启动的时候，Windows执行的实际逻辑变成了：

![](https://mmbiz.qpic.cn/mmbiz_png/9EP6QFMcTmSPQyjCzntic6eQhpsa8LVgrjsDtblvUL3u3nJGU1w04MkhP1DQphHygSdWgMl0YiaXhzxrUTqdJiahw/640?wx_fmt=png&from=appmsg)

而实际上，在Windows中的`\`并非是我们理解的那种**能将所有符号进行转义**，转义字符。其只能转义`\`本身，类似于作为路径的时候，以及转义换行符。所以，上述的命令实际上等价于：

![](https://mmbiz.qpic.cn/mmbiz_png/9EP6QFMcTmSPQyjCzntic6eQhpsa8LVgrRnibfFic8YEHlmic7WeicQpAcFUfYnKicVVb0t72eRR8QTmiaxYW6PBQTlUA/640?wx_fmt=png&from=appmsg)此时命令解析模式如下：

![](https://mmbiz.qpic.cn/mmbiz_png/9EP6QFMcTmSPQyjCzntic6eQhpsa8LVgrjOfoFiaZyIagAjyWNZnKe1CRg16vKKHRbalWicMdrB0fvkeVXicGbDMng/640?wx_fmt=png&from=appmsg)

可见依然发生了命令注入。实际上，如果想要在Windows下进行我们常规理解下的命令转换，要使用`^`符号，例如将上述指令修改成如下的形式，即可防止命令注入：

![](https://mmbiz.qpic.cn/mmbiz_png/9EP6QFMcTmSPQyjCzntic6eQhpsa8LVgrmEcF3dEicjl248Zf6P2azNyzdqWCXOaqLIiavICbdSNHmU3Dw1lWQf4Q/640?wx_fmt=png&from=appmsg)

作者给出了他测试过的受到影响的语言：

* Erlange
* Go
* Haskell
* Java
* Node.js
* PHP
* Python
* Ruby
* Rust

这些语言的内置`Execute`或者`Command`函数都或多或少会受到影响。

**2、Rust CVE-2024-24576**

Rust也有这样的问题，所以进行了紧急修复，但是Rust一开始似乎是意识到了`.bat`的特异性行为，还给出了相关处理函数：

![](https://mmbiz.qpic.cn/mmbiz_png/9EP6QFMcTmSPQyjCzntic6eQhpsa8LVgrCwj83Lte7UlRP3xAIomJicFW8R6lnXHWLoLtiahNBbrI0mhibal868OAA/640?wx_fmt=png&from=appmsg)

然而它在处理的过程中，并未对双引号正确处理，而是同样使用了`\`：

![](https://mmbiz.qpic.cn/mmbiz_png/9EP6QFMcTmSPQyjCzntic6eQhpsa8LVgrwTuOgYKqEMxRSBabLWywULxeThM0TKgttT4OuWA4CPzP9Jhr8lDfUw/640?wx_fmt=png&from=appmsg)

在这边，错误的使用了`\\`作为过滤字符，所以同样导致了问题的出现。

这里参考网上流传的poc：

![](https://mmbiz.qpic.cn/mmbiz_png/9EP6QFMcTmSPQyjCzntic6eQhpsa8LVgrFJHP1HG3WIsiaQzeycDM1zNFnibNr0sXt0Bu98pZdDljvEAImYn3aVww/640?wx_fmt=png&from=appmsg)

当我们传入`"&calc.exe`时候就能弹出计算器，此时观察命令行的参数可以看到如下的内容：

![](https://mmbiz.qpic.cn/mmbiz_png/9EP6QFMcTmSPQyjCzntic6eQhpsa8LVgrKPlUBhSdqlM1LFw77KlfknfKJvoXBKMLlLEBpO61vqd5jVYMabGKdA/640?wx_fmt=png&from=appmsg)

Rust给出的修复在这边。经分析，可以知道主要是引入了函数`append_bat_arg`，在对各种字符串做了过滤之后，假设遇到双引号，则再次插入另一个，从而阻止绕过的发生：

![](https://mmbiz.qpic.cn/mmbiz_png/9EP6QFMcTmSPQyjCzntic6eQhpsa8LVgrjTPXlfSCicMdHic4oBdmKxQXqGuxvVX7iaQpqvZhjOyQknXcjd8DniaIRw/640?wx_fmt=png&from=appmsg)

**3、认知错误分析**

实际上，这个漏洞本身和Rust关联不大，但是我们仍然可以用这个认知模型对这个漏洞进行分析：

* 开发人员认知：Windows中，`\`与Linux下含义相同
* 实际运行环境：Windows中的`^`与Linux下`\`语义相同

这种对于操作系统的认知差异导致了这个问题的出现。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8EarBb1XmLBhgH7C3dzu9gb54gPGMibcVPxWBEMiacVScHvnrx6ERdWW1xI7u6Gx5opQd2c7Ms048Zw/640?wx_fmt=gif&from=appmsg)

**四**

**案例二：对特性的认知错误**

**1、内容重排序问题**

在[之前的文章中](http://mp.weixin.qq.com/s?__biz=Mzk0OTU2ODQ4Mw==&mid=2247485705&idx=1&sn=b10b583e944939d6c3a8e2b739817749&chksm=c3571f85f4209693b322eae9ec8308ac89a895674d1e067155eb0ef633a3ffdb75a8a7c11085&scene=21#wechat_redirect)提到过，Rust的结构体的变量顺序可能会由于内存对齐问题进行重排序，这边简单复习一下，假设存在结构体：

![](https://mmbiz.qpic.cn/mmbiz_png/9EP6QFMcTmSPQyjCzntic6eQhpsa8LVgrzfoVscuvcw6LliaR14qZUQ1iawZMVbh6Y1rVoQLNvegDiaQwhLICeeKMA/640?wx_fmt=png&from=appmsg)

上述结构体如果在C里面写的话，可以写作如下的形式：

![](https://mmbiz.qpic.cn/mmbiz_png/9EP6QFMcTmSPQyjCzntic6eQhpsa8LVgrD4aPQ2G3x2Ka86HLVZo3hGMOELUP4ZzL1wsvQkYnZgYkHCjGrLO9Ag/640?wx_fmt=png&from=appmsg)

此时，这个结构体的大小是什么呢？

实际上，假设我们打印结构体的大小和偏移，会得到这个答案：

![](https://mmbiz.qpic.cn/mmbiz_png/9EP6QFMcTmSPQyjCzntic6eQhpsa8LVgrE0ldTe97ddyCmjmkdc0RMSKa9jg6oANYpJTq66O7xl9bEnhnUXEO6g/640?wx_fmt=png&from=appmsg)

因为结构体对齐的时候，会遵顼三个原则：

* 第一个成员的起始地址为0
* 每个成员的首地址为自身大小的整数倍
* 总大小为成员大小的整数倍

由于b的起始地址必须是4对齐，所以所有的变量都被迫进行了4字节对齐，从而形成了这个状态。

![](https://mmbiz.qpic.cn/mmbiz_png/9EP6QFMcTmSPQyjCzntic6eQhpsa8LVgrClFgc2Tj4EKKe6rjQpADBAib4ib72LzCO4giaAmfAibpWWWR26g6uZxV8Q/640?wx_fmt=png&from=appmsg)

那么这个结构体在Rust中的内存排布是如何的呢？

![](https://mmbiz.qpic.cn/mmbiz_png/9EP6QFMcTmSPQyjCzntic6eQhpsa8LVgrl0bFfmOAnTeTZYnUwt9FoSMMiaKoHpGuSZHyXUvT21sehibRMfFB9Y3A/640?wx_fmt=png&from=appmsg)

如果我们尝试打印他们的偏移的话，可以得到如下的结果：

![](https://mmbiz.qpic.cn/mmbiz_png/9EP6QFMcTmSPQyjCzntic6eQhpsa8LVgrzS5pXy8OpqmaaGqW3nr1VpRvclBkUIlDSrohToRvPnokeibvex2kKvg/640?wx_fmt=png&from=appmsg)

从IDA中看，也可看到类似的结果：

![](https://mmbiz.qpic.cn/mmbiz_png/9EP6QFMcTmSPQyjCzntic6eQhpsa8LVgribYFmk7ehX9uic9BnkCfLdqc9YJTPtJmIVhg6wccsN94tbqfsM1UUaaQ/640?wx_fmt=png&from=appmsg)

可以看到field2和field3的偏移发生了变化，其原因源自于之前提到过的对齐特性，Rust会尽可能的缩小结构体大小，会因此调换结构体成员的变量顺序，从而保证结构体尽可能地小。

![](https://mmbiz.qpic.cn/mmbiz_png/9EP6QFMcTmSPQyjCzntic6eQhpsa8LVgrmgibUcb5o3DtEGeYUibHEDJCMRNVbjrrUMMATHmFUAzL4ECL5pVmDqug/640?wx_fmt=png&from=appmsg)

**2、repr**...
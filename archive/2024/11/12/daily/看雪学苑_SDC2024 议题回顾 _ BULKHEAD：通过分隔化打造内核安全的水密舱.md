---
title: SDC2024 议题回顾 | BULKHEAD：通过分隔化打造内核安全的水密舱
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458581829&idx=1&sn=6609aec959009ed4ed22d10f15a131b3&chksm=b18dcbcf86fa42d9ab1a35f5ddb9d21cbdcce149d7b3c986c7edb00bb322e3f50d65af9c977a&scene=58&subscene=0#rd
source: 看雪学苑
date: 2024-11-12
fetch_date: 2025-10-06T19:19:20.931641
---

# SDC2024 议题回顾 | BULKHEAD：通过分隔化打造内核安全的水密舱

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FcXdTqf7nDw2C85sW9icA1EeQy5J5Ib26mmopbOZnDAAcN2PicWUN5I6ZKmypSAzOdbtK6FyGIKNXQ/0?wx_fmt=jpeg)

# SDC2024 议题回顾 | BULKHEAD：通过分隔化打造内核安全的水密舱

原创

SDC 2024

看雪学苑

“

还在为挖不完的漏洞、打不完的补丁苦恼吗？不妨通过分隔化为潜在漏洞构筑安全“水密舱”，保障系统软件乘风破浪。

”

一起来回顾下郭迎港在SDC2024 上发表的议题演讲：《BULKHEAD：通过分隔化打造内核安全的水密舱》

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FcXdTqf7nDw2C85sW9icA1Ec5vmBhu1uficSw8afYZ90nxztC8yJgKiaIAz0TTRMWR95U4OHlwZHBdg/640?wx_fmt=jpeg&from=appmsg)

**郭迎港：南京大学计算机学院博士生**

师从曾庆凯教授，曾赴美国明尼苏达大学Prof. Kangjie Lu研究组做访问学者。主要研究方向为操作系统内核安全，包括内核特权分离和内核模块分隔化。研究项目基于最小特权原则增强内核安全，通过形式化建模分析各种特权分离方案的安全效果，并利用新的硬件特性结合程序分析技术实现内核模块的安全高效分隔化，限制内核漏洞的影响。相关成果发表于NDSS、ACSAC、ESORICS、软件学报等会议和期刊。

\*以下为速记全文

各位老师好，我是来自南京大学计算机学院的25届博士生郭迎港，今天很荣幸有机会和大家分享一下我们在操作系统内核安全方向的一些探索，议题题目叫BULKHEAD，也就是船舱与船舱之间隔板的意思。

接下来我们就看看如何通过在内核里边增加隔板来构建水密舱，从而有效地防止漏洞威胁的蔓延，避免整个系统的倾覆。

今天的报告主要分为这几个部分，首先我们介绍一下内核分隔化的背景，然后通过漏洞威胁来分析为什么需要分隔化，接着分享我们的解决方案以及它的实验效果。最后和大家开放性地探讨一下，除了操作系统内核，分隔化思想还能应用到哪些场景当中。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8FcXdTqf7nDw2C85sW9icA1ECG4wUISCrZrCJVicuZqYfcnJIAiaW0X6UXXj7Pgzlp7n89mv0fHeKtfQ/640?wx_fmt=gif&from=appmsg)

**01**

**背景概述：什么是内核分隔化**

内核是整个操作系统的基石，很多厂商现在也都有自己定制化的内核，那么从架构上来讲，可以分为两个大的阵营，宏内核以及微内核架构。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FcXdTqf7nDw2C85sW9icA1ELibzWznP5oKMqgyZ8Xxvroib5RHCNfg1cYA2aPHUgR0w6I607Micu06uQ/640?wx_fmt=png&from=appmsg)

以Linux为代表的宏内核，它的各个内核模块是处于同一地址空间当中，共享权限，模块之间可以高效地交互，但是缺乏故障隔离机制。任意一个薄弱的模块，特别像驱动，假如说出现一个漏洞，攻击者都有可能从这个漏洞出发，逐步地攻陷整个内核，颠覆整个系统。

相反，微内核把很多的内核模块分隔到不同的用户态进程当中，但这样一种安全隔离是以性能为代价的，因为模块之间的交互现在变成了进程间通信IPC，它需要陷入内核空间再返回，这样一来整个系统的开销就会有显著的增长。

如何来实现既安全又高效的内核架构呢？鸿蒙选择了一个微内核的技术路线，进行了全栈的自主研发，很大程度上去提升微内核的性能表现，具体的一些技术细节，推荐大家可以去读一下陈海波老师在今年OSDI上发表的一篇介绍鸿蒙微内核设计的论文。我们今天主要关注沿用宏内核架构的那些系统，特别是基于Linux Kernel的系统，对于这样一些系统而言，有没有机会以比较小的工程代价来获取安全保障上的提升呢？内核分隔化就是这样一种通用的、基础的防御解决方案。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FcXdTqf7nDw2C85sW9icA1Eto96D1VIqYgKNAsQlZUG28jnIgVKP54R5LWIibn4OKZ3dQ6gTEgB4nw/640?wx_fmt=png&from=appmsg)

我们类比造船的思想，通过增加一些隔板，把内核模块分隔到互不可信的安全域中。它不像微内核那样隔离到用户态进程当中，而是在内核内部，在内核的同一特权层，把这些模块分隔到单独的一个我们叫水密舱当中。这样一来，假如说薄弱模块出现一个漏洞，它的威胁仅仅会局限在单一的水密舱中，不会去影响其他的子系统，整个系统就不会被攻击者轻而易举地颠覆掉。

大家可能会觉得再怎么限制漏洞的影响范围，它不照样还能够被触发利用吗？值得注意的是，一次完整的攻击往往是由多步链接组成的。攻击者从最薄弱的模块如驱动入手，但是真正有价值的目标常常是在其他的内核模块，比如说文件系统、进程调度。如果我们做了细粒度的分隔化，就可以有效地阻断攻击链。即使单一的漏洞被触发，攻击者也无法实现攻击目的。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8FcXdTqf7nDw2C85sW9icA1ECG4wUISCrZrCJVicuZqYfcnJIAiaW0X6UXXj7Pgzlp7n89mv0fHeKtfQ/640?wx_fmt=gif&from=appmsg)

**02**

**威胁分析：为什么需要分隔化**

接下来我们就通过一些漏洞威胁来进一步地分析分隔化的必要性。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FcXdTqf7nDw2C85sW9icA1EgGfJ3aeRNFZyRUwVUjNAKWC0DVF2XTC8YovVsS2Xb6MLLDvKUEEr6Q/640?wx_fmt=png&from=appmsg)

随着像fuzzing这样的漏洞挖掘技术的不断发展，可以看到近年来内核漏洞的数量不断增长。并且内核仍然在不断的迭代，代码量还在不断的膨胀。可以说想要消除掉所有的内核漏洞显然是一个不现实的问题。那么除了被动地去做漏洞响应之外，我们亟需考虑如何主动地来应对潜在的漏洞威胁。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FcXdTqf7nDw2C85sW9icA1EEWZvwFAK9OzwHgNkc3e0DnwDKLNOe5tqCwhknr4lqYW8p23rx6BHvw/640?wx_fmt=png&from=appmsg)

从类型上来看，数量最多的漏洞类型仍然是内存损坏，接着是溢出以及输入验证相关的一些逻辑漏洞。这些类型的漏洞其实都可以通过对内存做分隔来进行有效的防控。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FcXdTqf7nDw2C85sW9icA1EejvOfK8sooNQq1TEZCpicJO9nl6pkldAmrhNZeJUMQiaSlbkvIPISJkg/640?wx_fmt=png&from=appmsg)

除了数量上层出不穷，我们可以看到 Linux Kernel的漏洞在各个子系统之间的分布也是非常广泛。各个模块多多少少都会有漏洞分布，虽然说网络驱动是最薄弱的，但是主内核的问题也不容忽视。因为我们没有办法预测下一个漏洞会出现在哪里，内核分隔化就应该考虑互不可信的威胁模型下的双向隔离。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FcXdTqf7nDw2C85sW9icA1EED6qSxaYR9eJfnYjT1DmnQibouSl81bM3oHEkIN9fHmMYwWc89YR71A/640?wx_fmt=png&from=appmsg)

刚才提到的主要是一些潜在的未知漏洞，其实对于已知的漏洞，修补也是非常困难的。我们做了一个统计，Linux kernel的漏洞从发现到补丁真正并入主线，平均花费66天的时间。如果我们再考虑供应链上下游的传播，一个补丁从主线到各个发行版，再到下游厂商自己定制的内核，传播时间会更长。这样一个漫长的漏洞修复时间窗口就给了攻击者发动N-day攻击的机会。分隔化可以及时地把出现问题的模块先放进一个沙箱环境里边去，限制它的影响，从而为我们进一步的根因分析、补丁开发来争取时间，避免N-day攻击的破坏。

总结一下，面对层出不穷，分布广泛，修补困难的漏洞困境，内核分隔化可以对已知漏洞起到一个防微杜渐的作用，对未知漏洞则可以防患于未然。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8FcXdTqf7nDw2C85sW9icA1ECG4wUISCrZrCJVicuZqYfcnJIAiaW0X6UXXj7Pgzlp7n89mv0fHeKtfQ/640?wx_fmt=gif&from=appmsg)

**03**

**解决方案：怎样实现分隔化**

隔离其实是一个非常传统的安全话题，我们先来比较一下各种隔离机制。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FcXdTqf7nDw2C85sW9icA1EzJcmjusdhrUry1HbrYJf3xjAG10kf9pAD6nSbnoicc4Dw6vL4cuZDaQ/640?wx_fmt=png&from=appmsg)

基于软件插桩检查的隔离也就是SFI为每一条访存指令插入检查来确保访存地址在合法范围内，大量的检查会显著降低系统性能。基于地址空间的隔离会用多套页表为不同地址空间构造不同的内存映射，但地址空间切换相较于函数调用也很耗时，并且跨地址空间传输数据需要进行复杂的拷贝。基于虚拟化的隔离通过二级页表也就是Intel的EPT构建不同的内存视图，vmfunc指令也支持高效的EPT切换，但这种方案依赖于更高特权层的hypervisor，引入了新的TCB也就是可信基，并且在云环境下还会面临嵌套虚拟化带来的挑战。相比而言，基于硬件机制的隔离可以通过软硬结合更好地平衡安全与性能，既不引入新的特权软件，还能实现高效访问控制和隔离域切换。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FcXdTqf7nDw2C85sW9icA1EwTicrQru9vAGibYpSiaOTh1KaHS7d3p8IFuuL4aBvRAia7J8Aho7pLvdibQ/640?wx_fmt=png&from=appmsg)

接下来就介绍一下我们基于Intel PKS特性的内核分隔化方案。这是整体的系统架构图。Intel PKS即Memory Protection Keys for Supervisors，是针对内核态页面的MPK变种，从12代酷睿和4代至强处理器开始支持。

从原理上讲，PKS使用页表项中的4位作为pkey也就是一种tag，从而可以将内存划分为2的4次方——16个不同的域。以一个新的per-thread寄存器PKRS对这些内存域进行访问控制，每个域都对应设置WD位即write-disabled不可写和AD位，access-disabled，不可读也不可写。

而我们就基于这一机制对Linux Kernel进行分隔。每个内核模块都用不同的pkey标记，LKM代表loadable kernel module。我们在配置内核时，选择为Y的功能就会编译进主内核，而选择为M的就会生成一个.ko文件，作为LKM加载至单独的分隔域中。当处于主内核域时，PKRS寄存器对应第一行的值，它设置主内核对其他内核模块的访问权限为10即不可写，所有的内核代码则设为01，既不可写也不可读，也就是我们稍后要介绍的应对控制流劫持的仅执行内存，自身内存资源则可以随意访问。通过更新PKRS寄存器可以高效实现分隔域切换，比如切换至其他行代表的内核模块就又会限制对主内核的访问权限，从而实现互不可信的模块间的双向隔离。

但记得我们开头强调过，宏内核原本是共享权限的，要是任意模块都能修改页表中的pkey或者更新PKRS寄存器的话，这种分隔化不就会被轻易打破吗？

为此，我们在内核内部通过特权分离构造一个in-kernel monitor，这是一个特殊的内核模块，只有它可以安全地更新页表和权限控制寄存器，并通过SGT即switch gate table中记录的元数据监管分隔域之间的切换和交互。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FcXdTqf7nDw2C85sW9icA1EDAMOIjI3mZPOHWjFwEiaf7xJSBicMrcvbicw6TAV9hSMibgbKDyleicLqOQ/640?wx_fmt=png&from=appmsg)

那么这个monitor是怎么构建出来呢？具体而言，特权分离的核心有两点，即管理内存资源的特权和管理寄存器资源的特权。

对于内存资源，我们确保页表页标有monitor域对应的pkey，这些页面对于其他域而言不可写，并为此hook所有页表分配和更新函数，切换PKRS至monitor，由monitor唯一负责页表管理。

而寄存器资源则涉及一些特权指令的执行，比如更新PKRS的wrmsr、加载页表基址的mov-to-cr3。我们必须消除monitor之外其他内核模块中的这些特权指令。由于x86是一个非定长的指令集，指令消除就必须考虑符合正常指令边界的intended指令，以及意图之外形成的unintended指令。

我们将正常指令流中的intended指令替换为跳转至monitor的switch gate，由monitor代为安全执行。而unintended指令则通过二进制改写消除掉。

以更新PKRS的指令0F30为例，假如其跨指令边界形成，则可以通过插入nop指令或者调整指令顺序来消除掉。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FcXdTqf7nDw2C85sW9icA1EDvHBolPvGp7o3PNSUIUDbKn1rq1fYwems4zST6gL4MVTvFKqibeTvHw/640?wx_fmt=png&from=appmsg)

假如其由一条更长指令的寄存器域构成，则可以通过寄存器重分配，把rcx改用rdx来消除掉。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FcXdTqf7nDw2C85sW9icA1ECibojn4QianPicnXTujCjmMe5N8qWicRJAHy7GdTDkicKrhQLVualrk8EPQ/640?wx_fmt=png&from=appmsg)

假如unintended指令由立即数组成，就可以进行数据调整。综合这些等效指令替换策略就可以保障只有monitor能够执行更新特权寄存器的指令，而其他内核模块不能借此破坏分隔化。

接下来我们看看内核分隔化设计如何全面应对各种安全威胁，包括数据篡改、控制流劫持和特殊的混淆代理攻击做好特权分离。

第一种典型威胁就是数据篡改，比如通过修改cred、file、inode等安全敏感数据对象实现提权攻击。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FcXdTqf7nDw2C85sW9icA1EM7zOQczOjicgUjv5St7J4pb3tibm3c1vbtvKYPchh7RRP9DgNjFRicQPg/640?wx_fmt=png&from=appmsg)

为此，分隔化保障了数据完整性。我们为每个分隔域实现了基于内存池的私有堆和私有栈。这些内存池都标记好了各自域的pkey，代表了内存对象的唯一所属权。通过hook内存分配函数确保每个域都使用属于自己的私有内存。

这样一来，堆漏洞和栈漏洞就都无法篡改其他域的数据。比如由于pkey不同，域1的堆溢出在试图影响域2时就会触发访存错误。

那么当域1真得需要向域2传递数据时怎么办呢？

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FcXdTqf7nDw2C85sW9icA1Eoopll3glxOC5VnmLhfZmn21nyj2BClYKE3MdZNrl5v7IYs9X0vlxkw/640?wx_fmt=png&from=appmsg)

对于共享数据，在首次跨域访存尝试触发错误后，我们在page fault handler中检查数据的合法性，检查通过后由monitor更新pkey即数据所属域，从而实现零拷贝的数据传输。

第二大类安全威胁则是控制流劫持，包括最传统的恶意代码注入和代码复用攻击，比如ROP以ret指令串联起代码中的若干gadget片段从而实现攻击。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FcXdTqf7nDw2C85sW9icA1EwiaBaaYjnxriaYxpyNG4BHViaX5lnibA7p6b7obPiadVIF04xicZqSxwAnDQ/640?wx_fmt=png&from=appmsg)

作为应对，我们选择了比控制流完整性CFI更加轻量高效的仅执行内存。代码区域不可写使得攻击者无法注入恶意代码，不可读再加上地址空间随机化使得攻击者难以找到有效gadget的位置来发起代码复用攻击。

最后介绍一种特别值得关注的混淆代理攻击，即攻击者模块利用接口混淆其他模块代其执行恶意行为。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FcXdTqf7nDw2C85sW9icA1EU83wib0myxDq8erjFVQ9kbMdFSUlibJFbZKqxjbdZYicg4fuGchxnoCqw/640?wx_fmt=png&from=appmsg)

这里看一个抽象的简单示例。假设LKM1不能访问LKM3内存而LKM2可以。但LKM1可以调用接口函数lkm12\_cpy来将size大小的mem1拷贝至mem2。

那么假如攻击者控制了LKM1，他就可以通过传入恶意参数，使得mem2实际指向LKM3的内存或者size溢出至LKM3的内存，从而混淆LKM2代理其破坏LKM3。

乍一听，大家可能会觉得这个例子有些奇怪，内核中对于这种类似内存拷贝函数的参...
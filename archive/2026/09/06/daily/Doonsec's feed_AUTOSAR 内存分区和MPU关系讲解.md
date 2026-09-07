---
title: AUTOSAR 内存分区和MPU关系讲解
url: https://mp.weixin.qq.com/s/auiNP3F8Tww1E9QgUJWThw
source: Doonsec's feed
date: 2026-09-06
fetch_date: 2026-09-07T06:48:07.957368
---

# AUTOSAR 内存分区和MPU关系讲解

# AUTOSAR 内存分区和MPU关系讲解

谈思实验室

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaAf3Eh4RynoftF7dz1NtAd2SYNXWsm8EaWOewRjSXxcCjicH0t59JtNOypwHKjHNlxV8CeJft7puVrzuEzoHibdHGKJ2Bhcc4iajI/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247579282&idx=2&sn=7e12011b5e25610e8be6a386580a3b98&scene=21#wechat_redirect)

**01**

**MPU的功能**

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9Tuic3xFCguSXSDwNzNQYdGEr2LgvllxxUiall8h124VpJAB8DZOD1aYfFbTSzdGFMyt6ewaoiarSnQ/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

**02**

**MPU功能简述**

MPU保护与当前执行的代码“不相关“的所有数据。

“不相关”是相关内存地址的权限受限制，或者是程序访问内存地址的范围于其无关，阻止关键数据被破坏，使嵌入式系统更加健壮与安全。

**03**

**MPU作用主要有两个方面**

为两个保护，一个检测。

**1）MPU的保护作用**

指访问区域的保护和读写区域的保护。

**① 访问区域的保护。**

可以将内存区域划为特权区域和普通区域，特权区域只有特权用户才能访问，普通用户被禁止访问，以此来保护特定的数据。

常见的应用场景：

1> 对带系统的来说，可以设置数据，以防止用户应用程序破坏操作系统使用过程中的数据。

2> 隔离任务,以防止一个任务访问其他任务的数据。

3> 将SRAM或者RAM空间定义为不可执行，防止代码注入。

**② 读写区域的保护。**

设置指定的区域为只读，可以有效的防止比较关键的数据被错误修改。

**2）MPU的检测功能**

指可以检测堆和栈的溢出情况及数组有没有越界。

**04**

**功能安全中对内存分区MPU的相关描述**

汽车ECU软件是高度模块化的嵌入式软件，其功能实现是可以为非功能安全，和功能安全的SWC组合，它们分别拥有不同的ASIL安全等级。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9Tuic3xFCguSXSDwNzNQYdGeImD5LOnl5fLGCA8kY6ceW9TUsYselZULHx5tw7zrS0WtVODB3YReA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

根据ISO26262，如果嵌入式软件包含不同ASIL等级的SWC，要么整个软件工程都需要基于最高安全等级的要求进行开发，需要保证拥有更高安全等级的SWC的操作不会受到其他SWC的干扰，也即需要做到FFI(Freedom from interference)的设计。

基于更低安全等级要求开发的SWC，可能会出现错误地访问到更高安全等级SWC的内存区域，产生干扰。

为此，SWC需要运行在不同的内存区域，或者不同的内存分区，来防止类似的内存访问违例。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9Tuic3xFCguSXSDwNzNQYdGBq6n97P1ichthe8SrpEniaQqNkc4biax0ibiaIwB7IJ6SpibTGv0vctr9W4Q/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)

ISO26262中，以下内存相关的故障影响被视为SWC之间产生干扰的原因：

* 内容损坏
* 读写区域属于另一个SWC
* 数据不一致
* 栈溢出或栈下溢

要满足上述定义，是MPU内存保护的目标，也可以通过限制对于内存以及内存对应的硬件的访问。

这里的内存分区意味着:

各OS Application运行在相互保护（不干涉）的内存区域，在某一个分区上运行的代码，无法修改另一个分区的内存。

内存分区也可以保护只读内存段（例如代码执行）以及内存对应的硬件。

内存分区和用户/特权模式可以保证SWC之前互不干扰——即使某一个SWC出现了内存相关的故障，也不会对其他软件模块有影响。

如果一个SWC运行在用户模式，那么它对CPU资源/指令的访问也是受限制的。

**05**

**MPU的微控制器有专用的硬件**

即内存保护单元（MPU），来支持内存分区。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9Tuic3xFCguSXSDwNzNQYdGfhIqEpHqNxA9qBCxblxP6WduHvaavggzD4rgDK0JIByde1JsVSByaQ/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=4)

若想深入理解上述的MPU描述，得先来看下，内存分区和MPU的基础知识。

**06**

**计算机程序执行的基础简介**

**内存**

计算机的主要作用是对输入数据进行处理和运算后输出，CPU处理器主要完成数据的处理运算，但输入输出数据包括处理过程中的临时数据需要有一个空间去存放，这个临时存放数据供处理器和外设使用的地方就是内存。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9Tuic3xFCguSXSDwNzNQYdG9lCO1W955Pn6qVjXa2WZic1domLuuIl3KDeAce2jVrAPeYiaFFMZlsyA/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=5)

如上图，为了提高效率把存放程序（也即控制指令）和数据（也即操作数）的空间分开，同时把访问指令与访问数据的总线分开，使取指令和执行指令能够重叠（处理器的流水线）。

**内存寻址**

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9Tuic3xFCguSXSDwNzNQYdGPalDibPnU441ibMvfHOknicJaySLicVS0Qz3rIpyrcdMtYZvV4A45W0EJw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=6)

处理器与内存之间有地址总线用于寻址，有数据总线用于传输数据，当然也有相应的控制线来读写操作。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9Tuic3xFCguSXSDwNzNQYdGhk6WqHlrk7iatGMm6JweXf2PkUpsFMvnzgAibtMHkbEhv8I6uBJ2FiaKQ/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=7)

存储器地址的映射简介

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9Tuic3xFCguSXSDwNzNQYdGgCAAxJiaVssL0icNiadQAiaAnKfPyxhEpy8QiaOuXbm1KC5q5ico5K8aVTxw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=8)

存储器本身不具有地址信息，它的地址是由芯片厂商或用户分配，如图所示，给存储器分配地址的过程称为存储器映射。

如果内核整体可以寻址的 0 到 2^32 -1 共计 4GB 的寻址空间。功能部件RAM, Flash,外设等共同排列在一个4GB的地址空间内。

**地址分配**

程序C语言通过这些地址可以访 问 RAM、Flash、外设等，进行读写操作。

C编译的程序占用的内存分为以下几个部分：

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9Tuic3xFCguSXSDwNzNQYdGKkT1530SCppPNjvwe1nWtKGDTnzDfTADwygDKMicNNCh5VsicnZePETQ/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=9)

***栈区（stack）***— 由编译器自动分配释放 ，存放函数的参数值，局部变量的值等。其操作方式类似于数据结构中的栈。

***堆区（heap）*** — 一般由程序员分配释放， 若程序员不释放，程序结束时可能由OS回收 。注意它与数据结构中的堆是两回事，分配方式倒是类似于链表。

***全局区（静态区）（static）***— 全局变量和静态变量的存储是放在一块的，初始化的全局变量和静态变量在一块区域， 未初始化的全局变量和未初始化的静态变量在相邻的另一块区域。

***文字常量区（.const）***—常量字符串就是放在这里的。

***程序代码区(.text)***—存放函数体的二进制代码。

**栈：**只要栈的剩余空间大于所申请空间，系统将为程序提供内存，否则将报异常提示栈溢出。MPU也支持堆栈溢出检测，简单如下图。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9Tuic3xFCguSXSDwNzNQYdGaxDeia4rddkRQb5tRzs2WWVvXaBdfq5ia0ca28DVpvNIW8Uf6Q2VlMQw/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=10)

**代码例子**

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9Tuic3xFCguSXSDwNzNQYdGv8KicpgJhWgj5ibgUbsJnAIMKcE5ibibFeoBZKc3YdaeKX5dm9oRcAMicnw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=11)

```
int a = 0; //全局初始化区int a = 0; //全局初始化区char *p1; //全局未初始化区main() {int b; //栈char s[] = "abc"; //栈char *p2; //栈char *p3 = "123456"; //123456\0在常量区，p3在栈上。static int c = 0; //全局（静态）初始化区    p1 = (char *)malloc(10);    p2 = (char *)malloc(20);//分配得来得10和20字节的区域就在堆区。strcpy(p1, "123456"); //123456\0放在常量区，编译器可能会将它与p3所指向的"123456"优化成一个地方。}
```

**07**

**MPU内存保护单元**

Memory Protection Unit

上文描述的内存区，堆栈区，数据区，代码区都可以被MPU保护，安全相关的微处理器通常都在硬件级别上支持内存分区保护，MPU主要是通过内存映射的地址范围限制，和监控非受信区域的内存访问来实现的。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9Tuic3xFCguSXSDwNzNQYdGrelqNW0H5PTOib4EkHwnhWzusqtjdztf3HWfjTwliaofFXHFvmTdyoRA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=12)

MPU可以保护的区域为内存映射区memory map，可以设置不同存储区域的存储器访问特性（如只支持特权访问或全访问）和存储器属性（如可缓存、可缓冲、可共享），对存储器（主要是内存和外设）提供保护，保护可执行程序的（data、code和stack）区域。

**08**

**MPU 的Region区域**

是可编程保护区域(需要控制器硬件支持)，如下图

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9Tuic3xFCguSXSDwNzNQYdGibyBmFaBoQd5TMVS9VwmfpvP5mCsicC5MYj8CX2DjNn1hfklzcJIOZfg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=13)

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9Tuic3xFCguSXSDwNzNQYdGP93ficODauo8pWYnCAicWvhvpC85vceiadHVbeuBMtTTZTOermqH9usWw/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=14)

MPU的配置是通过设置多个MPU寄存器，定义多个MPU region，每个MPU region的可配置选项包括: 被保护的起始地址，大小size,访问权限，所属硬件MPU分类，Region Owner 以及有效ID等。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9Tuic3xFCguSXSDwNzNQYdG5HBia3l5TSkdowTqFfIbaxTQeJzdIRgyic9HAkYETlqnr011ZEHLb1dQ/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=15)

MPU在执行其功能时，也是以“region区域”为单位的。

通过上述的MPU配置，各个软件模块将具备对不同memory区域的不同访问权限。

如图，一个region上述配置的一段连续的地址，它们的位置和范围都要满足一些限制。

MPU是可以管理所有的存储空间(如图 4G)，可以划分不同的Region内存区域，并为每个Region设置访问权限与规则，不同的Region允许相互重叠，重叠区域受多重访问规则的限制。

**09**

**Link命令对于内存的设置**

编译器关联的，可参考下面TI的解释

https://software-dl.ti.com/ccs/esd/documents/sdto\_cgt\_Linker-Command-File-Primer.html

**10**

**特权模式与用户模式**

是内核的执行模式。

当代码运行在特权模式下，代码拥有所有的访问许可；

而代码运行在用户模式，则访问权限受限制。

也是MPU中所定义的内存访问规则。

**11**

**AUTOSAR中的定义**

内存分区的定义

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9Tuic3xFCguSXSDwNzNQYdGrtYcCYJibBoYo69lC2NaPcRW3kYohOuAwM1y815AX1TGH1JsMHE3JEA/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=16)

如上图，一般来说

* BSW模块运行在授信模式/监控者模式内存分区当中。
* 部分SWC分组并放置到非授信/用户模式内存分区当中。
* 个别SWC也运行在授信/监控者模式内存分区当中。

项目中可以有多个非授信/用户分区，每个分区都可以包含一个或多个SWC。

上图中，分区是以应用软件OS-Application为对象定义的，OS-Application和内存分区（Partition）之间，是一对一的关系。

**12**

**如何理解OS-Application？**

如下图中，应用程序内的 AUTOSAR SWC

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9Tuic3xFCguSXSDwNzNQYdGVqxiatha3WCTKTzRz0xakWCKdEh9R8FknUK2l5XCB6ZbmpkdBBuYfmQ/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=17)

在AUTOSAR架构中，应用程序位于RTE之上的，基于应用功能逻辑定义，内部包含一组存在信息交换的软件组件（SWC）。

软件组件SWC是实现一系列的原子功能（最小单元不可拆分），SWC包含一系列的功能实现和变量定义，这些功能实现和变量定义对于外部是不可见的，仅能通过公布的RTE接口使用。

SWC以周期性执行或者以外部触发的runnable中执行。

从分配的角度来看，一个SWC可以由多个Runnable构成，一个OS-Task可以触发多个Runnable（同一个SWC内的Runnable可以在不同的OS-Task上执行），一个OS-Application可以管理多个OS-Task。

**13**

**AUTOSAR OS-Application**

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9Tuic3xFCguSXSDwNzNQYdGbfEDVLsnGAVWvJoZjdU3h5M21F3Ax8Y6VSwohicQZUynhmibzwgRYJSw/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=18)

AUTOSAR的OS-Application是操作系统对象的集合体，其中包括任务 (Tasks)，中断服务程序 (ISRs)，调度表 (Schedule Tables)，计数器 (Counters)和警报 (Al...
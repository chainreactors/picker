---
title: NDSS 2025｜ 抖音集团安全研究团队提出机密沙箱内存管理方案WAVEN
url: https://mp.weixin.qq.com/s?__biz=MzI1MzYzMjE0MQ==&mid=2247512487&idx=1&sn=2084969d835f481f70244a795d40aa77&chksm=e9d37a45dea4f353de5073b43f01ea2fbbc38b9a87692a5ebefb7ecee0daa6bf6aee12009547&scene=58&subscene=0#rd
source: 字节跳动技术团队
date: 2024-12-21
fetch_date: 2025-10-06T19:39:19.793403
---

# NDSS 2025｜ 抖音集团安全研究团队提出机密沙箱内存管理方案WAVEN

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5EcwYhllQOh3EmPBRCmPFzesXmw8m5EMTHWkGZt2co5rwUTCTG3WuMb0iblFyJZsjKsjMJn3CMR9c2X3dGtkUsw/0?wx_fmt=jpeg)

# NDSS 2025｜ 抖音集团安全研究团队提出机密沙箱内存管理方案WAVEN

原创

安全研究团队

字节跳动技术团队

抖音集团安全研究团队和南方科技大学可信系统安全实验室合作的研究论文《WAVEN: WebAssembly Memory Virtualization for Enclaves》，于近日入选信息安全领域国际顶会NDSS 2025。

# **一、概述**

NDSS会议（Network and Distributed System Security Symposium）是网络与信息安全领域的四大顶级会议之一，也是中国计算机学会推荐的网络与信息安全领域A类国际学术会议。会议以其高水准和创新性著称，近五年平均录用率约为17%，涵盖密码学、攻击防御、隐私保护等主题，是推动信息安全发展的重要平台。

本次入选的研究论文聚焦于为运行在可信执行环境（TEE）内的WebAssembly（Wasm）运行时设计一套适合机密计算的内存管理方案，以实现机密计算环境中Wasm模块之间的高效数据共享，并支持细粒度的内存访问控制。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOh3EmPBRCmPFzesXmw8m5EMpRoxzGzicelI4nRj39iaE74xiacYzAYYmZyKIhCeMkUic18GYjYdphjaCg/640?wx_fmt=png&from=appmsg)

# **二、研究背景**

可信执行环境（TrustedExecution Environments, TEEs）是一种硬件扩展，为机密应用程序提供了名为飞地（enclave）的安全容器，能够有效保护私有数据及计算的机密性和完整性。英特尔SGX是目前广泛部署的TEE之一，其成功极大地推动了机密计算范式的发展，并为WebAssembly（Wasm）带来了新的机遇。

Wasm是一种新的可移植、轻量级的二进制格式，也是许多高级语言（如C、C++和Rust等）的编译目标。用其他语言编写的程序首先被编译成Wasm格式，然后可以在Wasm运行时中作为模块执行。通过强制每个模块只能访问其自己的内存区域，Wasm为不受信任的代码提供了一个安全的沙箱执行环境，这是其最显著的安全特性。由于机密计算平台需要同时执行来自多个用户的不可信代码，因此需要在飞地内实现多租户和隔离功能，而这正是Wasm所提供的。

Wasm和TEE的结合实现了飞地内多租户隔离，使得这一搭配非常适合机密计算场景。然而，Wasm的线性内存模型缺乏有效的跨模块数据共享和细粒度的内存访问控制，这大大限制了其在机密计算中的应用。在机密计算领域，常见的情况是多个数据用户共享一份机密数据，并且只允许少数特权用户（例如数据所有者）对数据进行修改，例如机密函数即服务（FaaS）平台，机密数据交易市场等场景（如下图所示）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOh3EmPBRCmPFzesXmw8m5EMeJlpFiciaic8y0cEWNXDn9uWszK8GrqibPHaI99EZHbxRgsAXtAmIQPRUQ/640?wx_fmt=png&from=appmsg)

针对上述问题，本项目主要研究英特尔SGX内Wasm运行时的内存管理，以使“Wasm+TEE”这一设计范式能够更好地契合机密计算需求。具体而言，本项目提出了一种面向可信Wasm运行时的内存虚拟化方案，在SGX飞地内实现了多个模块之间的安全高效数据共享。

# **三、技术方案**

为了应对前述挑战，研究团队设计了WAVEN（WebAssembly Memory Virtualization for Enclaves）内存虚拟化方案。WAVEN旨在支持飞地内Wasm模块间的高效内存共享，并实现内存页粒度的访问控制。其核心设计包括以下几个方面：

## **3.1 分页方案**

研究论文中提出的分页方案支持任意页大小，但根据Wasm规范，我们将页面大小设置为64KB。对于一个32位的Wasm地址，其较高的16位表示页索引，而较低的16位表示页面内的偏移量。

一个Wasm模块最多拥有4GB内存空间，即65536个内存页面。页表将Wasm模块的32位地址（0x00000000~0xFFFFFFFF）转换为Wasm运行时中的64位虚拟地址。我们采用了单级页表来减少查表次数，从而减少内存虚拟化带来的开销。因此，一个模块所对应的页表由65536个条目组成，每个条目包含一个64位的虚拟地址。在这种设置下，一个页表仅占用512KB内存空间。

在将Wasm地址翻译成64位虚拟地址的过程中，Wasm运行时首先提取Wasm地址高16位作为页索引，查找页表以获取该Wasm页面的虚拟地址，然后加上低16位所代表的页内偏移量来计算要访问的虚拟地址。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOh3EmPBRCmPFzesXmw8m5EMFn99jZjyhXGdueWMHcGRdoyJIMyUx2WuGkic74icPGicN5ZW0icAvkgC9g/640?wx_fmt=png&from=appmsg)

上图展示了前述分页方案，箭头表示从Wasm页到虚拟页的映射（即一个页表项）。注意到，相邻的Wasm页面可以映射到非相邻的虚拟页面。与线性内存模型相比，分页在该地址翻译过程中引入了一个额外的内存读取。

## **3.2 内存隔离与访问控制**

WAVEN通过控制页表项来实现不同Wasm模块间的内存隔离。在模块实例化过程中，Wasm运行时不仅为其分配初始内存页，同时也为其创建了一个64KB大小的空异常页。对于初始内存空间内的Wasm地址（合法内存访问），Wasm运行时将它们对应的页表项设置为所分配的内存页的虚拟地址；对于初始内存空间之外的Wasm地址（越界内存访问），Wasm运行时会修改相关页表项使得他们指向异常页面。因此，当Wasm模块执行越界访问时，地址翻译流程会将非法地址指向模块的异常页，这可以有效地防止该模块干扰或者访问其他模块的内存。

与现代计算机系统中的分页方案类似，WAVEN也需要处理未对齐内存访问：完全位于64KB页面内的非对齐内存访问不需要关注，而那些跨越页面边界的非对齐内存访问则需要特殊处理。考虑到跨页访问的高开销和低发生概率，WAVEN禁止跨页访问——它为每个虚拟页填充若干个字节，以确保所有内存访问都位于单个虚拟页内。由于一个Wasm访存指令最多读写8个字节（不考虑SIMD指令），我们将页填充大小设为7字节。

访问控制方面，由于每个Wasm模块都有自己的页表，WAVEN利用双页表来实现高效的内存访问控制。

具体而言，WAVEN使用两个独立的页表来进行读取和写操作：写页表处理内存写操作，并存储可写Wasm页的虚拟地址；读页面表则用于内存读取，并存储可读Wasm页的虚拟地址。可写Wasm页的页表项在读、写页表内是相同的，均指向对应虚拟页的虚拟地址。对于只读页而言，在读页表中与只读页指向有效的虚拟地址；而在写页表中，只读页指向异常页的虚拟地址。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOh3EmPBRCmPFzesXmw8m5EMDzQPWRXI2c6wAweaA1GiaQNSxABr8DFgXia4IWJpXzJ4mrSTqesvvichQ/640?wx_fmt=png&from=appmsg)

上图是对WAVEN内存隔离和访问控制方案的说明，异常页用红色高亮部分表示，页填充则用黑色细长条矩形表示。同时，在该模块的读页表中，Wasm页面3被映射到一个普通的虚拟页面；但是，在写页表中，它被映射到异常页。因此，该模块可以读取Wasm页面3的内容，但不能对其进行修改。这种细粒度的访问控制在共享内存场景中特别有用。在共享内存场景中，多个Wasm模块可能需要读取共享内容，但不能随意修改它。此外，只读页面的引入也提高了Wasm内存管理的安全性。

## **3.3 内存重映射**

在WAVEN中，页表项将Wasm页面映射到虚拟页面，这允许Wasm运行时特定覆写页表项来将Wasm页面轻松地重新映射到另一个虚拟页面。这种内存重映射特性极大地促进了多个Wasm模块之间的共享内存，因为不同模块可以将它们的Wasm页面都映射到相同的虚拟页面上，实现数据共享。此外，通过将内存重映射与前述内存访问控制相结合，可以对共享内存区域规定只读权限，这意味着一些模块只能从共享内存中读取内容，而另一些模块还可以拥有修改权限。

# **四、总结**

WAVEN通过创新的设计方案解决了Wasm线性内存模型的局限，满足了机密计算中对高效数据共享和访问控制的需求。其实现已在WAMR运行时及英特尔SGX环境中成功部署，并在多种测试中展示了良好的性能表现。研究结果表明，WAVEN在PolyBench测试套件平均引入10.42%的开销，在高并发数据共享场景下性能最高提升2.4倍。

WAVEN目前已经被纳入到Jeddak数据安全沙箱的能力矩阵中，在端云融合计算、数据共享计算等多类场景模式下，为用户挖掘和创造更多数据价值。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOhkoWTP1gVm0Lqs480XOARyoSYjPEsRVCSF35cbWIp6cliaYic8KUfNfiaSjVnruzTQUTCA0lmv9vUmw/0?wx_fmt=png)

字节跳动技术团队

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOhkoWTP1gVm0Lqs480XOARyoSYjPEsRVCSF35cbWIp6cliaYic8KUfNfiaSjVnruzTQUTCA0lmv9vUmw/0?wx_fmt=png)

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
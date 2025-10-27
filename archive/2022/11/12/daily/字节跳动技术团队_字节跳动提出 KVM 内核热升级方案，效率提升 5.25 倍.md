---
title: 字节跳动提出 KVM 内核热升级方案，效率提升 5.25 倍
url: https://mp.weixin.qq.com/s?__biz=MzI1MzYzMjE0MQ==&mid=2247499903&idx=1&sn=2ffb5e2e3f25ed5ee0553c6e817e084c&chksm=e9d30b9ddea4828becc92cd2629676b5ee634d6a70916b00c123f4739263ec53518f7cb97ce7&scene=58&subscene=0#rd
source: 字节跳动技术团队
date: 2022-11-12
fetch_date: 2025-10-03T22:34:25.919147
---

# 字节跳动提出 KVM 内核热升级方案，效率提升 5.25 倍

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/5EcwYhllQOiagibiaKaEsDOTqHsNpfU2rGPHxaD1LrvicUOrFqMe0aG6icK41a25WD58OicXA14qjx2xwbicA7TRgufKw/0?wx_fmt=jpeg)

# 字节跳动提出 KVM 内核热升级方案，效率提升 5.25 倍

Fam Zheng

字节跳动技术团队

**动手点关注**

**![](https://mmbiz.qpic.cn/mmbiz_gif/JaFvPvvA2J063TNzibibGfI89U9UaWNPqYGUFNRVJ1TkA4Bv0Ew946EkhX4dNibLx6ZK9E4ibdtqH01ZGs9a4gvo4w/640?wx_fmt=gif)**

**干货不迷路**

#

1. **介绍**

作为云计算最重要的底层基础之一，KVM 虚拟化软件在现代的数据中心中应用非常广泛。基于 KVM 的 hypervisor 包括了构成宿主机的软硬件，共同为虚拟机中的应用程序提供高性能的 CPU、内存和 IO 设备等资源。在大规模部署的生产环境中，作为云服务提供商（Cloud Service Provider），如何从技术上保证软硬件的可运维性，一直是大家重点关注的问题。

为了给用户提供稳定、安全、高效并且功能丰富的云资源，IaaS 的底层软件必须能够支撑软硬件的各种运维需求。例如，在偶然出现一些难以避免的硬件故障时，需要能够把虚拟机及时热迁移到健康的宿主机；或者，在软件安全漏洞或功能缺陷被修复后，能够通过热升级，及时部署上线到生产环境中。

然而实现用户无感知地热迁移和热升级，却是一个复杂的系统工程问题。因为 KVM 虚拟化涉及众多不同层次的组件、诸多特性和灵活可选的组合方式，其中不乏一些非常复杂的软硬件技术例如 SR-IOV、Linux 内核、QEMU、DPDK、KubeVirt 或者 OpenStack 等，系统总体架构复杂度很高。而且这些软硬件模块各自都有复杂的接口和内部状态，在不影响虚拟机正常运行的情况下，要做到宿主机软件的热升级和热迁移，还需要做一些针对性的设计或改造。同时，作为云计算底座的一部分，它们也需要紧密的配合才能完成预期的功能。特别是对于内部状态处理能力要求非常高的热升级功能，更需要深入、全面的打通。

目前，在各个开源社区（如 Linux，QEMU，CloudHypervisor 等）和各大云计算公司，都在积极的尝试对 KVM 的热升级支持进行研发，也是历年各大技术峰会的一个重要研讨主题。字节跳动技术团队从实际场景出发，相应地对热升级问题进行了深入分析，与开源社区紧密合作，从多个角度做出了深度探索并取得了进展。

在今年 9 月份举行的虚拟化领域全球技术峰会 KVM Forum 上，**字节跳动系统技术****与****工程团队**（System Technologies & Engineering，简称 **STE** **团队**）公布了相关的技术成果：**首次提出一种在 KVM 热升级场景中透明支持** **PCI** **直通设备的方案，****能够显著降低内核热升级的实现成本**。通过对 host 内核和 QEMU 的扩展和改进，可以做到不依赖于特定硬件修改或者 guest 配合的热升级，支持 PCI 直通设备。同时，在性能方面，也通过深入的分析和优化，将一次内核热升级所需的最少时间（downtime）从 **1000****ms** **降低至** **160ms** **，效率****提升 5.25 倍****。**

本文将整理回顾 KVM Forum 大会中分享的主要技术方案，以飨读者。

> KVM Forum 会议演讲视频链接：
>
> Preserving IOMMU States During Kexec Reboot：https://share.weiyun.com/Mz3Wk6v8

# 2.  **IOMMU** **状态保持**

PCI 设备直通在当前数据中心的 KVM 虚拟化场景中广泛应用，能够为虚拟机中的应用提供高性能的 IO 设备。同时，直通设备的使用也为云计算底层软件设施的运维带来了一些复杂度。

其中，对热升级和热迁移的兼容性是 PCI 直通设备的一大难点。这是因为热升级或热迁移操作依赖于对虚拟机状态的提取、保持、传输等操作，而 PCI 直通设备的状态数据对于宿主机侧的 hypervisor 是不透明的。因此在 IaaS 的实践中，往往需要对使用了直通设备的虚拟机进行特殊处理。例如，通过定制的 SR-IOV 硬件，实现 PF 管理 VF 状态的逻辑；或者在虚拟机中运行特殊的驱动程序和 agent 进程，通过 guest 在过程中的协同配合来完成热迁移或热升级操作。

这些方法可以在一定程度上解决 PCI 直通设备的运维难题，但是带来了更高的研发成本、软件和配置的复杂度，也有可能会牺牲用户体验和 IO 性能。

## 2.1  **技术方案调研**

在 KVM 中对 PCI 设备的直通需要通过 VFIO-PCI 接口来完成。VFIO-PCI 是 Linux 内核对 IOMMU 和 PCI 底层逻辑的抽象封装 API，提供给运行在用户态的 QEMU 或者其它 VMM（Virtual Machine Manager）软件来配置虚拟设备的 IO 映射关系，从而允许虚拟机内核驱动直接访问硬件资源，以达到较高的 IO 效率。

在热升级过程中，虚拟机的运行状态需要被稳定的保持在升级之前的状态，其中包括虚拟机的 CPU 状态（寄存器里的数据等）、内存数据、虚拟设备的接口状态和内部状态等。对于 PCI 直通设备来说，有 2 个思路：

1. 设法提取设备的状态数据，备份在预先设计好的位置（如预留的内存或者磁盘），然后在热升级结束之前，从备份中恢复。提取备份的过程，一般称之为序列化；从数据中恢复状态的过程称之为反序列化。

2. 不提取设备状态数据，并在热升级过程中完全不改变设备状态。热升级完成后，虚拟机继续访问这个硬件设备。

前一种思路已经被证明是可行的方案，并且在某些较新的硬件中已实现，它的优点是不仅可以用来热升级，也可以用来热迁移；在热迁移过程中，虚拟机会被转移到不同的物理机上，也就不可能再使用同一个设备。但是，这个方式的缺点是必须有硬件支持，同时因为存在序列化、反序列化的操作，完成热升级所需时间较长。

我们对第二种情况进行调研和实验后发现，通过对 Linux 内核进行一些局部的修改，在 Intel IOMMU 上可以实现在热升级过程中，设备状态的完全隔离和保护，从而得到一个 PCI 透传设备的热升级通用支持方法。

## 2.2 **解决方案**

本文提出的方案主要包括三个部分：

**改进一：通过在 hypervisor 中引入必要的静态页面分配，保证 kexec 重启过程中的状态保持。**

静态分配主要有用户态和内核态两部分工作。其中，用户态的工作方式为：

1. 虚拟机的 RAM 使用 memmap 方式分配，在 host 侧使用 DAX 的形式管理。memmap 是一个内核参数，可以为物理内存分配不同的属性。其中 E820 type 12 是一个 NVDIMM 类型（例如 memmap = 2G!6G）。
2. 这个类型的物理页，将不再被内核动态管理，而是作为“非易失性内存”来看待。在启动后，我们可以通过创建一个 DevDax 字符设备，mmap 到 QEMU 的地址空间。
3. DevDax 的创建可以使用系统调用，也可以用 ndctl 命令：

```
  ndctl create-namespace -m devdax
```

4. 该命令会创建一个类似 /dev/dax1.0 的字符设备。这个字符设备提供一个支持 DAX（Linux内核提供的直接物理地址访问机制）的 mmap 接口，可以直接将物理内存映射到 QEMU 用户态。QEMU 命令行参数如下：

```
$qemu ... -object memory-backend-file,id=mem,size=2G,mem-path=/dev/dax1.0,share=on,align=2M \ -numa node,memdev=mem
```

5. 而后 QEMU 会通过 KVM 接口把这段预留内存用于填充 EPT 页表。

**改进二：** **内核态****的静态分配实现需要通过一个内核补丁来实现**

1. 我们在内核中引入了一个新的物理页管理器 KRAM，为其它模块提供 2 个分配页的函数接口。这两个接口的主要目的是提供静态物理页给硬件相关模块。

1. kram\_get\_fixed\_page(area, index)
2. kram\_alloc\_page()

2. 在 E820 的 enum 中定义新的 type 用以预留物理页给 KRAM：memmap=\*:\* 。
3. 在 Intel 的 IOMMU 驱动模块中，使用 kram 接口来分配 root page 和 DMAR page。包括`iommu_alloc_root_entry`和`alloc_pgtable_page`等函数中，将原本的`alloc_pgtable_page`替换成对 KRAM 模块的调用。

**改进三：对** **VFIO** **设备简化，保证硬件状态不被干扰**

在 VFIO - PCI 相关系统调用（VFIO\_GROUP\_SET\_FLAGS）中，我们加入了一个新的标志位，用以在 QEMU 热升级过程中，跳过对 VFIO - PCI 设备的初始化和重置。

*第二、三部分的相关代码将会在后续开源。*

## 2.3 **PoC** **验证**

目前我们在 QEMU 模拟环境中对上面的方案进行了实验。借助 KVM 在 Intel CPU 上的嵌套虚拟化支持，和 QEMU 对虚拟 IOMMU 的支持，可以很快的启动一个测试环境：

```
$qemu -machine q35 -device intel-iommu,intremap=on-cpuhost... -device e1000e,netdev=guestnet
```

上面的命令启动的嵌套虚拟化的 L1，运行的是增加了 VFIO - PCI 热升级的内核。对 L1 里安装的 QEMU 同样也加入了 CPR（Checkpoint Restore）和 VFIO - PCI 的扩展调用。

使用 VFIO - PCI 我们分配上面的虚拟 e1000e 网卡给 L2：

```
$qemu ... -device vfio-pci,addr=06.0,host={dev}
```

然后，通过 cpr-save -> kexec -> 启动 qemu -> restore 的流程来热升级整个  L1。

在测试过程中采集到的时间记录如下：

![](https://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOiagibiaKaEsDOTqHsNpfU2rGPC48r7QDbaqxYWyNkYHwdthSherPYJgMnX8bJdanicd3T3mRPgwNYc4g/640?wx_fmt=png)

从暂停虚拟机，到重启以后虚拟机恢复运行并在虚拟网络上继续发包，一共经过了 159ms。虚拟 e1000 网卡在这个过程中没有被 reset，始终保持运行状态。也就是说从外部或者应用视角来看，因宿主机热升级而导致的总响应时间，仅仅增加了不到 160ms 的时长，并且由于网卡的 rx 队列始终可用，在流量较低的情况下，也不会导致丢包和重传。

相比之下，如果用内核和 QEMU 的主线版本来执行上面的流程，可以采用 savevm 到磁盘后 kexec 重启并 loadvm 的步骤。但是这样不仅不能支持 VFIO - PCI 设备，也会因为缺少各种优化（如：savevm/loadvm 需要复制虚拟机内存），产生 1000ms 以上的 downtime 延迟。

# 3. **结论**

在使用 VFIO - PCI 透传设备的宿主机上，部署了具有上述改进的 host 内核和 QEMU 等程序。在测试中，基于 QEMU 通用的 checkpointing and recovery（CPR）框架，我们现可以支持低损耗的 host 内核热升级动作。从暂停虚拟机，到重启进入新内核并继续执行虚拟机，整个过程可在 160ms 左右完成。

此技术方案可被应用在公有云和私有云的 IaaS 业务场景，具有很高的实用价值，能够显著降低运维成本，提高云的安全性，并优化运维过程中的虚拟机运行性能和客户体验。字节跳动系统与技术工程团队将会继续优化 Linux 内核和虚拟化软件，为数据中心持续提供安全、稳定、高效运行的系统软件。

此外，在 Virtio 设备标准，QEMU 热升级，Linux 启动时间，io\_uring，kexec 等方面，团队也进行了深入的研究和优化。我们将会在本文和后续文章中持续分享相关技术和最新进展。

> **引用链接**
>
> CPR（Checkpoint Restore）:
>
> https://patchew.org/QEMU/1658851843-236870-1-git-send-email-steven.sistare@oracle.com/

# 4. 关于 STE 团队

字节跳动 STE 团队，一直致力于操作系统内核与虚拟化、系统基础软件与基础库的构建和性能优化、超大规模数据中心的系统稳定性和可靠性建设、新硬件与软件的协同设计等基础技术领域的研发与工程化落地，具备全面的基础软件工程能力，为字节上层业务保驾护航。同时，团队积极关注社区技术动向，拥抱开源和标准，欢迎更多同学加入我们，一起交流学习。点击【阅读原文】查看招聘岗位信息。

欢迎大家投递简历至：**huangxuechun.hr@bytedance.com；**  **wangan.hr@bytedance.com。**

![](https://mmbiz.qpic.cn/mmbiz_png/7QRTvkK2qC6RyGcCclHibMw08rYZOOtkfZud4IA4b3ORre5LScE0yBXTg19E6cQ4XbOP7iaWfVREuT3Dgxc4p3hw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_gif/7QRTvkK2qC7IHABFmuMlWQkSSzOMicicfBLfsdIjkOnDvssu6Znx4TTPsH8yZZNZ17hSbD95ww43fs5OFEppRTWg/640?wx_fmt=gif)

[● 深度解析字节跳动开源数据集成引擎](https://mp.weixin.qq.com/s?__biz=MzI1MzYzMjE0MQ==&mid=2247499707&idx=1&sn=251376ec0a2dec2d0e40dea5fd6c68d9&chksm=e9d33459dea4bd4fa1578f1dead154855c177bdad34e7357bb575d16b8fd9ae6907d10b56a76&token=785874804&lang=zh_CN&scene=21#wechat_redirect)BitSail

[● AB 实验为何值得信赖？](http://mp.weixin.qq.com/s?__biz=MzI1MzYzMjE0MQ==&mid=2247499793&idx=1&sn=3ae074560dd4630d3c64cb7dac0a157c&chksm=e9d30bf3dea482e5b922b9cd86ce8d6b156eb1c2219aaadbed2cdf9ead169c3a309694a4c61b&scene=21#wechat_redirect)

[● Android 插件化中资源错乱的解决方案](https://mp.weixin.qq.com/s?__biz=MzI1MzYzMjE0MQ==&mid=2247499708&idx=1&sn=4f30a9f5acc0a8c563c1e9323095a47d&chksm=e9d3345edea4bd48c44521c0ffb25999a5ea32cb03c7abd7be06b844023c20be9ba4d53fb9b2&token=785874804&lang=zh_CN&scene=21#wechat_redirect)

[● 【字节跳动技术沙龙】抖音 Android 基础技术大揭秘!](https://mp.weixin.qq.com/s?__biz=MzI1MzYzMjE0MQ==&mid=2247499750&idx=1&sn=c7fc5b6c7b0bcbec73a6f318014d2a58&chksm=e9d33404dea4bd128356318818a80f416a31bc9cf09aa74c6dc99e074a96a9b7f8c0b9a4f256&token=785874804&lang=zh_CN&scene=21#wechat_redirect)

****![](https://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOia2iaibTtxS07yz5OzyDhIBx1qbKx6I2nU2hVIL34oAWvJ1aQTHgFKX8QzdhtFDq2sk19UxydLypTyA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1) 戳**“阅读原文”，了解更多岗位信息！**

预览时标签不可点

阅读原文

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
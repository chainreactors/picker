---
title: Android Pixel 10 零点击漏洞利用链
url: https://mp.weixin.qq.com/s/0aU9fIxjJLzIBESNPv5z8Q
source: Doonsec's feed
date: 2026-05-22
fetch_date: 2026-05-23T05:38:19.741108
---

# Android Pixel 10 零点击漏洞利用链

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ibO9kiauylaDqiayH120s6BAhFqLOZEE1yAt5dhLzL7QFwmfUAMRp9l3m25YNx5Jlicibswmlg9LNxMgszBUfpf7zicicoSX7x9clBjwGQABtRE4Fw/0?wx_fmt=jpeg)

# Android Pixel 10 零点击漏洞利用链

白帽子

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于黑鸟
，作者Noname

![](http://wx.qlogo.cn/mmhead/X4XEGYefSBSxrDYncLtKiacf7vZpHQnuLDMVc1rQjZsw9xYSM6kSCezibImssYuBjTibclnyop737M/0)

**黑鸟**
.

一介草民，深耕威胁情报领域多年，自封威胁分析师，APT狩猎者，战略忽悠分析师。 专注推送一切前沿高科技/人工智能、网络安全分析、敌我战略分析、数据挖掘、情报扩线、网络武器分析、社会工程学、一切开源情报、军事分析忽悠等。

2026 年 5 月 13 日，Google Project Zero 安全研究员 Seth Jenkins 发布了针对 Google Pixel 10 的完整零点击漏洞链研究报告。该研究展示了攻击者如何在无需用户任何交互的情况下，仅通过两个漏洞就能从远程直接获取 Android 设备的 root 权限。

这是继今年早些时候针对 Pixel 9 的类似漏洞链之后，Project Zero 团队在移动安全领域的又一重要发现。

相关阅读：[Android Pixel 9 的零点击漏洞利用链全解析：从发送杜比音频解码到内核提权](https://mp.weixin.qq.com/s?__biz=MzAxOTM1MDQ1NA==&mid=2451184838&idx=1&sn=d4c35e35eca232ae996a5d4c50d06b08&scene=21#wechat_redirect)

### 主要内容：

* 他们把之前用于 Pixel 9 的 **Dolby 零点击漏洞**（CVE-2025-54957）稍作修改后，成功适配到 Pixel 10。
* Pixel 9 使用的 BigWave 驱动已被移除，但他们在 Tensor G5 芯片的 **VPU 视频解码驱动**（/dev/vpu）中发现了一个**极其简单的新漏洞**。
* 这个 VPU 漏洞允许任意 App 通过有缺陷的 mmap 函数，把**整个内核内存**映射到用户空间，实现对内核代码和数据的**完整读写**。
* 整个利用过程代码非常少，开发完整 root 漏洞只需不到一天时间。

Google 这次修复速度较快（71 天），严重程度评为 High，但文章指出 Android 驱动中仍不断出现明显且严重的代码质量问题。

目前仅影响未安装 2025 年 12 月及之后安全补丁的 Pixel 10 设备。

## 第一环：更新后的 Dolby 解码器漏洞

##

研究团队首先将之前用于 Pixel 9 的 Dolby 解码器漏洞 CVE-2025-54957 移植到了 Pixel 10 设备上。这个漏洞存在于 Android 系统的 Dolby Universal Decoder 组件中，影响所有运行未打补丁系统的 Android 设备，直到 2026 年 1 月才被官方修复。

移植过程相对简单，主要工作是将针对 Pixel 9 计算的库文件偏移量更新为 Pixel 10 对应版本的偏移量。

唯一的挑战来自 Pixel 10 引入的新安全机制。

Pixel 10 使用 RET PAC 替代了传统的栈保护机制 fstack-protector，这意味着攻击者无法再通过覆盖\_\_stack\_chk\_fail 函数来执行任意代码。

经过多次尝试，研究人员找到了一个替代方案。

他们选择覆盖 dap\_cpdp\_init 函数，这是解码器初始化时调用一次且之后不再使用的初始化代码。

覆盖该函数不会影响解码器的正常功能，同时能够实现代码执行。更新后的 Dolby UDC 漏洞利用代码已经公开，仅适用于 2025 年 12 月及更早安全补丁级别的未打补丁设备。

## 第二环：BigWave 消失，VPU 登场

##

将 Pixel 9 漏洞链的本地提权部分移植到 Pixel 10 并不可行，因为 Pixel 10 不再搭载 BigWave 驱动。然而，研究人员在 mediacodec SELinux 上下文中发现了一个新的设备节点 /dev/vpu。

这个驱动用于与 Tensor G5 芯片上的 Chips&Media Wave677DV 视频解码加速器进行交互。

根据开源代码中的注释，这个 VPU 驱动与之前的 BigWave 驱动由同一组开发人员编写和维护。

Project Zero 团队与 Jann Horn 合作，仅用了两个小时审计这个 VPU 驱动，就发现了一个极其严重的漏洞。

与上游 Linux 内核中用于较旧 Chips&Media 芯片 WAVE521C 的驱动不同，Pixel 的 WAVE677DV 驱动没有集成到 Video for Linux API 即 V4L2 中。

相反，它直接将芯片的硬件接口暴露给用户空间，包括允许用户空间映射芯片的 MMIO 寄存器接口。该驱动的主要功能是建立设备内存映射、进行电源管理以及允许用户空间等待芯片的中断信号。

这个 VPU 驱动中的漏洞异常简单且极易利用。问题出在驱动的 mmap 处理函数中。

```
static int vpu_mmap(struct file *fp, struct vm_area_struct *vm){	unsigned long pfn;struct vpu_core *core =		container_of(fp->f_inode->i_cdev, struct vpu_core, cdev);	vm_flags_set(vm, VM_IO | VM_DONTEXPAND | VM_DONTDUMP);/* This is a CSRs mapping, use pgprot_device */	vm->vm_page_prot = pgprot_device(vm->vm_page_prot);	pfn = core->paddr >> PAGE_SHIFT;return remap_pfn_range(vm, vm->vm_start, pfn, vm->vm_end-vm->vm_start, vm->vm_page_prot) ? -EAGAIN : 0;}
```

该函数的设计目的是将 VPU 硬件的 MMIO 寄存器区域映射到用户空间的虚拟地址空间。这个寄存器区域位于特定的物理内存地址范围内。然而，函数在调用 remap\_pfn\_range 时，完全基于用户提供的 VMA 大小进行映射，而没有对映射范围进行任何边界检查。

这意味着攻击者可以在调用 mmap 系统调用时指定一个大于寄存器区域的大小，从而从 VPU 寄存器区域的物理地址开始，映射任意数量的物理内存到用户空间。由于整个内核镜像包括代码段和数据段都位于比 VPU 寄存器区域更高的物理地址上，攻击者可以直接访问和修改内核的所有内容。

更致命的是，Pixel 设备的内核始终位于固定的物理地址上。

因此，VPU 内存区域与内核之间的偏移量是一个已知的常量。攻击者甚至不需要扫描映射的物理内存来寻找内核，只需根据 mmap 返回的地址加上固定偏移量，就能直接定位到内核的任意位置。

利用这个漏洞实现内核的任意读写仅需要 5 行代码，编写完整的漏洞利用程序花费了不到一天的时间。

## VPU 漏洞的处理过程展示了 Android 漏洞分类和修复流程的明显进步，严重漏洞的快速修复将有效保护大量 Android 用户的安全。

##

但与此同时，这个案例也凸显了 Android 驱动安全仍然存在巨大的改进空间。当研究人员报告 BigWave 驱动中的漏洞时，他们曾希望开发人员能够主动检查其他驱动中是否存在类似的明显安全问题。然而五个月后，他们在同一团队开发的 VPU 驱动中发现了一个同样严重且极其浅显的漏洞。即使是最粗略的代码审计也能立即发现这个问题。

相关资料：

https://projectzero.google/2026/05/pixel-10-exploit.html

VPU驱动的mmap 支持OOB物理映射相关

https://project-zero.issues.chromium.org/issues/463438263

### BigWave: Race between BIGO\_IOCX\_PROCESS timeout and bigo\_worker\_thread leads to UAF

https://project-zero.issues.chromium.org/issues/426567975

### Dolby Unified Decoder: Out of bounds write in evolution parsing

https://project-zero.issues.chromium.org/issues/428075495#attachment76717436

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/2dMzopbOicLibMplBZwCuQE2bMW3MP0GqZsRm1iaMYBL5dP8CfNuJwnEdFkXzbeJxcFJcPam8qQIv2TA6cCvLUMTA/0?wx_fmt=png)

白帽子

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/2dMzopbOicLibMplBZwCuQE2bMW3MP0GqZsRm1iaMYBL5dP8CfNuJwnEdFkXzbeJxcFJcPam8qQIv2TA6cCvLUMTA/0?wx_fmt=png)

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
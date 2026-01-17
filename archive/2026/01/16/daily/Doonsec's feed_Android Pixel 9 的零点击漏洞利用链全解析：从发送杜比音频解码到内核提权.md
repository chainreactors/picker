---
title: Android Pixel 9 的零点击漏洞利用链全解析：从发送杜比音频解码到内核提权
url: https://mp.weixin.qq.com/s/5ghBCECoOHZv98lVUnqD1w
source: Doonsec's feed
date: 2026-01-16
fetch_date: 2026-01-17T03:20:44.276135
---

# Android Pixel 9 的零点击漏洞利用链全解析：从发送杜比音频解码到内核提权

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/V9abY6oHTkp7F8yVrSNhxTpI0f03ONyVBN4ric65UkqibIoqY35VLGiaTjR7Bx7tkxb2nyuI3oTia9hTI8SAyngXuQ/0?wx_fmt=jpeg)

# Android Pixel 9 的零点击漏洞利用链全解析：从发送杜比音频解码到内核提权

原创

黑鸟
黑鸟

黑鸟

![]()

在小说阅读器中沉浸阅读

# 本文基于 Google Project Zero 于 2026 年 1 月发布的完整博客系列《Pixel 0-click Exploit Chain》（三部分），所有漏洞已在 2026 年 1 月 5 日的安全更新中修复。

现在的即时通讯应用（如 Google Messages）为提升用户体验，引入了自动语音转录、消息内容搜索等 AI 功能。

这些功能要求在用户未打开消息时，就对收到的音频附件进行解码和分析，从而将大量媒体解码器纳入零点击漏洞攻击面。

在 Pixel 9 上，不仅 Google Messages 会自动转录 RCS/SMS 音频，另一个进程 com.google.android.tts 也会解码所有收到的音频（可能用于增强搜索）。

需要注意的是，目前其他安卓手机系统还未确认有无该漏洞问题，因此需要谨慎对待。

两者均调用设备上所有可用解码器，包括 Dolby Unified Decoder（UDC），尽管日常消息极少使用 Dolby 格式（AC-3/EAC-3，主要见于商业影视）。

Project Zero 团队通过系统性分析，发现并构建了仅需两个漏洞的完整零点击漏洞利用链：

* CVE-2025-54957（Dolby UDC）：mediacodec 进程任意代码执行
* CVE-2025-36934（BigWave AV1 驱动）：内核任意读写 + root 提权

攻击流程为发送两条恶意构造的EAC-3 音频的消息附件，用户无需在任何交互。

## 第一阶段：Dolby UDC 整数溢出与 mediacodec 沙箱逃逸

### 漏洞是怎么形成的？

Dolby UDC 在处理 EAC-3 音频流时，会解析一种叫做 EMDF（Extensible Metadata Delivery Format）的额外元数据。这些元数据藏在音频帧的“skip”区域，最多可携带 3066 字节。

EMDF 结构中有一个关键字段：emdf\_payload\_size。它通过 variable\_bits(8) 方式读取，这种读取机制允许数值无限扩展，没有硬性上限。

解码器会先根据这个大小在自定义的 evo heap 上分配内存，然后把相应数量的字节拷贝进去。

但在分配时，代码为了内存对齐而调整总大小时，漏掉了整数溢出检查：当 payload\_size 极大时，总大小会溢出变成一个小值，导致只分配一小块内存，却试图拷贝巨量数据——形成经典的堆溢出。

特别有利的是，拷贝字节的数量和内容受另一个字段 emdf\_container\_length 控制，攻击者可以精确决定溢出多少字节、写什么数据。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/V9abY6oHTkp7F8yVrSNhxTpI0f03ONyVw0f6LiaaJFgUT1ruea4RNDLbj1YclY5oN4xjrm41ZsIrsGXXcpNFY3w/640?wx_fmt=jpeg)

同时，如果把 emdf\_container\_length 设得比实际 skip 数据长，解码器还会越界读取后续内存（这些内存要么是零，要么已被溢出填充），形成可控的信息泄露原语。

简单说，这个漏洞同时提供了精准堆溢出和内存泄露两种强大能力。

### 漏洞利用是怎么一步步进行的？

UDC 启动时会分配两块大内存区域：

* static buffer（约 69 万字节）：存放核心数据结构
* dynamic buffer（约 8.5 万字节）：用于临时计算，包含 skip buffer

攻击者先构造多个小 EMDF payload 把 evo heap 填满，让溢出正好覆盖一个关键的 skip pointer。这个指针原本指向 skip buffer，一旦被控制，后续所有 skip 数据就能写入攻击者指定的任意地址。

为了突破 evo heap 本身的容量限制，攻击者利用 Android 默认堆分配器 Scudo 的特性：通过反复触发解码过程（相当于反复打开/关闭恶意音频），让 dynamic buffer 被释放并重新分配。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/V9abY6oHTkp7F8yVrSNhxTpI0f03ONyV7AKPibwT0WvY229rUDFcPh8fMxia4K7e1lGdtymTO8RDWdibddECiaP9icw/640?wx_fmt=jpeg)

利用溢出精确修改它的 Scudo 二次分配头部，就能让下次分配时偷偷多出几千字节未初始化空间。在这些空间里植入伪造的 EMDF 容器，再配合泄露原语安全修改关键字段，最终获得在 static buffer 高地址区域任意写入 64 位值的强大原语(Primitive)。

有了这些原语，攻击者在 static buffer 中找到两个高频调用的函数指针。通过部分覆盖（只改低位字节，绕过 ASLR 的低位随机化），结合 memcpy gadget 和一个能固定增量的 adder gadget，逐步把 libc GOT 表里的普通函数指针改写成 pwrite。

最后，用 pwrite 把精心准备的 shellcode 写入 libc 中一个会频繁触发的位置（如 \_\_stack\_chk\_fail），一旦触发就执行攻击者代码，在 mediacodec 进程中实现任意代码执行。

整个过程需要几十个精心设计的同步帧，分三条恶意音频消息发送，平均几分钟内完成。

## 第二阶段：BigWave 驱动漏洞与内核提权

### 漏洞是怎么形成的？

虽然 mediacodec 进程受 SELinux 严格沙箱限制，但它可以访问 /dev/bigwave——这是 Pixel SoC 上专责 AV1 视频硬件加速的内核驱动。

每次打开这个设备，内核会分配一个 bigo\_inst 结构（内嵌 bigo\_job 子结构），挂在文件描述符的 private\_data 上。

用户通过 ioctl（BIGO\_IOCX\_PROCESS）提交任务时，把寄存器值塞进 job，job 被放入优先队列，由独立的内核 worker 线程（bigo\_worker\_thread）异步处理。

ioctl 在提交后会等待硬件完成，最多超时 16 秒。超时后它会尝试把 job 从队列移除。如果前面堆积了很多任务，worker 线程可能正好在处理这个 job，而 ioctl 已经认为超时并“删除”了它。此时用户迅速关闭文件描述符，bigo\_inst 和 job 就被释放——但 worker 线程还在继续使用它们。

释放后，worker 线程仍会：

* 从硬件拉取当前寄存器状态，写入 job->regs 指向的地址（UAF 写）
* 在结尾执行 complete()，操作 job 内的链表结构

这就是典型的跨线程 Use-After-Free（UAF）漏洞。

### 利用是怎么一步步进行的？

攻击者通过 Unix domain socket 消息喷洒大量小块内核堆对象，迅速重占释放的 job 内存，从而控制 job->regs（写入目标地址）。同时通过让硬件“不执行任何任务”，确保结束时的寄存器状态几乎与初始相同，从而精确控制写入内容。

这样就得到一个 2144 字节的半任意内核写原语。因为 Pixel 的 kASLR 实际存在固定线性映射偏移（无需完整泄露），可以直接针对内核 .data 区。

为了避免 worker 线程结尾的 complete() 操作导致崩溃（它会操作已释放对象的 swait\_queue\_head 链表），攻击者在 .data 区伪造安全的链表节点，指向无害的 init\_task 结构。

随后利用这个大块写原语分两步：

1. 先覆盖一个文件系统类型的 name 字符串指针，通过读取 /proc/self/mounts 泄露内容，转为可靠任意读，计算出真实 KASLR slide。
2. 再覆盖 ashmem 驱动的 fops 表，用 configfs 的 handler 制造类型混淆，通过普通 ASHMEM\_SET\_NAME ioctl 实现精准任意读写。

最终：关闭 SELinux 强制模式，fork 新进程，把它的 creds 指针改成 init\_cred——瞬间获得 root 权限。

这一阶段的 payload 作为 Dolby 阶段的 shellcode 注入，体积仅几 KB（甚至用 LLM 辅助生成 syscall wrapper 以进一步压缩）。

## 第三阶段：经验教训与改进建议

这个仅用两个漏洞的利用链，暴露了 Android 生态的几个系统性问题：

* AI 功能无意扩大 0-click 攻击面，把不常用解码器（如 UDC）纳入高危路径
* 内核驱动仍是“软目标”，漏洞易找且影响大
* 部分关键防护在 Pixel 上未完全生效（如 seccomp 缺失、kASLR 实际可绕、MTE 未默认开启）
* 补丁延迟严重：UDC 漏洞报告后 139 天才有设备修补，Pixel 又晚近两个月，部分因厂商低估沙箱内 RCE 严重性

Project Zero 建议：

* 从 0-click 路径移除不常用解码器
* 系统性 fuzz 和审计所有 0-click 攻击面
* 驱动逐步向 Rust 重写、严格限制无特权进程访问
* 强制启用 seccomp、编译时加 -fbounds-safety、默认开启 MTE
* 调整漏洞优先级矩阵，至少把利用链中一环评为 Critical
* 更多核心组件采用 APEX 机制实现 Play Store 快速更新

原文链接：

* Part 1: https://projectzero.google/2026/01/pixel-0-click-part-1.html
* Part 2: https://projectzero.google/2026/01/pixel-0-click-part-2.html
* Part 3: https://projectzero.google/2026/01/pixel-0-click-part-3.html

#

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkqrJPe3BMSmUuUaQMPJDnWTSrtbtXBAZSMfj0iaxiaMvM6cnIDqLXBbescHHicaricGUU0tHjJ4BqISKw/0?wx_fmt=png)

黑鸟

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkqrJPe3BMSmUuUaQMPJDnWTSrtbtXBAZSMfj0iaxiaMvM6cnIDqLXBbescHHicaricGUU0tHjJ4BqISKw/0?wx_fmt=png)

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
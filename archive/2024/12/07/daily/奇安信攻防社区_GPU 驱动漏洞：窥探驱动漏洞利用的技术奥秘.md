---
title: GPU 驱动漏洞：窥探驱动漏洞利用的技术奥秘
url: https://forum.butian.net/share/3924
source: 奇安信攻防社区
date: 2024-12-07
fetch_date: 2025-10-06T19:33:06.985218
---

# GPU 驱动漏洞：窥探驱动漏洞利用的技术奥秘

#

[问答](https://forum.butian.net/questions)

*发起*

* [提问](https://forum.butian.net/question/create)
* [文章](https://forum.butian.net/share/create)

[攻防](https://forum.butian.net/community)
[活动](https://forum.butian.net/movable)

Toggle navigation

* [首页 (current)](https://forum.butian.net)
* [问答](https://forum.butian.net/questions)
* [商城](https://forum.butian.net/shop)
* [实战攻防技术](https://forum.butian.net/community)
* [漏洞分析与复现](https://forum.butian.net/articles)
  NEW
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### GPU 驱动漏洞：窥探驱动漏洞利用的技术奥秘

本文尝试以 GPU 漏洞为引介绍围绕 GPU 驱动这一攻击面，安全研究人员对内核漏洞利用技术做的一些探索。
背景介绍
目前移动 SOC 平台上由多个硬件模块组成，常见的硬件模块有：CPU、GPU、Modem基...

本文尝试以 GPU 漏洞为引介绍围绕 GPU 驱动这一攻击面，安全研究人员对内核漏洞利用技术做的一些探索。
背景介绍
----
目前移动 SOC 平台上由多个硬件模块组成，常见的硬件模块有：CPU、GPU、Modem基带处理器、ISP（图像处理器）等，这些硬件模块通过硬件总线互联，协同完成任务。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-bfda087d8892abb2cae61dc1319f0bc9e12016b6.png)
对于 GPU 驱动漏洞研究来说，我们需要关注的一个关键特性是 \*\*GPU 和 CPU 共用同一块 RAM。\*\* 在 CPU 侧操作系统通过管理 CPU MMU 的页表来实现虚拟地址到物理地址的映射
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-9a0769933cbbd55176d6a54809ca2e3d45eb86ab.png)
GPU 也有自己的 MMU，不过 GPU 的页表由 CPU 内核中的 GPU 驱动管理，从而限制 GPU 能够访问的物理地址范围。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-6addbae99cdda81d1a80899d82fd186188398ad2.png)
在实际的业务使用中，一般是 CPU 侧分配一段物理内存，然后映射给 GPU ， GPU 从共享内存中取出数据完成计算、渲染后再将结果写回共享内存，从而完成 GPU 与 GPU 之间的交互。对于 GPU 驱动安全研究来说，特殊的攻击面在于由于其需要维护 GPU 页表，这个过程比较复杂，涉及到内核中的各个模块的配合，非常容易出现问题，历史上也出现了多个由于 GPU 页表管理失误导致的安全漏洞
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-9994ce32e05e442aaab046d466d3fd4b7226d372.png)
以 ARM Mali 驱动为例，这几年出现的几个比较有代表性的漏洞如下：
| 漏洞 | 类型 | 漏洞原语 |
|---|---|---|
| CVE-2021-39793 | 页权限错误 | 篡改 只读映射到用户进程的物理页 |
| CVE-2021-28664 | 页权限错误 | 篡改 只读映射到用户进程的物理页 |
| CVE-2021-28663 | GPU MMU 操作异常 | 物理页 UAF |
| CVE-2023-4211 | 条件竞争 UAF | SLUB 对象 UAF |
| CVE-2023-48409 | 整数溢出 | 堆溢出 |
| CVE-2023-26083 | 内核地址泄露 | 内核地址泄露 |
| CVE-2022-46395 | 条件竞争 UAF | 物理页 UAF |
> 其中前 3 个漏洞是管理 GPU 页表映射时的漏洞，后面几个就是常规驱动漏洞类型
CVE-2021-28664
--------------
分析代码下载：<https://armkeil.blob.core.windows.net/developer/Files/downloads/mali-drivers/kernel/mali-bifrost-gpu/BX304L01B-SW-99002-r19p0-01rel0.tar>
先以最简单的漏洞开始讲起，这个漏洞算是 Mali 第一个出名的漏洞了，同期出道的还有 CVE-2021-28664，这个漏洞是由 [Project Zero](https://googleprojectzero.github.io/0days-in-the-wild/0day-RCAs/2021/CVE-2021-39793.html) 捕获的在野利用，该漏洞的 Patch 如下
```c
static struct kbase\_va\_region \*kbase\_mem\_from\_user\_buffer(
struct kbase\_context \*kctx, unsigned long address,
unsigned long size, u64 \*va\_pages, u64 \*flags)
{
[...]
+ int write;
[...]
+ write = reg->flags & (KBASE\_REG\_CPU\_WR | KBASE\_REG\_GPU\_WR);
+
#if KERNEL\_VERSION(4, 6, 0) > LINUX\_VERSION\_CODE
faulted\_pages = get\_user\_pages(current, current->mm, address, \*va\_pages,
#if KERNEL\_VERSION(4, 4, 168) <= LINUX\_VERSION\_CODE && \
KERNEL\_VERSION(4, 5, 0) > LINUX\_VERSION\_CODE
- reg->flags & KBASE\_REG\_CPU\_WR ? FOLL\_WRITE : 0,
- pages, NULL);
+ write ? FOLL\_WRITE : 0, pages, NULL);
#else
- reg->flags & KBASE\_REG\_CPU\_WR, 0, pages, NULL);
+ write, 0, pages, NULL);
#endif
#elif KERNEL\_VERSION(4, 9, 0) > LINUX\_VERSION\_CODE
faulted\_pages = get\_user\_pages(address, \*va\_pages,
- reg->flags & KBASE\_REG\_CPU\_WR, 0, pages, NULL);
+ write, 0, pages, NULL);
#else
faulted\_pages = get\_user\_pages(address, \*va\_pages,
- reg->flags & KBASE\_REG\_CPU\_WR ? FOLL\_WRITE : 0,
- pages, NULL);
+ write ? FOLL\_WRITE : 0, pages, NULL);
#endif
```
Patch 的关键点在于将 get\\_user\\_pages 参数中的 reg-&gt;flags &amp; KBASE\\_REG\\_CPU\\_WR​ 换成了 reg-&gt;flags &amp; (KBASE\\_REG\\_CPU\\_WR | KBASE\\_REG\\_GPU\\_WR)​ ，这两个标记的作用如下：
- KBASE\\_REG\\_CPU\\_WR：表示 reg 能够已写权限映射到用户态进程
- KBASE\\_REG\\_GPU\\_WR: 表示 reg 能够已写权限映射到 GPU
reg 的类型为 struct kbase\\_va\\_region​ ， MALI 驱动中使用 kbase\\_va\\_region 管理物理内存，包括物理内存的申请/释放、GPU/CPU 页表映射管理等。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-8adc1bf70c15d1a962a7adc1e91dc5c0f1a920af.png)
图中的关键要素如下：
- kbase\\_va\\_region 中 cpu\\_alloc 和 gpu\\_alloc 指向 kbase\\_mem\\_phy\\_alloc ，表示该 reg 拥有的物理页，且大部分场景下 cpu\\_alloc = gpu\\_alloc
- kbase\\_va\\_region 的 flags 字段控制驱动映射 reg 时的权限，假如 flags 为 KBASE\\_REG\\_CPU\\_WR 表示该 reg 能够被 CPU 映射为可写权限，如果没有该 flag 则不允许将 reg 以可写模式映射到 CPU 进程，确保无法进程修改这些物理页
核心观点：驱动利用 kbase\\_va\\_region 表示一组物理内存，这组物理内存可以被 CPU 上的用户进程和 GPU 分别映射，映射的权限由 reg-&gt;flags 字段控制.
回到漏洞本身，其调用路径中的关键代码如下：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-104adf09acabfe04d6eab2cc9da9dbbeded5fd45.png)
漏洞在于传递 get\\_user\\_pages 参数是只考虑了 KBASE\\_REG\\_GPU\\_WR 情况，没有考虑 KBASE\\_REG\\_CPU\\_WR，当 reg-&gt;flags 为 KBASE\\_REG\\_CPU\\_WR 时 get\\_user\\_pages 的第三个参数为 0
```c
/\*
\* This is the same as get\_user\_pages\_remote(), just with a
\* less-flexible calling convention where we assume that the task
\* and mm being operated on are the current task's and don't allow
\* passing of a locked parameter. We also obviously don't pass
\* FOLL\_REMOTE in here.
\*/
long get\_user\_pages(unsigned long start, unsigned long nr\_pages,
unsigned int gup\_flags, struct page \*\*pages,
struct vm\_area\_struct \*\*vmas)
{
return \_\_get\_user\_pages\_locked(current, current->mm, start, nr\_pages,
pages, vmas, NULL, false,
gup\_flags | FOLL\_TOUCH);
}
```
get\\_user\\_pages 的作用的是根据用户进程提供的 va （start）遍历进程页表，返回的是 va 对应物理地址对应的 page 结构体指针，结果保存到 pages 数组中。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-6a2b3f6998f993d947a3dad3c26ecaad57106fa8.png)
> 即根据 task\\_struct-&gt;mm 找到进程页表，遍历页表获取物理地址
其中如果 gup\\_flags 为 1，表示获取 va 对应 page 后会写入 page 对应的物理页，然后在 get\\_user\\_pages 内部需要对只读页面和 COW 页面做额外处理，避免这些特殊 va 对应的物理页被修改导致非预期行为。
- 如果 vma 为只读，API 返回错误码
- VA 的映射为 COW 页，在 API 内会完成写时拷贝，并返回新分配的 page
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-d07d9fe84254d5692880a9f2f50772600a93e659.png)
当 gup\\_flags 为 0 时则直接返回页表遍历的结果（P0）
对于这个漏洞而言，我们可以创建一个 reg-&gt;flags​ 为 KBASE\\_REG\\_CPU\\_WR​ 的 kbase\\_va\\_region​，再导入页面时就可以获取进程中任意 va 对应 page 到 kbase\\_va\\_region​，最后再将其以可写权限映射到用户态进程，这样就可以实现篡改进程中任意只读映射对应的物理页。
这一原语要进一步利用需要依赖操作系统的机制，首先介绍最简单的一种利用方式，Linux 内核在处理磁盘中的文件系统时，会对从磁盘中读取的物理页做缓存来加速文件访问的性能，同时减少重复文件物理页，减少开销
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-390f2d00715d69ef22cdddff0356a5ecd6fec9b0.png)
如果所示：
- 当进程尝试读取物理页时，比如只读权限 mmap ，内核会搜索 page cache 如果找到就直接返回，否则就从磁盘中加载物理页到 Page Cache 中，然后返回
- 如果是写则会有对应的 flush cache 机制
具体来说，当两个进程同时以只读权限 mmap libc.so 文件时，这两个进程的 VA 会指向同一个物理页
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-f168a05e9a0fb9d86b0ff9f9856cf97564f2ea58.png)
这样当我们利用漏洞修改 Page Cache 中的物理页后，其他进程也会受到影响，因为都是映射的同一块物理地址，因此攻击思路就来了：
- 只读映射 libc.so 利用漏洞篡改其在 Page Cache 中物理页，在其中注入 shellcode，等高权限进程调用时就能提权
- 类似的手法修改 /etc/passwd 完成提权
除了修改文件系统的 Page Cache 外，在 Android 平台上还有一个非常好的目标，binder 驱动会往用户态进程映射只读 page，里面的数据结构为 flat\\_binder\\_object，binder\\_transaction\\_buffer\\_release 里面会使用 flat\\_binder\\_object-&gt;handle，相关代码如下：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-411c9155475c9887106096de79118dfc4a74f785.png)
首先通过 binder\\_get\\_node 查找 node，然后会调用 binder\\_put\\_node 减少 node 的引用计数，当 node 引用为0时会释放 node。
由于 flat\\_binder\\_object 所在物理页用户态无法修改，所以可以保证这个流程的正确性，当我们只读物理页写漏洞篡改 flat\\_binder\\_object-&gt;handle 指向另一个 node 时，触发 binder\\_transaction\\_buffer\\_release 就能导致 node 引用计数不平衡
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-c3a02c2c7122e70a15de2c5d546f1eb99b442768.png)
最后可以将漏洞转换为 binder\\_node 的UAF，然后采用 [CVE-2019-2205](https://labs.bluefrostsecurity.de/files/OffensiveCon2020\_bug\_collision\_tale.pdf) 的利用方式进行漏洞利用即可。
此外类似的漏洞在 2016 年就已经出现在高通 GPU 驱动中，[CVE-2016-2067](https://www.blackhat.com/docs/eu-16/materials/eu-16-Taft-GPU-Security-Exposed.pdf)：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attac...
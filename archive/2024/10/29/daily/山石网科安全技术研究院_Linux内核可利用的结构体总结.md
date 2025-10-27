---
title: Linux内核可利用的结构体总结
url: https://mp.weixin.qq.com/s?__biz=MzUzMDUxNTE1Mw==&mid=2247508478&idx=1&sn=7867cad41b7d792de6b595060fbbdb46&chksm=fa527440cd25fd56cb95b25830fbd7a1737c7d02bd182cdeb7a95c675ee4574a2af6d148e10c&scene=58&subscene=0#rd
source: 山石网科安全技术研究院
date: 2024-10-29
fetch_date: 2025-10-06T18:52:11.177014
---

# Linux内核可利用的结构体总结

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Gw8FuwXLJnRhdgiabTPVFggBqXqNg7v3K4PJYZgUEkmnxzOicyK7VFRicOvWhCdlxRDAIzrlicmkdWFib57hC6egEww/0?wx_fmt=jpeg)

# Linux内核可利用的结构体总结

原创

unr4v31

山石网科安全技术研究院

在Linux内核中，可以通过分配对象来对UAF、OOB等漏洞对象进行占位进行漏洞利用。内核中有许多可利用对象，某些对象有非常强大的利用原语，可以通过这些对象及其操作函数来实现权限提升。本文对Linux可利用的对象进行了统计和总结。总结表格如下：

| 结构体/系统调用名称 | cache | 大小(bytes) | 可泄露内核地址 | 可泄露堆地址 | 可泄露栈地址 | 可劫持RIP | 读写 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| signalfd\_ctx | kmalloc-8 | 8 | ❌ | ☑️ | ❌ | ❌ | ❌ |
| setxattr系统调用 | 大小可变 | size < 65536 | ❌ | ❌ | ❌ | ☑️ | ✅ |
| ldt\_struct | kmalloc-16 | 16 | ❌ | ❌ | ❌ | ❌ | ✅ |
| shm\_file\_data | kmalloc-32 | 32 | ✅ | ✅ | ❌ | ❌ | ✅ |
| seq\_operations | kmalloc-32 | 32 | ✅ | ❌ | ❌ | ✅ | ❌ |
| user\_key\_payload | 大小可变 | 0x18 < size < (0x7fff + 0x18) | ✅ | ✅ | ❌ | ❌ | ✅ |
| msg\_msg | 大小可变 | 0x30 < size < 0x1000 | ❌ | ✅ | ❌ | ❌ | ✅ |
| sendmsg系统调用 | 大小可变 | 44 < size < 0x7fffffff | ❌ | ❌ | ❌ | ❌ | ✅ |
| subprocess\_info | kmalloc-128 | 96 | ☑️ | ✅ | ❌ | ☑️ | ❌ |
| file | kmalloc-256 | 232 | ✅ | ✅ | ❌ | ✅ | ❌ |
| timerfd\_ctx | kmalloc-256 | 216 | ✅ | ✅ | ❌ | ❌ | ❌ |
| tty\_struct | kmalloc-1k | 0x290~0x2e0 | ✅ | ✅ | ❌ | ✅ | ❌ |
| pipe\_buffer | 大小可变 | 0x28 < size <= 0x1000 | ✅ | ✅ | ❌ | ✅ | ☑️ |
| packet\_sock | 大小可变 | 1024 < size < 2048 | ☑️ | ✅ | ❌ | ✅ | ✅ |
| sk\_buff | 大小可变 | 512 <= size | ❌ | ✅ | ❌ | ❌ | ✅ |

此外，在IDA分析过程中，kmalloc\_trace的参数kmalloc\_caches常见大小区间如下（详细见内核源码mm/slab\_common.cz中kmalloc\_caches定义）：

```
 kmalloc_caches[3] /* 8 */ kmalloc_caches[4] /* 16 */ kmalloc_caches[5] /* 24 ~ 32 */ kmalloc_caches[5] /* 32 */ kmalloc_caches[6] /* 40 ~ 64 */ kmalloc_caches[1]   /* 72 ~ 96 */ kmalloc_caches[7] /* 104 ~128 */ kmalloc_caches[2] /* 136 ~ 192 */
```

# signalfd、signalfd4

内核对象：signalfd\_ctx

size：8

内核基址：无法泄露

堆地址：可泄露

栈地址：无法泄露

劫持RIP：无法劫持

产生：系统调用signalfd、signalfd4

释放：无

示例：无

# setxattr系统调用

内核对象：xattr\_ctx->kvalue

size：size < 65536

内核基址：无法泄露

堆地址：无法泄露

栈地址：无法泄露

劫持RIP：可以通过写入功能向内核写入数据，改写某些函数指针，间接控制RIP。

产生：setxattr系统调用，例如：`setxattr("/etc/passwd", "user.test", addr, 0x400, 1)`

释放：函数内部会进行释放。

示例：SECCON 2020 kstack题目，writeup1：https://roderickchan.github.io/zh-cn/2022-04-28-seccon-2020-kstack/ ，writeup2: https://www.anquanke.com/post/id/266898

其他说明：setxattr在函数内部kvmalloc申请后使用后随即将对象进行释放，因此需要使用userfaultfd或FUSE等利用技术来对分配对象进行占位。

# ldt\_struct

内核对象：`struct ldt_struct`

size：16

内核基址：无法泄露

堆地址：无法泄露

栈地址：无法泄露

劫持RIP：无法劫持

产生：可通过modify\_ldt系统调用的write\_ldt功能来分配空间并写入数据，通过read功能，并控制`ldt->entries`成员，即可读取任意地址的数据。

释放：无。

示例：TCTF/0CTF 2021 FINAL kernote题目, writeup: https://github.com/YZloser/My-CTF-Challenges/tree/master/0ctf-2021-final/kernote

其他说明：通常在全局变量page\_offset\_base + 0x9d000 的地方存储着 secondary\_startup\_64 函数的地址，因此可利用read任意读泄露内核基址。

# shm\_file\_data

内核对象：`struct shm_file_data`

size：32

内核基址：可通过结构中的ns和vm\_ops泄露内核地址。

堆地址：可通过file成员泄露

栈地址：不可泄露

劫持RIP：无法劫持

产生：`shmat`系统调用

释放：`shmdt`系统调用

示例：RWCTF 2023 PWN digging into kernel 3题目，writeup: https://blingblingxuanxuan.github.io/2023/02/06/230206-rwctf2023-digging-into-kernel-3/#msg-msg-shm-file-data-gt-泄露内核地址

其他说明：在用户态中我们可以通过 `shmget`、`shmat`、`shmctl`、`shmdt` 这四个系统调用操纵共享内存。

# seq\_operations

内核对象：struct seq\_operations

size：32

内核基址：可通过泄露此对象中的函数指针来泄露内核基址。

堆地址：不可泄露

栈地址：不可泄露

劫持RIP：修改此对象中的`start`函数指针，并调用`read(seq_fd, NULL, 0)`劫持RIP。

产生：通过`fd = open("/proc/self/stat", O_RDONLY)`来分配。

释放：`close(fd)`

示例：InCTF 2021国际赛kqueue题目，writeup1: https://bbs.kanxue.com/thread-269031.htm, writeup2: https://www.anquanke.com/post/id/258160

# add\_key系统调用

内核对象：`struct user_key_payload`

size：(0x7fff + 0x18) > size > 0x18

内核基址：可泄露

堆地址：可泄露

栈地址：无法泄露

劫持RIP：无法劫持

产生：add\_key系统调用产生

释放：keyctl的KEYCTL\_REVOKE标志位可以将对象释放。

示例：2024 强网拟态 ker题目，writeup：https://blog.xmcve.com/2024/10/20/强网拟态2024-Writeup/#title-9

其他说明：在使用keyctl系统调用时，KEYCTL\_UPDATE可以分配一个临时对象将用户数据拷贝至内核，随后释放。KEYCTL\_READ可以读取payload的内容，KEYCTL\_UNLINK可以释放整个key。

# msg\_msg

内核对象：`struct msg_msg`

size：0x1000 > size > 0x30

内核基址：无法泄露

堆地址：可通过list或next成员泄露

栈地址：无法泄露

劫持RIP：通过篡改结构体m\_ts成员值实现越界读写，堆风水间接控制RIP。

产生：通过`msgget`创建消息队列，调用`msgsnd`生成msg\_msg对象。

释放：通过`msgrcv`系统调用接收队列消息并释放对象。

示例：D^ 3CTF2022 d3kheap题目，writeup：https://arttnba3.cn/2022/03/08/CTF-0X06-D3CTF2022\_D3KHEAP/

其他说明：在msgrcv中使用MSG\_COPY来读取队列消息但不进行释放，正好可以用于判断是否命中堆喷对象。

# sendmsg

内核对象：`unsigned char ctl[sizeof(struct cmsghdr) + 20] __aligned(sizeof(__kernel_size_t));`

size：0x7fffffff > size > 44

内核基址：无法泄露

堆地址：可泄露

栈地址：无法泄露

劫持RIP：无法直接劫持。

产生：`sendmsg`系统调用，数据放入msg.msg\_control指针。

释放：与产生路径相同。

示例：https://blog.csdn.net/panhewu9919/article/details/100637619

其他说明：与`setxattr`相同，可与userfaultfd结合使用。

# subprocess\_info

内核对象：subprocess\_info

size：96

内核基址：由于没有任何内核与用户数据交互，需要通过竞争来泄露内核基址

堆地址：可泄露

栈地址：不可泄露

劫持RIP：通过竞争来修改cleanup函数指针，然后触发执行`if (info->cleanup) info->cleanup(info)`

产生：创建一个未知协议（`socket(22, AF_INET, 0)`）时，便会创建一个 `subprocess_info` 结构体。

释放：在系统调用结束之后该结构体便会被立即释放。

示例：SCTF2021 - flying\_kernel，writeup：https://www.anquanke.com/post/id/264563

# file

内核对象：`struct file`

size：232

内核基址：可以通过f\_op字段泄露内核地址

堆地址：可泄露

栈地址：无法泄露

劫持RIP：重写`f_op`中的`shmctl`来控制

产生：`shmget`创建共享内存

释放：`shmctl`

示例：无

# timerfd\_ctx

内核对象：`struct timerfd_ctx`

size：kmalloc-256

内核基址：可以通过timerfd\_ctx 的 tmr 字段的 `function` 字段泄露内核地址

堆地址：可通过`base`成员泄露

栈地址：无法泄露

劫持RIP：无法劫持

产生：通过 `timerfd_create` 系统调用来分配一个 `timerfd_ctx` 结构体

释放：无

示例：CUCTF 2020 Hotrod题目，writeup：https://syst3mfailure.io/hotrod/

# tty\_struct

内核对象：tty\_struct

size：大小在0x290~0x2e0之间，不同版本的内核此结构体大小有变动。

内核基址：可通过`const struct tty_operations *ops` 成员泄露

堆地址：可泄露

栈地址：无法泄露

劫持RIP：通过劫持`const struct tty_operations *ops`中的函数指针实现

产生：打开一个控制终端，例如：`fd = open("/dev/ptmx", O_RDWR | O_NOCTTY)`

释放：`close(fd)`

示例：强网杯2021-notebook

其他说明：tty\_struct 的魔数为 `0x5401`，位于该结构体的开头，我们可以利用对该魔数的搜索以锁定该结构体。

# pipe\_buffer

内核对象：struct pipe\_buffer

size： kmalloc-1k

内核基址：通过pipe\_buffer的pipe\_buf\_operations泄露内核地址

堆地址：可泄露

栈地址：无法泄露

劫持RIP：在关闭管道时会调用`pipe_buffer->pipe_buffer_operations->release`函数指针，因此可劫持`release`来劫持RIP

产生：pipe和pipe2系统调用

释放：close关闭管道

示例：D^ 3CTF2022 d3kheap题目，writeup：https://arttnba3.cn/2022/03/08/CTF-0X06-D3CTF2022\_D3KHEAP/

其他说明：pipe\_buffer大小并非固定的1k，可以通过设置`F_SETPIPE_SZ` 来重新分配 pipe\_buffer 并指定其数量。这一步骤可以通过`fcntl`系统调用重新分配单个 pipe 的 pipe\_buffer 数量，从而实现近乎任意大小的对象分配 ，但需要是 `pipe_buffer` 结构体的 2 次幂倍。此外，若能够修改 `page` 指针，则我们便能完成对整个物理内存区域的读操作，以及对直接映射区上有写权限的内存区域的写操作。

# packet\_sock

内核对象：`struct packet_sock`

size：1024 < size < 2048，不同内核版本此结构体大小不同

内核基址：通过越界读写间接获取内核基址

堆地址：可泄露

栈地址：无法泄露

劫持RIP：packet\_sock -> rx\_ring -> prb\_bdqc -> retire\_blk\_timer -> function。在timeout超时后调用，可传参，可用于执行native\_write\_cr4(0x406e0)来关闭SMEP/SMAP。packet\_socket -> xmit。在接收数据时调用。

产生：分配packet\_socksocket(AF\_PACKET, SOCK\_DGRAM, htons(ETH\_P\_ARP)); —— sock(AF\_PACKET) -> packet\_create -> sk\_alloc，setsockopt(fd, SOL\_PACKET, PACKET\_RX\_RING, (void\*)&tp, sizeof(tp)); —— packet\_set\_ring()->init\_prb\_bdqc()->prb\_setup\_retire\_blk\_timer()->prb\_init\_blk\_timer()。

释放：

示例：https://bsauce.github.io/2021/05/19/CVE-2017-7308/

# sk\_buff

内核对象：`struct sk_buff`

size：size >= 512

内核基址：无法泄露

堆地址：可泄露

栈地址：无法泄露

劫持RIP：无法直接劫持

产生：对socket一类的操作都会创建socket，可以通过`socketpair`创建一对socket，从一段发送，另一端读出。

释放：从socket读出数据以释放对象。

示例：D^ 3CTF2022 d3kheap题目，writeup：https://arttnba3.cn/2022/03/08/CTF-0X06-D3CTF2022\_D3KHEAP/

# References

https://ptr-yudai.hatenablog.com/entry/2020/03/16/165628

https://arttnba3.cn/2021/11/29/PWN-0X02-LINUX-KERNEL-PWN-PART-II

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSZmibNONzibea8WkcAFcdQcXicIYgWuvOtR8HqlqJ68Avib679FBGHYqxRibldppr6etXJxxWRrlBToiaw/0?wx_fmt=png)

山石网科安全技术研究院

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSZmibNONzibea8WkcAFcdQcXicIYgWuvOtR8HqlqJ68Avib679FBGHYqxRibldppr6etXJxxWRrlBToiaw/0?wx_fmt=png)

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
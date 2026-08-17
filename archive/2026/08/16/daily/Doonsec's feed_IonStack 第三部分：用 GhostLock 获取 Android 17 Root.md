---
title: IonStack 第三部分：用 GhostLock 获取 Android 17 Root
url: https://mp.weixin.qq.com/s/E3kZcJQ5IuyNhaD6T9Y4MA
source: Doonsec's feed
date: 2026-08-16
fetch_date: 2026-08-17T02:53:56.412219
---

# IonStack 第三部分：用 GhostLock 获取 Android 17 Root

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/h4gtbB74nSjHZIvg0JfHvmhwAMAJ9VZAAt2hNwC4D8aSAhHibXHVddOg4C2HbUjawrXQnu2MoibicbRKfaJG3h6dkz7ATWaNnZ7mibDwqREtJ5I/0?wx_fmt=jpeg)

# IonStack 第三部分：用 GhostLock 获取 Android 17 Root

Nebula Security
Nebula Security

securitainment

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

| 原文链接 | 作者 |
| --- | --- |
| https://nebusec.ai/research/ionstack-part-3/ | Nebula Security |

> GhostLock（CVE-2026-43499）是 Nebula Security 发现的一个 Linux 内核漏洞，自 2011 年以来存在于每个主要发行版中。在将其转化为稳定的提权和容器逃逸并在 kernelCTF 中赢得 $92,337 后，我们更进一步，用 GhostLock 开发了全球首个公开的 Android 17 root。本篇 writeup 涵盖了将利用程序迁移到 Android 所使用的额外利用技术。

在上一篇中，我们讨论了 GhostLock（CVE-2026-43499）的根因——如何回收"已释放"的栈、伪造 `rt_mutex_waiter`并获得受限的指针写入、最终从 `inet6_protos`获得控制流劫持，以及使用 DirtyMode 在 Linux 上完成提权。

由于 Android 上默认启用了控制流完整性（CFI），我们需要找到另一种替代方案来帮助我们完成提权的最后一步。

此外，由于我们现在针对的是 ARM 设备且 KPTI 已启用，prefetch 侧信道不再容易使用，因此我们还需要另一种方法来绕过 KASLR。

当然，我们也需要改变回收栈的策略。

> 如果没有启用 CFI 保护（如 `CFI_CLANG`、ARM `BTI`或 Intel `CET`），在控制函数指针后获得任意代码执行要容易得多：RetSpill、Ret2BPFJIT、KEPLER、cpu\_entry\_area pivot、panic\_on\_oops disable……以及常规 ROP。

## **背景知识**

> 我对 kCFI、KernelSnitch 和 linear map 很熟悉，想直接看利用细节。

### **（内核）Android 上的控制流完整性**

2022 年之前，Android 使用基于跳转表的白名单来检查合法的调用/跳转目标并保护 CFI。该功能需要启用 LTO，这带来了沉重的编译开销，而且无法保护一些灵活的函数，如 JIT 编译的 BPF 程序（对这些函数调用完全没有检查）。

2022 年，Android 切换到基于函数签名的新 Clang CFI 功能。它对函数参数和返回值的类型进行哈希，并在每次间接调用前检查目标哈希。这种方法支持更灵活的目标，且不再依赖 LTO。

哈希在编译时烘焙，发射到一个 `__cfi_<func>`"前导"中，位于每个函数入口的正前方，调用方在每次间接调用前检查目标的哈希。

检查本身如下图所示：

![CFI 概览](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM7K9KvRoKa4ffKd34ibOZO7yzpwERswnfOgXEneuXcjhPx86yosmWV2zZmm8c59H8YZMgibiaMSiazkElK5ZMWribzF5mm09E90kW13gkSZVu23diag/640?wx_fmt=svg&from=appmsg)

CFI 概览

![CFI 概览](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM76j9ltqLx76qGKShLXHjIM7E7MGgV6RcoicyHSTsHkpHxsZlics1RHQic8ciaianaNLuTax7GUNYmstkDs72MtTSaz46ricia15q5Dmoh86JXHr7xicg/640?wx_fmt=svg&from=appmsg)

CFI 概览

调用方加载被调用方前方的哈希，并在调用点进行比较。在上图中，`proc_do_uuid`和 `proc_dostring`共享相同的参数和返回值类型，因此它们会有相同的哈希，CFI 将允许对它们中任何一个的间接调用，而例如 `commit_creds`具有不同的原型，会陷入 `report_cfi_failure()`。

使用 Android 上最新的 CFI 实现，我们只能将函数指针劫持到具有相同签名（即完全相同的参数和返回值类型）的另一个函数。在下面的 writeup 中，我们将 `ashmem`的 `read_iter`/`write_iter`替换为 `configfs`的，因为它们都是类型为 `ssize_t (struct kiocb *, struct iov_iter *)`的 VFS 处理函数（因此它们会有相同的哈希）。

> **能否伪造哈希？**

### **探测（几乎）任意内核对象的地址**

访问哈希表等内核数据结构所花费的周期数取决于其内部状态（例如空桶与冲突链）。NDSS 的初始工作表明，非特权进程可以通过受控的系统调用放大这些**软件级**的时间差异，并推断内核数据结构的状态。当目标哈希表将调用方的 `mm_struct`指针折叠到其桶索引中时，对桶遍历进行计时可以恢复当前 `mm_struct`的地址。

Lukas 的后续文章将这种时间泄漏与针对特定对象（如 `msg_msg`和 `pipe_buffer`）的跨缓存重用相结合。由于 `mm_struct`从专用的 `mm_cachep`slab 分配，其泄露的地址给出了后备 slab 页的位置。通过释放该页并通过分配器操作将其回收为目标 slab，攻击者可以获得目标对象的精确地址。

### **利用 Linear Map 的免费（但有限的）KASLR 绕过**

正如 Project Zero 所示，提交 `1db780bafa4c`移除了 arm64 上的 linear map 随机化，因此 `physmap`的基址不再被随机化。这使我们可以访问内核镜像的 rw 映射（对原始 ro 或 rx 内存为只读），地址固定，如下图所示。

![Linear map 概览](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM5S80vJja3DMTrZx4ow1q9c3dl4VDxZ8ib8SBK0CcZibxMCPro0AFaoR5ibibFf8J8UqibSDmibicYh0IFjOT6VM0CibicRpt8vr975r0JAMlrRVXUfZiaw/640?wx_fmt=svg&from=appmsg)

Linear map 概览

![Linear map 概览](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM7NNiccbjfGVMA1Fkh2Pel5g4pEtVfUgj0QWXJMphZql1BtepnzRGEGbVCLEYABjicf9vrAwlXbGiccwx8YibhAB5wkO0PXxOUiaIP9JM3amh1ZzMg/640?wx_fmt=svg&from=appmsg)

Linear map 概览

> 即使 `physmap`被正确随机化（或启用了物理 ASLR），其基址仍然可以通过 KernelSnitch 探测。

然而，由于 Linear Map 现在被映射为不可执行，如果我们想复用一些可执行代码，仍然需要单独的 KASLR 绕过。因此我们仍然需要真正的 KASLR slide。

## **利用摘要**

* **GhostLock**

  -> 在 waiter 任务的 `pi_blocked_on`中留下一个悬垂的 `rt_mutex_waiter`。
* ① **回收**-> 使用 `pselect`回收 waiter 的栈帧并在其上伪造 `rt_mutex_waiter`。
* ② **bootid**-> 覆盖 `boot_id`的 sysctl `.data`，读回 `&nfulnl_logger`以泄露 KASLR slide。
* ③ **ashmem**-> 用 `configfs`处理函数劫持 `ashmem`的 `fops`，实现受限的内核读写。
* ④ **pipe\_buffer**-> 将 `copy_{to,from}_user`升级为无限制的 `page*`全地址读写。
* ⑤ **获取 root**-> 禁用 SELinux 并修改 `cred`结构体以逃逸 seccomp 并成为 root。

> 注意 physmap 基址是固定的，且同一个 GhostLock 原语被使用了**两次**——第一次在 bootid 步骤中泄露 KASLR slide，然后覆盖 **`ashmem`**的 fops。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/h4gtbB74nSjeOVk2BEkzfAaaq1FJdqp0yLRpFYxGpsEYOOTd4XZahX2ylBFTJQicue0uKbpic4dqokHdmGkBhYA8ItrVwMibeo5gvP3ECb7W6M/640?wx_fmt=png&from=appmsg)

利用概览

![](https://mmbiz.qpic.cn/mmbiz_png/h4gtbB74nShhT5EicwjMnnUhw7My85wKpgicvZIJGm9dI3Wib8ibmDBtH3CQntEZ6h4InLkvZnbw1dicWy1UcKGNgYAiaOeaxOCuUXtZVhhVN8yW8/640?wx_fmt=png&from=appmsg)

利用概览

## **利用细节**

### **恢复内存写入原语**

回顾 GhostLock 的初始原语。我们最终可以向一个任意（但受限的）地址写入一个指针。为此，我们需要：

* 取回已释放的栈内存（喷射）：-> 复用栈
* 让伪造的 `rt_mutex_waiter`通过其结构检查和解引用：-> 伪造 waiter

#### **复用栈**

我们仍然从在相同栈偏移处喷射受控字节开始，而帮助我们回收栈帧的系统调用是目标特定的，因为帧深度和系统调用的触及范围会随内核镜像的变化而改变。在 Pixel 10（Android 17）上，我们使用 `pselect`，它将我们的 `fd_set`位图复制到内核栈上，正好覆盖已释放的帧。

> `clone`/`setsockopt`/`keyctl`及其他具有大量受控栈局部变量的系统调用工作方式相同。以下是我们的开源 PoC 代码中更多回收帧的方法。

在回收的帧上我们伪造 `rt_mutex_waiter`：

* `tree`

  /`pi_tree`，rb 节点经过精心构造，使擦除操作能给我们一个写入原语。
* `task`

  ，通过其 `physmap`别名设置为 `&init_task`，使链遍历的 task 解引用是安全的。
* `lock`

  ，指向我们喷射到 `sk_buff`数据中并用 KernelSnitch 定位的伪造 `rt_mutex`。

#### **伪造 waiter**

让伪造的 waiter 通过其结构检查和指针解引用需要在已知地址处有受控的内核内存，这与 CEA 在 x86 上扮演的角色相同。

由于 CEA 技巧在 ARM 上不再适用，这里我们用 `sendmsg`喷射 `sk_buff`数据——一种原始字节弹性对象——并用 KernelSnitch 加跨缓存重用来定位它。然后我们将 `lock`指向的伪造 `rt_mutex`放入已定位的 `sk_buff`中，以通过遍历对 `lock`的检查，并使出队的 rb-erase 成为我们唯一的受限写入。

### **用钉子锤击**

在 Android 上，纯数据方式的 LPE 使我们的工作更轻松，因为我们不再需要应对 CFI。但现在我们得到的只是一个带有大量约束的弱指针写入，我们寻找一条类似的函数表劫持路径，就像我们在 Linux 利用中使用的那样。

Project Zero 分析了一个现代的在野 Android 利用，并分享了用相同签名的 `configfs`处理函数覆盖 `ashmem`的 `file_operations`的技巧，将其 `read`/`write`转变为 CFI 无法区分的受限内核读写。

然而，从不受信任的 App 访问 `ashmem`随着时间推移变得越来越困难：

* SDK 29 之前，可以直接打开 `/dev/ashmem`，SELinux 不会报错。
* 面向 SDK 29（Android 10）的 App 不再能直接打开 `/dev/ashmem`，但有一段时间我们仍然可以通过以 `targetSdkVersion`28 或更低构建来规避这一点。
* 现在，即使旧的低 `targetSdkVersion`技巧也失效了，但不受信任的 App 仍然可以通过直接以每次启动的名称打开设备节点来访问驱动程序，即 `/dev/ashmem<boot_id>`。

在 Android 17 上，我们使用 `/dev/ashmem<boot_id>`访问 `ashmem`，并以相同方式劫持 `ashmem_misc.fops`表，将 `configfs`的 `read_iter`/`write_iter`放入其中（这些处理函数是活跃的 `.text`，因此此步骤需要我们在下一节中恢复的 KASLR slide）。

![Ashmem 任意读写概览](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM55cIL9U335dAND1s8Ra3nMK482VQibLt9ibyVNvkASUkDiaiczDgG4KWxzUDIKmCJ4ThNhxLtj8UZqIZ4N6sljw8nPu5xYWdZvXS36dZFnJGDC3Q/640?wx_fmt=svg&from=appmsg)

Ashmem 任意读写概览

![Ashmem 任意读写概览](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM7ran2adz3uApe16iaPE8xqub0aicIWPtkJ56yYW7xWjDKy4MDHTjzruwD25vyb6Dn3sW6dePqu7VibSuxyLaNIgvfOTyYNrQ6vDWRkZDGh6icTYg/640?wx_fmt=svg&from=appmsg)

Ashmem 任意读写概览

如上图所示，我们可以首先使用 `ASHMEM_SET_NAME`修改 `ashmem`的 `private_data`，它随后会在 `configfs`的处理函数中被当作 `struct configfs_buffer* buffer`处理。在我们覆盖了 `ashmem_misc.fops`之后，`read(fd, addr, len)`将使用 `buffer->page`作为目标地址，`write(fd, addr, len)`将使用 `buffer->bin_buffer`，这最终给了我们任意内核内存读写（它来自 `copy_{from,to}_user`，所以有少量额外检查和长度限制。但仍然足以完成 LPE）。

> **Rust 重写能拯救我们吗？**

### **泄露 KASLR，因为我们仍然需要它**

现在唯一的问题是我们知道许多内核地址，但没有一个是可执行的。伪造的 `fops`必须指向可执行内存中真正的 `configfs`处理函数，而 linear-map 别名是不可执行的。

我们已经有来自 GhostLock 的受限任意写入，因此我们寻找一个更合适的地址来覆盖——希望是一个能泄露 KASLR 的地址，也许是通过覆盖一个长度或数据指针。

经过漫长的搜索，我们锁定了 `/proc/sys/kernel/random/boot_id`。它的 sysctl 处理函数 `proc_do_uuid`将表 `.data`指针处的 16 字节格式化为 UUID 字符串。

因此，如果我们使用受限写入将该 `.data`重定向到一个内核已经填入了活跃内核指针的槽位，读取 `boot_id`就会将该指针以 UUID 格式打印回来。解码它并减去其已知的镜像偏移就得到了 KASLR slide。这里那个槽位是 netfilter 的 `loggers[0][1]`，其中存放 `&nfulnl_logger`。整个过程如下所示：

![BootID KASLR 泄露概览](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM7eN4QSughMcYiaicM5HGt83g2sxKA416CdsdjoPGB9F5FmJsicnFz2w1neermJ6tV6rM75TDv9v0amQVbTBV3icPIgAzv4enQ5xDWzpgtBWdOoFg/640?wx_fmt=svg&from=appmsg)

BootID KASLR 泄露概览

![BootID KASLR 泄露概览](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM6Y0OBStELE3CjvS1emKVgqPUxN8ogLqzxFqdUO2cB1foutXEv8LLo1hvibcqLtqmp6f1UGjVF0sUvqKHfoT0kzgNiaEMSNZvH3pIB89WPQicybw/640?wx_fmt=svg&from=appmsg)

BootID KASLR 泄露概览

> 这与 Project Zero 通过 `/proc/self/mounts`读取的 `sel_fs_type`名称指针覆盖是相同的思路，只是改经 `boot_id`和 `proc_do_uuid`实现。

### **最终阶段**

现在我们拥有了替换 `ashmem`函数表并获得任意内核内存读写所需的一切，是时候完成首个 Android 17 root 了！

#### **更进一步**

由于 `STATIC_USERMODEHELPER`在 Android 上已启用，我们需要多几个步骤，而不是直接欺骗 `usermode_helper`以 root 身份执行我们的后门。

使用 `pipe_buffer`（或类似 Page Table Entry 的受害者）来读写内核内存更方便，且几乎没有检查。...
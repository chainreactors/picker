---
title: GhostLock 移植实录：红米 A7 Pro 免解锁 root 与每启动 P0 推导
url: https://mp.weixin.qq.com/s/tDt2dCeUKLJxcA6Hy3fMrg
source: Doonsec's feed
date: 2026-10-25
fetch_date: 2026-10-26T07:16:36.888783
---

# GhostLock 移植实录：红米 A7 Pro 免解锁 root 与每启动 P0 推导

# GhostLock 移植实录：红米 A7 Pro 免解锁 root 与每启动 P0 推导

原创

Red Hunter
Red Hunter

黑白之道

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6N8mVI6CUI1TgtMBmMZWtqN4icCESXGqxMW4hQWrNhax80LgdyqmRAwTCu7Yc5FEFkfyBicm3OE0d6eoh9K7GV6UXrbfHvvmouhE/640?from=appmsg)
> **导语**：CVE-2026-43499 是 Linux 内核里藏了十五年的 futex 优先级继承栈释放后重用漏洞，公开的利用链在 Pixel 上早就跑通了。难的是换到展锐 T8300 芯片的红米 A7 Pro 上——内核镜像每次启动都装在不同的物理地址，而利用链需要这个地址才能写伪造的 file\_operations 表。作者用一次 tracefs 泄漏把这个地址算了出来，在不解锁 Bootloader、不刷任何镜像的前提下三次拿到 root。本文是完整复盘。

![GhostLock 攻击链示意](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6Nd9FPichOgYgA4zYZPPT1YTfQZeicDG05CHyUzqR08aZY2NaZE7VbnOmxAlz7ZZR66CsV3DNRZKcFgFtfgmIic0Or3s7ygfwumnc/640?from=appmsg "GhostLock 攻击链示意")

---

## 一、TL;DR

一台上了锁的手机，一个公开的漏洞，一个每次启动都会变的物理地址。

说人话就是：作者在一台 Bootloader 锁死、verified boot 校验通过的 Redmi A7 Pro 5G（展锐 T8300）上搞到了 root，**全程没有刷任何 boot 镜像，也没有解锁 Bootloader**。这不是锁屏绕过、不是密码绕过——手机正常开机，利用链从一个已授权的 ADB shell 里跑起来。

用到的公开内核漏洞是 GhostLock（CVE-2026-43499）。真正卡住人的是 KASLR 随机化带来的物理地址漂移。作者把 GhostLock 移植到了这台手机上，在三次独立启动里都拿到了 uid-0 的内核凭据补丁，第一次 root 用了 56 秒。不用暴力猜、不用串口，root 是每次启动现给的。

后面还有两次内核 panic，也都写在这篇里。

## 二、设备与威胁模型

目标机是零售版 Redmi A7 Pro 5G，代号 somalia，展锐 T8300（UMS9632），两颗 Cortex-A78 加六颗 Cortex-A55， Mali-G57 MC2 显卡，4 GB 内存，128 GB UFS 存储，Android 16，安全补丁停在 2026-08-01。

这是 user build：`ro.debuggable=0`、`ro.secure=1`，`adb root` 直接被拒绝。

有意思的是安全姿态本身。Bootloader 锁着，verified boot 是绿的，AVB 版本 1.3，八个 erofs 分区通过 dm-verity 只读挂载。设备是 A/B 双槽，但 A 槽已经起不来（`tries_remaining: 0`），所以 B 槽是唯一的 Android 启动路径，misc 分区里还压着一条待执行的 one-shot Bootloader 命令。**每次重启都有掉进 Bootloader 而不是 Android 的风险。**

这个约束塑造了整个过程：任何会让内核 panic 的操作，同时也威胁着这台设备最后一条能用的启动路径。

内核是 6.6.118-android15。`CONFIG_FUTEX_PI=y`，KASLR 开着，KCFI 开着，`kptr_restrict=2`，`CONFIG_STRICT_KERNEL_RWX=y`，`CONFIG_HARDENED_USERCOPY=y`。`CONFIG_USER_NS` 是关的，这堵掉了一整类基于容器的提权路径。shell 进程跑在 uid 2000，但带 readtracefs 组权限——这一点后面很关键。

整个过程默认只读，每次会话都有书面的所有者授权。没有写任何分区，没有解锁 Bootloader，没有改 boot 镜像。payload 只改内存里的内核状态。`/data/local/tmp` 之外唯一的持久化改动，是在 `/data/misc/adb` 下追加了一条 ADB 公钥（用于无线调试引导），做了备份，可还原。

## 三、这个 CVE 到底是谁的

这篇研究不声称自己发现了漏洞。

GhostLock 就是 CVE-2026-43499，由 NebuSec 在《IonStack Part II: GhostLock》里披露，2026-05-21 起在 NVD 和 MITRE 上公开。漏洞在 futex 优先级继承路径的 `remove_waiter()` 里。

具体机制：出问题的版本给 `current->pi_lock` 加了锁，清掉了 `current->pi_blocked_on`，但在 FUTEX\_CMP\_REQUEUE\_PI 的回滚路径上，`current` 实际是 requeuer 而不是 waiter。于是 waiter 带着一个悬垂的 `pi_blocked_on` 指针回到用户态，而这个指针指向的内核栈帧早就被释放了。

公开的说法是「所有 Linux 发行版都存在了 15 年」——这正是这个漏洞比这台手机有意思的地方。

作者用的利用链是公开的那条：aarch64 移植来自 JingMatrix/pixel-ksu-root（commit 65762e7），OnePlus 设备矩阵来自 JoinChang/ghostlock-oneplus，堆指针侧信道的思路来自 TU Graz 的 KernelSnitch。

这个项目自己加的东西是：展锐 T8300 移植、每启动 P0 推导、QEMU 对等实验室，以及那两份事故记录。致谢在 NOTICE 里，完整清单在文末的参考部分。

## 四、利用链

这台设备上的完整顺序：

1. **泄漏虚拟 KASLR 基址**。普通 shell 往 `trace_marker` 写一个标记，然后读 `per_cpu/cpu0/trace_pipe_raw`。记录里的 `ip` 字段保存的是 `tracing_mark_write()` 内部的 `_THIS_IP_` 值，减去这个镜像的固定偏移 `0x1f4ccc` 就得到 `_text`。能这么干是因为 `trace_marker` 全局可写、shell 在 readtracefs 组里、而 raw pipe 不受 `kptr_restrict` 过滤。
2. **从这个 slide 反推 P0**。这是设备定制的步骤，下一节专门讲。
3. **触发 futex UAF**。三个线程加三个 futex 字就能复现 FUTEX\_CMP\_REQUEUE\_PI 的死锁循环，内核返回 `-EDEADLK` 并执行那条会释放 waiter、却留下悬垂指针的回滚路径。
4. **用 pselect6 复用被释放的 waiter 栈**。一个大的 `fd_set` 被拷到已死的 `rt_mutex_waiter` 留下的栈槽上。描述符字节完全由攻击者控制，下一次 PI 链遍历就会把它们当成 waiter 字段读。
5. **把 rb-tree 摘除变成任意写**。unlink 操作会把选定值写到选定内核地址。目标是 ashmem miscdevice 的 fops 指针，通过 P0 提供的物理别名打过去。
6. **伪造 ashmem 的 file\_operations**。假表里的槽位不是用户态代码，而是真实内核函数的地址：configfs 的 read 和 write iterators、`copy_splice_read`、`noop_llseek`。这正是它能在 KCFI 下活下来的原因——KCFI 会拿间接调用目标跟调用点的类型哈希做比对。
7. **通过伪造的表打开 `/dev/ashmem`**，拿到内核读写原语。
8. **升级成基于管道的物理读写**，然后 patch 掉 root 子进程的 `cred` 和 `real_cred`：uid 和 gid 置 0，能力集填满，seccomp 清空，SELinux SID 设成内核 SID。
9. **写 `selinux_state.enforcing = 0`**。这台设备会一直报 Permissive，直到下次重启。

![GhostLock 五步攻击链](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6MiaN2rSpdpsqx41lfXK5OnMazLvrlPXDibdh8p7ZIzw5htLe1fFOic6niccxR5mzBr7ejOadknzyCr8UKgzzy1taCdSVqlXib5rtyU/640?from=appmsg "GhostLock 五步攻击链")

*五步：泄漏、释放、复用、写、拿 root。设备定制的部分，是从同一次 tracefs 泄漏里推出 P0。*

结果是利用子进程里的内核凭据补丁，不是一个交互式 root shell。新的 `adb shell id` 依然是 uid 2000。为了保住一个 uid-0 进程做侦察，第二次运行会先从那个子进程里起一个 abstract socket root server，等子进程退出后它被 init 收养，活到本次启动结束。

## 五、每启动 P0：推导过程

这段是整个项目最值得细读的地方，因为移植能成立全靠它。

上游的 Pixel 利用假设内核镜像坐在一个编译期固定的物理地址上。但展锐这条启动链上没有 U-Boot 环境，也没有 `kernel_addr_r`。内核由 EDK2 固件卷里的 SprdBoot.efi 加载，加载地址是运行时才决定的。

![Boot 链与 TOS 字节](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6MSZmAJmC250A9ibWI0S5H4dLeT9Fnc6PI6LH3iaJ0Hmy1VdRLk2JzskjzuHdsicAzE8FlDtXVMpEiciaOtRvJKIicXF8Q1W9D1DdzTc/640?from=appmsg "Boot 链与 TOS 字节")

*加载器、TrustZone 应答，以及同一个字节最终出现的两个位置：物理加载地址和 KASLR 种子。*

正常启动时，SprdBoot.efi 会用命令 `0x50` 调 TrustZone 协议，带一个 4 字节输出缓冲区。它只读应答的第一个字节，左移 15 位，写进 PCD token 31。这个值随后用在三处：内核读取的目的地址、入口 PC、以及 DTB 属性 `/chosen/kaslr-seed`。也就是说：

```
PCD31        = byte0 << 15
phys(_text)  = 0x80080000 + PCD31
kaslr-seed   = byte0 << 15
```

这个字节是 0 到 255 之间的随机值，所以物理加载地址在 `0x80080000` 到 `0x80878000` 之间，以 32 KiB 为步进。基址 `0x80080000` 本身不是 2 MiB 对齐的。

项目早期有两次尝试用了固定 P0：`0x80000000` 和 `0x80200000`。前者永远低于加载器基址，后者只在 256 个字节里恰好命中一个才正确。**这两次失败不是竞态输了，是压根打到了错误的物理页。**

![P0 加载范围](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6OzFCu1PuIF41sNKdxjuVx2BRz2f8t2Gia3eZNQw7QrhduHL5ASZuwj1eBlMLkBjzxsNAwe4cgQfczZR0r23xBTLBUDkRv1qICY/640?from=appmsg "P0 加载范围")

*加载器基址与 256 个 32 KiB 步进。原先的固定值根本不在候选范围里。*

关键洞察是：**同一个字节既种了虚拟 KASLR，又被 arm64 内核把物理位置的低 21 位编进了虚拟 slide**。源码里写得很直白——KASLR 偏移对 MIN\_KIMG\_ALIGN 取模来自物理放置位置，而不是来自种子。`head.S` 把 identity map 的物理低位 or 进偏移，MIN\_KIMG\_ALIGN 是 2 MiB。所以 slide 的低 21 位就是物理加载地址的低 21 位，而字节的高 2 位在 `(slide >> 21) & 3` 里露出来。

给定泄漏出来的 `_text`，推导是精确的，不需要暴力：

```
KIMAGE_VADDR = 0xffffffc080000000

slide = leaked_text - KIMAGE_VADDR
byte  = (((slide >> 21) & 3) << 6) | \
        ((((slide & 0x1fffff) - 0x80000) & 0x1fffff) >> 15)
P0    = 0x80080000 + (byte << 15)
```

合理性检查是 `0x80080000 <= P0 <= 0x80878000` 和 `(P0 - 0x80080000) % 0x8000 == 0`。算术在 `scripts/ghostlock_p0_from_slide.py` 里。

固件这一侧是反汇编验证的，不是猜的。SprdBoot.efi 调了一个 TOS 随机数辅助函数——TrustZone 命令 `0x50`，4 字节应答，只读第 0 字节，把 `byte << 15` 写进 PCD token 31。应答里另外三个字节直接丢弃。

PCD 31 之后被读了三处：内核读取目的地、入口 PC、以及写 DTB 属性 `/chosen/kaslr-seed` 的地方，写出去时做了字节序翻转。内核的 `kaslr_early_init` 消费掉这个属性之后就把它清零了。

![TOS 字节流向](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6PUqymF3hQlzv136iaRAZQajml2CIW4fRd3yZicZb6dPu8yaicvszVIjNjb9hTibVn5P3BgBbRGnVBd6voGyqRCNNfYhUnbvQic9hOY/640?from=appmsg "TOS 字节流向")

*这就是为什么静态分析 OTA 镜像得不到 P0——那个字节不在镜像里。内核的 kaslr\_early\_init 消费并清零了该属性，因此早期启动之后就无法恢复。这就是活着的 slide 成为唯一幸存副本的原因。*

算出来的结果跟实际记录吻合：

| 泄漏的 \_text | Slide | TOS 字节 | P0 | 结果 |
| --- | --- | --- | --- | --- |
| 0xffffffd080628000 | 0x1000628000 | 0xf5 | 0x80828000 | 第一次 root |
| 0xffffffd080720000 | 0x1000720000 | 0xd4 | 0x80720000 | debugfs panic 之后重新拿 root |
| 0xffffffd0801f0000 | 0x10001f0000 | 0x2e | 0x801f0000 | binder panic 之后重新拿 root |

中间那组数值也解释了之前固定 P0 为什么失败。第二次固定尝试用的是 `0x80200000`，但那次启动的实际加载地址是 `0x80368000`，差了 `0x168000`。伪造的写落在了错误的物理页上。**从头到尾就不是时序问题。**

第一次用推导 P0 的运行，泄漏到的 `_text` 是 `0xffffffd080628000`，slide 算出 `0x1000628000`，得到字节 `0xf5`、P0 `0x80828000`。用这个值构建的 payload 第一次尝试就命中：**56 秒，没有 panic**。

事后有两次独立的 root-only 读取印证了这个值：`uboot_log` 里有 `Start linux at PC:0x80828000` 这行，`/proc/iomem` 报告 `Kernel code at 0x80838000`，正好是 `_text + 0x10000`。这两次读取对利用本身都不是必需的——tracefs 泄漏先给出了答案。

推导是每次启动算一次。TOS 字节不在 OTA 镜像里，DTB 种子被内核早期清零，`/proc/iomem` 对 shell 是拒绝的。**这个值唯一的幸存副本就是活着的 slide。** 运行时的启动器把闭环合上了——泄漏 KASLR、在 payload 里算 P0、然后直接跑，下一次启动不需要在主机侧重新构建。

## 六、QEMU 实验室与 KCFI

在一台只有一个可启动槽位的设备上盲跑内核利用是个坏主意。所以上真机之前，整条链先在 QEMU 实验室里验证过。

厂商那个精确的 Image 能在 QEMU 里一路启动到 `/init`，并在虚拟机内复现 tracefs 泄漏。另一个源码对等的 GKI 6.6.118 构建在同一 banner commit 也能启动，但它的 clang 和配置不同，会把 `_THIS_IP_` 偏移从厂商的 `0x1f4ccc` 变成 `0x19ac64`。

**这个差异正是为什么偏移量是目标头文件的一部分，而不是一个通用常量。** 原版利用链在虚拟机内第一次尝试就完成了完整的 uid-0 凭据补丁。

实验室定下了两件真机运行依赖的事。

第一件是 KCFI（内核控制流完整性）。KCFI 会拿间接调用的目标跟调用点的类型哈希做比对。伪造的 fops 表里每个槽位都是类型正确的真实内核函数，所以这张表在不禁用任何缓解措施的情况下就是合法的——伪造的 fops 表能过检查，是因为每个槽位都是类型哈希匹配的真实内核函数，而不是因为 KCFI 缺席。

第二件是 pselect 重试逻辑。进程内刷新在 CFI 未命中之后会卡在一次慢速的第二次 groom 上，而进程级的 SIGALRM 看门狗跨线程也不可用。最后接受的修法是：每个进程只做一次 p...
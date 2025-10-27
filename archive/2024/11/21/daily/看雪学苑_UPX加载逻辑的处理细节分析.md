---
title: UPX加载逻辑的处理细节分析
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458583542&idx=1&sn=bf8405a303cf9d5ec7b80cf8d8eebf7e&chksm=b18c317c86fbb86a57e02cf5b34928c747e9f8b7e462ed57c7d6af5076cd5668b7482e86c535&scene=58&subscene=0#rd
source: 看雪学苑
date: 2024-11-21
fetch_date: 2025-10-06T19:16:17.859064
---

# UPX加载逻辑的处理细节分析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FGMzLvlHUiae0Bey2fMKCqOFq5uA31EMoYgO9YzCQ7rPUTgrYLPGdPtw9Z00Mib5pVh7UbRhzjGXxg/0?wx_fmt=jpeg)

# UPX加载逻辑的处理细节分析

Bogger

看雪学苑

在本人第一篇博客UPX代码buildloader函数分析（*https://bbs.kanxue.com/thread-283702.htm*），对加载器初始化过程阐明了不同条件下的加载逻辑，本文根据其**加载逻辑进行更细致的分析其操作细节。**

首先在文件*src\stub\src\amd64-win64.pe.S*中发现**PE文件加壳入口点：**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FGMzLvlHUiae0Bey2fMKCqOWekZT22ygttI0rS8LF5LBctQF44zwhXxia6PgXElOfd0hbOg9nPsQdA/640?wx_fmt=other&from=appmsg)

`.intel_syntax noprefix`是用于汇编语言的编译器指令，主要用于告诉汇编器使用**Intel 语法**来解析接下来的代码，并且在操作数之前不加任何前缀（`noprefix`）。

接下来按照加载逻辑的添加顺序分别分析其处理细节：

✦

**PEISDLL0与PEISEFI0**

✦

### 如果是dll文件，添加逻辑PEISDLL0

```
section         PEISDLL0
                mov     [rsp + 8], rcx
                mov     [rsp + 0x10], rdx
                mov     [rsp + 0x18], r8
```

在 Windows的 x64调用约定中，rcx是第一个参数，rdx是第二个参数，r8是第三个参数。因此在函数调用前保存参数。

### 如果是efi文件，添加逻辑PEISEFI0

```
section         PEISEFI0
                push     rcx
                push     rdx
```

此处处理过程与 PEISDLL0类似，保存了 rcx和 rdx 的内容，但这里的压栈方式不同，是直接将它们压入栈顶。可能是为了适应 EFI 系统环境的不同调用约定。

✦

**主程序解密逻辑**

✦

### 如果是dll文件，添加逻辑PEISDLL1

```
section         PEISDLL1
                cmp     dl, 1
                jnz     reloc_end_jmp
```

如果是dll文件，在主程序入口前还需要添加**初始化逻辑，判断是否是dll文件的卸载操作**。在 Windows 系统中，dl 在 DLL 入口点（DllMain 函数）中传递给 DLL 的 fdwReason 参数，值为 1 时表示 DLL 正在被卸载`（DLL_PROCESS_DETACH）`。在此处如果值并不为1（不是卸载操作），则程序将跳转到`reloc_end_jmp`标签，继续正常的初始化流程。

### PEMAINO1——主程序的入口点

```
section         PEMAIN01
                //; remember to keep stack aligned!
                push    rbx
                push    rsi
                push    rdi
                push    rbp
                lea     rsi, [rip + start_of_compressed]
                lea     rdi, [rsi + start_of_uncompressed]
```

这一部分代码是为压缩数据解压作准备的主要逻辑。**将压缩后的数据解压到内存中的指定位置，然后继续执行原始程序代码。**

a)   首先保存寄存器rbx、rsi、rdi 和 rbp的值。

b)`lea rsi, [rip + start_of_compressed]`计算压缩数据的起始地址，并存入 rsi 寄存器，其中rip 是当前指令地址。

c)`lea rdi, [rsi + start_of_uncompressed]`则计算未压缩数据的起始地址，存入 rdi 寄存器。

最后rsi 指向压缩数据，而 rdi 指向解压后的数据。

### 图标对应指令PEICONS1和PEICONS2

```
section         PEICONS1
                incw    [rdi + icon_offset]
section         PEICONS2
                add     [rdi + icon_offset], IMM16(icon_delta)
```

1.将内存地址`[rdi + icon_offset]`处的 16 位字增加 1,**更新图标的索引。**

2.将立即数`icon_delta`加到内存地址`[rdi + icon_offset]`上,过增量**更新图标的偏移。**

### 如果 tmp\_tlsindex 有效，添加指令PETLSHAK

```
section         PETLSHAK
                lea     rax, [rdi + tls_address]
                push    [rax]   // save the TLS index
                mov     [rax],  IMM32(tls_value) // restore compressed data overwritten by the TLS index
                push    rax
```

处理**TLS 相关的初始化操作**，包括保存和恢复被 TLS 索引覆盖的数据，确保数据正确性。

1.将`rdi + tls_address`的有效地址加载到 rax 寄存器中，指向 TLS（线程本地存储）地址。

2.将 rax 寄存器指向的内存值（即 TLS 索引）压入栈中保存。

3.将 tls\_value 存入 rax 指向的内存位置，恢复之前被 TLS 索引覆盖的数据。

4.将 rax 寄存器的值压入栈中保存。

### 如果压缩方法是LZMA，执行解压缩

```
.intel_syntax noprefix
section         LZMA_HEAD
                mov     eax, IMM32(lzma_u_len)
                push    rax
                mov     rcx, rsp
                mov     rdx, rdi
                mov     rdi, rsi
                mov     esi, IMM32(lzma_c_len)

.att_syntax
#define NO_RED_ZONE
#include "arch/amd64/regs.h"
#include "arch/amd64/lzma_d.S"

.intel_syntax noprefix
section         LZMA_TAIL
                leave
                pop     rax
```

LZMA\_HEAD**初始化了解压缩参数**，如压缩和解压数据的长度、内存位置等。

LZMA\_TAIL 则是**清理操作**，负责恢复栈并弹出数据，标志着解压过程的结束。

其中的regs.h头文件保存了对寄存器的相关信息：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FGMzLvlHUiae0Bey2fMKCqOthD3fb48ayia6o10SxDZU6ovca2RxzOwqweKXHPcjbicic8hUicibK0uTZg/640?wx_fmt=other&from=appmsg)

lzma\_d.S文件则是其中解压缩的算法实现文件，主要涉及**解码和处理 LZMA 压缩数据的逻辑**，对应添加指令LZMA\_ELF00，LZMA\_DEC20

在调用解密函数前，进行了**调用约定、压缩类型检查、解码器初始化以及堆栈分配对齐**。最后根据条件编译，选择不同的文件引入解码函数。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FGMzLvlHUiae0Bey2fMKCqOk6Ue3ibcFibSM2atNyu1LfaztTjnoWBAEYIiahXy3SyvzwoZZZqJ9IHjg/640?wx_fmt=other&from=appmsg)

这里其中lzma\_d\_cs.S、lzma\_d\_cf.S以及lzma\_d\_cn.S都是由汇编机器码组成的汇编文件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FGMzLvlHUiae0Bey2fMKCqOZJcJ7T3jNQa59uOQR1Sl7yQxbZ9OnX2MibBQqol4lBzdjJpIgdwhfjg/640?wx_fmt=png&from=appmsg)

### 如果压缩方法是NRV，执行解压缩

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FGMzLvlHUiae0Bey2fMKCqOJZTJQ36GEjf8QCiafKnncaQ8GTogicaBjicoiclYoib7ib6oiaP2XvBp66rlg/640?wx_fmt=other&from=appmsg)

NRV算法对应有2B、2D以及2E，这里以2E为例，即执行指令NRV2E。可见指令同样引入文件nrv2e\_d.S，这里对解压缩主要流程进行分析。

**1. 字节处理**

```
top_n2e:
    movb (%rsi),%dl  # speculate: literal, or bottom 8 bits of offset
    jnextb1yp lit_n2e
```

从 rsi（源指针）处获取下一个字节，并存储到 %dl 中。这一步**推测该字节是字面值（literal）还是偏移值**的一部分。然后根据寄存器的数据，跳转到 lit\_n2e 处理字面值数据。

```
lit_n2e:
    incq %rsi; movb %dl,(%rdi)
    incq %rdi
```

如果判定当前字节是字面值数据，则将其存储到目标位置 %rdi，并递增源和目标地址指针，准备处理下一个字节。

**2. 偏移与长度计算**

```
off_n2e:
    dec off
    getnextbp(off)
getoff_n2e:
    getnextbp(off)
    jnextb0np off_n2e
```

处理偏移值（off），首先从输入数据中获取偏移值的高位字节。

```
subl $ 3,off; jc offprev_n2e
shll $ 8,off; movzbl %dl,%edx
orl %edx,off; incq %rsi
xorl $~0,off; jz eof
sarl off  # Carry= original low bit
```

调整偏移值，判断是否需要跨越多个字节计算。如果偏移值满足某些条件（例如低位较小），会跳转到 offprev\_n2e。

off 最终得到的是需要从目标位置向后移动的距离，它决定了从哪里复制数据。

```
len_n2e:
    getnextb(len)
    jnextb0n len_n2e
    addl $6-2-2,len
```

从源数据中获取解压数据块的长度，利用 getnextb 函数从输入流中读取长度值。

**3. 数据复制**

```
gotlen_n2e:
    cmpq $-0x500,dispq
    adcl $2,len  # len += 2+ (disp < -0x500);
    call copy
```

根据前面解析出来的偏移值和长度，调用 copy 函数，**复制解压出来的数据块到目标位置**。这里的 adcl 指令根据偏移的大小，调整解压出的数据块长度。

NRV2E 压缩格式的解压流程：通过**多次从压缩数据中读取字节或位，代码能够逐步解析出偏移和长度信息，随后将数据块从先前的位置复制到新的位置，完成解压缩过程。**

✦

**导入表处理**

✦

### 1. 设置栈空间

```
sub     rsp, 0x28
lea     rdi, [rsi + compressed_imports]
```

分配栈空间，并将 compressed\_imports 加载到 rdi 中，准备开始解析导入表。

### 2. 加载导入表

```
next_dll:
mov     eax, [rdi]
or      eax, eax
jz      SHORT(imports_done)
mov     ebx, [rdi + 4]    // iat
lea     rcx, [rax + rsi + start_of_imports]
add     rbx, rsi
add     rdi, 8
call    [rip + LoadLibraryA]
xchg    rax, rbp
```

读取dll的名称地址，如果名称为空(eax=0)，则跳转到imports\_done结束导入表的修复。否则，继续准备加载dll的导入表，调用系统API函数LoadLibraryA加载dll，并将结果保存在rbp中。

### 3.遍历dll

```
next_func:
mov     al, [rdi]
inc     rdi
or      al, al
jz      next_dll
```

从 rdi 读取当前导入函数的标识符。如果标识符为 0，说明所有函数已处理完毕，跳转到 next\_dll 处理下一个 DLL。

### 4.按序号导入

```
section PEK32ORD
jpe     not_kernel32
mov     eax, [rdi]
add     rdi, 4
mov     rax, [rax + rsi + kernel32_ordinals]
jmp     SHORT(next_imp)
```

如果当前导入函数属于 kernel32.dll，则根据序号查找该函数的地址。

### 5.按名称导入

```
byname:
mov     rcx, rdi
mov     rdx, rdi
dec     eax
repne
scasb
first_imp:
mov     rcx, rbp
call    [rip + GetProcAddress]
```

如果函数按名称导入，使用 GetProcAddress 来获取函数地址。这里先通过 repne scasb 搜索字符串（函数名称），然后调用 GetProcAddress 获取函数的内存地址。

### 6.存取函数地址

```
next_imp:
mov     [rbx], rax
add     rbx, 8
jmp     SHORT(next_func)
```

将获取到的函数地址存储到 IAT 中，并继续处理下一个函数。

### 7.错误处理

```
imp_failed:
add     rsp, 0x28
pop     rbp
pop     rdi
pop     rsi
pop     rbx
xor     eax, eax
ret
```

如果导入失败，则清理栈空间，返回 eax = 0 表示失败。

这段代码**动态解析并加载 PE 文件的导入表**，加载所需的 DLL 并获取函数地址，完成导入表修复的任务。

✦

**重定位表处理**

✦

### 1.重定位表遍历

```
section PERELOC1
lea     rdi, [rsi + start_of_relocs]

section PERELOC2
add     rdi, 4
section PERELOC3
lea     rbx, [rsi - 4]
reloc_main:
xor     eax, eax
mov     al, [rdi]
inc     rdi
or      eax, eax
jz      SHORT(reloc_endx)
cmp     al, 0xEF
ja      reloc_fx
```

首先将重定位表地址初始化。然后每次从重定位表读取一个字节并检查其值。如果为 0x00，表示重定位表处理完毕，跳转到 reloc\_endx 结束处理。如果字节值大于 0xEF，则跳转到 reloc\_fx 处理其他类型的重定位项。

### 2.应用重定位

```
reloc_add:
add     rbx, rax
mov     rax, [rbx]
bswap   rax
add     rax, rsi
mov     [rbx], rax
jmp     reloc_main
```

将偏移量加到 rbx，然后从 rbx 地址加载目标地址（目标地址是反向字节序，因此使用 bswap 交换字节顺序）。接着，将目标地址加上基址 rsi，以便修正地址引用，并将结果存回原位置。

### 3.处理特殊重定位项

```
reloc_fx:
and     al, 0x0F
shl     eax, 16
mov     ax, [rdi]
add     rdi, 2
```

对于特殊的重定位项，使用低 4 位并移位来计算偏移。然后从 rdi 中读取额外的 2 个字节作为偏移量，进行地址修正。

### 4.高位和低位重定位的处理

#### 1.低位重定位

```
section PERLOHI0
xchg    rdi, rsi
lea     rcx, [r...
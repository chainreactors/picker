---
title: ARM64内核 Hook 研究
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458492659&idx=1&sn=6685b0f69a72da4de3fdd89471792498&chksm=b18eae7986f9276f47f37fcdc1892c48691894c31d9f7db47937949ff38fa594816db0987a82&scene=58&subscene=0#rd
source: 看雪学院
date: 2023-01-17
fetch_date: 2025-10-04T04:03:34.457907
---

# ARM64内核 Hook 研究

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Fz4lU5jRTibIbrXKXTr0s8TYC74V8ZzZoKRBBZB4RTCx1HgeJk10HjGuTGESW0drAC0fGsWyfsFqg/0?wx_fmt=jpeg)

# ARM64内核 Hook 研究

Ylarod

看雪学苑

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Fz4lU5jRTibIbrXKXTr0s8T5xeZdg3ib6ulz2ib4ffFUZhC9ib5yAgVc7UKdXbQfvc4dcXvanGaTVGibg/640?wx_fmt=jpeg)

本文为看雪论坛优秀文章

看雪论坛作者ID：Ylarod

本篇将实现一个劫持内核内BL指令跳转到自身模块函数执行的简单inline hook。

#

#

```
一

ARM64 指令基础
```

##

## **BL 指令**

跳转到相对于PC的指定地址，并将下一条指令地址存入LR寄存器。

跳转范围：±128MB

###

### 指令格式

```
31 | 30 29 28 27 26 | 25 ... 01  | 0  0  1  0  1  |  imm26
```

###

### 地址编码

imm26 负数使用补码表示

> 正数和0的补码就是该数字本身再补上符号位0。负数的补码则是将其对应正数按位取反再加1。

可能有人会有疑惑，明明立即数只有26位，跳转范围应该是±32MB才对，为什么会是±128MB呢？

因为arm64指令长度都是4字节，所以编码地址的时候除了4，比如跳转 0x4，imm26 是 1。

###

### 简单例子

```
BL 0x40b100101 00000000000000000000000001 BL -0x40b100101 11111111111111111111111111
```

###

### 使用keystone生成机器码

```
from keystone import *import structks = Ks(KS_ARCH_ARM64, KS_MODE_LITTLE_ENDIAN)code, count = ks.asm("BL 0x4")code = struct.unpack("<I", bytes(code))[0]print(bin(code))
```

###

### 以上代码输出：

0b10010100000000000000000000000001

###

### 模拟运行一下试试吧。

```
from capstone import *from keystone import *from unicorn import * test_code = """NOPmov x0, #1b 0x14add x0, x0, #1add x0, x0, #1add x0, x0, #1add x0, x0, #1""" def hook_code(_mu, address, size, user_data):    instruction = _mu.mem_read(address, size)    # 将地址设置为0，来得到原始的相对跳转地址    # 设置成address可以得到实际跳转地址    for i in cs.disasm(instruction, 0x0):        print('[0x%08X] %s\t%s' % (address, i.mnemonic, i.op_str)) ks = Ks(KS_ARCH_ARM64, KS_MODE_LITTLE_ENDIAN)cs = Cs(CS_ARCH_ARM64, CS_MODE_ARM)code, code_count = ks.asm(test_code) mu = Uc(UC_ARCH_ARM64, UC_MODE_ARM)mu.mem_map(0x0, 0x1000, UC_PROT_ALL)mu.mem_write(0x0, bytes(code))mu.hook_add(UC_HOOK_CODE, hook_code)mu.emu_start(0x0, code_count * 4)
```

#

输出如下：

[0x00000000] nop

[0x00000004] movz x0, #0x1

[0x00000008] b #0xc

[0x00000014] add x0, x0, #1

[0x00000018] add x0, x0, #1

#

#

```
二

相关内核基础
```

##

## **内核分段及权限设定**

###

### **1、分了哪些段**

见 arch/arm64/kernel/vmlinux.lds.S

* \_text → \_etext 之间是代码段。
* start\_rodata → end\_rodata 之间是只读数据段。
* init\_begin → init\_end 之间是内核初始化相关的段，包括代码和数据。
* \_data → \_end 之间是可读可写的数据段。

###

### **2、各个段的权限设定**

见 arch/arm64/mm/mmu.c 的 map\_kernel 函数

```
pgprot_t text_prot = rodata_enabled ? PAGE_KERNEL_ROX : PAGE_KERNEL_EXEC;map_kernel_segment(pgdp, _text, _etext, text_prot, &vmlinux_text, 0,               VM_NO_GUARD);map_kernel_segment(pgdp, __start_rodata, __inittext_begin, PAGE_KERNEL,               &vmlinux_rodata, NO_CONT_MAPPINGS, VM_NO_GUARD);map_kernel_segment(pgdp, __inittext_begin, __inittext_end, text_prot,               &vmlinux_inittext, 0, VM_NO_GUARD);map_kernel_segment(pgdp, __initdata_begin, __initdata_end, PAGE_KERNEL,               &vmlinux_initdata, 0, VM_NO_GUARD);map_kernel_segment(pgdp, _data, _end, PAGE_KERNEL, &vmlinux_data, 0, 0);
```

###

```
#define _PROT_DEFAULT        (PTE_TYPE_PAGE | PTE_AF | PTE_SHARED)#define PROT_DEFAULT        (_PROT_DEFAULT | PTE_MAYBE_NG)#define PROT_NORMAL        (PROT_DEFAULT | PTE_PXN | PTE_UXN | PTE_WRITE | PTE_ATTRINDX(MT_NORMAL))#define PAGE_KERNEL        __pgprot(PROT_NORMAL)#define PAGE_KERNEL_ROX        __pgprot((PROT_NORMAL & ~(PTE_WRITE | PTE_PXN)) | PTE_RDONLY)#define PAGE_KERNEL_EXEC    __pgprot(PROT_NORMAL & ~PTE_PXN)
```

###

###

### **3、结论**

###

### 代码段：\_text → \_etext

### rodata\_enabled ? PAGE\_KERNEL\_ROX : PAGE\_KERNEL\_EXEC;

### 可读特权模式可执行，rodata\_enabled为假时可写

###

### 只读数据段

### PAGE\_KERNEL

### 可读可写不可执行

###

### 初始化代码段：

### rodata\_enabled ? PAGE\_KERNEL\_ROX : PAGE\_KERNEL\_EXEC;

### 可读特权模式可执行，rodata\_enabled为假时可写

###

### 初始化数据段：

### PAGE\_KERNEL

### 可读可写不可执行

###

### 数据段：

### PAGE\_KERNEL

### 可读可写不可执行

##

## **寻找对应符号地址**

开了KASLR怎么办？摆！

###

### 方法一：kallsyms文件

解除内核符号限制

```
echo 0 > /proc/sys/kernel/kptr_restrict
```

> 部分设备需要 echo 1 才行

获取符号地址

```
cat /proc/kallsyms | grep xxxxx
```

###

### 方法二：kprobe大法 (\*推荐)

上代码：

```
uintptr_t kprobe_get_addr(const char *symbol_name) {    int ret;    struct kprobe kp;    uintptr_t tmp = 0;    kp.addr = 0;    kp.symbol_name = symbol_name;    ret = register_kprobe(&kp);    tmp = kp.addr;    if (ret < 0) {        goto out; // not function, maybe symbol    }    unregister_kprobe(&kp);out:    return tmp;}
```

底层原理：

使用 kallsyms\_lookup\_name 解析符号地址

> 需高版本内核！

###

### 方法三：kallsyms\_lookup\_name函数

如果该函数导出，可直接使用该函数定位，但是大部分内核中该函数并未导出。

###

### 方法四：奇门遁甲

###

### ① 将内核丢进IDA分析，依靠字符串和源码慢慢寻找位置

###

### ② 特征码定位

### 通过一些特征汇编代码定位

###

### ③ 根据导出函数，结合偏移辅助定位

### 比如 &printk - offsetof(printk) + offsetof(foo)

#

#

```
三

让我们开始吧
```

##

## **绕过内核只读限制**

###

### 方法一

修改内核，将 rodata\_enabled 改为 0

优点：简单方便，快捷高效

缺点：安全性降低

评价：开发机要什么安全，方便就完了！

###

### 方法二

修改pte，给权限加上可写

详见下面代码：

*https://github.com/null0333/aarch64\_silent\_syscall\_hook/blob/master/set\_page\_flags.c#L48*

##

## **开始写hook**

目标：\_\_arm64\_sys\_faccessat 的 BL do\_faccessat

目的：/memfd: 今天必须给我存在

```
__arm64_sys_faccessat var_s0          =  0     HINT            #0x19    STR             X30, [X18],#8    STP             X29, X30, [SP,#-0x10+var_s0]!    MOV             X29, SP    LDR             W8, [X0]    LDR             X1, [X0,#8]    LDR             W2, [X0,#0x10]    MOV             W3, WZR    MOV             W0, W8    BL              do_faccessat    LDP             X29, X30, [SP+var_s0],#0x10    LDR             X30, [X18,#-8]!    HINT            #0x1D    RET; End of function __arm64_sys_faccessat
```

代码：

```
#include <linux/cpu.h>#include <linux/memory.h>#include <linux/uaccess.h>#include <linux/init.h>#include <linux/module.h>#include <linux/kprobes.h>#include <linux/printk.h>#include <linux/string.h>#include <asm-generic/errno-base.h> #ifdef pr_fmt#undef pr_fmt#define pr_fmt(fmt) "InlineHookDemo: " fmt#endif static const uint32_t mbits = 6u;static const uint32_t mask  = 0xfc000000u; // 0b11111100000000000000000000000000static const uint32_t rmask = 0x03ffffffu; // 0b00000011111111111111111111111111static const uint32_t op_bl = 0x94000000u; // "bl" ADDR_PCREL26 typedef long (*do_faccessat_t)(int, const char __user *, int, int) ;static do_faccessat_t my_do_faccessat; unsigned int orig_insn, hijack_insn;unsigned long func_addr, insn_addr = 0; uintptr_t kprobe_get_addr(const char *symbol_name) {    int ret;    struct kprobe kp;    uintptr_t tmp = 0;    kp.addr = 0;    kp.symbol_name = symbol_name;    ret = register_kprobe(&kp);    tmp = (uintptr_t)kp.addr;    if (ret < 0) {        goto out; // not function, maybe symbol    }    unregister_kprobe(&kp);out:    return tmp;} bool is_bl_insn(unsigned long addr){    uint32_t insn = *(uint32_t*)addr;    const uint32_t opc = insn & mask;    if (opc == op_bl) {        return true;    }    return false;} uint64_t get_bl_target(unsigned long addr){    uint32_t insn = *(uint32_t*)addr;    int64_t absolute_addr = (int64_t)(addr) + ((int32_t)(insn << mbits) >> (mbits - 2u)); // sign-extended    return (uint64_t)absolute_addr;} uint32_t build_bl_insn(unsigned long addr, unsigned long target){    uint32_t insn = *(uint32_t*)addr;    const uint32_t opc = insn & mask;    int64_t new_pc_offset = ((int64_t)target - (int64_t)(addr)) >> 2; // shifted    uint32_t new_insn = opc | (new_pc_offset & ~mask);    return new_insn;} uint32_t get_insn(unsigned long addr){    return *(unsigned int*)addr;} void set_insn(unsigned long addr, unsigned int insn){    cpus_read_lock();    *(unsigned int*)addr = insn;    cpus_read_unlock();} long hijack_do_faccessat(int dfd, const char __user *filename, int mode, int flags){    char prefix[8];    pr_emerg("hijack success!");    copy_from_user(prefix, filename, 8);    prefix[7] = 0;    pr_emerg("access: %s", prefix);    if (strcmp(prefix, "/memfd:") == 0) {        pr_emerg("magic!");        return 0;    }    return my_do_faccessat(dfd, filename, mode, flags);} int ihd_init(void){    int i;     // 获取函数地址    func_addr = kprobe_get_addr("__arm64_sys_faccessat");    pr_emerg("...
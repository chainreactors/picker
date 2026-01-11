---
title: 深入浅出 Keystone 框架学习
url: https://mp.weixin.qq.com/s/x6jIP1sJkT1vdCvoUOIV0g
source: Doonsec's feed
date: 2026-01-10
fetch_date: 2026-01-11T03:37:54.488306
---

# 深入浅出 Keystone 框架学习

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GU7Z2cSK0VVkqRmRTec3xAv1lPINuzMNO6e0mTfEmlnZZBR3aSoUJW7nYXDay1hW5JWP60xL80QA/0?wx_fmt=jpeg)

# 深入浅出 Keystone 框架学习

xiusi

看雪学苑

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GU7Z2cSK0VVkqRmRTec3xAR7DfnpK5gaxMUggxXTYbTkwiaJshu04Af0XNGud7vwiaf720szOCnLxg/640?wx_fmt=png&from=appmsg)

**一、前言**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GU7Z2cSK0VVkqRmRTec3xAR7DfnpK5gaxMUggxXTYbTkwiaJshu04Af0XNGud7vwiaf720szOCnLxg/640?wx_fmt=png&from=appmsg)

# 通过此前的文章，我们已经掌握了两大框架。在逆向工程的工具链中，它们各司其职：

* **Unicorn (大脑)**：负责**跑**代码。它模拟 CPU 的状态流转与内存交互。

  > [原创]深入浅出 Unicorn 框架学习
* **Capstone (眼睛)**：负责**看**代码。它将枯燥的机器码翻译成人类可读的汇编语言。

  > [原创]深入浅出 Capstone 框架学习

然而，仅有“大脑”和“眼睛”是不够的。当我们想要修改程序的逻辑（例如 Patch 掉反调试检查、注入 Shellcode）时，我们需要——**Keystone (双手)**。

### 1. 什么是 Keystone？

**Keystone**是一个轻量级、多平台、多架构的汇编框架。它的作用与 Capstone 正好相反：**Capstone 将机器码转为汇编，而 Keystone 将汇编代码编译回机器码。**

### 2. Keystone 的核心价值

* **人类可读 -> 机器可读**

  例如，将`INC RAX` 瞬间转换为`\x48\xFF\xC0`。
* **多架构支持**

  一套 API 搞定 x86, ARM, MIPS, PowerPC, SPARC 等所有主流架构，无需安装笨重的 GCC 或各种交叉编译工具链。
* **动态灵活**

  它是一个库（Library），而不是一个独立的编译器。这意味着你可以在 Python 脚本运行时动态生成代码，无需调用外部程序。

##

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GU7Z2cSK0VVkqRmRTec3xAR7DfnpK5gaxMUggxXTYbTkwiaJshu04Af0XNGud7vwiaf720szOCnLxg/640?wx_fmt=png&from=appmsg)

**二、环境准备与基础概念**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GU7Z2cSK0VVkqRmRTec3xAR7DfnpK5gaxMUggxXTYbTkwiaJshu04Af0XNGud7vwiaf720szOCnLxg/640?wx_fmt=png&from=appmsg)

### 1. 环境安装

```
# 正确做法：安装 Keystone 汇编引擎
pip install keystone-engine

# 错误做法：安装 'keystone'
# 'keystone' 是 OpenStack 的身份认证组件，装错会导致冲突！
```

### 2. 核心类解析

在 Python 脚本中，我们主要使用以下两个类：

* **`Ks`**
  **(Keystone Engine)**
  这是汇编引擎的主入口。你需要实例化它来创建一个汇编器对象。

+ *初始化*：`ks = Ks(arch, mode)`
+ *核心方法*

  ：`ks.asm(code_string, addr)`

* **`KsError`**
  **(Exception)**
  异常处理类。当你的汇编代码有语法错误（如拼写错误、操作数不匹配）时，Keystone 会抛出此异常。

### 3. 架构与模式 (Architecture & Mode)

Keystone 的常量命名规范与 Unicorn/Capstone 保持高度一致，只需将前缀`UC_` 或`CS_` 换成 **`KS_`**即可。

**常用组合对照表**：

| 目标环境 | Unicorn | Capstone | Keystone |
| --- | --- | --- | --- |
| **x86 (32位)** | `UC_ARCH_X86`,`UC_MODE_32` | `CS_ARCH_X86`,`CS_MODE_32` | **`KS_ARCH_X86`**  **, `KS_MODE_32`** |
| **x64 (64位)** | `UC_ARCH_X86`,`UC_MODE_64` | `CS_ARCH_X86`,`CS_MODE_64` | **`KS_ARCH_X86`**  **, `KS_MODE_64`** |
| **ARM (32位)** | `UC_ARCH_ARM`,`UC_MODE_ARM` | `CS_ARCH_ARM`,`CS_MODE_ARM` | **`KS_ARCH_ARM`**  **, `KS_MODE_ARM`** |
| **ARM Thumb** | `UC_ARCH_ARM`,`UC_MODE_THUMB` | `CS_ARCH_ARM`,`CS_MODE_THUMB` | **`KS_ARCH_ARM`**  **, `KS_MODE_THUMB`** |

### 4. 语法格式 (Syntax)

对于 x86 架构，汇编语言有不同的格式。Keystone 允许通过`KS_OPT_SYNTAX`选项来切换语法风格。

* **`KS_OPT_SYNTAX_INTEL`**(默认)：Intel 语法。

+ *特点*：`mov dst, src`。绝大多数逆向工具（IDA, x64dbg）的默认风格。
+ *示例*：`mov eax, 1`

* **`KS_OPT_SYNTAX_ATT`**：AT&T 语法。

+ *特点*：`mov src, dst`，寄存器前加`%`，立即数加`$`。Linux/GDB 常用。
+ *示例*

  ：`mov $1, %eax`

* **`KS_OPT_SYNTAX_NASM`**：NASM 语法。

+ *特点*：与 Intel 类似，但在内存寻址和宏处理上更严格。

**设置方法**：

```
ks = Ks(KS_ARCH_X86, KS_MODE_64)
# 切换到 AT&T 语法
ks.syntax = KS_OPT_SYNTAX_ATT
```

---

##

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GU7Z2cSK0VVkqRmRTec3xAR7DfnpK5gaxMUggxXTYbTkwiaJshu04Af0XNGud7vwiaf720szOCnLxg/640?wx_fmt=png&from=appmsg)

**三、静态汇编初体验**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GU7Z2cSK0VVkqRmRTec3xAR7DfnpK5gaxMUggxXTYbTkwiaJshu04Af0XNGud7vwiaf720szOCnLxg/640?wx_fmt=png&from=appmsg)

在将 Keystone 集成到 Unicorn 之前，我们先单独运行它，体验一下如何将一句汇编代码翻译成机器码。

**目标**

将汇编指令`"xor rax, rax; inc rax"`编译为 x64 机器码。

**示例代码：**

```
from keystone import *

# 1. 准备汇编代码
# 使用分号 ; 分隔多条指令
ASSEMBLY = "xor rax, rax; inc rax"

try:
# 2. 初始化汇编引擎
# 架构: x86, 模式: 64位
    ks = Ks(KS_ARCH_X86, KS_MODE_64)

# 3. 执行编译 (Assemble)
# ks.asm(code, addr=0)
# code: 汇编字符串
# addr: (可选) 起始地址，用于计算相对跳转偏移，默认为 0
    encoding, count = ks.asm(ASSEMBLY)

# 4. 输出结果
print(f"Assembly: {ASSEMBLY}")
print(f"Encoding: {encoding}")  # 原始列表
print(f"Count   : {count}")     # 指令数量

# 关键步骤：将 list[int] 转换为 bytes
# Unicorn 的 mem_write 需要 bytes 类型
    machine_code = bytes(encoding)
print("Machine Code: ",end="")
for i in range(len(machine_code)):
print(f"{machine_code[i]:02x}", end=" ")
print()

except KsError as e:
print(f"ERROR: {e}")
```

**运行结果：**

![image](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GU7Z2cSK0VVkqRmRTec3xATAI0ic2lq3HfVpCKlyp0wzljQBW2GRYcHUruffwZe37slKY24jdwqNA/640?wx_fmt=png&from=appmsg)![]()

### 核心 API 详解：`ks.asm()`

`ks.asm()` 方法的返回值是一个元组`(encoding, count)`：

1. **`encoding`**
   **(list[int])**：

* 这是一个**整数列表**，例如`[0x48, 0x31, 0xC0]`。
* **注意**

  ：它**不是**Python 的`bytes` 对象！如果直接把它传给`uc.mem_write`，Unicorn 会报错。
* **正确做法**：使用`bytes(encoding)`将其转换为二进制字节流。

2. **`count`**
   **(int)**：

* 表示成功编译的汇编语句数量（以`;`分隔）。
* 如果编译失败（如语法错误），Keystone 会抛出`KsError`异常，而不是返回错误码。

##

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GU7Z2cSK0VVkqRmRTec3xAR7DfnpK5gaxMUggxXTYbTkwiaJshu04Af0XNGud7vwiaf720szOCnLxg/640?wx_fmt=png&from=appmsg)

**四、核心实战：Unicorn + Keystone Patch**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GU7Z2cSK0VVkqRmRTec3xAR7DfnpK5gaxMUggxXTYbTkwiaJshu04Af0XNGud7vwiaf720szOCnLxg/640?wx_fmt=png&from=appmsg)

### 场景 1：NOP 填充

**需求**：
在逆向分析中，我们经常遇到反调试指令（如`RDTSC`、`CPUID`）或者不需要执行的垃圾代码。

假设在地址`0x400000` 处有一条复杂的指令（例如`XOR EAX, EAX`，长度 2 字节），我们希望将其“抹去”，替换为`NOP`（空指令），让 CPU 什么都不做直接滑过去。

**示例代码**：

```
from unicorn import *
from unicorn.x86_const import *
from keystone import *
from capstone import *

# 1. 初始化所有引擎
mu = Uc(UC_ARCH_X86, UC_MODE_64)
ks = Ks(KS_ARCH_X86, KS_MODE_64)
cs = Cs(CS_ARCH_X86, CS_MODE_64)

# 2. 准备内存环境
ADDRESS = 0x400000
MEM_SIZE = 2 * 1024 * 1024
mu.mem_map(ADDRESS, MEM_SIZE)

# 写入原始代码: xor eax, eax (2字节) + inc eax (2字节)
# 机器码: 31 c0 ff c0
ORIGINAL_CODE = b"\x31\xc0\xff\xc0"
mu.mem_write(ADDRESS, ORIGINAL_CODE)

print("--- [Before Patch] ---")
for insn in cs.disasm(mu.mem_read(ADDRESS, 4), ADDRESS):
print(f"0x{insn.address:x}:\t{insn.mnemonic}\t{insn.op_str}")

# ==========================================
# 3. 核心操作：NOP Patch
# ==========================================
TARGET_ADDR = 0x400000
PATCH_LEN = 2  # 需要覆盖的长度 (xor eax, eax 是 2 字节)

print(f"\n[*] Patching {TARGET_ADDR:x} with {PATCH_LEN} NOPs...")

# 生成 NOP 机器码 ("nop; nop")
# encoding -> [0x90, 0x90]
encoding, _ = ks.asm("nop; " * PATCH_LEN)

# 写入内存覆盖原指令
mu.mem_write(TARGET_ADDR, bytes(encoding))

# ==========================================
# 4. 验证结果
# ==========================================
print("\n--- [After Patch] ---")
# 读取内存查看变化
patched_code = mu.mem_read(ADDRESS, 4)
for insn in cs.disasm(patched_code, ADDRESS):
print(f"0x{insn.address:x}:\t{insn.mnemonic}\t{insn.op_str}")

# 模拟执行验证
print("\n[*] Executing...")
mu.reg_write(UC_X86_REG_RAX, 10) # 初始值 10
mu.emu_start(ADDRESS, ADDRESS + 4)
print(f"RAX = {mu.reg_read(UC_X86_REG_RAX)}")
# 结果应为 11 (因为 XOR 被 NOP 掉了，只有 INC 执行了)
```

**运行结果**：

![image](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GU7Z2cSK0VVkqRmRTec3xAU79WYyEarhTM57MlZ5eJz7GkwsChW6sFmjBWXvU0yZKhuwKU33aR0w/640?wx_fmt=png&from=appmsg)![]()

---

### 场景 2：逻辑篡改 (Hook & Modify)

**需求**：
在破解 CrackMe 或去除混淆时，我们经常遇到关键的分支跳转，例如`TEST EAX, EAX; JZ 0xTarget`。如果验证失败，程序会跳转到错误处理分支。
我们的目标是：强制将`JZ`（条件跳转）修改为`JMP`（无条件跳转），确保程序始终走向我们预期的路径，从而绕过校验。

**核心挑战 (JIT 陷阱)**：
Unicorn 使用 JIT（即时编译）技术。如果在`UC_HOOK_CODE` 回调中动态修改当前指令的内存，CPU 实际上已经完成了该指令的取指和解码，Patch 仅对**下一次**执行有效。

因此，对于确定的逻辑修改，最佳实践是在**模拟启动前 (Pre-Patch)**就完成内存修改。

**示例代码：**

```
from unicorn import *
from unicorn.x86_const import *
from keystone import *
from capstone import *

# 1. 初始化引擎
mu = Uc(UC_ARCH_X86, UC_MODE_64)
ks = Ks(KS_ARCH_X86, KS_MODE_64)
cs = Cs(CS_ARCH_X86, CS_MODE_64)

# 2. 准备内存与代码
ADDRESS = 0x400000
MEM_SIZE = 2 * 1024 * 1024
mu.mem_map(ADDRESS, MEM_SIZE)

# --- 构造模拟场景 ---
# 汇编逻辑：
# 0x400000: XOR EAX, EAX  (EAX = 0)
# 0x400002: INC EAX       (EAX = 1, ZF = 0)
# 0x400004: JZ  0x40000A  (关键跳转：此时不应跳转)
# 0x400006: INC EAX       (EAX = 2, 正常路径)
# 0x40000A: DEC EAX       (EAX = 0, 跳转目标)

CODE_ASM = """
    xor eax, eax;
    inc eax;
    jz 0x40000a;
    inc eax;
    nop; nop;
    dec eax;
"""

# 编译并...
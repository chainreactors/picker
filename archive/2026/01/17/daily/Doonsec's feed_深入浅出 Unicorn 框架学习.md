---
title: 深入浅出 Unicorn 框架学习
url: https://mp.weixin.qq.com/s/0bIGf2Gqr8x_DJLRO4c1eA
source: Doonsec's feed
date: 2026-01-17
fetch_date: 2026-01-18T03:35:09.128208
---

# 深入浅出 Unicorn 框架学习

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FD1pneCxSgArF1z67m1qz4SlG8ialrIkk9xqAWc3maxzqBbEy7UxPMeCy4x6GJF0CAd5VHwSN06Uw/0?wx_fmt=jpeg)

# 深入浅出 Unicorn 框架学习

xiusi
xiusi

看雪学苑

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8FD1pneCxSgArF1z67m1qz4VP1p4bZXpZ8UE3489DXShooGyUeXiayNxgc6ZibEicaQphIRZN1a3fdBA/640?wx_fmt=gif&from=appmsg)

**0****1**

**简介**

# Unicorn是一个基于 QEMU 的轻量级、多平台、多架构 CPU 模拟器框架。相比于重量级的符号执行框架（如 Angr），Unicorn 虽然没有内置 Z3 约束求解器，但凭借其极致的性能、友好的 API 设计以及强大的 Hook 机制（指令级回调），成为了二进制分析、反混淆和 CTF 竞赛中的利器。

### 1. 核心特性

* **多架构支持**：全面覆盖 ARM, ARM64 (ARMv8), MIPS, x86 (含 x64), PowerPC, RISC-V, SPARC 等主流架构。
* **极致轻量**：基于纯 C 语言实现，无复杂的依赖链，API 设计直观且架构中立。
* **高性能**：利用 JIT（Just-In-Time）编译技术，模拟执行速度极快。
* **多语言绑定**：除了 C 语言原生接口，官方还提供了 Python, Java, Go, Rust, .NET 等几乎所有主流语言的绑定。
* **跨平台**：完美运行于 Windows, Linux, macOS, BSD 等操作系统。

### 2. Unicorn 到底是什么？

简单来说，Unicorn 是一款 **CPU 模拟器**。
但与 VMWare 或 Android 模拟器不同，Unicorn 不负责模拟整个操作系统或完整的硬件环境，它**不支持系统调用 (Syscall)**。

你需要像操作“裸机”一样：

1. 手动申请并映射内存 (Map Memory)。
2. 手动写入二进制代码和数据 (Write Data)。
3. 设置 CPU 寄存器状态 (Set Registers)。
4. 指定起始地址，开始模拟执行 (Emulate)。

### 3. 应用场景

* **恶意代码分析**：截取并模拟执行恶意软件中的解密函数，无需运行整个病毒样本。
* **CTF 竞赛**：解决复杂的逆向题目，特别是涉及自定义算法或混淆的代码。
* **代码反混淆**：模拟执行混淆代码（如 OLLVM），跟踪寄存器变化以还原真实逻辑。
* **Shellcode 测试**：在安全的环境中快速验证 Shellcode 的功能。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8FD1pneCxSgArF1z67m1qz4VP1p4bZXpZ8UE3489DXShooGyUeXiayNxgc6ZibEicaQphIRZN1a3fdBA/640?wx_fmt=gif&from=appmsg)

**02**

**环境准备**

为了避免污染系统的 Python 环境，推荐使用**Conda**进行环境隔离。

### 1. 创建虚拟环境

```
# 创建名为 "Unicorn" 的环境，指定 python 版本为 3.9
conda create -n Unicorn python=3.9
```

### 2. 激活环境

```
# 进入虚拟环境
conda activate Unicorn
```

### 3. 安装 Unicorn 模块

使用 pip 安装官方的 Python 绑定：

```
# 安装 unicorn 核心库
pip install unicorn
```

> \*\* 验证安装\*\*
> 在终端输入`python`进入交互模式，尝试导入：
>
> ```
> import unicorn
> print(unicorn.__version__)
> ```
>
> ![图片描述](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FD1pneCxSgArF1z67m1qz4OCJPr1PN9ZrNv8iay5kq9pSYYlgonib6ACt3RGYwZOhoMK3uoOAfsLXg/640?wx_fmt=other&from=appmsg)
>
> 如果无报错且输出了版本号，说明环境搭建成功。

### 4. 项目配置

打开你的 IDE（如 PyCharm 或 VSCode），创建一个新的 Python 项目。在解释器设置（Interpreter Settings）中，选择**Existing Environment**（现有环境），并指向刚刚创建的 Conda 环境路径。

![图片描述](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FD1pneCxSgArF1z67m1qz4kOKFphAibJIaDdfeUoYRnj3ozvW420xdSAhdibDzu6AyB4CfIhtH4NnA/640?wx_fmt=other&from=appmsg)![]()

---

##

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8FD1pneCxSgArF1z67m1qz4VP1p4bZXpZ8UE3489DXShooGyUeXiayNxgc6ZibEicaQphIRZN1a3fdBA/640?wx_fmt=gif&from=appmsg)

**03**

**基础内容**

学习 Unicorn 的过程，其实就是学习如何**手动扮演操作系统的角色**，为 CPU 准备好它运行所需的一切资源。

我们将按照以下顺序攻克 Unicorn 的核心要素：

### 3.1 核心思维模型：模拟执行五步曲

在开始编写 Unicorn 代码之前，我们必须建立一个清晰的思维模型。使用 Unicorn 就像是在扮演一个“手动挡”的操作系统，你必须亲手为 CPU 准备好它运行所需的一切资源。所有的 Unicorn 脚本（无论多么复杂）都逃不出以下 5 个标准步骤：

#### 第一步：初始化 (Initialize)

首先，我们需要引入 Unicorn 库，并实例化一个`Uc`对象。这一步决定了我们要模拟的硬件环境。

* **选择架构**：如`UC_ARCH_X86`,`UC_ARCH_ARM`
* **选择模式**：如`UC_MODE_32`,`UC_MODE_64`

```
from unicorn import *
# 加载 x86 和 x86-64 两种架构的常量
from unicorn.x86_const import *

# 初始化一个 X86-64 架构的模拟器实例
# UC_ARCH_X86: 架构
# UC_MODE_64:  64位模式
mu = Uc(UC_ARCH_X86, UC_MODE_64)
```

#### 第二步：映射内存 (Map Memory)

Unicorn 中的 CPU 只能访问已被映射的内存区域。我们需要像操作系统一样，规划并申请虚拟内存空间。

* **API**：`mu.mem_map(address, size)`
* **注意**：`address`（基址）和`size`（大小）必须是内存页大小（通常为 **4KB/0x1000**）的整数倍。

```
# 定义内存布局常量
ADDRESS = 0x400000          # 代码段基址
MEM_SIZE = 2 * 1024 * 1024  # 申请 2MB 内存

STACK_ADDR = 0x0            # 栈内存基址（示例）
STACK_SIZE = 1024 * 1024    # 1MB 栈空间

# 1. 映射代码段内存
mu.mem_map(ADDRESS, MEM_SIZE)

# 2. 映射栈内存
mu.mem_map(STACK_ADDR, STACK_SIZE)
```

#### 第三步：写入数据 (Write Data)

有了内存空间后，我们需要将机器码（Shellcode）或二进制文件内容写入其中。这相当于加载器（Loader）将程序加载到内存的过程。

* **API**：`mu.mem_write(address, data)`

```
# 读取本地二进制文件（Shellcode）
with open("./test", "rb") as f:
    CODE = f.read()

# 将代码写入到基址 0x400000 处
mu.mem_write(ADDRESS, CODE)
```

#### 第四步：设置环境 (Setup Context)

在运行前，必须初始化 CPU 的关键寄存器。最重要的是设置**指令指针 (RIP/EIP)**和 **栈指针 (RSP/ESP)**。

* **API**：`mu.reg_write(reg_id, value)`
* **宏定义**：Unicorn 提供了预定义的常量（如`UC_X86_REG_RSP`）来标识寄存器。

```
# 初始化栈指针 (RSP)
# 注意：栈通常是向下增长的，所以指针应指向栈内存的高地址末端
# 并且通常需要保持对齐（如 8字节或16字节对齐）
mu.reg_write(UC_X86_REG_RSP, STACK_ADDR + STACK_SIZE - 8)

# (可选) 初始化其他通用寄存器，作为函数参数
# mu.reg_write(UC_X86_REG_RAX, 0x1)
```

#### 第五步：开始执行 (Start Emulation)

一切准备就绪，指定入口点和结束点，按下“启动键”。

* **API**：`mu.emu_start(begin, end)`

+ `begin`：模拟执行的起始地址。
+ `end`：模拟执行的结束地址（运行到此地址**前**停止）。

```
# 开始模拟执行
# 从代码基址开始，执行到代码末尾
try:
print(">>> Start emulation...")
    mu.emu_start(ADDRESS, ADDRESS + len(CODE))
print(">>> Emulation done.")
except UcError as e:
print(f"ERROR: {e}")

# 执行结束后，可以读取寄存器查看结果
r_rax = mu.reg_read(UC_X86_REG_RAX)
print(f">>> RAX = 0x{r_rax:x}")
```

---

### 3.2 初始化与常量体系

在 Unicorn 中，一切的起点都是`Uc`类的实例化。这个步骤决定了你要模拟的“硬件规格”——即 CPU 的架构（Architecture）和运行模式（Mode）。

#### 1. 实例化引擎

要创建一个模拟器实例，我们需要传入两个核心参数：

```
# 原型：Uc(arch, mode)
mu = Uc(UC_ARCH_X86, UC_MODE_32)
```

* **`arch`**
  **(架构)**：指定 CPU 的指令集架构（如 x86, ARM）。
* **`mode`**
  **(模式)**：指定 CPU 的运行位数（32/64位）或字节序（大/小端）。

#### 2. 常用架构常量 (Architecture)

Unicorn 支持多种主流架构，以下是逆向分析中最常用的几种：

| 常量名 | 对应架构 | 说明 |
| --- | --- | --- |
| **`UC_ARCH_X86`** | x86 / x64 | 包含 Intel/AMD 的 16位、32位和 64位架构。 |
| **`UC_ARCH_ARM`** | ARM | 经典的 32位 ARM 架构（常见于旧版 Android）。 |
| **`UC_ARCH_ARM64`** | AArch64 | 现代移动设备（Android/iOS）的主流 64位架构。 |
| **`UC_ARCH_MIPS`** | MIPS | 常见于路由器、IoT 设备。 |

#### 3. 常用模式常量 (Mode)

模式常量用于进一步细分 CPU 的工作状态。需要注意的是，**不同的架构支持的模式不同**，且模式可以通过`+`号进行组合。

| 常量名 | 说明 | 适用架构 |
| --- | --- | --- |
| **`UC_MODE_32`** | 32位模式 | x86, ARM, MIPS 等 |
| **`UC_MODE_64`** | 64位模式 | x86, ARM64, MIPS64 等 |
| **`UC_MODE_THUMB`** | Thumb 模式 | **仅限 ARM**。用于模拟 16位 Thumb 指令集。 |
| **`UC_MODE_LITTLE_ENDIAN`** | 小端序 (默认) | 所有架构。数据低位存储在低地址。 |
| **`UC_MODE_BIG_ENDIAN`** | 大端序 | MIPS, PowerPC 等。数据高位存储在低地址。 |

#### 4. 实战组合示例

在实际使用中，我们经常需要组合使用这些常量。

**场景 A：模拟 PC 上的 32位 Windows 程序**

```
# 标准的 x86 32位环境
mu = Uc(UC_ARCH_X86, UC_MODE_32)
```

**场景 B：模拟 Android 上的 ARM64 代码**

```
# 标准的 ARM64 小端序环境
mu = Uc(UC_ARCH_ARM64, UC_MODE_64)
```

**场景 C：模拟 ARM Thumb 指令**
ARM 处理器可以在 ARM 状态（4字节指令）和 Thumb 状态（2字节指令）之间切换。

```
# 开启 ARM 的 Thumb 模式
mu = Uc(UC_ARCH_ARM, UC_MODE_THUMB)
```

**场景 D：模拟 IoT 设备的 MIPS 大端序程序**
某些路由器固件使用大端序 MIPS。

```
# 组合模式：32位 + 大端序
mu = Uc(UC_ARCH_MIPS, UC_MODE_32 + UC_MODE_BIG_ENDIAN)
```

---

### 3.3 内存操作 (Memory API)

Unicorn 模拟器内部没有操作系统的`malloc` 或`Heap`管理器。作为“上帝视角”的控制者，你必须手动管理每一页内存的分配、读写和释放。

Unicorn 的内存操作 API 非常精简，核心只有三个：**映射（申请）**、**写入**和 **读取**。

#### 1. 内存映射 (申请内存)

在 CPU 访问任何内存地址之前，该地址必须先被“映射”。访问未映射的内存会导致`UC_ERR_READ_UNMAPPED` 或`UC_ERR_WRITE_UNMAPPED`异常。

* **API**:`uc.mem_map(address, size, perms=UC_PROT_ALL)`

+ `address`: 起始基址。
+ `size`: 内存大小。**必须是 4KB (0x1000) 的整数倍**。
+ `perms`: (可选) 内存权限，默认可读写执行。

> **4KB 对齐：**
> 现代操作系统和 CPU 通常以“页（Page）”为单位管理内存，一页通常是 4096 字节 (0x1000)。
> 如果你尝试申请`0x100` 字节，Unicorn 会直接报错。必须向上取整到`0x1000`。

```
# 定义基址和大小
ADDRESS = 0x400000
# 错误写法：SIZE = 1024 (不是 4KB 倍数，会报错)
SIZE = 2 * 1024 * 1024  # 正确：2MB

# 申请 2MB 内存，默认权限 rwx (可读可写可执行)
mu.mem_map(ADDRESS, SIZE)

# 进阶：申请一块“只读”数据区 (UC_PROT_READ)
# 常用于模拟 .rodata 段
DATA_ADDR = 0x800000
mu.mem_map(DATA_ADDR, 0x1000, UC_PROT_READ)
```

#### 2. 内存写入 (写入数据)

有了内存空间后，我们需要将机器码（Shellcode）或数据填充进去。

* **API**:`uc.mem_write(address, data)`

+ `address`: 写入的起始地址。
+ `data`: 要写入的字节串 (`bytes`)。

```
# 机器码：INC EAX (0x40)
machine_code = b"\x40"

# 将机器码写入到刚才申请的代码段基址
mu.mem_write(ADDRESS, machine_code)

# 写入一个字符串到数据段
mu.mem_write(DATA_ADDR, b"Hello Unicorn")
```

#### 3. 内存读取 (获取结果)

在模拟执行结束后，或者在 Hook 回调中，我们通常需要读取内存中的数据来验证计算结果。

* **API**:`uc.mem_read(address, size)`

+ **返回**:`bytearray` 对象 (可转换为`bytes` 或`str`)。

```
# 读取刚才写入的字符串
# 读取 5 个字节 -> b'Hello'
data = mu.mem_read(DATA_ADDR, 5)
print(f"Read from memory: {bytes(data)}")
```

#### 4. 内存权限常量 (Permissions)

在`mem_map` 或`mem_protect` 中使用，用于控制内存页的读写执行权限（类似于 Linux 的`mprotect`）。

| 常量名 | 权限 | 说明 |
| --- | --- | --- |
| **`UC_PROT_READ`** | 可读 (r) | 允许读取数据。 |
| **`UC_PROT_WRITE`** | 可写 (w) | 允许写入数据。 |
| **`UC_PROT_EXEC`** | 可执行 (x) | 允许 CPU 在...
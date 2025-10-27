---
title: C语言性能优化指南
url: https://hurricane618.me/2024/12/31/C-language-performance-optimization-guide/
source: 风之栖息地
date: 2025-01-01
fetch_date: 2025-10-06T20:07:13.340963
---

# C语言性能优化指南



[风之栖息地](/)

C语言性能优化指南

[风之栖息地](/)

# C语言性能优化指南

总结
性能

字数统计: 10.5k阅读时长: 40 min


2024/12/31




Share

* 
* 
* 
* 
* 

![](/assets/loading.svg)

## 前言

在甲方待了一段时间发现，在企业中想要提升安全性或者落地某个新的安全能力，总是需要和业务性能进行对比。如果某个安全特性的性能开销过大，那么对于业务来讲是一种不可接受的代价。因此，安全从业者学习一点性能优化的手段也是非常重要的。这里博主主要在操作系统领域，相关的代码主要以C为主，所以性能优化也是围绕着语言相关特点。

C语言从代码到可执行文件，再到最终的运行阶段，主要是两个部分组成——编译阶段和执行阶段。针对编译阶段，我们能做的就是尽可能的利用编译器特性和特殊编码技法来优化；执行阶段涉及到指令的热点运行，由于程序执行的局部性原理，我们的大量代码在执行时往往会重复一小段逻辑。因此，性能优化的重点就是在于这些热点函数之中。对于非热点函数，我们则更加关注体积，怎么写能够使得代码编译出来的指令数最少，减少对空间的占用。

以下则从六种不同的角度，针对C语言程序做优化。

## 编译选项

对于非编译器开发的程序员来说，新增一个编译选项就能搞定的事情，肯定是非常之轻松的活。

### 通用编译优化 -O

编译器一般会默认一个优化等级，但当我们想要朝着更优的方向前行时，就需要将优化等级调高。这里在编译Linux内核时，默认是-O2，其他平台类二进制需要关注项目本身的设置。如果觉得-O2的效果一般，可以尝试-O3。

### 指令架构优化 -march

编译器针对不同的指令集以及cpu架构都有着极强的针对性优化（搞编译优化的人是真的顶），比如这里的`-march=x86-64-v3` 就是针对v3版本的x86-64指令集做专属优化。除了指令集还有cpu架构，比如经典的奔腾，haswell，还有i7等等。同理在ARM架构上也有类似的参数可控选择，根据不同的ARM指令集版本也有不同的参数。

更多细节可参考：

x86 <https://gcc.gnu.org/onlinedocs/gcc/x86-Options.html>

arm <https://gcc.gnu.org/onlinedocs/gcc/ARM-Options.html>

### 链接优化 -flto

通过把很多编译优化放在链接阶段执行，实现范围更广的优化面。

`-flto` 可以在编译时进行全局优化，但整体的时间开销和编译资源开销将大大增加，而 `-flto=thin` 是一种折衷方案，它在链接阶段进行优化，同时减少了编译时间和资源消耗。

链接优化的目标：

* 内联函数：优化开启之前只能针对单一C源代码优化，开启后能针对全局整体做内联优化
* 函数重定位：能通过静态分析调整函数代码位置，减少函数调用链长度
* 代码融合：多个代码块合并，减少代码的执行次数
* 数据流分析，移除不必要的死代码

总的来说，链接优化能在全局层面做到更好的优化方案，减少代码体积和增强程序性能。

### 关闭安全选项（不推荐）

作为一个安全从业者，非常的不推荐关闭这些安全选项，反而推荐去开启一些额外的安全编译选项来增强安全能力。但是，在某些性能要求的特殊场景下，确实会关闭某些安全能力来提升性能。

以下列举一些关闭的方式，但还是要说，这是饮鸩止渴。

* `-fno-sanitize=all` 关闭所有的消毒器
* `-fcf-protection=none` 关闭编译器自带的控制流保护
* `-fno-harden-compares` 关闭针对比较操作的防溢出处理
* `-fno-harden-conditional-branches` 关闭针对条件分支的安全增强
* `-fno-harden-control-flow-redundancy` 关闭控制流冗余检测的安全增强
* `-fno-hardened` 关闭一系列的安全增强选项
* `-fno-stack-protector` 关闭栈溢出保护机制
* `-fno-stack-check` 关闭栈的边界检查功能
* `-fno-stack-clash-protection` 关闭栈冲突保护
* `-fno-stack-limit` 关闭栈大小限制约束
* `-fno-split-stack` 关闭栈切割的安全增强
* `-fstrub=disable` 关闭编译器中的结构化控制流保护

## 编码优化

以下给出的代码示例，均通过在线的编译器网站进行编译反汇编转换。

网址：<https://godbolt.org/>

编译器：ARM64 gcc 7.3

### 局部变量缓存

**缓存多次访问的全局变量**

当我们有多次访问全局变量的需求时，不要多次使用全局变量，而是把全局变量读出后放入局部变量中，之后的读写都对该局部变量进行，最后的结果数值写回全局变量中，这样能避免频繁的内存空间访问，直接使用栈上的寄存器值。

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 ``` | ``` int sum = 0x1234; void func(void) {     int max_loop = get_loop_size();     for (int i = 0; i < max_loop; i++) {         sum += 1;     } } ``` |

这里如果有反汇编，就能看到每次读`sum`时都需要访问一次程序中的全局数据段。

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 ``` | ``` sum:         .word   4660 func():         stp     x29, x30, [sp, -32]!         add     x29, sp, 0         bl      get_loop_size()         str     w0, [x29, 24]         str     wzr, [x29, 28] .L3:         ldr     w1, [x29, 28]         ldr     w0, [x29, 24]         cmp     w1, w0         bge     .L4         adrp    x0, sum         add     x0, x0, :lo12:sum         ldr     w0, [x0]         add     w1, w0, 1         adrp    x0, sum         add     x0, x0, :lo12:sum         str     w1, [x0]         ldr     w0, [x29, 28]         add     w0, w0, 1         str     w0, [x29, 28]         b       .L3 .L4:         nop         ldp     x29, x30, [sp], 32         ret ``` |

如果将其存放进局部变量中，那么我们的值将会通过栈上的数据存储，在完成数据修改后再写回全局变量，这样能减少无效的内存访问，优化程序整体的速度。

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 ``` | ``` int sum = 0x1234; void func(void) {     int max_loop = get_loop_size();     int tmp_sum = sum; // 新的局部变量     for (int i = 0; i < max_loop; i++) {         tmp_sum += 1;     }     sum = tmp_sum; } ``` |

优化之后的反汇编结果：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 ``` | ``` sum:         .word   4660 func():         stp     x29, x30, [sp, -32]!         add     x29, sp, 0         bl      get_loop_size()         str     w0, [x29, 20]         adrp    x0, sum         add     x0, x0, :lo12:sum         ldr     w0, [x0]         str     w0, [x29, 28]         str     wzr, [x29, 24] .L3:         ldr     w1, [x29, 24]         ldr     w0, [x29, 20]         cmp     w1, w0         bge     .L2         ldr     w0, [x29, 28]         add     w0, w0, 1         str     w0, [x29, 28]         ldr     w0, [x29, 24]         add     w0, w0, 1         str     w0, [x29, 24]         b       .L3 .L2:         adrp    x0, sum         add     x0, x0, :lo12:sum         ldr     w1, [x29, 28]         str     w1, [x0]         nop         ldp     x29, x30, [sp], 32         ret ``` |

**缓存多次使用的表达式**

非常显而易见的事情，如果在编码中出现了多次的表达式，就应该用局部变量缓存一下，而不是用相同的语句再计算一遍。下面给了一个例子，我们在做计算的过程中，类似于`value_1` 和 `value_2`这样的表达式结果，如果后续还有使用的场景，在不影响最终结果的情况下就应该直接复用。

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 ``` | ``` int func(int a, int b) {     int value_1 = a + get_some_value();     int value_2 = b + get_other_value();     do_something(value_1, value_2);     int value_3 = a + b + get_some_value() + get_other_value();     return value_3; } ``` |

以上代码可以优化为下面的样子，当然这个地方编译器估计也能有点优化，但能优化到什么程度全看用的什么编译器，以及编译器的版本和编译选项。所以，这种能依靠编码优化的情况，尽量在代码实现时就完成最优处理。

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 ``` | ``` int func(int a, int b) {     int value_1 = a + get_some_value();     int value_2 = b + get_other_value();     do_something(value_1, value_2);     int value_3 = value_1 + value_2;     return value_3; } ``` |

### 标记条件分支

**\_\_builtin\_expect**

这个编译器内置的函数，能够标记最有可能进入的条件分支，而这个最常进入的条件分支的语句指令会被放在前面，不常进入的语句指令将会被放在后面，如此一来，可以最大化的发挥CPU的指令预取能力。`__builtin_expect`在很多时候也会被封装成`LIKELY`和`UNLIKELY`的宏，需要根据你所在的编码环境具体选择。（**需要添加-O2的编译选项才能触发标记条件分支的优化**）

具体用法如下：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 ``` | ``` #define LIKELY(x) __builtin_expect(!!(x), 1) #define UNLIKELY(x) __builtin_expect(!!(x), 0)  if (LIKELY(a > 5)) {     a -= 5;     b++; } else {     a += 5;     b--; }  if (UNLIKELY(a > 5)) {     a -= 5;     b++; } else {     a += 5;     b--; } ``` |

分别编译以上两段不同的程序，我们通过反汇编就可以查看到，当条件语句为`LIKELY(a > 5)`时，上面的`a -= 5;b++;`是在比较指令cmp的后面；

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 ``` | ```         cmp     w0, 5         ble     .L2         add     w1, w1, 1         sub     w0, w0, #5         add     w0, w0, w1         ret .L2:         sub     w1, w1, #1         add     w0, w0, 5         add     w0, w0, w1         ret ``` |

当条件语句为`UNLIKELY(a > 5)`时，下面的`a += 5;b--;`就会被放在指令cmp的后面。这样的结果，也对应了代码局部性原理，让更可能执行的指令放在一起。

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 ``` | ```         cmp     w0, 5         bgt     .L5         sub     w1, w1, #1         add     w0, w0, 5         add     w0, w0, w1         ret .L5:         add     w1, w1, 1         sub     w0, w0, #5         add     w0, w0, w1         ret ``` |

**\_\_builtin\_unreachable**

同样为编译器内置的函数，能够标记分支中明确不可达的部分，这样能让编译器感知到该分支永远不可达。（那么永远不可达的代码为啥还要写呢？这又是另外一个问题了，某些场景是为了程序员方便理解，某些场景是为了清除编译告警等问题）针对这类标记，编译器在感知到不可达信息之后，能够使用更加激进的优化方案处理这段代码的指令翻译。

具体用法如下：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` void __noreturn arm64_serror_panic(struct pt_regs *regs, unsigned long esr) {     ......     cpu_loop(); // 永远不会退出的循环     unreachable(); } ``` |

我这里直接拿了一段Linux内核的代码来举例子，这里有个场景是陷入循环中，永远不会退出。在这种场景下，末尾跟随一个`unreachable`表达后面永远不会到达。这样编译器，就能针对这个点单独做出优化，比如这样就不需要在函数末尾出栈和返回，以及针对性的做出指令地址布局的优化。

**static\_branch\_likely** 和 **static\_branch\_unlikely**

在内核中有着两个神奇的宏定义在`include/linux/jump_label.h`中，这就是`static_branch_likely`和`static_branch_unlikely`。这两个宏定义配合Linux内核的跳转表能玩出特别花的动态分支调整，这里的两个宏实际的用法，和上面的`LIKELY`和`UNLIKELY`是一样的，在条件判断中添加后用于优化编译后的指令布局。但它强大的地方在于，还提供了另外的接口`static_branch_enable`和`static_branch_disable`控制这种优化（还有`static_branch_inc`和`static_branch_dec`），在满足特定场景和条件的情况下，开启/关闭分支优化。

下面来看示例代码（从Linux内核摘抄，kvm模块的代码）：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 ``` | ``` static DEFINE_STATIC_KEY_FALSE(has_gic_active_state);  int kvm_timer_hyp_init(bool has_gic) {     ......     if (has_gic) {         ...         static_branch_enable(&has_gic_active_state);     } }  void kvm_timer_vcpu_load(struct kvm_vcpu *vcpu) {     ...     if (static_branch_likely(&has_gic_active_state)) {         ...     } } ``` |

在文件的最开头定义这个动态条件变量默认为`false`，在初始...
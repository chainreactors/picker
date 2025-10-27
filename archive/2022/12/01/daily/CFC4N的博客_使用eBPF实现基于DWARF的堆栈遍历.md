---
title: 使用eBPF实现基于DWARF的堆栈遍历
url: https://www.cnxct.com/profiling-without-frame-pointers-using-ebpf/
source: CFC4N的博客
date: 2022-12-01
fetch_date: 2025-10-04T00:11:48.797472
---

# 使用eBPF实现基于DWARF的堆栈遍历

Toggle navigation

[CFC4N的博客](https://www.cnxct.com/ "CFC4N的博客")
人不能过得太舒服，太舒服就会出问题。

* 作品
  + [eCapture旁观者–HTTPS/TLS抓包](https://ecapture.cc "eCapture旁观者--HTTPS/TLS抓包")
  + [Golang eBPF Manager](https://github.com/gojue/ebpfmanager "Golang eBPF Manager")
  + [eBPF技术精选资料](https://github.com/gojue/ehids-slide "eBPF技术精选资料")
  + [League Of legends启动器](https://github.com/cfc4n/lol_launcher "League Of legends启动器")
  + [eBPF HIDS主机入侵检测](https://github.com/gojue/ehids-agent "eBPF HIDS主机入侵检测")
* [归档](https://www.cnxct.com/archives/ "归档")
* [关于我](https://www.cnxct.com/about/ "关于我")
* [工作机会](https://www.cnxct.com/jobs/ "工作机会")

# 使用eBPF实现基于DWARF的堆栈遍历

[2022/12/012022/12/01](https://www.cnxct.com/profiling-without-frame-pointers-using-ebpf/)  [CFC4N](https://www.cnxct.com/author/admin/)

### 文章目录

1. [译者注：](#ftoc-heading-1)
2. [原文：](#ftoc-heading-2)
3. [x86\_64中的堆栈](#ftoc-heading-3)
4. [Can I have a (frame) pointer?](#ftoc-heading-4)
5. [硬件方法](#ftoc-heading-5)
6. [一场特殊的邂逅](#ftoc-heading-6)
   1. [DWARF’s Call Frame Information (CFI)](#ftoc-heading-7)
   2. [使用DWARF CFI遍历堆栈](#ftoc-heading-8)
7. [可能的实现](#ftoc-heading-9)
   1. [Why BPF?](#ftoc-heading-10)
   2. [展开表的BPF友好表示形式](#ftoc-heading-11)
8. [开发](#ftoc-heading-12)
   1. [Testing测试](#ftoc-heading-13)
9. [未来工作](#ftoc-heading-14)
10. [试用](#ftoc-heading-15)
11. [与社区合作](#ftoc-heading-16)
12. [致谢](#ftoc-heading-17)
13. [杂谈](#ftoc-heading-18)

## 译者注：

原文为<https://www.parca.dev/>的[Javier Honduvilla Coto](https://hondu.co/)，文章地址[DWARF-based Stack Walking Using eBPF](https://www.polarsignals.com/blog/posts/2022/11/29/profiling-without-frame-pointers/)，副标题`Deep dive into the new DWARF-based stack unwinder using eBPF`，即`深度解析使用eBPF基于DWARF的栈展开`。 文章为机翻，以及人工矫正。译者水平有限，有疑问请看原文。

**parca项目介绍**

> parca是一款基于eBPF技术实现的CPU、内存观测产品。可以持续分析 CPU 和内存使用情况产品，细化到行号和整个时间。 节省基础架构成本、提高性能并提高可靠性。 GitHub地址：<https://github.com/parca-dev/parca>

## 原文：

采样CPU分析器周期性地获取目标进程的堆栈，比如用C、C++、Rust等语言编写的进程，可能比大家想象的要复杂一些。最普遍的问题是因为缺少`frame pointer帧指针`。

我们已经开发了一个改进的堆栈遍历器 ：[Parca](https://www.parca.dev/) continuous profiling [Agent](https://github.com/parca-dev/parca-agent/)，即使在省略了`帧指针`的情况下也能工作。

## x86\_64中的堆栈

`x86_64`架构除了描述它的指令集和其他一些重要特征外，还定义了数据在其应用二进制接口或简称[ABI](https://en.wikipedia.org/wiki/Application_binary_interface)中应如何布局的规则。该规范显示了该架构下的堆栈应该如何设置。

当这段代码被执行时，不同的`call`指令将把返回地址压入堆栈中。一旦函数返回，CPU将读取返回地址并跳转到该地址，继续执行该函数的调用点。

由于没有额外的信息，不可能可靠地生成堆栈跟踪。可能有其他的值，比如函数的本地数据，被存储在堆栈中，可能看起来像函数地址。这就是帧指针要解决的问题。

## Can I have a (frame) pointer?

如下伪代码为例，假设没有编译器优化

```
int top(void) {
    for(;;) { }
}

int c1(void) {
    top();
}

int b1(void) {
    c1();
}

int a1(void) {
    b1();
}

int main(void) {
  a1();
}
```

使用这方法来遍历堆栈，我们需要保留指向上一帧的指针。 在x86体系结构中，这通常在帧指针`$rbp`中。 由于函数可能调用其他函数，因此必须在函数进入时存储该寄存器，并在函数退出时恢复该寄存器。

这是通过所谓的`function prologue`[函数序言](https://www.intel.com/content/www/us/en/docs/programmable/683836/current/function-prologues.html)来实现的，在函数入口处，它可能看起来像这样

```
push $rbp # saves the stack frame pointer
mov $rbp, $rsp # sets the current stack pointer to the frame pointer
```

`function epilogue`函数序言在函数返回处

```
pop $rbp # restores the function's frame pointer
ret # pops the saved return address and jumps to it
```

如果我们用帧指针编译并运行上面的C代码，堆栈将具有遍历堆栈所需的所有信息。 有效地调用不同的函数会创建一个需要遍历的链表。

**反汇编使用帧指针编译的代码**

```
# compiled with `gcc sample.c -o sample_with_frame_pointers -fno-omit-frame-pointer`
$ objdump -d ./sample_with_frame_pointers
0000000000401106 <top>:
  401106:       55                      push   %rbp
  401107:       48 89 e5                mov    %rsp,%rbp
  40110a:       eb fe                   jmp    40110a <top+0x4>

000000000040110c <c1>:
  40110c:       55                      push   %rbp
  40110d:       48 89 e5                mov    %rsp,%rbp
  401110:       e8 f1 ff ff ff          call   401106 <top>
  401115:       90                      nop
  401116:       5d                      pop    %rbp
  401117:       c3                      ret

0000000000401118 <b1>:
  401118:       55                      push   %rbp
  401119:       48 89 e5                mov    %rsp,%rbp
  40111c:       e8 eb ff ff ff          call   40110c <c1>
  401121:       90                      nop
  401122:       5d                      pop    %rbp
  401123:       c3                      ret

0000000000401124 <a1>:
  401124:       55                      push   %rbp
  401125:       48 89 e5                mov    %rsp,%rbp
  401128:       e8 eb ff ff ff          call   401118 <b1>
  40112d:       90                      nop
  40112e:       5d                      pop    %rbp
  40112f:       c3                      ret

0000000000401130 <main>:
  401130:       55                      push   %rbp
  401131:       48 89 e5                mov    %rsp,%rbp
  401134:       e8 eb ff ff ff          call   401124 <a1>
  401139:       b8 00 00 00 00          mov    $0x0,%eax
  40113e:       5d                      pop    %rbp
  40113f:       c3                      ret
```

![The contents of the native stack in the example code above when the top function is running. Shows the different return addresses, interleaved with the saved frame pointers. There's no local variables that have been pushed into the stack.](https://image.cnxct.com/2022/11/stack_with_fp.png)*上面的例子代码中的native stack的内容是在顶部函数运行时用帧指针编译的*

要遍历堆栈，我们必须遵循上面生成的链表，读取每个保存的`$rbp`之前压入的值，这将使我们的堆栈帧，直到`$rbp`为零，意味着已经到达了堆栈的末尾。

这很好，因为它允许我们以很低的成本计算出堆栈跟踪。 对于编译器实现者来说，添加它也相对容易，而且一般来说，只需要相当少量的周边基础设施就可以使它工作。

尽管有这些优点，但我们所依赖的许多代码并不是用帧指针编译的。 我们中的许多人依赖于我们的Linux发行版应用程序和库，其中绝大多数选择省略帧指针。 即使你使用框架指标编译程序，动态或静态链接你的发行版本所提供的任何库，也可能会让你无法仅使用帧指针来正确展开堆栈。

我们不会深入探讨在某些环境中禁用帧指针的原因以及与之相关的细微差别，但我们认为必须逐个应用地对它们的开销进行基准测试。 禁用帧指针带来的成本也应该考虑在内。

**反汇编不使用帧指针编译的代码**

```
# compiled with `gcc sample.c -o sample_without_frame_pointers -fomit-frame-pointer`
$ objdump -d ./sample_without_frame_pointers
[...]
0000000000401106 <top>:
  401106:       eb fe                   jmp    401106 <top>

0000000000401108 <c1>:
  401108:       e8 f9 ff ff ff          call   401106 <top>
  40110d:       90                      nop
  40110e:       c3                      ret

000000000040110f <b1>:
  40110f:       e8 f4 ff ff ff          call   401108 <c1>
  401114:       90                      nop
  401115:       c3                      ret

0000000000401116 <a1>:
  401116:       e8 f4 ff ff ff          call   40110f <b1>
  40111b:       90                      nop
  40111c:       c3                      ret

000000000040111d <main>:
  40111d:       e8 f4 ff ff ff          call   401116 <a1>
  401122:       b8 00 00 00 00          mov    $0x0,%eax
  401127:       c3                      ret
[...]
```

**二者差异**

```
top:
-       push   %rbp
-       mov    %rsp,%rbp
        jmp    40110a <top+0x4>
c1:
-       push   %rbp
-       mov    %rsp,%rbp
        call   401106 <top>
        nop
-       pop    %rbp
        ret
b1:
-       push   %rbp
-       mov    %rsp,%rbp
        call   40110c <c1>
        nop
-       pop    %rbp
        ret
a1:
-       push   %rbp
-       mov    %rsp,%rbp
        call   401118 <b1>
        nop
-       pop    %rbp
        ret
main:
-       push   %rbp
-       mov    %rsp,%rbp
        call   401124 <a1>
        mov    $0x0,%eax
-       pop    %rbp
        ret
```

假设我们在分析c1的执行过程，堆栈可能如下所示：

![执行top函数时，上述示例代码中的本机堆栈的内容正在运行。 显示不同的返回地址，没有其他内容，因为没有帧指针或局部变量。](https://image.cnxct.com/2022/11/stack_without_fp.png)*top运行时上述代码的native stack的内容*

我们需要一些其他信息或硬件支持，以便能够可靠地展开堆栈。

## 硬件方法

我们可以使用一些硬件设施来展开堆栈，例如Intel的[Last Branch Record (LBR)](https://lwn.net/Articles/680985/).LBR产生起始地址和目的地址对`FROM_IP`和`TO_IP`。我们可以使用它们来建立堆栈跟踪。 他的缺点就是他能记录的深度有限。

虽然 LBR 用途广泛且功能强大，但我们决定不将其用于 CPU 分析，因为并非每个虚拟化环境都提供此功能，而且它是英特尔特有的。这些缺点延伸到其他感兴趣的供应商特定的处理器特征，例如 [Intel Processor Trace (PT)](https://lwn.net/Articles/648154/)

## 一场特殊的邂逅

你可能会想，我怎么可能编译没有帧指针的C++应用程序，并且异常仍然工作得很好？ 那么Rust呢？在Rust中，默认情况下帧指针是禁用的，但是调用`panic()` 会显示完整且正确的堆栈跟踪。

为了使C++异常无论二进制代码是如何编译的都能工作，以及添加一些其他必要的工具来使它们发挥作用，编译器可以发出一些元数据来指示如何展开堆栈。 该信息提供程序计数器到关于如何恢复所有寄存器的指令的映射。

更多详情参见 [DWARF debugging information format](https://dwarfstd.org/doc/DWARF5.pdf) 和 [x86\_64 ABI](h...
---
title: Relocate、PLT、GOT And Lazy Binding
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458498698&idx=1&sn=f158b2958ca048423e10123368f5a58b&chksm=b18e860086f90f169490f11dc8c2f084b3c3f691e53bdf410db49c16c4ba7cb24e0b78c7b8e7&scene=58&subscene=0#rd
source: 看雪学苑
date: 2023-03-20
fetch_date: 2025-10-04T10:05:35.472814
---

# Relocate、PLT、GOT And Lazy Binding

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EnMsgyKyEBvTX1ia24gKQC1qIfiaGtVpvOSAiaQ63ibCibeb8jwuxBtJgVpUoRR99YFH0dMCnuJbll6DQ/0?wx_fmt=jpeg)

# Relocate、PLT、GOT And Lazy Binding

安和桥南

看雪学苑

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EnMsgyKyEBvTX1ia24gKQC1TYhs5xG4SUqH260icPNkibqnryfN02RZnkjAjT2bExL91o7TInxicZhmQ/640?wx_fmt=jpeg)

本文为看雪论坛优秀文章

看雪论坛作者ID：安和桥南

本篇文章将会尝试解释重定位，PLT，GOT以及延迟绑定，并且通过一个简单的例子动态调试追踪延迟绑定的过程。

##

## **1 Relocate**

> Relocation is the process of connecting symbolic references with symbolic definitions. Relocatable files must have information that describes how to modify their section contents, thus allowing executable and shared object files to hold the right information for a process's program image. Relocation entries are these data.

即：

重定位 是将符号定义和符号引用进行连接的过程。

重定位文件 需要提供一些描述如何修改section内容的相关信息，从而保证可执行文件和共享目标文件能够在程序镜像中存储正确的信息。

以32位系统为例（为了便于理解，本文后续内容均会以32位系统场景描述），其关键的数据结构如下：

```
// 隐式加法重定位，重定位处的汇编一般会是 e8 fc ff ff fftypedef struct {    Elf32_Addr r_offset;    uint32_t   r_info;} Elf32_Rel; // 显式加法重定位，重定位时需要计算的加数存储在 r_addendtypedef struct {    Elf32_Addr r_offset;     uint32_t   r_info;     int32_t    r_addend; } Elf32_Rela;
```

r\_offset指向了需要重定位的位置。

r\_information存储了需要重定位符号表的索引和重定位类型。

r\_addend 用于计算存储在可定位字段中的值。

在程序加载时，会通过自己的.rel section，告诉连接器需要重定位的位置，在后续会详细的展示一个32位程序重定位的过程。

##

## **2 PLT &GOT**

像上面那种在程序加载时，通过.relsection，让编译器基于重定位信息计算出调用函数在程序中的实际位置的加载方式，一般被称为静态链接，如果程序使用了外部的库函数时，整个库函数都会被直接编译到程序中。

可以思考一下它的缺点，以及对应的改正方法：

在一段只输出hello world的程序中，采用静态链接，需要将整个glibc链接到程序中，如果500个程序都需要使用glibc中的函数，那么glibc就会被封装进500个程序中。

可不可以将多个程序都会使用的库单独剥离出来，同时在源程序和库之间建立某种联系，确保源程序在执行的时候可以调用到库函数？

动态链接技术的提出就是为了解决这个问题，在程序运行时，将共享库和程序本身进行链接，同时，内存里的程序可以共享同一个库文件，这样既节省了硬盘存储空间，同样节省了内存空间。

静态链接与动态链接主要区别如下图所示。（本图参照《CTF竞赛权威指南》所画）
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EGhnFtJH2ysic4o9sUdFchNPgzFKLj061fsRt80LnccMXBDhicqVEnRnwCrrIALC6EydKnN0xiaiawAw/640?wx_fmt=png)

为了做到动态编译，首先需要生成位置无关代码（Posistion-Independent Code,PIC）,通过PIC一个共享库可以被多个进程共享。

同时想要完成动态链接在源程序中还需要有：

① 一个用来存储外部函数地址的数据段。

② 一段用来加载外部函数的代码。

因为数据段和代码段之间的距离是一个运行时常量，他们之间的偏移是固定的，于是这里就有了全局偏移表（GOT，Global Offset Table），它位于数据段的开始，用于保存全局变量以及库函数（外部函数）的引用，每一条8个字节，在程序加载时会完成重定位，并填入符号的绝对地址。GOT一般被拆成了两个section，不需要延迟绑定，用于存储全局变量，加载到内存中只需要被读取的.got，以及为了存储库函数需要延迟绑定写入的.got.plt。

而同时为了完成延迟绑定还需要将外部函数的值在运行时写入.got.plt，因此又引入了过程链接表（PLT,Procedure Liknage Table）。PLT是由代码片段组成，用于将地址无关函数转移到绝对地址。每一个被调用的库函数，都会映射到一组PLT 和 GOT。如下图所示：
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EGhnFtJH2ysic4o9sUdFchN8hGEsrKwc2xp1EjQTSPZDw5hZE3V0KiarG25Zy061W38KbiapzCS4ehA/640?wx_fmt=png)

##

## **3 Lazying Binding**

Lazy Binding，即延迟绑定，指的是只有当函数被调用的时候才进行函数绑定，这种方式加快的程序的启动速度。

为了完成延迟绑定的过程，PLT和GOT需要配合完成一些事情。

假设程序中存在一个puts函数被调用，在PLT 中的表项为puts@plt，在GOT中表项为`puts@got.plt。为了完成延迟绑定，在第一次执行的时候会完成以下事情：

① 源程序中call puts@plt.

② PLT 中对应表项存储的内容是jmp puts@GOT，因此会跳进到`puts@got.plt。

③ 在绑定之前，puts@got.plt位置存储还是puts@plt表项的第二指令的地址，因此会跳到PLT 执行第二条指令push n,这里的n指的是puts函数在GOT中的位置，这里的入栈操作是为了找到puts函数的符号名，以及puts函数在GOT表项中所占的位置，便于后续将函数的实际地址写入GOT表。

④ 执行PLT表项第三条指令jmp PLT[0],PLT[0]首先将GOT[1]入栈，然后jmp GOT [2].

⑤ GOT[2]保存的是\_dl\_runtime\_resolve()函数的入口地址，因此这里实际上就是调用\_dl\_runtime\_resolve()函数，完成符号解析和重定位工作，并将puts()函数的真实地址写入puts@got.plt。然后将控制权交给puts()函数。

在后续调用，就会直接到GOT表项取得puts函数的地址。

整理一下，PLT和GOT中存在着通用的指令和后续的指令如下所示：

```
PLT[0]: push GOT[1]        jmp GOT[2]PLT[1]: __libc_start_main()PLT[2]: jmp GOT[4]        push 0        jmp PLT[0]... GOT[0]: .dynmic 地址GOT[1]: relorGOT[2]: _dl_runtime_resolve()GOT[3]: sys startup  # 针对不同环境此处内容可能不同GOT[4]: PLT[2]第二条指令地址
```

整个过程草图如下所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EGhnFtJH2ysic4o9sUdFchN3F0tuCfFsC4S9yZnHPpMrf46GYyqeZOs1maR8Q4GUoXsv0h3h7Hstw/640?wx_fmt=png)

##

## **4 Quiz**

环境：

```
gcc (Ubuntu 11.3.0-1ubuntu1~22.04) 11.3.0 Linux null 5.15.0-67-generic #74-Ubuntu SMP Wed Feb 22 14:14:39 UTC 2023 x86_64 x86_64 x86_64 GNU/Linux
```

源代码：

```
#include <stdio.h> int print_hello() {        printf("hello PLT and GOT\n");} int main() {        print_hello();        return 0;}
```

编译：

```
gcc main.c -o test -save-temps -m32 -g -Wl,-z,lazy
```

-save-temps 会保存所有的中间输出结果。

-m32 表示输出的是32程序。

-Wl,-z,lazy强制开启延迟绑定。

-g 方便调试。

通过objdump查看目标文件汇编代码：

```
objdump -M intel -d main.o
```

print\_hello函数如下：

```
00000000 <print_hello>:   0:   53                      push   ebx   1:   83 ec 14                sub    esp,0x14   4:   e8 fc ff ff ff          call   5 <print_hello+0x5>   9:   81 c3 02 00 00 00       add    ebx,0x2   f:   8d 83 00 00 00 00       lea    eax,[ebx+0x0]  15:   50                      push   eax  16:   e8 fc ff ff ff          call   17 <print_hello+0x17>  1b:   83 c4 18                add    esp,0x18  1e:   5b                      pop    ebx  1f:   c3                      ret
```

main 函数如下：

```
00000024 <main>:  20:   55                      push   ebp  21:   89 e5                   mov    ebp,esp  23:   83 e4 f0                and    esp,0xfffffff0  26:   e8 fc ff ff ff          call   27 <main+0x7>  2b:   b8 00 00 00 00          mov    eax,0x0  30:   c9                      leave  31:   c3                      ret
```

通过objdump查看最终汇编代码：

```
objdump -M intel -d test
```

print\_hello函数如下：

```
0000119d <print_hello>:    119d:       53                      push   ebx    119e:       83 ec 14                sub    esp,0x14    11a1:       e8 fa fe ff ff          call   10a0 <__x86.get_pc_thunk.bx>    11a6:       81 c3 32 2e 00 00       add    ebx,0x2e32    11ac:       8d 83 30 e0 ff ff       lea    eax,[ebx-0x1fd0]    11b2:       50                      push   eax    11b3:       e8 98 fe ff ff          call   1050 <puts@plt>    11b8:       83 c4 18                add    esp,0x18    11bb:       5b                      pop    ebx    11bc:       c3                      ret
```

main函数如下：

```
000011bd <main>:    11bd:       55                      push   ebp    11be:       89 e5                   mov    ebp,esp    11c0:       83 e4 f0                and    esp,0xfffffff0    11c3:       e8 d5 ff ff ff          call   119d <print_hello>    11c8:       b8 00 00 00 00          mov    eax,0x0    11cd:       c9                      leave    11ce:       c3                      ret
```

**4.1 Relocate**

对比目标代码和最终代码的反汇编代码，可以看到，在print\_hello函数中，调用call函数时对应内容是有经过重定向的，如下图所示。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EGhnFtJH2ysic4o9sUdFchN6q6mfItbXlXdHR3tQEEYPeAArxJ58ptAwu2Yeibh8fXav8yJDz1wmdQ/640?wx_fmt=png)

在目标代码中：

```
4:   e8 fc ff ff ff          call   5 <print_hello+0x5> 16:   e8 fc ff ff ff          call   17 <print_hello+0x17>
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EGhnFtJH2ysic4o9sUdFchNIbKg27BtQIyCE9QkOv2pBib4DyKHgviaQzrMLOpJOyUKTZlAFDmn9FLw/640?wx_fmt=png)
查看对应重定位表，可以看到：

offset 为$5$ 的符号是 \_\_x86.get\_pc\_thunk.bx, offset为 $17$的符号是puts。

而在最终代码中：

```
11a1:       e8 fa fe ff ff          call   10a0 <__x86.get_pc_thunk.bx> 11b3:       e8 98 fe ff ff          call   1050 <puts@plt>
```

查看编译之后程序的符号：

```
readelf -s test 20: 000010a0     4 FUNC    GLOBAL HIDDEN    14 __x86.get_pc_thunk.bx 27: 00000000     0 FUNC    GLOBAL DEFAULT  UND puts@GLIBC_2.0
```

对于 \_\_x86.get\_pc\_thunk.bx, 采用的是S + A - P的方式计算偏移:

S 是符号的值

A 是重定位条目中的加数，在显示加数中，会使用ElfN\_REL中的值，而隐式的则是在call指令后面。

P 是要进行重定位的存储单位的地址。

即：\_\_x86.get\_pc\_thunk.bx: $0x10a0 + 0xffff fffc -0x11a2 = 0xffff fefa$

即重定位之后的调用：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EGhnFtJH2ysic4o9sUdFchNLmibAKicznbMSGhljXKMiakCbTCjqRCv0UDGicqoN8mkJiaJMjqKuHxkaRA/640?wx_fmt=png)
main函数中的print\_hello函数调用同理，不再赘述。

那么还剩下一个问题，puts函数此时在符号表中的值是0，又应该怎么计算呢？

###

### **4.2 Lazy Binding**

前面有讲到，Linux下符号动态链接默认采用的是延迟绑定的方式，也就是说，在程序运行时用到改符号的时候才会去解析它的地址（值）。

开始动态调试，启动后在puts@plt下断点:
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EGhnFtJH2ysic4o9sUdFchNiaKEmwOIBbfAto0QB34AeAmp86yjg8JCpU296veWpBaUXWJSLgfxtjg/640?wx_fmt=png)

可以看到PLT表的内容和上述所说的基本吻合，首先是一个jump指令，此时根据上面信息可以得知ebx寄存器存储的是GOT表地址，所以这条jump指令就跳转到GOT表中。第二条push 序号入栈，第三条jump 指令调转到的位置就是PLT[0]。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EGhnFtJH2ysic4o9sUdFchNQtWpAYt8yrPxXLkfnFgtIz4WDmWMQfFBxvqvxib...
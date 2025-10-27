---
title: How2模拟执行一个不同架构下的elf文件
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458563598&idx=1&sn=8c1239bb0331664d4c560c917506b7fb&chksm=b18d848486fa0d928de9fe7b14e9edf01dac647afd843113a596dc400f155dd5321bf7f619bd&scene=58&subscene=0#rd
source: 看雪学苑
date: 2024-07-14
fetch_date: 2025-10-06T17:41:19.716747
---

# How2模拟执行一个不同架构下的elf文件

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EDOEyyAjIYqJ7ZShibj1sPqkho42tstDuiaz56Hu633BXFbmJeqkVNarCHjUl3eL2DezcmjXNl2dkw/0?wx_fmt=jpeg)

# How2模拟执行一个不同架构下的elf文件

Aynakeya

看雪学苑

```
一

前言
```

关于ELF格式的解析和库文件的模拟执行在论坛里已经有很多了，这篇文章也算不上什么新的思路，单纯是作为个人在学习时的一点记录，希望我的经验能够帮助到大伙。如有错误缺漏请在评论区指正。

```
二

Introduction
```

在尝试逆向一个动态链接库的时候，有时你可能希望单独运行某个函数，以探究它的具体作用。

如果这个二进制文件的编译架构与你的机器架构相同，并且你拥有其所有依赖库，那么操作相对简单：直接使用`dlopen`加载动态库，然后通过 offset 获取函数地址，执行即可。

然而，如果遇到不同架构的二进制文件，比如 aarch64 架构，应如何方便地进行调试和模拟运行呢？

一种常见的方法是在相应架构上启动`gdbserver`或使用`frida`等类似工具进行跟踪。但这种方法过于笨重。是否存在一种更轻量级的方法来模拟运行这个 ELF 文件呢？

*unicorn模拟运行*,*外加elf简单介绍*

```
三

从去除字符串加密开始
```

让我们从我们的sample文件`libkpk.so`开始，这个库文件了包含了一个需要被逆向出来的加密算法。

`libkpk.so`是一个从安卓安装包里提取出来的库文件，根据反编译可以发现，这里面应该包含有三个函数，分别是`fetch`,`isKpk`和`kpk`，java通过jni来调用这几个函数。在这些函数中，我们重点关系的是`kpk`函数，这个函数是作为加密函数出现的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EQpXR3mibibqEQU4dF9tmOg44LaMGSiafrnIBDA4UhAjRE32qrdRribahllB5gJpAW6JHzWBviaSyd3Hg/640?wx_fmt=png&from=appmsg)

但是在这个二进制里，并没有找到任何和加密有关的字符串，即使有字符串，这些字符串也是已一种非常诡异的状态出现的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EQpXR3mibibqEQU4dF9tmOg43hqELIIlmGQYNhKnA7ulGm1uNYfH8FJb2LfqYkDC4xTWb0JfgJXIbw/640?wx_fmt=png&from=appmsg)

在观察这些诡异的字符串后，发现这些字符串都会在最开始被`init_array`里面的`.datadiv_decodexxx`函数修改，所以我们可以合理推断这些`datadiv_decode`函数就是解密函数，用在lib被加载的时候来解密被加密的字符串。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EQpXR3mibibqEQU4dF9tmOg4B45wf2uPowGIesN5R1Plfzx6CSuD5fYgHuHVFFtdjficaLmrGBWHHmA/640?wx_fmt=png&from=appmsg)

在经过搜索之后，可以发现`datadiv_decode`正是被Armariris进行字符串混淆后会出现的解密函数。

## Armariris混淆

Armariris是上海交通大学开发的基于llvm的混淆框架，开源在https://github.com/GoSSIP-SJTU/Armariris

armariris的字符串加密逻辑比较简单，“对于所有的常量字符串，先创建一份可读写的、类型相同、大小相同的全局变量，将原先的字符串xor随机数，存放到这块新的全局变量里[1]”。

解密也比较简单，把解密字符串的逻辑写到对应的解密的函数里，接下来只要在lib加载的时候，跑一下解密函数就行了。

## 详细步骤

所以，解密的方法可以被概括为：

1.加载elf到内存

2.模拟运行解密函数

3.保存解密后的字符串，覆盖掉原来加密的字符串

4.删掉所有的解密函数

然而，由于这个二进制是在是在`aarch64`下编译的，而我们的电脑是amd64的，没办法直接运行。这个时候，我们可以使用`unicorn`来模拟运行程序。

`unicorn`基于`qemu`，但是更加轻量级，提供了一个多个架构下模拟cpu运行的接口，非常适合在这个地方使用。

那么我们就可以开始惹。

### Step 1: 加载elf到内存中

第一部，我们需要加载elf文件到内存中，要完成这个，我们需要把elf文件里所有`PT_LOAD`segment标示的内存区域从文件中读取并写入相对应的内存地址。

在64位下，program header的定义如下。当`p_type`=`PT_LOAD`即代表该段为可装载段，表示即这个段将被装载或映射到内存中，其中`p_offset`代表该段在文件中的位置，`p_filesz`代表该段的长度。`p_vaddr`为数据映射到虚拟内存中的地址，`p_flags`代表这段区域的读写执行权限。当然因为我们是在cpu模拟机下执行，我们根本不关心他的权限，所以全部设置为`rwx`。

```
typedef struct {
        Elf64_Word      p_type;
        Elf64_Word      p_flags;
        Elf64_Off       p_offset;
        Elf64_Addr      p_vaddr;
        Elf64_Addr      p_paddr;
        Elf64_Xword     p_filesz;
        Elf64_Xword     p_memsz;
        Elf64_Xword     p_align;
} Elf64_Phdr;
```

> https://docs.oracle.com/cd/E19683-01/816-7777/chapter6-83432/index.html

在了解了基本概念后，我们就可以把elf对应的段加载到内存里了。如下代码所示，`get_mapping_address`会计算出这块内存需要mmap哪一块内存地址，并对齐page size，也就是0x1000。然后`mmap`并写入数据就行了。

```
for seg in lib.iter_segments_by_type('PT_LOAD'):
    st_addr, size = get_mapping_address(seg)
    # don't care, rwx everywhere
    emulator.mem_map(lib.address + st_addr, size, UC_PROT_ALL)
    emulator.mem_write(lib.address + seg.header.p_vaddr, seg.data())
    log.info("loaded segment 0x%x-0x%x to memory 0x%x-0x%x", seg.header.p_vaddr,seg.header.p_vaddr+seg.header.p_memsz, lib.address + st_addr, lib.address + st_addr+size)
```

###

### Step 2: 找到所有.datadiv\_decode开头的函数并执行

这步比较简单，用pwntools的读取文件后，在symbol table里找到所有开头为`.datadiv_decode`的函数，然后执行即可。

在aarch64中，return pointer的寄存器为`LR`，在进入函数前，先设置`LR`，那么函数结束的时候就会跳回`LR`，我们在这里把`LR`设置为0，那么就知道当程序运行到0的时候，函数就结束了。

```
datadivs = []
for name in lib.symbols:
    if name.startswith(".datadiv_decode"):
        datadivs.append(name)
for datadiv in datadivs:
    log.info("[%s] Function %s invoke", hex(lib.symbols[datadiv]), datadiv)
    emulator.reg_write(arm64_const.UC_ARM64_REG_LR, 0) # 把return pointer (LR) 设置为0
    emulator.emu_start(begin=lib.symbols[datadiv], until=0)
    log.info("[%s] Function return",hex(lib.symbols[datadiv]),)
```

###

### Step 3: 用解密后的数据patch掉原来加密的数据

这步也比较简单，因为所有的文本都在`.data`段里，直接把整个`.data`段覆盖掉就行了。

```
log.info("Patch .data section")
new_data = emulator.mem_read(lib.address + data_section_header.sh_addr, data_section_header.sh_size)
libfile.seek(data_section_header.sh_offset)
libfile.write(new_data)
```

###

### Step 4: Patch掉所有的解密函数

这步也比较简单，直接让函数ret就行了。

```
log.info("Patch .datadiv_decode functions")
for datadiv in datadivs:
    libfile.seek(lib.symbols[datadiv] & 0xFFFFFFFE)
    ret = b''
    try:
        ret = asm(shellcraft.ret())
    except:
        # fallback to manual
        ret = asm("ret")
    libfile.write(ret)
```

##

## 效果

把解密后的二进制拖入反编译软件，我们可以看到所有的字符串都已经被解密了，且对应的`JNINativeMethod`结构也比较好容易可以分辨出来。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EQpXR3mibibqEQU4dF9tmOg4vWC0I92cSUxcQRNcZs3fqXdLHO6BAE97EUchgLrgKvBzCfkiaj7g0bg/640?wx_fmt=png&from=appmsg)

找到了kpk对应的函数之后，就要考虑如何去模拟执行它了。

```
四

ELF文件是怎么Load的
```

在开始正式模拟运行之前，让我先来回顾一点基础知识，就是elf文件是怎么从加载到内存到运行的。

## Segment简单介绍

通过`readelf -l libkpk.decrypt.so`我们可以读取ELF文件并获取到一些基本的信息，首先我们可以知道这个库文件是一个**动态**的共享库文件。

他包含了几个关键的segment。

`PT_LOAD`:

在前文中提到了，`PT_LOAD`即可装载段，代表这类段会被加载到内存中。

`PT_DYNAMIC`:

这段也非常重要，代表了所有需要在运行时进行重定向的内容。这些内容包含got表，全局变量重定向信息以及任何其他需要在运行时重定向的内容。

比如说，现在大部分程序运行的时候都会开启PIE(position-independent executable)，开启pie之后，程序的基值就不为0了，这个时候就需要通过重定向修正符号正确的地址。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EQpXR3mibibqEQU4dF9tmOg4AKz6ZNA9OFBaHnjs6rRibeNtRXdZzrNiaukckQymjXsS7BMhHZulmJvw/640?wx_fmt=png&from=appmsg)

如果一个二进制文件不是库文件而是一个**动态的可执行文件**，那么还会有另外一个重要的segment，`PT_INTERP。`

`PT_INTERP`

这个segment里存放了所需要的程序解释器（也就是**动态链接器**）的信息与位置。动态链接器的作用是加载可执行文件的共享库，并且解析可执行文件中使用的符号，以便在程序运行时正确地调用这些库函数。它在程序启动时将各个共享库加载到内存中，并根据需要将符号解析成实际的内存地址，使得程序可以顺利执行。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EQpXR3mibibqEQU4dF9tmOg49eCB6wdG9xn9ycaLOIFIV5Gr2SeV1piaIZcwBa0xUyhg5jzcmBzW3lQ/640?wx_fmt=png&from=appmsg)

要注意的是，如果一个二进制文件是一个**静态**的可执行文件，简单来说，就是在build的时候加上`-static`参数的可执行文件，一般来说是没有`PT_DYNAMIC`和`PT_INTERP`segment的，因为没有必要。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EQpXR3mibibqEQU4dF9tmOg4TCASib9EJKdy8wF1kG1waKaw7bF4ocWQTLIsXEoxFdNXG1RIJUWibP9g/640?wx_fmt=png&from=appmsg)

##

## 静态链接与动态链接

我们知道，elf可执行文件根据编译的时候链接方式可以分为两类：一个是静态程序，编译的时候使用静态链接，另一种是动态程序，编译的时候使用动态链接。

### 静态链接

静态链接就是在编译链接时直接将目标的代码（也就是生成的.o文件）和所引用的库文件的代码一起打包的可执行文件中。也就是说，可执行文件本身就包含了所需的所有代码。

所以，通过静态链接的程序在发布与运行的时候不需要依赖库，可以独立运行。但是相对的，由于静态链接把所有需要的库都打包了进去，生成的二进制的文件会比较大。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EQpXR3mibibqEQU4dF9tmOg4ICPUwp0qqGb4G6wlFjsTLhjj8Qe0vszvFib5SCXjtcppIIE3fXhVkcw/640?wx_fmt=png&from=appmsg)

> source: 创建静态库的过程14

###

### 动态链接

动态链接是在编译时并不将所有目标代码和库文件的代码打包到可执行文件中，而是仅包含对这些库的引用信息。在程序运行时，**动态链接器**会根据这些引用信息找到并加载所需的共享库。

**编译时**：编译器生成目标文件（.o 文件），并将动态库的引用信息嵌入到可执行文件中，而不是库的实际代码。

**链接时**：链接器会将这些目标文件和必要的符号表一起打包生成最终的可执行文件。

**加载时**：程序启动时，制定的动态链接器会根据可执行文件中的引用信息，查找并加载需要的共享库，将它们映射到进程的地址空间中。

**符号解析**：动态链接器负责解析程序中使用的符号（例如函数调用和全局变量），将它们与加载的共享库中的实际地址进行匹配。

**重定位**：对于那些需要在运行时确定的地址，动态链接器会进行必要的重定位操作，确保程序在内存中正确运行。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EQpXR3mibibqEQU4dF9tmOg4tBkPTNIEC7RHYcauUDddcxBWF8bic71eZeQiby74sCnrm4YVTKQ5jr1A/640?wx_fmt=png&from=appmsg)

> source: 动态库链接过程14

##

## ELF LOOOADING.....

一个elf文件的loading也分情况讨论，如果需要加载的二进制文件是静态链接的，那么elf加载的过程相对来说就比较简单。

1.首先把所有`PT_LOAD`端都加载到内存中，设置并初始化好stack。

2.把pc(或者rip)指向elf头中的`entry`地址。

这样，一个静态elf文件就成功执行起来了。

但是，如果是动态链接的elf，那么就稍微比较复杂一点了，再加载完`PT_LOAD`端后还需要额外处理`PT_DYNAMIC`段修复重定向。

1.首先把所有`PT_LOAD`端都加载到内存中，设置并初始化好stack。

2.解析`PT_LOAD`并完成本程序内所有符号的重定向。

3.加载所有依赖的动态库。

4.根据重定位表（`.rel`或`.rela`），解析所有符号依赖，找到每个符号的实际地址，对符号引用进行重定位，修改内存中的代码或数据，使其指向正确的符号地址（包含即时绑定和懒绑定）。

5.把pc设置为`entry`，开始执行程序。

当然，在实际应用中，除了第一步，其他的步骤都不需要程序本体进行。这些步骤一般会被系统的动态链接器完成。所以动态加载的程序在完成自身程序的加载后，会首先用同样的方法把动态链接器加载到内存中，然后向动态链接器传入对应的数据，之后，程序就不需要管了，只需要等待动态连接器完成所有的操作并把pc重新指向程序本体的`entry`就好了。

当然，在这里我们就不依赖动态链接器了，我们可以来手动实现程序的重定向。

### 重定位

首先第一步是读取`PT_DYNAMIC`段来拿到所有需要的信息。在64位下，`PT_DYNAMIC`端中的数据结构可以由如下数据结构表示。

其中`d_tag`相当于一个类型标识符，`d_un`由`d_tag`控制，内部的值根据`d_tag`的不同代表不同的值。

```
typedef struct {
    Elf64_Xword d_tag;
    union {
        Elf64_Xword  ...
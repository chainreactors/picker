---
title: PWN入门-2-LibC取物-Ret2LibC
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458564568&idx=1&sn=f6f369138f3c2efab15f30973f1a0c49&chksm=b18d875286fa0e44f1ffbaff14a75c7be29743d822403a702d0c87ee9a8a9673c4e2c04f0b6f&scene=58&subscene=0#rd
source: 看雪学苑
date: 2024-07-23
fetch_date: 2025-10-06T17:43:24.390592
---

# PWN入门-2-LibC取物-Ret2LibC

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Fic0jo2Hu76p5858SiceSyULsq9rd3o1oYMpiaXciaR8jibpIN6OWVyoibvJjSwic81aSsGv9abyqB5PHZQ/0?wx_fmt=jpeg)

# PWN入门-2-LibC取物-Ret2LibC

福建炒饭乡会

看雪学苑

在【栈上的缓冲区溢出示例】（https://bbs.kanxue.com/thread-282188.htm）中介绍过编译器会将数据执行保护机制打开【Linux：`NX: No-Execute`，Windows：`DEP: Data Execution Prevention`】，该机制开启后，数据所在的内存页就会被标识为不可执行的状态。

栈上存放的都是数据，因此数据执行保护机制打开时，栈所在内存页会变成不可执行的状态，此时再将Shellcode放在栈上，显然Shellcode就无法执行了。

对于GCC编译器来讲，编译选项`-z execstack`和`-z noexecstack`可以打开或关闭数据执行保护机制。

在Linux中，可以通过`maps`虚文件查看内存布局，下面列出了当该机制打开和关闭时，栈所在内存页的状态。

```
r: 可读, w: 可写, x: 可执行, p: 私有段, s: 共享段

开启数据执行保护机制：
7ffeffee2000-7ffefff03000 rwxp 00000000 00:00 0                          [stack]

关闭数据执行保护机制：
7fff4d273000-7fff4d294000 rw-p 00000000 00:00 0                          [stack]
```

#

```
一

数据执行保护机制的实现
```

数据执行保护机制需要软硬件协作实现。

## 1.1 硬件支持

对于现代CPU而言，通常会采用冯诺依曼架构，少数使用ARM-v7指令集的CPU会基于哈弗架构实现。2种架构的区别在于，哈弗架构中指令和数据的保存区域是分开的，数据区是不可执行的，而冯诺依曼架构中并没有将指令和数据进行区分。

基于冯诺依曼架构实现的CPU为了保障系统的安全性，采用添加不可执行位到页表中，使得内存管理单元`MMU: Memory Manage Unit`可以控制页中数据是否可以执行。

从上面的栈地址可以看到，起始和结束地址都是以`x000`作为结尾，这是因为Linux中默认分配的页大小为4KB（0x1000），所以使用页表机制分配的地址都会以页作为基础单位，因此内存页的起始和结束地址都以`x000`结尾也就不奇怪了。

MMU不止支持操作系统设置页大小，不可执行位也是交给操作系统去配置的。在硬件支持不可执行位后，需要的就是软件支持。

## 1.2 软件支持

当需要操作系统支持数据执行保护机制时，首先面临1个问题，即操作系统从哪里得知应不应该设置不可执行位呢？

答案很简单，就是可执行文件，上面提到GCC的编译选项`-z execstack`和`-z noexecstack`会标识ELF是否开启数据执行保护机制。

ELF文件是Linux下可执行文件的标准格式，由ELF头信息、头表（段头表、节头表）信息、段信息、节信息组成。其中ELF头信息描述整个ELF文件的基本信息（如字节序、文件类型、目标机器等等）。段和节分别用于在运行期和链接期提供支持，不管是段还是节，都被划分成多个类型，不同的类型负责提供不同的功能。

不同类型段和节分布在ELF文件中的不同位置上，因此使用表结构去收纳不同类型的段和节，头表中会记录不同类型段或节的基本信息（其中包含段或节在ELF文件中的位置），段和节的信息并不会被收纳，但可以根据头表找到段或节，然后再获取其中的内容。

### 1.2.1 GNU\_STACK段的设置

操作系统加载可执行文件当然是运行期的事情，因此我们通过`readelf`工具`-l`参数查看ELF文件的段头表信息，在列出的段中可以看到`GNU_STACK`段的存在，当数据执行保护机制打开时其段属性会被设置成不可执行状态，反之则会设置成可执行状态。

```
readelf -l xxxx

R: 可写, W: 可读, E: 可执行

开启数据执行保护机制：
GNU_STACK      0x0000000000000000 0x0000000000000000 0x0000000000000000
                0x0000000000000000 0x0000000000000000  RW     0x10

关闭数据执行保护机制：
GNU_STACK      0x0000000000000000 0x0000000000000000 0x0000000000000000
                0x0000000000000000 0x0000000000000000  RWE    0x10
```

###

### 1.2.3 GNU\_STACK的检测

Linux中一般借助`execve`函数启动程序，`execve`函数会发送系统调用给内核。

```
SYSCALL_DEFINE3(execve,
        const char __user *, filename,
        const char __user *const __user *, argv,
        const char __user *const __user *, envp)
{
    return do_execve(getname(filename), argv, envp);
}
```

当内核收到系统调用请求后，会先检查请求的文件是否具备执行条件，如果文件可以执行就会调用`load_binary`接口加载ELF文件并执行。

```
static int search_binary_handler(struct linux_binprm *bprm)
{
    ......
    retval = fmt->load_binary(bprm);
    ......
}
```

在计算机中常常会有这样的情况，即同1个目标会可以有多个实现，这些实现即可能都需要加载，也可能视平台类型、硬件类型进行加载。为了更加方便的对这些实现进行管理，Linux会为目标设置统一的接口，接口内部会细化目标需要完成的功能，然后实现与具体的成员进行绑定，当Linux要针对某目标操作某些功能时，就会直接调用对应的成员。

不同实现对应的接口之间通常会使用链表进行管理。

```
static struct linux_binfmt elf_format = {
    .module		= THIS_MODULE,
    .load_binary	= load_elf_binary,
    .load_shlib	= load_elf_library,
#ifdef CONFIG_COREDUMP
    .core_dump	= elf_core_dump,
    .min_coredump	= ELF_EXEC_PAGESIZE,
#endif
};
```

比如下面是Linux平台上著名的驱动初始化代码，不同的驱动其实现不同，实现对应的函数名也会不同，如果初始化驱动时，还需要提前把每个实现的初始化函数的函数名和地址记下，在进行调用会非常麻烦。

所以Linux中规定了驱动的函数类型必须为`int`，那么此时只需要将初始化函数绑定到对应的结构体并注册到链表中，在初始化驱动时只需要遍历链表，再调用统一的成员名就可以，而不需要思考其他的细节。

**在计算机中没什么问题是添加中间层解决不了的**

```
内核：我要加载驱动！！！
内核：怎么有这么多驱动啊，函数名还不一样，我要怎么样才能挨个调用！！！
内核：不如设置一种统一的接口，所有驱动都要按照接口的格式设置初始化函数，然后注册，然后我遍历链表，挨个调用就可以
内核：具体你驱动内部怎么搞，我才不管呢！
```

```
按照统一格式设置初始化函数：
static int __init xxxx(void) { ...... }

static void __init do_pre_smp_initcalls(void)
{
    initcall_entry_t *fn;

    trace_initcall_level("early");
    for (fn = __initcall_start; fn < __initcall0_start; fn++) {
        do_one_initcall(initcall_from_entry(fn));
    }
}

fn对应驱动初始化函数地址：
int __init_or_module do_one_initcall(initcall_t fn)
{
    ......
    do_trace_initcall_start(fn);
    ret = fn();
    do_trace_initcall_finish(fn, ret);
    ......
}
```

当调用`load_binary`接口，通过`load_elf_binary`函数会检查段的类型及属性，其中就包含`GNU_STACK`段，然后根据`GNU_STACK`段的可执行属性设置`vm_flags`标志位，虚拟地址空间会根据该标志位设置页属性。

```
static int load_elf_binary(struct linux_binprm *bprm)
{
    ......
    for (i = 0; i < elf_ex->e_phnum; i++, elf_ppnt++)
        switch (elf_ppnt->p_type) {
        case PT_GNU_STACK:
            if (elf_ppnt->p_flags & PF_X)
                executable_stack = EXSTACK_ENABLE_X;
            else
                executable_stack = EXSTACK_DISABLE_X;
            break;

        case PT_LOPROC ... PT_HIPROC:
            retval = arch_elf_pt_proc(elf_ex, elf_ppnt,
                          bprm->file, false,
                          &arch_state);
            if (retval)
                goto out_free_dentry;
            break;
        }
    ......
}

int setup_arg_pages(struct linux_binprm *bprm,
            unsigned long stack_top,
            int executable_stack)
{
    ......
    if (unlikely(executable_stack == EXSTACK_ENABLE_X))
        vm_flags |= VM_EXEC;
    else if (executable_stack == EXSTACK_DISABLE_X)
        vm_flags &= ~VM_EXEC;
    ......
}
```

#

```
二

绕过思路-Libc取物
```

当我们观察最基本的C语言程序运行期的内存布局时，会发现C程序至少会依赖Libc、vDSO、LD三个动态链接库，并且这些动态链接库一定会存在可执行的部分，那么能否借助它们完成利用呢？

```
ldd ./example
        linux-vdso.so.1 (0x00007ffdb1ebb000)
        libc.so.6 => /usr/lib/libc.so.6 (0x00007f8b16ed7000)
        /lib64/ld-linux-x86-64.so.2 => /usr/lib64/ld-linux-x86-64.so.2 (0x00007f8b170ec000)
```

结论一定是可以的，下面会介绍C程序会什么会依赖上述3个动态链接库，以及到底该利用那个动态链接库完成PWN。

## 2.1 LD与LibC

在前面查看段头表时，可以看到`INTERP`段指定了`/lib64/ld-linux-x86-64.so.2`，并且发现它的格式还是动态链接库。

```
INTERP         0x0000000000000318 0x0000000000000318 0x0000000000000318
                0x000000000000001c 0x000000000000001c  R      0x1
        [Requesting program interpreter: /lib64/ld-linux-x86-64.so.2]

file /lib64/ld-linux-x86-64.so.2
/lib64/ld-linux-x86-64.so.2: ELF 64-bit LSB shared object, x86-64, version 1 (GNU/Linux), static-pie linked, BuildID[sha1]=c560bca2bb17f5f25c6dafd8fc19cf1883f88558, stripped
```

要知道现如今很难找到脱离动态链接而产生的程序，即使程序内只包含`main`函数且`main`函数直接返回，这是因为`main`函数其实不是程序的起点，真正起点会依赖其他东西。

当程序中没有`main`函数进行编译时，会发现存在未定义的数据导致无法成功链接。在GCC编译器的眼中，`main`函数需要由`_start`函数调用，它是ELF文件真正的入口。

```
/usr/bin/ld: /usr/lib/gcc/x86_64-pc-linux-gnu/14.1.1/../../../../lib/Scrt1.o: in function `_start':
(.text+0x1b): undefined reference to `main'
collect2: error: ld returned 1 exit status
```

可以在GDB中可以设置参数，对`main`函数前运行的情况进行调试。

```
set backtrace past-entry
set backtrace past-main

(gdb) bt
#0  main () at main.c:14
#1  0x00007ffff7dd8c88 in __libc_start_call_main (main=main@entry=0x55555555516a <main>, argc=argc@entry=1, argv=argv@entry=0x7fffffffdf68)
    at ../sysdeps/nptl/libc_start_call_main.h:58
#2  0x00007ffff7dd8d4c in __libc_start_main_impl (main=0x55555555516a <main>, argc=1, argv=0x7fffffffdf68, init=<optimized out>, fini=<optimized out>,
    rtld_fini=<optimized out>, stack_end=0x7fffffffdf58) at ../csu/libc-start.c:360
#3  0x0000555555555075 in _start ()
```

`_start`函数是与程序静态链接在一起的，不管是通过反汇编还是调试器进行观察，会发现`_start`函数会使用LibC中的`__libc_start_main`函数，这就使得程序必须与LibC建立动态链接的关系，`__libc_start_main`函数会对`main`函数的建立与退出进行处理。

当通过GDB在`_start`函数设置断点时，会发现有2个断点被设置下来，首先命中的是动态链接程序（也是ELF文件）的`_start`函数，其次才是主程序的`_start`函数。第一个`_start`函数来自动态链接库`/lib64/ld-linux-x86-64.so.2`，与前面`INTERP`段指定的动态链接库相同。

```
info b
Num     Type           Disp Enb Address            What
1       breakpoint     keep y   <MULTIPLE>
        breakpoint already hit 2 times
1.1                         y   0x0000555555555050 <_start>
1.2                         y   0x00007ffff7fe5740 <_start>

Breakpoint 1.2, 0x00007ffff7fe5740 in _start () from /lib64/ld-linux-x86-64.so.2
(gdb) c
Continuing.
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/usr/lib/libthread_db.so.1".
Breakpoint 1.1, 0x0000555555555050 in _start ()
```

由于现在的程序都依赖动态链接库，所以Linux会先将控制权交给动态链接器`ld-linux-x86-64.so.2`，LD会在主程序开始运行前进行预处理，其中有2个很重要的函数`dl_main`和`_dl_start_user`，`dl_main`函数负责解释`ld.so`参数并加载二进制文件和库，`_dl_start_user`函数负责跳转到主程序的入口点，然后把控制权交给主程序。

## 2.2 vDSO

程序的运行需要使用处理器、内存等物理...
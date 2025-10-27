---
title: 浅析linux系统加载：从CPU加电到用户态，讲讲BIOS、UEFI、MBR引导、GRUB引导
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458585295&idx=1&sn=8f423788cca9634b7603b8aa2f18fb0b&chksm=b18c384586fbb1539a5626afb200248f204060ecfc11efaab4955a2c9975750f9ed93708bcef&scene=58&subscene=0#rd
source: 看雪学苑
date: 2024-12-04
fetch_date: 2025-10-06T19:38:42.010151
---

# 浅析linux系统加载：从CPU加电到用户态，讲讲BIOS、UEFI、MBR引导、GRUB引导

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EEoP87icqNvOd9jAibJHwnO42sLQwym7GYQ3mzCCQCo6btpmpA3LC1dT7C6HH26EuwQSTPrzNoTSng/0?wx_fmt=jpeg)

# 浅析linux系统加载：从CPU加电到用户态，讲讲BIOS、UEFI、MBR引导、GRUB引导

是气球呀

看雪学苑

由于解密固件方面的逆向需要，所以需要了解linux系统加载机制。花了我好几天来来去去缕清关系和学习，学的时候还是慎用语言大模型不然容易被它绕进去。

本文默认读者学习过操作系统等课堂上能学到的知识，尝试使用通俗的语言+各个地方的截图+常见疑惑，结合来描述。

从CPU加电到用户态，大概流程如下(省略很多细节不过没关系，看这个图可以有个大概印象，不然刚开始接触那么多概念挺乱的记不住)

画了一张图，希望能帮到您进行理解：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EEoP87icqNvOd9jAibJHwnO4ETq0bNQpUAOI8CUib1FnGjHhWbEVHquFfh4DXgRxYvMFwTomRG4Dic3g/640?wx_fmt=jpeg&from=appmsg)

#

# 第零站：内核镜像bzImage文件结构

下图展现了bzImage里有什么？？

其就像一个“多级推进火箭”，在内核加载的过程中，逐渐把“有效载荷”（最右侧的vmlinux）解压到内存之中。
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EEoP87icqNvOd9jAibJHwnO4KIiahuRg1NcG3TZdwAYN8wBgeVKpSCkbp9FvzXV6tASFEh7t0231iabQ/640?wx_fmt=jpeg&from=appmsg)

##

## bzImage第一层：setup.bin

这部分是不进行压缩的，特别的是，此部分运行于386实模式。其专注于最基本的硬件探测和初始化。

### 历史

在历史上(Linux版本<=2.4，那时候还在用软盘)，直接由这一部分对内核进行内核的信息收集（如显示信息，内存信息等，通过BIOS的变量boot\_params获取），以及把内核加载进内存里。

### 现今

但后来人们制定了32位启动协议(32-bit boot protocol)，bootloader出现了，setup.bin以上职能都被取代了，其本身退化成辅助bootloader加载内核到内存里的部分。

那么，为什么不直接把setup.bin移除掉呢，这不是更省地方吗？

没有它却不太行，因为bootloader有些信息是必须要镜像来告诉它的，比如：内核是否是可重定位的，内核建议的加载地址等等。

而setup.bin在加载前未被压缩，天然的适合作为这样一个镜像与bootloader之间的“传话筒”。而且还要照顾到不能使用32位启动协议的场合，于是setup.bin便被保留下来了。

## bzImage第二层:uncompressed部分

这部分是不进行压缩的，与前者不一样，此部分运行于保护模式(或者64位长模式)。其专注于解压vmlinux内核镜像，以及内核重定位(如果内核可以重定位的话)

### 问题：为什么其不和setup.bin合并呢

有以下原因：

1.在实模式下,CPU 使用 20 位地址线,因此可寻址的内存空间最大只有 1MB (2^20 字节)，0x00000 ~ 0xFFFFF 。由于在实模式下直接执行内核的初始化逻辑与内核最终运行的保护模式(或者64位长模式)有较大差异，可能会遇到一些兼容性问题。

2.为了setup.bin的代码更为简洁，专注于单项功能，这样好维护。

## bzImage第三层：vmlinux.bin.gz(不一定是gzip也可以是别的)

顾名思义，使用了gzip压缩技术(或者lzma也可以，gzip压缩速度比较快)的部分，被uncompressed部分解压之后就是有效载荷vmlinux了。

### 问题：为什么一定要压缩呢，直接bin不是更加直接吗

首先这算半个历史遗留问题，在Linux版本<=2.4的时候内核镜像必须能够放入软盘里，而且当时加载内核的全过程都是在实模式下的，所以当时内核镜像必须经过压缩以小于1MB。

但是其实这样做也有好处所以保留了下来：gzip解压时间远远快于IO导入更大的镜像的耗时(因为是在CPU上执行解压的过程)，是有利的。

## bzImage最内层，有效载荷：vmlinux(.bin)

这是Linux 内核的完整可执行映像。其主要负责以下功能：

1.内存管理初始化：

◆在解压缩自身之后,vmlinux 会建立起完整的内存管理机制。

◆包括设置页表、初始化内存分配器等关键工作,为后续内核运行做好准备。

2.内核子系统初始化:

◆vmlinux 会启动各种内核子系统的初始化过程。

◆如进程管理、设备驱动、文件系统等核心功能模块的初始化。

3.内核main函数执行:

◆vmlinux 最终会执行内核的 main() 函数。

◆这是内核启动的最后一步,内核从此进入正式的运行状态。

那么，让我们按下电源键吧。

#

# 第一站：在CPU加电的那一刻

CPU进行了加电自检（Power-on self-test，POST），不需要太过了解，因为这属于硬件知识，只需要知道它做了这些事情：

1.初始化CPU内部寄存器和缓存
2.检查CPU功能是否正常
3.确定CPU的工作模式和性能参数
4.为操作系统启动做好基础设置

CPU被设计为只能运行内存里面的东西，RAM内存在断电时会丢失所有数据。也正是因为启动时RAM里面啥都没有，硬件工程师设计CPU时，硬性地规定了一个初始值沿用至今。

在加电的瞬间，强制将 CS 寄存器的值设置为 0XF0000，IP 寄存器的值设置为 0XFFFF0，CS 为代码段寄存器，而   IP 为指令指针寄存器。

这样计算机CS:IP 就是0xFFFF0 （CS\*10H+IP），cs左移4个二进制位。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EEoP87icqNvOd9jAibJHwnO48hf98PHiacibbiaibJKqcpibKzxS5TrQ0LMdt8LZY8eCMA9OLR0lbLRHOtA/640?wx_fmt=jpeg&from=appmsg)

在这两个地址上，便开始了一切的初始化。

# 第二站α路线：BIOS+MBR引导

BIOS(Basic Input/Output System，基本输入输出系统)
CS:IP 指向了 0XFFFF0 这个位置，这正是 BIOS 程序的入口地址。

## bootsect启动过程

在曾经的操作系统里面，bootsect是完成初始化任务的主要角色，后面才是grub

## bootsect模块(bootsect.s编译而成，存放在主引导扇区MBR，0磁道，0磁头，第1个扇区)

实际上BIOS的启动过程中，首先是去到入口点，如下所示，其会首先执行bootsect.s，而bootsect.s首要的任务就是把自身从0x07c00开始的数据复制到0x90000物理地址。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EEoP87icqNvOd9jAibJHwnO4xuGjS4fiabcr2cc9yw4nw7dQR6LWmR0lnDTZE3ZD6Zs1xwZqhLkGCXg/640?wx_fmt=jpeg&from=appmsg)

可以看到，这段x86汇编的主要功能就是设置寄存器指向原来的bootsect，以及复制数据，最后再次设置寄存器以备新的bootsect位置被使用。

从图上理解可能更为直观：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EEoP87icqNvOd9jAibJHwnO43eOiayBia9yaW1ZumnAnSJRKxCa01sgRCMLvEx9jt5UI20b3hw16Ijicg/640?wx_fmt=jpeg&from=appmsg)

相信很多人和我一样都会有疑惑,为什么需要复制到这里，岂不是多此一举？

当然不是的，这是因为以下两个主要原因：
1.原本的bootsect前后都有东西，空间很小，复制出来好进行更为复杂的操作
2.根据linux系统的设计，留在0x7c00以及附近的地址是危险的，会被后面加载的system模块覆盖，当然这个设计还是保守了，放心紧接着的后面会详细讲清的
然后就是setup.s登场了

### setup模块(setup.s编译而成，存放在MBR第2个到第4个扇区)

bootsect 执行完后，会跳转到内存地址 0x90200 处继续执行。

setup模块做了以下四件事情：

1.利用 BIOS 的 0x13 功能从硬盘读取当前引导设备的几何信息，ax的高8位ah表示扇区，ax的低8位al表示需要读取的扇区数量。
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EEoP87icqNvOd9jAibJHwnO4Ph942I7agMokV0czsSVQeaUc3jibrR6XDbZsEH9CKwIJSetrfm6jfsA/640?wx_fmt=jpeg&from=appmsg)
2.利用 BIOS中断0x10功能号ah=0x13扫描字符串内容，并显示"Loading system..."字样。
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EEoP87icqNvOd9jAibJHwnO4Jbf0MNr7Nm7UNGxeoE84VxgUsMmhSK3MeZyW1iaQAchNdHp30BAibXVQ/640?wx_fmt=jpeg&from=appmsg)
3.之后将硬盘上 setup 代码之后的 system 代码使用cmp加载到内存 0x10000 地址处。
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EEoP87icqNvOd9jAibJHwnO4iaVGzrodD74VavomJaF1wQkzDVjKQ8Sk35I7Kf8sm0mvGkFj2rros0w/640?wx_fmt=jpeg&from=appmsg)
4.接下来根据所保存的根文件系统设备号，以及从引导扇区获取的每个扇区的类型和大小(是 1.44M A 盘吗?)等信息，最终跳转到 setup 程序的入口(0x90200)执行 setup 程序。
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EEoP87icqNvOd9jAibJHwnO4U0aJ2xM8jesDR2V334Owcdgp6y3ckunhLh0ro1PNicLzxx1mWNCxOQQ/640?wx_fmt=jpeg&from=appmsg)

之后，内存布局变成的这样子：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EEoP87icqNvOd9jAibJHwnO4fHibF9JER7uBFpgoibov6gnRFzLicgZcvGvddvVaicrhxXrdxFrsQVbibtw/640?wx_fmt=jpeg&from=appmsg)

请注意，他们的内存空间不是是连续的，这个《Linux内核完全注释》里的图有误导之嫌疑。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EEoP87icqNvOd9jAibJHwnO4YeUcFADsUUBEOpVGKCVrPQWeOU4hEX5YJjhntDs5YKKqTE4j1FjycQ/640?wx_fmt=jpeg&from=appmsg)

在 Linux 0.11 版本中, system 代码占用了 240 个扇区。而在此之后的 2630 多个扇区都未被使用。这些未使用的空闲扇区可以用来存储一个基本的文件系统,从而可以支持从引导扇区启动系统的能力。

5.setup正式开始执行
setup程序的主要任务是利用BIOS中断去读取诸多系统需要的参数，并且将这些数据保存到bootsect的地方，直接覆盖掉已经使用完的bootsect。

获取的参数如下，看起来bootsect原来的位置确实够放了，这段代码比较长，都是获取参数的，此处限于篇幅不进行展示，了解一下获取的是什么就可以了。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EEoP87icqNvOd9jAibJHwnO44Jk0VygwR81ChxCfbLHInKm0qK7wqIUjSY2IS0geoyK25Y66NMzT7w/640?wx_fmt=jpeg&from=appmsg)

6.加载system模块(并进入保护模式(或者64位长模式))

setup程序将system代码加载到内存0x10000-0x8ffff的范围内(曾经人们认为这足以容纳整个系统代码,最大长度不会超过0x80000（512k），也即其末端不会超过内存地址0x10000+0x80000=0x90000)。

所以当时的人们认为，只需要让bootsect的地址放到0x90000，那么把system 模块加载到0x00000 开始的地方便不会波及bootsect和setup。

但是这显然对于现代的操作系统来说太小了，甚至整个实模式的空间加起来都不够system用的，所以后期还是要让system进入保护模式(或者64位长模式)，这样寻址空间就大了，足够让system加载进内存并执行了。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EEoP87icqNvOd9jAibJHwnO4icBsJDlULU42IEsj7j4DD1sDMY3HlVF5UHDBwkbXpMzQMMYtC5WMbpg/640?wx_fmt=jpeg&from=appmsg)
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EEoP87icqNvOd9jAibJHwnO42y2oUm5JbgAvBdcojnibxxDQ8J44JlFXtfnjR2NA1iakThboscaAWYkw/640?wx_fmt=jpeg&from=appmsg)

这里有些内容太太偏底层了，可以了解一下A20地址线、中断描述符号表IDT、全局描述符号表GDT。

A20地址线：
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EEoP87icqNvOd9jAibJHwnO4mqvBaYU3luicpkbsib4c1v3N5cVuicneq28D6MCRMBSXrAUBYsC4JKFaA/640?wx_fmt=jpeg&from=appmsg)

最后，内存布局变成了这样：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EEoP87icqNvOd9jAibJHwnO4Yia0gjG5yRvaQS65kvEibeJ2cXqPrtelJutTOhS3PucXMLCnf1LB3icZw/640?wx_fmt=jpeg&from=appmsg)

是的，在刚刚完成初始化以后，数据段和代码段描述符指针都直接指向0x00000，也就是system模块的起始点。

而setup的最后一条指令是jmp 0,8，此处8为段选择符，0是偏移量，在这里指临时全局描述符表gdt，于是跳转指向了0x00000。

### system模块(head.s以及各种内核程序编译而成，存放在第6扇区以后)

head.s，顾名思义，是system的head。其功能比较单一，首先是加载各个数据段寄存器，再重新设置中断描述符表idt，一共256项，每个描述符项占8字节....分页其实是基础知识问题，此处不再赘述。

设置中断+全局描述符的方式原来是封装好的：
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EEoP87icqNvOd9jAibJHwnO41kqVu2lp5kIv0APHDqXC9Djic6oIzLms5ibmJBLHPWbiaPiar6J3hpF6Zg/640?wx_fmt=jpeg&from=appmsg)

实际上长这样，有兴趣可以看看，不想看其实也没有啥关系。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EEoP87icqNvOd9jAibJHwnO4x5sDJ20iaG52zOM6fBGoSnRic49Cib1qz547ibBfiassv12Wic2NboHW99xg/640?wx_fmt=jpeg&from=appmsg)

后面还有设置页表的代码，比较复杂，有兴趣可以看看《Linux内核完全注释》。

总之，我们知道了head.s的主要任务就ok，那就是在进入保护模式(或者64位长模式)的那一刻，对idt、gdt、页表等进行了初始化，以让后面的内核模块顺利使用保护模式(或者64位长模式)。

此时的内存布局如图所示：
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EEoP87icqNvOd9jAibJHwnO4V1dGBZiaDFsLvIUZGNiaTInxpgsUkRhtRhFkpJeKK0mm3hFFiaWVAcRiaQ/640?wx_fmt=jpeg&from=appmsg)

此时的DS、CS、ESI，以及全局、局部描述符表寄存器的关系如图所示，注意一个LDT对应一个任务(进程)，一个GDT最多可以有64个LDT。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EEoP87icqNvOd9jAibJHwnO46out4f6s9dyEoqJJAJldPEaWNamvXQ65cgagmcqic9QqEWBcBETdSmg/640?wx_fmt=jpeg&from=appmsg)

##

## 从bootsect来看，BIOS需要做什么？

我们可以从一个系统正常运行的需求，反过来看BIOS需要做什么。

### 最需要的东西：CPU、内存

一个系统，没有CPU或者内存，啥都干不了。BIOS首先被CPU执行起来，然后它帮助CPU首先进行一些初始化，然后就是对内存进行初始化，BIOS把一部分的自身复制到内存里，最后就是跳到内存...
---
title: Windows内核：虚拟内存分页系统与自我引用技术
url: https://forum.butian.net/share/3806
source: 奇安信攻防社区
date: 2024-10-16
fetch_date: 2025-10-06T18:45:32.166057
---

# Windows内核：虚拟内存分页系统与自我引用技术

#

[问答](https://forum.butian.net/questions)

*发起*

* [提问](https://forum.butian.net/question/create)
* [文章](https://forum.butian.net/share/create)

[攻防](https://forum.butian.net/community)
[活动](https://forum.butian.net/movable)

Toggle navigation

* [首页 (current)](https://forum.butian.net)
* [问答](https://forum.butian.net/questions)
* [商城](https://forum.butian.net/shop)
* [实战攻防技术](https://forum.butian.net/community)
* [漏洞分析与复现](https://forum.butian.net/articles)
  NEW
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### Windows内核：虚拟内存分页系统与自我引用技术

前言
虚拟地址是现代计算机操作系统中非常重要的概念，尤其是在x86\_64架构中，操作系统通过分页机制来实现虚拟内存。分页不仅能够帮助操作系统有效管理内存，还能够提供内存隔离与保护，允许多...

前言
==
虚拟地址是现代计算机操作系统中非常重要的概念，尤其是在x86\\_64架构中，操作系统通过分页机制来实现虚拟内存。分页不仅能够帮助操作系统有效管理内存，还能够提供内存隔离与保护，允许多个进程共享物理内存的同时保持相互隔离，并能够提供比物理内存更大的地址空间。这对于多任务处理、程序的稳定性和安全性来说都至关重要。
分页机制
====
分页表
---
分页表是操作系统和处理器用于实现虚拟内存的一个关键数据结构，主要作用是将虚拟地址转换为物理地址。虚拟地址是程序看到的地址，而物理地址是硬件设备实际使用的地址。
通过分页，操作系统将内存分解为固定大小的块，称之为页面（Page），并通过页表进行地址映射，页面的大小通常为4KB。
### 虚拟地址布局
如下是一个典型的虚拟地址结构体：
```cpp
typedef union \_virt\_addr\_t
{
void\* value;
struct
{
std::uint64\_t offset : 12;
std::uint64\_t pt\_index : 9;
std::uint64\_t pd\_index : 9;
std::uint64\_t pdpt\_index : 9;
std::uint64\_t pml4\_index : 9;
std::uint64\_t reserved : 16;
};
} virt\_addr\_t, \*pvirt\_addr\_t;
```
在x86\\_64架构下，虚拟地址的布局如下：
1. \*\*Offset (偏移)\*\*：低12位用于页面内的偏移。每个页面的大小通常是4KB（即2^12字节），这12位决定了当前地址在页面内的偏移。
2. \*\*PT索引\*\*：页表的索引占9位（13到21位）
3. \*\*PD索引\*\*：页目录索引占9位（22到30位）
4. \*\*PDPT索引\*\*：页目录指针表的索引也占9位（31到39位）
5. \*\*PML4索引\*\*：最高9位（40到48位）用于索引PML4表项。PML4是x86\\_64架构中的最高级页表。
6. \*\*Reserved\*\*：最后16位是保留位。
如图所示：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-46958f9bdf121f1a33dd282f555cceabbf922bb1.png)
### 多级页表
多级页表使用了层次化的结构来减少每次内存访问时查找表项的开销。在x86\\_64架构的四级分页机制中，虚拟地址经过以下几个步骤转换为物理地址：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-67c2a928d1ad5e22bb7fbbb9aaa4847f86099dc1.png)
PML4是分页表的最顶层，如图可以看出，一个CR3指向PML4表，虚拟地址的PML4索引用于在PML4表中找到一个表项，该表项指向PDPT表，PDPT索引又从PDPT表中寻得一个表项用来指向PD表，以此类推。每一级分页表可以容纳512个条目，因此每级表占用9位地址空间，总共需要经过四级页表的查找来完成地址转换。
大页面
---
现在已知分页的粒度是4096字节大小，那如果要分配一个大页面呢？简而言之，不是使用一系列位来索引页表，而是使用虚拟地址的该范围来索引页面本身。
如下图：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-c26ec7b6696e359cb8586e0568e283d8091da6f2.png)
发现图中少了 9 bit for pt index ，通常，虚拟地址会经过多级页表（PML4 -&gt; PDPT -&gt; PD -&gt; PT）来映射到物理地址。然而，对于大页面，不需要像普通4KB页面那样经过所有四级页表的查找过程。如果是使用2MB大页面，虚拟地址中的PD索引直接指向物理内存块，而不需要再进入页表（PT）级别的查找。
如果使用1GB大页面也同理，虚拟地址中的PDPT索引直接指向物理内存块。这意味着不仅页表（PT）层被跳过，页目录（PD）层也被跳过。
同时，在使用2MB时，由于PT索引不需要使用，所以Offset偏移占21位，一个2MB页面大小为2^21字节。一个1GB页面为2^30字节。
访问分页表
-----
在x86\\_64架构中，\*\*PML4（Page Map Level 4）\*\* 是分页表的最顶层。每个虚拟地址首先通过PML4表中的一个条目被映射到下一层的页表（PDPT），从而完成虚拟地址到物理地址的映射。
由于\*\*Spectre/Meltdown\*\*漏洞的影响，操作系统引入了\*\*KPTI（Kernel Page Table Isolation）\*\*，即内核页表隔离。KPTI的机制是为每个进程创建两个不同的PML4表：
- \*\*用户模式和内核模式映射表\*\*：这个表包含所有用户模式和内核模式的映射，在传统操作系统中用于上下文切换时，保证进程能同时访问自己的内存和内核态内存。
- \*\*仅用户模式映射表\*\*：为了避免Spectre/Meltdown漏洞的利用，操作系统会在进入用户模式时切换到仅用户模式映射的PML4表，从而隔离内核空间，防止非法访问内核内存。
在Windows操作系统中，每个进程的内存管理由一个结构体`KPROCESS`管理，其中包含关于分页表和内存管理的关键信息。其子结构`EPROCESS`更详细描述了每个进程的内存布局、页表和其他资源的管理。
使用调试工具\*\*WinDbg\*\*，可以查看这些结构的布局，尤其是和分页表（特别是PML4）的关联。在WinDbg中输入命令`dt !\_KPROCESS`可以看到`KPROCESS`结构体的字段，其中第三个字段通常用于指向处理该进程的PML4表的页框号（PFN）。如下图：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-4b7925902c7577483340ca56e2af7c3860516f02.png)
### PFN（页框号）
\*\*PFN（Page Frame Number，页框号）\*\* 是物理页面的编号，PFN代表物理页面而不是物理地址本身。由于页面是按照4KB对齐的，因此物理地址的低12位可以忽略，这些低位仅用于页面内偏移，因此只存储高位来表示物理页面。
换句话说，PFN是物理地址的高位部分，用来标识一个物理页面，最后的12位表示偏移不需要直接存储，因为它们在页面对齐情况下都为零。为了解释如何将PFN转换回物理地址，需要将PFN左移12位（或将PFN乘以4096）。
### 访问PML4的物理地址
由多级页表可知，CR3寄存器存储的值是PML4表的基地址，现在要将其转换为物理地址，代码如下：
```cpp
typedef union \_cr3
{
std::uint64\_t flags;
struct
{
std::uint64\_t reserved1 : 3;
std::uint64\_t page\_level\_write\_through : 1;
std::uint64\_t page\_level\_cache\_disable : 1;
std::uint64\_t reserved2 : 7;
std::uint64\_t dirbase : 36;
std::uint64\_t reserved3 : 16;
};
} cr3;
const auto cr3\_value = CR3{ \_\_readcr3() }; // 读取当前进程的CR3寄存器
const auto pml4\_physical\_address = cr3\_value.dirbase &lt;&lt; 12; // 获取PML4表的物理地址
```
上述代码定义了一个联合体，该联合体通过位域分解了CR3寄存器的64位内容。主要关心的字段是`dirbase`，它表示PML4表的基地址。
`\_\_readcr3()`是MSVC编译器提供的一个内建函数，允许直接从硬件中读取CR3寄存器。之后从返回值中，获取`disbase`字段的值，并将其左移12位转换为完整的物理地址。
### 例子
假设有一个虚拟地址 0x71000000000 ，首先需要将其分解：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-855a1990673055f8a17f74d1cdbb3b4b98efd6bd.png)
虚拟地址的最低 12 位是页偏移量，接下来的 9 位是 PT 索引，接下来的 9 位是 PD 索引，接下来的 9 位是 PDPT 索引，接下来的 9 位是 PML4 索引。
由上，我们得到PML4\\_index=0x0E、PDPT\\_index=0x40、PD\\_index=0、PT\\_index=0、Offset=0。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-9cc216b2feed90c07a19b51e2f662419ad2eea66.png)
PML4索引0x0E在PML4表中为38a0000040653867。
在分页表中的每个条目（无论是PML4、PDPT、PD，还是PT条目）都有一个固定的结构，用于存储映射到物理地址的页框号（PFN）以及一些控制标志。对于x86\\_64系统，每个页表条目是64位长（8字节）。通常，页表条目包括以下几个关键部分：
- \*\*低12位\*\*：用于存储页表条目的标志位，如存在位（Present Bit）、读写位、用户/内核位等。这些位不包含物理地址的位。
- \*\*位12到位51\*\*：存储物理页框号（PFN）。
- \*\*位52到位63\*\*：这些位大多保留。
因此，0x38a0000040653867 可以转换为 0011 1000 1010 0000 0000 0000 0000 0000 0100 0000 0110 0101 0011 1000 0110 0111 。
在这里 1000 0110 0111 代表的就是低12位。十六进制867。而位12到位51的PFN则是0x40653，根据PFN到物理地址的转换，这里乘以0x1000，，使用该值（0x40653000）作为下一个分页表（PDPT）的基地址，并使用 PDPT\\_index（0x40）作为该表的索引：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-46c78efe3c71832472ac346d108bed750162c93f.png)
再次，取此 PFN（0x41cd7），将其乘以页面大小（0x1000），使用该值（0x41cd7000）作为下一个分页表（PD）的基地址，并使用 PD\\_index（0x00）作为此表的索引：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-7a53d86c68eb0c7868b90a5ac6a0d8e5c777a9e1.png)
最后一级也是同理：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-3475d1a8c0f9449b3614aefbbc257d1dc5173f73.png)
最后，剩下的就是将这个 PFN (0x3d7d9) 乘以页面大小 (0x1000)，并将 page\\_offset (0x000) 添加到之前的乘法 (0x3d7d9000)。
所以我们现在知道我们的虚拟地址 0x71000000000 实际上是映射物理地址 0x3d7d9000。
自我引用技术
======
自我引用这项技术允许通过虚拟地址来直接访问分页表的结构。这背后的原理是在分页表的某一层创建一个指向自身的条目，使得 CPU 可以通过特定的虚拟地址访问分页表本身。
原理
--
在64位系统中，分页使用了四级分页表架构：\*\*PML4\*\*、\*\*PDPT\*\*、\*\*PD\*\* 和 \*\*PT\*\*。自我引用技术的核心是将PML4中的某个条目指向它自身，即该条目不指向下一层的分页表（PDPT），而是指向PML4本身的物理地址。这样，当CPU尝试访问这个特定条目时，它实际上在访问整个分页表的结构。
这样做的好处是它允许通过虚拟地址直接访问分页表结构，使得系统中的任何进程都能够在虚拟地址空间中找到并遍历自己的页表，而无需进行复杂的CR3寄存器操作。
更具体的说，原本在64位系统中，PML4中的每个条目通常指向一个PDPT表，PDPT条目指向PD表，PD表条目指向PT表，最终PT表条目指向物理内存页面。通过自我引用技术，我们在PML4表中的某个条目（例如第0个条目或其他特定条目）指向PML4表本身的物理地址。这样，CPU在解析这个条目时，会发现这个条目指向的不是下一级表，而是PML4表本身，这就导致了每个级别（PDPT、PD、PT）都会再次指向PML4，从而形成了一个自我引用的循环。
实现
--
在64位系统中，假设我们使用PML4表中的第0个条目作为自我引用条目。具体来说，PML4表中的第0个条目会指向PML4表的物理地址，这与CR3寄存器中的地址相同。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-5eaab31daf88117da1cefa0c57a4d6fc72c7c8bd.png)
当PML4表中的一个条目指向PML4表本身时，CPU在分页过程中会反复使用该条目。它会导致：
- \*\*虚拟地址映射到PML4表本身\*\*：通过访问这个特殊的虚拟地址，CPU实际上是在访问PML4表的内容。这允许直接读取或修改PML4表中的内容。
- \*\*访问分页表的各个层级\*\*：由于CPU解析该虚拟地址时会多次使用相同的条目，它可以被重复使用用于所有分页级别（PML4、PDPT、PD、PT），从而允许通过虚拟地址直接遍历整个分页结构。
### 示例1 低端虚拟地址
使用 PML4 位置编号0的自引用条目：
假设，PML4表中的第0个条目指向PML4表的物理地址：
```c
PML4[0] = CR3; // CR3包含当前进程的PML4表物理地址
```
当CPU解析虚拟地址时：
- \*\*PML4索引0\*\*：指向PML4表的物理地址。
- \*\*PDPT索引0\*\*：继续指向PML4表。
- \*\*PD索引0\*\*：同样指向PML4表。
- \*\*PT索引0\*\*：指向PML4表中的页表条目。
这意味着从虚拟地址`0x0000000000000000`到`0x0000000000000FFF`，该地址范围实际上映射到了PML4表的前4KB内存。因此，访问该地址的内容实际上是在访问分页表本身。
### 示例2 高端虚拟地址
使用自定义的PML4位置编号：
假设，我们在PML4表中的一个特定条目，如0x1FF（最高位置）设置自引用条目：
```c
PML4[0x1FF] = CR3; // CR3包含PML4表的物理地址
```
则访问虚拟地址空间的高端地址（例如 `0xFFFFF80000000000`开始的地址）将会映射到PML4表，这意味着访问该地址时，CPU实际上是在访问分页表本身。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-11aef58ac5f7527c29fe6c32ecf3137449a00dcf.png)
这样就可以允许操作系统通过虚拟地址轻松遍历并修改当前进程的分页结构，而无需手动读取CR3寄存器的内容或直接操作物理地址。
弱点
--
通过自我引用条目，操作系统可以通过虚拟地址空间高效地管理分页表。但是它也有一定的缺点，主要问题在于\*\*自我引用条目缺乏随机性\*\*。
这里，\*\*PML4条目0x100\*\* 被用作自我引用条目，映射内存范围为 \*\*512GB\*\*，从 `0xFFFF8000'00000000` 到 `0xFFFF8080'00...
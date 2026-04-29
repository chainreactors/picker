---
title: Android从ELF-Loader到自定义Linker的实现及原理
url: https://mp.weixin.qq.com/s/5qJiLnpnVPOqtxuBWz8qjA
source: Doonsec's feed
date: 2026-04-28
fetch_date: 2026-04-29T05:09:47.320811
---

# Android从ELF-Loader到自定义Linker的实现及原理

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Cpo2XCpI7K0yczmESZdE3zkc9ds7llb7ocW5WKJNepfUzKTXibib3hRdMoyYPGESsmBVcMSo8TetpNHeCO839VJwRcH0eibmibibl3LoSPTglrms/0?wx_fmt=jpeg)

# Android从ELF-Loader到自定义Linker的实现及原理

东方玻璃
东方玻璃

看雪学苑

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/Cpo2XCpI7K0I5pLZxvbfBYrQk3k6jdR3oAUl49JmkLbd1Cyw2o43YjtY7cd9DlRhN9ofr7SwiaKBZdwbPhDRCYeIibUriafSxIjoP24GxlOFlE/640?wx_fmt=png&from=appmsg)

**1.ELF 文件结构**

![](https://mmbiz.qpic.cn/mmbiz_png/Cpo2XCpI7K2yVUxIbQe4rmSSU7cfsxmDfcVTricx3dIjvses5tJGCJAiatVc5k0VF5PibRydTibicuNJzaWuGOgnC6T1pyupP7zkkxBYjCiadtZbg/640?wx_fmt=png&from=appmsg)

在学习自定义linker前, 先过一遍ELF文件结构相关知识点。Linux 的一个 .so 或可执行文件本质上是 ELF(Executable and Linkable Format) 文件。

ELF文件结构解析和加载器实现可以参考本人之前的一篇文章:ELF文件结构浅析-解析器和加载器实现。

## ELF 基本框架

可以将ELF文件分为5大核心块：

1.ELF Header

描述ELF文件核心结构的基本信息，例如文件类型, 架构, 入口点地址等。并且指定了Program Headers和Section Headers的起始地址以及对应表项数目。

2.Program Headers

每个表项描述段(Segment)的基本信息, 包括段的起始地址, 大小, 权限等。供Linker判断segment是否需要加载, 如何加载到内存中。

3.Sections / Segments

节 Section 是文件视图, 每个节都有其功能, 划分各个节有助于静态分析工具和用户了解ELF文件的细节。段 Segment 是内存视图, Linker加载ELF文件到内存中只需要关注段如何加载, 不需要了解各个节的细节。一个段可以包含多个节, 如果节的权限相同且地址连续便可以视为同一个段方便。

4.Dynamic段

Section Headers 中, 为**.dynamic**节, Program  Headers中, 为 PT\_DYNAMIC 段

称之为 dynamic段 更加合适, 因为Linker在加载和链接时非常依赖它的信息。其指向了符号表(导入/导出符号), 重定位表, Hash表(导出表), 依赖库, PLT, GOT, .init, .init\_array等结构。

5.Section Headers

每个表项描述节(Section)的基本信息, 包括节名, 起始地址, 大小等。通常位于ELF文件末尾, Linker加载ELF文件时通常不会加载它, 因为运行时并不需要该结构, 但静态分析工具非常需要。

ELF文件按照顺序的布局大致如下 (以'.'开头的均为节区, 它们的顺序并非固定, 和编译器生成规则有关)：

![](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K1V52uiby3BgcOCxJk5UCRH2OLePMCtHpaIBAFfkLG9Ib7mRYdbR0czIk0DQ35Kw5IiaBzW59XKkmibHgep2GQPUSA4gsjdp21wu8/640?wx_fmt=jpeg&from=appmsg)![]()![]()

Section和Segment两者的关系:

* 一个Segment可以包含多个Section, 一个Section只属于一个Segment
* 加载器只关心Segment(Program Header), 不需要Section Header
* strip掉Section Header的SO仍然可以正常加载运行, 但会让IDA等逆向工具难以分析

Section和Segment在不同视角下的映射图：

![](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K3eKly6ze3zPgJds9nnlu0RwaswticBicCs4NjWGH3jTwAMnYQiaBp5zf9AXEZIHcwDWgUjlNy5vKUJA65wVkXPMGkBrhTLZjFY3k/640?wx_fmt=jpeg&from=appmsg)![]()![]()

IDA显示的segments, 可以发现相同权限的section通常是连续的。

即多个相同权限的section可以视为同一个segment：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K3PJIFbRJbndc1wLvSFDmkLIbBWTkg5quMg0A6nuiaZT2YIt0uzxlQEgws8yzyQMm3wHtbkWFRDJfZtGOZZ8tY0anibqfQRHwdr0/640?wx_fmt=png&from=appmsg)![]()![]()

## ELF Header

ELF Header位于文件最开头, 64位下固定64字节, 是整个文件的"身份证", 包含：

-ELF文件类型，目标CPU架构，入口点地址；

-ELF Header大小，Program / Section Headers的起始地址, 表项大小, 表项数等关键信息。

```
typedef struct {
unsignedchar e_ident[16];    // Magic: 0x7f 'E' 'L' 'F' + 类别/字节序/版本
uint16_t 	e_type;           // 文件类型: ET_EXEC(可执行) / ET_DYN(共享库/PIE)
uint16_t 	e_machine;        // 目标架构: EM_386 / EM_X86_64 / EM_AARCH64
uint32_t 	e_version;        // ELF版本
    Elf_Addr 	e_entry;          // 程序入口点虚拟地址 (可执行文件的_start,so通常为0)
    Elf_Off  	e_phoff;          // Program Header 表的文件偏移
    Elf_Off  	e_shoff;          // Section Header 表的文件偏移
    Elf64_Word	e_flags;		  // Processor-specific flags // 无用
      Elf64_Half	e_ehsize;		  // ELF Header 大小
      Elf64_Half	e_phentsize;	  // Program header 表项大小
uint16_t 	e_phnum;          // Program Header 表项条目数
    Elf64_Half	e_shentsize;	  // Section header 表项大小
uint16_t 	e_shnum;          // Section Header 表项条目数
    Elf64_Half	e_shstrndx;		  // 节名表在Section Headers中的索引
} Elf64_Ehdr;
```

Linker会首先读取该结构, 校验Magic Number (\x7fELF) 和 CPU架构, 然后从 e\_phoff 定位段表。

## Section Header

每个Section Header描述一个节的名称、类型、在文件中的位置和大小：

```
typedef struct
{
  Elf64_Word    sh_name;        /* 节区名称（在字符串表中的索引） */
  Elf64_Word    sh_type;        /* 节区类型（如 SHT_PROGBITS, SHT_SYMTAB 等） */
  Elf64_Xword   sh_flags;       /* 节区标志位（如可写 W、分配 A、执行 X） */
  Elf64_Addr    sh_addr;        /* 节区在执行时的虚拟内存地址 */
  Elf64_Off     sh_offset;      /* 节区在文件中的偏移量 */
  Elf64_Xword   sh_size;        /* 节区的字节大小 */
  Elf64_Word    sh_link;        /* 链接到另一个相关节区的索引 */
  Elf64_Word    sh_info;        /* 节区的附加信息（取决于节区类型） */
  Elf64_Xword   sh_addralign;   /* 节区的内存对齐要求（必须是 2 的幂） */
  Elf64_Xword   sh_entsize;     /* 如果节区包含固定大小的表项，则为每项的大小 */
} Elf64_Shdr;
```

一些常见的节区列表汇总如下, 文章后续会讲解这些节区:

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K0xywnElG34M2tiaDBkd2N2JNq9FHTFucMzRvHjoZUicnEibGww0bAYiakFfMRknzicWXGLmmiaPlpdFnvOBzNg6MUhpHlHIO0oONkc4/640?wx_fmt=png&from=appmsg)

以上并非所有节区, 一般还会有支持异常处理, 调试器辅助信息等功能的节区。

010editor查看Section Headers效果如下：

![](https://mmbiz.qpic.cn/mmbiz_png/Cpo2XCpI7K1icbiaXM8nZuGjXzqUqd8BmV0OEQclyzLj3o9yb96kNxuZER7yuLZ5XnkA51ZHz19rHGOxOKqI17z3LvebAo5ngT4QnCVZ0Rnts/640?wx_fmt=png&from=appmsg)![]()![]()

## Program Header

Program Header描述了文件中哪些部分需要映射到内存, 以及映射的属性:

```
typedef struct {
uint32_t p_type;    // 段类型
uint32_t p_flags;   // 权限: PF_R(读) | PF_W(写) | PF_X(执行)
    Elf_Off  p_offset;  // 段在文件中的偏移
    Elf_Addr p_vaddr;   // 段在内存中的虚拟地址
    Elf_Addr p_paddr;   // 物理地址(通常忽略)
uint64_t p_filesz;  // 段在文件中的大小
uint64_t p_memsz;   // 段在内存中的大小 (≥ p_filesz, 差值部分为BSS)
uint64_t p_align;   // 对齐要求
} Elf64_Phdr;
```

常见的段类型：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K100MWoxp3EGibjoVNNUPNhT45FIjhtRI0GLpW19aLRKSOf4Fiaia4ahI7ItI4xkuOW8N00TzjUOJZy0LE8CbnAAdszttf8OUicIia4/640?wx_fmt=png&from=appmsg)

010editor查看Program Headers效果如下, 带有很多辅助信息:

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K1MWubicaZYdJib1rbbCibj9TFQWjsfiaaYGEXxo95jiaJWyTYGRaqEXBseiciamc0ywxW8rHOl0uz1j7HibN1fYhkak2CgecNv65jP628/640?wx_fmt=png&from=appmsg)![]()![]()

Linker加载ELF文件时, 会遍历所有`PT_LOAD`段, 计算映像大小并分配内存, 将段填充至指定的虚拟地址, 之后设置段权限完成加载。

## String Table

ELF文件中有很多字符串,例如段名,变量名等, 由于字符串长度往往不固定,所以使用固定结构描述比较困难。

常见做法是将字符串集中起来存放到一张字符串表,然后通过索引查表来引用字符串

字符串表的内部结构极其简单：一块**连续的字节数组。**

设计规则：

* 每个字符串都以空字符`\0`(NULL) 结尾
* 表的第 0 个字节永远是`\0`
* 一个字符串可以包含另一个字符串

例如，如果有`"printf\0"`，恰好有个符号叫`rintf`，那么偏移量向后移动 1 位，就可以复用这段内存

ELF文件中有3种字符串表, 其中`.dynstr`最重要:

`.shstrtab`节头字符串表

存储“节区”自身的名字, 例如`".text"`,`".data"`,`".bss"`等字符串。非运行时必须, 主要供链接器和静态分析工具（如`readelf`）解析文件结构时使用。

`.strtab`静态字符串表

存储“静态符号”的名字, 包含了代码中所有的函数名, 全局变量名，用于调试的局部变量名和源文件名称。非运行时必须, 用于静态链接和调试。为了减小文件体积，发布前常使用`strip`命令将其剥离。

`.dynstr`动态字符串表

存储“动态链接”所需的名字: 1. 动态符号名(导入/导出函数和变量)  2. 依赖的外部共享库名称如 "libc.so.6"。运行时必须, 它是linker在运行时寻找外部函数、加载依赖库的符号名称来源,不可剥离。

010editor查看`.dynstr`效果如下:
![](https://mmbiz.qpic.cn/mmbiz_png/Cpo2XCpI7K2SugGkhLicBWtMrHTT58dBnz3R9fhaxlR3y78P74oElH3nbH5RjDR2YUbibVgAZSrstZk13ia88QYjShOf7TOHyZGsnI47jr5OQ0/640?wx_fmt=png&from=appmsg)![]()![]()

## Symbol Table

符号表记录了ELF导出和导入的所有符号(函数/全局变量等)：

```
typedef struct {
uint32_t st_name;   // 符号名在字符串表(.dynstr)中的偏移
uint8_t  st_info;   // 符号类型(函数/数据) + 绑定属性(全局/局部/弱)
uint8_t  st_other;  // 可见性
uint16_t st_shndx;  // 所在Section的索引 (SHN_UNDEF=外部符号)
    Elf_Addr st_value;  // 符号的地址(或偏移)
uint64_t st_size;   // 符号的大小
} Elf64_Sym;
```

通过符号表和对应的字符串表可以得到符号名,符号大小，符号地址等信息。

`.symtab`静态符号表

存储文件中的所有符号，包括局部函数、静态变量、调试信息等。非运行时必须，主要用于静态链接和调试(如`gdb`解析函数名),与`.strtab`一样，发布前常被`strip`剥离。

`.dynsym`动态符号表

仅存储动态链接所需的符号：导入/导出的外部函数/变量。运行时必须，它是Linker解析外部依赖的符号来源，不可剥离。

值得一提的是符号表中`st_name`存的不是字符串本身, 而是一个偏移量, 实际的函数名/变量名存在\*\*字符串表(`.dynstr`)\*\*中。

查找符号名时: symbolName = dynstr[sym.st\_name]

例如该样本中, strTableAddr = 0xA28, sym.st\_name = 0x2F

所以 sym\_name\_off = 0xA28+0x2F = 0xA57 , 即 strTable[0xA57] = "memcpy\0"

![](https://mmbiz.qpic.cn/mmbiz_png/Cpo2XCpI7K07HQvkej5ibwPwOoOaD6ibQ7L1ybbuNMCoXricGy3N5ibzKGGn5iaelq7iaw2hGG7wZZA55Ts6tsG1kKOTia5ZiatEkBK2qPVoocNwfH8/640?wx_fmt=png&from=appmsg)![]()![]()

## Dynamic Table

Dynamic Table 是动态链接的核心"索引目录", 它是一个`Elf_Dyn`数组, 每个元素是一个`(tag, value)`键值对：

```
typedef struct {
    Elf_Sxword d_tag;    // 标签类型
union {
        Elf_Xword d_val; // 整数值(如大小)
        Elf_Addr  d_ptr; // 地址值(如表的虚拟地址)
    } d_un;
} Elf64_Dyn;
```

Linker遍历Program Headers, 通过`PT_DYNAMIC`段属性找到dynamic table, 然后遍历提取所有需要的信息。

常见d\_tag标志含义及对应d\_un作用如下：

![](https://mmbiz.qpic.cn/mmbiz_png/Cpo2XCpI7K2B87Wo4Vadd9EfeyFhl4XMZlZVIey9nvHtyxRibmQAfmwicpbEqfProBlq1EBZUSDDXQy9V2NKTUmC07kUPF0HNBZujxO6AC8ek/640?wx_fmt=png&from=appmsg)

后续ELF Loader和自定义Linker会使用到其中大部分tag, 有一部分并不需要使用。

010editor查看Dynamic Segment效果如下：

![...
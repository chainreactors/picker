---
title: ELF文件结构浅析-解析器和加载器实现
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458587912&idx=1&sn=4ad15eeb82b8a9aa74549d38c434f8bc&chksm=b18c238286fbaa946e5eb7029be4c82277cba5b76f615a477adb6facc0f2e2e5102db924d3d4&scene=58&subscene=0#rd
source: 看雪学苑
date: 2025-01-01
fetch_date: 2025-10-06T20:07:41.569546
---

# ELF文件结构浅析-解析器和加载器实现

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FUhyEb7yfQEACaiafkKJLfNDkVTD7pYs07ibbEovN5JRvm3AJIGrXazI7VTx0ic5HGtibC6agDZzib8OA/0?wx_fmt=jpeg)

# ELF文件结构浅析-解析器和加载器实现

东方玻璃

看雪学苑

网上有不少ELF文件结构相关的文章,但大都介绍原理,具体的代码实现并不多(或许是因为有开源代码)。然而阅读开源代码不是我的强项(看的头大)，于是依据当年学习PE文件结构的思路，学习ELF文件格式。

仿照 readelf 的输出结果编写解析器, 最后编写了简单的ELF加载器。

代码支持x86和x64的ELF文件：

◆解析器针对x86/x64有两套实现, 支持解析x86和x64平台的ELF文件

◆加载器依赖编译环境,只能加载对应平台的ELF文件,要分别编译x86和x64的加载器

◆内容讲解演示主要以x86为主

环境&工具：

◆VMware pro 17.6.1

◆Kali Linux 2023.4 vmware amd64

◆gcc (Debian 14.2.0-8) 14.2.0

◆CLion 2024.2.3

◆010 Editor 13.0.1

◆IDA Pro 7.7

附件：

◆Sources.zip

◆CompiledTools.zip

◆TestFiles.zip

**由于本人水平有限, 内容错误之处还望大佬多多包涵, 批评指正**

```
一

ELF文件结构概述
```

ELF是UNIX系统实验室(USL)作为应用程序二进制接口(Application Binary Interface,ABI)而开发和发布的,也是Linux的主要可执行文件格式, 全称是Executable and Linking Format,这个名字相当关键,包含了ELF所需要支持的两个功能——执行和链接

ELF文件包含3大部分,**ELF头,ELF节,ELF段**：

◆节头表指向节, 类似PE的节表, 描述各个节区的信息

◆程序头表描述段信息,一个段可以包含多个节,指导ELF文件如何映射至文件

◆在OBJ文件中,段是可选的,在可执行文件中,节是可选的,但NDK编译的ELF文件同时有段和节

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Fu2sqFLykClOFThxX08GpMGc9mPQY2uLMk16ck2HLbg82XmyxicfZdFT0HMmQibUN1zNlv8eU2Bicww/640?wx_fmt=png&from=appmsg)

ELF文件封装了部分数据类型

```
#include <stdint.h>

typedef uint16_t Elf32_Half;
typedef uint16_t Elf64_Half;

/* Types for signed and unsigned 32-bit quantities.  */
typedef uint32_t Elf32_Word;
typedef	int32_t  Elf32_Sword;
typedef uint32_t Elf64_Word;
typedef	int32_t  Elf64_Sword;

/* Types for signed and unsigned 64-bit quantities.  */
typedef uint64_t Elf32_Xword;
typedef	int64_t  Elf32_Sxword;
typedef uint64_t Elf64_Xword;
typedef	int64_t  Elf64_Sxword;

/* Type of addresses.  */
typedef uint32_t Elf32_Addr;
typedef uint64_t Elf64_Addr;

/* Type of file offsets.  */
typedef uint32_t Elf32_Off;
typedef uint64_t Elf64_Off;

/* Type for section indices, which are 16-bit quantities.  */
typedef uint16_t Elf32_Section;
typedef uint16_t Elf64_Section;

/* Type for version symbol information.  */
typedef Elf32_Half Elf32_Versym;
typedef Elf64_Half Elf64_Versym;
```

可以发现,32和64位定义的数据结构仅有Addr和Off有位宽差距,我们可以定义对应的通用类型。

| ELF数据结构 | 原始类型 | 备注 |
| --- | --- | --- |
| Elfn\_Half | uint16\_t |  |
| Elfn\_Word | uint32\_t |  |
| Elfn\_Sword | int32\_t |  |
| Elfn\_Xword | uint64\_t |  |
| Elfn\_Sxword | int64\_t |  |
| Elf32\_Addr | uint32\_t | 地址 |
| Elf64\_Addr | uint64\_t |  |
| Elf32\_Off | uint32\_t | 文件偏移 |
| Elf64\_Off | uint64\_t |  |
| Elfn\_Section | uint16\_t | 节索引 |
| Elfn\_Versym | uint16\_t |  |

使用gcc分别编译32/64位的elf可执行文件用于测试。

```
#include <stdio.h>

int main(int argc, char* argv[]){
    printf("Hello ELF!\n");
    return 0;
}
```

```
gcc -m32 -O0 main.c -o HelloELF32
gcc -m64 -O0 main.c -o HelloELF64
```

编写ELF解析器/加载器前,定义文件读取函数。读取指定路径文件,返回字节指针和读取文件大小。

```
// 读取文件,返回buffer和读取字节数
uint8_t* readFileToBytes(const char *fileName,size_t* readSize) {
    FILE *file = fopen(fileName, "rb");
    if (file == NULL) {
        printf("Error opening file\n");
        fclose(file);
        return NULL;
    }
    fseek(file, 0,SEEK_END);
    size_t fileSize = ftell(file);
    fseek(file, 0,SEEK_SET);
    uint8_t *buffer = (uint8_t *) malloc(fileSize);
    if (buffer == NULL) {
        printf("Error allocating memory\n");
        fclose(file);
        return NULL;
    }
    size_t bytesRead = fread(buffer, 1, fileSize, file);
    if(bytesRead!=fileSize) {
        printf("Read bytes not equal file size!\n");
        free(buffer);
        fclose(file);
        return NULL;
    }
    fclose(file);
    if(readSize)
        *readSize=bytesRead;
    return buffer;
}
```

#

```
二

ELF Header
```

#

定义在elf.h中：

```
#define EI_NIDENT (16)
typedef struct
{
  unsigned char    e_ident[EI_NIDENT];    /* Magic number and other info */
  Elf32_Half    e_type;            /* Object file type */
  Elf32_Half    e_machine;        /* Architecture */
  Elf32_Word    e_version;        /* Object file version */
  Elf32_Addr    e_entry;        /* Entry point virtual address */
  Elf32_Off     e_phoff;        /* Program header table file offset */
  Elf32_Off     e_shoff;        /* Section header table file offset */
  Elf32_Word    e_flags;        /* Processor-specific flags */
  Elf32_Half    e_ehsize;        /* ELF header size in bytes */
  Elf32_Half    e_phentsize;        /* Program header table entry size */
  Elf32_Half    e_phnum;        /* Program header table entry count */
  Elf32_Half    e_shentsize;        /* Section header table entry size */
  Elf32_Half    e_shnum;        /* Section header table entry count */
  Elf32_Half    e_shstrndx;        /* Section header string table index */
} Elf32_Ehdr;

//64位
typedef struct
{
  unsigned char	e_ident[EI_NIDENT];	/* Magic number and other info */
  Elf64_Half	e_type;			/* Object file type */
  Elf64_Half	e_machine;		/* Architecture */
  Elf64_Word	e_version;		/* Object file version */
  Elf64_Addr	e_entry;		/* Entry point virtual address */
  Elf64_Off		e_phoff;		/* Program header table file offset */
  Elf64_Off		e_shoff;		/* Section header table file offset */
  Elf64_Word	e_flags;		/* Processor-specific flags */
  Elf64_Half	e_ehsize;		/* ELF header size in bytes */
  Elf64_Half	e_phentsize;		/* Program header table entry size */
  Elf64_Half	e_phnum;		/* Program header table entry count */
  Elf64_Half	e_shentsize;		/* Section header table entry size */
  Elf64_Half	e_shnum;		/* Section header table entry count */
  Elf64_Half	e_shstrndx;		/* Section header string table index */
} Elf64_Ehdr;
```

可以使用readelf查看

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Fu2sqFLykClOFThxX08GpMl9SUW8kialcYIpXA2FHia797CsrYlNzxdZnCcX6sQUVQmaJE8pLxnDsQ/640?wx_fmt=png&from=appmsg)

##

## e\_ident

16字节ELF标识，前4字节是ELF文件标识"\x7fELF"，不可修改。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Fu2sqFLykClOFThxX08GpM6jDcE2tg7xzEv0P5eI9PtFU5TmbwfGqdIPicuKoEZvyutGjxDxMwAAg/640?wx_fmt=png&from=appmsg)

010editor中解析如下

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Fu2sqFLykClOFThxX08GpM59Dhiba1wIaib4Xia7dzYUUcXeMb4SE4uDaslVpibY3xgRwEmPPRAAGLEg/640?wx_fmt=png&from=appmsg)

1.e\_ident[EI\_CLASS]

2.e\_ident[EI\_DATA]

3.e\_ident[EI\_VERSION]

## e\_type

2字节，表明目标文件属于哪种类型

Android5.0后，可执行文件全部为so，这个标志只能为03不可修改。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Fu2sqFLykClOFThxX08GpMTBsz8PxrWvRoTeFjeuMjYlX2XmntD5bzdnKjKHS0pWV77Gy1yLicRQA/640?wx_fmt=png&from=appmsg)

```
/* Legal values for e_type (object file type).  */

#define ET_NONE		0		/* No file type */
#define ET_REL		1		/* Relocatable file */
#define ET_EXEC		2		/* Executable file */
#define ET_DYN		3		/* Shared object file */
#define ET_CORE		4		/* Core file */
#define	ET_NUM		5		/* Number of defined types */
#define ET_LOOS		0xfe00		/* OS-specific range start */
#define ET_HIOS		0xfeff		/* OS-specific range end */
#define ET_LOPROC	0xff00		/* Processor-specific range start */
#define ET_HIPROC	0xffff		/* Processor-specific range end */
```

## e\_machine

2字节,该字段用于指定ELF文件适用的处理器架构,部分定义如下, 对于intel,固定为EM\_386

```
#define EM_NONE		 0	/* No machine */
#define EM_M32		 1	/* AT&T WE 32100 */
#define EM_SPARC	 2	/* SUN SPARC */
#define EM_386		 3	/* Intel 80386 */
#define EM_68K		 4	/* Motorola m68k family */
#define EM_88K		 5	/* Motorola m88k family */
#define EM_IAMCU	 6	/* Intel MCU */
#define EM_860		 7	/* Intel 80860 */
#define EM_MIPS		 8	/* MIPS R3000 big-endian */
#define EM_S370		 9	/* IBM System/370 */
#define EM_MIPS_RS3_LE	10	/* MIPS R3000 little-endian */
                /* reserved 11-14 */
#define EM_PARISC	15	/* HPPA */
                /* reserved 16 */
```

## e\_version

4字节,指明目标文件版本

Android不检查该字段,IDA检查,但对反汇编无影响

## e\_entry

4或8字节,程序入口点(OEP) RVA, 如果e\_type=2 即可执行程序, 则该字段为VA; 如果是so,则为0

## e\_phoff

4或8字节,程序头表偏移FOA,如果没有程序头表则该字段为0

## e\_shoff

4或8字节,节头表偏移FOA,如果没有节头表则该字段为0

Android对抗中经常会删除节表

## e\_flags

4字节标志,无用

## e\_ehsize

2字节,ELF文件头大小

Android不检查,默认ELF Header大小为52字节; IDA检查,修改该字段只会产生警告不影响反汇编

## e\_phentsize

2字节,表示程序头表每一个表项的大小

## e\_phnum

2字节,表示程序头表的表项数目

## e\_shentsize

2字节,节头表表项大小

## e\_shnum

2字节,节头表表项个数

## e\_shstrndx

2字节...
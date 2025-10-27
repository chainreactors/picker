---
title: Windows 通用日志文件系统（CLFS）解析
url: https://mp.weixin.qq.com/s?__biz=MzUzMDUxNTE1Mw==&mid=2247499262&idx=1&sn=378249e192ef03b85763c08056ccd322&chksm=fa522840cd25a156e0cf736e01e47d7c32ecfa15a94a03f231896201ad3de48c7a325220a5a8&scene=58&subscene=0#rd
source: 山石网科安全技术研究院
date: 2022-12-27
fetch_date: 2025-10-04T02:33:29.760524
---

# Windows 通用日志文件系统（CLFS）解析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Gw8FuwXLJnRO1e64AEPGB2AAcLibZBOrNe1Dc7A2dTbaemlibrY83aWn6MZCWaibjeFOvm35juh1lhaXREFUGLp8Q/0?wx_fmt=jpeg)

# Windows 通用日志文件系统（CLFS）解析

原创

信创安全实验室

山石网科安全技术研究院

**0****1**

**关于通用日志文件系统**

通用日志文件系统（CLFS）是Windows Vista引入的一种新的日志机制，它负责提供一个高性能、通用的日志文件子系统，专用客户端应用程序可以使用该子系统，多个客户端可以共享该子系统用来优化日志访问，任何需要日志记录或者是恢复支持的用户模式的应用程序都可以使用CLF。

**02****‍**

### **使用通用日志文件系统**

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnRO1e64AEPGB2AAcLibZBOrNUwfz854uPORLmmd0ODf0jWMtPFjBGzicb7UGfCwFhjBU0LNOqWIARSg/640?wx_fmt=png)

**• 创建日志文件**

CreateLogFile：创建或者打开日志文件（.blf）。日志名决定这个日志为单路日志还是多路日志，日志名格式为（log :<LogName>[::<LogStreamName>] ）,通过CloseHandle函数关闭日志文件。

**• 使用日志文件**

通过阅读MSDN文档

逆向clfs.sys

**BLF格式**

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnRO1e64AEPGB2AAcLibZBOrN5cMnpqFibsjrNKpd7kSG0YLE9dficZv2q5XKXhSBUJvWzicSqTDIj732g/640?wx_fmt=png)

在日志文件中有6个不同的元数据块，分别为Control Record、Base Record、Truncate Record以及三个对应的shadow blocks。在每个元数据块开始也会有一个\_CLFS\_LOG\_BLOCK\_HEADER用来保存一些基本信息。

一个CLFS日志的存储由两部分组成：

1. 包含元数据（metadata）的base log file（BLF）

BLF文件大小通常为64KB，但是可以根据需要增长，其中包含了日志存储所需的一些元信息，例如日志的起始位置，容器的大小和路径，日志名称，客户端信息等，考虑到日志恢复的需要，BLF文件中包含了一份元数据的拷贝，使用dump count参数来识别哪份信息是最新的。

2. 最多1023个包含真正数据的容器文件

容器是一个活动的日志流在空间上的基础分配单元，同一日志中的容器大小是一致的，是512KB（一个扇区的大小）的倍数，最大为4GB，CLFS客户端通过增加和删除容器实现日志流的扩大和缩小，在实现时，CLFS把容器当作BLF所在卷上的一个连续文件，通过在逻辑上将多个容器串在一起，形成包含一条日志的单个逻辑顺序磁盘区。初始化的时候一条日志至少要分配两个容器。‍

CLFS使用日志块对记录进行组织管理，每个日志块由多个512字节的扇区组成，之后对日志数据的读取和写入操作都在日志块上进行。

**\_CLFS\_LOG\_BLOCK\_HEADER结构**

```
typedef struct _CLFS_LOG_BLOCK_HEADER
{
UCHAR MajorVersion;
UCHAR MinorVersion;
UCHAR Usn;
CLFS_CLIENT_ID ClientId;
USHORT TotalSectorCount;
USHORT ValidSectorCount;
ULONG Padding;
ULONG Checksum;         // 日志块数据的校验和（Crc32校验）
ULONG Flags;
CLFS_LSN CurrentLsn;
CLFS_LSN NextLsn;
ULONG RecordOffsets[16];       // 每个记录的偏移值
ULONG SignaturesOffset;         // 一块内存的偏移值
} CLFS_LOG_BLOCK_HEADER, *PCLFS_LOG_BLOCK_HEADER;
```

Checksum是该日志块数据的校验和，在读取数据时会对该数据进行校验，采用的是CRC32的校验方式。‍‍

RecordOffsets保存每一个记录的偏移值，第一个记录与BlockHeader相连，偏移为sizeof(CLFS\_LOG\_BLOCK\_HEADER)，也就是0x70；

SignaturesOffset字段保存了一块内存的偏移值，日志在编码时每0x200字节的最后两个字节将被签名所覆盖，被覆盖前的数据将存放在SignaturesOffset字段所计算偏移的内存中。当解码的时候再将这段内存中保存的数据写回到原来的区域，编码和解码的函数分别为ClfsEncodeBlock和ClfsDecodeBlock

由于在编码阶段每个扇区的最后两个字节被改写成了扇区签名，因此需要对原始数据进行备份，日志块的最后一个扇区结尾处，有一个签名数组，这个数组中就保存了原始数据，由\_CLFS\_LOG\_BLOCK\_HEADER中的SignatureOffset表示。在写入日志的时候，可以比较每个扇区结尾签名位置的数据是否和签名数组中的数据一致来判断写入是否成功。

**\_CLFS\_CONTROL\_RECORD结构**

```
typedef struct _CLFS_CONTROL_RECORD
{
    CLFS_METADATA_RECORD_HEADER hdrControlRecord;
    ULONGLONG ullMagicValue;
    UCHAR Version;
    CLFS_EXTEND_STATE eExtendState;
    USHORT iExtendBlock;
    USHORT iFlushBlock;
    ULONG cNewBlockSectors;
    ULONG cExtendStartSectors;
    ULONG cExtendSectors;
    CLFS_TRUNCATE_CONTEXT cxTruncate;
    USHORT cBlocks;
    ULONG cReserved;
    CLFS_METADATA_BLOCK rgBlocks[ANYSIZE_ARRAY];
} CLFS_CONTROL_RECORD, *PCLFS_CONTROL_RECORD;
typedef struct _CLFS_METADATA_BLOCK
{
    union
    {
        PUCHAR pbImage; // 指向内存中数据的指针，
        ULONGLONG ullAlignment;
    };
    ULONG cbImage;          // 日志块的大小
    ULONG cbOffset; // 偏移
    CLFS_METADATA_BLOCK_TYPE eBlockType;
} CLFS_METADATA_BLOCK, *PCLFS_METADATA_BLOCK;
```

包含了有关布局，扩展区域以及截断区域的信息，其中cBlocks表示整个文件中包含的日志块的数量。

**\_CLFS\_BASE\_RECORD\_HEADER格式**

```
typedef struct _CLFS_BASE_RECORD_HEADER
{
    CLFS_METADATA_RECORD_HEADER hdrBaseRecord;
    CLFS_LOG_ID cidLog;
    ULONGLONG rgClientSymTbl[CLIENT_SYMTBL_SIZE];
    ULONGLONG rgContainerSymTbl[CONTAINER_SYMTBL_SIZE];
    ULONGLONG rgSecuritySymTbl[SHARED_SECURITY_SYMTBL_SIZE];
    ULONG cNextContainer;
    CLFS_CLIENT_ID cNextClient;
    ULONG cFreeContainers;
    ULONG cActiveContainers;             // 当前活跃的容器数
    ULONG cbFreeContainers;
    ULONG cbBusyContainers;
    ULONG rgClients[MAX_CLIENTS_DEFAULT];
    ULONG rgContainers[MAX_CONTAINERS_DEFAULT];   // 保存容器上下文的偏移值
    ULONG cbSymbolZone;
    ULONG cbSector;
    USHORT bUnused;
    CLFS_LOG_STATE eLogState;
    UCHAR cUsn;
    UCHAR cClients;
} CLFS_BASE_RECORD_HEADER, *PCLFS_BASE_RECORD_HEADER;
```

**\_CLFS\_CONTAINER\_CONTEXT结构**

```
typedef struct _CLFS_CONTAINER_CONTEXT
{
    CLFS_NODE_ID cidNode;
    ULONGLONG cbContainer;
    CLFS_CONTAINER_ID cidContainer;
    CLFS_CONTAINER_ID cidQueue;
    union
    {
        CClfsContainer* pContainer;    // 指向内核对象的指针，内核对象的首部有虚函数表
        ULONGLONG ullAlignment;
    };
    CLFS_USN usnCurrent;
    CLFS_CONTAINER_STATE eState;
    ULONG cbPrevOffset;
    ULONG cbNextOffset;
} CLFS_CONTAINER_CONTEXT, *PCLFS_CONTAINER_CONTEXT;
```

包含了因为截断操作而需要对扇区进行更改的客户端信息，以及具体更改的扇区字节。

**03****‍**

**Fuzz CLFS**

通过查阅一些paper之后，可以发现，对于CLFS的攻击面主要分为两类：

1. CLFS.sys中日志文件解析相关漏洞

2. CLFS.sys中IoCode处理相关漏洞

知道日志文件格式和日志处理函数之后，我们的fuzz设计就很简单：

1. 创建日志文件

2. 根据文件格式随机数据

3. 调用使clfs.sys对日志文件进行解析

需要注意的是在每次随机文件内容的时候，需要绕过CRC检查，伪代码：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnRO1e64AEPGB2AAcLibZBOrNMevtpRqemTLgFCH7FdiaUlZ5B1DvKDIibPHBE0ygX4ibANHPyLlgt0tlw/640?wx_fmt=png)

在逆向CLFS.sys文件中，我们可以看到一些以Get和Acquire开头的函数会直接从blf文件中读取数据，所以我们在随机数据的时候可以重点关注这些函数即可。

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnRO1e64AEPGB2AAcLibZBOrNXjDwlB0V47UMJOQektYjicuNibic9E85iaNSPeVJsANYicGaCkzlvkgwlFQ/640?wx_fmt=png)

**04****‍**

**漏洞分析**

**CVE-2022-21916**

第一个漏洞出现在CClfsBaseFilePersisted::ShiftMetadataBlockDescriptor函数

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnRO1e64AEPGB2AAcLibZBOrNllwJXhp66MC0stnCD8pGW5TUHdTR4y6uF3QL08nEWh4LhoMcNplic7g/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnRO1e64AEPGB2AAcLibZBOrNRygD16GDfEDXYpPg6fpf61j52OTgdc9VYEoJYgM0V8OfXXPyrq919w/640?wx_fmt=png)

该函数在解析 CLFS\_CONTROL\_RECORD 结构的时候出现了问题，该结构可以在 blf文件偏移 0x70 的位置找到，其中 iFlushBlock存在于 blf文件的 0x8A 处，iExtendBlock存在于文件的 0x88 处，此函数未正确对这两个参数进行检查导致了越界漏洞的产生。到达此函数还需要将 eExtendState字段设置为 2，此字段存在于 blf文件 0x84 的位置。

第二个漏洞出现在CClfsLogFcbPhysical::OverflowRegerral函数，与上一个漏洞类似，该漏洞也是在解析BLF文件格式的时候出现问题，该函数主要与ownerpage操作相关。

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnRO1e64AEPGB2AAcLibZBOrNcyqibia0kSVv3dx3Cj3V4raPEowXPQxxOFQ60rGYVn5baiaWibo4ESe0tQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnRO1e64AEPGB2AAcLibZBOrNfaLINAAvS7Tyrdp2wxYt8aBfjJb0icnSAn1KHG4pjB01ibpBcicuLj2iaQ/640?wx_fmt=png)

CClfsBaseFile::HighWaterMarkClientId 函数负责获取 blf文件中的 ClientId信息，可以通过修改 CLFS\_BASE\_RECORD\_HEADER 结构中的 cNextClient字段从而控制 ClientId，而 cNextClient可以直接从 blf文件中找到并修改。当 cNextClient被修改为其他值的时候，它会被用作错误的索引，从而导致越界漏洞。下图就是我们在文件中找到的 cNextClient。总而而言，此漏洞是一个大小为0x1000的分页池溢出漏洞，他将CLFS\_LSN\_INVALID和OldOwnerPage数据写入下一个池的头部。

Windows分页池溢出的利用方式一般有如下两种：

1. WNF

通过溢出占用\_WNF\_NAME\_INSTANCE结构的StateData指针可以实现有限制的任意地址读写

2. 命名管道

通过溢出占用PipeAttribute结构的Flink指针可以实现任意地址读

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnRO1e64AEPGB2AAcLibZBOrN22RagCHAEXLnGX2qgbq0ukL4zVpMSiczV3m81ej0KsO1Pib33Rbfk7sg/640?wx_fmt=png)

WNF的利用方式限制：当\_WNF\_NAME\_INSTANCE结构的大小为0xC0或者0xD0，而我们的漏洞是一个大小为0x1000的分页池溢出漏洞，我们无法将0xC0或者0xD0大小的分页池分配在0x1000的分页池后面，所以我们无法利用这个漏洞溢出WNF的\_WNF\_NAME\_INSTANCE结构

但是我们可以溢出0x1000大小的\_WNF\_STATE\_DATA结构，通过溢出\_WNF\_STATE\_DATA结构中的AllocateSize字段，我们可以实现最大长度为0x1000的越界写，它只能越界写0x1000大小的\_WNF\_STATE\_DATA结构后的数据，并且刚好只能越界写16字节，所以我们需要找到一个0x1000大小的分页池结构，然后通过修改这个结构的前16字节来实现任意地址写，我们可以在Windows ALPC中找到这个结构。

我们也找到了一种新的通用的Windows分页池溢出的利用方式，通过溢出占用\_ALPC\_HANDLE\_TABLE结构的Handles指针，我们可以实现任意地址的读写。

\_ALPC\_HANDLE\_TABLE的结构如下：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnRO1e64AEPGB2AAcLibZBOrN4ibEUDl0A4j7RHBuFL5nzOBayrkM4kibpAqnnII4gM2dtZ5wyIAvAIjg/640?wx_fmt=png)

这里可以通过NtAlpcCreateResourceReserve函数来创建一个Reserve Blob，会调用AlpcAddHandleTableEntry函数把刚创建好的Reserve Blob的地址写入到\_ALPC\_HANDLE\_TABLE结构的Handles数组中。

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnRO1e64AEPGB2AAcLibZBOrNe2RhOUjNS0lm5eNNRr3StkxAa6oiaFBqukXSicqbzYk3GqqAABs3OXag/640?wx_fmt=png)

当创建ALPC端口时，AlpcInitializeHandleTable函数会被调用来初始化HandleTable结构，Handles是一个初始大小为0x80的数组，他存放着blob结构的地址，当越来越多blob被创建时，Handles的大小成倍增加，所以Handles的大小可以为0x1000.

当溢出占用Handles数组中\_KALPC\_RESERVE结构的指针时，就可以伪造一个虚假的Reserve Blob，因为\_KALPC\_RESERVE中存储着Message的地址，所以可以进一步伪造一个虚假的\_KALPC\_MESSAGE结构。

...
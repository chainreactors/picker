---
title: [原创] UPX源码学习和简单修改
url: https://buaq.net/go-144562.html
source: unSafe.sh - 不安全
date: 2023-01-08
fetch_date: 2025-10-04T03:18:50.327630
---

# [原创] UPX源码学习和简单修改

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/c81fa6bf08a163fd2bcf11aacfe65daf.jpg)

[原创] UPX源码学习和简单修改

[原创] UPX源码学习和简单修改
*2023-1-7 12:18:31
Author: [bbs.pediy.com(查看原文)](/jump-144562.htm)
阅读量:144
收藏*

---

:   [原创] UPX源码学习和简单修改

    5小时前 413

之前一直学习如何脱壳，接触到的第一种壳就是UPX。经过一段脱壳训练后，逐渐对UPX的压缩流程有了兴趣。本文是笔者对UPX源码的学习记录，包括代码学习过程和源码简单修改，希望对大家有所帮助。

> 分析环境：

## 源码分析

为了方便调试，笔者只分析了x86-64位ELF文件的加壳流程代码，本文所用程序见结尾文件 `demo`。代码跟踪过程主要参考文章[UPX源码分析——加壳篇](https://www.cnblogs.com/ichunqiu/p/7245329.html)，大家有兴趣可详细阅读。这里只介绍大体流程。

### 加壳流程

UPX的核心加壳代码是 upx-3.96/src/p\_unix.cpp 文件的 pack 函数。

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43 | `void PackUnix::pack(OutputFile` `*``fo)`  `{`  `Filter` `ft(ph.level);`  `ft.addvalue` `=` `0``;`  `b_len` `=` `0``;`  `progid` `=` `0``;`  `/``/` `set` `options`  `blocksize` `=` `opt``-``>o_unix.blocksize;`  `if` `(blocksize <``=` `0``)`  `blocksize` `=` `BLOCKSIZE;`  `if` `((off_t)blocksize > file_size)`  `blocksize` `=` `file_size;`  `/``/` `init compression buffers`  `ibuf.alloc(blocksize);`  `obuf.allocForCompression(blocksize);`  `fi``-``>seek(``0``, SEEK_SET);`  `pack1(fo, ft);` `/``/` `generate Elf header, etc.`  `p_info hbuf;`  `set_te32(&hbuf.p_progid, progid);`  `set_te32(&hbuf.p_filesize, file_size);`  `set_te32(&hbuf.p_blocksize, blocksize);`  `fo``-``>write(&hbuf, sizeof(hbuf));`  `/``/` `append the compressed body`  `if` `(pack2(fo, ft)) {`  `/``/` `write block end marker (uncompressed size` `0``)`  `b_info hdr; memset(&hdr,` `0``, sizeof(hdr));`  `set_le32(&hdr.sz_cpr, UPX_MAGIC_LE32);`  `fo``-``>write(&hdr, sizeof(hdr));`  `}`  `pack3(fo, ft);` `/``/` `append loader`  `pack4(fo, ft);` `/``/` `append PackHeader` `and` `overlay_offset; update Elf header`  `/``/` `finally` `check the compression ratio`  `if` `(!checkFinalCompressionRatio(fo))`  `throwNotCompressible();`  `}` |

该函数调用了4个关键函数，分别为pack1、pack2、pack3和pack4，代表了加壳的四个步骤。

pack1 函数功能是，写入新文件的elf头，写入程序头表，写入1个初始化的l\_info结构。

pack2 函数功能是，对所有类型为PT\_LOAD的段进行压缩存储。

其中，在对第一个类型为PT\_LOAD的段(该块一般包含原文件的文件头和程序头表)进行压缩时，会将该段分为两个部分分别压缩写入。这两部分为：一、原文件的elf头和程序头表；二、该段数据的其他部分。
例如，demo文件中第一个PT\_LOAD段如下

![](https://bbs.pediy.com/upload/attach/202301/905958_BUM6JGPH9PGVY64.png)

第一段文件偏移为0，大小为0x5F0。从图中可以看到文件头+程序头表的大小为0x270，这就是需要压缩的第一块数据。第二块数据就是文件偏移为0x270，大小为0x380。

pack3 函数的功能是，写入loader，压缩原文件中除PT\_LOAD段之外的其余数据并写入，修正程序头表内容

pack4 函数的功能是，写入PackHeader和overlay\_offset。这里overlay\_offset值为p\_info字段的文件偏移。本demo中为0xf4。

![](https://bbs.pediy.com/upload/attach/202301/905958_A5VCSQKKX68483P.png)

### 文件格式

经过UPX处理后，压缩后的文件格式如下。

new eheader(64 bytes) (文件头)
+ new pheader(56 bytes) \* 3 (程序头表)
+ l\_info(12 bytes)
+ p\_info(12 bytes)
+ b\_info(12 bytes) + compressed block (原程序文件头和程序头表)
+ b\_info(12 bytes) + compressed block (第一个类型为PT\_LOAD的段中除原程序文件头和程序头表的部分)
+ b\_info(12 bytes) + compressed block (第二个类型为PT\_LOAD的段)
+ ......
+ fpad8 (8字节对齐)
+ int(4 bytes) (第一个b\_info的文件偏移)
+ int(4 bytes) (当前位置的文件偏移，也就是之前所有数据总长度)
+ loader (加载器，也就是脱壳代码)
+ b\_info(12 bytes) + compressed block (第一个PT\_LOAD和第二个PT\_LOAD中间的数据)
+ b\_info(12 bytes) + compressed block (第二个PT\_LOAD和第三个PT\_LOAD中间的数据)
+ ......
+ b\_info(12 bytes) + compressed block (最后一个PT\_LOAD到文件末尾之间的数据)
+ 00 00 00 00 55 50 58 21 00 00 00 00 (b\_info)
+ fpad4 (4字节对齐)
+ PackHeader(32 bytes)
+ int(4 bytes) (p\_info的文件偏移)

其中，b\_info、l\_info和p\_info是三个结构体。

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25 | `/``/` `在每个压缩块之前，存放压缩前和压缩后的数据大小`  `struct b_info {` `/``/` `12``-``byte header before each compressed block`  `uint32_t sz_unc;` `/``/` `uncompressed_size`  `uint32_t sz_cpr;` `/``/` `compressed_size`  `unsigned char b_method;` `/``/` `compression algorithm`  `unsigned char b_ftid;` `/``/` `filter` `id`  `unsigned char b_cto8;` `/``/` `filter` `parameter`  `unsigned char b_unused;`  `};`  `/``/` `存放校验数据和``"UPX!"``魔数`  `struct l_info` `/``/` `12``-``byte trailer` `in` `header` `for` `loader (offset` `116``)`  `{`  `uint32_t l_checksum;`  `uint32_t l_magic;`  `uint16_t l_lsize;`  `uint8_t  l_version;`  `uint8_t  l_format;`  `};`  `/``/` `全文只有一个该结构体，存储的是原文件的大小`  `struct p_info` `/``/` `12``-``byte packed program header follows stub loader`  `{`  `uint32_t p_progid;`  `uint32_t p_filesize;`  `uint32_t p_blocksize;`  `};` |

### loader

针对demo文件的loader生成代码在 upx-3.96/src/p\_lx\_elf.cpp 文件的PackLinuxElf64::buildLinuxLoader()函数中，loader中各section的相应顺序由函数PackLinuxElf::addStubEntrySections()确定。

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36 | `void`  `PackLinuxElf::addStubEntrySections(``Filter` `const` `*``)`  `{`  `addLoader(``"ELFMAINX"``, NULL);`  `if` `(hasLoaderSection(``"ELFMAINXu"``)) {`  `/``/` `brk() trouble` `if` `static`  `addLoader(``"ELFMAINXu"``, NULL);`  `}`  `/``/``addLoader(getDecompressorSections(), NULL);`  `addLoader(`  `( M_IS_NRV2E(ph.method) ?` `"NRV_HEAD,NRV2E,NRV_TAIL"`  `: M_IS_NRV2D(ph.method) ?` `"NRV_HEAD,NRV2D,NRV_TAIL"`  `: M_IS_NRV2B(ph.method) ?` `"NRV_HEAD,NRV2B,NRV_TAIL"`  `: M_IS_LZMA(ph.method)  ?` `"LZMA_ELF00,LZMA_DEC20,LZMA_DEC30"`  `: NULL), NULL);`  `if` `(hasLoaderSection(``"CFLUSH"``))`  `addLoader(``"CFLUSH"``);`  `addLoader(``"ELFMAINY,IDENTSTR"``, NULL);`  `if` `(hasLoaderSection(``"ELFMAINZe"``)) {` `/``/` `ppc64 big``-``endian only`  `addLoader(``"ELFMAINZe"``, NULL);`  `}`  `addLoader(``"+40,ELFMAINZ"``, NULL);`  `if` `(hasLoaderSection(``"ANDMAJNZ"``)) {` `/``/` `Android trouble with args to DT_INIT`  `if` `(opt``-``>o_unix.android_shlib) {`  `addLoader(``"ANDMAJNZ"``, NULL);` `/``/` `constant PAGE_SIZE`  `}`  `else` `{`  `addLoader(``"ELFMAJNZ"``, NULL);` `/``/` `PAGE_SIZE` `from` `AT_PAGESZ`  `}`  `addLoader(``"ELFMAKNZ"``, NULL);`  `}`  `if` `(hasLoaderSection(``"ELFMAINZu"``)) {`  `addLoader(``"ELFMAINZu"``, NULL);`  `}`  `addLoader(``"FOLDEXEC"``, NULL);`  `}` |

除了"FOLDEXEC"，其余section的汇编代码在upx-3.96/src/stub/src/amd64-linux.elf-entry.S文件中，编译后的二进制数据在文件upx-3.96/src/stub/amd64-linux.elf-entry.h中。loader直接使用\*.h文件中的二进制数据。

最终，demo文件压缩后loader的结构如下

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9 | `ELFMAINX`  `NRV_HEAD`  `NRV2E`  `NRV_TAIL`  `ELFMAINY`  `IDENTSTR`  `+``40` `(``4``字节对齐)`  `ELFMAINZ`  `FOLDEXEC` |

### FOLDEXEC

FOLDEXEC节存放的是压缩后的数据，源数据是编译后的二进制数据，存放在upx-3.96/src/stub/amd64-linux.elf-fold.h文件中。
编译前的代码分为两部分，一部分是upx-3.96/src/stub/src/amd64-linux.elf-fold.S文件中的汇编代码，一部分是upx-3.96/src/stub/src/amd64-linux.elf-main.c文件中的C代码。该文件核心是upx\_main()函数，此函数返回值为解压后程序(原程序)的入口点.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27 | `/``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*`  `/``/` `upx_main` `-` `called by our entry code`  `/``/`  `/``/` `This function` `is` `optimized` `for` `size.`  `*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``*``/`  `void` `*`  `upx_main(` `/``/` `returns entry address`  `struct b_info const` `*``const bi,` `/``/` `1st` `block header`  `size_t const sz_compressed,` `/``/` `total length`  `Elf64_Ehdr` `*``const ehdr,` `/``/` `temp char[sz_ehdr]` `for` `decompressing`  `Elf64_auxv_t` `*``const av,`  `f_expand` `*``const f_exp,`  `f_unfilter` `*``const f_unf`...
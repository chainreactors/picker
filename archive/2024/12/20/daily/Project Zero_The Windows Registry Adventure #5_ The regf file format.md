---
title: The Windows Registry Adventure #5: The regf file format
url: https://googleprojectzero.blogspot.com/2024/12/the-windows-registry-adventure-5-regf.html
source: Project Zero
date: 2024-12-20
fetch_date: 2025-10-06T19:38:23.487528
---

# The Windows Registry Adventure #5: The regf file format

# [Project Zero](https://googleprojectzero.blogspot.com/)

News and updates from the Project Zero team at Google

## Thursday, December 19, 2024

### The Windows Registry Adventure #5: The regf file format

Posted by Mateusz Jurczyk, Google Project Zero

As previously mentioned in the second installment of the blog post series (["A brief history of the feature"](https://googleprojectzero.blogspot.com/2024/04/the-windows-registry-adventure-2.html)), the binary format used to encode registry hives from Windows NT 3.1 up to the modern Windows 11 is called regf. In a way, it is quite special, because it represents a registry subtree simultaneously on disk and in memory, as opposed to most other common file formats. Documents, images, videos, etc. are generally designed to store data efficiently on disk, and they are subsequently parsed to and from different in-memory representations whenever they are read or written. This seems only natural, as offline storage and RAM come with different constraints and requirements. On disk, it is important that the data is packed as tightly as possible, while in memory, easy and efficient random access is typically prioritized. The regf format aims to bypass the reparsing step – likely to optimize the memory/disk synchronization process – and reconcile the two types of data encodings into a single one that is both relatively compact and easy to operate on at the same time. This explains, for instance, why hives don't natively support compression (but the clients are of course free to store compressed data in the registry). This unique approach comes with its own set of challenges, and has been a contributing factor in a number of historical vulnerabilities.

Throughout the 30 years of the format's existence, Microsoft has never released its official specification. However, the data layout of all of the building blocks making up a hive (file header, bin headers, cell structures) are effectively public through the PDB symbols for the Windows kernel image (ntoskrnl.exe) available on the [Microsoft Symbol Server](https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/microsoft-public-symbols). Furthermore, the Windows Internals book series also includes a section that delves into the specifics of the regf format (named Hive structure). Lastly, forensics experts have long expressed interest in the format for analysis purposes, resulting in the creation of several unofficial specifications based on reverse engineering, experimentation and deduction. These sources have been listed in my earlier [Learning resources](https://googleprojectzero.blogspot.com/2024/06/the-windows-registry-adventure-3.html) blog post; the two most extensive specifications of this kind can be found [here](https://github.com/libyal/libregf/blob/main/documentation/Windows%2520NT%2520Registry%2520File%2520%28REGF%29%2520format.asciidoc) and [here](https://github.com/msuhanov/regf/blob/master/Windows%2520registry%2520file%2520format%2520specification.md). The intent of this post is not to repeat the information compiled in the existing resources, but rather to highlight specific parts of the format that have major relevance to security, or provide some extra context where I found it missing. A deep understanding of the low-level regf format will prove invaluable in grasping many of the higher-level concepts in the registry, as well as the technical details of software bugs discussed in future blog posts.

## The hive structure: header, bins and cells

On the lowest level, data in hives is organized in chunks of 4 KiB (0x1000 bytes), incidentally the size of a standard memory page in the x86 architecture. The first 4 KiB always correspond to the header (also called the base block), followed by one or more bins, each being a multiple of 4 KiB in length. The header specifies general information about the hive (signature, version, etc.), while bins are an abstraction layer designed to enable the fragmentation of hive mappings in virtual memory – more on that later.

Each bin starts with a 32-byte (0x20) header, followed by one or more cells that completely fill the bin. A cell is the smallest unit of data in a hive that has a specific purpose (e.g. describes a key, value, security descriptor, and so on). The data of a cell is preceded by a 32-bit integer specifying its size, which must be a multiple of eight (i.e. its three least significant bits are clear), and is either in the free or allocated state. A free (unused) cell is indicated by a positive size, and an allocated cell is indicated by a negative one. For example, a free cell of 32 bytes has a length marker of 0x00000020, while an active cell of 128 bytes has its size encoded as 0xFFFFFF80. This visibly demonstrates the hybrid on-disk / in-memory nature of the hive format as opposed to other classic formats, which don't intentionally leave large chunks of unused space in the files.

The overall file structure is illustrated in the diagram below:

[![Pictoral representation of the overall file structure](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiQtJm0XNkozXGxjQnB9n1ka9OuxP7lrLSQN1KZF-Zc60Z06dBEz3AAA8aAYnmdrU4imLebCFvF6qXaE0h-uA_iXnuyAisG90JWawSAMPPaToLdXMGeC4FlyGz42FWkf1bPhJmwSez8Ot-DLI29n4jinIXswZ-LQoLyWX7PIKVF5EwkRoAXNUFYIdcCOwo/s1200/image8.png "Pictoral representation of the overall file structure")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiQtJm0XNkozXGxjQnB9n1ka9OuxP7lrLSQN1KZF-Zc60Z06dBEz3AAA8aAYnmdrU4imLebCFvF6qXaE0h-uA_iXnuyAisG90JWawSAMPPaToLdXMGeC4FlyGz42FWkf1bPhJmwSez8Ot-DLI29n4jinIXswZ-LQoLyWX7PIKVF5EwkRoAXNUFYIdcCOwo/s1999/image8.png)

In the Windows kernel, internal functions responsible for handling these low-level hive objects (base block, bins, cells) have names starting with "Hv", for example HvCheckHive, HvpAllocateBin or HvpViewMapCleanup. This part of the registry codebase is crucial as it forms the foundation of the registry logic, enabling the Configuration Manager to easily allocate, free, and access hive cells without concerning itself with the technical details of memory management. It is also a place with significant potential for optimizations, such as the incremental logging added in Windows 8.1, or section-based registry introduced in Windows 10 April 2018 Update (RS4). Both of these mechanisms are well described in the Windows Internals 7 (Part 2) book.

While integral to the correct functioning of the registry, hive management does not constitute a very large part of the overall registry-related codebase. In my analysis of the registry code growth shown in blog post #2, I counted 100,007 decompiled lines of code corresponding to this subsystem in Windows 11 kernel build 10.0.22621.2134. Out of these, only 10,407 or around 10.4% correspond to hive memory management. This is also reflected in my findings: out of the 52 CVEs assigned by Microsoft, only two of them were directly related to a Hv\* function implementation – [CVE-2022-37988](https://project-zero.issues.chromium.org/issues/42451463), a logic bug in HvReallocateCell leading to memory corruption, and [CVE-2024-43452](https://project-zero.issues.chromium.org/issues/42451731), a double-fetch while loading hives from remote network shares. This is not to say that there aren't more bugs in this mechanism, but their quantity is likely proportional to its size relative to the rest of the registry-related code.

Let's now have a closer look at how each of the basic objects in the hive are encoded and what information they store, starting with the base block.

### Base block

The base block is represented by a structure called \_HBASE\_BLOCK in the Windows Kernel, and its layout can be displayed in WinDbg:

0: kd> dt \_HBASE\_BLOCK

nt!\_HBASE\_BLOCK

   +0x000 Signature        : Uint4B

   +0x004 Sequence1        : Uint4B

   +0x008 Sequence2        : Uint4B

   +0x00c TimeStamp        : \_LARGE\_INTEGER

   +0x014 Major            : Uint4B

   +0x018 Minor            :...
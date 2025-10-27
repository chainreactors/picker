---
title: The Windows Registry Adventure #6: Kernel-mode objects
url: https://googleprojectzero.blogspot.com/2025/04/the-windows-registry-adventure-6-kernel.html
source: Project Zero
date: 2025-04-17
fetch_date: 2025-10-06T22:05:51.914683
---

# The Windows Registry Adventure #6: Kernel-mode objects

# [Project Zero](https://googleprojectzero.blogspot.com/)

News and updates from the Project Zero team at Google

## Wednesday, April 16, 2025

### The Windows Registry Adventure #6: Kernel-mode objects

Posted by Mateusz Jurczyk, Google Project Zero

Welcome back to the Windows Registry Adventure! In the [previous installment](https://googleprojectzero.blogspot.com/2024/12/the-windows-registry-adventure-5-regf.html) of the series, we took a deep look into the internals of the regf hive format. Understanding this foundational aspect of the registry is crucial, as it illuminates the design principles behind the mechanism, as well as its inherent strengths and weaknesses. The data stored within the regf file represents the definitive state of the hive. Knowing how to parse this data is sufficient for handling static files encoded in this format, such as when writing a custom regf parser to inspect hives extracted from a hard drive. However, for those interested in how regf files are managed by Windows at runtime, rather than just their behavior in isolation, there's a whole other dimension to explore: the multitude of kernel-mode objects allocated and maintained throughout the lifecycle of an active hive. These auxiliary objects are essential for several reasons:

* To track all currently loaded hives, their properties (e.g., load flags), their memory mappings, and the relationships between them (especially for delta hives overlaid on top of each other).
* To synchronize access to keys and hives within the multithreaded Windows environment.
* To cache hive information for faster access compared to direct memory mapping lookups.
* To integrate the registry with the NT Object Manager and support standard operations (opening/closing handles, setting/querying security descriptors, enforcing access checks, etc.).
* To manage the state of pending transactions before they are fully committed to the underlying hive.

To address these diverse requirements, the Windows kernel employs numerous interconnected structures. In this post, we will examine some of the most critical ones, how they function, and how they can be effectively enumerated and inspected using WinDbg. It's important to note that Microsoft provides official definitions only for some registry-related structures through PDB symbols for ntoskrnl.exe. In many cases, I had to reverse-engineer the relevant code to recover structure layouts, as well as infer the types and names of particular fields and enums. Throughout this write-up, I will clearly indicate whether each structure definition is official or reverse-engineered. If you spot any inaccuracies, please let me know. The definitions presented here are primarily derived from Windows Server 2019 with the March 2022 patches (kernel build 10.0.17763.2686), which was the kernel version used for the majority of my registry code analysis. However, over 99% of registry structure definitions appear to be identical between this version and the latest Windows 11, making the information directly applicable to the latest systems as well.

## Hive structures

Given that hives are the most intricate type of registry object, it's not surprising that their kernel-mode descriptors are equally complex and lengthy. The primary hive descriptor structure in Windows, known as \_CMHIVE, spans a substantial 0x12F8 bytes – exceeding 4 KiB, the standard memory page size on x86-family architectures. Contained within \_CMHIVE, at offset 0, is another structure of type \_HHIVE, which occupies 0x600 bytes, as depicted in the diagram below:

[![Diagram depicting the layout of the Windows Registry kernel structure _CMHIVE. It shows the overall _CMHIVE block, marked with a total size of 0x12F8 bytes. Within this block, the first part, from offset 0x0 to 0x600, is labeled as the _HHIVE structure. The remaining portion, from offset 0x600 to 0x12F8, is labeled "Rest of _CMHIVE".](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhIE8uHd2DJ-gPQVj9KpjdpoVP-aLCdRXjAU0lIpKprgSI3KpFkoomVyU2PvhTA3zp_8ha28xuZUoXTTKKJjyevXRUf2NQ_NaJlHMoPx91KfE6UBsoyKl-VnRbA73_AjPxTf4ZXasUNMAwMKh3kc9VTWczg0ua_9ltU9G1BK7I4xEIHpJ9ubrxah9Jds5U/s1200/image1.png "Diagram depicting the layout of the Windows Registry kernel structure _CMHIVE. It shows the overall _CMHIVE block, marked with a total size of 0x12F8 bytes. Within this block, the first part, from offset 0x0 to 0x600, is labeled as the _HHIVE structure. The remaining portion, from offset 0x600 to 0x12F8, is labeled \"Rest of _CMHIVE\".")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhIE8uHd2DJ-gPQVj9KpjdpoVP-aLCdRXjAU0lIpKprgSI3KpFkoomVyU2PvhTA3zp_8ha28xuZUoXTTKKJjyevXRUf2NQ_NaJlHMoPx91KfE6UBsoyKl-VnRbA73_AjPxTf4ZXasUNMAwMKh3kc9VTWczg0ua_9ltU9G1BK7I4xEIHpJ9ubrxah9Jds5U/s1200/image1.png)

This relationship mirrors that of other common Windows object pairs, such as \_EPROCESS / \_KPROCESS and \_ETHREAD / \_KTHREAD. Because \_HHIVE is always allocated as a component of the larger \_CMHIVE structure, their pointer types are effectively interchangeable. If you encounter a decompiled access using a \_HHIVE\* pointer that extends beyond the size of the structure, it almost certainly indicates a reference to a field within the encompassing \_CMHIVE object.

But why are two distinct structures dedicated to representing a single registry hive? While technically not required, this separation likely serves to delineate fields associated with different abstraction layers of the hive. Specifically:

* \_HHIVE manages the low-level aspects of the hive, including the hive header, bins, and cells, as well as in-memory mappings and synchronization state with its on-disk counterpart (e.g., dirty sectors).
* \_CMHIVE handles more abstract information about the hive, such as the cache of security descriptors, pointers to high-level kernel objects like the root Key Control Block (KCB), and the associated transaction resource manager (\_CM\_RM structure).

The next subsections will provide a deeper look into the responsibilities and inner workings of these two structures.

### \_HHIVE structure overview

The primary role of the \_HHIVE structure is to manage the memory-related state of a hive. This allows higher-level registry code to perform operations such as allocating, freeing, and marking cells as "dirty" without needing to handle the low-level implementation details. The \_HHIVE structure comprises 49 top-level members, most of which will be described in larger groups below:

0: kd> dt \_HHIVE

nt!\_HHIVE

   +0x000 Signature        : Uint4B

   +0x008 GetCellRoutine   : Ptr64     \_CELL\_DATA\*

   +0x010 ReleaseCellRoutine : Ptr64     void

   +0x018 Allocate         : Ptr64     void\*

   +0x020 Free             : Ptr64     void

   +0x028 FileWrite        : Ptr64     long

   +0x030 FileRead         : Ptr64     long

   +0x038 HiveLoadFailure  : Ptr64 Void

   +0x040 BaseBlock        : Ptr64 \_HBASE\_BLOCK

   +0x048 FlusherLock      : \_CMSI\_RW\_LOCK

   +0x050 WriterLock       : \_CMSI\_RW\_LOCK

   +0x058 DirtyVector      : \_RTL\_BITMAP

   +0x068 DirtyCount       : Uint4B

   +0x06c DirtyAlloc       : Uint4B

   +0x070 UnreconciledVector : \_RTL\_BITMAP

   +0x080 UnreconciledCount : Uint4B

   +0x084 BaseBlockAlloc   : Uint4B

   +0x088 Cluster          : Uint4B

   +0x08c Flat             : Pos 0, 1 Bit

   +0x08c ReadOnly         : Pos 1, 1 Bit

   +0x08c Reserved         : Pos 2, 6 Bits

   +0x08d DirtyFlag        : UChar

   +0x090 HvBinHeadersUse  : Uint4B

   +0x094 HvFreeCellsUse   : Uint4B

   +0x098 HvUsedCellsUse   : Uint4B

   +0x09c CmUsedCellsUse   : Uint4B

   +0x0a0 HiveFlags        : Uint4B

   +0x0a4 CurrentLog       : Uint4B

   +0x0a8 CurrentLogSequence : Uint4B

   +0x0ac CurrentLogMinimumSequence : Uint4B

   +0x0b0 CurrentLogOffset : Uint4B

   +0x0b4 MinimumLogSequence : Uint4B

   +0x0b8 LogFileSizeCap   : Uint4B

   +0x0bc LogDataPresent   : [2] UChar

   +0x0be PrimaryFileValid : UChar

   +0x0bf BaseBlockDir...
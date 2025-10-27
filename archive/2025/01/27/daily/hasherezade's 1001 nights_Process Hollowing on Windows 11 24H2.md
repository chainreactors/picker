---
title: Process Hollowing on Windows 11 24H2
url: https://hshrzd.wordpress.com/2025/01/27/process-hollowing-on-windows-11-24h2/
source: hasherezade's 1001 nights
date: 2025-01-27
fetch_date: 2025-10-06T20:08:08.508078
---

# Process Hollowing on Windows 11 24H2

[hasherezade's 1001 nights](https://hshrzd.wordpress.com/ "hasherezade's 1001 nights")

projects and tasks that I do in my free time

[![](https://hshrzd.wordpress.com/wp-content/uploads/2025/01/screen-full-of-1s-and-0s-and-a-cute-ghost-4.png?w=940&h=198&crop=1)](https://hshrzd.wordpress.com/ "hasherezade's 1001 nights")

[Skip to content](#content "Skip to content")

* [Home](https://hshrzd.wordpress.com)
* [Projects](https://hshrzd.wordpress.com/mycode/)
  + [PE-sieve](https://hshrzd.wordpress.com/pe-sieve/)
  + [PE\_unmapper](https://hshrzd.wordpress.com/pe_unmapper/)
  + [IAT Patcher](https://hshrzd.wordpress.com/iat-patcher/)
  + [PE-bear](https://hshrzd.wordpress.com/pe-bear/)
  + [ViDi](https://hshrzd.wordpress.com/vidi-visual-disassembler/)
  + [DMA Unlocker](https://hshrzd.wordpress.com/mycode/dma-unlocker/)
* [How to start RE/malware analysis?](https://hshrzd.wordpress.com/how-to-start/)

[← Flare-On 11 – Task 7](https://hshrzd.wordpress.com/2024/12/09/flare-on-11-task-7/)

[Tutorial: unpacking executables with TinyTracer + PE-sieve →](https://hshrzd.wordpress.com/2025/03/22/unpacking-executables-with-tinytracer-pe-sieve/)

## [Process Hollowing on Windows 11 24H2](https://hshrzd.wordpress.com/2025/01/27/process-hollowing-on-windows-11-24h2/)

Posted on [January 27, 2025](https://hshrzd.wordpress.com/2025/01/27/process-hollowing-on-windows-11-24h2/ "12:16 am") by [hasherezade](https://hshrzd.wordpress.com/author/hshrzd/ "View all posts by hasherezade")

[Process Hollowing (a.k.a. RunPE)](https://attack.mitre.org/techniques/T1055/012/) is probably the oldest, and the most popular process impersonation technique (it allows to run a malicious executable under the cover of a benign process). It is used in variety of PE loaders, PoCs, and offensive tooling. It was also used in one of the demos involving my library, [libPEconv](https://github.com/hasherezade/libpeconv). Recently I’ve got a [github issue from a user complaining that the demo no longer works on the latest Windows 11, 24H2](https://github.com/hasherezade/libpeconv/issues/59) . This [Windows release was published **October 1, 2024**](https://en.wikipedia.org/wiki/Windows_11%2C_version_24H2), so it is still fresh, but slowly gaining popularity. Searching for the solution I found out, that many people encountered the same problem with different implementations of RunPE, and it is a problem with the technique itself. Still, the answers that I found were not really reaching the root of the problem, so I decided to investigate it deeper. In this short blog I describe my findings, in hopes that it will help other people who experienced the same issue.

## The observed error: 0xc0000141

After the PE was implanted into the newly created, suspended process, we resume the process, and the implant is supposed to load, using the typical Windows loader mechanism. However, when we resume the 64-bit process on Windows 11 24H2, the loading will get interrupted with an error: 0xC0000141.

![](https://hshrzd.wordpress.com/wp-content/uploads/2025/01/run_pe_fai.jpeg?w=606)

## The root cause

This problem comes from changes that were implemented in the Windows loader.

The implementation of Run PE involves loading the payload into the newly allocated memory. Depending on the variant of the technique, it may be implemented in two ways:

* unmapping the original PE, allocating memory at exactly the same address, and writing the implant there
* allocating a new memory region, writing the implant there, then setting the new region as a base address of the main module in the PEB structure

In both cases, the new PE is stored in the private memory (MEM\_PRIVATE), unlike the normally mapped PE, which would be stored as image (MEM\_IMAGE). This is going to make a big difference further on.

Windows 11 24H2 added a native support for Hotpatching (see the details [here](https://ynwarcs.github.io/Win11-24H2-CFG)). It caused some changes at process initialization, such as, a new function, `RtlpInsertOrRemoveScpCfgFunctionTable` has been added ([see under “extras”](https://ynwarcs.github.io/Win11-24H2-CFG)). The subsequent functions are called:

LdrpInitializeProcess -> LdrpProcessMappedModule -> RtlpInsertOrRemoveScpCfgFunctionTable -> ZwQueryVirtualMemory

The function `ZwQueryVirtualMemory` is meant to retrieve the properties of each module in memory. It is called with the new argument [`MemoryImageExtensionInformation`](https://ntdoc.m417z.com/memory_information_class) that can be used only on images (MEM\_IMAGE). Since the implanted PE is not an image, but MEM\_PRIVATE, the function fails will the error (STATUS\_INVALID\_ADDRESS).

This further causes the loading to terminate with the observed error.

## The solution

There are two approaches with which we can solve this problem:

1. Use alternative technique, that stores the implant as MEM\_IMAGE, instead of MEM\_PRIVATE
2. Patch the NTDLL to bypass the check

### Alternative techniques

While RunPE is still the most known and popular process impersonation technique, in the meantime, multiple alternatives evolved, using which we can map our implant as MEM\_IMAGE rather than MEM\_PRIVATE.

There is a group of techniques that create a section first (using `NtCreateSection`), and then create the process from the section, using the native API `NtCreateProcessEx`. This group contains the following techniques:

* [Process Doppelganging](https://www.youtube.com/watch?v=Cch8dvp836w) ([PoC](https://github.com/hasherezade/process_doppelganging?tab=readme-ov-file))
* [Process Ghosting](https://www.elastic.co/blog/process-ghosting-a-new-executable-image-tampering-attack) ([PoC](https://github.com/hasherezade/process_ghosting))
* Process Herpaderping ([PoC](https://github.com/jxy-s/herpaderping))

However, this group of techniques is not as convenient to use as the classic RunPE. It involves filling a lot of structures manually. Another problem is, the process will distinguish itself from the normally created one, since it is created from an unnamed module (`GetProcessImageFileName` returns an empty string). This does not happen in case of RunPE. So, although they are a nice addition to the arsenal of techniques, they don’t make a perfect replacement of the classic.

With time more options for process impersonation appeared. Process Doppelganging and Process Ghosting inspired hybrid techniques, that are closer in their implementation to the Process Hollowing, yet, contain the major improvement of using the PE mapped as MEM\_IMAGE. Those hybrids are:

* [Transacted Hollowing](https://www.malwarebytes.com/blog/news/2018/08/process-doppelganging-meets-process-hollowing_osiris) ([PoC](https://github.com/hasherezade/transacted_hollowing))
* Ghostly Hollowing ([PoC](https://github.com/hasherezade/transacted_hollowing))
* Herpaderply Hollowing ([PoC](https://github.com/Hagrid29/herpaderply_hollowing))

In case of those techniques, `GetProcessImageFileName` returns the target’s path, and the process resembles more the one that is loaded normally. The payload is mapped as unnamed MEM\_IMAGE.

Later, I came up with one more variant of the loader, that would map the payload as named MEM\_IMAGE, making it yet more similar to a legitimately loaded PE. Details of the implementation, and comparison to other techniques, can be found in the repository:

* Process Overwriting [[PoC](https://github.com/hasherezade/process_overwriting)], [[FAQ](https://github.com/hasherezade/process_overwriting/wiki)]

According to my latest tests, Transacted/Ghostly Hollowing, as well as Process Overwriting, successfully loaded PEs on Windows 11 24H2, without the need of any additional changes or patches.

Demo (Process Overwriting on Windows 11 24H2):

### Patching NTDLL

If, for whatever reason, we insist to use the original RunPE, and run our payload from MEM\_PRIVATE, it is still possible to achieve it. However, it will require patching of the function that causes the error (`ZwQueryVirtualMemory`). O...
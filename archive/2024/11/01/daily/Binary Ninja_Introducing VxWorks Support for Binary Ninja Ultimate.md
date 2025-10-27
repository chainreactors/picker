---
title: Introducing VxWorks Support for Binary Ninja Ultimate
url: https://binary.ninja/2024/10/31/introducing-vxworks.html
source: Binary Ninja
date: 2024-11-01
fetch_date: 2025-10-06T19:16:28.602574
---

# Introducing VxWorks Support for Binary Ninja Ultimate

[![](/images/binary-ninja-logo.svg)](/)

* [Features](/features/)
* [Enterprise](/enterprise/)
* [Sidekick](https://sidekick.binary.ninja)
* [Cloud](https://cloud.binary.ninja)
* [Training](/training/)
* [Support](/support/)

  [Extended Support](/support/extended.html)
  [Documentation](/support/#documentation)
  [License/Installer Recovery](/recover/)
  [Renew Current License](/renew/)
  [Slack Signup](https://slack.binary.ninja/)
  [FAQ](/faq/)
  [Sponsorship Information](/sponsorship/)
  [Portal](https://portal.binary.ninja/)
  [Contact Us](/support/)
* [Blog](/blog/)
* [Gear](https://shop.binary.ninja)

[Free](/free)
[Purchase](/purchase)

Participate in our [Reverse Engineering Survey](/survey/) to win free licenses or admission to [RE//verse](https://re-verse.io/)!

# Binary Ninja Blog

## Introducing VxWorks Support for Binary Ninja Ultimate

* [Brandon Miller](https://github.com/zznop)
* 2024-10-31
* [reversing](/tag/reversing), [vxworks](/tag/vxworks)

[VxWorks](https://www.windriver.com/products/vxworks) is a widely deployed real-time operating system (RTOS). It is used in a wide range of applications, including
networking, aerospace, and industrial control systems. VxWorks is known for its reliability, performance, and
scalability, making it a popular choice for embedded mission-critical systems.

We are excited to announce support for VxWorks in version 4.2 of Binary Ninja Ultimate! This post provides an
introduction to VxWorks and explains how Binary Ninja can be used to reverse engineer VxWorks images.

## VxWorks Overview

VxWorks is a real-time operating system developed by Wind River Systems. It provides a wide range of features, including
a real-time monolithic kernel, a file system, networking support, and a variety of development tools. VxWorks is highly
customizable and can be tailored to meet the specific requirements of different applications. VxWorks is typically used
in embedded systems that require real-time performance and reliability. These systems often have strict requirements
for response time, determinism, and fault tolerance.

VxWorks images typically consist of a kernel, device drivers, and application code. Depending on the VxWorks version
and build configuration, device drivers and application code may be statically linked into the kernel image or loaded
dynamically at runtime. VxWorks images are typically stored in a proprietary format that includes a header, a symbol
table, and the kernel image itself. The symbol table provides information about the kernelâs functions and data
variables. This information is extremely useful for reverse engineering VxWorks images.

## VxWorks BinaryView

Binary Ninja 4.2 Ultimate Edition includes a new BinaryView for loading VxWorks images into Binary Ninja. The VxWorks
BinaryView supports loading of most VxWorks 5.x and 6.x kernel images. The VxWorks BinaryView uses heuristic analysis to
locate and parse the VxWorks symbol table. By locating the symbol table, the VxWorks BinaryView is able to determine
the base address of the kernel image, determine code and data sections, and apply symbol names to functions and data
variables.

![VxWorks BinaryView](/blog/images/vxworks/title-image.png)

### Scanning for the VxWorks Symbol Table

The VxWorks BinaryView uses a heuristic algorithm to locate the VxWorks symbol table. It scans backwards, starting at the
end of the raw VxWorks image. The VxWorks symbol table consists of symbol entries. The structure of the symbol entries
varies slightly between VxWorks 5.x and 6.x. The VxWorks BinaryView is only concerned with (3) members of the symbol
entry structure: the pointer to the symbol name, the pointer to the symbol location (function, data variable, etc.),
and the flags. When scanning for the symbol table, the VxWorks BinaryView looks for a sequence of symbol entries that
match the expected structure. The VxWorks BinaryView treats a data structure as a potential symbol table entry if it
meets the following criteria:

* The pointer to the symbol name is non-null
* The flags value is within the hashmap of known flag values for VxWorks 5.x or 6.x

VxWorks can run on a variety of architectures, including x86, ARM, PowerPC, and MIPS. MIPS and PowerPC are big-endian
architectures, while x86 and ARM are little-endian. When scanning for the symbol table, the VxWorks BinaryView must
take into consideration that pointers within the symbol entry structure may be in big-endian or little-endian format.
VxWorks images are typically raw binary files. There is no metadata, such as an ELF or PE header, to indicate the
endianess of the image. The VxWorks BinaryView uses a heuristic algorithm to verify that the pointers within the
collected symbol entries are valid. This algorithm ensures that the least significant byte of the pointers vary across
function symbol entries. If the symbol entries do not meet this criteria, the VxWorks BinaryView continues to scan
for the symbol table.

The VxWorks BinaryView will continue to scan for the symbol table until it reaches the start of the kernel image or
32 MiB from the end of the image, or it has collected atleast 1000 contiguous symbol entries that meet the expected
criteria.

### Identifying the Image Base Address

Once the VxWorks BinaryView has located the symbol table, it determines the base address of the image using
the symbol entry for the `sysInit` function. The `sysInit` function is the entry point for the VxWorks kernel. There
are many VxWorks images in which the `sysInit` function has been renamed. If there are no symbol entries with a name of
`sysInit` or `_sysInit`, the VxWorks BinaryView identifies the base address by searching for the lowest address of the
symbols containing a `GlobalTextSymbolType` (`0x5`) flag value. The text symbol with the lowest address is assumed to
be the entry point for the kernel.

### Identifying Sections

The VxWorks BinaryView identifies code and data sections by analyzing the symbol entries. Function symbols are assigned
to the `.text` section, data symbols are assigned to the `.data` section, and external symbols are assigned to
the `.extern` section. A special section is created for the symbol table, named `.symtab`. The start and end address of
each section is determined by the address of the first and last symbol in the section.

### Applying Names and Types

After the VxWorks BinaryView has identified the base address and has created sections from symbol entries, it iterates
through the symbol entries and applies names to functions and data variables. LLVM and GNU mangled symbol names are
demangled to provide a more readable representation. The VxWorks BinaryView also applies types to functions and data
variables that are included in the bundled VxWorks platform types, also released in version 4.2 of Binary Ninja
Ultimate. Binary Ninja bundles hundreds of types for VxWorks kernel functions and data structures. These types
contribute to more accurate analysis and decompilation of VxWorks images. The screenshots below show the difference
in decompilation between a VxWorks image loaded with the Mapped BinaryView and no type information and the same image
loaded with the VxWorks BinaryView and platform types applied.

![](/blog/images/vxworks/after-types.png)
![](/blog/images/vxworks/before-types.png)

### Limitations

The VxWorks BinaryView is designed to work with VxWorks 5.x and 6.x kernel images containing a VxWorks symbol table.
Some VxWorks images might not contain a symbol table, or the symbol table could be in a custom format. In these cases, the
VxWorks BinaryView will not be able to load the image. If the VxWorks BinaryView is unable to locate the symbol table,
the image will be loaded with the Mapped BinaryView, like any other raw binary file. The Mapped BinaryView allows users
to set the base address and select a VxWorks platform manually. It will load the image and platform types, but is unable
to apply symbol names or types to functions and data vari...
---
title: Shellcode: Windows on ARM64 / AArch64
url: https://modexp.wordpress.com/2024/09/16/windows_arm64/
source: modexp
date: 2024-09-17
fetch_date: 2025-10-06T18:24:49.510242
---

# Shellcode: Windows on ARM64 / AArch64

[modexp](https://modexp.wordpress.com/ "modexp")

Random posts about computer security

[![](https://modexp.wordpress.com/wp-content/uploads/2022/10/arm64_hash.png?w=940&h=198&crop=1)](https://modexp.wordpress.com/ "modexp")

[Skip to content](#content "Skip to content")

* [Home](https://modexp.wordpress.com/)
* [About](https://modexp.wordpress.com/about/)

[← Delegated NT DLL](https://modexp.wordpress.com/2024/02/13/delegated-nt-dll/)

## [Shellcode: Windows on ARM64 / AArch64](https://modexp.wordpress.com/2024/09/16/windows_arm64/)

Posted on [September 16, 2024](https://modexp.wordpress.com/2024/09/16/windows_arm64/ "2:32 pm") by [odzhan](https://modexp.wordpress.com/author/odzhan/ "View all posts by odzhan")

## Introduction

Back in October 2018, I wanted to write ARM assembly on Windows. All I could acquire then was a Surface tablet running [Windows RT](https://en.wikipedia.org/wiki/Windows_RT) that was released sometime in October 2012. Windows RT (now deprecated) was a version of Windows 8 designed to run on the 32-Bit ARMv7 architecture. By the summer of 2013, it was considered to be a [commercial flop](https://www.pcworld.com/article/452173/microsoft-offers-free-touch-or-type-covers-with-surface-rt-tablet-purchase.html).

For developers, it was possible to compile binaries on a separate machine and get them running on the tablet via USB stick or network, but unless you wanted to obtain a developer license, a [jailbreak exploit](https://www.theregister.com/2013/01/07/windows_rt_security_hacked/) was required. Since there were too many limitations, my attention shifted towards Linux on a Raspberry Pi4.

From what I read, the release of Windows 10 for ARMv7 in 2015 was a distinct improvement over Windows RT. Limitations for developers persisted but at least Microsoft provided support for emulating x86 applications.

Today, I finally have an ARM64 device running Windows 11 without all the problems that plagued previous versions. There’s full native support for developers with [Visual Studio 2022](https://devblogs.microsoft.com/visualstudio/arm64-visual-studio-is-officially-here/) and a Linux subsystem that can run Ubuntu or Debian if you want to program ARM64 applications for Linux. (I know WSL isn’t new, but still). Best of all perhaps is the ability to emulate both 32-bit and 64-bit applications for the x86 architecture.

## Toolchain

To support Windows on ARM, you have at least three options:

* [Visual Studio 2022](https://visualstudio.microsoft.com/vs/)
* [LLVM-MinGW](https://github.com/mstorsjo/llvm-mingw)
* [flat assembler g](https://github.com/tgrysztar/fasmg)

MSVC and LLVM-MinGW are best for C/C++. And I prefer the GNU Assembler (as) over the [ARM Macro Assembler](https://learn.microsoft.com/en-us/cpp/assembler/arm/arm-assembler-command-line-reference) (armasm64) shipped by Microsoft, but the main problem with both is the lack of support for macros. armasm64 supports most of the directives documented by ARM, but appears to have limitations.

From what I can tell, ARMASM has no support for structures making it very difficult to write programs in assembly. This is also a problem with the GNU Assembler and the only way around it is to use symbolic names with the hardcoded offset of each field.

There is some hope. Despite having no direct support for the ARM architecture, [flat assembler g](https://flatassembler.net/docs.php?article=fasmg) (FASMG) by [Tomasz Grysztar](https://x.com/grysztar) is an **adaptable assembly engine** that *“has the ability to become an assembler for any CPU architecture.”*. There are [include files](https://board.flatassembler.net/topic.php?t=20097) for fasmg which implement [ARM64 instructions](https://github.com/lantonov/asmFish/tree/master/arm/include/instructions) using macros and it’s what I decided to use for a simple PoC in this post.

Once you setup FASMG, copy the [AARCH64 macros from asmFish](https://github.com/lantonov/asmFish/tree/master/arm/include/instructions) to the include directory. My own batch file that I execute from a command prompt inside the root directory of fasm looks like this:

```
@echo off
set include=C:\fasmw\fasmg\packages\utility;C:\fasmw\fasmg\packages\x86\include
set path=%PATH%;C:\fasmw\fasmg\core
```

Thomas has also provided [an ARM64 example](https://board.flatassembler.net/topic.php?t=22444) to get started.

## Calling Convention

Windows uses the same as what’s used on Linux for subroutines. However, invocation of system calls are different: Linux uses x8 to hold system call ID whereas Windows embeds the ID in the SVC instruction.

| Register | Volatile? | Role |
| --- | --- | --- |
| x0 | Yes | Parameter/scratch register 1, result register |
| x1-x7 | Yes | Parameter/scratch register 2-8 |
| x8-x15 | Yes | Scratch registers. Used as parameter too. |
| x16-x17 | Yes | Intra-procedure-call scratch registers |
| x18 | No | Platform register: in kernel mode, points to KPCR for the current processor; in user mode, points to TEB |
| x19-x28 | No | Scratch register |
| x29/fp | No | Frame pointer |
| x30/lr | No | Link register |
| x31/zxr | No | Zero register |

## Hello, World! (Console)

Initially, I started working with ARMASM, so the following is just an example of how to create a simple console application.

```
    ; armasm64 hello.asm -ohello.obj
    ; cl hello.obj /link /subsystem:console /entry:start kernel32.lib

    AREA    .drectve, DRECTVE

    ; invoke API without repeating the same instructions
    ; p1 should be the number of register available to load address of API
    MACRO
        INVOKE $p1, $p2          ; name of macro followed by number of parameters
        adrp   $p1, __imp_$p2
        ldr    $p1, [$p1, __imp_$p2]
        blr    $p1
    MEND

    ; saves time typing "__imp_" for each API imported
    MACRO
        IMPORT_API $p1
        IMPORT __imp_$p1
    MEND

    AREA    data, DATA

Text    DCB "Hello, World!\n"

; symbolic constants for clarity
NULL equ 0
STD_OUTPUT_HANDLE equ -11

    ; the entrypoint
    EXPORT start

    ; the API used
    IMPORT_API ExitProcess
    IMPORT_API WriteFile
    IMPORT_API GetStdHandle

    ; start of code to execute
    AREA    text, CODE
start   PROC
    mov         x0, STD_OUTPUT_HANDLE
    INVOKE      x1, GetStdHandle

    mov         x4, NULL
    mov         x3, NULL
    mov         x2, 14     ; string length...
    adr         x1,Text
    INVOKE      x5, WriteFile

    mov         x0, NULL
    INVOKE      x1, ExitProcess

    ENDP
    END
```

And a simple GUI. A version for FASMG can be [found here](https://board.flatassembler.net/topic.php?t=22444).

## Hello, World! (GUI)

```
    ; armasm64 msgbox.asm -omsgbox.obj
    ; cl msgbox.obj /link /subsystem:windows /entry:start kernel32.lib user32.lib

    AREA    .drectve, DRECTVE

    ; invoke API without repeating the same instructions
    ; p1 should be the free register available to load address of API
    MACRO
        INVOKE $p1, $p2
        adrp   $p1, __imp_$p2
        ldr    $p1, [$p1, __imp_$p2]
        blr    $p1
    MEND

    ; saves time typing "__imp_" for each API imported
    MACRO
        IMPORT_API $p1
        IMPORT __imp_$p1
    MEND

    AREA    data, DATA

Text    DCB "Hello, World!", 0x0
Caption DCB "Hello from ARM64", 0x0

; symbolic names for clarity
NULL equ 0

    ; the entrypoint
    EXPORT start

    ; the API used
    IMPORT_API ExitProcess
    IMPORT_API MessageBoxA

    ; start of code to execute
    AREA    text, CODE
start   PROC
    mov         x3,NULL
    adr         x2,Caption
    adr         x1,Text
    mov         x0,NULL
    INVOKE      x4, MessageBoxA

    mov         x0, NULL
    INVOKE      x1, ExitProcess

    ENDP
    END
```

## Symbolic Names

```
; The following are 64-Bit offsets.
TEB_ProcessEnvironmentBlock                  = 0x00000060
TEB_LastErrorValue                           = 0x00000068

PEB_Ldr                                      = 0x00000018
PEB_LDR_DATA_InLoadOrderModuleList           = 0x00000010...
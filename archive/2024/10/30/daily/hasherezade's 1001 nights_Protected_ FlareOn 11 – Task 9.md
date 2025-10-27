---
title: Protected: FlareOn 11 – Task 9
url: https://hshrzd.wordpress.com/2024/10/29/flareon-11-task-9/
source: hasherezade's 1001 nights
date: 2024-10-30
fetch_date: 2025-10-06T18:51:53.232144
---

# Protected: FlareOn 11 – Task 9

[hasherezade's 1001 nights](https://hshrzd.wordpress.com/ "hasherezade's 1001 nights")

projects and tasks that I do in my free time

[![](https://hshrzd.wordpress.com/wp-content/uploads/2024/10/snake-emerging-from-assembly-code-serpentine-5.png?w=940&h=198&crop=1)](https://hshrzd.wordpress.com/ "hasherezade's 1001 nights")

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

[← Flare-On 11 – Task 10](https://hshrzd.wordpress.com/2024/10/27/flare-on-11-task-10/)

[Flare-On 11 – Task 5 →](https://hshrzd.wordpress.com/2024/12/08/flare-on-11-task-5/)

## [Flare-On 11 – Task 9](https://hshrzd.wordpress.com/2024/10/29/flareon-11-task-9/)

Posted on [October 29, 2024](https://hshrzd.wordpress.com/2024/10/29/flareon-11-task-9/ "12:24 pm") by [hasherezade](https://hshrzd.wordpress.com/author/hshrzd/ "View all posts by hasherezade")

*[Flare-On](https://flare-on.com/) is an annual CTF run by [Mandiant Flare Team](https://cloud.google.com/blog/topics/threat-intelligence/flareon-11-challenge-solutions). In this series of writeups I present solutions to some of my favorite tasks from this year. All the sourcecodes are available on my Github, in dedicated repository: [flareon2024](https://github.com/hasherezade/flareon2024)*.

The 9th task was undoubtedly the most difficult one this year. It is called “serpentine” – but despite the name, it is not a crypto challenge involving Serpent cipher. This is what the description says:

![](https://hshrzd.wordpress.com/wp-content/uploads/2024/10/serpentine_info.png?w=726)

We are provided with a PE loading an obfuscated, self-modifying shellcode, and using exception-based flow obfuscation. Those elements remind of some hard tasks from the previous editions, such as “[evil](https://hshrzd.wordpress.com/2021/10/23/flare-on-8-task-9/)“, and “[break](https://hshrzd.wordpress.com/2021/01/05/flare-on-7-task-10/)” that I previously described. But the way they are served is yet different.

## Overview

I started by opening the given executable in IDA. First thing we can notice is that it requires a password given as a commandline argument. It has to be 32-character long. If we supplied it, the program proceeds to run a shellcode. All the logic related to the password verification happens there.

![](https://hshrzd.wordpress.com/wp-content/uploads/2024/10/serpentine_start.png?w=614)

The shellcode is hardcoded within the PE, and copied to a dynamically loaded memory in a TLS callback, before the `main` function was executed:

![](https://hshrzd.wordpress.com/wp-content/uploads/2024/10/shc_load.png?w=461)

Analyzing the shellcode is a real challenge. It deobfuscates itself as it goes, and then obfuscates back. The flow is also interrupted by `HLT` instructions, that are causing an exception handler to trigger. It does not only makes our code to jump into an unexpected line, but also changes the execution context on return, making the whole logic very confusing and hard to follow.

![](https://hshrzd.wordpress.com/wp-content/uploads/2024/10/shellcode_start-1.png?w=459)

The beginning of the obfuscated shellcode

Oftentimes, such cases can be helped to a big extent by a [Pin tracer](https://www.intel.com/content/www/us/en/developer/articles/tool/pin-a-dynamic-binary-instrumentation-tool.html). I first tried to trace it with [Tiny Tracer](https://github.com/hasherezade/tiny_tracer/), but unfortunately, due to the specifics of this self-modifying code, the tracing followed only the initial part of the binary:

```
[...]
15770;kernelbase.InitializeCriticalSectionEx
14ab9;CPUID:1
20cb;kernel32.SetUnhandledExceptionFilter
14de;ntdll.RtlInstallFunctionTableCallback
15c4;kernel32.SetUnhandledExceptionFilter
1649;called: ?? [196f0000+0]
> 196f0000+0;ntdll.KiUserExceptionDispatcher
a736;ntdll.RtlAllocateHeap
116d;ntdll.[TpReleaseIoCompletion+1cc]*
> 196f0000+98;called: ?? [199d4000+d27]
```

Soon after the shellcode started, PIN exits with an error:

```
E: During exception handling, an inconsistent instrumentation had been found.
```

*EDIT: it turns out that it is possible to trace the self-modifying part with PIN as well, we just need to add an option `-smc_strict 1` – which means “Check for self-modifications inside basic block*” *(suggested by: aziz). Still, cleaning the code before the tracing, and removing the parts related to obfuscation, help a lot to keep the tracelog focused on the functionality, and reduces the need of its post-processing.*

## Exception handlers

As mentioned before, the `HLT` instructions, and the exception handlers (SEH) that they trigger, play a very important role in how this executable is obfuscated. After the exception, the code resumes its execution at a very different and unexpected address. If we don’t follow it, we lose the track.

At first, I tried to dump all the handlers addresses with the help of x64dbg. Each new exception handler is called via `ntdll.RtlpExecuteHandlerForException` . The redirection happens by `call rax`. By setting a breakpoint at this instruction, and editing the details, we can [log](https://help.x64dbg.com/en/latest/commands/script/log.html) the handler’s address. All the visited handlers will be saved in the listing at the log tab.

![](https://hshrzd.wordpress.com/wp-content/uploads/2024/10/dump_handler.png?w=814)

Soon I realized that there are too many blocks to resolve, and this is not the best way to dump them all. To really tackle this part, I have to parse the exception information.

In a typical case, the (SEH) exceptions thrown by a Windows binary are handled using the information stored in the Exception Table, that is a part of the PE format. However, this way of registering exceptions only work if they are thrown from within the corresponding PE image. In the current case, the exceptions are thrown from a shellcode, that is in a dynamically allocated, private memory. So the corresponding handlers have to be installed manually. In 64-bit Windows binaries it can be done with the help of the function `[RtlInstallFunctionTableCallback](https://learn.microsoft.com/en-us/windows/win32/api/winnt/nf-winnt-rtlinstallfunctiontablecallback)`. However, this function is nowhere to be found in the Import Table of our executable, and by looking in IDA, it is difficult to spot where it is called. Fortunately, in this particular part, the trace done by Tiny Tracer comes in handy. We can see the following calls in the TAG file:

```
20cb;kernel32.SetUnhandledExceptionFilter
14de;ntdll.RtlInstallFunctionTableCallback
15c4;kernel32.SetUnhandledExceptionFilter
```

When we [apply the tags in IDA](https://github.com/hasherezade/tiny_tracer/wiki/Using-the-TAGs-with-disassemblers-and-debuggers), it clarifies a lot.

![](https://hshrzd.wordpress.com/wp-content/uploads/2024/10/func.png?w=748)

As the MSDN says, one of the arguments of `[RtlInstallFunctionTableCallback](https://learn.microsoft.com/en-us/windows/win32/api/winnt/nf-winnt-rtlinstallfunctiontablecallback)` is a callback function to be installed. This callback is then executed each time an exception in the defined range gets hit. It is responsible for associating the exception with the relevant [UNWIND\_INFO](https://learn.microsoft.com/en-us/cpp/build/exception-handling-x64?view=msvc-170): a structure containing all information needed for handling it. It includes the address of the handler to be called, and unwinding codes that define how the stack should be modified before the handler gets executed.

T...
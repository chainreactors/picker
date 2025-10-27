---
title: Cat &amp; Mouse - or Chess?
url: https://s3cur3th1ssh1t.github.io/Cat_Mouse_or_Chess/
source: S3cur3Th1sSh1t
date: 2023-07-08
fetch_date: 2025-10-04T11:53:15.759611
---

# Cat &amp; Mouse - or Chess?

Cat & Mouse - or Chess? | S3cur3Th1sSh1t

[Home](/)
[About](/about/)

# [Cat & Mouse - or Chess?](/Cat_Mouse_or_Chess/)

July 07, 2023

Last year I had the idea for a new approach to block EDR DLLs from loading into a newly spawned process. After several months this idea lead to a PoC, which was then published after presenting the topic at [x33fcon](https://www.x33fcon.com/#!s/FabianMosch.md) and [Troopers](https://troopers.de/troopers23/talks/juxtj7/) this year.

This post will cover the background and description of the technique.

## How do EDRs typically detect malicious activities?

Endpoint detection and Response (EDR) systems detect malicious activities or software in various ways. The detections can occur from userland (where the user processes run) or from kernelland (operating system level).

Typical analysis/detections from userland include:

* Static & dynamic analysis
* Userland hooking
* Stack trace analysis

Whereas static analysis can be for example signatures for files (like any AV uses) or checking metadata such as certificates and their validity. Dynamic analysis can include active debugging of an executable, or putting it into a sandbox-like environment to see what it does on runtime.

Stack trace analysis can show, if an process was for example executing specific Windows APIs from an unbacked memory region (dynamic code in a private commit memory section, very likely shellcode) which is super suspicious.

Detection coming from kernelland typically make use of:

* Kernel Callbacks
* ETW Threat Intelligence (ETWti)

EDRs typically use a signed driver to also operate from kernelland. By doing this, they can check specific Kernel Callbacks for any running process to live intercept execution for those and execute their own code before the process resumes with whatever it will do afterward. If for example a new process is created, the EDR can intercept its execution and check what has to be executed with the Kernel Callback `PsSetCreateProcessNotifyRoutine()`. But they could also live intercept the creation of new threads with `PsSetCreateThreadNotifyRoutine()` to check their entrypoint for malicious code. As the code is running from the kernel, any mistake could lead to a system-wide bluescreen, which could be one reason for vendors to not make heavy use of it.

![](/assets/posts/RuyLopez/KernelCallbacks.png)

ETWti is an interface provided by Microsoft, where drivers can subscribe to receive special ETW events. These events are specifically meant to be used for detecting malicious activities and also include events such as for Process creation, Allocation of memory, Thread creation and much more:

![](/assets/posts/RuyLopez/ETWti.png)

For this blog post and technique, we will however focus on userland hook-based detections, as those at least from my experience are still the most relevant detections being mainly used by nearly all EDRs.

## What are userland hooks about?

For being able to do live analysis of userland processes, EDR vendors and most AV vendors as well load their own Dynamic Linked Library (DLL) into running processes on an operating system. After this DLL is loaded in a process, it will patch memory regions of chosen Windows APIs to place a hook, which is basically an JMP instruction going to their own DLLs memory region.

![](/assets/posts/RuyLopez/Hooks.png)

Via this, they can live intercept Windows APIs from being called on runtime of a process and inspect the input arguments for the Windows API being executed to check what it *wants to* do on runtime.

Let us imagine the following process for malware to execute shellcode in a remote process for a better understanding:

![](/assets/posts/RuyLopez/ProcInject.png)

First, the malware gets a Handle to the remote process by using `OpenProcess`. Afterwards it calls `VirtualAllocEx` to allocate memory in the remote process. `WriteProcessMemory` is used to actually write the Shellcode into the remote process newly allocated memory region. In the end, `CreateRemoteThread` is used to execute the Shellcode in the remote process in a newly created Thread. We also imagine, that the Shellcode was encrypted and decrypted on runtime before writing it into the remote process with `WriteProcessMemory` to avoid signature based detections. `CreateRemoteThread` will after being called itself call `NtCreateThreadEx` from `ntdll.dll`, which is the last function being called from userland. As `ntdll.dll` functions are the last ones being called from userland, many vendors tend to hook functions from this specific DLL.

An example definition for `NtCreateThreadEx` looks like the following:

![](/assets/posts/RuyLopez/Definition.png)

The EDR can inspect input arguments when hooked APIs are called on runtime, right? So in this case, the EDR could inspect the input parameters for `NtCreateThreadEx` and especially the `startAddress` input pointer. When a malware wants to start Shellcode in a new Thread, the `startAddress` will typically point to the already **decrypted** plain Shellcode, e.G. an C2 implant. Our EDR can now apply Yara-Rules (memory scan) on the `startAddress` memory region to find any **known malicious** C2 implants, such as CobaltStrike, Sliver, Covenant and so on. And if a rule matches, they know that malicious software wants to be called and therefore just kill the process.

So in the very end our malware has been stopped by the EDR on runtime, based on userland hook-based detections + verification of **known malicious** code.

## Existing Userland hook evasion techniques

Several different tools and techniques have been released over the last years, which are capable of bypassing userland hook-based detections. I will give a summary here, but won’t go into depth as there are many other articles to read about or code to check in the links.

1. Unhooking
2. The usage of direct Syscalls
3. Using Hardware Breakpoints
4. Patching the DLL entrypoint

#### Unhooking

With unhooking, a fresh copy of `ntdll.dll` is grabbed from any location (Disk, KnownDlls) and the *EDR patched* memory region with jumps to the EDR DLL is replaced with the original value of `ntdll.dll`. This effectively bypasses hooks, as no more jumps will take place and no more input argument analysis is done.

![](/assets/posts/RuyLopez/Unhook.png)

#### Direct Syscalls

Instead of calling `ntdll.dll` functions the regular way, their content can also be retrieved or re-build on runtime and executed directly from the current process memory. If we have our own `ntdll.dll` functions in our own process memory, there will also be no hooks in place, as those are only in the `ntdll.dll` memory location, which also leads to a bypass here. Proof of Concepts for different retrieval techniques are for example the following:

1. Re-build `ntdll.dll` functions with information from Memory ([HellsGate](https://github.com/am0nsec/HellsGate), [RecycledGate](https://github.com/thefLink/RecycledGate),\*-Gate)
2. Get a fresh `ntdll.dll` copy from Disk and put the function content to memory (GetSyscallStub, e.G. [C DInvoke](https://github.com/TheWover/DInvoke))
3. The Syscall Stubs are partially or completely embedded in the malware executable from the beginning - (Syswhispers [1](https://github.com/jthuraisamy/SysWhispers),[2](https://github.com/jthuraisamy/SysWhispers2),[3](https://github.com/klezVirus/SysWhispers3))

#### Usage of Hardware Breakpoints

The first PoC I know about which was using Hardware Breakpoints to evade userland hooks was [TamperingSyscalls](https://github.com/rad9800/TamperingSyscalls). The process looks like the following:

![](/assets/posts/RuyLopez/HardwareBreakpoints.png)

By placing Hardware Breakpoints to the `ntdll.dll` function we want to call afterward, we can effectively intercept execution before the jump to the EDR DLL takes place. In that moment, we hide the input parameters for this specific function from the stack by replacing it with arbitrary values and we back the original values up i...
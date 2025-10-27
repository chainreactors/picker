---
title: What child is this?
url: https://blog.trailofbits.com/2022/12/20/process-reparenting-microsoft-windows/
source: Trail of Bits Blog
date: 2022-12-21
fetch_date: 2025-10-04T02:05:02.216130
---

# What child is this?

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# What child is this?

Yarden Shafir

December 20, 2022

[program-analysis](/categories/program-analysis/)

*A Primer on Process Reparenting in Windows*

Process reparenting is a technique used in Microsoft Windows to create a child process under a different parent process than the one making the call to `CreateProcess`. Malicious actors can use this technique to evade security products or break process ancestry ties, making detection more challenging. However, process reparenting is also used legitimately across the operating system, for example during execution of packaged or store applications. Like many features, process reparenting can confuse both security products and security teams, leading to either missed detections or false positives on otherwise-innocent applications. This blog post will look at how to investigate this interesting behavior.

## Process Monitor and the Incorrect Stack Trace

Lately I was playing around with the Windows Terminal and the way it runs and operates (something I might write about more in a future blog post). I ran the Windows Terminal through the Windows start menu and recorded its execution with Process Monitor (ProcMon), a SysInternals tool that records the execution, file system, registry, and network operations of a process. When I looked at the recording, I noticed something strange:

[![](/img/wpdump/fcf2cf4f38e9f4e2a5e3d281d1bbe1b9.png)](/img/wpdump/fcf2cf4f38e9f4e2a5e3d281d1bbe1b9.png)

According to ProcMon, `explorer.exe` is starting the terminal process. This makes sense, as `explorer.exe` is generally the parent process of many user applications. But a close look at the call stack reveals some gaps: Frames 8 and 9 have no symbols and don’t even show a module name. Many would assume this is a shellcode: dynamic memory running from the heap, outside of a regular module. We can investigate this possibility using a debugger or a tool like Process Hacker (now known as System Informer). The output of Process Hacker is shown below.

[![](/img/wpdump/949f0988c881ff740d09bb91a333935f.png)](/img/wpdump/949f0988c881ff740d09bb91a333935f.png)

The memory range to which these stack frames point isn’t mapped at all. So either this is an especially sneaky shellcode and I should recheck my system for yet another nation-state attack, or there is a different explanation.

To get to the root cause, I turn to the (almost) always-reliable debugger: WinDbg. We’ll use a kernel debugger to track the process creation of the Windows Terminal and observe the data on which ProcMon operates, which should give some indication about what’s really going on.

First, let’s start a recording session with ProcMon, which makes it load its kernel driver and register a process notify routine. Many Endpoint Detection and Response (EDR) systems and system monitoring tools use this callback to get notified about process creation and termination. To follow ProcMon’s steps, we’ll set a breakpoint on this callback and see what happens.

The list of process creation callbacks is saved in an unexported kernel symbol called `PspCreateProcessNotifyRoutine`. Unfortunately, the callbacks themselves are saved in a data structure that isn’t available in the public symbols, so parsing them can be a bit of a pain. But the structure itself is sufficiently well known and stable that we can use hard-coded offsets to parse it. I wrote a simple [one-line script](https://github.com/yardenshafir/WinDbg_Scripts/blob/master/processNotifyRoutinesSymbols) to print all the registered callbacks (many other examples are available). If you’re using the newest version of WinDbg, you can even use the new [symbol builder](https://github.com/microsoft/WinDbg-Samples/tree/master/TargetComposition/SymBuilder) to push the structure and use it as if it were available in the symbols!

Running this script, we can easily find ProcMon’s process callback:

```
dx ((__int64(*)[64])&nt!PspCreateProcessNotifyRoutine)->Where(p => p)->Select(p =>
(void(*)())(*(((__int64*)(p & ~0xf)) + 1)))
((__int64(*)[64])&nt!PspCreateProcessNotifyRoutine)->Where(p => p)->Select(p =>
(void(*)())(*(((__int64*)(p & ~0xf)) + 1)))
    [0]              : 0xfffff80673f78900 : cng!CngCreateProcessNotifyRoutine+0x0
[Type: void (*)()]
    [1]              : 0xfffff80674b29f50 : WdFilter+0x49f50 [Type: void (*)()]
    [2]              : 0xfffff80673dbb4b0 : ksecdd!KsecCreateProcessNotifyRoutine+0x0
[Type: void (*)()]
    [3]              : 0xfffff8067510db70 : tcpip!CreateProcessNotifyRoutineEx+0x0
[Type: void (*)()]
    [4]              : 0xfffff8067561d990 : iorate!IoRateProcessCreateNotify+0x0
[Type: void (*)()]
    [5]              : 0xfffff80673eea160 : CI!I_PEProcessNotify+0x0 [Type: void
(*)()]
    [6]              : 0xfffff80678d6a590 : dxgkrnl!DxgkProcessNotify+0x0 [Type: void
(*)()]
    [7]              : 0xfffff8068184acf0 : peauth+0x3acf0 [Type: void (*)()]
    [8]              : 0xfffff80681b36400 : PROCMON24+0x6400 [Type: void (*)()]
```

The next step is setting a breakpoint on this callback, resuming the machine’s execution, and running the Windows Terminal from the start menu:

```
bp 0xfffff80681b36400; g
```

And our breakpoint gets hit!

```
1: kd> g
Breakpoint 0 hit
PROCMON24+0x6400:
fffff806`81b36400 4d8bc8          mov     r9,r8
```

To get more insight into what ProcMon sees, we should parse the function arguments. I’ll skip a couple of reverse engineering steps (if I don’t, this post will just keep on going forever) and simply let you know that on modern systems, ProcMon registers its process notify routine using [PsSetCreateProcessNotifyRoutineEx2](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntddk/nf-ntddk-pssetcreateprocessnotifyroutineex2). This matters because different versions of the process-notify routine receive slightly different arguments. In this case, the routine has the type [PCREATE\_PROCESS\_NOTIFY\_ROUTINE\_EX](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntddk/nc-ntddk-pcreate_process_notify_routine_ex):

```
void PcreateProcessNotifyRoutineEx (
  [_Inout_]           PEPROCESS Process,
  [in]                HANDLE ProcessId,
  [in, out, optional] PPS_CREATE_NOTIFY_INFO CreateInfo
)
```

With this knowledge, we can use the debugger data model to present the arguments with the correct types, just as the driver sees them. There’s only one issue: `PS_CREATE_NOTIFY_INFO` isn’t included in the public symbols, so we don’t have easy access to it. It is, however, included in the public `ntddk.h` header, so we can simply copy the structure definition (with minimal adjustments) into a separate header and use it in the debugger through Synthetic Types. To that end, let’s create the header file under `c:\temp\ntddk_structs.h`:

```
typedef struct _PS_CREATE_NOTIFY_INFO {
    ULONG64 Size;
    union {
        _In_ ULONG Flags;
        struct {
            _In_ ULONG FileOpenNameAvailable : 1;
            _In_ ULONG IsSubsystemProcess : 1;
            _In_ ULONG Reserved : 30;
        };
    };
    HANDLE ParentProcessId;
    _CLIENT_ID CreatingThreadId;
    _FILE_OBJECT *FileObject;
    _UNICODE_STRING *ImageFileName;
    _UNICODE_STRING *CommandLine;
    ULONG CreationStatus;
} PS_CREATE_NOTIFY_INFO, *PPS_CREATE_NOTIFY_INFO;
```

Next, let’s load it into the debugger through synthetic types:

```
dx Debugger.Utility.Analysis.SyntheticTypes.ReadHeader("c:\\temp\\ntddk_structs.h",
"nt")
Debugger.Utility.Analysis.SyntheticTypes.ReadHeader("c:\\temp\\ntddk_structs.h",
"nt")                 : ntkrnlmp.exe(ntddk_structs.h)
    ReturnEnumsAsObjects : false
    RegisterSyntheticTypeModels : false
    Module           : ntkrnlmp.exe
    Header           : ntddk_structs.h
    Types
```

(Side note: Try not to make any mistakes in your header files or you’ll have to restart the debugger session to reload the fixed version of t...
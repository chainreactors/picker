---
title: Bootkitting Windows Sandbox
url: https://secret.club/2022/08/29/bootkitting-windows-sandbox.html
source: Over Security - Cybersecurity news aggregator
date: 2025-07-02
fetch_date: 2025-10-06T23:56:17.301159
---

# Bootkitting Windows Sandbox

[SECRET CLUB](/) [HOME](/) [ABOUT](/about)

# Bootkitting Windows Sandbox

![main authors image](/assets/author_img/mrexodia.jpg)  [mrexodia](/author/mrexodia), [sdoogm](/author/sdoogm)

 Aug 29, 2022

---

## [Introduction & Motivation](#introduction--motivation)

[Windows Sandbox](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-sandbox/windows-sandbox-overview) is a feature that Microsoft added to Windows back in May 2019. As Microsoft puts it:

> Windows Sandbox provides a lightweight desktop environment to safely run applications in isolation. Software installed inside the Windows Sandbox environment remains “sandboxed” and runs separately from the host machine.

The startup is usually very fast and the user experience is great. You can [configure](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-sandbox/windows-sandbox-configure-using-wsb-file) it with a `.wsb` file and then double click that file to start a clean VM.

The sandbox can be useful for malware analysis and as we will show in this article, it can also be used for kernel research and driver development. We will take things a step further though and share how we can intercept the boot process and patch the kernel during startup with a bootkit.

TLDR: Visit the [SandboxBootkit](https://github.com/thesecretclub/SandboxBootkit) repository to try out the bootkit for yourself.

## [Windows Sandbox for driver development](#windows-sandbox-for-driver-development)

A few years back [Jonas L tweeted](https://twitter.com/jonasLyk/status/1366700591876079623) about the undocumented command `CmDiag`. It turns out that it is almost trivial to enable test signing and kernel debugging in the sandbox (this part was copied straight from my [StackOverflow answer](https://stackoverflow.com/a/73266007/1806760)).

First you need to enable development mode (everything needs to be run from an *Administrator* command prompt):

```
CmDiag DevelopmentMode -On
```

Then enable network debugging (you can see additional options with `CmDiag Debug`):

```
CmDiag Debug -On -Net
```

This should give you the connection string:

```
Debugging successfully enabled.

Connection string: -k net:port=50100,key=cl.ea.rt.ext,target=<ContainerHostIp> -v
```

Now start WinDbg and connect to `127.0.0.1`:

```
windbg.exe -k net:port=50100,key=cl.ea.rt.ext,target=127.0.0.1 -v
```

Then you start Windows Sandbox and it should connect:

```
Microsoft (R) Windows Debugger Version 10.0.22621.1 AMD64
Copyright (c) Microsoft Corporation. All rights reserved.

Using NET for debugging
Opened WinSock 2.0
Using IPv4 only.
Waiting to reconnect...
Connected to target 127.0.0.1 on port 50100 on local IP <xxx.xxx.xxx.xxx>.
You can get the target MAC address by running .kdtargetmac command.
Connected to Windows 10 19041 x64 target at (Sun Aug  7 10:32:11.311 2022 (UTC + 2:00)), ptr64 TRUE
Kernel Debugger connection established.
```

Now in order to load your driver you have to copy it into the sandbox and you can use `sc create` and `sc start` to run it. Obviously most device drivers will not work/freeze the VM but this can certainly be helpful for research.

The downside of course is that you need to do quite a bit of manual work and this is not exactly a smooth development experience. Likely you can improve it with the `<MappedFolder>` and `<LogonCommand>` options in your `.wsb` file.

## [PatchGuard & DSE](#patchguard--dse)

Running Windows Sandbox with a debugger attached will disable [PatchGuard](https://en.wikipedia.org/wiki/Kernel_Patch_Protection) and with test signing enabled you can run your own kernel code. Attaching a debugger every time is not ideal though. Startup times are increased by a lot and software might detect kernel debugging and refuse to run. Additionally it seems that the network connection is not necessarily stable across host reboots and you need to restart WinDbg every time to attach the debugger to the sandbox.

Tooling similar to [EfiGuard](https://github.com/Mattiwatti/EfiGuard) would be ideal for our purposes and in the rest of the post we will look at implementing our own bootkit with equivalent functionality.

## [Windows Sandbox internals recap](#windows-sandbox-internals-recap)

Back in March 2021 a great article called [Playing in the (Windows) Sandbox](https://research.checkpoint.com/2021/playing-in-the-windows-sandbox/) came out. This article has a lot of information about the internals and a lot of the information below comes from there. Another good resource is Microsoft’s official [Windows Sandbox architecture](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-sandbox/windows-sandbox-architecture) page.

Windows Sandbox uses VHDx layering and NTFS magic to allow the VM to be extremely lightweight. Most of the system files are actually NTFS reparse points that point to the host file system. For our purposes the relevant file is `BaseLayer.vhdx` (more details in the references above).

What the article did not mention is that there is a folder called `BaseLayer` pointing directly inside the mounted `BaseLayer.vhdx` at the following path on the host:

```
C:\ProgramData\Microsoft\Windows\Containers\BaseImages\<GUID>\BaseLayer
```

This is handy because it allows us to read/write to the Windows Sandbox file system without having to stop/restart `CmService` every time we want to try something. The only catch is that you need to run as `TrustedInstaller` and you need to enable development mode to modify files there.

When you enable development mode there will also be an additional folder called `DebugLayer` in the same location. This folder exists on the host file system and allows us to overwrite certain files (`BCD`, registry hives) without having to modify the `BaseLayer`. The configuration for the `DebugLayer` appears to be in `BaseLayer\Bindings\Debug`, but no further time was spent investigating. The downside of enabling development mode is that snapshots are disabled and as a result startup times are significantly increased. After modifying something in the `BaseLayer` and disabling development mode you also need to delete the `Snapshots` folder and restart `CmService` to apply the changes.

## [Getting code execution at boot time](#getting-code-execution-at-boot-time)

To understand how to get code execution at boot time you need some background on UEFI. We released [Introduction to UEFI](https://secret.club/2020/05/26/introduction-to-uefi-part-1.html) a few years back and there is also a very informative series called [Geeking out with the UEFI boot manager](https://oofhours.com/2022/06/29/geeking-out-with-the-uefi-boot-manager/) that is useful for our purposes.

In our case it is enough to know that the firmware will try to load `EFI\Boot\bootx64.efi` from the default boot device first. You can override this behavior by setting the `BootOrder` UEFI variable. To find out how Windows Sandbox boots you can run the following PowerShell commands:

```
> Set-ExecutionPolicy -ExecutionPolicy Unrestricted
> Install-Module UEFI
> Get-UEFIVariable -VariableName BootOrder -AsByteArray
0
0
> Get-UEFIVariable -VariableName Boot0000
�VMBus File System�VMBus�\EFI\Microsoft\Boot\bootmgfw.efi�
```

From this we can derive that Windows Sandbox first loads:

```
\EFI\Microsoft\Boot\bootmgfw.efi
```

As described in the previous section we can access this file on the host (as `TrustedInstaller`) via the following path:

```
C:\ProgramData\Microsoft\Windows\Containers\BaseImages\<GUID>\BaseLayer\Files\EFI\Microsoft\Boot\bootmgfw.efi
```

To verify our assumption we can rename the file and try to start Windows Sandbox. If you check in [Process Monitor](https://docs.microsoft.com/en-us/sysinternals/downloads/procmon) you will see `vmwp.exe` fails to open `bootmgfw.efi` and nothing happens after that.

Perhaps it is possible to modify UEFI variables and change `Boot0000` (Hyper-V Manager can do this for regular VMs so probably there is a wa...
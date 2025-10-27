---
title: The Windows Registry Adventure #4: Hives and the registry layout
url: https://googleprojectzero.blogspot.com/2024/10/the-windows-registry-adventure-4-hives.html
source: Project Zero
date: 2024-10-26
fetch_date: 2025-10-06T18:52:47.353970
---

# The Windows Registry Adventure #4: Hives and the registry layout

# [Project Zero](https://googleprojectzero.blogspot.com/)

News and updates from the Project Zero team at Google

## Friday, October 25, 2024

### The Windows Registry Adventure #4: Hives and the registry layout

Posted by Mateusz Jurczyk, Google Project Zero

To a normal user or even a Win32 application developer, the registry layout may seem simple: there are five root keys that we know from Regedit (abbreviated as HKCR, HKLM, HKCU, HKU and HKCC), and each of them contains a nested tree structure that serves a specific role in the system. But as one tries to dig deeper and understand how the registry really works internally, things may get confusing really fast. What are hives? How do they map or relate to the top-level keys? Why are some HKEY root keys pointing inside of other root keys (e.g. HKCU being located under HKU)? These are all valid questions, but they are difficult to answer without fully understanding the interactions between the user-mode Registry API and the kernel-mode registry interface, so let's start there.

## The high-level view

A simplified diagram of the execution flow taken when an application creates a registry key is shown below:

[![A diagram illustrating the call stack for the RegCreateKeyEx function in Windows. It shows the transition from user-mode to kernel-mode through various API calls: * **User-mode:** * Application.exe calls RegCreateKeyEx in KernelBase.dll * KernelBase.dll calls NtCreateKey in ntdll.dll * ntdll.dll makes a system call to NtCreateKey * **Kernel-mode:** * ntoskrnl.exe executes the NtCreateKey syscall](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg3DcA4NRlJwRBwZj_EfcUNKjvc_9LuRBEDgidTVSPDGLOqKyspZ1Xl3QNx3n9eXGTHLnRctQ49HyrBmXcRTc-_g2S_vBbm0Uo67bScEqCV15lcRWWb_eNVGb7K7bc9caSF0lKuRDH5GXlJsyMzZ6DqYVkR_JVP8wIYWuqAgUSuXM1x6BXcaJeAZWHADu8/s1200/image3.png "A diagram illustrating the call stack for the RegCreateKeyEx function in Windows. It shows the transition from user-mode to kernel-mode through various API calls: * **User-mode:** * Application.exe calls RegCreateKeyEx in KernelBase.dll * KernelBase.dll calls NtCreateKey in ntdll.dll * ntdll.dll makes a system call to NtCreateKey * **Kernel-mode:** * ntoskrnl.exe executes the NtCreateKey syscall")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg3DcA4NRlJwRBwZj_EfcUNKjvc_9LuRBEDgidTVSPDGLOqKyspZ1Xl3QNx3n9eXGTHLnRctQ49HyrBmXcRTc-_g2S_vBbm0Uo67bScEqCV15lcRWWb_eNVGb7K7bc9caSF0lKuRDH5GXlJsyMzZ6DqYVkR_JVP8wIYWuqAgUSuXM1x6BXcaJeAZWHADu8/s1999/image3.png)

In this example, Application.exe is a desktop program calling the documented [RegCreateKeyEx](https://learn.microsoft.com/en-us/windows/win32/api/winreg/nf-winreg-regcreatekeyexw) function, which is exported by KernelBase.dll. The KernelBase.dll library implements RegCreateKeyEx by translating the high-level API parameters passed by the caller (paths, flags, etc.) to internal ones understood by the kernel. It then invokes the [NtCreateKey](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdm/nf-wdm-zwcreatekey) system call through a thin wrapper provided by ntdll.dll, and the execution finally reaches the Windows kernel, where all of the actual work on the internal registry representation is performed.

The declaration of the RegCreateKeyEx function is as follows:

`LSTATUS RegCreateKeyExW(`

  [in]            HKEY                        hKey,

  [in]            LPCWSTR                     lpSubKey,

                  DWORD                       Reserved,

  [in, optional]  LPWSTR                      lpClass,

  [in]            DWORD                       dwOptions,

  [in]            REGSAM                      samDesired,

  [in, optional]  const LPSECURITY\_ATTRIBUTES lpSecurityAttributes,

  [out]           PHKEY                       phkResult,

  [out, optional] LPDWORD                     lpdwDisposition

);

As the first two arguments imply, many registry operations (and especially key opening/creation) are performed on a pair of a base key handle and a relative key path. HKEY is a dedicated type for registry key handles, but it is functionally equivalent to the standard HANDLE type. It can either contain a regular handle to a key object (as managed by the NT Object Manager), or one of a few possible pseudo-handles described in the [Predefined Keys](https://learn.microsoft.com/en-us/windows/win32/sysinfo/predefined-keys) list. They are defined in winreg.h with the following numeric values:

#define HKEY\_CLASSES\_ROOT                   (( HKEY ) (ULONG\_PTR)((LONG)0x80000000) )

#define HKEY\_CURRENT\_USER                   (( HKEY ) (ULONG\_PTR)((LONG)0x80000001) )

#define HKEY\_LOCAL\_MACHINE                  (( HKEY ) (ULONG\_PTR)((LONG)0x80000002) )

#define HKEY\_USERS                          (( HKEY ) (ULONG\_PTR)((LONG)0x80000003) )

#define HKEY\_PERFORMANCE\_DATA               (( HKEY ) (ULONG\_PTR)((LONG)0x80000004) )

#define HKEY\_PERFORMANCE\_TEXT               (( HKEY ) (ULONG\_PTR)((LONG)0x80000050) )

#define HKEY\_PERFORMANCE\_NLSTEXT            (( HKEY ) (ULONG\_PTR)((LONG)0x80000060) )

#define HKEY\_CURRENT\_CONFIG                 (( HKEY ) (ULONG\_PTR)((LONG)0x80000005) )

#define HKEY\_DYN\_DATA                       (( HKEY ) (ULONG\_PTR)((LONG)0x80000006) )

#define HKEY\_CURRENT\_USER\_LOCAL\_SETTINGS    (( HKEY ) (ULONG\_PTR)((LONG)0x80000007) )

As we can see, they all have the highest bit set, which is normally reserved for kernel-mode handles. Thanks to this, the values can never collide with legitimate user-mode handles, and can be freely used as special pseudo-handles. It is the responsibility of the Registry API to translate these values into their corresponding low-level registry paths before calling into the kernel. In other words, predefined keys are a strictly user-mode concept, and the kernel itself has no awareness of them. If someone decided to write a program interacting with the registry directly through system calls rather than the API, they wouldn't have any use of the HKEY\_\* constants whatsoever.

This explains why the top-level keys don't necessarily represent mutually exclusive subtrees – none of them inherently represent any specific part of the registry, and their meaning is purely conventional. It is up to KernelBase.dll to decide how it handles each of these keys, and this is further highlighted by the existence of the [Reg­Override­Predef­Key](https://learn.microsoft.com/en-us/windows/win32/api/winreg/nf-winreg-regoverridepredefkey) function, which allows an application to remap them in the context of the local process. In literature, root keys are sometimes described as being "links" to specific registry paths, and while conceptually correct, this may confuse readers who know about the existence of symbolic links, which is a separate, unrelated mechanism. In fact, if we count all the different ways in which access to a registry key can be transparently redirected to another path (either in the user or kernel part of the interface), we end up with at least four:

1. User-mode Registry API interpreting top-level keys and translating them into specific internal paths, as discussed above.
2. Kernel-mode Configuration Manager following symbolic links in the registry, i.e. keys created with the [REG\_OPTION\_CREATE\_LINK](https://learn.microsoft.com/en-us/windows/win32/api/winreg/nf-winreg-regcreatekeyexw#REG_OPTION_CREATE_LINK) flag and with a value named "SymbolicLinkValue" of type REG\_LINK.
3. Kernel-mode Configuration Manager applying [Registry Virtualization](https://learn.microsoft.com/en-us/windows/win32/sysinfo/registry-virtualization) to a specific legacy application, and thus redirecting reads/writes to/from subkeys of HKEY\_LOCAL\_MACHINE\Software to HKEY\_USERS\<SID>\_Classes\VirtualStore\Machine\Software.
4. The user-mode Registry API and kernel-mode Configuration Manager working together to handle so-called "predefined-handle keys" (marked by flag 0x40 in CM\_KEY\_NODE.Flags). This is a specia...
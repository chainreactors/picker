---
title: WOW64 Callback Table (FinFisher)
url: https://modexp.wordpress.com/2023/04/19/finding-the-wow64-callback-table/
source: modexp
date: 2023-04-20
fetch_date: 2025-10-04T11:32:48.342552
---

# WOW64 Callback Table (FinFisher)

[modexp](https://modexp.wordpress.com/ "modexp")

Random posts about computer security

[![](https://modexp.wordpress.com/wp-content/uploads/2023/04/wow64_table.png?w=940&h=198&crop=1)](https://modexp.wordpress.com/ "modexp")

[Skip to content](#content "Skip to content")

* [Home](https://modexp.wordpress.com/)
* [About](https://modexp.wordpress.com/about/)

[← Shellcode: Linux on RISC-V 64-Bit](https://modexp.wordpress.com/2022/05/02/shellcode-risc-v-linux/)

[Delegated NT DLL →](https://modexp.wordpress.com/2024/02/13/delegated-nt-dll/)

## [WOW64 Callback Table (FinFisher)](https://modexp.wordpress.com/2023/04/19/finding-the-wow64-callback-table/)

Posted on [April 19, 2023](https://modexp.wordpress.com/2023/04/19/finding-the-wow64-callback-table/ "6:07 pm") by [odzhan](https://modexp.wordpress.com/author/odzhan/ "View all posts by odzhan")

## Introduction

Ken Johnson (otherwise known as Skywing) first talked about the [KiUserExceptionDispatcher back in 2007](http://www.nynaeve.net/?p=201) . Since then, scattered around the internet are various posts talking about it, but for some reason nobody demonstrating how to use it. It’s been documented that FinFisher misuses the function pointers as part of its virtual machine functionality, so let’s take a look at how to find the table before doing anything creative with it…The code to locate the table didn’t take long and didn’t require looking at FinFisher internals or existing code. It’s a simple heuristic based search.

## References

* [WoW64 Internals](https://wbenny.github.io/2018/11/04/wow64-internals.html)
* [Heavens gate with bypass – load 64 bit modules into 32 bit process](http://www.rohitab.com/discuss/topic/43044-heavens-gate-with-bypass-load-64-bit-modules-into-32-bit-process/)
* <https://www.unknowncheats.me/forum/2699465-post6033.html>
* [Hardware breakpoints and exceptions on Window](https://ling.re/hardware-breakpoints/)
* [FinFisher exposed: A researcher’s tale of defeating traps, tricks, and complex virtual machines](https://www.microsoft.com/en-us/security/blog/2018/03/01/finfisher-exposed-a-researchers-tale-of-defeating-traps-tricks-and-complex-virtual-machines/)

## Observations

If you take a look at ***ntdll!LdrpLoadWow64***, that’s called during initialization of a WOW64 process, you’ll see it loading wow64.dll and resolving the address of six exports. This process has been better documented in the posts mentioned above.

* Wow64LdrpInitialize
* Wow64PrepareForException
* Wow64ApcRoutine
* Wow64PrepareForDebuggerAttach
* Wow64SuspendLocalThread
* Wow64SuspendLocalProcess

A closer look at how this works will provide you with an array of function names stored in STRING format and a pointer to a variable that holds each address resolved. The following is my attempt at recreating the same structure.

```
typedef union _W64_T {
    LPVOID p;
    DWORD64 q;
    LPVOID *pp;
} W64_T;

typedef struct _WOW64_CALLBACK {
    STRING Name;
    W64_T  Function;
} WOW64_CALLBACK, *PWOW64_CALLBACK;

//
// Structure based on 64-bit version of NTDLL on Windows 10
//
typedef struct _WOW64_CALLBACK_TABLE {
    WOW64_CALLBACK  Wow64LdrpInitialize;
    WOW64_CALLBACK  Wow64PrepareForException;
    WOW64_CALLBACK  Wow64ApcRoutine;
    WOW64_CALLBACK  Wow64PrepareForDebuggerAttach;
    WOW64_CALLBACK  Wow64SuspendLocalThread;
    WOW64_CALLBACK  Wow64SuspendLocalProcess;
} WOW64_CALLBACK_TABLE, *PWOW64_CALLBACK_TABLE;

WOW64_CALLBACK_TABLE Wow64Table = {
    {RTL_CONSTANT_STRING("Wow64LdrpInitialize"), NULL},
    {RTL_CONSTANT_STRING("Wow64PrepareForException"), NULL},
    {RTL_CONSTANT_STRING("Wow64ApcRoutine"), NULL},
    {RTL_CONSTANT_STRING("Wow64PrepareForDebuggerAttach"), NULL},
    {RTL_CONSTANT_STRING("Wow64SuspendLocalThread"), NULL},
    {RTL_CONSTANT_STRING("Wow64SuspendLocalProcess"), NULL}
    };
```

## Locating Table

There could be a number of ways to do this. In the following example, we search the .rdata section for STRING structures that equal the function pointer we wish to find. Since these strings are constant and unlikely to change, it works reasonably well.

```
BOOL
IsReadOnlyPtr(LPVOID ptr) {
    MEMORY_BASIC_INFORMATION mbi;

    if (!ptr) return FALSE;

    DWORD res = VirtualQuery(ptr, &mbi, sizeof(mbi));
    if (res != sizeof(mbi)) return FALSE;

    return ((mbi.State   == MEM_COMMIT    ) &&
            (mbi.Type    == MEM_IMAGE     ) &&
            (mbi.Protect == PAGE_READONLY));
}

BOOL
GetWow64FunctionPointer(PWOW64_CALLBACK Callback) {
    auto m = (PBYTE)GetModuleHandleW(L"ntdll");
    auto nt = (PIMAGE_NT_HEADERS)(m + ((PIMAGE_DOS_HEADER)m)->e_lfanew);
    auto sh = IMAGE_FIRST_SECTION(nt);

    for (DWORD i=0; i<nt->FileHeader.NumberOfSections; i++) {
        if (*(PDWORD)sh[i].Name == *(PDWORD)".rdata") {
            auto rva = sh[i].VirtualAddress;
            auto cnt = (sh[i].Misc.VirtualSize - sizeof(STRING)) / sizeof(ULONG_PTR);
            auto ptr = (PULONG_PTR)(m + rva);

            for (DWORD j=0; j<cnt; j++) {
                if (!IsReadOnlyPtr((LPVOID)ptr[j])) continue;

                auto api = (PSTRING)ptr[j];

                if (api->Length == Callback->Name.Length &&
                    api->MaximumLength == Callback->Name.MaximumLength)
                {
                    if (!strncmp(api->Buffer, Callback->Name.Buffer, Callback->Name.Length)) {
                        Callback->Function.p = (PVOID)ptr[j + 1];
                        return TRUE;
                    }
                }
            }
            break;
        }
    }
    return FALSE;
}

void
GetWow64CallbackTable(PWOW64_CALLBACK_TABLE Table) {
    GetWow64FunctionPointer(&Table->Wow64LdrpInitialize);
    GetWow64FunctionPointer(&Table->Wow64PrepareForException);
    GetWow64FunctionPointer(&Table->Wow64ApcRoutine);
    GetWow64FunctionPointer(&Table->Wow64PrepareForDebuggerAttach);
    GetWow64FunctionPointer(&Table->Wow64SuspendLocalThread);
    GetWow64FunctionPointer(&Table->Wow64SuspendLocalProcess);
}
```

## Summary

This type of code isn’t useful to a 32-Bit WOW process without jumping to 64-Bit since the function pointers are stored in the 64-Bit version of NTDLL. There are potentially other uses though like intercepting APCs, anti-debugging and processing exceptions before VEH or SEH, which FinFisher did successfully for many many years….

[PoC here](https://gist.github.com/odzhan/b4898fa96f36b131973f62b797c4f639)

### Share this:

* [Click to share on X (Opens in new window)
  X](https://modexp.wordpress.com/2023/04/19/finding-the-wow64-callback-table/?share=twitter)
* [Click to share on Facebook (Opens in new window)
  Facebook](https://modexp.wordpress.com/2023/04/19/finding-the-wow64-callback-table/?share=facebook)

Like Loading...

### *Related*

This entry was posted in [assembly](https://modexp.wordpress.com/category/assembly/), [data structures](https://modexp.wordpress.com/category/windows/data-structures-windows/), [programming](https://modexp.wordpress.com/category/programming/), [security](https://modexp.wordpress.com/category/security/), [windows](https://modexp.wordpress.com/category/windows/) and tagged [windows](https://modexp.wordpress.com/tag/windows/), [x64](https://modexp.wordpress.com/tag/x64/), [x86](https://modexp.wordpress.com/tag/x86/). Bookmark the [permalink](https://modexp.wordpress.com/2023/04/19/finding-the-wow64-callback-table/ "Permalink to WOW64 Callback Table (FinFisher)").

[← Shellcode: Linux on RISC-V 64-Bit](https://modexp.wordpress.com/2022/05/02/shellcode-risc-v-linux/)

[Delegated NT DLL →](https://modexp.wordpress.com/2024/02/13/delegated-nt-dll/)

### 1 Response to *WOW64 Callback Table (FinFisher)*

1. Pingback: [Delegated NT DLL | modexp](https://modexp.wordpress.com/2024/02/13/delegated-nt-dll/)

### Leave a comment [Cancel reply](/2023/04/19/finding-the-wow64-callback-table/#respond)

Δ

* Search for:
* ### Recent Posts

  + [Shellcode: Windows on ARM64 / AArch64](https://modexp.wordpress.com/2024/09/16/windows_ar...
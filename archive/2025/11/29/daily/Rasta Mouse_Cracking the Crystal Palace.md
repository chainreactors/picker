---
title: Cracking the Crystal Palace
url: https://rastamouse.me/cracking-the-crystal-palace/
source: Rasta Mouse
date: 2025-11-29
fetch_date: 2025-11-30T03:26:48.264140
---

# Cracking the Crystal Palace

[Rasta Mouse](https://rastamouse.me)

* [Home](https://rastamouse.me/)

29 Nov 2025

3 min read

# Cracking the Crystal Palace

If you follow this blog, you'll know I've been posting about Crystal Palace a LOT recently, mostly from an attack perspective. Today, I thought I'd channel my blue-teamer alter ego and look at Crystal Palace from a defence perspective. That is, are there any easy "tells" that a capability has been loaded by Crystal Palace?

To target Crystal Palace artefacts specifically, I only looked at the "stuff" that it inserts into the final assembly, rather than any code that can be written (or changed) by the user (including LibTCG).

Three possibilities jumped out:

## \_\_tag\_func intrinsic

This intrinsic is used with the `exportfunc` command and `PicoGetExport` function. It's essentially a way for a PICO to export a function and have it be callable by a loader.

```
/* this is the linker intrinsic to get the tag for our exported function */
int __tag_myfunc ( );

void go ( )
{
    ...

    /* call exported function in PICO */
    PicoGetExport ( pico_src, pico_dst, __tag_myfunc ( ) ) );
}
```

Crystal Palace generates a random 'tag' integer at link-time, which is used to identify the export. However, because this is only a single integer, there's not really enough there to identify anything specifically related to Crystal Palace.

## DFR resolver function

Dynamic Function Resolution (DFR) has become a popular convention for referencing APIs in COFFs. Here's an example:

```
WINBASEAPI LPVOID WINAPI KERNEL32$VirtualAlloc ( LPVOID, SIZE_T, DWORD, DWORD );
```

When turning a COFF into PIC, Crystal Palace requires a 'resolver' function that will resolve these references. The user is free to do this however they want, but the Tradecraft Garden samples do it by walking the PEB & EAT.

```
#include "tcg.h"

FARPROC resolve ( DWORD mod_hash, DWORD func_hash )
{
    HANDLE module = findModuleByHash ( mod_hash );
    return findFunctionByHash ( module, func_hash );
}
```

A loader will typically use DFR to load the given capability into memory:

```
void go ( )
{
    char * dll_src = GETRESOURCE ( _DLL_ );

    DLLDATA dll_data;
    ParseDLL ( dll_src, &dll_data );

    char * dll_dst = KERNEL32$VirtualAlloc ( NULL, SizeOfDLL ( &dll_data ), MEM_COMMIT | MEM_RESERVE, PAGE_EXECUTE_READWRITE );

    ...
}
```

When building the final assembly, Crystal Palace rewrites DFR references to calls to this resolve function. So this:

```
488B0500000000       mov       __imp_KERNEL32$VirtualAlloc,%rax
FFD0                 call      *%rax
```

Becomes this:

```
B95BBC4A6A           mov       $0x6A4A`BC5B,%ecx
BA54CAAF91           mov       $0x91AF`CA54,%edx
E8F0000000           call      resolve
```

Unfortunately, a generic `mov ecx, mov edx, call` pattern is wayyyyy too generic to be reliable.

## \_\_resolve\_hook() intrinsic

Don't worry - I saved the best for last. The `__resolve_hook()` intrinsic works with the `addhook` command, and is used to hook the IAT of a DLL as it's being loaded. The idea is to hook functions in a DLL and redirect them to another function in a memory-persistent PIC (or PICO), where evasion tradecraft, such as call stack spoofing, can be implemented.

```
FARPROC WINAPI _GetProcAddress ( HMODULE hModule, LPCSTR lpProcName )
{
    FARPROC result = __resolve_hook ( ror13hash ( lpProcName ) );

    if ( result != NULL ) {
        return result;
    }

    return GetProcAddress( hModule, lpProcName );
}
```

Each hook is defined in a spec file, e.g:

```
addhook "KERNEL32$VirtualAlloc" "_VirtualAlloc"
```

Crystal Palace dynamically inserts every hook at link-time, so:

```
89C1                 mov       %eax,%ecx
E800000000           call      __resolve_hook
```

Becomes something like:

```
89C1                 mov       %eax,%ecx
81F9A8A24DBC         cmp       $0x91AF`CA54,%ecx
7509                 jne       0x0000`0000`0000`0035
488D055F010000       lea       _VirtualAlloc,%rax
EB03                 jmp       0x0000`0000`0000`0038
```

This sequence of instructions is much more concrete and allows us to build a corresponding YARA rule. We obviously want to ignore the specific hashes and addresses, and look for a generic mov, cmp, jne, lea, jmp pattern.

My YARA rules looks like this:

```
rule Windows_Shellcode_CrystalPalace_HookIntrinsic {
    meta:
        author = "Rasta Mouse"
        description = "Identifies Crystal Palace's __resolve_hook() intrinsic"
        threat_name = "Windows.Shellcode.CrystalPalace"
        creation_date = "2025-11-29"
        last_modified = "2025-11-29"
        arch_context = "x86"
        scan_context = "file, memory"
        os = "windows"
        license = "bsd"
    strings:
        $a = { 89 C1 81 F9 ?? ?? ?? ?? 75 ?? 48 8D ?? ?? ?? ?? ?? E? ?? }
    condition:
        all of them
}
```

💡

I'm not a YARA expert and have zero knowledge of best practices when it comes to writing rules.

Testing this rule against the [Hooking TCG sample](https://tradecraftgarden.org/simplehook.html), gives us a nice hit :)

![](https://rastamouse.me/content/images/2025/11/image-3.png)

## +mutate?

Crystal Palace's code mutator introduces noise to make the final output more resilient against signature techniques. It does this by replacing some instructions with one or more instructions that do the same thing.

However, based on my testing, this option is only inserting alternate instructions on each side of this pattern, not within it. Therefore, at the time of writing, this seems like a pretty reliable way of detecting memory-resident PIC that's using Crystal Palace's `__resolve_hook()` intrinsic.

### Published by:

[![Rasta Mouse](https://www.gravatar.com/avatar/2b44f5ca5458931c49e1fa57da6705c1?s=250&r=x&d=mp)](/author/rasta/ "Rasta Mouse")

Rasta Mouse © 2025

* [Sign up](#/portal/)

[Powered by Ghost](https://ghost.org/)
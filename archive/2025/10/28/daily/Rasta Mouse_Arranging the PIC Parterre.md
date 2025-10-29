---
title: Arranging the PIC Parterre
url: https://rastamouse.me/arranging-the-pic-parterre/
source: Rasta Mouse
date: 2025-10-28
fetch_date: 2025-10-29T03:16:21.568732
---

# Arranging the PIC Parterre

[Rasta Mouse](https://rastamouse.me)

* [Home](https://rastamouse.me/)

28 Oct 2025

5 min read

[crystal-palace](/tag/crystal-palace/)

# Arranging the PIC Parterre

Raffi [just released](https://aff-wg.org/2025/10/27/tradecraft-gardens-pic-parterre/) an update to Crystal Palace (CP), so I wanted to write about some of the problems that I think it helps solve for PIC development and where it may take us in the future.

The philosophy of CP is to build evasion tradecraft as PIC that are separate and agnostic to the capability they are applied to. The majority of the [Tradecraft Garden (TCG) samples](https://tradecraftgarden.org/tradecraft.html) demonstrate how a loader can load one or more PICOs that are used to apply evasion tradecraft to a DLL.

💡

A position-independent code object (PICO) is a convention for running COFFs in memory.

The following is an example of a PICO that will display a message box:

```
#include <windows.h>

DECLSPEC_IMPORT int WINAPI USER32$MessageBoxA (HWND hWnd, LPCSTR lpText, LPCSTR lpCaption, UINT uType);

void go() {
    USER32$MessageBoxA(NULL, "Hello World!", "PICO", MB_OK);
}
```

pico.c

To run this PICO, a loader must load it into memory and call its entry point:

```
char * srcPico;
char * dstCode;
char * dstData;

/* get the PICO appended to this loader */
srcPico = GETRESOURCE(__PICO__);

/* allocate memory for the PICO's data and code sections */
dstData = KERNEL32$VirtualAlloc(NULL, PicoDataSize(srcPico), MEM_RESERVE|MEM_COMMIT, PAGE_READWRITE);
dstCode = KERNEL32$VirtualAlloc(NULL, PicoCodeSize(srcPico), MEM_RESERVE|MEM_COMMIT, PAGE_EXECUTE_READWRITE);

/* load the PICO into the allocated memory */
PicoLoad(funcs, srcPico, dstCode, dstData);

/* call its entry point */
PicoEntryPoint(srcPico, dstCode)(NULL);
```

loader.c

💡

`PicoLoad` and `PicoEntryPoint` are provided by `tcg.h`, which is from the [LibTCG](https://tradecraftgarden.org/libtcg.html) shared library.

The corresponding specification file to append the PICO to the loader and output a single PIC blob would look something like this:

```
x64:
  load "bin/loader.x64.o"
    make pic +optimize +gofirst
    dfr "resolve" "ror13"
    mergelib "libtcg.x64.zip"

  load "bin/pico.x64.o"
    make object
    export
    link "my_pico"

  export
```

Loading a PICO is not entirely dissimilar to loading a DLL, in that the loader must resolve any necessary imports (USER32$MessageBoxA in this example). To do this, PicoLoad will call LoadLibraryA to load user32.dll into the process, then GetProcAddress to determine the address of MessageBoxA, and then patches it into the PICO as it's loaded.

I've arrived at the view that a loader cannot solely rely on PICOs for its own evasion tradecraft, because loading PICOs in the first place is a risky and observable action.

## PICOs are the new PIC

If you didn't know - you can actually take a COFF and use `make pic` in a spec file, instead of `make object`, and that will give you a pure PIC blob that you can inject directly into memory without needing a dedicated loader. I've previously shown an example of how to do that [here](https://bsky.app/profile/rastamouse.me/post/3m3xjcfswps2u).

Using a loader is mandatory when loading a DLL due to the requirements of how they need to sit in memory, but PIC has no such restrictions. So if you're only working with PIC, the use of a loader is potentially redundant. If we can just build all our PICOs (including evasion tradecraft) straight to PIC, surely this solves the problem of a noisy loader?

## To load, or not to load (that is the question)

One of the issues with transforming COFFs directly into PIC is that CP's DFR resolution for PIC didn't handle module loads for you (until now). As Raffi noted in his post, the example above would just crash as PIC because user32.dll isn't loaded into a process by default.

I had already set myself on a philosophical debate regarding what should assume the responsibility for module loads - a loader or the PIC. I thought the "correct" answer should be the PIC, but I didn't fancy the idea of having to code a bunch of LoadLibrary calls somewhere. This would further bloat things if you're merging multiple COFFs into a single PIC because each one would have to ensure every module it's dependent on is loaded into the process.

I was on the verge of zig-zagging back to a preference for a loader, because that would provide me with the "central authority" for module loads, which is what I was looking for. But this is where Raffi's latest update has saved us.

### dfr "resolver" "method" "M1, M2"

This is a new way of declaring a DFR resolver function for specific modules, e.g. ones that are loaded by default, such as Kernel32 and NTDLL. Because these are guaranteed to be present, sticking with walking the EAT is functionally fine.

```
char * resolve_explicit(DWORD modHash, DWORD funcHash) {
    char * hModule = (char *)findModuleByHash(modHash);
    return findFunctionByHash(hModule, funcHash);
}
```

💡

This is where the current MessageBoxA PIC example would crash - because user32.dll is not loaded into a process by default, it would not be found in the InMemoryOrderModuleList.

You would define this in a spec file like so:

```
x64:
  load "bin/pico.x64.o"
    make pic +optimize +gofirst
    dfr "resolve_explicit" "ror13" "KERNEL32, NTDLL"
```

### dfr "resolver" "method"

This was previously the only way to declare a DFR resolver function, but can now be used to resolve functions from modules other than those explicitly declared above. Because these are not guaranteed to be loaded, the function needs to handle loading it if it needs to.

```
char * resolve_default(char * mod, char * func) {
  HANDLE hModule = KERNEL32$GetModuleHandleA(mod);
  if (hModule == NULL) {
    hModule = LoadLibraryA(mod);
  }

  return (char *)GetProcAddress(hModule, func);
}
```

This can be added to the spec file like this:

```
x64:
  load "bin/pico.x64.o"
    make pic +optimize +gofirst
    dfr "resolve_explicit" "ror13" "KERNEL32, NTDLL"
    dfr "resolve_default" "strings"
```

So `resolve_explicit` will be used only when resolving functions from Kernel32 and NTDLL, and `resolve_default` will be used for everything else. And as if by magic, this PICO can now be transformed into PIC and handle its own module loads without crashing.

![](https://rastamouse.me/content/images/2025/10/image.png)

## Evasion tradecraft

What I like about this design is that it allows developers to implement any evasion tradecraft for module loads, because they control the resolution functions. For example, I could merge my [threadpool library](https://github.com/rasta-mouse/LibTP) using `mergelib "../../LibTP/libtp.x64.zip"`, and use it to proxy calls to LdrLoadDll via the threadpool.

This is just one alternative to using vanilla LoadLibraryA.

```
HMODULE ldrLoadLibrary(char * module) {
    wchar_t path[64];
    MSVCRT$_snwprintf(path, sizeof(path), L"%S.DLL", module);

    UNICODE_STRING fileName;
    memset(&fileName, 0, sizeof(UNICODE_STRING));
    NTDLL$RtlInitUnicodeString(&fileName, (PCWSTR)(path));

    HANDLE hModule = NULL;

    NTARGS args;
    memset(&args, 0, sizeof(NTARGS));

    args.functionPtr = (ULONG_PTR)(NTDLL$LdrLoadDll);
    args.argument1   = (ULONG_PTR)(0);
    args.argument2   = (ULONG_PTR)(0);
    args.argument3   = (ULONG_PTR)(&fileName);
    args.argument4   = (ULONG_PTR)(&hModule);

    ProxyNtApi(&args);

    return (HMODULE)(hModule);
}

char * resolve_default(char * mod, char * func) {
    HANDLE hModule = KERNEL32$GetModuleHandleA(mod);
    if (hModule == NULL) {
        hModule = ldrLoadLibrary(mod);
    }

    return (char *)GetProcAddress(hModule, func);
}
```

The other nice feature of CP's merge command is that objects "inherit" access to these DFR resolution functions from whichever PICO they're in. This means that every other PICO can just define the DFR references that it needs, and doesn't need to worry about how they are resolved.

The archit...
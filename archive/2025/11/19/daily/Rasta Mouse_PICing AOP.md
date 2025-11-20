---
title: PICing AOP
url: https://rastamouse.me/picing-aop/
source: Rasta Mouse
date: 2025-11-19
fetch_date: 2025-11-20T03:10:21.414233
---

# PICing AOP

[Rasta Mouse](https://rastamouse.me)

* [Home](https://rastamouse.me/)

19 Nov 2025

8 min read

# PICing AOP

The 11.10.25 Crystal Palace release added more new commands in one go than I think I've seen thus far. Many of them seemed really similar at first blush, and it took me a while to get an understanding of where each one is applicable (I failed in that regard). The purpose of this post is to serve as a reference point for myself (and others), because I'm bound to forget if I don't write it down.

I also suggest you read Raffi's original post, as he explains the whole Aspect-Oriented Programming angle with Crystal Palace.

[Tradecraft Engineering with Aspect-Oriented Programming

It’s 2025 and apparently, I’m still a Java programmer. One of the things I never liked about Java’s culture, going back many years ago, was the tendency to hype frameworks that seemed to over-engin…

![](https://rastamouse.me/content/images/icon/cropped-affwgsiteimage_nowreath.png)Adversary Fan Fiction Writers GuildSkip to content

![](https://rastamouse.me/content/images/thumbnail/show-an-image-that-represents-a-hybrid-symbiosis-of-plants-1.png)](https://aff-wg.org/2025/11/10/tradecraft-engineering-with-aspect-oriented-programming/)

## exportfunc

A PICO must currently contain a `go` function, aka an entry point, to be called by a loader using `PicoEntryPoint`. Here's a simple example:

```
DECLSPEC_IMPORT int WINAPI USER32$MessageBoxA ( HWND, LPCSTR, LPCSTR, UINT );

void go ( )
{
    USER32$MessageBoxA ( NULL, "Hello World", "PICO", MB_OK );
}
```

pico.c

```
IMPORTFUNCS funcs;
funcs.GetProcAddress = GetProcAddress;
funcs.LoadLibraryA   = LoadLibraryA;

char * pico_src = GETRESOURCE ( _PICO_ );

char * pico_data = KERNEL32$VirtualAlloc ( NULL, PicoDataSize ( pico_src ), MEM_COMMIT | MEM_RESERVE, PAGE_READWRITE );
char * pico_code = KERNEL32$VirtualAlloc ( NULL, PicoCodeSize ( pico_src ), MEM_COMMIT | MEM_RESERVE, PAGE_EXECUTE_READWRITE );

PicoLoad       ( &funcs, pico_src, pico_code, pico_data );
PicoEntryPoint ( pico_src, pico_code ) ( NULL );
```

loader.c

![](https://rastamouse.me/content/images/2025/11/image-1.png)

Nothing new there. But the new `exportfunc` command provides a way for a loader to call functions in a PICO other than go (think of it like exporting a function from a DLL). This is paired with a new `PicoGetExport` function in `tcg.h` and a 'tag' system.

The following PICO has a function called `test_func`, which is exported using the tag `__tag_testfunc`:

```
void test_func ( )
{
    USER32$MessageBoxA ( NULL, "Test Func", "PICO", MB_OK );
}
```

pico.c

```
x64:
    load "bin/loader.x64.o"
        make pic +gofirst +optimize

    load "bin/pico.x64.o"
        make object +gofirst +optimize
        mergelib "libtcg.x64.zip"
        exportfunc "test_func" "__tag_testfunc"  # export test_func
        export
        link "pico"

    export
```

loader.spec

We then declare a corresponding tag intrinsic in the loader, and pass it to PicoGetExport:

```
/* linker intrinsic */
int __tag_testfunc ( );

void go ( )
{
    IMPORTFUNCS funcs;
    funcs.GetProcAddress = GetProcAddress;
    funcs.LoadLibraryA   = LoadLibraryA;

    char * pico_src = GETRESOURCE ( _PICO_ );

    char * pico_data = KERNEL32$VirtualAlloc ( NULL, PicoDataSize ( pico_src ), MEM_COMMIT | MEM_RESERVE, PAGE_READWRITE );
    char * pico_code = KERNEL32$VirtualAlloc ( NULL, PicoCodeSize ( pico_src ), MEM_COMMIT | MEM_RESERVE, PAGE_EXECUTE_READWRITE );

    PicoLoad ( &funcs, pico_src, pico_code, pico_data );

    /* call test_func */
    PicoGetExport ( pico_src, pico_code, __tag_testfunc ( ) ) ( NULL );
}
```

loader.c

Crystal Palace will replace the intrinsic with whatever tag ID it generated.

![](https://rastamouse.me/content/images/2025/11/image-2.png)

🐛

There's a bug in the 11.10.25 release where tags are not propagated with the `run` command. It will be fixed in a future release.

This is useful when a PICO has multiple setup steps, as they can be separated into different functions (and called at different times), rather than shoehorning them all into go. And given that exportfunc now exists, I suspect the mandatory requirement to have a go function in a PICO could be lifted in the future.

## addhook

The old way to hook API calls was to manually check functions being resolved in GetProcAddress (by hijacking `IMPORTFUNCS`), and then returning pointers to internal functions rather than the legitimate ones. For example:

```
DECLSPEC_IMPORT int WINAPI USER32$MessageBoxA ( HWND, LPCSTR, LPCSTR, UINT );

int WINAPI _MessageBoxA ( HWND hWnd, LPCSTR lpText, LPCSTR lpCaption, UINT uType )
{
    return USER32$MessageBoxA ( hWnd, "You've been hooked", "Hooked", uType );
}

char * WINAPI _GetProcAddress ( HMODULE hModule, LPCSTR lpProcName )
{
    char * result = ( char * ) GetProcAddress ( hModule, lpProcName );

    /*
    * Check to see what function is being resolved.
    * Note that lpProcName may be an ordinal, not a string.
    */

    if ( ( ULONG_PTR ) lpProcName >> 16 == 0 ) {
        /* it's an ordinal */
        return result;
    }

    /* Calculte function hash */
    DWORD h = hash ( ( char * ) lpProcName );

    if ( h == MESSAGEBOXA_HASH ) {
        return ( char * ) _MessageBoxA;
    } else if ( ... ) {
        ...
    } else {
        return result;
    }
}

void go ( IMPORTFUNCS * funcs )
{
    /* make the loader use our custom GetProcAddress */
    funcs->GetProcAddress = ( __typeof__ ( GetProcAddress ) * ) _GetProcAddress;
}
```

As you may imagine, the more hooks you want to add, the more cumbersome this gets. The new `addhook` command allows us to do this in a more automated fashion. It registers a hook for a DFR function with Crystal Palace, which is implemented via a `__resolve_hook ( DWORD func_hash )` intrinsic. That massive \_GetProcAddress function can now be boiled down to:

```
FARPROC WINAPI _GetProcAddress ( HMODULE hModule, LPCSTR lpProcName )
{
    FARPROC result = __resolve_hook ( ror13hash ( lpProcName ) );

    if ( result != NULL ) {
        return result;
    }

    return GetProcAddress ( hModule, lpProcName );
}
```

pico.c

And the hooks are now defined in the spec file:

```
load "bin/pico.x64.o"
    make object +gofirst +optimize
    mergelib "libtcg.x64.zip"
    addhook "USER32$MessageBoxA" "_MessageBoxA" # hook MessageBoxA
    ...
```

loader.spec

Crystal Palace will insert the necessary hash comparisons in the emitted assembly, which look something like this:

```
call  ror13hash
mov   %eax,%ecx
cmp   $0xBC4D`A2A8,%ecx ; 0xBC4DA2A8 is the ROR13 hash for MessageBoxA
lea   _MessageBoxA,%rax
```

![](https://rastamouse.me/content/images/2025/11/image.png)

## filterhooks

The `filterhooks` command is provided as a means to exclude any hooks that are not required for the capability being loaded. For instance, if we specify a bunch of hooks like OpenProcess, VirtualAlloc, WriteProcessMemory, etc, but the loaded DLL doesn't have them in its IAT, then it's unlikely that these hooks will be applicable and the final assembly will be larger than needed.

`filterhooks` walks the imports of the object on the stack (DLL or PICO) and removes any hooks that are not in their respective import tables.

```
push $DLL
    link "dll"

load "bin/hooks.x64.o"
    make object +gofirst +optimize
    mergelib "libtcg.x64.zip"
    addhook "USER32$MessageBoxA"    "_MessageBoxA"
    addhook "KERNEL32$OpenProcess"  "_OpenProcess"
    addhook "KERNEL32$VirtualAlloc" "_VirtualAlloc"
    filterhooks $DLL  # remove any unneeded hooks
    export
    link "pico"
```

If `+optimize` is used and a hook function (e.g. \_OpenProcess) hasn't any other references, then they will be removed from the final PICO. I initially wondered why filterhooks isn't done implicitly, but then I realised that you may not want to remove hooks in case modules and functions are loaded and resolved at runtime (e.g. BOF loads).

## attach

Where `addhook` is intended to be used with a loade...
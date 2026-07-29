---
title: COFF Mixing - Hiding in Plain Sight
url: https://rastamouse.me/coff-mixing/
source: Rasta Mouse
date: 2026-07-28
fetch_date: 2026-07-29T05:04:28.175663
---

# COFF Mixing - Hiding in Plain Sight

[Rasta Mouse](https://rastamouse.me)

* [Home](https://rastamouse.me/)

28 Jul 2026

4 min read

[crystal-palace](/tag/crystal-palace/)

# COFF Mixing - Hiding in Plain Sight

Capabilities written to PICO conventions can be output as PIC, PICOs, or COFFs. These formats typically require some sort of 'runner' to inject them into memory - whether that's a shellcode runner, PICO runner, or COFF/BOF runner. There are several challenges with memory-injected content, including:

* RW/RX memory allocation/flux.
* Unbacked RX memory or janky module stomping.
* Call stack analysis of WinAPI calls.

The [Simple Loader](https://tradecraftgarden.org/simpleobj.html) takes a COFF, turns it into a PICO, and pairs it with a loader. The following call stack is from a memory-injected PICO executing MessageBoxA:

```
 # Child-SP          RetAddr               Call Site
00 0000000d`b7fffc58 00007ff4`dde6002d     USER32!MessageBoxA
01 0000000d`b7fffc60 0000000d`b7fffd50     0x00007ff4`dde6002d
02 0000000d`b7fffc68 00000133`170e1360     0x0000000d`b7fffd50
03 0000000d`b7fffc70 00000000`00000000     0x00000133`170e1360
```

[COFF Mixing](https://tradecraftgarden.org/coffmixing.html) is an idea to mix a capability with benign code and output a PE-ready COFF. Linking said COFF to a PE frees us from memory-injected content as the capability lives in image-backed memory instead.

The following is a basic program that has a PE-ready entry point which just calls the capability.

```
#include <windows.h>

//
// basic pico convention
void go( );

//
// pe-ready entry point
int main( int argc, char * argv[ ] )
{
    go( );
    return 0;
}
```

main.c

The capability is merged with this program via a specification file:

```
capability.x64:
    push $OBJECT
        make coff +optimize +mutate

        load "../simple_pic/bin/services.x64.o"
            merge

        dfr "resolve" "ror13" "KERNEL32, NTDLL"
        dfr "resolve_ext" "strings"

        mergelib "../libtcg/libtcg.x64.zip"

    export

x64:
    .capability
        make coff +unwind

        load "bin/main.x64.o"
            merge

    export
```

mix.spec

This works in two steps:

1. Prepare the capability by merging DFR functionality and optionally perform link-time optimization, mutations, ised surgery, etc.
2. Merge the processed capability into the PE-ready COFF. The `+unwind` option generates the correct .xdata and .pdata sections for stack unwinding to work on x64.

The `cpl` utility can produce the PE-ready COFF, e.g: `cpl link mix.spec ../../demo/test.x64.o out.x64.o`. Then that COFF can be linked to a Windows PE: `x86_64-w64-mingw32-gcc -mwindows out.x64.o -o out.x64.exe`.

Executing the PE produces the following call stack:

```
 # Child-SP          RetAddr               Call Site
00 000000c3`5c1ff9c8 00007ff6`f9aa1932     USER32!MessageBoxA
01 000000c3`5c1ff9d0 00007ff6`f9aa15a9     out_x64+0x1932
02 000000c3`5c1ffa00 00007ff6`f9aa10d9     out_x64+0x15a9
03 000000c3`5c1ffa30 00007ff6`f9aa1436     out_x64+0x10d9
04 000000c3`5c1ffad0 00007ffe`691de957     out_x64+0x1436
05 000000c3`5c1ffb00 00007ffe`6b08ad6c     KERNEL32!BaseThreadInitThunk+0x17
06 000000c3`5c1ffb30 00000000`00000000     ntdll!RtlUserThreadStart+0x2c
```

## Symbols

Opening the PE in a tool like [Binary Ninja](https://binary.ninja/) will reveal symbols that are present in the capability.

![](https://storage.ghost.io/c/36/91/36918caa-651a-469a-9d4d-1ba06e2217bf/content/images/2026/07/image-2.png)

These can be removed frm the COFF using the `strip` command:

```
load "bin/main.x64.o"
    merge

strip "findFunctionByHash, resolve_ext, ParseDLL, go, hash_function, isForwardedFunction, GetDataDirectory, hash_module, findModuleByHash, resolve"
```

💡

Use `coffparse` to get a list of symbols in the COFF.

They will then be harder to identify in the final PE.

![](https://storage.ghost.io/c/36/91/36918caa-651a-469a-9d4d-1ba06e2217bf/content/images/2026/07/image-3.png)

## Function ordering

Instead of just merging a simple PE entry point, you can merge lots more benign code to make the PE look more legitimate. I found a library that contains lots of mathematical functionality.

[GitHub - ohirose/bcpd: Domain Elastic Transform / Bayesian Coherent Point Drift

Domain Elastic Transform / Bayesian Coherent Point Drift - ohirose/bcpd

![](https://storage.ghost.io/c/36/91/36918caa-651a-469a-9d4d-1ba06e2217bf/content/images/icon/favicon-ce0a1f0c-68d8-43c0-8ae7-4618c74bb4c2.svg)GitHubohirose

![](https://opengraph.githubassets.com/2de6113bf64550de5da2a09737ca0c7f4379549cca690af15175c5e694a52561/ohirose/bcpd)](https://github.com/ohirose/bcpd)

I built several of the .c files to their own COFF objects:

```
x64: bin
	$(CC_64) $(CFLAGS) -c src/main.c       -o bin/main.x64.o
	$(CC_64) $(CFLAGS) -c src/digamma.c    -o bin/digamma.x64.o
	$(CC_64) $(CFLAGS) -c src/dijkstra.c   -o bin/dijkstra.x64.o
	$(CC_64) $(CFLAGS) -c src/heap.c       -o bin/heap.x64.o
	$(CC_64) $(CFLAGS) -c src/kernel.c     -o bin/kernel.x64.o
	$(CC_64) $(CFLAGS) -c src/median.c     -o bin/median.x64.o
	$(CC_64) $(CFLAGS) -c src/misc.c       -o bin/misc.x64.o
	$(CC_64) $(CFLAGS) -c src/mt19937-64.c -o bin/mt19937-64.x64.o
	$(CC_64) $(CFLAGS) -c src/stat.c       -o bin/stat.x64.o
	$(CC_64) $(CFLAGS) -c src/util.c       -o bin/util.x64.o
```

Makefile

And then merged each one into the PE-ready COFF:

```
.capability
    make coff +unwind +disco

    load "bin/main.x64.o"
        merge
    load "bin/digamma.x64.o"
        merge
    load "bin/dijkstra.x64.o"
        merge
    load "bin/heap.x64.o"
        merge
    load "bin/kernel.x64.o"
        merge
    load "bin/median.x64.o"
        merge
    load "bin/misc.x64.o"
        merge
    load "bin/mt19937-64.x64.o"
        merge
    load "bin/stat.x64.o"
        merge
    load "bin/util.x64.o"
        merge
```

mix.spec

Adding the `+disco` option means that the capability's code will be randomly shuffled in with the benign code. You can also bury execution of the capability somewhere within the benign code. For example, modify `digamma` to call `go`:

```
double digamma (double x)
{
  double r, f, t;

  r = 0;

  while (x<=5)
  { r -= 1/x;
    x += 1;
  }

  f = 1/(x*x);

  t = f*(-1/12.0 + f*(1/120.0 + f*(-1/252.0 + f*(1/240.0 + f*(-1/132.0
       + f*(691/32760.0 + f*(-1/12.0 + f*3617/8160.0)))))));

  go();
  return r + log(x) - 0.5/x + t;
}
```

digamma.c

Then have `main` call `digamma` instead of `go` directly:

```
#include <windows.h>

double digamma( double x );

int main( int argc, char * argv[ ] )
{
    digamma( 1 );
    return 0;
}
```

That doesn't do much from a call stack perspective but it may make analysis of a PE more complicated.

## Conclusion

COFF mixing presents the opportunity to leverage capabilities without the presumption (and IOCs) of memory-injected content. This doesn't make sense for every scenario - memory injection is still useful - but for situations where injecting capabilities isn't required, and may just introduce more IOCs, COFF mixing is certainly an interesting alternative.

### Published by:

[![Rasta Mouse](https://www.gravatar.com/avatar/2b44f5ca5458931c49e1fa57da6705c1?s=250&r=x&d=mp)](/author/rasta/ "Rasta Mouse")

### You might also like...

06

Jul

## Hook Chains (how I built Crystal Kit incorrectly\*)

3 min read

05

Jun

## BOF Cocktails in Cobalt Strike

2 min read

26

May

## Module Stomping PIC

4 min read

25

Apr

## Atomic BOFs

5 min read

09

Apr

## Crystal Mask

8 min read

Rasta Mouse © 2026

* [Sign up](#/portal/)

[Powered by Ghost](https://ghost.org/)
---
title: Debugging the Tradecraft Garden
url: https://rastamouse.me/debugging-the-tradecraft-garden/
source: Rasta Mouse
date: 2025-07-26
fetch_date: 2025-10-06T23:55:42.753818
---

# Debugging the Tradecraft Garden

[Rasta Mouse](https://rastamouse.me)

* [Home](https://rastamouse.me/)

25 Jul 2025

7 min read

# Debugging the Tradecraft Garden

The suggested way to get started with Crystal Palace and the Tradecraft Garden projects is through the Windows Subsystem for Linux (WSL) on Windows. If you don't know what WSL is (where have you been!?) the tl;dr is that it's a compatibility layer for running a Linux environment directly on top of Windows, without the need for a VM or to dual-boot.

If you're familiar with Raffi's work, then you'll know that his preference is generally to write everything on Linux, usually just in nano, and cross-compile for Windows. The TCG [setup guide](https://tradecraftgarden.org/wslsetup.html) therefore has you install the `mingw-w64` cross-compiler and `make` for building TCG projects; and the Java `openjdk` for running Crystal Palace; all inside an Ubuntu WSL instance.

As a bare-minimum dev environment, this undoubtedly works really well. However, there are two aspects of development that I find really difficult to adapt to, and that's 1) not having any intellisense; and 2) not having a managed debugger. My goal for this post was to see if I could improve my QoL when working with the TCG, but in a way that respects the original setup guidance.

## Visual Studio Code

I find Visual Studio Code to be a nice middle-ground between a text-based editor like nano, and a full-fat IDE like Visual Studio, CLion, Rider, etc. However, if you launch vscode in Windows and open a TCG project, you'll likely be greeted with a litany of errors.

![](https://rastamouse.me/content/images/2025/07/image-6.png)

This is because the TCG is specifically written for MinGW, and we don't have that installed in Windows (at least I don't). My vscode tries to use cl.exe instead, which is Microsoft's MSVC compiler & linker, and this doesn't support things like `__attribute__` or `__typeof__`, hence all the errors.

Here is where I discovered the magic of the [WSL vscode extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl). One of its key features for us is in allowing access to compilers in the WSL environment, without needing modify the Windows environment. That means we can have vscode use the mingw compiler that is already installed in WSL as per the TCG setup. Once the extension is installed, you can activate 'remote mode' either by running vscode directly from a WSL command prompt:

```
daniel@RastaPad:/mnt/c/Tools/tcg/simple_rdll$ code .
```

Or by running it from Windows first, clicking on the blue icon in the bottom-left, and then selecting the WSL instance you want to connect to.

![](https://rastamouse.me/content/images/2025/07/image-7.png)

Once connected, you'll see all the project files, hopefully no code errors, full intellisense, and a WSL terminal as though the instance of vscode was running inside Linux.

![](https://rastamouse.me/content/images/2025/07/image-9.png)

Beautiful.

I wasn't able to get debugging working directly inside vscode with this setup. I think this is some limitation with GDB trying to debug a Windows PE on Linux. You may be able to debug via Wine or something, but ugh. If this isn't the case and you know how to make it work, do let me know.

## Debug Builds

The next best solution that I could think of was to produce a debuggable executable that I could use with WinDbg (other debuggers are available). The way I did this was to add a new 'debug' build to the Makefile. Adding the `-g` option embeds the required debug information; and then we can link it to an executable build, specifying 'go' as the entry point.

```
CC_64=x86_64-w64-mingw32-gcc

all: bin/loader.x86.o bin/loader.x64.o
debug: bin/loader.x64.exe

bin:
	mkdir bin

...

bin/loader.x64.exe: bin
	$(CC_64) -DWIN_X64 -shared -g -masm=intel -Wall -Wno-pointer-arith -c src/loader.c -o bin/loader.x64.o
	$(CC_64) -DWIN_X64 -nostartfiles -g -Wl,-e,go bin/loader.x64.o -o bin/loader.x64.exe
```

Makefile

```
$ make clean; make debug
rm -f bin/*
x86_64-w64-mingw32-gcc -DWIN_X64 -shared -g -masm=intel -Wall -Wno-pointer-arith -c src/loader.c -o bin/loader.x64.o
x86_64-w64-mingw32-gcc -DWIN_X64 -nostartfiles -g -Wl,-e,go bin/loader.x64.o -o bin/loader.x64.exe

$ ls -l bin/
total 44
-rwxrwxrwx 1 daniel daniel 24400 Jul 24 22:03 loader.x64.exe
-rwxrwxrwx 1 daniel daniel 20410 Jul 24 22:03 loader.x64.o
```

Then in WinDbg's settings, add the path to the loader's source code under debugging paths.

![](https://rastamouse.me/content/images/2025/07/image-10.png)

And then after launching the loader executable, you can place breakpoints, etc, and away you go.

![](https://rastamouse.me/content/images/2025/07/image-11.png)

The astute will notice that we don't actually have an appended DLL to load, because that would normally get linked in by Crystal Palace. That's ok - we can grab `test.x64.dll` from the CP distribution and use `xxd` to dump it to a C include-style array.

```
$ xxd -i test.x64.dll

unsigned char debug_dll[] = {
  0x4d, 0x5a, 0x90, 0x00, 0x03, 0x00, 0x00, 0x00, 0x04, 0x00, 0x00, 0x00,
  ...
};
```

Create a new header file, `debug.x64.h`, with this content and use a `DEBUG` preprocessor directive to build it in as needed.

```
#ifdef DEBUG
#ifdef WIN_X64
#include "debug.x64.h"
#else
#include "debug.x86.h"
#endif
#endif

...

char * findAppendedDLL() {
#ifdef DEBUG
	return (char*)debug_dll;
#else
	return (char *)&__DLLDATA__;
#endif
}
```

loader.c

💡

Don't forget to add `-DDEBUG` to the Makefile for the debug builds.

After building the executable again, we can debug it end-to-end.

![](https://rastamouse.me/content/images/2025/07/image-12.png)

## Debugging COFFs

I didn't have much hope of being able to debug COFFs like this, owing to the `MODULE$Function` (DFR) convention for linking to Win32 APIs. This is a custom convention that Raffi originally used in Cobalt Strike's BOFs, and now here again in Crystal Palace.

```
#include <windows.h>

WINBASEAPI VOID WINAPI USER32$MessageBoxW(HWND hWnd, LPCWSTR lpText, LPCWSTR lpCaption, UINT uType);

void go() {
    USER32$MessageBoxW(NULL, L"Hello World", L"PICO", MB_OK);
}
```

test.c

Standard linkers cannot handle this, so the build just throws an error.

```
/usr/bin/x86_64-w64-mingw32-ld: bin/test.x64.o: in function `go':
/mnt/c/Tools/tcg/simple_rdll/src/test.c:6:(.text+0x27): undefined reference to `__imp_USER32$MessageBoxW'
collect2: error: ld returned 1 exit status
```

The simplest way I could think of to deal with this is by using a preprocessor directive to only define the DFR when *not* in debug. When in debug, the linker will identify MessageBoxW and link to the legitimate function in user32 instead.

```
#include <windows.h>

#ifndef DEBUG
WINBASEAPI VOID WINAPI USER32$MessageBoxW(HWND hWnd, LPCWSTR lpText, LPCWSTR lpCaption, UINT uType);
#define MessageBoxW USER32$MessageBoxW
#endif

void go() {
    MessageBoxW(NULL, L"Hello World", L"PICO", MB_OK);
}
```

test.c

This is obviously quite ugly, so a more ergonomic solution may be to come up with a DFR macro like the [Cobalt Strike BOF template](https://github.com/Cobalt-Strike/bof-vs/blob/main/BOF-Template/base/helpers.h) has. Either way, linking the COFF to an executable in the same way above does allow WinDbg to debug it.

![](https://rastamouse.me/content/images/2025/07/image-13.png)

## Debugging PICOs?

I find myself dropping into a habit of using the terms COFF and PICO interchangeably, but this isn't accurate. A COFF is the artefact produced by the compiler and a PICO is what Crystal Palace produces from a COFF. That means you cannot take a COFF and attempt to run it in a loader (via `PicoLoad`/`PicoEntryPoint`).

A PICO is produced via a spec file, where you'd do something like:

```
x64:
  load "bin/loader.x64.o"
    make pic

  load "bin/test.x64.o"
    make object
	export
	link "test_pico"

export
```

You can technically write a spec file that will produce a PICO from a COFF, without linking it to a load...
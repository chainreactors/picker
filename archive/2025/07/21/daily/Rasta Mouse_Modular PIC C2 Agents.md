---
title: Modular PIC C2 Agents
url: https://rastamouse.me/modular-pic-c2-agents/
source: Rasta Mouse
date: 2025-07-21
fetch_date: 2025-10-06T23:24:23.389344
---

# Modular PIC C2 Agents

[Rasta Mouse](https://rastamouse.me)

* [Home](https://rastamouse.me/)

20 Jul 2025

9 min read

# Modular PIC C2 Agents

All post-exploitation C2 agents that I'm aware of are implemented as a single rDLL or PIC blob. This means that all of their core logic such as check-in's, processing tasks, sending output, etc, are all mashed into a single executable blob. If an agent is implemented as an rDLL, then it is also mapped into memory in a predictable way (i.e. each section is written to an RVA from the PE's base address, as defined by the section headers).

[Crystal Palace](https://tradecraftgarden.org/crystalpalace.html) provides loading capabilities that are written as "Position-Independent Code Objects", aka PICOs, as an alternative to DLLs (although it supports DLLs as well). One of the benefits of PICOs over DLLs is that you have more flexibility in where they are loaded into memory. For instance, the data section of a PICO does not have to live adjacent to its executable section. And if you have multiple PICOs that interact with each other, they can all be living in completely disparate regions of memory.

This makes it possible (at least in theory) to write a C2 agent that is made up of multiple individual PICOs, rather than a singular monolithic DLL or PIC code base. Each PICO could be responsible for a single aspect of the agent's functionality; e.g. for check-in, task processing, evasion capabilities, and so on. This architecture would also allow authors to easily swap out different PICOs depending on their needs; e.g. swap an HTTP-comms PICO with an SMB one; swap out one stack spoofing implementation for another, and so on.

The intention of this post is to show how the Crystal Palace ecosystem can facilitate this design. I will demonstrate how to load multiple PICOs from a loader, how one PICO can execute code in another PICO, and how you can dynamically patch data into a PICO at link-time.

## PICOs

First - what are PICOs? [PICOs](https://tradecraftgarden.org/docs.html#picos) are a Crystal Palace convention for embedding and running COFF files. They are an abstraction above PIC with lots of conveniences restored, such as being able to use strings and constants, as well as a calling convention for Win32 APIs.

Here's an example of a simple 'hello world' PICO.

```
#include <windows.h>

WINBASEAPI int WINAPI USER32$MessageBoxW (HWND hWnd, LPCWSTR lpText, LPCWSTR lpCaption, UINT uType);

void go() {
    USER32$MessageBoxW(NULL, L"Hello World!", L"PICO", MB_OK);
}
```

msgbox.c

These can be built as object files (COFFs) as x86 and x64 using mingw32.

```
x86_64-w64-mingw32-gcc -DWIN_X64 -shared -masm=intel -Wall -Wno-pointer-arith -c src/msgbox.c -o bin/msgbox.x64.o
i686-w64-mingw32-gcc -DWIN_X86 -shared -masm=intel -Wall -Wno-pointer-arith -c src/msgbox.c -o bin/msgbox.x86.o
```

## Reflective Loader

This PICO can be appended to a Crystal Palace reflective loader. The loader will locate the PICO at runtime, write its data and code sections into two different regions of memory, (perform some other bits of magic), and then call its entry point.

```
/*
 * Copyright (C) 2025 Raphael Mudge, Adversary Fan Fiction Writers Guild
 *
 * This file is part of Tradecraft Garden
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License along
 *  with this program; if not, see <https://www.gnu.org/licenses/>.
 */

/* function prototypes */
void ReflectiveLoader();

/* this is the REAL entry point to this whole mess and it needs to go first! */
__attribute__((noinline, no_reorder)) void go() {
	ReflectiveLoader();
}

/*
 * loader.h is a refactored Reflective Loader and some macros/definitions we need.
 * it has several functions intended to be used across loaders.
 */
#include "loaderdefs.h"
#include "loader.h"

/* header to run picos */
#include "picorun.h"

/*
 * implementations of findFunctionByHash and findModulebyHash by walking the
 * Export Address Table.
 */
#include "resolve_eat.h"

/* build a table of functions we need */
#define WIN32_FUNC( x ) __typeof__( x ) * x

typedef struct {
	WIN32_FUNC(LoadLibraryA);
	WIN32_FUNC(GetProcAddress);
	WIN32_FUNC(VirtualAlloc);
} WIN32FUNCS;

/*
 * Need other hashes?
 *
 * https://github.com/ihack4falafel/ROR13HashGenerator
 */
#define KERNEL32DLL_HASH	0x6A4ABC5B
#define LOADLIBRARYA_HASH	0xEC0E4E8E
#define GETPROCADDRESS_HASH	0x7C0DFCAA
#define VIRTUALALLOC_HASH	0x91AFCA54

void resolveFunctions(WIN32FUNCS * funcs) {

	char * hModule = (char *)findModuleByHash(KERNEL32DLL_HASH);

	funcs->LoadLibraryA   = (__typeof__(LoadLibraryA) *)   findFunctionByHash(hModule, LOADLIBRARYA_HASH);
	funcs->GetProcAddress = (__typeof__(GetProcAddress) *) findFunctionByHash(hModule, GETPROCADDRESS_HASH);
 	funcs->VirtualAlloc   = (__typeof__(VirtualAlloc) *)   findFunctionByHash(hModule, VIRTUALALLOC_HASH);
}

/*
 * This is the Crystal Palace convention for getting data linked with this loader.
 */
char __MSGBOXPICO__[0] __attribute__((section("msgbox_pico")));

#ifdef WIN_X86
__declspec(noinline) ULONG_PTR caller( VOID ) { return (ULONG_PTR)WIN_GET_CALLER(); }

char * getMsgBoxPICO() {
	return PTR_OFFSET(caller(), (ULONG_PTR)&__MSGBOXPICO__ + 5);
}
#else
char * getMsgBoxPICO() {
	return (char *)&__MSGBOXPICO__;
}
#endif

/* Reflective loader logic */
void ReflectiveLoader() {

	WIN32FUNCS   funcs;

	char       * pico;
	char       * dstData;
	char       * dstCode;

	/* resolve win32 functions */
	resolveFunctions(&funcs);

	/* find our PICO appended to this loader */
	pico = getMsgBoxPICO();

	/* allocate memory for the PICO */
	dstData = funcs.VirtualAlloc(NULL, PicoDataSize(pico), MEM_RESERVE|MEM_COMMIT|MEM_TOP_DOWN, PAGE_READWRITE);
	dstCode = funcs.VirtualAlloc(NULL, PicoCodeSize(pico), MEM_RESERVE|MEM_COMMIT|MEM_TOP_DOWN, PAGE_EXECUTE_READWRITE);

	/* load the PICO into destination address */
	PicoLoad((IMPORTFUNCS *)&funcs, pico, dstCode, dstData);

	/* execute the PICO */
	PicoEntryPoint(pico, dstCode) (NULL);
}
```

loader.c

I think most of this is straight-forward if you've worked with a reflective loader before. As you can probably see, the somewhat unique part to Crystal Palace is the "placeholder" to reference the PICO that will be linked.

```
char __MSGBOXPICO__[0] __attribute__((section("msgbox_pico")));
```

The `PicoCodeSize`, `PicoLoad`, and `PicoEntryPoint` functions are provided by `picorun.h`. This code is included in the [Tradecraft Garden samples](https://tradecraftgarden.org/tradecraft.html), so I won't explain their functionality in detail here. Essentially, each embedded PICO is prepended with a small data stub that helps the loader figure out how large the PICO is, and where its code and data sections are.

## Specification Files

Crystal Palace uses [specification files](https://tradecraftgarden.org/docs.html#specfiles) to link one or more PICOs (and/or DLLs) to a loader. The following is a basic example with comments for each line.

```
name     "Modular PICOs"
author   "Rasta Mouse"

x86:
	load "bin/loader.x86.o"			# read loader.x86.o from disk
		make pic					# turn it into PIC

		load "bin/msgbox.x86.o"		# read msgbox.x86.o from disk
			make object				# turn it into a PICO
			export					# convert PICO into raw bytes
			link "msgbox_pico"		# link PICO bytes to the __MSGBOXPICO__ section defined in the loader

		export						# export the combined loader + PICO blob

x64:
	load "bin/loader.x64.o"			# read loader.x64.o from disk
		make pic					# turn it into PIC

		load "bin/msgbox.x64.o...
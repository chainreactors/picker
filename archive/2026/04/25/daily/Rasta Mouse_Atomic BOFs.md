---
title: Atomic BOFs
url: https://rastamouse.me/atomic-bofs/
source: Rasta Mouse
date: 2026-04-25
fetch_date: 2026-04-26T05:03:33.350724
---

# Atomic BOFs

[Rasta Mouse](https://rastamouse.me)

* [Home](https://rastamouse.me/)

25 Apr 2026

5 min read

[crystal-palace](/tag/crystal-palace/)

# Atomic BOFs

## tl;dr

Inspired by Red Canary's [Atomic Red Team](https://github.com/redcanaryco/atomic-red-team), 'Atomic BOFs' is my attempt at an implementation pattern to ease detection engineering for Beacon Object Files.

[GitHub - rasta-mouse/atomic-bofs: Atomic test units for BOF execution

Atomic test units for BOF execution. Contribute to rasta-mouse/atomic-bofs development by creating an account on GitHub.

![](https://static.ghost.org/v5.0.0/images/link-icon.svg)GitHubrasta-mouse

![](https://storage.ghost.io/c/36/91/36918caa-651a-469a-9d4d-1ba06e2217bf/content/images/thumbnail/atomic-bofs)](https://github.com/rasta-mouse/atomic-bofs)

This project leverages two design ideas.

### BOF Inversions

A BOF is an object (COFF) file that's loaded by a C2 (such as Cobalt Strike) and linked to Win32 API, as well as some internal Beacon APIs. The implementation of those internal APIs live inside the Beacon agent, which makes a BOF dependent on it for execution. Practically every COFF/BOF loader project I've seen, such as TrustedSec's [COFFLoader](https://github.com/trustedsec/COFFLoader), includes a [compatibility layer](https://github.com/trustedsec/COFFLoader/blob/main/beacon_compatibility.c) that implements these functions for the BOF to call instead. [BOF Inversions](https://aff-wg.org/2026/04/13/small-pic-energy/) flips this around by merging the API implementations into the BOF instead of having them in the loader or C2 agent.

### BOF Cocktails

Cobalt Strike's BOF APIs include functions like `BeaconVirtualAlloc`. The idea behind these is to expose Beacon's evasion capabilities (such as syscalls) to BOFs. However, as above, this makes the BOF dependent on the C2 agent for evasion. [BOF Cocktails](https://rastamouse.me/bof-cocktails/) flips this by merging evasion tradecraft directly into the BOF.

### So what?

The outcome of these two ideas is that BOFs suddenly become 'self-contained', and no longer require a C2 agent to achieve equivalent functionality. By extension, self-contained units are far easier to use as test cases. The primary goal was to provide a means for detection engineers to execute BOFs within their test/analysis environments, without having the overhead of a whole C2 setup.

### The Harness

The meat and potatoes of the project is a simple BOF loader, which I called the 'harness'. This is responsible for loading a COFF into memory, calling its entry point, and passing any packed arguments.

```
#include <windows.h>
#include "loader.h"
#include "tcg.h"

DECLSPEC_IMPORT LPVOID WINAPI KERNEL32$VirtualAlloc   ( LPVOID, SIZE_T, DWORD, DWORD );
DECLSPEC_IMPORT BOOL   WINAPI KERNEL32$VirtualProtect ( LPVOID, SIZE_T, DWORD, PDWORD );

char _COFF_ [ 0 ] __attribute__ ( ( section ( "coff" ) ) );
char _ARGS_ [ 0 ] __attribute__ ( ( section ( "args" ) ) );

void go ( )
{
    RESOURCE * src  = GETRESOURCE ( _COFF_ );

    char * code = KERNEL32$VirtualAlloc ( NULL, PicoCodeSize ( src->val ), MEM_RESERVE | MEM_COMMIT, PAGE_EXECUTE_READWRITE );
    char * data = KERNEL32$VirtualAlloc ( NULL, PicoDataSize ( src->val ), MEM_RESERVE | MEM_COMMIT, PAGE_READWRITE );

    IMPORTFUNCS funcs;
    funcs.GetProcAddress = GetProcAddress;
    funcs.LoadLibraryA   = LoadLibraryA;

    PicoLoad ( ( IMPORTFUNCS * ) &funcs, src->val, code, data );

    RESOURCE * args = GETRESOURCE ( _ARGS_ );

    ( ( BOFMAIN ) PicoEntryPoint ( src->val, code ) ) ( args->val, args->len );
}
```

loader.c

Its corresponding spec file expects to receive `$COFF` and `$ARGS` variables, where `$COFF` are the bytes of a COFF file and `$ARGS` are packed arguments. There's also a variable called `%entrypoint` that will contain the BOF's entry point (typically `go`).

```
x64:
    load "bin/loader.x64.o"
        make pic +gofirst +optimize
        run "services.spec"
        mergelib "libtcg.x64.zip"

        push $COFF
            make object +optimize
            run "bof.spec" %entrypoint
            export
            preplen
            link "coff"

        push $ARGS
            preplen
            link "args"

    export
```

The BOF Inversion magic happens in `bof.spec`. First, we have `bofapi.c` that implements the BOF APIs, such as `BeaconDataParse`.

```
void BeaconDataParse ( datap * parser, char * buffer, int size )
{
    parser->original = buffer;
    parser->buffer   = buffer;
    parser->length   = size;
    parser->size     = size;
}

... etc ...
```

bofapi.c

The spec file merges these functions into the BOF and redirects any calls to them.

```
x64:
    entry %1

    load "bin/bofapi.x64.o"
        merge

    attach "$BeaconDataExtract"    "BeaconDataExtract"
    attach "$BeaconDataLength"     "BeaconDataLength"
    attach "$BeaconDataParse"      "BeaconDataParse"
    attach "$BeaconDataPtr"        "BeaconDataPtr"
    attach "$BeaconDataInt"        "BeaconDataInt"
    attach "$BeaconDataShort"      "BeaconDataShort"

    attach "$BeaconFormatAlloc"    "BeaconFormatAlloc"
    attach "$BeaconFormatReset"    "BeaconFormatReset"
    attach "$BeaconFormatAppend"   "BeaconFormatAppend"
    attach "$BeaconFormatPrintf"   "BeaconFormatPrintf"
    attach "$BeaconFormatToString" "BeaconFormatToString"
    attach "$BeaconFormatFree"     "BeaconFormatFree"
    attach "$BeaconFormatInt"      "BeaconFormatInt"
    attach "$BeaconPrintf"         "BeaconPrintf"
    attach "$BeaconOutput"         "BeaconOutput"
```

bof.spec

My intention is that a consumer of the project will not need to change anything related to the harness, as any changes can be made in other spec files (as I'll describe below).

### Test BOF

As a simple test, I've included a small piece of C that simply prints a message using `BeaconPrintf`.

```
#include <windows.h>
#include "beacon.h"

void go ( char * args, int len )
{
    datap parser;
    BeaconDataParse ( &parser, args, len );

    char * message = BeaconDataExtract ( &parser, NULL );

    BeaconPrintf ( CALLBACK_OUTPUT, "%s\n", message );
}
```

test.c

A `config.spec` file is used to configure the harness. This is where the `$COFF`, `$ARGS`, and `%entrypoint` variables need to be set.

```
x64:
    # load your coff
    load $COFF "bin/test.x64.o"

    # pack args
    pack $ARGS "iz" "16" "Hello World x64"

    # if none, pack 0
    # pack $ARGS "b" "0x0"

    # set desired entry point
    setg "%entrypoint" "go"
```

config.spec

To produce the final PIC, use Crystal Palace's `piclink` utility:

```
atomic-bofs$ ./piclink harness/loader.spec x64 test.x64.bin @test/config.spec
```

We are providing the harness' `loader.spec` as the main spec file, but the 'test' `config.spec` file to add the configurations to it. The output will be a `.bin` file that you can execute with any shellcode runner.

```
atomic-bofs$ /mnt/c/Tools/cpl/demo/run.x64.exe test.x64.bin
Allocated 0x00000199df9f0000 (1611 bytes) for PIC
Read 1611 bytes from test.x64.bin. Press 'enter' to continue.

BeaconOutput[0]: Hello World x64
```

### 3rd Party BOFs

The other example in the project uses the whoami BOF from TrustedSec's [CS-Situational-Awareness-BOF](https://github.com/trustedsec/CS-Situational-Awareness-BOF/tree/master) repo. This one demonstrates how BOF Cocktails can be used to change the default behaviour of a BOF.

`hooks.c` contains a single hook for `KERNEL32$GetCurrentProcess`:

```
#include <windows.h>

HANDLE _GetCurrentProcess ( )
{
    /* return pseudo handle directly */
    return ( HANDLE ) ( -1 );
}
```

hooks.c

The `hooks.spec` file merges this function into the COFF and hooks the Win32 API calls.

```
x64:
    load "../bin/hooks.x64.o"
        merge

    attach "KERNEL32$GetCurrentProcess" "_GetCurrentProcess"
```

hooks.spec

Finally, the `config.spec` file leverages Crystal Palace's `setg`, `resolve`, and `before` commands.

```
x64:
    load $COFF "whoami.x64.o"
    pack $ARGS "b" "0x0"
    setg "%entrypoint" "...
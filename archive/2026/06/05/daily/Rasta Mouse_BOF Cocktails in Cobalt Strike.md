---
title: BOF Cocktails in Cobalt Strike
url: https://rastamouse.me/bof-cocktails-in-cobalt-strike/
source: Rasta Mouse
date: 2026-06-05
fetch_date: 2026-06-06T05:51:30.537095
---

# BOF Cocktails in Cobalt Strike

[Rasta Mouse](https://rastamouse.me)

* [Home](https://rastamouse.me/)

05 Jun 2026

2 min read

[cobalt-strike](/tag/cobalt-strike/)

# BOF Cocktails in Cobalt Strike

In a previous post, I wrote about [BOF Cocktails](https://rastamouse.me/bof-cocktails/) - an execution pattern to merge tradecraft into postex BOFs so they didn't have to rely on an agent/loader for their evasion. That post outlines the problem areas more fully, so I encourage you to read that first.

At the time, Cobalt Strike did not have a nice way to intercept BOF execution, so we had to hack around it using `alias_clear` to override commands exposed by other Aggressor scripts. Fortunately, as was announced in the CS 4.13 release party [webinar](https://www.cobaltstrike.com/resources/videos/cobalt-strike-technical-walkthrough), Cobalt Strike has a new Aggressor hook called **BEACON\_INLINE\_EXECUTE**. Thank you for reading my blog CS team 😄.

💡

I will link to the documentation when it's published.

This hook is fired whenever Beacon is instructed to execute a BOF and presents the opportunity for operators to perform actions/processing on it before it's sent to Beacon.

The hook receives the original BOF in raw bytes, `$1`, and expects us to return a modified BOF, also in raw bytes. When using Crystal Palace, we process it through a specification file and return the transformed object.

```
import crystalpalace.spec.* from: crystalpalace.jar;
import java.util.HashMap;

# $1 - raw BOF bytes
set BEACON_INLINE_EXECUTE
{
    local( '$bof $spec_path $spec $capability $final' );

    $bof = $1;

    $spec_path  = script_resource( "cocktail.spec" );
    $spec       = [ LinkSpec Parse: $spec_path ];
    $capability = [ Capability Parse: cast( $bof, 'b' ) ];
    $final      = [ $spec run: $capability, [ new HashMap ] ];

    return $final;
}
```

cocktail.cna

You're free to do anything you want in the spec file. The following is a simple example of instrumenting calls to OpenProcessToken.

```
x86:
    push $OBJECT              # grab the bof
        make coff +optimize   # turn it into a coff-exporter object

    load "bin/hooks.x86.o"    # grab the hooks
        merge                 # merge with the bof

    mergelib "libtcg.x86.zip" # merge the tcg library

    attach "ADVAPI32$OpenProcessToken" "__OpenProcessToken"  # add a hook

    export  # export the merged bof

x64:
    push $OBJECT
        make coff +optimize

    load "bin/hooks.x64.o"
        merge

    mergelib "libtcg.x64.zip"

    attach "ADVAPI32$OpenProcessToken" "_OpenProcessToken"

    export
```

cocktail.spec

```
#include <windows.h>
#include "tcg.h"

DECLSPEC_IMPORT BOOL WINAPI ADVAPI32$OpenProcessToken( HANDLE, DWORD, PHANDLE );

BOOL WINAPI _OpenProcessToken( HANDLE ProcessHandle, DWORD DesiredAccess, PHANDLE TokenHandle )
{
    dprintf( "[*] _OpenProcessToken\n" );
    dprintf( "  -> ProcessHandle: 0x%p\n", ProcessHandle );
    dprintf( "  -> DesiredAccess: %d\n", DesiredAccess );

    return ADVAPI32$OpenProcessToken( ProcessHandle, DesiredAccess, TokenHandle );
}
```

hooks.c

![](https://storage.ghost.io/c/36/91/36918caa-651a-469a-9d4d-1ba06e2217bf/content/images/2026/06/image-1.png)

There's no much else to say other than thanks for the feature 👍

### Published by:

[![Rasta Mouse](https://www.gravatar.com/avatar/2b44f5ca5458931c49e1fa57da6705c1?s=250&r=x&d=mp)](/author/rasta/ "Rasta Mouse")

### You might also like...

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

04

Mar

## Islands of Invariance

6 min read

03

Jan

## BOF Cocktails

5 min read

Rasta Mouse © 2026

* [Sign up](#/portal/)

[Powered by Ghost](https://ghost.org/)
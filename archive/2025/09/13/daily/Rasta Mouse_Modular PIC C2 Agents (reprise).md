---
title: Modular PIC C2 Agents (reprise)
url: https://rastamouse.me/modular-pic-c2-agents-reprise/
source: Rasta Mouse
date: 2025-09-13
fetch_date: 2025-10-02T20:07:25.907853
---

# Modular PIC C2 Agents (reprise)

[Rasta Mouse](https://rastamouse.me)

* [Home](https://rastamouse.me/)

12 Sep 2025

2 min read

# Modular PIC C2 Agents (reprise)

A few months ago, I published a post called [Modular PIC C2 Agents](https://rastamouse.me/modular-pic-c2-agents/) where I mused about what it could look like to build a C2 agent out of individual (modular) COFFs. The idea was to build a capability by swapping interchangeable parts in and out based on the requirements of the agent.

The process was a little convoluted to say the least, involved some abuses of Crystal Palace, and put a lot of heavy lifting on the reflective loader. However, Raffi has since made some [changes](https://aff-wg.org/2025/09/10/coffing-out-the-night-soil/) that make this a lot easier.

## COFF Merging

In my previous attempt, I had the reflective loader load each PICO individually and patch in the relevant function pointers at load-time (i.e. load PICO 1, then load PICO 2 and patch in a pointer to a function within PICO 1).

The latest version of Crystal Palace introduces new `make coff` and `merge` commands. `make coff` will turn the data on the current stack into something called a COFF "exporter". This is a construct that I like to think of as a stack of COFFs. You can add multiple COFFs to the stack and then `export` them.

For example, the following spec will merge `coff1.x64.o` and `coff2.x64.o` into a single blob:

```
name     "Merge COFFs"
author   "Rasta Mouse"

x64:
    load "bin/coff1.x64.o"    # load first coff
        make coff             # create coff exporter

    load "bin/coff2.x64.o"    # loader second coff
        merge                 # merge it with the first

    export                    export merged coff
```

merge.spec

The output of this are the raw bytes of the merged COFF. And because Crystal Palace is a linker, it will do the heavy lifting in linking functions together. The result is a fully-functional and self-contained COFF.

For example, if COFF2 had a function called `show_message`:

```
#include <windows.h>

WINBASEAPI int WINAPI USER32$MessageBoxW (HWND hWnd, LPCWSTR lpText, LPCWSTR lpCaption, UINT uType);

void show_message(LPCWSTR lpText) {
    /* call Win32 API*/
    USER32$MessageBoxW(NULL, lpText, L"Merged", MB_OK);
}
```

coff2.c

Then COFF1 can just call it.

```
#include <windows.h>

extern void show_message(LPCWSTR lpText);

void go() {
    show_message(L"Hello World");
}
```

coff1.c

You don't need headers or even the `extern` declaration (although the compiler will give you warnings without it). The merged COFF can then be saved to disk, or turned into a PICO and given to a reflective loader. An example of that could be:

```
name     "Simple Loader"
author   "Rasta Mouse"

x64:
    load "bin/loader.x64.o"    # read reflective loader
        make pic               # turn it into pic

    run "merge.spec"           # process the merged coff
        make object            # turn it into a PICO
        export                 # export to raw bytes
        link "merged_pico"     # link pico to reflective loader

    export                     # export the whole lot
```

loader.spec

Running `piclink` against this loader specification will produce a PIC blob that contains the reflective loader + merged PICO.

![](https://rastamouse.me/content/images/2025/09/image.png)

## Future work?

I quite enjoyed working with COFFs in this way because it's so much easier from a development perspective.

I'm also interested in looking at the Java API a bit more to see how one might build a merged capability in a more progammatic fashion (imagine a GUI where you configure & build a capability by checking/unchecking "features" to include in the final output).

### Published by:

[![Rasta Mouse](https://www.gravatar.com/avatar/2b44f5ca5458931c49e1fa57da6705c1?s=250&r=x&d=mp)](/author/rasta/ "Rasta Mouse")

Rasta Mouse © 2025

* [Sign up](#/portal/)

[Powered by Ghost](https://ghost.org/)
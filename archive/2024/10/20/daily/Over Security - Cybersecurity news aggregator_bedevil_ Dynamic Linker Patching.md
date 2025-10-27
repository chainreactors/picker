---
title: bedevil: Dynamic Linker Patching
url: https://dfir.ch/posts/bedevil_dynamic_linker_patching/
source: Over Security - Cybersecurity news aggregator
date: 2024-10-20
fetch_date: 2025-10-06T18:51:18.436649
---

# bedevil: Dynamic Linker Patching

[Home](https://dfir.ch/)
[ ]

Menu

* [Home](/)
* [Posts](/posts/)
* [Talks](/talks/)
* [Tweets](/tweets/)
* |

LIGHT

DARK

# bedevil: Dynamic Linker Patching

19 Oct 2024

**Table of Contents**

* [Introduction](#introduction)
* [Patching the dynamic linker](#patching-the-dynamic-linker)
* [Investigation](#investigation)
* [Static binaries](#static-binaries)
* [Automatic checks](#automatic-checks)
* [Honorable mentions](#honorable-mentions)

## Introduction

bedevil (bdvl), according to the [GitHub page](https://github.com/Error996/bdvl), *is an LD\_PRELOAD rootkit. Therefore, this rootkit runs in userland.* The group `Muddled Libra` used bedevil to target VMware vCenter servers, according to Palo Alto’s [Unit42 Blog, 2024](https://unit42.paloaltonetworks.com/muddled-libra/). The rootkit comes with a nifty feature called `Dynamic Linker Patching`:

> Upon installation, the rootkit will patch the dynamic linker libraries. Before anything, the rootkit will search for a valid ld.so on the system to patch. When running ./bdv uninstall from a backdoor shell, the rootkit will revert the libraries back to having the original path. (/etc/ld.so.preload)

This topic is interesting from both a red- and blue-team perspective, primarily because the LD\_PRELOAD technique has been well-known for many years. Most detection tools and scripts are typically capable of identifying a shared library path in the `ld.so.preload` file or detecting a non-empty `LD_PRELOAD` environment variable. However, patching the dynamic linker provides attackers with significant advantages for stealth, while simultaneously creating new challenges for defenders attempting to identify such intrusions.

In this blog post, we will conduct an in-depth analysis of the patching technique used by the bedevil rootkit, exploring how it works and the advantages that dynamic linker patching offers to attackers.

## Patching the dynamic linker

The dynamic linker (also known as the dynamic loader) is a key component of Unix-like operating systems, including Linux, responsible for loading and linking shared libraries to programs at runtime. It allows applications to use code from shared libraries (like libc.so, which contains standard C library functions) without needing to embed this code directly into the executable.

In the `setup.py` file of the bedevil (bdvl) rootkit repository, there is a configuration flag that determines whether the dynamic linker should be overwritten during the installation process. By default, this flag is set to True, meaning that the dynamic linker will be replaced.

```
# patch the dynamic linker libraries as to overwrite
# the original /etc/ld.so.preload path with our own.
# setting to False will instruct the rootkit to use
# /etc/ld.so.preload instead.
PATCH_DYNAMIC_LINKER = True
```

In the header file `ldpatch.h` from the bedevil (bdvl) rootkit repository, two functions are defined. The first function, `_ldpatch`, is responsible for modifying or patching the dynamic linker (loader), effectively altering its behavior to facilitate the rootkitâs operations. The second function, `ldpatch`, is designed to reverse these modifications, restoring the dynamic linker to its original state when a login with the backdoor functionality occurs.

Additionally, the `ldhomes` array lists standard library paths where dynamic linkers can be found. The `ldfind` function searches these paths to locate linkers.

**inc/util/install/ldpatch/ldpatch.h** ([Source](https://github.com/Error996/bdvl/blob/nobash/inc/util/install/ldpatch/ldpatch.h))

```
static char *const ldhomes[7] = {"/lib", "/lib32", "/lib64", "/libx32",
                                 "/lib/x86_64-linux-gnu", "/lib/i386-linux-gnu", "/lib/arm-linux-gnueabihf"};

char **ldfind(int *allf);
#include "find.c"

int _ldpatch(const char *path, const char *oldpreload, const char *newpreload);
int ldpatch(const char *oldpreload, const char *newpreload);
#include "patch.c"
```

We will analyse key components of the file `patch.c.` next.

**inc/util/install/ldpatch/patch.c** ([Source](https://github.com/Error996/bdvl/blob/nobash/inc/util/install/ldpatch/patch.c))

The function `_ldpatch` takes three parameters:

* path: The path to the file which gets patched, for example, `/lib64/ld-linux-x86-64.so.2`
* oldpreload: The old LD\_PRELOAD value inside the file
* newpreload: The new LD\_PRELOAD value, which replaces the old value

```
int _ldpatch(const char *path, const char *oldpreload, const char *newpreload){
```

It checks next if the length of `oldpreload` matches the length of `newpreload`. If the lengths don’t match, the function returns 0 and exits early. Because the patching occurs in place, altering the file size would complicate the process or even break the process altogether.

```
if(strlen(oldpreload) != strlen(newpreload))
    return 0;
```

Here is the main code that overwrites the dynamic linker file(s), part of `patch.c`:

```
int count = 0,   // Counter to track matching characters in oldpreload
c = 0;       // Counter to track position in newpreload string

do{
    n = fread(buf, 1, fsize, ofp);  // Read from the original file into buf
    if(n){
        for(int i = 0; i <= fsize; i++){
            if(buf[i] == oldpreload[count]){
                if(count == LEN_OLD_PRELOAD){  // If we match the entire oldpreload string
                    for(int x = i-LEN_OLD_PRELOAD; x < i; x++)
                        memcpy(&buf[x], &newpreload[c++], 1);  // Overwrite with newpreload
                        break;  // Stop after the replacement
                    }
                    count++;
                } else count = 0;  // Reset if there's a mismatch
            }
        }else m = 0;
}while(n > 0 && n == m);  // Loop until all file content is processed
```

The value of `oldprelaod` is defined in the `setup.py` file (`/etc/ld.so.preload`)). Inside `setup.py`, we find the line: `'PRELOAD_FILE':ut.randpath(18)`. Thus, the path of the new LD\_PRELOAD file is not static and will be different on every machine, therefore hindering threat hunting for this particular value. In essence, the code scans for various dynamic loaders on the compromised system, loads the files into memory, and searches for occurrences of the string /etc/ld.so.preload. It then replaces this string with a new, randomly generated path. This path will hold the new path to a shared library, which is responsible for hijacking various system calls.

## Investigation

Now, to the most important question :) How do we find out if somebody tampered with our dynamic loaders when investigating a potentially compromised server? [Tony Lambert](https://x.com/ForensicITGuy/) on X has one possible answer to that question (original tweet [here](https://x.com/ForensicITGuy/status/1170149837490262016)):

![Tony Lambert](/images/bedevil_linker_patching/tony_lambert_bdvl.png "Tony Lambert")

Figure 1: Error Message

Quote: *If you get a match, your linker probably hasn’t been tampered with, if no match you might want to check its strings to see if it has a seemingly random file within.* Let’s explore a different technique.

**strace**

The dynamic linker processes the shared library specified with the LD\_PRELOAD environment variable or the content of the specifiedÂ ld.so.preloadÂ fileÂ **before**Â any other library or function is invoked. This is why LD\_PRELOAD libraries are always loaded first. See the following strace output, where we look at the invoked system calls ofÂ `ls`.

```
# strace ls
execve("/bin/ls", ["ls"], 0x7ffeb123ea50 /* 20 vars */) = 0
brk(NULL) Â  Â  Â  Â  Â  Â  Â  Â  Â  Â  Â  Â  Â  Â  Â  = 0x20b6000
mmap(NULL, 4096, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7fbfa6f79000
access("/bin/filebeathmili", R_OK)Â  Â  Â  = 0
open("/bin/filebeathmili", O_RDONLY|O_CLOEXEC) = 3
```

Have you spotted something anomalous? We found the malicious LD\_PRELOAD file! The first `access` syscall tries to load the file specified as the new LD\_PRELOAD...
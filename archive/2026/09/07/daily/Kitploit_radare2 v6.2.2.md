---
title: radare2 v6.2.2
url: https://kitploit.com/en/posts/github-radareorg-radare2-622
source: Kitploit
date: 2026-09-07
fetch_date: 2026-09-08T06:40:55.737627
---

# radare2 v6.2.2

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/3006/c19b136adc5b00ffa9e295f2624beea0f7fb78e36cfa8081c31116b9a5723a85.png)

New releaseSep 7, 2026

# radare2 v6.2.2

UNIX-like reverse engineering framework and command-line toolset

Share

[![screenshot](https://assets.kitploit.com/production/public/readmes/3006/3a698148c5a0a1bc714cb3ac4439316f08cf2349b8cd75366bc1b9d2bf7f9c22.png)](https://radare.org/)

## Radare2: Libre Reversing Framework for Unix Geeks

[![Latest packaged version](https://repology.org/badge/latest-versions/radare2.svg)](https://repology.org/project/radare2/versions) [![Tests Status](https://github.com/radareorg/radare2/actions/workflows/ci.yml/badge.svg?branch=master)](https://github.com/radareorg/radare2/actions/workflows/ci.yml?query=branch%3Amaster) [![build](https://github.com/radareorg/radare2/actions/workflows/build.yml/badge.svg?branch=master)](https://github.com/radareorg/radare2/actions/workflows/build.yml?query=branch%3Amaster) [![tcc](https://github.com/radareorg/radare2/actions/workflows/tcc.yml/badge.svg?branch=master)](https://github.com/radareorg/radare2/actions/workflows/tcc.yml)
[![CII Best Practices](https://bestpractices.coreinfrastructure.org/projects/741/badge)](https://bestpractices.coreinfrastructure.org/projects/741) [![Build Status](https://scan.coverity.com/projects/416/badge.svg)](https://scan.coverity.com/projects/416) [![Discord](https://badgen.net/discord/members/YBey7CR9jf)](https://discord.gg/YBey7CR9jf)

Current git `master` branch is `6.2.2`, next release will be `6.2.4`.

### Description

r2 is a complete rewrite of radare. It provides a set of libraries, tools and
plugins to ease reverse engineering tasks. Distributed under LGPLv3, despite
each plugin can have different licenses (see `r2 -Lj` for details)

The **radare** project started as a simple command-line hexadecimal editor
focused on forensics. Today, r2 is a full-featured low-level command-line tool
with support for scripting with the embedded Javascript interpreter or via r2pipe.

r2 can edit files on local hard drives, view kernel memory, and debug programs
locally or via a remote gdb/windbg servers. r2's wide architecture support allows
you to analyze, emulate, debug, modify, and disassemble any binary.

[![screenshot](https://assets.kitploit.com/production/public/readmes/3006/c19b136adc5b00ffa9e295f2624beea0f7fb78e36cfa8081c31116b9a5723a85.png)](https://www.radare.org/)

## Installation

Download the last [released](https://github.com/radareorg/radare2/releases) binaries.

The recommended way to install radare2 is from Git repository source:

root@kitploit:~

```
git clone https://github.com/radareorg/radare2
radare2/sys/install.sh
```

* Run `sys/install.sh` for the default acr+make+symlink installation
* meson/ninja (muon/samu also works) and make builds are supported.

### Nix

radare2 provides Nix packaging under [`dist/nix`](https://github.com/radareorg/radare2/blob/master/dist/nix/README.md).

### Source Build

* r2 can be installed from `git` or via `pip` using `r2env`.
* Windows builds require meson and msvc or mingw as compilers
* To uninstall the current build of r2 run `make uninstall`
* To uninstall ALL the system installations of r2 do: `sudo make purge`

On Windows use the .bat scripts and msvc:

root@kitploit:~

```
preconfigure.bat       REM setup python, meson, ninja
configure.bat          REM run meson b + vs project
make.bat               REM run ninja -C b
prefix\bin\radare2.exe
```

## Popular Plugins:

Using the `r2pm` tool you can browse and install many plugins and tools that use radare2.

* [iaito](https://github.com/radareorg/iaito): The official Qt graphical interface
* [keystone](https://github.com/radareorg/radare2-extras/tree/master/keystone) Assembler instructions using the Keystone library
* [decai](https://github.com/radareorg/r2ai) Decompiler based on AI
* [r2ai](https://github.com/radareorg/r2ai) Run a Language Model in localhost with Llama inside r2!
* [r2dec](https://github.com/wargio/r2dec-js): A decompiler based on r2 written in JS, accessed with the `pdd` command
* [r2diaphora](https://github.com/FernandoDoming/r2diaphora): [Diaphora](https://github.com/joxeankoret/diaphora)'s binary diffing engine on top of radare2
* [r2flutter](https://github.com/trufae/r2flutter): Dart/Flutter AOT snapshot analysis for Android and iOS apps
* [r2frida](https://github.com/nowsecure/r2frida): The frida io plugin. Start r2 with `r2 frida://0` to use it
* [r2ghidra](https://github.com/radareorg/r2ghidra): The standalone native ghidra decompiler accessible with `pdg`
* [r4ghidra](https://github.com/radareorg/r4ghidra): Feel the radare joy inside your Ghidra
* [r2papi](https://github.com/radareorg/radare2-r2papi) High level api on top of r2pipe
* [r2pipe](https://github.com/radareorg/radare2-r2pipe) Script radare2 from any programming language
* [r2poke](https://github.com/radareorg/radare2-extras/tree/master/r2poke) Integration with GNU/Poke for extended binary parsing capabilities
* [goresym](https://github.com/hanemile/radare2-GoReSym): Import GoReSym symbol as flags
* [r2yara](https://github.com/radareorg/r2yara) Run Yara from r2 or use r2 primitives from Yara
* [radius2](https://github.com/radareorg/radius2): A fast symbolic execution engine based on boolector and esil
* [r2sarif](https://github.com/radareorg/r2sarif) import/extend/export SARIF documents
* [r2hermes](https://github.com/radareorg/r2hermes) Disassembler and analyzer for React Native Hermes bytecode
* [r2renef](https://github.com/Ahmeth4n/r2renef) Renef IO Plugin for Radare2 - Dynamic Android Instrumentation
* [r2unity](https://github.com/radareorg/r2unity): Inspect Unity IL2CPP metadata and native binaries from radare2
* [warrp](https://github.com/radareorg/warrp) Native radare2 plugin for the binary ninja's WARP format

## Usage

These are the first steps to use r2, read the book or find tutorials for more details

root@kitploit:~

```
$ r2 /bin/ls   # open file in read-only
> aaa          # analyse the program (r2 -A)
> afl          # list all functions (try aflt, aflm)
> px 32        # print 32 byte hexdump current block
> s sym.main   # seek to main (using flag name)
> f~foo        # filter flags matching 'foo' (internal |grep)
> iS;is        # list sections and symbols (rabin2 -Ss)
> pdf; agf     # disassembly and ascii-art function graph
> oo+;w hello  # reopen in read-write and write a string
> ?*~...       # interactive filter in all command help
> q            # quit
```

Many plugins are included in r2 by default. But you can extend its capabilities
by using the [r2pm](https://github.com/radareorg/radare2-pm) package manager.

root@kitploit:~

```
r2pm -s <word>  # search packages matching a word
r2pm -Uci <pkg> # update database and clean install a package
r2pm -u <pkg>   # uninstall the given package
r2pm -l <pkg>   # list installed packages
```

## Resources

* [Official Book](https://book.rada.re): Read about r2 usage
* [COMMUNITY.md](https://github.com/radareorg/radare2/blob/master/COMMUNITY.md): Community engagement and loose guidelines
* [CONTRIBUTING.md](https://github.com/radareorg/radare2/blob/master/CONTRIBUTING.md): Information about reporting issues and
  contributing. See also [Contributing](#contributing)
* [DEVELOPERS.md](https://github.com/radareorg/radare2/blob/master/DEVELOPERS.md): Development guidelines for r2
* [SECURITY.md](https://github.com/radareorg/radare2/blob/master/SECURITY.md): Instructions for reporting vulnerabilities
* [USAGE.md](https://github.com/radareorg/radare2/blob/master/USAGE.md): Some example commands
* [INSTALL.md](https://github.com/radareorg/...
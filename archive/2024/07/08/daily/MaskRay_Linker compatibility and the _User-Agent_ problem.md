---
title: Linker compatibility and the "User-Agent" problem
url: https://maskray.me/blog/2024-07-07-linker-compatibility-and-the-user-agent-problem
source: MaskRay
date: 2024-07-08
fetch_date: 2025-10-06T17:40:36.315710
---

# Linker compatibility and the "User-Agent" problem

# [MaskRay](/blog/)

[Home](/blog/)
[Archives](/blog/archives/)
[Feeds](/blog/../feeds/)
[TIL](/blog/../til/)
[Presentations](/blog/../presentations/)

[![](/icon/github.svg)](https://github.com/MaskRay "GitHub")
[![](/icon/twitter.svg)](https://twitter.com/HaskRay "Twitter")



[2024-07-07](/blog/2024-07-07-linker-compatibility-and-the-user-agent-problem)

# Linker compatibility and the "User-Agent" problem

The output of `ld.lld -v` includes a message "compatible
with GNU linkers" to address [detection
mechanism used by GNU Libtool](https://lists.gnu.org/archive/html/libtool/2017-01/msg00007.html). This problem is described by [Software
compatibility and our own "User-Agent" problem](https://www.sigbus.info/software-compatibility-and-our-own-user-agent-problem).

The latest `m4/libtool.m4` continues to rely on a
`GNU` check.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 ``` | ``` [AC_CACHE_CHECK([if the linker ($LD) is GNU ld], lt_cv_prog_gnu_ld, [# I'd rather use --version here, but apparently some GNU lds only accept -v. case `$LD -v 2>&1 </dev/null` in *GNU* | *'with BFD'*)   lt_cv_prog_gnu_ld=yes   ;; *)   lt_cv_prog_gnu_ld=no   ;; esac]) ``` |

[Check-based
configuration](https://leahneukirchen.org/blog/archive/2024/04/what-autoconf-got-right.html) can be a valuable tool, ensuring software remains
functional in the future. However, this example highlights how overly
specific checks can lead to unintended consequences.

If Libtool needs to check whether certain options are available, it
can utilize [`-v`](#more-fun-with-versions).

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 ``` | ``` % ld.bfd -v --whole-archive GNU ld (GNU Binutils) 2.42.0 % ld.bfd -v --whole-archivex; echo $? GNU ld (GNU Binutils) 2.42.0 ld.bfd: unrecognized option '--whole-archivex' ld.bfd: use the --help option for usage information 1 ``` |

This blog post explores more forms of the "User-Agent" problem
exposed by an LLD patch changing the version message format.

LLD supports many object file formats. It largely emulates the
behavior of GNU ld for ELF, while emulating the behavior of MSVC
link.exe for PE/COFF. Previously, LLD's ELF port displays the version
information like this:

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` % /tmp/out/custom2/bin/ld.lld --version LLD 19.0.0 (compatible with GNU linkers) ``` |

A recent patch ([llvm-project#97323](https://github.com/llvm/llvm-project/pull/97323))
changed it to one of the following formats, depending on the build-time
variable `LLVM_APPEND_VC_REV`:

With `LLVM_APPEND_VC_REV=on`:

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` % /tmp/out/custom2/bin/ld.lld --version LLD 19.0.0 (git@github.com:llvm/llvm-project.git 0f9fbbb63cfcd2069441aa2ebef622c9716f8dbb), compatible with GNU linkers ``` |

With `LLVM_APPEND_VC_REV=off`:

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` % /tmp/out/custom2/bin/ld.lld --version LLD 19.0.0, compatible with GNU linkers ``` |

## Meson

In Meson, `mesonbuild/linkers/detect.py:guess_win_linker`
checks the `--version` output to determine whether the LLD
invocation is for ELF or PE/COFF. It performed an overly strict check
"(compatible with GNU linkers)", which failed when the parentheses were
stripped by #97323.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 ``` | ``` # mesonbuild/linkers/detect.py     if 'LLD' in o.split('\n', maxsplit=1)[0]:         if '(compatible with GNU linkers)' in o:             return linkers.LLVMDynamicLinker(                 compiler, for_machine, comp_class.LINKER_PREFIX,                 override, version=search_version(o))         elif not invoked_directly:             return linkers.ClangClDynamicLinker(                 for_machine, override, exelist=compiler, prefix=comp_class.LINKER_PREFIX,                 version=search_version(o), direct=False, machine=None) ``` |

The latest Meson has loosened the check ([meson#13383](https://github.com/mesonbuild/meson/pull/13383)).

It seems that the linker detection has a larger problem that
`--target=` is not taken into account with Clang ([#6662](https://github.com/mesonbuild/meson/issues/6662)).

## Linux kernel

The Linux kernel's `scripts/ld-version.sh` script detects
linker versions. Introduced in 2014, it initially checked for GNU ld
compatibility with GCC LTO (though LTO support remains unmerged). It was
later revamped to handle LLD versions as well. While it can handle
suffixes like `2.34-4.fc32`, it struggles with versions
containing with comma suffix (`19.0.0,`).

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` % scripts/ld-version.sh /tmp/out/custom2/bin/ld.lld scripts/ld-version.sh: line 19: 10000 * 19 + 100 * 0 + 0,: syntax error: operand expected (error token is ",") ``` |

The script extracts the version string from the
`--version` output and parses it as major.minor.patch.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 ``` | ``` # Get the first line of the --version output. IFS=' ' set -- $(LC_ALL=C "$@" --version)  # Split the line on spaces. IFS=' ' set -- $1  ...  # Some distributions append a package release number, as in 2.34-4.fc32 # Trim the hyphen and any characters that follow. version=${version%-*} ``` |

To support suffixes starting with either `-` or
`,`, the script [will
employ a POSIX shell trick](https://lore.kernel.org/all/20240705160007.GA875035%40thelio-3990X/) utilizing the "Remove Largest Suffix
Pattern" feature:

|  |  |
| --- | --- |
| ``` 1 ``` | ``` version=${version%%[!0-9.]*} ``` |

## More fun with versions

llvm-nm and llvm-objcopy also claim GNU compatibility.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 ``` | ``` % /tmp/Rel/bin/llvm-nm --version llvm-nm, compatible with GNU nm LLVM (http://llvm.org/):   LLVM version 19.0.0git   Optimized build with assertions. % /tmp/Rel/bin/llvm-objcopy --version llvm-objcopy, compatible with GNU objcopy LLVM (http://llvm.org/):   LLVM version 19.0.0git   Optimized build with assertions. ``` |

Ever wondered what the subtle differences are between
`-v`, `-V`, and `--version` when using
GNU ld? Let's break it down:

* `--version` skips linker input processing and displays
  brief copyright information.
* `-v` and `-V` keep processing command line
  arguments and perfoming a linking step. This behavior gives an easy way
  to check whether an option is supported.
* `-V` goes a step further than `-v` by
  including a list of supported BFD emulations alongside the version
  information.

Prior to September 2022, `-V` in ld.lld used to an alias
for `--version`. This caused issues when using
`gcc -v -fuse-ld=lld` on certain targets like
`*-freebsd` and `powerpc-*`: gcc passes -V to the
linker, expecting it to process the input files and complete the linking
step. However, ld.lld's behavior with `-V` skipped this
process.

I made an adjustment by [making
`-V` an alias for `-v`](https://github.com/llvm/llvm-project/issues/57859) instead. This ensures
that `gcc -v -fuse-ld=lld` performs the linking step.

GCC has a similar `-v` and `--version`
behavior, but `-V` does not exist.

Clang's GNU driver emulates GCC 4.2.1, but you can change the version
with `-fgnuc-version=`.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 ``` | ``` % clang -E -dM -xc /dev/null | grep GNU #define __GNUC_MINOR__ 2 #define __GNUC_PATCHLEVEL__ 1 #define __GNUC_STDC_INLINE__ 1 #define __GNUC__ 4 % clang -E -dM -xc /dev/null -fgnuc-version=5.3.2 | grep GNU #define __GNUC_MINOR__ 3 #define __GNUC_PATCHLEVEL__ 2 #define __GNUC_STDC_INLINE__ 1 #define __GNUC__ 5 ``` |

Share

* [linker](/blog/tags/linker/)
* [linux](/blog/tags/linux/)
* [lld](/blog/tags/lld/)

[**Newer**

Mapping symbols: rethinking for efficiency](/blog/2024-07-21-mapping-symbols-rethinking-for-efficiency)
[**Older**

Integrated assembler improvements in LLVM 19](/blog/2024-06-30-integrated-assembler-improvements-in-llvm-19)

### Popular

### Tag Cloud

[adc](/blog/tags/adc/) [ai9](/blog/tags/ai9/) [algorithm](/blog/tags/algorithm/) [arm](/blog/tags/arm/) [asc](/blog/tags/asc/) [assebmly](/blog/tags/assebmly/...
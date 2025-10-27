---
title: Distribution of debug information
url: https://maskray.me/blog/2022-10-30-distribution-of-debug-information
source: MaskRay
date: 2022-10-31
fetch_date: 2025-10-03T21:20:42.565815
---

# Distribution of debug information

# [MaskRay](/blog/)

[Home](/blog/)
[Archives](/blog/archives/)
[Feeds](/blog/../feeds/)
[TIL](/blog/../til/)
[Presentations](/blog/../presentations/)

[![](/icon/github.svg)](https://github.com/MaskRay "GitHub")
[![](/icon/twitter.svg)](https://twitter.com/HaskRay "Twitter")



[2022-10-30](/blog/2022-10-30-distribution-of-debug-information)

# Distribution of debug information

Updated in 2024-08.

Note: The article will likely get frequent updates in the next few
days.

This article describes some approaches to distribute debug
information. Commands below will use two simple C files for
demonstration.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 ``` | ``` cat > a.c <<eof void foo(int); int main() { foo(42); } eof cat > b.c <<eof #include <stdio.h> void foo(int x) { printf("%d\n", x); } eof ``` |

## Debug information in the executable or shared object

This is the simplest model. Debug information resides in the
executable or shared object.

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` gcc -c -g a.c b.c gcc a.o b.o -o a ``` |

The linker collects input debug sections, resolves relocations, does
minimum merging (`SHF_STRING` merge for
`.debug_str` and `.debug_line_str`), and combines
them into output debug sections.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 ``` | ```  0                0       a7     1 .debug_abbrev  0                0       38     1         a.o:(.debug_abbrev) 38               38       6f     1         b.o:(.debug_abbrev)  0                0       94     1 .debug_info  0                0       37     1         a.o:(.debug_info) 37               37       5d     1         b.o:(.debug_info)  0                0       44     1 .debug_str_offsets  0                0       1c     1         a.o:(.debug_str_offsets) 1c               1c       28     1         b.o:(.debug_str_offsets)  0                0       c1     1 .debug_str  0                0       c1     1         <internal>:(.debug_str)  0                0       28     1 .debug_addr  0                0       10     1         a.o:(.debug_addr) 10               10       18     1         b.o:(.debug_addr)  0                0       bf     1 .debug_line  0                0       5e     1         a.o:(.debug_line) 5e               5e       61     1         b.o:(.debug_line)  0                0        f     1 .debug_line_str  0                0        f     1         <internal>:(.debug_line_str) ``` |

## Separate debug files

Debug information is large and not needed by many people. As a
general size optimization, many distributions don't provide debug
information in main software packages. For debugging needs,
distributions may provide debug information in separate packages,
leveraging a debugger feature that debug information may reside in a
separate file. See <https://sourceware.org/gdb/onlinedocs/gdb/Separate-Debug-Files.html>.

objcopy from binutils-gdb can create a separate debug file (since
2003).

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` objcopy --only-keep-debug a a.debug strip -S a -o a.stripped ``` |

eu-strip from elfutils can generate two output files in one
invocation.

|  |  |
| --- | --- |
| ``` 1 ``` | ``` eu-strip -f a.debug a -o a.stripped ``` |

The elfutils way is convenient for simple use cases and is adopted by
rpm. But there is general ambiguity whether an operation applies to one
output file or both. The `--only-keep-debug` way is
orthogonal and integrates well with other features (e.g.
`--compress-debug-sections`, `--remove-section`).
I favor `--only-keep-debug` and [implemented it](https://reviews.llvm.org/D67137) in
llvm-objcopy.

When debugging `a.stripped` in gdb, use
`add-symbol-file -o xxx a.debug` to load the separate debug
file.

Solaris 11 Update 1 introduced a similar feature called Ancillary
Object. See [Ancillary
Objects: Separate Debug ELF Files For Solaris](http://www.linker-aliens.org/blogs/ali/entry/ancillary_objects_separate_debug_elf/). They made a nice
choice that `ld -z ancilliary` creates two output files,
saving one objcopy command in the GNU linking model. However, if you
want extra objcopy options beside `--only-keep-debug`, you
will still need an objcopy command.

In July 2024, mold added [`--separate-debug-info`](https://github.com/rui314/mold/issues/1294),
which is like a variant of Solaris ld's `-z ancilliary`.

### `.gnu_debuglink`

`objcopy --add-gnu-debuglink=a.debug a.stripped` adds a
non-`SHF_ALLOC` section `.gnu_debuglink` to
`a.stripped`. The section contains a filename (no directory
information) and a four-byte CRC checksum.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` % objdump -g a.stripped ... Contents of the .gnu_debuglink section (loaded from a.stripped):    Separate debug info file: a.debug   CRC value: 0x4d1e2a66 ``` |

gdb has [supported
`.gnu_debuglink` since 2003](https://sourceware.org/git/?p=binutils-gdb.git;a=commit;h=5b5d99cf4d5ded93b60fd64c6069d45e3eeab1d3). It finds a debug file in the
same directory of the executable and `.debug/` relative to
the directory. (I filed a [feature
request](https://sourceware.org/bugzilla/show_bug.cgi?id=29584) for supporting zstd in 2022-09.)

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` % gdb -ex q a.stripped Reading symbols from a.stripped... Reading symbols from /tmp/c/a.debug... ``` |

Directories specified by `debug-file-directory` are used
as well. This option needs to be set before loading the inferior.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 ``` | ``` % pwd /tmp/c % install -D -t debug/tmp/c a.debug % rm a.debug % gdb -iex 'set debug-file-directory debug' -ex q a.stripped Reading symbols from a.stripped... Reading symbols from debug//tmp/c/a.debug... ``` |

A debug file can be found by build ID. A build ID resides in an ELF
note section. Many Linux distributions configure GCC with
`--enable-linker-build-id` to generate a build ID by default.
See [--build-id](/blog/2020-11-15-explain-gnu-linker-options)
for the option.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 ``` | ``` % readelf -Wn a.stripped ... Displaying notes found in: .note.gnu.build-id   Owner                Data size        Description   GNU                  0x00000008       NT_GNU_BUILD_ID (unique build ID bitstring)         Build ID: a3b3f0788440fd94 % install -D -T debug/tmp/c/a.debug debug/.build-id/a3/b3f0788440fd94.debug % rm debug/tmp/c/a.debug % gdb -nx -iex 'set debug-file-directory debug' -ex q a.stripped Reading symbols from a.stripped... Reading symbols from /tmp/c/debug/.build-id/a3/b3f0788440fd94.debug... ``` |

lldb uses `target.debug-file-search-paths` to locate a
separate debug file. (TODO)

On Debian, if we install `hello-dbgsym`, a debug file will
be available in `/usr/lib/debug`.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` % gdb -batch -ex 'show debug-file-directory' The directory where separate debug symbols are searched for is "/usr/lib/debug". % gdb -ex q =hello Reading symbols from /usr/bin/hello... Reading symbols from /usr/lib/debug/.build-id/ff/29703f105c66821e9b10149db8cff3b2e4043a.debug... ``` |

Debian uses [`dh_strip`](https://github.com/Debian/debhelper/blob/master/dh_strip)
for packaging commands. `dh_strip` uses
`objcopy --only-keep-debug --compress-debug-sections` to [compress debug
sections](/blog/2022-01-23-compressed-debug-sections).

## MiniDebugInfo

See <https://sourceware.org/gdb/onlinedocs/gdb/MiniDebugInfo.html>
([implemented
in 2012](https://sourceware.org/git/?p=binutils-gdb.git;a=commit;h=608e2dbbfefcec9aa3efc863ffcc889786ae93d7)). When a binary contains `.gnu_debugdata`, gdb
decompresses it with xz and loads it.

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` objcopy --only-keep-debug a a.debug xz a.debug objcopy -S --add-section=.gnu_debugdata=a.debug.xz a a.stripped ``` |

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` % gdb -ex q a.stripped Reading symbols from a.stripped... Reading symbols from .gnu_debugdata for /tmp/c/a.stripped... ``` |

Fedora uses the feature to improve symbolization of stack traces in
the abse...
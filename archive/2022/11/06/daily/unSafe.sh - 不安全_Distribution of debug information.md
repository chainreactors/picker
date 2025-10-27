---
title: Distribution of debug information
url: https://buaq.net/go-133392.html
source: unSafe.sh - 不安全
date: 2022-11-06
fetch_date: 2025-10-03T21:49:29.091048
---

# Distribution of debug information

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![]()

Distribution of debug information

UNDER CONSTRUCTIONThis article describes some approaches to distribute debug inform
*2022-11-5 16:0:0
Author: [maskray.me(查看原文)](/jump-133392.htm)
阅读量:77
收藏*

---

UNDER CONSTRUCTION

This article describes some approaches to distribute debug information. Commands below will use two simple C files for demonstration.

|  |  |
| --- | --- |
| ``` 1 ``` | ``` cat > a.c < void foo(int); int main() { foo(42); } eof cat > b.c <  void foo(int x) { printf("%d\n", x); } eof ``` |

## Debug information in the object file

This is the simplest model. Debug information resides in the executable or shared object.

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` gcc -c -g a.c b.c gcc a.o b.o -o a ``` |

## Separate debug files

Debug information is large and not needed by many people. As a general size optimization, many distributions move debug information into separate packages. This levages the feature that debug information may reside in a separate file. See <https://sourceware.org/gdb/onlinedocs/gdb/Separate-Debug-Files.html>.

objcopy from binutils-gdb can create a separate debug file (since 2003).

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` objcopy --only-keep-debug a a.debug strip -S a -o a.stripped ``` |

eu-strip from elfutils can generate two output files in one invocation.

|  |  |
| --- | --- |
| ``` 1 ``` | ``` eu-strip -f a.debug a -o a.stripped ``` |

The elfutils way is convenient for simple use cases and is adopted by rpm. But for certain operations there is ambiguity whether they need to apply to one output file or both. The `--only-keep-debug` way has orthogonality and integrates well with other features (e.g. `--compress-debug-sections`, `--remove-section`). I favor `--only-keep-debug` and [implemented it](https://reviews.llvm.org/D67137) in llvm-objcopy.

When debugging `a.stripped` in gdb, use `add-symbol-file -o xxx a.debug` to load the separate debug file.

### `.gnu_debuglink`

`objcopy --add-gnu-debuglink=a.debug a.stripped` adds a non-`SHF_ALLOC` section `.gnu_debuglink` to `a.stripped`. The section contains a filename (no directory information) and a four-byte CRC checksum.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` % objdump -g a.stripped ... Contents of the .gnu_debuglink section (loaded from a.stripped):    Separate debug info file: a.debug   CRC value: 0x4d1e2a66 ``` |

gdb has [supported `.gnu_debuglink` since 2003](https://sourceware.org/git/?p=binutils-gdb.git;a=commit;h=5b5d99cf4d5ded93b60fd64c6069d45e3eeab1d3). It finds a debug file in the same directory of the executable and `.debug/` relative to the directory.

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` % gdb -ex q a.stripped Reading symbols from a.stripped... Reading symbols from /tmp/c/a.debug... ``` |

Directories specified by `debug-file-directory` are used as well. This option needs to be set before loading the inferior.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 ``` | ``` % pwd /tmp/c % install -D -t debug/tmp/c a.debug % rm a.debug % gdb -iex 'set debug-file-directory debug' -ex q a.stripped Reading symbols from a.stripped... Reading symbols from debug//tmp/c/a.debug... ``` |

A debug file can be found by build ID. A build ID resides in an ELF note section. Many Linux distributions configure GCC with `--enable-linker-build-id` to generate a build ID by default. See [--build-id](https://maskray.me/blog/2020-11-15-explain-gnu-linker-options) for the option.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 ``` | ``` % readelf -Wn a.stripped ... Displaying notes found in: .note.gnu.build-id   Owner                Data size        Description   GNU                  0x00000008       NT_GNU_BUILD_ID (unique build ID bitstring)         Build ID: a3b3f0788440fd94 % install -D -T debug/tmp/c/a.debug debug/.build-id/a3/b3f0788440fd94.debug % rm debug/tmp/c/a.debug % gdb -nx -iex 'set debug-file-directory debug' -ex q a.stripped Reading symbols from a.stripped... Reading symbols from /tmp/c/debug/.build-id/a3/b3f0788440fd94.debug... ``` |

lldb uses `target.debug-file-search-paths` to locate a separate debug file. (TODO)

On Debian, if we install `hello-dbgsym`, a debug file will be available in `/usr/lib/debug`.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` % gdb -batch -ex 'show debug-file-directory' The directory where separate debug symbols are searched for is "/usr/lib/debug". % gdb -ex q =hello Reading symbols from /usr/bin/hello... Reading symbols from /usr/lib/debug/.build-id/ff/29703f105c66821e9b10149db8cff3b2e4043a.debug... ``` |

See [`dh_strip`](https://github.com/Debian/debhelper/blob/master/dh_strip) for packaging commands.

## MiniDebugInfo

See <https://sourceware.org/gdb/onlinedocs/gdb/MiniDebugInfo.html> ([implemented in 2012](https://sourceware.org/git/?p=binutils-gdb.git;a=commit;h=608e2dbbfefcec9aa3efc863ffcc889786ae93d7)). When a binary contains `.gnu_debugdata`, gdb decompresses it with xz and loads it.

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` objcopy --only-keep-debug a a.debug objcopy -S --add-section=.gnu_debugdata=a.debug.xz a a.stripped ``` |

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` % gdb -ex q a.stripped Reading symbols from a.stripped... Reading symbols from .gnu_debugdata for /tmp/c/a.stripped... ``` |

Fedora uses the feature to improve symbolization of stack traces in the absence of debug information. A Fedora MiniDebugInfo file mostly just provides note sections and a `.symtab` with symbols not in `.dynsym`. Non-`SHF_ALLOC` `SHT_PROGBITS/SHT_NOTE/SHT_NOBITS` sections (e.g. `.comment`) are removed. Note sections are duplicated in the original binary and the MiniDebugInfo file due to a small missing optimization in `eu-strip -f`.

See [Support MiniDebugInfo in rpm](https://bugzilla.redhat.com/show_bug.cgi?id=834073) for the original implementation. The new implementation is in `scripts/find-debuginfo.in` in the [`debugedit`](https://sourceware.org/debugedit/) repository. [Support for mini-debuginfo in LLDB](https://archive.fosdem.org/2020/schedule/event/debugging_mini/) introduces the lldb implementation.

Here is a simplified demonstration of what `scripts/find-debuginfo.in` does:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 ``` | ``` eu-strip --remove-comment -f a.mini a -o a.stripped nm a -f sysv --defined-only | awk -F \| '$4 ~ "FUNC" {print $1}' | sort > a.symtab nm a -f sysv --defined-only -D | sort > a.dynsym comm -13 a.dynsym a.symtab > a.keepsyms objcopy -S --keep-symbols=a.keepsyms a.mini xz a.mini objcopy -S --add-section=.gnu_debugdata=a.mini.xz a a.stripped ``` |

## DWARF supplementary object files

## Split DWARF object files

This was originally proposed as GCC [debug fission](https://gcc.gnu.org/wiki/DebugFission). Later in DWARF version 5 this feature was standardized as split DWARF object files, commonly abbreviated as "split DWARF". The idea is to move the bulk of `.debug_*` sections into a separate file (`.dwo`) and leave just a small amount in the relocatable object file (`.o`). `.dwo` files are not handled by the linker: this reduces the input section combining work and relocation work for the linker, leading to smaller link time and lower memory usage. The smaller input has advantages for a distributed build farm.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 ``` | ``` % clang -c -g -gsplit-dwarf a.c b.c % readelf -WS a.o | grep ' .debug_gnu_pub'   [12] .debug_gnu_pubnames PROGBITS        0000000000000000 0000be 00001c 00      0   0  1   [14] .debug_gnu_pubtypes PROGBITS        0000000000000000 0000da 00001b 00      0   0  1 % readelf -WS a.dwo | grep ']'   [Nr] Name              Type            Address          O...
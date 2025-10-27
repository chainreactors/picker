---
title: All about LeakSanitizer
url: https://buaq.net/go-149085.html
source: unSafe.sh - 不安全
date: 2023-02-13
fetch_date: 2025-10-04T06:27:31.068172
---

# All about LeakSanitizer

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

All about LeakSanitizer

Clang and GCC 4.9implemented LeakSanitizer in 2013. LeakSanitizer(LSan) is a memor
*2023-2-12 16:0:0
Author: [maskray.me(查看原文)](/jump-149085.htm)
阅读量:97
收藏*

---

Clang and [GCC 4.9](https://gcc.gnu.org/PR59061)
implemented LeakSanitizer in 2013. [LeakSanitizer](https://clang.llvm.org/docs/LeakSanitizer.html)
(LSan) is a memory leak detector. It intercepts memory allocation
functions and by default detects memory leaks at `atexit`
time. The implementation is purely in the runtime
(`compiler-rt/lib/lsan`) and no instrumentation is
needed.

LSan has very little architecture-specific code and supports many
64-bit targets. Some 32-bit targets (e.g. Linux arm/x86-32) are
supported as well, but there may be high false negatives because of the
small pointer size. Every supported operating system needs to provide
some way to "stop the world".

## Usage

LSan can be used in 3 ways.

* Standalone (`-fsanitize=leak`)
* AddressSanitizer (`-fsanitize=address`)
* HWAddressSanitizer (`-fsanitize=hwaddress`)

The most common way to use LSan is
`clang -fsanitize=address` (or GCC). For LSan-supported
targets (`#define CAN_SANITIZE_LEAKS 1`), the
AddressSanitizer (ASan) runtime enables LSan by default.

|  |  |
| --- | --- |
| ``` 1 ``` | ``` % cat a.c #include <stdlib.h> int main() {   void **p = malloc(42); // leak (categorized as "Direct leak")   *p = malloc(43);       // leak (categorized as "Indirect leak")   p = 0; } % clang -fsanitize=address a.c -o a % ./a  ================================================================= ==594015==ERROR: LeakSanitizer: detected memory leaks  Direct leak of 42 byte(s) in 1 object(s) allocated from:     #0 0x55fffef9482e  (/tmp/c/a+0xea82e)     #1 0x55fffefcf1d1  (/tmp/c/a+0x1251d1)     #2 0x7f7301626189  (/lib/x86_64-linux-gnu/libc.so.6+0x27189) (BuildId: c4f6727c560b1c33527ff9e0ca0cef13a7db64d2)  Indirect leak of 43 byte(s) in 1 object(s) allocated from:     #0 0x55fffef9482e  (/tmp/c/a+0xea82e)     #1 0x55fffefcf1df  (/tmp/c/a+0x1251df)     #2 0x7f7301626189  (/lib/x86_64-linux-gnu/libc.so.6+0x27189) (BuildId: c4f6727c560b1c33527ff9e0ca0cef13a7db64d2)  SUMMARY: AddressSanitizer: 85 byte(s) leaked in 2 allocation(s). ``` |

As a runtime-only feature, `-fsanitize=leak` is mainly for
link actions. It does affect compile actions for the following C/C++
preprocessor feature.

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` #if __has_feature(leak_sanitizer) ... #endif ``` |

## Implementation overview

Standalone LSan intercepts malloc-family functions. It uses the
temporized `SizeClassAllocator{32,64}` with chunk metadata.
The interceptors record the allocation information (requested size,
stack trace).

AddressSanitizer already intercepts malloc-family functions. Its
chunk metadata has extra bits for LSan.

By default, the common options `detect_leaks` and
`leak_check_at_exit` are enabled. The runtime installs a hook
with `atexit` which will perform the leak check.
Alternatively, the user can call `__lsan_do_leak_check` to
request a leak check before the exit time.

Upon a leak check, the runtime performs a job very similar to a
mark-and-sweep garbage collection algorithm. It suspends all threads
("stop the world") and scans root regions (find allocations reachable by
the process). Root regions include:

* ignored allocations due to `__lsan_ignore_object` or
  `__lsan_disable`
* global regions (`__lsan::ProcessGlobalRegions`). On
  Linux, these refer to memory mappings due to writable
  `PT_LOAD` program headers. This ensures that allocations
  reachable by a global variable are not leaks.
* for each thread, registers (default `use_registers=1`),
  stack (default `use_stack=1`), thread-local storage (default
  `use_tls=1`), and additional pointers in the thread
  context
* root regions due to `__lsan_register_root_region`
* operating system specific allocations. This is currently
  macOS-specific: libdispatch and Foundation memory regions, etc.

The runtimes uses a flood fill algorithm to find reachable
allocations from a region. The runtime is conservative and scans all
aligned words which look like a pointer. (It is not feasible to
determine whether a pointer-like word is used as an integer/floating
point number, not as a pointer.) If the word looks like a pointer into a
heap (many 64-bit targets use
`[0x600000000000, 0x640000000000)`), the runtime checks
whether it refers to an active chunk. In Valgrind's terms, a reference
can be a "start-pointer" (a pointer to the start of the chunk) or an
"interior-pointer" (a pointer to the middle of the chunk).

Finally, the runtime iterates over all active allocations and reports
leaks for unmarked allocations.

### Metadata

Each allocation reserves 2 bits to record its state:
leaked/reachable/ignored. For better diagnostics, "leaked" can be direct
or indirect. If a chunk is marked as leaked, all chunks reachable from
it are marked as indirectly leaked. (`*p = malloc(43);` in
the very beginning example is an indirect leak.)

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` enum ChunkTag {   kDirectlyLeaked = 0,     kIndirectlyLeaked = 1,   kReachable = 2,   kIgnored = 3 }; ``` |

Standalone LSan uses this chunk metadata struct:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 ``` | ``` struct ChunkMetadata {   u8 allocated : 8;     ChunkTag tag : 2; #if SANITIZER_WORDSIZE == 64   uptr requested_size : 54; #else   uptr requested_size : 32;   uptr padding : 22; #endif   u32 stack_trace_id; }; ``` |

ASan just stores a 2-bit `ChunkTag` in its existing chunk
metadata (`__asan::Chunkheader::lsan_tag`). Similarly, HWASan
stores a 2-bit `ChunkTag` in its existing chunk metadata
(`__hwasan::Metadata::lsan_tag`).

### Allocator

Both standalone LSan and ASan use the temporized
`SizeClassAllocator{32,64}` (primary allocator) with a
thread-local cache (`SizeClassAllocator{32,64}LocalCache`).
The cache defines many size classes and maintains free lists for these
classes. Upon an allocation request, if the free list for the requested
size class is empty, the cache will call `Refill` to grab
more chunks from `SizeClassAllocator{32,64}`. If the free
list is not empty, the cache hands over a chunk from the free list to
the user.

`SizeClassAllocator64` has a total allocator space of
`kSpaceSize` bytes. The space is split into multiple regions
of the same size (`kSpaceSize`), each serving a single size
class. When the cache calls `Refill`,
`SizeClassAllocator64` takes a lock of the region and calls
`mmap` to allocate a new memory mapping (and if
`kMetadataSize!=0`, another memory mapping for metadata). For
an active allocation, it is very efficient to compute its index in the
region and its associated metadata.

### Stop the world

On Linux, the runtime invokes the clone syscall to create a tracer
thread. The tracer thread calls `ptrace` with
`PTRACE_ATTACH` to stop every other thread.

## Runtime options

Specify the environment variable `LSAN_OPTIONS` to toggle
runtime behaviors.

For standalone LSan, `exitcode=23` is the default. The
runtime calls `_exit(23)` upon leaks. For ASan-integrated
LSan, `exitcode=1` is the default.

`LSAN_OPTIONS=use_registers=0:use_stack=0:use_tls=0` can
remove some default root regions.

`leak_check_at_exit=0` disables registering an
`atexit` hook for leak checking.

`report_objects=1` reports the addresses of individual
leaked objects.

`detect_leaks=0` disables all leak checking, including
user-requested ones due to `__lsan_do_leak_check` or
`__lsan_do_recoverable_leak_check`. This is similar to
defining
`extern "C" int __lsan_is_turned_off() { return 1; }` in the
program. Using standalone ...
---
title: All about LeakSanitizer
url: https://maskray.me/blog/2023-02-12-all-about-leak-sanitizer
source: MaskRay
date: 2023-02-13
fetch_date: 2025-10-04T06:27:39.648060
---

# All about LeakSanitizer

# [MaskRay](/blog/)

[Home](/blog/)
[Archives](/blog/archives/)
[Feeds](/blog/../feeds/)
[TIL](/blog/../til/)
[Presentations](/blog/../presentations/)

[![](/icon/github.svg)](https://github.com/MaskRay "GitHub")
[![](/icon/twitter.svg)](https://twitter.com/HaskRay "Twitter")



[2023-02-12](/blog/2023-02-12-all-about-leak-sanitizer)

# All about LeakSanitizer

Clang and [GCC 4.9](https://gcc.gnu.org/PR59061)
implemented LeakSanitizer in 2013. [LeakSanitizer](https://clang.llvm.org/docs/LeakSanitizer.html)
(LSan) is a memory leak detector. It intercepts memory allocation
functions and by default detects memory leaks at `atexit`
time. The implementation is purely in the runtime
(`compiler-rt/lib/lsan`) and no instrumentation is
needed.

LSan has very little architecture-specific code and supports many
64-bit targets. Some 32-bit targets (e.g. Linux arm/x86-32) are
supported as well, but there may be high false negatives because
pointers with fewer bits are more easily confused with integers/floating
points/other data of a similar pattern. Every supported operating system
needs to provide some way to "stop the world".

## Usage

LSan can be used in 3 ways.

* Standalone (`-fsanitize=leak`)
* AddressSanitizer (`-fsanitize=address`)
* HWAddressSanitizer (`-fsanitize=hwaddress`)

The most common way to use LSan is
`clang -fsanitize=address` (or
`gcc -fsanitize=address`). For LSan-supported targets
(`#define CAN_SANITIZE_LEAKS 1`), the AddressSanitizer (ASan)
runtime enables LSan by default.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 ``` | ``` % cat a.c #include <stdlib.h> int main() {   void **p = malloc(42); // leak (categorized as "Direct leak")   *p = malloc(43);       // leak (categorized as "Indirect leak")   p = 0; } % clang -fsanitize=address a.c -o a % ./a  ================================================================= ==594015==ERROR: LeakSanitizer: detected memory leaks  Direct leak of 42 byte(s) in 1 object(s) allocated from:     #0 0x55fffef9482e  (/tmp/c/a+0xea82e)     #1 0x55fffefcf1d1  (/tmp/c/a+0x1251d1)     #2 0x7f7301626189  (/lib/x86_64-linux-gnu/libc.so.6+0x27189) (BuildId: c4f6727c560b1c33527ff9e0ca0cef13a7db64d2)  Indirect leak of 43 byte(s) in 1 object(s) allocated from:     #0 0x55fffef9482e  (/tmp/c/a+0xea82e)     #1 0x55fffefcf1df  (/tmp/c/a+0x1251df)     #2 0x7f7301626189  (/lib/x86_64-linux-gnu/libc.so.6+0x27189) (BuildId: c4f6727c560b1c33527ff9e0ca0cef13a7db64d2)  SUMMARY: AddressSanitizer: 85 byte(s) leaked in 2 allocation(s). ``` |

As a runtime-only feature, `-fsanitize=leak` is mainly for
link actions. When linking an executable, with the default
`-static-libsan` mode on many targets, Clang Driver passes
`--whole-archive $resource_dir/lib/$triple/libclang_rt.lsan.a --no-whole-archive`
to the linker. GCC and some platforms prefer shared runtime/dynamic
runtime. See [All
about sanitizer interceptors](/blog/2023-01-08-all-about-sanitizer-interceptors#elf-platforms).

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` % clang -fsanitize=leak a.o '-###' |& grep --color lsan ... --whole-archive" "/tmp/Rel/lib/clang/17/lib/x86_64-unknown-linux-gnu/libclang_rt.lsan.a" "--no-whole-archive" ... % gcc -fsanitize=leak a.o '-###' |& grep --color lsan ... /usr/lib/gcc/x86_64-linux-gnu/12/liblsan_preinit.o --push-state --no-as-needed -llsan ... ``` |

`-fsanitize=leak` affects compile actions as well, but
only for the following C/C++ preprocessor feature.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 ``` | ``` // Active if -fsanitize=leak #if __has_feature(leak_sanitizer) ... #endif  // Active if -fsanitize=leak or -fsanitize=address #if __has_feature(leak_sanitizer) || __has_feature(address_sanitizer) #endif ``` |

## Implementation overview

Standalone LSan intercepts malloc-family and free-family functions.
It uses the temporized `SizeClassAllocator{32,64}` with chunk
metadata. The interceptors record the allocation information (requested
size, stack trace).

AddressSanitizer and HWAddressSanitizer already intercept
malloc-family functions. Their chunk metadata representations have a
flag field for LSan.

By default the common options `detect_leaks` and
`leak_check_at_exit` are enabled. The runtime installs a hook
with `atexit` which will perform the leak check.
Alternatively, the user can call `__lsan_do_leak_check` to
request a leak check before the exit time.

Upon a leak check, the runtime performs a job very similar to a
mark-and-sweep garbage collection algorithm. It suspends all threads
("stop the world") and scans the root set to find reachable allocations.
The root set includes:

* ignored allocations due to `__lsan_ignore_object`,
  `__lsan::ScopedDisabler`, or `__lsan_disable`
* global regions (`__lsan::ProcessGlobalRegions`). On
  Linux, these refer to memory mappings due to writable
  `PT_LOAD` program headers. This ensures that allocations
  reachable by a global variable are not leaks.
* for each thread, general-purpose registers (default
  `use_registers=1`), stacks (default
  `use_stacks=1`), thread-local storage (default
  `use_tls=1`), and additional pointers in the thread
  context
* root regions due to `__lsan_register_root_region`
* operating system specific allocations. This is currently
  macOS-specific: libdispatch and Foundation memory regions, etc.

(When ASan is used and `use_stacks` is enabled, fake
stacks are also in the root set for `use-after-return`
detection. See
`compiler-rt/test/lsan/TestCases/use_after_return.cpp`.)

The runtimes uses a flood fill algorithm to find reachable
allocations from the root set. This done conservatively by finding all
aligned bit patterns which look like a pointer. If the word looks like a
pointer into the heap (many 64-bit targets use
`[0x600000000000, 0x640000000000)` as the allocator space),
the runtime checks whether it refers to an allocated chunk. In
Valgrind's terms, a reference can be a "start-pointer" (a pointer to the
start of the chunk) or an "interior-pointer" (a pointer to the middle of
the chunk).

Finally, the runtime iterates over all allocated allocations and
reports leaks for unmarked allocations.

### Metadata

Each allocation reserves 2 bits to record its state:
leaked/reachable/ignored. For better diagnostics, "leaked" can be direct
or indirect (Valgrind memcheck's term). If a chunk is marked as leaked,
all chunks reachable from it are marked as indirectly leaked.
(`*p = malloc(43);` in the very beginning example is an
indirect leak.)

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` enum ChunkTag {   kDirectlyLeaked = 0,  // default   kIndirectlyLeaked = 1,   kReachable = 2,   kIgnored = 3 }; ``` |

The idea may be that after the user fixes all direct leaks, indirect
leaks will likely go away if directly leaked objects have destructors to
deallocate their references. However, indirect leaks may form a cycle
and fixing all direct leaks does not fix these indirect leaks.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 ``` | ``` #include <stdlib.h> #include <stdio.h> int main() {   void *x = malloc(8), *y = malloc(8);   *(void **)x = y;   // in a cycle. Indirect leak   *(void **)y = x;   // in a cycle. Indirect leak   printf("%p %p\n", x, y); } ``` |

Standalone LSan uses this chunk metadata struct:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 ``` | ``` struct ChunkMetadata {   u8 allocated : 8;  // Must be first.   ChunkTag tag : 2; #if SANITIZER_WORDSIZE == 64   uptr requested_size : 54; #else   uptr requested_size : 32;   uptr padding : 22; #endif   u32 stack_trace_id; }; ``` |

ASan just stores a 2-bit `ChunkTag` in its existing chunk
metadata (`__asan::Chunkheader::lsan_tag`). Similarly, HWASan
stores a 2-bit `ChunkTag` in its existing chunk metadata
(`__hwasan::Metadata::lsan_tag`).

### Allocator

Sanitizers use very similar allocators. To share code,
`compiler-rt/lib/sanitizer_common` defines temporized
`SizeClassAllocator{32,64}` as allocator factories. Each
sanitizer instantiates one of `S...
---
title: All about UndefinedBehaviorSanitizer
url: https://maskray.me/blog/2023-01-29-all-about-undefined-behavior-sanitizer
source: MaskRay
date: 2023-01-30
fetch_date: 2025-10-04T05:09:59.262218
---

# All about UndefinedBehaviorSanitizer

# [MaskRay](/blog/)

[Home](/blog/)
[Archives](/blog/archives/)
[Feeds](/blog/../feeds/)
[TIL](/blog/../til/)
[Presentations](/blog/../presentations/)

[![](/icon/github.svg)](https://github.com/MaskRay "GitHub")
[![](/icon/twitter.svg)](https://twitter.com/HaskRay "Twitter")



[2023-01-29](/blog/2023-01-29-all-about-undefined-behavior-sanitizer)

# All about UndefinedBehaviorSanitizer

Updated in 2025-01.

[UndefinedBehaviorSanitizer](https://clang.llvm.org/docs/UndefinedBehaviorSanitizer.html)
(UBSan) is an undefined behavior detector for C/C++. It consists of code
instrumentation and a runtime. Both components have multiple independent
implementations.

Clang [implemented](https://github.com/llvm/llvm-project/commit/a3e2ff19e59c587ea14611eb64400c6d0ecabcee)
the first few checks in 2009-12, initially named
`-fcatch-undefined-behavior`. In 2012
`-fsanitize=undefined` was added and
`-fcatch-undefined-behavior` was [removed](https://github.com/llvm/llvm-project/commit/b1b0ab41e79f4f11ab21e6e56ded7147241f8615).
GCC 4.9 [implemented](de5a5fa1395db2cb5da4d0593fef40ec22378576)
`-fsanitize=undefined` in 2013-08.

The runtime used by Clang lives in
`llvm-project/compiler-rt/lib/ubsan`. GCC from time to time
syncs its downstream fork of the sanitizers part of compiler-rt
(`libsanitizer`). The end of the article lists some
alternative runtime implementations.

## Available checks

There are many undefined behavior [checks](https://clang.llvm.org/docs/UndefinedBehaviorSanitizer.html)
which can be detected. One can specify `-fsanitize=xxx,yyy`
where xxx and yyy are the names of the individual checks, or more
commonly, specify `-fsanitize=undefined` to enable all of
them.

Some checks are not undefined behavior per language standards, but
are often code smell and lead to surprising results. They are
`implicit-unsigned-integer-truncation`,
`implicit-integer-sign-change`,
`unsigned-integer-overflow`, etc.

We can use `-###` to get the list of default UBSan checks.

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` % clang -fsanitize=undefined -xc /dev/null '-###' ... -fsanitize=alignment,array-bounds,bool,builtin,enum,float-cast-overflow,function,integer-divide-by-zero,nonnull-attribute,null,pointer-overflow,return,returns-nonnull-attribute,shift-base,shift-exponent,signed-integer-overflow,unreachable,vla-bound,vptr" "-fsanitize-recover=alignment,array-bounds,bool,builtin,enum,float-cast-overflow,function,integer-divide-by-zero,nonnull-attribute,null,pointer-overflow,returns-nonnull-attribute,shift-base,shift-exponent,signed-integer-overflow,vla-bound,vptr" ... ``` |

GCC implements [slightly
fewer](https://gcc.gnu.org/onlinedocs/gcc/Instrumentation-Options.html##:~:text=fsanitize=undefined) checks than Clang.

If any check in the "undefined" group is enabled,
`#if __has_feature(undefined_behavior_sanitizer)` will
apply.

## Modes

UBSan provides 3 modes to allow tradeoffs between code size and
diagnostic verboseness.

* Default mode
* Minimal runtime (`-fsanitize-minimal-runtime`)
* Trap mode (`-fsanitize-trap=undefined`): no runtime

Let's use the following program to compare the instrumentation and
runtime behaviors.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 ``` | ``` #include <stdio.h> int foo(int a) { return a * 2; } int main() {   int x;   scanf("%d", &x);   printf("a %d\n", foo(x));   printf("b %d\n", foo(x)); } ``` |

### Default mode

With the umbrella option `-fsanitize=undefined` or the
specific `-fsanitize=signed-integer-overflow`, Clang emits
the following LLVM IR for `foo`:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 ``` | ``` define dso_local i32 @foo(i32 noundef %a) local_unnamed_addr #0 { entry:   %0 = add i32 %a, 1073741824   %1 = icmp sgt i32 %0, -1   br i1 %1, label %cont, label %handler.mul_overflow, !prof !4, !nosanitize !5  handler.mul_overflow:                             ; preds = %entry   %2 = zext i32 %a to i64, !nosanitize !5   tail call void @__ubsan_handle_mul_overflow(ptr nonnull @1, i64 %2, i64 2) #3, !nosanitize !5   br label %cont, !nosanitize !5  cont:                                             ; preds = %handler.mul_overflow, %entry   %3 = shl i32 %a, 1   ret i32 %3 } ``` |

The `add` and `icmp` instructions check whether
the argument is in the range [-0x40000000, 0x40000000) (no overflow). If
yes, the `cont` branch is taken and the non-overflow result
is returned. Otherwise, the emitted code calls the callback
`__ubsan_handle_mul_overflow` (implemented by the runtime)
with arguments describing the source location.

By default, all UBSan checks except `return,unreachable`
are recoverable (i.e. non-fatal). After
`__ubsan_handle_mul_overflow` (or another callback) prints an
error, the program keeps executing. The source location is marked and
further errors about this location are [suppressed](https://github.com/llvm/llvm-project/commit/765c266892d712db91b2a1677584f09feb862109).
This deduplication feature makes logs less noisy. In one program
invocation, we may observe errors from potentially multiple source
locations.

We can let Clang exit the program upon a UBSan error (with error code
1, customized by `UBSAN_OPTIONS=exitcode=2`). Just specify
`-fno-sanitize-recover` (alias for
`-fno-sanitize-recover=all`),
`-fno-sanitize-recover=undefined`, or
`-fno-sanitize-recover=signed-integer-overflow`. A non-return
callback will be emitted in place of
`__ubsan_handle_mul_overflow`. Note that the emitted LLVM IR
terminates the basic block with an `unreachable` instruction.

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` handler.mul_overflow:                             ; preds = %entry   %2 = zext i32 %a to i64, !nosanitize !5   tail call void @__ubsan_handle_mul_overflow_abort(ptr nonnull @1, i64 %2, i64 2) #4, !nosanitize !5   unreachable, !nosanitize !5 ``` |

#### Linking

The UBSan callbacks are provided by the runtime. For a link action,
we need to inform the compiler driver that the runtime should be linked.
This can be done by specifying `-fsanitize=undefined`.
(Actually, any specific UBSan check that needs runtime can be used, e.g.
`-fsanitize=signed-integer-overflow`.)

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` clang -c -O2 -fsanitize=undefined a.c clang -fsanitize=undefined a.o -o a ``` |

Some checks (`function,vptr`) call C++ specific callbacks
implemented in `libclang_rt.ubsan_standalone_cxx.a`. We need
to use `clang++ -fsanitize=undefined` for the link action (or
use
`clang -fsanitize=undefined -fsanitize-link-c++-runtime`).

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` % clang -fsanitize=undefined a.o '-###' |& grep --color ubsan ... "--whole-archive" ".../libclang_rt.ubsan_standalone.a" "--no-whole-archive" "--dynamic-list=.../libclang_rt.ubsan_standalone.a.syms" ... % clang++ -fsanitize=undefined a.o '-###' |& grep --color ubsan ... "--whole-archive" ".../libclang_rt.ubsan_standalone.a" "--no-whole-archive" "--dynamic-list=.../libclang_rt.ubsan_standalone.a.syms" "--whole-archive" ".../libclang_rt.ubsan_standalone_cxx.a" "--no-whole-archive" "--dynamic-list=.../libclang_rt.ubsan_standalone_cxx.a.syms" ... % clang++ -fsanitize=undefined -shared-libsan a.o '-###' |& grep --color ubsan ... ".../libclang_rt.ubsan_standalone.so" ... ``` |

When linking an executable, with the default
`-static-libsan` mode on many targets, Clang Driver passes
`--whole-archive $resource_dir/lib/$triple/libclang_rt.ubsan.a --no-whole-archive`
to the linker. GCC and some platforms prefer shared runtime/dynamic
runtime. See [All
about sanitizer interceptors](/blog/2023-01-08-all-about-sanitizer-interceptors#elf-platforms).

Some sanitizers (`address`, `memory`,
`thread`, etc) ship a copy of UBSan runtime files.

### Minimal runtime

The default mode provides verbose diagnostics which help programmers
identify the undefined behavior. On the other hand, the detailed log
helps attackers and the code size may be a concern in some
configurations.

UBSan provides a minimal runtime mode to log very little information.
Specify `-f...
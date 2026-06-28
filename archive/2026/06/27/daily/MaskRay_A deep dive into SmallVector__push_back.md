---
title: A deep dive into SmallVector::push_back
url: https://maskray.me/blog/2026-06-27-a-deep-dive-into-smallvector-push-back
source: MaskRay
date: 2026-06-27
fetch_date: 2026-06-28T06:13:39.039387
---

# A deep dive into SmallVector::push_back

# [MaskRay](/blog/)

[Home](/blog/)
[Archives](/blog/archives/)
[Feeds](/blog/../feeds/)
[TIL](/blog/../til/)
[Presentations](/blog/../presentations/)

[![](/icon/github.svg)](https://github.com/MaskRay "GitHub")
[![](/icon/twitter.svg)](https://twitter.com/HaskRay "Twitter")



[2026-06-27](/blog/2026-06-27-a-deep-dive-into-smallvector-push-back)

# A deep dive into SmallVector::push\_back

tl;dr This blog post describes a recent
`SmallVector::push_back` optimization for approximately
trivially copyable element types.

`SmallVector` is LLVM's most-used container, and
`push_back` its hot operation. For the trivially-copyable
specialization the fast path should be fast.

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` #include <llvm/ADT/SmallVector.h>  void f(llvm::SmallVectorImpl<int> &v, int x) { v.push_back(x); } ``` |

`clang -S --target=x86_64 -O2 -DNDEBUG a.cc`
generates:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 ``` | ``` push   rbp                 # callee-saved spills + a stack realignment, push   rbx                 # all on the fast path push   rax mov    eax, [rdi + 8]      # size cmp    eax, [rdi + 12]     # vs capacity jae    .Lgrow .Lstore:                   # reached from the fast path AND from .Lgrow mov    rcx, [rdi] mov    [rcx + rax*4], esi inc    dword ptr [rdi + 8] add    rsp, 8 pop    rbx pop    rbp ret .Lgrow: mov    rbx, rdi            # keep `this`/`x` alive across the call mov    ebp, esi call   SmallVectorBase<unsigned>::grow_pod ... jmp    .Lstore ``` |

`push_back` reserves capacity and *then* stores, so
the store at `.Lstore` is shared between the no-grow and
post-grow paths. On the grow path `this` and `x`
must survive the `grow_pod` call, which means they are saved
in callee-saved registers, leading to
`push rbx`/`push rbp` in the prologue.
`push rbp` is needed to maintain the 16-byte alignment of the
stack frame.

GCC's output is also inefficient:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` push   rbp ; mov ebp, esi    # x -> rbp, in the entry block push   rbx ; mov rbx, rdi    # this -> rbx ... ; cmp ; jnb .Lslow .Lmerge:                     # reached by both paths, reads rbx/rbp mov    rdx, [rbx] ; mov [rdx+rax*4], ebp ; ... ``` |

## Shrink wrapping can't remove it

Shrink wrapping relocates the save/restore of callee-saved registers;
it never duplicates a block. To carry `this`/`x`
across the conditional `grow_pod` call into a store the fast
path also reaches, a callee-saved register must be live from entry.
`clang -mllvm -debug-only=shrink-wrap` reports
`No Shrink wrap candidate found`. GCC's
`-fshrink-wrap-separate` (on at `-O2`) does not
optimize this as well.

The transformation that *would* help is tail duplication â
give the slow path its own copy of the store so the fast path keeps
`this`/`x` in their argument registers. Neither
compiler does it here, and it is not shrink-wrapping's job.

## Optimization: tail calling the slow path

<https://github.com/llvm/llvm-project/pull/206213> moves
the grow-and-store out of line and tail calls it:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 ``` | ``` LLVM_ATTRIBUTE_NOINLINE void growAndPushBack(ValueParamT Elt) {   T Tmp = Elt;  // in case Elt aliases storage that grow() invalidates   this->grow(this->size() + 1);   std::memcpy(reinterpret_cast<void *>(this->end()), &Tmp, sizeof(T));   this->set_size(this->size() + 1); }  void push_back(ValueParamT Elt) {   if (LLVM_UNLIKELY(this->size() >= this->capacity()))     return growAndPushBack(Elt);   std::memcpy(reinterpret_cast<void *>(this->end()), &Elt, sizeof(T));   this->set_size(this->size() + 1); } ``` |

The generated assembly is now optimal for the fast path:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 ``` | ``` mov    eax, [rdi + 8] cmp    eax, [rdi + 12] jae    growAndPushBack         # TAILCALL mov    rcx, [rdi] mov    [rcx + rax*4], esi inc    dword ptr [rdi + 8] ret ``` |

7 instructions instead of 14, no callee-saved registers, nothing to
shrink-wrap.

The slow path, now in an out-of-line function (in a separate section
using COMDAT), becomes even slower.

`noinline` is load-bearing, otherwise Clang and GCC may
inline the helper back and the prologue returns.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 ``` | ``` #include <llvm/ADT/SmallVector.h> // noinline growAndPushBack is load-bearing for both Clang and GCC. void DecodeMOVDDUPMask(unsigned n, llvm::SmallVectorImpl<int> &v) {   for (unsigned l = 0; l < n; l += 2)     for (unsigned i = 0; i < 2; ++i)       v.push_back(i); } ``` |

`T Tmp = Elt` handles `Elt` referencing the
vector's own storage. It is elided for small by-value types. While the
out-of-line call has a drawback that the element's address escapes,
defeating construct-in-place for large element types, the one copy is
negligible since grow has to copy `size()` elements.

## Results

`lld` `.text` shrinks 40,512 bytes;
by-`const&` element types win most, e.g.
`GotSection::addConstant` goes 167Â âÂ 45 bytes. On the [LLVM compile-time
tracker](https://llvm-compile-time-tracker.com/) the clang build is 0.41â0.51% fewer
`instructions:u` across every configuration, for +0.13%
binary size.

Sorted by relative size, a few outliers grow ~13.8% â the constexpr
ByteCode interpreter (`Interp.cpp`,
`EvalEmitter.cpp`). A smaller `push_back` likely
perturbs the bottom-up inliner's near-threshold decisions.

## `std::vector<T>::push_back` is slow in both libc++ and libstdc++

Both libraries need a stack frame for their
`vector<int>::push_back` fast path. <https://godbolt.org/z/5h85M9Gr9>

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 ``` | ``` #include <llvm/ADT/SmallVector.h> #include <vector>  void pb_int(std::vector<int> &v, int x) { v.push_back(x); } void pb_int(llvm::SmallVectorImpl<int> &v, int x) { v.push_back(x); }  struct T {int x[32];}; void pb_Tcreate(std::vector<T> &v, int x){ v.push_back(T{{x, 1}}); } void pb_Tcopy(std::vector<T> &v, const T &t){ v.push_back(t); }  void pb_Tcreate(llvm::SmallVectorImpl<T> &v, int x){ v.push_back(T{{x, 1}}); } void pb_Tcopy(llvm::SmallVectorImpl<T> &v, const T &t){ v.push_back(t); } ``` |

libc++'s `push_back` forwards to
`emplace_back`, which routes the grow decision through
`std::__if_likely_else(cond, fast, slow)`. The slow path is
kept out of line, but as a by-reference lambda, so its closure
`{&__end_, &__x, this}` is materialized on the stack
and the trailing `this->__end_ = __end` is a merge. The
fast path therefore spills the closure and runs with a 48-byte
frame:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 ``` | ``` push   rbx sub    rsp, 48 mov    [rsp+12], esi          # spill x mov    rax, [rdi+8]           # __end mov    [rsp+16], rax lea    rcx, [rsp+16] ; mov [rsp+24], rcx   # } closure {&__end, lea    rcx, [rsp+12] ; mov [rsp+32], rcx   # }  &x, this}, built mov    [rsp+40], rdi                       # }  on the fast path jae    .Lslow                # else: store x; this->__end_ = __end ``` |

libstdc++ is heavier still: its `push_back` inlines
`_M_realloc_insert`, pulling the whole reallocation â
`operator new`, `memcpy`,
`operator delete`, and the `length_error` throw â
into the function. To keep state live across those calls the fast path
holds six callee-saved registers, on both g++ and clang.

A direct out-of-line member taking `(this, Elt)` in
registers â the `growAndPushBack` above â is what keeps the
fast path free of both a frame and callee-saved registers.

Note: many libc++ builds enable [hardening](https://libcxx.llvm.org/Hardening.html) by default.
Disable it (and exceptions) for the best performance:

|  |  |
| --- | --- |
| ``` 1 ``` | ``` -fno-exceptions -D_LIBCPP_HARDENING_MODE=_LIBCPP_HARDENING_MODE_NONE ``` |

## Boost's small\_vector has the same frame

`boost::container::small_vector<int, N>::push_back`
tells the same story, independent of the inline capacity `N`
(even `N == 0`):

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 ``` | ``` sub    rsp, ...
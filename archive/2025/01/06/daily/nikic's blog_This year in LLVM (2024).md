---
title: This year in LLVM (2024)
url: https://www.npopov.com/2025/01/05/This-year-in-LLVM-2024.html
source: nikic's blog
date: 2025-01-06
fetch_date: 2025-10-06T20:09:18.674126
---

# This year in LLVM (2024)

Blog by **nikic**.
Find me on [GitHub](https://github.com/nikic),
[StackOverflow](https://stackoverflow.com/users/385378/nikic),
[Twitter](http://twitter.com/nikita_ppv) and
[Mastodon](https://mastodon.social/%40nikic).
Learn more [about me](/aboutMe.html).

[« Back to article overview.](/)

# This year in LLVM (2024)

05. January 2025

Another year has passed, so it’s once again time for my yearly summary blog post. As usual, this summary is mostly about my own work, and only covers the more significant / higher level items.

Previous years: [2023](https://www.npopov.com/2024/01/01/This-year-in-LLVM-2023.html), [2022](https://www.npopov.com/2022/12/20/This-year-in-LLVM-2022.html)

## ptradd

I started working on the [ptradd migration](https://discourse.llvm.org/t/rfc-replacing-getelementptr-with-ptradd/68699) last year, but the first significant steps towards it only landed this year. The goal is to move away from the type-based/structural `getelementptr` (GEP) instruction, to a `ptradd` instruction, which does no more and no less than adding an offset to a pointer. The value of that offset is computed using normal mul/add instructions, if necessary.

The general implementation approach is to gradually canonicalize all getelementptrs into `getelementptr i8` representation, which is equivalent to `ptradd`, at which point we can remove support for specifying other types.

The first step was to [canonicalize constant-offset GEPs](https://github.com/llvm/llvm-project/pull/68882). For example, `getelementptr i32, ptr %p, i64 1` becomes `getelementptr i8, ptr %p, i64 4`, removing the implicit multiplication. Just this step already fixed a number of optimization failures caused by the old representation. Of course, it also exposed new optimization weaknesses, like [insufficient select unfolding in SROA](https://github.com/llvm/llvm-project/pull/80983).

The second step was to [canonicalize constant-expression GEPs](https://github.com/llvm/llvm-project/pull/89872) as well. That is, `getelementptr (i32, ptr @g, i64 1)` is converted to `getelementptr (i8, ptr @g, i64 4)`. However, this first required a change to how the `inrange` attribute on GEP constant expressions is represented.

```
; Old:
getelementptr inbounds ({ [4 x ptr], [4 x ptr] }, ptr @vt, i64 0, inrange i32 1, i64 2)
; New:
getelementptr inbounds inrange(-16, 16) (i8, ptr @vt, i64 48)
```

`inrange` is a niche feature that is only used when generating vtables. It specifies that the GEP result can only be accessed in a limited range, which enables global splitting. Previously, this range was specified by marking a GEP index as `inrange`, limiting any accesses to occur “below” that index only. The new representation explicitly specifies the range of valid offsets instead, which removes the dependence on the structural GEP type.

The next step for this project will be to canonicalize `getelementptr` instructions with variable offsets as well, in which case we will have to emit explicit offset arithmetic. I hope we can take this step next year.

## getelementptr nuw

I have worked on a number of new instruction flags, the most significant of which are probably the [`nusw` (no unsigned-signed wrap) and `nuw` (no unsigned wrap) flags for `getelementptr`](https://discourse.llvm.org/t/rfc-add-nusw-and-nuw-flags-for-getelementptr/78672).

Getelementptr instructions already supported the `inbounds` flag, which indicates that the pointer arithmetic cannot go outside the underlying allocated object. This also implies that the addition of the pointer, interpreted as an unsigned number, and the offset, interpreted as a signed number, cannot wrap around the address space.

This implied property can now be specified using the `nusw` flag, without also requiring the stronger `inbounds` property. The intention of this change is to be more explicit about which property transforms actually need, and to allow frontends (e.g. Rust) to experiment with alternative semantics that don’t require the hard to formalize `inbounds` concept.

However, the much more useful new flag is `nuw`, which specifies that the addition of the address and the offset does not wrap in an unsigned sense. Combined with `nusw` (or `inbounds`), it implies that the offset is non-negative. This flag fixes two key problems.

The first are bounds/overflow check elimination failures caused by not knowing that an offset is non-negative. For example, if we have a check like `ptr + offset >= ptr`, we want it to optimize to `true`, for the case where `offset` is unsigned and pointer arithmetic cannot wrap. Previously this was not possible, because the frontend had no way to convey that this is a valid optimization to LLVM.

The second is accesses to structures like `struct vec { size_t len; T elems[N]; }`. The `nuw` flag allows us to convey that `vec.elems[i]` cannot access the `len` field using a negative `i`.

The core work for the new GEP flags is complete. Both alias analysis and comparison simplification can take advantage of them. However, there is still a good bit of work that can be done to preserve the new flags in all parts of the compiler.

One interesting complication of the `nuw` flag is the interaction with incorrectly implemented overflow checks in C code. The `ptr + offset >= ptr` example above is something we want to be able to optimize, because this kind of pattern can, for example, appear when using a hardened STL implementation.

However, a C programmer might also write literally that check with the intention of detecting an overflowing pointer addition. This is incorrect, because `ptr + offset` will already trigger UB on overflow (or, in fact, just going out of bounds of the underlying object). These incorrect overflow checks will now be optimized away.

I have [extended](https://github.com/llvm/llvm-project/pull/120222) the `-Wtautological-compare` warning to catch trivial cases of this problem, and the `-fsanitize=pointer-overflow` warning catches the issue reliably – if you have test coverage.

## trunc nuw/nsw

Another new set of instruction flags are the [`nuw` and `nsw` flags on `trunc`](https://discourse.llvm.org/t/rfc-add-nowrap-flags-to-trunc/77453). These flags specify that only zero bits (nuw) or sign bits (nsw) are truncated. The important optimization property of these new flags is that `zext (trunc nuw (x))` is just `x` and `sext (trunc nsw (x))` is also just `x`.

These kinds of patterns commonly occur when booleans are converted between their i1 value and i8 memory representation, or during widening of induction variables.

Unfortunately, rolling out these flags did not go as smoothly as expected. While we do take advantage of the new flags to some degree, we don’t actually perform the motivating `zext (trunc nuw (x)) -> x` fold yet, and instead keep folding this to `and x, 1` (for i1). The reason is that completely eliminating the zext/trunc loses the information that only the low bit may be set. We need to strengthen some other optimizations before we’ll be able to take this step.

## icmp samesign

Yet another new instruction flag is [`samesign` on `icmp` instructions](https://discourse.llvm.org/t/rfc-signedness-independent-icmps/81423). As one might guess from the name, it indicates that both sides of the comparison have the same sign, i.e. are both non-negative or both negative.

If `samesign` is set, we can freely convert between signed and unsigned comparison predicates. The motivation is that LLVM generally tries to canonicalize signed to unsigned operations, including for comparisons. So something like `icmp slt` will become `icmp ult` if we can prove the operands have the same sign. However, after this has happened, later passes may have a hard time understanding how this unsigned comparison relates to another signed comparison that has related operands. The `samesign` flag allows easily converting back to a signed predicate when needed.

The bring-up work for `samesign` has only just started, so there’s b...
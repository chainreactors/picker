---
title: This year in LLVM (2025)
url: https://www.npopov.com/2026/01/31/This-year-in-LLVM-2025.html
source: nikic's blog
date: 2026-01-31
fetch_date: 2026-02-01T04:26:44.674557
---

# This year in LLVM (2025)

Blog by **nikic**.
Find me on [GitHub](https://github.com/nikic),
[StackOverflow](https://stackoverflow.com/users/385378/nikic),
[Twitter](http://twitter.com/nikita_ppv) and
[Mastodon](https://mastodon.social/%40nikic).
Learn more [about me](/aboutMe.html).

[« Back to article overview.](/)

# This year in LLVM (2025)

31. January 2026

It’s 2026, so it’s time for my yearly summary blog post. I’m a bit late, but at least it’s still January! As usual, this summary is about my own work, and only covers the more significant / higher-level items.

Previous years: [2024](https://www.npopov.com/2025/01/05/This-year-in-LLVM-2024.html), [2023](https://www.npopov.com/2024/01/01/This-year-in-LLVM-2023.html), [2022](https://www.npopov.com/2022/12/20/This-year-in-LLVM-2022.html)

## ptradd

I have been making slow progress on the [ptradd migration](https://discourse.llvm.org/t/rfc-replacing-getelementptr-with-ptradd/68699?u=nikic) over the last three years. The goal of this change is to move away from the type-based `getelementptr` (GEP) representation, towards a `ptradd` instruction, which just adds an integer offset to a pointer.

The state at the start of the year was that constant-offset GEP instructions were canonicalized to the form `getelementptr i8, ptr %p, i64 OFFSET`, which is equivalent to a `ptradd`.

The progress this year was to canonicalize all GEP instructions to have a single offset. For example, `getelementptr [10 x i32], ptr %p, i64 %a, i64 %b` gets split into two instructions now. This moves us closer to `ptradd`, which only accepts a single offset argument. However, the change is also independently useful, because it allows CSE of common GEP prefixes.

This work happened in multiple phases, first splitting [multiple variable indices](https://github.com/llvm/llvm-project/pull/137297), then splitting off [constant indices as well](https://github.com/llvm/llvm-project/pull/151333) and finally removing [leading zero indices](https://github.com/llvm/llvm-project/pull/155415).

As usual, the bulk of the work was not in the changes themselves, but in mitigating resulting regressions. Many transforms were extended to work on chains of GEPs rather than only a single one. Once again, this is also useful independently of the ptradd migration, as chained GEPs were already very common beforehand.

There are still some major remaining pieces of work to complete this migration. The first one is to decide whether we want `ptradd` to support a constant scaling factor, or require it to be represented using a separate multiplication. There are good arguments in favor of both options.

The second one is to move from mere canonicalization towards requiring the new form. This would probably involve first making IRBuilder emit it, and then actually preventing construction of the type-based form. That would be the point where we’d actually introduce the `ptradd` instruction.

## ptrtoaddr

LLVM 22 [introduces](https://github.com/llvm/llvm-project/pull/139357) a new `ptrtoaddr` instruction. This is the outcome of a [long discussion](https://discourse.llvm.org/t/clarifiying-the-semantics-of-ptrtoint/83987?u=nikic) on the semantics of `ptrtoint` and pointer comparisons for [CHERI architectures](https://en.wikipedia.org/wiki/Capability_Hardware_Enhanced_RISC_Instructions).

The semantics of `ptrtoaddr` are similar to `ptrtoint`, but differ in two respects:

* It does not expose the provenance of the pointer. In Rust terms, it corresponds to `addr()` instead of `expose_provenance()`.
* It returns only the address portion of the pointer. This matters for CHERI, where pointers also carry additional metadata bits.

A non-exposing way to convert a pointer into an integer is an important step towards figuring out LLVM’s provenance story. LLVM currently ignores the fact that `ptrtoint` has an (exposure) side-effect, and having a side-effect-free alternative is one of the prerequisites to actually taking this seriously. (The other is the [byte type](https://discourse.llvm.org/t/rfc-add-a-new-byte-type-to-llvm-ir/89522?u=nikic).)

The downside of having two instructions that do something similar but not quite the same is that it requires careful adjustment of existing optimizations to work on both forms, where possible. This is something I have been working on, and `ptrtoaddr` should now be supported in most of the important optimizations.

## Lifetime intrinsics

LLVM represents stack allocations using `alloca` instructions. These are generally always placed inside the entry block, while the actual lifetime of the allocation is marked using [`lifetime.start`](https://llvm.org/docs/LangRef.html#llvm-lifetime-start-intrinsic) and [`lifetime.end`](https://llvm.org/docs/LangRef.html#llvm-lifetime-end-intrinsic) intrinsics. The primary purpose of these intrinsics is to enable stack coloring, which can place stack allocations that are not live at the same time at the same address, greatly reducing stack usage.

I have made two major changes to lifetime intrinsics: The first is to enforce that they are [only used with allocas](https://github.com/llvm/llvm-project/pull/149310). Previously, it was possible to use them on arbitrary pointers, such as function arguments. This is incompatible with stack coloring, which requires that all lifetime markers for an allocation are visible – they can’t be hidden behind a function call.

Making this an IR validity requirement was helpful in uncovering quite a few cases where we ended up using lifetimes on non-allocas by mistake, as a result of optimization passes. Most commonly, the alloca was accidentally obscured by phi nodes.

The second change was to [remove the size argument](https://github.com/llvm/llvm-project/pull/150248) from lifetime intrinsics. In theory, this argument allowed you to control the lifetime of a subset of the allocation. In practice, this was never used, and stack coloring just ignored the argument. This was a smaller change in terms of IR semantics, but significantly larger in impact because it required updates to all code and tests involving lifetime intrinsics.

While these changes have resolved some issues with our handling of lifetimes, more problems (with [store speculation](https://github.com/llvm/llvm-project/issues/51838) and [comparisons](https://github.com/llvm/llvm-project/issues/45725)) remain. A core issue is that in the current representation, it’s not possible to efficiently determine whether an alloca is live at a given point, or whether the lifetime of two allocas can overlap. Fixing this requires more intrusive changes.

## Capture tracking

Another piece of work that carried over from the previous year are improvements to capture tracking. I [proposed](https://discourse.llvm.org/t/rfc-improvements-to-capture-tracking/81420?u=nikic) this last year, but the majority of the implementation work happened this year.

The most important part of this proposal is that we now distinguish between capturing the address of a pointer, and its provenance. Many optimizations only care about the latter, because only provenance capture may result in non-analyzable memory effects.

The most significant changes to enable this were [inference support](https://github.com/llvm/llvm-project/pull/125880), and updating alias analysis to only check for [provenance captures](https://github.com/llvm/llvm-project/pull/130777) and make use of [read-only captures](https://github.com/llvm/llvm-project/pull/143097).

I’ve also extended this feature by adding [`!captures` metadata](https://github.com/llvm/llvm-project/pull/160913) on stores. This is intended to allow encoding that stores of non-mut references in Rust only capture read provenance, which is helpful to optimize around constructs like `println!()`, which capture via memory rather than function arguments. Whether we can actually do this depends on an [open question](https://github.com/rust-lang/unsafe-code-guidelines/issues/371) in Rust’s aliasing model.

## ABI

One of the...
---
title: Recent LLVM hash table improvements
url: https://maskray.me/blog/2026-06-07-recent-llvm-hash-table-improvements
source: MaskRay
date: 2026-06-07
fetch_date: 2026-06-08T06:32:40.593447
---

# Recent LLVM hash table improvements

# [MaskRay](/blog/)

[Home](/blog/)
[Archives](/blog/archives/)
[Feeds](/blog/../feeds/)
[TIL](/blog/../til/)
[Presentations](/blog/../presentations/)

[![](/icon/github.svg)](https://github.com/MaskRay "GitHub")
[![](/icon/twitter.svg)](https://twitter.com/HaskRay "Twitter")



[2026-06-07](/blog/2026-06-07-recent-llvm-hash-table-improvements)

# Recent LLVM hash table improvements

LLVM has several hash tables. They used quadratic probing with
in-band sentinel keys (empty, tombstone); recent work has been replacing
that with linear probing with tombstone key removed.

* `DenseMap` (replacement for
  `std::unordered_map`):
  `DenseMapInfo::getEmptyKey()` /
  `getTombstoneKey()`.
  + `DenseSet`: implemented using `DenseMap`
  + `compiler-rt/lib/sanitizer_common/sanitizer_dense_map.h`
    ports the implementation for sanitizers.
* `SmallPtrSet` (replacement for
  `std::unordered_set<T *>`): hard-coded `-1`
  (empty) and `-2` (tombstone).
* `StringMap` (replacement for
  `std::unordered_map<std::string, V>`)
  + `StringSet`: implemented using
    `StringMap`

For the open-addressed `DenseMap` and
`SmallPtrSet`, pointers, references, and iterators are
invalidated by insert. `StringMap` is different: each entry
lives in a heap-allocated `StringMapEntry<V>` node, so
entry pointers survive grow. `std::unordered_map`, being
node-based, keeps surviving-element pointers valid across both insert
and erase and only invalidates the erased element's own iterator. LLVM
code rarely needs that stronger contract â callers do not hold
long-lived references into the container across mutation â and that gap
is what gives pass to relocating erase and bit-array occupancy.

Recently,

* Tombstones have been removed from DenseMap and SmallPtrSet.
  `erase()` also invalidates pointers.
* DenseMap has also retired its empty-key sentinel, leading to
  significant performance improvements. DenseMap with integer keys
  (`int`/`unsigned`/`size_t`) had
  `-1`/`-2` reserved â a footgun, now fixed.
* TODO: pending patch on StringMap

## SmallPtrSet

SmallPtrSet has a small mode, used when the number of elements is
below a threshold, and a large mode. The tombstone state was removed by
[#96762](https://github.com/llvm/llvm-project/pull/96762) in
2024. The patch changed `erase()` operation to invalidate
iterators, requiring treewide fixes.

The large mode used a quadratic probing with two sentinel keys
(empty, tombstone).

Knuth TAOCP Vol. 3 Â§6.4 Algorithm R describes an algorithm that
avoids lazy deletion. [#197637](https://github.com/llvm/llvm-project/pull/197637) has
implemented it.

I've investigated Robin Hood Hashing and Abseil Swiss Table family
implementations - both would lead to inferior performance. Robin Hood
Hashing primarily improves find-miss on high-load factors but imposes a
small cost on find-hit and inserts.

## DenseMap

Two major changes have been merged:

* Replace the tombstone state with Algorithm R deletion. ([#200595](https://github.com/llvm/llvm-project/pull/200595))
* Replace the empty state with a bitarray. ([#201281](https://github.com/llvm/llvm-project/pull/201281))

### What the workload looks like

An instrumented clang counts every `(KeyT, ValueT)`
operation while compiling
`llvm/lib/Analysis/ScalarEvolution.cpp`. **597**
distinct `DenseMap`/`DenseSet` types,
**~186M** user ops:

| op | count | probes mean |
| --- | --- | --- |
| find-hit | 65.2M | 1.55 |
| find-miss | 65.7M | 1.28 |
| insert | 47.8M | 1.71 |
| erase | 7.0M | â |
| grow | 1.5M | â |

Lookups are ~70% of the load; insert ~26%, erase ~4%. Probe means sit
between 1.3 and 1.7 â well inside what linear probing handles.
`operator[]` is classified at the bucket it lands on: a
present key is counted as find-hit, an empty slot as insert.

A few instantiations carry most of the traffic:

| type | find-hit | find-miss (mean) | insert | erase | grow | peak |
| --- | --- | --- | --- | --- | --- | --- |
| `DenseMap<const void *, Pass *>` | 680K | 24.8M (1.03) | 202K | 202K | 9.3K | 1 KiB |
| `DenseMap<Value *, ValueHandleBase *>` | 2.8M (2.02) | 0 | 2.2M | 2.2M | 11 | 1 MiB |
| `DenseMap<const Value *, StringMapEntry<Value *> *>` | 3.0M | 1.4M (2.26) | 540K | 439K | 13 | 4 MiB |
| `DenseMap<DeclarationName, StoredDeclsList>` | 772K | 1.2M (1.94) | 143K | 0 | 9.0K | 64 KiB |
| `DenseMap<LazyCallGraph::Node *, LazyCallGraph::SCC *>` | 1.3M | 98K (2.95) | 175K | 173K | 15 | 258 KiB |
| `DenseMap<AnalysisKey *, bool>` | 2.8M | 2.0M (1.52) | 2.0M | 0 | 124K | 1 KiB |

`DenseMap<const void *, Pass *>` runs 25.5M lookups
at 1.03 mean â volume is not clustering.
`DenseMap<Value *, ValueHandleBase *>` is the single
largest erase consumer at 2.2M; this is the workload where the Algorithm
R relocating-erase callback earns its keep. Its find-miss column is zero
because every access in `llvm/lib/IR/Value.cpp` goes through
`operator[]` or `erase` â there is no
`find`/`lookup` call site, so an empty-slot probe
is bucketed as insert rather than find-miss. The bucket's value-slot
address is captured by
`ValueHandleBase *&Entry = Handles[V]` and stored as a
linked-list back-pointer (`PrevPtr`), which is exactly what
the new `OnMoved` callback refreshes when Algorithm R shifts
neighbors. `StringMapEntry` peaks at 4 MiB, the regime where
the used-bit array's byte overhead matters most. Structural and
graph-pointer keys (`DeclarationName`,
`LazyCallGraph::Node *`) still cost a couple of extra probes
per miss.

Code size matters. SIMD tables may be a poor fit.

### Linear probing + Algorithm R deletion ([#200595](https://github.com/llvm/llvm-project/pull/200595))

Linear probing needs a strong pointer hash. The old
`DenseMapInfo<T*>::getHashValue`
(`(p>>4)^(p>>9)`) never mixes the high bits of
the address. Pointers from one allocator grown across multiple slabs map
to the same narrow bucket range, bad under linear probing. Quadratic
probing had masked this issue. [#197390](https://github.com/llvm/llvm-project/pull/197390)
switched to a stronger mixer, unblocking both SmallPtrSet and DenseMap.
[#199369](https://github.com/llvm/llvm-project/pull/199369)
tightened DenseMap's `erase()` to invalidate iterators under
`LLVM_ENABLE_ABI_BREAKING_CHECKS`, surfacing stale-iterator
call sites before Algorithm R could crash on them.

#200595 replaces quadratic probing plus tombstones with linear
probing plus Algorithm R. Two bucket states, no lazy markers. Erase now
relocates following entries to close the hole, so entry pointers may be
invalidated. The new `erase(Key, OnMoved)` and
`erase(iterator, OnMoved)` overloads fire a callback once per
shifted bucket; `ValueHandleBase::RemoveFromUseList` uses
this to refresh `PrevPtr`.

The first attempt had a war story. The original landed as [#199615](https://github.com/llvm/llvm-project/pull/199615),
then got reverted by [#200421](https://github.com/llvm/llvm-project/pull/200421)
after a SCEV crash: `PoisoningVH` cached a bare bucket
pointer across an op that, post-Algorithm R, relocates. The bug was
latent under tombstones, which don't relocate, and only surfaced once
the algorithm flipped. Fixed in [#200540](https://github.com/llvm/llvm-project/pull/200540),
relanded as #200595.

On stage1-O3 the change is **-1.34%** instructions and
all ten CTMark benchmarks improve between -0.85% and -1.61% ([compare](https://llvm-compile-time-tracker.com/compare.php?from=90779840d51aa3fff6fa030ade7150bc647ac5ff&to=1f10f1ca8af3dff956b353d7ff3ea169c82ed909&stat=instructions:u)).
Clang wall is **-1.54%**, stage1 binary
**-1.40%** â fewer bucket states means less generated code.
The commit message remarks that *"the in-band sentinel value approach
â¦ is the best, or at least very difficult to beat."* The used-bit
array below earns the right to violate this.

### Packed used-bit array ([#201281](https://github.com/llvm/llvm-project/pull/201281))

The empty-slot test has switched from `getEmptyKey()` to a
bit test. There is a 1-bit-per-bucket `uint32` array sharing
one allocation wit...
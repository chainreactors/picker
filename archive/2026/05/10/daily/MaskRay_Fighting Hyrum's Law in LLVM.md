---
title: Fighting Hyrum's Law in LLVM
url: https://maskray.me/blog/2026-05-10-fighting-hyrums-law-in-llvm
source: MaskRay
date: 2026-05-10
fetch_date: 2026-05-11T05:54:56.343837
---

# Fighting Hyrum's Law in LLVM

# [MaskRay](/blog/)

[Home](/blog/)
[Archives](/blog/archives/)
[Feeds](/blog/../feeds/)
[TIL](/blog/../til/)
[Presentations](/blog/../presentations/)

[![](/icon/github.svg)](https://github.com/MaskRay "GitHub")
[![](/icon/twitter.svg)](https://twitter.com/HaskRay "Twitter")



[2026-05-10](/blog/2026-05-10-fighting-hyrums-law-in-llvm)

# Fighting Hyrum's Law in LLVM

> *With a sufficient number of users of an API, it does not matter
> what you promise in the contract: all observable behaviors of your
> system will be depended on by somebody.* â Hyrum's Law

In a compiler, the most common form of Hyrum's Law is dependence on
*unspecified behavior* â hash bucket order, the order of equal
elements after `std::sort`, padding offsets. The same framing
covers a few cases that are technically undefined behavior (use of an
invalidated iterator) or plain incidental properties (ABI struct layout,
ELF section offsets).

When the compiler itself harbors such a dependency, the symptom is
usually output that varies build-to-build: an unstable sort that lands
differently after the standard library changes, a hash map whose
iteration order shifts when the hash function does. Occasionally the
variation is run-to-run within a single build â
`DenseMap<void *, X>` keys with an ASLR-derived seed
reorder buckets each invocation. Either way, reproducible builds,
bisection, and bug reports all assume same input â same output, and a
stealth Hyrum dependency breaks that.

This post surveys some mechanisms that perturb the contract's blind
spots so dependencies cannot quietly form.

## Hash seed perturbation

The first line of defense is the hash function itself.
`llvm/include/llvm/ADT/Hashing.h`:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 ``` | ``` inline uint64_t get_execution_seed() { #if LLVM_ENABLE_ABI_BREAKING_CHECKS   return static_cast<uint64_t>(       reinterpret_cast<uintptr_t>(&install_fatal_error_handler)); #else   return 0xff51afd7ed558ccdULL; #endif } ``` |

The seed XORed into every `llvm::hash_value` is the
runtime address of `install_fatal_error_handler` â under
ASLR, different every process. The header comment is explicit:

> *the seed is non-deterministic per process (address of a function
> in LLVMSupport) to prevent having users depend on the particular hash
> values.*

Every `hash_combine` / `hash_integer_value`
call picks up the seed, and every `DenseMap<K, V>`
keyed by a `hash_value`-using type then reorders its buckets
per run. MD5, BLAKE3, SHA1, SHA256 stay byte-stable â those are the
right tools when you actually want a digest.

My [commit
`ce80c80dca45`](https://github.com/llvm/llvm-project/commit/ce80c80dca45) introduced the seed in 2024.

## Container iteration order

Code can grow dependencies on the iteration order.
`LLVM_ENABLE_REVERSE_ITERATION` walks hash containers
backwards to flag violations.
`llvm/include/llvm/Support/ReverseIteration.h`:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 ``` | ``` template <class T = void *> constexpr bool shouldReverseIterate() { #if LLVM_ENABLE_REVERSE_ITERATION   return detail::IsPointerLike<T>::value; #else   return false; #endif } ``` |

`DenseMap` flips its `BucketItTy` to
`std::reverse_iterator<pointer>`;
`SmallPtrSet` swaps `begin()` and
`end()`; `StringMap` bitwise-NOTs the hash before
bucket selection â the only thing that perturbs `StringMap`,
since its hash bypasses `get_execution_seed`.

Unlike the hash seed, reverse iteration isn't auto-on with
assertions; `-DLLVM_REVERSE_ITERATION=ON` opts in explicitly.
In 2026 has already merged fixes triggered by it: [`7f703cabf728`](https://github.com/llvm/llvm-project/commit/7f703cabf728)
(MLIR SSA-value completion order), [`0b3afd35c41d`](https://github.com/llvm/llvm-project/commit/0b3afd35c41d)
(MLIR SROA alloca order), and [`f5e2c5ddcec7`](https://github.com/llvm/llvm-project/commit/f5e2c5ddcec7)
(a clang test).

## Iterator invalidation

Orthogonal to iteration order: what happens to an existing iterator
after a mutation. `llvm/include/llvm/ADT/EpochTracker.h`:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 ``` | ``` class DebugEpochBase {   uint64_t Epoch = 0; public:   void incrementEpoch() { ++Epoch; }   ~DebugEpochBase() { incrementEpoch(); }  // catches use-after-free    class HandleBase {     bool isHandleInSync() const {       return *EpochAddress == EpochAtCreation;     }   }; }; ``` |

`DenseMap` and friends inherit from
`DebugEpochBase`. Mutations bump the epoch; iterators capture
it at construction and assert on mismatch. The destructor bumps too, so
stale iterators into destroyed containers assert rather than read freed
memory.

Without it, mutate-during-iteration "happens to work" depending on
bucket layout â and bucket layout is what the hash seed and reverse
iteration above perturb. The epoch check turns the latent bug into a
clean assert regardless of which "lucky" layout the run lands on.
Collapses to a no-op under `NDEBUG`.

## Pre-shuffling unstable sorts

The same defensive pattern shows up twice in the monorepo, in
different sub-projects, years apart.

### `llvm::sort` under `EXPENSIVE_CHECKS`

`llvm/include/llvm/ADT/STLExtras.h`:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 ``` | ``` #ifdef EXPENSIVE_CHECKS namespace detail { inline unsigned presortShuffleEntropy() {   static unsigned Result(std::random_device{}());   return Result; }  template <class IteratorTy> inline void presortShuffle(IteratorTy Start, IteratorTy End) {   std::mt19937 Generator(presortShuffleEntropy());   llvm::shuffle(Start, End, Generator); } } // end namespace detail #endif  template <typename IteratorTy, typename Compare> inline void sort(IteratorTy Start, IteratorTy End, Compare Comp) { #ifdef EXPENSIVE_CHECKS   detail::presortShuffle<IteratorTy>(Start, End); #endif   std::sort(Start, End, Comp); } ``` |

`std::sort` and `qsort` are unstable; code
observing the order of equal elements is depending on undocumented
behavior. Pre-shuffling makes that observation different every run. [commit
`5a3d47fabcb6`](https://github.com/llvm/llvm-project/commit/5a3d47fabcb6) added the wrapper in 2018, motivated by [PR35135](https://bugs.llvm.org/show_bug.cgi?id=35135).

LLVM also ships its own `llvm::shuffle` rather than
calling `std::shuffle`, "so that LLVM behaves the same when
using different standard libraries." A reproducibility tool whose
reproducibility depends on the host stdlib is worse than no tool â and
the linker section below relies on this.

`llvm::stable_sort` deliberately does not pre-shuffle; it
is the explicit opt-in for code that legitimately needs ordering of
equal elements.

### libc++ `_LIBCPP_DEBUG_RANDOMIZE_UNSPECIFIED_STABILITY`

libc++ has a near-perfect parallel mechanism, designed for downstream
users rather than the project's own internals.
`libcxx/include/__debug_utils/randomize_range.h`:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 ``` | ``` template <class _AlgPolicy, class _Iterator, class _Sentinel> _LIBCPP_HIDE_FROM_ABI _LIBCPP_CONSTEXPR_SINCE_CXX14 void __debug_randomize_range(_Iterator __first, _Sentinel __last) { #ifdef _LIBCPP_DEBUG_RANDOMIZE_UNSPECIFIED_STABILITY   if (!__libcpp_is_constant_evaluated())     std::__shuffle<_AlgPolicy>(__first, __last, __libcpp_debug_randomizer()); #else   (void)__first; (void)__last; #endif } ``` |

Three callsites:

* `std::sort` â pre-shuffles the input.
* `std::partial_sort` â pre-shuffles the input *and*
  re-shuffles the unsorted tail afterward.
* `std::nth_element` â pre-shuffles, then re-shuffles each
  side of the partition.

Seed handling rhymes with `get_execution_seed`: ASLR or
static `std::random_device` for per-process variation, with
`_LIBCPP_RANDOMIZE_UNSPECIFIED_STABILITY_SEED=<n>` as a
fixed-seed escape hatch. Off by default; C++11 and later only.

`libcxx/docs/DesignDocs/UnspecifiedBehaviorRandomization.rst`
explains the motivation:

> *Google has measured couple of thousands of tests to be depende...
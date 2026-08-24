---
title: Block frequency
url: https://maskray.me/blog/block-frequency
source: MaskRay
date: 2026-08-23
fetch_date: 2026-08-24T02:58:57.651983
---

# Block frequency

# [MaskRay](/blog/)

[Home](/blog/)
[Archives](/blog/archives/)
[Feeds](/blog/../feeds/)
[TIL](/blog/../til/)
[Presentations](/blog/../presentations/)

[![](/icon/github.svg)](https://github.com/MaskRay "GitHub")
[![](/icon/twitter.svg)](https://twitter.com/HaskRay "Twitter")



[2026-08-23](/blog/block-frequency)

# Block frequency

[Estimating branch
probabilities](/blog/estimating-branch-probabilities) says how one branch splits.
`BlockFrequencyInfo` turns those local numbers into per-block
frequencies, which nearly every profitability decision in LLVM ends up
reading.

The core is a linear-time propagation over loop-packaged regions.
Where no such structure exists â irreducible control flow â the accuracy
goes with it.

## What it produces

`getBlockFreq(BB)` returns a `BlockFrequency`,
a bare `uint64_t` with no unit. `finalizeMetrics`
rescales each function so that its *hottest* block lands on
2âµâ´.

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` const unsigned Slack = 10; Scaled64 ScalingFactor = Scaled64(1, MaxBits - Slack) / Max;  // Max: the hottest block ``` |

As `opt -passes='print<block-freq>'` on a module
shows:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 ``` | ``` block-frequency-info: hot  - entry: float = 1.0,  int = 562949953421312     <- 2^49  - loop:  float = 32.0, int = 18014398509481984   <- 2^54  - exit:  float = 1.0,  int = 562949953421312  block-frequency-info: flat  - entry: float = 1.0,  int = 18014398509481984   <- 2^54  - a:     float = 0.5,  int = 9007199254740992  - b:     float = 0.5,  int = 9007199254740992 ``` |

The two printed columns do not share a reference: `float`
is the frequency with the *entry* at 1.0, `int` is the
same frequency with the *hottest block* at 2âµâ´.

`MachineBlockFrequencyInfo::getBlockFreqRelativeToEntryBlock`
divides by `getEntryFreq()` to recover the entry-relative
ratio, which is the whole of what register allocation weights a spill
by. Turning a frequency into a count needs a profile as well:

|  |  |
| --- | --- |
| ``` 1 ``` | ``` count(BB) = entryCount Ã freq(BB) / freq(entry) ``` |

`getProfileCountFromFreq` returns nothing when the
function carries no entry count â which is how `isHotBlock`
and the rest degrade to "unknown" rather than to "cold".

2âµâ´ rather than `UINT64_MAX` because consumers add
frequencies up and multiply them by instruction costs, and
`Slack = 10` leaves room before those saturate. At the other
end every block is floored at 1: the coldest-to-hottest range rarely
fits in 64 bits, and the comment says outright that the precision is
spent on the hot end.

Until `finalizeMetrics` runs, a frequency is a
`Scaled64` â `ScaledNumber<uint64_t>`, a
software float with a 64-bit significand and an exponent. Loop scales
compose multiplicatively, so the range runs far past anything a fraction
of one could hold; the integers above are the last step, not the working
representation.

## Mass, packaging, scale

BFI propagates mass one loop level at a time. The scheme is the
propagation half of Wu and Larus, *Static Branch Frequency and
Program Profile Analysis* (MICRO-27, 1994), though nothing in the
tree cites it.

Blocks are numbered in reverse post-order, and a
`BlockNode`'s index **is** its RPO index â which
is why later code can test edge direction with a plain
`<`.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 ``` | ``` compute(F):   for L in loop forest of F, innermost first:     sweep(L)     L.scale = 1 / (1 - L.BackedgeMass)     package L: one pseudo-node reusing its header's RPO number,                whose successors are the exits sweep(L) recorded   sweep(F)                                 # every loop is a single node by now   freq = mass                              # each block's mass within its innermost region   for L in loop forest of F, outermost first:     scale = L.scale * freq[L.package]      # final already; read before the writes below     for b in members(L):       freq[b] = mass[b] * scale  # members(R) are R's *immediate* members, in RPO order.  A nested loop contributes # exactly one node, its package, never its blocks.  For the function that means every # block outside any loop, plus one node per top-level loop.  sweep(R):                                  # R is one loop, or the whole function   mass[entry of R] = 1   for b in members(R):     for (b -> s, w) in succWeights(b):     # a package reports its recorded exits       m = mass[b] * w / total weight out of b       if s is R's header:   R.BackedgeMass += m       elif s is outside R:  R.Exits += (s, m)       else:                 mass[s] += m ``` |

`sweep` runs on a DAG and computes `mass[b]`,
the probability that a walk from the header passes through
`b`. A backedge deposits into `BackedgeMass`
instead of being followed and every sub-loop is already a single node,
so RPO is a topological order there and one pass suffices:
`O(V+E)`. GCC's `propagate_freq` instead re-walks
each block once per loop depth, `O(VÂ·D)`.

Mass is therefore a fraction of one, and the `1` above is
a `BlockMass`: a `uint64_t` in which
`BlockMass::getFull()` â `UINT64_MAX` â is that
one. Fixed point, so a split across successors recombines exactly;
`distributeMass` dithers the remainder, an even split of full
mass giving `8000000000000000` and
`7fffffffffffffff`, which add back to
`ffffffffffffffff`. Distribution stays exact; the scales, and
the frequencies built from them, are `Scaled64`.

The scale is the geometric series: return 90% of the mass to the
header and the loop runs 10 times.

What makes this sound is that a natural loop's header is its
*only* way in. All mass enters there, so each member's mass comes
out a fixed multiple of the header's, determined by the branch
probabilities alone. The loop's internal shape and its scale are settled
without knowing anything outside it, and `unwrapLoops`
supplies the header's real frequency afterwards â one multiplication,
applied to a shape that never needed revising.

An irreducible loop has no such invariant. Mass enters at several
blocks at once, and the members' relative frequencies depend on how it
splits among those entries â a ratio fixed by the enclosing region, not
by the SCC.

## Irreducible loops

A natural loop is a strongly connected component with one way in, its
header. An SCC with two or more entries is *irreducible*. It is
packaged like a loop â the lowest-RPO member stands for the package and
donates its RPO number â and `solveIrreducibleMass` settles
the members instead.

The routine is up against one missing number: inside the region the
frequencies solve

|  |  |
| --- | --- |
| ``` 1 ``` | ``` f = e + fP ``` |

with `P` the intra-SCC probabilities and `e`
the mass arriving from outside at each entry. Packaging is bottom-up:
the SCC has to collapse to a single node before the enclosing region is
swept, because that sweep is only valid on a DAG â but `e` is
what that sweep produces. At solve time it does not exist yet. A natural
loop does not care, its `e` being a scalar on the one header;
an irreducible SCC's is a distribution over its entries, and its shape
is part of the answer.

So the solve drops `e`. It starts `F` uniform
over the members and iterates `F â FÂ·P`, converging towards
**Ï**, the dominant left eigenvector of `P`: the
shape the SCC settles into after circulating a long time, whichever way
the entry mass split. Members carrying
`!irr_loop_header_weight` â PGO metadata recording a measured
frequency for an irreducible header â are held fixed instead, and the
rest settle around them.

What that gives up shows in the true solution. Expand it as a series,
where term `k` is the mass that came in through the entries
and has since gone round the SCC `k` times. Split
`e` along the eigenvectors of `P` â
`e = câÏ + câeâ + â¯`, with `Î»áµ¢` the eigenvalue
belonging to `eáµ¢` â and that series collapses:

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` f = ...
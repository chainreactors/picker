---
title: Irreducible loops
url: https://maskray.me/blog/2026-07-12-irreducible-loops
source: MaskRay
date: 2026-07-12
fetch_date: 2026-07-13T05:30:06.886698
---

# Irreducible loops

# [MaskRay](/blog/)

[Home](/blog/)
[Archives](/blog/archives/)
[Feeds](/blog/../feeds/)
[TIL](/blog/../til/)
[Presentations](/blog/../presentations/)

[![](/icon/github.svg)](https://github.com/MaskRay "GitHub")
[![](/icon/twitter.svg)](https://twitter.com/HaskRay "Twitter")



[2026-07-12](/blog/2026-07-12-irreducible-loops)

# Irreducible loops

The [dominator tree](/blog/2020-12-11-dominator-tree) lets
us identify [natural loops](/blog/2025-01-20-natural-loops):
a back edge `T->H` whose head `H` dominates its
tail `T` defines a loop with the single entry `H`.
This works only for *reducible* control flow graphs. Optimized
machine code and decompiler output routinely contain
*irreducible* loops, which have more than one entry and thus no
dominating header, so the dominator-based method cannot see them.

This post builds a loop-nesting forest for an arbitrary CFG with the
single-pass depth-first search of é¦é¬ãæ¯åãé¹ç»´ãéå®(Tao Wei, Jian
Mao, Wei Zou & Yu Chen) *A New Algorithm for Identifying Loops in
Decompilation*, SAS 2007 (The 14th International Static Analysis
Symposium).

## Reducibility

A depth-first search from the entry classifies every non-tree edge
relative to the spanning tree. A *retreating edge*
`u->v` goes to an ancestor `v` of
`u` on the DFS path. A *cycle* is a closed path in the
CFG, a graph-theoretic object with no distinguished entry; a
*loop* is the control-flow structure built on top â a set of
nodes with a header, nested into a forest. (LLVM draws the same line:
`LoopInfo` represents natural loops, while the
`GenericCycleInfo` used below generalizes them to irreducible
control flow.) A CFG is *reducible* when, in every DFS, each
retreating edge is a *back edge* â its head `v`
dominates its tail `u`. Then every cycle lies in a natural
loop whose header dominates it, so control enters the loop only through
that header.

A CFG is *irreducible* when some cycle has two or more
entries: nodes with a predecessor outside the cycle. No single node
dominates the cycle, so there is no natural header. The smallest example
is the *irreducible core*:

![The irreducible core: 0 enters the 1â2 cycle at both nodes. Double circle = header (1, visited first); dashed = the re-entry edge.](/static/2026-07-12-irreducible-loops/core.svg)

The irreducible core: 0 enters the 1âï¸2
cycle at both nodes. Double circle = header (1, visited first); dashed =
the re-entry edge.

Node 0 branches to both 1 and 2, and `1 -> 2 -> 1`
is a cycle entered at 1 (through `0->1`) and at 2 (through
`0->2`). M.S. Hecht and J.D. Ullman proved that a CFG is
irreducible if and only if it contains this three-node pattern as a
subgraph, allowing each edge to be a path through other nodes.

Because no node dominates an irreducible cycle, its header is not
intrinsic â we must pick one of the entries. The standard choice
(Havlak, LLVM, and the algorithm below) is the node the DFS reaches
first, i.e. the loop member with the smallest preorder number. So the
loop-nesting forest of an irreducible CFG depends on the DFS order.

## Loop-nesting forest

There is no agreed definition of the loop-nesting forest for
irreducible CFGs. Steensgaard, SreedharâGaoâLee, Havlak, and Ramalingam
each give a different one; for the CFG in Wei et al.'s Fig. 3 they
report two, one, three, and one loops respectively. We adopt Havlak's,
the finest, because it gives each loop a single header and the fewest
`goto`s when re-structuring, and it is what LLVM's
`GenericCycleInfo` computes:

* The outermost loops are the maximal strongly connected regions (with
  at least one internal edge).
* A loop's header is its minimum-preorder node.
* Its inner loops are the loops of the subgraph induced on (loop nodes
  â header), found recursively.

The forest has a compact encoding. For each node record its
*innermost loop header* `iloop_header`: the header of
the smallest loop containing it, or none. A header's own
`iloop_header` is the header of its parent loop. Following
the `iloop_header` links from a node lists its enclosing
loops innermost-first â the "loop header list" of the paper. Which nodes
are headers, plus every node's innermost header, determines the whole
forest; that is what the program below prints.

## Identifying loops in one DFS pass

Natural loops need a dominator tree first. Wei et al. observe that a
single DFS with a little bookkeeping suffices for an arbitrary CFG â no
dominator tree, no UNION-FIND, no second bottom-up pass.

Let `p` be the current DFS path, the recursion stack from
the entry to the node being visited (`DFSP` in the paper).
`pos[b]` is `b`'s 1-based position on that path,
or 0 once `b` has been popped. Every node carries
`iloop_header`, its innermost loop header discovered so far.
When visiting `b0`, each successor `b` falls into
one of five cases:

* 1. `b` is unvisited â a tree edge. Recurse; the call returns
     `b`'s innermost header, which we merge into `b0`'s
     chain.
* 2. `b` is on the current path (`pos[b] > 0`) â
     a back edge. `b` is a loop header; merge it into
     `b0`.
* 3. `b` is finished and in no loop â a forward or cross edge
     to a non-loop node; ignore it.
* 4. `b` is finished, inside a loop whose innermost header
     `h` is still on the path â `b0` belongs to that
     loop too; merge `h`.
* 5. `b` is finished, inside a loop whose innermost header is
     *not* on the path â the edge `b0->b` enters the
     loop below its header: a *re-entry edge*, and the loop is
     *irreducible*. Walk up `b`'s header chain to the first
     header that is on the path and merge that.

Merging a header (`tag_lhead`) splices it into the node's
innermost-to-outermost chain, ordered by DFS position; this replaces the
UNION-FIND of the classical HavlakâTarjan algorithm. The total cost is
`O(N + k*E)`, where `k` is an *unstructuredness
coefficient* that measures the case-(E) climbs and the chain
splices. On real code `k` is tiny (empirically below 1.5), so
the algorithm is near-linear.

The input format matches the natural-loops post: `n m` on
the first line, then `m` edges `u v`, with node 0
the entry. The program prints each node's innermost loop header, then
the forest, then any re-entry edges.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 ``` | ``` // Identify loops in an arbitrary (possibly irreducible) CFG in a single DFS // pass -- Wei, Mao, Zou, Chen, SAS 2007. #include <cstdio> #include <utility> #include <vector> using namespace std;  // Per-node DFS state kept together (AoS), matching the paper's `Block` fields: // the hot path touches a node's ilh/pos/traversed as a unit, so one cache line // per node beats five parallel arrays. struct Node {   int ilh = -1;             // iloop_header: innermost loop header, -1 = none   int pos = 0;              // DFSP_pos: 1-based depth on the current DFS path;                             // 0 once the node leaves it (or is unvisited)   bool traversed = false;   // has the DFS reached this node?   bool header = false;      // is this node the header of some loop?   bool irreducible = false; // ...the header of an irreducible (multi-entry) loop? };  vector<Node> nd;                // per-node state, indexed by node id vector<vector<int>> succ;       // successor lists, in input order vector<pair<int, int>> reentry; // re-entry edges b0->b  // Weave loop header h (and its own header chain) into b's innermost-loop-header // chain, keeping the chain ordered innermost..outermost by DFS-path position. // This is what replaces the UNION-FIND merge of the classical Havlak algor...
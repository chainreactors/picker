---
title: Natural loops
url: https://maskray.me/blog/2025-01-20-natural-loops
source: MaskRay
date: 2025-01-21
fetch_date: 2025-10-06T20:09:21.175430
---

# Natural loops

# [MaskRay](/blog/)

[Home](/blog/)
[Archives](/blog/archives/)
[Feeds](/blog/../feeds/)
[TIL](/blog/../til/)
[Presentations](/blog/../presentations/)

[![](/icon/github.svg)](https://github.com/MaskRay "GitHub")
[![](/icon/twitter.svg)](https://twitter.com/HaskRay "Twitter")



[2025-01-20](/blog/2025-01-20-natural-loops)

# Natural loops

A [dominator tree](/blog/2020-12-11-dominator-tree) can be
used to compute natural loops.

* For every node `H` in a post-order traversal of the
  dominator tree (or the original CFG), find all predecessors that are
  dominated by `H`. This identifies all back edges.
* Each back edge `T->H` identifies a natural loop with
  `H` as the header.
  + Perform a flood fill starting from `T` in the reversed
    dominator tree (from exiting block to header)
  + All visited nodes reachable from the root belong to the natural loop
    associated with the back edge. These nodes are guaranteed to be
    reachable from `H` due to the dominator property.
  + Visited nodes unreachable from the root should be ignored.
  + Loops associated with visited nodes are considered subloops.

Here is an C++ implementation:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144 145 146 147 148 149 ``` | ``` #include <cstdio> #include <deque> #include <numeric> #include <vector> using namespace std;  vector<vector<int>> e, ee, edom; vector<int> dfn, dfn2, rdfn, uf, best, sdom, idom; int tick;  void dfs(int u) {   dfn[u] = tick;   rdfn[tick++] = u;   for (int v : e[u])     if (dfn[v] < 0) {       uf[v] = u;       dfs(v);     } }  int eval(int v, int cur) {   if (dfn[v] <= cur)     return v;   int u = uf[v], r = eval(u, cur);   if (dfn[best[u]] < dfn[best[v]])     best[v] = best[u];   return uf[v] = r; }  void semiNca(int n, int r) {   idom.assign(n, -1);   dfn.assign(n, -1);   rdfn.resize(n); // initial values are unused   uf.resize(n); // initial values are unused   sdom.resize(n); // initial values are unused   tick = 0;   dfs(r);   best.resize(n);   iota(best.begin(), best.end(), 0);   for (int i = tick; --i; ) {     int v = rdfn[i];     sdom[v] = v;     for (int u : ee[v])       if (~dfn[u]) {         eval(u, i);         if (dfn[best[u]] < dfn[sdom[v]])           sdom[v] = best[u];       }     best[v] = sdom[v];     idom[v] = uf[v];   }   edom.assign(n, vector<int>());   for (int i = 1; i < tick; i++) {     int v = rdfn[i];     while (dfn[idom[v]] > dfn[sdom[v]])       idom[v] = idom[idom[v]];     edom[idom[v]].push_back(v);   } }  struct Loop {   int idx, header;   Loop *parent = nullptr, *child = nullptr, *next = nullptr;   vector<int> nodes; }; deque<Loop> loops;  void postorder(int u) {   dfn[u] = tick;   for (int v : edom[u])     if (dfn[v] < 0)       postorder(v);   rdfn[tick++] = u;   dfn2[u] = tick; }  void identifyLoops(int n, int r) {   vector<int> worklist;   vector<Loop *> to_loop(n);   dfn.assign(n, -1);   dfn2.assign(n, -1);   tick = 0;   postorder(r);   loops.clear();   for (int i = 0; i < tick; i++) {     int header = rdfn[i];     for (int u : ee[header])       if (dfn[header] <= dfn[u] && dfn2[u] <= dfn2[header])         worklist.push_back(u);     if (worklist.empty())       continue;     loops.push_back(Loop{(int)loops.size(), header});     Loop *lp = &loops.back();     while (worklist.size()) {       int v = worklist.back();       worklist.pop_back();       if (!to_loop[v]) {         if (dfn[v] < 0) // Skip unreachable node           continue;         // Find a node not in a loop.         to_loop[v] = lp;         lp->nodes.push_back(v);         if (v == header)           continue;         for (int u : ee[v])           worklist.push_back(u);       } else {         // Find a subloop.         Loop *sub = to_loop[v];         while (sub->parent)           sub = sub->parent;         if (sub == lp)           continue;         sub->parent = lp;         sub->next = lp->child;         lp->child = sub;         for (int u : ee[sub->header])           if (to_loop[u] != sub)             worklist.push_back(u);       }     }   } }  int main() {   int n, m;   scanf("%d%d", &n, &m);   e.resize(n);   ee.resize(n);   for (int i = 0; i < m; i++) {     int u, v;     scanf("%d%d", &u, &v);     e[u].push_back(v);     ee[v].push_back(u);   }   semiNca(n, 0);   for (int i = 0; i < n; i++)     printf("%d: %d\n", i, idom[i]);    identifyLoops(n, 0);   for (Loop &lp : loops) {     printf("loop %d:", lp.idx);     for (int v : lp.nodes)       printf(" %d", v);     for (Loop *c = lp.child; c; c = c->next)       printf(" (loop %d)", c->idx);     puts("");   } } ``` |

The code iterates over the dominator tree in post-order.
Alternatively, a post-order traversal of the original control flow graph
could be used.

`worklist` may contain duplicate elements. This is
acceptable. You could also deduplicate elements.

Importantly, the header predecessor of a subloop can be another
subloop.

In the final `loops` array, parent loops are listed after
their child loops.

This example examines multiple subtle details: a self-loop (node 6),
an unreachable node (node 8), and a scenario where the header
predecessor of one subloop (nodes 2 and 3) leads to another subloop
(nodes 4 and 5).

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 ``` | ``` 9 12 0 1 1 2 1 7 2 3 2 4 3 2 8 3 4 5 4 6 5 4 6 1 6 6 ``` |

Use
`awk 'BEGIN{print "digraph G{"} NR>1{print $1"->"$2} END{print "}"}'`
to generate a graphviz dot file.

Share

* [algorithm](/blog/tags/algorithm/)
* [graph](/blog/tags/graph/)

[**Newer**

lld 20 ELF changes](/blog/2025-02-02-lld-20-elf-changes)
[**Older**

Understanding and improving Clang -ftime-report](/blog/2025-01-12-understanding-and-improving-clang-ftime-report)

### Popular

### Tag Cloud

[adc](/blog/tags/adc/) [ai9](/blog/tags/ai9/) [algorithm](/blog/tags/algorithm/) [arm](/blog/tags/arm/) [asc](/blog/tags/asc/) [assebmly](/blog/tags/assebmly/) [assembler](/blog/tags/assembler/) [assembly](/blog/tags/assembly/) [automaton](/blog/tags/automaton/) [awesome](/blog/tags/awesome/) [bctf](/blog/tags/bctf/) [binary](/blog/tags/binary/) [binutils](/blog/tags/binutils/) [bmc](/blog/tags/bmc/) [build system](/blog/tags/build-system/) [c](/blog/tags/c/) [c++](/blog/tags/c/) [ccls](/blog/tags/ccls/) [cgc](/blog/tags/cgc/) [chroot](/blog/tags/chroot/) [clang](/blog/tags/clang/) [clang-format](/blog/tags/clang-format/) [codinsanity](/blog/tags/codinsanity/) [coffee script](/blog/tags/coffee-script/) [compiler](/blog/tags/compiler/) [compression](/blog/tags/compression/) [computer security](/blog/tags/computer-security/) [contest](/blog/tags/contest/) [cpp](/blog/tags/cpp/) [csv](/blog/tags/csv/) [ctf](/blog/tags/ctf/) [data structure](/blog/tags/data-structure/) [debug](/blog/tags/debug/) [defcon](/blog/tags/defcon/) [desktop](/blog/tags/desktop/) [docker](/blog/tags/docker/) [elf](/blog/tags/elf/) [emacs](/blog/tags/emacs/) [email](/blog/tags/email/) [emoji](/blog/tags/emoji/) [emscripten](/blog/tags/emscripten/) [event](/blog/tags/event/) [expect](/blog/tags/expect/) [ext4](/blog/tags/ext4/) [fdpic](/blog/tags/fdpic/) [feeds](/blog/tags/feeds/) [firmware](/blog/tags/firmware/) [floating point](/blog/tags/floating-point/) [forensics](/blog/tags/forensics/) [fp](/blog/tags/fp/) [freebsd](/blog/tags/freebsd/) [game](/blog/tags/game/) [gcc](/blog/tags/gcc/) [gdb](/blog/tags/gdb/) [gentoo](/blog/tags/gentoo/) [github](/blog/tags/github/) [glibc](/blog/tags/glibc/) [graph](/blog/tags/graph/) [graph drawing](/blog/tags/graph-drawing/) [gtk](/blog/tags/gtk/) [hacker culture](/blog/tags/hacker-culture/) [hackerrank](/blog/tags/ha...
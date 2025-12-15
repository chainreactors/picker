---
title: Weak AVL Tree
url: https://maskray.me/blog/2025-12-14-weak-avl-tree
source: MaskRay
date: 2025-12-14
fetch_date: 2025-12-15T03:27:15.953453
---

# Weak AVL Tree

# [MaskRay](/blog/)

[Home](/blog/)
[Archives](/blog/archives/)
[Feeds](/blog/../feeds/)
[TIL](/blog/../til/)
[Presentations](/blog/../presentations/)

[![](/icon/github.svg)](https://github.com/MaskRay "GitHub")
[![](/icon/twitter.svg)](https://twitter.com/HaskRay "Twitter")



[2025-12-14](/blog/2025-12-14-weak-avl-tree)

# Weak AVL Tree

tl;dr: Weak AVL trees are replacements for AVL trees and red-black
trees.

The 2014 paper [*Rank-Balanced
Trees*](https://sidsen.azurewebsites.net/papers/rb-trees-talg.pdf) (Haeupler, Sen, Tarjan) presents a framework using ranks
and rank differences to define binary search trees.

* Each node has a non-negative integer rank `r(x)`. Null
  nodes have rank -1.
* The rank difference of a node `x` with parent
  `p(x)` is `r(p(x)) â r(x)`.
* A node is `i,j` if its children have rank differences
  `i` and `j` (unordered), e.g., a 1,2 node has
  children with rank differences 1 and 2.
* A node is called 1-node if its rank difference is 1.

Several balanced trees fit this framework:

* AVL tree: Ranks are defined as heights. Every node is 1,1 or 1,2
  (rank differences of children)
* Red-Black tree: All rank differences are 0 or 1, and no parent of a
  0-child is a 0-child. (red: 0-child; black: 1-child; null nodes are
  black)
* Weak AVL tree (new tree described by this paper): All rank
  differences are 1 or 2, and every leaf has rank 0.
  + A weak AVL tree without 2,2 nodes is an AVL tree.

|  |  |
| --- | --- |
| ``` 1 ``` | ``` AVL trees â« weak AVL trees â« red-black trees ``` |

## Weak AVL Tree

Weak AVL trees are replacements for AVL trees and red-black trees. A
single insertion or deletion operation requires at most two rotations
(forming a double rotation when two are needed). In contrast, AVL
deletion requires O(log n) rotations, and red-black deletion requires up
to three.

Without deletions, a weak AVL tree is exactly an AVL tree. With
deletions, its height remains at most that of an AVL tree with the same
number of insertions but no deletions.

The rank rules imply:

* Null nodes have rank -1, leaves have rank 0, unary nodes have rank
  1.

### Insertion

The new node `x` has a rank of 0, changed from the null
node of rank -1. There are three cases.

* If the tree was previously empty, the new node becomes the
  root.
* If the parent of the new node was previously a unary node (1,2
  node), it is now a 1,1 binary node.
* If the parent of the new node was previously a leaf (1,1 node), it
  is now a 0,1 binary node, leading to a rank violation.

When the tree was previously non-empty, `x` has a parent
node. We call the following subroutine with `x` indicating
the new node to handle the second and third cases.

The following subroutine handles the rank increase of `x`.
We call `break` if there is no more rank violation, i.e. we
are done.

The 2014 paper isn't very clear about the conditions.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 ``` | ``` // Assume that x's rank has just increased by 1 and rank_diff(x) has been updated.  p = x->parent; if (rank_diff(x) == 1) {   // x was previously a 2-child before increasing x->rank.   // Done. } else {   for (;;) {     // Otherwise, p is a 0,1 node (previously a 1,1 node before increasing x->rank).     // x being a 0-child is a violation.      Promote p.     // Since we have promoted both x and p, it's as if rank_diff(x's sibling) is flipped.     // p is now a 1,2 node.          x = p;     p = p->parent;     // x is a 1,2 node.     if (!p) break;     d = p->ch[1] == x;        if (rank_diff(x) == 1) { break; }     // Otherwise, x is a 0-child, leading to a new rank violation.          auto sib = p->ch[!d];     if (rank_diff(sib) == 2) { // p is a 0,2 node       auto y = x->ch[d^1];       if (y && rank_diff(y) == 1) {         // y is a 1-child. y must the previous `x` in the last iteration.         Perform a double rotation involving `p`, `x`, and `y`.       } else {         // Otherwise, y is null or a 2-child.         Perform a single rotation involving `p` and `x`.         x is now a 1,1 node and there is no more violation.       }       break;     }        // Otherwise, p is a 0,1 node. Goto the next iteration.   } } ``` |

Insertion never introduces a 2,2 node, so insertion-only sequences
produce AVL trees.

### Deletion

TODO: Describe deletion

### Implementation

In 2020, FreeBSD has changed its `sys/tree.h` to use weak
AVL trees instead of red-black trees. <https://reviews.freebsd.org/D25480> The `rb_`
prefix remains as it can also indicate `Rank-Balanced`:)

Here is a C++ implementation with the following operations

* `insert`: insert a node
* `remove`: remove a node
* `rank`: count elements less than a key
* `select`: find the k-th smallest element (0-indexed)
* `prev`: find the largest element less than a key
* `next`: find the smallest element greater than a key

The insertion and deletion operations are inspired by the FreeBSD
implementation, with the insertion further optimized.

We encode rank differences instead of the absolute rank values. Since
valid rank differences can only be 1 or 2, a single bit suffices to
encode each. We take 2 bits from the `parent` pointer to
store the two child rank differences.

The paper suggests that each node can use one bit to encode its own
rank difference. However, this representation is not ideal. A null node
can be either a 1-child (parent is binary) or a 2-child (parent is
unary). Retrieving the child rank difference requires probing the
sibling node:

`int rank_diff(Node *p, int d) { return p->ch[d] ? p->ch[d]->par_and_flg & 1 : p->ch[!d] ? 2 : 1; }`

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159 160 161 162 163 164 165 166 167 168 169 170 171 172 173 174 175 176 177 178 179 180 181 182 183 184 185 186 187 188 189 190 191 192 193 194 195 196 197 198 199 200 201 202 203 204 205 206 207 208 209 210 211 212 213 214 215 216 217 218 219 220 221 222 223 224 225 226 227 228 229 230 231 232 233 234 235 236 237 238 239 240 241 242 243 244 245 246 247 248 249 250 251 252 253 254 255 256 257 258 259 260 261 262 263 264 265 266 267 268 269 270 271 272 273 274 275 276 277 278 279 280 281 282 283 284 285 286 287 288 289 290 291 292 293 294 295 296 297 298 299 300 301 302 303 304 305 306 307 308 309 310 311 312 313 314 315 316 317 318 319 320 321 322 323 324 325 326 327 328 329 330 331 332 333 334 335 336 337 338 339 340 341 342 343 344 345 346 347 348 349 350 351 352 353 354 355 356 357 358 359 360 361 362 363 364 365 366 367 368 369 370 371 372 373 374 375 376 377 378 379 380 381 382 383 384 385 386 387 388 389 390 391 392 393 ``` | ``` #include <algorithm> #include <cassert> #include <cstdint> #include <cstdio> #include <cstdlib> #include <numeric> #include <random> #include <vector> using namespace std;  struct Node {   Node *ch[2]{};   uintptr_t par_and_flg{};   int i{}, sum{}, size{};    Node *parent() const { return reinterpret_cast<Node*>(par_and_flg & ~3UL); }   void set_parent(Node *p) { par_and_flg = (par_and_flg & 3) | reinterpret_cast<uintptr_t>(p); }   uintptr_t flags() const { return par_and_flg & 3; }   bool rd2(int d) const { return par_and_flg & (1 << d); }   void flip(int d) { par_and_flg ^= (1 << d); }   void clr_flags() { par_and_flg &= ~3UL; }    void mconcat() {     sum = i;     size = 1;     if (ch[0]) sum += ch[0]->sum, size += ch[0]->size;     if (ch[1]) sum += ch[1]->sum, size += ch[1]->size;   }  ...
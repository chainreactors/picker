---
title: Building Intuition for Lattice-Based Signatures – Part 2: Fiat-Shamir with Aborts
url: https://buaq.net/go-174711.html
source: unSafe.sh - 不安全
date: 2023-08-18
fetch_date: 2025-10-04T11:58:58.981901
---

# Building Intuition for Lattice-Based Signatures – Part 2: Fiat-Shamir with Aborts

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/b2885704c2dd1c08a48d2c9efbcea68c.jpg)

Building Intuition for Lattice-Based Signatures – Part 2: Fiat-Shamir with Aborts

IntroductionThis two-part blog series aims to build some intuition for
*2023-8-17 23:32:31
Author: [research.nccgroup.com(查看原文)](/jump-174711.htm)
阅读量:18
收藏*

---

## Introduction

This two-part blog series aims to build some intuition for the main techniques that are used to construct lattice-based signatures, focusing in particular on the techniques underlying Falcon and Dilithium, the two lattice-based signature schemes selected for standardization by the National Institute of Standards and Technology (NIST). In part 1 of this two-part blog post ([Building Intuition for Lattice-Based Signatures – Part 1: Trapdoor Signatures](https://research.nccgroup.com/2023/07/24/building-intuition-for-lattice-based-signatures-part-1-trapdoor-signatures/)), we covered how to build lattice-based trapdoor signatures based on the hardness of the Closest Vector Problem (CVP) using the hash-and-sign paradigm, which lies at the core of Falcon.

In this second part, we will describe an alternative construction of lattice-based signatures relying on the hardness of the Shortest Vector Problem (SVP) and the Fiat-Shamir paradigm, which is used as a basis for the signature scheme Dilithium. For a quick refresher on lattice theory and notation that will be used throughout this post, see the [Lattice Background](https://research.nccgroup.com/2023/07/24/building-intuition-for-lattice-based-signatures-part-1-trapdoor-signatures/#lattice-background) section in part 1 of this blog post.

### Table of Contents

1. [Introduction](https://research.nccgroup.com/2023/08/17/building-intuition-for-lattice-based-signatures-part-2-fiat-shamir-with-aborts/#introduction)
   1. [Table of Contents](https://research.nccgroup.com/2023/08/17/building-intuition-for-lattice-based-signatures-part-2-fiat-shamir-with-aborts/#table-of-contents)
2. [Constructing Signatures Using Fiat-Shamir and the SVP](https://research.nccgroup.com/2023/08/17/building-intuition-for-lattice-based-signatures-part-2-fiat-shamir-with-aborts/#constructing-signatures-using-fiat-shamir-and-the-svp)
   1. [Signature Schemes from Identification Schemes](https://research.nccgroup.com/2023/08/17/building-intuition-for-lattice-based-signatures-part-2-fiat-shamir-with-aborts/#signature-schemes-from-identification-schemes)
   2. [Lattice-Based Identification Schemes](https://research.nccgroup.com/2023/08/17/building-intuition-for-lattice-based-signatures-part-2-fiat-shamir-with-aborts/#lattice-based-identification-schemes)
   3. [Options and Optimizations](https://research.nccgroup.com/2023/08/17/building-intuition-for-lattice-based-signatures-part-2-fiat-shamir-with-aborts/#options-and-optimizations)
3. [Conclusion](https://research.nccgroup.com/2023/08/17/building-intuition-for-lattice-based-signatures-part-2-fiat-shamir-with-aborts/#conclusion)
4. [Footnotes](https://research.nccgroup.com/2023/08/17/building-intuition-for-lattice-based-signatures-part-2-fiat-shamir-with-aborts/#footnotes)
5. [References](https://research.nccgroup.com/2023/08/17/building-intuition-for-lattice-based-signatures-part-2-fiat-shamir-with-aborts/#references)

## Constructing Signatures Using Fiat-Shamir and the SVP

Recall that the SVP![_\gamma](https://s0.wp.com/latex.php?latex=_%5Cgamma&bg=ffffff&fg=000&s=0&c=20201002) problem asks to find a short lattice vector of length at most a multiplicative approximation factor ![\gamma \geq 1](https://s0.wp.com/latex.php?latex=%5Cgamma+%5Cgeq+1&bg=ffffff&fg=000&s=0&c=20201002) of the length of the shortest (non-zero) vector in the lattice. In order to construct a lattice-based signature scheme based on the SVP![_\gamma](https://s0.wp.com/latex.php?latex=_%5Cgamma&bg=ffffff&fg=000&s=0&c=20201002), we focus on a special case of the SVP![_\gamma](https://s0.wp.com/latex.php?latex=_%5Cgamma&bg=ffffff&fg=000&s=0&c=20201002) problem instantiated on ![q](https://s0.wp.com/latex.php?latex=q&bg=ffffff&fg=000&s=0&c=20201002)-ary lattices, known as the Short Integer Solution (SIS) problem. Formally, SIS![_{n,m,q,\beta}](https://s0.wp.com/latex.php?latex=_%7Bn%2Cm%2Cq%2C%5Cbeta%7D&bg=ffffff&fg=000&s=0&c=20201002) can be defined as follows. Given ![A \subseteq \mathbb{Z}_q^{m \times n}](https://s0.wp.com/latex.php?latex=A+%5Csubseteq+%5Cmathbb%7BZ%7D_q%5E%7Bm+%5Ctimes+n%7D&bg=ffffff&fg=000&s=0&c=20201002), find a short ![\vec{z} \in \mathbb{Z}^m](https://s0.wp.com/latex.php?latex=%5Cvec%7Bz%7D+%5Cin+%5Cmathbb%7BZ%7D%5Em&bg=ffffff&fg=000&s=0&c=20201002) in the ![q](https://s0.wp.com/latex.php?latex=q&bg=ffffff&fg=000&s=0&c=20201002)-ary lattice ![\Lambda^\perp(A)](https://s0.wp.com/latex.php?latex=%5CLambda%5E%5Cperp%28A%29&bg=ffffff&fg=000&s=0&c=20201002) satisfying ![A\vec{z} \equiv \vec{0} \mod q](https://s0.wp.com/latex.php?latex=A%5Cvec%7Bz%7D+%5Cequiv+%5Cvec%7B0%7D+%5Cmod+q&bg=ffffff&fg=000&s=0&c=20201002) and ![\|\vec{z}\| \leq \beta](https://s0.wp.com/latex.php?latex=%5C%7C%5Cvec%7Bz%7D%5C%7C+%5Cleq+%5Cbeta&bg=ffffff&fg=000&s=0&c=20201002). (Note that any norm can be used here. Common choices include the ![\ell_2](https://s0.wp.com/latex.php?latex=%5Cell_2&bg=ffffff&fg=000&s=0&c=20201002) and ![\ell_\infty](https://s0.wp.com/latex.php?latex=%5Cell_%5Cinfty&bg=ffffff&fg=000&s=0&c=20201002) norms.)

The SIS problem lends itself well to constructing cryptographic primitives. If we choose our domain to be a set of short vectors, then we can show the function ![\vec{x} \to A\vec{x}](https://s0.wp.com/latex.php?latex=%5Cvec%7Bx%7D+%5Cto+A%5Cvec%7Bx%7D&bg=ffffff&fg=000&s=0&c=20201002) is in fact a hash function[1](#footnotes) which is collision-resistant and one-way.

Indeed, let ![D_b^m : \{\vec{x}: \|\vec{x}\|_\infty \leq b\}](https://s0.wp.com/latex.php?latex=D_b%5Em+%3A+%5C%7B%5Cvec%7Bx%7D%3A+%5C%7C%5Cvec%7Bx%7D%5C%7C_%5Cinfty+%5Cleq+b%5C%7D&bg=ffffff&fg=000&s=0&c=20201002) and suppose we define the hash function ![f_A: D^m \to \mathbb{Z}_q](https://s0.wp.com/latex.php?latex=f_A%3A+D%5Em+%5Cto+%5Cmathbb%7BZ%7D_q&bg=ffffff&fg=000&s=0&c=20201002). If we could find a collision ![\vec{x}_1, \vec{x}_2 \in \mathbb{Z}^m](https://s0.wp.com/latex.php?latex=%5Cvec%7Bx%7D_1%2C+%5Cvec%7Bx%7D_2+%5Cin+%5Cmathbb%7BZ%7D%5Em&bg=ffffff&fg=000&s=0&c=20201002) such that ![A\vec{x}_1 \equiv A\vec{x}_2 \mod{q}](https://s0.wp.com/latex.php?latex=A%5Cvec%7Bx%7D_1+%5Cequiv+A%5Cvec%7Bx%7D_2+%5Cmod%7Bq%7D&bg=ffffff&fg=000&s=0&c=20201002), then ![\vec{x}_1  - \vec{x}_2](https://s0.wp.com/latex.php?latex=%5Cvec%7Bx%7D_1++-+%5Cvec%7Bx%7D_2&bg=ffffff&fg=000&s=0&c=20201002) is a solution to the SIS![_{n,m,q,\beta = 2b}](https://s0.wp.com/latex.php?latex=_%7Bn%2Cm%2Cq%2C%5Cbeta+%3D+2b%7D&bg=ffffff&fg=000&s=0&c=20201002) problem. Indeed, we have that ![A\vec{x}_1 - A\vec{x}_2 = A(\vec{x}_1 - \vec{x}_2) \equiv \vec{0} \mod{q}](https://s0.wp.com/latex.php?latex=A%5Cvec%7Bx%7D_1+-+A%5Cvec%7Bx%7D_2+%3D+A%28%5Cvec%7Bx%7D_1+-+%5Cvec%7Bx%7D_2%29+%5Cequiv+%5Cvec%7B0%7D+%5Cmod%7Bq%7D&bg=ffffff&fg=000&s=0&c=20201002) and, since both ![\vec{x}_1](https://s0.wp.com/latex.php?latex=%5Cvec%7Bx%7D_1&bg=ffffff&fg=000&s=0&c=20201002) and ![\vec{x}_2](https://s0.wp.com/latex.php?latex=%5Cvec%7Bx%7D_2&bg=ffffff&fg=000&s=0&c=20201002) are short, we know ![\vec{x}_1 - \vec{x}_2](https://s0.wp.com/latex.php?latex=%5Cvec%7Bx%7D_1+-+%5Cvec%7Bx%7D_2&bg=ffffff&fg=000&s=0&c=20201002) is also bounded, with ![\|\vec{x}_1 - \vec{x}_2\|_\infty \leq \|\vec{x}_1\|_\infty + \|\vec{x}_2\|_\infty  = 2b](https://s0.wp.com/latex.php?latex=%5C%7C%5Cvec%7Bx%7D_1+-+%5Cvec%7Bx%7D_2%5C%7C_%5Ci...
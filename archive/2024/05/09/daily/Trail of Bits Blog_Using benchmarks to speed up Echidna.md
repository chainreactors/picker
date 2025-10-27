---
title: Using benchmarks to speed up Echidna
url: https://blog.trailofbits.com/2024/05/08/using-benchmarks-to-speed-up-echidna/
source: Trail of Bits Blog
date: 2024-05-09
fetch_date: 2025-10-06T17:15:44.673679
---

# Using benchmarks to speed up Echidna

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# Using benchmarks to speed up Echidna

Ben Siraphob

May 08, 2024

[blockchain](/categories/blockchain/), [echidna](/categories/echidna/), [fuzzing](/categories/fuzzing/), [internship-projects](/categories/internship-projects/)

During my time as a Trail of Bits associate last summer, I worked on optimizing the performance of [Echidna](https://github.com/crytic/echidna), Trail of Bits’ open-source smart contract fuzzer, written in Haskell. Through extensive use of profilers and other tools, I was able to pinpoint and debug a massive space leak in one of Echidna’s dependencies, [hevm](https://github.com/ethereum/hevm). Now that this problem has been fixed, Echidna and hevm can both expect to use several gigabytes less memory on some test cases compared to before.

In this blog post, I’ll show how I used profiling to identify this deep performance issue in hevm and how we fixed it, improving Echidna’s performance.

## Overview of Echidna

Suppose we are keeping track of a fixed supply pool. Users can transfer tokens among themselves or burn tokens as needed. A desirable property of this pool might be that supply never grows; it only stays the same or decreases as tokens are transferred or burned. How might we go about ensuring this property holds? We can try to write up some test scenarios or try to prove it by hand… or we can fuzz the code with Echidna!

![](/img/wpdump/a45e1c42eb7e4ce16f9ec1d1412c05ae.png)

How Echidna works

Echidna takes in smart contracts and assertions about their behavior that should always be true, both written in Solidity. Then, using information extracted from the contracts themselves, such as method names and constants, Echidna starts generating random transaction sequences and replaying them over the contracts. It keeps generating longer and new sequences from old ones, such as by splitting them up at random points or changing the parameters in the method calls.

How do we know that these generations of random sequences are covering enough of the code to eventually find a bug? Echidna uses *coverage-guided fuzzing*—that is, it keeps track of how much code is actually executed from the smart contract and prioritizes sequences that reach more code in order to create new ones. Once it finds a transaction sequence that violates our desired property, Echidna then proceeds to *shrink* it to try to minimize it. Echidna then dumps all the information into a file for further inspection.

## Overview of profiling

The Glasgow Haskell Compiler (GHC) provides various tools and flags that programmers can use to understand performance at various levels of granularity. Here are two:

* **Compiling with profiling:** This modifies the compilation process to add a [profiling system](https://downloads.haskell.org/ghc/latest/docs/users_guide/profiling.html#cost-centres-and-cost-centre-stacks) that adds costs to cost centers. Costs are annotations around expressions that completely measure the computational behavior of those expressions. Usually, we are interested in top-level declarations, essentially functions and values that are exported from a module.
* **Collecting runtime statistics:** Adding `+RTS -s` to a profiled Haskell program makes it show [runtime statistics](https://downloads.haskell.org/ghc/latest/docs/users_guide/runtime_control.html?highlight=rts#rts-options-to-produce-runtime-statistics). It’s more coarse than profiling, showing only aggregate statistics about the program, such as total bytes allocated in the heap or bytes copied during garbage collection. After enabling profiling, one can also use the `-hT` option, which breaks down the heap usage by closure type.

Both of these options can produce human- and machine-readable output for further inspection. For instance, when we compile a program with profiling, we can output JSON that can be displayed in a flamegraph viewer like [speedscope](https://www.speedscope.app/). This makes it easy to browse around the data and zoom in to relevant time slices. For runtime statistics, we can use [eventlog2html](https://github.com/mpickering/eventlog2html) to visualize the heap profile.

Looking at the flamegraph below and others like it led me to conclude that at least from an initial survey, Echidna wasn’t terribly bloated in terms of its memory usage. Indeed, various changes over time have targeted performance directly. (In fact, a Trail of Bits [wintern](https://blog.trailofbits.com/2022/03/02/optimizing-a-smart-contract-fuzzer/) from 2022 found performance issues with its coverage, which were then fixed.) However, notice the large blue regions? That’s hevm, which Echidna uses to evaluate the candidate sequences. Given that Echidna spends the vast majority of its fuzzing time on this task, it makes sense that hevm would take up a lot of computational power. That’s when I turned my attention to looking into performance issues with hevm.

![](/img/wpdump/194dca81e8747815d15f1975ae1fafe5.png)

The time use of functions and call stacks in Echidna

## Profilers can sometimes be misleading

Profiling is useful, and it helped me find a bug in hevm whose fix led to improved performance in Echidna (which we get to in the next section), but you should also know that it can be misleading.

For example, while profiling hevm, I noticed something unusual. Various optics-related operators (getters and setters) were dominating CPU time and allocations. How could this be? The reason was that the `optics` library was not properly inlining some of its [operators](https://hackage.haskell.org/package/optics-core-0.4.1.1/docs/Optics-Optic.html#v:-37-). As a result, if you run [this code](https://github.com/siraben/lens-optics-profiling/blob/fb86a84f35debcd0168b3e9b22d4b66e5bb856a7/app/Main-optics.hs) with profiling enabled, you would see that the `%` operator takes up the vast majority of allocations and time instead of the `increment` function, which is actually doing the computation. This isn’t observed when running an optimized binary though, since GHC must have decided to inline the operator anyway. I wrote up [this issue](https://github.com/siraben/lens-optics-profiling) in detail and it helped the `optics` library developers close an [issue](https://github.com/well-typed/optics/issues/469) that was opened last year! This little aside made me realize that I should compile programs with and without profiling enabled going forward to ensure that profiling stays faithful to real-world usage.

## Finding my first huge memory leak in hevm

Consider the following program. It repeatedly hashes a number, starting with 0, and writes the hashes somewhere in memory (up to address `m`). It does this `n` times.

```
contract A {
  mapping (uint256 => uint256) public map;
  function myFunction(uint256 n, uint256 m) public {
    uint256 h = 0;
    for (uint i = 0; i < n; i++) {
      uint256 x = h;
      h = uint256(keccak256(abi.encode(h)));
      map[x % m] = h;
    }
  }
}
```

What should we expect the program to do as we vary the value of `n` and `m`? If we hold `m` fixed and continue increasing the value of `n`, the memory block up to `m` should be completely filled. So we should expect that no more memory would be used. This is visualized below:

![](/img/wpdump/4a5b53fd2800003c862af64a004f203d.png)

Holding m fixed and increasing n should eventually fill up m.

Surprisingly, this is not what I observed. The memory used by hevm went up linearly as a function of `n` and `m`. So, for some reason, hevm continued to allocate memory even though it should have been reusing it. In fact, this program used so much memory that it could use hundreds of gigabytes of RAM. I wrote up the issue [here](https://github.com/ethereum/hevm/issues/292).

![](/img/wpdump/1220f45025d45c96c2d2c945ef4f70a5.png)

A graph showing allocations growing rapidly

I figured that if this memory issue affect...
---
title: What would you do with that old GPU?
url: https://blog.trailofbits.com/2024/09/05/what-would-you-do-with-that-old-gpu/
source: Trail of Bits Blog
date: 2024-09-06
fetch_date: 2025-10-06T18:26:38.528101
---

# What would you do with that old GPU?

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# What would you do with that old GPU?

Artem Dinaburg, [Peter Goodman](https://x.com/peter_a_goodman)

September 05, 2024

[research-practice](/categories/research-practice/)

(Would you get up and throw it away?)
[sing to the tune of [The Beatles – With A Little Help From My Friends](https://www.youtube.com/watch?v=wMXRk0EUYAs)]

Here’s a riddle: when new GPUs are constantly being produced, product cycles are ~18-24 months long, and each cycle doubles GPU power (per [Huang’s Law](https://en.wikipedia.org/wiki/Huang%27s_law)), what happens to [10-year-old server GPUs](https://www.nvidia.com/en-gb/data-center/tesla-k80/)? We’ve asked around and no one can answer; we do know that they get kicked out of [Google Cloud](https://cloud.google.com/compute/docs/eol/k80-eol) and [Microsoft Azure](https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/migration-guides/nc-series-retirement) (but not [AWS](https://aws.amazon.com/ec2/instance-types/p2/)), and they’re useless for machine learning, with so many new and exponentially more powerful versions available.

Surely these older GPUs—which are still racked, installed, and functional, with their capital costs already paid—aren’t just going to be [thrown in the dump](https://unwire.hk/2018/07/02/sichuanminingfactory/fun-tech/)… are they?

Please don’t do that! Here at Trail of Bits, we want to use old GPUs—even those past their official end of life—to solve interesting computer security and program analysis problems. If you’re planning to dispose of a rack of old GPUs, don’t! We’d love to chat about extending the useful life of your capital investment.

### How to put old GPUs to use

Below are some of the ideas we’ve been working on and would like to pursue further.

**Fuzzing embedded platforms.** GPUs are a natural fit for the fuzzing problem, since the fuzzing is embarrassingly parallel and there are natural workarounds for divergence issues. GPU fuzzing is most effective in the embedded space, since one needs to write an emulator anyway. It makes sense, then, to write a fast emulator instead of a slow one. Our [prototype GPU fuzzer](https://www.youtube.com/watch?v=iHpi35o5wgc) shows that the concept is sound, but it has limitations that make it difficult to use for real-world fuzzing. We would like to fix this and are working on some ideas (avoiding static translation, applying performance lessons from [our fast DBT tools](https://github.com/lifting-bits/grr), etc.) to make emulator creation practical.

**Stochastic optimization.** Stochastic optimizers, like Stanford’s [STOKE](https://github.com/StanfordPL/stoke), search through a large set of potential machine instructions and look for novel, non-obvious transformations that improve program performance. A key bottleneck to this approach is search throughput, which we believe could be done much faster on GPUs.

**SMT solving.** SMT has numerous uses in optimization and security, but is resistant to parallelism at the algorithm level. Two specific instances of the SMT problem can benefit from simple and effective GPU acceleration. The first is floating point. Prior research has used [brute-force search with CPUs to solve floating-point SMT](https://www.doc.ic.ac.uk/~afd/homepages/papers/pdfs/2019/FSE.pdf) on CPUs, which we’d like to extend with GPU acceleration. Second, GPUs can brute-force-search traditional integer SMT theories that are resistant to normal algorithms. GPU-based search would occur in parallel with other approaches and be a strict improvement over the current state of the art.

**Reachability queries.** Another key primitive of program analysis is reachability queries; that is, given a (very large) program, can I reach line X from line Y, and if so, what are the path(s)? This problem typically runs in O(n3) time and is frequently a [bottleneck in real program analysis](https://www.youtube.com/watch?v=tzVJ6RD5fj4). We believe that we can use GPU computation to make even complex reachability queries more practical.

**Datalog acceleration.** Datalog has found new life as a language to enable static analysis of large programs via tools like [Souffle](https://souffle-lang.github.io/). Recent research has shown promise in [accelerating datalog operations via GPUs](https://www.usenix.org/system/files/atc23-shovon.pdf), which should allow better, more scalable static analysis tools.

**API-level translation.** This is not a use of GPUs, but is related to GPU programming: We believe that we can use MLIR and [Trail of Bits’ VAST](https://github.com/trailofbits/vast) to transparently compile code across API layers. That is, source code would stay on one API (e.g., from CUDA), but during compilation, the compiler would use MLIR dialect translations to transform the program from CUDA semantics to OpenCL semantics. We’d like to create a prototype to see if this kind of compilation is feasible.

### Help us save old GPUs!

We’ve been thinking about these problems for a while, and would like to write some practical proof-of-concept software to solve them. To do that, we are seeking research funding and access to spare GPU capacity. Importantly, we do not need access to the latest and greatest GPUs; hardware that will soon be end-of-lifed or that is no longer viable for AI/ML applications suits us just fine. If you’d like to help, [let us know](https://www.trailofbits.com/contact/)! We have a history of collaborating with universities on similar research challenges and would be eager to continue such partnerships.

#### If you enjoyed this post, share it:

[X](https://x.com/trailofbits "X")

[LinkedIn](https://linkedin.com/company/trail-of-bits "LinkedIn")

[GitHub](https://github.com/trailofbits "GitHub")

[Mastodon](https://infosec.exchange/%40trailofbits "Mastodon")

[Hacker News](https://news.ycombinator.com/from?site=trailofbits.com "Hacker News")

#### Page content

#### Recent Posts

* [Taming 2,500 compiler warnings with CodeQL, an OpenVPN2 case study](/2025/09/25/taming-2500-compiler-warnings-with-codeql-an-openvpn2-case-study/)
* [Supply chain attacks are exploiting our assumptions](/2025/09/24/supply-chain-attacks-are-exploiting-our-assumptions/)
* [Use mutation testing to find the bugs your tests don't catch](/2025/09/18/use-mutation-testing-to-find-the-bugs-your-tests-dont-catch/)
* [Fickling’s new AI/ML pickle file scanner](/2025/09/16/ficklings-new-ai/ml-pickle-file-scanner/)
* [How Sui Move rethinks flash loan security](/2025/09/10/how-sui-move-rethinks-flash-loan-security/)

© 2025 Trail of Bits.
Generated with [Hugo](https://gohugo.io/) and [Mainroad](https://github.com/Vimux/Mainroad/) theme.
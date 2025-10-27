---
title: The future of Clang-based tooling
url: https://buaq.net/go-173153.html
source: unSafe.sh - 不安全
date: 2023-07-29
fetch_date: 2025-10-04T11:51:15.433977
---

# The future of Clang-based tooling

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

![]()

The future of Clang-based tooling

By Peter GoodmanClang is a marvelous compiler; it’s a compiler’s compiler! But i
*2023-7-28 19:0:19
Author: [blog.trailofbits.com(查看原文)](/jump-173153.htm)
阅读量:24
收藏*

---

*By Peter Goodman*

Clang is a marvelous compiler; it’s a compiler’s compiler! But it isn’t a toolsmith’s compiler. As a toolsmith, my ideal compiler would be an open book, allowing me to get to everywhere from anywhere. The data on which my ideal compiler would operate (files, macros, tokens), their eventual interpretation (declarations, statements, types), and their relations (data flow, control flow) would all be connected.

On its own, Clang does not do these things. [libClang](https://clang.llvm.org/docs/Tooling.html) looks like an off-the-shelf, ready-to-use solution to your C, C++, and Objective-C parsing problems, but it’s not. In this post, I’ll investigate the factors that drive Clang’s popularity, why its tooling capabilities are surprisingly lacking despite those factors, and the new solutions that make Clang’s future bright.

## What lies behind Clang’s success?

Clang is the name of the “compiler front end” that generates an intermediate representation (IR) from your C, C++, and Objective-C source code. That generated IR is subsequently taken as input by the LLVM compiler back end, which converts the IR into machine code. Readers of this blog will know LLVM by the trail [of](https://github.com/lifting-bits/remill) [our](https://github.com/lifting-bits/anvill) [lifting](https://github.com/lifting-bits/rellic) [tools](https://github.com/lifting-bits/magnifier).

I adopted Clang as my primary compiler over a decade ago because of its actionable (and pretty!) diagnostic messages. However, Clang has only recently become one of the most popular production-quality compilers. I believe this because it has, over time, accumulated the following factors that drive compiler popularity:

1. Fast compile times: Developers don’t [want to wait](https://xkcd.com/303/) ages for their code to compile.
2. Generated machine code runs quickly: Everyone wants their code to run faster, and for some users, a small-percentage performance improvement can translate to millions of dollars in cost savings (so cloud spend can go further!).
3. End-to-end correctness: Developers need to trust that the compiler will almost always (because [bugs do happen](https://blog.regehr.org/archives/2148)) translate their source code into semantically equivalent machine code.
4. Quality of diagnostic messages: Developers want actionable messages that [point to errors](https://clang.llvm.org/diagnostics.html) in their code, and ideally recommend solutions.
5. Generates debuggable machine code: The machine code must work with yesterday’s [debugger](https://dwarfstd.org/) [formats](https://llvm.org/devmtg/2016-11/Slides/Kleckner-CodeViewInLLVM.pdf).
6. Backing and momentum: People with lots of time (those in academia) or money (those in the industry) need to push forward the compiler’s development so that it is always improving on the above metrics.

However, one important factor is missing from this list: tooling. Despite many improvements over the past few years, Clang’s tooling story still has a long way to go. The goal of this blog post is to present a reality check about the current state of Clang-based tooling, so let’s dive in!

### The Clang AST is a lie

Clang’s abstract syntax tree (AST) is the primary abstraction upon which all tooling is based. ASTs capture essential information from source code and act as scaffolding for semantic analysis (e.g., type checking) and code generation.

But what about when things aren’t in the source code? In C++, for example, one generally does not explicitly invoke class destructor methods. Instead, those methods are implicitly invoked at the end of an object’s lifetime. C++ is full of these implicit behaviors, and almost none of them are actually explicitly represented in the Clang AST. This is a big blind spot for tools operating on the Clang AST.

### The Clang CFG is a (pretty good) lie

I complained above that it was a shame that the wealth of information available to compilers is basically left on the table in favor of ad-hoc solutions. To be fair, this is simplistic; Clang is not ideally engineered for interactivity within an IDE, for example. But also, there are some really fantastic Clang-based tools out there that are actively used and developed, such as the [Clang Static Analyzer](https://clang-analyzer.llvm.org/).

Because the Clang Static Analyzer is “built on Clang,” one might assume that its analyses are performed on a representation that is faithful to both the Clang AST and the generated LLVM IR. Yet just above, I revealed to you that the Clang AST is a lie—it’s missing quite a bit, such as implicit C++ destructor calls. The Clang Static Analyzer apparently side-steps this issue by operating on a data structure called the CFG.

The Clang CFG, short for control-flow graph, represents how a theoretical computer would execute the statements encoded in the AST. The accuracy of analysis results hinges on the accuracy of the CFG. Yet the CFG isn’t actually used during Clang’s codegen process, which produces LLVM IR containing—you guessed it—control-flow information. The Clang CFG is actually just a very good approximation of the implementation that actually matters. As a toolsmith, I care about accuracy; I don’t want to have to guess about where the abstraction leaks.

### LLVM IR as the one true IR is a lie

Clang’s intermediate representation, LLVM IR, is produced directly from the Clang AST. LLVM IR is superficially machine code independent. The closer you look, the easier it is to spot the machine-dependent parts, such as intrinsics, target triples, and data layouts. However, these parts are not expected to be retargetable because they are explicitly specific to the target architecture.

What makes LLVM IR fall short of being a practically retargetable IR actually has very little to do with LLVM IR itself, and more to do with how it is produced by Clang. Clang doesn’t produce identical-looking LLVM IR when compiling the same code for different architectures. Trivial examples of this are that LLVM IR contains constant values where the source code contained expressions like `sizeof(void *)`. But those are the known knowns; the things that developers can reasonably predict will differ. The unreasonable differences happen when Clang over-eagerly chooses type, function parameter, and function return value representations that will “fit” well with the target application binary interface (ABI). In practice, this means that your `std::pair<int, int>` function parameter might be represented as [a single i64](https://godbolt.org/z/W83TvYov5), [two i32s](https://godbolt.org/z/EnnGYvo5z), [an array of two i32s](https://godbolt.org/z/YEe1h4Gxj), or even as [a pointer to a structure](https://godbolt.org/z/83h8aTdf8)… but never a structure. Hilariously, LLVM’s back end handles structure-typed parameters just fine and correctly performs target-specific ABI lowering. I bet there are bugs lurking between these two completely different systems for ABI lowering. Reminds you of the CFG situation a bit, right?

The takeaway here is that the Clang AST is missing information that is invented by the LLVM IR code generator, but LLVM IR is also missing information that is destroyed by said code generator. And if you want to bridge that gap, you need to rely on an approximation: the Clang CFG.

### Encore: the lib in libClang is a lie

Libraries are meant to be embedded into larger programs; there...
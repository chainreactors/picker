---
title: Finding 10x+ Performance Improvements in C++ with CodeQL – Part 2/2 on Combining Dynamic and Static Analysis for Performance Optimisation
url: https://sean.heelan.io/2023/03/01/finding-10x-performance-improvements-in-c-with-codeql-part-2-2-on-combining-dynamic-and-static-analysis-for-performance-optimisation/
source: Sean Heelan's Blog
date: 2023-03-02
fetch_date: 2025-10-04T08:26:46.990676
---

# Finding 10x+ Performance Improvements in C++ with CodeQL – Part 2/2 on Combining Dynamic and Static Analysis for Performance Optimisation

[Skip to content](#content)

Open Menu

* [Home](https://sean.heelan.io/)
* [All Posts](https://sean.heelan.io/posts/)
* [Research & Publications](https://sean.heelan.io/research/)
* [About Me](https://sean.heelan.io/about-me/)

*Search*

Search for:

 Close

[![](https://sean.heelan.io/wp-content/uploads/2023/02/logo_ireland-1.jpg)](https://sean.heelan.io/)

# [Sean Heelan's Blog](https://sean.heelan.io/)

## Software Exploitation and Optimisation

[Performance Optimisation](https://sean.heelan.io/category/performance-optimisation/) / [Static analysis](https://sean.heelan.io/category/static-analysis/)

# Finding 10x+ Performance Improvements in C++ with CodeQL – Part 2/2 on Combining Dynamic and Static Analysis for Performance Optimisation

[March 1, 2023](https://sean.heelan.io/2023/03/01/finding-10x-performance-improvements-in-c-with-codeql-part-2-2-on-combining-dynamic-and-static-analysis-for-performance-optimisation/) [seanhn](https://sean.heelan.io/author/seanhn/)

In the [previous post](https://sean.heelan.io/2023/02/14/combining-static-and-dynamic-analysis-in-performance-optimisation-part-1-60-improvements-with-continuous-profiling-and-library-matching/) I advocated for building systems that combine static and dynamic analysis for performance optimisation. By doing so, we can build tools that are much more useful than those focused on either analysis approach alone. In fact, for many static analyses it’s likely that the difference between being *useful at all* and not so, is whether or not it’s combined with a profiler. As an example, continuous profiling can gather information on the hottest code paths in production environments, and this can be used to rank the output of the static analysis. A developer can then focus their efforts on the most important findings. This minimises the time wasted due to false positives, or unimportant true positives, from the static analysis. Conversely, static analysis can be used to provide further context on the output of continuous profiling and make its results more actionable, such as suggesting *why* a particular function may be hot, or suggesting potential optimisations.

In the previous post also I outlined a trivial-but-very-effective combination of analyses, in which the Top N most expensive functions identified by continuous profiling are piped into a service that checks library and function names against a list of known faster replacements, allowing a developer to optimize their application with zero code changes. e.g. swapping jemalloc for libc malloc, zlib-ng for zlib, orjson for Python’s stdlib JSON etc.

In this post we’re going to go deeper, with a static analysis that actually looks at the application’s code. When I started thinking about combinations of analyses for performance optimisation, I didn’t find much in the way of off-the-shelf static analyses that I could just use. So, I decided to build my own. We’re going to try and answer the question: can we use static analysis to find C/C++ code patterns that lead to sub-optimal machine code being emitted by the compiler?

I’ll first describe a particular code pattern that can lead to the compiler emitting unnecessary memory reads, and failing to auto-vectorise loops. When these patterns exist they can lead to functions being 10-20x or more slower than they otherwise could be. I’ll show how we can build CodeQL queries to find the patterns, and how we can modify the code to allow the compiler to auto-vectorise. I’ll then discuss results of applying the queries to a few code bases, lay out some issues that arise, and detail some potential future work and open questions.

## CodeQL

CodeQL allows you to write queries in a declarative object-oriented language, and apply those queries to a codebase that has been converted into a relational representation in a database. In other words, it provides a relatively easy-to-work-with query language for finding interesting patterns in code. Typically it is used in the security space for bug hunting. From a vulnerability hunter’s point of view CodeQL provides a relatively unique and powerful capability for a static analysis tool. Existing static analysis tools (Coverity, the clang static analyser etc.) encode checks for common vulnerability patterns, but by virtue of the fact that these very tools are part of the toolbox of many software developers, and the fact that trivial overflow patterns are less and less likely to make it through modern QA, such analysers aren’t particularly helpful for a vulnerability hunter. For this reason, and others, static analysis by and large does not have a great reputation amongst people interested in finding exploitable software flaws. By allowing one to conveniently encode arbitrary patterns and search for them in a database, CodeQL enables “variant analysis”, i.e. searching for variations of a given bug in the same codebase, or a new codebase. This turns out to be a fruitful way of finding security vulnerabilities. As of yet CodeQL hasn’t seen any use that I’m aware of in the realm of detecting performance issues, but its flexibility makes it an excellent candidate technology for any property that can be encoded as predicates over an abstract syntax tree.

## The Inconveniences of Type Aliasing in C/C++

In [Optimising an eBPF Optimiser with eBPF](https://sean.heelan.io/2023/02/10/optimising-an-ebpf-optimiser-with-prodfiler-repost/) I discussed searching for performance improvements in a program synthesis engine. One of the optimisations I made was to modify the code to allow the compiler to auto-vectorise a series of very hot loops which looked as follows:

[![](https://sean.heelan.io/wp-content/uploads/2023/02/codeex.png?w=974)](https://sean.heelan.io/wp-content/uploads/2023/02/codeex.png)

Under the hood, a `std::vector<bool>` has some properties that mean the loops cannot be auto-vectorised. See the [post](https://sean.heelan.io/2023/02/10/optimising-an-ebpf-optimiser-with-prodfiler-repost/) I just mentioned for details, but in short: we needed to replace `std::vector<bool>` with a vector of *something* other than a bool. The original *something* that I chose was a `uint8_t` but, to my surprise, instead of getting out a nicely unrolled and vectorised loop, what I got was this:

[![](https://sean.heelan.io/wp-content/uploads/2023/02/boolasm.png?w=527)](https://sean.heelan.io/wp-content/uploads/2023/02/boolasm.png)

The compiler has generated code that on each iteration of the loop loads the source and destination pointers from `[r12]` and `[rbx+0xa8]`, and thus it cannot auto-vectorise. I eventually tracked down the issue with the help of this [post](https://travisdowns.github.io/blog/2019/08/26/vector-inc.html) by Travis Downs. The problem is type aliasing. In C/C++, the `char` type (and its kin, such as `uint8_t`) can alias every other type. On a write to memory through such a type the compiler has to assume that it may have modified any other heap-based memory location, even if that location has an entirely different type (such as the data pointers contained in the source and destination vectors in the above example). Because of this, in the above example, the compiler must assume `[r12]` and `[rbx+0xa8]` could have been modified by the write to `[rdx+rax]` and therefore cannot safely auto-vectorise the loop as it needs to reload these values after each write.

In many situations, having to reload a value from memory is not the end of the world, but in the context of loops in particular the issue can lead to drastically worse code being generated by the compiler than would otherwise be possible. In Travis’ blog post he shows a particularly pathological example where the issue leads to code that is 20x slower than it could be.

There are a variety of ways to fix this ‘problem’. Where possible, replacing the `uint8_t/char` type with a `char8_t` will solve it. The `char8_t` type, introduced in C++20, does not have the aliasing issue that `char` does. If C++20 canno...
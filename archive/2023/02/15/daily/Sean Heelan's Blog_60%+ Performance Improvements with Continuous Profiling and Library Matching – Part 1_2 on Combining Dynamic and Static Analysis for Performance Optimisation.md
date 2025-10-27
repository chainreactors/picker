---
title: 60%+ Performance Improvements with Continuous Profiling and Library Matching – Part 1/2 on Combining Dynamic and Static Analysis for Performance Optimisation
url: https://sean.heelan.io/2023/02/14/combining-static-and-dynamic-analysis-in-performance-optimisation-part-1-60-improvements-with-continuous-profiling-and-library-matching/
source: Sean Heelan's Blog
date: 2023-02-15
fetch_date: 2025-10-04T06:37:23.549316
---

# 60%+ Performance Improvements with Continuous Profiling and Library Matching – Part 1/2 on Combining Dynamic and Static Analysis for Performance Optimisation

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

[Performance Optimisation](https://sean.heelan.io/category/performance-optimisation/)

# 60%+ Performance Improvements with Continuous Profiling and Library Matching – Part 1/2 on Combining Dynamic and Static Analysis for Performance Optimisation

[February 14, 2023](https://sean.heelan.io/2023/02/14/combining-static-and-dynamic-analysis-in-performance-optimisation-part-1-60-improvements-with-continuous-profiling-and-library-matching/) [seanhn](https://sean.heelan.io/author/seanhn/)

This is the first post in a two part series on combining static and dynamic analyses for performance optimisation. I’ve split them up as otherwise it’ll be horrifically long, and the second post will be online later this week. This post lays out some high level context, discusses why we should combine analyses, and has a loose framework for thinking about analysis combination. I’ll then explain a straightforward combination of continuous profiling with pattern matching on library names and versions which has led to 60%+ performance gains per service in real customer infrastructure.

In the follow-up post, I’ll discuss experimental work I did last year on using CodeQL to search for performance optimisation opportunities in C/C++ codebases. CodeQL is typically used to find security vulnerabilities, but I’ll show how it can also be used to find C++ code patterns that may lead to the compiler producing machine code that is 10x, or more, slower than it could be. Primarily, these patterns relate to code constructs that prevent the compiler from auto-vectorising loops and where, with some minor type changes or reordering of statements, we can achieve significant performance improvements.

## Why Combine Static and Dynamic Analyses?

A few years ago I co-founded [optimyze.cloud](https://prodfiler.com/about/), and we built [Prodfiler](https://prodfiler.com/) (now the [Elastic Universal Profiler](https://www.elastic.co/observability/universal-profiling)) – a fleet-wide, continuous, whole-system profiler. That is, a profiler that is sufficiently efficient that it can be always on, everywhere, profiling the entire system on every machine in your fleet. Enabling Prodfiler/EUP gives insight into exactly which lines of code are costing you CPU resources across your entire fleet, regardless of whether it is in userland, the kernel, native code, or some higher level runtime runtime. That’s fantastic, but, when presented with the top 10, or 100, most expensive functions in your fleet, the question arises: is it “fine” that these functions are that expensive, or not? And if not, why are they so expensive and what can be done to remedy matters?

If you’re lucky, the expensive functions are in code that you wrote and understand, and the answers to these questions may be easily arrived at. If you’re unlucky, it’s in some third party library you’re unfamiliar with, written in a language you don’t know, and on top of a runtime you’ve never heard of. A common question from our users is whether, instead of just a list of expensive functions, we could also suggest root causes or, even better, fixes. It is from here we come to the need for some sort of complementary analysis that can “reason” about *why* a particular chunk of code may be expensive, and if possible suggest a way to make it less so.

A lesson I’ve taken from building bug finding and exploit generation tools is that the sweet spot for tooling usually brings together:

1. Large scale, *fast*, dynamic analysis, involving the execution of software/system and observing what it does under a large and diverse set of inputs.
2. Automated static analysis, that may augment, or be augmented by the dynamic analysis.
3. A well designed UI/UX that enables exploratory workflows even in the presence of large amounts of data. The UI should bring together all available context, while supporting filtering, slicing and searching, with little to no perceptible lag.

With Prodfiler we have 1 and 3, but 2 is relatively unexplored in the performance world, and certainly in the context of combining it with continuous profiling.

My belief is that, just like security, the sweet spot for performance analysis is in the intersection of points 1-3, with dynamic and static analysis being mutually beneficial, and an intuitive and performant UI being game changing. In this post I am going to focus exclusively on the static analysis part of the equation. If you’d like to learn more about how to build a high performance continuous profiling engine then we have an initial [blog post](https://www.elastic.co/blog/universal-profiling-frame-pointers-symbols-ebpf) on this topic over on the Elastic blog, and will have more in the future.

## Modes of Combining Dynamic and Static Analysis

In general, in program analysis R&D, there are no hard and fast rules on what does and does not work well, and it’s an area where’s there’s plenty of ongoing work in both academia and industry. It’s also not the case that one might stick to combining one static analysis with one dynamic analysis. You may even decide to skip one form of analysis entirely, and chain a bunch of exclusively dynamic analyses, or vice versa. As an example, for the purposes of bug finding, an over-approximate but fast abstract interpretation based analysis could be applied to every function in the code base to find potential bugs. The potentially buggy functions could then be passed to a symbolic execution engine to validate the bugs in the intraprocedural context. Finally, a fuzzer could be used to try and find paths to those buggy functions which exercise the conditions required to trigger the bug. For a concrete example, check out Sys, which combines static analysis and symbolic execution to leverage the strengths of each to find bugs in web browsers [[code](https://github.com/PLSysSec/sys)] [[paper & talk](https://www.usenix.org/conference/usenixsecurity20/presentation/brown)].

When it comes to performance optimisation and analysis, there are three modes of operation that I can think of where multiple analyses may be mutually beneficial:

1. **Context-for-ranking** in which a dynamic analysis provides a ground truth on the most expensive parts of the system, ideally when it is executing in production on real workloads. This context can then be used to rank the results of a static analysis. Ranking is important for two reasons. First, developers have finite time. An approximate analysis with false positives will require a developer to validate each result. If we want a developer to actually use the tool then we need some way to ensure that their efforts are applied to the most impactful findings before they run out of time or energy. Second, whether a finding from a static analysis tool intended to find performance issues is even valid or not may hinge on whether the code in question is on a hot path. The results of the static analysis are essentially incomplete unless combined with the context indicating what code is hot on production workloads. An example of context-for-ranking might be continuous CPU profiling in production being used to rank the output of an analysis which lists the loops in a program that the compiler failed to auto-vectorise. If a loop is unvectorised in a function that only executes once on startup then it probably doesn’t matter, but continuous profiling gives you a way to filter out this sort of noise and focus on the loops that are significant.
2. **Ranking-for-analysis** in which a lightweight dynamic analysis provides information on t...
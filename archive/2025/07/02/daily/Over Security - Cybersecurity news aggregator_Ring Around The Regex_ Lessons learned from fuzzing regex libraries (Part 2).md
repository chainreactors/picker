---
title: Ring Around The Regex: Lessons learned from fuzzing regex libraries (Part 2)
url: https://secret.club/2024/08/23/ring-around-the-regex-2.html
source: Over Security - Cybersecurity news aggregator
date: 2025-07-02
fetch_date: 2025-10-06T23:56:23.390076
---

# Ring Around The Regex: Lessons learned from fuzzing regex libraries (Part 2)

[SECRET CLUB](/) [HOME](/) [ABOUT](/about)

# Ring Around The Regex: Lessons learned from fuzzing regex libraries (Part 2)

![main authors image](/assets/author_img/addison.jpg)  [addison](/author/addison)

 Aug 23, 2024

---

I’m a little late (one whole month passed in a blink of an eye!). Let’s catch up.

We briefly explored this idea that fuzzing has some limitations, looking specifically at problems associated with harnessing and input mutation. Sometimes, we can do everything right and yet the fuzzer still struggles to find bugs. Regex engines fall into this camp quite strongly; let’s figure out why by looking at PCRE2.

# [Target 2: PCRE2](#target-2-pcre2)

PCRE2 is (likely!) the world’s most used regex library. It started as PCRE back in 1998, eventually upgrading to PCRE2 in 2014 due to major API changes. I highly recommend reading [Joe Brockmeier’s article on the library and the primary developer, Philip Hazel](https://lwn.net/Articles/978463/) – the library, and its author, have quite an incredible history.

A few months ago, now a few years after [my exploration of rust-regex](https://github.com/rust-lang/regex/security/advisories/GHSA-m5pq-gvj9-9vr8), I stumbled across a bug in PCRE2 during a research project. The bug suggested the presence of latent bugs in the [just-in-time compiled component](https://github.com/zherczeg/sljit) of PCRE2. At CISPA, we are encouraged to investigate such tangents and, being the fuzzing-oriented person I am, I started deep diving the fuzzers in PCRE2.

## [OSS-Fuzz, or: Learned Helplessness](#oss-fuzz-or-learned-helplessness)

There is a standing fear that if a project is in OSS-Fuzz, there is no point in fuzzing it. This is especially the case for PCRE2: [it’s been in OSS-Fuzz since the very beginning](https://github.com/google/oss-fuzz/pull/24)! PCRE2 has likely been fuzzed for *multiple centuries of CPU time* at this point.

And yet, [there are fuzzing-discoverable bugs in OSS-Fuzz projects](https://blog.isosceles.com/the-webp-0day/). How could we miss them?

### [fuzz-introspector](#fuzz-introspector)

Trying to understand this very problem, [OpenSSF](https://openssf.org/), led by David Korczynski, developed Fuzz Introspector in 2021. This tool inspects fuzzer performance over time by tracking various metrics and is most notably deployed on OSS-Fuzz.

[With this tool, we can inspect how well (or, more frequently, how poorly) various harnesses are performing in OSS-Fuzz](https://introspector.oss-fuzz.com/projects-overview).

We can see that a majority of targets get very low coverage. This flies in the face of the assumption one might make regarding how well fuzzed targets in OSS-Fuzz are, and [is a problem that Google spends a lot of money trying to solve](https://bughunters.google.com/about/rules/open-source/5097259337383936/oss-fuzz-reward-program-rules). Yet [PCRE2 has historically reached high code coverage](https://storage.googleapis.com/oss-fuzz-introspector/pcre2/inspector-report/20231001/fuzz_report.html), so what went wrong here?

One of the limitations of Fuzz Introspector is that it can only determine if something is *uncovered* if it can find the function within the binary. In the case of PCRE2, [the JIT compiler was never actually included in the fuzz testing](https://github.com/PCRE2Project/pcre2/pull/317#issuecomment-1804274817). As a result, [once enabled](https://github.com/google/oss-fuzz/pull/11195), the [true coverage of the source code was shown to be far lower](https://introspector.oss-fuzz.com/project-profile?project=pcre2):

![a chart displaying the percent of covered lines over time, with a sudden drop from approximately 95% to just above 80% on February 21st](/assets/pcre2-coverage.png)

So, even for programs with high code coverage, you cannot merely take it at face value that the code is well-covered. Similarly, [coverage is not indicative of bug discovery](https://dl.acm.org/doi/pdf/10.1145/3510003.3510230), so we cannot take the coverage itself at face value.

## [You’re JIT-ing me](#youre-jit-ing-me)

To improve the OSS-Fuzz harness, I submitted changes that enabled fuzzing of the JIT compiler in tandem with the normal executor. We do this because fuzzing the JIT compiler alone is insufficient.

Consider the mechanism by which code coverage is measured. In libFuzzer, this works via [the SanitizerCoverage pass](https://clang.llvm.org/docs/SanitizerCoverage.html), which adds callbacks at code points which will track the traversal of certain edges. For the coverage to be tracked, the code must exist at compile-time.

In the presence of a JIT compiler, the code which is executed is not guaranteed to be produced at compile-time.

When a JIT compiler is used, some code is generated at runtime. This can lead to curious problems where we cover the JIT compilation code, but not the compiled code itself. For example: consider a regex like `a|(0)` (“match the literal `a` OR [capture](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Capturing_group) a literal `0`”). The JIT compiler *emits* capturing code, but if we only execute this regex on the input `a`, we will *never actually run* the emitted code, meaning we will never execute the code performing the capture. In effect, the code coverage for the JIT compiler represents a *superset* of the coverage of the regex which is executed.

To get around this, when fuzzing regexes which are JIT’d, we must also execute each regex without JIT to get a sense of what code regions are actually used during execution, lest we overestimate what we’ve actually tested and not just generated. But even this can be misleading, because the JIT implementation does not necessarily strongly relate to the implementation of the “classic” implementation. There are likely specific optimisations in each which will need to be tested, and there are no guarantees that a corresponding code region exists in the coverage-measured code for a code region emitted by JIT. As such, this is an inescapable limitation.

### [But Addison, you can measure the code coverage in QEMU or something!](#but-addison-you-can-measure-the-code-coverage-in-qemu-or-something)

You do not want to do this. The JIT’d region will change every time you execute the program, and it effectively turns each tested regex into its own little program that must be covered. More importantly, it will not be trivial to distinguish whether two regexes are meaningfully different. Without serious investment into mapping which JIT regions are produced and affected by which JIT compiler regions, this would only lead to an explosion of inputs considered “interesting” without real progress.

TL;DR: don’t use emulated code coverage with JIT compilers.

## [Regex is more than just a parser](#regex-is-more-than-just-a-parser)

Fuzzers were originally crafted targeting parsing programs, like [image parsers](https://lcamtuf.blogspot.com/2014/11/pulling-jpegs-out-of-thin-air.html). These programs are generally simple; when you’re parsing an image, there’s only so many ways in which a given parsing region can be reached. Similarly, there’s only so much state which affects how the corresponding region of input is parsed by that code.

Regex engines first parse the pattern, then execute the (very limited) program represented by that pattern. When you explore the coverage of a parser, you typically explore most of the behaviours of the parser (with [notable exceptions](https://blog.isosceles.com/the-webp-0day/)). When you explore the coverage of a regex engine, you explore very little of its behaviours because of the huge amount of impact that what has previously been processed by the pattern affects what *will* be parsed by the pattern yet. This is especially true for PCRE2, which [supports referencing previously-captured data](https://github.com/PCRE2Project/pcre2/issues/334) and [context-specific control of execution behaviour](https://www.pcre.org/current/doc/html/pcre2syntax.htm...
---
title: Ring Around The Regex: Lessons learned from fuzzing regex libraries (Part 1)
url: https://secret.club/2024/06/30/ring-around-the-regex-1.html
source: Over Security - Cybersecurity news aggregator
date: 2025-07-02
fetch_date: 2025-10-06T23:56:22.291333
---

# Ring Around The Regex: Lessons learned from fuzzing regex libraries (Part 1)

[SECRET CLUB](/) [HOME](/) [ABOUT](/about)

# Ring Around The Regex: Lessons learned from fuzzing regex libraries (Part 1)

![main authors image](/assets/author_img/addison.jpg)  [addison](/author/addison)

 Jun 30, 2024

---

Okay, if you’re reading this, you probably know what fuzzing is. As an incredibly reductive summary: fuzzing is an automated, random testing process which tries to explore the state space (e.g., different interpretations of the input or behaviour) of a program under test (PUT; sometimes also SUT, DUT, etc.). Fuzzing is often celebrated as one of the most effective ways to find bugs in programs due to its inherently random nature, which defies human expectation or bias[1](#fn:1). The strategy has found countless security-critical bugs (think tens or hundreds of thousands) over its 30-odd-years of existence, and yet faces regular suspicion from industry and academia alike.

The bugs I’m going to talk about in this post are not security critical. The targets and bugs described below are instead offered as a study for fuzzing design decisions and understanding where fuzzing fails. I think this might be useful for people considering fuzz testing in both security and non-security contexts. If anything is poorly explained or incorrect, please [reach out](https://nothing-ever.works/%40addison) and I will happily make corrections, links, or add explanations as necessary.

In this blog post, I’m going to talk about the fuzzing of two very different regular expression libraries. For each, I’ll detail how I went about designing fuzzers for these targets, the usage of the fuzzers against these targets, the analysis and reporting of the bugs, and the maintainence of the fuzzers as automated regression testing tools.

# [Targets](#targets)

Okay, our PUTs for today are:

* [rust-lang/regex](https://github.com/rust-lang/regex)
* [PCRE2](https://github.com/PCRE2Project/pcre2)

We develop separate [differential fuzzing](https://secret.club/2022/05/11/fuzzing-solana.html#the-target-and-figuring-out-how-to-test-it) harnesses for each that are dependent on the specific guarantees of each program.

## [Sidebar: What is regex?](#sidebar-what-is-regex)

If you have programmed anything dealing with string manipulation, you’ve almost certainly encountered **reg**ular **ex**pression (RegEx, or just regex) libraries. There are many forms of regular expressions, from the [formal definitions](https://en.wikipedia.org/wiki/Regular_expression#Formal_language_theory) to the [many modern implementations](https://en.wikipedia.org/wiki/Comparison_of_regular_expression_engines), like the two discussed here. Modern “flavours” of regex often include quality-of-life features or extended capabilities not described in the original formal definitions, and as such actually represent greater formal constructs (e.g., I’m fairly confident that PCRE2 is capable of encoding something higher than a context-free grammar).

The purpose of these libraries is definitionally straightforward: to provide a language that can define patterns to search through text. Their implementation is rarely so straightforward, for two primary reasons:

1. Users demand expressive patterns by which to search text. Many different strategies must be made available by these libraries so that users may search and extract details from text effectively.
2. Text searching is often a hot path in text processing programs. Any implementation of regex must be implemented to process text extremely efficiently for any reasonable pattern.

I won’t give an overview of the writing and usage of regex here, as it’s mostly irrelevant for the rest of this. For those interested, [you can find an overview of common features here](https://www.regular-expressions.info/refflavors.html).

## [Target 1: rust-lang/regex](#target-1-rust-langregex)

The [regex crate](https://github.com/rust-lang/regex) (hereon, rust-regex) is one of the most widely used crates in the entire Rust ecosystem. Its syntax is potentially more complex than some other engines due to its extended support of Unicode, but notably restricts itself to [regular languages](https://en.wikipedia.org/wiki/Regular_language). rust-regex, unlike most other regex libraries, offers [moderate complexity guarantees](https://docs.rs/regex/latest/regex/#iterating-over-matches) and is thus resistant (to a degree!) to certain malicious inputs.

I fuzzed rust-regex some time ago now (>2 years), but below is a brief summary of how I approached the software.

### [Analysis of the existing harness](#analysis-of-the-existing-harness)

A fuzzing harness (in most cases) is simply a function which accepts an input and runs it in the target. Ultimately, from the perspective of the user, the fuzzing process can be thought of as so:

1. the fuzzer runtime starts
2. the runtime produces some input
3. the harness is run with the new input; if an input causes a crash, stop
4. the runtime learns something about your program to make better inputs with
5. go to step 2

So, to be super explicit, we describe the *fuzzer* as the whole program which performs the fuzz testing, the *fuzzer runtime* as the code (typically not implemented by the user) which generates inputs and analyzes program behaviour, and the *harness* as the user code which actually manifests the test by calling the PUT. Having a poor fuzzer runtime means your program won’t be tested well. Having a poor harness means that the inputs produced by the runtime might not actually test much of the program, or may not test it very effectively.

Since we don’t want to make a custom fuzzer runtime and just want to test the program, let’s focus on improving the harness.

When I started looking into rust-regex, it was already in [OSS-Fuzz](https://github.com/google/oss-fuzz/). This means potentially thousands of [CPU-years](https://www.gridrepublic.org/joomla/components/com_mambowiki/index.php/GFlops%2C_G-hours%2C_and_CPU_hours) of fuzzing has already been performed on the target. Here, we’ll talk about two ways to find new bugs: better inputs and more ways to detect bugs. Both of these are directly affected by how one harnesses the PUT.

[Here is the rust-regex harness as I originally saw it.](https://github.com/rust-lang/regex/blob/2f9103e6bf940894b366cf4ead61237b1382bacf/fuzz/fuzz_targets/fuzz_regex_match.rs) This harness works by interpreting the first byte as a length field, then using that to determine where to split the remainder of the input as the search pattern and the “haystack” (text to be searched).

```
index                                      | meaning
------------------------------------------------------------
0                                          | length field
------------------------------------------------------------
[1, 1 + data[0] % (len(data) - 1))         | search pattern
------------------------------------------------------------
[1 + data[0] % (len(data) - 1), len(data)) | haystack
```

And, this works; for several years, this fuzzer was used in practice and found [several bugs](https://bugs.chromium.org/p/oss-fuzz/issues/list?sort=reported&q=label%3AProj-rust-regex%20opened%3C2023-01-01&can=1). But this harness has some problems, the biggest of which being: data reinterpretation over mutation.

#### [Looking under the hood](#looking-under-the-hood)

Fuzzers, sadly, are not magic bug printers. The fuzzer runtime used here is [libFuzzer](https://llvm.org/docs/LibFuzzer.html), which performs random byte mutations and has no fundamental understanding of the program under test. In fact, the only thing the fuzzer really considers to distinguish the effects of different inputs is the coverage of the program[2](#fn:2). When an input is generated, it is only considered interesting (and therefore retained) if the program exhibits new coverage.

Moreover, inputs are not simply generated by libFuzzer. They are rather the result of *mutation* – the process of modifying an existing input to get a new input. Let’s...
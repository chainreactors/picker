---
title: Fuzzers vs. AI: Comparing Fuzzilli and BigSleep on JavaScript Engines
url: https://projectzero.google/2026/10/fuzzing-v-AI.html
source: Project Zero
date: 2026-10-27
fetch_date: 2026-10-28T07:50:18.697447
---

# Fuzzers vs. AI: Comparing Fuzzilli and BigSleep on JavaScript Engines

[Project Zero](/)

---

[ ]

* [blog archive](/archive.html)
* [bug reports](https://project-zero.issues.chromium.org/savedsearches/7162405)
* [about](/about-pz.html)
* [Working at PZ](/working-at-project-zero.html)
* [0day: spreadsheet](/0day.html)
* [0day: Root Cause Analyses](https://googleprojectzero.github.io/0days-in-the-wild/rca.html)
* [vulnerability disclosure policy](/vulnerability-disclosure-policy.html)
* [reporting transparency](/reporting-transparency.html)
* search

# Fuzzers vs. AI: Comparing Fuzzilli and BigSleep on JavaScript Engines

[2026-Oct-27](/2026/10/fuzzing-v-AI.html "Permalink to this post")
Samuel GroÃ

## Summary

Project Zero compared two automated tools used by Google to find vulnerabilities in Chromeâs JavaScript engine, V8, on a regular basis. [Fuzzilli](https://github.com/googleprojectzero/fuzzilli) is a generative JavaScript engine fuzzer and [BigSleep](https://projectzero.google/2024/10/from-naptime-to-big-sleep.html) is an LLM-based bug finding system. In the past six months, BigSleep found more vulnerabilities than Fuzzilli (45 versus 37) with a 25% overlap in the specific bugs reported. Since this comparison methodology has a tendency to underestimate overlap, we also performed dedicated experiments to test theoretical overlap in vulnerabilities reported since 2023. These experiments estimated overlap at roughly 60%. Regardless of which value is accurate, a substantial portion of vulnerabilities were discoverable by only LLMs or only fuzzing. While it is extremely promising that LLMs have become able to find so many vulnerabilities so quickly, fuzzing and LLMs are still complementary approaches. We recommend vendors perform both fuzzing and agentic analysis of their code to maximize the number of vulnerabilities that get reported before they impact users.

## Introduction

Fuzzing has long been successfully applied to software projects such as Chrome or V8 (Chromeâs JavaScript engine) to detect bugs. Recently, the arrival of powerful LLMs able to read, reason about, and write code is causing a transformative change to software development and software security. With [hundreds, sometimes thousands of new bugs and vulnerabilities](https://blog.google/security/chrome-stronger-with-every-update/) having been discovered in well-fuzzed targets, a natural question arises: how do new LLMs compare to âtraditionalâ fuzzers? Are they starting to replace them or do the two approaches complement each other? To help answer this, we look at three key questions:

1. How many bugs does each approach find in the real world?
2. What is the overlap between the two approaches?
3. What is the âshapeâ of bugs discovered by one system but not the other?

For this blog post, we will limit ourselves to two concrete systems: [Fuzzilli](https://github.com/googleprojectzero/fuzzilli), a JavaScript engine fuzzer, and [BigSleep](https://projectzero.google/2024/10/from-naptime-to-big-sleep.html), an agentic bug finding system. Both of these systems run in production and automatically look for bugs in newly added code, which makes them fairly directly comparable. Specifically, Fuzzilli runs continuously across many instances, with the first ones usually picking up new changes within a few hours, while BigSleep currently runs once per day and is prompted to review new commits and write proof-of-concept testcases for any bugs it discovers. Both systems report bugs through [Clusterfuzz](https://github.com/google/clusterfuzz), which will do basic crash triaging, then file bug reports in [Chromeâs issue tracker.](https://issues.chromium.org/home)

We also limit ourselves to V8 as a target, a high-performance JavaScript and WebAssembly engine with a sophisticated and mature testing and fuzzing setup. In particular, Fuzzilli is a special-purpose fuzzing tool designed to find bugs in these engines. The usually complicated nature of these bugs makes for an interesting âplaygroundâ to compare the two approachesâ ability to find deep and complex bugs in well-tested software. We leave it to future work to perform similar analysis on a broader set of targets, fuzzers, and agentic bug finding systems.

We will now look into each of the three main questions in a dedicated section. Each section will first summarize the general approach, then describe the methodology in detail (often as bullet points, so you can skip those blocks if you donât care too much about the details) before exploring the results. We conclude with an attempt at interpreting the results to get a picture of the current state of fuzzing vs. AI.

# Part 1: Production Statistics

This is the simplest part to analyze, although with some caveats weâll see in a bit. The basic idea is to query issues from [Chromiumâs bugtracker](http://issues.chromium.org/) (where V8 bugs are tracked) and extract various statistics from there. This is especially easy since thereâs a dedicated hotlist for each of the two systems. We limit our analysis to the six months from April to September 2026 as the automatic BigSleep pipeline only became active in April this year. As such, our raw data comes from the following two bug tracker queries:

* Fuzzilli: [hotlistid:5433121 created:2026-04-01..2026-09-30](https://issues.chromium.org/issues?q=hotlistid:5433121%20created:2026-04-01..2026-09-30)
* BigSleep: [hotlistid:8067258 created:2026-04-01..2026-09-30](https://issues.chromium.org/issues?q=hotlistid:8067258%20created:2026-04-01..2026-09-30)

From there, the raw numbers of bug reports are:

* Fuzzilli: 316
* BigSleep: 441

Small win for BigSleep. However, this includes all types of bugs, and BigSleep initially also found a lot of configuration and integration issues in V8, for example [crbug.com/503869331](https://crbug.com/503869331) where the [unsafe flag blocking mechanism](https://source.chromium.org/chromium/chromium/src/%2B/main%3Av8/src/flags/flag-definitions.h;l=4303;drc=4bd243831302ef96b70f7e159e5685bb2eba306f) didnât work properly yet. These are legitimate issues, but less relevant for our comparison since thereâs little real-world security impact. One easy way to get rid of these is to look specifically at vulnerabilities by limiting the results to `type:vulnerability`:

* Fuzzilli: 178
* BigSleep: 95

Suddenly a clear win for the fuzzers? Not quite. There are still some problems with this data, notably duplicates and unactionable reports (e.g. bugs [closed as WAI](https://issues.chromium.org/issues?q=hotlistid:\(8067258%20%7C%205433121\)%20status:intended_behavior)). At first, this seems like a simple thing to fix: just include another constraint such as `status:(fixed | verified)`. Unfortunately, things are a bit more complicated. Take for example Fuzzilli bug [crbug.com/511935486](https://crbug.com/511935486). The events on this bug are basically:

* The bug is filed by Clusterfuzz on May 11 and assigned to an engineer
* The bug is closed by Clusterfuzz as the testcase no longer reproduces later that same day

As such, this bug received zero developer interactions. Most likely what happened here is that this bug was a duplicate of another bug, [crbug.com/511210507](https://crbug.com/511210507), but Clusterfuzz didnât realize it as the crash signature (derived from the stack trace) was slightly different. When the other bug received a fix, the testcase stopped reproducing on Clusterfuzz, which closed the issue.

Maybe the best thing we can do is to look at âactionableâ bugs, defined as those that are not marked as duplicates or WAI *and* that received at least one fix commit referencing them. Then, looking at only `Type-Vuln` bugs filters out a lot of the less-relevant BigSleep bugs, even though these were âactionableâ. With that, the final picture looks like this:

![](/images/2026-10-27-fuzzing-v-AI-image1.png)

So in terms of vulnerabilities, itâs roughly a tie (small advantage BigSleep) at the moment: 45 vs. 37.

This naturally raises the question of co...
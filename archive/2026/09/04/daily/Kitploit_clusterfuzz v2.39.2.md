---
title: clusterfuzz v2.39.2
url: https://kitploit.com/en/posts/github-google-clusterfuzz-v2392
source: Kitploit
date: 2026-09-04
fetch_date: 2026-09-05T06:28:28.923275
---

# clusterfuzz v2.39.2

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/4906/22372ac3f7ec0a0ff2ac34c631a12c27251c14a0b4133db2307f80269de202ec.png)

New releaseSep 4, 2026

# clusterfuzz v2.39.2

Scalable fuzzing infrastructure with coverage-guided engines (libFuzzer, AFL, Honggfuzz), automated crash deduplication, bug filing, and regression bisection for finding security and stability issues.

Share

# ClusterFuzz

![](https://assets.kitploit.com/production/public/readmes/4906/22372ac3f7ec0a0ff2ac34c631a12c27251c14a0b4133db2307f80269de202ec.png)

[![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/google/clusterfuzz/badge)](https://api.securityscorecards.dev/projects/github.com/google/clusterfuzz)

ClusterFuzz is a scalable [fuzzing](https://en.wikipedia.org/wiki/Fuzzing)
infrastructure that finds security and stability issues in software.

Google uses ClusterFuzz to fuzz all Google products and as the fuzzing
backend for [OSS-Fuzz](https://github.com/google/oss-fuzz).

ClusterFuzz provides many features which help seamlessly integrate fuzzing into
a software project's development process:

* Highly scalable. Can run on any size cluster (e.g. OSS-Fuzz instance runs on
  100,000 VMs).
* Accurate deduplication of crashes.
* Fully automatic bug filing, triage and closing for various issue trackers
  (e.g. [Monorail](https://opensource.google.com/projects/monorail), [Jira](https://www.atlassian.com/software/jira)).
* Supports multiple [coverage guided fuzzing engines](https://google.github.io/clusterfuzz/setting-up-fuzzing/libfuzzer-and-afl/)
  ([libFuzzer](http://llvm.org/docs/LibFuzzer.html), [AFL](https://github.com/google/AFL), [AFL++](https://github.com/AFLplusplus/AFLplusplus) and [Honggfuzz](https://github.com/google/honggfuzz))
  for optimal results (with [ensemble fuzzing](https://www.usenix.org/system/files/sec19-chen-yuanliang.pdf) and [fuzzing strategies](https://i.blackhat.com/eu-19/Wednesday/eu-19-Arya-ClusterFuzz-Fuzzing-At-Google-Scale.pdf#page=27)).
* Support for [blackbox fuzzing](https://google.github.io/clusterfuzz/setting-up-fuzzing/blackbox-fuzzing/).
* Testcase minimization.
* Regression finding through [bisection](https://en.wikipedia.org/wiki/Bisection_%28software_engineering%29).
* Statistics for analyzing fuzzer performance, and crash rates.
* Easy to use web interface for management and viewing crashes.
* Support for various authentication providers using [Firebase](https://firebase.google.com/docs/auth).

## Overview

![](https://assets.kitploit.com/production/public/readmes/4906/16c76d25b0cf158a92a338fea3ab3bb31428fb55724d1be02c7a998a18a210ea.png)

## Documentation

You can find detailed documentation [here](https://google.github.io/clusterfuzz).

## Trophies

As of February 2023, ClusterFuzz has found ~27,000 bugs in Google (e.g. [Chrome](https://bugs.chromium.org/p/chromium/issues/list?can=1&q=label:ClusterFuzz+-status:WontFix,Duplicate)). Additionally, ClusterFuzz has helped identify and fix over [8,900](https://bugs.chromium.org/p/oss-fuzz/issues/list?q=status:Fixed,Verified%20Type=Bug-Security&can=1) vulnerabilities and [28,000](https://bugs.chromium.org/p/oss-fuzz/issues/list?q=status:Fixed,Verified%20Type=Bug&can=1) bugs across [850](https://github.com/google/oss-fuzz/tree/master/projects) projects integrated with [OSS-Fuzz](https://github.com/google/oss-fuzz).

## Getting Help

You can [file an issue](https://github.com/google/clusterfuzz/issues/new) to ask
questions, request features, or ask for help.

## Staying Up to Date

We will use [clusterfuzz-announce(#)googlegroups.com](https://groups.google.com/forum/#!forum/clusterfuzz-announce) to make announcements about ClusterFuzz.

## ClusterFuzzLite

For a more lightweight version of ClusterFuzz that runs on CI/CD
systems, check out [ClusterFuzzLite](https://github.com/google/clusterfuzzlite).

[Read more](/en/tools/github/google/clusterfuzz?expand=1)

## Categories

[Dynamic Analysis (Sandboxing)](/en/categories/dynamic-analysis-sandboxing)[Vulnerability Analysis](/en/categories/vulnerability-analysis)[Fuzzing](/en/categories/fuzzing)[DevSecOps](/en/categories/devsecops)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Kitploit is a directory of hacking, cybersecurity, and pentesting tools. Discover the latest project updates to find vulnerabilities, analyze systems, automate testing, and strengthen your security.

·Analytics preferences·[Feeds](/en/feeds)·[Contact](/en/contact)·[Privacy](/en/privacy)·© 2026 Kitploit

Tool Directory

## Categories

[View all categories](/en/categories)

Loading categories
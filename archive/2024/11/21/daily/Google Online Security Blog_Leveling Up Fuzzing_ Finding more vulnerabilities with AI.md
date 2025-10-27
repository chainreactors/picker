---
title: Leveling Up Fuzzing: Finding more vulnerabilities with AI
url: http://security.googleblog.com/2024/11/leveling-up-fuzzing-finding-more.html
source: Google Online Security Blog
date: 2024-11-21
fetch_date: 2025-10-06T19:14:15.583993
---

# Leveling Up Fuzzing: Finding more vulnerabilities with AI

![](https://ad.doubleclick.net/ddm/activity/src=2542116;type=gblog;cat=googl0;ord=1?)

[![](https://www.gstatic.com/images/branding/googlelogo/2x/googlelogo_color_150x54dp.png)](https://security.googleblog.com/)
[## Security Blog](/.)

The latest news and insights from Google on security and safety on the Internet

## [Leveling Up Fuzzing: Finding more vulnerabilities with AI](https://security.googleblog.com/2024/11/leveling-up-fuzzing-finding-more.html "Leveling Up Fuzzing: Finding more vulnerabilities with AI")

November 20, 2024

Posted by Oliver Chang, Dongge Liu and Jonathan Metzman, Google Open Source Security Team

Recently, OSS-Fuzz reported [26 new vulnerabilities](https://github.com/google/oss-fuzz-gen?tab=readme-ov-file#bugs-discovered) to open source project maintainers, including one vulnerability in the critical OpenSSL library ([CVE-2024-9143](https://openssl-library.org/news/secadv/20241016.txt)) that underpins much of internet infrastructure. The reports themselves aren’t unusual—we’ve reported and helped maintainers fix over 11,000 vulnerabilities in the 8 years of the project.

But these particular vulnerabilities represent a milestone for automated vulnerability finding: each was found with AI, using AI-generated and enhanced fuzz targets. The OpenSSL CVE is one of the first vulnerabilities in a critical piece of software that was discovered by LLMs, adding another real-world example to a recent Google discovery of [an exploitable stack buffer underflow in the widely used database engine SQLite](https://googleprojectzero.blogspot.com/2024/10/from-naptime-to-big-sleep.html).

This blog post discusses the results and lessons over a year and a half of work to bring AI-powered fuzzing to this point, both in introducing AI into fuzz target generation and expanding this to simulate a developer’s workflow. These efforts continue our explorations of how AI can transform vulnerability discovery and strengthen the arsenal of defenders everywhere.

# The story so far

In August 2023, the OSS-Fuzz team announced [AI-Powered Fuzzing](https://security.googleblog.com/2023/08/ai-powered-fuzzing-breaking-bug-hunting.html), describing our effort to leverage large language models (LLM) to improve fuzzing coverage to find more vulnerabilities automatically—before malicious attackers could exploit them. Our approach was to use the coding abilities of an LLM to generate more fuzz targets, which are similar to unit tests that exercise relevant functionality to search for vulnerabilities.

The ideal solution would be to completely automate the manual process of developing a fuzz target end to end:

1. Drafting an initial fuzz target.
2. Fixing any compilation issues that arise.
3. Running the fuzz target to see how it performs, and fixing any obvious mistakes causing runtime issues.
4. Running the corrected fuzz target for a longer period of time, and triaging any crashes to determine the root cause.
5. Fixing vulnerabilities.

In August 2023, we [covered our efforts](https://security.googleblog.com/2023/08/ai-powered-fuzzing-breaking-bug-hunting.html) to use an LLM to handle the first two steps. We were able to use an [iterative process to generate a fuzz target](https://google.github.io/oss-fuzz/research/llms/target_generation/) with a simple prompt including hardcoded examples and compilation errors.

In January 2024, we [open sourced](https://security.googleblog.com/2024/01/scaling-security-with-ai-from-detection.html) the [framework](http://github.com/google/oss-fuzz-gen) that we were building to enable an LLM to generate fuzz targets. By that point, LLMs were reliably generating targets that exercised more interesting code coverage across 160 projects. But there was still a long tail of projects where we couldn’t get a single working AI-generated fuzz target.

To address this, we’ve been improving the first two steps, as well as implementing steps 3 and 4.

# New results: More code coverage and discovered vulnerabilities

We’re now able to automatically gain more coverage in [272 C/C++ projects on OSS-Fuzz](https://github.com/google/oss-fuzz-gen?tab=readme-ov-file#current-top-coverage-improvements-by-project) (up from 160), adding 370k+ lines of new code coverage. The top coverage improvement in a single project was an increase from 77 lines to 5434 lines (a 7000% increase).

This led to the discovery of [26 new vulnerabilities](https://github.com/google/oss-fuzz-gen?tab=readme-ov-file#bugs-discovered) in projects on OSS-Fuzz that already had hundreds of thousands of hours of fuzzing. The highlight is [CVE-2024-9143](https://openssl-library.org/news/secadv/20241016.txt) in the critical and well-tested OpenSSL library. We reported this vulnerability on September 16 and a fix was published on October 16. As far as we can tell, this vulnerability has likely been present for two decades and wouldn’t have been discoverable with existing fuzz targets written by humans.

Another example was a bug in the project [cJSON](https://github.com/DaveGamble/cJSON/issues/800), where even though an existing human-written harness existed to fuzz a specific function, we still discovered a new vulnerability in that same function with an AI-generated target.

One reason that such bugs could remain undiscovered for so long is that line coverage is not a guarantee that a function is free of bugs. Code coverage as a metric isn’t able to measure all possible code paths and states—different flags and configurations may trigger different behaviors, unearthing different bugs. These examples underscore the need to continue to generate new varieties of fuzz targets even for code that is already fuzzed, as has also been shown by Project Zero in the past ([1](https://googleprojectzero.blogspot.com/2024/10/effective-fuzzing-dav1d-case-study.html), [2](https://googleprojectzero.blogspot.com/2021/12/this-shouldnt-have-happened.html)).

# New improvements

To achieve these results, we’ve been focusing on two major improvements:

1. Automatically generate more relevant context in our prompts. The more complete and relevant information we can provide the LLM about a project, the less likely it would be to hallucinate the missing details in its response. This meant providing more accurate, project-specific context in prompts, such as function, type definitions, cross references, and existing unit tests for each project. To generate this information automatically, we [built new infrastructure](https://introspector.oss-fuzz.com/api-doc) to index projects across OSS-Fuzz.

2. LLMs turned out to be highly effective at emulating a typical developer’s entire workflow of writing, testing, and iterating on the fuzz target, as well as triaging the crashes found. Thanks to this, it was possible to further automate more parts of the fuzzing workflow. This additional iterative feedback in turn also resulted in higher quality and greater number of correct fuzz targets.

# The workflow in action

Our LLM can now execute the first four steps of the developer’s process (with the fifth soon to come).

1. Drafting an initial fuzz target

A developer might check the source code, existing documentation and unit tests, as well as  usages of the target function when to draft an initial fuzz target. An LLM can fulfill this role here, if we provide a prompt with this information and ask it to come up with a fuzz target.

|  |
| --- |
| Prompt:    Your goal is to write a fuzzing harness for the provided function-under-test signature using <code>LLVMFuzzerTestOneInput</code>. It is important that the provided solution compiles and actually calls the function-under-test specified by the function signature:  <function signature>  unsigned char \* buffer\_append\_base64\_decode(buffer \*, const char \*, size\_t, base64\_charset)  </function signature>   Here is the source code of the function being tested:  <code>  unsigned char\* buffer\_append\_base64\_decode(buffer \*out, const char\* in, size\_t in\_length, ba...
---
title: Taking the next step: OSS-Fuzz in 2023
url: http://security.googleblog.com/2023/02/taking-next-step-oss-fuzz-in-2023.html
source: Google Online Security Blog
date: 2023-02-02
fetch_date: 2025-10-04T05:27:52.487382
---

# Taking the next step: OSS-Fuzz in 2023

![](https://ad.doubleclick.net/ddm/activity/src=2542116;type=gblog;cat=googl0;ord=1?)

[![](https://www.gstatic.com/images/branding/googlelogo/2x/googlelogo_color_150x54dp.png)](https://security.googleblog.com/)
[## Security Blog](/.)

The latest news and insights from Google on security and safety on the Internet

## [Taking the next step: OSS-Fuzz in 2023](https://security.googleblog.com/2023/02/taking-next-step-oss-fuzz-in-2023.html "Taking the next step: OSS-Fuzz in 2023")

February 1, 2023

Posted by Oliver Chang, OSS-Fuzz team

Since [launching in 2016](https://security.googleblog.com/2016/12/announcing-oss-fuzz-continuous-fuzzing.html), Google's free OSS-Fuzz code testing service has helped get over [8800](https://bugs.chromium.org/p/oss-fuzz/issues/list?q=status%3AFixed%2CVerified%20Type%3DBug-Security&can=1) vulnerabilities and [28,000](https://bugs.chromium.org/p/oss-fuzz/issues/list?q=status%3AFixed%2CVerified%20Type%3DBug&can=1) bugs fixed across [850](https://github.com/google/oss-fuzz/tree/master/projects) projects. Today, we’re happy to announce an expansion of our OSS-Fuzz Rewards Program, plus new features in OSS-Fuzz and our involvement in supporting academic fuzzing research.

# Refreshed OSS-Fuzz rewards

The OSS-Fuzz project's purpose is to support the open source community in adopting fuzz testing, or [fuzzing](https://github.com/google/fuzzing/blob/master/docs/why-fuzz.md) — an automated code testing technique for uncovering bugs in software. In addition to the OSS-Fuzz service, which provides a free platform for continuous fuzzing to critical open source projects, we established an [OSS-Fuzz Reward Program](https://testing.googleblog.com/2017/05/oss-fuzz-five-months-later-and.html) in 2017 as part of our wider [Patch Rewards Program](https://bughunters.google.com/about/rules/4928084514701312/patch-rewards-program-rules).

We’ve operated this successfully for the past 5 years, and to date, the OSS-Fuzz Reward Program has awarded over $600,000 to over 65 different contributors for their help integrating new projects into OSS-Fuzz.

Today, we’re excited to announce that we’ve expanded the scope of the OSS-Fuzz Reward Program considerably, introducing many new types of rewards!

These [new reward types](https://bughunters.google.com/about/rules/5097259337383936/oss-fuzz-reward-program-rules) cover contributions such as:

* Project fuzzing coverage increases* Notable FuzzBench fuzzer integrations* Integrating a new sanitizer ([example](https://security.googleblog.com/2022/09/fuzzing-beyond-memory-corruption.html)) that finds two new vulnerabilities

These changes boost the total rewards possible per project integration from a maximum of $20,000 to $30,000 (depending on the criticality of the project). In addition, we’ve also established two new reward categories that reward wider improvements across all OSS-Fuzz projects, with up to $11,337 available per category.

For more details, see the [fully updated rules](https://bughunters.google.com/about/rules/5097259337383936/oss-fuzz-reward-program-rules) for our dedicated OSS-Fuzz Reward Program.

# OSS-Fuzz improvements

We’ve continuously made improvements to OSS-Fuzz’s infrastructure over the years and expanded our language offerings to cover C/C++, Go, Rust, Java, Python, and Swift, and have introduced support for new frameworks such as [FuzzTest](https://github.com/google/fuzztest). Additionally, as part of an ongoing collaboration with Code Intelligence, we’ll soon have [support for JavaScript fuzzing](https://github.com/google/oss-fuzz/issues/8324) through [Jazzer.js](https://www.code-intelligence.com/blog/jazzer-js).

# FuzzIntrospector support

Last year, we [launched the OpenSSF FuzzIntrospector](https://openssf.org/blog/2022/06/09/introducing-fuzz-introspector-an-openssf-tool-to-improve-fuzzing-coverage/) tool and integrated it into OSS-Fuzz.

We’ve continued to build on this by adding new language support and better analysis, and now [C/C++, Python, and Java projects integrated into OSS-Fuzz](https://oss-fuzz-introspector.storage.googleapis.com/index.html) have detailed insights on how the coverage and fuzzing effectiveness for a project can be improved.

The [FuzzIntrospector](https://github.com/ossf/fuzz-introspector) tool provides these insights by identifying complex code blocks that are blocked during fuzzing at runtime, as well as suggesting new fuzz targets that can be added. We’ve seen users successfully use this tool to improve the coverage of *[jsonnet](https://github.com/ossf/fuzz-introspector/blob/main/doc/CaseStudies.md#jsonnet)*, *[file](https://github.com/ossf/fuzz-introspector/blob/main/doc/CaseStudies.md#file)*, *[xpdf](https://github.com/ossf/fuzz-introspector/blob/main/doc/CaseStudies.md#xpdf)* and *[bzip2](https://github.com/ossf/fuzz-introspector/blob/main/doc/CaseStudies.md#bzip2)*, among others.

Anyone can use this tool to increase the coverage of a project and in turn be rewarded as part of the [refreshed OSS-Fuzz rewards](https://bughunters.google.com/about/rules/5097259337383936/oss-fuzz-reward-program-rules#fuzzing-coverage). See the [full list](https://oss-fuzz-introspector.storage.googleapis.com/index.html) of all OSS-Fuzz FuzzIntrospector reports to get started.

# Fuzzing research and competition

The OSS-Fuzz team maintains [FuzzBench](https://google.github.io/fuzzbench/), a service that enables security researchers in academia to test fuzzing improvements against real-world open source projects. Approaching its third anniversary in serving free benchmarking, FuzzBench is [cited by over 100 papers](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=fuzzbench&btnG=) and has been used as a platform for academic fuzzing workshops such as [NDSS’22](https://fuzzingworkshop.github.io/).

This year, FuzzBench has been invited to participate in the [SBFT'23](https://sbft23.github.io/) workshop in [ICSE](https://conf.researchr.org/home/icse-2023), a premier research conference in the field, which for the first time is hosting [a fuzzing competition](https://sbft23.github.io/tools/fuzzing). During this competition, the FuzzBench platform will be used to evaluate state-of-the-art fuzzers submitted by researchers from around the globe on both code coverage and bug-finding metrics.

# Get involved!

We believe these initiatives will help scale security testing efforts across the broader open source ecosystem. We hope to accelerate the integration of critical open source projects into OSS-Fuzz by providing stronger incentives to security researchers and open source maintainers. Combined with our involvement in fuzzing research, these efforts are making OSS-Fuzz an even more powerful tool, enabling users to find more bugs, and, more critically, find them before the bad guys do!

![Share on Twitter](https://www.gstatic.com/images/icons/material/system/2x/post_twitter_black_24dp.png)

![Share on Facebook](https://www.gstatic.com/images/icons/material/system/2x/post_facebook_black_24dp.png)

[Google](https://plus.google.com/112374322230920073195)

#### No comments :

[Post a Comment](https://draft.blogger.com/comment/fullpage/post/1176949257541686127/5472284988377201943)

[**](https://security.googleblog.com/)

[**](https://security.googleblog.com/2023/02/the-us-government-says-companies-should.html "Newer Post")

[**](https://security.googleblog.com/2023/01/sustaining-digital-certificate-security_13.html "Older Post")

![](data:image/png;base64...)

## Labels

**

* [#sharethemicincyber](https://security.googleblog.com/search/label/%23sharethemicincyber)
* [#supplychain #security #opensource](https://security.googleblog.com/search/label/%23supplychain%20%23security%20%23opensource)
* [AI Security](https://security.googleblog.com/search/label/AI%20Security)
* [android](https://security.googleblog.com/search/label/android)
* [android security](https://security.googleblog.com/search/label/android%20security)
* [android tr](https://security.googleblog...
---
title: $22k awarded to SBFT ‘23 fuzzing competition winners
url: http://security.googleblog.com/2023/05/22k-awarded-to-sbft-23-fuzzing.html
source: Google Online Security Blog
date: 2023-05-16
fetch_date: 2025-10-04T11:36:55.899860
---

# $22k awarded to SBFT ‘23 fuzzing competition winners

![](https://ad.doubleclick.net/ddm/activity/src=2542116;type=gblog;cat=googl0;ord=1?)

[![](https://www.gstatic.com/images/branding/googlelogo/2x/googlelogo_color_150x54dp.png)](https://security.googleblog.com/)
[## Security Blog](/.)

The latest news and insights from Google on security and safety on the Internet

## [$22k awarded to SBFT ‘23 fuzzing competition winners](https://security.googleblog.com/2023/05/22k-awarded-to-sbft-23-fuzzing.html "$22k awarded to SBFT ‘23 fuzzing competition winners")

May 15, 2023

Dongge Liu, Jonathan Metzman and Oliver Chang, Google Open Source Security Team

Google’s Open Source Security Team recently sponsored a fuzzing competition as part of [ICSE’s](https://conf.researchr.org/home/icse-2023) [Search-Based and Fuzz Testing (SBFT) Workshop](https://sbft23.github.io/). Our goal was to encourage the development of new [fuzzing](https://owasp.org/www-community/Fuzzing) techniques, which can lead to the discovery of software vulnerabilities and ultimately a safer open source ecosystem.

The competitors’ fuzzers were judged on code coverage and their ability to discover bugs:

* [HasteFuzz](https://github.com/google/fuzzbench/tree/SBFT%2723/fuzzers/hastefuzz) took the [$11,337](https://bughunters.google.com/about/rules/5097259337383936/oss-fuzz-reward-program-rules) prize for code coverage
* [PASTIS](https://github.com/google/fuzzbench/tree/SBFT%2723/fuzzers/pastis) and [AFLrustrust](https://github.com/google/fuzzbench/tree/SBFT%2723/fuzzers/aflrustrust) tied for bug discovery and split the $11,337 prize

Competitors were evaluated using [FuzzBench](https://github.com/google/fuzzbench), Google’s open source platform for testing and comparing fuzzers. The platform boasts a wide range of real world benchmarks and vulnerabilities, allowing researchers to test their fuzzers in an authentic environment. We hope the [results](https://arxiv.org/pdf/2304.10070.pdf) of the SBFT fuzzing competition will lead to more efficient fuzzers and eventually newly discovered vulnerabilities.

# A closer look at our winners

Eight teams submitted fuzzers to the final competition and an additional four industry fuzzers ([AFL++](https://github.com/google/fuzzbench/tree/SBFT%2723/fuzzers/aflplusplus), [libFuzzer](https://github.com/google/fuzzbench/tree/SBFT%2723/fuzzers/libfuzzer), [Honggfuzz](https://github.com/google/fuzzbench/tree/SBFT%2723/fuzzers/honggfuzz), and [AFL](https://github.com/google/fuzzbench/tree/SBFT%2723/fuzzers/afl)) were included as controls to represent current practice.

* [Code coverage winner](https://storage.googleapis.com/www.fuzzbench.com/reports/experimental/SBFT23/Final-Coverage/index.html) - HasteFuzz

HasteFuzz, is a modification of the widely used AFL++ fuzzer. HasteFuzz filters out potentially duplicate inputs to increase efficiency, making it able to cover more code in the 23-hour test window because it is not likely to be retracing its steps. AFL++ is already a strong fuzzer—it had the best code coverage of the industry fuzzers tested in this competition—and HasteFuzz’s filtering took it to the next level.

* [Bug discovery winners](https://storage.googleapis.com/www.fuzzbench.com/reports/experimental/SBFT23/Final-Bug/index.html) - PASTIS and AFLrustrust

PASTIS makes use of multiple fuzzing engines that can independently cover different program locations, allowing PASTIS to find bugs quickly. AFLrustrust rewrites AFL++ on top of LibAFL, which is a library of features that allows you to customize existing fuzzers. AFLrustrust effectively prunes redundant test cases, improving its bug finding efficiency. Both PASTIS and AFLrustrust found 8 out of 15 possible bugs, with each fuzzer missing only one bug discovered by others. They both outperformed the industry fuzzers, which found 7 or fewer bugs under the same constraints.

Additional competitors, such as [AFL+++](https://github.com/google/fuzzbench/tree/master/fuzzers/aflplusplusplus) and [AFLSmart++](https://github.com/google/fuzzbench/tree/master/fuzzers/aflsmart_plusplus), also showed improvements over the industry controls, a result we had hoped for with the competition.

# Fuzzing research continues

The innovation and improvement shown through the SBFT fuzzing competition is one example of why we have invested in the FuzzBench project. Since [its launch in 2020](https://security.googleblog.com/2020/03/fuzzbench-fuzzer-benchmarking-as-service.html), FuzzBench has significantly contributed to [high-quality fuzzing research](https://google.github.io/fuzzbench/publications/), conducting over 900 experiments and discussed in more than 100 academic papers. FuzzBench was provided as a resource for the SBFT competition, but it is also available to researchers every day as a service. If you are interested in testing your fuzzers on FuzzBench, please see our guide to [adding your fuzzer](https://google.github.io/fuzzbench/getting-started/adding-a-new-fuzzer/).

FuzzBench is in active development. We’d welcome feedback from any current or prospective FuzzBench users, your responses to [this survey](https://forms.gle/xBxLz1dLt5Lt7AwDA) can help us plan the future of FuzzBench.

The Google Open Source Security Team would like to thank the ICSE conference and the SBFT workshop for hosting the fuzzing competition. We also want to thank each participant for their hard work. Together, we continue to push the boundaries of software security and create a safer, more robust open source ecosystem.

![Share on Twitter](https://www.gstatic.com/images/icons/material/system/2x/post_twitter_black_24dp.png)

![Share on Facebook](https://www.gstatic.com/images/icons/material/system/2x/post_facebook_black_24dp.png)

[Google](https://plus.google.com/112374322230920073195)

#### No comments :

[Post a Comment](https://www.blogger.com/comment/fullpage/post/1176949257541686127/7917589855671352598)

[**](https://security.googleblog.com/)

[**](https://security.googleblog.com/2023/05/new-android-google-device-VRP.html "Newer Post")

[**](https://security.googleblog.com/2023/05/introducing-new-way-to-buzz-for-ebpf.html "Older Post")

![](data:image/png;base64...)

## Labels

**

* [#sharethemicincyber](https://security.googleblog.com/search/label/%23sharethemicincyber)
* [#supplychain #security #opensource](https://security.googleblog.com/search/label/%23supplychain%20%23security%20%23opensource)
* [AI Security](https://security.googleblog.com/search/label/AI%20Security)
* [android](https://security.googleblog.com/search/label/android)
* [android security](https://security.googleblog.com/search/label/android%20security)
* [android tr](https://security.googleblog.com/search/label/android%20tr)
* [app security](https://security.googleblog.com/search/label/app%20security)
* [big data](https://security.googleblog.com/search/label/big%20data)
* [biometrics](https://security.googleblog.com/search/label/biometrics)
* [blackhat](https://security.googleblog.com/search/label/blackhat)
* [C++](https://security.googleblog.com/search/label/C%2B%2B)
* [chrome](https://security.googleblog.com/search/label/chrome)
* [chrome enterprise](https://security.googleblog.com/search/label/chrome%20enterprise)
* [chrome security](https://security.googleblog.com/search/label/chrome%20security)
* [connected devices](https://security.googleblog.com/search/label/connected%20devices)
* [CTF](https://security.googleblog.com/search/label/CTF)
* [diversity](https://security.googleblog.com/search/label/diversity)
* [encryption](https://security.googleblog.com/search/label/encryption)
* [federated learning](https://security.googleblog.com/search/label/federated%20learning)
* [fuzzing](https://security.googleblog.com/search/label/fuzzing)
* [Gboard](https://security.googleblog.com/search/label/Gboard)
* [google play](https://security.googleblog.com/search/label/google%20play)
* [google play protect](https://security.googleblog.com/search/label/google%20play%20protect)
* [hacking](https://security.googleblog.com/sea...
---
title: Fuzzing Farm #2: Evaluating Performance of Fuzzer
url: https://buaq.net/go-172073.html
source: unSafe.sh - 不安全
date: 2023-07-15
fetch_date: 2025-10-04T11:51:31.369001
---

# Fuzzing Farm #2: Evaluating Performance of Fuzzer

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

![](https://8aqnet.cdn.bcebos.com/34b1583a786a194dabafa5be5afe50be.jpg)

Fuzzing Farm #2: Evaluating Performance of Fuzzer

Author: hugeh0ge This article is Part 2 of the 4 blog posts in the Fuzzing Farm series. You can f
*2023-7-14 17:10:0
Author: [ricercasecurity.blogspot.com(查看原文)](/jump-172073.htm)
阅读量:23
收藏*

---

Author: hugeh0ge

 This article is Part 2 of the 4 blog posts in the Fuzzing Farm series. You can find the previous post at "[Fuzzing Farm #1: Fuzzing GEGL with fuzzuf](https://ricercasecurity.blogspot.com/2023/07/fuzzing-farm-1-fuzzing-gegl-with-fuzzuf.html)."

 As mentioned in Part 1, our Fuzzing Farm team uses our fuzzing framework, [fuzzuf](https://github.com/fuzzuf/fuzzuf), to find software bugs. It's not just the Fuzzing Farm team that works with fuzzers in our company; many situations arise where we need to evaluate the performance of different fuzzers, both in the development of Fuzzuf itself and in other research.

 However, there is little organized documentation about evaluating fuzzers, and numerous pitfalls exist in benchmarking. Without careful evaluation, one may draw incorrect conclusions. Does greater code coverage mean better performance? Is a fuzzer that finds more crashes superior?

 Evaluating the performance of a fuzzer is a challenging task. Setting up the experiment properly and drawing useful conclusions can be very difficult. Unfortunately, even in academia, where experiments should adhere to *scientific* standards, researchers sometimes rush to conclusions in statistically incorrect ways, or fail to set up experiments in a way that the fuzzing community recommends.

 In this article, we provide some cautions and recommended experimental settings for evaluating the performance of fuzzers. These recommendations are based on our research and experience in performance evaluations.

 Before going over the general recommended experimental setup, we will first elaborate on some problems in the performance evaluation of fuzzers.

### Ambiguity of Metrics

 The first challenge in evaluating the "performance" of a fuzzer is to establish an evaluation metric. While the aim of a fuzzer is typically to discover crashes (resulting from bugs or vulnerabilities), some people believe that the more crashes a fuzzer detects, the better its performance.

 However, consider the scenario where fuzzer A detects crashes *p*, *q*, and *r*, and fuzzer B detects crashes *r* and *s*. Can we conclude that fuzzer A is superior because it found one more crash than fuzzer B? In this case, we must also take into account the fact that fuzzer A could not find crash *s* (and similarly, fuzzer B could not find crashes *p* and *q*).

 Thus, if we want to assess fuzzer A's superiority based on this outcome alone, we should focus on evaluating fuzzers that can generally uncover a large number of crashes across a wide range of program-under-test (PUT), without considering the types of crashes that they can find.

 Moreover, it is important to note that **if we rely on the number of crashes as an evaluation metric, crash deduplication must be as precise as possible**. Since a mutation-based fuzzer generates many similar inputs, it creates a large number of inputs that trigger crashes on the same bugs.

 Generally, the fuzzer itself lacks the ability to pinpoint the cause of the crash and can only provide a simple classification. As a result, **the number of inputs that cause crashes is frequently not equivalent to the number of bugs/vulnerabilities found**.

 Consider an example where fuzzer A discovers 100 inputs that cause crash *r*, while fuzzer B identifies only one input that causes crash *r*. In this case, we cannot merely conclude that there is a difference of 99 in the number of crashes detected. (See Figure 1)

|  |
| --- |
| [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjIATIgUiAA-YoRSICM_xIH2oVLmKmEGW3iDbqBf5YduYYID2-8fV0KvXylrSpcGFkGcWTTeOT2cOwNu9_KEBVL-uReNvM00b_Ce-eFrePsac83_ynov0ceRx1KL250m4iXSMUqOeacFhFFaMi_l_6RAlQ815MpkE6T_P4aH7ynWT2AH8KS5XrWLilck1Y4/w640-h406/fuzzing-performance.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjIATIgUiAA-YoRSICM_xIH2oVLmKmEGW3iDbqBf5YduYYID2-8fV0KvXylrSpcGFkGcWTTeOT2cOwNu9_KEBVL-uReNvM00b_Ce-eFrePsac83_ynov0ceRx1KL250m4iXSMUqOeacFhFFaMi_l_6RAlQ815MpkE6T_P4aH7ynWT2AH8KS5XrWLilck1Y4/s911/fuzzing-performance.png) |
| Figure 1. More crashes found in Fuzzer A, but all inputs are causing the same bug |

文章来源: https://ricercasecurity.blogspot.com/2023/07/fuzzing-farm-2-evaluating-performance.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)
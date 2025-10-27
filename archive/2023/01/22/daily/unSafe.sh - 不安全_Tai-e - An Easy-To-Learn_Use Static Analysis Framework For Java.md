---
title: Tai-e - An Easy-To-Learn/Use Static Analysis Framework For Java
url: https://buaq.net/go-146425.html
source: unSafe.sh - 不安全
date: 2023-01-22
fetch_date: 2025-10-04T04:32:26.131847
---

# Tai-e - An Easy-To-Learn/Use Static Analysis Framework For Java

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

![](https://8aqnet.cdn.bcebos.com/bcdebc2750f0fd604cd197db5fd7bc96.jpg)

Tai-e - An Easy-To-Learn/Use Static Analysis Framework For Java

Tai-e What is Tai-e? Tai-e (Chinese: 太阿; pronunciation: [ˈtaɪə:]) is a new static analysis
*2023-1-21 19:30:0
Author: [www.kitploit.com(查看原文)](/jump-146425.htm)
阅读量:30
收藏*

---

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjonh-kfxzLVPUU2AOj4xBHHozowEaKKnwDgs1xYYV2no6SXApyw48wAxUPtXTK9t8zmvCdqhwbF1bjSWNJv9RA1siCAf_rWfEctkpQsuXaRB0eRmEC66bxl1jvQjc6kuqZ4mmuAIKr32KxAR_0rqdfBGd-Ecnd__2dzv2DCrVTM2LG5e1etzuh34PmNA/w285-h400/Tai-e.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjonh-kfxzLVPUU2AOj4xBHHozowEaKKnwDgs1xYYV2no6SXApyw48wAxUPtXTK9t8zmvCdqhwbF1bjSWNJv9RA1siCAf_rWfEctkpQsuXaRB0eRmEC66bxl1jvQjc6kuqZ4mmuAIKr32KxAR_0rqdfBGd-Ecnd__2dzv2DCrVTM2LG5e1etzuh34PmNA/s704/Tai-e.png)

## Tai-e

## What is Tai-e?

Tai-e (Chinese: 太阿; pronunciation: [ˈtaɪə:]) is a new static [analysis framework](https://www.kitploit.com/search/label/Analysis%20Framework "analysis framework") for Java (please see [our technical report](https://arxiv.org/abs/2208.00337 "our technical report") for details), which features arguably the "best" designs from both the novel ones we proposed and those of classic [frameworks](https://www.kitploit.com/search/label/Frameworks "frameworks") such as Soot, WALA, Doop, and SpotBugs. Tai-e is easy-to-learn, easy-to-use, efficient, and highly extensible, allowing you to easily develop new analyses on top of it.

Currently, Tai-e provides the following major analysis components (and more analyses are on the way):

* Powerful pointer analysis framework
  + On-the-fly call graph construction
  + Various classic and advanced [techniques](https://www.kitploit.com/search/label/Techniques "techniques") of heap abstraction and context sensitivity for pointer analysis
  + Extensible analysis plugin system (allows to conveniently develop and add new analyses that interact with pointer analysis)
* Various fundamental/client/utility analyses
  + Fundamental analyses, e.g., reflection analysis and exception analysis
  + Modern language feature analyses, e.g., lambda and method reference analysis, and invokedynamic analysis
  + Clients, e.g., configurable [taint analysis](https://www.kitploit.com/search/label/Taint%20Analysis "taint analysis") (allowing to configure sources, sinks and taint transfers)
  + Utility tools like analysis timer, constraint checker (for debugging), and various graph dumpers
* Control/Data-flow analysis framework
  + Control-flow graph construction
  + Classic data-flow analyses, e.g., live variable analysis, constant propagation
  + Your data-flow analyses
* SpotBugs-like bug detection system
  + Bug detectors, e.g., null pointer detector, incorrect `clone()` detector
  + Your bug detectors

Tai-e is developed in Java, and it can run on major operating systems including Windows, Linux, and macOS.

## How to Obtain Runnable Jar of Tai-e?

The simplest way is to download it from [GitHub Releases](https://github.com/pascal-lab/Tai-e/releases "GitHub Releases").

Alternatively, you might build the latest Tai-e yourself from the source code. This can be simply done via Gradle (be sure that Java 17 (or higher version) is available on your system). You just need to run command `gradlew fatJar`, and then the runnable jar will be generated in `tai-e/build/`, which includes Tai-e and all its dependencies.

## Documentation

We are hosting the documentation of Tai-e on [the GitHub wiki](https://github.com/pascal-lab/Tai-e/wiki "the GitHub wiki"), where you could find more information about Tai-e such as [Setup in IntelliJ IDEA](https://github.com/pascal-lab/Tai-e/wiki/Setup-Tai%E2%80%90e-in-IntelliJ-IDEA "Setup in IntelliJ IDEA") , [Command-Line Options](https://github.com/pascal-lab/Tai-e/wiki/How-to-Run-Tai%E2%80%90e%3F-%28command%E2%80%90line-options%29 "Command-Line Options") , and [Development of New Analysis](https://github.com/pascal-lab/Tai-e/wiki/How-to-Develop-A-New-Analysis-on-Tai%E2%80%90e%3F "Development of New Analysis") .

## Tai-e Assignments

In addition, we have developed an [educational version of Tai-e](http://tai-e.pascal-lab.net/en/intro/overview.html "educational version of Tai-e") where eight programming assignments are carefully designed for systematically training learners to implement various [static analysis](https://www.kitploit.com/search/label/Static%20Analysis "static analysis") techniques to analyze real Java programs. The educational version shares a large amount of code with Tai-e, thus doing the assignments would be a good way to get familiar with Tai-e.

Tai-e - An Easy-To-Learn/Use Static Analysis Framework For Java
![Tai-e - An Easy-To-Learn/Use Static Analysis Framework For Java](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjonh-kfxzLVPUU2AOj4xBHHozowEaKKnwDgs1xYYV2no6SXApyw48wAxUPtXTK9t8zmvCdqhwbF1bjSWNJv9RA1siCAf_rWfEctkpQsuXaRB0eRmEC66bxl1jvQjc6kuqZ4mmuAIKr32KxAR_0rqdfBGd-Ecnd__2dzv2DCrVTM2LG5e1etzuh34PmNA/s72-w285-c-h400/Tai-e.png)
Reviewed by Zion3R
on
8:30 AM
Rating: 5

文章来源: http://www.kitploit.com/2023/01/tai-e-easy-to-learnuse-static-analysis.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)
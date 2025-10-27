---
title: A Summarize-then-Search Method for Long Video Question Answering: Method
url: https://buaq.net/go-241649.html
source: unSafe.sh - 不安全
date: 2024-05-27
fetch_date: 2025-10-06T16:49:08.742694
---

# A Summarize-then-Search Method for Long Video Question Answering: Method

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

![](https://8aqnet.cdn.bcebos.com/8b39f78c364ca9592b0a252cc4e54a06.jpg)

A Summarize-then-Search Method for Long Video Question Answering: Method

Too Long; Didn't ReadIn this paper, researchers explore zero-shot video QA using GPT-3, outperformin
*2024-5-26 21:0:29
Author: [hackernoon.com(查看原文)](/jump-241649.htm)
阅读量:2
收藏*

---

![Read on Terminal Reader](https://hackernoon.imgix.net/computer.png?auto=format&fit=max&w=48)

## Too Long; Didn't Read

In this paper, researchers explore zero-shot video QA using GPT-3, outperforming supervised models, leveraging narrative summaries and visual matching.

![featured image - A Summarize-then-Search Method for Long Video Question Answering: Method](https://hackernoon.imgix.net/images/zhLunuihpBhk4IjuH4amrounSwE2-xm831k8.jpeg?auto=format&fit=max&w=3840)

![Kinetograph: The Video Editing Technology Publication HackerNoon profile picture](https://hackernoon.imgix.net/images/N0ENUd29UdNJCFcl7GnmZHdk2fA2-7g83zaa.jpeg?w=100&auto=format&fit=max)

## Table of Links

* [Abstract and Intro](http://hackernoon.com/preview/FU3Y0flSk1IUBC4Ybc7j?ref=hackernoon.com)
* [Method](http://hackernoon.com/preview/v8y8pJhiGiNLfeaAUHRP?ref=hackernoon.com)
* [Experiments](https://hackernoon.com/preview/Y5IGFrcynikECEHh1WBo?ref=hackernoon.com)
* [Related Work](http://hackernoon.com/preview/DhVb6BifG7SlHCbyNUCO?ref=hackernoon.com)
* [Conclusion](http://hackernoon.com/preview/oBH1W0dDeDXSMAetmlCG?ref=hackernoon.com)
* [Limitations and References](http://hackernoon.com/preview/Sf3XW3Lw0gnyUt05EsZq?ref=hackernoon.com)
* [A. Experiment Details](http://hackernoon.com/preview/rsN0nCDLaIT4rMp93OoS?ref=hackernoon.com)
* [B. Prompt Samples](http://hackernoon.com/preview/aNeVLElcaSSlspFKEUwX?ref=hackernoon.com)

## 2. Method

![](https://hackernoon.imgix.net/images/fWZa4tUiBGemnqQfBGgCPf9594N2-1w83zz7.png?auto=format&fit=max&w=1920)

![Figure 2: The qualitative result showing our proposed Long Story Short (LSS) model that generates and retrieves the index of raw video footage. When the model predicts the final answer from (i) the generated Summary and (ii) the retrieved text context, CLIPCheck validates each candidate’s answers to revise the final answer for the question.](https://hackernoon.imgix.net/images/fWZa4tUiBGemnqQfBGgCPf9594N2-l593zlf.png?auto=format&fit=max&w=2048)

### 2.1. Plot Generation

![](https://hackernoon.imgix.net/images/fWZa4tUiBGemnqQfBGgCPf9594N2-fwa3zx2.png?auto=format&fit=max&w=2048)

### 2.2. Narrative Search

Given the summarized narrative and the question, we wish to retrieve the relatively short clip relevant to the question from the long video. Language models generate open-ended text which is irregular and often noisy. To retrieve the exact part of the video, we drive the model to output indices of the plot rather than the text form.

![](https://hackernoon.imgix.net/images/fWZa4tUiBGemnqQfBGgCPf9594N2-rvb3zyd.png?auto=format&fit=max&w=2048)

The generated indices might still be noisy due to the open-ended nature of language models. When the model outputs an answer in text form, we use rouge-l [19] score to find plot piece candidates whose similarity with the generated sentence are above the specified threshold α ≥ 0.5.

![](https://hackernoon.imgix.net/images/fWZa4tUiBGemnqQfBGgCPf9594N2-hnc3zsx.png?auto=format&fit=max&w=2048)

### 2.3. Visual Checking

![](https://hackernoon.imgix.net/images/fWZa4tUiBGemnqQfBGgCPf9594N2-j6d3z80.png?auto=format&fit=max&w=3840)

文章来源: https://hackernoon.com/a-summarize-then-search-method-for-long-video-question-answering-method?source=rss
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)
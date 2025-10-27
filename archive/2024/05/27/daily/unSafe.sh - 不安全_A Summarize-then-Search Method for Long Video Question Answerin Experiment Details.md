---
title: A Summarize-then-Search Method for Long Video Question Answerin Experiment Details
url: https://buaq.net/go-241650.html
source: unSafe.sh - 不安全
date: 2024-05-27
fetch_date: 2025-10-06T16:49:09.413879
---

# A Summarize-then-Search Method for Long Video Question Answerin Experiment Details

* [unSafe.sh - дёҚе®үе…Ё](https://unsafe.sh)
* [жҲ‘зҡ„ж”¶и—Ҹ](/user/collects)
* [д»Ҡж—ҘзғӯжҰң](/?hot=true)
* [е…¬дј—еҸ·ж–Үз«](/?gzh=true)
* [еҜјиҲӘ](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [зј–з Ғ/и§Јз Ғ](/encode)
* [ж–Үд»¶дј иҫ“](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
й»‘еӨңжЁЎејҸ

![]()

A Summarize-then-Search Method for Long Video Question Answerin Experiment Details

Table of LinksAbstract and IntroMethodExperimentsRelated WorkConclusionLimitations and Refer
*2024-5-26 21:0:27
Author: [hackernoon.com(жҹҘзңӢеҺҹж–Ү)](/jump-241650.htm)
йҳ…иҜ»йҮҸ:3
ж”¶и—Ҹ*

---

## Table of Links

* [Abstract and Intro](http://hackernoon.com/preview/FU3Y0flSk1IUBC4Ybc7j?ref=hackernoon.com)
* [Method](http://hackernoon.com/preview/v8y8pJhiGiNLfeaAUHRP?ref=hackernoon.com)
* [Experiments](https://hackernoon.com/preview/Y5IGFrcynikECEHh1WBo?ref=hackernoon.com)
* [Related Work](http://hackernoon.com/preview/DhVb6BifG7SlHCbyNUCO?ref=hackernoon.com)
* [Conclusion](http://hackernoon.com/preview/oBH1W0dDeDXSMAetmlCG?ref=hackernoon.com)
* [Limitations and References](http://hackernoon.com/preview/Sf3XW3Lw0gnyUt05EsZq?ref=hackernoon.com)
* [A. Experiment Details](http://hackernoon.com/preview/rsN0nCDLaIT4rMp93OoS?ref=hackernoon.com)
* [B. Prompt Samples](http://hackernoon.com/preview/aNeVLElcaSSlspFKEUwX?ref=hackernoon.com)

## A. Experiment Details

**Computational Budget.** Long Story Short uses GPT-3 (175B parameters) via OpenAI API as the backbone. An average prompt to summarize a video segment processes вҲј 3000 tokens, while a QA prompt usually takes вҲј 4000 tokens. For CLIPCheck, we extract CLIP features and compute the cosine similarity using a single NVIDIA A6000 GPU: it takes 0.5 hours to process video frames for the MovieQA validation split.

**Hyperparameters**. All hyperparameters are pre-defined by analyzing a single training sample. For narrative search, we use sentence similarity threshold Оұ вүҘ 0.5 to find plot pieces when GPT-3 does not output a single index. We use the binary entropy threshold E вҖІ вүҘ 0.4 in CLIPCheck. We run each experiment only once, as our method is deterministic and is not susceptible to randomness in initialization.

**Video Segmentation Scheme.** There are predefined segment boundary annotations for all datasets we utilize in this paper. Also, all plot pieces have aligned clip segments in turn since we perform summarization on each clip segmented with the predefined boundaries. Also, before applying LSS we filter out clip segments that 1. are too short, 2. have no aligned image frame, or 3. have no text context to make sure that we can retrieve the clip segments using plot summaries.

**External Libraries.** We use OpenAI API to access GPT-3 language model. The CLIP features are computed with the Huggingface implementations (https://huggingface. co/docs/transformers/main/en/model\_doc/clip).

ж–Үз« жқҘжәҗ: https://hackernoon.com/a-summarize-then-search-method-for-long-video-question-answerin-experiment-details?source=rss
 еҰӮжңүдҫөжқғиҜ·иҒ”зі»:admin#unsafe.sh

© [unSafe.sh - дёҚе®үе…Ё](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [е®үе…Ёй©¬е…Ӣ](https://aq.mk)
* [жҳҹйҷ…й»‘е®ў](https://xj.hk)
* [T00ls](https://t00ls.net)
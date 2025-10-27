---
title: Towards Automatic Satellite Images Captions Generation Using LLMs: Abstract & Introduction
url: https://buaq.net/go-245485.html
source: unSafe.sh - 不安全
date: 2024-06-17
fetch_date: 2025-10-06T16:54:59.990421
---

# Towards Automatic Satellite Images Captions Generation Using LLMs: Abstract & Introduction

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

![]()

Towards Automatic Satellite Images Captions Generation Using LLMs: Abstract & Introduction

Authors:(1) Yingxu He, Department of Computer Science National University of Singapore {[email pro
*2024-6-16 22:30:18
Author: [hackernoon.com(查看原文)](/jump-245485.htm)
阅读量:4
收藏*

---

**Authors:**

(1) Yingxu He, Department of Computer Science National University of Singapore {[[email protected]](https://hackernoon.com/cdn-cgi/l/email-protection)};

(2) Qiqi Sun, College of Life Sciences Nankai University {[[email protected]](https://hackernoon.com/cdn-cgi/l/email-protection)}.

## Table of Links

* [Abstract and Intro](http://hackernoon.com/preview/0SKmdJWIEyPiarywYBSv?ref=hackernoon.com)
* [Methodology](http://hackernoon.com/preview/JowAM9SEdUdM6bATYkkp?ref=hackernoon.com)
* [References](http://hackernoon.com/preview/dQSRCDQ0CRpqs0ijvtYZ?ref=hackernoon.com)

## Abstract

Automatic image captioning is a promising technique for conveying visual information using natural language. It can benefit various tasks in satellite remote sensing, such as environmental monitoring, resource management, disaster management, etc. However, one of the main challenges in this domain is the lack of large-scale image-caption datasets, as they require a lot of human expertise and effort to create. Recent research on large language models (LLMs) has demonstrated their impressive performance in natural language understanding and generation tasks. Nonetheless, most of them cannot handle images (GPT-3.5, Falcon, Claude, etc.), while conventional captioning models pre-trained on general ground-view images often fail to produce detailed and accurate captions for aerial images (BLIP, GIT, CM3, CM3Leon, etc.). To address this problem, we propose a novel approach: Automatic Remote Sensing Image Captioning (ARSIC) to automatically collect captions for remote sensing images by guiding LLMs to describe their object annotations. We also present a benchmark model that adapts the pre-trained generative image2text model (GIT) to generate high-quality captions for remote-sensing images. Our evaluation demonstrates the effectiveness of our approach for collecting captions for remote sensing images.

Many previous studies have shown that LLMs such as GPT-3.5 and GPT-4 are good at understanding semantics but struggle with numerical data and complex reasoning. To overcome this limitation, ARSIC leverages external APIs to perform simple geographical analysis on images, such as object relations and clustering. We perform clustering on the objects and present the significant geometric relations for LLM to make summarizations. The final output of the LLM is several captions that describe the image, which will be further ranked and shortlisted based on language fluency and consistency with the original image.

We fine-tune a pre-trained generative image2text (GIT) model on 7 thousand and 2 thousand image-caption pairs from the Xview and DOTA datasets, which contain satellite images with bounding box annotations for various objects, such as vehicles, constructions, ships, etc. We evaluate our approach on the RSICD dataset, a benchmark dataset for satellite image captioning with 10,892 images and 31,783 captions annotated by human experts. We remove captions with unseen object types from the training data and obtain 1746 images with more than 5 thousand captions, where we achieve a CIDEr-D score of 85.93, demonstrating the effectiveness and potential of our approach for automatic image captioning in satellite remote sensing. Overall, this work presents a feasible way to guide them to interpret geospatial datasets and generate accurate image captions for training end-to-end image captioning models. Our approach reduces the need for human annotation and can be easily applied to datasets or domains.

## 1. Introduction

Satellite remote sensing is essential in numerous fields, such as disaster management, environmental monitoring, and resource management. It involves analyzing images captured from space, focusing on detecting and classifying objects on Earth’s surface to produce useful spatial information. As these images can contain a rich amount of data, automatic image captioning has emerged as an efficient method to interpret and convey the visual information in these images using natural language.

Despite its significant potential, a major challenge in automatic image captioning in satellite remotesensing images is the scarcity of large-scale image-caption datasets. Creating such datasets is labor-intensive and demands significant human expertise. Often, pre-existing models, such as GPT3.5[7], Falcon, and Claude, fall short in their applicability as they are not equipped to interpret numerical data or carry out complex reasoning. Similarly, models like BLIP[5], GIT[9], CM3[1], and CM3Leon[12] that are pre-trained on general ground-view images struggle to generate precise captions for aerial images. These limitations make it challenging to achieve high-quality automatic captioning for remote-sensing images.

To confront this issue, in this study, we propose a novel approach: Automatic Remote Sensing Image Captioning (ARSIC), which leverages both large language models and satellite data to generate high-quality captions for remote sensing images efficiently. Our contributions are threefold. First, we develop several geographical analysis APIs to detect clusters, identify shapes formed by objects, and calculate distances to offer an enhanced understanding of the image. Second, we automate the process of caption collection by guiding large language models to summarize the results from the geographical APIs into captions. This reduces the need for human annotation considerably. Lastly, we provide a benchmark by finetuning a generative image2text (GIT) model on image-caption pairs collected following our ARSIC approach from the Xview[4] and DOTA[2] datasets and tailored to generate high-quality and accurate captions for aerial images.

The effectiveness of our approach is validated through rigorous testing on the RSICD[6] test dataset, setting a new benchmark CIDEr-D[8] score in the field. In summary, our work presents an innovative approach towards interpreting and captioning remote sensing images - a method that is not only promising for optimizing end-to-end image captioning models but also flexible enough to be applied across datasets or domains.

文章来源: https://hackernoon.com/towards-automatic-satellite-images-captions-generation-using-llms-abstract-and-introduction?source=rss
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)
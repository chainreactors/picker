---
title: [译][论文] 大语言模型（LLM）综述与实用指南（2023）
url: https://buaq.net/go-172718.html
source: unSafe.sh - 不安全
date: 2023-07-24
fetch_date: 2025-10-04T11:51:13.530331
---

# [译][论文] 大语言模型（LLM）综述与实用指南（2023）

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

![](https://8aqnet.cdn.bcebos.com/1b64a1326a2e740d81e2cb72b5406ded.jpg)

[译][论文] 大语言模型（LLM）综述与实用指南（2023）

Published at 2023-07-23 | Last Update 2023-07-23 译者序本文来自 2023 年一篇大模型论文：Harnessi
*2023-7-23 08:0:0
Author: [arthurchiao.github.io(查看原文)](/jump-172718.htm)
阅读量:112
收藏*

---

Published at 2023-07-23 | Last Update 2023-07-23

### 译者序

本文来自 2023 年一篇大模型论文：
[Harnessing the Power of LLMs in Practice: A Survey on ChatGPT and Beyond](https://arxiv.org/abs/2304.13712)，
翻译了其中感兴趣的部分。

论文信息：

```
@article{yang2023harnessing,
	title={Harnessing the Power of LLMs in Practice: A Survey on ChatGPT and Beyond},
	author={Jingfeng Yang and Hongye Jin and Ruixiang Tang and Xiaotian Han and Qizhang Feng and Haoming Jiang and Bing Yin and Xia Hu},
	year={2023},
	eprint={2304.13712},
	archivePrefix={arXiv},
	primaryClass={cs.CL}
}
```

![](https://arthurchiao.github.io/assets/img/llm-practical-guide/fig-1.png)

一些工程信息：

1. 训练

   1. 训练费用：**`GPT-3 175B`** 单次训练 **460 万美元** [3]。
   2. 能耗：训练 PaLM 两个月左右耗费约了 3.4 Gwh [6]。
   3. 数据集大小：**`GPT-3 175B`** 训练了 **4990 亿个 token** [16]。
   4. OpenAI 训练集群：285k CPU, 10k high-end GPU。
2. 推理

   1. 推理时间

      * 最大 token 分别为 2、8 和 32 时，GPT-J 6B 模型的推理时间分别为 0.077s、0.203s 和 0.707s。
      * 最大 token 固定为 32 时，InstructGPT 模型（davinci v2）的推理时间为 **`1.969s`**。
   2. API 延迟：OpenAI API 的平均延迟时间从几百毫秒到几秒不等。
   3. InstructGPT davinci v2（175B）的理想**去噪推理时间**
      **`0.21s/request`**。

**译者水平有限，不免存在遗漏或错误之处。如有疑问，敬请查阅原文。**

以下是译文。

---

文章来源: https://arthurchiao.github.io/blog/llm-practical-guide-zh/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)
---
title: [译][论文] LLaMA 2：开放基础和微调聊天模型（Meta/Facebook，2023）
url: https://buaq.net/go-173797.html
source: unSafe.sh - 不安全
date: 2023-08-07
fetch_date: 2025-10-04T11:59:00.683939
---

# [译][论文] LLaMA 2：开放基础和微调聊天模型（Meta/Facebook，2023）

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

![](https://8aqnet.cdn.bcebos.com/0c7de01a370ab1ff9d44b088ebc487e0.jpg)

[译][论文] LLaMA 2：开放基础和微调聊天模型（Meta/Facebook，2023）

Published at 2023-08-06 | Last Update 2023-08-06 译者序本文来自 2023 年 Meta（facebook）的大
*2023-8-6 08:0:0
Author: [arthurchiao.github.io(查看原文)](/jump-173797.htm)
阅读量:124
收藏*

---

Published at 2023-08-06 | Last Update 2023-08-06

### 译者序

本文来自 2023 年 Meta（facebook）的大模型论文：
[Llama 2: Open Foundation and Fine-Tuned Chat Models](https://arxiv.org/abs/2307.09288)。
翻译了其中感兴趣的部分。

LLaMA2 用了两个 GPU 集群进行训练：

1. RSC 集群：**`200Gbps InfiniBand + 400W A100 GPU`**；
2. 生产集群：**`200Gbps RoCE + 350W A100 GPU`**；

**`RoCE + 350W GPU`** 的集群，经过优化的代码能达到
**`IB + 400W GPU`** 集群性能的 **`90%`**。
总共耗费 **`3.3M GPU-hour`**。

**译者水平有限，不免存在遗漏或错误之处。如有疑问，敬请查阅原文。**

以下是译文。

---

文章来源: https://arthurchiao.github.io/blog/llama2-paper-zh/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)
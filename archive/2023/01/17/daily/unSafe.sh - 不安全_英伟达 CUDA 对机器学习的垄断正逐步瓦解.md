---
title: 英伟达 CUDA 对机器学习的垄断正逐步瓦解
url: https://buaq.net/go-145800.html
source: unSafe.sh - 不安全
date: 2023-01-17
fetch_date: 2025-10-04T04:01:59.737422
---

# 英伟达 CUDA 对机器学习的垄断正逐步瓦解

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

英伟达 CUDA 对机器学习的垄断正逐步瓦解

过去十年，机器学习软件开发框架经历了巨大变化。虽然大部分框架严重依赖于英伟达 CUDA，在 英伟达 CUDA 上有最佳性能。但随着 PyTorch 2.0 和 OpenAI Triton
*2023-1-16 22:16:29
Author: [www.solidot.org(查看原文)](/jump-145800.htm)
阅读量:22
收藏*

---

过去十年，机器学习软件开发框架经历了巨大变化。虽然大部分框架严重依赖于英伟达 CUDA，在 英伟达 CUDA 上有最佳性能。但随着 PyTorch 2.0 和 OpenAI Triton 的到来，英伟达 CUDA 对机器学习的垄断地位正逐渐瓦解。几年前，Google 的 TensorFlow 框架及专用加速器 TPU 具有先发优势，Google 被认为有望在机器学习行业占据主导地位。然而 Google 未能将先发优势转变为行业主导地位。PyTorch 赢了。没有使用 PyTorch 和 GPU 的 Google 孤立于机器学习社区。Google 偏爱自己软件栈和硬件，甚至于以典型的 Google 风格，它还开发了第二个框架 Jax 与自家的 TensorFlow 展开直接竞争。PyTorch 的一大优势是其灵活性，而即将到来的 2.0 将能更容易的利用不同硬件资源。PyTorch 2.0 改进英伟达 A100 GPU 训练性能达 86%，CPU 推理性能提升 26%，显著减少了训练模型所需的计算时间和成本。它还可以扩展到 AMD、英特尔、Tenstorrent、Luminous Computing、特斯拉、Google、亚马逊、微软、Marvell、Meta、Graphcore、Cerebras、SambaNova 等公司生产的 GPU 和加速器上。OpenAI 的 Triton 同样对英伟达的机器学习闭源软件护城河产生冲击，它可以跳过闭源 CUDA 库如 cuBLAS，使用开源库如 cutlass。使用 CUDA 需要对底层硬件有深入了解，而 Triton 能让高级语言达到与使用低级语言相当的性能，提高了可用性。OpenAI Triton 目前只支持英伟达 GPU，但未来将会支持其它硬件制造商。

https://www.semianalysis.com/p/nvidiaopenaitritonpytorch

文章来源: https://www.solidot.org/story?sid=73904
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)
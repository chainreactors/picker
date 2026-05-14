---
title: 2.DFlash - 研究人员找到了将大语言模型加速 8.5 倍的方法？
url: https://mp.weixin.qq.com/s/8bvXo0XcDHb2I63paluKwg
source: Doonsec's feed
date: 2026-05-13
fetch_date: 2026-05-14T05:45:29.604108
---

# 2.DFlash - 研究人员找到了将大语言模型加速 8.5 倍的方法？

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icfnkibn16Vej4avQotb2dJT7aDtPd4p9MWT8s4pX2M1wbwJDibfKaf9QXqBvTQxHgLAG0XZcRRzJjX5rtYUu548ibAjKUu2MyquTZia12UXDvibM/0?wx_fmt=jpeg)

# 2.DFlash - 研究人员找到了将大语言模型加速 8.5 倍的方法？

原创

Esn Arsenal
Esn Arsenal

Esn技术社区

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**DFlash**是一种轻量级**块扩散**模型，专为推测性解码而设计。它能够实现高效、高质量的并行绘图。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icfnkibn16VeiakYDiaeXEsXM8anSkQkxibhsw8ZX5UUTHkBjTx27SwQqfjk1GZYNiaUNxI6Mq4nKOCRR2XHdN5Pib4dOKPphMGOFAZafpyjf4EZVQ/640?wx_fmt=png&from=appmsg)

**投机解码（Speculative Decoding）** 是一种相当有效的方法，可解决传统大语言模型推理中的“单令牌（逐词）生成”瓶颈。

其工作流程是：先由一个小型草稿模型生成多个后续令牌，再由大型目标模型通过一次前向传播并行验证它们。

如果某个位置的令牌被验证为错误，则保留该位置之前的所有正确令牌，并从此处继续生成。**该方法的最终输出质量绝不会劣于传统解码方式。**

然而，当前投机解码中使用的草稿模型仍然是逐个预测令牌的。这导致草稿生成阶段本身成为了新的瓶颈，使得实际场景中的加速比通常只能达到 2–3 倍。

**DFlash** 是一项新技术，它用轻量级的\*\*块扩散模型（Block Diffusion Model）\*\*取代了自回归草稿模型，能够在一个前向传播中并行预测所有令牌。

无论投机预测的令牌数量有多少，草稿生成的计算开销都保持恒定。

此外，草稿模型会接收来自目标模型多个层的隐藏特征，并将这些特征注入到草稿生成的每一层中。得益于这种上下文信息的注入，其预测精度相比无此机制的模型有了显著提升。

如上方演示所示，传统解码的速度为 48.5 令牌/秒，而 DFlash 在同一模型上达到了 **415 令牌/秒**，且没有任何质量损失。

该技术目前已集成到 `vLLM`、`SGLang` 和 `Transformers` 框架中。针对 Qwen3、Qwen3.5、Llama 3.1、Kimi-K2.5、gpt-oss 等众多模型的草稿模型也已上架 HuggingFace。

* GitHub 仓库：https://github.com/EsnBl0ckdev/dflash

**KV 缓存（KV-Caching）** 是加速大语言模型推理的另一项核心技术。关于它的详细介绍，可参考这篇文章。https://x.com/\_avichawla/status/2034902650534187503

##

https://github.com/EsnBl0ckdev/dflash

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/PwaXL3w2IRbdW3dY1XLuF3qWXIEQCvzWGBaFGLibfRGHs2JDuomUTlU6FRYuHxWDaluyrOwDgzyiaxeUjMODURDw/0?wx_fmt=png)

Esn技术社区

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/PwaXL3w2IRbdW3dY1XLuF3qWXIEQCvzWGBaFGLibfRGHs2JDuomUTlU6FRYuHxWDaluyrOwDgzyiaxeUjMODURDw/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过
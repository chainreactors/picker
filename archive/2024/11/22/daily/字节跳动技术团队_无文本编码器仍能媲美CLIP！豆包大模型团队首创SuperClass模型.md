---
title: 无文本编码器仍能媲美CLIP！豆包大模型团队首创SuperClass模型
url: https://mp.weixin.qq.com/s?__biz=MzI1MzYzMjE0MQ==&mid=2247511692&idx=1&sn=675c2d38e9ab671f56f9709ea53746e2&chksm=e9d3656edea4ec78cc5943dd700f74d3acdf3480f4ca5381ecef7f1dca2f8a012b72dcd85bd1&scene=58&subscene=0#rd
source: 字节跳动技术团队
date: 2024-11-22
fetch_date: 2025-10-06T19:19:31.545431
---

# 无文本编码器仍能媲美CLIP！豆包大模型团队首创SuperClass模型

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5EcwYhllQOjficxj6J2gOCtf2j1Jk3WFLicv9Vm5H8GeMbSA91FKdkQYtqqiam7qTr1XTPYzX3ibCicZPwNYmFNcsYA/0?wx_fmt=jpeg)

# 无文本编码器仍能媲美CLIP！豆包大模型团队首创SuperClass模型

字节跳动技术团队

近日，字节跳动豆包大模型团队提出 SuperClass ，一个超级简单且高效的预训练方法。该方法首次舍弃文本编码器，直接使用原始文本的分词作为多分类标签，无需额外的文本过滤或筛选，比 CLIP 具有更高的训练效率。

实验结果表明，SuperClass 在多种纯视觉任务和视觉语言多模态下游任务上表现出色，并且在模型大小和数据集大小方面具备与 CLIP 相同或更优的 Scalability 。本文将介绍 SuperClass 的实现原理、技术亮点及实验结果。

CLIP，可谓 AI 大模型中的“眼睛”。该模型通过将图像与文本对齐，实现了图像与语言之间的理解与关联。近些年来，CLIP 被广泛应用于视觉理解、图像问答、机器人/具身智能等多个领域。

但 CLIP 自身结构对计算量的高要求，限制其进一步应用与发展。

字节跳动豆包大模型视觉基础研究团队于近日公布最新成果 SuperClass 。该模型首次去掉了文本编码器，仅利用海量的图像-文本数据集预训练，无需文本编码器及构建大规模对比 Batch Size ，就能得到强大甚至表现更好的视觉模型。

取代 CLIP 的对比学习方法，SuperClass 不仅成功解决计算负担重的问题，同时可获得效果可观的视觉模型。实验结果表明，SuperClass 在各种纯视觉场景和视觉-语言多模态场景下均优于 CLIP ，同时基于分类的方法，模型展现出与 CLIP 相当，甚至更优的 Scalability 。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/IrH3BAPESuiaChY7fIFz5ibVONanUiaZqaO5Z3TjAlSo1bNCoW2PoM3MvofHvZ3Z11e1qeJYp6bPOV4wfhnzPEV2Q/640?wx_fmt=gif&from=appmsg)

目前，论文成果和代码仓库已对外公开，并被 NeurIPS 2024 接收。

> ***SuperClass: Classification Done Right for Vision-Language Pre-Training***
>
> ***论文链接：**https://arxiv.org/abs/2411.03313*
>
> ***代码链接：**https://github.com/x-cls/superclass*

**1. 高计算量带来 CLIP 的限制**

近年来，基于 Web-Scale 的图像-文本数据集的预训练方法已彻底改变计算机视觉领域，尤其 Contrastive Language Image Pretraining (CLIP)  及其系列模型获得了越来越多关注，并已成为大多数当前视觉语言模型（VLM）的默认选择。

CLIP 的广泛应用源自于三方面优势：首先，优越的视觉表征能力，大幅提升零样本视觉识别的精度和下游任务适配的泛化性。其次，CLIP 表现出不错的 Scalability ，一定程度上，能持续受益于更大模型和更多数据。第三，强大的跨模态能力，本质上，CLIP 就是为连接文本与图像而设计的。

尽管 CLIP 已取得成功，但要达到更佳性能，模型在训练时就需要非常大的 Batch Size 用于对比学习，同时，还需要大量计算资源进行文本编码。对于计算量的高要求一定程度上限制了该技术应用与进一步发展。

## **2. 首创超级简单的多分类方法，无文本编解码器**

面向上述问题，豆包大模型团队在业内率先提出一种全新、超级简单的多分类方法 SuperClass 。

无需文本编码器和解码器，也无需额外文本过滤和筛选，仅使用原始文本，团队实现了监督视觉模型的高效训练，同时具有良好的模型和数据 Scalability 。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/IrH3BAPESuiaChY7fIFz5ibVONanUiaZqaOKQ3zfiaBVUicia6g1up5ygcZe4xIo4GxabkMzOVvCnsb6IPQLZwjRibkOQ/640?wx_fmt=jpeg)

* **实现原理**

我们希望建立一个基于图像分类的预训练方案，保持简单性、可扩展性和高效率，同时精度可以与 CLIP 相媲美。因此，我们采用 Vision Transformer (ViT) 作为视觉编码器的主干网络，后接全局平均池化层和一个线性层作为分类头。

在训练步骤中，我们的方法类似于典型监督多标签分类网络，输入一张图像，提取全局特征，并通过分类层获得逻辑向量 ![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/IrH3BAPESuiaChY7fIFz5ibVONanUiaZqaOcVbic8C22wMXdtWFHviaNC5688GY8rb24XLhowicSBP98ffbacIeDUS6A/640?wx_fmt=jpeg) 。分类标签从图像对应的文本中得到，分类损失由文本衍生的分类标签和预测向量共同构成。

* **文本映射成分类标签**

与之前的基于分类方法不同，对于一个包含 N 对图像 **I** 和文本描述 **T** 的图像-文本数据集![](https://mmbiz.qpic.cn/sz_mmbiz_png/IrH3BAPESuiaChY7fIFz5ibVONanUiaZqaO0ruGbAFjdkahHQBPKOWERzzkl1XTugOy2hSNnfianzJEsq1nNFO0ZIA/640?wx_fmt=png&from=appmsg)，我们直接使用现有子词级别分词器（如 CLIP 或 Bert 中使用的分词器），词汇表大小为 **v** ，输入文本 **T**并获得相应的子词 ID 集合 **C**作为分类标签。

集合 **C**中的标签满足![](https://mmbiz.qpic.cn/sz_mmbiz_png/IrH3BAPESuiaChY7fIFz5ibVONanUiaZqaOPrFtORnLCGXJUjek7Yic7Mthr0x4QNs3c6KHN6zq6VRpkI4qv5ja4jg/640?wx_fmt=png&from=appmsg)。分类 **C**标签将被转换为 N-hot 向量![](https://mmbiz.qpic.cn/sz_mmbiz_png/IrH3BAPESuiaChY7fIFz5ibVONanUiaZqaOiavTS1nFCvzfniaYTQBVrg7XWEb7iab6ERtrLob9S2kJ5keN7nzAgVzWg/640?wx_fmt=png&from=appmsg)，其中当 **c**在集合 **C**中时![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/IrH3BAPESuiaChY7fIFz5ibVONanUiaZqaOicU4yFJnphvAJ8cvXLGTynByuP2kcfsTvKzv8aNqWwnPQHDfFQjuTdA/640?wx_fmt=jpeg&from=appmsg)，否则![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/IrH3BAPESuiaChY7fIFz5ibVONanUiaZqaOLVNhJ63V5WzdP2pGgjFPxxwNlia95pnvFk7QWgbXfqGRDmQkMTrpHwQ/640?wx_fmt=jpeg&from=appmsg) 。

与之前基于分类的预训练方法相比，我们的方法不需要任何预处理或手动阈值设置，同时，它也避免了之前方法可能遇到的词表溢出（Out-of-vocabulary）问题。

* **分类损失函数**

业内已有大量研究探讨多标签分类损失函数。然而，值得注意的是，我们的目标是预训练视觉编码器，而不是真正专注于多标签分类准确率。因此，我们对几种多标签分类损失进行了消融实验，包括 Softmax Loss、BCE Loss、Soft Margin Loss、ASL 和 Two-way Loss。

令人惊讶的是，简单的 Softmax 损失产生了最佳预训练结果。这可能是因为当前多标签分类损失建立在标签精确且完整的假设基础上，努力优化正负类别之间的间隔。然而，图像-文本数据中存在固有噪声，且文本在完整描述图像内容方面的局限性，意味着图像中所有对象并不总在配对文本中被提及。

在多标签场景中，通过以概率方式描述标签来应用 Softmax 损失，其中 ![](https://mmbiz.qpic.cn/sz_mmbiz_png/IrH3BAPESuiaChY7fIFz5ibVONanUiaZqaOokTCkKaRt4p3OyESVptVPNgO7Yu6SPXzsVNiab1bAP24WIoGicrskaCQ/640?wx_fmt=png&from=appmsg) 是归一化加权标签。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/IrH3BAPESuiaChY7fIFz5ibVONanUiaZqaOelgGzC6qkWN92072DelCGic83nR1aBreqQxIZyxAwaWIFwvIbnlmTCg/640?wx_fmt=png&from=appmsg)

* **逆文档频率作为类别权重**

在子词词汇表中，每个词都承载着不同程度的信息量，不同类别之间并非同等重要。此外，考虑到子词词典中包含许多语句常见词，这些词与视觉内容无关，并不能提供有效的监督信息。

因此，团队认为，携带大量信息的词在训练过程中应被赋予更大权重。我们使用逆文档频率（Inverse Document Frequency 或 IDF ）来衡量信息量，IDF 包含特定词的样本数量越少，该词区分不同样本的能力就越强。

我们使用类别（子词）的逆文档频率（IDF）统计作为分类标签的权重，为分类标签 **c**分配不同的权重![](https://mmbiz.qpic.cn/sz_mmbiz_png/IrH3BAPESuiaChY7fIFz5ibVONanUiaZqaOVvAODqIHicHpGGxcGgKgIhksZGXTGsgQrficGJjzKTGBYAPvAuJYxjxQ/640?wx_fmt=png&from=appmsg)：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/IrH3BAPESuiaChY7fIFz5ibVONanUiaZqaOicicKaJ84dP3QyG4AuLLV0TJGHZFzdo3ibFHxvTnBM62uiaZuYI6qd2yAw/640?wx_fmt=png&from=appmsg)

其中，![](https://mmbiz.qpic.cn/sz_mmbiz_png/IrH3BAPESuiaChY7fIFz5ibVONanUiaZqaOKMTrIwHvRBvQ5xxX1Or9nR1kPEIPQXkoLNfdObyAvicmmvtgMCmQUOA/640?wx_fmt=png&from=appmsg) 是图像-文本对的总数，![](https://mmbiz.qpic.cn/sz_mmbiz_png/IrH3BAPESuiaChY7fIFz5ibVONanUiaZqaOuDKfnQrzpX1yCmia1TQDJaoUbAyV1cJLbibDbyx6FgmtVdUrhgTiciaJJQ/640?wx_fmt=png&from=appmsg) 是子词**c**的文档频率（df），也就是包含子词**c**的文本数量。为了更加便于使用，我们在训练过程中实现了在线 IDF 统计，无需在训练前离线统计。这使得 SuperClass 方法更加友好且便于移植。

## **3. SuperClass 不仅简单和高效，还能学习到更好的视觉表征**

由于不需要文本编码器和构建巨大的相似性矩阵，SuperClass 可以节省大约 50% 的显存使用，加速 20% 以上。

为了更好度量预训练得到的视觉表征能力，我们固定住训练好的视觉模型的参数，将其应用到 Linear probing 、zero-shot 、10-shot 等分类任务，同时接入到 LLM 做视觉和语言多模态下游任务进行评测。

所有实验中，我们均采用和 CLIP 相同的模型和训练参数设置。

* **更好的视觉表征**

结果显示，SuperClass 在各种模型大小和数据规模都取得不错的精度。与其他无监督方法相比， SuperClass 由于依靠语义信息作为监督，训练数据多样，在各种图像分类数据集和不同分类任务上均取得更好精度。

与 CLIP 相比，SuperClass 在使用相同数据集的训练参数设置下，图像分类精度也基本优于 CLIP 模型，比如 ImageNet linear probing 分类，SuperClass 比 CLIP 高 1.1% (85.0 vs. 83.9) 。考虑到 SuperClass 无需文本编码器和构建大规模 Batch Size ，使其更加适合应用于大模型预训练场景。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/IrH3BAPESuiaChY7fIFz5ibVONanUiaZqaOrBJQfEltyRU2Fsd0Xlyq3YRPtUhtHsWOSibZfLypWqBquXoZhuibTtWw/640?wx_fmt=png&from=appmsg)

* **更好的跨模态能力**

CLIP 广泛应用的另一个场景是多模态理解，作为多模态大模型中的视觉编码器，展现了很好的跨模态能力。在预训练过程中，SuperClass 的特征也对齐到了文本空间，同样可应用于多模态理解任务中。

本文采用了 2 种大语言模型，按照 clipcap 中的设置，使用 GPT-2 作为 Decoder ，在 COCO captions 上评估 image captioning 能力。根据表 3 的结果所示，SuperClass 取得了略优于 CLIP 的 CIDEr 结果。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/IrH3BAPESuiaChY7fIFz5ibVONanUiaZqaO7OSrLW71hp67wQhOWVq7qTtXILYoJD1GHFg9PnVUvO8OYolsrx72Fg/640?wx_fmt=png&from=appmsg)

另外按照 LLaVA 的设置，使用 7B 的 LLM 评估了更多的多模态下游任务，同样 SuperClass 也取得了更好的精度。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/IrH3BAPESuiaChY7fIFz5ibVONanUiaZqaO88iaCv1djweiaicHevHHk8uBNb5QLLQWMHgy4fApP0TZ93EnxCSD5yZIw/640?wx_fmt=png&from=appmsg)

更多实验配置和测试细节请移步完整论文（https://arxiv.org/abs/2411.03313）。

* **更好的可扩展性 Scalability**

团队对比了 SuperClass 和 CLIP 在不同的模型大小和不同的数据规模下的精度，包括纯视觉任务和多模态下游任务：

1. 在纯视觉任务和多模态下游任务上，SuperClass 和 CLIP 具有相似的 Scalability ；
2. 在 Text-VQA 任务上，SuperClass 明显取得了比 CLIP 更好的精度和 Scalability ，团队推测，SuperClass 训练可能可以学习到更强的 OCR 能力。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/IrH3BAPESuiaChY7fIFz5ibVONanUiaZqaOicTl6UluicOPtSLlILMq1SC0HxQ2sQF6B5GxzmqBbjzUmOLUmV9aiafeA/640?wx_fmt=png&from=appmsg)

**4. 展望未来**

团队会继续推进图像文本预训练技术迭代，基于文本顺序信息，训练得到更强视觉模型，以便更好地服务于视觉和多模态相关的任务。如果你对该团队研究工作感兴趣，有志于探索视觉大模型前沿课题，可点击阅读原文，前往豆包大模型团队官网，了解更多信息。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/IrH3BAPESugP4pgV3m4sm7iaL5YQKnwzVgzXsgicVupQ16FZVjotMEEWqjAnxM635ibmJrVpYDJMWT8H2KUQ1612w/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/IrH3BAPESugqoE1HDUrgFyNJHTtZic4BAXrjqdmWGZlSEmmcUq0MGKC4xHTj9oBwhmhfkn83eBSFa48f3bibicib1A/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/IrH3BAPESuiaChY7fIFz5ibVONanUiaZqaOARESicheZtvF4Ak4O04EFqJr6CzNFsibnVHpibAic965DAlgOsK9q9y0HA/640?wx_fmt=png&from=appmsg)](http://mp.weixin.qq.com/s?__biz=MzkzMDY5MzYxNg==&mid=2247484993&idx=1&sn=10b3b6e1261b957de9391c72e7c401bc&chksm=c2772edef500a7c8c42314050204d2bbe2a45f2d22a37f8eaabdc65f9090f8a696610ce89e14&scene=21#wechat_redirect)[![](https://mmbiz.qpic.cn/sz_mmbiz_png/IrH3BAPESuiafFqdsHqjHdUVVYf78m4wXNbPuZXfMDlYj9oH7nZdaN70n5jTGHSMKjvibgkzuz31aiaCsyPOhLXBQ/640?wx_fmt=other&from=...
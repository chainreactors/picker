---
title: 基于微调CLIP的多模态大模型安全防御
url: https://forum.butian.net/share/4289
source: 奇安信攻防社区
date: 2025-04-30
fetch_date: 2025-10-06T22:02:51.565223
---

# 基于微调CLIP的多模态大模型安全防御

#

[问答](https://forum.butian.net/questions)

*发起*

* [提问](https://forum.butian.net/question/create)
* [文章](https://forum.butian.net/share/create)

[攻防](https://forum.butian.net/community)
[活动](https://forum.butian.net/movable)

Toggle navigation

* [首页 (current)](https://forum.butian.net)
* [问答](https://forum.butian.net/questions)
* [商城](https://forum.butian.net/shop)
* [实战攻防技术](https://forum.butian.net/community)
* [漏洞分析与复现](https://forum.butian.net/articles)
  NEW
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### 基于微调CLIP的多模态大模型安全防御

* [漏洞分析](https://forum.butian.net/topic/48)

大模型在各种任务上都有广泛的应用，但是从其本质来说，扩大模型规模意味着需要增加训练数据的数量和多样性，这就需要从网络上抓取数十亿条数据，这个过程是无需人工监督的。
那么这也就会带来隐患，因为其中可能会有很多不适当的、有害的内容。
尽管现在模型的开发者普遍采用了过滤器和自动检查，但这种做法仍然会引入一些不适当的内容，最终导致模型产生不安全、有偏见或有毒的行为。

前言
==
大模型在各种任务上都有广泛的应用，但是从其本质来说，扩大模型规模意味着需要增加训练数据的数量和多样性，这就需要从网络上抓取数十亿条数据，这个过程是无需人工监督的。
那么这也就会带来隐患，因为其中可能会有很多不适当的、有害的内容。
尽管现在模型的开发者普遍采用了过滤器和自动检查，但这种做法仍然会引入一些不适当的内容，最终导致模型产生不安全、有偏见或有毒的行为。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-cd29d8db9bda594a983a0726458503d69c6cb060.png)
这种情况也出现在基于嵌入空间的多模态大模型中，有毒内容可能会嵌入到潜在空间中。
例如，当使用一个“不适合工作场合”（NSFW）的文本提示进行跨模态任务时，其嵌入可能会到达潜在空间中的不安全点，从而导致生成不想要的图像，或者检索到不适当的内容。同样，在图像到文本生成中，如果使用不适当的图像作为提示，生成的描述性文本可能会有毒或冒犯性。下图就是例子。左上角就是执行多模态任务的时候基于文本检索出了错误的图像，右上角则是给定文本生成了NSFW图像。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-1f5f251a7f41fa9b6aaaaab292496f1c5bac2259.png)
所以，现在一个很重要的领域就是要提升预训练多模态模型的安全性。
那么这就离不开CLIP。
CLIP原理
======
CLIP（Contrastive Language–Image Pretraining）是OpenAI在2021年提出的一种多模态模型，它通过联合训练图像与文本，使得模型能够理解自然语言与图像之间的对应关系。它的核心思想是将图像和文本映射到同一个语义空间，这样模型就能直接比较图像和文本的相似度，实现“用文字理解图片”或者“用图片理解文字”。
CLIP主要由两个部分组成：
1）图像编码器：一般使用ResNet或ViT（Vision Transformer）对图像进行编码，提取视觉特征向量
2）文本编码器：一般使用Transformer对自然语言文本进行编码，提取语义特征向量
这两个编码器分别将图像和文本编码成相同维度的向量，便于后续比较。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-dd05a9191accb216101d284c494da09be501aadd.png)
训练过程中，CLIP使用了大规模图文对（如图像及其对应的描述）来进行对比学习：
给定一组图像与一组文本（batch），
模型计算图像和文本向量之间的余弦相似度，
最大化匹配图文对的相似度，最小化非匹配对的相似度。
换句话说，CLIP试图让正确图文对的向量靠得更近，错误配对的距离更远。
这种训练方式使模型不仅学会了图像和文本之间的语义联系，还具备了零样本学习（zeroshot learning）的能力。CLIP的提出代表了多模态学习的一大飞跃，它让图像“读懂”文字，也让文字“看懂”图像。通过共享语义空间，CLIP实现了高度灵活和通用的图文理解能力，为许多人工智能任务提供了基础模块。
大致想法
====
有了这些背景知识，如果我们可以使类似CLIP的嵌入空间变得更安全，使其对不适当输入具有不变性那就可以确保多模态大模型的安全。我们只需要减少类似CLIP的嵌入空间中的不适当概念就行。它具有更广泛的影响和适用性，因为类似CLIP的模型被用于许多不同的应用，包括跨模态检索、文本到图像和图像到文本生成，以及作为不同任务的特征提取器。
我们的初步思路就是微调嵌入空间，以避免表示不适当的内容，同时不改变其正常的表达能力。我们可以通过结合多种损失函数来实现这一点，这些损失函数旨在将不适当的内容重定向到安全的嵌入区域，同时尽可能保持嵌入空间的结构。
经过我们微调的CLIP安全版本可以应用于跨模态检索、文本到图像和图像到文本生成。例如，如果我们要求微调后的CLIP检索与带有NSFW内容的文本提示相对应的图像，它将找到一个语义相似但内容适当的图像。此外，基于我们微调后的CLIP的Stable Diffusion模型将生成一个适当内容的图像，没有暴力、裸露或其他有毒方面，同时保持输入提示的安全语义。同样，基于我们的安全CLIP的多模态LLM（如LLaVA）将生成一个没有不适当内容的文本描述。这个想法非常的巧妙，具体发表在计算机视觉顶会ECCV上，名为SafeCLIP: Removing NSFW Concepts from VisionandLanguage Models，这也是本文的核心。
方法原理
====
之前我们已经说过类似 CLIP 的模型是用从网络上抓取的数据训练的，而这些数据可能包含不适当的内容。因此，要让这些模型变得更安全，要么需要从头开始用大规模清理过的数据重新训练，要么通过某种监督方式对它们进行微调，以减少不适当的知识。
第一种方法需要大规模清理数据，而目前这种方法在实践中并不有效，所以我们采用了第二种策略。具体来说，我们专注于让 CLIP 的文本编码器和视觉编码器都变得更安全。
理想情况下，我们希望安全版本的 CLIP 文本编码器能够忽略输入句子中的不适当内容，并理解其大部分干净的内容。同样地，我们希望安全版本的 CLIP 视觉编码器能够忽略输入图像中的不适当内容。此外，我们还希望尽可能保留嵌入空间在安全文本或视觉区域附近的原始结构，以便安全编码器可以直接连接到基于它们构建的下游模型，而无需进一步适配。
从数学上来说，假设有一个不安全的句子
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-09baf5521cca9ee85020aee613de759b426bd3a5.png)
和一个“清理”函数
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-83cca8b3e06ed0c8e6ec99b080ec642bc6a9103e.png)
该函数可以移除句子中的所有不适当内容，那么我们希望我们的安全文本编码器 T 相对于原始的预训练 CLIP 文本编码器 T0，满足以下条件
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-ff0bef41b62c7c3a9fbdc56c41178ab8c8c6958f.png)
这里用 ≈ 表示在嵌入空间中高度相似。可以看到，公式中的第一个条件确保了不适当内容被忽略，而第二个条件则确保安全的 CLIP 文本编码器能够正确编码输入句子的干净部分。同时，这也确保了 T 可以无缝连接到基于 T0训练的下游模型（例如，对于 CLIP ViTL/14，下游模型可能是 Stable Diffusion v1.4）。对于视觉编码器也有同样的要求：给定一个不安全的图像
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-44c1ce0e36eb92afb5d90eb11b70038412636bce.png)
和一个视觉“清理”函数
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-6a417fd6fd4e3ce70b53235dbdd4fb09e87e1f78.png)
我们要求：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-c94f11669950fc777c6a2547549725a86401c7f6.png)
其中 V 是安全的视觉编码器，V0是原始的 CLIP 视觉编码器
数据集
---
为了修改 CLIP 以避免表示不适当的内容，我们的方法需要一个包含安全和不安全（即 NSFW）图像及句子四元组的数据集，记作
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-14e27dd892dc64faf9b1e4854bc14cb113756cbc.png)
其中vi表示安全图像，ti是其对应的句子，而不安全图像 vi\\*和不安全句子 ti∗是与它们安全对应物“配对”的，以传达相似的语义含义。
例如，t i可以被视为 t i∗的净化版本，表达相似的含义但不含不适当的概念，视觉部分也是如此。由于这样的数据集并不存在，我们通过自动标注程序构建 D，它可以做到1）从干净的句子 ti自动生成不安全句子 t i∗；2） 从不安全句子 ti∗生成不安全图像 v i∗
​
训练NSFW文本生成器
-----------
为了实现第一个目标，可以对一个大语言模型进行微调，使其能够从安全句子生成不安全句子。为此比如可以使用100 对手动策划的安全不安全句子对，这些句子对是手动编写和通过 Vicuna自动生成的句子的混合。为了确保数据集能够提供适当的监督，我们遵循其他工作中对 NSFW 内容的定义，将其归为以下二十个类别：仇恨、骚扰、暴力、痛苦、羞辱、伤害、自杀、色情、裸露、体液、血液、猥亵手势、非法活动、吸毒、盗窃、破坏、武器、虐待、残忍、残暴，并在这些类别之间平衡训练数据集的样本，以鼓励 LLM 生成多样化的不安全内容。
我们首先使用监督微调对 LLM 进行微调，使用一个解释任务的提示模板，然后让模型从 t
i开始生成 t i∗。
这种微调过程可以LLM其转化为一个能够生成 NSFW 内容的生成器，其生成的内容甚至超出了我们在训练集中看到的不适当概念。
对齐NSFW文本生成器
-----------
为了提高生成的不安全句子的质量以及它们与提示的语义相关性，我们采用了一个微调阶段，设计了一种直接偏好优化（DPO）的变体。DPO 最初被提出作为一种替代人类反馈强化学习（RLHF）的方法，它具有更好的稳定性，并且不需要显式训练奖励模型。然而，和 RLHF 一样，DPO 依赖于大规模的人类偏好标注，而我们并没有这些标注。因此，我们构建了一个自动排序程序，用它来替代人类偏好标注，同时提高我们 NSFW 生成器的对齐程度。
具体来说，给定一个安全文本ti，我们通过从 SFT 模型的输出概率分布中采样，得到两个不同的不安全补全
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-97b07176eb002134f792aa38ccee31fa06041f00.png)
然后，我们根据它们的 NSFW 程度和与 t i的语义相似性来对这些补全的质量进行排序。对于第一个标准，我们通过提示 GPT3.5 来对补全进行评估，得到一个二元的 NSFW 评分
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-1513594ad6ec87856154809934e52421298b6ce3.png)
对于第二个标准，我们使用预训练文本编码器预测的 CLIP 相似性来衡量ti和每个补全之间的相似性，这个相似性通过余弦相似性计算，范围在\[1,1\]
最终，给定安全提示 t i，一个不安全补全 t i∗的质量等级计算如下
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-e9420acc8b7fd2eb082cfc98845528584c4e6475.png)
其中 CLIP-Sim(·, ·) 是 CLIP 相似度，NSFWRate(t\\_i\\*) 是前面提到的二进制 NSFW 评级。这个公式综合考虑了文本完成项与安全提示的相似程度以及它是否包含 NSFW 内容。如果一个文本完成项与安全提示相似且不包含 NSFW 内容，它的质量程度会较高；反之，如果不相似或包含 NSFW 内容，质量程度会较低
总的来说， SFT 和偏好优化流程将 Llama 2Chat 转化为一个强大的 NSFW 文本内容生成器，它不仅能够完美地保持与安全输入句子的语义相关性，还能支持多样化的提示，这些提示与训练时看到的不同。
有了 NSFW 生成器，我们就可以从安全且视觉相关的句子开始生成 NSFW 文本。从 NSFW 句子出发，我们再利用一个在 NSFW 内容上训练过的基于扩散模型的生成器来生成对应的 NSFW 图像 v i∗。最后就可以构造出数据集。
我们将数据集分为训练集、验证集和测试集。为了确保生成的数据集在二十个 NSFW 类别之间保持平衡，我们会提示 NSFW 生成器，要求它在安全句子中注入一个特定的、随机选择的类别。
训练CLIP
------
在构建了一个包含安全和不安全图像及句子四元组
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-d87d33518a482f91a396006c6e85ce540985a816.png)
的数据集之后，我们通过一个程序来使 CLIP 模型变得更加安全，该程序确保满足公式中表达的条件。为此，我们采用了一种多模态训练方案，包含四个损失函数。具体来说，我们定义了两个不适当内容重定向损失，旨在教导模型忽略输入文本或输入图像中的不安全内容，以及两个结构保持损失，旨在维持嵌入空间在安全区域的原始结构。
T 和 V 将分别表示正在微调的文本编码器和视觉编码器，而 T 0和 V 0是在微调开始之前获得的文本和视觉编码器的冻结“深度副本”。
为了教导模型忽略不适当的内容，我们建议在数据集中强制要求不安全句子 t i∗与对应的图像 vi之间以及不安全图像 v i∗与对应的文本 t i之间存在跨模态相似性。值得注意的是，这种相似性在 T 0和 V 0中是无法保证的，而 T 0和 V 0之间原本就具有良好的度量学习属性，即在安全的 t i和 v i之间表现良好。
为了进一步加强这种效果，我们还要求不安全句子 t i∗的嵌入与对应的干净句子 t i的嵌入在冻结的文本编码器下匹配，不安全图像 v i∗的嵌入与对应的干净图像 v i的嵌入在冻结的视觉编码器下匹配。我们通过一个余弦相似性项来实现这一点，该相似性项仅考虑正样本对，而忽略与负样本之间的距离。
形式化
---
给定一批图像
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-1a4459cffeba4a655812f2a27694121bad4e5e6d.png)
和它们对应的干净文本
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-b78e18868f22780478e6fa3dca2dcb74885258a4.png)
不安全文本
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-c8637289b666882a9bb9cfed225e0f7bbf976f8f.png)
以及不安全图像
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-f08e5013035fe1203a82aa124c24bf5969ecd35e.png)
我们定义了两个NxN的矩阵，分别包含 T ∗与 V 之间以及 V ∗与 T 之间的成对余弦相似性。然后，我们采用对称的 InfoNCE 损失，该损失旨在最大化 N 对匹配的跨模态安全和不安全嵌入之间的余弦相似性，并最小化 N ^2−N 对非匹配对之间的相似性。在这个过程中，其中一个编码器被冻结，而另一个则进行微调。
![image.png](https://cd...
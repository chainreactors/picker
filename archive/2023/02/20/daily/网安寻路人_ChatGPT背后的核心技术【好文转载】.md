---
title: ChatGPT背后的核心技术【好文转载】
url: https://mp.weixin.qq.com/s?__biz=MzIxODM0NDU4MQ==&mid=2247499104&idx=1&sn=c65ee739966ef5eaa307aa3d4fcad333&chksm=97e9408aa09ec99c49648d0e8cff4c10c4464ae52624c42d8a0631ffa4dd23ae33aeb2b2d626&scene=58&subscene=0#rd
source: 网安寻路人
date: 2023-02-20
fetch_date: 2025-10-04T07:33:40.119624
---

# ChatGPT背后的核心技术【好文转载】

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/jErr674f9micdEnOAibmEQFiaXpSEFJmSgOc4jCcgib0cJy5VIGnlqZuiacMt0EfagScpq4OTCJIbJQVmh9GFPzQhdA/0?wx_fmt=jpeg)

# ChatGPT背后的核心技术【好文转载】

James Pei

网安寻路人

**编者按**

关于LLMs（大型语言模型）的风险和监管，本公号发布过以下文章：

1. [ChatGPT是网络上的一个模糊的JPEG文件（外专观点）](http://mp.weixin.qq.com/s?__biz=MzIxODM0NDU4MQ==&mid=2247499037&idx=1&sn=edf919c148180dbce5fab395d737cb90&chksm=97e940f7a09ec9e1e5f9c62de2ba580d3e35c5d5a5c093c07b7dea83425d4fa6aeee24ca3c0f&scene=21#wechat_redirect)
2. [ChatGPT是如何劫持民主进程（外专观点）](http://mp.weixin.qq.com/s?__biz=MzIxODM0NDU4MQ==&mid=2247499047&idx=1&sn=d03eecb21b9ebc57280cb2f07fc467a3&chksm=97e940cda09ec9db66b84ad7178bd7e9a52a2e71cb238e3b91ae495eb55acc94aaafd311d95c&scene=21#wechat_redirect)
3. [ChatGPT：欧洲禁止Replika "虚拟伴侣"聊天机器人应用（外媒编译）](http://mp.weixin.qq.com/s?__biz=MzIxODM0NDU4MQ==&mid=2247499054&idx=1&sn=b53342145b2eaacdee56a017294201aa&chksm=97e940c4a09ec9d297cf8792919a347b9e119ab8e32c9fd89f2dd1083370f519faed22ce8c17&scene=21#wechat_redirect)

今天和大家分享的是从公众号【分布式实验室】那转载的一篇技术性的文章：【[找到了一篇介绍ChatGPT核心技术的论文](http://mp.weixin.qq.com/s?__biz=Mzg5Mjc3MjIyMA==&mid=2247558679&idx=1&sn=9b00caf5caeeee24c6a6e0d33ed8b1b5&chksm=c03aac04f74d2512d5309f6cca5499773edacebb162b018da33ed9c80d1064d0596e0994eab7&scene=21#wechat_redirect)】。公号君觉得是一篇好文，非常有助于我们理解LLMs背后的技术逻辑。

*—****1*** *—*

**缘起**

输入几个简单的关键词，AI能帮你生成一篇短篇小说甚至是专业论文。作为上知天文下知地理对话语言模型，最近大火的ChatGPT在邮件撰写、视频脚本、文本翻译、代码编写等任务上强大表现，让埃隆·马斯克都声称感受到了AI的“危险”。

最近大火的ChatGPT的计算逻辑来自于一个算法名字叫Transformer。它来源于2017年的一篇科研论文《Attention is all your need》。本来这篇论文是聚焦在自然语言处理领域，但由于其出色的解释性和计算性能开始广泛地使用在AI各个领域，成为最近几年最流行的AI算法模型，无论是这篇论文还是Transformer模型，都是当今AI科技发展的一个缩影。

这也是我想在这里给大家分析这篇文章的核心要点和主要创新的初衷。

但我非AI（数学，计算机）专业，只是梳理并分享自己学习的体会和思考，与大家一起讨论，欢迎各位多提宝贵意见；所述并不专业，各位大牛可以绕行。

从Transformer提出到“大规模预训练模型”GPT（Generative Pre-Training）的诞生，再到GPT2的迭代标志Open AI成为营利性公司，以及GPT3和ChatGPT的“出圈”；再看产业界，第四范式涉及到多个重要领域比如生物医疗，智能制造纷纷有以Transformer落地的技术产生。在这个浪潮下，我的思考是：

一是，未来很长一段时间在智能化领域，我们都将经历“科研、算力、基础架构、工程、数据、解决方案”这个循环的快速迭代；流动性、创新性短期不会稳定下来，而是会越来越强。

我们很难等到科技封装好，把这些知识全部屏蔽掉，再去打磨产品。未来在竞争中获胜的，将是很好地“解决了产品化和科研及工程创新之间平衡”的团队。我们一般理解的研发实际上是工程，但AI的实践科学属性需要团队更好的接纳这种“流动性”。因此对所有从业者或者感兴趣智能化的小伙伴了解全栈知识成了一个刚需。

二是，通过对这篇论文的探讨，可以更直观地理解：在科研端发生了什么，以什么样的速度和节奏发生；哪些是里程碑？是科学界的梅西横空出世，带我们发现真理；哪些是微创新？可能方向明确了，但还有很多空间可以拓展；哪些更像炼金术？仍然在摸索，尚需要很长一段时间，或者一直会保持这个状态。

三是，在AI领域，由于技术原因，更多的论文是开源代码的，一方面，促进了更多人参与进来改进迭代；另一方面，科研跟工程实现无缝连接，一篇论文可以拉动从核心代码到平台，到具体应用很大范围的价值扩散。一篇论文很可能就是一个领域，一条赛道，甚至直接驱动业务价值和客户价值的大幅提升。

四是， AI技术发展有很多领域（感知，认知，感知又分图像、语音、文字等，认知也可以分出很多层次），之前这些领域的算法逻辑存在很大差别，Transformer的出现有一定程度上推动各个领域汇聚的迹象，介绍清楚这篇文章，对把握整体，可能有些作用。另外ChatGPT属于现象级应用，大家更有直观感受，未来这类应用的体验提升和更新速度只会更快，理解了其背后的逻辑，更有助于我们把握这个趋势。

*—****2*** *—*

**论文介绍**

下面步入正题，开始介绍这篇论文，会涉及一些技术细节及公式，可能还需要仔细看一下，相信一旦看进去，你会对AI的理解加深很多。

**总体把握**

这篇论文的结构非常精炼，提出问题，分析问题，解决问题，给出测试数据。顶刊文章讲究言简意赅，有描述，有代码，有结果；其中最核心的是以下这张图，作者团队提出Transformer的核心算法结构：

![](https://mmbiz.qpic.cn/mmbiz_jpg/vHicVZXtcAzCHu1muhF0Klu6lLHaSmJclUbOvTicpGAvAAM3lYEYT8mKLtPibxggQRSD2kdbo8AdVGpV7bynhBhOw/640?wx_fmt=jpeg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

整篇文章就是围绕这张图来进行解释的，由于篇幅所限，我们聚焦在一条主线上：1、文章想解决主要问题是什么；2、如何解决的；3、从文章提出的解决方案作为一个案例来引发整体思考，因此我们将内容简化，主要关注核心部分。

![](https://mmbiz.qpic.cn/mmbiz_jpg/vHicVZXtcAzCHu1muhF0Klu6lLHaSmJclziaA3PS2SEzv1CNNb1JSOEru6D5E0ENyk86f5wkcxhPoCShva3QcfjQ/640?wx_fmt=jpeg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

这张图表达的内容如果理解了，那基本上你掌握了这篇论文85%的内容，也是最关键的部分。

《Attention is all your need》在编写时主要是为了考虑NLP任务，是由几个Google的科研人员一起完成的，其中一个背景是Google也在推广自己的并行计算芯片以及AI TensorFlow开发平台。平台主要功能特点是并行计算，这篇文章的算法也是在最大限度的实现并行计算。我们就以一个简单的例子来把这个算法串一遍。

**核心内容**

需求是我们需要训练一个模型，进行中文到英文翻译。

背景知识：这个需求要把“翻译：我爱你 to I love you”转置成一个y=f(x)问题，x代表中文，y是英文，我们要通过训练得到f()，一旦训练成功f()，就可以实现翻译。大家拼的就是谁的训练方法更准确，更高效，谁的f()更好用。

之前自然语言处理主要的算法叫RNN（循环神经网络），它主要的实现逻辑是每个“字”计算之后将结果继承给第二个字。算法的弊病是需要大量的串行计算，效率低。而且当遇到比较长的句子时，前面信息很有可能会被稀释掉，造成模型不准确，也就是对于长句子效果会衰减。这是这篇文章致力于要解决的问题，也就是说这篇文章有训练处更好的f()的方法。联想一下ChatGPT可以做论文，感受一下。

在Transformer里，作者提出了将每个字与句子中所有单词进行计算，算出这个词与每个单词的相关度，从而确定这个词在这个句子里的更准确意义。（这句话要是理解了，后面其实可以不看了。）

在此处，要开始进入一些技术细节，在开始之前，我们有必要再熟悉一下机器学习领域最核心的一个概念——“向量”。在数字化时代，数学运算最小单位往往是自然数字。但在AI时代，这个最小单元变成了向量。这是数字化时代计算和智能化时代最重要的差别之一。

举个例子，比如，在银行，判断一个人的信用额度，我们用一个向量来表示：

![](https://mmbiz.qpic.cn/mmbiz_jpg/vHicVZXtcAzCHu1muhF0Klu6lLHaSmJclMrH4gFMicGpQlDNaWzKTAXf8OiaicBsu2snCgoxzpSLpS0ZVg3I1ET73Q/640?wx_fmt=jpeg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

向量是一组数据的集合，也可以想象成在一个超高维度空间里的一个点。一个具体的信用额度向量，就是在8个特征组成的高维空间的一个点。数据在高维空间将展现更多的数学性质比如线性可分，容易让我们抓住更多隐藏的规律。

向量的加减乘除是计算机在进行样本训练是最主要的计算逻辑。第四范式一直强调的高维，实时，自学习，其中高维就是把企业信息拉升到一个非常高维的空间，变成向量。

Transformer模型的主要意义就是找到了一个算法，分成三步把一个词逐步定位到了一个高维空间，在这个过程中赋予这个单词比其它算法更优的信息。很多情况下这个高维空间有着不同的意义，一旦这个向量赋予的信息更准确更接近真实情况，后面的机器学习工作就很容易展开。还拿刚才信用额度向量举例子：

![](https://mmbiz.qpic.cn/mmbiz_jpg/vHicVZXtcAzCHu1muhF0Klu6lLHaSmJclSicYibLVnHS6pbJEQBIRZ1XJAOJibckj9RcIjbAxjibpbibhav0ibc6eo8RA/640?wx_fmt=jpeg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

![](https://mmbiz.qpic.cn/mmbiz_jpg/vHicVZXtcAzCHu1muhF0Klu6lLHaSmJclicDFdica4lp5xiaorTXBnSeLRiaGmzJTLoRHzwyhr5VW2eECO4K0CqUD5w/640?wx_fmt=jpeg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

这两个向量存在于两个不同的向量空间，主要的区别就是前者多了一个向量特征：“年薪”。可以思考一下如果判断一个人的信用额度，“年薪”是不是一个很重要的影响因子？

以上例子还是很简单的，只是增加了一个特征值，在Transformer里就复杂很多，它是要把多个向量信息通过矩阵加减乘除综合计算，从而赋予一个向量新的含义。

好，理解了向量的重要性，我们看回Transformer的三步走，这三步走分别是：1、编码（Embedding）；2、定位（Positional encoding）；3、自注意力机制（Self-Attention），这个真的大名鼎鼎。

举个例子，比如，翻译句子Smart John is singing到中文。

首先，要对句子每个词进行向量化。

我们先看“John”这个词，需要先把“John”这个字母排列的表达转换成一个512维度的向量John，这样计算机可以开始认识它。说明John是在这个512维空间的一个点；这是第一步：编码（Embedding）。

再次，第二步，定位（Positional encoding）。利用以下公式（这是这篇文章的创新）：

![](https://mmbiz.qpic.cn/mmbiz_jpg/vHicVZXtcAzCHu1muhF0Klu6lLHaSmJcl2csPZwQ5hM0rGia0KfNwKEriaAs89EAd2eIBicicaDgS9N0L2US3IRnFdA/640?wx_fmt=jpeg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

微调一个新的高维空间，生成一个新的向量：

![](https://mmbiz.qpic.cn/mmbiz_jpg/vHicVZXtcAzCHu1muhF0Klu6lLHaSmJclKXvlchq9QHwf910RbNNFkgbOC5ZxnKsv3dGTHJb71QicBEdbCT7sWpA/640?wx_fmt=jpeg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

我们不用太担心这个公式，它核心意义是：在这个新的向量里面每一位由原来的0和1表示，分别取代成由sin和cos表示，这个目的是可以通过sin和cos的定律，让这个新向量不仅表示John这个单词的意义，还可以表示John在Smart John is singing这个句子的位置信息。

如果不理解，可以直接忽略，只要记住第二步是用来在“表达John这个词的向量”中，加入了John在句子中的位置信息。John已经不是一个孤立的词，而是一个具体句子中的一个词，虽然还不知道句子中其他词是什么含义。

如果第一步计算机理解了什么是John，第二步计算机理解了“\* John\*\*”。

最后，第三步，自注意力机制（Self-Attention），通过一个Attention（Q，K，V）算法，再次把John放到一个新的空间信息里，我们设为：

![](https://mmbiz.qpic.cn/mmbiz_jpg/vHicVZXtcAzCHu1muhF0Klu6lLHaSmJclppy4LyntMoUmFLFNqqIebSQgiaUlszRNGhFdJpXOk25BnJIxNzRF9WA/640?wx_fmt=jpeg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

在这个新向量里，不仅包含了John的含义，John在句子中位置信息，更包含了John和句子中每个单子含义之间的关系和价值信息。我们可以理解，John作为一个词是一个泛指，但Smart John就具体了很多，singing的Smart John就又近了一步。而且Attention （Q，K，V）算法，不是对一个单词周围做计算，是让这个单词跟句子里所有单词做计算。通过计算调整这个单词在空间里的位置。

这种方法，可以在一个超长句子中发挥优势，而且最关键的是一举突破了时序序列的屏障，以前对于图像和NLP算法的划分，很大程度上是由于NLP有很明显的时序特征，即每个单词和下一个以及在下一个有比较明显的时序关系。但Transformer这种算法打破了这种束缚，它更在意一个单词跟句子中每个单词的价值权重。这是Transformer可以用到everywhere的主要原因。

![](https://mmbiz.qpic.cn/mmbiz_png/vHicVZXtcAzCHu1muhF0Klu6lLHaSmJclXuNxLfngdOX2VZsKEdze1T2iamENVu7NTzH0YVy8r5WUwgnjIxJgQiaw/640?wx_fmt=png&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

**计算过程**

如果不感兴趣，可以跳过这一部分介绍，直接进入启发收获部分。

具体的计算过程，用翻译句子“我爱你”到“I love you”举例（这句更简单一些）。首先进行向量化并吸收句子位置信息，得到一个句子的初始向量组。

![](https://mmbiz.qpic.cn/mmbiz_jpg/vHicVZXtcAzCHu1muhF0Klu6lLHaSmJclwdPBBXG4mibwU2gWtJzxjmic2fNHBOp0ICFkqgx2IdYVQkWySvJFOH2A/640?wx_fmt=jpeg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

由于样本每个句子长短不同，所以每个句子都会是一个512\*512的矩阵，如果长度不够就用0来代替。这样在训练时，无论多长的句子，都可以用一个同样规模的矩阵来表示。当然512是超参，可以在训练前调整大小。

接着，用每个字的初始向量分别乘以三个随机初始的矩阵WQ，Wk，Wv 分别得到三个量Qx，Kx，Vx。下图以“我”举例。

![](https://mmbiz.qpic.cn/mmbiz_jpg/vHicVZXtcAzCHu1muhF0Klu6lLHaSmJcl222v1bKnwxH30K7SeicuQq69pab9puOm7GJY0JPtkCf2gbiaib40EcNXA/640?wx_fmt=jpeg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

然后，计算每个单词的attention数值，比如“我”字的attention值就是用“我”字的Q我分别乘以句子中其他单词的K值，两个矩阵相乘的数学含义就是衡量两个矩阵的相似度。然后通过一个SoftMax转换（大家不用担心如何计算），计算出它跟每个单词的权重，这个权重比例所有加在一起要等于1。再用每个权重乘以相对应的V值。所有乘积相加得到这个Attention值。

![](https://mmbiz.qpic.cn/mmbiz_jpg/vHicVZXtcAzCHu1muhF0Klu6lLHaSmJcl219y68jGcqP8OmsC2zYnSLdEvroGEQiap5g0xibRl5fE6466rp4zbpjQ/640?wx_fmt=jpeg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

这个attention数值就是除了“我”字自有信息和位置信息以外，成功的得到了这个句子中每个单词的相关度信息。

...
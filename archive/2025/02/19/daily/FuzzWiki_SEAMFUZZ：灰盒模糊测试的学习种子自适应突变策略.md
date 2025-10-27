---
title: SEAMFUZZ：灰盒模糊测试的学习种子自适应突变策略
url: https://mp.weixin.qq.com/s?__biz=MzU1NTEzODc3MQ==&mid=2247486942&idx=1&sn=d249d0aa9047c41d34cb0da0cb74053b&chksm=fbd9a662ccae2f741e774425250e2a2894e7b3796ce123e69795798288442b9c5d04647a4069&scene=58&subscene=0#rd
source: FuzzWiki
date: 2025-02-19
fetch_date: 2025-10-06T20:48:08.656942
---

# SEAMFUZZ：灰盒模糊测试的学习种子自适应突变策略

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/JchE46RGRlonXc2PJn7iazXQXITW1AIhw7bqIurUIibhDibKT8VoqJqpvcUtt5Dh9safL1ShJbibrlyblNPOw64ZEA/0?wx_fmt=jpeg)

# SEAMFUZZ：灰盒模糊测试的学习种子自适应突变策略

原创

FuzzWiki

FuzzWiki

![](https://mmbiz.qpic.cn/mmbiz_gif/JchE46RGRlr92CPaC2cSiaTUCEWwOd0OucLNLlY09jGCso4gTL4BmXsBNsvOlSMv9qPopLaecg7r21KD4gBERqA/640?wx_fmt=gif)

**基本信息**

**原文名称：**Learning Seed-Adaptive Mutation Strategies for Greybox Fuzzing

**原文作者：**Myungho Lee；Sooyoung Cha；Hakjoo Oh

**原文链接：**https://ieeexplore.ieee.org/abstract

/document/10172576

**发表期刊：**International Conference on Software Engineering，2023

**开源代码：**https://github.com/kupl/SeamFuzz-public

**一、概述**

本文提出了一种名为SEAMFUZZ的灰盒模糊测试工具，旨在通过学习种子自适应变异策略来提高模糊测试的性能。模糊测试的有效性在很大程度上依赖于变异策略，而现有的程序自适应策略往往无法充分考虑种子输入的不同特性，从而限制了测试的深度和漏洞发现能力。

为了解决这一问题，SEAMFUZZ通过聚类技术将种子输入根据其句法、语义（和稀有性）的相似性分组，并为每个种子组学习优化的变异策略。SEAMFUZZ的主要创新点在于其种子自适应变异策略，不同于传统的程序自适应技术，SEAMFUZZ能够自动捕捉和利用每个种子输入的特性而应用不同的变异策略。这一方法通过定制的汤普森采样算法，有效地学习并应用于各个种子组，从而提高了模糊测试的覆盖率和崩溃输入生成能力。

**二、介绍**

AFL可以为任何类型的测试程序在合理的时间内（例如，在3天生成的96 亿个测试用例）生成大量测试用例。然而，由于其固有的随机性，生成有意义的测试用例的效率较低，从而导致未探索的程序位置。

为了提高基于突变的模糊器的效率和性能，程序自适应方法，特别是MOPT 已经成为一种趋势方法，旨在控制选择与目标程序相关的突变方法的概率分布。然而，他们仅针对测试程序调整突变策略，错过了利用不同种子输入的不同特征的机会，忽略了每个种子输入的独特性。由于不同种子输入具有不同的句法和语义特性，采用统一的变异策略可能无法充分挖掘每个种子的潜力，从而限制了模糊测试的深度和漏洞发现能力。

SEAMFUZZ包含两个关键组件：种子聚类（Seed Cluster）：将种子输入聚类成具有相似特征的种子组；概率学习器（Probability Learner）：为每个种子组学习并应用不同的变异策略。这种方法旨在捕捉每个种子输入的独特性，并为其应用最合适的变异策略，从而提高模糊测试的覆盖率和漏洞发现能力。

![](https://mmbiz.qpic.cn/mmbiz_png/JchE46RGRlonXc2PJn7iazXQXITW1AIhwnXaaLOL4VtTxuzz3PSDCN7tXEZ7FRKXwvDibTagF4W60dJicrmeaQrMQ/640?wx_fmt=png&from=appmsg)

**图 1  SEAMFUZZ工作流**

**三、技术分析**

![](https://mmbiz.qpic.cn/mmbiz_png/JchE46RGRlonXc2PJn7iazXQXITW1AIhwaoxv2dv3YyoQbBA4HjVmribHfYngYib3zNN7QNkmZb1v0XnnY2lpcAdQ/640?wx_fmt=png&from=appmsg)

**图 2  SEAMFUZZ整体算法**

整体算法中的第7行，CLUSTER函数识别所选种子输入s所属的种子组，并返回相应的组g - 五元组(sid,S,Pid,Dg,Db)。

在采样变异方法生成测试用例之前，在第11行中确定是遵循已学习的概率 Pid（利用）还是随机概率 Pr（探索）。由于利用和探索之间的平衡对性能影响很大，作者通过反复试验将利用和探索的概率分别设定为70%和30%（即第11行的ε值为0.7）。

整体算法中的第14行，在每次测试用例执行中，积累有用的数据，这些数据稍后在第15行的LEARN函数中用于更新优化种子组g的概率分布Pid。通过CLUSTER和LEARN之间的迭代交互，能够学习采样概率，以选择针对种子组优化的有用变异方法。

**1．种子聚类**

**（Seed Cluster）**

给定一个种子输入s和一组种子组G，种子集群的目标是将选定的种子输入 s聚类到具有相似特征的适当种子组中。为了实现这一目标，定义了相似度分数scoresim和函数CLUSTER。相似度得分表示种子输入与种子组的接近程度，CLUSTER函数根据分数将种子输入分组到种子组中。相似度分数由句法、语义和稀有性相似度计算得出。

1. 语义相似度

描述种子输入和种子组覆盖的执行路径的相似性；覆盖执行路径越相同，它们就越相似。通过计算单个种子组中种子输入覆盖的所有执行路径的集合Covall (S)来定义种子组的一般语义行为。Cov(s)表示种子输入s覆盖的路径集。

![](https://mmbiz.qpic.cn/mmbiz_png/JchE46RGRlonXc2PJn7iazXQXITW1AIhwF5cogibknR8aupo6rBZ46y7yJhFw8vVYOYbBicAMribpnP8U9Q3q149JA/640?wx_fmt=png&from=appmsg)

语义相似度的计算方式为：

![](https://mmbiz.qpic.cn/mmbiz_png/JchE46RGRlonXc2PJn7iazXQXITW1AIhwmXdPOibIGSaHFM8akyq1ApibhnrqHp5BvEtezuNty7yQ2qicqgq9paJoQ/640?wx_fmt=png&from=appmsg)

For example:

![](https://mmbiz.qpic.cn/mmbiz_png/JchE46RGRlonXc2PJn7iazXQXITW1AIhw74pSVZBWia5C3BfH1eZNE8eWKWbUkCe4qQ69bKfD9hUspH5tXrLW8Xw/640?wx_fmt=png&from=appmsg)

大写字母表示每个独特的路径。由于两组共有两条路径（A和B），而Covall(S)的大小为 8，所以语义相似度Simsem (s,g)为0.25。

2. 句法相似度

将种子输入s视为大小为N位(s∈{0,1}N)的位字符串，并为种子组的句法特征定义一个具有代表性的种子输入sid。代表性种子输入是集合S中最多到达那些很少覆盖的路径(Covrare)的种子输入。

给定两个大小为N的种子输入s和sid，计算句法相似度Simsyn(s,g)如下：

![](https://mmbiz.qpic.cn/mmbiz_png/JchE46RGRlonXc2PJn7iazXQXITW1AIhwmicic8iaYXDp5ZDokSdz7KQMdePyibb3ZiczXichoDTs7LBUF9CjVVLPNiaag/640?wx_fmt=png&from=appmsg)

其中μ(s,sid)是两个种子输入中具有相同值的第i位位置的集合，s[i]表示种子输入s的第i位的值。

For example:

![](https://mmbiz.qpic.cn/mmbiz_png/JchE46RGRlonXc2PJn7iazXQXITW1AIhw7xRWicrIhadUJs2JUlEEYQQKia17qssM4WaXXRxdED9b5YOiaqcZoBmlw/640?wx_fmt=png&from=appmsg)

其中粗体位表示同一位置的不同值。所以s和s'之间的句法相似度为 0.7，因为只有三个位不同，而N的值为10。

两个种子输入之间的句法相似度Simsyn表示两个种子输入中相同位置的位值相同的数量与种子输入中位总数的比率。如果两个种子输入的长度不同，较短种子与较长种子之间差的那些位都算作是不同对应位值的位，N的值为较长种子输入的大小。

3. 稀有性相似度

稀有性相似度是基于这样的期望，即从很少被探索的路径开始的突变很可能导致未被探索的更深的程序位置。因此，当种子输入覆盖了种子组所覆盖的不经常探索的路径时，计算一个如下的稀有度分数。

![](https://mmbiz.qpic.cn/mmbiz_png/JchE46RGRlonXc2PJn7iazXQXITW1AIhw5RfG776o8aLEFe7YCrmhrAP2gAiaMHKSbLVWQZTNiby3978TqSpVlia7Q/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/JchE46RGRlonXc2PJn7iazXQXITW1AIhwgcWGvwPPo5u3MRuypJ5CGyH0miaJZNzAgyzlLUIcf00Xib52VibiahGIww/640?wx_fmt=png&from=appmsg)

其中hit(path)表示路径的命中计数。

4. 相似度得分

在获得三个不同的相似度（即语义、句法和稀有性）后，CLUSTER计算种子输入和每个种子组之间的相似度得分（scoresim），并确定给定种子输入将属于哪个种子组。形式上，CLUSTER函数定义为：

![](https://mmbiz.qpic.cn/mmbiz_png/JchE46RGRlonXc2PJn7iazXQXITW1AIhwibCriatKOEetkthcydBINOlBMxDgYMMlBSnml1ycmBpYRbNxcVLPq2xA/640?wx_fmt=png&from=appmsg)

其中dmax表示所有计算相似度分数中最高的一个，argmax函数返回得分dmax的种子组。使用以下方程获得相似度分数scoresim ：

![](https://mmbiz.qpic.cn/mmbiz_png/JchE46RGRlonXc2PJn7iazXQXITW1AIhw5qNw2Va4HNtxjKcfibqdEfHGUrNfdOcCU3LJFA0ffxjkHOpT8d4CdXg/640?wx_fmt=png&from=appmsg)

CLUSTER函数计算种子输入s和每个种子组之间的相似度得分，并在最高相似度分数dmax超过γ的值时返回具有更新种子输入集的种子组。如果不属于任何现有种子组的种子输入s（即dmax小于γ的值），CLUSTER函数通过使用种子输入s作为代表性种子来初始化一个新的种子组。在这种情况下，将Pid初始化为均匀分布(Pr)，因为新生成的组不存在学习的概率分布；所有组概率分布Pid 都以哑行为（即随机概率）开始，并且随着学习的进行变得更加智能。

**2．概率学习器**

**（probability learner）**

它学习为每个种子组选择有效突变方法的概率分布。

1. 采样空间

首先定义一个选择变异方法m的取样空间，m方法指定变异位置(loc)和变异方式(op)。直观上，如何变异直接与通常预定义的变异操作符相关，因此选择变异操作符的取样空间可以很容易地确定。然而，变异位置是未固定的，由种子输入的大小决定，而这些大小是多样的，这使得定义选择变异位置的特定取样空间变得困难。

通过值p对种子输入的长度进行划分，并使loc的取样空间大小为 p，而不论种子输入的大小如何。通过划分空间，可以将选择变异位置(loc)的取样空间从未定义的大小减少到具体确定的大小(p)。一旦变异策略选择了某个变异分区，它就会在选定的分区内随机选择变异位置。

例如，假设p的值为10，作者在实验中也使用了这个值。给定一个大小为 40 比特的种子输入，每个分区的大小就为4比特（40 / 10 = 4）。如果按照学习到的概率分布选择了第4个分区，种子变异器将随机选择第4个分区中的第13到第16比特作为变异位置。

2. 汤普森采样

为了学习哪些变异方法能够带来更好的性能，首先注意到，问题自然可以表示为多臂老虎机问题（Multi-Armed Bandit，MAB）。

MAB问题假设有N个老虎机，其目标是从中获得最大化的奖励。在每一轮中，选择一个老虎机进行操作，并根据为每个老虎机设定的概率分布来获得奖励。

直观上，在问题设置中，每个老虎机对应于每个变异操作符op和变异分区p。在模糊测试技术中，奖励对应于发现新的路径或新的崩溃输入。

现在，目标变成了找到最有利可图的老虎机（即有效的变异方法）以实现最大化奖励，其中第k个老虎机有成功获取奖励的概率θk。

为了实现这一目标，作者采用了汤普森采样算法，这是经典MAB问题的知名解决方案。汤普森采样从观察到的奖励中建立一个概率模型，并从对应的模型中对每个老虎机的期望值进行采样，以选择下一轮的老虎机。

直观上，对于某个特定老虎机，观察到的奖励越多，在下一轮选择该老虎机的可能性就越大，因为期望值会在所有老虎机中最高。如果某个老虎机的成功概率较低，随着数据的增多，选择该老虎机的概率会降低。

基于汤普森抽样，定义选择第i个变异算子的概率如下:

![](https://mmbiz.qpic.cn/mmbiz_png/JchE46RGRlonXc2PJn7iazXQXITW1AIhw20alrjXfoMvcDUbyBv3AFXKicYb9rqOoY7Ov5kd5AdQ40CoGt1RtSQg/640?wx_fmt=png&from=appmsg)

θiop表示从Beta分布中采样的第i个变异算子的预期奖励。

|Vop|表示用于突变生成的变异算子的数量。

Vgop[i]表示生成成功测试用例时选择第i个变异算子的次数。

Vbop[i]表示生成失败测试用例时选择第i个变异算子的次数。

用同样的方法得到选择突变分区Pp的概率分布

成功测试用例：interesting or s’覆盖了Covrare中至少一个路径。

失败测试用例：不成功的同时s’覆盖了Covcommon中超过80%的路径。

为每个路径维护一个命中计数表。当程序pgm使用生成的测试用例执行时，此命中计数表都会更新。使用这个命中计数信息按升序排列，建立了前10%和后30%的两个集合Covrare和Covcommon。

基于上述分类标准，更新学习数据Dg和Db。主要地，学习数据D是两个向量的对，分别是变异操作符数据（Vop）和变异分区数据（Vp）。每个向量的第i个元素分别表示第i个变异操作符和分区被选择的次数。基于学习数据D，Dg是用于积累在生成成功测试用例时使用的变异方法次数的良好学习数据，而 Db 则用于失败测试用例。例如，假设 Covrare 、Covcommon 和两个种子输入（s1和s2）的覆盖路径如下：

![](https://mmbiz.qpic.cn/mmbiz_png/JchE46RGRlonXc2PJn7iazXQXITW1AIhw0NZpmicicgxQ2jyM247MyPwKumsT5q0IZGaCynKXqA9nNMtthgX2N0cg/640?wx_fmt=png&from=appmsg)

将Covtotal定义为迄今为止覆盖的路径集合。在这个例子中，s1和s2都不是有趣的测试用例，因为它们未能覆盖新的路径。然而，s1被认为是一个成功测试用例，因为它满足第一个额外条件，用生成s1时使用的变异方法来更新良好学习数据 Dg。对于s2，由于它既不是成功测试用例，也不满足是失败测试用例，既不更新 Dg也不更新Db。

**四****、实验**

作者在AFL++的基础上实现了SEAMFUZZ，并将其与AFL++和AFL++ MOPT进行了比较。作者评估的三个模糊测试工具均基于AFL++的3.15a版本。为了减轻模糊测试技术固有随机性的影响，作者对每个基准程序进行了20次24小时试验，并报告了平均结果。

所有实验都在运行Ubuntu 20.04、具有64个CPU和256GB内存的机器上完成，该机器配备了AMD Ryzen Threadripper 3990X 64核处理器。

![](https://mmbiz.qpic.cn/mmbiz_png/JchE46RGRlonXc2PJn7iazXQXITW1AIhwQPVTxw1hpjQL3tpO82SnUGMdjxwvFBk6QNpO98kBoYmw2fW8VRFsiaA/640?wx_fmt=png&from=appmsg)

图 3 测试基准程序

**实验1：14个程序上覆盖率和crash对比**

![](https://mmbiz.qpic.cn/mmbiz_png/JchE46RGRlonXc2PJn7iazXQXITW1AIhwYafyYAj8MDU4CniabmzmbiaicenDaPEJmescgyEfG6MCMtaymGVAMgqmA/640?wx_fmt=png&from=appmsg)

**图 4 20次试验在14个程序上24小时的平均结果**

SEAMFUZZ平均比AFL++和AFL++ MOPT多覆盖了5.6%和7.7%的边。SEAMFUZZ生成的崩溃输入比AFL++和AFL++ MOPT分别多56.4%和57.1%。对于某些程序（例如，openssl），SEAMFUZZ和AFL++ MOPT相对于AFL++ 的性能提升较小。作者调查了这些情况，发现这些基准程序上的边覆盖数量趋于每个模糊测试工具达到的最大性能。例如，在openssl程序上，所有模糊测试工具在3小时内都达到了5,800个边，剩下的18小时内的覆盖增益不到1%。

**实验2：独特bug数量**

![](https://mmbiz.qpic.cn/mmbiz_png/JchE46RGRlonXc2PJn7iazXQXITW1AIhwGY5WVdvfq1BGGX4Hd9sDRO8jtGCukrCZeibZxLtoDrPvicNcuOJ7fVaQ/640?wx_fmt=png&from=appmsg)

**图 5 每个工具发现的独特bug数量的维恩图**

此外，SEAMFUZZ即使在边覆盖率仅有小幅增加的情况下，也能生成显著更多的崩溃输入。例如，在php-parser上，SEAMFUZZ生成的崩溃输入比AFL++ 多233.3%，而边覆盖数量的增益仅为0.4%。
...
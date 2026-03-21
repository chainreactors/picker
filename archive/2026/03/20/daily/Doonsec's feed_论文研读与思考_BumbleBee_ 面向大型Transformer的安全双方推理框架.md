---
title: 论文研读与思考|BumbleBee: 面向大型Transformer的安全双方推理框架
url: https://mp.weixin.qq.com/s/AnnxQSaNbK3GUkCCTAYR_A
source: Doonsec's feed
date: 2026-03-20
fetch_date: 2026-03-21T03:58:53.796556
---

# 论文研读与思考|BumbleBee: 面向大型Transformer的安全双方推理框架

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/q6TQOF8qUIypRC6STFsfH3Fm5jSohBXPHglrRDZp3CJjpqaY9z2IwHq96MIXRngBRPTARImfddn4lgLicYdT5qPrNqmfYgsslZec0QXoL8b4/0?wx_fmt=jpeg)

# 论文研读与思考|BumbleBee: 面向大型Transformer的安全双方推理框架

Jiale
Jiale

玄枢战队-Arcane Hub

![]()

在小说阅读器中沉浸阅读

在云端使用大模型时，隐私如何保障？发表于NDSS 2025上面的文章《BumbleBee:Secure Two-party Inference Framework for Large Transformers》通过压缩与激活函数优化等技术，实现模型的数据安全。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/q6TQOF8qUIzukMv6S12yPoVuYJ5icPm5cmeuY43PoSCMjquz5VsKWboe9ukiaMJM800t3GYzgp2rM25zWJx1COpvWzHya8IOZU0aVt4eiaPh2k/640?wx_fmt=png&from=appmsg)

开源：https://github.com/AntCPLab/OpenBumbleBee

# 一、研究背景与动机

1.1研究背景

基于大型Transformer的模型，如BERT、GPT和ViT已经在许多任务上实现了最先进的性能，包括人员重新识别、语音助手和代码自动完成等。随着Transformer处理越来越多敏感的数据和任务，隐私已成为模型部署过程中的主要问题之一。本文重点研究在双方场景下的私密推理，其中一方持有私密输入，另一方持有模型。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/q6TQOF8qUIzzS0oLyvC38NLmfPcYlZ22jOyk2ciaJw9fuShMj6d43LdQJ2J66Uw1qThew1iaNbk9W1R09SKFYbrMsiaNO9RiayEDFJNQ7zjGzFQ/640?wx_fmt=png)

Private inference旨在保护模型权重免受用户影响，同时保证服务器不会了解有关用户私人输入的信息。

1.2研究动机

目前许多研究引入了基于MPC的密码框架，以实现深度学习模型（例如CNN和基于Transformer的模型）的私有推理。虽然2PC可以在几分钟内高效地完成卷积神经网络（CNN）的推理，但基于Transformer模型的私密推理却带来了新的挑战，尤其是在通信开销方面。例如对一个12层BERT模型进行一次私密推理可能需要高达90GB的通信量。下表指出对一个12层ViT模型进行一次私密推理可能需要交换约262GB的消息。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/q6TQOF8qUIweB8VKgXQNHLp1JJ74bZy6kiaV1tNsrNuS6Eibpzjr42qjTkiaMr0p4BTxq4CGib2MxRcWMAibHxw5Q1W8KPalLQZm4etic4UCT0eTk/640?wx_fmt=png)

因此，高速带宽至关重要，但是Transformer模型的Private inference的快速且通信友好的2PC框架所面临两大挑战。

（1）大规模矩阵乘法。基于Transformer的模型推理可能涉及数百次大型矩阵乘法。大多数现有的用于私有矩阵乘法的加密协议依赖于不经意传输（OT）或同态加密（HE）。然而，这两种方法都有其局限性。基于OT的私有矩阵乘法方法计算时间较短，但需要传输大量消息。基于HE的方法计算量显著增加，但比OT方法更便于通信。如何开发一种既快速又便于通信的矩阵乘法协议是一种挑战.

（2）更复杂的激活函数。与CNN中使用的简单ReLU激活函数不同，Transformer模型包含softmax、高斯误差线性单元（GeLU）和Sigmoid线性单元（SiLU）等复杂的激活函数。这些激活函数的计算需要用到指数运算、除法运算和双曲运算等基本函数。虽然已经开发了针对这些基本函数的特定协议，但直接在Transformer模型中使用它们仍然不切实际。主要原因是Transformer模型中的激活函数数量极其庞大。例如，对GPT2模型进行一次推理需要评估大约3.9 × 10⁶个逐点GeLU。如何为这些复杂的激活函数设计高效的2PC协议也是一种挑战.

# 二、主要贡献

本文提出了BumbleBee一个快速且通信友好的2PC私密Transformer推理框架。贡献主要体现在三个方面：首先，提出了优化的矩阵乘法协议，与现有技术相比，显著降低了80%至90%的通信成本。其次，开发了一种构建高效协议的方法，对Transformer模型中非线性激活函数进行优化，与之前方法相比，本次优化显著提高了处理速度，同时显著降低了80%至95%的通信成本。最后，对五个Transformer模型进行了广泛的基准测试，BumbleBee通过评估LLaMA-7B模型展示了其性能，实验结果进一步表明，BumbleBee的性能比Iron (NeurIPS 22)高出一个数量级以上，比BOLT(S&P 24)快三倍，而通信量仅为BOLT (S&P 24)的十分之一。

## 2.1 高效矩阵乘法协议（OLT）

提出了一种名为不经意线性变换（OLT）的原语。OLT被描述为一个双边协议，它分别从通信双方获取两个私有矩阵Q和V，并生成它们之间的共享矩阵。利用OLT可以在模2l的环上实现两个加性共享矩阵的乘法运算。基于HE的方法的一个显著局限性在于其巨大的通信开销，这是由于输出密文的“稀疏”格式造成的，具体地说，每个输出密文都加密了一个长向量，然而乘法结果只需要向量中一小部分元素。解密仍然需要传输整个加密向量。为了克服这一不足，提出了一种压缩方法，通过同态化将加密向量中不必要的元素置零，从而将多个“稀疏”向量合并成一个“稠密”向量。由于需要发送的密文数量减少，通信量也随之降低。与之前的密文压缩方法相比，本文的压缩方法速度提升了约50倍，通信成本降低了80%至90%。除了矩阵乘法之外，逐点乘法也是Transformer推理中的重要计算。许多基于HE的逐点乘法协议需要设置相对较大的明文模数t。本文提出了一种模数提升函数，用于统一底层HE的秘密共享模数和明文模数。该提升函数使得可以对HE密文执行模2l的算术运算，这允许选择更小的HE参数，即 t ≈ 2²l。实验结果表明，将该提升函数应用于后，性能提升了1.3倍。

## 2.2 激活函数优化框架

本文提出了一种构建高效且精确的Transformer激活函数协议的框架。首先，提出了一个用于构建高效且精确的2PC协议的通用框架以处理许多Transformer模型中使用的激活函数。这些激活函数具有一个共同的特性：它们在原点附近的一个短区间内相对平滑，而在区间两侧则近似线性。基于这一特性，本文使用一个或两个低阶多项式来逼近短区间内的激活函数，并在区间两侧使用恒等函数。如下图所示使用两个低阶多项式P(x)和Q(x)来逼近SiLU，以最小化最小二乘误差。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/q6TQOF8qUIxib025lMVVziaSKplSdZxVXTQ1iae9wDk0Gh8ktxSBdwW4iaIz1W1tPU7FcEDD0tUqxr9GNoMrHDsA2R4CKT09Cn9banFIwic6vKuk/640?wx_fmt=png)

然后，本文利用激活函数的平滑性来提高效率，但是带来的代价是有轻微的误差。其次引入优化方案来提高在同一输入点上评估多个多项式时的摊销效率，与现有数值方法相比，本文优化的激活协议速度提高了9到20倍，通信量减少了80%到95%。

## 2.3 实现并开源BumbleBee框架

BumbleBee支持易于使用的Private inference。目前的方法仅考虑了BERT系列模型。为了进行比较，本文利用Hugging Face网站上提供的模型权重和Python程序，成功在5个预训练的Transformer模型上运行了BumbleBee，包括BERT-base、BERT-large、GPT2-base、LLaMA-7B和ViT-base。本文还评估了BumbleBee在四个公共数据集上的准确性，所有的实验都是使用本文的协议进行的，不是通过模拟。

# 三、核心技术细节

本文使用的相关函数：

|  |  |
| --- | --- |
| SIMD编码 | 将长度为N的向量编码为环上的多项式，使得多项式乘法对应向量的逐点乘法 |
| Lift函数 | 将Z2l中的元素放大并近似映射到Zt |
| Dawn函数 | 将Zt中的元素缩小并取整回Z2l |
| RLWE函数 | 使用公钥pk加密多项式，支持同态加法和乘法（明文模t，密文模q） |
| FH2A | 将 RLWE 密文安全地转换为两个算术共享，同时隐藏密文噪声（电路隐私） |

## 3.1 安全矩阵乘法优化（OLT）

不经意线性变换（OLT）的原语来实现这两种类型的矩阵乘法。

共享矩阵与明文矩阵的乘法：对于每个Transformer块，通过计算共享输入矩阵与服务器的明文权重矩阵的乘积，需要一次OLT，服务器将W以明文形式提供给协议，客户端贡献[X]，结果[XW]返回双方；注意力机制内部两个秘密共享矩阵的乘法：需要两次OLT分别计算[Q]0\*[K]1、[Q]1\*[K]0再将结果本地相加。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/q6TQOF8qUIxYcvG87POiczl0298JHkxG96ABDDaunesXRk7qt8NAR2EjBNpRINkeibT6Pr4C1t94AJbQfmjgDImzw5u6IPnFKf0p8XV1oHapM/640?wx_fmt=png)

服务器（S）：持有完整的Transformer模型权重（包括Embedding表、各层的权重矩阵等）。

客户端（C）：持有私密输入，如一段文本或一张图像。

输入编码：客户端将输入（如token ID）转换为秘密共享形式，发送给服务器。模型逐层计算：双方通过一系列安全协议，协同完成Embedding层、多头注意力、层归一化、前馈网络（Feed‑Forward）。输出：最终得到推理结果的秘密共享，可选择性让客户端或双方获知。图中所有虚线箭头都代表流动的是秘密共享值，即每个中间结果都以[\*]的形式在双方之间传递，任何一方都无法单独还原明文信息。

## 3.2 批量点乘协议（OLE协议）

除了矩阵乘法之外，Transformer 模型中还需要标量乘法，使用Batch OLE (bOLE) 来描述一种双边计算协议，该协议接收来自发送方S的向量x和来自接收方R的向量y，并生成它们Hadamard积的秘密份额。如下图所示，算法是bOLE with Error协议，用于在两方之间高效的计算两个向量的Hadamard乘积的秘密共享，并允许结果存在1bit的LSB误差。

![](https://mmbiz.qpic.cn/mmbiz_png/q6TQOF8qUIzz0z6QugxBibMIayNxr9LGcY5bQq9sDSQLK7Ne09abKicOpc7WquJxfmW24YTAiaiaq8sHw2QylZ4xz01409krkiapB9CYkFpCHWuc/640?wx_fmt=png)

如上图算法所示，主要思想是BumbleBee使用“放大-加密乘-缩小”流程，通过允许微小误差换取更快的速度和更少的通信。发送方通过预处理与加密将生成的密文发送给R，R接收到后利用同态乘法计算，双方调用FH2A功能，将密文安全的转换为两个算术共享，最后双方分别对各自的多项式共享进行SIMD解码得到向量，得到的向量应用于Dawn函数，得到最终共享并输出。其中Lift函数的取整操作引入的舍入误差，以及FH2A内部可能添加的随机掩码，共同导致最终结果与精确乘积存在±1的偏差。然而，该误差出现在LSB层面，而后续的截断协议在定点数计算中会自动将其消除，因此不影响模型推理的数值精度。

## 3.3 激活函数协议优化

GeLU函数因其包含tanh和三次项，在2PC中计算代价极高。BumbleBee采用“分段多项式近似”作为框架进行优化。先用低次分段多项式将非线性函数转化为线性运算的组合，然后通过近似比较和批处理OT降低分支判断的开销，再通过平方复用和混合位宽减少核心计算的通信量，最后利用函数本身的平滑性和负值特性，接受可控范围内的微小误差，从而换取整体性能的大幅提升。

在Algorithm 3算法中，输入值x的秘密共享以及预先定义的分段多项式系数，输出分段近似结果的秘密共享。主要通过四步骤：幂次计算，通过平方协议和乘法协议计算 x2、x3、x4、x6的秘密共享，利用平方协议仅需普通乘法一半的通信开销，且复用已计算的x2提升效率。多项式求值，分别计算三次多项式和六次多项式的值，并加上微小常数以匹配分段定义，所有运算在秘密共享域上进行，并通过截断协议维持定点数精度。分支选择，通过私密比较协议计算输入x与阈值的比较结果，进而组合出三个区间选择位。最后通过结果聚合，利用复用器功能根据选择位选出对应区间的结果，并本地求和得到最终输出的秘密共享。

![](https://mmbiz.qpic.cn/mmbiz_png/q6TQOF8qUIxCkA3FBZibiaX8x73CfYlx3QorlqbGaGrYLEz8ODOkH23pHibKWCSoGH4o6dsXGN6XhqpynRoz6UmnIzLgwZctzHibiaSh9uQAEBp0/640?wx_fmt=png)

如下图所示，图中两条曲线重合，在区间内部无法区分差异，说明分段多项式近似能够高精度地替代原始GeLU，在分段点如x=−1.97、x=−1.97 和 x=3x=3附近，两条曲线平滑连接，没有明显跳变表明即使分支判断略有误差，结果也不会剧烈偏离，由于函数在区间两端近似线性，可以安全地用线性函数替代，从而避免在两端进行复杂多项式求值。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/q6TQOF8qUIxicPZhl3QHdeJIMkQd9Hc8tb3JibNLxPD93u27FO1VB8NWwhxu2Ribg3iaiaRFFKOYvr01LOPAqBNOUVgtNrv0ssF9ZcpGic0eHBV0s/640?wx_fmt=png)

# 四、实验评估

## 4.1 实验设置

模型和数据集，本文在5个Transformer模型上评估BumbleBee，包括四个NLP模型，即BERT-base、BERT-large、GPT2-base和LLaMA-7B，以及计算机视觉模型ViT-base。使用了4个公开数据集：GLUE基准中的CoLA、RTE、QNLI（用于NLP任务）以及ImageNet-1k用于图像分类任务。

## 4.2 实验结果

 Iron、BOLT和CipherGPT是为Transformer设计的2PC推理框架。这三个框架都大量重用了SiRNN框架中基于OT的协议来评估激活函数。BOLT被认为是安全两方变压器推理的最先进技术。BumbleBee的性能优于BOLT，特别是在通信效率方面。BumbleBee相对于BOLT的优势主要原因总结如下：

![](https://mmbiz.qpic.cn/mmbiz_png/q6TQOF8qUIxmos4CANkTenfb2ykYqoeqUKSElTWNsapHHXYDE3LeA0aRwQDgC9S6TElbeOlJ46Wn6TnicgfdTlO60p3OHG3eGwTo01tZic46I/640?wx_fmt=png)

4.2.1 微基准测试

在下表中将所提出的协议与当前最先进协议 (SOTA) 在运行时间和通信成本方面的比较，实验表明本文的协议显着降低了通信成本，GeLU节省了约89%的通信成本，softmax节省了约80%的通信成本

![](https://mmbiz.qpic.cn/mmbiz_png/q6TQOF8qUIyviaL2ThiaUO4X6Iic6ZSy0uKd6bPsE4LvaFpaDChUlCsTbicDWrNTQhSpf18zu2ia59BqwKp79dibDDS2dngbdLtuCiaZjnp4ZMQaQY/640?wx_fmt=png)

4.2.2 大型Transformers评估

在五种Transformer模型上运行了BumbleBee，其中包括四种NLP模型（BERT-base、BERT-large、GPT2-base 和 LLaMA-7B）和一种视觉Transformer（ViT-base），为了证明 BumbleBee的有效性在四个数据集上对BERT-base和ViT-base模型进行了私有推理。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/q6TQOF8qUIy4rCIGuAic1LatWV8Y5AccSVtQq3H4CkkHRH4796IEzhlMfJVOMB4r5jTx2B9LtUqTLxn5XIIrawgV5MLcmpa0stibWSrUCaiaBo/640?wx_fmt=png)

如表所示，与明文预测相比，BumbleBee达到了相当的准确度。需要强调的是，我们所有的实验都是使用提议的2PC协议而不是通过明文模拟进行的。此外，本文不进行任何模型微调。下表详细列出了GPT2-base和LLaMA-7B的BumbleBee推理时间和通信。这两个模型的输入分别由128个和8个令牌组成。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/q6TQOF8qUIw1lKXphulz7OlhKYtJAYbZMFicuc8nibtkAsfSX8wrYEhpW6j5TVK2ete4toia2BmALadwX2bNVaibAicWOJLicpwJZlAgLN00NZpnU/640?wx_fmt=png)

4.2.3 与现有框架的比较

我们主要与现有的两个2PC框架进行比较：Iron和BOLT，但是Iron和BOLT都只考虑了基于BERT的变压器模型。对于其他框架，即MPCFormer、PUMA和SIGMA，它们具有与2PC不同的威胁模型，本文列出了它们的性能。

![](https://mmbiz.qpic.cn/mmbiz_png/q6TQOF8qUIznS4RRwAW7kyKewdRaXzic536wfefHpbrQJpibkUOdicOGf4xeoJnLKa7giaUNnh3z2uREfn7WriayEeVaqGISbwRQj1AJRx0qic9Tw/640?wx_fmt=png)

如上表所示与BOLT（...
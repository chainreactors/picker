---
title: 论文研读与思考 | BLB：利用混合CKKS和MPC重塑私有Transformer推理
url: https://mp.weixin.qq.com/s/qtWDWh05I81b3d_GzUk1uA
source: Doonsec's feed
date: 2026-03-14
fetch_date: 2026-03-15T04:27:14.680576
---

# 论文研读与思考 | BLB：利用混合CKKS和MPC重塑私有Transformer推理

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/q6TQOF8qUIyQkLBMYPn77JYjMJwRMrSsuNYqAIJicpdY7CYZwv7w9qZEGxJaGcDw5XL2p5FS7D2L7HRbwuIybYic4qbvZd6SeWib867NudSHqk/0?wx_fmt=jpeg)

# 论文研读与思考 | BLB：利用混合CKKS和MPC重塑私有Transformer推理

Jiale
Jiale

玄枢战队-Arcane Hub

![]()

在小说阅读器中沉浸阅读

随着人工智能技术的广泛部署，像ChatGPT这样的语言模型已深度融入医疗咨询、金融分析等敏感领域。用户在与这些服务交互时，不可避免地会暴露个人隐私数据。如何在保障模型服务可用性的同时，防止服务提供方窥探用户输入，成为隐私计算领域亟待解决的核心问题。发表于USENIX 2025上的论文《Breaking the Layer Barrier: Remodeling Private Transformer Inference with Hybrid CKKS and MPC》提出了一种名为BLB的创新框架，旨在突破Transformer模型（如BERT、GPT等）私有推理的效率瓶颈，为高精度、低开销的隐私保护推理提供了新的解决方案。

![](https://mmbiz.qpic.cn/mmbiz_png/q6TQOF8qUIydZzEb38ibe1NznzIp5LYgrxODSR4vydWicady6ZNlNHK13MhAAdpTwjgyRkXoPicQKDuqpyBJjfGBqBR8BKgLKqKJw5aPowboG0/640?wx_fmt=png)

一、研究背景

论文Iron**（****NeurIPS 2022****）、BOLT(S&P 2024)、BumbleBee(NDSS 2025)**和BLB(USENIX 2025)都是关于隐私保护的Transformer推理，且都采用了混合HE与MPC的框架。它们的目标是相同的：在保护用户输入数据和服务器模型参数的前提下，高效地完成Transformer模型的推理。下表分别从4篇文章从各个维度介绍关于隐私保护的Transformer推理相关技术发展。

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | **Iron****（****NeurIPS 2022****）** | **BOLT (S&P 2024)** | **BumbleBee (NDSS 2025)** | **BLB ( USENIX 2025)** |
| 创新 | 将混合HE/MPC框架系统性的应用于transformer，为矩阵乘法和复杂非线性函数提供若干新的安全协议。 | 在Iron基础上引入BSGS减少密文旋转；用高阶多项式精确近似。 | 提出了更高效的矩阵乘法和非线性函数协议。 | **系统架构重构**：提出“打破层边界”的细粒度算子融合”。 |
| 针对问题 | Transform模型尺寸大、矩阵乘法维度高、非线性函数复杂，现有cnn方案直接扩展效率极低。 | 矩阵-矩阵乘法效率低；非线性函数（GeLU, Softmax）在MPC中开销巨大。 | BOLT等框架的通信开销依然过高；HE与MPC之间的转换仍过于频繁。 | 频繁的**截断操作**和**HE与MPC转换**是通信的主要瓶颈；BFV方案的密文比特宽度在算子融合后增长过快。 |
| HE方案 | BFV | **BFV** | **BFV** | **CKKS** |
| 通信量 | **280 GB** | **59.61 GB** | **6.4 GB** | **3.0 GB** |

目前主流方案采用的是HE和MPC的混合协议，HE负责线性层（如矩阵乘法），MPC负责非线性层（如Softmax、GeLU），但这类方法仍面临巨大的通信开销，成为部署瓶颈。

在论文BOLT(S&P 2024)中针对Transformer结构进行了深度优化的工作。它解决了矩阵-矩阵乘法的打包问题，并引入了BSGS减少旋转，但是通信量依然巨大，其算子融合粒度较粗，且使用BFV方案导致密文膨胀问题在融合时难以处理。在论文Bumblebee (NDSS 2025)中没有改变BOLT的逐层执行的基本架构，仅仅在协议层面做了优化，该论文中提出的矩阵乘法InterLeave算法能高效地将多个稀疏的密文结果压缩成一个稠密的密文，从而大幅降低传输开销，并且利用激活函数，在比较分支时采用“近似比较”，减少了比较次数，同时优化了多项式的计算顺序，多用平方，少用乘法，使得BumbleBee相对于BOLT的通行量降至6GB。

二、研究动机

从Bumblebee (NDSS 2025)中，分析其通信开销可以发现过多的截断操作和频繁的HE与MPC转换这两项合计占到Bumblebee协议总通信量的80%以上。

![](https://mmbiz.qpic.cn/mmbiz_png/q6TQOF8qUIwAgWsTDYEgPM1OE7AcRRBKYye5PeMicrV0PibF9yemUJsejvRFKKjnFGckXpaJictvzUv04uCXeViclibibxtxaVOy5jaLdqERFo6Hk/640?wx_fmt=png)

依据以上存在的问题，BLB(USENIX 2025)框架提出了一个核心思想“打破层壁垒”包含以下三个方面：

2.1 线性算子融合

将**Iron****（****NeurIPS 2022****）、**BOLT(S&P 24)以及Bumblebee (NDSS 25)中的层级别融合细化为算子级别，识别并合并相邻的线性算子，从而减少HE/MPC转换和截断通信。

论文首先将Transformer中的所有操作分为线性算子和非线性算子，对线性算子分为四类，非线性算子分为三类（比较、多路选择、倒数和平方根倒数）。

![](https://mmbiz.qpic.cn/mmbiz_png/q6TQOF8qUIzOTicxsqjTQaDdeTadDyxykA3uptRiaZbIM3qAibdIrQ7Nj12EicuZZEn27gXXGJamfcIicXsbCRG93Uv6KRaL8GSLnSJzIClwIrro/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/q6TQOF8qUIyV1LnPeeBBhFLm3JqQ8dpAX66uk0tr9v1WpyuITQUDSPt3TWMnQ0nlyHibmbahm4khNYc6Bg3DictyTHQMGw4AvlvUgufXnZMcg/640?wx_fmt=png)

为了使不同算子能够无缝融合，所有算子的输入输出必须遵循空间优先打包：即沿着空间维度L的元素连续存放，然后缩减维度D。对于Transformation算子，BOLT等已有协议满足此规则；但对于Expansion和Reduction，现有方法（如NEXUS）采用reduce-first打包，导致打包不一致。因此，论文设计了新的打包算法。

Reduction求和算法：使用旋转加和方法。对于输入密文m（尺寸L×D），通过log2 D次左旋转和累加，将沿D维的求和结果压缩到L维。公式如下：

![](https://mmbiz.qpic.cn/mmbiz_png/q6TQOF8qUIzx6WwQ9TbJCtH85KcFXVqEXcOBhfBN1grWzT17qfPuVZ7jaGIrEPDI345aibzK59VJPiaoicI3dTp5hp47VMRqIro8B2JVbuKTqk/640?wx_fmt=png)

广播算法：类似地，通过右旋转将标量扩展到L×D，当求和与广播相邻时，可以省略中间的掩码和广播步骤，进一步简化。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/q6TQOF8qUIz4vlY7cf2CvVNAYMviaBKGLQwG5Vk1IGAZTgcqs4qqSguHebtFHxHOgSSkjzI9sApnaKdahfcH3g2Iibbfok9M0k3CBEQYia3ZjY/640?wx_fmt=png)

相比NEXUS，该算法仅需log2 D次旋转，且保持输入输出打包一致，如下表所示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/q6TQOF8qUIznOQcJj6XiaUWTyHYTdL3DfdrwSNNRImup7yxcXeW5rzFnKEyNFbZImcX76SLMAiaeECT9GAG4uFUgTyMsymfFgXnhwAFzbiavdI/640?wx_fmt=png)

根据第一个和第二个算子的类型，论文总结了融合后的算子类型及是否需要新打包算法，其中绿色表示融合合法且无需新打包算法；橙色表示融合合法但需要新打包算法；红色表示不会出现的情况，如Reduction+Expansion在Transformer中几乎不存在。

![](https://mmbiz.qpic.cn/mmbiz_png/q6TQOF8qUIzNjZorULXX96avGTicWlBXP1vYkGZXpW0lYVS8BOejqxulOZDyf1fLynibOicP5AflRN4NnPKdpW4wp32Wdg3O60zOnlOR5liaRpY/640?wx_fmt=png)

构建融合计算图，将整个Transformer模型分解为基本算子形成计算图，然后遍历相邻的线性算子，根据下图所示的模式进行融合，合并成更大的线性块。例如，下图展示了一个Transformer块经过FineGrainFusion后形成了5个融合块（不同颜色标记）。这些块内所有线性操作一次性用HE计算，消除了块内部的HE/MPC转换和截断。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/q6TQOF8qUIzuK8yiat9RNxibQgI1P8vvq9ZtpRnQVgBUbshYaQxJaAyqTUomVo7icYVLibcT7Tp5sqqEPCh8UWv9tFicPdwkF1WIibPGI1yzterKc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/q6TQOF8qUIxLPxHCfPmdAR7HDDhicKxuUiclSWr5P2W0pjqfGzic8mVMVLhSRu6CwZLHTlv0a1gBCBQftn0dYAicciaMvDYsr3LGCrTVLaELtVnE/640?wx_fmt=png)

2.2 混合CKKS和MPC安全转换协议

在**Iron****（****NeurIPS 2022****）、**BOLT(S&P 24)以及Bumblebee (NDSS 25)中对于HE方案的选用均采用的是BFV整数算数，但是BFV在计算连续乘法时，规模因子呈指数增长，如图a所示，导致密文位宽急剧增长，需提高多项式阶数以满足安全性，进而造成大量的通信量和计算成本，本文BLB中采用支持rescale操作的CKKS，每次乘法后可通过降低模数将规模因子恢复至原始水平，从而控制位宽线性增长，如图b所示。因此，CKKS更适合融合后的多线性操作。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/q6TQOF8qUIwaVFOrxdn7Daibh8e6r5Tc50odK83uvoicT1Lk4F6qL3tdpIX7EsXUmneZlZvCVeaDcuVt51l7fSumLibAJdnDvQjMMEWL7ph1jw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/q6TQOF8qUIy4ticUh8Oib502DJgeHEb1qYuibUKLachza7aOBusZl92Yoe35H7Pkib98JLShgBMYqacnZVicMwX5BQOPyaufgn31hWvgYgiaMWzCs/640?wx_fmt=png)

本论文中提出了首个安全的CKKS与MPC转换协议，直接使用均匀随机多项式作为掩码。

![](https://mmbiz.qpic.cn/mmbiz_png/q6TQOF8qUIz92bLKrv3wdnAlnhE21ec5OTFadTtmhovrPkhYqIybWFWT85Db83DU495UyFZD7IPCzmCvGh1uaI9iaib7xCu9xzlcjib1guhaFQ/640?wx_fmt=png)

CKKS到MPC转换，服务器均匀随机采样多项式，然后使用同态加法掩盖密文，发送给客户端。客户端解密后得到tmp，双方调用域转换协议将秘密共享切换到环上，因为MPC在环上执行更有效，接着双方在本地执行CKKS解码，得到秘密共享。

![](https://mmbiz.qpic.cn/mmbiz_png/q6TQOF8qUIx4kLZL7zAq2otiarrLOTsAFuH9hmAUPv7EeKIt7O2zWBJKxGL8dQNEicwK9b4byLASkxh0uTm65l27jOIauB0Pxyjwc2MNBN2fc/640?wx_fmt=png)

MPC到CKKS的转换，双方本地执行CKKS编码，调用域转换，客户端加密其份额得到Enc发送给服务器，服务器同态加得到 Enc(Encode(x))。

其中在域转换中：借鉴BOLT/SIRNN的扩展协议，实现到环上的的安全转换。在ring-to-field中，先将共享扩展到更大环，然后模q。

本地解码和截断：解码消耗O(logN)乘法深度，为避免通信，采用概率性本地截断，在扩展环上算术右移后模回原环，确保错误概率可忽略。

2.3 旋转高效融合计算MatMul协议

在CKKS或BFV这类方案中一个密文通常对应一个多项式。为了充分利用空间，我们会把多个数据打包到这个密文的不同slot中。传统的做法是对两个密文进行加法或乘法，相当于对这两个保险箱里对应位置的小盒子进行加或乘，这非常高效，是并行的。但是旋转操作是想要把保险箱里所有小盒子的内容循环移动一下位置，比如把第0个盒子的数据移到第1个盒子，第1个移到第2个，最后一个移到第0个，但是，我们必须在不打开保险箱的前提下完成这个移动。在融合矩阵乘法，特别是密文-密文乘法中，需要做的是减少HE旋转次数，提高效率，从而减少通信开销。在本文中提到，旋转次数是640，延迟1.7秒，在BOLT(S&P 24)中旋转次数是18432，延迟224秒，可以看到BLB方案中有了显著的提高。

![](https://mmbiz.qpic.cn/mmbiz_png/q6TQOF8qUIxGU2AdhY5vjQ0QdiczlbQ8DvsfnhZuaP3aUhd8VVich7o6BQ5BvYlchiaBnKNd9UXbOrU9kyHaa6yJwkx4MS7PIEoyXvfKWN5Xqw/640?wx_fmt=png)

对于矩阵乘法C=A\*B，按列打包A，按行打包B，在该旋转协议中，首先进行预处理对B的每一行进行内旋转，使每行中的元素按t步移位。内旋转通过掩码和旋转实现，需要D次内旋转（每行一次），其次行内旋转与乘法：对每个偏移t，将B的所有行旋转t步，得到L个密文，每个密文与A相乘，得到L个密文，每个包含了不同对角线的部分和。最后对角线旋转与求和：将这L个密文旋转对齐，提取部分和，并累加得到最终C矩阵。

三、实验设置

3.1 硬件与网络环境

CPU：2.7 GHz Intel Xeon Platinum 8558P，64线程。

GPU：NVIDIA A100（用于加速HE计算）。

网络模拟：使用Linux的tc命令模拟四种网络条件，覆盖局域网（LAN）和广域网（WAN）的不同带宽与延迟：

|  |  |  |
| --- | --- | --- |
| 网络类型 | 带宽 | 往返时间RTT（ms） |
| LAN | 1Gbps | 0.3 |
| WAN1 | 400Mbps | 4 |
| WAN2 | 100Mbps | 4 |
| WAN3 | 100Mbps | 80 |

3.2 软件实现

HE库：基于Microsoft SEAL库，使用CKKS方案。

MPC库：基于C++实现，OT采用IKNP和VOLE两种变体。

GPU加速：基于PhantomFHE库。

3.3 模型与数据集

模型：BERT-base、BERT-large、GPT2-base（来自Hugging Face预训练模型，不做任何微调）

数据集：GLUE基准中的四个数据集MRPC、RTE、SST-2、QNLI

输入长度：BERT系列为128 token，GPT2-base为64 token

3.4 对比基线

|  |  |  |
| --- | --- | --- |
| 框架 | 类型 | 核心技术 |
| Iron | 2pc | 基于秘密共享，优化矩阵乘法打包 |
| BOLT | BFV+MPC | 线性层用BFV，非线性层用MPC，支持两层矩阵乘法融合 |
| Bumblebee | BFV+MPC | 引入HE辅助非线性层计算，降低通信 |
| SIGMA | 3PC | 基于函数秘密共享，支持GPT推理 |
| MPCFormer | 3PC | 面向Transformer的3PC框架 |
| NEXUS | FHE | 全同态加密，非线性层用多项式近似 |
| BLB（本文） | CKKS+MPC | 算子级融合+安全转换+旋转高效矩阵乘法 |

3.5 通信开销对比

![](https://mmbiz.qpic.cn/mmbiz_png/q6TQOF8qUIzoJO6XM2DO2awNlgSR6ribb64NCzUyAMKEzvRv7VlMZA8SWiaoiczJvxW1T3dQMZmaibNxrrg5fXlRoCHUIZt5XsiabkVS97s2Jbys/640?wx_fmt=png)

|
|  |

|
|  |

按通信构成（截断、HE/MPC转换、非线性操作等）分解，对比BOLT、Bumblebee和BLB。结果（以BERT-large为例）：BOLT：63.6 GB，Bumblebee：15.2 GB，BLB：7.8 GB。相比BOLT降低8.2倍，相比Bumblebee降低1.9倍。改进主要来自消除截断通信和减少HE/MPC转换。

3.6 CKKS和BFV对比

![](https://mmbiz.qpic.cn/mmbiz_png/q6TQOF8qUIxBpzibeoreP45Td4icst6Vkx4286k0QiafVyVsReUrHLcVN7oKlbWqdJcs8oAydujM2aNyngwQ6ic8G02oEK6e755ujn1gYS9XicP4/640?wx_fmt=png)...
---
title: LLM时代中的AI推理
url: https://blog.csdn.net/ariesjzj/article/details/139693922
source: 世事难料，保持低调
date: 2024-06-16
fetch_date: 2025-10-06T16:54:19.408540
---

# LLM时代中的AI推理

# LLM时代中的AI推理优化

![](https://csdnimg.cn/release/blogv2/dist/pc/img/original.png)

[ariesjzj](https://jinzhuojun.blog.csdn.net "ariesjzj")
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newUpTime2.png)
已于 2024-11-30 16:37:01 修改

![](https://csdnimg.cn/release/blogv2/dist/pc/img/articleReadEyes2.png)
阅读量7.5k
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)
收藏

47

![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)
点赞数
18

CC 4.0 BY-SA版权

文章标签：
[人工智能](https://so.csdn.net/so/search/s.do?q=%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[LLM](https://so.csdn.net/so/search/s.do?q=LLM&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[推理](https://so.csdn.net/so/search/s.do?q=%E6%8E%A8%E7%90%86&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[大模型](https://so.csdn.net/so/search/s.do?q=%E5%A4%A7%E6%A8%A1%E5%9E%8B&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[AI](https://so.csdn.net/so/search/s.do?q=AI&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

于 2024-06-15 11:05:14 首次发布

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

本文链接：<https://blog.csdn.net/jinzhuojun/article/details/139693922>

## 问题与挑战

毫无疑问，AI是当下最热的话题之一，而大模型又是当前AI的主角。几年前，正当深度学习进入瓶颈时，以GPT为首的LLM的横空出世让之似乎又找到了“第二增长曲线”。当模型规模大到一定程度时，它所表现出来的涌现能力（Emergent ability）是之前在小模型中所不曾见过的。这种大模型所特有的推理、计算等能力给我们带来了无穷的想象空间。

但是，它的代价是模型和以往模型相比增大了成百上千倍。要玩大模型十亿参数基本是个入门级门槛，上百亿才算像点样。各个大公司为了争夺大模型的话语权，更是将大模型越“卷”越大。模型规模增大所带来的挑战是多方面的，这里我们主要关注它在计算，尤其是推理时带来的挑战。提高LLM推理性能，降低LLM推理成本是加速其相关应用产品化的必经之路。

具体来说，LLM推理计算的主要挑战来自几个方面：

* 内存用量大：模型参数多，导致模型本身及中间张量的内存使用量增大。就算以FP16存储，模型的大小基本上也是参数量的两倍。一个模型本身动辄占用几十、几百个G，就已经数倍于主流GPU的内存了。再加上推理时其它一些中间张量，及KV Cache等，所需内存往往需要参数本身的几倍。因此，内存就成为了非常严峻的问题，甚至决定了能否跑得起来的关键因素。
* 硬件利用率低：目前主流的LLM推理采用auto-regressive方式。它是一个迭代的过程，每次迭代会产生一个token。其工作范式分为两个阶段：第一个阶段称为Prefill或prompt Processing。它根据给定的prompt计算KV Cache，并产生第一个输出token。第二个阶段称为decoding或token generation。它迭代式地逐个生成token，同时更新KV Cache用于下一次迭代。两者的计算模式有很大不同，前者通常为compute-bound；后者由于arithmetic density较低，通常为memory-bound。它难以并行，导致硬件利用率低。

## 优化技术

业界提出了很多LLM的推理优化技术。本文无法全部覆盖，主要涉及以下几个方面：

* **Attention Optimization**
* **Approximate Attention**
* **KV Cache**
* **Decoding**
* **Batching**
* **Distributed**
* **Offloading**
* **Compression**
* **Others**

### Attention优化

目前主流LLM模型几乎都是基于Transformer架构。该网络架构除了头尾，其它都是Transformer layer（或称为Transformer block）的重复堆叠。Transformer block包含三部分：dense layer projection，self-attention, feed-forward。它们之中，除了self-attention其它其实都是GEMM。GEMM的优化技术被研究了几十年，相对成熟，不用多说。而attention的结构相对更复杂，更难并行，而且naive的实现中内存占用与context长度是平方关系。这使它成为耗时与内存占用的瓶颈，因此是优化的重点。

其中一个优化角度是Sharing-based Attention优化，即修改Attention结构使多个头间共享部分数据。如论文《Fast Transformer Decoding: One Write-Head is All You Need》中提出的MQA（Multi-Query Attention）与论文《GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints》中提出的GQA（Group-Query Attention）。它们被用于在PaLM, StarCoder, LLaMA2等模型中。但由于涉及网络结构本身的改变，这里不作展开。

#### **FlashAttention & FlashAttention2**

FlashAttention系列可能是这几年中关于Attention最重要的优化。论文《FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness》与《FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning》分别提出了FlashAttention（FA）和FlashAttention 2（FA2）。由于出色的性能表现，目前已成为业界的标配。

记Attention的输入为
Q
,
K
,
V
∈
R
N
×
d
\mathbf{Q,K,V} \in \mathbb{R}^{N \times d}
Q,K,V∈RN×d，其计算过程的数学描述为：

S
=
Q
K
T
∈
R
N
×
N
,
P
=
softmax
(
S
)
∈
R
N
×
N
,
O
=
P
V
∈
R
N
×
d
\mathbf{S = QK}^T \in \mathbb{R}^{N \times N}, \quad \mathbf{P} = \text{softmax}(\mathbf{S}) \in \mathbb{R}^{N \times N}, \quad \mathbf{O = PV} \in \mathbb{R}^{N \times d}
S=QKT∈RN×N,P=softmax(S)∈RN×N,O=PV∈RN×d
 其中矩阵相乘
Q
K
T
\mathbf{QK}^T
QKT产生shape为[batch, head num, seq len, seq len]的中间张量，
P
\mathbf{P}
P也一样。而最终需要的
O
\mathbf{O}
O是shape为[batch, head num, seq len, hidden size of one head]的张量。由于seq len一般会很长（现在的模型中支持的seq len越来越长，如GPT-3为2K, LLaMA-2为4K到32K，GPT-4有32k，CodeLlama有100k，Gemini 1.5有1M），因此前者的中间张量会非常大。这也意味着如果按照上面的数学定义来计算，中间张量大概率会把内存撑爆。FlashAttention使用tiling解决了该问题，同时减少了HBM与SRAM的读写。谈到tiling，很多文献是针对GEMM或者Conv这样的算子，但要应用于softmax咋一看会有些棘手，因为它本身包含了reduction的语义。对于这个问题，FlashAttention使用论文《Online normalizer calculation for softmax》中的online softmax技术，从而避免了构建巨大的attention matrix，同时也使得softmax可以被并行（原文3.1节）。该算法使内存的复杂度降低到线性，极大降低了它的memory footprint。另外，它还通过kernel fusion，将attention所有操作融合到一个CUDA kernel中，从而减少了kernel launch与访存的开销。

FlashAttention可达理论FLOPS的25-40%，比标准的attention快2-4倍，节省10-20倍的内存。但是它在thread block与warp的任务切分上还不是最优的，会导致occupancy低下，以及不必要的shared memory读写。另外，近年来context长度越来越长，FA在这方面没有专门的优化。在这样的背景下，FlashAttention 2对它进行了优化，改进了计算任务的划分，提升了并行性，使之能达到理论FLOPS的50~73%，性能提升2倍。它采用的主要技术包括：

* 通过online softmax与casual mask计算的调整，减少了非GEMM运算（由于GEMM计算有Tensor Cores加持，相比而言厚厚GEMM计算虽然FLOPs占比不大，但耗时占比大）
* 除了FA中对于batch与head并行外，还在seq维度上并行，从而提升在长seq length时的性能。
* FA中的split-K scheme需要所有的warps都将中间结果写入shared memory，同步后累加。FA2中变换了切分策略，使得warps间不需要通信，从而减少shared memory读写。

论文《A Case Study in CUDA Kernel Fusion: Implementing FlashAttention-2 on NVIDIA Hopper Architecture using the CUTLASS Library》针对NVIDIA Hopper架构改进了Flash-Attention-2实现。它基于CUTLASS实现，利用了Hopper架构新引入的特性-Tensor Memory Accelerator（TMA）和Warpgroup Matrix-Multiply-Accumulate（WGMMA）指令。通过将TMA copy与WGMMA指令进行overlap，同时选取最优的tile size以平衡寄存器压力与shred memory的使用，相比Ampere架构上的FA 2实现有20-50%的性能提升。

#### **FlashDecoding & FlashDecoding++**

文章["Flash-Decoding for long-context inference"](https://pytorch.org/blog/flash-decoding/)和论文《FlashDecoding++: Faster Large Language Model Inference on GPUs》提出了Flash-Decoding（FD）与FlashDecoding++（FD++），也称为FlashAttention-V3和V4。前面的FA是训练与推理通用的，而FD，就像它的名字一样，是针对推理场景中的decoding的。

Attention的性能瓶颈在于对中间张量
Q
K
T
QK^T
QKT的读和写。前面的FA在batch size与query length维度上做并行。训练阶段由于batch大，容易并行。但推理阶段query length一般是1，同时推理时batch一般还比较小。这意味着如果batch数小于SM数量，就打不满GPU，硬件资源会被浪费。这在长序列时尤为严重，因为序列长一般意味着batch较小。因此，FA的优化不太适用于推理。

FD在FA的基础上，对于长序列推理有8x的提速。它的主要思想将并行化维度扩展到key和value，使得它们可以并行地加载和计算。其代价是最后需要做reduction。其工作流程有三步：1) 将keys/values切成更小的chunk。这一步无需GPU操作。2) 使用FlashAttention并行地为每个split计算query的attention。3) 最后，对所有split的结果做reduction。

FlashDecoding++通过进一步实现了Attention计算的并行，并针对扁平矩阵的乘法进行了优化。它针对LLM推理中存在的三个问题，在FD的基础上做了如下改进：

| 挑战 | 方案 |
| --- | --- |
| Synchronized partial softmax update | Asynchronized softmax with unified max value |
| Computation resources is under-utilized for the flat GEMM operation | Flat GEMM optimization with double buffering |
| The performance of LLM inference suffers from the static dataflow | Heuristic dataflow with hardware resource adaption |

基于这些优化，FlashDecoding++与FlashDeocding相比提速1.37x。

* **Asynchronous Softmax**
   为了数值稳定性，避免溢出，在计算softmax一般会先将数值减去最大值。以往FA中采用partial softmax的方式，将数据切块，分别计算块内softmax。虽然达到了一定程度的并行，但由于依赖于其它的partial结果，因此最后仍需要以同步的方式更新。这种synchronized partial softmax update的方式占到Attention计算的相当比重（Llama2-7B中18.8%）。文中指出LLM中的softmax的输入值域99.99%都在特定区间中，因此可以使用一个统一的值来取代这个最大值，从而避免同步，让这部分计算完全并行起来。如果发生溢出，再用同步的方法进行重计算（recomputation）。
* **Flat GEMM**
   Decode阶段batch size与seq len一般较小，因此GEMM操作中的矩阵比较扁平（即flat GEMM）。当batch size为1时甚至退化成GEMV。另外当prefill阶段的seq len较小时也会产生flat GEMM。这些情况下会导致硬件利用率很低。LLM推理中广泛使用cuBLAS或CUTLASS这样的库利用Tensor Core进行加速。尽管Tensor Core支持GEMM中的M=8，但库中一般会在M维度上将tile size设为64以hide memory latency。但是，decode阶段中GEMM的M常常远小于64，这样会需要padding从而导致浪费。 FD++将矩阵padding到8（而非像之前设计中的64）的倍数以提升利用率。文中指出不同shape的flat GEMM会面临不同的瓶颈（当N较小时是parallelism-bound，N较大时是memory-bound）。FD++在N较大时通过引入double buffering来hide memory latency。即在shared memory中分配两块buffer：一个buffer中的tile执行GEMM操作，另一个块buffer为下一次GEMM操作加载tile。这样，计算与访存就可以overlap。
* **Heuristic Dataflow**
   LLM推理中的GEMM是多样的，可能是GEMV（decode阶段batch size=1的情况），可能是flat GEMM（decode阶段小batch size情况，或是prefill阶段小seq len情况），也可能是传统的GEMM（prefill阶段当batch size与seq len都较大时）。当前的框架（如FasterTransformer，DeeSpeed）使用cuBLAS中的高性能GEMM实现处理不同的worklo...
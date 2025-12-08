---
title: DeepSeek时代的Large-scale LLM推理
url: https://blog.csdn.net/ariesjzj/article/details/155660533
source: 世事难料，保持低调
date: 2025-12-07
fetch_date: 2025-12-08T03:20:58.196057
---

# DeepSeek时代的Large-scale LLM推理

# DeepSeek时代的Large-scale LLM推理

原创
已于 2025-12-07 17:59:08 修改
·
485 阅读

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)

15

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)

11
·

CC 4.0 BY-SA版权

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

文章标签：

[#LLM](https://so.csdn.net/so/search/s.do?q=LLM&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#DeepSeek](https://so.csdn.net/so/search/s.do?q=DeepSeek&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#推理优化](https://so.csdn.net/so/search/s.do?q=%E6%8E%A8%E7%90%86%E4%BC%98%E5%8C%96&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#大模型](https://so.csdn.net/so/search/s.do?q=%E5%A4%A7%E6%A8%A1%E5%9E%8B&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#大规模EP](https://so.csdn.net/so/search/s.do?q=%E5%A4%A7%E8%A7%84%E6%A8%A1EP&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

于 2025-12-07 15:41:58 首次发布

2025年底DeepSeek V3发布炸场，几乎为业界之后的LLM优化方向定了调，尤其是大规模推理优化方面。去年快年底时对LLM的推理优化技术做过一个简单的总结：[《LLM时代中的AI推理优化》](https://blog.csdn.net/jinzhuojun/article/details/139693922?spm=1001.2014.3001.5501)，现在看来已有很多变化。在DeepSeek V3问世快一年之际，这里简单整理总结一下业界与之相关的推理优化技术。

根据官方技术报告《DeepSeek-V3 Technical Report》，DeepSeek V3在网络结构上仍然采用了Transformer架构。Transformer layer中的Attention与FFN部分，分别采用了Multi-Head Latent Attention（MLA）和DeepSeekMoE。简单来说，前者采用了lora技巧减少了KV cache，使MLA的计算在decode阶段也不会memory-bound（可参见《A Deep-Dive Into the New Flash MLA Kernel》），后者采用了fine-grained MoE使得模型可以在推理计算量可控的前提下更好地scale。这两种结构和之前的DeepSeek V2是基本一致的，可参见论文《DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model》和论文《DeepSeekMoE: Towards Ultimate Expert Specialization in Mixture-of-Experts Language Models》。有个差别是在MoE中DeepSeek V3采用了称为auxiliary-loss-free的load balancing策略。另外DeepSeek V3还使用了Multi-Token Prediction（MTP）输出多个token。这个结构在推理中是可选的，如果要用的话可用于投机推理。之后发布的DeepSeek R1与DeepSeek V3在网络结构上一致。

在DeepSeek V3之后业界涌现出了很多新的网络，可以从中一窥业界的发展趋势。

* **Kimi-K2**: 参见《Kimi K2: Open Agentic Intelligence》。网络结构与DeepSeek V3是一样的，区别主要是一些超参（如专家数提高到384，Attention head数降低到64等）的改变，其总参数量提高到了~1T。
* **Qwen3**：参见《Qwen3 Technical Report》。Qwen3分为dense和MoE两类，后者带MoE结构。它的Attention部分采用了GQA，并做了些改动（加了QK-Norm）。和Qwen2.5（参见《Qwen2.5 Technical Report》），一样也采用了DeepSeekMoE中的fine-grained experts。与Qwen2.5不同，MoE中没有shared expert。
* **Ling-1T**：其网络结构基于论文《Towards Greater Leverage: Scaling Laws for Efficient Mixture-of-Experts Language Models》中activation ratio，expert granularity, shared experts ratio等配置参数对于MoE模型有效性影响的研究。Attention模块采用GQA。MLP部分前4层采用Dense FFN，后面的MoE采用类似DeepSeek V3的256个experts，每个token激活1 shared expert + 8 experts。
* **LongCat-Flash**：参见《LongCat-Flash Technical Report》。它采用了DeepSeek V3中的MLA，MTP与fine-graned expert的设计。区别在于每个layer包含了两个MLA和多个FFN。MoE中，一方面基于不同的token所需计算量不同，它采用了zero-computation experts使得模型根据contextual importance来动态调节计算量。另一方面，它采用Shortcut-connected MoE (ScMoE)用shotcut连接第一个MLA到MoE，另一条路是FFN->MLA->FFN。这样无需shared expert也可以使通信与计算能很好地做single-batch overlap。
* **Step-3**：参见《Step-3 is Large yet Affordable: Model-system Co-design for Cost-effective Decoding》。Attention部分采用Multi-Matrix Factorization Attention（MFA），详细可参见《Multi-matrix Factorization Attention》。它与MLA类似，先将Q降维，经过归一化后再升维。不同的是对K和V不会做这个操作。Q的所有head共享K和V。FFN部分采用了与DeepSeekMoE类似的结构。
* **DeepSeek OCR**：参见《DeepSeek-OCR: Contexts Optical Compression》。它是VLM架构。Encoder部分为包含SAM和CLIP的DeepEncoder，用于图像的特征提取。Decoder部分采用小规模的DeepSeek-3B-MoE。
* **DeepSeek V3.2-Exp**：参见《DeepSeek-V3.2-Exp: Boosting Long-Context Efficiency with DeepSeek Sparse Attention》。它引入了DeepSeek Sparse Attention（DSA）结构。该结构包含Lightning Indexer和Top-k Token Selection，实现了细粒度稀疏注意力机制。Lightning indexer计算query token与前面token的index score，然后挑最大的K个token对应的KV与query进行attention计算。它主要解决传统的稠密attention在长序列下计算复杂度指数增长的问题。
* **MiniMax-M1/M2**：参见《MiniMax-01: Scaling Foundation Models with Lightning Attention》与《MiniMax-M1: Scaling Test-Time Compute Efficiently with Lightning Attention》。Attention部分使用lightning attention（一种linear attention）与softmax attention（GQA）按7：1的比例堆叠。MoE部分采用32专家选2的策略。之后出的MiniMax-M2模型没有用MiniMax-M1中的lightning attention，而是用回了full attention（原因可参见官方文章《为什么MiniMax M2是一个Full Attention模型？》）。MoE部分更加稀疏（230B参数激活10B）。
* **Qwen3-Next**：参见《Qwen3-Next: Towards Ultimate Training & Inference Efficiency》。Attention使用Hybrid Attention（混合注意力机制），它将Gated DeltaNet（线性注意力）与Gated Attention（标准Attention加了Gating机制等改进）以3比1的比例组合。线性注意力可以将标准Attention的平方复杂度降到线性。MoE部分高度稀疏（80B参数激活~3B）。
* **Kimi Linear**：参见《Kimi Linear: An Expressive, Efficient Attention Architecture》。它的核心是Kimi Delta Attention（KDA），是一种线性注意力机制。它扩展了Gated DeltaNet，将其head-wise的遗忘门变成更细粒度的channel-wise。它对Gated DeltaNet的转移矩阵Diagonal-Plus-Low-Rank（DPLR）通过加限制得到其变体，使得可以用硬件高效的chunkwise并行算法进行计算。Kimi Linear架构将KDA与MLA以3:1的比例混合。

Attention由于其复杂度为序列长度的平方，因此对长上下文的处理是比较挑战的。这个问题上最近有两个比较热的方向：

* **Sparse Attention**
   如DeepSeek的NSA和DSA。早些年就有不少工作指出Attention中其实只需要KV中的部分就能得到不错的accuracy，如《H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models》和《Quest: Query-Aware Sparsity for Efficient Long-Context LLM Inference》等。它们以一定的标准，基于KV-cache的eviction或 selection的方法选取对精度影响大的KV部分参与计算。但是它们是作为推理阶段的近似方法提出的，对accuracy通常影响会较大。对accuracy影响更小的方式是在训练时就采用Sparse Attention。DeepSeek团队之前的论文《Native Sparse Attention: Hardware-Aligned and Natively Trainable Sparse Attention》提出过一种用于长上下文的Sparse Attention结构-NSA。该结构比较复杂，结合了三种方式：粗粒度的压缩信息，细粒度的token选择和局部上下文的滑动窗口，再由gate控制。相比之下，DeepSeek V3.2中的DSA结构会简单一些。
* **Linear Attention**
   如MiniMax-M1，Qwen3-Next和Kimi Linear。Attention中K和V可以看作是状态，Q可以看作每步的输入。它与K和V进行计算并更新K和V。理想情况是K和V作为状态增量更新，每步Q与这个状态相乘。但由于softmax的存在，我们没法用结合率将K与V先相乘。如果直接去掉softmax自然会使模型的表达能力降低，因为这样Attention就退化成一个纯线性函数。Linear Attention将softmax去掉，但是将Q与K通过一个非线性函数转到特征空间。然后在特征空间上相乘。这样便可以利用结合率将K和V相关部分先乘了。在前深度学习时代流行一时的kernel method似乎又以新的形式重回舞台。

回到DeepSeek V3的部署上来。在模型发布之后的DeepSeek [开源周](https://github.com/deepseek-ai/open-infra-index)里，各重要组件（FlashMLA，DeepEP，DeepGEMM，DualPipe, EPLB，3FS）以开源项目的形式陆续发布。尽管推理引擎（从文章《The Path to Open-Sourcing the DeepSeek Inference Engine》中可知是基于早期版本vllm）没有开源，但这些开源的组件已普遍被吸收到各主流推理引擎中。

DeepSeek在官方的技术报告《DeepSeek-V3 Technical Report》与技术文章《DeepSeek-V3 / R1 推理系统概览》中有关于部署方案的说明。但由于没有开源完整的推理解决方案。业界有很多相关实现和优化工作，如：

* SGLang
  + 《Deploying DeepSeek with PD Disaggregation and Large-Scale Expert Parallelism on 96 H100 GPUs》
  + 《Deploying DeepSeek on GB200 NVL72 with PD and Large Scale EP (Part I): 2.7x Higher Decoding Throughput》
  + 《Deploying DeepSeek on GB200 NVL72 with PD and Large Scale EP (Part II): 3.8x Prefill, 4.8x Decode Throughput》
  + 《Together with SGLang: Best Practices for Serving DeepSeek-R1 on H20-96G》
* Ascend
  + 华为昇腾服务器 DeepSeek V3/R1 推理部署最佳实践
  + 《Serving Large Language Models on Huawei CloudMatrix384》
  + 《DeepServe: Serverless Large Language Model Serving at Scale》
  + 《xDeepServe: Model-as-a-Service on Huawei CloudMatrix384》
* TensorRT-LLM
  + 《Optimizing DeepSeek R1 Throughput on NVIDIA Blackwell GPUs: A Deep Dive for Developers》
  + 《Pushing Latency Boundaries: Optimizing DeepSeek-R1 Performance on NVIDIA B200 GPUs》
* 《RTP-LLM DeepSeek Reproduce Tech Report》
* 《腾讯太极团队实现DeepSeek模型业内H20最高性能15800+ tokens/s》

## PD分离

现代LLM主流采用的auto-regressive的生成方式主要由两阶段组成：Prefill（或称context）和Decode（或称generation）。两者在计算模式上有很大的不同。前者计算密度高，KV cache需求相对小，一般是compute-bound；后者则相反，一般是memory-bound。

传统的做法是把两个阶段放在一个GPU或者一个节点上做。该做法的缺点是对资源的利用效率不高，会出现跑prefill请求时带宽资源用不满，跑decode请求时计算资源用不满的情况。另一方面，prefill与decode会相互干扰。LLM服务通常会有TPOT的SLO，而如果计算资源被prefill 请求占用，容易会使TPOT增大无法达到SLO要求，尤其是在长序列的情况下更为严重。论文《SARATHI: Efficient LLM Inference by Piggybacking Decodes with Chunked Prefills》和《DeepSpeed-FastGen: High-throughput Text Generation for LLMs via MII and DeepSpeed-Inference》等工作中的chunked prefill将长的prompt切成多份，然后将它们与decode阶段的请求混合起来执行，可以一定程度上缓解该问题。但它会有一些缺点：1.实际当中很难选取合适的chunk size。大了不满足SLO，小了又打不满GPU。...
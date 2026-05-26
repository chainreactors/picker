---
title: AI Infra入门干货总结：大模型是如何高效推理的
url: https://mp.weixin.qq.com/s/gCRMjGry2EmBmv1CFfCzVQ
source: Doonsec's feed
date: 2026-05-25
fetch_date: 2026-05-26T06:00:10.515492
---

# AI Infra入门干货总结：大模型是如何高效推理的

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/KVER9adz9052MxYfxQsCibfj0jc833YryZxibJevoGic2tsUP4fRA2JKhskQ6Zr5acVb7vqxy3UKSspKvMkclZSV7CWhjiaqIBlnrqibZXce9f5E/0?wx_fmt=jpeg)

# AI Infra入门干货总结：大模型是如何高效推理的

原创

腾讯程序员
腾讯程序员

腾讯技术工程

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/j3gficicyOvasVeMDmWoZ2zyN8iaSc6XWYj79H3xfgvsqK9TDxOBlcUa6W0EE5KBdxacd2Ql6QBmuhBJKIUS4PSZQ/640?wx_fmt=gif&from=appmsg)

作者：binnnliu

> 看了很多的文章和视频，我以为我理解大模型的工作原理了，直到看了vLLM的代码，我发现很多地方理解的太过表面。因此花了大概2个月的业余时间，深入阅读了vLLM的源码，本文算是对于学习代码的一个总结。另外由于当前主流LLM都是 Decoder-Only 架构，本文会聚焦LLM，不会像网络上其他介绍Transformers的文章从原始论文的 Encoder-Decoder架构讲起。

![](https://mmbiz.qpic.cn/mmbiz_jpg/KVER9adz905HG3eetemicV3ceLLn03OrbiamFgNqUxl5bibyybamw6FBwGmyg5DyC2CVRZyuhJqDfjuVqQnvicA1pyNHBNTNNkyIZq081y5MRyw/640?wx_fmt=other&from=appmsg)

在阅读 vLLM 源码的过程中发现，追踪推理过程中每一步的张量维度变化，对于理解大模型工作原理非常有用。因此，本文将以 Llama 3为例，介绍推理过程中的每个计算环节，在每个计算环节都会标注Tensor的维度变化。

我们知道通过批处理可以提高GPU的利用率：本质是提升计算强度，即通过复用权重数据来均摊内存访问开销；而减少Kernel启动开销与通过海量warp充分发挥隐藏延迟仅是随之而来的次要优化。而批处理内的请求要步调一致，同时开始，同时结束。而对于LLM这类生成式任务，其核心矛盾在于每个请求的输出序列长度是不可预测且差异巨大的。那怎么办呢？

有没有可能将调度的从request level下沉到token level呢？ 恭喜你发明了continuous batching。

那每个请求的KV Cache显存申请是不是应该也是token level，不要一次申请所有的显存。搞一个地址数组(block table)来维护每个请求的KV Cache地址就好？ 恭喜你发明了Paged Attention。

没错，以上两个概念是当今大模型得以高性能运行的关键。

### 连续批处理 (Continuous Batching)

在vLLM调度器的视角中，不存在Prefill 阶段和Decode阶段的区分。 每个请求主要关注：

* num\_computed\_tokens：已经计算过的 token 数（含 Prefix Cache 命中的部分）
* num\_tokens：该请求当前总共拥有的 token 数（prompt + 已生成的 output）

每一步调度的目标就是：让`num_computed_tokens`**追上**`num_tokens`。差多少就调度多少——当然要受限于 token 预算。

调度受4个硬性约束限制：

1. 最大并发请求数

   `self.max_num_running_reqs = scheduler_config.max_num_seqs`
2. token budget   单步最多计算多少 token（所有请求之和），控制 GPU 计算量上限

   ```
   self.max_num_scheduled_tokens = (
       self.scheduler_config.max_num_scheduled_tokens       # 优先用这个
       if self.scheduler_config.max_num_scheduled_tokens
       else self.scheduler_config.max_num_batched_tokens    # fallback
   )
   ```
3. 模型最大序列长度

   `self.max_model_len = model_config.max_model_len`
4. 是否还有空闲的KV Cache blocks

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KVER9adz904ibib8BBklBicOpr1QuGX2Lam3GSKYFmSzPVKfNbdiaiad2ASw9VDg5bHRvuDeN2O2vV44uj2jZTJcyvb4SA2PfqqltA9RFictmCpRI/640?wx_fmt=png&from=appmsg)

如上图所示，vLLM的每轮推理都会基于token level调度，后续的执行的输入都是类似input\_ids这种打平的token数组，即Flattened。(这里的调度逻辑是在Tokenize之后, 本文后续的num\_sched\_tokens都对应上图中的total\_num\_scheduled\_tokens)

### Paged Attention

vLLM启动时会申请显存 kv\_cache shape为：`[num_layers, 2, num_blocks, block_size, num_kv_heads, head_dim]`，每一层key\_cache和value\_cache的shape都是`[num_blocks, block_size, num_kv_heads, head_dim]`。

block\_table会记录每个请求分配到的物理块ID，shape为`[max_num_reqs, max_num_blocks_per_req]`，请求0分配了块`[5, 8, 12]`，请求1分配了块`[3, 7]`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KVER9adz905qiafiay4uf58j2GiclGZQx22yhp0NkjYOLDAAodYmWUAwaBg26HkYl7JQJjIm1GsUqyAHwuCK1Vg6ombQ5mMYx6T96rFYML3544/640?wx_fmt=png&from=appmsg)
> 为什么 `slot_mapping` 和 `block_table` 不需要 `num_layers` 维度？
>
> 如果一个请求的第 25 个 Token 被分配到了物理块 ID 为 `8` 的位置，那么在模型的**第 0 层到第 31 层**，这个 Token 的 KV 值都会被存储在物理块 `8` 的相同位置。

而推理过程中，通过slot\_mapping告诉kernel 把新产生的 KV 写到哪个 slot，通过block\_table告诉 kernel 去哪些物理 block 读取 KVCache。

```
# slot_idx对应token对应的最终存储位置:  slot_idx = block_idx * block_size + block_offset
const int64_t slot_idx = slot_mapping[token_idx];

const int64_t block_idx = slot_idx / block_size;     // 计算块索引
const int64_t block_offset = slot_idx % block_size;  // 计算块内偏移
```

> 比如：`block_size = 16`（每个块存储16个token）,请求0的block\_table为：[5, 8, 12]，token位置为25，计算过程：
>
> 1. block\_idx = 25 // 16 = 1（属于第1个虚拟块）
> 2. block\_idx = block\_table[0, 1] = 8（从页表查找物理块ID）
> 3. block\_offset = 25 % 16 = 9
> 4. slot\_idx = 8 \* 16 + 9 = 137

PagedAttention 的虚拟页表机制解决了显存碎片的问题，极大地提升了 GPU 的显存利用率，是支撑 Continuous Batching 高性能推理的基础。

然而PagedAttention 引入的 block\_table 间接寻址机制，打破了一个请求在物理显存上的绝对连续性。当 Attention Kernel 跨越 block 读取历史 KVCache 时，会触发离散访存（Uncoalesced Access），这在底层对 Memory Controller 是非常不友好的，同时也会导致 L2 Cache 的命中率下降，带来一定的带宽折损。当然，系统设计从来都是 Trade-off。

vLLM 通过设置合理的 block\_size（默认通常是 16）来缓解这个问题：在一个 block 内部的 16 个 Token 的物理显存依然是连续的，能够保证高效率的合并访存。相比于因显存碎片导致的OOM，牺牲少部分的访存带宽换取整个系统吞吐量（Throughput）的大幅跃升，在 LLM 推理的整体逻辑中是划算的。

### LLM推理流程

![](https://mmbiz.qpic.cn/mmbiz_png/KVER9adz9041sjUf9jgC1I5icX9ZVB7YxPqrH2utFURsByPibkCcskNhbDuic95r0w84zYVHWnjzDxusYznwseGYKicUWm3ZcmfliaIq17ECDROk/640?wx_fmt=png&from=appmsg)

### Tokenize

对用户输入提示词进行分词并转换为数字表示。目前主流 LLM 几乎全部使用 BPE（Byte Pair Encoding）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KVER9adz906aYCdHaXf2nmjCLnSn4YFCOicaY7N7KGuXUt2Y884cOicAibzrQuiaEJwIk0SAOyOr8GG9tbmTFeyzwsMHThrJzgtN4hqCC4Agf6M/640?wx_fmt=png&from=appmsg)

BPE的词表训练方式如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KVER9adz904YzORgl8hSXWthYpFujQEEvibJcXzEFMWxktubEaFP8vWKoXicOBSLdIvzBSQr3ZsicTIN5DXA9hmH4bysnweGic0ciabYcu8UgBUQ/640?wx_fmt=png&from=appmsg)

### Embedding Lookup

Embedding Lookup 本质上是一个查表操作，它将一维的 Token ID 数组`[num_sched_tokens]`直接转化为 `[num_sched_tokens, hidden_size]` 的特征矩阵，作为进入大模型真正意义上的数学输入。

#### 理论实现

| 目标矩阵 | 计算公式 | 输入  维度 | 权重矩阵  维度 | 输出结果维度 | 备注 |
| --- | --- | --- | --- | --- | --- |
| Embedding |  | `[batch_size, seq_len]` | `[V, hidden_size]` | `[batch_size, seq_len, hidden_size]` | 本质是索引取值，而非矩阵乘法 |

#### vLLM中的实现

| 目标矩阵 | 计算公式 | 输入   维度 | 权重矩阵  维度 | 输出结果维度 | 备注 |
| --- | --- | --- | --- | --- | --- |
| Embedding |  | `[num_sched_tokens]` | `[V, hidden_size]` | `[num_sched_tokens, hidden_size]` | Flattened 布局 |

将 Batch 中所有请求的有效 Token 拼接为一维长向量，彻底消除 Padding。

### Transformer Block

#### Attention Module (以标准GQA + RoPE为例)

##### RMSNorm

为了保证大模型在神经网络中的数值稳定性，必须引入特征归一化（Normalization）机制。与传统 LayerNorm 要求同时缩放与平移不同，为了提升计算效率，现代大模型广泛为采用了 RMSNorm ：砍掉平移操作，仅沿特征维度对数据进行尺度缩放，能够有效防止前向传播中的方差膨胀与硬件数值溢出，从而极大缓解反向传播时的梯度异常（消失或爆炸）问题，为深层网络的稳定训练提供基础保障。

| 目标矩阵 | 计算公式 | 输入  维度 | 权重维度 | 输出结果维度 | 备注 |
| --- | --- | --- | --- | --- | --- |
| RMSNorm |  | `[num_sched_tokens, hidden_size]` | `[hidden_size]` | `[num_sched_tokens, hidden_size]` | 是一维向量而非矩阵，做的是逐通道缩放而非 GEMM |

##### Q/K/V Linear Proj - Fused QKV

| 目标矩阵 | 计算公式 | 输入 X 维度 | 权重矩阵  维度 | 输出结果维度 | 备注 |
| --- | --- | --- | --- | --- | --- |
| Fused QKV |  | `[num_sched_tokens, hidden_size]` | `[hidden_size,qkv_proj_size]` | `[num_sched_tokens, qkv_proj_size]` | 权重按列拼接，执行单次宽矩阵 GEMM 4096 (Q) + 1024 (K) + 1024 (V) = 6144 |

##### Reshape & Cache

| 目标矩阵 | Q, K, V Slice | RoPE(维度不变) | Multi-Head Reshape | **备注** |
| --- | --- | --- | --- | --- |
| Query () | `[num_sched_tokens, hidden_size]` |  | `[num_sched_tokens,num_heads,head_dim]` | 前 4096 列 |
| Key () | `[num_sched_tokens, kv_channels]` |  | `[num_sched_tokens,num_kv_heads,head_dim]` | 中间 1024 列 |
| Value () | `[num_sched_tokens, kv_channels]` |  | `[num_sched_tokens,num_kv_heads,head_dim]` | 最后 1024 列 |

注：是一个块对角旋转矩阵，实际实现中通过元素级 sin/cos 运算避免矩阵乘法。

这个阶段的大概流程： QKV 按列拆分 -> 对Q、K进行RoPE计算 -> Q、K、V Reshape多头视角  -> 然后reshape\_and\_cache按照slot\_mapping Scatter写入Paged KVCache。

RoPE 的核心思想就是：**用旋转的角度来代表 Token 的位置**。 虽然不是矩阵乘法，sin/cos 属于超越函数，在 GPU 上由 SM 内的特殊函数单元（SFU, Special Function Unit）执行。SFU 的吞吐量通常仅为 FP32 ALU 的 1/4。所以VLLM中不在 RoPE kernel实时计算sin/cos ，而是引擎初始化时按模型配置预计算好 cos\_sin\_cache，shape 为 [max\_position\_embeddings, rotary\_dim]。 RoPE kernel 运行时按 positions 索引出对应的 cos/sin 行，与 Q/K 做逐元素乘加即可。本质是用一份小表（典型大小几 MB 到几十 MB）换掉每次 forward 几百万次的 sin/cos 调用——经典的空间换时间 /访存换算力。

##### Attention (FlashAttention, Scaled Dot-Product Attention)

 读取请求对应 KV Cache 进行 FlashAttention 计算。

> Softmax 的核心原理可以用一句话概括：将一组任意的实数（通常称为 Logits），转化为一套总和为 1 的概率分布，同时放大差异。ps: 这里的为head\_dim。

感觉Attention的逻辑是整个LLM推理最复杂的地方了：

1. Attention 的数学逻辑并不复杂，但是为了提升计算强度，打破内存墙，业界在这里做了非常多的优化，比如FlashAttention；
2. 其他阶段基本都是Token维度打平的，而Attention计算必须要在请求维度进行运算。

特别注意: 在进入Attention kernel之前，需要从全局Flattened视角`[num_sched_tokens, ...]`切换到请求维度视角`[batch_size, ...]`。这是因为Attention计算本质上是请求内部的操作，不同请求的KV Cache不能交叉。vLLM/FlashAttention通过`cu_seqlens`（累积序列长度）数组来实现这种变长序列的请求级隔离，而无需真正Reshape为`[batch_size, ...]`的规整张量。 这里的K和V Shape算子逻辑上为`[batch_size, num_kv_heads, seq_len, head_dim]`，而不同请求的seq\_len肯定不一致。实际上在cuda算子层已经确保了不同请求不会分配到同一个 thread block，即保证这里的运算是请求维度隔离的。

K的Shape为`[seq_le...
---
title: 腾讯混元AI Infra如何优化Hy3 Preview：一次大模型推理性能提升的技术拆解
url: https://mp.weixin.qq.com/s/miAOHTBZLyuDfNle1jrO0w
source: Doonsec's feed
date: 2026-06-26
fetch_date: 2026-06-27T05:48:09.393187
---

# 腾讯混元AI Infra如何优化Hy3 Preview：一次大模型推理性能提升的技术拆解

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/KVER9adz905w9BuUXrAicj6gpIyNy7sGAibAIkQwO8LXQ9xibZP5PcP1nJicrjWPTQpYuX7U5FQp93p2G5loL9rbKhVP6iaPJhxeSI0nMOPB9yf4/0?wx_fmt=jpeg)

# 腾讯混元AI Infra如何优化Hy3 Preview：一次大模型推理性能提升的技术拆解

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

作者：混元AI Infra推理团队

> 本文将从算子优化与融合、并行策略、多级缓存、MTP和异步调度优化、量化与稀疏五大维度，逐一剖析各项技术的设计思路、核心算法与实测收益，全面揭示 Hy3 preview 模型在 Hopper 卡上从算子到系统的极致性能优化实践。

### 一、背景和优化成果

随着大语言模型向千亿参数、百万级上下文加速演进，推理效率已成为模型规模化落地的决定性瓶颈。更大的模型、更长的序列、更复杂的 MoE 稀疏架构，在带来能力跃升的同时，也对算力、显存与通信提出了前所未有的挑战。

混元Hy3 preview作为腾讯新一代旗舰大模型，采用 GQA + MoE 混合架构，原生支持 256K 超长上下文，面向 Agent、Coding 等场景。然而主部署卡 NVIDIA Hopper卡 相比业界主流Blackwell系列卡存在算力极低、显存紧凑、缺乏超节点互联等劣势，这意味着必须在极其有限的硬件和长上下文场景下，将推理性能优化至极致方能满足 SLO 约束并实现成本最优。

面对这一系统性挑战，混元 AI Infra 推理团队对 Hy3 preview 推理全栈进行了深度优化。本文将从**算子优化与融合、并行策略、多级缓存、MTP和异步调度优化、量化与稀疏**五大维度，逐一剖析各项技术的设计思路、核心算法与实测收益，全面揭示 Hy3 preview 模型在Hopper 卡上从算子到系统的极致性能优化实践。

**优化成果**

* 测试数据集:  5000条真实数据(最大输入192k，平均输入68k；最大输出64k， 平均输出0.9k；缓存理论命中80%)
* 测试机器：**Hopper架构-96G**
* 限制**50ms TPOP，4s TTFT**
* 精度： W8A8C8

![image-20260624104035572](https://mmbiz.qpic.cn/mmbiz_png/KVER9adz906Oiaic8wcWiaOfyE0Ufwd8OztYGle1k6NVfHmnIm6sEOgibhfTN9icTiarXU0mrSFRMHpJ8WiaCMeOJEG2gkss5dxNAicA9CuCnoE4uPg/640?wx_fmt=png&from=appmsg)

### 二、性能优化方案

#### 2.1 算子优化

针对Hopper架构和Hy3 preview模型，我们深度优化Attention、MoE、Rope、Router、Sampler和通信算子，并开源在**[HPC-Ops仓库](https://github.com/Tencent/hpc-ops)**。

##### **2.1.1 Attention：动态调度负载均衡，根治推理长尾延迟**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KVER9adz906FldQ2yGrrribJfRz8pqKN0RKvbDvYTicib0FnTiaYBgdqInib3p5gFEFUZVClFg4U0HZzxUCx7c3ZTjgwFI1RobvsuaoufPB11UGA/640?wx_fmt=png&from=appmsg)

**问题**

线上推理存在请求长度实时波动、batch 内长短请求混杂等特征， 传统静态 split-kv 需要在长序列吞吐和短序列开销之间做固定权衡。长序列需要更大的 split-kv 才能充分并行，短序列则只需要少量拆分，固定策略很难两头兼顾。

**动态调度方案**

* 所有推理请求按统一Tile粒度拆分，依据全局Tile总量均衡分配各CTA任务规模
* 再通过贪心装桶算法实现Tile任务极致均分，从源头杜绝计算单元负载失衡问题
* 在执行链路中，Task Assign 模块会在每次推理前生成专属任务映射表，各层Attention Kernel依据映射表精准领取并执行对应任务
* 最终由Combine Kernel统一合并split-kv计算结果，实现全流程负载均衡、高效协同运算。

**性能收益**

* 单 batch 长文本场景下单算子最高加速 **2.95x**
* 混合长度 batch 场景下加速 **1.59x~1.76x**

##### **2.1.2 Router GEMM：双BF16重构FP32计算，兼顾高精度与高性能**

![](https://mmbiz.qpic.cn/mmbiz_png/KVER9adz907jCjDa8eWMo4Iux7t1Q9hYicn3TlV4VcAf9O9sAAMg3UzCI6I6Xm7Xn2F8UQrDYuRm2Vnib89KKJvRF6WYP2WL8MP2ODoUfIA6I/640?wx_fmt=png&from=appmsg)

**问题**

在 MoE 路由及稀疏 Attention 等数值敏感模块中，传统的 BF16 激活 × FP32 权重 计算面临效率与精度的两难抉择：若将权重降级，会显著损耗模型精度；若将激活升频至 FP32/TF32，则需引入逐元素类型转换的额外开销，且受限于 CUDA Core 较低的算力带宽，硬件利用率极低。

**方案**

1. 离线阶段将 FP32 权重拆分为高位 BF16 与低位残差 BF16 两组张量：**W ≈ W\_high + scale × W\_low**（scale = 1/256，对齐 BF16 的 8 位尾数）。
2. 推理阶段执行两次 BF16 GEMM 并做线性组合，激活值全程保持 BF16，无需类型转换，均运行在 BF16 Tensor Core 上。
3. 实现上，双路计算融合至单一 Kernel：输入数据仅搬运一次，双寄存器累加器分别缓存两路中间结果，Epilogue 阶段经一次 FFMA 修正出高精度结果写出显存，全程无 HBM 往返，无冗余开销。

**性能收益：**N=192、K=4096 规格，在M=2~4096范围 相比FP32(cuBLAS)实现 有 **2.86x ～ 3.22x** 加速

##### **2.1.3 FusedMoE：全算子流水线重构，极致压缩推理开销**

**重构方案**

HPC-Ops 对 MoE 完整推理链路进行深度融合与执行逻辑重排，将五大核心阶段整合为一体化执行链路：

1. **路由与索引预处理**：基于共享内存分块统计，为每个专家预留连续显存输出区间，大幅降低大规模 Token 场景下的索引构建成本。
2. **Gate-Up GEMM**：通过路由索引直接读取原始输入，省去显式 Gather 搬运；取消 Warp Specialization，由同一 Warp Group 完成搬运与计算，将访存掩盖逻辑由 CTA 内软件流水升级为跨 CTA 硬件调度，显著提升 SM 驻留密度与资源利用率。
3. **激活量化 + Down GEMM**：量化结果按专家维度紧凑写入显存，确保 Down GEMM 高效顺序访存。
4. **Top-K 加权聚合**：在推理末端完成加权求和，全程无额外 HBM 往返。
5. **PDL 无气泡串联**：全流程通过 PDL 技术构建无气泡执行链路，彻底消除频繁 Kernel 启动开销。

**性能收益**

* TP=8 / EP=1 场景：相比 vLLM CUTLASS、vLLM Triton、SGLang 获得 **1.5x – 1.6x** 加速
* TP=1 / EP=8 场景：获得 **1.2x – 1.5x** 加速

### 2.2 算子融合

#### **2.2.1 Fused R**ope+Norm+[Hadamard]+Quant+Store KV

在 QKV Projection 之后，存在连续的 Element-wise 算子链（Rope、RMSNorm、Hadamard 积、量化、KV Cache 写入）。由于各算子计算量极小且算力强度低，频繁启动 Kernel 并反复读写 HBM 导致严重的 **访存带宽受限**，成为 Prefill 阶段不可忽视的延迟来源。

我们通过算子深度融合，将上述 5 个算子重构为单一的微型流水线 Kernel。数据从 HBM 载入寄存器后，在片上完成全链路变换，最终仅写回一次结果，将多次 HBM 往返压减至最低。

* **寄存器级数据流转**：全流程采用寄存器暂存中间结果，彻底消除中间变量（如 Norm 后、Rope 后）的 HBM 存取开销。
* **在线量化与KVCache存储**：在写入 KV Cache 前完成在线量化（Quant），直接以低比特格式写入显存，进一步压缩写出带宽。

**性能收益：**融合算子加速约**5x**

#### **2.2.2 Fused AllReduce+Norm+Add**

针对张量并行场景下，通信、残差计算、归一化拆分执行导致的性能损耗，联合腾讯网络平台部，创新实现通信、残差计算与归一化的全链路融合，封装为 NVLink 原生一体化操作：RMSNorm(AllReduce(x) + residual, weight)。基于 CUDA 多播与 P2P 技术，支持 BF16 及单机多卡部署，采用高效 Two-shot 策略。

* 高吞吐版本（fuse\_allreduce\_rmsnorm\_high\_throughput）依托NVSwitch多播机制完成归约计算，适配大规模 Token 的 Prefill 预处理场景；
* 低延迟版本（fuse\_allreduce\_rmsnorm\_low\_latency）基于Lamport P2P机制，通过PDL实现双Kernel重叠执行，适配小批量Token的Decode推理场景。

**性能收益**

* 覆盖8~32k tokens 场景
* 相比NCCL与FlashInfer同类路径，实测最高加速**1.68x**

#### 2.2.3 采样融合算子

传统采样后处理链路由十余个零碎 Kernel 串联实现（重复惩罚、温度缩放、Top-K、Top-P、Softmax、随机采样等），流程碎片化严重。每个 Kernel 独立访问全局词表（vocab\_size 级别），导致 HBM 加载次数线性膨胀；此外，重复惩罚阶段的掩码数据需通过 CPU-GPU 拷贝传输，引入额外同步开销。

**方案**

将10余个零碎 Kernel融合为2个核心CUDA Kernel，并封装为单一fused\_sampler算子。针对差异化业务场景提供更加精简专用内核，针对差异化业务场景（简单温度采样 / 完整采样），算子内自动适配调度专用内核，最大化 GPU 利用率。

* **全词表单次加载**：将采样全流程所需的全局词表 GPU 读取压缩至 **1 次**，计算与访存充分掩盖。
* **GPU 闭环惩罚计算**：重复惩罚掩码在 GPU 内部完成，彻底消除 CPU-GPU 数据拷贝开销。
* **细粒度多 CTA 并行**：单请求拆分至多线程块并行执行，提升小 Batch 场景下的 SM 并发度。
* **局部堆归并 Top-K**：当 Max Top-K ≤ 64 时，采用局部堆归并替代全局阈值扫描或拒绝采样，避免全词表重复读取。
* **Top-K 与 Softmax 融合**：将 Top-K 归约与 Softmax 的 max/sum 计算合并，进一步削减访存与计算开销。

**收益**

融合前：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KVER9adz907k4SzpsWCIibEm1jMsNJ4AA0qEYnHf4icg6CibQlWkHrR0Ufd5ps5LCjCtB9C3fJjH2TGAyDIFEHLyic4wDPwR14YCRWGANWzKD8E/640?wx_fmt=png&from=appmsg)

融合后：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KVER9adz905CDVrOy1zyJMRKibSuicqUZ3PxOZDpIK7DkiclfjEBAmvCyrZ7wUPrTg3c9PVOibt2ygRrkkUWFjDhWcsNnGia8DMOd77bicib9rGBOA/640?wx_fmt=png&from=appmsg)

相比 vLLM 与 FlashInfer 里的采样算子提升约 **5.5x、2.5x**

#### 2.2.4 Gemm+Comm细粒度通算融合

针对 prefill TPSP 并行场景，我们实现 GEMM 与 ReduceScatter 的细粒度通算融合。SM 资源被显式划分为计算 SM（执行矩阵乘）与通信 SM（执行 RS 搬运）两类角色：计算 SM 每产出一个 Tile 即落盘至本地 Buffer，并通过信号量通知通信 SM 对就绪分片立即发起 RS，实现 Tile 级计算与通信重叠。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KVER9adz906DEbEGD972S7yf3FLsMPMkurcKy9CRnMhyiaXfQZKgKLzs1x7yBmGk4KYELoTWHU0pZexbbqWL2k4vVMugDWICnEJzwzySTnac/640?wx_fmt=png&from=appmsg)

在传统 Load Warp 与 MMA Warp 之外，特化出专职 **Epilogue Warp**，形成 `Load → MMA → Epilogue` 三级流水：

1. **Load Warp**：异步预取下一轮 Tile
2. **MMA Warp**：累加完毕后仅写回 SMEM，立即进入下一轮计算
3. **Epilogue Warp**：异步取出 SMEM 结果，完成 Quant/Scale 等后处理并写回 HBM，最后触发通信 SM 就绪信号

**性能收益**

| 矩阵形状 | 分段耗时 |  |  | 端到端耗时 |  | 加速比 |
| --- | --- | --- | --- | --- | --- | --- |
| (M, N, K) | GEMM | RS | 串行 | 本方案 | 覆盖率 | vs 串行 |
| (8k, 4096, 1024) | 257.74 | 250.93 | 560.12 | 316.63 | 76.5% | 1.77× |
| (16k, 4096, 1024) | 512.04 | 480.82 | 1,096.59 | 604.98 | 80.7% | 1.81× |
| (32k, 4096, 1024) | 1,016.46 | 945.63 | 1,962.30 | 1,162.79 | 84.5% | 1.69× |
| (64k, 4096, 1024) | 2,026.13 | 1,846.68 | 3,872.58 | 2,307.68 | 84.8% | 1.68× |

\**本能力由腾讯混元AI Infra团队与腾讯网络平台部联合优化打磨。*

#### 2.3 并行策略优化

##### 2.3.1 Prefill并行策略：TPSP

Hy3 preview 模型上纯 TP8 方案会引入三重代价：

1. **冗余计算**：Elementwise / Router 等 token-wise 算子沿完整序列维度在各卡重复执行
2. **通信过重**：AllReduce 在 8 卡间交换全量数据，通信开销显著
3. **算子畸形**：MoE Grouped GEMM 被沿 hidden 维切至极窄 shape，计算效率急剧退化

**方案**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KVER9adz907RQ7kZe6FgbMZib3s8W1guUbXuKFg8Td5glcD70R3Gh4d0iaag60XibymAWuIJVaCvMIYQGpopXvLvI25YEb0vKg2D3pJMeBuwKQ/640?wx_fmt=png&from=appmsg)

在保持单机 8 卡部署与模型精度不变的前提下，通过 **SP 拆分 + 通算融合 + 通信量化 + 并行模式调整** 四项技术组合，系统性压缩 TTFT

**性能收益**

| 场景 | 优化前 TTFT | 优化后 TTFT | 节省 | 降幅 |
| --- | --- | --- | --- | --- |
| Prefill 16k | 764 ms | 536 ms | −228 ms | −29.9% |
| Prefill 32k | 1885 ms | 1424 ms | −461 ms | −24.5% |

##### 2.3.2 Decode并行策略：DP+EP

**问题**

Hy3 preview 在单机部署时面临存算双重瓶颈：

1. 显存被权重占用将近一半，挤压 KV Cache 空间，直接制约最大并发数
2. 在小 Batch 场景下，MoE Grouped GEMM 算力强度（Arithmetic Intensity）低，严重受限于访存带宽（Memory-bound）

**方案**

采用 Attention DP + MoE EP 的跨节点混合并行架构。通过增加专家并行度（EP Size）实现权重的多机分布式存储，以此腾出显存空间转产为 KV Cache 吞吐。同时，跨节点聚合 Batch Size 使 Grouped GEMM 进入 Compute-bound 区域，最大化 Tensor Core 利用率。

* 自研 HPC Kenrel，包含 gate，route，group gemm ，count and gather ，combine，在 Hopper卡上取得 sota 性能
* 长序列 Attn DPTP 混合策略，大幅降低 dp 负载不均衡所有带来的影响，而只需承担少量机内通信的额外开销
* 异步专家负载均...
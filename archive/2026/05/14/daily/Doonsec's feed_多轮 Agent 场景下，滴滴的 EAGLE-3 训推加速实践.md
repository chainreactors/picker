---
title: 多轮 Agent 场景下，滴滴的 EAGLE-3 训推加速实践
url: https://mp.weixin.qq.com/s/PZMX-55W_gqJKtHIYXJVyA
source: Doonsec's feed
date: 2026-05-14
fetch_date: 2026-05-15T05:48:22.286131
---

# 多轮 Agent 场景下，滴滴的 EAGLE-3 训推加速实践

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/1kYDdPrxHSpJ53vWciboFWicTOjHiaNADCRBVZLzh4ShzHF1ay7KkKmV6X4QVSv55EG7hLALhN6Mhz6uPNRVcUAVvT19QQxswqScWNbSBe9REE/0?wx_fmt=jpeg)

# 多轮 Agent 场景下，滴滴的 EAGLE-3 训推加速实践

原创

封宇 唐永振
封宇 唐永振

滴滴技术

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/1kYDdPrxHSpr0F1qynzu79udjQ3gFIDaWTnAneCNrMMZgwWVgibaeh0QAZ1ZG1O7WYG5DFdvRAICibibmJhtSrmY4R2peZLOfujHP5ncmIyb1I/640?wx_fmt=gif&from=appmsg)

**概述**

过去两年，大语言模型（LLM）的应用形态从 ChatBot 快速演进为 AI Agent。在自动化代码工程、长文档分析、多轮工具调用等复杂工作流中，上下文长度已从千级 token 扩展至数十万级；与此同时，LLM 的自回归生成具有强串行特性，导致延迟和吞吐成为制约用户体验与成本的核心瓶颈。

围绕这一问题，本文基于开源投机采样框架——SpecForge，介绍滴滴在多轮 Agent 场景中对 EAGLE-3 训练与推理的实践。在训练侧，针对 EAGLE-3 在长序列场景中的显存与通信瓶颈，引入统一序列并行（USP），使得在大规模集群上训练 128K 乃至更长上下文成为可能，现已将相关能力贡献至 SpecForge 开源社区；推理侧，相较 MTP 方法，EAGLE-3 在长序列场景中可实现超过 2 倍 的 TPOT（Mean/P95）收益。上述训练与推理优化，已在实际业务场景中得到验证。

![](https://mmbiz.qpic.cn/mmbiz_gif/1kYDdPrxHSoWHXVf9t3PR0ZcocQiafYCOt5uciat7FVHcLCeJAFbVibTrAHEwES7JwDLocENUaj2hIFgLXmoZZt7bOZtNhYanJ9uMiaibJkMxv7E/640?wx_fmt=gif&from=appmsg)

**智能体时代的推理挑战：**

**为何我们需要极致训推速度？**

**2.1 从 Chat 到 Agent：推理延迟会被“复合放大”**

在传统 Chat 场景中，交互以短问答为主，用户对秒级延迟具有一定容忍度；而在 Agent 场景下，执行流程演进为“思考—行动—观察—再规划”的多轮循环，包括读取上下文、生成思考 token、调用工具并基于反馈持续迭代。这样的循环结构会使推理延迟被不断叠加与放大。

以一个直观示例来看：如果模型生成速度是 20 tokens/s，一个包含 500 tokens 的“思考过程”就需要 25 秒，若一个任务包含 10 轮类似循环，仅“思考”就可能达到分钟级。在对实时性要求较高的场景中，这样的延迟难以被接受。

**2.2 解码阶段的现实瓶颈：memory-bound 与串行依赖**

解码阶段通常属于典型的 memory-bound 场景，每生成一个 token 都需要执行一次前向计算，并伴随对显存的高频访问（包含权重访问与 KV cache 读写等）。与此同时，自回归的顺序依赖使得整个生成过程难以并行优化，使得推理呈现“逐 token 串行执行”的特征。

因此在实际执行中，每生成一个 token 都对应一次高成本的前向计算与显存访问开销（权重 + KV cache），直接推高了基础 TPOT；在多并发或多卡环境下，由于部分 decode step 存在排队或同步等待现象，还会进一步拉高 TPOT 的 P95/P99，从而放大长输出请求的端到端长尾延迟。

**2.3 投机解码：为什么“推理变快”离不开“训练做对”**

投机解码可以理解成：**先用更便宜的方式写草稿，再让大模型一次性批改**；在验证过程中，单次可被接受的 token 越多，**推理就越快**。其本质价值在于减少 Target 模型的验证 step 数量，使 TPOT 的均值与尾部延迟同时下降，实现整体推理加速。

![](https://mmbiz.qpic.cn/mmbiz_png/1kYDdPrxHSq6yicrtcRezHTvVoribmkKF3snQH7OvQ7CYBRMXHCTiaPmfbscZBueRibqR3VmRicoe8m9f2bicvZEAhwQnuuhZaD2Dj3QW3BUkFbhU/640?wx_fmt=png&from=appmsg)

图 1：投机采样的两阶段流程（Draft → Target 一次验证接受多 token）

来源：Thomas Myxke, Efficiently serving LLMs (Part 3): How speculative decoding works, LinkedIn Pulse，https://www.linkedin.com/pulse/efficiently-serving-llms-part-3-how-speculative-decoding-thomas-myxke

具体来讲就是：

* **Draft**：生成一段候选 token
* **Verify**：Target 一次前向整体校验
* **Accept/Reject**：通过的直接输出，失败则回退重来

在 Agent 长上下文场景中（如工具调用、多轮链式推理、结构化输出），高熵片段通常更为密集，表现为前序一步偏差，后序往往整段作废，导致 Draft 生成序列的 Accept Len 容易骤降，加速效果会明显波动，甚至“越长越不赚”。

业界普遍认为，投机解码的加速效果主要取决于两个因素：Draft 的生成成本，以及 Accept Len 的长度与稳定性。换言之，关键不在于“有没有 Draft”，而在于 Draft 能否以较低的成本，持续生成可被稳定接收的长序列草稿。

表 1：投机采样方法对比

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1kYDdPrxHSqIBSn47ht3gVibEpsFe2b5BygrYq3THPAGu6ibWB0zjWAIjp2cu2cb92NkIc2pWWibjCURTmNVXzJOYkCx0eHIBchcKT6uatJj5k/640?wx_fmt=png&from=appmsg)

我们对比了不同投机路线（见表 1）。在 Agent 场景里，长上下文（64K/128K+）是常态：工具调用历史、长链路推理、代码/文档混合输入都会把序列拉长。只用 2K/4K 训练会导致上线后高熵段频繁掉链子，**Accept Len 变短且波动**，加速难以稳定兑现——因此**长序列训练是前置条件**。

在这个前提下，对比各类投机路线（见表 1）：model-free 复用依赖重复性，高熵段命中率下降快；独立小 Draft/多头预测在长链路里误差更易累积，Accept Len 往往随上下文变长而衰减。所以我们选择训练 **EAGLE-3**：用 TTT 等机制按真实推理流程对齐训练，让长上下文下的连续放行长度更稳，从而把推理加速真正落到业务场景。

![](https://mmbiz.qpic.cn/mmbiz_gif/1kYDdPrxHSoZQicwyUichUTVI9rhNnMLbAV0M7It4PjibCRE35WIqwwQPQXe1cwT1ZicPvlibxfyKflmpLUYvOngTrlua7zze6uAWLPicpAb8lzPs/640?wx_fmt=gif&from=appmsg)

**EAGLE-3 的训练形态：**

**为什么小模型也会在长序列下 OOM？**

在将 EAGLE-3 用作投机解码方案后，训练阶段会出现一个反直觉现象：序列长度达到 16K+ 时便开始 OOM。按照常规 SFT 的经验，这一现象并不符合预期——以约 1.5B 规模的 Draft 模型为例，在 batch=1、未开启 checkpoint 的情况下，16K 序列的单卡显存占用通常在约 30GiB 左右，在 80GB 显存卡上仍应有较大余量。

这一差异的关键在于 EAGLE-3 训练目标的“双重性”：即：不只是“把 token 拟合好”，还需要**拉长可连续接收的长度**，为此，EAGLE-3 改变了训练形态。要理解显存为何突然变重，需要从其两个核心设计出发进行分析。

**3.1 多层特征融合：条件更强，状态也更多**

EAGLE-3 并不是简单放大 Draft，而是增强它的输入条件。在生成候选 token 时，由于不同层级承载的信息粒度不同，Draft 会融合 Target 的**低层 / 中层 / 高层特征**，而不是只使用最后一层 hidden state。

* 低层：局部形式、短程线索
* 中层：结构与模式
* 高层：语义与决策信号

通过多层信息融合，可以提升多步预测的稳定性，使 Draft 更容易生成“连续可被接收”的高一致性草稿。但这一设计在工程上带来的代价也较为直接：

* 需要保留多层特征参与计算
* 反向传播时需要保存更多中间激活

相比传统 SFT 仅依赖单层表示的方法，这种多层特征参与会显著增加激活存储与反传计算开销，且该开销随序列长度增长而进一步放大。

**3.2 TTT：把推理流程搬进训练**

更大的显存压力来自 TTT（Training-Time Test），即在训练阶段引入推理过程。传统训练通常以 ground truth 历史 token 作为条件，而在真实推理中，Draft 只能基于自身刚生成的历史继续生成，这会导致训练-推理分布不一致：训练阶段 Step1 模型始终接收“干净输入”，而推理阶段 Step2 则需要在“带误差的历史”上持续生成。一旦前序预测出现偏差，误差会逐步累积，后续 token 更容易被拒收，导致 Accept Len 快速下降。

为缓解这一问题，EAGLE-3 在训练阶段引入 TTT 机制（见图 2），按照真实 decode 流程展开：先生成一步预测，再将该预测作为下一步输入，多步递进，从模拟真实推理过程。通过这种方式，使训练与推理形态保持一致，让模型在训练阶段即适应“带误差历史”的输入环境，从而在推理时获得更稳定的连续接收能力。

![](https://mmbiz.qpic.cn/mmbiz_jpg/1kYDdPrxHSoBiafGmaKjhMZ60JtMP0hJMB7261hBjEIe3vgKdDWupKia4J0e25RNsbslZEEFUrmNJnIl486SzmjQq5bueJke69TckXKbZt40Y/640?wx_fmt=jpeg&from=appmsg)

图 2：TTT 如何减小训练-推理分布偏移

来源：EAGLE-3, arXiv:2503.01840, Fig. 3

**3.3 显存为什么会OOM？**

直观来看，Draft 模型规模并不大，但由于 EAGLE-3 的训练形态不同于常规 SFT，其显存开销来源也发生了变化：除了与参数规模相关的基础开销外，更主要的消耗来自“中间状态”与“训练展开步数”。可以将这两部分理解为两层“放大器”。

**放大器 1：多层特征参与训练（激活存储增加）**

EAGLE-3 的 Draft 会用到 Target 的多层特征，这会带来更多输入状态与中间表示。在 offline 训练中，这体现为更多 hidden states 的加载、缓存与搬运成本；在 online 训练中，还会叠加 Target 前向生成特征的显存与调度压力。真正反向传播的主要压力仍集中在 Draft/Fusion 路径及 TTT 多步展开产生的激活上。随着序列长度增加，这部分激活占用也会更快增长。

**放大器 2：TTT 的多步展开（k 倍计算与中间态）**

普通 SFT 基本是“一次前向算完 loss”。而 TTT 则是在训练中模拟推理 decode：如果需要连续预测 k 个 token，就需要将过程展开 k 次（每一步基于上一步的预测继续向后计算）。由于反向传播需要保存每一步的中间结果，显存开销会近似按 k 倍放大。当序列长度 L 也很大时，两者会叠加形成乘法效应：每一步本身就因为 L 很长而“很重，再叠加 TTT 的展开步数 k，最终出现“16K+ 就触发 OOM”的现象。

一句话总结：EAGLE-3 的显存问题来自<长序列 L × TTT 展开步数 k × 多层特征带来的额外中间态>的叠加，而不是 Draft 参数量本身。

![](https://mmbiz.qpic.cn/mmbiz_gif/1kYDdPrxHSp4e8IPKyzYmHyiab3PLlVbtuySKibJb7wBdMBHmNcFcl7TNLbJKDKDN1bu4wNERQnoEBnCG7uLviclKRicTUApJdtKiaalDquQ1sy4/640?wx_fmt=gif&from=appmsg)

**长序列训练的显存墙：**

**问题在激活，不在参数（所以必须 SP）**

**4.1 EAGLE-3显存墙的实质：“中间状态”**

在 64K / 128K 级别的长序列训练中，显存的主要消耗来自“中间状态”，包括 attention 的中间激活（如 softmax 相关中间量、Q/K/V 张量等），以及反向传播必须保留的激活，包括 EAGLE-3 特有的多层特征参与训练所带来的额外激活存储，与 TTT 多步展开引入的 k 轮中间态堆叠。这类开销的共同特点是会随着序列长度 L 快速增长，并在 TTT 场景下近似按 k 倍进一步放大。因此，即使 Draft 参数量本身并不大，长序列训练也会很快撞上显存墙，其瓶颈并不在参数规模，而在“激活与 attention 中间状态”。

**4.2 显存墙：128K 下单卡训练无法启动**

当序列长度扩展到 128K 时，瓶颈主要来自 attention 和激活等中间状态，而非参数规模本身。在此基础上，再叠加第 3 节中的多层特征与 TTT 多步展开机制，显存开销会随 L×k 快速放大，使得单卡难以稳定启动训练。不同并行方式在长序列场景下的作用边界如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1kYDdPrxHSoW7Q90OPymEZk504ibKibejegb6ue6UPtLXIfmUrtcYlVm2tQ4XUwUEbdDZ36Nmzc4kUG3uBO08qttxTQwn1ZJvD2O3fibZn9xm8/640?wx_fmt=png&from=appmsg)

因此，要让长序列训练可行，必须引入序列并行（Sequence Parallelism, SP），在 token 维度对激活与 attention 中间状态进行切分。接下来我们将进一步说明，为什么需要通过 USP 将 SP 进一步做到“既能跑、又能快、还要稳”。

**4.3 为什么进一步需要 USP：不仅要能切，还要切得快、切得稳**

序列并行（SP）虽然降低了显存占用，但在扩展到更长序列时仍面临两个关键限制：其一是更高的通信频率，序列切分越细，跨卡数据交换越频繁；其二是更高性能的算子，attention 的实现方式直接影响整体吞吐与显存开销。

综合这两方面因素，我们采用 USP（Unified Sequence Parallelism），在统一框架下组合序列并行策略，兼顾**显存切分**与**通信/算子效率**，将长序列训练从“可启动”进一步提升为“可规模化”。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1kYDdPrxHSrJ0Ga1AhffJMcKeccPwISIXFjdTIF9GhwqdicgWQCB8sibIXQDWkMCAjlT0Bul3LV6IGJKC1EUvEzgwlGB74wPXRAiaH0l70NXAo/640?wx_fmt=gif&from=appmsg)

**我们的工作：**

**EAGLE-3 专属的统一序列并行（USP）**

我们为 EAGLE-3 实现了 USP，将注意力计算拆分为“主干（main）+ TTT 分支（branch）”两条路径：主干部分采用 ring attention 进行分布式计算，分支部分在本卡完成增量更新，最终通过 LSE 进行数值一致性融合。该设计一方面将显存压力按序列维度分摊到多卡，另一方面保证了训练过程的稳定性，使 Accept Len 不受影响。

基于这套实现，超长序列训练从“无法启动”推进到**单机 8 卡即可稳定支持 128K 上下文**；在此基础上，进一步提升上下文长度时，也可以通过扩展 SP 规模（横向增加卡数或机器数）实现持续扩展。

**5.1  USP：把 Ulysses（按 head 切）+ Ring（按序列切）组合起来**

在 EAGLE-3 的长序列训练中，显存压力主要来自两个方面：一是序列长度 L 很大，使得 attention/KV/及激活等中间状态随之快速增长；二是 TTT 需要进行多步展开，使整体训练开销近似再乘以 K。在这种 L×K 的设置下，单一并行方式通常难以覆盖全部瓶颈，因此我们引入 USP，将两种互补的序列并行方式统一到同一条 attention 计算路径中。

* **Ulysses：按 head 维度切分（All-to-All 重排）**，将 attention 计算分摊到不同 head 上，使吞吐更容易提升；但由于切分粒度受 head 数限制，在序列较长时，显存开销更多来自序列相关的中间状态，仅依赖 head 切分难以完整覆盖。
* **Ring：按序列/token 维度切分（ring attention 通信）**，将随序列长度 L 增长的 KV/中间状态按 token 分布到多卡，从而使显存可随 SP 规模近似线性下降；但其代价是通信更频繁，因此要在算子与通信编排上做好优化，才能兼顾性能与稳定性。

USP 的核心作用在于将两者统一协同：由 Ring 负责将长序列训练的显存压力“托住”，由 Ulysses 提升并行计算效率，同时结合后续的要介绍的“主干 / 分支解耦 + LSE 融合”机制，保证在分布式切分条件下 EAGLE-3 的计算规则与数值口径依然一致。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1kYDdPrxHSpeBTpETibL0UWS2JicaTtacS9fq47AvgzHXRmNRuRPG4sRicnKsb8oBgqAenId9eL3YyBL5kpKHBakVLF2EvVAOsvTq6r4Z6AuvM/640?wx_fmt=png&from=appmsg)

图 3：USP 的总体思路（Ulysses...
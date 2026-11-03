---
title: 揭秘小红书自研稀疏训练引擎 SparseGear：面向搜广推模型 Scaling Up 的资源协同与 HBM-Friendly 架构
url: https://mp.weixin.qq.com/s/7anhf5KS7hhOUk_lQjo4gA
source: Doonsec's feed
date: 2026-11-02
fetch_date: 2026-11-03T08:47:39.284671
---

# 揭秘小红书自研稀疏训练引擎 SparseGear：面向搜广推模型 Scaling Up 的资源协同与 HBM-Friendly 架构

# 揭秘小红书自研稀疏训练引擎 SparseGear：面向搜广推模型 Scaling Up 的资源协同与 HBM-Friendly 架构

原创

REDtech
REDtech

小红书技术REDtech

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_jpg/P9Hs04VFGRnT3YIicOEjyCFXpMD4BxlLUoQzLHltcj06krD8Ur9NiafrfwfQZtH3mMibvP7YfpBRQjH0NiaDk6uiaqAXSkDrmlUAtf6zfJns38RM/640?wx_fmt=jpeg&from=appmsg)

**导读**

随着小红书搜广推模型的序列长度向万级增长、Dense 参数规模向百亿级扩展，训练系统既要提高稀疏参数供给效率，也要为 Dense 计算留出更多显存空间。小红书自研训练引擎 SparseGear 从调整资源分工入手，充分利用主机资源与通信链路改善参数供给，并通过 HBM-Friendly 多级存储降低稀疏侧的显存占用，支撑模型持续 Scaling Up。

围绕完整训练链路，SparseGear 还通过统一特征抽取平台降低公共特征重复生产的成本，以原生五维并行支撑模型扩展，并引入 Agent 自动调优降低优化成本，最终在多个业务场景取得了 20%～300% 的训练性能收益。

**01**

**业务背景与架构瓶颈**

小红书的搜广推业务持续探索长序列建模和更大规模的 Dense 网络。更长的行为序列可以为模型提供更完整的用户历史，帮助刻画长期兴趣及其变化；更大规模的 Dense 网络则为复杂特征交互提供更强的表达能力。

与此同时，多模型并行迭代已成为业务研发的常态。因此，训练系统既要支撑单个模型的规模扩展，也要控制多模型迭代的整体成本。原有 TorchLarC 训练系统采用 CPU Worker、GPU Worker 与远端 Parameter Server（PS）协同的架构：CPU Worker 负责数据读取和特征处理，GPU Worker 完成 Dense 前向、反向及稠密参数更新，Remote PS 管理稀疏参数。这套架构将词表容量与 GPU 计算资源解耦，支持存储和计算独立扩展，并具备成熟的特征处理与异步执行能力。但随着模型规模增长和并行实验增多，训练系统也面临以下新的瓶颈。

![](https://mmbiz.qpic.cn/mmbiz_png/P9Hs04VFGRk89rTYtNtqlotlbLXuBLicrw9dwahm8ibShoVWALsLszDR8vlfoPyceEbErC9IxSLa78EHPiaXib7yGPoJsMYq5Dm8k8HLYNba6XE/640?wx_fmt=png&from=appmsg)

图 1｜TorchLarC 原有 PS 训练架构。CPU Worker 负责数据读取与特征工程，GPU Worker 完成模型计算，Remote PS 管理完整稀疏词表。

**参数供给：带宽受限，资源利用不均。**样本与稀疏参数传输分别集中在 CPU Worker—GPU Worker、Remote PS—GPU Worker 两条链路，随序列增长逐渐受限于带宽。多卡重复访问进一步增加数据搬运量，异步预取也无法消除这部分开销。与此同时，GPU Worker 所在节点的 CPU、内存利用率长期低于 35%，CPU Worker 与 Remote PS 之间的带宽仍有余量。

**显存容量：稀疏缓存与 Dense 竞争 HBM。**为缓解远端访问压力，业界主流方案将热门参数缓存到 GPU，并用 Host 内存扩大本地容量。但增加 GPU 缓存会挤占 Dense 计算的 HBM，缩小缓存又会增加对下层存储的访问，需要兼顾参数供给与 Dense 扩展。

**迭代成本：重复数据生产与人工调优。**长序列增加了特征处理开销，多模型独立生产数据又导致公共特征被重复计算和存储。模型结构与访问分布频繁变化，也使依赖专家经验的人工调优难以跟上迭代。

针对这些问题，SparseGear 重新组织计算、存储与通信分工，利用主机资源与链路余量改善稀疏参数供给；设计 HBM-Friendly 多级存储，为 Dense 扩展释放显存；结合公共特征复用与 Agent 自动调优，降低数据生产和持续调优成本。

**02**

**统一特征抽取平台：公共特征复用，实验特征增量生产**

在训练数据生产环节，同一业务场景下的多个模型通常共享大部分特征，差异集中在少量新增特征或处理逻辑上。为减少重复计算和存储，我们建设了统一特征抽取平台，集中生产公共特征，各模型只补充自身所需的增量。

**计算图复用：减少公共特征重复计算**

平台基于特征引擎（NovaFG），用计算图描述特征抽取、转换等步骤及其依赖关系。稳定、可复用的公共计算图归入公共计算部分（Base），各模型独有的计算图归入实验计算部分（Exp）。通过匹配计算节点及其依赖关系，确定公共复用范围和各实验需要执行的增量计算。

实验变化时，仅重算受影响的子图及必要依赖；无法可靠匹配的计算采用保守重算，避免错误复用。

**增量结果存储：减少公共特征重复保存**

Base 结果与各模型的增量结果（Exp Delta）存储在 Paimon 表的不同分支中，通过共享 Base 数据减少重复存储和生产阶段的读写开销。Delta 通过 Data Evolution 写入，与 Base 按行对齐，训练时通过列级 Merge on Read 高效读取。

**独立执行：按需配置资源，支持异构计算**

特征生产独立于模型训练运行，可按自身负载调整资源。执行层采用 Ray，通过常驻 Actor 复用 novaFG 初始化状态，减少重复加载开销。同时，依托 Ray 的异构资源调度能力，为后续接入需要 GPU 的特征抽取任务提供支持。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/P9Hs04VFGRkW4H7phSa8CNjBElyRaXlNlMo9gXuygxEaH6zervNWJ5J47A6EYYsicuCmrelBR67icHYeD0PLOj0PoXgIfykVVBRX3MgZYsAFA/640?wx_fmt=png&from=appmsg)

图 2｜统一特征抽取平台：根据计算图及依赖确定复用范围，Base 统一生产，各模型独立生产 Exp Delta，训练时通过列级 Merge on Read 高效读取。

**实践收益**

以某业务场景下的 1 个基线模型和 2 个实验模型为例，统一特征抽取平台使该场景特征生产的 CPU 总消耗降低了 40%。与各自原有的全量计算任务相比，Exp 增量计算任务的 CPU 消耗降低了 50% 以上。

**03**

**SparseGear：HBM-Friendly 高性能多级存储稀疏训练框架**

长序列训练持续增加稀疏参数访问量，Dense 网络扩展则不断提高显存需求。SparseGear 在设计时同时考虑稀疏参数供给效率与 HBM 使用效率，结合特征消费方式、访问分布和训练时序，在保障参数访问性能的同时降低稀疏侧 HBM 占用，支撑 Sparse/Dense Scaling Up。

**总体架构：分布式多级存储与异步流水**

SparseGear 对稀疏参数进行分片，由对应的 GPU Worker（Owner）管理。来自不同 GPU 的请求汇聚到对应 Owner，合并重复 key 后查找并分发参数；反向梯度也在 Owner 汇聚更新，减少重复访问与缓存副本。

存储层由 HBM、Host DRAM 和 Remote PS 构成，分别承载高频参数、更大的本地缓存和完整的数十 TB 规模词表。在满足参数更新依赖的前提下，后续 batch 的参数准备与当前 batch 的 Dense 前向、反向计算重叠，减少访问等待。

在多级存储与异步流水的基础上，SparseGear 通过 Pooling 前移、分表缓存规划、参数与状态独立缓存、Host 元数据下沉四项设计，进一步提高 HBM 使用效率。

![](https://mmbiz.qpic.cn/mmbiz_gif/P9Hs04VFGRlNWRBNx2Jgu3vKuEGXwrG6VANZI2FWeKEQAiaFmOcS3ClHB9lXcUNkicDblEJ2rViaxNdAsvrqjmY7TUS6GyabSeeNk5CGVdEyiak/640?wx_fmt=gif&from=appmsg)

图 3｜SparseGear 的多级存储与异步流水。四个编号对应 Pooling 前移、分表缓存规划、参数与状态独立缓存、Host 元数据下沉；底部展示 Embedding 与优化器状态不同的预取窗口。

**Pooling 特征分流至 CPU：减少词表 HBM 占用**

小红书业务中，稀疏访问瓶颈往往集中在原始序列特征。这类特征需要保留完整序列的 Embedding，无法提前 pooling，因此通过 GPU 缓存路径访问参数。未构成瓶颈的 Pooling 特征则由已有 CPU Worker 查询参数并汇聚，仅向 GPU 传输结果，同时利用 CPU Worker 与 Remote PS 间的富余带宽。真实业务测试中，纯 Pooling 词表分流后，在训练吞吐不变的情况下，稀疏词表常驻 HBM 占用减少约 26%。

**自适应缓存规划：提高 HBM 缓存效率**

各词表的访问频率、Embedding 维度与热点工作集不同，固定比例分配容易造成容量错配。SparseGear 通过 warmup 拟合各表缓存容量与下层回填数据量的函数关系，在给定 HBM 预算内自动生成最优的分表配置。真实业务测试中，相同 HBM 预算下，从下层存储回填的数据量减少约 43%，训练性能提升 17%。

**参数与状态独立缓存：减少优化器状态 HBM 占用**

现有稀疏框架通常将 Embedding 与优化器状态成对缓存在 HBM，但两者的使用时序不同：Embedding 需在 Dense 前向前就绪，优化器状态直到反向结束后的参数更新才会使用。在相同预取起点下，优化器状态拥有更长的准备窗口。SparseGear 利用这一时间差独立规划两者的缓存容量，将更多优化器状态放在 Host，并保证更新时序一致。根据所用优化器的不同，稀疏参数的 HBM 占用可减少 25%～33%。

**Host 元数据下沉：释放元数据占用的 HBM 空间**

原有实现将 Host 词表的索引与管理元数据保留在 HBM，由 GPU 并行查找 key，再由 CPU 收集、回传参数。Host 词表越大，元数据对 HBM 的占用越高，扩容也因此受限于 HBM。SparseGear 将这部分元数据下沉至 DRAM，由 CPU 通过 SIMD 指令加速检索与驱逐，解除 Host 扩容对 GPU 元数据容量的依赖。真实业务中，HBM 占用下降约 30%；进一步扩大本地缓存后，穿透到 Remote PS 的 key 数减少约 20%。

**整体收益**

最终，在相同 HBM 预算下，稀疏参数穿透率可降低 50% 以上；在相同穿透率下，稀疏参数 HBM 占用可降低 50%，为更长序列和更大规模的 Dense 计算释放显存空间。

**04**

**Dense：原生并行与模型规模扩展**

稀疏侧释放 HBM 后，Dense 侧仍需应对长序列和大模型带来的参数和激活存储需求，以及计算开销。仅扩大数据并行规模，难以突破单卡容量约束，因此需要多种并行方式协同。

SparseGear 采用 PyTorch 原生技术路线，以 DTensor 表达张量在多卡间的切分与复制，结合 TorchTitan 组织分布式执行，原生支持 TP、CP、PP、DP、EP 五种并行方式，并扩展支持 Per Token EP，使业务能够根据参数规模、序列长度和专家结构选择并行组合。

依托 PyTorch 的标准算子与 DTensor 体系，框架能够复用硬件厂商对 PyTorch 的适配成果，减少逐模型、逐卡型重复维护的成本。

**05**

**sg-opt：Agent 自动调优**

搜广推模型迭代快，人工调优耗时，也依赖专家经验。为降低持续优化的成本，我们建设了 sg-opt（SparseGear-Optimizer），支持 Agent 在 WebIDE 中进行单机调试，并在 LarC 平台提交多机任务。

**两级 Profile，逐层定位瓶颈**

sg-opt 提供 High-level 和 Low-level 两级 Profile。High-level Profile 面向稀疏参数访问与 Dense 流水，记录模块级执行过程，将 CPU 侧的锁依赖、GPU 侧的 Event 依赖转换为 Trace 中的有向边，使分散在不同线程、Stream 中的执行与等待关系清晰可见，便于定位阻塞流水推进的环节。

确定目标模块后，Agent 再通过模块名关联基于 PyTorch 原生 Profiler 的 Low-level Profile，查看目标模块的算子耗时与执行细节。

**状态机与独立验证**

Agent 建立基线后，结合代码和 Profile 定位瓶颈、生成修改；状态机管理优化阶段，记录每轮修改与验收结果，支持中断恢复。每轮先对照独立参考实现，校验前向输出、Loss、模型参数梯度及回传给 Embedding 的梯度。数值校验通过后，再独立运行性能测试，并将数值检查与性能结果绑定到同一份代码。只有验证通过且有收益的修改才会成为下一轮的起点，Agent 在给定预算内持续优化，最终交付代码与收益报告。

**知识库与优化模式**

优化前检索 Wiki 知识库；sg-opt 新发现的优化点自动提交，经人工审核、整理后入库。Normal 模式仅用知识库方法，平衡 Token 成本与收益；Ultra 模式在此基础上继续自由探索，在更充裕的预算内追求更高性能。

**成本与收益**

sg-opt 在多个业务模型上取得 20%～120% 的性能提升。以使用外部模型运行 sg-opt 的一次业务优化为例，基线单步耗时约为 670 ms。Normal 累计 Token 费用约 9 美元，耗时降至约 356 ms（下降约 47%）；Ultra 累计 Token 费用约 34 美元，耗时降至约 309 ms（下降约 54%）。

![](https://mmbiz.qpic.cn/mmbiz_png/P9Hs04VFGRmUc91OfcAJayzyOV4l9SibQYkuhTOyUYwJWto3tEnjMPqmPoN8Sia8l48iaSoUu8wibricQdibvHAAXI2W5znRJGpwhyFLpaaE0o3Ac/640?wx_fmt=png&from=appmsg)

图 4｜sg-opt 的优化成本与收益。

///

**总结与展望**

SparseGear 已在多个业务场景取得 20%～300% 的训练性能收益。这些收益源于对业务负载与资源分工的重新审视：充分利用主机资源和通信链路改善稀疏参数供给，并将 HBM 使用效率纳入多级存储设计，在提升训练吞吐的同时，为 Dense 扩展留出显存空间。

面向更长序列和更大规模的模型，我们将进一步探索给定资源下稀疏参数与 Dense 计算的联合优化，更充分、高效地利用系统已有资源。统一特征抽取平台已完成首版建设，后续将结合更多业务场景与运行反馈，持续优化计算复用、增量读写和资源调度，降低多模型实验的数据成本。我们也将扩展 sg-opt 对复杂模型、分布式执行和异构硬件的调优覆盖，将业务中验证有效的优化持续沉淀到框架与知识库，降低模型调优成本，为算法迭代提供更大的探索空间。

///

**团队简介**

**小红书引擎架构部 AI Infra 团队**

小红书引擎架构部 AI Infra 团队负责支撑小红书搜索、广告、推荐、审核、创作等核心业务的 AI 化演进，与算法一起为 LLM/VLM 在业务的落地效果负责，致力于大模型分布式训练、强化学习框架、高性能推理及异构硬件编译器等核心技术的研发，持续打造先进、高效、易用的 AI 基础引擎。

团队研究方向涵盖以下几个方面：

* **超大规模分布式训练：**面向超大规模训练集群，围绕训练稳定性与 MFU 提升，重点研究跨集群训练、低精度训练、容错机制和弹性训练等关键技术。
* **强化学习系统：**聚焦端到端的大模型强化学习系统，面向动态负载、复杂 Agent 与环境交互、异构资源调度及多模态场景，探索下一代高效强化学习基础设施。
* **推理并行方案：**针对大模型推理中的计算与访存瓶颈，研究多机推理、异构硬件并行推理及调度优化方案，全面提升推理性能与资源利用效率。
* **下一代模型与硬件体系联合优化：**结合下一代硬件体系与新一代生成式、理解式模型架构，探索更先进的模型结构、训练范式与推理模式，推动模型与系统协同演进。

///

**招聘信息**

**AI Infra 工程师/专家**

小红书招聘

**【Ace 顶尖实习生】Large Scale Machine Learning Model 训练和推理性能极致优化**

小红书招聘

**【REDstar】机器学习框架工程师-搜广推方向**

**小红书招聘**

**机器学习框架工程师/专家-搜广推方向**

**小红书招聘**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/P9Hs04VFGRnuJnHzBsIkDFjqSxYchIsgWgmKdwGVgAkzmZCkNpVhrG08SuCJOyBEmd3qv7Fa8SNAialGI9CAj7kZdtQfT1OlPiaBsOicqhez7A/640?wx_fmt=png&from=appmsg)

预览时标签不可点

不喜欢

![]()

微信扫一扫
关注该公众号

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/vxnkL2N86IsWfuArZ4Oibu3JjynORoXVKc5OaGgUib1G8yiam3A5HlC2PDpDw1qTu4lasuiakZ76vRsf3KJNKiaye5w/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过
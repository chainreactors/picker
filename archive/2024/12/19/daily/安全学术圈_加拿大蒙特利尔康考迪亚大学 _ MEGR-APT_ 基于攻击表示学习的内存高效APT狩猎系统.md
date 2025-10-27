---
title: 加拿大蒙特利尔康考迪亚大学 | MEGR-APT: 基于攻击表示学习的内存高效APT狩猎系统
url: https://mp.weixin.qq.com/s?__biz=MzU5MTM5MTQ2MA==&mid=2247491476&idx=1&sn=935e5e510d99a3785aeb6cbbb41e86e3&chksm=fe2ee01fc959690960b7e3937e9d36e472fac154ebf4df12f9d74185aa6b12178b57cf6947e9&scene=58&subscene=0#rd
source: 安全学术圈
date: 2024-12-19
fetch_date: 2025-10-06T19:38:56.022285
---

# 加拿大蒙特利尔康考迪亚大学 | MEGR-APT: 基于攻击表示学习的内存高效APT狩猎系统

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6Dibw6L070WF99VHL1DK4z5TBI3f2Itiah42SvyPWNGReXU01vcuzG4wPjyhAFK826gia8vXGfAbhn2aE2q8fciaXA/0?wx_fmt=jpeg)

# 加拿大蒙特利尔康考迪亚大学 | MEGR-APT: 基于攻击表示学习的内存高效APT狩猎系统

原创

吴柯欣@安全学术

安全学术圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WF99VHL1DK4z5TBI3f2ItiahYR2m6ic8iad4mrqENByAhrVrmILHBDfFKrGiaO21g2wCLFE89D6cO4HOw/640?wx_fmt=png&from=appmsg)
> *原文标题：MEGR-APT: A Memory-Efficient APT Hunting System Based on Attack Representation Learning*
> *原文作者：Ahmed Aly, Shahrear Iqbal, Amr Youssef, Essam Mansour*
> *原文链接：10.1109/TIFS.2024.3396390*
> *发表期刊：IEEE Transactions on Information Forensics and Security*
> *开源代码：https://github.com/CoDS-GCS/MEGR-APT-code*
> *笔记作者：吴柯欣@安全学术圈*
> *主编：黄诚@安全学术圈*

### 一、背景介绍

高级持续性威胁（Advanced Persistent Threats, APTs）是当前网络安全领域面临的最具挑战性的威胁之一。APT 攻击具有隐蔽性和长期持续性的特点，攻击者往往采取“低频慢速”（Low and Slow）策略，通过分散在几个月甚至几年的间歇性活动来隐藏攻击痕迹，使得传统的安全检测手段难以察觉。

1. APT 攻击通常遵循复杂的攻击链，涉及多个阶段，例如：

* 初始渗透：通过利用零日漏洞、钓鱼邮件或恶意链接入侵目标系统。
* 横向移动：在内部网络中扩散，通过系统间的交互活动进一步渗透。
* 数据收集与外泄：搜集敏感数据并将其传输到攻击者控制的命令与控制（C&C）服务器。

2. 现有检测方法的局限性

现有的入侵检测系统（IDS）和溯源系统面临以下主要问题：

* 日志数据规模庞大：操作系统审计日志快速膨胀，单个主机每天生成数 GB 到数十 GB 数据，数月或数年的日志规模可达数 TB。
* 内存消耗过大：基于内存的系统（如 Poirot）需将整个起源图（Provenance Graph）加载到内存，面对大规模数据时难以扩展。
* 性能瓶颈：基于磁盘的系统虽可节省内存，但由于频繁的 I/O 操作，查询和匹配性能严重下降，通常需要数小时才能检测到攻击痕迹。
* 低效的子图匹配：现有子图匹配技术要么基于规则匹配，依赖于专家手动定义规则，通用性差；要么采用简单的图相似度计算，难以捕获攻击模式的全局特征。

3. 起源图（Provenance Graph）及其在 APT 检测中的作用

起源图是通过系统审计日志构建的有向图，能够表示系统实体（如进程、文件、网络流）之间的因果关系和信息流。

* 起源图的特点：

+ 节点：代表系统实体（进程、文件、网络流等）。
+ 边：表示系统事件（如进程间通信、文件读取/写入等）。

然而，起源图的数据规模庞大，导致传统的检测方法在处理大规模图数据时面临内存瓶颈和性能瓶颈。

4. 本研究旨在解决以下关键问题

* **内存高效的 APT 检测：** 在大规模审计日志构建的起源图中，以低内存消耗提取与攻击场景相关的可疑子图。
* **高效的子图匹配：** 利用图神经网络（GNN） 和攻击表示学习，快速匹配可疑子图与攻击场景（查询图）。
* **大规模数据的可扩展性：** 支持处理跨数月甚至数年的大规模起源图，保证检测性能和内存消耗的可扩展性。

### 二、MEGR-APT 系统

图1显示 MEGR-APT 系统的整体架构，**MEGR-APT** 系统通过内核审计日志构建**基于 RDF 的起源图**，并结合网络威胁情报（CTI）报告中的攻击查询图（标注入侵指示器 IOC）进行检测。系统通过 **SPARQL** 查询提取与查询图相关的可疑子图，并利用表示学习模型生成图嵌入向量，结合图匹配模型计算查询图与子图之间的**相似度分数**。基于相似度，系统触发警报并生成调查报告，报告包括相似度分数、被覆盖的 IOC、时间戳、统计分析及可视化图形。通过高效的子图提取和自动化的图匹配，MEGR-APT 在大规模数据中实现内存高效的 APT 攻击检测和调查验证。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WF99VHL1DK4z5TBI3f2ItiahwhjcqiasicQ2QSJIhGbubMhLN2ia14AM3pNqIuGRXnFcV5yqvWNekcyqw/640?wx_fmt=png&from=appmsg)

图1  MEGR-APT 系统的整体架构

**A. 基于 RDF 的起源图设计与构建**

MEGR-APT 使用基于 RDF 的数据模型构建起源图，将内核审计日志转换为 RDF 格式的多关系、异构、有向图，支持大规模数据处理并显著减少内存消耗。RDF 数据模型通过三元组 ⟨主语, 谓语, 宾语⟩ 灵活表示系统实体（节点）和事件（边），并利用 RDF 图数据库中的 SPARQL 查询高效提取子图，而无需加载整个起源图到内存。RDF 引擎（如 Stardog）通过内置的索引机制提升查询性能，同时支持批量加载审计日志并通过并行化算法构建起源图。边属性（如时间戳）采用 RDF-star 格式注释，用于标识事件发生的时间。最终，RDF 三元组以 Turtle 格式存储并加载到数据库中，支持实时流式日志的动态更新，无需重建整个起源图。

**B. 攻击查询图构建**

MEGR-APT 系统通过分析网络威胁情报（CTI）报告，将攻击模式抽象为查询图（Query Graph），其中系统实体（如进程、文件、网络流等）被表示为节点，事件和行为作为有向边连接这些节点，并附加相关属性（如路径、命令或 IP）。构建过程包括识别报告中的系统实体，使用 NetworkX 工具生成多关系有向图，添加事件和行为作为边，提取并标注入侵指示器（IOCs）节点（如恶意 IP、恶意文件等），从而帮助提取可疑子图并优化检测算法。查询图的结构化设计支持高效的APT攻击检测和溯源分析。

### 三、基于GNN的APT HUNTING

本节将介绍基于GNN的APT狩猎的三个核心组件。MEGR-APT 通过以下步骤执行APT狩猎：提取与查询图相关的可疑子图，使用表示学习模型对查询图和子图进行表示，然后通过图相似性模型评估查询图与每个提取子图之间的相似性。

**A. 基于IOC的子图提取**

MEGR-APT 基于如下图所示的算法，通过匹配查询图的 IOC 节点从 RDF 起源图中提取可疑子图。算法首先标记与查询图 IOC 节点匹配的可疑节点，并通过插入新的三元组记录标记信息。随后，MEGR-APT 通过并行 SPARQL 查询，从每个可疑节点开始多跳遍历提取子图，遍历跳数根据查询图的平均深度确定。为确保子图规模接近查询图，系统过滤掉节点数和边数超过设定阈值的子图，并移除同一节点间的重复谓词。最终，系统输出与查询图相关的可疑子图列表，用于进一步分析和相似性匹配。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WF99VHL1DK4z5TBI3f2Itiahibt4ubrNg5Lswqtd6ASCIBjkNZ7a9yX0jSFcvYYeswL1hdw4wnMkMMQ/640?wx_fmt=png&from=appmsg)

图2 MEGR-APT子图提取算法

下图可视化展示了一个简化的起源图及其对应的查询图。虚线红色矩形显示了通过MEGR-APT的提取算法从右上角的‘ztmp’文件节点开始提取的子图。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WF99VHL1DK4z5TBI3f2Itiahy3YMG5Wmgatq5ArfMgIia0VywkR3jPUibWibVIeYwJ1BMnpicjHchmTKug/640?wx_fmt=png&from=appmsg)

图3 在简化的 DARPA TC3 Linux 4 起源图中，右侧展示了一个检测到的子图，其对应的查询图位于左侧

**B. 基于攻击的表示学习**

MEGR-APT 的第二个核心组件是基于攻击的表示学习模型，该模型通过生成查询图和可疑子图的图嵌入来反映攻击行为。查询图将攻击场景抽象为一组入侵指示器（IOCs）及其之间的行为关系。在表示攻击场景时，反映这些行为对获得具有代表性的嵌入至关重要。

为阐明这一概念，文中通过 DARPA TC3 数据集的两个正常时期子图和一个攻击时期子图进行可视化说明（如图4所示）。DARPA TC3 数据集包含14天的活动日志，其中攻击从第4天开始。正常时期的起源图是攻击发生之前的图，而攻击时期的起源图包含攻击和正常活动。三个子图均与图3中展示的查询图相关。

* **正常子图（图4顶部）**：显示的是一种正常行为，例如进程‘sh’执行另一个进程‘cmp’来比较两个文件。‘cmp’进程依次打开文件、读取文件、关闭文件，随后结束自身。整个行为流正常，且该行为在提取的子图中重复三次。
* **检测到的子图（图4底部）**：显示的是一种可疑行为，例如进程‘sh’执行另一个进程‘ztmp’，后者将自身复制为两个子进程‘gtcache’。第一个子进程更新文件、修改其属性、关闭文件并终止自身；被修改的文件通过另一个进程连接到远程服务器，随后被第二个‘gtcache’进程删除。虽然该子图未包含整个攻击场景，但其行为流与攻击流程相似，包括下载文件、执行文件、创建子进程、连接远程服务器以及删除下载文件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WF99VHL1DK4z5TBI3f2ItiahxIfcnXZE9icG4Ok20zrOsVH94iaqhd1geQqicrWMox0MD015ysBLvXrKQ/640?wx_fmt=png&from=appmsg)

图4  从 TC3 数据集的正常时期提取的两个正常子图（绿色）以及从 TC3 Linux 4 攻击起源图中提取的一个恶意子图（红色）

总之，MEGR-APT 的基于攻击的表示学习模型通过生成查询图和可疑子图的图嵌入来捕捉攻击行为模式。模型关注通用的恶意活动特征而避免依赖具体属性值（如IP地址和文件路径），从而提高泛化能力，能够检测不同场景中具有相同行为模式的攻击。使用多层关系图卷积网络（RGCN）对图的节点和边进行聚合，并通过全局上下文注意力层生成图嵌入向量。与一般模型（如 SimGNN）或包含所有图特征的模型（如 DeepHunter）相比，MEGR-APT 更注重攻击行为，从而提升检测效率和准确性。模型在 DARPA TC3 数据集上验证了其对恶意行为的有效区分能力，同时避免了虚假关联，提高了泛化性和检测性能。

**C. 基于GNN的图匹配模型**

在 APT 狩猎流程的最后一步是对查询图与每个提取的子图进行两两比较。MEGR-APT 的图匹配模型通过基于 GNN 的架构计算查询图与提取子图的相似度分数，使用神经张量网络（NTN）计算图表示向量间的相似性，并通过全连接神经网络整合为单一的相似度分数。训练过程中，模型基于随机生成的正常子图构建训练数据集，利用图编辑距离（GED）作为相似度标签，且通过多核并行化降低了计算成本。模型专注于预测图对的相似性，而非对图进行恶意或正常分类，从而提升了泛化能力和检测效率，同时避免了训练过程中对测试数据的依赖。

### 四、评估

#### 4.1 数据集

评估使用了两个基准数据集：DARPA TC3 和 DARPA OpTC。DARPA TC3 数据集包含两周的操作系统日志，记录了少量模拟的APT攻击和数百万条正常背景活动日志。该数据集涵盖三个主机（TRACE、THEIA 和 CADETS），分别运行 Linux 和 FreeBSD 操作系统，作者利用该报告构建了8个不同的攻击查询图，详见图5。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WF99VHL1DK4z5TBI3f2Itiah0XvcTDXqicm4uEsU4rxFBIiafDkSshGt3uXOUrmO7frLPAjeB74AkPNQ/640?wx_fmt=png&from=appmsg)

图5 DARPA TC3 和 OPTC 攻击查询图统计

#### 4.2 评估设置

评估过程采用 Poirot[1]的标准设置，定义了真正例（TP）、假反例（FN）、假正例（FP）和真负例（TN）的检测标准。真实标注（Ground Truth）来自攻击报告，报告提供了攻击行为的整体上下文、攻击实体的详细信息（如文件路径、恶意进程命令、C&C服务器IP）以及时间戳信息，用于区分正常起源图和感染起源图。作者仅在正常起源图提取的子图上训练模型，测试时使用从正常和感染起源图中提取的子图，通过手动分析调查报告，确认检测到的子图是否包含与攻击报告时间戳一致的恶意行为，从而确保评估的准确性和公平性。

#### 4.3 GNN模型训练

GNN模型针对不同操作系统独立训练，使用归一化的图编辑距离（GED）作为相似性分数，训练数据包含75万对正常子图，节点用独热编码，边用标签编码表示。模型训练使用75%数据，验证25%，通过均方误差（MSE）评估相似性预测性能，平均训练时间约1小时56分钟。测试阶段使用精确率、召回率、F1分数、TPR、FPR和AUC等指标，AUC特别适用于不平衡数据集。消融实验验证了超参数的影响，并推荐了默认参数配置。

### 五、实验结果

#### 5.1 使用 DARPA TC3 的评估结果

MEGR-APT 在 DARPA TC3 数据集上的评估显示了其高效性和鲁棒性。系统与 Poirot 和 DeepHunter 进行了比较，并成功检测了所有攻击场景的恶意子图。在内存使用方面，MEGR-APT 远优于其他系统，例如处理131 GB起源图时，仅消耗288 MB内存，而  DeepHunter[2] 崩溃，Poirot则需21 GB内存。尽管优化了内存使用，MEGR-APT 在准确性和检测时间上仍与 Poirot 相当。此外，MEGR-APT 对正常数据集未产生误报，证明其高精确性和鲁棒性。相比其他系统，MEGR-APT 更适合处理大规模起源图，具备更强的扩展能力。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WF99VHL1DK4z5TBI3f2ItiahkueBWM50CBfKicOSrmEzmF5a7OjzbBUEwFyU2827U9bVX4iazSeMuvWA/640?wx_fmt=png&from=appmsg)

图6 DARPA TC3 的评估结果

#### 5.2 使用 DARPA OpTC 的评估结果

MEGR-APT 在 DARPA OpTC 数据集上成功检测了所有攻击场景的恶意子图（图7顶部），并未对正常起源图产生误报（图7底部），展现了高精确性。MEGR-APT 的内存消耗与可疑节点数量相关，而非起源图总大小。例如，在主机‘201’中，尽管起源图仅包含400万条边，但由于有3772个可疑节点，与查询图 IOC 匹配，导致内存消耗达到542 MB，为实验中最高值。在“Custom Powershell”攻击中，MEGR-APT 成功检测了攻击行为，包括从主机‘501’发起的持久化、数据窃取、痕迹清理及横向移动，但在目标主机‘358’的日志中未发现攻击痕迹，符合攻击行为特性。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WF99VHL1DK4z5TBI3f2Itiahe17Z6T6JT4fPwibklGsaDjuFCWQYCqmLlLxY8uUxxSUQibtxfbmtIJJg/640?wx_fmt=png&from=appmsg)

图7  DARPA OpTC 的评估结果

#### 5.3 真实用例：企业数据集

此外，作者在一家企业中进行了真实案例测试，数据集来自4000台主机的内核日志，覆盖六个月的时间范围。系统成功检测出一台被攻击主机的56个恶意子图，其中9个与人工报告的时间戳完全匹配，其他子图发现了同一攻击的未报告恶意活动。对12台正常主机的测试中，11台未产生误报，1台的两次报警与攻击模式高度相似，可能是人工报告遗漏的有效警报。MEGR-APT 平均检测时间为2.2分钟，最大内存消耗为290 MB，展现了其在有限计算资源下快速、准确识别高级威胁的能力。企业研究人员认为 MEGR-APT 能减少人工工作量并提高效率，未来将作为开源工具分享给网络安全从业者和研究人员。

#### 5.4 发现

**检测到的子图的正确性**：MEGR-APT 在 TC3 数据集上验证了其检测恶意子图的准确性。检测到的子图与攻击报告中的特征和时间戳一致，例如在 BSD 1 攻击中（图8），成功识别了数据泄露和以 root 权限执行恶意进程的攻击早期行为。在 BSD 2 攻击中（图9），MEGR-APT 检测到报告中描述的 5 个 IOC 中的 4 个，并重构了大部分攻击行为。此外，MEGR-APT 检测到的子图比查询图包含更多细节，例如显示进程的具体行为（如发送、接收、连接等），这对威胁狩猎非常有用，表明 MEGR-APT 对攻击模式的检测能力强且对查询图的精确性不敏感。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WF99VHL1DK4z5TBI3f2ItiahYIicETvdRd2embnZaeHFDicDhQzYlhoI5hOytuerLLUgCp76juT9VwWA/640?wx_fmt=png&from=appmsg)

图8  TC3 BSD 1 场景的查询图（左侧）及其检测到的子图（右侧）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WF99VHL1DK4z5TBI3f2Itiah4pvufA1TVqdbrMRvZAO6UK4rbeCDwTD0gK15icicQMdMwbGn9FLQVn8Q/640?wx_fmt=png&from...
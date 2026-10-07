---
title: 基于混淆算法的端侧大模型保护机制研究
url: https://mp.weixin.qq.com/s/PHf7rlI3tYJdvsKjnNyaVQ
source: Doonsec's feed
date: 2026-10-06
fetch_date: 2026-10-07T07:53:21.302462
---

# 基于混淆算法的端侧大模型保护机制研究

# 基于混淆算法的端侧大模型保护机制研究

原创

赛博新经济
赛博新经济

赛博新经济

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**基于混淆算法的**

**端侧大模型保护机制研究**

*Understanding the Security Boundary of*

*Obfuscation-based On-Device LLM Protection*

今天为大家介绍一篇被 ACM CCS 2026 录用的论文 *Understanding the Security Boundary of Obfuscation-based On-Device LLM Protection*，第一作者为清华大学硕士生周浛屹，通讯作者为刘卓涛老师，作者还包括李晨阳、博士生庞元喆、徐恪老师和徐明伟老师。

大模型在终端设备上的部署带来了模型窃取风险，现有方案通过可信执行环境与轻量级混淆算法相结合，在达到保护模型权重目的的同时，利用外部硬件（如GPU）加速推理。但当前已有工作的混淆算法多为启发式设计，整个领域缺少对各类算法的系统比较和认识。针对这一问题，我们将本领域代表性方案抽象为可组合的混淆算子，刻画既有算子组合的安全边界，并提出模型提取攻击方法 **Collapse**，攻破了8个先进防御方案。在防御方面，研究团队引入两类新的混淆算子，构建防御方案![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaJcPGD01bWVEJ8DgGOn1YglOwsrobgkib3pic3VnVoKOBKAgsO4k4qS0gamEk9WnnVX3Uj6fccPXLygChqXWGwtyG0fcVw722JskTC9O8sRW4/640?wx_fmt=png)，以较小的额外开销显著降低了 **Collapse** 的攻击效果，为端侧模型保护及新型攻防算法设计提供了参考。

**论文原文：**https://arxiv.org/abs/2609.10117

**开源代码：**https://github.com/InspiringGroup-NeoLab/TEE-Obfuscation

**01**

**研究背景**

将大模型部署到手机、个人电脑等终端，可以减少推理时延，并把用户数据留在本地，保护隐私。但是模型权重一旦离开云端，部署在端测，会面临新的问题：设备拥有者能够控制操作系统和运行环境，读取其中的代码、内存与中间结果，从而窃取模型权重。

可信执行环境（Trusted Execution Environment，TEE）通过硬件隔离保护代码和数据，为端侧模型保护提供了基础。然而，传统 CPU 侧 TEE 的安全内存和计算能力有限，难以将完整的大模型推理放入其中。

![](https://mmbiz.qpic.cn/mmbiz_png/iaJcPGD01bWXI07yYwnkm3AjQ9en5RstcR7cibHH2x26KwnI2BiaCE98aGBhJ7jcIcxpRxc6WtlT9ibO84fbrvAhwhpCNI1mMWz5oKh4Jibic4Yw0/640?wx_fmt=png)

图 1 端侧模型保护与提取场景

攻击者结合公开预训练模型、可见的混淆权重和少量任务数据构建替代模型

为解决这一问题，已有研究采用基于 TEE 保护的模型分区方法（TSLP）：将轻量级计算保留在 TEE 内，将计算密集的矩阵乘法经过混淆和掩码之后，卸载至外部非可信的GPU 或 NPU完成高效计算，这类计算环境统称为普通执行环境（REE）。

**02**

**现有混淆方案的安全边界**

既有 TSLP 方案使用了列置换、列缩放、稀疏加性掩码、低秩掩码等轻量级混淆算法。研究团队从已有混淆方案中抽象出 4 种“混淆算子”，分析了已有的 8 个混淆方案，并将其拆成这 4 种混淆算子的组合。这 4 类算子刻画了方案在 TEE 与 REE 边界处的权重变换：稀疏掩码与低秩掩码属于加性变换，列置换与列缩放属于乘性变换。

|  |  |  |
| --- | --- | --- |
| **混淆算子** | **主要操作** | **仍可能保留的**  **结构信息** |
| **列置换 Π** | 打乱权重矩阵的列顺序 | 每一列的方向仍然存在 |
| **列缩放 *D*** | 对各列乘以非零系数 | 列的尺度变化，方向结构仍在 |
| **稀疏掩码 *S*** | 对少量权重元素加扰动 | 大部分元素未被该掩码修改 |
| **低秩掩码 *L*** | 叠加低维子空间中的扰动 | 该子空间之外仍有可利用信息 |

表 1 四类既有混淆算子及其结构特征

更进一步地，研究团队探索了这 4 种已有混淆算子组合出的最强形式 ![](https://mmbiz.qpic.cn/mmbiz_png/iaJcPGD01bWUiaibAjw1KhggdeOb8ia67jicAEOhIHNU2wprHqepYrYhwyHLno1fj7VsxcllUXeib4DibRhrNCEKjmcTN8RtO4Nt8LGaficvl01YtSI/640?wx_fmt=png)，并称之为已有混淆方案的安全边界。由这 4 类算子构成的组合，都可以化为同一种规范形式：

![](https://mmbiz.qpic.cn/mmbiz_png/iaJcPGD01bWUCmLefko4r3ShQTt7TticfgNyDpoad7zVT2m5SIajFsoxQwYL0GbSXOlHnWQbNH4k6FKDFD7iaJHuOI60pJMwbuEsVjMPEggfT0/640?wx_fmt=png)

其中，***W***是原始权重，***S***和 ***L***分别是稀疏掩码与低秩掩码，***D***和 **Π** 分别表示列缩放与列置换。NNSplitter、LoRO、TSQP、TransLinkGuard、ArrowCloak 等方案的代表性矩阵级权重变换，都可以在这一框架中描述。因此，在既定威胁模型下，只要能有效攻击![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaJcPGD01bWUZrvMl9c7ehTQELCoSHHGfFDB4E5R1yjvJiaGggHqW5LrxUaYONRxdhBIMLe906HCibtJtr2FqZcoL1El2PD4PZGKdxZObXaYrk/640?wx_fmt=png)，就能将同一攻击思路用于这四类算子构成的任意组合方案。

**03**

**攻击与防御设计**

**▌ 核心攻击方案：Collapse**

针对![](https://mmbiz.qpic.cn/mmbiz_png/iaJcPGD01bWXm74iclXcjEib4YtZsoolslS6NSFicMH9sa5VuETuYZMRP7Qxq6y9xGic2OH46228mznlDY0oBIWyfF9YibOaXyjKtZ3HiaGyCAdibeI/640?wx_fmt=png)，研究团队设计了攻击算法 Collapse。该算法利用混淆权重中保留的结构信息，结合公开预训练模型与少量任务数据，构建能力接近受保护模型的替代模型。具体而言，攻击者能够记录 TEE 与 REE 边界处暴露的混淆后权重，通过查询受保护模型获得标注任务数据，预算为原训练集规模的 1%。在此基础上，Collapse 通过以下三个阶段完成攻击。

![](https://mmbiz.qpic.cn/mmbiz_png/iaJcPGD01bWU65F6pbSLoOjXCLqN0PFqjTiczDEegFicMU22hAawJrNt5Sq7ibdhkr46ondn02RnjaRaFEdJPeA3Jg373FzNVbCaySKyniczdNYY/640?wx_fmt=png)

图 2 Collapse 的攻击流程

先对齐不同观测中的列，再分离低秩掩码，最后结合公开先验与少量数据完成模型提取

**第一阶段是跨视图列对齐。** 不同轮次的混淆权重虽然列顺序不同，但对应同一原始列的观测仍具有可检验的线性关系。Collapse 通过线性依赖检测（LDD）判断两组列是否对应相同的原始列集合，再逐步确定对应关系，将多个视图放到一致的列顺序中。

**第二阶段是低秩掩码恢复。** 攻击者使用四个已经对齐的视图，通过列空间的交集识别低秩掩码子空间，再利用不同视图在该子空间之外暴露的信息，联合求解相对缩放和低秩掩码分量。去除低秩掩码后，得到仍含稀疏扰动与列缩放的中间权重。

**第三阶段是先验匹配与少量数据微调。** 攻击者根据列方向与公开预训练权重的相似性恢复绝对列顺序，定位可能被稀疏掩码修改的位置，并估计列尺度。随后用公开权重初始化候选受扰位置，将各层组装为模型，再利用有限任务数据微调，最终得到替代模型。

**▌ 新型混淆算法：![](https://mmbiz.qpic.cn/mmbiz_png/iaJcPGD01bWVeRBXyRP8TGZ8xyy1SGBakCRZricGl13Y3wa89cmu0kc9OLm3sF9jX0L2t4lxavOiaZ2iaoMTff4JqDib0wBH0zRwAiadTRhibTCiac8/640?wx_fmt=png)**

Collapse 的攻击依赖于既有混淆算子保留的行列结构。针对这一问题，研究团队提出新的混淆算法 ![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaJcPGD01bWUstPqaiaES2uAwluElFp7B1VWx9ibSl00oicpR1vHKeIVuzPyy9stXdiaxNMFCkza4kgMaN5iatTJDfz4q61POghuTzO9vxXXWLR8o/640?wx_fmt=png)，通过引入新的乘性混淆算子，提升防御强度。

稀疏乘性混淆算子首先对权重矩阵的列进行混合，其混淆与计算结果恢复操作为：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaJcPGD01bWUps9JD8DX9QHZRDMJoWCiacE9OPwy7zst4hTaFw6ZDtroIIDI83elTIEk22VicfDNnfJibfuIJAYVZmWWwGmTXWozCr3baaSpsYk/640?wx_fmt=png)

其中， ***X***为输入，![](https://mmbiz.qpic.cn/mmbiz_png/iaJcPGD01bWUenrNndNribOJR0ZfKtiaME2PgEoTEtu2KZsicfXYawxmiayiajEvRiajicc13r3DEo8DUmzBAzrBbYu6ZwhicqibA3DktEstv5Kf5DH5M/640?wx_fmt=png) 为混淆权重。***M*** 是稀疏可逆的混合矩阵，使每个混淆列由少量原始列线性组合而成，破坏单列对应关系；其逆矩阵 ***M⁻¹*** 同样稀疏，以保证 TEE 还原计算结果的开销较低。

仅进行列混合时，计算结果的行结构仍被保留。双侧乘性混淆算子进一步联合变换输入与权重，同时混合权重的行与列：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaJcPGD01bWWrib6lApTWkdA9h8jAicjqSofna89ArMbguibibvVaXHVLh4KlPicBhDsV1N8H0G3n1h5MRFx7458ee4tibJ6NE4ykXR1kGNWTz06fk/640?wx_fmt=png)

其中，![](https://mmbiz.qpic.cn/mmbiz_png/iaJcPGD01bWVQkVM7YZ5uE2ukib55XOFd6YoTwOlHmllwAGoY4VFGfT5puiawXxj1uo2z7le1IwVrstTTuRgPvdbXbz4Z8wAoyaywia9PquKhv4/640?wx_fmt=png) 与 ![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaJcPGD01bWUeHLcb1VmuiakYmsO5r6plydCnoI6szZia0yxHl5JZC8MqI8Ynjm5pRyH83LoD7dhUgczHItXR9I7Nbs7eLbyocZh1bena6AFyQ/640?wx_fmt=png) 为独立采样的上述混合矩阵。输入侧的混合矩阵与权重侧对应的逆矩阵相互抵消，TEE 再去除输出侧混合，即可得到正确的计算结果。

![](https://mmbiz.qpic.cn/mmbiz_png/iaJcPGD01bWWoMK3Eictwvb5FAMkP1PUvCd4GyDdGagATcWF9LVRBel1kcEwL7yr44feG80ic9mRH6icQT0ibzf5qe0nibrfib7cu7Crx1mwoagmv0/640?wx_fmt=png)将这两类新算子与稀疏掩码、低秩掩码相结合，在 TEE 与加速器协同计算的框架下，对权重施加加性扰动和双侧混合，成功抵抗 Collapse 的攻击。

**04**

**实验验证**

研究团队通过三组实验评估攻击与防御：Collapse 攻击实验针对五种现有方案及完整组合 ![](https://mmbiz.qpic.cn/mmbiz_png/iaJcPGD01bWWrThCmafEOSQqltEyLUuU0a1U773slQibcpLq5lcrheicXmCehNuYV5Rjhw2rj0KSHwWQztSXibEZgzUK5d0LTzaBam2QS0ic9k7g/640?wx_fmt=png) 开展，并验证各攻击阶段的有效性；![](https://mmbiz.qpic.cn/mmbiz_png/iaJcPGD01bWUFY6LkyP5Qt5aUu06C2c4BwFRufmxdF7uKmghkUiaVHDYuXicBDGzRu00yy151MqTketo5XAAdM8gz6GbLWFTUPgEknzyOicWicIo/640?wx_fmt=png)防御实验比较其与现在方案在相同 Collapse 配置下的防御效果。攻击与防御实验覆盖 BERT-Base、ViT-Base、Qwen2.5-0.5B 和 Qwen2.5-1.5B 四个模型，任务包括 MNLI、QNLI、SST-2 与 CIFAR-100。任务数据预算统一为原训练集的 1%。白盒参照使用受保护模型的完整权重，黑盒参照从公开预训练权重出发，二者均在相同数据预算下微调；替代模型准确率越高，表示攻击提取的任务能力越强。

**▌****Collapse 攻击实验**

实验结果显示，Collapse 在六种受测配置下均能构建高准确率替代模型。在完整组合 ![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaJcPGD01bWUvMEPwjMz8GSvrqN1E5FdIibRSyFt3zXTkr6B6j69CCQY71uGlZRm830flORyEXhNJVDzzuEQgs4rtQ2M6UHpXwNGGZic0Y8H8Y/640?wx_fmt=png) 下，十个模型与任务组合上的平均任务准确率达到 89.97%，白盒参照为 91.11%，黑盒参照为 62.51%。这说明，在这些实验条件下，现有混淆方案的安全性难以得到保障。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaJcPGD01bWUn8ibgAgBEzlFZ8W4sbk3MTVGT5G5iaZ8wxPlibzj7g7KibmyB0KnfyBtuy3KmxbIwAYa5ZoNgrr6HQiaQf7VGereCelHvoZC8IbGc/640?wx_fmt=png)

表 2 不同模型与混淆配置下的任务准确率（%），采用单个随机种子

*𝓜obf*表示直接使用混淆权重的对照，Collapse 表示攻击后得到的替代模型

如表 3 所示，在 BERT-Base 的 MNLI 任务上，三次独立攻击的平均结果显示，相对列置换与绝对列置换的恢复准确率均为 100%，低秩掩码恢复相似度为 99.97%，稀疏扰动位置识别的 F1 值为 99.29%。这些结果表明，攻击确实恢复了关键的结构信息。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaJcPGD01bWWTvy8LHjl5MibkO9kuwfY45jicdS3m8CqVsKgq4xcY3c1kia0ibIAJPjWQzj579QEscWiarMdkWTTbjbdiaWSG70O47ckUzkTJF7LibU/640?wx_fmt=png)

表 3 Collapse 各攻击阶段的结果，BERT-Base / MNLI 上三次独立攻击的均值

**▌**![](https://mmbiz.qpic.cn/mmbiz_png/iaJcPGD01bWXC5IbJmpnjt5EVb3oCxOIArGoRwLol7IX3oZ5YuibxqOVKQutfzW2Prd1HUFDP6icjwgJjYWaiaxSXxN10Dr14ibAiamvsjdmBeMBg/640?wx_fmt=png)**防御效果**

研究团队在九个模型与任务组合上，进一步对比了扩展防御方案 ![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaJcPGD01bWXXXVKwweKKD2ssO7pKt8Ra4lNfzUamNXY9bfKId9dJF4Ee0QJVhLQAtF0MODBekLafvVKvp8FG238Zwz0msObraaRGibmfWlAE/640?wx_fmt=png) 与既有方案对照 Prior Best。在相同 Collapse 配置下，替代模型的平均准确率从 **89.67%** 降至 **62.23%**，下降约 **27.4 个百分点**。

![](https://mmbiz.qpic.cn/mmbiz_png/iaJcPGD01bWWZqGSx83KoEl5X1fzeQwMN5wqWJbJrlPPaQTjRSgtFTIKUYkb9hlibr58tzdPO6KFpCWOzZc2aZdh4EjE3ywce89IjyicNxYW8g/640?wx_fmt=png)

表 4 扩展防御方案的防御效果

Rel.Black 为替代模型准确率与对应黑盒参照的比值，Average 行为各项指标的平均值；统计范围与表 2 不同

平均相对黑盒准确率为 1.00×，表明受测攻击的平均表现接近经验黑盒参照，但各任务的防御效果仍存在差异。例如，在 Qwen2.5-0.5B 的 SST-2 任务上，这一比值仍为 1.31×。

**▌![](https://mmbiz.qpic.cn/mmbiz_png/iaJcPGD01bWUHA2xpZ0YdjDuNovuicjBFnAv9vJxYmVBzflMkNIamQT0Scg7I8n8PvOmm2Qxeu16ibEpnvG2rq3vDykf4v8cibYVK...
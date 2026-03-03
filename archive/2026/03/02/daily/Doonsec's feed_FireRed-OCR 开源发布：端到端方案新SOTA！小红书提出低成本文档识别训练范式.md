---
title: FireRed-OCR 开源发布：端到端方案新SOTA！小红书提出低成本文档识别训练范式
url: https://mp.weixin.qq.com/s/if7rvPDqf4TGPADji-Z_3g
source: Doonsec's feed
date: 2026-03-02
fetch_date: 2026-03-03T04:10:20.484847
---

# FireRed-OCR 开源发布：端到端方案新SOTA！小红书提出低成本文档识别训练范式

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/P9Hs04VFGRl5icl21zuyLgOcCyfk63n0c5phCh2A0CZkiayZ7TZibmszwHRtNGOOHPhhmIfL0xQgtvhb2wRnia5XLTFmyxFPvtZrA0On5bI2Y0o/0?wx_fmt=jpeg)

# FireRed-OCR 开源发布：端到端方案新SOTA！小红书提出低成本文档识别训练范式

原创

REDtech
REDtech

小红书技术REDtech

![]()

在小说阅读器中沉浸阅读

![](https://mmecoa.qpic.cn/mmecoa_jpg/pawZofA4fxOEVeb6Nc1R6SDW3jmnecc6nnUgffHzky2vUME58SxxKTnDKSVfLNHAqaibF9ZWqjVvp9vXQZa4U9TfU7N0Bh3rRXvdPvcKGWibU/640?wx_fmt=jpeg)

无缝兼容qwen系列加速方案，开箱即用的工业级 OCR 结构化专家。

![](https://mmecoa.qpic.cn/mmecoa_png/pawZofA4fxNuRcseNURbZVribFy3YjNKTkWTTRUGfV11885ic0aaEDiafRYSxBEfUxNPGIym4bOf9ryUsG81WXswkB0zwete7iauuk7NiaxcqRB4/640?wx_fmt=png)

图1：FireRed-OCR 及其他模型在 OmniDocBench v1.5  的结果

FireRed-OCR 研究团队今日正式宣布开源其最新一代智能文档处理模型——**FireRed-OCR**。

针对当前视觉语言模型（VLM）在处理复杂文档时普遍存在的“结构性幻觉”（Structural Hallucination）问题，该框架首创性地引入**“三阶段渐进优化”策略**与"几何+语义"数据工厂，在 Qwen3-VL-2B的基础上实现了从“语义理解”到“结构重构”的跨越式突破，**达成端到端方案SOTA**，在权威评测 **OmniDocBench v1.5**中，FireRed-OCR 凭借其卓越的结构化解析能力，综合评分及各项细分指标在诸多端到端方案中全面领跑，证明了“通用多模态模型 → 专用结构化文档模型”范式的巨大潜力。

获取资源

FireRed-OCR 现已全面开源，研究人员与开发者可通过

以下链接获代码、模型权重以及在线体验：

GitHub 项目主页：https://github.com/FireRedTeam/FireRed-OCR

Hugging Face 模型权重：https://huggingface.co/FireRedTeam/FireRed-OCR

HF Demo 体验：https://huggingface.co/spaces/FireRedTeam/FireRed-OCR

ModelScope 模型权重：

https://modelscope.cn/models/FireRedTeam/FireRed-OCR

ModelScope Demo体验：

https://www.modelscope.cn/studios/FireRedTeam/FireRed-OCR

![](https://mmecoa.qpic.cn/sz_mmecoa_png/pawZofA4fxNSWYE5z7b95aOSu9bFq53s61QhiacPI6LhVKjZQCYFFCROwxdBdgoM2NJzFrUQYQeFlan3052dAMvppyNrIc1ibtqibnDt6J2oj0/640?wx_fmt=png)

尽管 VLM 迎来了其通用的“iPhone 时刻”，但在处理财务报表、学术论文或复杂表单时，通用模型往往表现得像一位“不可靠的天才”——它们能理解图片意图，却常常在输出 Markdown 表格时错乱行列，或凭空创造不存在的语法。这种“懂意图，不懂规矩”的现象被称为**结构性幻觉**。

FireRed-OCR 的核心理念在于使用任务难度逐步提升的三阶段渐进式优化策略，使得原本输出结构不稳定的通用VLM在学习中理解文档解析任务的内在逻辑，最终实现在面对复杂的文档布局时可以兼具输出内容的高准确性和高结构正确性。

![](https://mmecoa.qpic.cn/mmecoa_png/pawZofA4fxPEnnticWBY6qcnwcpbPJ8j118TqDvibgOicM5YokR92TE9VzfzH4Yh9GBGqvfq1ZzziaVo3gicqPXZynQ3n8UQGHst4yzMDw1ndzg0/640?wx_fmt=png)

图2：FireRed-OCR 三阶段训练流程

**技术架构：三段式进化路径**

FireRed-OCR 基于 Qwen3-VL 架构，通过以下三个精密耦合的阶段完成“驯化”：

**Stage 1：多任务 OCR 预对齐（Multi-task Pre-alignment）** 这是模型的“基础课”。模型不再直接生成最终结果，而是并行学习**检测框、区域识别**与**全图解析**任务。通过三个互补任务建立对文档的物理感知：

* **检测框列举及 OCR**：输出所有检测框及其文本，强化定位能力。
* **指定区域 OCR**：对给定坐标区域进行精确识别。
* **全图 OCR**：初步尝试整页文档的 Markdown 输出。

这一阶段成功将模型关注点从通用图文理解迁移至“文本定位 + 内容识别 + 结构表达”的 OCR 垂直领域。这一阶段不仅教会模型“识字”，更重要的是建立像素级的空间坐标感，让模型学会区分“哪里是字，哪里是图”。

**Stage 2：全图 Markdown 专项 SFT（Specialized SFT）** 在具备空间感知后，模型进入“专业课”阶段。系统聚焦于**全图 Markdown**输出，通过监督微调（SFT）强化模型在跨语种、复杂布局下的**结构一致性**与**层级表达稳定性**，确保 Markdown 格式规范，不再出现“胡编乱造”的语法。

**Stage 3：基于约束的 GRPO 强化学习（Format-Constrained GRPO）** 这是 FireRed-OCR 的“点睛之笔”。团队引入了强化学习机制，重点约束：

* **公式语法合法性**
* **层级结构闭合性**
* **表格结构完整性**
* **文字内容准确性**

通过这一阶段，模型被赋予了“自我纠错”能力，显著减少了复杂文档中的格式偏移，实现了工业级的输出稳定性。

![](https://mmecoa.qpic.cn/sz_mmecoa_png/pawZofA4fxMEibxuLMDFXFIavzx2ia32494hl3YIQXEJb9PgQVGendw0ZvlJhicJZATz0iaoun021uKfLwSs6mWy7ryomqP5aymkMJ8FDmibwtLQ/640?wx_fmt=png)

![](https://mmecoa.qpic.cn/sz_mmecoa_png/pawZofA4fxPXfTf8aZyd38c83jiap4h65oicUcZb880NHBgLKnjqKOndSyWPoAyg41hg2L3icc7XeCibshZyIBVPxBiaf8gAOvTnd2siaEIMce5VY/640?wx_fmt=png)

图3：FireRed-OCR 训练数据生产流程

为了支撑上述高精度的训练，FireRed-OCR 构建了一座自动化、可扩展的数据生产工厂，通过五大核心步骤实现了从源头对数据质量的极致把控而非堆数量。值得注意的是，这条流水线上的绝大多数环节都由开源模型构成，极大降低了数据生产成本：

**1. 几何特征驱动与多维 Tag 体系**

传统的随机采样难以保证数据分布的合理性。我们引入了**“几何+语义”双重索引机制**：

* **几何聚类：**利用传统图像编码器提取文档的**几何结构特征**并进行聚类，精准识别数据集间的结构重叠、稀缺版式及高度相似的冗余数据。
* **多维 Tag 体系：**构建包含语种、页面布局、文档来源及文体类型（论文/发票/合同等）的标签体系，弥补了几何特征的不足，使数据分布**可解释、可调控、可均衡**。

**2. 均衡采样与统一重标注**

基于上述分析，系统执行**分层均衡采样**，确保语种分布合理、布局类型均衡、长尾结构得到保留与稀缺类型不被淹没。随后，我们利用 **PaddleOCR-VL**对所有数据进行了统一风格的**Markdown 重标注**（在此特别致谢 Paddle 团队的优秀工作），消除了不同来源数据的标注风格冲突，确保 Markdown 风格一致、表达规范统一、标注标准一致，为模型收敛提供了标准化的“高质燃油”。

**3. 稀缺数据合成**

针对数据分布中缺失的类型，系统搭建了基于 HTML 母本的**图像渲染合成链路**，人工合成稀缺数据。

**4. 自动化质量控制与难样例沉淀**

在训练前引入**双重质量检测流程**：

* **自动化质检：**检测 Markdown 层级闭合、表格完整性及重复/乱码问题。
* **大模型内容审核：**辅助审核文本质量，将不合格数据将进行二次分类：空白样本、高度模糊图像、内容严重缺失。不合格样本中，“明显无效”的被丢弃，而“高难错题”被纳入 **Hard Case 库**。

**5. 专家级修正**

为了挖掘高难样例的价值，我们引入 **Gemini 3.0 Pro**  等外部高精度模型对少量 Hard Case 库中的数据进行**辅助标注修正**。这一步骤有效修复了关键结构错误并提升了复杂页面的 GT（Ground Truth）精度，减少系统性偏差，通过“专家会诊”极大提升了高价值样本的训练效能。

![](https://mmecoa.qpic.cn/mmecoa_png/pawZofA4fxMVSTVeVIibMKkuhgMoVy7x0ibfKWULVDMBAVTBibb90AsE5N37Z6vSq3tHGulzouGnuU6h6UKVZ7kT3ybKWc2CJkFFVKm4z1xmFM/640?wx_fmt=png)

OmniDocBench v1.5 榜单端到端模型首位，在综合评分及各项细分指标上全面领先。

![](https://mmecoa.qpic.cn/mmecoa_png/pawZofA4fxNuRcseNURbZVribFy3YjNKTkWTTRUGfV11885ic0aaEDiafRYSxBEfUxNPGIym4bOf9ryUsG81WXswkB0zwete7iauuk7NiaxcqRB4/640?wx_fmt=png)

图4：FireRed-OCR 及其他模型在 OmniDocBench v1.5  的结果

FireRed-OCR-2B在与DeepSeek-OCR 2、OCRVerse、dots.ocr 等顶尖闭源/开源端到端模型的同台竞技中展现了统治级表现：

* **综合评分 (Overall)：**FireRed-OCR 是**唯一突破 92% 准确率阈值**的端到端模型（**92.94%**），显著优于 DeepSeek-OCR 2（第二名, 91.09%）及 OCRVerse，确立了当前文档解析领域的 SOTA 地位。与 Qwen3-VL-2B 相比，FireRed-OCR-2B 提高了 11.07 分，显著优化了文档解析能力，证明了“通用多模态模型 → 专用结构化文档模型”范式的巨大潜力。
* **文本识别 (Text Score)：**在纯文本识别维度，得益于高质量的数据清洗与多任务预对齐，模型得分高达 **96.8%**，展现了像素级的字符识别精度。
* **结构化能力 (Formula & Table)：**这是 FireRed-OCR 核心优势的集中体现。

  **·公式解析 (Formula CDM)：**得益于 GRPO 对语法合规性的强约束，得分达 **91.71%**，大幅领先于 DeepSeek-OCR 2 和 OCRVerse。

  **·表格重构 (Table TEDs)：**在最考验逻辑的表格还原任务中，模型得分达 **90.31%**，证明了其在复杂行列对齐中的鲁棒性。
* **阅读顺序 (R-order Score)：**凭借几何特征驱动的训练，模型在理解文档逻辑顺序上表现完美，得分达 **95.9%**，有效解决了多栏排版下的阅读乱序问题。

![](https://mmecoa.qpic.cn/mmecoa_png/pawZofA4fxMxm4k4wv2o1SMwJNj2VriaPrJGFnrnGexEPdVUSnje72W4F6QHPFicrtKSf1rVrssnIsf0BHNqq9r0sNLfEAM2ZKH8e98TNfI80/640?wx_fmt=png)

**Case 1：极致的数学公式解析能力——从像素到LaTeX的完美转译**

**【场景挑战】**在教育科技（EdTech）与学术科研领域，数学公式的数字化一直是个难题。传统的 OCR 技术往往只能识别文本，面对包含极限（limit）、分数叠加、导数符号等复杂的微积分公式时，容易出现乱码或结构错位，无法还原公式的数学逻辑。

**【模型表现】**本模型展示了卓越的**公式结构化提取能力**。面对图中《The Product Rule》（乘法法则）的教学课件，模型不仅精准识别了“The Product Rule”等标题文本，更关键的是，它**完美解析了复杂的微积分推导过程**。

即使是 limΔx→0 这种包含上下标、希腊字母以及多层分数的复杂结构，模型也能将其精准转化为标准的  LaTeX 格式或 Markdown 公式。这意味着模型不仅仅是“看见”了符号，更是“理解”了数学语言的空间结构，为理科教材的数字化和智能搜题提供了坚实的技术底座。

输入图片与模型输出（渲染后结果）

![](https://mmecoa.qpic.cn/mmecoa_png/pawZofA4fxMG6zjwhl9ts14YIe7CQ4yibQUXJedyCia34LwlNepAuzecCG0WUGbI7ZXEf7dQibvILCJe91licAjwOwvjcgS8YMO0yfCicKUZpDDY/640?wx_fmt=png)

![](https://mmecoa.qpic.cn/mmecoa_png/pawZofA4fxPibYzwrtsbRm9yd2fAPLgo6LFiaLCM0MwSquMAk5ia8HtNCMDMD1fQibj3IF54noWiamqrssv5dXkZNLsZP1zXz5Nx7IPDeXnnib8u4/640?wx_fmt=png)

**Case 2：打破“印刷体”限制——高鲁棒性的手写体识别**

**【场景挑战】**真实世界的数据并不总是整洁的印刷体。会议白板记录、学生作业、医生处方等场景中充斥着潦草的手写文字。手写体字迹千人千面，连笔、倾斜、涂改极易导致AI识别失败。

**【模型表现】**本 Case 展示了模型在手写体识别领域的强悍实力。面对这张在横格纸上的英文手写笔记，尽管字迹存在连笔和个人书写习惯的差异，模型依然保持了极高的召回率和准确率。

它能够精准分离背景横线与笔迹前景，顺畅地读取出段落内容。这种能力证明了模型在“非结构化文档”处理上的通用性，使其能够轻松应对办公自动化中的会议记录归档或作业智能批改等高频需求，真正做到了“见字如面，精准还原”。

输入图片与模型输出（渲染后结果）

![](https://mmecoa.qpic.cn/sz_mmecoa_jpg/pawZofA4fxOEyicpOs47xx2EQjicBh2MObcpUGbSkTpXB7SNFbVjUvkoAtXwhT4wFUwu53wK7JnrJiaGKoklic8ZZxTZdwnOYGEsjlUQXQHQQEY/640?wx_fmt=jpeg)

![](https://mmecoa.qpic.cn/sz_mmecoa_png/pawZofA4fxP7eeN7tqv5vJW3hznYfSWibJVV8ZNvseqPNEqHz3donR6EZZdxJ3AOibJdiak8oicE6C3plYyv3npUZtNFDgA9KJjV6NyzHapVpsg/640?wx_fmt=png)

**Case 3：跨越时空的版面理解——复杂报纸文档的重构**

**【场景挑战】**报纸、古籍等文档往往采用复杂的混合排版：竖排文本、横排标题、图片穿插以及多栏分块。普通模型在处理此类文档时，常常搞错阅读顺序（Reading Order），将不同栏目的文字混在一起，导致语义支离破碎。

**【模型表现】**在这张中文报纸的识别中，模型展示了业界领先的**版面分析（Layout Analysis）能力**。它准确识别出了报纸特有的**竖排文本**，并正确处理了中文阅读习惯中的“从右向左、从上到下”的逻辑顺序。

同时，模型成功区分了标题区、正文区和图片区，没有受困于复杂的分割线。这表明模型具备极强的**文档结构认知**，不仅能“读字”，更能“看懂版面”，对于档案数字化、历史文献修复以及金融公告处理具有不可替代的价值。

输入图片

![](https://mmecoa.qpic.cn/mmecoa_jpg/pawZofA4fxMt3Vv6te2uq2BsKyJst1MU2AZMzibMuILD1YKl0Va8V0n5QXCibRbUUPhDvDaR0JcTzYQicg0L2mhCuLAX8JBbIBXcicEyTLxJWQM/640?wx_fmt=jpeg)

模型输出（渲染后结果） 向下滑动查看

![](https://mmecoa.qpic.cn/mmecoa_png/pawZofA4fxNZ20VLCMxPibZoooIiaaLHCkZxZpYDB7gacnwwEI6215YBPKFvyhqRa3qe4UF42xFXibEUTeCv4ticfCkfPEzErvuEVtuIBPBV2Pw/640?wx_fmt=png)

**Case 4：数据资产的精准解锁——复杂表格结构还原**

**【场景挑战】**表格是商业报告中信息密度最高的载体。然而，包含合并单元格、跨行表头、背景色填充的复杂表格，一直是机器解析的噩梦。一旦结构识别错误，提取出的数据将失去关联性，变得毫无价值。

**【模型表现】**本模型通过对这张包含多层级表头的 PPT 表格进行处理，证明了其表格结构还原的硬实力。模型不仅准确提取了单元格内的细微文字，更精准还原了表格的行、列对应关系。

无论是跨列的总体标题，还是细分的子项目，模型都能构建出正确的逻辑树。这意味着企业在进行年报分析、合同审核或 RPA 自动化流程时，可以直接将非结构化的图片转化为可编辑的 Excel 或结构化数据库，极大地释放了数据...
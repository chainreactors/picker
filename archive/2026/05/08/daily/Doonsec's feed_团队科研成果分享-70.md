---
title: 团队科研成果分享-70
url: https://mp.weixin.qq.com/s/2URBvaMmlt-NG6lgIMmp1g
source: Doonsec's feed
date: 2026-05-08
fetch_date: 2026-05-09T05:03:58.736699
---

# 团队科研成果分享-70

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/jBQAokCLibp1eicZhdfoaNAqwkSzrFO0duFxKtbOBLv44p8ibwwdeibSd9SuCUSdca6w8k0pdK9HOTTOXwlibC7Eia8hh4IUV655UJjKbNwuBWngU/0?wx_fmt=jpeg)

# 团队科研成果分享-70

网络与安全实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/jBQAokCLibp09lTzzQBARqsWgj9gciaVHJpTj7BgwMHpIfT1RiauiagyQL3MiaKFibLl9UlBrtIksibncuTypHlUib06Pu3AqvQWRrXUcrn1jfg7DS8/640?wx_fmt=jpeg&from=appmsg)

**团队科研成果分享**

2026.05.04-2026.05.10

**标题:**Swin-Transformer-based JSCC Exploring Detail-aware Enhancement and Progressive Semantic Fusion in Wireless Image Transmission

**期刊:**IEEE Transactions on Network Science and Engineering (Early Access), Date of Publication: 9 April 2026.

**作者:**Zhongyu Ma,Hua Liang,Jizhe Zhang, Zhenyu Wei,Xunan Jin, Zhaobin Li, Yan Zhang.Guangjie Han

**分享人:** 梁华

**01**

**研究背景**

**BACKGROUND**

**研究背景**

随着远程医疗、沉浸式体验、具身智能等多样化应用兴起，高清图像、视频及大规模计算任务的高效可靠传输对现有无线技术提出巨大挑战。传统通信架构基于香农定理，将信源编码与信道编码独立设计，前者用于消除原始信息冗余，后者抵御无线信道噪声干扰，理论上可在不损失系统效率的前提下达到香农极限。但该设计存在明显局限：其实现前提是信息块趋近无限长度，与实际应用场景不符；且传统设计追求比特级精度、平等对待所有数据，在传输高冗余但语义丰富的数据时，效率低下问题突出。在此背景下，作为联合信源信道编码（Joint Source-Channel Coding,JSCC）的语义通信，成为突破上述局限、实现从符号中心传输向任务导向传输范式转变的潜在方案。基于深度学习的JSCC可在压缩信息的同时保留语义特征，大幅降低延迟与带宽消耗，在可靠性和效率上展现出超越传统通信系统的巨大潜力，相关研究具有重要现实意义。

**02**

**关键技术**

**TECHNOLOGY**

**关键技术**

本文面向JSCC在高分辨率图像无线传输中存在的细节退化、跨层级语义不一致问题，尤其针对低信噪比、高压缩场景下的细节丢失与语义失配痛点，研究如何在低计算复杂度前提下，提升语义通信系统的特征表示能力与信道适应性。为此，文章提出DSF-JSCC架构，以Swin-Transformer作为语义编码器与解码器的核心骨干，通过设计细节感知增强模块(Detail-Aware Enhancement Module,DAEM）和渐进式多尺度语义融合模块(Progressive Multi-level Semantic Fusion,PMSF），构建端到端的语义传输框架，实现高分辨率图像在复杂信道环境下的高质量重建。

在方法上，DSF-JSCC以Swin-Transformer为基础骨干，通过堆叠Swin-Transformer块实现长距离依赖表示与层级特征提取；DAEM模块作为骨干网络的重要组成，采用一组并行的深度可分离卷积分支实现多尺度感知，重点捕捉和重建高分辨率图像的纹理、边缘等精细细节；PMSF模块级联在骨干网络之后，通过空间对齐、分辨率匹配和自适应加权融合的序贯设计，对不同层级提取的语义特征进行智能整合，弥补不同阶段的语义差距，实现全局语义一致性与细节保真度的平衡。同时，通过峰值信噪比（Peak Signal-to-Noise Ratio，PSNR）、多尺度结构相似性指数（Multi-Scale Structural Similarity Index，MS-SSIM）和感知图像块相似性（Learned Perceptual Image Patch Similarity，LPIPS）等指标，对系统性能进行全面评估，验证其优越性。

基于上述内容，本文的创新点可概括为：

1）新型JSCC架构设计：针对现有Transformer-based JSCC的固有缺陷，提出DSF-JSCC架构，以Swin-Transformer为核心骨干，整合DAEM和PMSF模块，构建端到端传输框架，有效解决细节退化与跨层级语义不一致问题。

2）细节感知增强模块（Detail-Aware Enhancement Module,DAEM）：设计DAEM作为Swin-Transformer块的关键组件，通过并行深度可分离卷积实现多尺度感知，提升复杂信道下高分辨率图像的细节捕捉与重建能力。

3）渐进式多尺度语义融合模块（Progressive Multi-level Semantic Fusion,PMSF）：提出PMSF模块，通过空间对齐、分辨率匹配和自适应加权融合，充分挖掘骨干网络不同阶段的多层级语义信息，弥补跨阶段语义差距，提升重建图像的全局语义一致性与视觉质量。

4）全面性能验证与对比：通过多指标、多场景的实验，将DSF-JSCC与传统分离式信源信道编码方案及Deep-JSCC、Swin-JSCC等新兴JSCC方法对比，验证其在不同信道条件下，能实现像素级重建保真度与感知视觉质量的优越平衡。

**03**

**算法介绍**

**ALGORITHMS**

**算法介绍**

**算法1的思想（细节感知增强模块）**

![](https://mmbiz.qpic.cn/mmbiz_png/jBQAokCLibp0eBCr4MKcJTxnTXe9vDjJvkIrVtgKIkjUQOFDT8EoScgfpjldmpr88aB3lnrxpxJcyZpIPrHuZibX5LibvJJIxr4YwKib9efIHZc/640?wx_fmt=png&from=appmsg)

算法1

细节感知增强模块是DSF-JSCC架构的关键组件，其核心功能是提升复杂信道下高分辨率图像的细节捕捉与重建能力，模拟人类视觉对细节的敏感性。该算法以输入特征为基础，先通过层归一化和自适应调制对特征进行预处理，再将特征投影到紧凑空间；随后通过多组不同卷积核的并行深度可分离卷积提取多尺度特征，结合全局平均池化获取特征全局统计信息，利用注意力机制计算各尺度特征的权重并进行自适应融合；最后通过逐点卷积实现信道交互、维度恢复，再与原始输入特征残差连接，输出增强后的特征，为高分辨率图像语义传输中的细节保留提供支撑，是DSF-JSCC架构解决细节退化问题的核心技术之一。

**算法2的思想（渐进式多尺度语义融合模块）**

渐进式多尺度语义融合模块是DSF-JSCC架构的核心模块之一，其核心功能是挖掘Swin-Transformer不同阶段的多层级语义信息，弥补跨阶段语义差距，提升重建图像的全局语义一致性与视觉质量。该算法以Swin-Transformer输出的多层级特征图为输入，首先通过信道投影将所有层级特征统一到相同维度；随后初始化相邻两层特征的融合结果，再通过渐进式迭代过程，依次对融合结果与下一层级特征进行空间对齐（基于可变形对齐操作预测偏移量并完成对齐）、分辨率匹配（通过上/下采样调整空间尺寸）、自适应加权（利用评分函数计算动态权重并完成加权融合）；经过多轮迭代融合后，输出最终的融合语义表示，为解决现有Transformer-based JSCC的跨层级语义不一致问题提供关键支撑，与DAEM模块协同保障DSF-JSCC的传输性能。

![](https://mmbiz.qpic.cn/mmbiz_png/jBQAokCLibp3Llu7ibe6HTGm2FkBqV5unQnGlb7oh0uaxZJicHpKXCEWJp4hC4ePo5pPkxz3UUXo1nmOUp7UmuF92Nkwcic5icyg6Mm8otFHz72w/640?wx_fmt=png&from=appmsg)

**04**

**实验结果**

**EXPERIMENTS**

**实验结果**

**1. 实验设置：**

数据集：兼顾低分辨率与高分辨率场景，分别用于验证模型的基础语义传输能力与实际场景适配性：低分辨率场景采用CIFAR10数据集作为训练与测试集，评估模型基础性能与泛化能力；高分辨率场景以DIV2K数据集为训练集（含800张2K分辨率各类场景图像，训练时随机裁剪为256×256补丁，不采用额外数据增强以保证对比公平），以Kodak数据集（24张高质量自然图像）和CLIC2021数据集（含多种难压缩特性图像）为测试集，测试时将两类测试集图像分辨率统一调整为128的整数倍，消除尺寸不匹配干扰。

对比方案：设计多组对照实验，涵盖传统编码与新兴JSCC方法，并通过消融实验验证核心模块的有效性：

BPG+LDPC：作为传统分离式信源信道编码代表，采用BPG图像压缩为信源编码、LDPC为信道编码，结合不同编码率与QAM调制模拟实际无线信道。

Deep-JSCC：CNN基JSCC方法，是实现发射机与接收机联合设计的开创性工作。

Swin-JSCC：Swin-Transformer基JSCC方法，引入注意力机制以增强特征提取能力。

**2. 实验结果图**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jBQAokCLibp0xk86w8mk6eibxj2ZOwN4LXugHz81PB4KNJrfSAfI5xWmGoA5nyiaJNhfibjlYFLgERASeXd8vf5lR7G0hHJmmr5odicYEHLIib230/640?wx_fmt=png&from=appmsg)

图1 不同信噪比下PSNR性能对比

图1展示了在高斯白噪声信道和瑞利信道下，所提DSF-JSCC框架与其他对比方案在不同信噪比条件下的峰值信噪比性能对比。可以看出，在两种不同信道环境下，所有算法的峰值信噪比均随信噪比的提升而升高。显然，在两种信道中，当信噪比处于较低水平时，所提DSF-JSCC框架的峰值信噪比均高于其他对比方案，凸显了该框架及其对应变体在应对复杂信道环境时的优越性。在低分辨率数据集上，所提DSF-JSCC相较于深度联合信源信道编码方法实现了一定程度的性能提升，相较于传统分离式编码方案的性能提升更为显著。需要注意的是，在信噪比处于较高水平时，传统分离式编码方案的峰值信噪比表现更为优越。此外，DSF-JSCC的峰值信噪比与仅集成渐进式多尺度语义融合模块的变体较为接近，这体现了所提DSF-JSCC与该变体在不同信噪比水平和信道环境下均具备较强的鲁棒适应性，这主要得益于渐进式多尺度语义融合模块的设计，使得图像在高斯白噪声信道和瑞利信道中均能实现有效的传输与重建。

![](https://mmbiz.qpic.cn/mmbiz_png/jBQAokCLibp3aiarVylRcPTRCsHS7lQmv5tyyTQwSn7XSh4W2rDGK48oFCYgyxROxM0lMl5ZjfD9fjBdJMXDxh6dzofO5mFuyicBd6jQia35eo8/640?wx_fmt=png&from=appmsg)

图2 不同压缩比下PSNR性能对比

图2展示了在高斯白噪声信道和瑞利信道下，所有框架在不同信道带宽比条件下的性能增益对比，旨在进一步评估各框架在不同传输效率下的表现。总体而言，所有框架的峰值信噪比均随信道带宽比的提升而升高，所提DSF-JSCC框架及其变体在所有考虑的数据集、两种信道环境下，峰值信噪比均优于其他对比基准方案。尤其在瑞利信道条件下、带宽受限场景中的低分辨率图像传输中，DSF-JSCC的性能显著优于传统分离式编码方案，其性能优势主要源于两方面：一是新兴的联合信源信道编码设计相较于传统分离式编码方案，对各类信道具备更强的适应性；二是与CNN和Swin Transformer的联合信源信道编码方法相比，DSF-JSCC通过细节感知增强模块和渐进式多尺度语义融合模块，实现了细节感知与多层级语义融合的平衡。此外，在高分辨率图像传输中，DSF-JSCC在不同信道带宽比条件下均能实现性能提升，相较于深度联合信源信道编码方法保持着稳定的性能优势，但当信道带宽比足够高时，其峰值信噪比略逊于传统分离式编码方案，这表明高度优化的传统分离式编码方案在近理想信道条件下仍具备优势。

![](https://mmbiz.qpic.cn/mmbiz_png/jBQAokCLibp1dTqrj5CSE3BvVaBcRtfiaVEzllAfDIbEpYtr0RblKh6zGf6LA0SkBCPibS0NichymiaNQpmu42QUOIhcicia2libZfxWRLEB4QPhE8g/640?wx_fmt=png&from=appmsg)

图3 不同场景下MS-SSIM性能对比

为全面评估框架的图像重建性能，图3展示了各框架在不同场景下的多尺度结构相似性指数对比，该指标相较于峰值信噪比更贴近人类主观视觉感知，能更直观地反映原始图像与重建图像的结构相似性，其数值范围通常在0到1之间，数值越接近1表示结构相似性越高，为便于展示趋势，已将其转换为分贝尺度，且实验仅考虑高斯白噪声信道以方便分析。从图3可以看出，所有方案的多尺度结构相似性指数均随信噪比和信道带宽比的提升而升高。但在高分辨率数据集上，传统分离式编码方案的多尺度结构相似性指数表现不如所有联合信源信道编码类方案，这是因为该方案中选用的图像压缩方法属于均方误差最小化设计。所提DSF-JSCC的多尺度结构相似性指数相较于传统分离式编码方案有明显提升，相较于深度联合信源信道编码方法也具备显著优势。此外，基于Swin Transformer的联合信源信道编码类方案的多尺度结构相似性指数始终优于基于卷积神经网络的深度联合信源信道编码方法，这得益于前者更强的特征提取能力。其中，所提DSF-JSCC及其仅集成细节感知增强模块的变体，其多尺度结构相似性指数均高于原始Swin Transformer联合信源信道编码，这归功于细节感知增强模块有效提升了重建图像的主观质量。总体而言，所提DSF-JSCC完美实现了像素级误差与人类视觉感知之间的平衡，这一点从其在峰值信噪比和多尺度结构相似性指数上的良好表现中得到了充分体现。

![](https://mmbiz.qpic.cn/mmbiz_png/jBQAokCLibp1lpbw9Kt3ic5YrdvItdJ3F8XsbUBXnBibaU7ibg99HRB5JbZ5K6pU1k1ovJH2CDH4mWvsY1naky6WbTOX3tJ1wbCeYAaibkjiaWXT8/640?wx_fmt=png&from=appmsg)

图4 不同场景下LPIPS性能对比

为全面评估重建图像的感知质量，图4展示了各框架在不同场景下的感知图像块相似性指数对比，该指标的数值越低，代表原始图像与重建图像的感知相似性越高，实验仅考虑高斯白噪声信道以方便分析。从图4可以看出，所有方案的感知图像块相似性指数均随信噪比和信道带宽比的提升而降低。在高分辨率数据集上，传统分离式编码方案的感知图像块相似性指数高于所有联合信源信道编码类方案，与之相反，所提DSF-JSCC的感知图像块相似性指数始终低于传统分离式编码方案，明显体现出其在感知质量上的显著提升。此外，基于Swin Transformer的联合信源信道编码类方案的感知图像块相似性指数表现始终优于基于卷积神经网络的深度联合信源信道编码方法，其中所提DSF-JSCC的感知图像块相似性指数相较于深度联合信源信道编码方法有明显降低，感知质量优势突出。同时，仅集成渐进式多尺度语义融合模块的变体和仅集成细节感知增强模块的变体，其感知图像块相似性指数表现均优于原始Swin Transformer联合信源信道编码。

**05**

**总结**

**CONCLUSION**

**总结**

本文提出了用于高分辨率图像语义传输的DSF-JSCC框架，以Swin-Transformer作为核心骨干，并设计了DAEM和PMSF两个专用特征增强模块，用于克服高分辨率图像传输中细节重建和语义保留方面的性能瓶颈，增强多尺度空间维度下关键语义信息的建模与重建能力。与传统BPG+LDPC方案及新兴的Deep-JSCC、Swin-JSCC相比，DSF-JSCC在不同信道条件下均表现出更优越的图像重建性能，即使在高压缩比或低信噪比条件下，也能保持高质量、高保真的重建效果；未来研究将重点关注参数高效、计算友好的轻量化架构，以推动语义通信在智能系统中的实际部署。

**END**

![](https://mmbiz.qpic.cn/mmbiz_jpg/jBQAokCLibp2icLg8icarqkxbTmLjIZqqeg5HJjokfWib8IibgZf5gMMiahYnELCIgMNEia0kCsaD9Tbuyn5icqrrUZ0zG8wRibRN0LzpmpuBll0Hvs8/640?wx_fmt=jpeg&from=appmsg)

扫描二维码关注我们

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/ASlHg58pYMe1HLLDN2MwVD3d9iaphI4Evp3oib9RPtU2gOR3ubr5qzibTwSBgaJgJ52tuI5knfsB9ECKibfibAt40KA/0?wx_fmt=png)

网络与安全实验室

向上滑动看下一个

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ASlHg58pYMe1HLLDN2MwVD3d9iaphI4Evp3oib9RPtU2gOR3ubr5qzibTwSBgaJgJ52tuI5knfsB9ECKibfibAt40KA/0?wx_fmt=png)

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
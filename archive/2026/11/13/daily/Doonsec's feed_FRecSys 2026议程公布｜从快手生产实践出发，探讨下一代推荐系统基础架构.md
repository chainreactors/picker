---
title: FRecSys 2026议程公布｜从快手生产实践出发，探讨下一代推荐系统基础架构
url: https://mp.weixin.qq.com/s/H_ABIf_weU9Z2lcAtkFG5g
source: Doonsec's feed
date: 2026-11-13
fetch_date: 2026-11-14T08:14:34.469832
---

# FRecSys 2026议程公布｜从快手生产实践出发，探讨下一代推荐系统基础架构

# FRecSys 2026议程公布｜从快手生产实践出发，探讨下一代推荐系统基础架构

原创

快手技术
快手技术

快手技术

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/ZxDY5TMPs0EqL7dlyXD8OFyXn6yNGvQ8uEibL6TkOHqFvaK0bR9GEhZicTHuDtaTficMGS88ecXKIVPnFJCTMz7aQ/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0)![]()![]()![]()![]()![]()

11 月 15 日，首届前沿推荐系统研讨会 FRecSys 2026 将在香港沙田凯悦酒店与 ACM SIGOPS ATC 2026 同期举行。香港大学计算机系助理教授、Cloudless Computing Lab 负责人邱一鸣，北京航空航天大学副教授、国家级青年人才杨任宇，以及快手技术副总裁、算法引擎部负责人杨晨，共同担任本届研讨会大会联合主席。

本届研讨会共收录了13篇论文，覆盖生成式推荐推理与服务、训练系统与智能体优化，作者来自快手、Meta、阿里巴巴、小红书及多所高校。研讨会论文集计划纳入 ACM ICPS，并在 ACM Digital Library 出版。其中，快手团队共有5篇论文入选，将在现场分享生成式推荐推理与解码、RL 后训练权重同步及智能体优化等方向的研究成果。

* 研讨会官网：https://atcworkshop-rec.github.io/
* 联系邮箱：frecsys26@googlegroups.com

具体议程如下：

![](https://mmbiz.qpic.cn/mmbiz_png/1gVUsotpT1XkOlTicmibpmDEeRecA1JZpH5gSZeg0vAAeO9gm86O0K5fIsBCfO3nLGLtXXYKicjC0un3U3N7ic2SAuAZzMQSqLj2fuVmQdic94Xg/640?wx_fmt=png&from=appmsg)

图：FRecSys 2026议程

短视频、广告和电商等场景，长期考验着推荐系统在高并发、低延迟下的吞吐效率、算力成本、服务稳定性与实时响应能力。随着生成式推荐和大模型驱动的推荐逐步进入实践，新的挑战也随之而来：如何高效完成生成式推理，如何在十亿级物料库中进行请求约束解码，如何支撑训练与服务的持续演进？

快手近两年推动推荐系统向生成式推荐、LLM 驱动的推荐演进，研发并落地了 OneRec 等系列模型及面向生成式推荐的训推引擎。这些来自真实生产环境的问题，也是快手参与举办首届前沿推荐系统研讨会 FRecSys 2026 的出发点：让工业实践与学术研究相互碰撞，推动更贴近生产约束的基准、评测方法与开放议题。

「论文亮点解读」

过去，推荐系统基础设施围绕“召回—排序”流水线、大规模 Embedding 表、特征平台与 DLRM 式服务架构演进；如今，生成式推荐、基础模型、多模态与智能体等新范式，正在重新提出三个问题：算什么、怎么建、怎么服务？这也是本届研讨会的主线。

* 生成式推荐推理，进入“细节决定效率”的阶段：第一场论文环节的 8 篇报告中，6 篇直接面向生成式推荐。其中，OneLA、RIG、Taming Wide Beams 与 FSBO 围绕生成式推荐的推理与解码效率展开，涉及大束宽解码、推理框架，以及词表投影与候选选择融合等问题；另外两篇分别讨论语义 ID 的服务架构，以及十亿级物料库上的请求约束解码。

* 从新硬件到新方法，讨论不止于推理：第一场论文环节将讨论基于 CXL 内存池的向量检索，以及昇腾 NPU 上的 LLM 服务性能预测；第二场则进一步关注推荐训练系统、RL 后训练中的权重同步，以及借助 Agent 优化系统的方法。

* 真实生产约束，走进学术讨论：13篇论文均有企业作者参与，其中4篇作者均来自企业，9篇由高校与企业共同署名。

快手团队入选的5篇论文——OneLA、Taming Wide Beams、FlagCD、KAISync 和 RobustSGPO——分别围绕推理效率、约束解码、权重同步与智能体优化展开。FRecSys 2026 也希望以这些具体问题为切入点，促进系统领域与推荐领域的交流合作，推动更贴近真实负载的基准、Trace 与评测方法等共享资源建设，让研究更严谨、更可复现。

Session 1｜生成式推荐的高效解码

09:10–10:00

论文1｜OneLA: Scaling Linear-Attention Decoding to Large Beams in Generative Recommendation

作者单位：香港大学、快手、北京大学

论文2｜RIG: GPU Inference Framework for Long-Context, Short-Decode, Large-Beam Generative Recommendation

作者单位：NVIDIA

论文3｜Taming Wide Beams: Request-Adaptive Inference for Generative Recommendation

作者单位：中国人民大学、南京大学、快手

论文4｜FSBO: Fusing Vocabulary Projection and Beam Selection for Efficient Generative Recommendation

作者单位：郑州大学、中科曙光、清华大学

论文5｜FlagCD: Exact Request-Constrained Decoding over Billion-Scale Item Catalogs

作者单位：北京大学、香港大学、快手

Session 2｜训练、推理和Agentic阶段优化

10:30–11:50

论文1｜Token-Native Serving Architecture for Generative Recommendation with Semantic IDs

作者单位：Meta

论文2｜ServerlessANN: Low-Latency Serverless Vector Search with CXL Memory Pools

作者单位：华中科技大学、小红书

论文3｜NaviPerf: Architecture-Aware Performance Prediction for LLM Serving on Ascend NPUs

作者单位：北京航空航天大学、小红书

论文4｜RecIS: Unifying Sparse and Dense Computation for Efficient Recommendation Training

作者单位：阿里巴巴、中国科学院大学

论文5｜SparseRec: Predictive GPU Sharing and Data-Aware Scheduling for Recommendation Model Training

作者单位：北京航空航天大学、小红书、利兹大学

论文6｜KAISync: Characterizing and Optimizing Weight Synchronization in Co-Located RL Post-Training

作者单位：北京航空航天大学、快手

论文7｜TALOS: Torch Acceleration through a Loop-Driven Optimization Skill for Recommendation Systems

作者单位：NVIDIA

论文8｜RobustSGPO: Search-Space Control for Agent Harness Evolution

作者单位：快手

「快手技术展台」

11 月 16—18 日，快手技术团队将在展台与大家见面。如果你关注生成式推荐的工程落地，或正在思考推荐系统在推理效率、训练系统和智能体优化方面的挑战，欢迎来到快手展台，与我们交流实践经验和研究思路。现场还准备了丰富的互动活动和快手技术周边，期待与你见面。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1gVUsotpT1V3mQymSPHkGic4OluaKU8Fhpcqicqibia7ibUg3znriaOesicLJ5JKhEXGicf5Tpcg8uSou31tEcfPFQBIaJPiaiaQuyskMUr7b67zpZraA/640?wx_fmt=png&from=appmsg)

「组织委员会」

* General Co-Chairs: Yiming Qiu (The University of Hong Kong)、Renyu Yang (Beihang University)、Chen Yang (Kuaishou Technology)
* Steering Committee: Yuan Xie (Hong Kong University of Science and Technology)、Ceyu Xu (Hong Kong University of Science and Technology)
* Program Committee: Xiaofei Liao (Huazhong University of Science and Technology)、Xiang Chen (Peking University)、Yibo Huang (Oracle)、Minhui Xie (Nanjing University)、Ang Chen (University of Michigan)、Jieming Zhu (Huawei 2012 Labs)、Hao Peng (Beihang University)、Zuming Jiang (The University of Hong Kong)、Hao Wu (The University of Hong Kong)、Yuning Chen (Meta)、Yunming Xiao (The Chinese University of Hong Kong, Shenzhen)、Qiang Su (Xiamen University)、Teng Ma (Alibaba Cloud)
* Publication & Web Chair: Xiangrui Yang (The University of Hong Kong)
* Media Support: PaperWeekly

👇 点击【阅读原文】，查看官网！

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/ZxDY5TMPs0GnTFDtpq8oAf91ZQDzvLt6LCp56JQCbFT2cT8uZquFdeJOKbmM4fucIPqtAPvMT0X4DpfpuZibic3Q/0?wx_fmt=png)

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
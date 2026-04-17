---
title: 突破零样本TTS音色克隆上限：LongCat-AudioDiT 的声音克隆艺术
url: https://mp.weixin.qq.com/s/qGwajB8FN_kjqgtc44sqew
source: Doonsec's feed
date: 2026-04-16
fetch_date: 2026-04-17T04:44:10.775357
---

# 突破零样本TTS音色克隆上限：LongCat-AudioDiT 的声音克隆艺术

![cover_image](http://mmecoa.qpic.cn/mmecoa_jpg/V95GN2mm0Dx51PEgpxrhn3krrCATCk7XibPNJsKGolpXGYIs6YZ8I2WZJL6lfs4mdf14qibxMP992c5485L6ETuNNu3mhic1icR2AiceFLos9Htw/0?wx_fmt=jpeg)

# 突破零样本TTS音色克隆上限：LongCat-AudioDiT 的声音克隆艺术

龙猫LongCat
龙猫LongCat

美团技术团队

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JhVy5CXYiaojXvOIjWT55tecOxv207WDia11AuRLsLMzTn978eEPgeXCks1icyoZn71sOrGIDDwpbyjdrZVq7UxlxiaSlNpD7c1kAn1xA3ibOia0U/640?wx_fmt=png&from=appmsg#imgIndex=0)

音频生成技术正在经历一场全新的范式迁移——从传统级联架构，逐步向端到端生成范式演进。长期以来，主流的做法是“曲线救国”：合成系统先将音频压缩成梅尔频谱图等中间表征，再依赖神经声码器“翻译”回波形。每一次转换都带来信息损失与误差累积，最终丢失了最需要保留的细腻音色与个性化细节。

能不能让 AI 直接学会声音本身的规律，跳过中间环节？

为破解这一技术瓶颈，**美团 LongCat 团队正式发布 LongCat-AudioDiT**。在该模型中，**我们彻底抛弃梅尔谱等中间表示，直接在波形潜空间进行基于扩散模型的文本转语音（Text-to-Speech, TTS），从根源阻断数据转换的级联误差。**

另外，我们做了两个关键改进：首先，我们**识别并纠正了一个长期存在的“训练-推理不匹配”问题**；其次，我们**用自适应投影引导（APG）取代了传统的无分类器引导（CFG）**，从而大幅提升了最终的语音生成质量。

结果表明，**LongCat-AudioDiT 在 Seed 基准测试中取得当前最优（SOTA）的零样本语音克隆性能，同时保持了具有竞争力的可懂度。**其中LongCat-AudioDiT-3.5B模型，在Seed-ZH测试集的说话人相似度（SIM）指标提升至0.818，Seed-Hard 测试集达到0.797，超过了Seed-TTS、CosyVoice3.5、MiniMax-Speech等知名模型，验证了波形空间直接生成范式的有效性。

今天，我们将 LongCat-AudioDiT（1B/3.5B）完整开源：

* Paper:

  <https://arxiv.org/abs/2603.29339v1>
* GitHub:

  <https://github.com/meituan-longcat/LongCat-AudioDiT>
* HuggingFace:

  <https://huggingface.co/meituan-longcat/LongCat-AudioDiT>

接下来，我们将为您拆解 LongCat-AudioDiT 的核心技术创新。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JhVy5CXYiaoiagUEEw2qN3vK1Q62CX1bkTHX13xWerP2XF5rJ9dRJTBfm9279SOCDeUM18Qo7eyUTt2icPV0H2LDBw2UjwwUSHKqzg4VicH5H18/640?wx_fmt=png#imgIndex=1)

业界主流TTS系统长期受困于“多阶段”的复杂流程：先预测中间声学特征（如梅尔频谱），再依赖一个独立的神经声码器将特征“翻译”成最终波形。这种“预测+翻译”的范式，本质上是在两个不同空间里“传话”，必然会累积误差，导致最终合成的声音丢失了高保真、个性化的细节——而这恰恰是零样本语音克隆最需要保留的部分。

为此，我们构建了全新的 LongCat-AudioDiT 架构。其核心逻辑非常简单：

**|****只用一个波形变分自编码器（Wav-VAE）和一个扩散Transformer（DiT），在波形隐空间里完成声音的压缩、建模与重建。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JhVy5CXYiaoiaZAT4aialb23f0g4spZyzaDam4n3BtQib3Bbr7yTkGf2XeBSoia1znBa1zS0TZj926JG6KSQiaJ6XCuFbic8Ep4hcIicWcVohr6PIAg/640?wx_fmt=png#imgIndex=2)

图1：LongCat-AudioDiT架构概览

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JhVy5CXYiaoiaGWyDI2EEWiaxOZ4hzANz9HE9J57BboOVQusGcywgN9YzQQoDv064LP0WjzL6Blicg78SowOh0XrDUGibHpBkmTfRwLibuQbSoBwk/640?wx_fmt=png&from=appmsg#imgIndex=3)

Wav-VAE 作为一个全卷积音频自编码器，它将原始波形压缩为紧凑的连续隐向量。其设计蕴含了多项关键创新：

* **高效的下采样与多尺度建模：**编码器通过多级Oobleck块实现层级下采样，每个块内堆叠了带空洞卷积的残差单元，能够捕获从局部到全局的时序依赖。最终将24kHz的波形压缩到约11.7Hz的帧率，压缩比超过2000倍。
* **非参数捷径稳定训练：**为了在激进下采样时保持训练稳定，每个编码器/解码器块都引入了非参数的“空间到通道”或“通道到空间”捷径分支，为梯度提供了直接的线性通路，大幅提升了收敛稳定性。
* **对抗式多目标训练：**Wav-VAE的优化目标融合了多分辨率STFT损失、多尺度梅尔损失、时域L1损失、KL散度正则，以及多尺度STFT判别器的对抗损失和特征匹配损失。这套组合拳确保了重建波形既保持精确的时频结构，又具备自然听感。

![](https://mmbiz.qpic.cn/mmbiz_png/JhVy5CXYiaojrghXW4ZEF3T4AfCx17PETxgmrYjjRIhuRib8rNQUOO1BFONMCq76I3F0wib1TDboTeKS3QeccFUibvjcHkydibSYCfb2eLp5uk00/640?wx_fmt=png&from=appmsg#imgIndex=4)

有了高质量的隐空间，我们的DiT模型便在这个空间里学习条件流匹配（CFM）。

文本编码方面，我们选择了支持107种语言的UMT5作为文本编码器。一个关键的发现是：仅使用最后一层隐藏状态模型无法生成可懂的语音。我们推测这是因为高层语义抽象丢失了关键的词法、音素线索。因此，我们创新性地将原始词嵌入（第一层）与最后一层隐藏状态相加，经过LayerNorm平衡scale后送入后续模块。这种“高低结合”的策略大幅提升了生成语音的可懂度。此外，我们还引入了轻量的ConvNeXt V2序列模块对文本表征进行细化处理，加速了文本-语音对齐的收敛。

DiT的骨干网络基于Transformer，并集成了多项结构优化：

* 全局自适应层归一化（Global AdaLN）： 注入时间步信息，并通过全局共享的AdaLN块有效减少参数量。
* QK-Norm + RoPE 稳定注意力训练：同时利用旋转位置编码捕捉相对位置关系。
* 长跳跃连接： 将输入直接加到输出，在实验中带来了一致的质量提升。
* 表征对齐（REPA）： 借助mHuBERT的自监督特征引导DiT中间层，虽不提升最终质量，但显著加速了收敛。

![](https://mmbiz.qpic.cn/mmbiz_png/JhVy5CXYiaoiaG5LeP5ibrw4wDJibFd5o8tptziaZ7AQzSLicALsrdENzZhLUFALlZLiba5GsvvNXLQfqDzszeqwcQ3tFdS2vmYZhib5bSbaKmO9TOc/640?wx_fmt=png#imgIndex=5)

如果说波形潜在空间架构解决了声学建模的"空间选择"问题，那么我们对推理过程的两项关键改进，则从根本上优化了生成过程的"路径精度"与"质量纯度"。

![](https://mmbiz.qpic.cn/mmbiz_png/JhVy5CXYiaohAqld4ewUomnAvIPddgstIFo32vVUR7eKpzAjDO3ojEe4sG2EMvOD5ciap8J2pjgznmL4piah86H6uh2JJnlqprMPia3SlVt1KzE/640?wx_fmt=png&from=appmsg#imgIndex=6)

我们首次发现并解决了流匹配TTS中长期存在的训练-推理不匹配问题。在标准CFM训练框架中，模型仅在掩码区域计算损失，而音频提示区域（prompt）并不参与优化；然而在推理阶段，这些同样提供音色条件的提示区域却会不受约束地通过扩散ODE自由演化，导致其分布轨迹偏离训练时的约束条件，最终造成生成语音的说话人音色漂移与稳定性下降。

为此，我们提出双重约束机制：

1. 提示区域隐变量强制重置：在每一步推理迭代中，严格将提示区域的隐变量重置为其理论真值（即训练时的ground truth），确保提示区域的演化轨迹与训练分布完全对齐，为生成部分提供稳定且纯净的声学条件；
2. 无条件预测净化：在计算无条件速度场时，移除提示区域的隐变量输入，从而计算出完全正确的无条件速度，避免信息泄漏。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JhVy5CXYiaog91zLuHyxah3WWB9HIGCmOaLPckkbM94NDgDF8rfQZ7mAJJse3Bj9dkMYyy0licM1iaFhzQA1D5Uk8IODER5JfZmMCoK7icJPrX4/640?wx_fmt=png&from=appmsg#imgIndex=7)

传统的扩散模型普遍使用无分类器引导（CFG），通过放大条件预测与无条件预测的差异来提升生成质量。但这种方法有一个副作用：引导强度越大，越容易导致频谱“过饱和”，从而使得音质劣化、语音听起来不够自然。

我们提出的自适应投影引导（APG）则换了一个思路：引导信号中真正有益的部分，和引发劣化的部分，在几何上是正交的。APG将引导信号分解为平行与正交两个分量，保留正交分量（有益部分），同时抑制平行分量（劣化部分），从而在提升自然度的同时避免音质损失。

简单来说，CFG是“无差别放大”，APG是“精准筛选”。两项推理优化协同作用，在保持高说话人相似度的同时，显著提升了生成语音的自然度与声学质量。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JhVy5CXYiaoiapgtNVaJnZKMnaibQOMibB6QpFTvxws0IlVzHahDoA4nhKERswhJWX54qevrw8TIh8br45FviaQkdo5UrYCVBziay7EW9GUKU6at4/640?wx_fmt=png#imgIndex=8)

在 Wav-VAE 的实验中，我们观察到了一个非常有意思的现象：VAE重建质量越好 ≠ 语音生成效果越好

单纯追求高重建分数，会导致潜空间维度膨胀。这使得下游的扩散模型难以学习，导致综合表现下降。

为了深入探究这个问题，我们系统性地对比了不同潜空间维度与帧率配置下的建模表现，最终确定了最优配置：64维潜在维度 + 11.7Hz帧率。这一配置既为生成模型留出足够的学习空间，又保留了足够的声学细节，实现了重建保真度与生成质量的最佳平衡。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JhVy5CXYiaoj0T1VSMTkdvR7zOAuicxIicUbOOOStL6B4YLbEc4nQ0bsnicblnw4d9RAKZDlZbvw2wNqPcDOGJznjYQyEL1WTsTRoICibASBUmto/640?wx_fmt=png#imgIndex=9)

图2：不同潜变量维度下Wav-VAE重建与TTS合成的客观评估结果

![](https://mmbiz.qpic.cn/mmbiz_png/JhVy5CXYiaoiaWC4wNdLsLST778LIibVObv2vAP4YQYkE9dicXib3HtsUhfdPKANWposrY6lFHBj57apgzjicicTFSbjKLS8Y6QQCVeehjoicus6PZ0/640?wx_fmt=png#imgIndex=10)

我们在Seed基准上测试了LongCat-AudioDiT的表现，并与业界知名模型，比如SeedTTS、CosyVoice3.5、MiniMax-Speech等进行对比。

结果表明，LongCat-AudioDiT在说话人相似度（SIM）方面取得了SOTA的表现，同时具有极具竞争力的可懂度。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JhVy5CXYiaog5iczGkEa58gUut5WfZ8KhkWxEvpqiavL7ubtxBz8Hvu1cGRjYv6IWAkAZ7iaHsdCrVkdfCPegtsKib8s68B87GgI0If7jaCjdBK0/640?wx_fmt=png#imgIndex=11)

图3：LongCat-AudioDiT 在 Seed 基准测试

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JhVy5CXYiaoiasT8cvy3ZQHAGG9ZyJHQZsSjic21EJLr7O4uvJf2EHRd6YbuM4EG4npjtBh93kNJR7bGljy1bPq1WndYeHXV4nVWwCzrPCA4Qg/640?wx_fmt=png&from=appmsg#imgIndex=12)

* **中文测试集（Seed-ZH）：**LongCat-AudioDiT-3.5B 取得了 0.818的相似度分数，大于之前SOTA Seed-DiT的分数0.809。
* **中文难句测试集（Seed-Hard）：**LongCat-AudioDiT-3.5B 取得了0.797的SOTA分数。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JhVy5CXYiaojOVMZl4NiaiaN50iciaTGzju7K6NCKibCLN2iabaiaiaFRTbC0XEia8K7Hsw4icQUZIBHczKLgiaoEicx0lpWQzeU1spCYQOYRYgPZWNSymYg/640?wx_fmt=png&from=appmsg#imgIndex=13)

* **中文 CER：**LongCat-AudioDiT-1.1B 为 1.18%，LongCat-AudioDiT-3.5B 为 1.09%。在 NAR（非自回归）模型中表现非常出色。
* **英文 WER：**两个版本分别为 1.78% 和 1.50%。其中 LongCat-AudioDiT-3.5B 的 1.50% 达到所有参评模型中的第二最低的错误率，展现了极强的英文文本转语音准确性。
* **中文难句 CER：**LongCat-AudioDiT-3.5B 取得了 6.04% 的成绩，相比于同样基于扩散模型的F5 TTS (8.67%) 错误率大幅降低，表现稳健。

模型在准确率指标上保持了第一梯队的水平，没有为了追求相似度而牺牲可懂度。

值得一提的是，LongCat-AudioDiT并没有使用高质量人工标注数据和多阶段的训练，仅仅通过ASR转写的预训练数据和单阶段预训练就取得了比多阶段训练的模型，如Seed-TTS、CosyVoice3.5、MiniMax-Speech等知名模型更好的表现。

总结来说，LongCat-AudioDiT 模型凭借其优秀的说话人相似度（SIM）和稳定的准确率（WER/CER），在零样本语音克隆任务中展现出强大的竞争力。

![](https://mmbiz.qpic.cn/mmbiz_png/JhVy5CXYiaojrRnjCkTXeiaBcic6NbEEq62KBrG68EOBOEJFlvbTw5HV0hnvJchlYWKNcj1EdXRXuG0qxhQLInORpkO8iasrnfbGuEwI00tp5Oo/640?wx_fmt=png#imgIndex=14)

请参考

公众号「龙猫LongCat」推文（文末扫码关注）：《突破零样本TTS音色克隆上限：LongCat-AudioDiT 的声音克隆艺术》

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JhVy5CXYiaoh2J7B4nKEKVPMbNxIJrOichWznUTR0nbPoOr4QAIBOwpnVhnCr7XXvRw8ibQp4aeicV9Ko8vNTng25gxUWicjhamno3bebX53WfG8/640?wx_fmt=png#imgIndex=15)

LongCat-AudioDiT以极简的架构、纯粹的波形潜空间建模，证明了绕开中间表征的扩散TTS路线不仅能走通，更能达到业界最佳水平。我们相信，这套“波形隐空间直通”的设计范式将为高保真语音合成与多模态音频生成提供新的思路。

今天，我们将LongCat-AudioDiT 模型（1B / 3.5B）全部开源，期待与社区同仁共同推动语音生成技术的边界。

🚀 **开源平台链接：**

* **Paper：**

  **<https://arxiv.org/abs/2603.29339v1>**
* **GitHub:**

  <https://github.com/meituan-longcat/LongCat-AudioDiT>
* **HuggingFace:**

  <https://huggingface.co/meituan-longcat/LongCat-AudioDiT>

我们也期待，这套技术能帮助更多开发者和研究者，构建出更自然、更富表现力的语音交互体验。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JhVy5CXYiaohESFibJtWQLYmGrnRe3aMNexHd7amU7z43XuTApfhcIMClCuZ5jVvdO0lVlRMkfJ6xZ1Y3CKvOOpRgaobstypbMUg5a2LbjKnk/640?wx_fmt=jpeg&from=appmsg#imgIndex=16)

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_p...
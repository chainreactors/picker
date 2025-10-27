---
title: NeurIPS 2024 | 从单图到3D：HumanSplat 基于Gaussian Splatting实现高保真人体3D生成
url: https://mp.weixin.qq.com/s?__biz=MzI1MzYzMjE0MQ==&mid=2247512496&idx=1&sn=2e93dfa836d04030cded6042ef5b10e0&chksm=e9d37a52dea4f344ff38647679c17f18b2b6becf3dc4a9ab179f413f08b06e4c79a82c2b8d73&scene=58&subscene=0#rd
source: 字节跳动技术团队
date: 2024-12-23
fetch_date: 2025-10-06T19:36:38.124764
---

# NeurIPS 2024 | 从单图到3D：HumanSplat 基于Gaussian Splatting实现高保真人体3D生成

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5EcwYhllQOgp5LgowYBM3lu7WxM8j3PwwmTOrUa9s6aticQ20G1FntUD0InaPv5sM7p3gl0X8eXnhnzKaFBHhUw/0?wx_fmt=jpeg)

# NeurIPS 2024 | 从单图到3D：HumanSplat 基于Gaussian Splatting实现高保真人体3D生成

原创

苏卓

字节跳动技术团队

在虚拟和增强现实中，构建写实风格的虚拟人体形象已成为实现自然交互和逼真体验的关键技术之一，并且在社交媒体、游戏、电商、远程交流等领域拥有广泛应用。然而，现有的人体重建方法通常依赖大量的多视图图像输入或需要对每个实例进行耗时的优化处理，这不仅限制了其在实际场景中的适用性和效率，也难以满足快速和高质量建模的需求。因此，仅从单张输入图像生成高保真度的人体模型仍然是一个充满挑战的课题。

在近日召开的神经信息处理系统大会（NeurIPS 2024）中，来自字节跳动 PICO 交互感知团队、清华大学和北京大学的研究人员发表了最新研究成果《HumanSplat: Generalizable Single-Image Human Gaussian Splatting with Structure Priors》。该论文提出了一种创新的单张图像人体重建方法——HumanSplat，这是一个基于结构先验的泛化人体3D生成框架，可以高效地从单张输入图像预测人体的3D重建结果。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOh3EmPBRCmPFzesXmw8m5EM0fXPmnibiauN0dJeX98ibDek18NWXDUksQRmIiazY3EpfAOoIq5tBvY1Rw/640?wx_fmt=png&from=appmsg)

HumanSplat在保持最快运行时间的同时，实现了领先的渲染质量：(a) 定性结果对比；(b) 效果和运行时间对比

**论文链接：**

**https://arxiv.org/pdf/2406.12459**

**项目主页：**

**https://humansplat.github.io/**

**代码链接：**

**https://github.com/humansplat/humansplat**

## 背景

目前，单图像人体重建方法主要分为显式方法和隐式方法。显式方法（如基于参数化人体模型SMPL的方法）通过直接优化模型参数和服装偏移以拟合输入图像，从而生成人体网格。然而，这些方法通常难以处理复杂的服装样式，并且需要较长的优化时间。隐式方法则通过连续函数（如占据场、SDF 或 NeRF）表示人体，这些方法在建模灵活拓扑结构上表现较好，但由于训练和推理的高计算成本，其在可扩展性和效率方面存在局限性。

近期，3D Gaussian Splatting（3DGS）技术为3D人体模型重建提供了效率与渲染质量的平衡。然而，已有的方法通常需要多视图图像或单目视频作为输入，并未能解决单图像输入重建问题。此外，一些基于扩散模型的研究通过得分蒸馏采样（SDS）将二维扩散模型先验提升到三维，但每个实例通常需要长达数小时的优化时间；一些泛化的人/物体生成模型虽然能够直接生成三维表示，但往往忽略了人体几何先验，或仍然需要多视图输入，导致其在稳定性和实用性上的不足

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/5EcwYhllQOh3EmPBRCmPFzesXmw8m5EM7uQTwIjrbY5RuAeTDkEaWia5S3w9POBdWYbeaYnKSgmW8QTTibl1YNfQ/640?wx_fmt=gif&from=appmsg)

HumanSplat 的核心是结合2D生成扩散模型和人体几何结构先验，在统一的框架中整合几何和语义信息，从而在保持高质量的同时实现高效重建。为了解决单视图输入下的不可见区域问题，HumanSplat 首先利用一个 2D 多视角扩散模型（novel-view synthesizer）生成目标人体的不可见区域，然后通过一个泛化的隐空间重建 Transformer （latent reconstruction transformer）将扩散模型生成的特征与人体结构先验进行深度交互，最终重建基于3DGS表达的人体模型。

## 方法

HumanSplat设计了一个泛化的人体3DGS生成框架，通过在人体数据集上精调的2D多视角扩散模型和精心设计的基于参数化模型的3D人体结构先验实现高保真度的人体重建。与现有的3DGS方法不同，我们的方法直接从单张输入图像推断3DGS的高斯属性，无需对每个实例进行优化，也无需密集捕获的目标人体的图像数据，从而有效地在各种场景下进行泛化，提供高质量的重建结果。

**核心框架** HumanSplat网络的核心框架如下图所示，它结合了2D生成式扩散模型（novel view synthesizer，图中（a）所示）与隐空间重建Transformer（latent reconstruction transformer，图中（b）所示），并在统一框架中充分融合了人体几何先验、2D外观先验和基于人体语义信息的分层监督和定制损失函数（图中（c）所示）。我们的方法主要分为以下几步：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOh3EmPBRCmPFzesXmw8m5EMia6xRiaKbkCVdPakCoc2k5Y7vsGWjABqdAbNia8RdPFKYOkFk1js9CZNA/640?wx_fmt=png&from=appmsg)

1. **结构先验与****CLIP****特征提取** 我们首先使用SMPL预测器估计人体结构先验，即当前图像对应的参数化人体模型SMPL参数，并通过CLIP特征提取器提取输入图像的嵌入式特征。
2. **多视角特征****生成器** 我们采用了基于时间-空间隐式编码的2D扩散模型，即通过人体数据精调SV3D视频生成模型，然后结合输入图像和CLIP嵌入式特征生成多视角潜空间特征。
3. **隐空间重建与高斯点云生成** 我们提出了一种新颖的隐空间重建Transformer，结合第一步中得到的人体几何先验与和第二步中得到的多视角隐空间特征，经过一个Transformer框架的模型进行信息交互，信息交互方式如下图所示，然后生成人体高斯属性。随后，这些高斯点被渲染成新的视角图像。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOh3EmPBRCmPFzesXmw8m5EMdKN7Uic81ibxicic3utGcud0sJk69F1Uf3QibSw4C33HrESttXAJvycdIFQ/640?wx_fmt=png&from=appmsg)

4. **分层****语义****损失设计** 最后，为了提升人体的细节重建质量并更好地约束多视角生成结果，我们还设计了分层语义感知损失，将人体语义先验融入到训练中。

**训练与****推理**

* **训练阶段** 我们使用3000个3D扫描的人体数据进行训练，以确保网络能够从不同视角获取准确的监督信号。训练过程在八卡A100上不超过3天。
* **推理****阶段** 在推理时，直接基于训练好的模型从单张图像生成新视角，无需任何微调或优化步骤。

**贡献总结**

1. 提出了一个新颖的泛化的单图人体高斯生成网络，实现从单图像进行高保真度人体重建。我们的方法首次结合2D生成式扩散模型与隐空间高斯重建模型，在端到端框架中高效且准确地进行单图像人体重建。
2. 通过结合SMPL模型中的人体几何先验与2D生成式扩散模型中的外观先验，稳定了人体几何的高质量生成，并帮助生成有着复杂几何人体的不可见部分。
3. 通过引入语义线索、分层监督和定制损失函数，提升了重建人体模型的细节保真度，实验结果表明，我们的方法超越了现有方法，达到了领先的效果。

## 实验结果

在我们的实验中，HumanSplat展现了显著的优势，尤其在渲染质量、重建速度和泛化能力方面，超越了现有的一些最先进的方法。

1. **重建速度**：HumanSplat 在视频扩散模型生成多视角潜在特征的速度上仅需约 9秒，而后续的3D高斯重建只需 0.3秒，显著提升了效率。此外，基于 NVIDIA A100 GPU，它能够以超过 150 FPS 的速度渲染新视角，极大提升了实时渲染性能。
2. **定量对比**：在 THuman2.0 和 Twindom 数据集上，HumanSplat 在 PSNR 和 LPIPS 等指标上都表现出色，尤其在 Twindom 数据集上，PSNR 提升了 10.16%，LPIPS 减少了 0.063，超越了最新的 TeCH 方法。与 TeCH 需要 4.5小时的重建时间相比，HumanSplat 的重建时间仅为 9.3秒，大大提高了实用性。
3. **定性对比**：如下图所示，和已有的方法对比，HumanSplat 显示出更加细致和高保真度的结果，HumanSplat 比 GTA 和 LGM 更能还原细节。此外，HumanSplat 能有效预测3D高斯点的属性，无需针对每个实例进行优化，展示了强大的泛化能力。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5EcwYhllQOh3EmPBRCmPFzesXmw8m5EMMRwmbFSsoGfU6iaER0NYBRgqibaGGN9xaWos7a1xDibc2yeLDMkcQpSFA/640?wx_fmt=jpeg)

1. 在复杂姿势、不同身份和摄像机视角下的重建的对比见下图：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOh3EmPBRCmPFzesXmw8m5EMtqkpSrP4QAWLbmRNCVoqTdAhww0ibLia5xIgsFFhqI5BalELsqMbxyWQ/640?wx_fmt=png&from=appmsg)

b. 在挑战性较大的一般（In-the-wild）图像中的对比见下图：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOh3EmPBRCmPFzesXmw8m5EM9Ofdk0CFS06LY1bPsS3bM25aEFR5fhugjURoON6KZ7HBSAbaelbItw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5EcwYhllQOh3EmPBRCmPFzesXmw8m5EMJ3iao80cVS2et069L6jcak3l616NMXGnkQSUNwkkuUeD7HMcell86Ww/640?wx_fmt=jpeg)

## 总结

HumanSplat 展示了仅依靠单张图像即可生成高保真虚拟人体模型的能力，特别是在面部和手部等关键区域实现了高质量的重建效果。该方法结合了生成式扩散模型与隐码重建Transformer模型，并融入了人体结构先验与语义感知的分层损失设计，实现了无需优化或微调的高保真度重建，特别是在面部和手部等关键区域效果显著。与现有方法相比，HumanSplat在质量与效率上均有显著提升，能够稳健应对复杂姿态和宽松服饰。

相信在未来的虚拟现实与沉浸式体验场景中，借助 HumanSplat 的技术，个性化虚拟形象的生成将变得更加高效便捷。无论是在社交媒体、虚拟会议还是游戏娱乐中，每个人都能快速创建专属的高真实感形象，显著提升互动的沉浸感与真实感，为各种领域的用户体验带来改变。

欢迎加入字节跳动PICO交互感知团队

团队致力于在3D数据资产和数字内容消费等领域开发AI技术。我们专注于3D数字内容的获取、处理以及AI生成。团队注重协作、创新思维与持续学习，诚邀您的加入，共同为公司的成长贡献力量！

👇通过扫描下方二维码，或者点击下方**阅读原文**进行简历投递：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOgp5LgowYBM3lu7WxM8j3Pw5ribjSSUtfhicsyjUvlWnnydBLic5J0mbVaHOGdvOnufxyyXLvX5JkJlw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOgp5LgowYBM3lu7WxM8j3Pw5KgurlnzCFgIgo1dTwmgHg8mlJicqeZPic38OBRj0djgQHLoGdzNAozQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOgp5LgowYBM3lu7WxM8j3PwBq9QxMtjZ8iaibro8ibq4Outpyboq9y89Xk6WNBw8Y8ekBbhTW0FvZGlA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOgp5LgowYBM3lu7WxM8j3Pwxq6o1ce7zicLonjNYSI9XanwnC5EAnjufb1P0S1QrPUHJxH6Kx9Zichw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOgp5LgowYBM3lu7WxM8j3PwS2ia3Wo6sMGWzibx2n6YfWfqq3Yxkjo8v5APiaIcHoJ9ukthf0paE0GoQ/640?wx_fmt=png&from=appmsg)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOhkoWTP1gVm0Lqs480XOARyoSYjPEsRVCSF35cbWIp6cliaYic8KUfNfiaSjVnruzTQUTCA0lmv9vUmw/0?wx_fmt=png)

字节跳动技术团队

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOhkoWTP1gVm0Lqs480XOARyoSYjPEsRVCSF35cbWIp6cliaYic8KUfNfiaSjVnruzTQUTCA0lmv9vUmw/0?wx_fmt=png)

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
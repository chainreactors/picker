---
title: Seed Research | 视频生成模型最新成果，可仅靠视觉认知世界！现已开源
url: https://mp.weixin.qq.com/s?__biz=MzI1MzYzMjE0MQ==&mid=2247513283&idx=1&sn=56430e9ca40e3d7b8f37678ec93af4d1&chksm=e9d37f21dea4f637b33d4f26efcd15ece737f3d3fd0fd7506369dfd7580683eca9f3713f3381&scene=58&subscene=0#rd
source: 字节跳动技术团队
date: 2025-02-13
fetch_date: 2025-10-06T20:36:32.738990
---

# Seed Research | 视频生成模型最新成果，可仅靠视觉认知世界！现已开源

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5EcwYhllQOhZfr3mRJyiayyCcNOStFuDqQHIEK6yfZNiaV0KJIsiakJjNrhQDhUIynccGhlQ9gPSIxAdylKv2evww/0?wx_fmt=jpeg)

# Seed Research | 视频生成模型最新成果，可仅靠视觉认知世界！现已开源

豆包大模型团队

字节跳动技术团队

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/IrH3BAPESuhPOK4aGeiaH4xc3K9hftIaU71lyDxgDhL6bBVPsvAOQYppS5FHQwstITiaIR6GsvryQicocJcx7BNOw/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

视频生成实验模型“VideoWorld”由豆包大模型团队与北京交通大学、中国科学技术大学联合提出。不同于 Sora 、DALL-E 、Midjourney 等主流多模态模型，VideoWorld 在业界首次实现无需依赖语言模型，即可认知世界。

正如李飞飞教授 9 年前 TED 演讲中提到 “幼儿可以不依靠语言理解真实世界”，VideoWorld 仅通过 “视觉信息”，即浏览视频数据，就能让机器掌握推理、规划和决策等复杂能力。团队实验发现，仅 300M 参数量下，VideoWorld 已取得可观的模型表现。

现有模型大多依赖语言或标签数据学习知识，很少涉及纯视觉信号的学习。然而，语言并不能捕捉真实世界中的所有知识。例如，折纸、打领结等复杂任务，难以通过语言清晰表达。

作为一种通用视频生成实验模型，VideoWorld 去掉语言模型，实现了统一执行理解和推理任务。同时，它基于一种潜在动态模型，可高效压缩视频帧间的变化信息，显著提升知识学习效率和效果。

在不依赖任何强化学习搜索或奖励函数机制前提下，VideoWorld 达到了专业 5 段 9x9 围棋水平，并能够在多种环境中，执行机器人任务。

团队认为，尽管面向真实世界的视频生成和泛化仍存在很大挑战，视频生成依然可以成为一种通用的知识学习方法，并在现实世界充当思考和行动的“人工大脑”。

**目前，该项目代码与模型已开源，欢迎体验交流。**

> **VideoWorld: Exploring Knowledge Learning from Unlabeled Videos**
>
> **论文链接：**https://arxiv.org/abs/2501.09781
>
> **代码链接：**https://github.com/bytedance/VideoWorld
>
> **项目主页：**https://maverickren.github.io/VideoWorld.github.io

**1. 模型仅靠“视觉”即可学习知识**

面向本次研究，研究团队构建了两个实验环境：**视频围棋对战和视频机器人模拟操控。**

其中，围棋可以很好地评估模型的规则学习、推理和规划能力，且围棋关键信息仅有黑白两色及棋盘，可将外观、纹理等复杂细节与高级知识的评估分离，非常适合对上述问题的探索。同时，团队还选取了机器人任务，以考察模型在理解控制规则和规划任务方面的能力。

在模型训练环节，团队构建了一个包含大量视频演示数据的离线数据集，让模型“观看”学习，以此得到一个可以根据过往观测，预测未来画面的视频生成器。

模型架构上，团队使用朴素的自回归模型实例化视频生成器，它包含一个 VQ-VAE 编码器 - 解码器和一个自回归 Transformer 。编码器负责将视频帧（画面）转换为离散标记，Transformer 在训练期间使用这些标记预测下一标记。

在推理过程中，Transformer 生成下一帧（画面）的离散标记，这些标记随后由解码器转换回像素空间。通过任务相关的映射函数，模型可将生成画面转换为任务执行动作。这让视频生成实验模型可在不依赖任何动作标签情况下，学习和执行具体任务。

基于上述朴素的框架对围棋和机器人视频数据进行建模，团队观测到，模型可以掌握基本的围棋规则、走棋策略以及机器人操纵能力。

但团队同时也发现，视频序列的知识挖掘效率显著落后于文本形式，具体如下图所示。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/IrH3BAPESuh0OrV2TkQvZnZyXl8zA63ibjIZSNs69Ls6mfO0estoFia2VSiaw8LaCyFia19jeWHsnqR8yzMf5qoMCg/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

团队将这归因于——视频中存在大量冗余信息，影响了模型的学习效率。

例如，学习棋子移动过程中，模型只需通过状态序列中少量位置标记编码，但面向视频数据，编码器则会产生过多冗余标记，不利于模型对复杂知识的快速学习。

**2. 压缩视觉变化，让视频学习更加高效**

根据上述观测结果，团队提出 VideoWorld 。**它在保留丰富视觉信息的同时，压缩了关键决策和动作相关的视觉变化，实现了更有效的视频学习。**

通常，视频编码需要数百或数千个离散标记来捕捉每帧内的视觉信息，这导致知识被稀疏地嵌入标记中。为此，VideoWorld 引入了一个潜在动态模型（Latent Dynamics Model, LDM），可将帧间视觉变化压缩为紧凑的潜在编码，提高模型的知识挖掘效率。

举例而言，围棋中的多步棋盘变化或机器人连续动作均表现出强时间相关性，通过将这些多步变化压缩成紧凑嵌入，不仅让策略信息更紧凑，还将前向规划指导信息进行编码。

LDM 采用了 MAGVITv2 风格的编码器 - 解码器结构，同时取消时间维度下采样，以保留每帧细节。

对于一个视频片段，LDM 采样每一帧及其后续固定数量帧，编码器先以因果方式提取每帧特征图，且进行量化，以保留详细视觉信息。

接下来，LDM 定义了一组注意力模块和对应可学习向量。每个向量通过注意力机制捕捉第一帧至后续固定帧的动态变化信息，然后通过 FSQ 量化。其中，量化器作为信息筛选器，防止 LDM 简单记忆后续帧原始内容，而非压缩关键动态信息。

最后，解码器使用第一帧的特征图和帧之间的视觉变化编码重建后续帧，最终实现对未来动作的预测和规划，实现对知识的认知学习。

下图为模型架构概览，左侧为整体架构，右侧为潜在动态模型。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/IrH3BAPESuhqB3IEiaNtzltdW5KmNGtEHGYFUvPlEyggTbS3mKwBwicKViaRFQO0orVERWq02w9xcpWx6ibPx9D5Jw/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

通过使用多个向量顺序编码第一帧到后续多帧的动态变化，VideoWorld 实现了紧凑且信息丰富的视觉表示，可以捕捉视觉序列中的短期和长期依赖关系。这对于长期推理和规划任务至关重要。

通过引入 LDM ，VideoWorld 在仅有 300M 参数量下，达到专业 5 段的 9x9 围棋水平，且不依赖任何强化学习中的搜索或奖励函数机制。在机器人任务上，VideoWorld 也展现出了对多任务、多环境的泛化能力。

有关 LDM 的更多详细信息，请阅读论文。

**3. 纯视觉模型可“预测”未来，并能“理解”因果关系**

针对 LDM 提高视频学习效率的原因，团队进行了更为细致地分析，得出如下 3 点结论：

* **LDM 建模了训练集的数据模式。**

下图为 LDM 潜在编码 UMAP 可视化呈现，面向围棋和机器人训练集，每个点代表一个潜在编码。

其中，UMAP 是一种流行的降维算法，用于将高维数据映射到低维空间，展现模型特征提取情况。

在下图左侧中，奇数步表示白方走棋，偶数步表示黑方，图例展示了新增黑棋的一些常见模式。UMAP 可视化表明：LDM 建模了训练集中常见的走棋模式，并能将短期和长期数据模式压缩至潜在空间中，提取并总结走棋规律。

同理，下图右侧为机械臂沿 X/Y/Z 轴运动方向可视化潜在编码，随着步数（Step）增多，也能看到 LDM 可以建模多步动态依赖关系。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/IrH3BAPESuhqB3IEiaNtzltdW5KmNGtEHncoG4iaAsZh1sHXPyybyLQGDzQNFQGC4bia2QtHYDvuXkGYO2ess49eQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

* **LDM 帮助模型在测试时进行前向规划。**

团队还研究了 LDM 在模型推理中的价值。

如下图 UMAP 可视化所示，在测试阶段，模型生成的潜在编码按照时间步（Time-step）进行分组，使得模型能够从更长远视角进行围棋决策。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/IrH3BAPESuh0OrV2TkQvZnZyXl8zA63ibxOp93fGoPPegaExgFjHRNcPGY8mmZoXPP5bPwLOhQQictQeo3JK8EVg/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

在机器人场景实验中，团队也观察到了类似现象。

下图展示了 VideoWorld 在不同机器人操控任务中预测的潜在编码。不同时间步的潜在编码根据任务类型进行分组，突显了模型逐步捕捉特定任务长程变化的能力。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/IrH3BAPESuh0OrV2TkQvZnZyXl8zA63ibMK29XnhxIVdjh66X0vkuViamdoc4pVnQicsDvr3GAuzyUvWLciaxiaGibew/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

* **LDM 可以生成因果相关的编码。**

为进一步研究潜在编码的影响，团队进行了一项干预实验：用随机标记替换不同时间步的潜在编码，并观察其对模型性能的影响。

实验结果显示，干预第一个编码的影响最大，这可能由于编码之间存在因果依赖，团队认为：改变第一个编码，即下一时间步的最佳决策，会影响所有未来的决策，侧面说明模型可生成因果相关编码，理解因果关系。

**4. 写在最后**

尽管 VideoWorld 在围棋和模拟机器人操控环境中展现了卓越性能，团队同时也意识到，其在真实世界环境中的应用，仍面临着高质量视频生成和多环境泛化等挑战。

在未来，团队将着力解决这些难题，推动视频生成模型成为真实世界中的通用知识学习器。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/IrH3BAPESuhPOK4aGeiaH4xc3K9hftIaUvIbIUYD96j6WzbF5CrcXHwW14icf6miaj6HpfuznuzydOfsEJjVqliaFw/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/IrH3BAPESuhPOK4aGeiaH4xc3K9hftIaU3MN90fRIZIY52RMj5VtLRmefmGNAlWnOvj300xc679X68eIVL399lw/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/IrH3BAPESuhPOK4aGeiaH4xc3K9hftIaUe00KHxMqxNzOpROicednLZoYdbvBkoVlkpbF3oEn2f995qqkriaSmKAA/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

[![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/IrH3BAPESuhqB3IEiaNtzltdW5KmNGtEHV4AKYT3ucmgYd36NkECbaXcU1SpmCN2kvPTYv1Zxkmr2d9Z9a2v8Xw/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)](https://mp.weixin.qq.com/s?__biz=MzkzMDY5MzYxNg==&mid=2247489533&idx=1&sn=f3817426de5156f65a19af95d2360671&scene=21#wechat_redirect)[![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/IrH3BAPESuhqB3IEiaNtzltdW5KmNGtEHo9ApZFOyiaZ820MoUudkQbS2zzcbicxTIamDVkhkzjM09Nsd9pKC1NDA/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)](http://mp.weixin.qq.com/s?__biz=MzkzMDY5MzYxNg==&mid=2247486518&idx=1&sn=a83683f8874eae9db687f27c911c3c24&chksm=c27724a9f500adbf96c5752f1e37394a79f9b0e135040cc47479acc3079680f64d3a4b27ebc7&scene=21#wechat_redirect)

****点击“阅读原文”，了解更多团队信息！****

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
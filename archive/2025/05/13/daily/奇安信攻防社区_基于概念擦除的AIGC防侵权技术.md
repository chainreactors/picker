---
title: 基于概念擦除的AIGC防侵权技术
url: https://forum.butian.net/share/4314
source: 奇安信攻防社区
date: 2025-05-13
fetch_date: 2025-10-06T22:23:17.518401
---

# 基于概念擦除的AIGC防侵权技术

#

[问答](https://forum.butian.net/questions)

*发起*

* [提问](https://forum.butian.net/question/create)
* [文章](https://forum.butian.net/share/create)

[攻防](https://forum.butian.net/community)
[活动](https://forum.butian.net/movable)

Toggle navigation

* [首页 (current)](https://forum.butian.net)
* [问答](https://forum.butian.net/questions)
* [商城](https://forum.butian.net/shop)
* [实战攻防技术](https://forum.butian.net/community)
* [漏洞分析与复现](https://forum.butian.net/articles)
  NEW
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### 基于概念擦除的AIGC防侵权技术

* [漏洞分析](https://forum.butian.net/topic/48)

最近的文生图模型因为卓越的图像质量和看似无限的生成能力而受到关注。最近出圈，可能是因为openai的模型可以将大家的图像转变为吉卜力风格。

前言
==
最近的文生图模型因为卓越的图像质量和看似无限的生成能力而受到关注。最近出圈，可能是因为openai的模型可以将大家的图像转变为吉卜力风格。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-b50ec2aa6aa392ee294e95192b4f518010e572a3.png)
这些文生图模型在庞大的互联网数据集上进行训练，使它们能够模仿广泛的概念。然而，模型学习到的一些概念是容易招来官司的，包括受版权保护的内容和色情内容。比如对于最近的吉卜力事件，许多插画师指责OpenAI“侵犯版权”，“严重侵犯艺术家权利和生计”。
所以现在一个密切相关的子领域，就是希望在模型的输出中避免这些内容。
之前有很多典型的方法集中在数据集过滤、生成后过滤或推理引导上。那么是否可以在预训练后从文本条件模型的权重中选择性地移除单个概念呢？
如果可以的话，相比于数据过滤方法，这种方法不需要重新训练，就比较实用。而基于推理的方法虽然可以有效地审查或引导输出远离不受欢迎的概念，但它们很容易被绕过。相比之下，我们希望的这种方法直接从模型的参数中移除该概念，使其权重的分发更加安全。
这真是扩散模型领域被广泛关注的概念移除技术。
背景
==
为了限制不安全图像的生成，Stable Diffusion第一个版本附带了一个简单的NSFW（Not Safe For Work，不适合工作场合）过滤器，如果触发过滤器就会审查图像。然而，由于代码和模型权重都是公开可用的，因此很容易禁用该过滤器。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-57afb9d61d9597072c658af55abf5c184e1b8359.png)
为了防止敏感内容的生成，后续的SD 模型是在经过过滤以移除明确图像的数据上进行训练的，这一实验在50亿图像的LAION数据集上消耗了15万小时的GPU计算时间。这一过程的高成本使得很难建立起数据中的具体变化与出现的能力之间的因果联系，但用户报告称，从训练数据中移除明确图像和其他主题可能对输出质量产生了负面影响。尽管如此，模型输出中仍然存在大量明确内容.
之前已经有研究人员证实，当使用不适当图像提示（I2P）基准中的4703个提示来评估图像生成时，流行的SD 1.4模型产生了796张被裸体检测器识别出暴露身体部位的图像，而新的训练集受限的SD 2.0模型产生了417张，统计结果如下图所示。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-d0cc69c67dfe875c539a25daa5b9f3c8e3243d98.png)
关于文生图模型的另一个主要问题是它们模仿可能受版权保护内容的能力。人工智能生成的艺术作品不仅与人类生成的艺术作品质量相当，而且还能忠实复制真实艺术家的艺术风格。之前在安全四大上，就有学者发过论文提出了对应的防护方法。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-bac458334d428db07e6181040a5dc280d9146477.png)
上图中左侧是原始艺术的风格，右侧是让文生图模型模仿该风格画出的图像。而下图则是当时那篇论文提出的防护方法
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-25c1837490413c01772a7b97752c2ecb678597ac.png)
该方法通过隐藏在线艺术作品来保护受害艺术家免受 AI 风格模仿。（上图）艺术家 V 应用隐藏算法（使用特征提取器 Φ 和目标风格 T）来生成 V 艺术作品的隐藏版本。每个隐藏版本都是人眼无法察觉的细微扰动。（下图）模仿者从网上抓取隐藏的艺术作品，并利用它们来微调模型以模仿 V 的风格。当被要求生成 V 风格的艺术作品时，模仿者的模型将生成目标风格 T 的作品，而不是 V 的真实风格。
不过这个威胁模型其实也是从训练数据角度来做的，我们本文将介绍发表在人工智能顶会ICCV上的方法Erasing Concepts from Diffusion Models，从训练后的模型权重中移除这些特定的概念。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-951b45e57562dd25def89f05f246e78f72b7ad39.png)
上图所示是期望的效果。只需提供一段简短的文本描述，描述不需要的视觉概念，无需额外数据，即可微调模型权重，从而消除目标概念。这种方法可以避免 NSFW 内容，阻止对特定艺术家风格的模仿，甚至从模型输出中消除整个对象类别，同时保留模型在其他主题上的行为和能力。
扩散模型
====
文生图模型的底层是扩散模型，所以有必要了解其背景。
去噪扩散模型
------
Denoising Diffusion Models（去噪扩散模型）是一类生成模型（Generative Models），通过模拟数据从噪声中逐步生成的过程来进行图像、音频、文本等数据的生成。它们近年来在图像生成领域取得了非常显著的成果，例如 OpenAI 的 DALL·E 2、Stability AI 的 Stable Diffusion 等都基于这一类模型。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-234e9a3f2f44068e1ec665f9df04b8d9fd8b8bbe.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-4cf20fd9511c21dc4fbc855d850f0563caebb7f3.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-b030c966ac46ff8b6f4c90d79a5f25b0bd145645.png)
潜在扩散模型
------
Latent Diffusion Models（潜在扩散模型，简称 LDM）是在传统 Denoising Diffusion Models 基础上的一种优化变体，其核心思想是：在图像的潜在空间（latent space）而不是像素空间中进行扩散过程，从而极大地降低计算成本，同时保持生成质量。它是 Stable Diffusion 的核心技术。
传统扩散模型直接在高分辨率的图像像素空间（如512×512×3）上操作，内存与计算开销极大。为了解决这个问题，Latent Diffusion Models 提出：
将高维图像压缩到一个低维潜在空间中进行扩散，再解码回图像空间。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-7865258e4663326d2ba9d64bd8add1d066be0640.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-e87ac09e62adcade915c860734dd67ab89f03ae9.png)
整体工作流程可以表示如下
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-eb4b4d313eb96504f81eb1d794dfd116afda4e6a.png)
方法原理
====
之前已经提到过，我们是希望利用模型自身的知识，无需额外数据，从文本到图像的扩散模型中擦除特定概念。因此考虑对预训练模型进行微调，而不是从头开始训练一个新模型。
Stable Diffusion包含3个子网络：文本编码器T、扩散模型（U-Net）θ\\* 和解码器模型D。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-1683337de659531ec9af3df076f50e6880b108c6.png)
我们将训练新的参数θ。
这期间会涉及编辑预训练的扩散U-Net模型的权重，以移除特定的风格或概念。我们的目标是根据概念所描述的可能性（通过一个幂因子η进行缩放）来降低生成图像x的概率。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-e2e35a2510b89cbd497743915edfa02ce2dd191f.png)
其中，Pθ\\* (x) 表示原始模型生成的分布，c表示要擦除的概念。根据P(c|x) = P(x|c)P(c)，对数概率P(x)的梯度∇logPθ(x)将与以下表达式成比例：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-40a98f8c0417a4b47d6cb5331bd3c884430b71db.png)
根据重参数化技巧，我们可以引入一个随时间变化的加噪过程，并将每个分数（对数概率的梯度）表示为去噪预测ε(xt, c, t)。因此，公式可以表示为
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-8aa12e1d2c8f44599d693363e9344bf0d78db7aa.png)
这个修改后的分数函数将数据分布移动，以最小化可以被标记为c的图像x的生成概率。公式中的目标函数对参数θ进行微调，使得εθ(xt, c, t)模拟负向引导噪声。这样，在微调之后，经过编辑的模型的条件预测将被引导远离被擦除的概念。
下图展示了训练过程。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-1ac55ba26c97a8fed069ca38bdbf443fa274ad3d.png)
我们利用模型对概念的已有知识来合成训练样本，从而避免了数据收集的需要。训练过程中使用了多个扩散模型实例，其中一组参数保持固定（θ\\*），而另一组参数（θ）则用于擦除概念。我们使用θ根据条件c采样部分去噪的图像xt，然后在固定的模型θ\\*上进行两次推理以预测噪声，一次是有条件的（基于c），另一次是无条件的。最后，我们将这两个预测线性组合，以抵消与概念相关的预测噪声，并将新模型调整到这个新的目标方向上。
代码实现
====
现在分析具体的实现代码
如下代码实现了一个基于扩散模型的语义“抹除”训练过程，主要目的是：
让模型在生成图像时，不再表现出某个概念（如“gun”）即使该词出现在上下文中（如“man with gun”）。这是对模型生成偏好的一种定向干预。
我们来进行分析
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/05/attach-a3739a32b4f65a8f48f0d924689887d3327bdaec.png)
首先，设置了一个变量表示去噪过程中的步数，这是扩散模型生成图像时的标准流程步骤。
接着，加载了一个扩散模型，并将其移动到指定的设备上（如 GPU）。然后设置了模型为训练模式，以便可以进行参数更新。
随后，定义了一个微调模型，用于对扩散模型的特定部分进行训练。传入的参数决定了具体要训练哪些部分。
之后，初始化了优化器和损失函数。这里使用的是 Adam 优化器和均方误差损失函数，用来指导模型如何更新参数以减少预测误差。
为了方便观察训练进度，创建了一个进度条，显示当前的迭代次数。
接下来，处理需要擦除的概念及其对应的来源类别。将输入的字符串按逗号分割成多个概念，并去除每个概念前后的空格。
如果来源类别的数量与要擦除的概念数量不一致，但来源只有一个，则复制该来源以匹配长度；否则抛出异常，提示两者长度必须一致。
然后将要擦除的概念与其来源配对，形成一个二维列表，便于后续处理。
最后，打印出整理后的擦除概念列表，并清空 GPU 缓存以释放内存，避免训练过程中出现内存不足的问题。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/05/attach-8fb12d3bc10b2c0d4a974ea2508bcc5a51689b16.png)
在每次训练迭代中，程序会随机选择一个需要“擦除”的概念及其对应的来源概念。比如我们想让模型学会把“狗”这个概念从图像中擦掉，可能对应的来源就是“一只狗的照片”。
接下来，程序会生成三种文本嵌入（可以理解为文本的数学表示）：
中性嵌入 ：使用空文本（相当于没有任何提示），作为基准。
正向嵌入 ：使用的是要擦除的概念（如“狗”）。
目标嵌入 ：使用的是希望保留或替换的内容（如“猫”或者空白）。
然后设置扩散模型的时间步数，这是控制图像生成过程的一个参数。
清空优化器的梯度，准备进行新一轮的参数更新。
接着，随机选择一个去噪过程中的时间点（称为 iteration）。这一步是为了模拟在图像生成过程中某个中间阶段对模型进行干预。
生成一个初始的随机潜在表示（latents），这是扩散模型用来逐步生成图像的基础。
然后，使用正向嵌入（也就是那个要被擦除的概念）来进行一部分图像生成过程，运行到之前选定的那个时间点，得到当前的潜在状态。
再将模型的时间步数恢复为完整的 1000 步，并将之前选中的时间点映射到新的时间尺度上。
最后，分别使用正向嵌入、中性嵌入和目标嵌入来预测该时间点下的噪声。这些噪声预测会在后续用于计算损失，从而指导模型如何调整参数，以达到“擦除”特定内容的目的。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/05/attach-12554974c429f5a3f721e608fb89bf56e493c024.png)
在训练循环的这一部分，程序首先会检查当前选中的“要擦除的概念”和“希望保留的概念”是否相同。例如，如果两者都是“狗”，那就说明我们其实不想生成任何内容，相当于要从图像中完全抹去这个概念。在这种情况下，系统会把目标噪声（也就是期望得到的结果）设为中性噪声的一个副本，表示不希望模型在这个位置保留任何特定信息。
接下来，在模型内部进行一次前向传播，使用目标文本嵌入来预测当前时间步下的噪声输出，并将这个结果作为负向噪声预测。
为了确保训练过程中不会对某些中间结果计算梯度，程序将正向噪声和中性噪声设置为不需要梯度更新。
然后，程序开始计算损失。损失的计算方式是基于负向噪声与目标噪声之间的差异。其中，目标噪声并不是直接使用目标提示生成的噪声，而是结合了负向和正向噪声之间的差值，并乘以一个负向引导系数，这样可以让模型更有针对性地抑制那些需要被擦除的内容。
接着，程序根据计算出的损失值，进行反向传播，自动计算梯度，并通过优化器更新模型参数，使模型在下一次迭代中能更准确地实现“擦除”目标。
完成参数更新之后，模型会被保存到指定路径，以便后续使用或测试。
为了释放内存资源，所有不再需要的变量都会被删除，包括模型、优化器、损失以及各种中间张量。最后清空 GPU 的缓存，为其他任务腾出空间。
现在我们以差擦与梵高这个艺术家有关的风格为例
进行微调
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-99553ed50a68554a5c7e9541b2fd773135c0ebc7.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-842c08801bda45d79f3ebda4ecb85e7234994076.png)
![image.png](https://cdn-yg-...
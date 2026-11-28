---
title: AI 是如何生成一张图片的？（上）：生图的第一步，竟然是把原图“毁掉”？
url: https://mp.weixin.qq.com/s/uM5Uy_jJ-B9TFCymg5bGCw
source: Doonsec's feed
date: 2026-11-27
fetch_date: 2026-11-28T09:37:38.259516
---

# AI 是如何生成一张图片的？（上）：生图的第一步，竟然是把原图“毁掉”？

# AI 是如何生成一张图片的？（上）：生图的第一步，竟然是把原图“毁掉”？

原创

CSL
CSL

联想全球安全实验室

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**点击蓝字**

**关注我们**

**赵爽**

![](https://mmbiz.qpic.cn/mmbiz_gif/SHwAnKFwKRRK6njo3XibTT8quCrQFtiaIA7ouDDYpb1iciat2KKuGKnic5f13APfxpMKd0iaiaREE4MzqicaNjiaXklNSPMrtzvJXjImFFDlic9ZGOgMw/640?from=appmsg)

**从随机噪声，到一只宇航员橘猫**

输入一句“一只穿着宇航服的橘猫，站在月球上”，稍等片刻，一张图片就出现了。AI 到底做了什么？先画轮廓，再填颜色？还是从图库里找出猫、宇航服和月球，拼在一起？

要理解扩散模型，核心就是一句话：训练时，把图片逐渐变成噪声，让模型学习如何去噪；生成时，从随机噪声出发，一步步构造出图片。

下面以经典噪声预测扩散模型及 Stable Diffusion 式文生图流程为例，一步一步讲解这个流程。不同模型的实现有所区别，但这条主线可以帮助我们更好地理解关键机制。

**PART.01**

**正向扩散：先把图片“弄乱”**

![](https://mmbiz.qpic.cn/mmbiz_gif/wMd7dk6Wufkjk3DlDvh0VHPeDibyE3vBNVxnSktCO1aLicTB0iaFW9l1oDPN3ibkVtQHjc3BIv8DhqEic6XlPwZ6ZIiakus3bcibohk2hmgU8O4OHM/640?from=appmsg)

想象一张清晰的橘猫照片。不断往里面加入随机噪点：开始只是有点花，接着毛发和眼睛变得模糊，最后几乎只剩下电视“雪花”。这个从图片走向噪声的过程，就叫正向扩散。

![](https://mmbiz.qpic.cn/mmbiz_png/0UKPAuBeu7mcWYzSsXwOBsgHW6zSvopxicSIP9LkyHk0jl6lYAdYUEbX9Zo0fPEYseenSCL2QziaZRFZN2YlxGWsJlATPlTsTn9o6E6iaB6iaico/640?from=appmsg)

*图1｜正向扩散：图片信息逐渐被噪声淹没。*

经典做法是按预设规则加入高斯噪声，也就是一种常见的随机扰动。噪声越多，原图中可辨认的信息就越少。但加噪不需要智能。真正值得训练的是反方向：给模型一个被噪声污染的状态，它能否判断，下一步该怎样让这个状态变得更像合理的图片？

![](https://mmbiz.qpic.cn/mmbiz_gif/r3yydX7W9iaeEXe68OCuEeYjgn2OAG39MZRTIhRs6gbgO4uzvOFKVyPPRvm7enn5Okf2TLebQITWayctTD00f44dEzNOD7HtuRN0dg5PC1g8/640?from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/r3yydX7W9iaeEXe68OCuEeYjgn2OAG39MZRTIhRs6gbgO4uzvOFKVyPPRvm7enn5Okf2TLebQITWayctTD00f44dEzNOD7HtuRN0dg5PC1g8/640?from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/r3yydX7W9iaeEXe68OCuEeYjgn2OAG39MZRTIhRs6gbgO4uzvOFKVyPPRvm7enn5Okf2TLebQITWayctTD00f44dEzNOD7HtuRN0dg5PC1g8/640?from=appmsg)

**PART.02**

**训练：AI 怎么知道哪些是噪声？**

![](https://mmbiz.qpic.cn/mmbiz_gif/wMd7dk6Wufkjk3DlDvh0VHPeDibyE3vBNVxnSktCO1aLicTB0iaFW9l1oDPN3ibkVtQHjc3BIv8DhqEic6XlPwZ6ZIiakus3bcibohk2hmgU8O4OHM/640?from=appmsg)

答案是：训练时，噪声是我们自己加进去的，因此有标准答案。每次训练，都可以出一道“带答案的题”。

1. 取一张真实图片，随机选择一个噪声等级；

2. 生成随机噪声，按对应比例与原图混合；

3. 把加噪图片和噪声等级交给神经网络，让它预测所加的噪声；

4. 比较预测噪声与实际噪声的差距，通过反向传播更新网络参数。

![](https://mmbiz.qpic.cn/mmbiz_png/0UKPAuBeu7mdnbYTsjQzHN3rqGN9XbstmMpbFBYQIBlalSHVXUBepBNt1gdb4MRUmUKIExhy2TMe71d7TMIicPTianeKQcK5gh4hhKh0gjmCc/640?from=appmsg)

*图2｜训练的核心：比较预测噪声与实际噪声，再更新网络参数。*

这里要准确理解图中的误差比较：预测噪声和实际噪声共同用于计算误差，误差再用于更新神经网络；不是先更新参数，再产生用于比较的预测结果。

经典训练可以用一个式子概括：

![](https://mmbiz.qpic.cn/mmbiz_png/0UKPAuBeu7mblbTXj22OdUfEvzsH54Bd5nle7MuASHweF97n4mSynWdGtG0vKqrSDBQiaN2ZavBgUaibYuRM3nPMvMNShBiawo8ESLCC650n7g/640?from=appmsg)

其中，x₀ 是原图，ε 是随机噪声，xₜ 是加噪后的图片，ᾱₜ 控制原图保留多少。用通俗的话翻译过来，就是“带噪图片＝一定比例的原图＋一定比例的噪声”。

神经网络看到 xₜ 和噪声等级 t，学习预测 ε。训练目标通常是让预测噪声与实际噪声的均方误差尽量小。训练时也不必真的连续加噪许多次，可以直接用上面的公式生成指定等级的样本。

经过大量练习，模型学到的不是某一张图片的修复密码，而是不同噪声程度下，图像结构与去噪方向之间的统计规律。

![](https://mmbiz.qpic.cn/mmbiz_gif/r3yydX7W9iaeEXe68OCuEeYjgn2OAG39MZRTIhRs6gbgO4uzvOFKVyPPRvm7enn5Okf2TLebQITWayctTD00f44dEzNOD7HtuRN0dg5PC1g8/640?from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/r3yydX7W9iaeEXe68OCuEeYjgn2OAG39MZRTIhRs6gbgO4uzvOFKVyPPRvm7enn5Okf2TLebQITWayctTD00f44dEzNOD7HtuRN0dg5PC1g8/640?from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/r3yydX7W9iaeEXe68OCuEeYjgn2OAG39MZRTIhRs6gbgO4uzvOFKVyPPRvm7enn5Okf2TLebQITWayctTD00f44dEzNOD7HtuRN0dg5PC1g8/640?from=appmsg)

**PART.03**

**生成：没有原图，只有随机起点**

![](https://mmbiz.qpic.cn/mmbiz_gif/wMd7dk6Wufkjk3DlDvh0VHPeDibyE3vBNVxnSktCO1aLicTB0iaFW9l1oDPN3ibkVtQHjc3BIv8DhqEic6XlPwZ6ZIiakus3bcibohk2hmgU8O4OHM/640?from=appmsg)

训练时有原图，真正生成时是不需要原图的。模型先随机产生一团噪声，再重复执行：预测噪声、按规则更新当前状态、继续预测。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0UKPAuBeu7lYIjF7j2L4yYHHHILk4gia08olRMOCf6Aia6kggMAbGZfH7g16JjibFExP4zDP5Z3dMEn5YIXSYQCUvF3q9QsywWzfvib8DbTicfX8/640?from=appmsg)

*图3｜反向生成：从随机起点出发，经过多轮更新形成图像。*

这里有两个重要的搭档：神经网络估计当前噪声，调度器根据估计结果和当前时间步计算下一步状态。因此，“减掉噪声”只是直观说法，实际更新还涉及缩放等运算，并非简单直接相减。

一个关键区别是：随机噪声里，并没有藏着一张等待显影的猫咪照片。模型是在学到的图像分布中逐步采样，而不是找回唯一的原图。

同一句提示词能生成不同图片，原因之一就是起始噪声不同。随机种子可以控制这一随机起点；要稳定复现结果，还需保持模型、采样设置和运行条件等一致。

要解释的是，图中的“从模糊到清晰”是帮助理解的示意，不代表所有模型都会严格按照“先画轮廓、再补细节”的固定顺序工作。

![](https://mmbiz.qpic.cn/mmbiz_gif/r3yydX7W9iaeEXe68OCuEeYjgn2OAG39MZRTIhRs6gbgO4uzvOFKVyPPRvm7enn5Okf2TLebQITWayctTD00f44dEzNOD7HtuRN0dg5PC1g8/640?from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/r3yydX7W9iaeEXe68OCuEeYjgn2OAG39MZRTIhRs6gbgO4uzvOFKVyPPRvm7enn5Okf2TLebQITWayctTD00f44dEzNOD7HtuRN0dg5PC1g8/640?from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/r3yydX7W9iaeEXe68OCuEeYjgn2OAG39MZRTIhRs6gbgO4uzvOFKVyPPRvm7enn5Okf2TLebQITWayctTD00f44dEzNOD7HtuRN0dg5PC1g8/640?from=appmsg)

**PART.04**

**文字如何指挥生成？**

**为什么还需要潜空间？**

![](https://mmbiz.qpic.cn/mmbiz_gif/wMd7dk6Wufkjk3DlDvh0VHPeDibyE3vBNVxnSktCO1aLicTB0iaFW9l1oDPN3ibkVtQHjc3BIv8DhqEic6XlPwZ6ZIiakus3bcibohk2hmgU8O4OHM/640?from=appmsg)

仅会去噪，模型还不知道你想画什么。文生图系统会先通过文本编码器，把提示词转换成一组数字表示，也就是语义向量。去噪网络在生成过程中参考这些信息，让画面朝符合文字描述的方向推进。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0UKPAuBeu7niaryBzeOoYKQKiazumdFnjaOTict2S0o5ib3dC64Et6STBFibO7zktRL7bCticnvrwrpwx3gqB2TWQYWYQ2M9Aia7QuxKfyDGfXofvg/640?from=appmsg)

*图4｜典型潜空间文生图流程：文字引导去噪，VAE解码得到图片。*

图中的条件连接应理解为：文本编码器输出语义向量，语义向量输入“多轮去噪”模块，而不是输入最终潜表示。以早期 Stable Diffusion 为例，交叉注意力机制把文字条件引入去噪网络。

可以把它想成：模型处理画面时，不断参考“橘猫”“宇航服”“月球”等信息。但这不是给每个词指定一块固定像素区域，而是一种条件约束。

另一个问题是效率：直接处理高分辨率像素，计算开销很大。潜空间扩散先把图像表示压缩到更紧凑的空间，在那里完成加噪和去噪。这里的潜在空间表示是多通道数字特征，不是普通缩略图。

承担图像与潜在空间表示转换的模块叫 VAE。训练时，VAE 编码器把图片转换成潜表示；生成时，从随机潜噪声出发，经过多轮去噪，再由VAE解码器转换成可见图片。纯文生图没有输入图片，因此通常无需在开始时运行图像编码器。

![](https://mmbiz.qpic.cn/mmbiz_gif/r3yydX7W9iaeEXe68OCuEeYjgn2OAG39MZRTIhRs6gbgO4uzvOFKVyPPRvm7enn5Okf2TLebQITWayctTD00f44dEzNOD7HtuRN0dg5PC1g8/640?from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/r3yydX7W9iaeEXe68OCuEeYjgn2OAG39MZRTIhRs6gbgO4uzvOFKVyPPRvm7enn5Okf2TLebQITWayctTD00f44dEzNOD7HtuRN0dg5PC1g8/640?from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/r3yydX7W9iaeEXe68OCuEeYjgn2OAG39MZRTIhRs6gbgO4uzvOFKVyPPRvm7enn5Okf2TLebQITWayctTD00f44dEzNOD7HtuRN0dg5PC1g8/640?from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/SHwAnKFwKRRK6njo3XibTT8quCrQFtiaIA7ouDDYpb1iciat2KKuGKnic5f13APfxpMKd0iaiaREE4MzqicaNjiaXklNSPMrtzvJXjImFFDlic9ZGOgMw/640?from=appmsg)

**结语：把整条流水线串起来**

提示词 → 文本编码器 → 语义向量；随机潜噪声在语义向量引导下，经过神经网络与调度器的多轮配合 → 最终潜表示 → VAE解码器 → 图片。

最后要说明的是，本文讲的是经典“预测噪声”路线，并非所有新模型都直接预测噪声，也不是所有系统都用同一种网络。有的采用 Transformer，有的使用流匹配等方法，学习从噪声到数据的变化方向。

理解了这条主线，就抓住了扩散式生图的关键思想：生成图片，可以不是逐笔描画，而是从随机出发，在学到的规律与文字条件引导下，一步步建立秩序。

**参考阅读：**

· Hugging Face：*The Annotated Diffusion Model（经典扩散原理与训练）*

· Hugging Face：*Stable Diffusion with Diffusers（潜空间文生图组件）*

· Hugging Face Diffusers：*Understanding pipelines, models and schedulers（去噪网络与调度器）*

**往期精彩合集**

●[CVE-2026-31720：摄像头固件里一次没走完的内核栈写穿](https://mp.weixin.qq.com/s?__biz=MzU1ODk1MzI1NQ==&mid=2247494944&idx=1&sn=44502f60bdc80cd793987036d1d0a081&scene=21#wechat_redirect)

●[给脸是信任，护脸是责任｜读懂人脸背后的隐私防护技术](https://mp.weixin.qq.com/s?__biz=MzU1ODk1MzI1NQ==&mid=2247494936&idx=1&sn=4efc1d12906be0548af40feebdba8800&scene=21#wechat_redirect)

●[当 AI 说“完成了”，你敢信吗？](https://mp.weixin.qq.com/s?__biz=MzU1ODk1MzI1NQ==&mid=2247494899&idx=1&sn=d0873125c4ff6b7a2df8ef7c6328f36b&scene=21#wechat_redirect)

●[OWASP LLM Top10 2026：AI 安全进入治理时代](https://mp.weixin.qq.com/s?__biz=MzU1ODk1MzI1NQ==&mid=2247494887&idx=1&sn=4ca5901c79197b538640431f065b6314&scene=21#wechat_redirect)

●[自进化长效智能体：Prime Agent 项目全方位解析](https://mp.weixin.qq.com/s?__biz=MzU1ODk1MzI1NQ==&mid=2247494845&idx=1&sn=13d80f3810c5911ba87f371f2c65fe4f&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/0UKPAuBeu7mCdnicElCkZibM2AqVwo02tL8iaRkAJBO6KIpmV0DN9ZqhGkaS3ibM6CicWNH0V0ldTZcvoH9ltHUHq4VTnibr866IYBSrSriauic57Yw/640?wx_fmt=gif&from=appmsg)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/PicDhHpwdziaibPZd0FJCTel2o5j0mRe7AsGTibmwUbRoonkSFQBNETSL4jqgjKSCE7z3B8KeR9q94miagM69SFsB3A/0?wx_fmt=png)

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
推荐
，轻点两下取消推荐
分享
留言
收藏
听过
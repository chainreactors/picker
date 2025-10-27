---
title: 火山引擎论文入选国际会议ACM MM'24｜对齐人类主观偏好的图像质量评价方法
url: https://mp.weixin.qq.com/s?__biz=MzI1MzYzMjE0MQ==&mid=2247512116&idx=1&sn=fdb4cc5d282ae2c65fc8a01af479b776&chksm=e9d37bd6dea4f2c06cbf28e92e6bdfb9733f251f7d26f57ecc45572b7b83fad12399958ef588&scene=58&subscene=0#rd
source: 字节跳动技术团队
date: 2024-12-05
fetch_date: 2025-10-06T19:39:18.835445
---

# 火山引擎论文入选国际会议ACM MM'24｜对齐人类主观偏好的图像质量评价方法

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5EcwYhllQOiapZjo9l0sNhQxR9s314vx1k0n5Urczr5g6nicvUJpcrSujAPAnuiaufHCcjwtGcxKZ0nJmRGFpiakiaQ/0?wx_fmt=jpeg)

# 火山引擎论文入选国际会议ACM MM'24｜对齐人类主观偏好的图像质量评价方法

流媒体技术

字节跳动技术团队

# 会议背景

2024年10月28日至11月1日，ACM Multimedia(ACM MM) 2024在澳大利亚墨尔本召开，该会议是中国计算机学会(CCF)推荐的多媒体领域的A类国际学术会议。2024年共4395篇参与审稿，最终录用1149篇论文，录用率26.1%。

火山引擎-流媒体技术与湖南工商大学、湘江实验室合作的论文"Align-IQA: Aligning Image Quality Assessment Models with Diverse Human Preferences via Customizable Guidance" 被ACM Multimedia 2024 收录。

论文链接：https://openreview.net/pdf?id=CdA18J5jJx

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOiapZjo9l0sNhQxR9s314vx1REtXo8Iyz7DRZAuvhC0F8IKiaatdD1Xk1MIyuQum0ic7Cp9D3SpSvOEg/640?wx_fmt=png&from=appmsg)

# 论文方案

## **论文背景**

图像质量评价（Image Quality Assessment, IQA）是图像处理和计算机视觉领域中的一项重要任务，旨在模拟人类视觉系统对图像质量的感知过程，构建与人类主观判断尽可能一致的客观质量评价算法。最初，IQA的研究主要聚焦于评估经过特定处理（如压缩、模糊或添加噪声）的自然场景图像、之后逐步扩展到用户生成内容（User-Generated Content, UGC）（如使用智能手机等电子设备拍摄的图像），以及近年来流行的人工智能生成内容（AI-Generated Content, AIGC）（如通过文本到图像模型生成的图像）。为了应对这些不同类型的图像内容的质量评估需求，研究者们投入了大量精力，提出了多种IQA方法。然而，由于人类对于不同类型的图像内容的偏好存在差异，如何使得IQA模型与这些偏好保持一致，依然是一个亟待解决的挑战。尽管现有的IQA方法通过利用预训练模型中的知识，在评估特定图像内容（自然场景图像、UGC图像）方面取得了重大成功，但由于影响最终评估结果的复杂因素众多，以及这些方法所特有的、精心设计的网络架构，它们在准确捕捉人类对新型的图像内容（AIGC图像）的偏好方面仍存在不足。

## **基于可定制指导的对齐人类主观偏好的图像质量评价方法——Align-IQA**

为了解决现有的IQA方法在准确捕捉人类对新颖图像内容的偏好方面的不足，本文提出了一种基于可定制指导的对齐人类主观偏好的图像质量评价方法——Align-IQA。该方法能够针对不同类型的图像内容，生成与人类偏好高度一致的质量评分。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOiapZjo9l0sNhQxR9s314vx1z1Iic3DuIIo44lTqgAl2chuXC6iapgRCWs2tK3g9OSKRZhuwicibAToxxA/640?wx_fmt=png&from=appmsg)

### 可定制指导注入模块

在对自然场景图像、UGC图像和AIGC图像进行质量评估时，人类能够根据自身的知识和经验灵活地调整评估标准。对于自然场景图像和UGC图像，人类评估的重点是图像的视觉保真度；而对于AIGC图像，除了视觉保真度之外，人类还会关注图像与文本提示之间的语义一致性。为此，本文提出了一种可定制指导注入模块（Customizable Guidance Injector, CGI），旨在根据不同类型的图像内容（自然场景图像、UGC图像和AIGC图像）引入相应的人类先验知识，从而使得同一个质量评价模型能够针对这些不同类型的图像内容进行自适应评估。

具体而言，对于自然场景图像和UGC图像，CGI模块通过引入视觉显著性特征作为指导，来帮助模型提取与质量感知相关的特征；对于AIGC图像，CGI模块则通过引入图像和文本提示之间的语义一致性特征，来引导模型提取与质量感知相关的特征。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOiapZjo9l0sNhQxR9s314vx1vY7ojjBk3Vgic8HDOObW4PkB1IHicQib8gAvhIxgtLqqT20hib00ZsdwGA/640?wx_fmt=png&from=appmsg)

### 多尺度特征聚合模块

在人类视觉系统中，有许多视觉特性影响着人类对图像质量的感知。为了构建一个能更贴近人类视觉感知的图像质量评价模型，本文提出了一种多尺度特征聚合模块（Multi-scale Feature Aggregator, MSFA）。该模块通过模拟人类视觉系统的多尺度机制，能够更全面且有效地提取与质量感知相关的特征。同时，它还结合了深度可分离膨胀卷积，以较少的参数高效地实现多尺度信息的提取和融合工作。

## **实验结果**

在八个公开数据集（四个自然场景图像数据集：LIVE、CSIQ、TID2013和KADID-10K；两个UGC图像数据集：CLIVE和KonIQ-10K；两个AIGC图像数据集：AGIQA-1K和AGIQA-3K）上的实验结果显示，Align-IQA能够针对不同类型的图像内容，生成与人类偏好高度一致的质量评分。这充分验证了Align-IQA的有效性和普适性。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOiapZjo9l0sNhQxR9s314vx1f79g7gWuoZEnBdbiaVYcG49ehnb4GwiaTC9Sf6snfDzwaFwP88ows7Yw/640?wx_fmt=png&from=appmsg)

# 总结

本文提出了一种基于可定制指导的对齐人类主观偏好的图像质量评价方法—Align-IQA，该方法能够自适应地对自然场景图像、UGC图像和AIGC图像进行高效的质量评估。为了实现这一适应性评估，本文提出了一个可定制指导注入模块，用于根据不同类型的图像内容引入相应的人类先验知识。此外，为了更准确地从人类视觉感知的角度预测图像的质量评分，本文提出了一个多尺度特征聚合模块。实验结果表明，Align-IQA在涵盖多种图像类型的八个公开数据集上，达到了优于或与SOTA方法相当的性能。

# 团队信息

**火山引擎-流媒体技术-网络传输**团队致力于提供业界领先的流媒体传输质量与传输能力。该团队提出的创新算法及解决方案已广泛应用于抖音、飞书等众多产品的直播、实时通信等业务。

**火山引擎**是字节跳动旗下的云服务平台，将字节跳动快速发展过程中积累的增长方法、技术能力和应用工具开放给外部企业，帮助企业构建用户体验创新、数据驱动决策和业务敏捷迭代等数字化能力，实现业务可持续增长。

预览时标签不可点

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
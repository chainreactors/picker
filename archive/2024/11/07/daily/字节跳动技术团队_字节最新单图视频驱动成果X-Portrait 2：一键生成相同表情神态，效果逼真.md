---
title: 字节最新单图视频驱动成果X-Portrait 2：一键生成相同表情神态，效果逼真
url: https://mp.weixin.qq.com/s?__biz=MzI1MzYzMjE0MQ==&mid=2247511227&idx=1&sn=e8ddd714733141ea160c376515a054a9&chksm=e9d36759dea4ee4fd7094663d0774f16f17c6bd12dd83c08977994f746416a5c7588d28945cf&scene=58&subscene=0#rd
source: 字节跳动技术团队
date: 2024-11-07
fetch_date: 2025-10-06T19:19:03.527448
---

# 字节最新单图视频驱动成果X-Portrait 2：一键生成相同表情神态，效果逼真

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5EcwYhllQOia3noktdW5qRwQ8OfjqLMtYqKs6jcHsxuDhCS2e517Xq4KTluiaFKZTYIQ0UnoicWURUxCF7hWvMZuQ/0?wx_fmt=jpeg)

# 字节最新单图视频驱动成果X-Portrait 2：一键生成相同表情神态，效果逼真

智能创作团队

字节跳动技术团队

单图视频驱动技术为创作富有表现力、逼真的角色动画和视频片段提供了一种成本极低且高效的方法：只需一张静态照片和一段驱动视频即可生成高质量、电影级的视频。

字节跳动智能创作团队近期推出最新单图视频驱动技术X-Portrait 2，基于前一代的X-Portrait研究成果，将人像驱动的表现力提升到了一个全新的高度。

该模型不仅能保留原图的ID，还能准确捕捉并逼真迁移从细微到夸张的表情和情绪，呈现高度真实的效果，大幅简化了现有动作捕捉、角色动画和内容创作流程。

项目网页：https://byteaigc.github.io/X-Portrait2/

# 整体方案

不同于以往依赖人脸关键点检测的单图驱动方法，X-Portrait 2构建了一个最先进的表情编码器模型，通过一种创新的端到端自监督训练框架，能够从大量人像视频中自学习ID无关的运动隐式表征。

进一步将这个编码器与强大的生成式扩散模型相结合，即可生成流畅且富有表现力的视频。

经过在大规模高质量表情视频上的训练，X-Portrait 2在运动表现力和ID保持性方面显著优于先前技术。

算法能够从驱动视频中提取不同颗粒度的表情特征（如挑眉、咬唇、吐舌、皱眉），并有效迁移到扩散模型，实现精准的表情动作控制，进而能实现驱动视频中人物情感的高保真迁移。

# 外观与运动解耦

在训练表情编码器时，为了让编码器关注驱动视频中与表情相关的信息，X-Portrait 2较好地实现了外观和运动的解耦。

通过为模型设计过滤层，编码器能有效过滤运动表征中的ID相关信号，使得即使ID图片与驱动视频中的形象和风格差异较大，模型仍可实现跨ID、跨风格的动作迁移，涵盖写实人像和卡通图像。

这使得X-Portrait 2能高度适应各种各样的应用场景，包括现实世界中的叙事创作、角色动画、虚拟形象以及视觉特效等。

# 技术对比

与前一代X-Portrait以及最近发布的 Runyway Act-One 等业界领先的方法相比，X-Portrait 2能够如实表现快速的头部动作、细微的表情变化以及强烈的个人情感，这些方面对于高质量的内容创作（比如动画和电影制作）至关重要。

# 安全说明

此工作仅以学术研究为目的，会严格规范模型的应用，防止恶意利用。文中使用的图片/视频，如有侵权，请联系作者及时删除。

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
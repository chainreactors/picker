---
title: 横扫四大赛道，火山引擎斩获 MSU 世界视频编码器大赛“最佳ASIC编码器”
url: https://mp.weixin.qq.com/s?__biz=MzI1MzYzMjE0MQ==&mid=2247509758&idx=1&sn=c206adf04f2559856ba49f2196435c2c&chksm=e9d36d1cdea4e40a07cc009809ee0c0fb38395f074d1054570f1ce7451405f6ded18bab8570e&scene=58&subscene=0#rd
source: 字节跳动技术团队
date: 2024-08-31
fetch_date: 2025-10-06T18:08:41.050411
---

# 横扫四大赛道，火山引擎斩获 MSU 世界视频编码器大赛“最佳ASIC编码器”

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5EcwYhllQOghIICRUEE5kT09olp5m6kC8H9Mb7cYPn0MumptpECBpiaYSqqrTAJxTJItAZ6a0ztR5mz0IicBdZicA/0?wx_fmt=jpeg)

# 横扫四大赛道，火山引擎斩获 MSU 世界视频编码器大赛“最佳ASIC编码器”

多媒体实验室

字节跳动技术团队

**MSU****世界编码器大赛由莫斯科国立大学（MSU）举办，是****视频****编码****领域极具影响力的国际赛事**，比赛采用**「SSIM、**PSNR、VMAF」等多个评价指标对全球范围内参赛的软硬件编码器进行多维度的评估和排名，已成功举办18届。

2024年硬件编码器赛道竞争激烈，吸引了各大科技巨头参赛，包括腾讯、Streamlake、Netint、Intel、英伟达、AMD等。火山引擎自研视频转码芯片的**「BVE1.2编码器」**首次亮相，全面参与**1080p@30fps、1080p@60fps、1080p@120fps、和1080p@240fps 四个子赛道**，获得多项指标第一，及全部参赛H.265/HEVC编码器中所有指标第一， 并斩获所有四个赛道“**「最佳****ASIC****编码器」**”称号。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOghIICRUEE5kT09olp5m6kCPicmFYnIVq6hXo6QVYZcibPWCcKLzKIsCLkhfiatespWDXd5r85roibMkg/640?wx_fmt=png&from=appmsg)

在所有的四个赛道中，BVE1.2是表现最好的ASIC编码器，不仅表现出**「优异的编码性能」**，同时**「吞吐率」**大幅度领先同类产品。在高吞吐1080p@240fps赛道中，BVE1.2包揽了所有四项质量指标的第一，并且保持显著的领先幅度 (Fig1)。在1080p@30fps、1080p@60fps、以及1080p120fps 赛道上，BVE1.2是最好的H.265/HEVC编码器（仅次于基于最新一代标准的H.266/VVC编码器），同时相比于压缩性能前三的其他编码器吞吐性能也有非常明显的优势 (Fig2)。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOghIICRUEE5kT09olp5m6kCNLnJGwA5ICh2AYh0vZ4TIB8bACgTKbfmvtU6Oia7b5ROktMhOTlc6Uw/640?wx_fmt=png&from=appmsg)

**「Fig1.BVE1以及其他codecs的overall quality比较(赛道240 fps)」**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOghIICRUEE5kT09olp5m6kCryEB3rWGKyW15oysVEVQIR3Q7g7dcntpUdxiaZ9fqGW9pZ8DlydcbSQ/640?wx_fmt=png&from=appmsg)

**「Fig2.****BVE1.2、Streamlake-200、Netint Quadra以及changhaiV2 吞吐率比较」**

比赛结果不仅证明了BVE1.2编码器能同时实现高吞吐和高质量的双重优势，适应多种不同的编码场景，能够同时兼顾画质、延迟、及成本，带给用户更好的视觉体验。

为了加强在视频编码领域的竞争力，字节跳动在核心技术上不断加大投入，从2019年就开始启动自研硬件编码器研发，目前自研硬件编码器包含FPGA编码器（过去两年都参加了MSU编码器大赛并荣获“最佳FPGA编码器”）和ASIC编码器，覆盖场景从图片到视频，在各个场景下都展现了更极致的压缩效率，并进一步探索具备高压缩率、灵活性、高吞吐率、多标准兼容的未来编码器架构。结果表明，硬件编码器的各项指标不仅在MSU比赛中表现优秀，更在互联网视频方面，进一步扩大了领先优势，火山引擎视频转码芯片集成了视频编解码、视频分析、视频前处理、主观优化、内容自适应编码等关键技术，适用于各种业务场景，包含静图、动图、短视频、长视频、视频直播、视频会议、云游戏等，并通过火山引擎服务外部客户。

当前，直播和短视频迅速增长，导致带宽成本显著增加。火山引擎视频转码芯片以其高编码质量和高密度特性，单卡支持120路 1080p30fps 编码和“一进多出”转码模式。相比通用CPU平台上的软件编码方案，在达到同样的视频压缩效率前提下，拥有几十倍以上的成本优势，同时提供行业领先的编码质量，并支持画质增强，显著降低带宽成本以及计算成本。为满足不同业务及视频应用场景的需求，火山引擎视频转码芯片还提供ABR、CBR、CRF、VBV 等多种码控方案，及low latency模式等。

火山引擎自研芯片及系统可大规模节省IDC机房中视频类应用的成本和能耗，不仅能大幅降低客户的视频类应用成本，还能获得更好的视频主观及客观质量。字节跳动一直致力于推动技术创新和研发，不断提升产品的技术水平和用户体验，在视频编码领域持续突破。

**关于火山引擎多媒体实验室****：**

火山引擎多媒体实验室是字节跳动旗下的研究团队，致力于探索多媒体领域的前沿技术，参与国际标准化工作，其众多创新算法及软硬件解决方案已经广泛应用在抖音、西瓜视频等产品的多媒体业务，并向火山引擎的企业级客户提供技术服务。实验室成立以来，多篇论文入选国际顶会和旗舰期刊，并获得数项国际级技术赛事冠军、行业创新奖及最佳论文奖。

火山引擎是字节跳动旗下的云服务平台，将字节跳动快速发展过程中积累的增长方法、技术能力和工具开放给外部企业，提供云基础、视频与内容分发、大数据、人工智能、开发与运维等服务，帮助企业在数字化升级中实现持续增长。

欢迎更多小伙伴加入，共同探索多媒体前沿技术！

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
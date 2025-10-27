---
title: 火山引擎多媒体实验室VR全链路处理传输显示方案ResVR入选ACM Multimedia 2024最佳论文提名
url: https://mp.weixin.qq.com/s?__biz=MzI1MzYzMjE0MQ==&mid=2247511362&idx=1&sn=b1825032127f175afb4e8ee1a8fa0d7b&chksm=e9d366a0dea4efb69a02b029e02f3c8972c5c254611deeae907f27f5496f0e71f43931ab92aa&scene=58&subscene=0#rd
source: 字节跳动技术团队
date: 2024-11-16
fetch_date: 2025-10-06T19:18:24.560574
---

# 火山引擎多媒体实验室VR全链路处理传输显示方案ResVR入选ACM Multimedia 2024最佳论文提名

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5EcwYhllQOiaw85HOUqWx0LwCHUx6oKllw13pQ8PE1NBbrXW2icQwLwvBLfyX62XT86bFS4bbyyNJibrUE5kfHTibg/0?wx_fmt=jpeg)

# 火山引擎多媒体实验室VR全链路处理传输显示方案ResVR入选ACM Multimedia 2024最佳论文提名

原创

多媒体实验室

字节跳动技术团队

# 会议背景

近日，ACM Multimedia 2024在墨尔本召开，该会议是国际多媒体领域学术和产业界交流的顶级盛会也是中国计算机学会（CCF）推荐的多媒体领域唯一的A类国际学术会议。据悉本次会议共有4385篇投稿进入审稿阶段，最终1149篇论文被录用，录用论文中共有26篇论文（入选比例0.5%）被提名ACM Multimedia 2024最佳论文（Best Paper Nomination）。

火山引擎多媒体实验室和北京大学合作的论文 "ResVR: Joint Rescaling and Viewport Rendering of Omnidirectional Images" 荣获本次会议最佳论文提名。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5EcwYhllQOiaw85HOUqWx0LwCHUx6oKlltjUTtNhTD5emI8biasUpuDpC6een8szsdEibkYoBKSD9WSvsiaOHFUKsw/640?wx_fmt=jpeg&from=appmsg)

# 论文方案

## 论文背景

全景图像（Omnidirectional Images，ODI）等内容已在虚拟现实头戴式VR设备中得到广泛应用，代表性产品包括PICO 4、Meta Quest 3等。全景内容相关技术的应用遍及教育、旅游和娱乐等多个领域。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOiaw85HOUqWx0LwCHUx6oKll7O2M1bqicTxZy9bj6mAZvs43qK0dOpxYpgMedqtCrQzFrD3QYqZWaJg/640?wx_fmt=png&from=appmsg)

全景内容通常采用等距圆柱投影（Equirectangular Projection，简称ERP）格式进行存储。然而，当在VR头戴式设备上观看时，需要将ERP图像转换到观看视角（viewport）进行显示。为较好的用户体验，全景图像和视频的分辨率通常需达到8K甚至更高的标准，这对传输提出了挑战。

在实际应用的场景中，尤其在网络带宽有限的情况下，经常会涉及到全景图像的重采样，它分为三个主要步骤实施：首先，在服务端，我们对高分辨率ERP图像进行下采样，以创建一个低分辨率版本；然后将这个低分辨率图像传输到用户的VR设备后，再将其上采样回与原始图像相同尺寸的高分辨率ERP图像；最后，当用户通过头戴式显示器观看特定视角时，相应的视角再从上采样的图像中渲染出来。

## 端到端全景内容显示方案ResVR

现有的方案这三个步骤是独立的，由于缺少整体链路的联合优化，会出现纹理丢失、像素错位等问题。为了解决这个问题，多媒体实验室的研究人员提出了一种直接优化渲染显示结果的端到端联合优化方案ResVR，并且为了进行端到端训练提出了多项算法创新。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5EcwYhllQOiaw85HOUqWx0LwCHUx6oKll5CT57sxVnGEXSZCHW65AziaMFKC34IiaFNFxVvdnamebet5up8oKqzPg/640?wx_fmt=jpeg&from=appmsg)

## 离散像素采样策略（Discrete Pixel Sampling Strategy）

云端的ERP图像和渲染显示的视角都不能同时是规则的矩形图像形状，从而影响了端到端训练。为了解决这个问题，论文提出了一种离散像素采样策略（Discrete Pixel Sampling Strategy）来创建训练数据对。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOiaw85HOUqWx0LwCHUx6oKllM5FtlDAklSlXiaMnxOiadyq9mmKBibv7JDzZsj5BODQ99HEkBbYSkiaWbg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOiaw85HOUqWx0LwCHUx6oKllDyPRIKdDBqMJVh0icviaL2HGrVcsfia9cL9URr1miaX8YMEjuy3ibMZDbPg/640?wx_fmt=png&from=appmsg)

## **球面像素形状表示（Spherical** **Pixel** **Shape Representation ）**

为了进一步提升端到端训练效果，让网络感知到球面上像素的形状和位置。论文使用了描述渲染过程中球面上像素的方向和曲率，雅可比（Jacobian）矩阵和黑塞（Hessian）矩阵，并基于球面微分使用数值导数来对它们进行估计。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOiaw85HOUqWx0LwCHUx6oKllWVcaKKmOmWZ9naJia1FkGJoCy6f83QPXSWTG0JvJBvic2fUzS36BL3hA/640?wx_fmt=png&from=appmsg)

示例中使用球面视角上的一个点y来说明这个过程。首先，对点y及其8个最近邻点应用逆映射，以在ERP上获得点x及其邻点。然后，这些点被转换为球面坐标，这些坐标用于计算数值导数，以估计像素形状表示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOiaw85HOUqWx0LwCHUx6oKllbAAKCw97cowImfgkB4RuUAPhnyria6KU91oSDyfCsfRDic2oNjSweaibg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOiaw85HOUqWx0LwCHUx6oKllEZFOpia2VIQunI52JK735a9V0ia9YRs94j53zBBQSaNk2I52PI8yuU7Q/640?wx_fmt=png&from=appmsg)

## 实验结果

两个公开数据集测试中的实验结果表明，ResVR在保证全景图像传输效率的同时，实现了最佳的渲染质量。并且值得注意的是，该方案能够使用消费级GPU实现实时渲染，表明在实际应用中有较强的实用性。此外我们从示例图中可以看到，论文的方法超越了现有的方案，在实现了1dB的PSNR增益的同时主观效果也有明显提升。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOiaw85HOUqWx0LwCHUx6oKllFxwVFIIOr9VuJ0yxYx1jnupX81iadficQKRCmtQABN7ibkl4ic1bFvoRicA/640?wx_fmt=png&from=appmsg)

# 总结

在ResVR论文中，多媒体实验室的研究人员提出了一种用于处理、传输以及显示全景图像的新框架，可以同时优化传输效率和渲染质量。为了实现端到端优化，论文提出了一种离散像素采样算法，以创建ERP和GT像素的数据对。此外为了让网络框架对渲染的内容有更好感知，论文引入了一种球面像素形状表示算法。最后，实验表明ResVR在多个测试序列上，达到了sota的主客观效果，并且该方案可以在消费级显卡中实时运行。

**火山引擎多媒体实验室**是字节跳动旗下的研究团队，致力于探索多媒体领域的前沿技术，参与国际标准化工作，其众多创新算法及软硬件解决方案已经广泛应用在抖音、西瓜视频等产品的多媒体业务，并向火山引擎的企业级客户提供技术服务。实验室成立以来，多篇论文入选国际顶会和旗舰期刊，并获得数项国际级技术赛事冠军、行业创新奖及最佳论文奖。

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
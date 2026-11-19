---
title: 论文 | 中国矿业大学利用InSAR反演看不见的地下煤火：煤矿燃烧源深度与物探实测只差几米
url: https://mp.weixin.qq.com/s/twcQy5cSc9gwkLOvEKFucg
source: Doonsec's feed
date: 2026-11-18
fetch_date: 2026-11-19T09:43:56.465373
---

# 论文 | 中国矿业大学利用InSAR反演看不见的地下煤火：煤矿燃烧源深度与物探实测只差几米

# 论文 | 中国矿业大学利用InSAR反演看不见的地下煤火：煤矿燃烧源深度与物探实测只差几米

原创

mapxiaotu
mapxiaotu

空天感知

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

导读：地下煤火在地下几十米深处阴燃，地面上看不见火，只能看到两类间接信号：煤层烧空后地面沉降，热量传上来造成地表温度异常。中国矿业大学闫世勇团队把卫星雷达形变、热红外温度和物理反演模型拼在一起，用在新疆吉木萨尔县水西沟煤田：识别出两个沉降盆地，最大累积沉降约 160 毫米；反演出的两处燃烧源深度为 53.11 米和 80.65 米，与独立物探估计的 56.0 米、85.5 米接近。

地下煤火是煤矿区最难缠的灾害之一。煤层在地下缓慢燃烧，烧掉的是资源，排出的是废气，烧空之后地面还会塌陷，威胁周边基础设施。麻烦在于它藏在地下，燃烧带在哪里、埋多深、烧空的腔体有多大，从地面很难直接量出来。

这篇论文 2026 年发表于《环境遥感》（Remote Sensing of Environment，第 348 卷），作者为中国矿业大学的闫世勇团队。

![](https://mmbiz.qpic.cn/mmbiz_jpg/cemuAg1hRPv5jP5W1KnHXiaqnmlUGkQCzMpVBmcHsZQDgffFjic01DqSEIo7fYkFFybUIlFw90aLPZvJEmovlwYdvGFCVA4KhHibDIUYRaKRGI/640?from=appmsg)

分享阅读笔记如下：

01 难在哪：火在地下，地面只有间接信号

地下燃烧会在地表留下两种痕迹。一是沉降：煤烧掉之后，上覆岩层失去支撑，地面缓慢下沉。二是热异常：燃烧的热量沿裂缝传到地表，热红外影像上会出现高温斑块。论文的框架就建立在这两种痕迹的联合分析上。

单一信号都不可靠。地表高温也可能来自其他热源，地面沉降也可能由采矿活动引起，两种异常还会互相错位。矿区地表破碎、植被稀疏，传统永久散射体方法能用的观测点少且分布不均，形变场容易残缺。

💡 一句话理解分布式散射体（DS）：永久散射体只用楼房、岩石这类单个强反射点，分布式散射体把一整片统计性质均匀的地表当作一个观测对象。在矿区、农田、堤防这类缺少强反射点的场景，DS 能把观测点密度提上一个量级。

02 做法：形变、温度、物理模型三件套

团队给水西沟煤田搭了一套三段式框架，输入是两类卫星观测，输出是地下燃烧腔的几何形状：

• 形变一路用 2018 年 1 月至 2019 年 12 月的 32 幅 Sentinel-1A 影像，做非局部分布式散射体干涉处理（NL DS-InSAR），得到高密度的视线向形变时间序列；

• 温度一路用 Landsat-8 热红外影像，以广义单通道算法反演地表温度时间序列；

• 反演一步把累积形变场送入带光滑正则化约束的 Okada 矩形位错模型，解出等效燃烧腔的几何参数，再用磁法、电法等地球物理调查结果独立核对。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/cemuAg1hRPsOEz8QwGzpZjgUmC41JmDM1fiaWeKQbqNBlZQcf9x3lK7kzqm4Zu5aHAdtTSFia9f9VkSHEGibibIslT5f5E7HIAnVBHtaBXLTpSE/640?from=appmsg)

非局部相位优化是形变一路的关键。它在估计每个像元相位时参考周围统计相似的像元，在低散射区域也能保住测量点密度，沉降盆地的边界因此更清晰。形变与温度两条时间序列还会做联合分析，用来刻画煤火活动的时空演变。

![](https://mmbiz.qpic.cn/mmbiz_jpg/cemuAg1hRPuSlMJaHFNGQw2SHicazCq8E0fChGibkHican1OM8ObDyXFqAuib7CDUFUwKFp3EJmKTnqm2VNzPo4szykL9jKPtHm070KygtrpGmc/640?from=appmsg)

03 结果：两个沉降盆地，深度对上了物探

实验矿区内共识别出两个主要沉降盆地，最大累积视线向位移分别约为 −160 毫米和 −120 毫米。也就是说，两年时间里，火区上方地面最深处沉降了约 16 厘米，这个量级与地下燃烧的持续掏空相对应。

![](https://mmbiz.qpic.cn/mmbiz_jpg/cemuAg1hRPsoZDiaWJssgCLh4lrLRI5YdpaJVBbYqHP7GF6sCxQIfX4dlf0QxzwJNy7FAcn73IUgWq4ia9VA6NJmXeqBIyqicNm4K5TtCoscgM/640?from=appmsg)

更关键的是深度。模型反演出的两处燃烧源深度为 53.11 米和 80.65 米，独立地球物理调查给出的估计是 56.0 米和 85.5 米。卫星从地面沉降反推的深度，与物探在地面测出的深度相差只有几米，两条独立的证据链对上了。

![](https://mmbiz.qpic.cn/mmbiz_jpg/cemuAg1hRPu2Bc4vVeFgWnsqEBvicJHC4lkOMItqXMaKQDa7xs0pIIIPbH7Hom6Pib92IvtPoobuLeFzCP7GxwnfstEJYb1j6UJfz9cia3Gt1Q/640?from=appmsg)

联合分析还给出了燃烧带的空间分工：长期燃烧带与集中沉降在空间上对应，热异常则优先出现在沉降中心周围的裂缝系统里。热量顺着裂缝往上跑，沉降标出烧空的主体，两种响应各管一摊，合起来才是完整的火区画像。

水西沟煤田位于新疆吉木萨尔县西南、天山北麓，团队此前已在同一煤田做过温度与形变融合的煤火识别研究。这次的工作在此基础上再推进一步：识别解决的是「火在哪里」，反演回答的是「火有多深、腔有多大」，后者直接决定治理工程的下手方式。

💡 小结：这篇论文的价值在于把「识别煤火」推进到「量出燃烧腔」。以往多源遥感多停留在圈定异常范围，这套框架进一步用物理模型反演出燃烧源的深度和腔体几何，并用物探结果闭环验证。对煤火治理来说，深度和范围正是决定封堵、注浆等工程措施怎么下手的先决参数。水西沟的结论能否直接迁移到其他煤田，也取决于地质条件是否相似。

论文信息：Yan, S., Qiu, W., Niu, Y., Zhang, H., Zhao, J., Lu, Z. Mapping subsurface combustion cavities in underground coal fires using nonlocal DS-InSAR and physics-based inversion. Remote Sensing of Environment, 348, 2026.

论文链接：https://doi.org/10.1016/j.rse.2026.115709

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ObyhaySm97WZNjpySwibqk7H5ntMHKzv68D9ES1ajKEoa99iaKyw0UHfrzyqxcAe0RgoS61lwXicia92djIK593Atg/0?wx_fmt=png)

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
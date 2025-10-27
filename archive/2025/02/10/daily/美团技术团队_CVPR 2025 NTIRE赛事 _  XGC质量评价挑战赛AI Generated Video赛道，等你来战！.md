---
title: CVPR 2025 NTIRE赛事 |  XGC质量评价挑战赛AI Generated Video赛道，等你来战！
url: https://mp.weixin.qq.com/s?__biz=MjM5NjQ5MTI5OA==&mid=2651779786&idx=1&sn=e916cd0a8e1f153de64cb03191dbcb34&chksm=bd122b878a65a291fe1c423a6ae3af7d8d3133d254b5650cf686710e0fe112e080397d890638&scene=58&subscene=0#rd
source: 美团技术团队
date: 2025-02-10
fetch_date: 2025-10-06T20:37:16.557480
---

# CVPR 2025 NTIRE赛事 |  XGC质量评价挑战赛AI Generated Video赛道，等你来战！

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hEx03cFgUsVRnq63vF3yMuMXUGC8nZ6TASsNkfbSMaXyQVS3jEs9OIGghdfV9U4zFzIaRptE6gsWgF0pJGibF7A/0?wx_fmt=jpeg)

# CVPR 2025 NTIRE赛事 | XGC质量评价挑战赛AI Generated Video赛道，等你来战！

原创

美团技术团队

美团技术团队

CVPR NTIRE（New Trends in Image Restoration and Enhancement）Workshop 是计算机视觉顶会CVPR下极具影响力的国际学术研讨会，聚焦图像复原、图像增强、生成技术、质量评估的突破性进展。为了促进视频生成技术的持续发展，美团联合上海交通大学在CVPR 2025 NTIRE Workshop上举办XGC质量评价挑战赛（AI Generated Video赛道），期望能够提供一种新的视频质量评价（VQA）方法，以准确预测生成视频的质量。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hEx03cFgUsVRnq63vF3yMuMXUGC8nZ6TjH2eEoWwbNwJlRd9ibibicznr72xloBpkc8G4biatE0oYR0qqB4mIa3zGw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hEx03cFgUsVRnq63vF3yMuMXUGC8nZ6TuUEib8fRFDPpa8N9Lvd0y56c5TsgoFNBTibbuIbWsGuhZwSGN916NHuQ/640?wx_fmt=png)

随着AIGC的蓬勃发展，以Sora、可灵AI为代表的模型引领了视频生成领域的一波热潮，为了推进视频生成这一领域的发展，置信准确的自动化评估生成算法性能成为一个重要任务。而对于AI生成的视频进行质量评价又和传统UGC视频有很大的区别，在对UGC视频进行质量评价时，我们更多关注视频的清晰度、色彩和光照；对于AI生成的视频，我们在进行质量评价时主要关注视频中物体运动的流畅性和内容的真实性，这就需要提出新的视频质量评价（VQA）方法，以准确预测生成视频的质量。

为此，我们与 NTIRE 研讨会联合举办了一项关于生成视频质量评价的挑战赛，任务是基于视频-prompt及其感知质量标签的先验示例，预测生成视频的感知质量分数。目标是设计一种网络，期望能获得一个与我们标注的真实值（MOS分数）尽可能高的相关性指标。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hEx03cFgUsVRnq63vF3yMuMXUGC8nZ6ThPbbf11AHSr8DKTsoWDkcGAVMNV71OlzF7uhibbv84M5sINk52iazgzA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hEx03cFgUsVRnq63vF3yMuMXUGC8nZ6TB0dFQb26icI4iccIw3ClWuLLeOd3dLZU7iaM6vYO3oJ6jLvrKYNslibuLg/640?wx_fmt=png)

我们的数据集具有很好的多样性和全面性，涵盖多种场景和内容。具体来说，其包含34,029个不同视频，这些视频由14个不同的视频生成模型（包括cogvideo、SVD等主流模型）使用4,689条prompt生成。我们按照7:1:2的比例将整个数据集划分为训练集、验证集和测试集。其中训练集包含23,820条生成视频、各自对应的prompt和质量分数；验证集包含3,402条生成视频以及各自对应的prompt；测试集包含6,807条生成视频以及各自对应的prompt。

**我们给出的具体数据集格式如下：**

这里以训练集为例，以JSON形式保存，每个字典元素包含两个属性，video存储视频名称，prompt为生成该视频使用的prompt，gt\_score为该视频的人工标注质量分数。

验证集、测试集无质量分数，仅包含video和prompt两个属性。

**提交结果格式如下**

结果同样要求保存为JSON文件，每个元素包含两个属性，video为视频名称，predict\_score为模型预测质量分数；同时我们要求额外提交readme.txt，记录模型其他信息，具体提交要求见比赛主页evaluation页面。

**评估指标**

Score = (PLCC + SROCC) / 2

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hEx03cFgUsVRnq63vF3yMuMXUGC8nZ6TL5U3ogF5Iy8D4H4l6dPXRqmQmUb14UwVF3z6WCiaYsW4ssO9iaFibWiahg/640?wx_fmt=png)

本次挑战赛面向全社会开放，个人、高等院校、科研单位、企业等人员均可报名参赛。每支队伍只能提交一种针对AI Generated Video质量评价算法进行最终排名。参赛队伍可自由选择是否发表竞赛相关论文，且该选择不会成为参加挑战赛或获奖的必要条件。

本次挑战赛将邀请排名靠前的参赛者向NTIRE研讨会提交论文，以供同行评审。论文录用后将发表在2025年CVPR研讨会论文集中。

**赛程安排**

2025.02.05 | 发布训练集和验证集

2025.02.05 | 发布在线验证平台

2025.03.14 | 发布测试集，关闭验证平台

2025.03.21 | 测试结果提交截止日期

2025.03.22 | 概况介绍和代码/可执行文件提交截止日期

2025.03.24 | 向参与者发布初步测试结果

2025.04.01 | 挑战参赛作品的论文提交截止日期

2025.06.15 | NTIRE研讨会和挑战、成果和颁奖典礼（暂定）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hEx03cFgUsVRnq63vF3yMuMXUGC8nZ6TePkchTUriagGtiaoziaEj5F8nOCFR4nibWHNl1SvjkyZvqHe2tPrAt6mfQ/640?wx_fmt=png)

CVPR NTIRE 2025官网：<https://cvlai.net/ntire/2025/>

CodaLab比赛网址：<https://codalab.lisn.upsaclay.fr/competitions/21485>

**比赛奖金**

**一等奖**：1200美元

**二等奖**：1000美元

**三等奖**：800美元

\*三个奖项各评选出一支获胜队伍。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hEx03cFgUsVRnq63vF3yMuMXUGC8nZ6TkjC3G1wsgX8e2EYsL9jUJwbriaX1UEFcz2s8manGrn5zE9t3Ie9Wiayw/640?wx_fmt=png)

NTIRE2025 XGC质量评价挑战赛- AI Generated Video赛道由上海交通大学与美团共同举办。其中交大团队成员包括刘笑宏、闵雄阔、翟广涛教授及其带领的博士后孙伟，博士研究生张子澄、李春一，硕士研究生寇腾川、王书石。美团成员来自计算和智能平台部。

特别感谢[AGI-Eval](https://agi-eval.cn/mvp/home)大模型评测社区为本次赛事提供人工标注结果。AGI-Eval是由上海交通大学、同济大学、华东师范大学、Datawhale等高校和机构合作发布的大模型评测社区，以“评测助力，让AI成为人类更好的伙伴”为使命，旨在打造公正、可信、科学、全面的评测生态，牵引模型实现通用人工智能。

在比赛中遇到的任何问题可以联系组织者：

**王书石** <wss2002@sjtu.edu.cn>

**补充信息**

下面是我们CVPR论文中对于该数据集的一些实验：

1. 不同生成模型得到的视频质量分数分布图

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hEx03cFgUsVRnq63vF3yMuMXUGC8nZ6Tq1Tqiae5yaDIVIXVhYUmvIibqGjz284ASrYw6VMiaFhot9MzjkqVEU6dQ/640?wx_fmt=png)

2.目前业界并无成熟的用于AI生成视频质量评价的算法，下面是我们使用现有图像质量评价模型和多模态大模型在我们的数据集上进行的实验结果：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hEx03cFgUsVRnq63vF3yMuMXUGC8nZ6TNygicSEzicUrhIgNlDTkEJ71Qzpd6bkF4N53IFia2IZ7ibD04aEfo0xlZA/640?wx_fmt=png)

可以看到，直接将现有的图像质量评价模型或多模态大模型应用到该任务上很难取得一个好的效果。因此，我们诚挚地邀请参赛者积极参与此次挑战，提交高质量的算法方案。您的创新和努力将对推动这一领域的发展起到至关重要的作用。我们期待大家的参与和贡献，以共同促进AI 生成视频质量评价技术的发展。

**NTIRE 2025 XGC 比赛交流群**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hEx03cFgUsVRnq63vF3yMuMXUGC8nZ6TZwhrFictf8MXfp2joEcFHe5pjXXYPDb15KHHsHANvHOHmmZkYhZczMQ/640?wx_fmt=jpeg)

如果链接过期，请联系

王书石<wss2002@sjtu.edu.cn>

点击文末[阅读原文](https://codalab.lisn.upsaclay.fr/competitions/21485)，直达比赛网址

欢迎大家报名参赛！

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/hEx03cFgUsVGibnsaEib3aNlqF0tOrA2RGEmNSbia2nnohE4Tpf95UyTiaSjDVbHRfY8WNBeTuLLTaVdSckkNyEx1Q/0?wx_fmt=png)

美团技术团队

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/hEx03cFgUsVGibnsaEib3aNlqF0tOrA2RGEmNSbia2nnohE4Tpf95UyTiaSjDVbHRfY8WNBeTuLLTaVdSckkNyEx1Q/0?wx_fmt=png)

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
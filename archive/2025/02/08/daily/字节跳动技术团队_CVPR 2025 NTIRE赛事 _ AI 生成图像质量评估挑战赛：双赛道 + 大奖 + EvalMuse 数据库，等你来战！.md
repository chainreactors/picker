---
title: CVPR 2025 NTIRE赛事 | AI 生成图像质量评估挑战赛：双赛道 + 大奖 + EvalMuse 数据库，等你来战！
url: https://mp.weixin.qq.com/s?__biz=MzI1MzYzMjE0MQ==&mid=2247512994&idx=1&sn=9f9973f045bd18d0d54352882528615d&chksm=e9d37840dea4f156cc97dd8bd7a8ff41bff2b59cd5c1351fbaed8ee123c5bfa827a3056d8ebf&scene=58&subscene=0#rd
source: 字节跳动技术团队
date: 2025-02-08
fetch_date: 2025-10-06T20:38:15.480214
---

# CVPR 2025 NTIRE赛事 | AI 生成图像质量评估挑战赛：双赛道 + 大奖 + EvalMuse 数据库，等你来战！

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/IMJ5I2wiakztSnU1QgNBIzY7ia5uvRkice6WxtCGdsXAI9xLSEibicnQtf6nSZpSqHvyKssu6iaYf8DJpocSp54WeH2A/0?wx_fmt=jpeg)

# CVPR 2025 NTIRE赛事 | AI 生成图像质量评估挑战赛：双赛道 + 大奖 + EvalMuse 数据库，等你来战！

字节跳动技术团队

以下文章来源于抖音多媒体评测实验室
，作者抖音评测实验室

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM4WnVwcnMM07XK9RjteWrOSyuB4JuM81vYy4jtGStVLjA/0)

**抖音多媒体评测实验室**
.

抖音端到端视频图像画质，音频评测技术以及各类增强算法分享。

CVPR NTIRE（New Trends in Image Restoration and Enhancement）Workshop 是计算机视觉顶会CVPR下极具影响力的国际学术研讨会，聚焦图像复原、图像增强、生成技术、质量评估的突破性进展。为了推进生成图像/视频领域的发展，建立生成图像/视频领域的质量评估“黄金标准”，抖音多媒体质量实验室/豆包大模型团队（字节跳动）联合南开大学在第十届CVPR NTIRE workshop上举办AI生成图像质量评估学术竞赛。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/IMJ5I2wiakztSnU1QgNBIzY7ia5uvRkice6J0QZEX2PegmnFib0F2NegImArqqkffjmLQV7tSibB5WnlS9tKZ92Jy5A/640?wx_fmt=png&from=appmsg)

**比赛介绍**

近年来，文生图（T2I）模型技术迅速发展，催生了Dreamina、DALL·E3和Midjourney等热门工具。它们能够精准理解用户的prompt（提示词），将简短描述转化为高质量且富有美感和一致性的图像。这一技术显著降低了创作门槛，提升了效率和趣味性，让艺术创作、广告设计及日常分享变得更加简单直观。文生图技术的普及，为数字内容创作开辟了全新可能性。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/IMJ5I2wiakztSnU1QgNBIzY7ia5uvRkice60HhUnAT2icyj3adiad0rJLwjqj7wY0tbs0ZWcaQEYIibZyWp6FeMMTNvw/640?wx_fmt=png&from=appmsg)

然而，如何评估文生图模型的性能，特别是**在图文匹配度/美学/结构完整性方面**，一直是一个巨大的挑战。传统评估方法已无法全面衡量图像与文本的匹配度，多模态大模型对结构问题的挖掘能力也存在很大不足。为解决这一问题，抖音多媒体质量实验室与豆包大模型团队及南开大学合作，**推出了业界规模最大的文生图评估数据库—EvalMuse**，并提出了SOTA的文生图评价解决方案，具体内容可以参考论文EvalMuse。

> 论文🔗：https://arxiv.org/abs/2412.18150

基于**EvalMuse**提供的大规模数据集，本次竞赛开设两个子赛道，分别为文生图的**图文匹配度**和**结构问题挖掘**的自动化评估能力。

**赛事具体介绍**

**Track 1-生成图像质量评估-细粒度图文匹配度打分**

比赛网址：https://codalab.lisn.upsaclay.fr/competitions/21220

数据介绍

* 训练数据：包含30k个image-text 对，这些图像是通过20+T2I生成模型、3000个prompts生成的。我们提供了图文匹配度打分（prompt level）和细粒度图文匹配度打分（element level）的标签来进行训练/测试（具体内容可见evalmuse paper）。
* Validation阶段数据：约10k image-text pairs。
* Test阶段数据：约5k image-text pairs。
* 以上数据可通过codalab比赛主页，参与对应比赛获取链接。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/IMJ5I2wiakztSnU1QgNBIzY7ia5uvRkice68cm7DH6ncTybEtv9bxibhfwmTITKpyibalY9zDb93LxPhibm5J9ZTa0Dw/640?wx_fmt=png&from=appmsg)

模型输出要求&baseline

要求模型输出prompt维度的图文匹配度分数，以及element维度是否命中的标签。

> 例：
>
> 给定Prompt ：musician plays guitar aerial shot , 给定element : musician,plays,guitar,aerial shot
>
> 模型需要输出
>
> 1. 整体图文匹配度打分(可归一化到1-5)
> 2. element维度是否命中，0代表未命中，及图像中不存在element对应的元素，1代表命中，及图像中存在element对应的元素。以上图为例，musician，plays，guitar均命中，应输出1，aerial shot未命中，应输出0.

Baseline可参考Fga-blip2仓库：https://github.com/DYEvaLab/EvalMuse

评估指标

本赛道通过prompt维度图文匹配度打分srcc/plcc以及element维度的acc来确定最终得分。具体计算方式可见比赛codalab网站，Evaluation部分。

> Final\_Score = PLCC / 4 + SRCC / 4 + acc / 2

**Track 2-生成图像质量评估-结构问题挖掘**

* 比赛网址：https://codalab.lisn.upsaclay.fr/competitions/21269

数据介绍

* 训练数据说明：以json形式保存，字典的key为img\_name，value为每张图片的标注信息
* 信息说明：

+ prompt\_en：生成图像的prompt，英文。
+ mos：图像的结构mos分数，范围为1-5分。
+ bbox\_info：有结构问题的区域标注信息，列表格式，长度为3，元素为一个信息列表，分别代表每一个标注员的标注结果，若列表为空则代表该标注员认为当前图像中没有结构问题；若列表不为空，则其中元素为字典形式，记录每一个结构问题区域的bbox信息：

1. bbox\_type：bbox标注类型，值为1表示该标注为矩形bbox，值为2表示该标注为多边形bbox
2. bbox：列表格式，元素为bbox顶点坐标

1. bbox\_type=1 ，记录矩形的左上角、右下角坐标
2. bbox\_type=2， 以顺时针顺序记录多边形顶点坐标

模型输出要求&baseline

将结果保存为dict，以pkl格式存储，img\_name与测试集图片命名保持一致，对应一张图片的预测结果。

baseline可参考 ：https://github.com/DYEvaLab/EvalMuse-Structure

评估指标

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/IMJ5I2wiakztSnU1QgNBIzY7ia5uvRkice6FReQcLicmtVDOho7QrwKRlWwK6rZ0sM0zfzAu0ChoibhbkWPn0RWUItg/640?wx_fmt=jpeg&from=appmsg)

**大赛奖励**

* 本次大赛由将由**抖音多媒体质量实验室提供奖金！总额在****10w元人民币****左右**，具体奖项设定待定，届时会在比赛codalab网站上进行更新说明。
* 参赛队伍可自由选择是否发表竞赛相关论文，本次挑战赛将邀请排名靠前的参赛者向NTIRE研讨会提供论文，论文录用后将会发表在2025年CVPR研讨会论文集。
* 赛道排名前三的队伍将会获得CVPR NTIRE的获奖证书及由抖音多媒体质量实验室提供的奖金。两条赛道的奖金暂定如下：

+ 第一名：2000-4000美元奖金 + 证书
+ 第二名：1000-2000美元奖金 + 证书
+ 第三名：500-1000美元奖金 + 证书

**大赛要求**

* 本次学术竞赛面向全社会开放，个人、高校、科研单位、企业等人员均可报名参加。
* 每支队伍只能提供一种方法进行最终排名。
* 为保证公平性，如果使用额外数据，请在最终方案报告中说明。
* 提交的方法必须本地可复现，提交API的方式不被允许。

**大赛官网**

图文匹配度赛道网址：

https://codalab.lisn.upsaclay.fr/competitions/21220

结构问题挖掘赛道网址：

https://codalab.lisn.upsaclay.fr/competitions/21269

EvalMuse项目主页：

https://shh-han.github.io/EvalMuse-project/

EvalMuse 开源项目地址：

https://github.com/DYEvaLab/EvalMuse

**交流群**

如链接过期，可联系

hansh@mail.nankai.edu.cn

fanhaotian@bytedance.com

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/IMJ5I2wiakztSnU1QgNBIzY7ia5uvRkice6ysffFm73wfIXYtt73ib18FQ3p2pjU5nxmnnic337OyRibcSELKeeBBkiaQ/640?wx_fmt=jpeg&from=appmsg)

**主办方**

CVPR NTIRE 2025 文生图质量评估挑战赛由抖音多媒体质量实验室与南开大学共同举办。主办方联系方式：

* 如对比赛细节有疑问，可优先联系

+ hansh@mail.nankai.edu.cn
+ fanhaotian@bytedance.com
+ lichongyi@nankai.edu.cn

* 其他organizers联系方式

+ litao.walker@bytedance.com
+ cuijunhui@bytedance.com
+ sunjingwei.jerry@bytedance.com
+ guochunle@nankai.edu.cn
+ radu.timofte@uni-wuerzburg.de
+ kongfangyuan@bytedance.com
+ wangyunqiu.qqq@bytedance.com
+ liliang.58@bytedance.com

**附：EvalMuse数据库介绍**

> 具体介绍参考https://mp.weixin.qq.com/s/RWxspVh0SbisNKEb75jrOw

**EvalMuse-40K**是一个包含40,000对图像-文本对和超过100万细粒度人类标注的Benchmark，旨在全面评估T2I模型在图像-文本对齐方面的表现。该Benchmark的构建过程既复杂又细致，我们通过精心设计的数据集和标注体系，力求最大程度地反映T2I模型在实际应用中的表现。

**EvalMuse-40K** 的构建过程复杂而细致。我们首先从 **DiffusionDB** 中收集了2,000个真实用户的提示，这些提示反映了用户的多样化需求。同时，我们生成了2,000个合成提示，涵盖了物体数量、颜色、材质、环境设置、活动属性等多个方面，以全面评估T2I模型在不同任务中的表现。

接下来，我们使用20种不同的扩散模型生成了40,000张图像，确保了图像的多样性和质量。在数据标注阶段，我们对这些图像-文本对进行了细致的人工标注，涵盖图像-文本对齐评分、元素级别的匹配检查和结构问题标记。标注过程分为预标注、正式标注和重新标注三个阶段，以确保数据的可靠性和准确性。

与现有的文本到图像（T2I）模型的Benchmark相比，**EvalMuse-40K**提供了一个更大规模、更细粒度的评估数据库。超过100万细粒度人类标注，使得 **EvalMuse-40K** 在数据集规模和多样性上远超许多现有Benchmark。与业界一些相关Benchmark的比较见下表：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/IMJ5I2wiakztSnU1QgNBIzY7ia5uvRkice6E1XADOG9Veyeicx37DibeIt52K6jib3YuXMOxKIuic27ia0B8nicAOr9cMSQ/640?wx_fmt=png&from=appmsg)

除此之外，EvalMuse还提供了两种SOTA的图文匹配度评估算法，旨在提升图文匹配度评估的准确性，确保与人类评估结果的一致性。

**关注我们，了解更多精彩**

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
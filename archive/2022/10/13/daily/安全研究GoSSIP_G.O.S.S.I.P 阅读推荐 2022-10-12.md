---
title: G.O.S.S.I.P 阅读推荐 2022-10-12
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247492887&idx=1&sn=03dbf3caa13b448b6f9d1a4d1acbb8d2&chksm=c063cbcef71442d83b19f7f476529e62d0439007ac35539eba781c920efa66de794551f6014d&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2022-10-13
fetch_date: 2025-10-03T19:47:28.712939
---

# G.O.S.S.I.P 阅读推荐 2022-10-12

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/uicdfzKrO21FVOuWOjgftKN2TXbkIPHEdKoghnHjmHYYTwb0OGI1REzIuK6nBBgtgGiakhtsRg0ibgSxcnICxZLew/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2022-10-12

Zizhuang@IIE

安全研究GoSSIP

今天为大家推荐的论文是来自[中科院信工所陈恺、孟国柱老师研究组](http://mp.weixin.qq.com/s?__biz=MzA5MzQ1MDI2MA==&mid=2456041846&idx=1&sn=45db2c6fabe2c61db50d4675c051ce46&chksm=87cd200db0baa91b57417adfa41131eaa0f8c6027a79afe01590369eadd03aef342f46c06a90&scene=21#wechat_redirect)投稿的关于大规模终端应用中深度学习模型安全性度量评估的工作***Understanding Real-world Threats to Deep Learning Models in Android Apps***，目前该工作已发表于CCS 2022。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21FVOuWOjgftKN2TXbkIPHEdRLMgndRD8EzibTDNyhzd9Tg6UIaVh0JHWib4M4bGrpZGu05N6JnyyZrg/640?wx_fmt=png)

在这项研究工作中，作者旨在了解终端应用中的深度学习模型是否会受到两种威胁的影响，即模型窃取威胁和对抗样本威胁，如果受到影响，进一步评估这种影响带来的威胁的严重程度。最后，作者将提供在这项工作中收集使用的现实模型数据集。该工作设计一套方法来自动化提取模型并且对其进行测试，适配到当前的对抗样本生成算法。包括四个步骤：

1. 自动化从app中提取深度学习模型；
2. 从应用代码中推理深度学习模型的接口信息和使用方法；
3. 生成并验证测试数据集，以供模型使用；
4. 适配攻击算法生成对抗样本，并通过观察app的执行来验证攻击效果。对于黑盒模型，该工作设计了一种基于语义的方法来建立合适的数据集，并在进行迁移攻击时使用它们来训练替代模型。

该工作存在的三个难点：

1. 如何从移动app中自动化提取模型；
2. 自动化分析得出模型的使用接口信息（包括模型的输入，输入预处理方法和参数，模型的任务及输出）；
3. 自动化生成和验证对抗样本是一个挑战。

为了解决上述挑战，该工作设计了一种方法，如图1所示，并实现了一个名为AdvDroid的工具。随后对移动app中的深度学习模型进行大规模的端到端攻击，包括自动提取设备上的深度学习模型，分析其输入格式和输出标签，通过各种攻击方法生成对抗样本，并验证生成的对抗样本，进而衡量各种对抗样本生成算法的性能。为了解决第一个挑战，作者发现无论如何改变模型的文件名和位置，app最终会通过深度学习框架提供的API加载模型。即使模型是加密的，app也会在使用模型进行推理之前在内存中解密。基于这一观察，AdvDroid采用一种语义引导的方法来提取模型文件。如果模型是加密的，AdvDroid试图自动触发加载模型的代码（称为模型推理调用点或简称MIS）。在app加载模型后，AdvDroid通过API钩子动态地从内存中提取解密的模型。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21FVOuWOjgftKN2TXbkIPHEdoeShr1D68L6Q4PfYPJE6DWojIZahZYfUYfquCia5uvu4QPgZ5LBjj5g/640?wx_fmt=png)

图1. 移动端深度学习模型攻击测试框架图

然后，AdvDroid推断出模型的输入和输出（又称模型接口）。为了实现这一目标，AdvDroid首先定位了MIS（模型调用点），然后用MIS的交叉引用进行数据流分析。该工作还设计了量身定做的静态数据流分析，以快速确定是否存在从输入（即源点）到MIS（即汇点）的路径，如果有，app如何预处理输入。另外，从MIS中，AdvDroid进行前向切片，以定位和识别输出。如果提取的模型可以被加载到已知的深度学习框架中，并且它们的接口可以被识别，则被视为白盒。否则，它需要更多的步骤来攻击不能从app中加载的黑盒模型。这项工作专注于图像分类和物体检测模型，因为它们占据了设备上模型的大部分（70.31%）。更进一步地，该工作根据不同的模型提取难度，将模型分成三类：（1）Type-A：未加任何保护的开源框架模型；（2）Type-B：添加了一定保护的开源框架模型；（3）Type-C：使用闭源框架的黑盒模型，他们的分布情况如表1所示，括号内为去除重复后的模型数目。总体来看，模型窃取难度较低，61.2%的模型可被提取加载。并且基于自动化的模型接口推理方法，作者将模型攻击成功比例从7%提升到47%。

同时，文章对现实世界的模型和传统模型进行了比较。现实世界的模型与学术界的模型表现出明显的差异。具体来说，现实世界模型：1. 容易采用低成本的网络架构，如MobileNets、EfficientNet，这对预测精度有负面影响。这些模型的平均文件大小为4.35MB。2. 为边缘设备和硬件加速器（如TPU、NPU）设计的混淆层或自定义运算符。在本文数据集中发现了12种自定义运算符，例如MaxPoolingWithArgmax2D、MaxUnpooling2D、StrSim和TextEncoder3。3. 存在模型量化（占比40.55%），模型压缩和剪枝优化。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21FVOuWOjgftKN2TXbkIPHEdabTkHvLM8AT13TzmlHIQIGy3zucscbnBT954wbZjcS3EsxkDHaPw6A/640?wx_fmt=png)

表1. 三类模型在不同深度学习框架中的分布情况

最后，作者总结有以下几项新的发现，（一）对抗攻击方面：1）同一模型在不同的攻击算法测试下CW方法最优；2）非量化模型生成的对抗样本在量化模型上的可迁移性较差。（二）物理窃取方面：1）对模型所在的app类别分析，发现模型集中在照片/视频处理类别的app中，图片格式模型占比最多；2）模型承担的安全攸关任务中占比最多的两项任务分别是人脸识别和证件/票据识别；3）现有模型中已经部署了一些模型保护措施，分系统层面和模型层面。系统层面：模型远程加载，模型加密，模型打包，身份认证，完整性校验等；模型层面：神经网络层混淆，权重变换，自定义算子等。同时这其中也有不少问题：有些app直接将模型解密密钥明文放在代码中，有些app对模型使用者的鉴权仅仅依赖本地校验码等。

文章链接：https://arxiv.org/abs/2209.09577

---

投稿作者：邓子壮@IIE

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EibxMcqx9KdafugxDicBiaW3cb1gyTuWooDCJjH1ibu8aibOiapYLq8BJMwNbIeUK1t0japdvmdqTfCxhg/0?wx_fmt=png)

安全研究GoSSIP

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EibxMcqx9KdafugxDicBiaW3cb1gyTuWooDCJjH1ibu8aibOiapYLq8BJMwNbIeUK1t0japdvmdqTfCxhg/0?wx_fmt=png)

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
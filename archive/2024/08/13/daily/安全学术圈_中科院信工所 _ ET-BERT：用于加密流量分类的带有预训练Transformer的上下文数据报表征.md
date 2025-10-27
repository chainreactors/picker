---
title: 中科院信工所 | ET-BERT：用于加密流量分类的带有预训练Transformer的上下文数据报表征
url: https://mp.weixin.qq.com/s?__biz=MzU5MTM5MTQ2MA==&mid=2247491101&idx=1&sn=2cd8538a36a20d92477f737f94b91de8&chksm=fe2ee196c959688049b704a7cdadc62d4421beb9705d091eac22c6973f70a4fca07232f12779&scene=58&subscene=0#rd
source: 安全学术圈
date: 2024-08-13
fetch_date: 2025-10-06T18:07:36.562749
---

# 中科院信工所 | ET-BERT：用于加密流量分类的带有预训练Transformer的上下文数据报表征

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6Dibw6L070WHzF9RvjtjQKrRIziaU1w4uELOvyHnH6nDyDds4E87Zj3hFUB8cR4mToI013BHgicl2xUrC3qtApRLQ/0?wx_fmt=jpeg)

# 中科院信工所 | ET-BERT：用于加密流量分类的带有预训练Transformer的上下文数据报表征

原创

JSY

安全学术圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WHzF9RvjtjQKrRIziaU1w4uE06zd8NW6Plwwmv13GnGc4TkWh4ta9MPC4fcTWCvTsrYq41c1IMP9Kw/640?wx_fmt=png&from=appmsg)

> *论文题目：ET-BERT: A Contextualized Datagram Representation with Pre-training Transformers for Encrypted Traffic Classification*
> *论文作者：Xinjie Lin, Gang Xiong, Gaopeng Gou, Zhen Li, Junzheng Shi, Jing Yu*
> *发表会议/期刊：WWW*
> *发布时间：2022*
> *主题类型：流量分析*
> *笔记作者：JSY@Web攻击检测与追踪课程*
> *通信作者主页：于静 https://mmlab-iie.github.io/*

本文提出了一种新的加密流量分类模型ET-BERT，利用预训练的Transformer模型进行深度上下文数据包表示的学习。

加密流量的广泛使用带来了巨大的挑战，传统的基于深度包检测（DPI）的方法由于无法访问加密流量的内容，难以适用于加密流量分类，针对特定加密流量的方法难以适应新环境或新的加密策略。

### 研究方法

ET-BERT模型运作阶段由两部分组成：预训练阶段和微调阶段；其核心包括三个部分，Datagram2Token，Pre-training和Fine-tuning。![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WHzF9RvjtjQKrRIziaU1w4uEqYBS66fwY2WkhJ7x5YGZMMdQrL0vCpsIthPSly1VyfaogGKUTicdPzg/640?wx_fmt=png&from=appmsg)

* **Datagram2Token**用于将网络流（由五元组确定）转化为能被BERT接受的token序列。分为3步：

+ BURST Generator 用于将流量形成BURST（作者定义为单个会话中的一系列请求或响应的包，分为src和dst两个方向）。
+ BURST2Token 用于将每个BURST中的数据包转化为基于字节对编码（Byte-Pair Encoding）的token表示。
+ Token2Embedding 用于将token表示、位置表示和段表示拼接（即BERT需要的输入格式），作为预训练的输入。

* **Pre-training**用于对流量数据进行BERT模型预训练。

+ Masked BURST Model (MBM)：类似于BERT中的Masked Language Model，其实现方法是通过随机掩码部分token，让模型根据上下文预测被掩码的token（即BERT训练过程）。
+ Same-origin BURST Prediction (SBP)：用于预测BURST之间的关系，即通过预测两个sub-BURST是否来自同一BURST源，捕捉流量包之间的依赖关系。

* **Fine-tuning**用于对BERT模型进行微调，微调过程与预训练基本一致，目的是创造两个微调模型：

+ Packet-level Fine-tuning：实现对输入单个数据包进行分类。
+ Flow-level Fine-tuning：输入多个连续的数据包（流）进行分类。

### 实验结果

文章提供了五个实验，使用的数据集如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WHzF9RvjtjQKrRIziaU1w4uEKOtPJBBxzNMv3D6QeyP2kbJyia1Mnhf7L7gOWOA0faaPTZtYX3HdE1A/640?wx_fmt=png&from=appmsg)

1. 通用加密应用分类（GEAC）：测试在标准加密协议下的跨平台应用流量分类
2. 加密恶意软件分类（EMC）：对恶意软件和良性应用的加密流量进行分类
3. VPN加密流量分类（ETCV）：对VPN进行通信的加密流量进行分类

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WHzF9RvjtjQKrRIziaU1w4uELRRGo9mmYazmbb7TVDibq84dcaKLrJu5WJsD2jSrX6CrzQ3freheZVg/640?wx_fmt=png&from=appmsg)

4. Tor上的加密应用分类（EACT）：对Tor流量进行分类
5. TLS 1.3上的加密应用分类（EAC-1.3）：对基于新加密协议TLS 1.3的加密流量进行分类

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WHzF9RvjtjQKrRIziaU1w4uEDDABI5SzO2RAFJicKFicpqdFhveY0gGqzhJ6iculdJiaDEcBemY7TSleGg/640?wx_fmt=png&from=appmsg)

作者还做了消融实验：![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WHzF9RvjtjQKrRIziaU1w4uEPMN3XFl7myAHyLOYRrxd4xg6hrsDaELoTzC7ibkIA5TxIoqqc8N6WLQ/640?wx_fmt=png&from=appmsg)

对比实验：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WHzF9RvjtjQKrRIziaU1w4uEzD0wu9Mkw0oVEHP9ly9eayf1PB35uxD31bo9ImuKDWh8ibF5nRPlU0w/640?wx_fmt=png&from=appmsg)

多种加密算法的实验：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WHzF9RvjtjQKrRIziaU1w4uEyXjY4Q75ic9wEzAnRTY1pp0bjuLCLQhrHbTRe3la0f9ZLibs8OqMic1mA/640?wx_fmt=png&from=appmsg)

以及实用性实验等。

## 贡献分析

* 贡献点1：论文针对加密流量分类问题，提出了一个利用大规模未标记加密流量进行预训练的框架，实现了通用数据包表示的学习。
* 贡献点2：论文针对加密流量中隐含模式难以捕捉的问题，提出了两种自监督预训练任务（Masked BURST Model 和 Same-origin BURST Prediction），实现了字节级和BURST级上下文关系的捕捉。
* 贡献点3: 论文针对加密流量分类任务中数据不平衡和新加密技术难以适应的问题，提出了利用预训练模型进行微调的方法，实现了在五个加密流量分类任务上取得新的最先进性能。

## 代码分析

* 代码使用类库分析：该代码 https://github.com/linwhitehat/ET-BERT（72 Forks，302 Stars）不全为开源类库的集成，提供了较为良好的工具CLI和文档，可在较为用户友好的情况下运行。
* 代码实现难度适中，工作量极大，因其包含了对大量开源数据集的整合和处理工作，以及对BERT模型的预训练和微调的工作。
* 代码关键实现的功能如上文所示，主要有三个部分：Datagram2Token，Pre-training和Fine-tuning。其中我认为预处理部分，即Datagram2Token和数据预处理是代码中最为关键的部分，也是全文较为值得借鉴的部分。其涉及将流量包转化为BERT能识别和训练的Token。

## 论文点评

* 优点：

+ 实验详实，工作量足
+ 语言简单，较为易懂
+ 考虑到的方法较为全面，性能也相较当时的SOTA更佳。

* 可改进之处：

+ 速度和占用资源问题：BERT作为预训练模型，其模型参数较大，在运行时需要占用更多算力资源，运行时也会较为慢。也许可以通过使用模型蒸馏或模型量化的方式改善这一问题。
+ 模型过时问题：BERT较为古早，新的预训练模型，甚至LLM的技术已经被提出。也许可以通过新的预训练模型来实现该任务来改善这一问题。
+ 可扩展性问题：模型可能会产生类似“概念迁移”的问题，同样，对于较新的恶意代码产生的流量，该模型可能会难以识别。也许可以通过在线训练的方式来实现该任务来改善这一问题。
+ 可解释性问题：深度学习模型会存在可解释性问题。BERT基于Transformer，亦存在可解释性问题。解决方式仅有进一步研究和提升模型的解释性，提供更多关于模型如何进行特征提取和分类决策的细节来改善这一问题。
+ 实际应用的问题：模型仍然存在着一定的漏报率，而且由于其基于较复杂的预训练模型（BERT-base已经有几百M的大小），在线实时检测或是旁路镜像检测镜像检测的速度均无法满足要求。解决方式可以是提升检测机器的性能；但该模型的实用程度可能当前还仅能停留在实验室。

> [安全学术圈招募队友-ing](http://mp.weixin.qq.com/s?__biz=MzU5MTM5MTQ2MA==&mid=2247484475&idx=1&sn=2c91c6a161d1c5bc3b424de3bccaaee0&chksm=fe2efbb0c95972a67513c3340c98e20c752ca06d8575838c1af65fc2d6ddebd7f486aa75f6c3&scene=21#wechat_redirect)
> 有兴趣加入学术圈的请联系 **secdr#qq.com**

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/6Dibw6L070WFvZRQiafv3iccicic1dIYUEQ1ZzLh1a10l7tfw7zkWkRbY9kEPBwX2NiadOrwFl9a48as9qiayp3eOgDUQ/0?wx_fmt=png)

安全学术圈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/6Dibw6L070WFvZRQiafv3iccicic1dIYUEQ1ZzLh1a10l7tfw7zkWkRbY9kEPBwX2NiadOrwFl9a48as9qiayp3eOgDUQ/0?wx_fmt=png)

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
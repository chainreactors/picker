---
title: AI For Security，你真的用明白AI了吗？
url: https://mp.weixin.qq.com/s/_a6qpyxTgcDhNTg5oRquzw
source: Doonsec's feed
date: 2026-05-16
fetch_date: 2026-05-17T05:43:04.916993
---

# AI For Security，你真的用明白AI了吗？

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/M0M2LxLjvZj0FFRtu3gGweAfFDFLBwFQUicDt16Ao256Da3G4ibvaRXnk8jpZicGPfoVVsGVQSDwezguK5KzMaFhv0QbWffVM65cLhHFibv8VeY/0?wx_fmt=jpeg)

# AI For Security，你真的用明白AI了吗？

原创

Alphabug
Alphabug

百灵鸟安全团队

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

## 前言

大家好，我是Alphabug。随着LLM的快速发展，它已经改变了各行各业从业者的工作习惯，但大家都真正用好AI了吗？

## 事件1

2024年11月，在我参与支撑的一个项目交流会议上，客户想办一个“AI+创新”比赛（面向网络安全技术人员）。我方师傅执着于让选手训练大模型。我当时心里在想：大家真的懂什么是LLM吗？

## 现象

2025年11月底，Anthropic的Claude Opus 4.5发布，惊艳业界。12月我测试了Cursor内置的Opus 4.5，能力提升非常大。2025年6月时无法处理或生成的“AI For Security”项目代码，在这次测试中都高效完成了。周围研究技术的大佬们高喊“AI是未来”，据我了解，很多公司也都在“梭哈AI”，目的有两个：一是降本增效，二是想“分AI+市场的一杯羹”。有一次同事跟我说，他一夜烧掉了1亿个Opus 4.6 Token，我很震惊！

以Claude Max套餐为例，1亿Token的消耗量对应如下成本：

| 套餐版本 | 月费 | 额度相对于 Pro | 能覆盖 1 亿 token/月 吗？ |
| --- | --- | --- | --- |
| Claude Max 5x | $100 | 5 倍 | ❌ 约 4000 万 token，不够 |
| Claude Max 20x | $200 | 20 倍 | ✅ 约 1.6 亿 token，足够且有富余 |

## 事件2

最近在给客户培训过程中，我发现学员喜欢用AI帮他们打靶标，结果折腾了半小时也没打出来。培训内容是比较基础的渗透测试实战。其中有一套环境，是我几年前随便从GitHub找了个CMS搭建的，当时网上没有POC也没有Exploit。我凭着经验，5分钟不到就完成了从信息收集到后台getshell。这个环境当时发给过其他师傅一起玩，他们也差不多10分钟左右都能拿下，很有实战意义。

## 思考

所以，“AI For Security”到底反映出什么？我思考了很久，大概梳理出使用AI的以下几类情况：

* **懂安全，用好AI**：效率翻倍，突破性创新潜力巨大，实实在在降本增效；
* **懂安全，不会用AI**：相比用好AI的人，效率较低，Token消耗巨大；
* **不懂安全，不懂AI**：想尝试“AI For Security”，Token消耗巨大，而且反复消耗同类型Token。

因为“懂安全”，在决策上能让LLM少走弯路，减少不必要的Token消耗；因为“用好AI”，知道让AI做哪些事、怎么做、预期结果是什么，效率翻倍。

如果你正在做或打算做“AI For Security”，那么Token消耗、模型选择、时间成本都需要认真考虑。

## 那LLM值得自己训练吗？

LLM是Large Language Model（大型语言模型）的缩写。它是一种基于深度学习、参数量巨大（通常从数十亿到数万亿不等）的人工智能模型，通过在海量文本数据上进行预训练，学习语言的语法、知识、推理和上下文理解能力。

很多人一谈AI就要“训练大模型”，但真正值得自己从零开始训练的，少之又少。从零开始在TB级原始文本上，通过分布式训练框架（如Megatron-DeepSpeed）完成全量参数更新，需要满足：

* **参数规模**：通常≥70亿（7B），千亿级（100B+）才算“大模型”。
* **数据量**：训练Token数需达1-2万亿（例如LLaMA-3 70B使用15T Tokens）。
* **算力门槛**：需千卡级AI加速集群（如512张A100/H100），单次训练耗电可达数百万度。

**关键区别一定要分清：**

* **训练（Pretraining）**：从头学习语言规律，成本极高（70B模型约50万-200万美元）。
* **微调（Fine-tuning）**：在预训练模型上调整部分参数，成本可降至1/10以下（如LoRA仅需单机8卡）。

| 任务类型 | 算力需求 | 成本范围 | 典型场景 |
| --- | --- | --- | --- |
| 全量预训练（70B+） | 512-1024张A100/H100 | 50万-200万美元 | Meta、OpenAI等头部企业 |
| 指令微调（SFT） | 8-64张A100 | 5千-5万美元 | 企业定制行业模型 |
| 参数高效微调（LoRA） | 1-8张消费级显卡 | <500美元 | 个人开发者实验 |

训练1个70B模型需要140TB显存总量（远超单卡80GB上限），必须依赖分布式训练框架，而非技术人员几乎无法掌握通信优化技术。电力消耗方面，单次70B训练耗电约300万度（相当于300户家庭年用电量）。

**所以，除非是头部企业或国家级实验室，否则“训练LLM”这句话，大概率是把“微调”或“调用API”说错了。**

***以上表格、数据来源于 AI 模型（Qwen、DeepSeek）。***

## 总结

AI For Security 的核心，从来不是你有没有AI，而是你懂不懂安全，以及会不会用AI。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/mmbXTwYCQ9mPH65CMJ4RhCx8MWdmyFLYHtyibVkeA5DPU9dVRGgZo9XSdT7NfrKl4bEiaNZibwxTSvqHPPRI8YAtQ/0?wx_fmt=png)

百灵鸟安全团队

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/mmbXTwYCQ9mPH65CMJ4RhCx8MWdmyFLYHtyibVkeA5DPU9dVRGgZo9XSdT7NfrKl4bEiaNZibwxTSvqHPPRI8YAtQ/0?wx_fmt=png)

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
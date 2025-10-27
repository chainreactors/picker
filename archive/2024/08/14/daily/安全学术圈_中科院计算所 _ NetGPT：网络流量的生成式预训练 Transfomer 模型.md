---
title: 中科院计算所 | NetGPT：网络流量的生成式预训练 Transfomer 模型
url: https://mp.weixin.qq.com/s?__biz=MzU5MTM5MTQ2MA==&mid=2247491113&idx=1&sn=5528e90d02ed888c28cf8c1c9e259854&chksm=fe2ee1a2c95968b48cc1b6dcb1cf062883cd52575313ef1cd87aab01cd8574bef133c0c92527&scene=58&subscene=0#rd
source: 安全学术圈
date: 2024-08-14
fetch_date: 2025-10-06T18:03:29.865245
---

# 中科院计算所 | NetGPT：网络流量的生成式预训练 Transfomer 模型

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6Dibw6L070WEb3JQ2J7hg1icGib4f9VCfaOr3RO3sMXOT158yHgenAZafDH71DcUxAwL281qNCEfpKyIxlictgdKug/0?wx_fmt=jpeg)

# 中科院计算所 | NetGPT：网络流量的生成式预训练 Transfomer 模型

原创

JSY

安全学术圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WEb3JQ2J7hg1icGib4f9VCfaO78WaF29ibNYLoITkWf5cH6QiaYzTV51mtiaSqtmrS6fLhFAl6McMrLLZA/640?wx_fmt=png&from=appmsg)

> *论文题目：NetGPT: Generative Pretrained Transformer for Network Traffic*
> *论文作者：Xuying Meng, Chungang Lin, Yequan Wang, Yujun Zhang*
> *发表会议/期刊：arXiv*
> *发布时间：2023*
> *主题类型：流量分析*
> *笔记作者：JSY@Web 攻击检测与追踪课程*
> *作者主页：孟绪颖* *http://www.ict.ac.cn/sourcedb/cn/jssrck/202012/t20201204\_5808220.html*

### 研究概述

NetGPT 是一种生成式预训练 Transformer 模型，旨在解决现有的传统网络流量模型仅为解决特定任务设计、难以在小样本数据集上充分训练、开发成本高昂的问题。NetGPT 通过预训练策略，利用大规模的网络流量数据学习其内在特征，使其能够轻松适应各种下游任务，如应用分类、攻击检测和流量生成。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WEb3JQ2J7hg1icGib4f9VCfaOhjBjhexLJaYG3a300NpabKF4YFibpx2Kib4BibNxnAgh8PucxNrj2xmew/640?wx_fmt=png&from=appmsg)

在技术实现上，NetGPT 引入了多模式网络流量建模，通过将异构的网络流量头部和载荷编码为统一的文本输入，支持流量理解和生成任务。在预训练过程中，NetGPT 使用基于十六进制的通用编码策略，将明文和加密流量转化为通用语义空间，从而构建了一个基础的预训练模型。在微调过程中，通过随机化头部字段、分割流中的数据包，并结合任务特定标签来优化模型，以适应不同的下游任务。

实验结果表明，NetGPT 在多种不同的流量数据集上的流量感知和流量生成任务均表现出色，显著优于当前最先进的基线模型。![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WEb3JQ2J7hg1icGib4f9VCfaOibic4lCwSMSJltUxgL31ISeDz7bbIP7TvJkFnPtBica7QV1TlJAibQjjHw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WEb3JQ2J7hg1icGib4f9VCfaOc666ny4CHkhhFFKvbyazJsRl6JbHpF9icNxjS1gCVQzOnVGjvBqwwDg/640?wx_fmt=png&from=appmsg)

作者进一步做了消融实验，检测移除随机化头部字段和数据包分割模块的影响，进一步证明所提出方法的有效性。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WEb3JQ2J7hg1icGib4f9VCfaOnVlT0FmF9iboDnwFUBJKibawrnEhmf1G7PnDZzGwxMUqk7yGibCCHZlLQ/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WEb3JQ2J7hg1icGib4f9VCfaOmILPgjQ0VShIUVyibj2JLI6cWMMMcaXC9pC47GXPbltb0oD7t4FAjgg/640?wx_fmt=png&from=appmsg)

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
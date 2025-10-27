---
title: 弗吉尼亚大学 | FLASH：基于可信度图的证明式学习的综合入侵检测方法
url: https://mp.weixin.qq.com/s?__biz=MzU5MTM5MTQ2MA==&mid=2247491370&idx=1&sn=590eb1c36f12ff8969527fa12d9ec1d4&chksm=fe2ee0a1c95969b70ffee2a7c212b72e1bc248ae48849f9b08ac149240072b0ba7f1d4117ef9&scene=58&subscene=0#rd
source: 安全学术圈
date: 2024-11-15
fetch_date: 2025-10-06T19:19:37.621393
---

# 弗吉尼亚大学 | FLASH：基于可信度图的证明式学习的综合入侵检测方法

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6Dibw6L070WHzibUUlatA9INRoibjc3IwLkkmiczYgKYycvchibITTHEV4qlgSCmL89FjWS0C3y65PH5hb0tbujRKEQ/0?wx_fmt=jpeg)

# 弗吉尼亚大学 | FLASH：基于可信度图的证明式学习的综合入侵检测方法

原创

杨运涛

安全学术圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WHzibUUlatA9INRoibjc3IwLk31picDvictCBy5bzGhV24TLYLIibZ1zGFjS0ic3SiaRkLruIQrc2ZwsHugg/640?wx_fmt=png&from=appmsg)
> *原文标题：FLASH: A Comprehensive Approach to Intrusion Detection via Provenance Graph Representation Learning*
> *原文作者：Mati Ur Rehman，Hadi Ahmadi，Wajih Ul Hassan*
> *第一作者/通信作者主页：https://mati607.github.io/*
> *发表期刊：2024 IEEE Symposium on Security and Privacy*
> *主题类型：攻击检测*
> *笔记作者：杨运涛@Web攻击检测与追踪*
> *主编：黄诚@安全学术圈*

# 研究概述

高级持续续性威胁（APT）攻击以其长期性、隐匿性、多阶段、使用零日漏洞的特点而著名，因而难以检测。近年来，基于溯源图（即将系统日志转化为图，日志中的实体如进程、文件、套接字变为节点，实体之间的操作如写、执行、创建变为边）的入侵检测系统（IDS）因利用了日志中丰富的上下文信息在检测APT攻击上展现了卓越的潜力而广受关注。但目前的IDS存在有粗粒度、忽略了实体的语义信息和事件的时间信息、嵌入处理速度慢等缺陷。在此背景下，本文设计了一个名为FLASH的检测系统，该系统在节点级对APT攻击进行检测溯源。所设计的系统不仅具有高效的处理速度同时还具有可扩展性，可用于不同的环境中。

图1是本文的系统架构图，包含溯源图构造器、基于Word2Vec的语义编码器、基于GNN的上下文编码器、嵌入数据库和异常检测器五个模块。核心思想是利用节点的语义和上下文信息来训练分类模型，使得模型输出包含异常节点的攻击路径图，实现对APT攻击的检测和溯源。训练时,首先溯源图构造器将良性的日志信息转化为图，其次基于Word2Vec的语义编码器将节点的语义属性和时间信息转为节点的特征向量，然后基于GNN的上下文编码器把上一步的Word2Vec向量和节点的邻域信息结合起来生成最终嵌入，最后异常检测器根据节点的异常分数阈值来对节点进行分类，当其能够将所有良性节点正确分类为良性时，模型训练完成。这些良性节点的最终嵌入会存放到嵌入数据库中，以便于在检测时，直接将匹配的节点嵌入直接输出，避免生成嵌入这一步骤带来的时间消耗，提高了检测速度。当检测到攻击时，异常检测器会输出一个包含异常节点及其相关攻击的攻击路径图，便于分析师进行溯源。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WHzibUUlatA9INRoibjc3IwLkA4TMp9c4gY0b3d1WCc7pcB7J6DlaDbdSKtOQhOWmMa3ZFK6boB84zQ/640?wx_fmt=png&from=appmsg)

图1 FLASH架构

# 贡献分析

1. 贡献点1：论文针对忽略节点的语义信息和事件的时间信息问题，提出了基于Word2vec和GNN的嵌入方法，实现了为节点生成语义丰富的特征向量这一功能。
2. 贡献点2：论文针对实时性检测速度慢的问题，提出了基于GNN嵌入数据库和选择性图遍历的方法，实现了高效的检测功能。
3. 贡献点3：论文针对粗粒度难溯源问题，提出了基于异常分数的XGBoost分类器和攻击进化图的方法，实现了在节点级进行攻击检测溯源的功能。

# 代码分析

代码链接：*https://github.com/DART-Laboratory/Flash-IDS*

1. 代码使用的类库全为开源类库的集成；
2. 代码实现总体难度适中，只是在使用word2vec生成嵌入向量的时候，word2vec模型本身存在没有保留句子中单词的顺序这一限制，而论文需要考虑到事件的时间信息。因此在对word2vec模型进行修改将位置编码引入到输入嵌入以考虑事件的时间信息时，难度有所增加。论文的工作量尚可，分别对DARPA E3数据集（包括Cadets、Trace、Theia、Fivedirections）、DARPA OpTC、StreamSpot、Unicorn，进行了实验，详细地完成了日志转化、节点嵌入、攻击检测和溯源整个检测流程；
3. 代码关键实现的功能有：1、将日志信息转化为溯源图。2、解析并存储节点的相关属性，利用word2vec综合节点的语义信息、节点的属性以及事件的时间信息生成嵌入向量。3、利用GNN结合选择性图遍历方法根据word2vec生成的嵌入向量，生成节点的最终向量。4、利用属性抽象技术生成嵌入数据库中用于检索和存储的键。5、基于XGBoost的分类器。6、生成包含异常节点及其相关攻击的攻击路径图。

# 论文点评

1. 在溯源图构建方面，本文将日志直接转化为溯源图，这种方法虽然直观，但会导致转换后的溯源图规模庞大，并且包含许多无用的节点和边，影响后续嵌入生成工作的效率。改进的方向可以从溯源图预处理入手，例如删除孤立节点和重复边，或者将整个图分为子图处理，以减少溯源图的大小，从而缩短嵌入生成时间，提高检测效率。
2. 在报警溯源方面，本文只是简单地将检测到的异常节点及其相关的边进行保存，并根据这些路径和节点重建攻击图。然而，由于单个节点在一个长期的过程中可能连接大量的边，最终导致重建的攻击图仍然是一个很大的图，不利于分析师进行有效分析。改进的方向可以从减少这些路径的思路着手，例如对路径进行异常分数排名，选取异常分数较高的若干条路径，从而缩小攻击图的规模，提高分析的可行性和效率。
3. 在内存存储方面，本文通过多批次将日志信息加载并转换为溯源图以生成嵌入，但在处理大型网络环境时，即便是小批次的日志信息也会生成非常大的溯源图。将整个图加载到内存中处理以生成嵌入，会增加内存的消耗，导致处理时间变长。改进的方向可以通过内外存相结合的方法，避免将整个图全部加载到内存中处理，从而优化内存使用，提升处理效率。
4. 在GNN嵌入方面，本文仅仅尝试了基于GraphSAGE的图卷积技术来聚合节点的上下文信息，但是GraphSAGE只能处理同构图。未来的改进方向可以通过改进GraphSAGE或者利用其他图卷积技术来处理异构图，以增强系统的泛化能力，适应更多样化的图结构，提升检测的广泛适用性和准确性。

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
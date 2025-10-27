---
title: 普林斯顿大学 | 评估Snowflake作为一种难以区分的审查规避工具
url: https://mp.weixin.qq.com/s?__biz=MzU5MTM5MTQ2MA==&mid=2247491442&idx=1&sn=0f0f4fff86e4481cc823632b6796bc79&chksm=fe2ee0f9c95969ef836aabac8f766b81ba2a1f69cd273da52e1afd509876dfb6332edb39584f&scene=58&subscene=0#rd
source: 安全学术圈
date: 2024-12-11
fetch_date: 2025-10-06T19:41:29.011096
---

# 普林斯顿大学 | 评估Snowflake作为一种难以区分的审查规避工具

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6Dibw6L070WFUnM6wOoia32gJJGia160ib2mUHAibcZNEHNkPjJYZibnicwL55WSWLicHUvTtdCTPquVAfI7KaSN2nhz1g/0?wx_fmt=jpeg)

# 普林斯顿大学 | 评估Snowflake作为一种难以区分的审查规避工具

原创

宋坤书

安全学术圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WFUnM6wOoia32gJJGia160ib2mq1ialJba8FCGqbsXqgrytVrxEU62pMJDQ3WuP3JPamrAI1pLuZRiahCA/640?wx_fmt=png&from=appmsg)
> *原文标题：Evaluating Snowflake as an Indistinguishable Censorship Circumvention Tool*
> *原文作者：Kyle MacMillan, Jordan Holland, Prateek Mittal*
> *原文链接：https://arxiv.org/abs/2008.03254*
> *笔记作者：宋坤书@安全学术圈*
> *主编：黄诚@安全学术圈*

### 1、背景介绍

Snowflake是一种新型的可插拔传输工具（PT），旨在帮助用户规避互联网审查。它由客户端（Client）、中介（Broker）和代理（Proxy）三部分组成。客户端位于受审查地区，通过中介与代理建立连接，代理提供非审查的互联网访问。建立连接后，双方使用WebRTC协议进行点对点通信，从而访问Tor中继。

WebRTC是一种支持浏览器之间点对点通信的框架，其握手过程采用DTLS协议。Snowflake的有效性依赖于WebRTC的广泛应用和流量的不可区分性。WebRTC被广泛用于许多服务（如Facebook Messenger和Google Hangouts），因此全面封锁WebRTC流量可能带来严重后果，但审查方仍可能通过分析WebRTC握手特征来识别Snowflake流量。总体而言，Snowflake利用WebRTC的普遍性和伪装性规避审查，但其协议特性也可能成为审查方识别的依据。

### 2、Snowflake的可识别性分析

#### 2.1 建立威胁模型

假设攻击者能够访问客户端的WebRTC数据包，包括其头部、协议和有效载荷，同时假设审查方能够观察互联网接入点的流量，但存在一定的带宽和计算限制。考虑到Snowflake采用临时代理和域名伪装技术，IP地址检测的难度较大，因此Snowflake能够有效避免通过IP地址进行流量检测。

#### 2.2 数据收集

本文通过捕获孤立的DTLS握手数据进行分析，收集的数据已经公开发布在 *https://github.com/kyle-macmillan/snowflake\_fingerprintability* 上。下图总结了收集到的握手数量：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WFUnM6wOoia32gJJGia160ib2m5fCe6O6luHvibbNGWYRxqDibibfLmzCbU2x1NurqcRCGibOnortTBc1xsg/640?wx_fmt=png&from=appmsg)

#### 2.3 不同服务平均握手次数

分析结果显示，Snowflake握手的平均数据包在数量上显著高于其他服务。具体而言，Snowflake握手通常需要进行多次重传，因此平均数据包数较多。而其他服务的握手过程中，重传现象较少，因此平均数据包数较少。不同服务每次握手的平均数据包数如下图所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WFUnM6wOoia32gJJGia160ib2m3yXzEYibxnZ6LHegHsLFKgwXPLAQjk34SFKV5DVOITQ0EHQrUCMCnEg/640?wx_fmt=png&from=appmsg)

### 3、基于机器学习的Snowflake特征分类

#### 3.1 分类方法

本文提取了20个特征用于进行分类，对于非数值数据，采用独热编码（one-hot encoding）将其转换为二进制特征。选择随机森林分类器来训练模型，因为它可以帮助分析哪些特征对模型性能有重要影响。文中使用准确性（accuracy）和微加权F1分数作为评估指标，所有评估指标都使用了5折交叉验证。从WebRTC握手中提取的特征如下图所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WFUnM6wOoia32gJJGia160ib2mpumAhz4NZ1GNflnKWsqFlKmRGP4yzknXQzT5YKAb4ClSU9UAPmNQ8g/640?wx_fmt=png&from=appmsg)

#### 3.2 分类评估

通过对提取到的特征进行独热编码，最终得到61个特征。文中使用scikit-learn的随机森林分类器模块进行训练。结果表明，分类器在所有类别上的平均准确率达到99.8%，并且能够完美识别Snowflake，准确率和微加权F1分数均表现出色。基于这些结果，本文进一步分析了识别特征，即那些在每个类别中唯一的特征。

#### 3.3 特征重要性分析

利用模型的特征重要性，文中识别出了一些Snowflake独有的特征。其中“supported\_groups”和“renegotiation\_info”是Server Hello中提供的拓展。“Server Message Sequence”中的“1”表示Snowflake的DTLS协议包含了其他服务所忽略的可选Client Hello和Hello Verify Request数据包。不同服务握手中包含重要特征的比例如下图：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WFUnM6wOoia32gJJGia160ib2m9v52tj6e1GU7nclXpGB9H39POhPzyLoeNuHqZZNYWf1BMoTsH1XYPQ/640?wx_fmt=png&from=appmsg)

### 4、本文贡献

本文主要贡献如下：

* Snowflake可识别性的实证研究与分析：本文通过收集和分析超过6,500个DTLS握手数据，实证地展示了Snowflake流量可以被100%准确识别，这与Snowflake设计的初衷（不可区分于其他WebRTC服务）相违背。
* 关键特征的识别与分析：本文识别出两个关键特征：Server Message Sequence: 1和supported\_groups，它们在Snowflake流量中出现的比例为100%；而renegotiation\_info特征在Snowflake中从未出现。这些特征使得Snowflake流量与其他WebRTC服务区分开来，为识别其流量提供了依据。
* 改进Snowflake识别抗性的建议：基于上述发现，文章提出了一系列的改进建议，旨在提高Snowflake的不可区分性，使其更难被审查者检测和封锁。短期建议包括修改DTLS握手过程中的某些行为，如不发送可选的Client Hello和Hello Verify Request，提供renegotiation\_info作为服务器Hello中的扩展，以及不提供supported\_groups作为服务器Hello中的扩展。长期建议则是让Snowflake采用现有的WebRTC服务实现。这些建议对于Snowflake的开发和维护具有实际指导意义，有助于增强其作为审查规避工具的有效性。

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
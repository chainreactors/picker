---
title: Twitter算法源代码
url: https://blog.upx8.com/3552
source: 黑海洋 - WIKI
date: 2023-05-14
fetch_date: 2025-10-04T11:39:03.567193
---

# Twitter算法源代码

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# Twitter算法源代码

发布时间:
2023-05-13

分类:
[Web开发/Code](https://blog.upx8.com/code/)

热度:
18106

# ![](https://pic9.58cdn.com.cn/nowater/webim/big/n_v23132dfbf86d2467591b1c3d5cde93d1b.png)![](https://pic5.58cdn.com.cn/nowater/webim/big/n_v2c1f1b387c67a41fa8a5ed83f470e9cc5.png)

# 推特的推荐算法

Twitter 的推荐算法是一组服务和作业，负责在所有 Twitter 产品表面（例如，为您时间线、搜索、探索）提供推文和其他内容的提要。有关算法工作原理的介绍，请参阅我们的[工程博客](https://blog.upx8.com/go/aHR0cHM6Ly9ibG9nLnR3aXR0ZXIuY29tL2VuZ2luZWVyaW5nL2VuX3VzL3RvcGljcy9vcGVuLXNvdXJjZS8yMDIzL3R3aXR0ZXItcmVjb21tZW5kYXRpb24tYWxnb3JpdGht)。

## 建筑学

Twitter 的产品界面建立在一组共享的数据、模型和软件框架之上。下面列出了此存储库中包含的共享组件：

| 类型 | 成分 | 描述 |
| --- | --- | --- |
| 数据 | [统一用户操作](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL3R3aXR0ZXIvdGhlLWFsZ29yaXRobS9ibG9iL21haW4vdW5pZmllZF91c2VyX2FjdGlvbnMvUkVBRE1FLm1k) | Twitter 上的实时用户操作流。 |
|  | [用户信号服务](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL3R3aXR0ZXIvdGhlLWFsZ29yaXRobS9ibG9iL21haW4vdXNlci1zaWduYWwtc2VydmljZS9SRUFETUUubWQ) | 用于检索显式（例如喜欢、回复）和隐式（例如个人资料访问、推文点击）用户信号的集中式平台。 |
| 模型 | [模拟集群](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL3R3aXR0ZXIvdGhlLWFsZ29yaXRobS9ibG9iL21haW4vc3JjL3NjYWxhL2NvbS90d2l0dGVyL3NpbWNsdXN0ZXJzX3YyL1JFQURNRS5tZA) | 社区检测和稀疏嵌入这些社区。 |
|  | [双核](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL3R3aXR0ZXIvdGhlLWFsZ29yaXRobS1tbC9ibG9iL21haW4vcHJvamVjdHMvdHdoaW4vUkVBRE1FLm1k) | 用户和推文的密集知识图嵌入。 |
|  | [信任和安全模型](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL3R3aXR0ZXIvdGhlLWFsZ29yaXRobS9ibG9iL21haW4vdHJ1c3RfYW5kX3NhZmV0eV9tb2RlbHMvUkVBRE1FLm1k) | 用于检测 NSFW 或滥用内容的模型。 |
|  | [实图](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL3R3aXR0ZXIvdGhlLWFsZ29yaXRobS9ibG9iL21haW4vc3JjL3NjYWxhL2NvbS90d2l0dGVyL2ludGVyYWN0aW9uX2dyYXBoL1JFQURNRS5tZA) | 预测 Twitter 用户与另一个用户交互的可能性的模型。 |
|  | [推特](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL3R3aXR0ZXIvdGhlLWFsZ29yaXRobS9ibG9iL21haW4vc3JjL3NjYWxhL2NvbS90d2l0dGVyL2dyYXBoL2JhdGNoL2pvYi90d2VlcGNyZWQvUkVBRE1F) | 用于计算 Twitter 用户信誉的 Page-Rank 算法。 |
|  | [recos-注射器](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL3R3aXR0ZXIvdGhlLWFsZ29yaXRobS9ibG9iL21haW4vcmVjb3MtaW5qZWN0b3IvUkVBRE1FLm1k) | [流式事件处理器，用于为基于GraphJet](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL3R3aXR0ZXIvR3JhcGhKZXQ)的服务构建输入流。 |
|  | [图特征服务](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL3R3aXR0ZXIvdGhlLWFsZ29yaXRobS9ibG9iL21haW4vZ3JhcGgtZmVhdHVyZS1zZXJ2aWNlL1JFQURNRS5tZA) | 为一对定向用户提供图形特征（例如，有多少用户 A 的关注点赞了用户 B 的推文）。 |
|  | [主题社会证明](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL3R3aXR0ZXIvdGhlLWFsZ29yaXRobS9ibG9iL21haW4vdG9waWMtc29jaWFsLXByb29mL1JFQURNRS5tZA) | 标识与各个推文相关的主题。 |
|  | [代表记分员](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL3R3aXR0ZXIvdGhlLWFsZ29yaXRobS9ibG9iL21haW4vcmVwcmVzZW50YXRpb24tc2NvcmVyL1JFQURNRS5tZA) | 使用嵌入相似性计算实体对（用户、推文等）之间的分数。 |
| 软件架构 | [导航](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL3R3aXR0ZXIvdGhlLWFsZ29yaXRobS9ibG9iL21haW4vbmF2aS9SRUFETUUubWQ) | 用 Rust 编写的高性能机器学习模型服务。 |
|  | [产品混合器](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL3R3aXR0ZXIvdGhlLWFsZ29yaXRobS9ibG9iL21haW4vcHJvZHVjdC1taXhlci9SRUFETUUubWQ) | 用于构建内容提要的软件框架。 |
|  | [时间线聚合框架](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL3R3aXR0ZXIvdGhlLWFsZ29yaXRobS9ibG9iL21haW4vdGltZWxpbmVzL2RhdGFfcHJvY2Vzc2luZy9tbF91dGlsL2FnZ3JlZ2F0aW9uX2ZyYW1ld29yay9SRUFETUUubWQ) | 用于批量或实时生成聚合特征的框架。 |
|  | [代表经理](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL3R3aXR0ZXIvdGhlLWFsZ29yaXRobS9ibG9iL21haW4vcmVwcmVzZW50YXRpb24tbWFuYWdlci9SRUFETUUubWQ) | 检索嵌入的服务（即 SimClusers 和 TwHIN）。 |
|  | [twml](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL3R3aXR0ZXIvdGhlLWFsZ29yaXRobS9ibG9iL21haW4vdHdtbC9SRUFETUUubWQ) | 基于 TensorFlow v1 构建的旧版机器学习框架。 |

此存储库中当前包含的产品表面是为您时间线。

### 为你时间线

下图说明了主要服务和工作如何相互关联以构建“为您服务”时间表。

![](https://pic8.58cdn.com.cn/nowater/webim/big/n_v2bda78ac00fae4ff6bd2d0d54b1bac526.png)

下面列出了此存储库中包含的 For You Timeline 的核心组件：

| 类型 | 成分 | 描述 |
| --- | --- | --- |
| 候选来源 | [搜索索引](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL3R3aXR0ZXIvdGhlLWFsZ29yaXRobS9ibG9iL21haW4vc3JjL2phdmEvY29tL3R3aXR0ZXIvc2VhcmNoL1JFQURNRS5tZA) | 查找网络内推文并对其进行排名。约 50% 的推文来自此候选来源。 |
|  | [混音器](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL3R3aXR0ZXIvdGhlLWFsZ29yaXRobS9ibG9iL21haW4vY3ItbWl4ZXIvUkVBRE1FLm1k) | 用于从底层计算服务中获取网络外推文候选者的协调层。 |
|  | [用户推文实体图](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL3R3aXR0ZXIvdGhlLWFsZ29yaXRobS9ibG9iL21haW4vc3JjL3NjYWxhL2NvbS90d2l0dGVyL3JlY29zL3VzZXJfdHdlZXRfZW50aXR5X2dyYXBoL1JFQURNRS5tZA)(UTEG) | 在内存中维护一个用户到推文的交互图，并根据该图的遍历找到候选者。这是建立在[GraphJet](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL3R3aXR0ZXIvR3JhcGhKZXQ)框架之上的。其他几个基于 GraphJet 的功能和候选源位于[此处](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL3R3aXR0ZXIvdGhlLWFsZ29yaXRobS9ibG9iL21haW4vc3JjL3NjYWxhL2NvbS90d2l0dGVyL3JlY29z)。 |
|  | [遵循推荐服务](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL3R3aXR0ZXIvdGhlLWFsZ29yaXRobS9ibG9iL21haW4vZm9sbG93LXJlY29tbWVuZGF0aW9ucy1zZXJ2aWNlL1JFQURNRS5tZA)(FRS) | 为用户提供要关注的帐户的建议，以及来自这些帐户的推文。 |
| 排行 | [光级](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL3R3aXR0ZXIvdGhlLWFsZ29yaXRobS9ibG9iL21haW4vc3JjL3B5dGhvbi90d2l0dGVyL2RlZXBiaXJkL3Byb2plY3RzL3RpbWVsaW5lcy9zY3JpcHRzL21vZGVscy9lYXJseWJpcmQvUkVBRE1FLm1k) | 搜索索引 (Earlybird) 使用的 Light Ranker 模型对推文进行排名。 |
|  | [重级](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL3R3aXR0ZXIvdGhlLWFsZ29yaXRobS1tbC9ibG9iL21haW4vcHJvamVjdHMvaG9tZS9yZWNhcC9SRUFETUUubWQ) | 用于对候选推文进行排名的神经网络。用于选择时间轴推文的主要信号之一。 |
| 推文混合和过滤 | [家用调音台](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL3R3aXR0ZXIvdGhlLWFsZ29yaXRobS9ibG9iL21haW4vaG9tZS1taXhlci9SRUFETUUubWQ) | 用于构建和服务主页时间线的主要服务。建立在[产品混合器](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL3R3aXR0ZXIvdGhlLWFsZ29yaXRobS9ibG9iL21haW4vcHJvZHVjdC1taXhlci9SRUFETUUubWQ)上。 |
|  | [可见性过滤器](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL3R3aXR0ZXIvdGhlLWFsZ29yaXRobS9ibG9iL21haW4vdmlzaWJpbGl0eWxpYi9SRUFETUUubWQ) | 负责过滤 Twitter 内容以支持法律合规性、提高产品质量、增加用户信任度、通过使用硬过滤、可见产品处理和粗粒度降级来保护收入。 |
|  | [时间线排序器](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL3R3aXR0ZXIvdGhlLWFsZ29yaXRobS9ibG9iL21haW4vdGltZWxpbmVyYW5rZXIvUkVBRE1FLm1k) | 旧版服务，它提供来自 Earlybird 搜索索引和 UTEG 服务的相关性评分推文。 |

## 构建和测试代码

我们包括大多数组件的 Bazel BUILD 文件，但不包括顶级 BUILD 或 WORKSPACE 文件。我们计划在未来添加更完整的构建和测试系统。

马斯克履行诺言， Twitter 推荐算法开源了，该开源项目涵盖了推荐算法在内的许多推特源代码，包括用来控制用户在 For You 时间线上看到的推文的机制。

推特的推荐算法是一组服务和作业，负责构建和服务主页时间线。

开源项目： [https://github.com/twitter/the-algorithm](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL3R3aXR0ZXIvdGhlLWFsZ29yaXRobQ)

官方博客：[https://blog.twitter.com/engineering/en\_us/topics/open-source/2023/twitter-recommendation-algorithm](https://blog.upx8.com/go/aHR0cHM6Ly9ibG9nLnR3aXR0ZXIuY29tL2VuZ2luZWVyaW5nL2VuX3VzL3RvcGljcy9vcGVuLXNvdXJjZS8yMDIzL3R3aXR0ZXItcmVjb21tZW5kYXRpb24tYWxnb3JpdGht)

[取消回复](https://blog.upx8.com/3552#respond-post-3552)

### 在下方留下您的评论.[加入TG群](https://t.me/).[打赏🍗](/reward.html)

提交评论

* [Post](/author/1)
* [Link](/links.html)
* [工具](https://tools.upx8.com/)
* [关于](/about.html)
* [文库](/WooyunDrops)

[![](/usr/uploads/ypyun.png)](https://www.upyun.com/?utm_source=lianmeng&utm_medium=referral "赞助商")
Copyright © 2024 黑海洋. All rights reserved.
[看雪赞助](https://www.kanxue.com/ "看雪学院赞助")

[浙ICP备2021040518号](http://beian.miit.gov.cn "浙ICP备2021040518号") [Sitemap](sitemap.xml?type=index "Sitemap")
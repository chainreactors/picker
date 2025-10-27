---
title: Twitter算法源代码
url: https://buaq.net/go-163193.html
source: unSafe.sh - 不安全
date: 2023-05-14
fetch_date: 2025-10-04T11:37:49.474198
---

# Twitter算法源代码

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/dd0eb154039cc33963d860355d3c80f4.jpg)

Twitter算法源代码

Twitter 的推荐算法是一组服务和作业，负责在所有 Twitter 产品表面（例如，为您时间线、搜索、探索）提供推文和其他内容的提要。有关算法工作原
*2023-5-13 15:50:0
Author: [blog.upx8.com(查看原文)](/jump-163193.htm)
阅读量:34
收藏*

---

Twitter 的推荐算法是一组服务和作业，负责在所有 Twitter 产品表面（例如，为您时间线、搜索、探索）提供推文和其他内容的提要。有关算法工作原理的介绍，请参阅我们的[工程博客](https://blog.twitter.com/engineering/en_us/topics/open-source/2023/twitter-recommendation-algorithm)。

## 建筑学

Twitter 的产品界面建立在一组共享的数据、模型和软件框架之上。下面列出了此存储库中包含的共享组件：

| 类型 | 成分 | 描述 |
| --- | --- | --- |
| 数据 | [统一用户操作](https://github.com/twitter/the-algorithm/blob/main/unified_user_actions/README.md) | Twitter 上的实时用户操作流。 |
|  | [用户信号服务](https://github.com/twitter/the-algorithm/blob/main/user-signal-service/README.md) | 用于检索显式（例如喜欢、回复）和隐式（例如个人资料访问、推文点击）用户信号的集中式平台。 |
| 模型 | [模拟集群](https://github.com/twitter/the-algorithm/blob/main/src/scala/com/twitter/simclusters_v2/README.md) | 社区检测和稀疏嵌入这些社区。 |
|  | [双核](https://github.com/twitter/the-algorithm-ml/blob/main/projects/twhin/README.md) | 用户和推文的密集知识图嵌入。 |
|  | [信任和安全模型](https://github.com/twitter/the-algorithm/blob/main/trust_and_safety_models/README.md) | 用于检测 NSFW 或滥用内容的模型。 |
|  | [实图](https://github.com/twitter/the-algorithm/blob/main/src/scala/com/twitter/interaction_graph/README.md) | 预测 Twitter 用户与另一个用户交互的可能性的模型。 |
|  | [推特](https://github.com/twitter/the-algorithm/blob/main/src/scala/com/twitter/graph/batch/job/tweepcred/README) | 用于计算 Twitter 用户信誉的 Page-Rank 算法。 |
|  | [recos-注射器](https://github.com/twitter/the-algorithm/blob/main/recos-injector/README.md) | [流式事件处理器，用于为基于GraphJet](https://github.com/twitter/GraphJet)的服务构建输入流。 |
|  | [图特征服务](https://github.com/twitter/the-algorithm/blob/main/graph-feature-service/README.md) | 为一对定向用户提供图形特征（例如，有多少用户 A 的关注点赞了用户 B 的推文）。 |
|  | [主题社会证明](https://github.com/twitter/the-algorithm/blob/main/topic-social-proof/README.md) | 标识与各个推文相关的主题。 |
|  | [代表记分员](https://github.com/twitter/the-algorithm/blob/main/representation-scorer/README.md) | 使用嵌入相似性计算实体对（用户、推文等）之间的分数。 |
| 软件架构 | [导航](https://github.com/twitter/the-algorithm/blob/main/navi/README.md) | 用 Rust 编写的高性能机器学习模型服务。 |
|  | [产品混合器](https://github.com/twitter/the-algorithm/blob/main/product-mixer/README.md) | 用于构建内容提要的软件框架。 |
|  | [时间线聚合框架](https://github.com/twitter/the-algorithm/blob/main/timelines/data_processing/ml_util/aggregation_framework/README.md) | 用于批量或实时生成聚合特征的框架。 |
|  | [代表经理](https://github.com/twitter/the-algorithm/blob/main/representation-manager/README.md) | 检索嵌入的服务（即 SimClusers 和 TwHIN）。 |
|  | [twml](https://github.com/twitter/the-algorithm/blob/main/twml/README.md) | 基于 TensorFlow v1 构建的旧版机器学习框架。 |

此存储库中当前包含的产品表面是为您时间线。

### 为你时间线

下图说明了主要服务和工作如何相互关联以构建“为您服务”时间表。

![](https://pic8.58cdn.com.cn/nowater/webim/big/n_v2bda78ac00fae4ff6bd2d0d54b1bac526.png)

下面列出了此存储库中包含的 For You Timeline 的核心组件：

| 类型 | 成分 | 描述 |
| --- | --- | --- |
| 候选来源 | [搜索索引](https://github.com/twitter/the-algorithm/blob/main/src/java/com/twitter/search/README.md) | 查找网络内推文并对其进行排名。约 50% 的推文来自此候选来源。 |
|  | [混音器](https://github.com/twitter/the-algorithm/blob/main/cr-mixer/README.md) | 用于从底层计算服务中获取网络外推文候选者的协调层。 |
|  | [用户推文实体图](https://github.com/twitter/the-algorithm/blob/main/src/scala/com/twitter/recos/user_tweet_entity_graph/README.md)(UTEG) | 在内存中维护一个用户到推文的交互图，并根据该图的遍历找到候选者。这是建立在[GraphJet](https://github.com/twitter/GraphJet)框架之上的。其他几个基于 GraphJet 的功能和候选源位于[此处](https://github.com/twitter/the-algorithm/blob/main/src/scala/com/twitter/recos)。 |
|  | [遵循推荐服务](https://github.com/twitter/the-algorithm/blob/main/follow-recommendations-service/README.md)(FRS) | 为用户提供要关注的帐户的建议，以及来自这些帐户的推文。 |
| 排行 | [光级](https://github.com/twitter/the-algorithm/blob/main/src/python/twitter/deepbird/projects/timelines/scripts/models/earlybird/README.md) | 搜索索引 (Earlybird) 使用的 Light Ranker 模型对推文进行排名。 |
|  | [重级](https://github.com/twitter/the-algorithm-ml/blob/main/projects/home/recap/README.md) | 用于对候选推文进行排名的神经网络。用于选择时间轴推文的主要信号之一。 |
| 推文混合和过滤 | [家用调音台](https://github.com/twitter/the-algorithm/blob/main/home-mixer/README.md) | 用于构建和服务主页时间线的主要服务。建立在[产品混合器](https://github.com/twitter/the-algorithm/blob/main/product-mixer/README.md)上。 |
|  | [可见性过滤器](https://github.com/twitter/the-algorithm/blob/main/visibilitylib/README.md) | 负责过滤 Twitter 内容以支持法律合规性、提高产品质量、增加用户信任度、通过使用硬过滤、可见产品处理和粗粒度降级来保护收入。 |
|  | [时间线排序器](https://github.com/twitter/the-algorithm/blob/main/timelineranker/README.md) | 旧版服务，它提供来自 Earlybird 搜索索引和 UTEG 服务的相关性评分推文。 |

## 构建和测试代码

我们包括大多数组件的 Bazel BUILD 文件，但不包括顶级 BUILD 或 WORKSPACE 文件。我们计划在未来添加更完整的构建和测试系统。

马斯克履行诺言， Twitter 推荐算法开源了，该开源项目涵盖了推荐算法在内的许多推特源代码，包括用来控制用户在 For You 时间线上看到的推文的机制。

推特的推荐算法是一组服务和作业，负责构建和服务主页时间线。

开源项目： <https://github.com/twitter/the-algorithm>

官方博客：<https://blog.twitter.com/engineering/en_us/topics/open-source/2023/twitter-recommendation-algorithm>

文章来源: https://blog.upx8.com/3552
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)
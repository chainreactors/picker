---
title: 【算法】用C++实现A*算法
url: https://blog.csdn.net/nokiaguy/article/details/145584125
source: 一个被知识诅咒的人
date: 2025-02-13
fetch_date: 2025-10-06T20:34:05.204107
---

# 【算法】用C++实现A*算法

# 【算法】用C++实现A\*算法

![](https://csdnimg.cn/release/blogv2/dist/pc/img/original.png)

[![](https://csdnimg.cn/release/blogv2/dist/pc/img/identityVipNew.png)](https://mall.csdn.net/vip)
[蒙娜丽宁](https://unitymarvel.blog.csdn.net "蒙娜丽宁")
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCurrentTime2.png)
于 2025-02-12 08:58:36 发布

![](https://csdnimg.cn/release/blogv2/dist/pc/img/articleReadEyes2.png)
阅读量1.7k
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)
收藏

8

![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)
点赞数
12

CC 4.0 BY-SA版权

分类专栏：
[算法](https://blog.csdn.net/nokiaguy/category_508758.html)
文章标签：
[算法](https://so.csdn.net/so/search/s.do?q=%E7%AE%97%E6%B3%95&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[c++](https://so.csdn.net/so/search/s.do?q=c%2B%2B&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[java](https://so.csdn.net/so/search/s.do?q=java&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

本文链接：<https://blog.csdn.net/nokiaguy/article/details/145584125>

#### A\*算法的背景与原理

A\*（A-Star）算法是一种广泛应用于路径规划和图搜索问题中的启发式搜索算法。它结合了Dijkstra算法的广度优先搜索和贪心最佳优先搜索的优点，通过引入启发式函数来估计从当前节点到目标节点的成本，从而有效地减少搜索空间。A\*算法的核心思想是使用一个评估函数 `f(n) = g(n) + h(n)` 来选择下一个要扩展的节点。其中，`g(n)` 表示从起点到当前节点的实际代价，`h(n)` 是从当前节点到目标节点的估计代价（启发式函数），而 `f(n)` 则是总代价，表示从起点经过当前节点到达目标节点的估计总代价。

在路径寻找和图搜索中，A*算法的优势在于其能够在保证找到最优解的同时，显著减少不必要的搜索。这一特性使得A*算法在许多实际应用中表现出色，尤其是在需要高效计算最短路径的场景中，如游戏开发中的NPC寻路、地图导航系统中的路径规划以及机器人路径规划等。

##### 启发式函数的选择

启发式函数 `h(n)` 的选择对A\*算法的性能至关重要。一个好的启发式函数应当满足以下两个条件：

1. **可接受性**：启发式函数必须是可接受的，即对于任意节点 `n`，`h(n)` 不应高估从该节点到目标节点的实际代价。换句话说，`h(n)` 应当是一个下界估计。如果启发式函数满足这一条件，A\*算法能够保证找到最优解。
2. **一致性**：启发式函数还应当是一致的（或单调的）。这意味着对于任意两个相邻节点 `n` 和 `m`，满足 `h(n) ≤ c(n, m) + h(m)`，其中 `c(n, m)` 是从节点 `n` 到节点 `m` 的实际代价。一致性确保了A\*算法在扩展节点时不会重复访问已经处理过的节点，从而提高了算法的效率。

常见的启发式函数包括曼哈顿距离和欧几里得距离。曼哈顿距离适用于只能沿网格线移动的情况，计算公式为 `h(n) = |x1 - x2| + |y1 - y2|`。欧几里得距离则适用于可以沿任意方向移动的情况，计算公式为 `h(n) = sqrt((x1 - x2)^2 + (y1 - y2)^2)`。

##### A\*算法的工作流程

A\*算法的工作流程可以分为以下几个步骤：

1. **初始化**：创建一个优先队列（通常是最小堆），用于存储待扩展的节点。初始时，将起点加入优先队列，并将其 `g(n)` 设为0，`h(n)` 设为从起点到目标的启发式估计值。
2. **节点扩展**：从优先队列中取出 `f(n)` 最小的节点进行扩展。对于每个扩展的节点，检查其是否为目标节点。如果是，则回溯路径并返回结果；如果不是，则继续扩展。
3. **邻居节点处理**：对于当前节点的每个邻居节点，计算其 `g(n)` 值（即从起点到该邻居节点的实际代价），并根据启发式函数计算其 `h(n)` 值。然后，将该邻居节点加入优先队列。
4. **关闭列表**：为了避免重复访问已经处理过的节点，A\*算法使用一个关闭列表来记录已经访问过的节点。每次扩展节点时，检查其是否已经在关闭列表中。如果是，则跳过该节点。
5. **终止条件**：如果优先队列为空且未找到目标节点，则说明没有可行路径；否则，当找到目标节点时，回溯路径并返回结果。

##### A\*算法的复杂度分析

A*算法的时间复杂度和空间复杂度都取决于启发式函数的选择。在最坏情况下，A*算法的时间复杂度为 `O(b^d)`，其中 `b` 是每个节点的分支因子，`d` 是解的深度。空间复杂度与时间复杂度相同，因为需要存储所有待扩展的节点。

然而，通过合理设计启发式函数，可以显著提高A*算法的效率。例如，使用曼哈顿距离作为启发式函数时，A*算法能够快速排除不可能的路径，从而减少搜索空间。此外，A\*算法的空间复杂度可以通过一些优化技术（如双向搜索、迭代加深等）进一步降低。

#### C++实现A\*算法的详细解析

为了更好地理解A\*算法的实现，我们将在之前的代码基础上进行更详细的解释，并探讨如何优化算法以适应不同的应用场景。

##### 数据结构设计

在C++实现中，我们使用了几个关键的数据结构来支持A\*算法的运行：

1. **Node结构体**：每个节点包含其坐标 `(x, y)`、从起点到当前节点的实际代价 `g`、从当前节点到目标节点的启发式估计代价 `h`，以及指向父节点的指针 `parent`。父节点指针用于在找到目标节点后回溯路径。

   ```
   struct Node {

       int x, y; // 节点坐标
       int g, h; // g: 从起点到当前节点的实际代价，h: 启发式估计代价
       Node* parent; // 父节点，用于回溯路径

       Node(int _x, int _y, int _g, int _h, Node* _parent)
   ```

![](https://csdnimg.cn/release/blogv2/dist/pc/img/lock.png)最低0.47元/天 解锁文章

200万优质内容无限畅学

![](https://csdnimg.cn/release/blogv2/dist/pc/img/vip-limited-close-newWhite.png)

确定要放弃本次机会？

福利倒计时

*:*

*:*

![](https://csdnimg.cn/release/blogv2/dist/pc/img/vip-limited-close-roup.png)
立减 ¥

普通VIP年卡可用

[立即使用](https://mall.csdn.net/vip)

[![](https://profile-avatar.csdnimg.cn/2ccacbf1fc8347338ede60bde7fb2eec_nokiaguy.jpg!1)

蒙娜丽宁](https://unitymarvel.blog.csdn.net)

关注
关注

* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarThumbUpactive.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/like-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/like.png)

  12

  点赞
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike.png)

  踩
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCollectActive.png)

  8

  收藏

  觉得还不错?
  一键收藏
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/collectionCloseWhite.png)
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/guideRedReward01.png)
  知道了

  [![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/comment.png)

  0](#commentBox)

  评论
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/share.png)
  分享

  复制链接

  分享到 QQ

  分享到新浪微博

  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/share/icon-wechat.png)扫一扫
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/more.png)

  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/report.png)
  举报

  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/report.png)
  举报

专栏目录

参与评论
您还未登录，请先
登录
后发表或查看评论

![](https://csdnimg.cn/release/blogv2/dist/components/img/blogType.png)
博客
[AIGC撕裂劳动力市场：技术狂潮下，人类将走向乌托邦还是深渊？](https://unitymarvel.blog.csdn.net/article/details/145234235)

01-18
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
2559

[随着人工智能（AI）技术的迅猛发展，尤其是生成式AI（AIGC），劳动力市场正经历前所未有的变革。从内容创作到自动化生产线，几乎每个行业都在经历一场技术的洗礼。然而，这场革命并不是全然的光明，它带来了深刻的社会变动，也引发了广泛的担忧和不安。我们不得不面对一个核心问题：AIGC将如何影响未来的工作？会让人类的大多数工作消失，还是会创造出全新的职业机会？](https://unitymarvel.blog.csdn.net/article/details/145234235)

![](https://csdnimg.cn/release/blogv2/dist/components/img/blogType.png)
博客
[【Python图形图像】《Python OpenCV从菜鸟到高手》——零基础进阶，开启图像处理与计算机视觉的大门！](https://unitymarvel.blog.csdn.net/article/details/143574491)

11-07
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
2251

[《Python OpenCV从菜鸟到高手》是一本深入探讨Python与OpenCV技术的图像处理教程。从Python的基础知识到OpenCV的强大功能，这本书带领读者逐步掌握计算机视觉的核心技术。Python因其简洁和强大的库生态被广泛应用于数据分析、人工智能等领域，而OpenCV则是图像处理与计算机视觉的利器。本书通过循序渐进的方式，让读者从零基础到掌握高级图像处理技能，帮助你实现从初学者到高手的跃升。](https://unitymarvel.blog.csdn.net/article/details/143574491)

![](https://csdnimg.cn/release/blogv2/dist/components/img/blogType.png)
博客
[【奇妙的Python】解锁Python编程的无限可能：《奇妙的Python》带你漫游代码世界](https://unitymarvel.blog.csdn.net/article/details/141889588)

09-04
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
3140

[《奇妙的Python——神奇代码漫游之旅》是一本面向实际应用的Python编程指南，涵盖文件操作、GUI设计、多媒体处理、自动化办公、加密解密等多个领域。由华为HDE专家李宁编写，通过丰富的实战案例，帮助读者在工作和项目中高效应用Python，提升编程技能。无论是新手还是有经验的开发者，这本书都将带你深入探索Python的无限可能，开启一段充满创意与实用性的编程之旅。](https://unitymarvel.blog.csdn.net/article/details/141889588)

![](https://csdnimg.cn/release/blogv2/dist/components/img/blogType.png)
博客
[2025机器人产业大洗牌：新兴初创企业的技术革命与崛起之路](https://unitymarvel.blog.csdn.net/article/details/151067555)

09-01
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
1049

[摘要：2025年机器人产业正经历技术驱动的深度变革，AI初创企业通过创新算法和低成本方案挑战传统巨头。本文剖析产业洗牌动因，包括AI融合、融资热潮和应用场景扩展，重点解析人形机器人等关键技术。通过ROS控制、A\*路径规划和PyTorch视觉识别等代码示例（附中文注释），展示初创企业的技术优势。文章预测Figure AI、Unitree等公司将引领消费级机器人市场，推动社会进入智能协作新时代。（150字）](https://unitymarvel.blog.csdn.net/article/details/151067555)

![](https://csdnimg.cn/release/blogv2/dist/components/img/blogType.png)
博客
[Java应用容器化革命：Docker部署从入门到精通](https://unitymarvel.blog.csdn.net/article/details/151067543)

09-01
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
963

[在现代软件开发中，容器化技术已成为提升应用部署效率和可移植性的关键工具。本文以“Java 与 Docker：容器化部署入门”为主题，深入探讨如何将Java应用无缝集成到Docker环境中。从Docker的基本概念和安装入手，我们将逐步引导读者构建一个简单的Java Web应用，并通过编写Dockerfile实现镜像的创建和容器的运行。文章涵盖了多阶段构建、环境变量配置、数据持久化、网络管理以及安全最佳实践等核心内容。通过大量的代码示例和详细的中文注释，读者可以轻松上手实践操作。同时，我们还将介绍常见问题排查](https://unitymarvel.blog.csdn.net/article/details/151067543)

![](https://csdnimg.cn/release/blogv2/dist/components/img/blogType.p...
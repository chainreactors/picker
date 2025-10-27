---
title: 【算法】Dijkstra算法的实现与优化：C语言实现最短路径算法
url: https://blog.csdn.net/nokiaguy/article/details/145531502
source: 一个被知识诅咒的人
date: 2025-02-10
fetch_date: 2025-10-06T20:35:16.762712
---

# 【算法】Dijkstra算法的实现与优化：C语言实现最短路径算法

# 【算法】Dijkstra算法的实现与优化：C语言实现最短路径算法

![](https://csdnimg.cn/release/blogv2/dist/pc/img/original.png)

[![](https://csdnimg.cn/release/blogv2/dist/pc/img/identityVipNew.png)](https://mall.csdn.net/vip)
[蒙娜丽宁](https://unitymarvel.blog.csdn.net "蒙娜丽宁")
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCurrentTime2.png)
于 2025-02-09 13:45:41 发布

![](https://csdnimg.cn/release/blogv2/dist/pc/img/articleReadEyes2.png)
阅读量1.2k
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)
收藏

15

![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)
点赞数
17

CC 4.0 BY-SA版权

分类专栏：
[C杂谈](https://blog.csdn.net/nokiaguy/category_12890481.html)
[算法](https://blog.csdn.net/nokiaguy/category_508758.html)
文章标签：
[算法](https://so.csdn.net/so/search/s.do?q=%E7%AE%97%E6%B3%95&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[c语言](https://so.csdn.net/so/search/s.do?q=c%E8%AF%AD%E8%A8%80&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[图论](https://so.csdn.net/so/search/s.do?q=%E5%9B%BE%E8%AE%BA&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

本文链接：<https://blog.csdn.net/nokiaguy/article/details/145531502>

### 1. Dijkstra算法概述

#### 1.1 算法简介

Dijkstra算法是计算图中某个顶点到其他所有顶点的最短路径的一种经典算法。该算法由计算机科学家Edsger Dijkstra于1956年提出，广泛应用于路由算法、网络优化、地图导航等领域。它的基本思想是，通过一个贪心策略，每次选择当前未处理的最短路径顶点，然后更新其邻居顶点的最短路径，直到处理所有顶点。

Dijkstra算法只适用于图中的边权重都是非负数的情况，对于负权边则需要使用Bellman-Ford算法或其他适合负权边的算法。

#### 1.2 算法原理

Dijkstra算法的原理可以简述为以下步骤：

1. **初始化**：首先，选择一个源点，并初始化源点到所有其他点的距离为无穷大，源点到源点的距离为0。标记所有节点为未访问。
2. **选择最小值顶点**：每次从未访问的顶点中选择一个距离源点最近的顶点。
3. **更新邻接节点的距离**：对于当前选择的顶点，检查它的所有邻接顶点，如果通过该顶点到达某个邻接顶点的距离更短，则更新该邻接顶点的最短路径。
4. **重复**：继续选择未访问的顶点，直到所有顶点的最短路径都被找到。

Dijkstra算法可以通过优先队列（通常是最小堆）来优化，以减少寻找最小距离节点的时间复杂度。

---

### 2. C语言实现Dijkstra算法

接下来，我们将使用C语言实现Dijkstra算法，解决图中的最短路径问题。我们将分步解释实现过程。

#### 2.1 基本实现

在此实现中，我们假设图是一个邻接矩阵表示的有向图，`graph[i][j]`表示从顶点i到顶点j的边权重。如果没有边，则设置为无穷大（`INF`）。

##### 2.1.1 C语言代码实现

```
#include <stdio.h>
#include <limits.h>

#define MAX_VERTICES 10  // 图中最大顶点数
#define INF INT_MAX      // 定义无穷大

// 函数：选择最短路径的顶点
int selectMinVertex(int distance[], bool processed[], int n) {

    int minimum = INF;
    int vertex;

    // 查找未处理的最短路径顶点
    for (int i = 0; i < n; i++) {

        if (!processed[i] && distance[i] < minimum) {

            vertex = i;
            minimum = distance[i];
        }
    }

    return vertex;
}

// 函数：Dijkstra算法实现
void dijkstra(int graph[MAX_VERTICES][MAX_VERTICES], int n, int start) {

    int distance[MAX_VERTICES];  // 存储从源点到各个顶点的最短距离
    bool processed[MAX_VERTICES]; // 标记顶点是否已经处理

    // 初始化
    for (int i = 0; i < n; i++) {

        distance[i] = INF;
        processed[i] = false;
    }
    distance[start] = 0;

    // 计算最短路径
    for (int count = 0; count < n - 1; count++) {

        // 选择未处理的最短路径顶点
        int u = selectMinVertex(distance, processed, n);
        processed[u] = true;

        // 更新与该顶点相邻的所有顶点的最短路径
        for (int v = 0; v < n; v++) {

            if (graph[u][v] != INF && !processed[v]) {

                int newDist = distance[u] + graph[u][v];
                if (newDist < distance[v
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

  17

  点赞
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike.png)

  踩
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCollectActive.png)

  15

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

![](https://csdnimg.cn/release/blogv2/dist/components/img/blogType.png)
博客
[【人工智能】AI代理重塑游戏世界：动态NPC带来的革命性沉浸...
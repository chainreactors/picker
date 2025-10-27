---
title: 【人工智能】深入浅出协同过滤：使用Python构建个性化推荐系统
url: https://blog.csdn.net/nokiaguy/article/details/147757418
source: 一个被知识诅咒的人
date: 2025-05-08
fetch_date: 2025-10-06T22:24:22.697961
---

# 【人工智能】深入浅出协同过滤：使用Python构建个性化推荐系统

# 【人工智能】深入浅出协同过滤：使用Python构建个性化推荐系统

原创
[![](https://csdnimg.cn/release/blogv2/dist/pc/img/identityVipNew.png)](https://mall.csdn.net/vip)
于 2025-05-07 11:38:23 发布
·
1.2k 阅读

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)

28

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)

28
·

CC 4.0 BY-SA版权

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

文章标签：

[#人工智能](https://so.csdn.net/so/search/s.do?q=%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#python](https://so.csdn.net/so/search/s.do?q=python&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#开发语言](https://so.csdn.net/so/search/s.do?q=%E5%BC%80%E5%8F%91%E8%AF%AD%E8%A8%80&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

[《Python OpenCV从菜鸟到高手》带你进入图像处理与计算机视觉的大门！](https://blog.csdn.net/nokiaguy/article/details/143574491)

[解锁Python编程的无限可能：《奇妙的Python》带你漫游代码世界](https://unitymarvel.blog.csdn.net/article/details/141889588)

推荐系统是当今数据驱动世界中的一项核心技术，广泛应用于电商、社交平台、媒体等领域。协同过滤（Collaborative Filtering）是最常见的推荐算法之一，它基于用户历史行为数据来推荐用户可能感兴趣的物品。协同过滤可以分为基于用户的协同过滤和基于物品的协同过滤两种方法。本篇文章将详细介绍协同过滤的基本原理，结合Python中的`Surprise`库实现一个简单的推荐系统。文章包括了从数据预处理、模型构建到评价指标等全方位的内容，帮助读者理解推荐系统的基本操作和实现步骤。通过丰富的代码示例和详细的中文注释，读者能够全面掌握如何使用Python实现一个基于协同过滤的推荐系统，并将其应用于实际项目中。

---

#### 引言

推荐系统是当前互联网应用中不可或缺的一部分，尤其是在电商、社交网络、影音平台等场景中。用户每天都面临着海量的信息，推荐系统帮助用户在这些信息中找到最感兴趣的部分，提高了用户体验并促进了平台的商业化。推荐系统的核心任务是通过分析用户的行为数据，预测用户对未接触过的物品的偏好，并进行个性化推荐。

在众多推荐算法中，协同过滤（Collaborative Filtering）因其简单、易于理解且有效的特点，成为了最广泛使用的推荐技术之一。协同过滤的基本思想是：如果用户A和用户B对一些物品的评分相似，那么他们可能对其他物品也有相似的兴趣。基于这种假设，协同过滤推荐系统能够通过分析历史数据，推荐用户感兴趣的物品。

在本篇文章中，我们将深入探讨协同过滤的原理，使用Python中的`Surprise`库来实现一个简单的协同过滤推荐系统。文章将包括完整的代码和详细的解释，帮助读者理解协同过滤算法的实现过程。

#### 1. 协同过滤的基本原理

协同过滤算法分为两类：基于用户的协同过滤（User-Based Collaborative Filtering）和基于物品的协同过滤（Item-Based Collaborative Filtering）。它们的基本思路相似，区别在于推荐的对象。

##### 1.1 基于用户的协同过滤

基于用户的协同过滤算法的基本思路是：通过寻找与目标用户兴趣相似的其他用户，来预测目标用户可能感兴趣的物品。例如，如果用户A和用户B在过去对许多相同的物品给出了相似的评分，那么他们在其他物品上的兴趣可能也会相似。基于这个假设，推荐系统可以根据用户B对物品的评分来推荐给用户A。

##### 1.2 基于物品的协同过滤

与基于用户的协同过滤不同，基于物品的协同过滤算法关注的是物品之间的相似性。如果用户A喜欢物品X，且物品X与物品Y非常相似，那么用户A也可能喜欢物品Y。基于物品的协同过滤通过计算物品之间的相似性，来向用户推荐他们尚未接触过的类似物品。

##### 1.3 协同过滤的挑战

尽管协同过滤算法简单且易于理解，但它也面临一些挑战，如：

* **稀疏性问题**：在实际应用中，用户与物品之间的交互数据通常非常稀疏。大部分用户只与少数物品发生过交互，这使得协同过滤算法很难找到足够的相似用户或物品。
* **冷启动问题**：对于新用户或新物

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

  28

  点赞
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike.png)

  踩
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCollectActive.png)

  28

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
3141

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
[【人工智能】AI代理重塑游戏世界：动态NPC带来的革命性沉浸式体验](https://unitymarvel.blog.csdn.net/article/details/150948550)

08-28
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
1081

[在当今游戏行业迅猛发展的时代，AI代理技术正悄然引发一场革命，尤其是动态非玩家角色（NPC）的应用，将传统静态游戏体验提升至全新的沉浸式境界。本文深入探讨AI代理在游戏中的核心作用，从传统NPC的局限性入手，分析AI代理如何通过机器学习、强化学习和自然语言处理等技术实现动态行为响应。文章详细阐述了AI代理的架构设计、实现路径，并提供大量代码示例，包括Python和C#语言的实际实现，辅以中文注释，帮助读者理解从简单状态机到复杂代理系统的构建过程。同时，引入数学模型如Q-learning算法的LaTeX公式，](https://unitymarvel.blog.csdn.net/article/details/150948550)

![](https://csdnimg.cn/release/blogv2/dist/components/img/blogType.png)
博客
[具身智能与AI代理融合的全能助手革命](https://unitymarvel.blog.csdn.net/article/details/150948537)

08-28
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
1367

[在2025年，人工智能技术迅猛发展，具身智能（Embodied Intelligence）与AI代理（AI Agents）的结合正悄然重塑人类生活和工作方式。这种融合将抽象的AI算法嵌入物理实体中，形成具备感知、决策和行动...
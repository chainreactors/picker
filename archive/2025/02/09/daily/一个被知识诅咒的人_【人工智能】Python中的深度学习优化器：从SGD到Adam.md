---
title: 【人工智能】Python中的深度学习优化器：从SGD到Adam
url: https://blog.csdn.net/nokiaguy/article/details/145513088
source: 一个被知识诅咒的人
date: 2025-02-09
fetch_date: 2025-10-06T20:35:49.838359
---

# 【人工智能】Python中的深度学习优化器：从SGD到Adam

# 【人工智能】Python中的深度学习优化器：从SGD到Adam

原创
[![](https://csdnimg.cn/release/blogv2/dist/pc/img/identityVipNew.png)](https://mall.csdn.net/vip)
于 2025-02-08 12:17:10 发布
·
1.8k 阅读

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)

29

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)

15
·

CC 4.0 BY-SA版权

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

文章标签：

[#人工智能](https://so.csdn.net/so/search/s.do?q=%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#python](https://so.csdn.net/so/search/s.do?q=python&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#深度学习](https://so.csdn.net/so/search/s.do?q=%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

[《Python OpenCV从菜鸟到高手》带你进入图像处理与计算机视觉的大门！](https://blog.csdn.net/nokiaguy/article/details/143574491)

[解锁Python编程的无限可能：《奇妙的Python》带你漫游代码世界](https://unitymarvel.blog.csdn.net/article/details/141889588)

在深度学习模型的训练过程中，优化器起着至关重要的作用，它决定了模型的收敛速度以及最终的性能。本文将介绍深度学习中常用的优化器，从传统的随机梯度下降（SGD）到现代的自适应优化器（如Adam）。我们将深入探讨每种优化器的原理、优缺点，并通过Python实现这些优化器的算法。为了帮助读者更好地理解，我们会提供大量的代码示例，并逐步解释每个优化器的数学原理和实现细节。此外，本文还将比较这些优化器在不同任务中的表现，包括它们的收敛速度和最终的性能。

---

#### 引言

深度学习作为一种强大的机器学习方法，在图像识别、自然语言处理等多个领域取得了显著的突破。在深度学习的训练过程中，优化器是决定模型训练效率和效果的关键因素之一。优化器通过调整模型的参数，使得模型的损失函数逐渐减小，从而找到最优解。常见的优化器包括随机梯度下降（SGD）、动量法（Momentum）、AdaGrad、RMSProp和Adam等。

在本文中，我们将介绍这些优化器的基本原理，逐步深入它们的数学背景，并提供详细的Python代码实现。通过对比它们在不同训练任务中的表现，帮助读者选择最适合自己问题的优化算法。

#### 第一部分：优化器的基本概念与原理

##### 1.1 梯度下降法（Gradient Descent）

梯度下降法是最基础的优化算法，它通过计算损失函数相对于模型参数的梯度来更新参数。具体而言，在每次迭代中，参数会沿着梯度的反方向进行调整，从而最小化损失函数。

梯度下降的更新公式为：
  θ t + 1 = θ t − η ∇ θ J ( θ t ) \theta\_{t+1} = \theta\_t - \eta \nabla\_{\theta} J(\theta\_t) θt+1​=θt​−η∇θ​J(θt​)
 其中， θ t \theta\_t θt​表示模型的参数， η \eta η是学习率， ∇ θ J ( θ t ) \nabla\_{\theta} J(\theta\_t) ∇θ​J(θt​)是损失函数 J ( θ ) J(\theta) J(θ)关于 θ t \theta\_t θt​的梯度。

梯度下降法有三种变种：批量梯度下降（Batch Gradient Descent）、随机梯度下降（Stochastic Gradient Descent，SGD）和小批量梯度下降（Mini-batch Gradient Descent）。

##### 1.2 随机梯度下降（SGD）

在标准的梯度下降法中，我们需要计算整个数据集的梯度来更新参数，这在数据量很大的时候非常耗时。随机梯度下降（SGD）通过每次使用一个样本来更新参数，从而大大提高了计算效率。

SGD的更新公式为：
  θ t + 1 = θ t − η ∇ θ J ( θ t , x i , y i ) \theta\_{t+1} = \theta\_t - \eta \nabla\_{\theta} J(\theta\_t, x\_i, y\_i) θt+1​=θt​−η∇θ​J(θt​,xi​,yi​)
 其中， ( x i , y i ) (x\_i, y\_i) (xi​,yi​)是第 i i i个样本， ∇ θ J ( θ t , x i , y i ) \nabla\_{\theta} J(\theta\_t, x\_i, y\_i) ∇θ​J(θt​,xi​,yi​)是损失函数相对于参数 θ \theta θ的梯度。

###### 1.2.1 SGD的优缺点

* 优点：
  + 计算效率高，适用于大规模数据。
  + 可以跳出局部最小值，具有一定的探索性。
* 缺点：
  + 收敛速度较慢，损失函数的震荡较大，导致优化过程不稳定。

##### 1.3 动量法（Momentum）

动量法通过引入“惯性”来加速SGD，减少梯度下降过程中震荡的影响。其基本思想是，将当前的梯度与前一步的梯度相结合，从而使得模型更新时更具方向性。

动量法的更新公式为：
  v t + 1 = β v t + ( 1 − β ) ∇ θ J ( θ t ) v\_{t+1} = \beta v\_t + (1 - \beta) \nabla\_{\theta} J(\theta\_t) vt+1​=βvt​+(1−β)∇θ​J(θt​)
  θ t + 1 = θ t − η v t + 1 \theta\_{t+1} = \theta\_t - \eta v\_{t+1} θt+1​=θt​−ηvt+1​
 其中， v t v\_t vt​是动量项， β \beta β是动量因子，通常设置为0.9。

###### 1.3.1 动量法的优缺点

* 优点：
  + 减少了SGD的震荡，加快了收敛速度。
  + 对于大规模数据和深度网络非常有效。
* 缺点：
  + 需要手动调整动量因子，可能导致过冲或过度平滑。

##### 1.4 AdaGrad

AdaGrad（Adaptive Gradient）是一个自适应学习率的优化算法，它根据每个参数的历史梯度动态调整学习率，从而使得常见的特征具有较小的学习率，而不常见的特征具有较大的学习率。

AdaGrad的更新公式为：
  θ t + 1 = θ t − η G t + ϵ ∇ θ J ( θ t ) \theta\_{t+1} = \theta\_t - \frac{\eta}{\sqrt{G\_{t} + \epsilon}} \nabla\_{\theta} J(\theta\_t) θ

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

  29

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

[在现代软件开发中，容器化技术已成为提升应用部署效率和可移植性的关键工具。本文以“Java 与 Docker：容器化部署入门”为主题，深入探讨如何将Java应用无缝集成到Docker环境中。从Docker的基本概念和安装入手，我们将逐步引导读者构建一个简单的Java Web应用，并通过编写Dockerfile实现镜像的创建和容器的运行。文章涵盖了多阶段构建、环境变量配置、数据持久化、网络管理以及安全最佳实践等核心内容。通过大量的代码示...
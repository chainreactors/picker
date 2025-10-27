---
title: 探索Python中的神经网络：从零构建一个简单的深度学习模型
url: https://blog.csdn.net/nokiaguy/article/details/142714825
source: 一个被知识诅咒的人
date: 2024-10-08
fetch_date: 2025-10-06T18:49:43.282841
---

# 探索Python中的神经网络：从零构建一个简单的深度学习模型

# 探索Python中的神经网络：从零构建一个简单的深度学习模型

![](https://csdnimg.cn/release/blogv2/dist/pc/img/original.png)

[![](https://csdnimg.cn/release/blogv2/dist/pc/img/identityVipNew.png)](https://mall.csdn.net/vip)
[蒙娜丽宁](https://unitymarvel.blog.csdn.net "蒙娜丽宁")
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCurrentTime2.png)
于 2024-10-07 10:00:00 发布

![](https://csdnimg.cn/release/blogv2/dist/pc/img/articleReadEyes2.png)
阅读量1.4k
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)
收藏

20

![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)
点赞数
33

CC 4.0 BY-SA版权

分类专栏：
[Python杂谈](https://blog.csdn.net/nokiaguy/category_12800257.html)
文章标签：
[深度学习](https://so.csdn.net/so/search/s.do?q=%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[python](https://so.csdn.net/so/search/s.do?q=python&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[神经网络](https://so.csdn.net/so/search/s.do?q=%E7%A5%9E%E7%BB%8F%E7%BD%91%E7%BB%9C&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

本文链接：<https://blog.csdn.net/nokiaguy/article/details/142714825>

[解锁Python编程的无限可能：《奇妙的Python》带你漫游代码世界](https://unitymarvel.blog.csdn.net/article/details/141889588?spm=1001.2014.3001.5502)

### 引言

随着人工智能（AI）和机器学习（ML）的快速发展，深度学习（Deep Learning）逐渐成为解决复杂问题的强大工具。神经网络是深度学习的核心，它模拟了人脑神经元之间的连接，能够学习数据中的复杂模式和特征。本文将带领读者从零开始，使用Python构建一个简单的神经网络模型，帮助理解深度学习的基础概念、工作原理以及如何实现。

本文的目标是通过逐步拆解神经网络的工作流程，让读者从构建简单的神经元到完成一个具有多个隐藏层的深度神经网络。我们将实现前向传播（Forward Propagation）、损失函数（Loss Function）、反向传播（Backpropagation）以及权重更新（Weight Update）的所有过程。

---

### 什么是神经网络？

神经网络（Neural Network）是一种模拟生物神经元结构的计算模型。它由多个神经元组成，神经元之间通过权重连接。神经网络的输入通过一系列的隐藏层处理后，最终输出一个结果。深度学习的关键思想是使用大量的神经元和隐藏层，使网络能够从数据中学习到复杂的模式。

神经网络的结构可以简单地分为以下几个部分：

1. **输入层**：接收数据输入，每个输入对应一个神经元。
2. **隐藏层**：位于输入和输出之间，可以有多个层，负责处理和提取数据的特征。
3. **输出层**：生成最终的预测结果。
4. **权重和偏置**：每个连接都附有权重，控制数据在网络中的传递过程。偏置是每个神经元的初始值，增加网络的灵活性。

#### 神经网络的工作流程

神经网络的工作流程主要包括以下几个步骤：

* **前向传播**：将输入数据经过每一层神经元的计算，最后生成输出。
* **损失计算**：根据输出和实际值的差异计算损失，通常使用均方误差（Mean Squared Error, MSE）或交叉熵损失（Cross Entropy Loss）。
* **反向传播**：通过链式法则计算损失对各个权重的梯度。
* **权重更新**：使用梯度下降算法更新权重，减少损失函数的值。

我们将在后面的实现部分中详细介绍这些步骤。

---

### 环境准备

在开始实现之前，我们需要配置开发环境并安装必要的库。虽然我们将手动实现神经网络的核心部分，但仍需借助NumPy来进行矩阵运算。

#### 安装NumPy

NumPy是Python中用于数值计算的基础库，它提供了高效的多维数组对象以及丰富的数学函数。我们将使用NumPy来实现神经网络中的矩阵运算。

使用以下命令安装NumPy：

```
pip install numpy
```

---

### 构建一个简单的神经网络

接下来，我们将从零开始构建一个简单的神经网络。为简化实现，我们将创建一个**前馈神经网络**（Feedforward Neural Network），它包含一个输入层、一个隐藏层和一个输出层。我们将用这个网络来解决一个分类问题。

#### 1. 数据准备

首先，我们为神经网络准备一个简单的数据集。为了便于理解，我们生成一个二维数据集，其中每个点属于两个类别中的一个。

```
import numpy as np
import matplotlib.pyplot as plt

# 生成数据集
np.random.seed(0)
num_samples_per_class = 100
D = 2  # 数据的维度
K = 2  # 类别数量

# 类别0的样本
X0 = np.random.randn(num_samples_per_class, D) + np.array([0, -1])
# 类别1的样本
X1 = np.random.randn(num_samples_per_class, D) + np.array([1, 1])

# 合并样本
X = np.vstack([X0, X1])
# 标签
y = np.array([0] * num_samples_per_class + [
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

  33

  点赞
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike.png)

  踩
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCollectActive.png)

  20

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
2558

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
962

[在现代软件开发中，容器化技术已成为提升应用部署效率和可移植性的关键工具。本文以“Java 与 Docker：容器化部署入门”为主题，深入探讨如何将Java应用无缝集成到Docker环境中。从Docker的基本概念和安装入手，我们将逐步引导读者构建一个简单的Java Web应用，并通过编写Dockerfile实现镜像的创建和容器的运行。文章涵盖了多阶段构建、环境变量配置、数据持久化、网络管理以及安全最佳实践等核心内容。通过大量的代码示例和详细的中文注释，读者可以轻松上手实践操作。同时，我们还将介绍常见问题排查](https://unitymarvel.blog.csdn.net/article/details/151067543)

![](https://csdnimg.cn/release/blogv2/dist/components/img/blogType.png)
博客
[【人工智能】AI代理重塑游戏世界：动态NPC带来的革命性沉浸式体验](https://unitymarvel.blog.csdn.net/article/details/150948550)

08-28
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readC...
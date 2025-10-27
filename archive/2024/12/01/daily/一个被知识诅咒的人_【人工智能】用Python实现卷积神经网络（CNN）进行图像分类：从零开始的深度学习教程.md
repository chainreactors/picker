---
title: 【人工智能】用Python实现卷积神经网络（CNN）进行图像分类：从零开始的深度学习教程
url: https://blog.csdn.net/nokiaguy/article/details/144153759
source: 一个被知识诅咒的人
date: 2024-12-01
fetch_date: 2025-10-06T19:33:57.634736
---

# 【人工智能】用Python实现卷积神经网络（CNN）进行图像分类：从零开始的深度学习教程

# 【人工智能】用Python实现卷积神经网络（CNN）进行图像分类：从零开始的深度学习教程

原创
[![](https://csdnimg.cn/release/blogv2/dist/pc/img/identityVipNew.png)](https://mall.csdn.net/vip)
于 2024-11-30 13:40:50 发布
·
1.5k 阅读

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)

33

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)

21
·

CC 4.0 BY-SA版权

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

文章标签：

[#人工智能](https://so.csdn.net/so/search/s.do?q=%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#深度学习](https://so.csdn.net/so/search/s.do?q=%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#python](https://so.csdn.net/so/search/s.do?q=python&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

[《Python OpenCV从菜鸟到高手》带你进入图像处理与计算机视觉的大门！](https://blog.csdn.net/nokiaguy/article/details/143574491)

卷积神经网络（CNN）是处理图像分类任务的核心工具，它通过卷积操作和池化机制提取图像的特征并实现分类。本文将手把手教你如何使用 Python 和深度学习框架（PyTorch）从头实现一个 CNN 模型，应用于图像分类任务。我们将从基础概念入手，详细讲解卷积层、池化层和全连接层的工作原理，配合代码示例逐步搭建一个完整的 CNN，并在 CIFAR-10 数据集上进行训练和测试。通过本文，你将掌握 CNN 的基本原理和实现方法，为后续深入学习深度学习奠定坚实基础。

---

### **一、卷积神经网络的基础知识**

#### **1.1 什么是卷积神经网络（CNN）？**

卷积神经网络（Convolutional Neural Network，CNN）是一种专门用于处理图像数据的深度学习模型。其核心在于通过卷积操作提取图像的局部特征，并逐步组合成更高层次的特征。

CNN 的主要结构包括：

1. **卷积层（Convolutional Layer）**：提取图像的特征。
2. **池化层（Pooling Layer）**：减少特征图的尺寸，降低计算量。
3. **全连接层（Fully Connected Layer）**：将提取的特征映射到输出类别。

#### **1.2 卷积层的核心概念**

##### 卷积操作

卷积操作通过一个小的核（kernel 或 filter）对图像的局部区域进行加权求和，从而提取特征。

设输入图像为二维矩阵  I I I，卷积核为  K K K，则卷积的公式为：

O ( i , j ) = ∑ m = 0 M − 1 ∑ n = 0 N − 1 I ( i + m , j + n ) ⋅ K ( m , n ) O(i, j) = \sum\_{m=0}^{M-1} \sum\_{n=0}^{N-1} I(i+m, j+n) \cdot K(m, n) O(i,j)=m=0∑M−1​n=0∑N−1​I(i+m,j+n)⋅K(m,n)

其中：

* O ( i , j ) O(i, j) O(i,j) 是输出特征图的像素值。
* M × N M \times N M×N 是卷积核的大小。

##### 卷积操作示例

以下代码实现一个简单的二维卷积操作：

```
import numpy as np

def convolution2d(image, kernel):
    # 获取图像和卷积核的尺寸
    image_height, image_width = image.shape
    kernel_height, kernel_width = kernel.shape

    # 计算输出图像的尺寸
    output_height = image_height - kernel_height + 1
    output_width = image_width - kernel_width + 1

    # 初始化输出矩阵
    output = np.zeros((output_height, output_wi
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

  21

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

[在2025年，人工智能技术迅猛发展，具身智能（Embodied Intelligence）与AI代理（AI Agents）的结合正悄然重塑人类生活和工作方式。这种融合将抽象的AI算法嵌入物理实体中，形成具备感知、决策和行动能力的“全能助手”。本文深入探讨了这一主题的核心概念、技术框架和实际应用。从具身智能的理论基础到AI代理的自主学习机制，我们将剖析强化学习、计算机视觉和多模态融合等关键技...
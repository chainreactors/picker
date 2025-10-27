---
title: 【C++】掌握C++异常处理机制：从try-catch到noexcept
url: https://blog.csdn.net/nokiaguy/article/details/143109258
source: 一个被知识诅咒的人
date: 2024-11-01
fetch_date: 2025-10-06T19:15:52.840029
---

# 【C++】掌握C++异常处理机制：从try-catch到noexcept

# 【C++】掌握C++异常处理机制：从try-catch到noexcept

![](https://csdnimg.cn/release/blogv2/dist/pc/img/original.png)

[![](https://csdnimg.cn/release/blogv2/dist/pc/img/identityVipNew.png)](https://mall.csdn.net/vip)
[蒙娜丽宁](https://unitymarvel.blog.csdn.net "蒙娜丽宁")
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCurrentTime2.png)
于 2024-10-31 09:15:00 发布

![](https://csdnimg.cn/release/blogv2/dist/pc/img/articleReadEyes2.png)
阅读量1.9k
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)
收藏

38

![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)
点赞数
36

CC 4.0 BY-SA版权

分类专栏：
[C++杂谈](https://blog.csdn.net/nokiaguy/category_12807248.html)
文章标签：
[C++](https://so.csdn.net/so/search/s.do?q=C%2B%2B&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[异常](https://so.csdn.net/so/search/s.do?q=%E5%BC%82%E5%B8%B8&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

本文链接：<https://blog.csdn.net/nokiaguy/article/details/143109258>

[解锁Python编程的无限可能：《奇妙的Python》带你漫游代码世界](https://unitymarvel.blog.csdn.net/article/details/141889588?spm=1001.2014.3001.5502)

异常处理是C++语言中的一个关键特性，旨在提高程序的健壮性并确保在发生错误时能够妥善处理。然而，错误的异常处理不仅会增加程序的复杂性，还可能导致难以调试的错误。本文将深入探讨C++中的异常处理机制，涵盖`try-catch`块的基本使用、如何设计异常安全的代码，以及`noexcept`关键字的作用与使用。我们还将探讨`noexcept`对程序性能的影响，帮助读者在编写C++程序时更好地平衡代码的健壮性和效率。

### 引言

异常处理是一种控制流程的方式，旨在处理程序运行中的异常情况。异常通常是一些无法在正常流程中预期的错误，例如内存不足、文件无法打开或网络连接中断。通过异常处理机制，程序可以捕获这些异常并采取适当的措施，而不是直接崩溃。

C++中的异常处理机制与其他高级编程语言（如Java、Python等）类似，但也有其独特之处。C++不仅允许我们在运行时捕获并处理异常，还提供了更多的灵活性，使我们能够在编译期优化代码。理解并正确使用这些工具对于编写健壮且高效的C++程序至关重要。

本文将从C++的异常处理机制入手，介绍`try-catch`结构的基本用法，讨论如何设计异常安全的代码，探讨不同的异常处理策略，并深入分析`noexcept`关键字的作用及其对性能的影响。

### C++异常处理的基本机制

#### 什么是异常？

异常是指程序在执行过程中遇到的无法正常处理的情况。C++中的异常可以是程序运行时的错误，如空指针解引用、除以零或内存分配失败等。为了应对这些错误，C++提供了一个用于抛出、捕获和处理异常的结构化机制。

在C++中，异常处理通常通过以下三个步骤完成：

1. **抛出异常**：使用`throw`关键字抛出异常对象。
2. **捕获异常**：使用`try-catch`块捕获并处理异常。
3. **传播异常**：如果当前函数无法处理异常，异常会沿调用栈向上传播，直到找到合适的异常处理程序。

#### `try-catch`的基本用法

`try-catch`结构是C++中处理异常的主要工具。`try`块包围可能抛出异常的代码，而`catch`块用于捕获和处理异常。以下是一个简单的例子：

```
#include <iostream>
#include <stdexcept>

int divide(int a, int b) {

    if (b == 0) {

        throw std::runtime_error("除数不能为零");
    }
    return a / b;
}

int main() {

    try {

        int result = divide(10, 0);
        std::cout << "结果是: " << result << std::endl;
    } catch (const std::runtime_error& e) {

        std::cerr << "捕获异常: " << e.what() << std::endl;
    }

    return 0;
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

  36

  点赞
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike.png)

  踩
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCollectActive.png)

  38

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
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
1081

[在当今游戏行业迅猛发展的时代，AI代理技术正悄然引发一场革命，尤其是动态非玩家角色（NPC）的应用，将传统静态游戏体验提升至全新的沉浸式境界。本文深入探讨AI代理在游戏中的核心作用，从传统NPC的局限性入手，分析AI代理如何通过机器学习、强化学习和自然语言处理等技术实现动态行为响应。文章详细阐述了AI代理的架构设计、实现路径，并提供大量代码示例，包括Python和C#语言的实际实现，辅以中文注释，帮助读者理解从简单状态机到复杂代理系统的构建过程。同时，引入数学模型如Q-learning算法的LaTeX公式，](https://unitymarvel.blog.csdn.net/article/details/150948550)

![](https://csdnimg.cn/release/blogv2/dist/components/img/blogType.png)
博客
[具身智能与AI代理融合的全能助手革命](https://unitymarvel.blog.csdn.net/article/details/150948537)

08-28
![](https://csdnimg.cn/release/blogv2/dist/pc/img/read...
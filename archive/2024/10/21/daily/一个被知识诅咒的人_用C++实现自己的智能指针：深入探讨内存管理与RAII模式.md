---
title: 用C++实现自己的智能指针：深入探讨内存管理与RAII模式
url: https://blog.csdn.net/nokiaguy/article/details/142918435
source: 一个被知识诅咒的人
date: 2024-10-21
fetch_date: 2025-10-06T18:48:38.558128
---

# 用C++实现自己的智能指针：深入探讨内存管理与RAII模式

# 用C++实现自己的智能指针：深入探讨内存管理与RAII模式

![](https://i-operation.csdnimg.cn/images/cf31225e169b4512917b2e77694eb0a2.png)C++智能指针实现与内存管理解析

![](https://csdnimg.cn/release/blogv2/dist/pc/img/original.png)

[![](https://csdnimg.cn/release/blogv2/dist/pc/img/identityVipNew.png)](https://mall.csdn.net/vip)
[蒙娜丽宁](https://unitymarvel.blog.csdn.net "蒙娜丽宁")
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCurrentTime2.png)
于 2024-10-20 10:15:00 发布

![](https://csdnimg.cn/release/blogv2/dist/pc/img/articleReadEyes2.png)
阅读量1.3k
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)
收藏

22

![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)
点赞数
20

CC 4.0 BY-SA版权

分类专栏：
[C++杂谈](https://blog.csdn.net/nokiaguy/category_12807248.html)
文章标签：
[c++](https://so.csdn.net/so/search/s.do?q=c%2B%2B&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[java](https://so.csdn.net/so/search/s.do?q=java&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[jvm](https://so.csdn.net/so/search/s.do?q=jvm&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

本文链接：<https://blog.csdn.net/nokiaguy/article/details/142918435>

[解锁Python编程的无限可能：《奇妙的Python》带你漫游代码世界](https://unitymarvel.blog.csdn.net/article/details/141889588?spm=1001.2014.3001.5502)

C++中的内存管理一直以来是程序员的一个难点，尤其是在处理动态内存分配时。智能指针（如`std::unique_ptr`和`std::shared_ptr`）通过RAII（资源获取即初始化）的设计理念，极大地简化了动态内存的管理，减少了内存泄漏的风险。然而，为了更好地理解智能指针的工作原理，掌握其背后的技术至关重要。本文将从零开始讲解如何实现自己的智能指针，探讨其内部细节，分析C++的内存管理机制，并展示如何利用RAII模式确保资源的安全释放。通过代码实例、详细的技术分析和表格展示，你将深入理解智能指针的本质及其实现方式。

---

### 目录

1. 引言
2. C++内存管理机制概述
   * 动态内存管理
   * RAII模式简介
3. 智能指针的作用和分类
   * `unique_ptr`
   * `shared_ptr`
4. 实现自己的`UniquePtr`
   * 构造与析构
   * 移动语义与禁止复制
   * 代码实现
5. 实现自己的`SharedPtr`
   * 引用计数机制
   * 弱引用与循环引用问题
   * 代码实现
6. 智能指针的高级话题
   * 自定义删除器
   * 多线程中的智能指针
7. 总结与展望

---

### 1. 引言

C++作为一门广泛应用的系统级编程语言，其内存管理一直是开发者必须关注的核心问题。尽管C++11引入了智能指针来简化内存管理，但对智能指针的理解仅停留在使用层面还远远不够。为了深入理解C++内存管理的原理，以及如何通过RAII模式防止内存泄漏和资源泄露，本文将详细讲解如何从零实现自己的智能指针，包括`UniquePtr`和`SharedPtr`。

通过本文，你将不仅掌握智能指针的使用，还将了解它们背后的设计思想，学习如何构建自己高效、可靠的内存管理工具。

---

### 2. C++内存管理机制概述

#### 动态内存管理

在C++中，内存分为两种主要类型：**静态内存**（编译时分配的变量，如全局变量和局部变量）和**动态内存**（运行时通过`new`和`delete`分配和释放）。动态内存管理提供了极大的灵活性，但也带来了潜在的风险：

1. **内存泄漏**：动态分配的内存未被正确释放，导致程序的内存占用不断增长。
2. **悬空指针**：当一个指针指向已经释放的内存时，再次访问该内存会产生未定义行为。
3. **双重释放**：同一块内存被释放两次，也会引发程序崩溃。

#### RAII模式简介

RAII（Resource Acquisition Is Initialization，资源获取即初始化）是C++的一种内存管理模式。其核心思想是将资源（如内存、文件、网络连接等）的分配和释放绑定到对象的生命周期中。对象构造时获取资源，析构时释放资源，这样可以确保资源在任何情况下都能正确释放。智能指针就是RAII模式的一个经典应用。

在使用RAII的类中，构造函数负责资源的获取，析构函数负责资源的释放。由于C++中对象的生命周期与作用域密切相关，一旦对象超出作用域，其析构函数会自动被调用，确保资源的安全释放。

---

### 3. 智能指针的作用和分类

#### 智能指针的作用

智能指针的主要功能是在对象生命周期结束时自动释放内存，从而避免内存泄漏和悬空指针问题。智能指针封装了普通指针，并通过C++的RAII机制，确保内存管理的安全和高效。C++标准库提供了几种常用的智能指针：

1. **`std::unique_ptr`**：独占所有权的智能指针，不允许多个指针同时管理同一块内存。
2. **`std::shared_ptr`**：引用计数智能指针，允许多个指针共享管理同一块内存，当引用计数为0时释放内存。
3. **`std::weak_ptr`**：辅助`shared_ptr`的智能指针，不影响引用计数，避免循环引用。

#### `unique_ptr`

`unique_ptr`是最简单的智能指针类型，它提供独占所有权。即一个`unique_ptr`实例拥有某块动态内存，并在其生命周期结束时释放该内存。任何时候只能有一个`unique_ptr`指向某个对象。为了保证这一点，`unique_ptr`禁止复制操作，但支持移动语义。

```
#include <iostream>
#include <memory>

int main() {

    std::unique_ptr<int> ptr1 = std::make_unique<int>(42);
    // ptr2 = ptr1; // Error: unique_ptr cannot be copied
    std::unique_ptr<int> ptr2 = std::move(ptr1); // ptr1 is now null
    std::cout << *ptr2 << std::endl;
    return 0;
}
```

#### `shared_ptr`

`shared_ptr`允许多个指针同时指向同一对象，并通过引用计数的方式管理对象的生命周期。当最后一个`shared_ptr`被销毁时，对象才会被释放。`shared_ptr`通常用于需要共享资源的场景。

```
#include <iostream>
#include <memory>

int main() {

    std::shared_ptr<int> ptr1 = std::make_shared<int>
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

  20

  点赞
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike.png)

  踩
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCollectActive.png)

  22

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
[Java应用容器化革命：Docker部署从入门到精通](https://unitymarvel.blog.csdn...
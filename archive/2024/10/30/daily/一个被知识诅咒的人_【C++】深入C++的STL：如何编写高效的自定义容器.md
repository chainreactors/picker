---
title: 【C++】深入C++的STL：如何编写高效的自定义容器
url: https://blog.csdn.net/nokiaguy/article/details/143077219
source: 一个被知识诅咒的人
date: 2024-10-30
fetch_date: 2025-10-06T18:51:20.332402
---

# 【C++】深入C++的STL：如何编写高效的自定义容器

# 【C++】深入C++的STL：如何编写高效的自定义容器

![](https://csdnimg.cn/release/blogv2/dist/pc/img/original.png)

[![](https://csdnimg.cn/release/blogv2/dist/pc/img/identityVipNew.png)](https://mall.csdn.net/vip)
[蒙娜丽宁](https://unitymarvel.blog.csdn.net "蒙娜丽宁")
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCurrentTime2.png)
于 2024-10-29 10:30:00 发布

![](https://csdnimg.cn/release/blogv2/dist/pc/img/articleReadEyes2.png)
阅读量1.9k
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)
收藏

43

![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)
点赞数
27

CC 4.0 BY-SA版权

分类专栏：
[C++杂谈](https://blog.csdn.net/nokiaguy/category_12807248.html)
文章标签：
[c++](https://so.csdn.net/so/search/s.do?q=c%2B%2B&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[开发语言](https://so.csdn.net/so/search/s.do?q=%E5%BC%80%E5%8F%91%E8%AF%AD%E8%A8%80&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

本文链接：<https://blog.csdn.net/nokiaguy/article/details/143077219>

[解锁Python编程的无限可能：《奇妙的Python》带你漫游代码世界](https://unitymarvel.blog.csdn.net/article/details/141889588?spm=1001.2014.3001.5502)

C++标准模板库（STL）提供了一系列强大的容器类，如`vector`、`list`、`map`等，这些容器极大地简化了开发工作。然而，在某些情况下，现有的STL容器无法完全满足特定需求，因此编写自定义容器就变得非常重要。本文将深入探讨STL容器的内部机制，讲解如何编写高效的自定义容器类，涵盖性能优化、迭代器实现、异常安全性等重要主题。

### 1. STL容器的基本结构

STL容器是泛型类，能够存储任意类型的对象。它们通过使用模板技术来实现通用性。STL中的容器通常包括以下几个核心部分：

* **数据存储结构**：容器内部的数据组织形式，如数组、链表或树。
* **迭代器**：用于遍历容器内元素的抽象工具，使用户可以不依赖容器的内部结构进行遍历。
* **异常安全性**：STL容器需要保证在发生异常时能够恢复到一致的状态。

理解这些核心部分是编写高效自定义容器的基础。

#### 1.1 数据存储结构

STL容器基于不同的存储结构，具有各自的性能优势。例如，`std::vector` 使用动态数组，能够提供O(1)的随机访问，而 `std::list` 则使用双向链表，擅长进行O(1)的插入和删除操作。我们在编写自定义容器时，也需要选择合适的数据结构来实现预期的性能目标。

#### 1.2 迭代器的角色

迭代器是STL容器的重要组成部分。它抽象了访问容器元素的方式，使用户可以以统一的方式遍历不同类型的容器。STL迭代器支持的功能可以通过五种类型分类：输入迭代器、输出迭代器、前向迭代器、双向迭代器和随机访问迭代器。

我们在设计自定义容器时，也需要为其定义合适的迭代器类型，以确保与STL的其他部分能够良好协作。

#### 1.3 异常安全性

STL容器必须在发生异常时保证容器内的数据不会出现不一致的状态。C++标准库中使用的“三重保证”概念是实现异常安全的重要基础。它们分别是：

1. **基本保证**：在出现异常时，保证容器内部不出现非法状态。
2. **强保证**：在操作失败时，容器恢复到操作前的状态。
3. **无失败保证**：操作绝不会失败。

自定义容器在设计时，需要考虑如何处理可能出现的异常，并确保满足一定的异常安全性标准。

### 2. 编写自定义容器的核心步骤

#### 2.1 数据存储

首先，自定义容器需要决定如何存储元素。最常见的选择是使用动态数组或链表，但也可以根据需求选择更复杂的数据结构，如树或图。以下是一个简单的动态数组容器的实现：

```
template<typename T>
class MyVector {

private:
    T* data;
    size_t size;
    size_t capacity;

    void resize() {

        capacity *= 2;
        T* newData = new T[capacity];
        for (size_t i = 0; i < size; ++i) {

            newData[i] = data[i];
        }
        delete[] data;
        data = newData;
    }

public:
    MyVector() : data(new T[1]), size(0), capacity(1) {

   }

    ~MyVector() {

        delete[] data;
    }

    void push_back(const T& value) {

        if (size == capacity) {

            resize();
        }
        data[size++] = value;
    }

    T& operator[](size_t index) {

        return data[index];
    }

    size_t getSize() const {

        return size;
    }
};
```

在这个实现中，我们采用了动态数组的方式存储数据，并提供了 `push_back` 方法来向容器末尾添加元素。在 `push_back` 方法中，当容器满时，会进行扩容操作。

#### 2.2 迭代器的实现

为了能够遍历容器内的元素，我们需要为容器实现迭代器。STL中，迭代器通常定义为嵌套类，它实现了指针语法，如`++`、`*`等操作符。以下是我们为 `MyVector` 容器实现的简单迭代器：

```
template<typename T>
class MyVector {

    // 上面的代码...

public:
    class Iterator {

    private:
        T* ptr;
    public:
        Iterator(T* p) : ptr(p) {

   }

        T& operator*() const {

    return *ptr; }
        Iterator& op
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

  27

  点赞
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike.png)

  踩
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCollectActive.png)

  43

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

[在现代软件开发中，容器化技术已成为提升应用部署效率和可移植性的关键工具。本文以“Java 与 Docker：容器化部署入门”为主题，深入探讨如何将Java应用无缝集成到Docker环境中。从Docker的基本概念和安装入手，我们将逐步引导读者构建一个简单的Java Web应用，并通过编写Dockerfile实现镜像的创建和容器的运行。文章涵盖了多阶段构建、环境变量配置、数据持久化、网络管理以及安...
---
title: 【C++】智能指针的奥秘：深度解析std::unique_ptr与std::shared_ptr
url: https://blog.csdn.net/nokiaguy/article/details/143091122
source: 一个被知识诅咒的人
date: 2024-10-31
fetch_date: 2025-10-06T18:52:37.213690
---

# 【C++】智能指针的奥秘：深度解析std::unique_ptr与std::shared_ptr

# 【C++】智能指针的奥秘：深度解析std::unique\_ptr与std::shared\_ptr

原创
[![](https://csdnimg.cn/release/blogv2/dist/pc/img/identityVipNew.png)](https://mall.csdn.net/vip)
于 2024-10-30 10:00:00 发布
·
921 阅读

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)

11

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)

25
·

CC 4.0 BY-SA版权

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

文章标签：

[#c++](https://so.csdn.net/so/search/s.do?q=c%2B%2B&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#java](https://so.csdn.net/so/search/s.do?q=java&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#jvm](https://so.csdn.net/so/search/s.do?q=jvm&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

[解锁Python编程的无限可能：《奇妙的Python》带你漫游代码世界](https://unitymarvel.blog.csdn.net/article/details/141889588?spm=1001.2014.3001.5502)

在C++中，内存管理一直是程序员面临的一个核心挑战，手动管理内存分配与释放极易导致内存泄漏和悬空指针等问题。智能指针的引入解决了这一难题。本文将深入分析C++标准库中的智能指针类型——`std::unique_ptr`和`std::shared_ptr`。我们将探讨它们的实现细节、内存管理机制、使用场景，以及如何通过正确使用这些工具来避免常见的内存管理问题。此外，本文还将对比这两种智能指针的优缺点，并举例说明如何在实际开发中选择最适合的工具，从而编写更加健壮、高效的C++程序。

### 引言

内存管理是C++编程中的一个永恒话题。在传统的C++开发中，程序员需要手动管理内存的分配与释放，这不仅复杂且容易出错。内存泄漏、悬空指针和重复释放内存等问题时常困扰开发者，尤其是在复杂的应用场景中，可能导致难以调试的bug。

为了解决这些问题，C++11标准引入了智能指针（Smart Pointers），它们可以自动管理内存，确保在不再需要对象时自动释放其占用的资源。智能指针通过RAII（Resource Acquisition Is Initialization）模式确保资源管理的正确性，极大地简化了内存管理任务。

在智能指针中，最常用的两种类型是`std::unique_ptr`和`std::shared_ptr`。`std::unique_ptr`提供了独占的所有权语义，保证一个对象在某一时刻只能由一个指针拥有；而`std::shared_ptr`则提供了共享所有权语义，允许多个指针同时拥有同一个对象。

接下来，我们将深入分析这两种智能指针的工作原理、内存管理机制，以及它们在不同场景中的最佳实践。

### 智能指针的基本概念

#### 为什么需要智能指针？

在传统的C++编程中，使用`new`和`delete`来手动管理内存。一个常见的错误是忘记释放已经分配的内存，从而导致内存泄漏。另一个常见问题是重复释放同一块内存，导致程序崩溃。

智能指针通过自动管理对象的生命周期，帮助我们避免这些问题。当智能指针超出其作用域时，它会自动调用对象的析构函数，并释放相应的内存。智能指针可以看作是指针的“包装器”，其内部封装了普通指针，并为其提供了额外的功能。

#### `std::unique_ptr`与`std::shared_ptr`的区别

1. **`std::unique_ptr`**：

   * `std::unique_ptr`是一种独占所有权的智能指针。它确保一个对象在某一时刻只能有一个指针拥有，不能被复制。
   * 当`std::unique_ptr`超出作用域时，指向的对象会被自动释放。
   * 可以通过`std::move`将所有权转移给另一个`std::unique_ptr`，但不能直接复制它。
2. **`std::shared_ptr`**：

   * `std::shared_ptr`是一种共享所有权的智能指针，多个`std::shared_ptr`可以同时指向同一个对象。
   * 它通过引用计数机制（Reference Counting）管理对象的生命周期，当最后一个`std::shared_ptr`销毁时，对象的内存才会被释放。
   * `std::shared_ptr`可以被复制，因此适用于多个部分需要共享对象的场景。

### `std::unique_ptr`的实现与使用

#### 基本使用

`std::unique_ptr`的主要特点是独占所有权，这意味着一个对象在任何时刻只能被一个`unique_ptr`实例拥有。以下是一个简单的示例：

```
#include <iostream>
#include <memory>

int main() {

    std::unique_ptr<int> ptr = std::make_unique<int>(10);
    std::cout << "Value: " << *ptr << std::endl;

    // 错误: 无法复制 unique_ptr
    // std::unique_ptr<int> ptr2 = ptr;

    // 正确: 使用 std::move 转移所有权
    std::unique_ptr<int> ptr2 = std::move(ptr);

    if (!ptr) {

        std::cout << "ptr 已被转移" << std::endl;
    }
    std::cout << "ptr2 拥有的值: " << *ptr2 << std::endl;

    return 0;
}
```

在这个示例中，`std::unique_ptr<int> ptr`拥有一个动态分配的整数`10`。我们尝试将其复制到另一个`unique_ptr`时，编译器会报错，因为`unique_ptr`不允许复制。要转移所有权，必须使用`std::move`。

#### `std::unique_ptr`的实现细节

`std::unique_ptr`的实现相对简单，它通过禁用复制构造函数和复制赋值运算符来保证独占所有权。以下是它的部分简化实现：

```
template <typename T>
class unique_ptr {

private:
    T* ptr;  // 内部裸指针

public:
    // 构造函数
    explicit unique_ptr(T* p = nullptr) : ptr(p) {

   }

    // 禁用复制
    unique_ptr(const unique_ptr&) = delete;
    unique_ptr& operator=(const unique_ptr&) = delete;

    // 允许移动
    unique_ptr(unique_ptr&& other) noexcept : ptr(other.ptr) {

        other.ptr = nullptr;
    }

    unique_ptr& operator=(unique_ptr&& other) noexcept {

        if (this != &other) {

            delete ptr;
            ptr = other.ptr
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

  11

  点赞
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike.png)

  踩
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCollectActive.png)

  25

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
![](https://csdnimg.cn/release/blogv2/d...
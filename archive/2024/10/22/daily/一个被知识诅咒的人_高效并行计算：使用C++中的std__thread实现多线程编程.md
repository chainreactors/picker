---
title: 高效并行计算：使用C++中的std::thread实现多线程编程
url: https://blog.csdn.net/nokiaguy/article/details/142945161
source: 一个被知识诅咒的人
date: 2024-10-22
fetch_date: 2025-10-06T18:50:11.272076
---

# 高效并行计算：使用C++中的std::thread实现多线程编程

# 高效并行计算：使用C++中的std::thread实现多线程编程

![](https://i-operation.csdnimg.cn/images/cf31225e169b4512917b2e77694eb0a2.png)C++ std::thread实现多线程并行计算

![](https://csdnimg.cn/release/blogv2/dist/pc/img/original.png)

[![](https://csdnimg.cn/release/blogv2/dist/pc/img/identityVipNew.png)](https://mall.csdn.net/vip)
[蒙娜丽宁](https://unitymarvel.blog.csdn.net "蒙娜丽宁")
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCurrentTime2.png)
于 2024-10-21 10:00:00 发布

![](https://csdnimg.cn/release/blogv2/dist/pc/img/articleReadEyes2.png)
阅读量1k
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)
收藏

11

![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)
点赞数
22

CC 4.0 BY-SA版权

分类专栏：
[C/C++](https://blog.csdn.net/nokiaguy/category_606047.html)
[C++杂谈](https://blog.csdn.net/nokiaguy/category_12807248.html)
文章标签：
[c++](https://so.csdn.net/so/search/s.do?q=c%2B%2B&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[java](https://so.csdn.net/so/search/s.do?q=java&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[开发语言](https://so.csdn.net/so/search/s.do?q=%E5%BC%80%E5%8F%91%E8%AF%AD%E8%A8%80&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

本文链接：<https://blog.csdn.net/nokiaguy/article/details/142945161>

[解锁Python编程的无限可能：《奇妙的Python》带你漫游代码世界](https://unitymarvel.blog.csdn.net/article/details/141889588?spm=1001.2014.3001.5502)

在现代计算中，随着多核处理器的普及，如何充分利用硬件资源以提升程序性能成为关键问题之一。C++标准库提供了丰富的多线程支持，其中`std::thread`是用于实现并发计算的核心工具之一。通过合理的多线程设计，程序可以实现并行计算，显著缩短任务执行时间。本文将详细讨论如何在C++中使用`std::thread`进行多线程编程，涵盖线程的创建、同步、资源共享、数据竞争问题等关键内容，并通过代码示例演示如何通过并行计算提升性能。最终，我们将分析多线程编程中的性能调优和最佳实践。

---

### 目录

1. 引言
2. 多线程与并行计算的基础知识
   * 什么是多线程
   * 并行计算的优势
3. 使用`std::thread`实现C++中的多线程
   * `std::thread`的基本用法
   * 创建线程并传递参数
   * 主线程与子线程的协调
4. 线程同步与共享资源
   * 数据竞争与临界区问题
   * 使用`std::mutex`进行锁机制
   * 线程间的条件变量`std::condition_variable`
5. 实践：通过多线程实现并行计算
   * 并行矩阵乘法的实现
   * 多线程文件处理
6. 性能优化与多线程调优
   * 线程数量的合理选择
   * 避免不必要的上下文切换
7. 最佳实践与常见陷阱
   * 死锁问题与避免方法
   * 多线程调试技巧
8. 总结

---

### 1. 引言

随着处理器的多核化，单线程程序的性能已无法充分利用现代硬件的优势。因此，并行计算变得越来越重要。通过将程序中的任务拆分成多个独立的部分，并在多个CPU核心上同时执行，程序的执行时间可以显著缩短。C++11引入了多线程支持，使得开发者能够更方便地编写并发程序。本文将深入介绍C++标准库中的`std::thread`类，以及如何利用它来实现高效的并行计算。

---

### 2. 多线程与并行计算的基础知识

#### 什么是多线程

多线程是一种并发执行的编程方式，允许程序在同一时间执行多个线程。每个线程可以被看作是一个独立的任务，它们共享同一个进程的内存空间。多线程的出现使得程序能够利用多核处理器的优势，从而加速任务的执行。

在C++中，多线程的主要优势包括：

* **并行执行**：多个线程可以同时运行，提升程序效率。
* **响应性提高**：尤其在GUI应用中，主线程处理用户交互，后台线程执行繁重计算。
* **任务解耦**：复杂任务可以被分解为多个子任务，分配给不同的线程执行。

#### 并行计算的优势

并行计算的核心思想是将大的计算任务分成若干个小任务，并在多个处理器核心上并行运行。相比传统的串行执行，合理使用多线程可以显著减少任务的完成时间。例如，矩阵乘法、文件处理、图像处理等计算密集型任务在并行化后可以得到大幅度的性能提升。

---

### 3. 使用`std::thread`实现C++中的多线程

C++11引入了`std::thread`类，开发者可以方便地在C++程序中创建并管理线程。`std::thread`封装了POSIX线程库，使得跨平台的多线程开发更加容易。

#### `std::thread`的基本用法

创建线程的最基本方法是使用`std::thread`类，传入可调用对象（函数、lambda表达式或类的成员函数）。以下是一个简单的示例，展示了如何使用`std::thread`创建和启动新线程。

**示例：简单的多线程程序**

```
#include <iostream>
#include <thread>

void threadFunction() {

    std::cout << "Hello from thread!" << std::endl;
}

int main() {

    std::thread t(threadFunction);  // 创建一个新线程
    t.join();  // 等待线程t完成
    std::cout << "Hello from main!" << std::endl;
    return 0;
}
```

在这个例子中，`std::thread`被用来创建一个新的线程，该线程执行`threadFunction`函数。同时，主线程继续执行自己的逻辑，直到`join()`语句阻塞主线程等待子线程完成。

#### 创建线程并传递参数

有时我们希望线程执行的函数能够接收参数。`std::thread`支持通过构造函数传递参数给线程函数。

**示例：传递参数给线程函数**

```
#include <iostream>
#include <thread>

void threadFunction(int x) {

    std::cout << "Thread function received value: " << x << std::endl;
}

int main() {

    int value = 42;
    std::thread t(threadFunction, value);  // 传递参数给线程
    t.join();  // 等待线程结束
    return 0;
}
```

在这个例子中，`threadFunction`函数接收一个整数参数`x`，并打印其值。主线程将`value`传递给子线程。

#### 主线程与子线程的协调

当主线程希望等待子线程完成工作时，可以使用`join()`函数。`join()`会阻塞主线程，直到子线程执行完毕。如果不调用`join()`，主线程可能会提前退出，从而导致子线程未完成任务。

```
std::thread t(function);
t.join();  // 主线程等待子线程结束
```

此外，如果不需要等待子线程完成，主线程可以使用`detach()`函数将子线程与主线程分离，这样子线程可以在后台独立运行：

```
std::thread t(function
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

  22

  点赞
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike.png)

  踩
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCollectActive.png)

  11

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

[摘要：2025年机器人产业正经历技术驱动的深度变革，AI初创企业通过创新算法和低成本方案挑战传统巨头。本文剖析产业洗牌动因，包括AI融合、融资热潮和应用场景扩展，重...
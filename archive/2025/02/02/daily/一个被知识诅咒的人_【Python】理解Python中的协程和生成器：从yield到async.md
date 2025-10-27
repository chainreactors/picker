---
title: 【Python】理解Python中的协程和生成器：从yield到async
url: https://blog.csdn.net/nokiaguy/article/details/145412058
source: 一个被知识诅咒的人
date: 2025-02-02
fetch_date: 2025-10-06T20:35:54.153149
---

# 【Python】理解Python中的协程和生成器：从yield到async

# 【Python】理解Python中的协程和生成器：从yield到async

原创
[![](https://csdnimg.cn/release/blogv2/dist/pc/img/identityVipNew.png)](https://mall.csdn.net/vip)
于 2025-02-01 13:12:52 发布
·
956 阅读

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)

26

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)

10
·

CC 4.0 BY-SA版权

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

文章标签：

[#python](https://so.csdn.net/so/search/s.do?q=python&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#开发语言](https://so.csdn.net/so/search/s.do?q=%E5%BC%80%E5%8F%91%E8%AF%AD%E8%A8%80&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

[《Python OpenCV从菜鸟到高手》带你进入图像处理与计算机视觉的大门！](https://blog.csdn.net/nokiaguy/article/details/143574491)

[解锁Python编程的无限可能：《奇妙的Python》带你漫游代码世界](https://unitymarvel.blog.csdn.net/article/details/141889588)

在现代编程中，异步编程成为提升程序性能和响应速度的重要手段。Python作为一门功能强大的编程语言，提供了丰富的工具来实现异步操作，其中协程和生成器是核心概念。本文将深入探讨Python中协程和生成器的实现方式，从基础的`yield`语句入手，逐步引导读者理解生成器的工作机制，进而介绍如何将生成器转换为协程。通过详细的代码示例和中文注释，本文不仅阐明了协程与生成器的概念，还展示了它们在实际开发中的应用场景。此外，文章还将介绍Python 3.5引入的`async`和`await`关键字，解析其背后的原理与优势。无论是初学者还是有经验的开发者，本文都将帮助读者全面掌握Python中的协程与生成器，提升编程效率与代码质量。

---

### 目录

1. [引言](#%E5%BC%95%E8%A8%80)
2. [生成器的基础](#%E7%94%9F%E6%88%90%E5%99%A8%E7%9A%84%E5%9F%BA%E7%A1%80)
   * 什么是生成器
   * `yield`的使用
   * 生成器的优势
3. [生成器的高级特性](#%E7%94%9F%E6%88%90%E5%99%A8%E7%9A%84%E9%AB%98%E7%BA%A7%E7%89%B9%E6%80%A7)
   * 生成器的`send`方法
   * 生成器的`throw`方法
   * 生成器的`close`方法
4. [协程的基础](#%E5%8D%8F%E7%A8%8B%E7%9A%84%E5%9F%BA%E7%A1%80)
   * 什么是协程
   * 协程与线程的区别
   * 协程的优点
5. [从生成器到协程](#%E4%BB%8E%E7%94%9F%E6%88%90%E5%99%A8%E5%88%B0%E5%8D%8F%E7%A8%8B)
   * 生成器作为协程的基础
   * 协程的调度与管理
6. [Python中的`async`和`await`](#python%E4%B8%AD%E7%9A%84async%E5%92%8Cawait)
   * `async`的使用
   * `await`的使用
   * `async`与`await`的工作原理
7. [异步编程的应用场景](#%E5%BC%82%E6%AD%A5%E7%BC%96%E7%A8%8B%E7%9A%84%E5%BA%94%E7%94%A8%E5%9C%BA%E6%99%AF)
   * I/O密集型任务
   * 高并发网络服务
   * 实时数据处理
8. [实践案例](#%E5%AE%9E%E8%B7%B5%E6%A1%88%E4%BE%8B)
   * 使用生成器实现简单的协程
   * 使用`async`和`await`构建异步HTTP请求
   * 比较生成器协程与`async`协程的性能
9. [常见问题与解决方案](#%E5%B8%B8%E8%A7%81%E9%97%AE%E9%A2%98%E4%B8%8E%E8%A7%A3%E5%86%B3%E6%96%B9%E6%A1%88)
10. [结论](#%E7%BB%93%E8%AE%BA)
11. [参考文献](#%E5%8F%82%E8%80%83%E6%96%87%E7%8C%AE)

---

### 引言

随着互联网和分布式系统的迅猛发展，应用程序需要处理大量的并发任务和高频率的I/O操作。传统的同步编程模型在面对这些需求时，往往表现出性能瓶颈，难以高效利用系统资源。为了应对这些挑战，异步编程应运而生，成为提升程序性能和响应速度的重要手段。

在Python中，生成器（Generator）和协程（Coroutine）是实现异步编程的两大关键概念。生成器通过`yield`语句实现延迟计算和数据流的生成，而协程则提供了一种更加灵活和高效的方式来管理并发任务。自Python 3.5引入`async`和`await`关键字以来，协程的使用变得更加便捷和强大。

本文旨在系统地介绍Python中的生成器与协程，深入解析它们的工作原理、实现方式以及在实际开发中的应用。通过详细的代码示例和丰富的中文注释，本文将帮助读者全面掌握协程与生成器的使用方法，提升编程效率与代码质量。

### 生成器的基础

#### 什么是生成器

生成器（Generator）是Python中一种用于创建迭代器的简单而强大的工具。与普通函数不同，生成器使用`yield`语句返回数据，每次调用时会记住上一次的执行状态，从而能够逐步生成数据。这种特性使得生成器在处理大量数据或无限数据流时，表现出极高的效率和灵活性。

生成器的核心在于其能够暂停和恢复执行，这通过`yield`语句实现。当生成器函数执行到`yield`时，会将值返回给调用者，并冻结当前的执行状态，等待下一次调用继续执行。

#### `yield`的使用

`yield`是生成器的关键字，用于在函数内部返回一个值，并暂停函数的执行。每次调用生成器的`__next__()`方法时，函数会从上一次暂停的地方继续执行，直到遇到下一个`yield`语句或函数结束。

以下是一个简单的生成器示例：

```
# 定义一个生成器函数，生成斐波那契数列
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# 创建生成器对象
fib = fibonacci(10)

# 使用for循环遍历生成器
for num in fib:
    print(num)
```

**输出：**

```
0
1
1
2
3
5
8
13
21
34
```

在上述代码中，`fibonacci`函数是一个生成器函数，它使用`yield`语句逐步生成斐波那契数列。每次调用`__next__()`方法时，生成器会返回下一个斐波那契数。

#### 生成器的优势

生成器相比于普通函数和列表推导式，具有以下几个显著优势：

1. **内存效率高**：生成器按需生成数据，不需要一次性将所有数据存储在内存中，适合处理大型数据集或无限数据流。
2. **惰性求值**：生成器在每次迭代时才生成下一个值，避免了不必要的计算，提高了程序的性能。
3. **简洁的语法**：使用`yield`语句，生成器代码更为简洁，易于理解和维护。
4. **支持协作式多任务**：生成器可以在执行过程中暂停，配合`send`等方法，实现协作式的多任务处理。

### 生成器的高级特性

在理解了生成器的基本用法后，进一步探讨其高级特性，可以更好地利用生成器的强大功能。

#### 生成器的`send`方法

生成器不仅可以用来生成值，还可以接收外部传入的值。通过`send`方法，可以向生成器发送数据，并在生成器内部使用这些数据。

以下是一个使用`send`方法的示例：

```
# 定义一个生成器，接收外部发送的数据
def echo():
    while True:
        received = yield
        print(f"Received: {

     received}")

# 创建生成器对象
generator = echo()

# 启动生成器
next(generator)

# 发送数据到生成器
generator.send("Hello")
generator.send("World")
generator.send(123)
```

**输出：**

```
Received: Hello
Received: World
Received: 123
```

在这个示例中，`echo`生成器在每次`yield`后等待接收数据，通过`generator.send()`方法将数据发送到生成器，并在生成器内部打印接收到的数据。

#### 生成器的`throw`方法

`throw`方法允许向生成器抛出一个异常，这在生成器内部进行异常处理时非常有用。

以下是一个使用`throw`方法的示例：

```
# 定义一个生成器，处理异常
def divide():
    while True:
        try:
            x = yield
            result = 10 / x
            print(f"10 / {

     x} = {

     result}")
        except ZeroDivisionError:
            print("除数不能为零！")

# 创建生成器对象
gen = divide()

# 启动生成器
next(gen)

# 发送有效数据
gen.send(2)

# 发送导致除零的值
gen.send(0)

# 发送另一个有效数据
gen.send(5)
```

**输出：**

```
10 / 2 = 5.0
除数不能为零！
10 / 5 = 2.0
```

在上述代码中，`divide`生成器通过`try-except`块捕获`ZeroDivisionError`异常。当发送`0`作为除数时，生成器捕获到异常并打印错误信息，而不会导致程序崩溃。

#### 生成器的`close`方法

`close`方法用于关闭生成器，导致生成器抛出一个`GeneratorExit`异常，从而终止生成器的执行。

以下是一个使用`close`方法的示例：

```
# 定义一个生成器，处理生成器关闭
def generator_example():
    try:
        while True:
            x = yield
            print
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

  26

  点赞
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike.png)

  踩
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCollectActive.png)

  10

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

[《Python OpenCV从菜鸟到高手》是一本深入探讨Python与OpenCV技术的图像处理教程。从Python的基础知识到OpenCV的强大功能，这本书带领读者逐步掌握计算机视觉的核心技术。Python因其简洁和强大的库生态被广泛应用于数据分析、人工智能等领域，而OpenCV则是图像处理与...
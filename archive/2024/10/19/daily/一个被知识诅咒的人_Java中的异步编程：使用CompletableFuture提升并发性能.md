---
title: Java中的异步编程：使用CompletableFuture提升并发性能
url: https://blog.csdn.net/nokiaguy/article/details/142886856
source: 一个被知识诅咒的人
date: 2024-10-19
fetch_date: 2025-10-06T18:51:25.261955
---

# Java中的异步编程：使用CompletableFuture提升并发性能

# Java中的异步编程：使用CompletableFuture提升并发性能

![](https://i-operation.csdnimg.cn/images/cf31225e169b4512917b2e77694eb0a2.png)Java使用CompletableFuture提升并发性能

![](https://csdnimg.cn/release/blogv2/dist/pc/img/original.png)

[![](https://csdnimg.cn/release/blogv2/dist/pc/img/identityVipNew.png)](https://mall.csdn.net/vip)
[蒙娜丽宁](https://unitymarvel.blog.csdn.net "蒙娜丽宁")
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCurrentTime2.png)
于 2024-10-18 10:30:00 发布

![](https://csdnimg.cn/release/blogv2/dist/pc/img/articleReadEyes2.png)
阅读量1.6k
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)
收藏

21

![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)
点赞数
38

CC 4.0 BY-SA版权

分类专栏：
[Java杂谈](https://blog.csdn.net/nokiaguy/category_12806115.html)
文章标签：
[java](https://so.csdn.net/so/search/s.do?q=java&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[python](https://so.csdn.net/so/search/s.do?q=python&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[数据库](https://so.csdn.net/so/search/s.do?q=%E6%95%B0%E6%8D%AE%E5%BA%93&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

本文链接：<https://blog.csdn.net/nokiaguy/article/details/142886856>

[解锁Python编程的无限可能：《奇妙的Python》带你漫游代码世界](https://unitymarvel.blog.csdn.net/article/details/141889588?spm=1001.2014.3001.5502)

### 引言

在现代应用程序中，响应速度和并发性能变得越来越重要。随着处理任务变得复杂，应用程序常常需要同时处理多个任务，这对系统资源和性能提出了严峻的挑战。在传统的阻塞式编程模型中，线程等待任务完成往往会导致资源浪费，影响整体的并发能力和响应速度。

为了应对这些挑战，Java 8引入了**CompletableFuture**，这是一种灵活的异步编程工具，它允许我们轻松实现并行任务处理，避免线程阻塞，从而提升系统的并发性能。本文将深入探讨如何使用`CompletableFuture`及其相关工具进行异步编程，通过丰富的代码示例展示它在提升并发性能中的强大能力。

#### 目录

1. 异步编程的意义
2. Java中的Future接口概述
3. CompletableFuture简介
4. 使用CompletableFuture进行异步计算
5. 组合多个异步任务
6. 处理异步任务的结果
7. 异常处理与恢复
8. 自定义Executor提升性能
9. 实践中的异步编程案例
10. 总结

---

### 1. 异步编程的意义

**异步编程**是指在处理任务时，程序可以不必等待任务的完成，允许其他任务继续执行。这种模式在处理IO操作、网络请求、文件读写等耗时任务时，尤为重要。通过异步编程，我们可以避免不必要的线程阻塞，提升系统的整体效率。

传统的阻塞式编程模式，例如使用`Thread.sleep()`等待任务完成，通常会导致CPU空转，浪费了宝贵的系统资源。而异步编程通过回调机制、事件驱动或任务组合，能够让CPU充分利用时间，处理其他任务，从而提升并发性能。

---

### 2. Java中的Future接口概述

在Java 5中，引入了`Future`接口，用于表示异步计算的结果。`Future`可以让我们启动一个异步任务并返回一个表示结果的对象。我们可以通过调用`get()`方法来获取异步任务的结果。

```
ExecutorService executor = Executors.newSingleThreadExecutor();
Future<Integer> future = executor.submit(() -> {

    Thread.sleep(1000);
    return 42;
});
System.out.println(future.get()); // 阻塞直到任务完成
```

虽然`Future`提供了一种异步计算的方式，但它有几个局限性：

* **阻塞获取结果**：`future.get()`方法是阻塞的，必须等待任务完成才能继续。
* **无法主动取消任务**：`Future`的取消操作依赖于任务的执行状态。
* **任务组合困难**：多个`Future`的结果组合较为繁琐。

为了解决这些问题，Java 8引入了更为强大的`CompletableFuture`。

---

### 3. CompletableFuture简介

**CompletableFuture** 是 Java 8 中新增的类，扩展了`Future`接口，提供了更丰富的功能。它不仅允许非阻塞地获取异步计算的结果，还支持任务的组合、链式调用和异常处理。此外，`CompletableFuture` 内部结合了`ForkJoinPool`，实现了高效的线程管理。

#### CompletableFuture 的核心方法

| 方法 | 描述 |
| --- | --- |
| `supplyAsync` | 异步地执行一个供应函数并返回结果。 |
| `thenApply` | 在异步任务完成后，对结果进行转换。 |
| `thenAccept` | 异步任务完成后，对结果执行某个操作（无返回值）。 |
| `thenCombine` | 组合两个异步任务的结果。 |
| `exceptionally` | 处理异步任务中的异常情况。 |
| `complete` | 手动完成任务并提供结果。 |
| `join` | 阻塞地获取异步任务的结果，但不抛出`InterruptedException`。 |

---

### 4. 使用CompletableFuture进行异步计算

在实际开发中，我们经常需要执行异步任务并获取结果。`CompletableFuture`允许我们在不阻塞主线程的情况下执行耗时操作，例如网络请求或文件读写。我们可以通过`CompletableFuture.supplyAsync`方法来启动异步任务。

#### 4.1 基本示例

以下是一个简单的异步计算示例，它模拟了一个耗时的计算任务，并在任务完成后获取结果。

```
import java.util.concurrent.CompletableFuture;
import java.util.concurrent.ExecutionException;

public class AsyncExample {

    public static void main(String[] args) throws ExecutionException, InterruptedException {

        // 启动异步任务
        CompletableFuture<Integer> future = CompletableFuture.supplyAsync(() -> {

            try {

                Thread.sleep(1000);  // 模拟耗时任务
            } catch (InterruptedException e) {

                e.printStackTrace();
            }
            return 42;
        });

        // 获取异步任务结果
        System.out.println("计算结果: " + future.get());  // 阻塞获取结果
    }
}
```

#### 4.2 非阻塞获取结果

使用`get()`方法会阻塞当前线程，直到异步任务完成。为了实现真正的异步效果，我们可以使用`thenAccept()`方法，在任务完成时处理结果，而不阻塞主线程。

```
CompletableFuture<Integer> future = CompletableFuture.supplyAsync(() -> {

    try {

        Thread.sleep(
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

  38

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
[2025机器人产业大洗牌：新兴初创企业的技术革命与崛起之路](https://unitymarvel.blog.c...
---
title: Java高效编程（8）：避免使用终结器和清理器
url: https://blog.csdn.net/nokiaguy/article/details/142620469
source: 一个被知识诅咒的人
date: 2024-10-02
fetch_date: 2025-10-06T18:53:42.699681
---

# Java高效编程（8）：避免使用终结器和清理器

# Java高效编程（8）：避免使用终结器和清理器

![](https://csdnimg.cn/release/blogv2/dist/pc/img/original.png)

[蒙娜丽宁](https://unitymarvel.blog.csdn.net "蒙娜丽宁")
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCurrentTime2.png)
于 2024-10-01 10:00:00 发布

![](https://csdnimg.cn/release/blogv2/dist/pc/img/articleReadEyes2.png)
阅读量851
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)
收藏

11

![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)
点赞数
17

CC 4.0 BY-SA版权

分类专栏：
[Java高效编程](https://blog.csdn.net/nokiaguy/category_12795365.html)
文章标签：
[java](https://so.csdn.net/so/search/s.do?q=java&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[开发语言](https://so.csdn.net/so/search/s.do?q=%E5%BC%80%E5%8F%91%E8%AF%AD%E8%A8%80&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

本文链接：<https://blog.csdn.net/nokiaguy/article/details/142620469>

[![](https://i-blog.csdnimg.cn/columns/default/20201014180756928.png?x-oss-process=image/resize,m_fixed,h_224,w_224)

Java高效编程
专栏收录该内容](https://blog.csdn.net/nokiaguy/category_12795365.html "Java高效编程")

19 篇文章

订阅专栏

[解锁Python编程的无限可能：《奇妙的Python》带你漫游代码世界](https://unitymarvel.blog.csdn.net/article/details/141889588?spm=1001.2014.3001.5502)

终结器（finalizers）是不可预测的，通常危险且不必要的。使用它们可能导致程序不稳定的行为、性能下降以及跨平台的兼容性问题。虽然终结器在某些情况下确实有用，但一般应尽量避免使用。自Java 9以来，终结器已被标记为废弃，取而代之的是清理器（cleaners）。虽然清理器相对更安全，但它们依然不可靠，且性能较差。因此，清理器也应当谨慎使用。

#### 终结器与清理器的局限性

C++程序员可能会将终结器和清理器误解为Java的析构函数（destructor），但这种理解是不正确的。在C++中，析构函数是释放对象相关资源的常规方式，构成了与构造函数对称的操作。而在Java中，垃圾回收器会自动处理对象的内存回收，程序员不需要像在C++中那样手动释放内存资源。对于Java中的非内存资源（如文件、网络连接等），通常使用 `try-with-resources` 或 `try-finally` 语句来管理资源的生命周期（详见【条目9】）。

终结器和清理器的主要问题之一在于，它们的执行时间不可预测。对象变为不可达到终结器或清理器执行之间的时间可能是任意长的。这意味着不应该将任何时间敏感的操作放在终结器或清理器中。比如，依赖终结器或清理器关闭文件是一种严重错误，因为文件描述符是有限的资源。如果系统无法及时回收这些资源，程序可能会因为无法再打开文件而崩溃。

终结器和清理器的执行依赖于垃圾回收器的调度策略，而不同的JVM实现可能使用不同的垃圾回收算法，这使得依赖终结器或清理器执行时间的程序行为难以保证一致性。例如，程序可能在开发环境中运行良好，但在生产环境中，由于垃圾回收器的行为不同，可能表现出完全不同的结果。

#### 终结器的具体问题

终结器的另一个问题是，它们可能延迟对象的回收。为类提供终结器会导致实例的回收被任意延迟。我的一位同事曾遇到一个长期运行的GUI应用程序，在运行过程中频繁抛出 `OutOfMemoryError`。经过分析，发现当程序崩溃时，成千上万的图形对象正在终结器队列中等待回收，导致内存耗尽。更糟糕的是，终结器线程的优先级较低，导致终结器执行速度远低于对象生成的速度。语言规范并不保证终结器由哪个线程执行，因此无可移植的方式可以防止此类问题。相比之下，清理器稍微好一些，因为类的作者可以控制清理器的线程，但清理器依然是在后台运行，无法保证清理的及时性。

更严重的是，Java语言规范没有保证终结器或清理器会在对象不可达时一定被执行，甚至可能永远不会执行。因此，依赖终结器或清理器来更新持久化状态是非常危险的。例如，依赖终结器或清理器来释放共享资源（如数据库的锁）可能导致整个分布式系统停滞。

#### 性能与安全问题

使用终结器或清理器还会带来严重的性能损失。在我的机器上，创建一个简单的 `AutoCloseable` 对象并通过 `try-with-resources` 关闭它的耗时约为12纳秒。而使用终结器处理对象则耗时550纳秒，足足慢了50倍。这是因为终结器会阻碍垃圾回收的高效运行。清理器的性能与终结器相当，但如果仅作为安全网使用，清理器的开销会稍小一些。在这种情况下，创建、清理和销毁一个对象的时间约为66纳秒，虽然依然比不使用清理器要慢5倍，但相比终结器要快得多。

除此之外，终结器还会带来一个潜在的安全问题——终结器攻击。攻击者可以通过抛出异常使构造函数或反序列化方法（如 `readObject` 或 `readResolve`）未能正常结束，从而在对象应被销毁时调用终结器，恢复该对象并执行恶意代码。如果一个类是 `final` 的，那么它免疫终结器攻击；但对于非 `final` 类，防止此类攻击的方式是定义一个 `final finalize` 方法，且该方法不做任何操作。

#### 使用AutoCloseable替代终结器

那么，当一个类封装了需要显式释放的资源（如文件、线程）时，应该怎么做呢？最好的解决方案是实现 `AutoCloseable` 接口，并要求用户在不再需要该对象时调用 `close` 方法。通常，用户可以使用 `try-with-resources` 来保证资源的释放，即使在异常情况下也能正常执行 `close`。此外，`close` 方法应记录对象已关闭的状态，确保在对象关闭后调用其他方法时抛出 `IllegalStateException` 异常。

#### 清理器的作用与示例

尽管如此，清理器并非完全无用。它们的主要作用有两种：一是作为安全网，防止客户端忘记调用 `close` 方法。虽然清理器的执行时间不确定，但如果客户端未能关闭资源，迟到的清理总比永不清理要好。Java库中的一些类（如 `FileInputStream` 和 `ThreadPoolExecutor`）就使用了终结器作为这种安全网。

二是用于处理本地对象（native peers）。本地对象是通过Java调用本地方法关联的非Java对象。因为垃圾回收器无法感知本地对象的存在，因此无法自动回收它们。此时，清理器可以用于释放这些本地资源。

下面是一个简单的 `Room` 类示例，演示了如何使用清理器作为安全网。假设房间在回收之前需要清理：

```
// 使用清理器的可自动关闭类
public class Room implements AutoCloseable {
    private static final Cleaner cleaner = Cleaner.create();

    private static class State implements Runnable {
        int numJunkPiles;

        State(int numJunkPiles) {
            this.numJunkPiles = numJunkPiles;
        }

        @Override
        public void run() {
            System.out.println("清理房间");
            numJunkPiles = 0;
        }
    }

    private final State state;
    private final Cleaner.Cleanable cleanable;

    public Room(int numJunkPiles) {
        state = new State(numJunkPiles);
        cleanable = cleaner.register(this, state);
    }

    @Override
    public void close() {
        cleanable.clean();
    }
}
```

在此示例中，`Room` 实现了 `AutoCloseable`，并使用了清理器作为安全网。如果用户未调用 `close` 方法，清理器会在房间对象被垃圾回收时自动执行清理工作。不过，如果用户在 `try-with-resources` 中使用 `Room`，那么清理器永远不会被触发。

```
// 良好使用的示例
public class Adult {
    public static void main(String[] args) {
        try (Room myRoom = new Room(7)) {
            System.out.println("Goodbye");
        }
    }
}
```

运行该程序后，输出为：

```
Goodbye
Cleaning room
```

但如果程序没有显式调用 `close` 方法，清理器的行为就不确定了。例如：

```
// 错误使用的示例
public class Teenager {
    public static void main(String[] args) {
        new Room(99);
        System.out.println("Peace out");
    }
}
```

在这段代码中，由于未使用 `try-with-resources` 或 `close` 方法，清理器可能永远不会运行。输出可能只是：

```
Peace out
```

要使清理器在程序结束时运行，可能需要调用 `System.gc()`，但即便如此，清理器的执行仍然依赖于具体的JVM实现，无法保证跨平台的一致性。

#### 总结

终结器和清理器不应当作为资源管理的常规手段使用，除非作为安全网或用于释放非关键的本地资源。即便如此，也要警惕其不可预测性和性能开销。对于需要显式管理资源的类，推荐使用 `AutoCloseable` 接口和 `try-with-resources` 语句，这样可以确保资源被及时释放，避免不必要的资源泄露和安全问题。

---

关注博主即可阅读全文
![](https://csdnimg.cn/release/blogv2/dist/pc/img/arrowDownAttend.png)

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

  17

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

[《Python OpenCV从菜鸟到高手》是一本深入探讨Python与OpenCV技术的图像处理教程。从Python的基础知识到O...
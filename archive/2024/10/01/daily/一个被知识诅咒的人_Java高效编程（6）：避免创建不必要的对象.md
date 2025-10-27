---
title: Java高效编程（6）：避免创建不必要的对象
url: https://blog.csdn.net/nokiaguy/article/details/142620132
source: 一个被知识诅咒的人
date: 2024-10-01
fetch_date: 2025-10-06T18:49:35.966388
---

# Java高效编程（6）：避免创建不必要的对象

# Java高效编程（6）：避免创建不必要的对象

![](https://csdnimg.cn/release/blogv2/dist/pc/img/original.png)

[蒙娜丽宁](https://unitymarvel.blog.csdn.net "蒙娜丽宁")
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCurrentTime2.png)
于 2024-09-30 10:00:00 发布

![](https://csdnimg.cn/release/blogv2/dist/pc/img/articleReadEyes2.png)
阅读量1k
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)
收藏

20

![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)
点赞数
30

CC 4.0 BY-SA版权

分类专栏：
[Java高效编程](https://blog.csdn.net/nokiaguy/category_12795365.html)
文章标签：
[java](https://so.csdn.net/so/search/s.do?q=java&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[ajax](https://so.csdn.net/so/search/s.do?q=ajax&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[开发语言](https://so.csdn.net/so/search/s.do?q=%E5%BC%80%E5%8F%91%E8%AF%AD%E8%A8%80&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

本文链接：<https://blog.csdn.net/nokiaguy/article/details/142620132>

[![](https://i-blog.csdnimg.cn/columns/default/20201014180756928.png?x-oss-process=image/resize,m_fixed,h_224,w_224)

Java高效编程
专栏收录该内容](https://blog.csdn.net/nokiaguy/category_12795365.html "Java高效编程")

19 篇文章

订阅专栏

[解锁Python编程的无限可能：《奇妙的Python》带你漫游代码世界](https://unitymarvel.blog.csdn.net/article/details/141889588?spm=1001.2014.3001.5502)

在开发中，尽量复用已经存在的对象，而不是每次都创建一个功能等价的新对象。对象复用不仅速度更快，也显得更加优雅。尤其是对于不可变对象，可以始终安全地复用（详见【条目17】）。举一个极端的反例：

```
String s = new String("bikini"); // 不要这样做！
```

这种写法每次执行时都会创建一个新的 `String` 实例，而其实完全没有必要。字符串字面量 `"bikini"` 本身已经是一个 `String` 实例，它与构造函数生成的对象功能上完全相同。如果这种代码出现在循环或频繁调用的方法中，可能会无端创建成千上万的 `String` 对象，浪费资源。改进后的代码如下：

```
String s = "bikini";
```

此版本只使用了一个 `String` 实例，且在同一虚拟机中任何包含相同字面量的代码都会重用该对象，从而避免不必要的对象创建。

#### 静态工厂方法的优势

在使用不可变类时，优先选择静态工厂方法（详见【条目1】），可以进一步避免创建不必要的对象。例如，`Boolean.valueOf(String)` 比 `Boolean(String)` 构造函数更优，因为后者每次都会创建一个新对象，而前者可以选择复用已有的实例。实际上，Java 9 中已将 `Boolean(String)` 构造函数废弃。

除了不可变对象，某些可变对象在确保不会被修改的前提下也可以复用。对于某些开销较大的对象，反复创建显然是不划算的。这时我们可以通过缓存这些对象来实现复用，减少性能消耗。

#### 避免重复创建昂贵对象

并不是所有对象的创建成本都是相同的。假设我们要编写一个方法，用于判断某个字符串是否是有效的罗马数字。最简单的实现方式是使用正则表达式：

```
// 性能可以显著提升！
static boolean isRomanNumeral(String s) {
    return s.matches("^(?=.)M*(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(I[XV]|V?I{0,3})$");
}
```

虽然这种写法简洁，但每次调用 `matches` 方法时，都会新建一个 `Pattern` 对象，并在使用后将其丢弃，导致性能下降。为了提升效率，可以将正则表达式编译为一个静态的 `Pattern` 对象并缓存起来：

```
// 通过复用昂贵对象提升性能
public class RomanNumerals {
    private static final Pattern ROMAN = Pattern.compile(
            "^(?=.)M*(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(I[XV]|V?I{0,3})$");

    static boolean isRomanNumeral(String s) {
        return ROMAN.matcher(s).matches();
    }
}
```

改进后的 `isRomanNumeral` 方法在高频调用时性能提升显著。在我的机器上，原版本处理8字符输入需要1.1微秒，而改进版本只需0.17微秒，速度提升了6.5倍。此外，代码的可读性也有所提高，因为我们将正则表达式封装成了具有语义的静态字段 `ROMAN`，使代码更加清晰。

#### 复用其他类型的对象

不仅仅是不可变对象可以复用，有时一些"适配器"（如视图）对象也可以复用。适配器对象是一种将操作委托给其他对象的模式，通常只提供不同的接口，而不包含额外的状态。例如，`Map` 接口的 `keySet` 方法返回一个视图对象，表示 `Map` 中的所有键。尽管 `keySet` 返回的实例是可变的，但其背后依赖的是同一个 `Map` 实例，因此无论 `keySet` 被调用多少次，返回的对象功能上都是相同的。

```
// 返回相同的 Set 视图对象
Set<String> keys1 = myMap.keySet();
Set<String> keys2 = myMap.keySet();
// keys1 和 keys2 实际上是同一个视图对象
```

在这种情况下，重复创建视图对象不仅没有任何好处，还会徒增对象数量，增加内存开销。

#### 自动装箱的代价

自动装箱（autoboxing）是另一种常见的导致不必要对象创建的机制。自动装箱允许我们在基本类型和包装类型之间自由切换，编译器会自动进行类型转换。然而，自动装箱带来了性能上的隐性成本。例如，下面的代码在计算所有正整数的和时，由于一个细微的错误而导致大量不必要的对象创建：

```
// 极其缓慢！能发现对象创建的原因吗？
private static long sum() {
    Long sum = 0L; // 使用了包装类型 Long，而不是基本类型 long
    for (long i = 0; i <= Integer.MAX_VALUE; i++)
        sum += i;
    return sum;
}
```

上述代码每次 `long` 加法操作都会创建一个新的 `Long` 实例，导致生成约 2^31 个不必要的对象，极大地影响了性能。将 `Long` 换为 `long` 后，运行时间从 6.3 秒减少到 0.59 秒，性能提升了十倍。

#### 对象创建并不总是昂贵

需要注意的是，本文讨论的并不是说对象创建本身是昂贵的。实际上，现代 JVM 对象创建和垃圾回收的效率非常高，创建一些轻量级对象并不会带来显著的性能开销。因此，为了提升代码的简洁性或可读性，适当地创建对象是值得的。反过来，手动管理对象池通常是一个糟糕的主意，除非对象非常重量级（例如数据库连接）。维护对象池会导致代码复杂度增加，内存占用上升，性能反而下降。

#### 总结

不要为了性能避免创建对象，而是要避免不必要的对象创建。在可以复用对象时，应优先复用，尤其是不可变对象、昂贵的对象和适配器对象等。使用自动装箱时也应小心，避免无意中引入不必要的对象创建。同时，不要误认为对象创建一定是昂贵的——现代 JVM 的垃圾回收机制已经非常高效。只有在对象真正影响性能时，才需要关注对象的创建和复用。

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

  30

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

[摘要：2025年机器人产业正经历技术驱动的深度变革，AI初创企业通过创新算法和...
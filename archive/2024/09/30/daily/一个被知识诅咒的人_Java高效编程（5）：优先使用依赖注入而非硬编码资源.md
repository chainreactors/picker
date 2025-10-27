---
title: Java高效编程（5）：优先使用依赖注入而非硬编码资源
url: https://blog.csdn.net/nokiaguy/article/details/142619591
source: 一个被知识诅咒的人
date: 2024-09-30
fetch_date: 2025-10-06T18:23:11.711586
---

# Java高效编程（5）：优先使用依赖注入而非硬编码资源

# Java高效编程（5）：优先使用依赖注入而非硬编码资源

![](https://csdnimg.cn/release/blogv2/dist/pc/img/original.png)

[蒙娜丽宁](https://unitymarvel.blog.csdn.net "蒙娜丽宁")
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCurrentTime2.png)
于 2024-09-29 10:00:00 发布

![](https://csdnimg.cn/release/blogv2/dist/pc/img/articleReadEyes2.png)
阅读量732
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)
收藏

13

![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)
点赞数
10

CC 4.0 BY-SA版权

分类专栏：
[Java高效编程](https://blog.csdn.net/nokiaguy/category_12795365.html)
文章标签：
[java](https://so.csdn.net/so/search/s.do?q=java&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[开发语言](https://so.csdn.net/so/search/s.do?q=%E5%BC%80%E5%8F%91%E8%AF%AD%E8%A8%80&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

本文链接：<https://blog.csdn.net/nokiaguy/article/details/142619591>

[![](https://i-blog.csdnimg.cn/columns/default/20201014180756928.png?x-oss-process=image/resize,m_fixed,h_224,w_224)

Java高效编程
专栏收录该内容](https://blog.csdn.net/nokiaguy/category_12795365.html "Java高效编程")

19 篇文章

订阅专栏

[解锁Python编程的无限可能：《奇妙的Python》带你漫游代码世界](https://unitymarvel.blog.csdn.net/article/details/141889588?spm=1001.2014.3001.5502)

在软件开发中，许多类依赖于某些底层资源。例如，一个拼写检查器类可能依赖于一个词典资源。这种类通常会被错误地实现为静态工具类或单例类，导致不灵活且难以测试。常见的例子是将这些资源硬编码在类内部，这种做法的主要问题在于它假设只有一个固定的资源可供使用，忽视了实际情况中的多样性需求，例如不同语言或特殊领域的词典。

##### 静态工具类和单例类的局限性

首先，考虑静态工具类的实现方式：

```
// 静态工具类的错误使用 - 不灵活且难以测试！
public class SpellChecker {
    private static final Dictionary dictionary = new Dictionary();
    private SpellChecker() {} // 防止实例化

    public static boolean isValid(String word) {
        // 校验单词
        return true;
    }

    public static List<String> suggestions(String typo) {
        // 提供拼写建议
        return List.of("建议1", "建议2");
    }
}
```

这种设计将词典资源固定在了类内部，难以适应多种词典需求，例如不同语言或领域的专用词典。并且它不允许使用模拟词典来进行测试，导致测试的灵活性受限。

类似地，单例模式也存在类似问题：

```
// 单例模式的错误使用 - 不灵活且难以测试！
public class SpellChecker {
    private final Dictionary dictionary;
    private static final SpellChecker INSTANCE = new SpellChecker(new Dictionary());

    private SpellChecker(Dictionary dictionary) {
        this.dictionary = dictionary;
    }

    public static SpellChecker getInstance() {
        return INSTANCE;
    }

    public boolean isValid(String word) {
        return true;
    }

    public List<String> suggestions(String typo) {
        return List.of("建议1", "建议2");
    }
}
```

单例模式同样假设只有一个词典，无法灵活切换，也难以使用不同的词典进行测试。这种设计不适合行为依赖于底层资源的类。

##### 依赖注入的灵活性

为了解决上述问题，我们可以通过依赖注入的方式将资源传递给类的构造函数，使其更加灵活且易于测试。依赖注入是一种将类所需的资源作为参数传递到构造函数中的设计模式。如下所示：

```
// 使用依赖注入实现灵活性和可测试性
public class SpellChecker {
    private final Dictionary dictionary;

    public SpellChecker(Dictionary dictionary) {
        this.dictionary = Objects.requireNonNull(dictionary);
    }

    public boolean isValid(String word) {
        // 根据提供的词典检查单词
        return true;
    }

    public List<String> suggestions(String typo) {
        // 根据提供的词典提供建议
        return List.of("建议1", "建议2");
    }
}
```

通过这种方式，我们在实例化 `SpellChecker` 时可以灵活地传入不同的词典，如英语词典、法语词典，或甚至用于测试的模拟词典。依赖注入不仅提高了代码的可重用性，还保证了类的不可变性，因为资源是通过构造函数传入的，保证了对象一旦创建后其依赖的资源不会发生变化。

##### 依赖注入与工厂模式

在某些情况下，我们可能希望动态创建资源，而不是直接传递资源实例。此时，我们可以将资源工厂传递给构造函数。工厂是一种可以重复调用以创建资源实例的对象。这种模式称为工厂方法模式，可以使用 Java 8 引入的 `Supplier<T>` 接口来表示工厂。例如，我们可以创建一个马赛克，并使用客户端提供的工厂生成每个图块：

```
public class Mosaic {
    public static Mosaic create(Supplier<? extends Tile> tileFactory) {
        // 使用工厂生成图块并创建马赛克
        return new Mosaic();
    }
}
```

通过传递工厂，我们能够在不同的环境下灵活生成所需的资源。这种模式允许更复杂的依赖图，并且通过 `Supplier<T>` 接口，可以让方法接受任意类型的子类型工厂，从而增加灵活性。

##### 依赖注入框架

在较大的项目中，通常会有大量的依赖项，手动进行依赖注入可能会显得繁琐。在这种情况下，我们可以使用依赖注入框架（如 Dagger、Guice 或 Spring）来自动管理依赖关系。尽管这些框架超出了本书的范围，但值得注意的是，使用这些框架时，依赖注入的 API 很容易适应它们，框架可以帮助我们自动处理大量的依赖关系，减少代码复杂性。

##### 总结

不要使用单例或静态工具类来实现依赖于底层资源的类，尤其当这些资源会影响类的行为时。也不要让类直接创建其所依赖的资源。相反，应当通过构造函数、静态工厂或构建器传递资源或资源工厂，这种实践称为依赖注入。依赖注入不仅能大幅提高类的灵活性、可重用性和可测试性，还能有效减少代码中的硬编码资源依赖，提升代码的维护性。

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

  10

  点赞
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike.png)

  踩
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCollectActive.png)

  13

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
2250

[《Python OpenCV从菜鸟到高手》是一本深入探讨Python与OpenCV技术的图像处理教程。从Python的基础知识到OpenCV的强大功能，这本书带领读者逐步掌握计算机视觉的核心技术。Python因其简洁和强大的库生态被广泛应用于数据分析、人工智能等领域，而OpenCV则是图像处理与计算机视觉的利器。本书通过循序渐进的方式，让读者从零基础到掌握高级图像处理技能，帮助你实现从初学者到高手的跃升。](https://unitymarvel.blog.csdn.net/article/details/143574491)

![](https://csdnimg.cn/release/blogv2/dist/components/img/blogType.png)
博客
[【奇妙的Python】解锁Python编程的无限可能：《奇妙的Python》带你漫游代码世界](https://unitymarvel.blog.csdn.net/article/details/141889588)

09-04
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
3139

[《奇妙的Python——神奇代码漫游之旅》是一本面向实际应用的Python编程指南，涵盖文件操作、GUI设计、多媒体处理、自动化办公、加密解密等多个领域。由华为HDE专家李宁编写，通过丰富的实战案例，帮助读者在工作和项目中高效应用Python，提升编程技能。无论是新手还是有经验的开发者，这本书都将带你深入探索Python的无限可能，开启一段充满创意与实用性的编程之旅。](https://unitymarvel.blog.csdn.net/article/details/141889588)

![](https://csdnimg.cn/release/blogv2/dist/components/img/blogType.png)
博客
[2025机器人产业大洗牌：新兴初创企业的技术革命与崛起之路](https://unitymarvel.blog.csdn.net/article/details/151067555)

09-01
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
1049

[摘要：2025年机器人产业正经历技术驱动的深度变革，AI初创企业通过创新算法和低成本方案挑战传统巨头。本文剖析产业洗牌动因，包括AI融合、融资热潮和应用场景扩展，重点解析人形机器人等关键技术。通过ROS控制、A\*路径规划和PyTorch视觉识别等代...
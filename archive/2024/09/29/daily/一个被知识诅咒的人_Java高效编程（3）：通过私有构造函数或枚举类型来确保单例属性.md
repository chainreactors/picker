---
title: Java高效编程（3）：通过私有构造函数或枚举类型来确保单例属性
url: https://blog.csdn.net/nokiaguy/article/details/142619385
source: 一个被知识诅咒的人
date: 2024-09-29
fetch_date: 2025-10-06T18:22:13.471975
---

# Java高效编程（3）：通过私有构造函数或枚举类型来确保单例属性

# Java高效编程（3）：通过私有构造函数或枚举类型来确保单例属性

![](https://i-operation.csdnimg.cn/images/cf31225e169b4512917b2e77694eb0a2.png)单例模式的三种实现方式及比较

![](https://csdnimg.cn/release/blogv2/dist/pc/img/original.png)

[蒙娜丽宁](https://unitymarvel.blog.csdn.net "蒙娜丽宁")
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newUpTime2.png)
已于 2024-09-28 18:19:54 修改

![](https://csdnimg.cn/release/blogv2/dist/pc/img/articleReadEyes2.png)
阅读量864
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)
收藏

11

![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)
点赞数
13

CC 4.0 BY-SA版权

分类专栏：
[Java高效编程](https://blog.csdn.net/nokiaguy/category_12795365.html)
文章标签：
[java](https://so.csdn.net/so/search/s.do?q=java&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[开发语言](https://so.csdn.net/so/search/s.do?q=%E5%BC%80%E5%8F%91%E8%AF%AD%E8%A8%80&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

于 2024-09-28 18:18:35 首次发布

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

本文链接：<https://blog.csdn.net/nokiaguy/article/details/142619385>

[![](https://i-blog.csdnimg.cn/columns/default/20201014180756928.png?x-oss-process=image/resize,m_fixed,h_224,w_224)

Java高效编程
专栏收录该内容](https://blog.csdn.net/nokiaguy/category_12795365.html "Java高效编程")

19 篇文章

订阅专栏

[解锁Python编程的无限可能：《奇妙的Python》带你漫游代码世界](https://unitymarvel.blog.csdn.net/article/details/141889588?spm=1001.2014.3001.5502)

单例模式是一种常见的设计模式，指的是一个类在整个应用程序中只会被实例化一次【Gamma95】。通常，单例模式用于表示无状态的对象（例如某些功能模块），或是那些在系统中独一无二的组件。实现单例模式时，有时会带来测试难度，因为单例类无法轻易被替换为一个模拟实现，除非这个单例类实现了某种接口，使其可以被替换。

实现单例的两种常见方法是通过将类的构造函数设为私有，并通过一个公共的静态成员来提供对唯一实例的访问。在第一种方式中，这个静态成员是一个 `final` 字段：

```
// 通过公共final字段实现单例
public class UniqueInstance {
    public static final UniqueInstance INSTANCE = new UniqueInstance();
    private UniqueInstance() {
        // 构造函数内容
    }

    public void performAction() {
        System.out.println("执行操作");
    }
}
```

在这个实现中，私有构造函数只会在静态字段 `UniqueInstance.INSTANCE` 初始化时被调用一次。因为没有提供公共或受保护的构造函数，因此这个类保证了只能存在一个实例——无论客户端做什么，永远只有一个 `UniqueInstance`。不过，有一个例外：特权客户端可以通过反射调用私有构造函数（详见【条目65】），使用 `AccessibleObject.setAccessible` 方法绕过限制。如果你想防止这种攻击，可以在构造函数中加入检测机制，抛出异常以防止创建第二个实例。

第二种实现单例的方式是使用静态工厂方法：

```
// 通过静态工厂方法实现单例
public class UniqueInstance {
    private static final UniqueInstance INSTANCE = new UniqueInstance();
    private UniqueInstance() {
        // 构造函数内容
    }

    public static UniqueInstance getInstance() {
        return INSTANCE;
    }

    public void performAction() {
        System.out.println("执行操作");
    }
}
```

在这种实现中，每次调用 `UniqueInstance.getInstance()` 方法都会返回相同的对象引用，因此不会创建其他的 `UniqueInstance` 实例（依然有前面提到的反射攻击问题）。

#### 这两种方法的比较

第一种方法（公共字段）有一个显著的优点：API 非常直观，明确表明这个类是单例的，因为 `public static final` 字段会一直指向同一个对象引用。另外，这种实现方式比较简单。

而第二种方法（静态工厂）则提供了更大的灵活性。尽管它当前返回的是单例，但你可以在不修改 API 的情况下，改变返回的实例类型，例如可以返回一个针对每个线程的不同实例。另外，如果你的应用需要，可以编写通用的单例工厂。此外，使用静态工厂的另一个好处是它允许将方法引用作为供应者，例如 `UniqueInstance::getInstance` 可以作为 `Supplier<UniqueInstance>` 使用。如果这些优点对你的需求并不重要，那么使用公共字段的方式会更简单直观。

#### 序列化单例类

如果你希望通过上述方式实现的单例类是可序列化的（见第12章），仅仅在类声明中添加 `implements Serializable` 是不够的。为了维持单例特性，必须将所有实例字段声明为 `transient`，并提供一个 `readResolve` 方法（详见【条目89】）。否则，每次反序列化时，都会创建一个新的实例，这在我们的例子中可能会导致多个 “伪” 的 `UniqueInstance` 存在。为避免这种情况，可以添加以下 `readResolve` 方法：

```
// 通过 readResolve 方法确保单例属性
private Object readResolve() {
    // 返回唯一的 UniqueInstance 实例，并让垃圾回收机制处理其他重复实例
    return INSTANCE;
}
```

#### 使用枚举实现单例

还有第三种方式实现单例，即使用枚举：

```
// 枚举单例——推荐的实现方式
public enum UniqueInstance {
    INSTANCE;

    public void performAction() {
        System.out.println("执行操作");
    }
}
```

这种方式类似于公共字段的方法，但更加简洁，并且自带序列化机制，同时还能确保在任何情况下都不会出现多实例问题，即使在面对复杂的序列化或反射攻击时也是如此。尽管这种方式可能看起来有些不自然，但使用单元素枚举通常是实现单例的最佳方式。需要注意的是，如果你的单例类需要继承某个父类（除了 `Enum` 之外），这种方法就无法使用了，不过你可以让枚举实现接口。

#### 总结

对于单例模式，有三种主要实现方式：使用公共 `final` 字段、使用静态工厂方法以及使用枚举。每种方式都有其优缺点，选择时应根据具体需求进行权衡。如果你希望实现简单且明确的单例模式，公共字段的方式是不错的选择；如果你希望在保持单例的同时拥有更大的灵活性，静态工厂方法将会更加适合。而当你需要极简并且想避免复杂的序列化问题时，使用枚举实现单例几乎是最佳选择。

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

  13

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

[摘要：2025年机器人产业正经历技术驱动的深度变革，AI初创企业通过创新算法和低成本方案挑战传统巨头。本文剖析产业洗牌动因，包括AI融合、融资热潮和应用场景扩展，重点解析人形机器人等关键技术。通过ROS控制、A\*路径规划和PyTorch视觉识别等代码示例（附中文注释），展示初创企业的技术优势。文章预测Figure AI、Unitree等公司将引领消费级机器人市场，推动社会进入智能协作新时代。（150字）...
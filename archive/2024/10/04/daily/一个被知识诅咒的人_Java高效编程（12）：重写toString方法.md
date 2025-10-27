---
title: Java高效编程（12）：重写toString方法
url: https://blog.csdn.net/nokiaguy/article/details/142620908
source: 一个被知识诅咒的人
date: 2024-10-04
fetch_date: 2025-10-06T18:48:21.300823
---

# Java高效编程（12）：重写toString方法

# Java高效编程（12）：重写toString方法

![](https://csdnimg.cn/release/blogv2/dist/pc/img/original.png)

[蒙娜丽宁](https://unitymarvel.blog.csdn.net "蒙娜丽宁")
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCurrentTime2.png)
于 2024-10-03 10:00:00 发布

![](https://csdnimg.cn/release/blogv2/dist/pc/img/articleReadEyes2.png)
阅读量1.3k
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)
收藏

10

![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)
点赞数
19

CC 4.0 BY-SA版权

分类专栏：
[Java高效编程](https://blog.csdn.net/nokiaguy/category_12795365.html)
文章标签：
[java](https://so.csdn.net/so/search/s.do?q=java&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[开发语言](https://so.csdn.net/so/search/s.do?q=%E5%BC%80%E5%8F%91%E8%AF%AD%E8%A8%80&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

本文链接：<https://blog.csdn.net/nokiaguy/article/details/142620908>

[![](https://i-blog.csdnimg.cn/columns/default/20201014180756928.png?x-oss-process=image/resize,m_fixed,h_224,w_224)

Java高效编程
专栏收录该内容](https://blog.csdn.net/nokiaguy/category_12795365.html "Java高效编程")

19 篇文章

订阅专栏

[解锁Python编程的无限可能：《奇妙的Python》带你漫游代码世界](https://unitymarvel.blog.csdn.net/article/details/141889588?spm=1001.2014.3001.5502)

尽管 `Object` 类提供了 `toString` 方法的默认实现，但它返回的字符串通常不是类的使用者想要看到的。默认返回的字符串格式是类名加上“@”符号和哈希码的十六进制表示，例如 `PhoneNumber@163b91`。然而，`toString` 方法的合同要求返回一个简洁且信息丰富的字符串表示，以便用户阅读。显然，与“707-867-5309”相比，“PhoneNumber@163b91”并不具备太多的可读性和信息量。因此，建议重写 `toString` 方法。

虽然重写 `toString` 不如重写 `equals` 和 `hashCode` 那样重要（如【条目10】和【条目11】所述），但提供一个良好的 `toString` 实现能让你的类更加易用，且有助于调试。当对象被传递给 `println`、`printf`、字符串连接操作符或断言语句时，`toString` 会自动调用。即使你不主动调用 `toString`，其他人可能会。例如，某个组件在记录错误消息时可能会包含对象的字符串表示。如果你没有重写 `toString`，这些消息几乎是无用的。

#### 为什么要重写 `toString`

如果你为 `PhoneNumber` 提供了一个好的 `toString` 方法，那么生成有用的诊断消息会变得非常简单：

```
System.out.println("Failed to connect to " + phoneNumber);
```

不论你是否重写 `toString`，程序员通常都会以这种方式生成诊断消息，但只有当你重写了 `toString`，这些消息才真正有用。`toString` 的好处不仅体现在类的实例本身，也会反映在包含这些实例的对象上，特别是集合。比如，当你打印一个 `Map` 时，哪一个更可读：`{Jenny=PhoneNumber@163b91}` 还是 `{Jenny=707-867-5309}`？

`toString` 方法应尽可能返回对象中的所有有趣信息。对于较大的对象或不适合字符串表示的对象，可以返回摘要信息，例如 `Manhattan residential phone directory (1487536 listings)` 或 `Thread[main,5,main]`。理想情况下，字符串应该是自解释的。

#### 格式化和文档化

实现 `toString` 时，一个重要的决定是是否要在文档中指定返回值的格式。对于像电话号码这样的值类，建议指定格式，因为这可以为对象提供一种标准且明确的表示，可以用于输入、输出以及持久化数据（如 CSV 文件）。如果你指定了格式，最好提供匹配的静态工厂方法或构造函数，以便程序员能够在对象和字符串表示之间轻松转换。许多 Java 平台库中的值类（如 `BigInteger`、`BigDecimal` 和大多数包装类）都采用了这种方法。

指定 `toString` 格式的缺点是，一旦你指定了格式，就必须长期坚持使用，特别是当你的类被广泛使用时。如果将来修改了表示格式，可能会导致程序崩溃或数据损坏。因此，如果你不指定格式，就保留了将来改进格式的灵活性。

无论是否指定格式，都应该明确记录你的意图。如果指定格式，要精确说明。例如，下面是与【条目11】中的 `PhoneNumber` 类相匹配的 `toString` 方法文档：

```
/**
 * 返回该电话号码的字符串表示。
 * 字符串由十二个字符组成，格式为“XXX-YYY-ZZZZ”，
 * 其中 XXX 是区号，YYY 是前缀，ZZZZ 是号码。
 *
 * 如果这三个部分中的任意一部分不够长，会用前导零填充。
 * 例如，如果号码值是 123，字符串表示的最后四个字符将是“0123”。
 */
@Override
public String toString() {
    return String.format("%03d-%03d-%04d", areaCode, prefix, lineNum);
}
```

如果你选择不指定格式，则文档注释可能会类似如下：

```
/**
 * 返回该药水的简短描述。表示的具体细节未指定，并且可能会变化，
 * 但通常的格式可能如下：
 *
 * "[Potion #9: type=love, smell=turpentine, look=india ink]"
 */
@Override
public String toString() {
    // 自定义实现
}
```

这种文档确保了使用者在解析字符串表示时不能抱怨格式变化引发的问题。

#### 提供访问器

无论是否指定 `toString` 格式，都应提供程序化访问对象信息的途径。以 `PhoneNumber` 类为例，应该提供获取区号、前缀和号码的访问器。如果没有这些访问器，程序员不得不解析字符串来获取这些信息，这不仅降低了性能，还可能导致错误的系统。如果没有访问器，即使你声明字符串格式是可变的，它实际上仍然会成为一个事实上的 API。

#### 特殊情况

不必在静态工具类（【条目4】）或大多数 `enum` 类型中编写 `toString` 方法，因为 Java 已经为 `enum` 提供了一个很好的默认实现。不过，在抽象类中，如果子类共享相同的字符串表示形式，则应该编写 `toString` 方法。例如，许多集合实现继承了抽象集合类的 `toString` 实现。

此外，Google 的开源 `AutoValue` 工具可以自动生成 `toString` 方法，绝大多数 IDE 也提供了自动生成 `toString` 的功能。这些自动生成的方法对于了解类的字段内容非常有用，但并不适合表示类的特定含义。例如，电话号码类应该有一个标准的字符串表示，而药水类则可以接受自动生成的 `toString` 方法。不过，自动生成的 `toString` 方法仍然比继承自 `Object` 的默认实现好得多，后者几乎无法提供任何有用信息。

#### 总结

除非超类已经重写了 `toString`，否则在你编写的每个实例类中都应重写 `toString`。这会让你的类更易用，并有助于调试。`toString` 方法应返回对象的简洁、有用的描述，并且格式美观。

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

  19

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

[摘要：2025年机器人产业正经历技术驱动的深度变革，AI初创企业通过创新算法和低成本方案挑战传统巨头。本文剖析产业洗牌动因，包括AI融合、融资热潮和应用场景扩展，重点解析人形机器人等关键技术。通过ROS控制、A\*路径规划和PyTorch视觉识别等代码示例（附中文注释），展示初创企业的技术优势。文章预测Figure AI、Unitre...
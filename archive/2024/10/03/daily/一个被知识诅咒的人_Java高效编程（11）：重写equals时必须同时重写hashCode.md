---
title: Java高效编程（11）：重写equals时必须同时重写hashCode
url: https://blog.csdn.net/nokiaguy/article/details/142620856
source: 一个被知识诅咒的人
date: 2024-10-03
fetch_date: 2025-10-06T18:51:36.985794
---

# Java高效编程（11）：重写equals时必须同时重写hashCode

# Java高效编程（11）：重写equals时必须同时重写hashCode

原创
于 2024-10-02 10:00:00 发布
·
839 阅读

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)

16

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)

8
·

CC 4.0 BY-SA版权

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

文章标签：

[#java](https://so.csdn.net/so/search/s.do?q=java&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#开发语言](https://so.csdn.net/so/search/s.do?q=%E5%BC%80%E5%8F%91%E8%AF%AD%E8%A8%80&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

[![](https://i-blog.csdnimg.cn/columns/default/20201014180756928.png?x-oss-process=image/resize,m_fixed,h_224,w_224)

Java高效编程
专栏收录该内容](https://blog.csdn.net/nokiaguy/category_12795365.html "Java高效编程")

19 篇文章

订阅专栏

[解锁Python编程的无限可能：《奇妙的Python》带你漫游代码世界](https://unitymarvel.blog.csdn.net/article/details/141889588?spm=1001.2014.3001.5502)

每当你在类中重写 `equals` 方法时，必须同时重写 `hashCode`。如果不这样做，你的类将违反 `hashCode` 的通用合同，导致在使用 `HashMap`、`HashSet` 等基于哈希的集合时出现问题。`hashCode` 方法合同的主要要求如下：

1. 在应用程序执行期间，每次调用对象的 `hashCode` 方法时，如果对象未发生改变，应返回相同的值。该值不必在不同应用程序执行之间保持一致。
2. 如果两个对象根据 `equals` 方法相等，则它们的 `hashCode` 必须相同。
3. 如果两个对象根据 `equals` 方法不相等，它们的 `hashCode` 不必不同，但生成不同 `hashCode` 值可以提升哈希表的性能。

#### 为什么需要重写 `hashCode`

假设我们有一个 `PhoneNumber` 类（如【条目10】所示）用作 `HashMap` 的键。如果该类只重写了 `equals`，而没有重写 `hashCode`，则即使两个 `PhoneNumber` 实例在逻辑上相等，它们的哈希值也会不同，这违反了 `hashCode` 合同。由于哈希值不同，`HashMap` 在尝试检索时可能会在错误的哈希桶中查找，导致 `get` 方法返回 `null`，即便插入时相等的实例的键值对确实存在。

为了解决这个问题，我们需要为 `PhoneNumber` 类编写一个合适的 `hashCode` 方法。以下是一个简单的例子：

```
// 合适的 hashCode 方法
@Override public int hashCode() {
    int result = Short.hashCode(areaCode);
    result = 31 * result + Short.hashCode(prefix);
    result = 31 * result + Short.hashCode(lineNum);
    return result;
}
```

#### 编写一个好的 `hashCode` 方法

要编写一个好的 `hashCode` 方法，可以遵循以下步骤：

1. 声明一个 `int` 类型的变量 `result`，并将第一个重要字段的 `hashCode` 赋值给它。
2. 对于每个剩余的字段，计算其 `hashCode` 并将其加入 `result` 中：`result = 31 * result + c;`，其中 `c` 是该字段的 `hashCode`。
3. 返回 `result`。

通过上述方法，`hashCode` 方法将确保逻辑上相等的对象有相同的哈希值，从而符合 `hashCode` 合同。

#### 额外注意事项

* **缓存 `hashCode`**：如果计算 `hashCode` 的开销较大且类是不可变的，可以考虑在对象实例化时缓存 `hashCode`，以避免每次调用时重新计算。不过，需要确保在并发环境下缓存是线程安全的。
* **不要排除重要字段**：为了提升性能，不要排除在 `equals` 方法中被比较的字段，否则可能导致多个实例被映射到相同的哈希码，从而影响哈希表的性能。
* **使用现有的工具**：Java 提供了一些工具类，例如 `Objects.hash()`，可以简化 `hashCode` 方法的编写，虽然这种方法的性能较差，尤其是涉及原始类型时需要进行装箱和拆箱操作。在性能不敏感的场景中可以使用这种简化的方式。

#### 性能考虑

`hashCode` 方法的质量直接影响哈希表的性能。如果不同实例的 `hashCode` 过于相似，哈希表的性能会退化成链表的线性查找，严重影响效率。因此，虽然编写一个 `hashCode` 方法可能略显繁琐，但它对于保证哈希表的性能至关重要。

#### 总结

每次重写 `equals` 方法时，必须同时重写 `hashCode`，否则程序中的基于哈希的集合将无法正常工作。`hashCode` 方法应遵循合同规定，确保逻辑上不相等的对象尽量产生不同的哈希值。遵循本文中提供的步骤和建议，可以确保你编写的 `hashCode` 方法高效且可靠。

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

  16

  点赞
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike.png)

  踩
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCollectActive.png)

  8

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

[在现代软件开发中，容器化技术已成为提升应用部署效率和可移植性的关键工具。本文以“Java 与 Docker：容器化部署入门”为主题，深入探讨如何将Java应用无缝集成到Docker环境中。从Docker的基本概念和安装入手，我们将逐步引导读者构建一个简单的Java Web应用，并通过编写Dockerfile实现镜像的创建和容器的运行。文章涵盖了多阶段构建、环境变量配置、数据持久化、网络管理以及安全最佳实践等核心内容。通过大量的代码示例和详细的中文注释，读者可以轻松上手实践操作。同时，我们还将介绍常见问题排查](https://unitymarvel.blog.csdn.net/article/details/151067543)

![](https://csdnimg.cn/release/blogv2/dist/components/img/blogType.png)
博客
[【人工智能】AI代理重塑游戏世界：动态NPC带来的革命性沉浸式体验](https://unitymarvel.blog.csdn.net/article/details/150948550)

08-28
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
1081

[在当今游戏行业迅猛发展的时代，AI代理技术正悄然引发一场革命，尤其是动态非玩家角色（NPC）的应用，将传统静态游戏体验提升至全新的沉浸式境界。本文深入探讨AI代理在游戏中的核心作用，从传统NPC的局限性入手，分析AI代理如何通过机器学习、强化学习和自然语言处理等技术实现动态行为响应。文章详细阐述了AI代理的架构设计、实现路径，并提供大量代码示例，包括Python和C#语言的实际实现，辅以中文注释，帮助读者理解从简单状态机到复杂代理系统的构建过程。同时，引入数学模型如Q-learning算法的LaTeX公式，](https://unitymarvel.blog.csdn.net/article/details/150948550)

![](https://cs...
---
title: Java高效编程（10）：重写equals时必须遵循通用约定
url: https://blog.csdn.net/nokiaguy/article/details/142620809
source: 一个被知识诅咒的人
date: 2024-09-29
fetch_date: 2025-10-06T18:22:12.764937
---

# Java高效编程（10）：重写equals时必须遵循通用约定

# Java高效编程（10）：重写equals时必须遵循通用约定

原创
于 2024-09-28 20:04:47 发布
·
921 阅读

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)

18

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)

15
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

重写 `equals` 方法看似简单，但极易出错，且后果严重。要避免问题，最简单的方法就是不重写 `equals`，这样每个类的实例只与自身相等。如果以下情况适用，那么不重写 `equals` 是正确的选择：

1. **类的每个实例都是独一无二的**：例如 `Thread` 类，其代表的是活跃实体，而不是值，默认的 `equals` 方法已经适用。
2. **类不需要逻辑上的相等性测试**：例如 `Pattern` 类可以重写 `equals` 来检查两个正则表达式是否相同，但设计者认为不需要这个功能。
3. **超类已经重写了 `equals` 并且该行为适用于子类**：例如，大多数 `Set` 实现继承自 `AbstractSet` 的 `equals`，`List` 实现继承自 `AbstractList`，`Map` 实现继承自 `AbstractMap`。
4. **类是私有或包私有的，且你确定 `equals` 不会被调用**：可以通过重写 `equals` 方法抛出 `AssertionError` 来确保该方法不会被意外调用。

#### 何时应该重写 `equals`？

当类有逻辑上的相等性要求且超类没有重写 `equals` 时，就应该重写。通常这是值类的情况，例如 `Integer` 或 `String`。程序员期望通过 `equals` 比较这些值类的逻辑等价性，而不是对象的引用是否相同。重写 `equals` 方法不仅是为了满足程序员的预期，也是为了让实例在作为键或集合元素时表现一致且可预测。

不需要重写 `equals` 的情况之一是使用实例控制（【条目1】）确保每个值最多只有一个对象。例如 `Enum` 类型，因为逻辑等价就是对象标识，`Object` 的 `equals` 方法已足够。

#### `equals` 合同

重写 `equals` 时，必须遵循 `equals` 的一般合同。合同规定 `equals` 实现等价关系，具体包括以下五个属性：

1. **自反性**：对于任何非空引用值 `x`，`x.equals(x)` 必须返回 `true`。
2. **对称性**：对于任何非空引用值 `x` 和 `y`，`x.equals(y)` 必须返回与 `y.equals(x)` 相同的结果。
3. **传递性**：如果 `x.equals(y)` 为真，且 `y.equals(z)` 为真，那么 `x.equals(z)` 必须为真。
4. **一致性**：只要 `equals` 比较中使用的信息没有被修改，`x.equals(y)` 的多次调用必须始终返回相同的结果。
5. **非空性**：对于任何非空引用值 `x`，`x.equals(null)` 必须返回 `false`。

这些要求听起来复杂，但理解后不难遵守。如果违反合同，可能导致程序行为不稳定，甚至崩溃，且错误源头难以定位。

#### 详细解释 `equals` 合同

##### 自反性

自反性要求对象必须与自身相等。违反这一要求很少见。如果违反它，可能导致集合中的 `contains` 方法无法找到刚添加的对象。

##### 对称性

对称性要求两个对象必须对其相等性意见一致。例如，以下类实现了一个忽略大小写的字符串：

```
// 错误示例 - 违反对称性
public final class CaseInsensitiveString {
    private final String s;
    public CaseInsensitiveString(String s) {
        this.s = Objects.requireNonNull(s);
    }

    @Override public boolean equals(Object o) {
        if (o instanceof CaseInsensitiveString)
            return s.equalsIgnoreCase(((CaseInsensitiveString) o).s);
        if (o instanceof String)
            return s.equalsIgnoreCase((String) o);
        return false;
    }
}
```

上面的 `equals` 方法试图与普通字符串互操作，但这导致了对称性问题：`cis.equals(s)` 返回 `true`，而 `s.equals(cis)` 返回 `false`。为解决此问题，可以去掉与 `String` 的互操作代码：

```
@Override public boolean equals(Object o) {
    return o instanceof CaseInsensitiveString &&
           ((CaseInsensitiveString) o).s.equalsIgnoreCase(s);
}
```

##### 传递性

传递性要求如果 `x.equals(y)` 为真且 `y.equals(z)` 为真，那么 `x.equals(z)` 也必须为真。考虑扩展类 `Point` 添加颜色属性的场景：

```
public class ColorPoint extends Point {
    private final Color color;

    public ColorPoint(int x, int y, Color color) {
        super(x, y);
        this.color = color;
    }

    @Override public boolean equals(Object o) {
        if (!(o instanceof ColorPoint))
            return false;
        return super.equals(o) && ((ColorPoint) o).color == color;
    }
}
```

此方法违反了对称性和传递性：`p.equals(cp)` 返回 `true`，而 `cp.equals(p)` 返回 `false`。为解决此问题，使用组合而不是继承：

```
public class ColorPoint {
    private final Point point;
    private final Color color;

    public ColorPoint(int x, int y, Color color) {
        point = new Point(x, y);
        this.color = Objects.requireNonNull(color);
    }

    @Override public boolean equals(Object o) {
        if (!(o instanceof ColorPoint))
            return false;
        ColorPoint cp = (ColorPoint) o;
        return cp.point.equals(point) && cp.color.equals(color);
    }
}
```

##### 一致性

一致性要求对象在未被修改时，相等性必须一致。如果类是可变的，则要确保修改后 `equals` 的结果也保持一致。

##### 非空性

对象必须与 `null` 不相等。即使传递 `null` 时 `equals` 返回 `false`，也不应抛出 `NullPointerException`。这可以通过 `instanceof` 检查来实现。

#### 编写高质量的 `equals` 方法

1. 使用 `==` 检查参数是否为当前对象。
2. 使用 `instanceof` 检查参数类型。
3. 将参数转换为正确类型。
4. 比较所有“重要”字段，确保它们的值相等。

#### 结论

不应轻易重写 `equals`，除非有必要。如果需要重写，务必确保比较类的所有重要字段，并遵守 `equals` 合同的五个规定。对于复杂的值比较，应考虑使用组合而非继承。

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

  18

  点赞
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike.png)

  踩
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCollectActive.png)

  15

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

[《奇妙的Python——神奇代码漫游之旅》是一本面向实际应用的Python编程指南，涵盖文件操作、GUI设计、多媒体处理、自动化办公、加密解密等多个领域。由华为HDE专家李宁编写，通过丰富的实战案例，帮助读者在工作和项目中高效应用Python，提升编程技能。无论是...
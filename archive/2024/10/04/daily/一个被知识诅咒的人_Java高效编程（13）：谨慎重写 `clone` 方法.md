---
title: Java高效编程（13）：谨慎重写 `clone` 方法
url: https://blog.csdn.net/nokiaguy/article/details/142620990
source: 一个被知识诅咒的人
date: 2024-10-04
fetch_date: 2025-10-06T18:48:19.478153
---

# Java高效编程（13）：谨慎重写 `clone` 方法

# Java高效编程（13）：谨慎重写 `clone` 方法

原创
于 2024-10-03 10:00:00 发布
·
1k 阅读

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)

11

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)

11
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

`Cloneable` 接口的设计初衷是作为一个混合接口，用来表明类支持克隆功能。然而，它没有达到这个目的，主要的缺陷是缺乏 `clone` 方法，而 `Object` 类中的 `clone` 方法是受保护的。你无法直接调用 `clone` 方法，即便对象实现了 `Cloneable`，除非借助反射。更糟糕的是，反射调用也不一定总能成功，因为对象可能没有可访问的 `clone` 方法。因此，虽然 `Cloneable` 有很多问题，但它还是被广泛使用，因此理解如何正确实现 `clone` 方法是有价值的。本条目将讨论如何实现一个良好行为的 `clone` 方法，何时适合使用它，以及有哪些替代方法。

那么，`Cloneable` 实际上做了什么呢？虽然它没有定义任何方法，但它会影响 `Object` 类中受保护的 `clone` 方法的行为：如果一个类实现了 `Cloneable`，那么 `clone` 方法将进行逐字段的浅拷贝；否则，它会抛出 `CloneNotSupportedException` 异常。这种接口的使用方式极不常见，因为通常实现接口意味着一个类可以对其客户端做某些事情，而 `Cloneable` 的实现则改变了超类中的受保护方法的行为。

虽然规范没有明确说明，但实际上，一个实现了 `Cloneable` 接口的类通常被期望提供一个正常工作的 `clone` 方法。为了实现这个目标，类及其所有超类必须遵循复杂且不可强制执行的规则。这种机制非常脆弱、危险，并且脱离了语言的核心逻辑：它允许在不调用构造函数的情况下创建对象。

`clone` 方法的通用合同非常宽松。根据 `Object` 规范，`clone` 方法的合同如下：

* `x.clone() != x` 必须为真。
* `x.clone().getClass() == x.getClass()` 必须为真，但这并不是绝对要求。
* `x.clone().equals(x)` 通常为真，但这也不是绝对要求。

通过惯例，`clone` 方法返回的对象应当通过调用 `super.clone` 得到。如果一个类及其所有超类都遵循此惯例，则 `x.clone().getClass() == x.getClass()` 通常成立。

与构造函数链类似，`clone` 机制不是强制执行的：如果某个类的 `clone` 方法通过调用构造函数来创建对象而不是通过 `super.clone`，编译器不会报错，但如果子类调用 `super.clone`，生成的对象可能会有错误的类型，从而导致克隆方法无法正常工作。如果一个类是 `final` 的，则可以安全地忽略这个惯例，因为没有子类存在的风险。

#### 实现 `clone` 方法的示例

假设你想在一个超类已经提供了正确 `clone` 实现的类中实现 `Cloneable`，那么你需要首先调用 `super.clone`。通过 `super.clone` 获取的对象将是原始对象的完全副本。如果类的所有字段都是基本类型或不可变对象的引用，那么返回的对象就是你想要的结果。在这种情况下，不需要进行额外处理。比如，对于【条目11】中的 `PhoneNumber` 类，重写 `clone` 方法可以像这样：

```
// Clone method for class with no references to mutable state
@Override public PhoneNumber clone() {
    try {
        return (PhoneNumber) super.clone();
    } catch (CloneNotSupportedException e) {
        throw new AssertionError();  // Can't happen
    }
}
```

为了让此方法正常工作，`PhoneNumber` 的类声明需要实现 `Cloneable`。虽然 `Object` 的 `clone` 方法返回 `Object`，但 `clone` 方法可以返回 `PhoneNumber` 类型，这是因为 Java 支持协变返回类型，避免了客户端对结果进行类型转换的需求。调用 `super.clone` 方法时，需要将返回的对象从 `Object` 类型转换为 `PhoneNumber`，但这种转换保证会成功。

如果一个类包含对可变对象的引用，像上面这种简单的实现方式可能会带来灾难。例如，考虑【条目7】中的 `Stack` 类：

```
public class Stack {
    private Object[] elements;
    private int size = 0;
    private static final int DEFAULT_INITIAL_CAPACITY = 16;

    public Stack() {
        this.elements = new Object[DEFAULT_INITIAL_CAPACITY];
    }

    public void push(Object e) {
        ensureCapacity();
        elements[size++] = e;
    }

    public Object pop() {
        if (size == 0)
            throw new EmptyStackException();
        Object result = elements[--size];
        elements[size] = null; // Eliminate obsolete reference
        return result;
    }

    private void ensureCapacity() {
        if (elements.length == size)
            elements = Arrays.copyOf(elements, 2 * size + 1);
    }
}
```

如果这个类实现了 `Cloneable`，并且它的 `clone` 方法只是简单调用 `super.clone()`，那么新生成的 `Stack` 实例的 `elements` 数组引用将与原始实例共享同一个数组。这种共享可能导致在修改一个对象时破坏另一个对象的状态。为了避免这种问题，`clone` 方法必须对 `Stack` 类的内部状态进行深拷贝。最简单的方式是对 `elements` 数组递归调用 `clone`：

```
@Override public Stack clone() {
    try {
        Stack result = (Stack) super.clone();
        result.elements = elements.clone();
        return result;
    } catch (CloneNotSupportedException e) {
        throw new AssertionError();
    }
}
```

#### 克隆复杂的可变对象

对于更复杂的类，简单地递归调用 `clone` 可能还不足够。例如，考虑一个哈希表实现，它使用链表存储键值对。直接克隆其桶数组会导致新旧对象共享链表，产生错误结果。此时，需要对每个桶的链表进行深拷贝：

```
public class HashTable implements Cloneable {
    private Entry[] buckets = ...;

    private static class Entry {
        final Object key;
        Object value;
        Entry next;

        Entry(Object key, Object value, Entry next) {
            this.key = key;
            this.value = value;
            this.next = next;
        }

        // Recursive deep copy method
        Entry deepCopy() {
            return new Entry(key, value, next == null ? null : next.deepCopy());
        }
    }

    @Override public HashTable clone() {
        try {
            HashTable result = (HashTable) super.clone();
            result.buckets = new Entry[buckets.length];
            for (int i = 0; i < buckets.length; i++) {
                if (buckets[i] != null)
                    result.buckets[i] = buckets[i].deepCopy();
            }
            return result;
        } catch (CloneNotSupportedException e) {
            throw new AssertionError();
        }
    }
}
```

上面的代码通过递归拷贝链表来保证克隆对象和原对象彼此独立。

#### 设计可扩展的类时的选择

当设计一个可继承的类时，你有两个选择：要么提供一个有效的 `clone` 方法并允许子类重写，要么根本不提供 `clone` 方法，并确保子类也无法实现 `clone` 方法。后一种方式可以通过在类中声明一个 `final` 的 `clone` 方法来实现，该方法简单地抛出 `CloneNotSupportedException`。

如果你编写的是线程安全的类，记得同步 `clone` 方法，以确保线程安全。`Object` 的 `clone` 方法没有同步，因此如果需要，必须在你的 `clone` 方法中添加同步机制。

#### 替代 `Cloneable` 的复制方法

与 `Cloneable` 和 `clone` 方法相关的复杂性通常是不必要的。更好的方法是提供复制构造函数或复制工厂方法。复制构造函数是一种以自身类型作为参数的构造函数：

```
// Copy constructor
public Yum(Yum yum) { ... }
```

复制工厂方法则是静态工厂方法的变体：

```
// Copy factory
public static Yum newInstance(Yum yum) { ... }
```

这些方法相比 `clone` 更简单、灵活，并且不需要遵循复杂的协议。

#### 总结

当你重写 `clone` 时，确保使用 `super.clone` 并对任何可变对象进行深拷贝。如果类的所有字段都是不可变的，则无需额外处理。对于大多数情况下，使用复制构造函数或工厂方法代替 `clone` 是更好的选择。

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

  11

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
[AIGC撕...
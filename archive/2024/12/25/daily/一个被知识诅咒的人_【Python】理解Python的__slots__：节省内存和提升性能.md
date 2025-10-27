---
title: 【Python】理解Python的__slots__：节省内存和提升性能
url: https://blog.csdn.net/nokiaguy/article/details/144703377
source: 一个被知识诅咒的人
date: 2024-12-25
fetch_date: 2025-10-06T19:36:05.570037
---

# 【Python】理解Python的__slots__：节省内存和提升性能

# 【Python】理解Python的\_\_slots\_\_：节省内存和提升性能

原创
已于 2025-01-09 16:49:49 修改
·
976 阅读

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)

15

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)

9
·

CC 4.0 BY-SA版权

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

文章标签：

[#python](https://so.csdn.net/so/search/s.do?q=python&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#开发语言](https://so.csdn.net/so/search/s.do?q=%E5%BC%80%E5%8F%91%E8%AF%AD%E8%A8%80&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

于 2024-12-24 21:30:03 首次发布

[![](https://i-blog.csdnimg.cn/columns/default/20201014180756925.png?x-oss-process=image/resize,m_fixed,h_224,w_224)

Python杂谈
专栏收录该内容](https://blog.csdn.net/nokiaguy/category_12800257.html "Python杂谈")

390 篇文章

订阅专栏

Python作为一门灵活且功能强大的编程语言，广泛应用于各种数据处理和开发项目。然而，Python的灵活性也带来了一些性能上的挑战，特别是在处理大量数据时，内存消耗和属性访问速度可能成为瓶颈。本文深入探讨了Python中的`__slots__`机制，介绍如何通过限制对象属性的存储方式来节省内存并提高性能。我们将通过大量代码示例，详细解释`__slots__`的使用、内部实现原理及其应用场景。通过合理利用`__slots__`，在数据量大的项目中，能够显著优化内存使用，提升程序的执行效率。无论是在机器学习、数据科学还是Web开发中，`__slots__`都能为性能优化提供强有力的支持。

---

#### 1. 引言

在Python中，类的实例化对象通常会使用字典来存储其属性，这使得Python具有极高的灵活性，可以动态地向对象添加属性。但是，这种灵活性也意味着，每个对象都会占用比必要更多的内存。尤其是在大规模数据处理或需要创建大量实例对象的场景中，这种内存消耗可能会成为性能瓶颈。

为了优化这种情况，Python提供了`__slots__`机制，它允许开发者限制对象的属性存储方式，从而节省内存和提升属性访问的速度。通过使用`__slots__`，Python不再为每个实例创建一个字典来存储属性，而是为每个属性创建一个固定的内存结构。这样，内存的使用就更加高效，属性的访问速度也得到了提升。

本文将详细介绍如何在Python中使用`__slots__`，并通过具体的代码示例展示其在内存优化和性能提升中的实际应用。

---

#### 2. `__slots__`的基本概念

##### 2.1 为什么需要`__slots__`？

在默认情况下，Python类的实例对象会为每个属性创建一个字典（`__dict__`）。该字典允许我们在运行时动态地向对象添加属性。然而，这种灵活性也带来了开销。每个对象不仅要存储属性的值，还要存储与属性名相关的键值对。因此，当我们需要创建大量对象时，内存消耗会急剧增加。

##### 2.2 `__slots__`的工作原理

`__slots__`机制允许开发者通过定义一个类变量`__slots__`，显式地指定该类的实例只能拥有哪些属性。通过这种方式，Python会使用一个更紧凑的数据结构（通常是一个C语言数组或类似结构）来存储这些属性，而不是使用字典。这种方式节省了内存空间，并且提升了属性访问的速度。

举个例子，假设我们有一个`Person`类，包含`name`和`age`两个属性：

```
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

在没有`__slots__`的情况下，`Person`类的每个实例都会有一个`__dict__`属性，用来存储`name`和`age`。但是，如果我们使用`__slots__`来限制`Person`类的属性：

```
class Person:
    __slots__ = ['name', 'age']

    def __init__(self, name, age):
        self.name = name
        self.age = age
```

此时，Python不再为每个实例创建`__dict__`，而是为`name`和`age`分配了固定的内存空间。这种方式节省了内存，并且属性的访问速度也得到了提升。

##### 2.3 `__slots__`的优势

* **节省内存**：通过禁止动态添加属性，`__slots__`能够显著减少每个对象的内存开销，特别是在需要创建大量对象时。
* **加速属性访问**：由于属性存储在固定位置，访问速度比字典查找更快。
* **限制对象属性**：`__slots__`通过明确列出允许的属性名称，防止对象拥有未定义的属性，从而避免错误。

##### 2.4 `__slots__`的限制

尽管`__slots__`有许多优势，但它也有一些限制：

* **无法动态添加属性**：一旦在类中定义了`__slots__`，只能使用`__slots__`中定义的属性名。如果试图为实例添加其他属性，会抛出`AttributeError`。
* **不支持`__dict__`**：如果没有定义`__dict__`，将无法使用`__dict__`访问属性。
* **无法继承`__slots__`**：子类默认不继承父类的`__slots__`，如果子类需要定义`__slots__`，需要显式声明。

---

#### 3. 使用`__slots__`节省内存和提升性能

##### 3.1 基础示例：使用`__slots__`减少内存开销

假设我们需要创建大量的`Person`对象，每个对象都有`name`和`age`属性。如果没有使用`__slots__`，Python会为每个对象创建一个`__dict__`字典来存储属性。

```
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

在这种情况下，我们可以使用`sys.getsizeof()`来查看每个对象的内存占用：

```
import sys

# 创建没有__slots__的Person对象
person = Person('John', 30)
print(sys.getsizeof(person))  # 输出对象的内存大小
```

接下来，我们使用`__slots__`来优化内存：

```
class PersonWithSlots:
    __slots__ = ['name', 'age']

    def __init__(self, name, age):
        self.name = name
        self.age = age
```

通过这种方式，我们避免了为每个对象创建一个字典。再运行`sys.getsizeof()`来对比两个类的内存占用：

```
person_with_slots = PersonWithSlots('John', 30)
print(sys.getsizeof(person_with_slots))  # 输出优化后的内存大小
```

在大多数情况下，使用`__slots__`会显著减少每个对象的内存占用。

##### 3.2 属性访问速度的提升

除了节省内存，`__slots__`还可以提升属性访问速度。我们可以通过以下代码对比两种方式访问属性的时间：

```
import time

# 没有使用__slots__的Person类
start_time = time.time()
person = Person('John', 30)
for _ in range(1000000):
    person.name
end_time = time.time()
print("访问未优化对象的时间：", end_time - start_time)

# 使用__slots__的PersonWithSlots类
start_time = time.time()
person_with_slots = PersonWithSlots('John', 30)
for _ in range(1000000):
    person_with_slots.name
end_time = time.time()
print("访问优化对象的时间：", end_time - start_time)
```

在大量访问属性的情况下，使用`__slots__`的`PersonWithSlots`类将比没有使用`__slots__`的`Person`类更快，因为它避免了字典查找。

##### 3.3 适用场景

`__slots__`适用于以下几种场景：

* **大量实例化对象**：当需要创建大量对象时，使用`__slots__`可以显著减少内存开销。
* **性能敏感的应用**：在需要高频访问属性的场景中，`__slots__`能够提高属性访问速度。
* **数据处理与分析**：在处理大量数据时，尤其是需要创建大量数据对象的应用中，`__slots__`能够提高性能，减少内存消耗。

---

#### 4. `__slots__`的进阶使用

##### 4.1 继承中的`__slots__`

当我们有继承结构时，`__slots__`的行为会稍有不同。如果子类定义了`__slots__`，它不会自动继承父类的`__slots__`。因此，我们需要在子类中显式地定义`__slots__`。

###### 示例：继承和`__slots__`

```
class Animal:
    __slots__ = ['name', 'species']

    def __init__(self, name, species):
        self.name = name
        self.species = species

class Dog(Animal):
    __slots__ = ['breed']

    def __init__(self, name, species, breed):
        super().__init__(name, species)
        self.breed = breed
```

在这个示例中，`Dog`类继承了`Animal`类，但它不会自动继承`Animal`类的`__slots__`，需要在`Dog`类

中显式地定义`__slots__`。

##### 4.2 动态添加属性

如果我们尝试在使用`__slots__`的对象上动态添加未定义的属性，将会抛出`AttributeError`。

###### 示例：试图添加未定义的属性

```
try:
    person_with_slots.address = '123 Main St'  # 这将抛出异常
except AttributeError as e:
    print(e)
```

这种限制可以有效防止属性误操作，提升代码的健壮性。

---

#### 5. 总结

本文详细介绍了Python中的`__slots__`机制，并通过具体的代码示例展示了如何使用`__slots__`来节省内存和提升性能。通过限制对象属性的存储方式，`__slots__`不仅能够显著减少内存开销，还能提高属性访问速度，尤其在数据量大的项目中，`__slots__`能够为性能优化提供强有力的支持。

然而，`__slots__`也有一些限制，如无法动态添加属性和无法继承`__slots__`，因此在使用时需要根据实际情况权衡利弊。在实际开发中，合理使用`__slots__`能够让我们的代码更加高效，特别是在处理大量数据和需要频繁访问属性的场景下，`__slots__`提供了一个有效的优化手段。

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

  15

  点赞
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike.png)

  踩
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCollectActive.png)

  9

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

[随着人工智能（AI）技术的迅猛发展，尤其是生成式AI（AIGC），劳动力市场正经历前所未有的变革。从内容创作到自动化生产线，几乎每个行业都在经历一场技术的洗礼。然而，这场革命并不是全然的光明，它带来了深刻的社会变动，...
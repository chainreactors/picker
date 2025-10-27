---
title: 【Python】深入了解Python中的属性访问控制：通过__getattr__与__setattr__实现动态属性管理
url: https://blog.csdn.net/nokiaguy/article/details/144507172
source: 一个被知识诅咒的人
date: 2024-12-17
fetch_date: 2025-10-06T19:38:06.271011
---

# 【Python】深入了解Python中的属性访问控制：通过__getattr__与__setattr__实现动态属性管理

# 【Python】深入了解Python中的属性访问控制：通过\_\_getattr\_\_与\_\_setattr\_\_实现动态属性管理

原创
已于 2025-01-09 16:53:12 修改
·
1k 阅读

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)

25

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)

29
·

CC 4.0 BY-SA版权

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

文章标签：

[#python](https://so.csdn.net/so/search/s.do?q=python&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#javascript](https://so.csdn.net/so/search/s.do?q=javascript&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#前端](https://so.csdn.net/so/search/s.do?q=%E5%89%8D%E7%AB%AF&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

于 2024-12-16 13:50:51 首次发布

[![](https://i-blog.csdnimg.cn/columns/default/20201014180756925.png?x-oss-process=image/resize,m_fixed,h_224,w_224)

Python杂谈
专栏收录该内容](https://blog.csdn.net/nokiaguy/category_12800257.html "Python杂谈")

390 篇文章

订阅专栏

在Python中，类的属性访问控制是通过魔术方法（magic methods）实现的，其中`__getattr__`和`__setattr__`是两个至关重要的魔术方法。本文将深入探讨这两个方法的原理和用法，展示它们如何支持动态属性的管理、访问控制以及数据封装等高级特性。通过丰富的代码示例和解释，帮助读者理解如何灵活地通过这两个方法定制类的属性行为。

本文将通过以下几个方面来展开讨论：如何使用`__getattr__`获取不存在的属性，如何通过`__setattr__`控制属性的设置，如何通过这两个方法实现数据封装和懒加载等高级功能。除此之外，还将探讨在实际开发中如何通过这两个方法实现属性验证、动态计算、惰性初始化等功能。最终，我们将总结如何利用这两个方法实现更具可维护性、灵活性的Python类设计。

### 1. 引言

在Python中，属性是对象的核心组成部分，通常我们使用点操作符（`.`）来访问对象的属性。但在某些情况下，我们希望对这些属性的访问和修改进行更精细的控制。这时，Python的魔术方法（magic methods）`__getattr__`和`__setattr__`便派上了用场。通过这两个方法，我们可以在类中动态地拦截属性的访问与赋值操作，执行特定的逻辑。

具体来说：

* `__getattr__(self, name)`：当我们尝试访问一个对象中不存在的属性时，`__getattr__`方法会被调用。可以在这个方法中进行动态属性的计算或返回默认值。
* `__setattr__(self, name, value)`：这个方法会在我们试图设置对象的属性值时被调用。通过这个方法，我们可以验证属性值、记录日志、执行懒加载等操作。

理解这两个方法的用法和原理，可以帮助开发者设计更加灵活和高效的Python类。

### 2. `__getattr__`与`__setattr__`的基本原理

#### 2.1 `__getattr__`：动态属性访问

`__getattr__`是一个在属性访问时触发的魔术方法。当访问的属性不存在于对象的`__dict__`中时，Python会调用该方法。该方法接受两个参数：

* `self`：指向当前对象的引用。
* `name`：我们尝试访问的属性名。

如果`__getattr__`方法返回值，那么该值就会作为属性的值返回；如果`__getattr__`没有返回任何内容，Python会抛出`AttributeError`异常。

以下是一个简单的例子，展示了如何使用`__getattr__`来访问动态生成的属性：

```
class DynamicAttributes:
    def __init__(self):
        self.existing_attribute = "I am an existing attribute"

    # 当访问不存在的属性时调用
    def __getattr__(self, name):
        print(f"Accessing the non-existent attribute: {name}")
        if name == "dynamic_attribute":
            return "This is a dynamically created attribute"
        else:
            raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")

# 创建对象
obj = DynamicAttributes()

# 访问存在的属性
print(obj.existing_attribute)  # 输出: I am an existing attribute

# 访问不存在的属性，触发__getattr__
print(obj.dynamic_attribute)  # 输出: This is a dynamically created attribute
```

在上面的示例中，当访问`dynamic_attribute`时，由于该属性在对象的`__dict__`中不存在，因此会触发`__getattr__`方法，从而返回一个动态生成的属性值。对于其他未定义的属性，`__getattr__`会抛出`AttributeError`异常。

#### 2.2 `__setattr__`：动态属性设置

`__setattr__`方法用于在试图设置对象的属性时进行拦截。与`__getattr__`不同，`__setattr__`方法会在任何属性的赋值操作时被调用。它有三个参数：

* `self`：指向当前对象的引用。
* `name`：我们尝试设置的属性名。
* `value`：属性的新值。

`__setattr__`方法必须显式地调用`super().__setattr__(name, value)`来设置真实的属性值，否则会导致无限递归。以下是一个简单的例子，展示如何通过`__setattr__`控制属性赋值：

```
class AttributeSetter:
    def __init__(self):
        self._existing_attribute = "I am an existing attribute"

    # 拦截属性赋值
    def __setattr__(self, name, value):
        if name == "_existing_attribute":
            print("Modifying existing attribute!")
            super().__setattr__(name, value)  # 需要调用父类的方法来实际设置属性
        else:
            print(f"Setting new attribute: {name} = {value}")
            super().__setattr__(name, value)  # 继续调用父类方法设置属性

# 创建对象
obj = AttributeSetter()

# 设置属性
obj._existing_attribute = "Modified existing attribute"
obj.new_attribute = "This is a new attribute"
```

在这个例子中，我们通过`__setattr__`拦截了对`_existing_attribute`的赋值，并在控制台输出了一条消息。对于其他属性，`__setattr__`会直接进行赋值操作。

### 3. 实际应用中的高级技巧

#### 3.1 数据封装与属性验证

使用`__getattr__`和`__setattr__`可以在类中实现更为复杂的数据封装和属性验证功能。我们可以在这些方法中验证属性值的合法性，或者在属性被访问时进行计算。以下是一个通过`__setattr__`实现属性验证的例子：

```
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __setattr__(self, name, value):
        if name == "age":
            if value < 0:
                raise ValueError("Age cannot be negative")
        super().__setattr__(name, value)

# 创建对象
person = Person("Alice", 25)

# 设置合法属性值
person.age = 30
print(person.age)  # 输出: 30

# 设置非法属性值
try:
    person.age = -5
except ValueError as e:
    print(e)  # 输出: Age cannot be negative
```

在这个例子中，我们通过`__setattr__`确保`age`属性不能设置为负值。如果尝试将`age`设置为负数，就会抛出`ValueError`异常。

#### 3.2 懒加载属性

懒加载（Lazy Loading）是指延迟初始化对象属性，只有在需要时才进行计算或加载。这对于需要消耗大量资源的属性非常有用。我们可以通过`__getattr__`实现懒加载功能：

```
class LazyLoading:
    def __init__(self):
        self._data = None

    def _load_data(self):
        print("Loading data...")
        self._data = "This is the expensive data"

    def __getattr__(self, name):
        if name == "data":
            if self._data is None:
                self._load_data()
            return self._data
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")

# 创建对象
obj = LazyLoading()

# 第一次访问数据，触发懒加载
print(obj.data)  # 输出: Loading data... \n This is the expensive data

# 再次访问数据，不会触发加载
print(obj.data)  # 输出: This is the expensive data
```

在这个例子中，`data`属性在第一次访问时会通过`_load_data`方法加载，而后续访问则直接返回已加载的数据。这样可以避免不必要的计算或I/O操作，从而提高效率。

#### 3.3 代理模式（Proxy Pattern）

代理模式通过一个代理对象来控制对真实对象的访问，通常用于延迟加载、访问控制等场景。在Python中，我们可以使用`__getattr__`和`__setattr__`来实现代理模式。以下是一个简单的代理模式实现：

```
class RealService:
    def fetch_data(self):
        print("Fetching data from the real service...")
        return "Real data"

class ProxyService:
    def __init__(self):
        self._real_service = None

    def __getattr__(self, name):
        if name == "fetch_data":
            if self._real_service is None:
                print("Creating the real service...")
                self._real_service = RealService()
            return getattr(self._real_service, name)

# 使用代理
proxy = ProxyService()
print(proxy.fetch_data())  # 第一次调用，会创建真实的服务

print(proxy.fetch_data())  # 第二次调用，直接使用已有的服务
```

在这个示例中，`ProxyService`类通过`__getattr__`延迟创建`RealService`实例，只有在访问`fetch_data`方法时，才会创建并调用`RealService`的真实方法。

### 4. 性能考虑

虽然`__getattr__`和`__setattr__`提供了强大的功能，但它们的使用可能会对性能产生一定的影响。每次访问或修改属性时，都会触发这两个方法，尤其在属性频繁访问的场景下，可能会导致额外的计算开销。因此，使用时应避免不必要的复杂逻辑，尽量简化方法内部的操作。

### 5. 总结

通过`__getattr__`和`__setattr__`，我们可以灵活地控制Python类中属性的访问与赋值操作。这些魔术方法不仅支持懒加载、属性验证等功能，还能够帮助我们实现设计模式（如代理模式）和复杂的数据封装。

尽管这些方法为我们提供了很强的动态特性，但我们也需要谨慎使用，避免因复杂逻辑带来的性能问题。掌握这些技巧，可以使我们的代码更加灵活、简洁且高效。

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

  25

  点赞
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike.png)

  踩
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCollectActive.png)

  29

  收藏

  觉得还不错?
  一键收藏
  ...
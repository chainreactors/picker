---
title: Python中的上下文管理器：如何用contextlib编写高效代码
url: https://blog.csdn.net/nokiaguy/article/details/144883775
source: 一个被知识诅咒的人
date: 2025-01-03
fetch_date: 2025-10-06T20:07:57.800164
---

# Python中的上下文管理器：如何用contextlib编写高效代码

# Python中的上下文管理器：如何用contextlib编写高效代码

原创
[![](https://csdnimg.cn/release/blogv2/dist/pc/img/identityVipNew.png)](https://mall.csdn.net/vip)
已于 2025-01-02 12:41:32 修改
·
1.5k 阅读

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)

29

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)

24
·

CC 4.0 BY-SA版权

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

文章标签：

[#python](https://so.csdn.net/so/search/s.do?q=python&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#开发语言](https://so.csdn.net/so/search/s.do?q=%E5%BC%80%E5%8F%91%E8%AF%AD%E8%A8%80&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

于 2025-01-02 12:40:15 首次发布

[《Python OpenCV从菜鸟到高手》带你进入图像处理与计算机视觉的大门！](https://blog.csdn.net/nokiaguy/article/details/143574491)

[解锁Python编程的无限可能：《奇妙的Python》带你漫游代码世界](https://unitymarvel.blog.csdn.net/article/details/141889588)

在Python编程中，资源管理是一个关键的环节，尤其是在处理文件操作、网络连接以及锁等需要精确控制资源释放的场景中。上下文管理器（Context Manager）通过`with`语句提供了一种优雅且高效的资源管理方式。然而，手动编写上下文管理器往往需要编写冗长的代码，包括`__enter__`和`__exit__`方法。Python的`contextlib`模块通过装饰器和上下文管理器工具，极大地简化了上下文管理器的创建过程，使代码更加简洁、可读性更强。本文将深入探讨`contextlib`模块的使用方法，通过丰富的示例和代码演示，展示如何利用`contextlib`编写高效的上下文管理器，提升代码的可维护性和性能。我们将涵盖`contextmanager`装饰器、`closing`、`suppress`、`ExitStack`等工具，并通过实际案例说明它们在不同场景中的应用。通过本文的学习，读者将能够掌握使用`contextlib`优化资源管理的技巧，从而编写出更加高效和优雅的Python代码。

### 引言

在Python编程中，资源管理是一个至关重要的方面。无论是文件操作、网络连接，还是线程锁的管理，正确地获取和释放资源都是保证程序稳定性和性能的基础。传统上，Python通过上下文管理器（Context Manager）和`with`语句来简化资源的管理。然而，编写上下文管理器通常需要实现`__enter__`和`__exit__`方法，这在简单场景下显得冗长且繁琐。为了解决这一问题，Python提供了`contextlib`模块，通过装饰器和一系列工具，极大地简化了上下文管理器的创建过程，使开发者能够以更简洁和高效的方式管理资源。

本文将深入探讨`contextlib`模块的功能和使用方法，介绍如何利用`contextlib`编写高效的上下文管理器。我们将通过丰富的代码示例和详细的解释，展示`contextlib`在不同场景中的应用，帮助读者掌握优化资源管理的技巧，从而编写出更加优雅和高效的Python代码。

### 上下文管理器基础

在深入探讨`contextlib`之前，首先需要了解上下文管理器的基本概念和使用方法。上下文管理器是实现了`__enter__`和`__exit__`方法的对象，通过`with`语句可以自动管理资源的获取和释放。

#### 使用`with`语句管理文件

以下是一个使用`with`语句管理文件的简单示例：

```
# 使用with语句打开文件，确保文件在使用后自动关闭
with open('example.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)
```

在这个示例中，`open`函数返回一个文件对象，该对象实现了上下文管理器协议。`with`语句确保在代码块执行完毕后，文件会被自动关闭，无论代码块内是否发生异常。

#### 自定义上下文管理器

有时，内置的上下文管理器无法满足特定需求，此时需要自定义上下文管理器。传统的方式是创建一个类，并实现`__enter__`和`__exit__`方法。

```
class MyContextManager:
    def __enter__(self):
        print("进入上下文")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("退出上下文")
        if exc_type:
            print(f"异常类型: {

     exc_type}")
        # 可以选择是否抑制异常，返回True表示抑制
        return False

# 使用自定义的上下文管理器
with MyContextManager() as manager:
    print("在上下文中执行代码")
    # 触发异常
    raise ValueError("一个示例异常")
```

输出：

```
进入上下文
在上下文中执行代码
退出上下文
异常类型: <class 'ValueError'>
Traceback (most recent call last):
  File "example.py", line 21, in <module>
    raise ValueError("一个示例异常")
ValueError: 一个示例异常
```

在这个示例中，自定义的上下文管理器在进入上下文时打印一条消息，退出时打印另一条消息，并在发生异常时捕获并打印异常信息。

### `contextlib`模块简介

`contextlib`模块提供了一系列工具，用于简化上下文管理器的创建和使用。通过使用`contextlib`，可以避免手动编写`__enter__`和`__exit__`方法，从而减少代码量，提高代码可读性和可维护性。

#### 常用工具

`contextlib`模块中常用的工具包括：

* `contextmanager`装饰器
* `closing`上下文管理器
* `suppress`上下文管理器
* `redirect_stdout`和`redirect_stderr`
* `ExitStack`上下文管理器

接下来，我们将逐一介绍这些工具的使用方法和应用场景。

### 使用`contextmanager`装饰器

`contextmanager`装饰器是`contextlib`模块中最常用的工具之一，它允许开发者使用生成器函数来创建上下文管理器。通过这种方式，可以以更直观和简洁的方式定义上下文管理器。

#### 基本用法

`contextmanager`装饰器通过装饰一个生成器函数，该函数使用`yield`语句将资源的获取和释放分开。`yield`之前的代码用于资源的获取，`yield`之后的代码用于资源的释放。

##### 示例：简化自定义上下文管理器

假设我们需要创建一个上下文管理器，用于在进入上下文时打印一条消息，退出时打印另一条消息。传统的方式需要定义一个类并实现`__enter__`和`__exit__`方法，而使用`contextmanager`可以简化这一过程。

```
from contextlib import contextmanager

@contextmanager
def my_context_manager():
    print("进入上下文")
    try:
        yield
    finally:
        print("退出上下文")

# 使用自定义的上下文管理器
with my_context_manager():
    print("在上下文中执行代码")
```

输出：

```
进入上下文
在上下文中执行代码
退出上下文
```

在这个示例中，`my_context_manager`函数通过`@contextmanager`装饰器被转换为一个上下文管理器。`yield`语句之前的代码在进入上下文时执行，`yield`之后的代码在退出上下文时执行。

#### 处理异常

`contextmanager`装饰器还可以用于处理上下文中的异常。例如，我们可以创建一个上下文管理器，在发生异常时执行特定的操作。

```
from contextlib import contextmanager

@contextmanager
def exception_handler():
    try:
        yield
    except Exception as e:
        print(f"捕获异常: {

     e}")

# 使用带有异常处理的上下文管理器
with exception_handler():
    print("在上下文中执行代码")
    raise ValueError("一个示例异常")
```

输出：

```
在上下文中执行代码
捕获异常: 一个示例异常
```

在这个示例中，当上下文中的代码抛出异常时，`exception_handler`上下文管理器捕获并处理了该异常。

#### 传递资源

`contextmanager`装饰器还可以用于传递资源。例如，创建一个上下文管理器，用于打开和关闭文件。

```
from contextlib import contextmanager

@contextmanager
def open_file(file_path, mode):
    f = open(file_path, mode, encoding='utf-8')
    try:
        yield f
    finally:
        f.close()

# 使用自定义的文件上下文管理器
with open_file('example.txt', 'w') as file:
    file
```

![](https://csdnimg.cn/release/blogv2/dist/pc/img/lock.png)最低0.47元/天 解锁文章

200万优质内容无限畅学

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

  29

  点赞
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike.png)

  踩
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCollectActive.png)

  24

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
[【奇妙的Python】解锁Python编程的无限可能：《...
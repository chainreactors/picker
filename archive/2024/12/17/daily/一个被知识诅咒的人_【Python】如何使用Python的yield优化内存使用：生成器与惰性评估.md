---
title: 【Python】如何使用Python的yield优化内存使用：生成器与惰性评估
url: https://blog.csdn.net/nokiaguy/article/details/144507223
source: 一个被知识诅咒的人
date: 2024-12-17
fetch_date: 2025-10-06T19:38:05.585975
---

# 【Python】如何使用Python的yield优化内存使用：生成器与惰性评估

# 【Python】如何使用Python的yield优化内存使用：生成器与惰性评估

![](https://csdnimg.cn/release/blogv2/dist/pc/img/original.png)

[蒙娜丽宁](https://unitymarvel.blog.csdn.net "蒙娜丽宁")
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newUpTime2.png)
已于 2025-01-09 16:52:58 修改

![](https://csdnimg.cn/release/blogv2/dist/pc/img/articleReadEyes2.png)
阅读量862
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)
收藏

26

![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)
点赞数
27

CC 4.0 BY-SA版权

分类专栏：
[Python杂谈](https://blog.csdn.net/nokiaguy/category_12800257.html)
文章标签：
[python](https://so.csdn.net/so/search/s.do?q=python&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[开发语言](https://so.csdn.net/so/search/s.do?q=%E5%BC%80%E5%8F%91%E8%AF%AD%E8%A8%80&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

于 2024-12-16 13:52:54 首次发布

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

本文链接：<https://blog.csdn.net/nokiaguy/article/details/144507223>

[![](https://i-blog.csdnimg.cn/columns/default/20201014180756925.png?x-oss-process=image/resize,m_fixed,h_224,w_224)

Python杂谈
专栏收录该内容](https://blog.csdn.net/nokiaguy/category_12800257.html "Python杂谈")

390 篇文章

订阅专栏

Python的`yield`关键字是实现生成器的核心，它能够以惰性求值的方式生成数据，在处理大规模数据时显著提高内存效率。生成器与传统的列表相比，使用了懒加载机制，即只有在需要时才生成数据，从而避免了一次性将所有数据加载到内存中。本文将深入探讨`yield`在优化内存使用方面的应用，讲解如何使用生成器提高内存效率，特别是在处理大量数据时的优势。我们将通过代码示例展示生成器的使用，并对比传统方法和生成器的内存消耗，帮助读者理解如何利用`yield`提升内存效率，并探索其在实际开发中的应用场景。

---

#### 1. 引言

Python是一种高级编程语言，因其简单易用而广泛应用于各种场景。然而，Python作为解释型语言，通常在处理大规模数据时会面临内存消耗过大的问题，尤其是在需要遍历大量数据的任务中。例如，处理大文件、数据流、网络请求等场景时，传统的列表和数据结构容易导致内存的高占用，甚至出现内存溢出的情况。

为了优化内存使用，Python提供了`yield`关键字，它支持生成器（generator）的实现。生成器是一个迭代器，可以惰性生成数据，这意味着只有在需要时才会计算出下一个值，从而节省了大量内存。通过使用生成器，Python能够有效地处理大数据集、流式数据，甚至实现无限序列的生成。

本文将介绍如何使用`yield`来优化内存使用，展示生成器与传统数据结构的区别，并提供多种场景的应用示例，帮助开发者理解如何在内存受限的情况下高效地处理大规模数据。

---

#### 2. 生成器与惰性评估

##### 2.1 什么是生成器？

生成器是一个特殊的迭代器，它能惰性地生成一系列数据。当调用`yield`时，生成器会暂停当前函数的执行，并将数据返回给调用方，直到下一次迭代时，生成器会继续执行并生成下一个数据。与普通函数不同，生成器函数可以在执行过程中被暂停和恢复，从而避免了在内存中一次性存储所有数据。

生成器的优点在于它不需要一次性加载所有数据，这在处理大规模数据时尤为重要。传统的列表和其他数据结构通常会一次性将所有元素加载到内存中，而生成器只有在实际需要时才会生成下一个元素，从而显著节省内存。

##### 2.2 如何使用`yield`？

在Python中，`yield`关键字用来定义生成器。与普通函数不同，生成器函数使用`yield`返回值而不是`return`。每次`yield`会暂停函数的执行，并将当前值返回，直到下一次迭代时恢复函数执行。

###### 示例：使用`yield`实现生成器

```
def simple_generator():
    yield 1
    yield 2
    yield 3

# 使用生成器
gen = simple_generator()
for value in gen:
    print(value)
```

输出：

```
1
2
3
```

在上面的例子中，`simple_generator`是一个生成器函数，每次遇到`yield`时，函数的执行会暂停并返回当前值。当迭代器再次请求下一个值时，函数会从上次停止的地方继续执行。

##### 2.3 生成器与普通函数的区别

* 普通函数一次性返回所有值，生成器函数通过`yield`按需返回值，节省内存。
* 普通函数在执行时会占用完整的栈空间，而生成器函数则只占用当前状态，不需要保存完整的上下文。
* 生成器是惰性求值的，只有在实际需要时才生成数据，而普通函数则会立即生成所有数据。

##### 2.4 生成器的内存效率

由于生成器是惰性评估的，它们不会一次性生成所有数据，而是在需要时生成一个数据项。这意味着生成器能够处理比列表更大的数据集而不占用大量内存。例如，使用生成器遍历一个大文件时，我们可以避免将整个文件加载到内存中，从而节省了内存。

---

#### 3. 使用生成器优化内存

##### 3.1 传统方法与生成器对比

在处理大数据时，传统的列表方法往往会占用大量内存。假设我们需要处理一个庞大的数据集，生成该数据集的所有元素并存储在内存中的话，可能会导致内存溢出或性能瓶颈。使用生成器则能逐步生成数据，减少内存占用。

###### 示例：传统方法生成大量数据

```
# 传统方法：将所有数据存储在列表中
def generate_numbers(n):
    return [x for x in range(n)]

numbers = generate_numbers(1000000)
print(numbers[:10])  # 打印前10个数字
```

在这个例子中，我们将所有的数字存储在一个列表中，意味着整个100万数字都被加载到内存中。这可能会导致内存消耗过大，尤其是在内存有限的情况下。

###### 示例：使用生成器优化内存

```
# 使用生成器：按需生成数据
def generate_numbers_gen(n):
    for x in range(n):
        yield x

numbers_gen = generate_numbers_gen(1000000)
print(next(numbers_gen))  # 打印第一个数字
print(next(numbers_gen))  # 打印第二个数字
```

在这个优化后的例子中，生成器函数按需生成数据，只有在调用`next()`时才会计算出下一个数字。由于数据没有被一次性加载到内存中，因此我们能够处理更大的数据集，并显著减少内存使用。

##### 3.2 生成器的内存消耗对比

我们可以通过`sys.getsizeof()`来比较生成器与传统数据结构的内存消耗。

###### 示例：内存消耗对比

```
import sys

# 使用列表生成数据
numbers_list = [x for x in range(1000000)]
print(f"List memory usage: {sys.getsizeof(numbers_list)} bytes")

# 使用生成器生成数据
numbers_gen = (x for x in range(1000000))
print(f"Generator memory usage: {sys.getsizeof(numbers_gen)} bytes")
```

输出：

```
List memory usage: 8000008 bytes
Generator memory usage: 128 bytes
```

可以看到，生成器仅占用极少的内存，而列表则占用了大量内存。即使我们处理的数据集非常大，生成器的内存消耗也保持在一个较低的水平。

##### 3.3 处理大文件的生成器

生成器在处理大文件时尤其有用。假设我们需要读取一个很大的文本文件，并处理其中的每一行。如果一次性将整个文件加载到内存中，可能会导致内存溢出。使用生成器可以逐行读取文件，从而避免将文件内容全部加载到内存中。

###### 示例：使用生成器逐行读取文件

```
# 生成器逐行读取文件
def read_file_line_by_line(file_name):
    with open(file_name, 'r') as file:
        for line in file:
            yield line.strip()

# 使用生成器读取大文件
file_name = "large_file.txt"
lines = read_file_line_by_line(file_name)

for line in lines:
    print(line)  # 逐行处理文件内容
```

通过生成器，我们可以逐行读取文件，并将内存使用控制在一个较低的水平，而不需要一次性将整个文件加载到内存中。

##### 3.4 无限序列的生成

生成器还可以用来生成无限序列。由于生成器是惰性评估的，只有在请求时才会生成下一个元素，因此它们可以用来表示无限序列，例如斐波那契数列、素数序列等。

###### 示例：生成无限斐波那契数列

```
# 生成斐波那契数列
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# 使用生成器获取斐波那契数列
fib = fibonacci()
for _ in range(10):
    print(next(fib))
```

在这个例子中，我们使用生成器生成无限的斐波那契数列。由于生成器的惰性求值特性，生成器只会在需要时计算下一个斐波那契数，因此我们无需担心内存的消耗。

---

#### 4. 生成器的应用场景

##### 4.1 大规模数据处理

在数据分析、机器学习等领域，我们通常需要处理大规模数据集。如果使用传统的数据结构存

储所有数据，会占用大量内存并导致性能问题。通过使用生成器，我们可以逐步加载和处理数据，避免内存溢出，并提高处理效率。

##### 4.2 流式数据处理

对于实时数据流的处理，生成器是一个非常有效的解决方案。生成器能够按需生成数据，并实时进行处理。这对于流式数据的处理非常有用，例如从网络连接中读取数据、实时日志分析等。

##### 4.3 无限序列生成

生成器非常适合生成无限序列，因为它们只有在请求时才会生成数据，这使得我们能够表示和计算理论上无限的序列，例如斐波那契数列、素数等。

---

#### 5. 总结

本文探讨了如何使用Python的`yield`关键字优化内存使用，重点介绍了生成器的特性和优势。通过使用生成器，我们能够以惰性求值的方式逐步生成数据，避免一次性加载所有数据，从而大大减少内存消耗。生成器在处理大数据、流式数据以及无限序列等场景中表现尤为突出。

通过本文中的示例，您可以更好地理解生成器的使用，并应用它们来优化内存使用，提升程序的性能。在面对大数据集或内存受限的场景时，生成器是Python开发者的一个强大工具，能够帮助我们高效地处理数据。

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

  27

  点赞
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike.png)

  踩
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCollectActive.png)

  26

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

[随着人工智能（AI）技术的迅猛发展，尤其是生成式AI（AIGC），劳动力市场正经历前所未有的变革。从内容创作到自动化生产线，几乎每个行业都在经历一场技术的洗礼。然而，这场革命并不是全然的光明，它带来了深刻的社会变动，也引发了广泛的担忧和不安。我们不得不面对一个核心问题：AIGC将如何影响未来的工作？会让人类的大多数工作消失，还是会创造出全新的职业机会？](https://unitymarvel...
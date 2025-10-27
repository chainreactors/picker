---
title: Python中的字典优化：如何高效使用defaultdict和Counter
url: https://blog.csdn.net/nokiaguy/article/details/144769034
source: 一个被知识诅咒的人
date: 2024-12-28
fetch_date: 2025-10-06T19:37:02.850944
---

# Python中的字典优化：如何高效使用defaultdict和Counter

# Python中的字典优化：如何高效使用defaultdict和Counter

![](https://i-operation.csdnimg.cn/images/cf31225e169b4512917b2e77694eb0a2.png)Python中defaultdict与Counter的高效应用

![](https://csdnimg.cn/release/blogv2/dist/pc/img/original.png)

[蒙娜丽宁](https://unitymarvel.blog.csdn.net "蒙娜丽宁")
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newUpTime2.png)
已于 2025-01-09 16:49:12 修改

![](https://csdnimg.cn/release/blogv2/dist/pc/img/articleReadEyes2.png)
阅读量1.6k
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)
收藏

25

![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)
点赞数
48

CC 4.0 BY-SA版权

分类专栏：
[Python杂谈](https://blog.csdn.net/nokiaguy/category_12800257.html)
文章标签：
[python](https://so.csdn.net/so/search/s.do?q=python&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[开发语言](https://so.csdn.net/so/search/s.do?q=%E5%BC%80%E5%8F%91%E8%AF%AD%E8%A8%80&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

于 2024-12-27 14:42:52 首次发布

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

本文链接：<https://blog.csdn.net/nokiaguy/article/details/144769034>

[![](https://i-blog.csdnimg.cn/columns/default/20201014180756925.png?x-oss-process=image/resize,m_fixed,h_224,w_224)

Python杂谈
专栏收录该内容](https://blog.csdn.net/nokiaguy/category_12800257.html "Python杂谈")

390 篇文章

订阅专栏

在Python编程中，字典（`dict`）是最常用的数据结构之一，用于存储键值对数据。然而，普通字典在处理某些特定任务时可能显得笨重且效率低下。为了解决这些问题，Python标准库提供了两个强大的工具——`defaultdict`和`Counter`，它们分别针对默认值管理和计数任务进行了优化。本文将深入探讨这两个工具的使用方法、应用场景及其在实际项目中的高效应用。通过大量的代码示例和详尽的中文注释，读者将能够全面掌握`defaultdict`和`Counter`的高级用法，提升代码的简洁性和运行效率。此外，本文还将比较这两个工具与普通字典在性能上的差异，帮助开发者在实际项目中做出更明智的选择。

### 引言

在Python编程中，字典（`dict`）作为一种内置的数据结构，以其高效的键值对存储和快速查找能力，广泛应用于各种场景。然而，随着项目复杂度的增加，普通字典在处理默认值和频繁计数任务时，可能需要额外的代码来处理异常情况，如键不存在时的处理。这不仅增加了代码的冗余性，还可能影响代码的可读性和性能。

为了解决这些问题，Python标准库中的`collections`模块提供了两个极具实用价值的工具——`defaultdict`和`Counter`。`defaultdict`通过提供一个默认值工厂函数，简化了字典的默认值处理逻辑；`Counter`则专门用于高效地进行计数操作，简化了频繁计数任务的代码编写。本文将详细介绍这两个工具的使用方法、应用场景，并通过丰富的代码示例，展示它们如何在实际项目中提升代码的效率和可读性。

### 1. Python字典的基本用法

在深入了解`defaultdict`和`Counter`之前，首先回顾一下Python普通字典的基本用法及其在默认值处理和计数任务中的不足。

#### 1.1 字典的基本操作

字典是Python中一种无序的可变容器，存储的是键值对（key-value pairs）。每个键在字典中是唯一的。

**示例代码：**

```
# 创建一个普通字典
student_scores = {
    'Alice': 85,
    'Bob': 92,
    'Charlie': 78
}

# 访问字典中的值
print(student_scores['Alice'])  # 输出: 85

# 添加或更新键值对
student_scores['David'] = 88
student_scores['Alice'] = 90

# 删除键值对
del student_scores['Bob']

# 遍历字典
for student, score in student_scores.items():
    print(f"{student}: {score}")
```

**输出结果：**

```
85
Alice: 90
Charlie: 78
David: 88
```

#### 1.2 字典在默认值处理中的不足

在使用普通字典时，如果访问一个不存在的键，会引发`KeyError`异常。为了避免这种情况，通常需要使用条件语句或`dict.get()`方法进行处理。

**示例代码：**

```
# 使用普通字典进行计数
word_counts = {}

words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

print(word_counts)
```

**输出结果：**

```
{'apple': 3, 'banana': 2, 'orange': 1}
```

上述代码在处理计数任务时，需要频繁地检查键是否存在，这增加了代码的复杂性和冗余。

### 2. `defaultdict`的介绍与使用

`defaultdict`是`collections`模块中的一个子类，它提供了一个工厂函数，用于在访问不存在的键时生成默认值，从而简化了默认值的处理逻辑。

#### 2.1 `defaultdict`的基本用法

要使用`defaultdict`，首先需要导入`collections`模块，然后指定一个工厂函数，该函数将在键不存在时提供默认值。

**示例代码：**

```
from collections import defaultdict

# 使用int作为默认工厂函数，默认值为0
word_counts = defaultdict(int)

words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

for word in words:
    word_counts[word] += 1

print(word_counts)
```

**输出结果：**

```
defaultdict(<class 'int'>, {'apple': 3, 'banana': 2, 'orange': 1})
```

在上述代码中，当访问一个不存在的键时，`defaultdict`会自动调用`int()`生成一个默认值0，然后再进行加1操作。

#### 2.2 常见的默认工厂函数

`defaultdict`的灵活性体现在可以使用任何可调用对象作为默认工厂函数。以下是一些常见的工厂函数及其应用场景：

* `int`: 生成0，适用于计数任务。
* `list`: 生成一个空列表，适用于需要聚合多个值的场景。
* `set`: 生成一个空集合，适用于需要去重的场景。
* `lambda`: 自定义默认值。

**示例代码：**

```
from collections import defaultdict

# 使用list作为默认工厂函数
student_courses = defaultdict(list)

student_courses['Alice'].append('Math')
student_courses['Alice'].append('Science')
student_courses['Bob'].append('English')

print(student_courses)
```

**输出结果：**

```
defaultdict(<class 'list'>, {'Alice': ['Math', 'Science'], 'Bob': ['English']})
```

#### 2.3 `defaultdict`的优点

* **简化代码**：无需频繁检查键是否存在，减少了条件语句的使用。
* **提高可读性**：代码更加简洁明了，易于理解。
* **灵活性高**：可以根据不同的需求选择合适的默认工厂函数。

#### 2.4 示例：使用`defaultdict`进行分组

假设我们有一组学生及其对应的课程信息，需要将学生按照课程进行分组。

**示例代码：**

```
from collections import defaultdict

# 学生及其课程
student_courses = [
    ('Alice', 'Math'),
    ('Bob', 'English'),
    ('Alice', 'Science'),
    ('Bob', 'Math'),
    ('Charlie', 'Science'),
    ('Charlie', 'Math')
]

# 使用defaultdict进行分组
courses = defaultdict(list)

for student, course in student_courses:
    courses[course].append(student)

print(courses)
```

**输出结果：**

```
defaultdict(<class 'list'>, {'Math': ['Alice', 'Bob', 'Charlie'], 'English': ['Bob'], 'Science': ['Alice', 'Charlie']})
```

在这个示例中，`defaultdict(list)`简化了将学生按照课程分组的逻辑，无需手动初始化每个课程对应的列表。

### 3. `Counter`的介绍与使用

`Counter`同样是`collections`模块中的一个子类，专门用于计数任务。它提供了许多便捷的方法，使得频繁的计数操作更加高效和简洁。

#### 3.1 `Counter`的基本用法

`Counter`可以通过传入一个可迭代对象、字典或关键字参数来初始化。

**示例代码：**

```
from collections import Counter

# 通过可迭代对象初始化
words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
word_counts = Counter(words)
print(word_counts)
```

**输出结果：**

```
Counter({'apple': 3, 'banana': 2, 'orange': 1})
```

#### 3.2 `Counter`的常用方法

`Counter`提供了丰富的方法，帮助开发者更方便地进行计数和相关操作。

* `elements()`: 返回一个迭代器，按元素出现的次数生成元素。
* `most_common([n])`: 返回一个列表，列出最常见的n个元素及其计数。
* `subtract()`: 从计数器中减去一个计数器或可迭代对象的计数。
* `update()`: 更新计数器，将新的计数加入现有计数。

**示例代码：**

```
from collections import Counter

# 初始化Counter
word_counts = Counter({'apple': 3, 'banana': 2, 'orange': 1})

# 使用elements()
print(list(word_counts.elements()))  # 输出: ['apple', 'apple', 'apple', 'banana', 'banana', 'orange']

# 使用most_common()
print(word_counts.most_common(2))  # 输出: [('apple', 3), ('banana', 2)]

# 使用subtract()
word_counts.subtract({'apple': 1, 'banana': 1})
print(word_counts)  # 输出: Counter({'apple': 2, 'banana': 1, 'orange': 1})

# 使用update()
word_counts.update(['banana', 'orange', 'orange'])
print(word_counts)  # 输出: Counter({'apple': 2, 'orange': 3, 'banana': 2})
```

#### 3.3 `Counter`的优点

* **简化计数任务**：提供了直接的计数方法，无需手动初始化和更新计数。
* **丰富的方法支持**：内置了多种操作方法，支持元素的统计、排序和更新。
* **高效性**：在处理大规模数据时，`Counter`的性能表现优异。

#### 3.4 示例：使用`Counter`进行词频统计

词频统计是自然语言处理中的基础任务之一，`Counter`在这一任务中表现尤为出色。

**示例代码：**

```
from collections import Counter
import re

# 示例文本
text = """
Python is a versatile programming language. Python is widely used in web development, data analysis, artificial intelligence, and more.
"""

# 使用正则表达式提取单词
words = re.findall(r'\w+', text.lower())

# 使用Counter进行词频统计
word_counts = Counter(words)

print(word_counts)
```

**输出结果：**

```
Counter({'python': 2, 'is': 2, 'a': 1, 'versatile': 1, 'programming': 1, 'language': 1, 'widely': 1, 'used': 1, 'in': 1, 'web': 1, 'development': 1, 'data': 1, 'analysis': 1, 'artificial': 1, 'intelligence': 1, 'and': 1, 'more': 1})
```

### 4. `defaultdict`与`Counter`的性能对比

在实际开发中，选择合适的数据结构不仅影响代码的简洁性，还直接关系到程序的性能。下面我们将通过性能测试，比较`defaultdict`、`Counter`与普通字典在计数任务中的表现。

#### 4.1 测试环境与方法

我们将在相同的环境下，使用普通字典、`defaultdict`和`Counter`分别进行大规模的计数任务，并记录它们的执行时间。

**示例代码：**

```
import time
from collections import defaultdict, Counter

# 生成一个包含100万个随机单词的列表
import random
import string

def generate_random_words(n):
    words = []
    for _ in range(n):
        word = ''.join(random.choices(string.ascii_lowercase, k=5))
        words.append(word)
    return words

words = generate_random_words(1000000)

# 使用普通字典
def count_with_dict(words):
    counts = {}
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

# 使用def...
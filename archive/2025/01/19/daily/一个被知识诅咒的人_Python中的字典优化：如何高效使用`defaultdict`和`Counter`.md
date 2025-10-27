---
title: Python中的字典优化：如何高效使用`defaultdict`和`Counter`
url: https://blog.csdn.net/nokiaguy/article/details/145227999
source: 一个被知识诅咒的人
date: 2025-01-19
fetch_date: 2025-10-06T20:08:08.132007
---

# Python中的字典优化：如何高效使用`defaultdict`和`Counter`

# Python中的字典优化：如何高效使用`defaultdict`和`Counter`

原创
于 2025-01-18 15:22:40 发布
·
1.1k 阅读

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)

19

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)

20
·

CC 4.0 BY-SA版权

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

文章标签：

[#python](https://so.csdn.net/so/search/s.do?q=python&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#javascript](https://so.csdn.net/so/search/s.do?q=javascript&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#前端](https://so.csdn.net/so/search/s.do?q=%E5%89%8D%E7%AB%AF&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

[![](https://i-blog.csdnimg.cn/columns/default/20201014180756925.png?x-oss-process=image/resize,m_fixed,h_224,w_224)

Python杂谈
专栏收录该内容](https://blog.csdn.net/nokiaguy/category_12800257.html "Python杂谈")

390 篇文章

订阅专栏

[《Python OpenCV从菜鸟到高手》带你进入图像处理与计算机视觉的大门！](https://blog.csdn.net/nokiaguy/article/details/143574491)

[解锁Python编程的无限可能：《奇妙的Python》带你漫游代码世界](https://unitymarvel.blog.csdn.net/article/details/141889588)

在Python编程中，字典（`dict`）是最常用的数据结构之一，广泛应用于数据存储、检索和操作。然而，随着数据规模的增大和复杂性的提升，传统字典在某些场景下的性能和便利性显得不足。本文深入探讨了Python标准库中的两个强大工具——`defaultdict`和`Counter`，详细介绍了它们的工作原理、优势以及在实际编程中的高效应用。通过大量的代码示例和详细的中文注释，本文展示了如何利用这两个工具简化代码逻辑、提升执行效率，并解决常见的计数和默认值管理问题。此外，本文还比较了`defaultdict`与`Counter`在不同场景下的适用性，并提供了一些高级优化技巧，帮助读者在实际项目中灵活运用这些工具，实现更高效、更优雅的代码编写。无论是初学者还是有经验的开发者，本文都将为您提供有价值的见解和实用的方法，助力Python编程技能的提升。

### 引言

在Python编程中，字典（`dict`）是一种极为重要的数据结构，因其高效的键值对存储和快速的查找性能而广受欢迎。随着数据处理任务的复杂性增加，传统的字典在处理默认值和计数操作时，往往需要编写额外的逻辑，这不仅增加了代码的复杂度，也可能影响程序的执行效率。为了解决这些问题，Python标准库提供了`collections`模块中的两个强大工具——`defaultdict`和`Counter`，它们分别针对默认值管理和计数操作进行了优化。

本文将深入探讨这两个工具的使用方法和优化技巧，帮助开发者在实际编程中高效地进行字典操作。我们将通过大量的代码示例，详细解释它们的工作原理和应用场景，并提供中文注释以便读者更好地理解和掌握。此外，本文还将比较这两者的异同，探讨在不同场景下的最佳实践，以助力读者编写出更高效、简洁的Python代码。

### `defaultdict`的深入应用

#### 什么是`defaultdict`

`defaultdict`是Python标准库`collections`模块中的一个子类，继承自内置的`dict`类。它的主要特点是在访问不存在的键时，能够自动为该键创建一个默认值，而无需手动进行键存在性的检查。这一特性在处理需要默认值的场景中，极大地简化了代码逻辑，提高了代码的可读性和执行效率。

#### `defaultdict`的工作原理

`defaultdict`的构造函数接受一个工厂函数作为参数，这个工厂函数在创建新的键时被调用，以生成默认值。常见的工厂函数包括`list`、`set`、`int`、`float`等。使用`defaultdict`时，如果访问的键不存在，`defaultdict`会自动调用工厂函数创建一个新的默认值，并将其赋值给该键。

#### 使用示例

下面通过一个简单的例子，展示如何使用`defaultdict`来简化字典操作。

```
from collections import defaultdict

# 使用普通字典统计单词出现次数
word_counts = {}
words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

print("普通字典统计结果：", word_counts)
# 输出: {'apple': 3, 'banana': 2, 'orange': 1}

# 使用defaultdict简化代码
word_counts_dd = defaultdict(int)

for word in words:
    word_counts_dd[word] += 1  # 不需要检查键是否存在

print("defaultdict统计结果：", word_counts_dd)
# 输出: defaultdict(<class 'int'>, {'apple': 3, 'banana': 2, 'orange': 1})
```

在上述例子中，使用`defaultdict(int)`代替了普通字典，在每次访问一个新的键时，自动为其赋值为`0`（因为`int()`返回`0`），从而简化了计数逻辑。

#### `defaultdict`的常见应用场景

1. **分组操作**：将数据按某一特征进行分组，例如按类别、日期等。
2. **多级字典**：创建嵌套字典结构，例如统计二维数据。
3. **自动初始化复杂数据结构**：如列表、集合等作为默认值，便于后续的追加操作。

##### 分组操作示例

假设我们有一组员工数据，包含姓名和部门信息，现需按部门对员工进行分组。

```
from collections import defaultdict

employees = [
    {'name': 'Alice', 'department': 'Engineering'},
    {'name': 'Bob', 'department': 'HR'},
    {'name': 'Charlie', 'department': 'Engineering'},
    {'name': 'David', 'department': 'Marketing'},
    {'name': 'Eve', 'department': 'HR'}
]

# 使用defaultdict进行分组
dept_groups = defaultdict(list)

for employee in employees:
    dept = employee['department']
    dept_groups[dept].append(employee['name'])

print("按部门分组结果：", dept_groups)
# 输出: defaultdict(<class 'list'>, {'Engineering': ['Alice', 'Charlie'], 'HR': ['Bob', 'Eve'], 'Marketing': ['David']})
```

在此示例中，`defaultdict(list)`确保每个新部门都有一个空列表作为默认值，便于直接调用`append`方法添加员工姓名。

##### 多级字典示例

假设需要统计不同年份、不同月份的销售数据。

```
from collections import defaultdict

# 创建一个两级defaultdict
sales_data = defaultdict(lambda: defaultdict(int))

# 模拟一些销售记录
records = [
    {'year': 2023, 'month': 1, 'amount': 1500},
    {'year': 2023, 'month': 2, 'amount': 2000},
    {'year': 2023, 'month': 1, 'amount': 1800},
    {'year': 2024, 'month': 1, 'amount': 2200},
    {'year': 2024, 'month': 3, 'amount': 1700},
]

for record in records:
    year = record['year']
    month = record['month']
    amount = record['amount']
    sales_data[year][month] += amount

print("多级字典销售数据：")
for year, months in sales_data.items():
    for month, total in months.items():
        print(f"Year {year}, Month {month}: {total}")
```

输出：

```
多级字典销售数据：
Year 2023, Month 1: 3300
Year 2023, Month 2: 2000
Year 2024, Month 1: 2200
Year 2024, Month 3: 1700
```

在这个例子中，使用`defaultdict`的嵌套结构方便地统计了不同年份和月份的销售总额，无需手动初始化每个子字典。

#### `defaultdict`的高级用法

`defaultdict`不仅限于简单的数据结构初始化，还可以用于创建更加复杂的嵌套结构。

##### 创建三级嵌套字典

```
from collections import defaultdict

# 创建一个三级defaultdict
def recursive_defaultdict():
    return defaultdict(recursive_defaultdict)

nested_dict = defaultdict(recursive_defaultdict)

# 添加数据
nested_dict['level1']['level2']['level3'] = 'deep_value'

print("三级嵌套字典：", nested_dict)
# 输出: defaultdict(<function recursive_defaultdict at 0x...>, {'level1': defaultdict(<function recursive_defaultdict at 0x...>, {'level2': defaultdict(<function recursive_defaultdict at 0x...>, {'level3': 'deep_value'})})})
```

通过递归地定义`defaultdict`，可以轻松创建多级嵌套的字典结构，适用于复杂的数据存储需求。

#### `defaultdict`与普通字典的性能对比

在需要频繁检查键是否存在并进行初始化的场景中，`defaultdict`相较于普通字典具有明显的性能优势。通过减少条件判断和初始化代码，`defaultdict`不仅使代码更简洁，还能提高执行效率。

下面通过一个简单的性能测试，比较`defaultdict`与普通字典在统计单词频率时的性能差异。

```
import time
from collections import defaultdict

# 生成一个包含大量单词的列表
words = ['word{}'.format(i) for i in range(100000)] + ['common'] * 100000

# 使用普通字典
start_time = time.time()
word_counts = {}
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1
end_time = time.time()
print("普通字典计数时间：{:.4f}秒".format(end_time - start_time))

# 使用defaultdict
start_time = time.time()
word_counts_dd = defaultdict(int)
for word in words:
    word_counts_dd[word] += 1
end_time = time.time()
print("defaultdict计数时间：{:.4f}秒".format(end_time - start_time))
```

输出示例：

```
普通字典计数时间：0.0456秒
defaultdict计数时间：0.0321秒
```

从测试结果可以看出，`defaultdict`在处理大量数据时，性能更优。这主要得益于其内部优化的默认值处理机制，减少了条件判断的开销。

### `Counter`的深入应用

#### 什么是`Counter`

`Counter`同样是Python标准库`collections`模块中的一个类，专门用于计数可哈希对象。它是一个子类，继承自`dict`，提供了快速、简洁的方式来进行元素计数和频率分析。`Counter`不仅支持常规的字典操作，还提供了许多有用的方法，如`most_common`、`elements`等，极大地简化了计数相关的操作。

#### `Counter`的工作原理

`Counter`内部维护了一个字典，其中键为待计数的元素，值为对应的计数。它提供了便捷的接口来更新计数、合并计数器以及进行数学运算，如加法、减法、交集和并集等。`Counter`还支持直接从可迭代对象初始化，自动完成元素的计数。

#### 使用示例

以下示例展示了如何使用`Counter`来统计元素的出现次数，并利用其内置方法进行分析。

```
from collections import Counter

# 统计单词出现次数
words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
word_counts = Counter(words)

print("Counter统计结果：", word_counts)
# 输出: Counter({'apple': 3, 'banana': 2, 'orange': 1})

# 获取出现次数最多的两个单词
most_common_two = word_counts.most_common(2)
print("出现次数最多的两个单词：", most_common_two)
# 输出: [('apple', 3), ('banana', 2)]
```

#### `Counter`的常见应用场景

1. **文本分析**：统计单词或字符的频率，进行词云生成、关键词提取等。
2. **数据清洗**：识别数据中的异常值或高频项，辅助数据清洗和预处理。
3. **推荐系统**：基于用户行为数据统计物品的流行度，辅助推荐算法。
4. **统计分析**：在科学计算和统计分析中，用于快速统计实验数据或观测值的分布。

##### 文本分析示例

假设需要对一段文本进行单词频率统计，以生成词云。

```
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud

text = """
Python is a high-level, interpreted, general-purpose programming language.
Its design philosophy emphasizes code readability with the use of significant indentation.
"""

# 分词
words = text.lower().split()

# 统计单词频率
word_counts = Counter(words)

# 生成词云
wordcloud = WordCloud(width=800, height=400, background_col...
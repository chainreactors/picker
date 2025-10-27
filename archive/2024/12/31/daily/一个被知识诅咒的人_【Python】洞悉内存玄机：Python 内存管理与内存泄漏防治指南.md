---
title: 【Python】洞悉内存玄机：Python 内存管理与内存泄漏防治指南
url: https://blog.csdn.net/nokiaguy/article/details/144822873
source: 一个被知识诅咒的人
date: 2024-12-31
fetch_date: 2025-10-06T19:38:05.323447
---

# 【Python】洞悉内存玄机：Python 内存管理与内存泄漏防治指南

# 【Python】洞悉内存玄机：Python 内存管理与内存泄漏防治指南

原创
已于 2025-01-09 16:48:03 修改
·
946 阅读

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)

20

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)

10
·

CC 4.0 BY-SA版权

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

文章标签：

[#python](https://so.csdn.net/so/search/s.do?q=python&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#开发语言](https://so.csdn.net/so/search/s.do?q=%E5%BC%80%E5%8F%91%E8%AF%AD%E8%A8%80&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

于 2024-12-30 13:00:17 首次发布

[![](https://i-blog.csdnimg.cn/columns/default/20201014180756925.png?x-oss-process=image/resize,m_fixed,h_224,w_224)

Python杂谈
专栏收录该内容](https://blog.csdn.net/nokiaguy/category_12800257.html "Python杂谈")

390 篇文章

订阅专栏

内存管理是任何程序设计中至关重要的一个方面，尤其是在长时间运行的应用程序中。Python 作为一种动态类型的解释型语言，其内存管理机制相对复杂，但也提供了一系列工具和技术来帮助开发者有效地管理内存。本文将深入剖析 Python 的内存管理机制，包括引用计数、垃圾回收（包括标记-清除和分代回收），以及内存池等关键概念。重点讲解如何检测和避免 Python 程序中常见的内存泄漏问题，并提供大量的代码示例和最佳实践，帮助开发者更好地理解 Python 的内存管理机制，提升程序的稳定性和性能，从而写出更加健壮的应用程序。本文还将讨论一些内存分析工具，帮助读者更好地定位内存泄漏问题。

#### 1. Python 的内存管理机制概述

Python 使用自动内存管理，这意味着开发者不需要像 C 或 C++ 那样手动分配和释放内存。Python 的内存管理主要依赖于以下几个机制：

* **引用计数（Reference Counting）：** 这是最基本的内存管理机制。每个对象都有一个引用计数器，记录着有多少个变量引用了该对象。当引用计数变为 0 时，对象所占用的内存就会被释放。
* **垃圾回收（Garbage Collection）：** 为了解决引用计数无法处理的循环引用问题，Python 引入了垃圾回收机制。垃圾回收器会定期检查不再使用的对象，并释放它们占用的内存。垃圾回收又包含标记-清除和分代回收两种算法。
* **内存池（Memory Pools）：** Python 为了提高内存分配的效率，引入了内存池机制。对于小对象，Python 会使用内存池进行分配，避免频繁地调用操作系统的内存分配函数。

#### 2. 引用计数

每个 Python 对象都维护着一个引用计数器 `Py_REFCNT`。当创建一个新对象时，其引用计数被初始化为 1。当有新的变量引用该对象时，引用计数加 1。当对象的引用被删除或超出作用域时，引用计数减 1。当引用计数变为 0 时，Python 解释器会自动释放该对象所占用的内存。

```
import sys

a = [1, 2, 3]  # 创建列表对象，引用计数为 1
print(sys.getrefcount(a))  # 输出：2 (因为getrefcount也会增加一次计数)

b = a  # b 也引用了该列表对象，引用计数变为 2
print(sys.getrefcount(a))  # 输出：3

del a  # 删除 a 的引用，引用计数变为 2
print(sys.getrefcount(b))# 输出：2

del b # 删除 b 的引用,此时没有其他对象指向该列表对象，引用计数变为0，内存被回收
#print(sys.getrefcount(b)) #如果此处继续调用会报错，因为对象已经被回收
```

#### 3. 垃圾回收

引用计数虽然简单高效，但无法解决循环引用的问题。例如：

```
class Node:
    def __init__(self):
        self.next = None

a = Node()
b = Node()
a.next = b
b.next = a

del a
del b
```

在这个例子中，`a` 和 `b` 互相引用，即使删除了 `a` 和 `b` 变量，它们的引用计数仍然为 1，导致它们所占用的内存无法被释放，造成内存泄漏。

为了解决这个问题，Python 引入了垃圾回收机制，它主要使用两种算法：

* **标记-清除（Mark and Sweep）：** 垃圾回收器会从根对象（例如全局变量、栈上的变量）开始遍历所有对象，标记所有可达的对象。然后，清除所有未被标记的对象。
* **分代回收（Generational Collection）：** 基于“大部分对象的生命周期都很短”的假设，Python 将对象分为三代：0 代、1 代和 2 代。新创建的对象属于 0 代。垃圾回收器会更频繁地检查 0 代的对象，如果对象经过多次检查仍然存活，就会被移到下一代。这样可以提高垃圾回收的效率。

可以通过 `gc` 模块来控制垃圾回收：

```
import gc

# 启用垃圾回收
gc.enable()

# 手动执行一次垃圾回收
gc.collect()

# 获取垃圾回收器的统计信息
print(gc.get_stats())

#获取当前自动执行垃圾回收的频率
print(gc.get_threshold())#返回一个元组，(700, 10, 10),意思是 0代达到700个对象时进行垃圾回收，此后1代达到10次0代回收，则触发一次1代回收，2代同理。
```

#### 4. 内存池

Python 为了提高小对象的分配效率，引入了内存池机制。Python 会预先分配一大块内存，然后将其分割成小的内存块，用于分配给小对象。这样可以避免频繁地调用操作系统的内存分配函数，减少内存分配的开销。对于大于256kb的对象，则会直接使用malloc进行分配。

Python 的内存管理机制可以概括为以下几个层次：

1. **第0层：** `malloc` 和 `free` 等操作系统提供的内存分配和释放函数。
2. **第1层：** Python 内存分配器，负责在操作系统的基础上进行内存管理，例如使用内存池分配小对象。
3. **第2层：** 对象分配器，负责分配 Python 对象所需的内存。
4. **第3层：** 用户代码。

#### 5. 如何检测内存泄漏

检测内存泄漏的方法有很多，常用的包括：

* **手动检查：** 通过观察程序的内存占用情况来判断是否存在内存泄漏。可以使用操作系统的工具（例如 Windows 的任务管理器、Linux 的 top 命令）或 Python 的 `psutil` 模块来获取进程的内存占用信息。

```
import psutil
import os
process = psutil.Process(os.getpid())
print(process.memory_info().rss) # 内存占用，单位是字节
```

* **使用 `tracemalloc` 模块（Python 3.4+）：** `tracemalloc` 模块可以跟踪 Python 程序的内存分配情况，并提供统计信息，帮助我们定位内存泄漏的位置。

```
import tracemalloc

tracemalloc.start()

# 执行一些代码
a = [i for i in range(1000000)]

snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('lineno')

for stat in top_stats[:10]:
    print(stat)

tracemalloc.stop()
```

* **使用 `objgraph` 库：** `objgraph` 库可以生成对象之间的引用关系图，帮助我们分析循环引用等问题。

```
#需要先安装 objgraph: pip install objgraph
import objgraph
import gc

class Node:
    def __init__(self):
        self.next = None
a = Node()
b = Node()
a.next = b
b.next = a
del a
del b
gc.collect()
objgraph.show_backrefs([objgraph.by_type('Node')], filename='sample-graph.png') #会将对象关系图保存到sample-graph.png文件中
```

* **使用内存分析工具：** 一些专业的 Python 内存分析工具，例如 `memory_profiler`、`filprofiler` 等，可以提供更详细的内存分析报告。

#### 6. 如何避免内存泄漏

避免内存泄漏的最佳实践包括：

* **避免循环引用：** 这是最常见的内存泄漏原因。在设计类和数据结构时，应该尽量避免循环引用。如果无法避免，可以使用弱引用（weakref）来打破循环引用。

```
import weakref

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

a = Node(1)
b = Node(2)
a.next = weakref.ref(b) # 使用 weakref.ref 创建弱引用
b.next = weakref.ref(a)

print(a.next()) # 通过调用弱引用获取对象，输出 <weakref at 0x...>，实际对象存在
del b #删除b，由于是弱引用，不会阻止b被回收
print(a.next()) # b 对象已经被删除，弱引用返回 None

#循环引用导致内存泄漏的例子
class Node_leak:
    def __init__(self,data):
        self.data = data
        self.next = None
a_leak = Node_leak(1)
b_leak = Node_leak(2)
a_leak.next = b_leak
b_leak.next = a_leak
del a_leak
del b_leak #此时a_leak和b_leak对象由于循环引用，无法被回收，造成内存泄漏
import gc
gc.collect() #手动调用垃圾回收，也无法回收循环引用的对象
```

* **及时关闭文件和网络连接：** 打开的文件和网络连接会占用系统资源，包括内存。应该在使用完毕后及时关闭它们。可以使用 `with` 语句来自动关闭文件和连接。

```
with open('file.txt', 'w',encoding='utf-8') as f: #使用encoding指定编码，防止中文乱码
    f.write("这是一段测试文本") # 处理文件
    #with语句块结束后会自动关闭文件
    print(f.closed) #输出True，表明文件已经关闭
try:
    f = open('file.txt','r',encoding = 'utf-8')
    print(f.read())
finally:
    f.close() #无论是否发生异常，finally语句块中的代码都会被执行，确保文件被关闭
print(f.closed)

import socket
try:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(('www.baidu.com',80))
    s.send(b'GET / HTTP/1.1\r\nHost: www.baidu.com\r\nConnection: close\r\n\r\n')
    data = s.recv(1024)
    print(data)
finally:
    s.close()
```

* **避免创建大量临时对象：** 大量临时对象的创建和销毁会增加垃圾回收的负担，影响程序的性能。应该尽量重用对象，避免不必要的创建。特别是字符串的拼接，如果使用`+`号进行大量的字符串拼接，会产生大量的临时字符串对象，造成性能下降。推荐使用`join`方法或者f-string进行字符串拼接。

```
import time
start_time = time.time()
test_str = ''
for i in range(100000):
    test_str +='test'
end_time = time.time()
print(f'使用+号拼接字符串耗时：{end_time - start_time}')
start_time = time.time()
test_list = []
for i in range(100000):
    test_list.append('test')
test_str_join = ''.join(test_list)
end_time = time.time()
print(f'使用join拼接字符串耗时：{end_time - start_time}')
start_time = time.time()
test_str_f = ''.join(f'test' for i in range(100000))
end_time = time.time()
print(f'使用f-string和join拼接字符串耗时：{end_time - start_time}')
```

* **使用生成器和迭代器：** 生成器和迭代器可以按需生成数据，而不是一次性加载所有数据到内存中，从而有效地减少内存占用。

```
def fibonacci(n): #生成器函数
    a, b = 0, 1
    for _ in range(n):
        yield b
        a, b = b, a + b

for num in fibonacci(10):
    print(num)

#使用列表的实现，会占用更多的内存
def fibonacci_list(n):
    result = []
    a, b = 0,1
    for _ in range(n):
        result.append(b)
        a,b = b, a+b
    return result

for num in fibonacci_list(10):
    print(num)
```

* **使用 `__slots__` 限制实例属性：** 默认情况下，Python 对象的实例使用 `__dict__` 字典来存储属性。如果一个类有大量的实例，这会占用大量的内存。可以使用 `__slots__` 限制实例可以拥有的属性，从而减少内存占用。

```
class MyClass:
    __slots__ = ('name', 'age')

    def __init__(self, name, age):
        self.name = name
        self.age = age

obj = MyClass("test",20)
#obj.address = 'beijing' #如果尝试添加__slots__中没有声明的属性，则会报错

print(obj.__dict__ if hasattr(obj,'__dict__') else "对象没有__dict__属性") #因为使用了__slots__，对象不再有__dict__属性
```

* **合理使用上下文管理器：** 除了文件操作，上下文管理器还可以用于其他资源的自动管理，例如数据库连接、锁等。

```
import contextlib

@contextlib.contextmanager
def managed_resource():
    # 获取资源
    print("获取资源")
    resource = "my_resource"
    try:
        yield resource  # 将资源提供给调用者
    finally:
        # 释放资源
        print("释放资源")

with managed_resource() as res:
    print(f"使用资源：{res}")
```

* **使用适当的数据结构：** 选择合适的数据结构可以有效地减少内存占用。例如，如果只需要存储一组唯一的元素，可以使用 `set` 而不是 `list`。
* **避免在全局变量中存储大量数据：** 全局变量的生命周期很长，会一直占用内存。如果需要在多个函数之间共享数据，可以考虑使用其他方式，例如函数参数传递或类属性。
* **手动调用 `gc.collect()`：**...
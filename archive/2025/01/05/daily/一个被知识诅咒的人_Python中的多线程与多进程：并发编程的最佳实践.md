---
title: Python中的多线程与多进程：并发编程的最佳实践
url: https://blog.csdn.net/nokiaguy/article/details/144928512
source: 一个被知识诅咒的人
date: 2025-01-05
fetch_date: 2025-10-06T20:07:14.914865
---

# Python中的多线程与多进程：并发编程的最佳实践

# Python中的多线程与多进程：并发编程的最佳实践

原创
已于 2025-01-09 16:45:39 修改
·
1.3k 阅读

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)

16

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)

18
·

CC 4.0 BY-SA版权

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

文章标签：

[#python](https://so.csdn.net/so/search/s.do?q=python&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#开发语言](https://so.csdn.net/so/search/s.do?q=%E5%BC%80%E5%8F%91%E8%AF%AD%E8%A8%80&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

于 2025-01-04 13:13:30 首次发布

[![](https://i-blog.csdnimg.cn/columns/default/20201014180756925.png?x-oss-process=image/resize,m_fixed,h_224,w_224)

Python杂谈
专栏收录该内容](https://blog.csdn.net/nokiaguy/category_12800257.html "Python杂谈")

390 篇文章

订阅专栏

随着计算机硬件性能的提升和应用需求的日益复杂，如何高效利用系统资源成为开发者关注的焦点。Python作为一门广泛应用的编程语言，提供了多种并发编程模型，其中多线程和多进程是最为常用的两种方式。本文深入探讨了Python中的多线程与多进程，详细介绍了它们各自的工作原理、适用场景以及在实际应用中的优缺点。通过对比分析、丰富的代码示例和详尽的中文注释，本文旨在帮助开发者理解并掌握如何在不同的任务类型下选择合适的并发模型。此外，文章还涵盖了Python中的全局解释器锁（GIL）对多线程性能的影响，并介绍了如何通过异步编程（asyncio）进一步优化并发策略。无论是初学者还是有经验的开发者，都能从中获得实用的指导和启发，以提升代码的执行效率和系统的整体性能。

### 引言

在现代计算机科学中，并发编程已成为提升程序性能和响应速度的重要手段。通过并发执行多个任务，程序可以更高效地利用系统资源，尤其是在多核处理器和分布式系统的环境下。Python作为一门功能强大且易于学习的编程语言，提供了多种并发编程模型，包括多线程、多进程以及异步编程等。然而，选择合适的并发模型并非易事，特别是在面对不同类型的任务（如I/O密集型和CPU密集型）时。本文将重点探讨Python中的多线程与多进程，比较它们的适用场景，并提供实用的代码示例，帮助开发者在实际项目中做出明智的选择。

### 并发编程基础

#### 并发与并行的区别

在讨论并发编程之前，理解并发（Concurrency）与并行（Parallelism）的区别至关重要：

* **并发**：指的是系统能够处理多个任务，但这些任务可能并不同时执行，而是在时间上交替进行。例如，在单核处理器上，通过快速切换任务，使得多个任务看起来同时在进行。
* **并行**：指的是系统能够同时执行多个任务，通常依赖于多核处理器或多台计算机。每个任务在不同的处理器核心上独立运行。

#### 为什么需要并发

并发编程的主要目的是提高程序的执行效率和响应能力。具体优势包括：

1. **提高吞吐量**：通过并发执行多个任务，可以在相同的时间内完成更多的工作。
2. **提升响应速度**：在用户界面应用中，使用并发可以确保界面保持响应，即使后台有耗时操作。
3. **更好地利用多核处理器**：现代计算机通常配备多核处理器，合理的并发策略可以充分利用这些资源。

### Python中的并发模型

Python提供了多种并发编程模型，主要包括多线程（Threading）和多进程（Multiprocessing），此外还有异步编程（Asyncio）。本文将重点比较多线程与多进程的适用场景及其优缺点。

#### 线程（Threading）

线程是轻量级的执行单元，同一进程中的多个线程共享内存空间。Python通过`threading`模块提供对多线程编程的支持。

#### 进程（Multiprocessing）

进程是独立的执行单元，每个进程有自己独立的内存空间。Python通过`multiprocessing`模块提供对多进程编程的支持。

### Python中的全局解释器锁（GIL）

在深入讨论多线程与多进程之前，了解Python中的全局解释器锁（Global Interpreter Lock, GIL）是非常必要的。GIL是CPython解释器中的一个机制，它确保在任何时候只有一个线程在执行Python字节码。这意味着，即使在多核处理器上，多线程程序在执行CPU密集型任务时，实际的并行性也受到限制。

GIL 的存在使得多线程在 CPU 密集型任务中无法充分利用多核优势，但在 I/O 密集型任务中，多线程仍然能带来性能提升。
\text{GIL 的存在使得多线程在 CPU 密集型任务中无法充分利用多核优势，但在 I/O 密集型任务中，多线程仍然能带来性能提升。}
GIL 的存在使得多线程在 CPU 密集型任务中无法充分利用多核优势，但在 I/O 密集型任务中，多线程仍然能带来性能提升。

由于GIL的存在，多进程成为Python在执行CPU密集型任务时的更优选择，因为每个进程都有自己的Python解释器和GIL，不同进程之间可以真正实现并行执行。

### 多线程详解

#### 适用场景

多线程适用于I/O密集型任务，例如网络请求、文件读写、数据库操作等。在这些场景中，线程可以在等待I/O操作完成时切换到其他任务，从而提高整体的执行效率。

#### 示例代码

下面是一个使用多线程执行I/O密集型任务的示例，该示例模拟了多个网络请求的并发执行。

```
import threading
import time

# 模拟I/O密集型任务
def io_bound_task(task_id, sleep_time):
    print(f"任务 {task_id} 开始，睡眠 {sleep_time} 秒")
    time.sleep(sleep_time)
    print(f"任务 {task_id} 完成")

# 创建并启动多个线程
threads = []
for i in range(5):
    t = threading.Thread(target=io_bound_task, args=(i+1, 2))
    threads.append(t)
    t.start()

# 等待所有线程完成
for t in threads:
    t.join()

print("所有I/O任务完成")
```

**代码解释：**

1. **定义任务函数**：`io_bound_task`函数模拟了一个I/O密集型任务，通过`sleep_time`参数模拟I/O操作的等待时间。
2. **创建线程**：通过循环创建5个线程，每个线程执行`io_bound_task`函数，并传入不同的任务ID和睡眠时间。
3. **启动线程**：调用`start()`方法启动每个线程。
4. **等待线程完成**：使用`join()`方法等待所有线程完成。
5. **输出结果**：所有任务完成后，打印提示信息。

**输出示例：**

```
任务 1 开始，睡眠 2 秒
任务 2 开始，睡眠 2 秒
任务 3 开始，睡眠 2 秒
任务 4 开始，睡眠 2 秒
任务 5 开始，睡眠 2 秒
任务 1 完成
任务 2 完成
任务 3 完成
任务 4 完成
任务 5 完成
所有I/O任务完成
```

#### 多线程同步与锁

在多线程编程中，多个线程可能会访问共享资源，这就需要同步机制来防止数据竞争和不一致性。Python提供了多种同步机制，如锁（Lock）、条件变量（Condition）、信号量（Semaphore）等。

下面是一个使用锁来同步线程访问共享资源的示例。

```
import threading

# 共享资源
counter = 0
# 创建锁
lock = threading.Lock()

def increment_counter():
    global counter
    for _ in range(100000):
        # 获取锁
        lock.acquire()
        try:
            counter += 1
        finally:
            # 释放锁
            lock.release()

# 创建多个线程
threads = []
for _ in range(10):
    t = threading.Thread(target=increment_counter)
    threads.append(t)
    t.start()

# 等待所有线程完成
for t in threads:
    t.join()

print(f"最终计数器的值: {counter}")
```

**代码解释：**

1. **共享资源**：定义一个全局变量`counter`作为共享资源。
2. **创建锁**：使用`threading.Lock()`创建一个锁对象`lock`。
3. **定义任务函数**：`increment_counter`函数每次增加`counter`的值，并在修改前后获取和释放锁，以确保线程安全。
4. **创建线程**：创建10个线程，每个线程执行`increment_counter`函数。
5. **启动线程**：调用`start()`方法启动每个线程。
6. **等待线程完成**：使用`join()`方法等待所有线程完成。
7. **输出结果**：打印最终的计数器值。

**输出示例：**

```
最终计数器的值: 1000000
```

#### 使用上下文管理器简化锁的使用

为了简化锁的获取和释放，Python提供了上下文管理器（`with`语句）来自动管理锁的生命周期。以下是使用上下文管理器重写上述示例的代码。

```
import threading

# 共享资源
counter = 0
# 创建锁
lock = threading.Lock()

def increment_counter():
    global counter
    for _ in range(100000):
        with lock:
            counter += 1

# 创建多个线程
threads = []
for _ in range(10):
    t = threading.Thread(target=increment_counter)
    threads.append(t)
    t.start()

# 等待所有线程完成
for t in threads:
    t.join()

print(f"最终计数器的值: {counter}")
```

**代码解释：**

使用`with lock:`语句可以自动获取和释放锁，避免手动调用`acquire()`和`release()`，使代码更简洁且更不易出错。

### 多进程详解

#### 适用场景

多进程适用于CPU密集型任务，例如图像处理、科学计算、大规模数据分析等。在这些场景中，每个进程可以在不同的CPU核心上独立执行，真正实现并行计算，绕过GIL的限制，从而充分利用多核处理器的性能。

#### 示例代码

下面是一个使用多进程执行CPU密集型任务的示例，该示例计算多个大整数的阶乘。

```
import multiprocessing
import math
import time

# CPU密集型任务
def compute_factorial(n):
    print(f"进程 {multiprocessing.current_process().name} 开始计算 {n} 的阶乘")
    result = math.factorial(n)
    print(f"进程 {multiprocessing.current_process().name} 完成计算 {n} 的阶乘")
    return result

if __name__ == "__main__":
    numbers = [100000, 200000, 300000, 400000, 500000]
    start_time = time.time()

    # 创建进程池
    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(compute_factorial, numbers)

    end_time = time.time()
    print(f"所有任务完成，总耗时: {end_time - start_time:.2f} 秒")
```

**代码解释：**

1. **定义任务函数**：`compute_factorial`函数计算给定数字的阶乘，并打印进程信息。
2. **主程序**：在`if __name__ == "__main__":`保护下执行，避免Windows系统下的递归启动问题。
3. **任务列表**：定义一个包含多个大整数的列表`numbers`。
4. **创建进程池**：使用`multiprocessing.Pool`创建一个进程池，指定最多同时运行4个进程。
5. **分配任务**：使用`pool.map`方法将任务分配给进程池中的进程。
6. **记录时间**：计算任务执行的总耗时，并打印结果。

**输出示例：**

```
进程 ForkPoolWorker-1 开始计算 100000 的阶乘
进程 ForkPoolWorker-2 开始计算 200000 的阶乘
进程 ForkPoolWorker-3 开始计算 300000 的阶乘
进程 ForkPoolWorker-4 开始计算 400000 的阶乘
进程 ForkPoolWorker-1 完成计算 100000 的阶乘
进程 ForkPoolWorker-1 开始计算 500000 的阶乘
进程 ForkPoolWorker-2 完成计算 200000 的阶乘
进程 ForkPoolWorker-3 完成计算 300000 的阶乘
进程 ForkPoolWorker-4 完成计算 400000 的阶乘
进程 ForkPoolWorker-1 完成计算 500000 的阶乘
所有任务完成，总耗时: 30.45 秒
```

#### 多进程中的进程间通信

在多进程编程中，不同进程之间的通信（Inter-Process Communication, IPC）是一个重要的问题。Python的`multiprocessing`模块提供了多种IPC机制，如队列（Queue）、管道（Pipe）等。

以下是使用队列在进程间传递数据的示例。

```
import multiprocessing
import time

def producer(queue, items):
    for item in items:
        print(f"生产者生产: {item}")
        queue.put(item)
        time.sleep(1)
    queue.put(None)  # 发送结束信号

def consumer(queue):
    while True:
        item = queue.get()
        if item is None:
            break
        print(f"消费者消费: {item}")
    print("消费者结束")

if __name__ == "__main__":
    q = multiprocessing.Queue()
    items_to_produce = ['苹果', '香蕉', '橙子', '葡萄']

    p = multiprocessing.Process(target=producer, args=(q, items_to_produce))
    c = multiprocessing.Process(target=consumer, args=(q,))

    p.start()
    c.start()

    p.join()
    c.join()
```

**代码解释：**

1. **生产者函数**：`producer`函数将商品放入队列，每生产一个商品后休眠1秒，并在所有商品生产完毕后放入一个`None`作为结束信号。
2. **消费者函数**：`consumer`函数从队列中获取商品，直到接收到`None`信号才停止。
3. **主程序**：创建一个`Queue`对象，并分别启动生产者和消费者进程，最后等待它们完成。

**输出示例：**

```
生产者生产: 苹果
消费者消费: 苹果
生产者生产: 香蕉
消费者消费: 香蕉
生产者生产: 橙子
消费者消费: 橙子
生产者生产: 葡萄
消费者消费: 葡萄
消费者结束
```

#### 使用共享内存

有时，多个进程需要共享数据，这可以通过共享内存（Value、Array）来实现。以下是一个使用共享内存共享计数器的示例。

```
imp...
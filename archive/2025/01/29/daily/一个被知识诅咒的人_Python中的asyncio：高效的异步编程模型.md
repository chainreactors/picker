---
title: Python中的asyncio：高效的异步编程模型
url: https://blog.csdn.net/nokiaguy/article/details/145386296
source: 一个被知识诅咒的人
date: 2025-01-29
fetch_date: 2025-10-06T20:06:16.171125
---

# Python中的asyncio：高效的异步编程模型

# Python中的asyncio：高效的异步编程模型

原创
[![](https://csdnimg.cn/release/blogv2/dist/pc/img/identityVipNew.png)](https://mall.csdn.net/vip)
于 2025-01-28 10:35:48 发布
·
1.2k 阅读

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)

9

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)

28
·

CC 4.0 BY-SA版权

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

文章标签：

[#python](https://so.csdn.net/so/search/s.do?q=python&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#开发语言](https://so.csdn.net/so/search/s.do?q=%E5%BC%80%E5%8F%91%E8%AF%AD%E8%A8%80&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

[《Python OpenCV从菜鸟到高手》带你进入图像处理与计算机视觉的大门！](https://blog.csdn.net/nokiaguy/article/details/143574491)

[解锁Python编程的无限可能：《奇妙的Python》带你漫游代码世界](https://unitymarvel.blog.csdn.net/article/details/141889588)

随着互联网应用的迅猛发展，对高并发、高性能的需求日益增加。Python 作为广泛应用的编程语言，其原生的同步编程模型在处理I/O密集型任务时往往面临性能瓶颈。为了解决这一问题，Python 提供了 `asyncio` 库，旨在实现高效的异步编程。本文将深入探讨 `asyncio` 的核心概念、事件循环、协程、任务调度等关键技术，结合丰富的代码示例和详细的中文注释，全面解析如何利用 `asyncio` 提升程序的响应性和处理能力。通过对比传统同步编程模型，展示 `asyncio` 在处理大规模并发任务中的优势，并介绍实际应用中的最佳实践和优化策略。无论是初学者还是有经验的开发者，本文都将为您提供系统性的指导，助力您在Python异步编程领域取得突破。

### 引言

在现代软件开发中，随着用户需求的多样化和复杂性的增加，应用程序需要处理大量的并发请求，尤其是在Web开发、网络爬虫、实时数据处理等领域。传统的同步编程模型在处理I/O密集型任务时，往往因为阻塞操作而导致资源利用率低下，影响程序的整体性能和响应速度。为了解决这一问题，Python 引入了 `asyncio` 库，提供了一种基于协程的异步编程模型，使开发者能够编写高效、可扩展的并发程序。

`asyncio` 库自 Python 3.4 版本引入以来，已经成为实现异步编程的标准工具。它不仅简化了异步代码的编写方式，还通过事件循环机制有效地管理和调度并发任务，提高了程序的执行效率。本文将系统性地介绍 `asyncio` 的核心组件和工作原理，并通过实际代码示例展示其在处理I/O密集型任务中的应用。

### 1. 异步编程概述

#### 1.1 同步与异步编程

在同步编程模型中，程序按照顺序执行，每一步操作需要等待前一步完成才能继续。这种模型在处理计算密集型任务时表现良好，但在面对I/O密集型任务时，由于I/O操作的不可预测性和潜在的延迟，程序的整体性能可能受到严重影响。

相比之下，异步编程允许程序在等待I/O操作完成的同时，继续执行其他任务，从而更有效地利用系统资源，提高程序的吞吐量和响应速度。异步编程通过事件循环、回调函数和协程等机制，实现了非阻塞的任务调度和执行。

#### 1.2 `asyncio` 的作用

`asyncio` 是 Python 标准库中的一个模块，专门用于编写异步代码。它提供了事件循环、协程、任务和未来对象等核心组件，帮助开发者管理和调度并发任务。通过 `asyncio`，开发者可以编写出高效的异步应用，尤其适用于需要处理大量并发连接或I/O操作的场景，如Web服务器、实时数据处理系统等。

### 2. `asyncio` 的核心概念

#### 2.1 协程（Coroutine）

协程是 `asyncio` 的基本执行单元，是一种比线程更轻量级的并发方式。与传统的线程不同，协程由程序控制调度，避免了线程切换的开销。Python 中的协程通过 `async` 和 `await` 关键字实现。

```
import asyncio

async def say_hello():
    print("Hello, asyncio!")

# 运行协程
asyncio.run(say_hello())
```

在上述代码中，`say_hello` 是一个协程函数，通过 `async def` 定义。调用 `asyncio.run` 方法可以执行该协程。

#### 2.2 事件循环（Event Loop）

事件循环是 `asyncio` 的核心机制，负责调度和管理所有的异步任务。它不断地从任务队列中取出可执行的任务，并在任务完成时处理其回调函数。

```
import asyncio

async def say_after(delay, message):
    await asyncio.sleep(delay)
    print(message)

async def main():
    print("Start")
    await say_after(1, "Hello")
    await say_after(2, "World")
    print("End")

# 获取事件循环并运行
asyncio.run(main())
```

在上述示例中，`main` 协程依次调用 `say_after` 协程，事件循环负责调度和执行这些任务。

#### 2.3 任务（Task）

任务是对协程的封装，允许协程在事件循环中并发执行。通过 `asyncio.create_task` 方法，可以将协程转化为任务并调度执行。

```
import asyncio

async def say_after(delay, message):
    await asyncio.sleep(delay)
    print(message)

async def main():
    task1 = asyncio.create_task(say_after(1, "Hello"))
    task2 = asyncio.create_task(say_after(2, "World"))

    print("Tasks created")

    await task1
    await task2
    print("Tasks completed")

asyncio.run(main())
```

上述代码中，`say_after` 协程被创建为两个任务 `task1` 和 `task2`，并发执行。

#### 2.4 Future 对象

Future 对象表示一个尚未完成的操作，可以在未来某个时刻获取其结果。`asyncio` 中的 Future 对象用于在任务之间传递结果或状态。

```
import asyncio

async def set_after(fut, delay, value):
    await asyncio.sleep(delay)
    fut.set_result(value)

async def main():
    fut = asyncio.Future()

    asyncio.create_task(set_after(fut, 1, "Future Result"))

    result = await fut
    print(result)

asyncio.run(main())
```

在上述示例中，`fut` 是一个 Future 对象，通过 `set_after` 协程在延迟后设置其结果。`main` 协程等待 Future 对象完成并获取结果。

### 3. 使用 `asyncio` 实现异步任务调度

#### 3.1 基本任务调度

通过 `asyncio`，可以轻松地调度和管理多个异步任务。以下示例展示了如何并发执行多个任务，并等待所有任务完成。

```
import asyncio

async def fetch_data(delay, data):
    print(f"Fetching {

     data}...")
    await asyncio.sleep(delay)
    print(f"Fetched {

     data}")
    return data

async def main():
    tasks = [
        asyncio.create_task(fetch_data(2, "Data1")),
        asyncio.create_task(fetch_data(3, "Data2")),
        asyncio.create_task(fetch_data(1, "Data3")),
    ]

    results = await asyncio.gather(*tasks)
    print("All tasks completed.")
    print("Results:", results)

asyncio.run(main())
```

**输出:**

```
Fetching Data1...
Fetching Data2...
Fetching Data3...
Fetched Data3
Fetched Data1
Fetched Data2
All tasks completed.
Results: ['Data1', 'Data2', 'Data3']
```

在此示例中，`fetch_data` 协程模拟了数据获取操作，通过 `asyncio.create_task` 创建三个任务，并使用 `asyncio.gather` 等待所有任务完成。任务并发执行，显著提高了执行效率。

#### 3.2 处理任务异常

在实际应用中，任务执行过程中可能会发生异常。`asyncio` 提供了多种方式来处理任务异常，确保程序的健壮性。

```
import asyncio

async def faulty_task():
    await asyncio.sleep(1)
    raise ValueError("An error occurred in the task.")

async def main():
    task = asyncio.create_task(faulty_task())

    try:
        await task
    except ValueError as e:
        print(f"Caught exception: {

     e}")

asyncio.run(main())
```

**输出:**

```
Caught exception: An error occurred in the task.
```

在上述代码中，`faulty_task` 协程在执行过程中抛出了一个 `ValueError` 异常。`main` 协程通过 `try-except` 块捕获并处理该异常，避免程序因未处理的异常而崩溃。

#### 3.3 取消任务

有时需要在任务执行过程中取消某些任务，以释放资源或响应用户的操作。`asyncio` 提供了取消任务的方法，确保任务能够安全地终止。

```
import asyncio

async def long_running_task():
    try:
        while True:
            print("Task is running...")
            await asyncio.sleep(1)
    except asyncio.CancelledError:
        print("Task was cancelled.")

async def main():
    task = asyncio.create_task(long_running_task())

    await asyncio.sleep(3)
    task.cancel()

    try:
        await task
    except asyncio.CancelledError:
        print("Main: Task has been cancelled.")

asyncio.run(main())
```

**输出:**

```
Task is running...
Task is running...
Task is running...
Task was cancelled.
Main: Task has been cancelled.
```

在此示例中，`long_running_task` 协程模拟了一个长时间运行的任务。`main` 协程在等待3秒后取消该任务，并通过异常处理确保任务被安全终止。

### 4. 处理I/O密集型任务

#### 4.1 异步文件操作

虽然 `asyncio` 本身不直接支持异步文件操作，但通过使用 `aiofiles` 等第三方库，可以实现异步文件读写，避免I/O阻塞。

首先，安装 `aiofiles`：

```
pip install aiofiles
```

然后，使用 `aiofiles` 进行异步文件操作：

```
import asyncio
import aiofiles

async def read_file(file_path):
    async with aiofiles.open(file_path, mode='r') as f:
        contents =
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

  9

  点赞
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike.png)

  踩
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCollectActive.png)

  28

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

  分享到新浪微博...
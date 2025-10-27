---
title: 【Python运维】Python运维工具：用`psutil`监控系统性能
url: https://blog.csdn.net/nokiaguy/article/details/144667172
source: 一个被知识诅咒的人
date: 2024-12-24
fetch_date: 2025-10-06T19:36:57.630475
---

# 【Python运维】Python运维工具：用`psutil`监控系统性能

# 【Python运维】Python运维工具：用`psutil`监控系统性能

![](https://i-operation.csdnimg.cn/images/cf31225e169b4512917b2e77694eb0a2.png)Python库实现系统性能监控与优化

原创
已于 2025-01-09 16:50:24 修改
·
1.3k 阅读

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)

25

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)

25
·

CC 4.0 BY-SA版权

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

文章标签：

[#python](https://so.csdn.net/so/search/s.do?q=python&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#运维](https://so.csdn.net/so/search/s.do?q=%E8%BF%90%E7%BB%B4&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#开发语言](https://so.csdn.net/so/search/s.do?q=%E5%BC%80%E5%8F%91%E8%AF%AD%E8%A8%80&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

于 2024-12-23 14:53:56 首次发布

[![](https://i-blog.csdnimg.cn/columns/default/20201014180756925.png?x-oss-process=image/resize,m_fixed,h_224,w_224)

Python杂谈
同时被 2 个专栏收录![](https://csdnimg.cn/release/blogv2/dist/pc/img/newArrowDown1White.png)](https://blog.csdn.net/nokiaguy/category_12800257.html "Python杂谈")

390 篇文章

订阅专栏

[![](https://i-blog.csdnimg.cn/columns/default/20201014180756724.png?x-oss-process=image/resize,m_fixed,h_224,w_224)

运维](https://blog.csdn.net/nokiaguy/category_11917999.html "运维")

32 篇文章

订阅专栏

在现代的IT运维中，实时监控系统性能是确保服务器、网络和应用健康运行的基础。Python作为一种灵活的编程语言，在运维管理中得到了广泛应用。`psutil`是Python中一个强大的库，用于获取系统的各种资源信息，如CPU、内存、磁盘、网络等。本文将深入分析如何利用`psutil`库监控系统性能，并生成详细的报表。通过大量代码实例和中文注释，逐步讲解如何使用`psutil`获取系统资源的使用情况，如何设置定时监控任务，以及如何将监控结果生成报告或图表，方便运维人员进行分析和决策。本文不仅包括基本的监控任务，还介绍了如何优化监控脚本的性能，如何处理监控数据的存储和展示，帮助读者更好地应用这一工具进行系统运维。

#### 目录

1. **引言**
2. **`psutil`库概述**
   * 安装与配置
   * 库的主要功能
3. **获取系统资源信息**
   * CPU监控
   * 内存监控
   * 磁盘监控
   * 网络监控
4. **定时监控任务**
5. **生成报表与数据可视化**
   * 文本报表
   * 图表报表
6. **优化与性能提升**
7. **总结与展望**

---

#### 1. 引言

系统性能监控是IT运维的核心任务之一，尤其是在处理大量数据、分布式应用和云计算环境下，系统的健康状态直接影响到服务的可靠性与可用性。在日常的系统运维中，常常需要监控各类系统资源，包括CPU负载、内存使用情况、磁盘读写速度以及网络流量等，确保系统能够在高负载时稳定运行。

`psutil`是一个跨平台的库，能够帮助Python程序员快速访问这些系统性能指标。它支持Linux、Windows和macOS等操作系统，能够方便地获取系统资源的实时数据，并进行详细分析。本文将介绍如何使用`psutil`进行系统监控，并结合大量的代码实例，帮助读者快速掌握如何利用这一工具在实际的运维工作中提高效率。

---

#### 2. `psutil`库概述

##### 安装与配置

首先，我们需要安装`psutil`库。可以使用`pip`进行安装：

```
pip install psutil
```

安装完成后，我们可以导入`psutil`并开始使用它：

```
import psutil
```

##### 库的主要功能

`psutil`提供了丰富的API来访问系统信息。常见的功能包括：

* **CPU信息**：获取CPU的使用率、核心数、频率等。
* **内存信息**：获取系统的内存使用情况，包括总内存、已用内存、空闲内存等。
* **磁盘信息**：获取磁盘的使用情况、磁盘读写速度等。
* **网络信息**：获取网络接口的流量情况、网络连接等。

#### 3. 获取系统资源信息

##### CPU监控

要监控CPU的使用情况，`psutil`提供了多个方法，最常用的包括：

* `psutil.cpu_percent(interval=1)`：返回当前CPU的使用率。
* `psutil.cpu_times()`：返回每个CPU核心的使用时间，包括用户态、系统态、空闲态等。

下面是一个获取CPU使用率并每秒更新的代码示例：

```
import psutil
import time

def monitor_cpu():
    while True:
        cpu_percent = psutil.cpu_percent(interval=1)  # 获取CPU使用率
        print(f"当前CPU使用率: {cpu_percent}%")
        time.sleep(1)  # 每秒更新一次

monitor_cpu()
```

输出示例：

```
当前CPU使用率: 25.0%
当前CPU使用率: 30.0%
当前CPU使用率: 28.5%
```

##### 内存监控

使用`psutil`可以轻松获取系统的内存使用情况。常用的方法包括：

* `psutil.virtual_memory()`：返回虚拟内存的使用情况，包括总内存、已用内存、剩余内存等。
* `psutil.swap_memory()`：返回交换内存的使用情况。

代码示例：

```
import psutil

def monitor_memory():
    mem = psutil.virtual_memory()  # 获取内存信息
    print(f"总内存: {mem.total / (1024 ** 3):.2f} GB")
    print(f"已用内存: {mem.used / (1024 ** 3):.2f} GB")
    print(f"剩余内存: {mem.free / (1024 ** 3):.2f} GB")
    print(f"内存使用率: {mem.percent}%")

monitor_memory()
```

输出示例：

```
总内存: 16.00 GB
已用内存: 8.50 GB
剩余内存: 7.50 GB
内存使用率: 53.2%
```

##### 磁盘监控

`psutil`还可以监控磁盘的使用情况。常用的函数有：

* `psutil.disk_usage(path)`：返回磁盘的使用情况。
* `psutil.disk_io_counters()`：返回磁盘的读写计数。

代码示例：

```
import psutil

def monitor_disk():
    disk_usage = psutil.disk_usage('/')  # 获取根目录磁盘使用情况
    print(f"总磁盘空间: {disk_usage.total / (1024 ** 3):.2f} GB")
    print(f"已用磁盘空间: {disk_usage.used / (1024 ** 3):.2f} GB")
    print(f"剩余磁盘空间: {disk_usage.free / (1024 ** 3):.2f} GB")
    print(f"磁盘使用率: {disk_usage.percent}%")

monitor_disk()
```

输出示例：

```
总磁盘空间: 500.00 GB
已用磁盘空间: 200.00 GB
剩余磁盘空间: 300.00 GB
磁盘使用率: 40.0%
```

##### 网络监控

`psutil`提供了对网络接口的详细监控，包括：

* `psutil.net_io_counters()`：返回网络接口的流量统计。
* `psutil.net_connections()`：返回所有网络连接的信息。

代码示例：

```
import psutil

def monitor_network():
    net_io = psutil.net_io_counters()
    print(f"发送字节数: {net_io.bytes_sent / (1024 ** 2):.2f} MB")
    print(f"接收字节数: {net_io.bytes_recv / (1024 ** 2):.2f} MB")

monitor_network()
```

输出示例：

```
发送字节数: 50.00 MB
接收字节数: 75.00 MB
```

---

#### 4. 定时监控任务

在实际运维中，我们需要定期或持续地监控系统资源，可以利用Python的`time`模块或`schedule`库来实现定时任务。

##### 使用`time.sleep`进行定时监控

```
import time

def scheduled_monitor():
    while True:
        # 每10秒执行一次资源监控
        monitor_cpu()
        monitor_memory()
        monitor_disk()
        monitor_network()
        time.sleep(10)

scheduled_monitor()
```

##### 使用`schedule`库进行定时任务调度

`schedule`是一个简单的定时任务调度库，可以替代`time.sleep`，让任务执行更加灵活。

```
pip install schedule
```

```
import schedule
import time

def job():
    monitor_cpu()
    monitor_memory()
    monitor_disk()
    monitor_network()

# 每5分钟执行一次任务
schedule.every(5).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
```

---

#### 5. 生成报表与数据可视化

在系统监控过程中，获取的数据需要经过处理和展示，才能为运维人员提供有价值的信息。简单的文本报表可能无法直观地呈现数据的趋势和异常，因此，生成图表报表和可视化数据是一个重要的环节。这里我们将介绍如何使用Python中的`psutil`与`matplotlib`、`pandas`等库，将监控数据进行处理，并生成可视化的报表。

##### 5.1 文本报表

生成文本报表是最基本的一种方式，它直接将监控数据打印出来，方便进行记录和检查。在实际运维中，文本报表可以按时间戳生成，并保存到文件中，供后续分析和追踪。

###### 示例代码：生成CPU、内存、磁盘、网络使用情况的文本报表

```
import psutil
import time

def generate_report():
    # 获取系统的CPU使用率
    cpu_percent = psutil.cpu_percent(interval=1)
    # 获取系统的内存使用情况
    memory = psutil.virtual_memory()
    memory_percent = memory.percent
    # 获取系统磁盘使用情况
    disk = psutil.disk_usage('/')
    disk_percent = disk.percent
    # 获取网络使用情况
    net = psutil.net_io_counters()
    bytes_sent = net.bytes_sent
    bytes_recv = net.bytes_recv

    # 生成报表内容
    report = f"""
    系统监控报表
    -------------------------
    时间: {time.strftime('%Y-%m-%d %H:%M:%S')}

    CPU使用率: {cpu_percent}%
    内存使用率: {memory_percent}%
    磁盘使用率: {disk_percent}%

    网络流量:
    发送字节数: {bytes_sent} bytes
    接收字节数: {bytes_recv} bytes
    """
    return report

# 每隔一段时间生成报表并保存到文件
def save_report():
    while True:
        report = generate_report()
        with open("system_report.txt", "a") as file:
            file.write(report)
        print("报表已保存。")
        time.sleep(60)  # 每60秒生成一次报表

if __name__ == "__main__":
    save_report()
```

###### 解释：

在上述代码中，我们定义了一个`generate_report`函数，用来获取CPU、内存、磁盘、网络的实时数据，并生成格式化的文本报表。然后，通过`save_report`函数，每隔一分钟将生成的报表追加到`system_report.txt`文件中。这样，运维人员就可以方便地查看每次记录的系统状态。

##### 5.2 图表报表

虽然文本报表简洁，但对于系统性能的趋势分析而言，图表报表更加直观。我们可以使用`matplotlib`和`pandas`等库来生成图表，从而帮助我们更好地理解数据变化。

###### 示例代码：生成CPU、内存、磁盘使用情况的图表

```
import matplotlib.pyplot as plt
import psutil
import time
import pandas as pd

def get_system_data():
    # 获取CPU使用率
    cpu_percent = psutil.cpu_percent(interval=1)
    # 获取内存使用情况
    memory = psutil.virtual_memory()
    memory_percent = memory.percent
    # 获取磁盘使用情况
    disk = psutil.disk_usage('/')
    disk_percent = disk.percent
    return cpu_percent, memory_percent, disk_percent

def plot_system_data(cpu_data, memory_data, disk_data):
    # 使用pandas整理数据
    data = {
        'Time': pd.date_range(start='2024-12-08', periods=len(cpu_data), freq='T'),
        'CPU使用率': cpu_data,
        '内存使用率': memory_data,
        '磁盘使用率': disk_data,
    }
    df = pd.DataFrame(data)

    # 绘制图表
    plt.figure(figsize=(10, 6))
    plt.plot(df['Time'], df['CPU使用率'], label='CPU使用率', color='red')
    plt.plot(df['Time'], df['内存使用率'], label='内存使用率', color='blue')
    plt.plot(df['Time'], df['磁盘使用率'], label='磁盘使用率', color='green')
    plt.xlabel('时间')
    plt.ylabel('使用率 (%)')
  ...
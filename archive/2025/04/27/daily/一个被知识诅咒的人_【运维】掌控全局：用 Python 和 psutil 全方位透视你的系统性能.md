---
title: 【运维】掌控全局：用 Python 和 psutil 全方位透视你的系统性能
url: https://blog.csdn.net/nokiaguy/article/details/147531203
source: 一个被知识诅咒的人
date: 2025-04-27
fetch_date: 2025-10-06T22:03:22.135589
---

# 【运维】掌控全局：用 Python 和 psutil 全方位透视你的系统性能

# 【运维】掌控全局：用 Python 和 psutil 全方位透视你的系统性能

![](https://i-operation.csdnimg.cn/images/cf31225e169b4512917b2e77694eb0a2.png)用 Python 和 psutil 实现系统性能监控

原创
[![](https://csdnimg.cn/release/blogv2/dist/pc/img/identityVipNew.png)](https://mall.csdn.net/vip)
于 2025-04-26 13:42:19 发布
·
813 阅读

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)

15

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)

22
·

CC 4.0 BY-SA版权

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

文章标签：

[#运维](https://so.csdn.net/so/search/s.do?q=%E8%BF%90%E7%BB%B4&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#python](https://so.csdn.net/so/search/s.do?q=python&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#开发语言](https://so.csdn.net/so/search/s.do?q=%E5%BC%80%E5%8F%91%E8%AF%AD%E8%A8%80&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

[《Python OpenCV从菜鸟到高手》带你进入图像处理与计算机视觉的大门！](https://blog.csdn.net/nokiaguy/article/details/143574491)

[解锁Python编程的无限可能：《奇妙的Python》带你漫游代码世界](https://unitymarvel.blog.csdn.net/article/details/141889588)

系统管理员和开发者经常需要监控服务器或个人电脑的性能，以便及时发现瓶颈、优化资源利用率，甚至预测潜在问题。Python 的 `psutil` 库提供了一个强大、跨平台的方式来获取各种系统指标，如 CPU 使用率、内存占用、磁盘 I/O、网络流量等。本文将深入探讨 `psutil` 的功能，结合大量代码示例（包括详细的中文注释）和 LaTeX 数学公式，展示如何利用它构建全面的系统监控工具。您将学会如何收集、处理和展示性能数据，最终实现对系统健康状况的全面掌控。本文的目标是让您能够构建自己的定制化监控解决方案，或将 `psutil` 集成到现有的运维工具链中。

#### 1. 引言：为什么我们需要系统监控？

在数字化时代，无论是个人电脑还是大型服务器集群，系统的稳定性和性能都至关重要。系统监控就像是给我们的数字基础设施安装了一个“健康检查仪”，可以帮助我们：

* **及时发现问题:** 在系统崩溃或性能严重下降之前，预警潜在的硬件故障、资源耗尽等问题。
* **优化性能:** 识别系统瓶颈，例如 CPU 过载、内存不足、磁盘 I/O 阻塞等，从而进行针对性的优化。
* **资源规划:** 了解系统资源的使用趋势，预测未来的需求，为扩容或缩容提供依据。
* **故障排除:** 当问题发生时，提供详细的性能数据，帮助快速定位问题的根源。
* **安全审计:** 监控异常的网络流量、进程活动等，有助于发现潜在的安全威胁。

`psutil` (process and system utilities) 是一个跨平台的 Python 库，可以轻松获取系统和进程的各种信息，是实现系统监控的理想工具。

#### 2. psutil 库：安装与初步探索

##### 2.1 安装

安装 `psutil` 非常简单，使用 `pip` 即可：

```
pip install psutil
```

##### 2.2 初步探索：获取 CPU 信息

让我们从获取 CPU 信息开始，体验 `psutil` 的便捷性：

```
# 导入 psutil 库
import psutil

# 获取 CPU 逻辑核心数
cpu_count_logical = psutil.cpu_count()
print(f"CPU 逻辑核心数: {

     cpu_count_logical}")

# 获取 CPU 物理核心数
cpu_count_physical = psutil.cpu_count(logical=False)
print(f"CPU 物理核心数: {

     cpu_count_physical}")

# 获取 CPU 使用率（每隔 1 秒刷新一次）
for i in range(5):  # 监控5次
    cpu_percent = psutil.cpu_percent(interval=1)
    print(f"CPU 使用率: {

     cpu_percent}%")
```

这段代码展示了如何获取 CPU 的逻辑核心数、物理核心数，以及每秒的 CPU 使用率。`psutil.cpu_percent()` 函数的 `interval` 参数指定了采样间隔。

#### 3. CPU 监控：深入挖掘

##### 3.1 CPU 详细使用率

除了总体 CPU 使用率，`psutil` 还可以提供更详细的信息：

```
# 获取 CPU 的详细使用率信息
cpu_times_percent = psutil.cpu_times_percent(interval=1)

print(f"用户态 CPU 使用率: {

     cpu_times_percent.user}%")
print(f"内核态 CPU 使用率: {

     cpu_times_percent.system}%")
print(f"空闲 CPU 使用率: {

     cpu_times_percent.idle}%")
print(f"I/O 等待 CPU 使用率: {

     cpu_times_percent.iowait}%")  # 注意：某些系统可能不支持
# ... 其他指标，如 nice, irq, softirq, steal, guest, guest_nice
```

`cpu_times_percent()` 返回一个命名元组，包含了 CPU 在不同模式下花费时间的百分比。这些指标对于分析 CPU 负载的类型非常有用。例如，如果 `iowait` 很高，可能表示磁盘 I/O 存在瓶颈。

##### 3.2 CPU 负载：平均负载

除了瞬时使用率，我们还可以获取系统的平均负载，这是一个反映系统繁忙程度的指标：

```
# 获取系统平均负载（1 分钟、5 分钟、15 分钟）
load_avg = psutil.getloadavg()
print(f"1 分钟平均负载: {

     load_avg[0]}")
print(f"5 分钟平均负载: {

     load_avg[1]}")
print(f"15 分钟平均负载: {

     load_avg[2]}")

# 建议：将平均负载除以 CPU 核心数，得到一个更直观的指标
load_avg_per_core = [x / psutil.cpu_count() for x in load_avg]
print(f"每核心 1 分钟平均负载: {

     load_avg_per_core[0]:.2f}")
print(f"每核心 5 分钟平均负载: {

     load_avg_per_core[1]:.2f}")
print(f"每核心 15 分钟平均负载: {

     load_avg_per_core[2]:.2f}")
```

平均负载表示在一段时间内，系统中处于可运行状态（正在使用 CPU 或等待 CPU）的平均进程数。一般来说，如果每核心的平均负载持续高于 0.7，就可能需要关注系统的性能问题。

##### 3.3 CPU 频率

```
# 获取当前 CPU 频率
cpu_freq = psutil.cpu_freq()
print(f"当前 CPU 频率: {

     cpu_freq.current} MHz")
print(f"最小 CPU 频率: {

     cpu_freq.min} MHz")
print(f"最大 CPU 频率: {

     cpu_freq.max} MHz")
```

`cpu_freq()` 返回一个命名元组，其中包含了当前频率、最小频率和最大频率。

##### 3.4 CPU 温度 (部分硬件支持)

```
# 获取 CPU 温度（如果硬件支持）
try:
    cpu_temperatures = psutil.sensors_temperatures()
    if 'coretemp' in cpu_temperatures: #不同平台，key值可能不同
        for entry in cpu_temperatures['coretemp']:
            print(f"{

     entry.label}: {

     entry.current}°C")
except AttributeError:
    print("无法获取 CPU 温度信息。")
```

部分硬件和操作系统可能不支持该功能。

#### 4. 内存监控

##### 4.1 内存使用情况

```
# 获取内存使用情况
memory = psutil.virtual_memory()

print(f"总内存: {

     memory.total / (1024 ** 3):.2f} GB")  # 转换为 GB
print(f"已使用内存: {

     memory.used / (1024 ** 3):.2f} GB")
print(f"可用内存: {

     memory.available / (1024 ** 3):.2f} GB")
print(f"内存使用率: {

     memory.percent}%")
print(f"空闲内存: {

     memory.free/ (1024 ** 3):.2f} GB")
# ... 其他指标，如 active, inactive, buffers, cached, shared, slab
```

`psutil.virtual_memory()` 返回一个命名元组，包含了各种内存指标。`total` 是总内存，`used` 是已使用的内存，`available` 是可供应用程序使用的内存（包括空闲内存和可回收的缓存），`percent` 是内存使用率。

##### 4.2 Swap 交换分区

```
# 获取 Swap 交换分区使用情况
swap = psutil.swap_memory()

print(f"总 Swap 空间: {

     swap.total / (1024 ** 3):.2f} GB")
print(f"已使用 Swap 空间: {

     swap.used / (1024 ** 3):.2f} GB")
print(f"空闲 Swap 空间: {

     swap.free / (1024 ** 3):.2f} GB")
print(f"Swap 使用率: {

     swap.percent}%")
print(f"从磁盘换入内存: {

     swap.sin / (1024 ** 3):.2f} GB") #数据量
print(f"从内存换出到磁盘: {

     swap.sout / (1024 ** 3):.2f} GB")#数据量
```

Swap 交换分区是在物理内存不足时，将一部分硬盘空间用作内存的区域。`swap_memory()` 提供了 Swap 分区的总大小、已用大小、空闲大小、使用率等信息。`sin` 和 `sout` 分别表示从磁盘换入内存和从内存换出到磁盘的数据量。

#### 5. 磁盘监控

##### 5.1 磁盘分区信息

```
# 获取磁盘分区信息
partitions = psutil.disk_partitions()

for partition in partitions:
    print(f"设备: {

     partition.device}")
    print(f"挂载点: {

     partition.mountpoint}")
    print(f"文件系统类型: {

     partition.fstype}")
    try:
        usage = psutil.disk_usage(partition.mountpoint)
        print(f"  总空间: {

     usage.total / (1024 ** 3):.2f} GB")
        print(f"  已用空间: {

     usage.used / (1024 ** 3):.2f} GB")
        print(f"  空闲空间: {

     usage.free / (1024 ** 3):.2f} GB")
        print(f"  使用率: {

     usage.percent}%")
    except PermissionError:
        print("  无权限访问该分区信息。")
```

这段代码会列出所有磁盘分区及其详细信息，包括设备名、挂载点、文件系统类型、总空间、已用空间、空闲空间和使用率。

##### 5.2 磁盘 I/O 统计

```
# 获取磁盘 I/O 统计信息
disk_io = psutil.disk_io_counters()

print(f"读取次数: {

     disk_io.read_count}")
print(f"写入次数: {

     disk_io.write_count}")
print(f"读取字节数: {

     disk_io.read_bytes / (1024 ** 3):.2f} GB")
print(f"写入字节数: {

     disk_io.write_bytes / (1024 ** 3):.2f} GB")
print(f"读取时间: {

     disk_io.read_time} ms")
print(f"写入时间: {

     disk_io.write_time} ms")

# 可以针对每个磁盘单独获取 I/O 统计
for disk, io in psutil.disk_io_counters(perdisk=True).items():
    print(f"磁盘 {
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

  15

  点赞
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike.png)

  踩
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCollectActive.png)

  22

  收藏

  觉得还不错?
  一键收藏
  ...
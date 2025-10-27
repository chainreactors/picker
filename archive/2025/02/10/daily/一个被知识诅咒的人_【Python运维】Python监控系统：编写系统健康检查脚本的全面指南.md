---
title: 【Python运维】Python监控系统：编写系统健康检查脚本的全面指南
url: https://blog.csdn.net/nokiaguy/article/details/145531240
source: 一个被知识诅咒的人
date: 2025-02-10
fetch_date: 2025-10-06T20:35:18.992960
---

# 【Python运维】Python监控系统：编写系统健康检查脚本的全面指南

# 【Python运维】Python监控系统：编写系统健康检查脚本的全面指南

![](https://csdnimg.cn/release/blogv2/dist/pc/img/original.png)

[![](https://csdnimg.cn/release/blogv2/dist/pc/img/identityVipNew.png)](https://mall.csdn.net/vip)
[蒙娜丽宁](https://unitymarvel.blog.csdn.net "蒙娜丽宁")
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCurrentTime2.png)
于 2025-02-09 13:23:29 发布

![](https://csdnimg.cn/release/blogv2/dist/pc/img/articleReadEyes2.png)
阅读量857
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)
收藏

12

![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)
点赞数
15

CC 4.0 BY-SA版权

分类专栏：
[Python杂谈](https://blog.csdn.net/nokiaguy/category_12800257.html)
[运维](https://blog.csdn.net/nokiaguy/category_11917999.html)
文章标签：
[人工智能](https://so.csdn.net/so/search/s.do?q=%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[python](https://so.csdn.net/so/search/s.do?q=python&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[机器翻译](https://so.csdn.net/so/search/s.do?q=%E6%9C%BA%E5%99%A8%E7%BF%BB%E8%AF%91&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

本文链接：<https://blog.csdn.net/nokiaguy/article/details/145531240>

[《Python OpenCV从菜鸟到高手》带你进入图像处理与计算机视觉的大门！](https://blog.csdn.net/nokiaguy/article/details/143574491)

[解锁Python编程的无限可能：《奇妙的Python》带你漫游代码世界](https://unitymarvel.blog.csdn.net/article/details/141889588)

在现代信息技术环境中，系统的稳定运行对于企业和个人用户至关重要。本文深入探讨了如何利用Python编写系统健康检查脚本，以实现对系统资源利用率、服务状态等关键指标的实时监控和管理。文章首先介绍了系统健康检查的基本概念和重要性，随后详细讲解了使用Python进行系统监控的各种方法和工具，包括`psutil`库的应用、服务状态的检测、磁盘空间和内存使用的监控等。通过丰富的代码示例和详细的中文注释，读者将能够掌握如何构建一个功能强大且可靠的监控系统。此外，文章还讨论了报警机制的实现和监控数据的可视化展示，帮助用户全面了解和管理系统的运行状况。无论是系统管理员、DevOps工程师，还是Python开发者，都能从中获得实用的技术指导，提升系统管理的效率和可靠性。

### 目录

1. 引言
2. 系统健康检查的必要性
3. Python在系统监控中的优势
4. 环境准备与依赖安装
5. 使用`psutil`库监控系统资源
   * CPU利用率监控
   * 内存使用情况监控
   * 磁盘空间监控
   * 网络流量监控
6. 服务状态检查
   * 检查服务是否运行
   * 自动重启服务
7. 日志记录与报警机制
   * 日志记录
   * 发送报警通知
8. 定时任务与脚本自动化
9. 数据可视化与报告生成
10. 实战案例：构建一个完整的系统健康检查脚本
11. 总结与展望

### 1. 引言

在当今高度依赖计算机系统的时代，系统的稳定性和可靠性直接影响到业务的连续性和效率。无论是服务器、工作站还是个人计算机，系统的资源利用率和服务状态的实时监控都是保障其正常运行的基础。手动监控不仅效率低下，而且容易出现遗漏，特别是在大型复杂系统中更是难以胜任。因此，自动化的系统健康检查脚本成为了系统管理员和开发者的必备工具。

Python，作为一种简洁、高效且功能强大的编程语言，凭借其丰富的第三方库和强大的社区支持，成为编写系统监控脚本的理想选择。本文将全面介绍如何使用Python编写系统健康检查脚本，涵盖从基本的资源监控到复杂的服务状态检测，并通过实际代码示例帮助读者快速上手。

### 2. 系统健康检查的必要性

系统健康检查是指通过监控和分析系统的各项指标，及时发现和解决潜在的问题，确保系统的稳定运行。具体来说，系统健康检查包括但不限于以下几个方面：

* **资源利用率监控**：监控CPU、内存、磁盘、网络等资源的使用情况，避免资源瓶颈导致的性能下降。
* **服务状态检测**：确保关键服务（如Web服务器、数据库服务器等）处于运行状态，及时重启故障服务。
* **日志分析**：通过分析系统日志，发现异常行为或错误信息，提前预警潜在问题。
* **安全监控**：监控系统的安全状态，检测可疑活动或未授权访问。

通过系统健康检查，可以实现以下目标：

* **提高系统可靠性**：及时发现并解决问题，减少系统故障时间。
* **优化资源配置**：了解资源使用情况，合理分配和调整资源，提高系统性能。
* **保障业务连续性**：确保关键服务的稳定运行，避免业务中断。
* **增强安全性**：及时发现并应对安全威胁，保护系统和数据的安全。

### 3. Python在系统监控中的优势

Python因其简洁的语法、丰富的库和广泛的社区支持，成为系统监控脚本开发的首选语言。以下是Python在系统监控中的主要优势：

* **易于学习和使用**：Python的语法简洁明了，适合快速开发和原型设计。
* **丰富的第三方库**：如`psutil`、`schedule`、`logging`等，涵盖了系统监控的各个方面。
* **跨平台支持**：Python可以在Windows、Linux、macOS等多种操作系统上运行，确保脚本的广泛适用性。
* **强大的社区支持**：大量的开源项目和社区资源，方便获取帮助和解决方案。
* **良好的可扩展性**：Python支持面向对象和模块化编程，便于构建复杂的监控系统。

### 4. 环境准备与依赖安装

在开始编写系统健康检查脚本之前，需要准备好开发环境并安装必要的依赖。本文将以Python 3.x为例，推荐使用虚拟环境来管理项目依赖。

#### 4.1 安装Python

首先，确保系统中已安装Python 3.x。可以通过以下命令检查：

```
python3 --version
```

如果未安装，可以从[Python官方网站](https://www.python.org/downloads/)下载并安装适合的版本。

#### 4.2 创建虚拟环境

创建一个独立的虚拟环境，以避免与系统全局环境的依赖冲突。

```
# 安装virtualenv（如果未安装）
pip install virtualenv

# 创建虚拟环境
virtualenv venv

# 激活虚拟环境
# Windows
venv\Scripts\activate

# Unix或MacOS
source venv/bin/activate
```

#### 4.3 安装必要的Python库

使用`pip`安装编写系统监控脚本所需的库，包括`psutil`、`schedule`、`requests`等。

```
pip install psutil schedule requests
```

* **psutil**：用于获取系统和进程信息。
* **schedule**：用于定时任务调度。
* **requests**：用于发送HTTP请求，如发送报警通知。

### 5. 使用`psutil`库监控系统资源

`psutil`（Python system and process utilities）是一个跨平台库，用于检索系统信息和管理进程。它提供了丰富的接口，可以方便地获取CPU、内存、磁盘、网络等资源的使用情况。

#### 5.1 安装`psutil`

如果尚未安装，可以使用以下命令安装：

```
pip install psutil
```

#### 5.2 CPU利用率监控

通过`psutil`可以轻松获取CPU的使用情况，包括整体利用率和各核心的利用率。

```
import psutil
import time

def get_cpu_usage(interval=1):
    """
    获取CPU利用率
    :param interval: 采样时间间隔（秒）
    :return: CPU利用率（百分比）
    """
    cpu_percent = psutil.cpu_percent(interval=interval)
    return cpu_percent

if __name__ == "__main__":
    while True:
        cpu = get_cpu_usage()
        print(f"CPU利用率: {

     cpu}%")
        time.sleep(5)
```

**代码说明**：

* `psutil.cpu_percent(interval=1)`：获取1秒内的CPU利用率。
* 使用一个无限循环，每5秒打印一次CPU利用率。

#### 5.3 内存使用情况监控

内存使用情况包括总内存、已用内存、可用内存等信息。

```
import psutil
import time

def get_memory_info():
    """
    获取内存使用情况
    :return: 字典包含总内存、已用内存、可用内存、使用率
    """
    mem = psutil.virtual_memory()
    mem_info = {

        'total': mem.total,
        'used': mem.used,
        'available': mem.available,
        'percent': mem.percent
    }
    return mem_info

if __name__ == "__main__":
    while True:
        memory = get_memory_info()
        print(f"内存总量: {

     memory['total'] / (1024 ** 3):.2f} GB")
        print(f"已用内存: {

     memory['used'] / (1024 ** 3):.2f} GB")
        print(f"可用内存: {

     memory['available'] / (1024 ** 3):.2f} GB")
        print(f"内存使用率: {

     memory['percent']}%")
        time.sleep(5)
```

**代码说明**：

* `psutil.virtual_memory()`：获取虚拟内存信息。
* 打印总内存、已用内存、可用内存和内存使用率。

#### 5.4 磁盘空间监控

监控磁盘的使用情况，包括各挂载点的总空间、已用空间、可用空间和使用率。

```
import psutil
import time

def get_disk_info():
    """
    获取磁盘使用情况
    :return: 列表，每个元素是一个挂载点的磁盘信息
    """
    partitions = psutil.disk_partitions()
    disk_info = []
    for partition in partitions:
        try:
            usage = psutil.disk_usage(partition.mountpoint)
            disk_info.append({

                'device': partition.device,
                'mountpoint': partition.mountpoint,
                'fstype': partition.fstype,
                'total': usage.total,
                'used': usage.used,
                'free': usage.free,
                'percent': usage.percent
            })
        except PermissionError:
            # 忽略无权限访问的挂载点
            continue
    return disk_info

if __name__ == "__main__":
    while True:
        disks = get_disk_info()
        for disk in disks:
            print(f"设备: {

     disk['device']}")
            print(f"挂载点: {

     disk['mountpoint']}")
            print(f"文件系统类型: {

     disk['fstype']}")
            print(f"总空间: {

     disk['total'] / (1024 ** 3):.2f} GB")
            print(f"已用空间: {

     disk['used'] / (1024 ** 3):.2f} GB")
            print(f"可用空间: {

     disk['free'] / (1024 ** 3):.2f} GB")
            print(f"使用率: {

     disk['percent']}%")
            print("-" * 30)
        time.sleep(10)
```

**代码说明**：

* `psutil.disk_partitions()`：获取所有磁盘分区信息。
* 对每个分区调用`psutil.disk_usage()`获取其使用情况。
* 打印设备名称、挂载点、文件系统类型、总空间、已用空间、可用空间和使用率。

#### 5.5 网络流量监控

监控网络接口的流量情况，包括发送和接收的字节数。

```
import psutil
import time

def get_network_info():
    """
    获取网络流量信息
    :return: 字典包含发送和接收的字节数
    """
    net_io = psutil.net_io_counters(pernic=True)
    network_info = {

   }
    for iface, stats in net_io.items():
        network_info[iface] = {

            'bytes_sent': stats.bytes_sent,
            'bytes_recv': stats.bytes_recv
        }
    return network_info

if __name__ == "__main__":
    while True:
        network = get_network_info()
        for iface, stats in network.items():
            print(f"接口: {

     iface}")
            print(f"发送字节数: {

     stats['bytes_sent']}")
            print(f"接收字节数: {

     stats['bytes_recv']}"
```

![](https://csdnimg.cn/release/blogv2/dist/pc/img/lock.png)最低0.47元/天 解锁文章

200万优质内容无限畅学

![](https://csdnimg.cn/release/blogv2/dist/pc/img/vip-limited-close-newWhite.png)

确定要放弃本次机会？

福利倒计时

*:*

...
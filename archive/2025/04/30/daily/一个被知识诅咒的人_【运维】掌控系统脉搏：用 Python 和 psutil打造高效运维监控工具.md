---
title: 【运维】掌控系统脉搏：用 Python 和 psutil打造高效运维监控工具
url: https://blog.csdn.net/nokiaguy/article/details/147605034
source: 一个被知识诅咒的人
date: 2025-04-30
fetch_date: 2025-10-06T22:04:32.221950
---

# 【运维】掌控系统脉搏：用 Python 和 psutil打造高效运维监控工具

# 【运维】掌控系统脉搏：用 Python 和 psutil打造高效运维监控工具

![](https://csdnimg.cn/release/blogv2/dist/pc/img/original.png)

[![](https://csdnimg.cn/release/blogv2/dist/pc/img/identityVipNew.png)](https://mall.csdn.net/vip)
[蒙娜丽宁](https://unitymarvel.blog.csdn.net "蒙娜丽宁")
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newUpTime2.png)
已于 2025-04-29 11:36:56 修改

![](https://csdnimg.cn/release/blogv2/dist/pc/img/articleReadEyes2.png)
阅读量857
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)
收藏

10

![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)
点赞数
11

CC 4.0 BY-SA版权

分类专栏：
[Python杂谈](https://blog.csdn.net/nokiaguy/category_12800257.html)
[运维](https://blog.csdn.net/nokiaguy/category_11917999.html)
文章标签：
[人工智能](https://so.csdn.net/so/search/s.do?q=%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[python](https://so.csdn.net/so/search/s.do?q=python&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[分类](https://so.csdn.net/so/search/s.do?q=%E5%88%86%E7%B1%BB&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

于 2025-04-29 11:35:23 首次发布

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

本文链接：<https://blog.csdn.net/nokiaguy/article/details/147605034>

[《Python OpenCV从菜鸟到高手》带你进入图像处理与计算机视觉的大门！](https://blog.csdn.net/nokiaguy/article/details/143574491)

[解锁Python编程的无限可能：《奇妙的Python》带你漫游代码世界](https://unitymarvel.blog.csdn.net/article/details/141889588)

在现代运维中，实时监控系统性能是保障服务稳定运行的关键。本文深入探讨如何利用 Python 的 `psutil` 库开发一个功能强大的系统资源监控工具，覆盖 CPU、内存、磁盘和网络等核心指标。通过详细的代码示例和解释，读者将学习如何获取系统运行状态、计算资源使用率、生成可视化报表，并实现自动化监控。本文不仅展示了 `psutil` 的基本用法，还深入分析了其高级功能，如进程管理、传感器数据读取等。结合中文注释和丰富的实例代码，本文旨在帮助开发者快速上手，打造适用于生产环境的监控解决方案。无论是初学者还是资深运维工程师，都能从中获得实用技能和灵感，提升系统管理效率。

---

#### 正文

##### 引言

随着云计算和分布式系统的普及，服务器性能监控成为运维工作中不可或缺的一部分。Python 作为一门简单易学且功能强大的编程语言，结合其丰富的第三方库，为开发高效运维工具提供了无限可能。其中，`psutil`（Process and System Utilities）是一个跨平台的系统监控库，能够轻松获取 CPU、内存、磁盘、网络等资源的使用情况。本文将从基础用法入手，逐步深入，带你用 `psutil` 打造一个完整的系统性能监控工具，并生成详细的报表。

##### 1. `psutil` 简介与安装

`psutil` 是一个开源的 Python 库，支持 Windows、Linux、macOS 等多种操作系统。它提供了丰富的 API，用于获取系统资源信息、进程管理甚至硬件状态。安装非常简单，只需运行以下命令：

```
pip install psutil
```

安装完成后，我们可以通过 Python 脚本验证其是否正常工作：

```
import psutil
print(psutil.__version__)  # 输出 psutil 的版本号，例如 5.9.8
```

##### 2. 监控 CPU 性能

CPU 是系统的核心部件，其性能直接影响服务器的运行效率。`psutil` 提供了多种方法来获取 CPU 的使用情况。

###### 2.1 获取 CPU 使用率

`psutil.cpu_percent()` 是获取 CPU 使用率最常用的方法。它返回一个浮点数，表示当前 CPU 的使用百分比。

```
import psutil
import time

# 获取 CPU 总体使用率
cpu_usage = psutil.cpu_percent(interval=1)  # interval=1 表示采样间隔为1秒
print(f"当前 CPU 使用率: {

     cpu_usage}%")

# 按核心获取 CPU 使用率
cpu_usage_per_core = psutil.cpu_percent(interval=1, percpu=True)
print(f"每个核心的 CPU 使用率: {

     cpu_usage_per_core}")
```

**代码解释**：

* `interval=1` 表示采样间隔为 1 秒，避免瞬时数据波动。
* `percpu=True` 返回一个列表，每个元素对应一个 CPU 核心的使用率。

###### 2.2 获取 CPU 频率和负载

除了使用率，CPU 的频率和负载也是重要指标。`psutil.cpu_freq()` 返回 CPU 的当前频率、最小频率和最大频率。

```
# 获取 CPU 频率
cpu_freq = psutil.cpu_freq()
if cpu_freq:
    print(f"当前频率: {

     cpu_freq.current} MHz")
    print(f"最小频率: {

     cpu_freq.min} MHz")
    print(f"最大频率: {

     cpu_freq.max} MHz")
else:
    print("无法获取 CPU 频率信息")
```

**注意**：在某些虚拟机或容器环境中，频率信息可能不可用。

###### 2.3 计算 CPU 负载

CPU 负载可以通过 `psutil.getloadavg()` 获取（仅限 Linux/Unix 系统）：

```
try:
    load_avg = psutil.getloadavg()  # 返回 1、5、15 分钟的平均负载
    print(f"系统负载 (1min, 5min, 15min): {

     load_avg}")
except AttributeError:
    print("当前系统不支持获取负载信息")
```

##### 3. 监控内存使用情况

内存是系统性能的另一个关键指标。`psutil.virtual_memory()` 返回内存的详细状态。

```
# 获取内存使用情况
memory = psutil.virtual_memory()

print(f"总内存: {

     memory.total / (1024 ** 3):.2f} GB")
print(f"已用内存: {

     memory.used / (1024 ** 3):
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

  11

  点赞
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike.png)

  踩
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCollectActive.png)

  10

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
2559

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
[【奇妙的Python】解锁Python编程的无限可能：《奇妙的Python》带你漫游代码世界](https://unitymarvel.blog.csdn.net/article/details/141889588)

09-04
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
3141

[《奇妙的Python——神奇代码漫游之旅》是一本面向实际应用的Python编程指南，涵盖文件操作、GUI设计、多媒体处理、自动化办公、加密解密等多个领域。由华为HDE专家李宁编写，通过丰富的实战案例，帮助读者在工作和项目中高效应用Python，提升编程技能。无论是新手还是有经验的开发者，这本书都将带你深入探索Python的无限可能，开启一段充满创意与实用性的编程之旅。](https://unitymarvel.blog.csdn.net/article/details/141889588)

![](https://csdnimg.cn/release/blogv2/dist/components/img/blogType.png)
博客
[2025机器人产业大洗牌：新兴初创企业的技术革命与崛起之路](https://unitymarvel.blog.csdn.net/article/details/151067555)

09-01
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
1049

[摘要：2025年机器人产业正经历技术驱动的深度变革，AI初创企业通过创新算法和低成本方案挑战传统巨头。本文剖析产业洗牌动因，包括AI融合、融资热潮和应用场景扩展，重点解析人形机器人等关键技术。通过ROS控制、A\*路径规划和PyTorch视觉识别等代码示例（附中文注释），展示初创企业的技术优势。文章预测Figure AI、Unitree等公司将引领消费级机器人市场，推动社会进入智能协作新时代。（150字）](https://unitymarvel.blog.csdn.net/article/details/151067555)

![](https://csdnimg.cn/release/blogv2/dist/components/img/blogType.png)
博客
[Java应用容器化革命：Docker部署从入门到精通](https://unitymarvel.blog.csdn.n...
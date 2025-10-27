---
title: 用Python编写自己的命令行工具：深入解析argparse
url: https://blog.csdn.net/nokiaguy/article/details/144062354
source: 一个被知识诅咒的人
date: 2024-11-27
fetch_date: 2025-10-06T19:16:23.350099
---

# 用Python编写自己的命令行工具：深入解析argparse

# 用Python编写自己的命令行工具：深入解析argparse

![](https://csdnimg.cn/release/blogv2/dist/pc/img/original.png)

[![](https://csdnimg.cn/release/blogv2/dist/pc/img/identityVipNew.png)](https://mall.csdn.net/vip)
[蒙娜丽宁](https://unitymarvel.blog.csdn.net "蒙娜丽宁")
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCurrentTime2.png)
于 2024-11-26 16:30:18 发布

![](https://csdnimg.cn/release/blogv2/dist/pc/img/articleReadEyes2.png)
阅读量840
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)
收藏

26

![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)
点赞数
17

CC 4.0 BY-SA版权

分类专栏：
[Python杂谈](https://blog.csdn.net/nokiaguy/category_12800257.html)
文章标签：
[python](https://so.csdn.net/so/search/s.do?q=python&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[javascript](https://so.csdn.net/so/search/s.do?q=javascript&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[开发语言](https://so.csdn.net/so/search/s.do?q=%E5%BC%80%E5%8F%91%E8%AF%AD%E8%A8%80&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

本文链接：<https://blog.csdn.net/nokiaguy/article/details/144062354>

[《Python OpenCV从菜鸟到高手》带你进入图像处理与计算机视觉的大门！](https://blog.csdn.net/nokiaguy/article/details/143574491)

命令行工具是开发者日常工作的重要工具，它们以简单、高效和灵活著称。Python 的标准库 `argparse` 提供了强大的功能，用于解析命令行参数并生成详细的帮助文档。在本文中，我们将深入探讨如何使用 `argparse` 构建功能丰富的命令行工具。通过逐步扩展示例，涵盖从基本参数解析到高级特性（如子命令、参数验证、自定义格式化等），帮助读者全面掌握 `argparse` 的使用技巧。结合丰富的代码和详细的中文注释，我们不仅会展示如何设计和实现一个命令行工具，还会探讨如何优化其用户体验和可维护性。无论是初学者还是资深开发者，都能从中找到有用的实践指导。

---

### 引言

命令行工具是开发者工具链中不可或缺的一环。Python 的 `argparse` 是一个标准库模块，专门用于处理命令行参数。无论是快速开发脚本，还是构建复杂的命令行程序，`argparse` 都提供了高效的解决方案。

#### 为什么选择`argparse`？

* **内置库**：不需要额外安装。
* **功能强大**：支持位置参数、可选参数、子命令等。
* **用户友好**：自动生成帮助文档，易于扩展。

以下是本文的主要内容：

1. `argparse` 的基础知识
2. 使用位置参数和可选参数
3. 子命令的实现
4. 高级功能解析
5. 实战：编写一个完整的命令行工具
6. 提升用户体验的优化技巧

---

### 一、`argparse` 的基础知识

`argparse` 提供了一个简洁的接口，用于定义程序接受的参数和选项。它通过以下三个核心步骤完成参数解析：

1. 创建解析器对象（`ArgumentParser`）。
2. 定义参数（位置参数、可选参数）。
3. 解析输入（`parse_args()`）。

#### 第一个示例：简单的参数解析

以下是一个简单的 `argparse` 示例，展示如何解析单个参数。

```
# 引入 argparse 库
import argparse

# 创建解析器对象
parser = argparse.ArgumentParser(description="这是一个简单的命令行工具示例")

# 添加参数
parser.add_argument("name", help="用户的名字")  # 必选参数

# 解析参数
args = parser.parse_args()

# 打印解析结果
print(f"你好, {

     args.name}!")
```

运行此脚本并传入一个参数：

```
python script.py Alice
```

输出结果：

```
你好, Alice!
```

##### 代码解析

* **创建解析器**：`ArgumentParser()` 是参数解析的入口，`description` 用于生成帮助文档。
* **添加参数**：`add_argument()` 定义参数名称及其描述。
* **解析参数**：`parse_args()` 将命令行参数解析为一个对象。

---

### 二、位置参数和可选参数

#### 1. 位置参数

位置参数是命令行中必须提供的参数，顺序重要。

##### 示例：多个位置参数

```
import argparse

# 创建解析器
parser = argparse.ArgumentParser(description="计算两个数字的和")

# 添加两个位置参数
parser.add_argument("num1", type=int, help="第一个数字")
parser.add_argument("num2", type=int, help="第二个数字")

# 解析参数
args = parser.parse_args()

# 计算和
result = args.num1 + args.num2
print(f"{

     args.num1} + {

     args.
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

  17

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
3140

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
[Java应用容器化革命：Docker部署从入门到精通](https://unitymarvel.blog.csdn.net/article/details/151067543)

09-01
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
962

[在现代软件开发中，容器化技术已成为提升应用部署效率和可移植性的关键工具。本文以“Java 与 Docker：容器化部署入门”为主题，深入探讨如何将Java应用无缝集成到Docker环境中。从Docker的基本概念和安装入手，我们将逐步引导读者构建一个简单的Java Web应用，并通过编写Dockerfile实现镜像的创建和容器的运行。文章涵盖了多阶段构建、环境变量配置、数据持久化、网络管理以及安全最佳实践等核心内容。通过大量的代码示例和详细的中文注释，读者可以轻松上手实践操作。同时，我们还将介绍常见问题排查](https://unitymarvel.blog.csdn.net/article/details/151067543)

![](https://csdnimg.cn/release/blogv2/dist/components/img/blogType.png)
博客
[【人工智能】AI代理重塑游戏世界：动态NPC带来的革命性沉浸式体验](https://unitymarvel.blog.csdn.net/article/details/150948550)

08-28
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
1081

[在当今游戏行业迅猛发展的时代，AI代理技术...
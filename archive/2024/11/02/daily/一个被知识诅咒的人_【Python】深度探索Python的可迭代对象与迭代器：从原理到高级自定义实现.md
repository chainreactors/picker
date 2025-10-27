---
title: 【Python】深度探索Python的可迭代对象与迭代器：从原理到高级自定义实现
url: https://blog.csdn.net/nokiaguy/article/details/143428576
source: 一个被知识诅咒的人
date: 2024-11-02
fetch_date: 2025-10-06T19:16:48.686888
---

# 【Python】深度探索Python的可迭代对象与迭代器：从原理到高级自定义实现

# 【Python】深度探索Python的可迭代对象与迭代器：从原理到高级自定义实现

![](https://csdnimg.cn/release/blogv2/dist/pc/img/original.png)

[![](https://csdnimg.cn/release/blogv2/dist/pc/img/identityVipNew.png)](https://mall.csdn.net/vip)
[蒙娜丽宁](https://unitymarvel.blog.csdn.net "蒙娜丽宁")
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newUpTime2.png)
已于 2024-11-01 12:03:00 修改

![](https://csdnimg.cn/release/blogv2/dist/pc/img/articleReadEyes2.png)
阅读量1.1k
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)
收藏

22

![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)
点赞数
12

CC 4.0 BY-SA版权

分类专栏：
[Python杂谈](https://blog.csdn.net/nokiaguy/category_12800257.html)
文章标签：
[python](https://so.csdn.net/so/search/s.do?q=python&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[开发语言](https://so.csdn.net/so/search/s.do?q=%E5%BC%80%E5%8F%91%E8%AF%AD%E8%A8%80&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

于 2024-11-01 12:01:01 首次发布

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

本文链接：<https://blog.csdn.net/nokiaguy/article/details/143428576>

[解锁Python编程的无限可能：《奇妙的Python》带你漫游代码世界](https://unitymarvel.blog.csdn.net/article/details/141889588?spm=1001.2014.3001.5502)

在Python编程中，可迭代对象和迭代器构成了许多数据操作的核心。理解它们的定义、如何实现自定义的可迭代对象，以及深入掌握 `__iter__()` 和 `__next__()` 方法的实现细节，不仅能提升代码的可读性和高效性，还为理解Python的底层机制打下坚实基础。本文章从概念入手，通过大量的代码示例和细致的中文注释，深入探讨Python中可迭代对象与迭代器的实现细节。将介绍惰性求值、自定义数据流、多种迭代模式的支持、以及实际应用场景等内容，使读者能扎实掌握Python中这一关键特性。

##### 目录

1. [引言：Python中的迭代协议](#%E5%BC%95%E8%A8%80%EF%BC%9APython%E4%B8%AD%E7%9A%84%E8%BF%AD%E4%BB%A3%E5%8D%8F%E8%AE%AE)
2. [迭代对象与迭代器的基本概念](#%E8%BF%AD%E4%BB%A3%E5%AF%B9%E8%B1%A1%E4%B8%8E%E8%BF%AD%E4%BB%A3%E5%99%A8%E7%9A%84%E5%9F%BA%E6%9C%AC%E6%A6%82%E5%BF%B5)
3. [`__iter__()` 和 `__next__()` 方法的基础实现](#__iter__%28%29-%E5%92%8C-__next__%28%29-%E6%96%B9%E6%B3%95%E7%9A%84%E5%9F%BA%E7%A1%80%E5%AE%9E%E7%8E%B0)
4. [自定义可迭代对象的详细实现](#%E8%87%AA%E5%AE%9A%E4%B9%89%E5%8F%AF%E8%BF%AD%E4%BB%A3%E5%AF%B9%E8%B1%A1%E7%9A%84%E8%AF%A6%E7%BB%86%E5%AE%9E%E7%8E%B0)
5. [惰性求值与生成器迭代器](#%E6%83%B0%E6%80%A7%E6%B1%82%E5%80%BC%E4%B8%8E%E7%94%9F%E6%88%90%E5%99%A8%E8%BF%AD%E4%BB%A3%E5%99%A8)
6. [支持多种迭代模式的自定义迭代器](#%E6%94%AF%E6%8C%81%E5%A4%9A%E7%A7%8D%E8%BF%AD%E4%BB%A3%E6%A8%A1%E5%BC%8F%E7%9A%84%E8%87%AA%E5%AE%9A%E4%B9%89%E8%BF%AD%E4%BB%A3%E5%99%A8)
7. [可迭代对象与迭代器的实际应用场景](#%E5%8F%AF%E8%BF%AD%E4%BB%A3%E5%AF%B9%E8%B1%A1%E4%B8%8E%E8%BF%AD%E4%BB%A3%E5%99%A8%E7%9A%84%E5%AE%9E%E9%99%85%E5%BA%94%E7%94%A8%E5%9C%BA%E6%99%AF)
8. [总结](#%E6%80%BB%E7%BB%93)

---

#### 1. 引言：Python中的迭代协议

在Python中，迭代协议是一种接口标准，主要包括`__iter__()`和`__next__()`方法。这些方法使得Python中的数据结构能够与`for`循环等迭代控制结构兼容。通过实现迭代协议，我们可以轻松访问集合中的每个元素、延迟生成数据，甚至可以处理无限数据流。因此，理解迭代协议和实现可迭代对象，是理解Python语言特性和数据操作的基础。

#### 2. 迭代对象与迭代器的基本概念

在Python中，**可迭代对象**是指实现了 `__iter__()` 方法的对象，这个方法返回一个迭代器。**迭代器**是实现了 `__next__()` 方法的对象，每次调用 `__next__()` 会返回下一个元素，直到数据耗尽。以下是Python中两者的具体定义：

* **可迭代对象**：任何可以返回一个迭代器的对象，例如列表、元组和字典等集合类型。
* **迭代器**：实现了 `__next__()` 方法并能返回下一个元素的对象。

在实现时，通常会使用 `StopIteration` 异常来指示迭代的结束。下面是一个简单的示例，展示了如何手动调用 `__iter__()` 和 `__next__()` 方法：

```
# 示例：手动获取迭代器并逐步获取元素
my_list = [1, 2, 3]
iterator = iter(my_list)  # 获取迭代器

print(next(iterator))  # 输出 1
print(next(iterator))  # 输出 2
print(next(iterator))  # 输出 3
# 下一次调用会引发 StopIteration 异常
```

#### 3. `__iter__()` 和 `__next__()` 方法的基础实现

在Python中，实现迭代器的类需要定义 `__iter__()` 方法来返回自身（`self`），以及 `__next__()` 方法来返回序列中的下一个值。以下是一个简单的自定义迭代器类，实现了数字的计数：

```
class Counter:
    def __init__(self, start, end):
        self.current = start
        self.end = end
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

  12

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

[在现代软件开发中，容器化技术已成为提升应用部署效率和可移植性的关键工具。本文以“Java 与 Docker：容器化部署入门”为主题，深入探讨如何将Java应用无缝集成到Docker环境中。从Docker的基...
---
title: 【计算机视觉】OpenCV 4高级编程与项目实战（Python版）【7】：拼接图像
url: https://blog.csdn.net/nokiaguy/article/details/129289633
source: 一个被知识诅咒的人
date: 2023-03-02
fetch_date: 2025-10-04T08:25:04.546929
---

# 【计算机视觉】OpenCV 4高级编程与项目实战（Python版）【7】：拼接图像

# 【计算机视觉】OpenCV 4高级编程与项目实战（Python版）【7】：拼接图像

![](https://csdnimg.cn/release/blogv2/dist/pc/img/original.png)

[蒙娜丽宁](https://unitymarvel.blog.csdn.net "蒙娜丽宁")
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newUpTime2.png)
已于 2023-03-01 21:02:12 修改

![](https://csdnimg.cn/release/blogv2/dist/pc/img/articleReadEyes2.png)
阅读量1.1k
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)
收藏

2

![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)
点赞数

CC 4.0 BY-SA版权

分类专栏：
[OpenCV高级编程与项目实战（Python版）](https://blog.csdn.net/nokiaguy/category_12162950.html)
文章标签：
[Python](https://so.csdn.net/so/search/s.do?q=Python&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[opencv](https://so.csdn.net/so/search/s.do?q=opencv&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[图像](https://so.csdn.net/so/search/s.do?q=%E5%9B%BE%E5%83%8F&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

于 2023-03-01 21:01:42 首次发布

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

本文链接：<https://blog.csdn.net/nokiaguy/article/details/129289633>

[![](https://i-blog.csdnimg.cn/blog_column_migrate/56256b7598fb005a8c32c420b606b60c.png?x-oss-process=image/resize,m_fixed,h_224,w_224)

OpenCV高级编程与项目实战（Python版）
专栏收录该内容](https://blog.csdn.net/nokiaguy/category_12162950.html "OpenCV高级编程与项目实战（Python版）")

9 篇文章

订阅专栏

我们已经知道，图像是通过数组描述的，那么拼接图像其实就是拼接数组。NumPy提供了2个拼接数组的函数，分别是hstack函数和vstack函数，这两个拼接函数可以将两个数组水平和垂直拼接在一起，也就相当于将两幅图像水平和垂直拼接在一起，本节将详细讲解如何使用这两个函数水平拼接图像和垂直拼接图像。

1. #### 水平拼接

hstack函数可以对数组进行水平拼接，hstack函数的原型如下：

```
hstack(tup) -> array
```

参数说明：

* tup：要拼接的数组元组。

* array：返回值，拼接后生成的新数组。

hstack函数可以拼接多个数组，但每一个参与拼接的数组必须行数相同，例如，2 × 2的数组只能与2行的数组进行拼接，2 × 3、2 × 4的数组都可以与2 × 2的数组进行拼接，但3 × 3的数组不能与2 × 2的数组进行拼接，因为前者是3行，后者是2行。

如果将2个或多个数组进行水平拼接，这些数组会横向首尾相接，如图1所示。

![](https://i-blog.csdnimg.cn/blog_migrate/5a314036d2a382196bb6f2135c3e8569.png)

下面的代码分别水平拼接了3个一维数组（a、b、c）和2个二维数组（x和y）。

```
import numpy as np
a = np.array([1,2,3])
b = np.array([4,5,6])
c = np.array([7,8,9])
result = np.hstack((a,b,c))        # 水平拼接a数组、b数组和c数组
print(result)                    # 输出拼接结果（1×9的数组）
x = np.array([[1,2],[3, 4]])
y = np.array([['a','b','c'],['d', 'e', 'f']])
result = np.hstack((x, y))        # 水平拼接x数组和y数组
print(result)                    # 输出拼接结果（2×5的数组）
```

运行程序，会输出如下的结果：

```
[1 2 3 4 5 6 7 8 9]
[['1' '2' 'a' 'b' 'c']
 ['3' '4' 'd' 'e' 'f']]
```

#### 2. 垂直拼接

vstack函数可以对数组进行垂直拼接，vstack函数的原型如下：

```
vstack(tup) -> array
```

参数说明：

* tup：要拼接的数组元组。

* array：返回值，拼接后生成的新数组。

vstack函数可以拼接多个数组，但每一个参与拼接的数组必须列数相同，例如，2 × 2的数组只能与2列的数组进行拼接，3 × 2、4 × 2的数组都可以与2 × 2的数组进行拼接，但3 × 3的数组不能与2 × 2的数组进行拼接，因为前者是3列，后者是2列。

如果将2个或多个数组进行垂直拼接，这些数组会纵向首尾相接，如图2所示。

![](https://i-blog.csdnimg.cn/blog_migrate/64df417df2838fc0973d63a48ce37b18.png)

下面的代码分别垂直拼接了3个一维数组（a、b、c）和2个二维数组（x和y）。

```
import numpy as np
a = np.array([1,2,3])
b = np.array([4,5,6])
c = np.array([7,8,9])
result = np.vstack((a,b,c))        # 垂直拼接3个1×3的数组（a、b、c）
print(result)                    # 输出垂直拼接的结果
x = np.array([[1,2],[3, 4]])
y = np.array([['a','b'],['c', 'd'],['e', 'f']])
result = np.vstack((x, y))        # 垂直拼接1个2×2的数组和1个3×2的数组
print(result)                    # 输出垂直拼接的结果
```

运行程序，会输出如下的结果。

```
[[1 2 3]
 [4 5 6]
 [7 8 9]]
[['1' '2']
 ['3' '4']
 ['a' 'b']
 ['c' 'd']
 ['e' 'f']]
```

#### 3. 将图像变成2 × 2网格

编写一个程序，通过水平拼接和垂直拼接，将图像变成2 × 2的网格效果，也就是横向2个同样的图像，纵向也有2个同样的图像。代码如下：

```
import cv2
import numpy as np

img = cv2.imread("alien.jpg")
img_h = np.hstack((img, img))          # 水平拼接2个图像
img_v = np.vstack((img_h, img_h))    # 将水平拼接的结果再垂直拼接
cv2.imshow("new_img", img_v)        # 显示拼接效果
cv2.waitKey()
cv2.destroyAllWindows()
```

运行程序，会看到如图3所示的拼接效果。

![](https://i-blog.csdnimg.cn/blog_migrate/5413c43a23e50d6cf6cefaed0fa18bda.png)

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

  0

  点赞
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike.png)

  踩
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCollectActive.png)

  2

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
2552

[随着人工智能（AI）技术的迅猛发展，尤其是生成式AI（AIGC），劳动力市场正经历前所未有的变革。从内容创作到自动化生产线，几乎每个行业都在经历一场技术的洗礼。然而，这场革命并不是全然的光明，它带来了深刻的社会变动，也引发了广泛的担忧和不安。我们不得不面对一个核心问题：AIGC将如何影响未来的工作？会让人类的大多数工作消失，还是会创造出全新的职业机会？](https://unitymarvel.blog.csdn.net/article/details/145234235)

![](https://csdnimg.cn/release/blogv2/dist/components/img/blogType.png)
博客
[【Python图形图像】《Python OpenCV从菜鸟到高手》——零基础进阶，开启图像处理与计算机视觉的大门！](https://unitymarvel.blog.csdn.net/article/details/143574491)

11-07
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
2244

[《Python OpenCV从菜鸟到高手》是一本深入探讨Python与OpenCV技术的图像处理教程。从Python的基础知识到OpenCV的强大功能，这本书带领读者逐步掌握计算机视觉的核心技术。Python因其简洁和强大的库生态被广泛应用于数据分析、人工智能等领域，而OpenCV则是图像处理与计算机视觉的利器。本书通过循序渐进的方式，让读者从零基础到掌握高级图像处理技能，帮助你实现从初学者到高手的跃升。](https://unitymarvel.blog.csdn.net/article/details/143574491)

![](https://csdnimg.cn/release/blogv2/dist/components/img/blogType.png)
博客
[【奇妙的Python】解锁Python编程的无限可能：《奇妙的Python》带你漫游代码世界](https://unitymarvel.blog.csdn.net/article/details/141889588)

09-04
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
3134

[《奇妙的Python——神奇代码漫游之旅》是一本面向实际应用的Python编程指南，涵盖文件操作、GUI设计、多媒体处理、自动化办公、加密解密等多个领域。由华为HDE专家李宁编写，通过丰富的实战案例，帮助读者在工作和项目中高效应用Python，提升编程技能。无论是新手还是有经验的开发者，这本书都将带你深入探索Python的无限可能，开启一段充满创意与实用性的编程之旅。](https://unitymarvel.blog.csdn.net/article/details/141889588)

![](https://csdnimg.cn/release/blogv2/dist/components/img/blogType.png)
博客
[2025机器人产业大洗牌：新兴初创企业的技术革命与崛起之路](https://unitymarvel.blog.csdn.net/article/details/151067555)

09-01
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
1040

[摘要：2025年机器人产业正经历技术驱动的深度变革，AI初创企业通过创新算法和低成本方案挑战传统巨头。本文剖析产业洗牌动因，包括AI融合、融资热潮和应用场景扩展，重点解析人形机器人等关键技术。通过ROS控制、A\*路径规划和PyTorch视觉识别等代码示例（附中文注释），展示初创企业的技术优势。文章预测Figure AI、Unitree等公司将引领消费级机器人市场，推动社会进入智能协作新时代。（150字）](https://unitymarvel.blog.csdn.net/article/details/151067555)

![](https://csdnimg.cn/release/blogv2/dist/components/img/blogType.png)
博客
[Java应用容器化革命：Docker部署从入门到精通](https://unitymarvel.blog.csdn.net/article/details/151067543)

09-01
![](...
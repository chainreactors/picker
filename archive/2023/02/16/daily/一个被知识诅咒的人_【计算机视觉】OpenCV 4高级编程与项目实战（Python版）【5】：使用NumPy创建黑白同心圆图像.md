---
title: 【计算机视觉】OpenCV 4高级编程与项目实战（Python版）【5】：使用NumPy创建黑白同心圆图像
url: https://blog.csdn.net/nokiaguy/article/details/129051147
source: 一个被知识诅咒的人
date: 2023-02-16
fetch_date: 2025-10-04T06:44:40.923427
---

# 【计算机视觉】OpenCV 4高级编程与项目实战（Python版）【5】：使用NumPy创建黑白同心圆图像

# 【计算机视觉】OpenCV 4高级编程与项目实战（Python版）【5】：使用NumPy创建黑白同心圆图像

![](https://csdnimg.cn/release/blogv2/dist/pc/img/original.png)

[蒙娜丽宁](https://unitymarvel.blog.csdn.net "蒙娜丽宁")
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newUpTime2.png)
已于 2023-02-15 22:31:40 修改

![](https://csdnimg.cn/release/blogv2/dist/pc/img/articleReadEyes2.png)
阅读量1.1k
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)
收藏

3

![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)
点赞数

CC 4.0 BY-SA版权

分类专栏：
[OpenCV高级编程与项目实战（Python版）](https://blog.csdn.net/nokiaguy/category_12162950.html)
文章标签：
[python](https://so.csdn.net/so/search/s.do?q=python&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[OpenCV](https://so.csdn.net/so/search/s.do?q=OpenCV&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[numpy](https://so.csdn.net/so/search/s.do?q=numpy&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

于 2023-02-15 21:44:23 首次发布

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

本文链接：<https://blog.csdn.net/nokiaguy/article/details/129051147>

[![](https://i-blog.csdnimg.cn/blog_column_migrate/56256b7598fb005a8c32c420b606b60c.png?x-oss-process=image/resize,m_fixed,h_224,w_224)

OpenCV高级编程与项目实战（Python版）
专栏收录该内容](https://blog.csdn.net/nokiaguy/category_12162950.html "OpenCV高级编程与项目实战（Python版）")

9 篇文章

订阅专栏

![](https://i-operation.csdnimg.cn/images/a7311a21245d4888a669ca3155f1f4e5.png)文章介绍了如何在OpenCV中利用NumPy数组来表示和操作图像，包括创建纯黑色和纯白色图像，以及在黑色图像上绘制白色图像和同心圆。OpenCV的imread函数返回的是NumPy数组，可以通过数组索引来改变图像的像素值，实现图像的绘制和编辑功能。

OpenCV中使用数组表示图像数据，不过这里的数组并不是Python数组，而是NumPy数组。NumPy是非常著名的科学计算库，可用于进行各种科学计算，由于底层使用C语言实现，所以效率非常高。

读者使用type函数输出imread函数的返回值看看这个函数返回的到底是什么数据类型，代码如下：

```
rgb_image = cv2.imread("flower.png")
print(type(rgb_image))
```

运行程序，会输出如下的内容：

```
<class 'numpy.ndarray'>
```

很明显，imread函数返回的是一个Numpy数组。既然OpenCV内部使用了NumPy数组管理图像，那么也可以通过创建NumPy数组的方式来创建图像，所以本节将直接通过NumPy来操作黑白和彩色图像。

在OpenCV中，黑白图像通过一个二维数组表示，彩色图像使用一个三维数组表示，这也非常容易理解。对于黑白图像来说，每一个像素点只有2个颜色：黑和白。通常用255表示白，用0表示黑。二维数组的每一个数组值正好表示黑和白两个颜色，数组的行和列就是图像的高和宽（图像尺寸），数组元素的个数就是图像中像素的个数。

对于彩色图像（RGB色彩空间）来说，每一个像素点需要3个值表示3种颜色（R、G和B），所以需要多出一个维度来表示颜色，因此，彩色图像需要用3维数组表示。

1. #### 创建纯黑色图像

在黑白图像中，像素值为0表示纯黑色，像素值为255表示纯白色。所以只需要用NumPy创建一个二维数组，并且每一个数组值为0，就是纯黑色图像，每一个数组值为255，就是纯白色图像。

下面的代码创建一个宽度和高度都是200的NumPy数组，数组元素格式为无符号8位整数，用0填充整个数组，最后将数组作为图像显示。

```
import cv2
import numpy as np

width = 200  # 图像的宽
height = 200  # 图像的高
# 创建指定宽高、单通道、像素值都为0的图像
img = np.zeros((height, width), np.uint8)
cv2.imshow("black image", img)  # 显示纯黑图像
cv2.waitKey()
cv2.destroyAllWindows()
```

运行程序，会看到如图1所示的纯黑图像。

![](https://i-blog.csdnimg.cn/blog_migrate/d0ef002f0e7ad3849aef0613fbf44e9c.png)

#### 2. 创建纯白色图像

创建纯白图像需要将二维数组中的每一个值都设置为255，可以先创建纯黑图像，然后将图像中所有的像素值都改为255，或者直接使用NumPy提供的ones函数创建一个像素值为1的数组，然后让数组乘以255，同样可以得到一个数组值都为255的数组，也就是纯白色的图像。

下面的代码创建一个宽度和高度都是200的NumPy数组，数组元素格式为无符号8位整数，用1填充整个数组，然后让数组与255相乘，最后将数组作为图像显示。

```
import cv2
import numpy as np

width = 200  # 图像的宽
height = 200  # 图像的高
# 创建指定宽高、单通道、像素值都为1的图像
img = np.ones((height, width), np.uint8) * 255
cv2.imshow("white", img)  # 显示图像
cv2.waitKey()
cv2.destroyAllWindows()
```

运行程序，会看到如图2所示的纯白图像。

![](https://i-blog.csdnimg.cn/blog_migrate/c75cc77e15ac04aea91d809b82744dce.png)

#### 3. 在黑色图像内部绘制白色图像

下面的代码先绘制黑色图像作为背景，然后用切片索引的方式将图像中纵坐标在80~150之间，横坐标在60~130之间的矩形区域改为白色，代码如下：

```
import cv2
import numpy as np

width = 200
height = 200
# 创建指定宽高、单通道、像素值都为0的图像
img = np.zeros((height, width), np.uint8)
# 图像纵坐标80~150、横坐标60~130之间的区域变为白色
img[80:151, 60:131] = 255
cv2.imshow("img", img)  # 显示图像
cv2.waitKey()
cv2.destroyAllWindows()
```

运行程序，会看到如图3所示的效果。

![](https://i-blog.csdnimg.cn/blog_migrate/c23305c67f9468399b38005be7fa4e8e.png)

注意：Python切片是半开半闭区间，即取值范围并不包含冒号（:）后面数值。例如，纵坐标在80~150范围内，应该使用[80:151]。

#### 4. 在黑色图像内部绘制白色同心圆

下面的代码在黑色背景正中心绘制3个不同半径的同心圆，半径分别为30,50和80。并且让同心圆的圆周线厚度为3。

通过像素点绘制圆形最常用的方式是通过三角函数计算圆周线上每一个像素点的坐标，然后在这些坐标上绘制白色像素点。如果加厚圆周线，只需要再绘制相邻半径的同心圆即可。例如，让半径为30的圆的圆周线的厚度是3，只需要在绘制半径分别为29和31的同心圆即可，代码如下：

```
import cv2
import math
import numpy as np

width = 200
height = 200
# 创建指定宽高、单通道、像素值都为0的图像
img = np.zeros((height, width), np.uint8)
# 同心圆中心坐标
centerX = 100
centerY = 100
# 定义同心圆半径
radiusList = [29,30,31, 49,50,51, 79,80,81]
# 通过循环，计算同心圆的圆周线上的坐标，并将坐标对应的位置设置为255（白色）
for radius in radiusList:
    # 从0到359度
for angle in range(0,360):
    # 将角度转换为弧度
        radian = (angle/360) * 2 * math.pi
        # 计算圆周线当前点的横坐标
        pointX = int(centerX + radius * math.cos(radian))
        # 计算圆周线当前点的纵坐标
        pointY = int(centerY - radius * math.sin(radian))
        #将圆周线上的像素点设置为白色
        img[pointY, pointX] = 255
cv2.imshow("img", img)  # 显示图像
cv2.waitKey()
cv2.destroyAllWindows()
```

运行程序，会看到如图4所示的效果。

![](https://i-blog.csdnimg.cn/blog_migrate/e5506d83884ac776d66b42314f34e1d1.png)

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

  3

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
![](https://csd...
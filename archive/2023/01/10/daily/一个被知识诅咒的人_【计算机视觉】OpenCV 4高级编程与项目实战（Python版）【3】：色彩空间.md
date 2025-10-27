---
title: 【计算机视觉】OpenCV 4高级编程与项目实战（Python版）【3】：色彩空间
url: https://blog.csdn.net/nokiaguy/article/details/128621423
source: 一个被知识诅咒的人
date: 2023-01-10
fetch_date: 2025-10-04T03:23:18.724612
---

# 【计算机视觉】OpenCV 4高级编程与项目实战（Python版）【3】：色彩空间

# 【计算机视觉】OpenCV 4高级编程与项目实战（Python版）【3】：色彩空间

![](https://csdnimg.cn/release/blogv2/dist/pc/img/original.png)

[蒙娜丽宁](https://unitymarvel.blog.csdn.net "蒙娜丽宁")
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newUpTime2.png)
已于 2023-01-14 17:29:14 修改

![](https://csdnimg.cn/release/blogv2/dist/pc/img/articleReadEyes2.png)
阅读量2.4k
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)
收藏

5

![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)
点赞数
2

CC 4.0 BY-SA版权

分类专栏：
[OpenCV高级编程与项目实战（Python版）](https://blog.csdn.net/nokiaguy/category_12162950.html)
文章标签：
[计算机视觉](https://so.csdn.net/so/search/s.do?q=%E8%AE%A1%E7%AE%97%E6%9C%BA%E8%A7%86%E8%A7%89&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[python](https://so.csdn.net/so/search/s.do?q=python&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[opencv](https://so.csdn.net/so/search/s.do?q=opencv&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

于 2023-01-09 21:55:31 首次发布

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

本文链接：<https://blog.csdn.net/nokiaguy/article/details/128621423>

[![](https://i-blog.csdnimg.cn/blog_column_migrate/56256b7598fb005a8c32c420b606b60c.png?x-oss-process=image/resize,m_fixed,h_224,w_224)

OpenCV高级编程与项目实战（Python版）
专栏收录该内容](https://blog.csdn.net/nokiaguy/category_12162950.html "OpenCV高级编程与项目实战（Python版）")

9 篇文章

订阅专栏

![](https://i-operation.csdnimg.cn/images/a7311a21245d4888a669ca3155f1f4e5.png)本文深入讲解OpenCV4(Python版)的图像处理技术，重点讨论了从RGB/BGR色彩空间到GRAY和HSV色彩空间的转换，包括灰度图像的概念、色彩空间转换函数cvtColor的使用以及RGB和HSV色彩空间的特点与转换。

视频课程：[《Python OpenCV 4高级编程与实战》](https://edu.csdn.net/course/detail/37684 "《Python OpenCV 4高级编程与实战》")

        本系列文章会深入讲解OpenCV 4（Python版）的核心技术，并提供了大量的实战案例。这是本系列文章的第3篇，主要讲解OpenCV处理图像的基本方法，主要包括读取图像、显示图像、保存图像和获取图像的属性。

**目录**

[1. 灰度（GRAY）色彩空间](#1.%20%E7%81%B0%E5%BA%A6%EF%BC%88GRAY%EF%BC%89%E8%89%B2%E5%BD%A9%E7%A9%BA%E9%97%B4)

[2. 从RGB/BGR色彩空间转换到GRAY色彩空间](#2.%20%E4%BB%8ERGB%2FBGR%E8%89%B2%E5%BD%A9%E7%A9%BA%E9%97%B4%E8%BD%AC%E6%8D%A2%E5%88%B0GRAY%E8%89%B2%E5%BD%A9%E7%A9%BA%E9%97%B4)

[3. RGB色彩空间的局限性](#3.%20RGB%E8%89%B2%E5%BD%A9%E7%A9%BA%E9%97%B4%E7%9A%84%E5%B1%80%E9%99%90%E6%80%A7)

[4. 适合图像处理的HSV色彩空间](#4.%20%E9%80%82%E5%90%88%E5%9B%BE%E5%83%8F%E5%A4%84%E7%90%86%E7%9A%84HSV%E8%89%B2%E5%BD%A9%E7%A9%BA%E9%97%B4)

[5. RGB/BGR色彩空间与HSV色彩空间之间相互转换](#5.%20RGB%2FBGR%E8%89%B2%E5%BD%A9%E7%A9%BA%E9%97%B4%E4%B8%8EHSV%E8%89%B2%E5%BD%A9%E7%A9%BA%E9%97%B4%E4%B9%8B%E9%97%B4%E7%9B%B8%E4%BA%92%E8%BD%AC%E6%8D%A2)

---

        在上一篇文章中，简单介绍了BGR色彩空间和RGB色彩空间，本文将介绍另外两个比较常见的色彩空间：GRAY色彩空间和HSV色彩空间。

### 1. 灰度（GRAY）色彩空间

        GRAY色彩空间通道指的是灰度图像，灰度图像的通常只有1个，值范围是[0, 255]，一共256个灰度级别。其中0表示纯黑色，255表示纯白色。0～255之间的数值表示不同的亮度（即色彩的深浅程度）的深灰色或浅灰色。因此，一副灰度图能展示丰富的细节信息，如图1所示。

![](https://i-blog.csdnimg.cn/blog_migrate/c1c640cb824c6ad751a85fb4214c951c.png)

### 2. 从RGB/BGR色彩空间转换到GRAY色彩空间

        不难发现，上一篇文章中的彩色花朵图与图1其实是一副图像，只是前者是彩色图像，后者是灰度图像。从这一点可以看出，同一副图像，是可以从一个色彩空间切换到另一个色彩空间的，OpenCV把这个转换过程称为色彩空间类型转换。

        那么，OpenCV是如何将图像从BGR色彩空间转换到GRAY色彩空间，进而得到图1所示的灰度图呢？答案就是OpenCV中的cvtColor函数。cvtColor函数用于转换图像的色彩空间，该函数的原型如下：

```
cvtColor(src, code[, dst[, dstCn]]) ->   dst
```

参数说明：

* src：转换前的初始图像数据。
* code：色彩空间转换码。
* dst：可选参数。dst既是参数，也是返回值，转换后的图像数据（目标图像数据）。也就是说，转换结果，可以通过cvtColor函数返回，也可以通过dst参数返回。
* dstCn：可选参数。目标图像的通道数，默认值是0，通道数会自动通过src参数和code参数确定。

        OpenCV提供的色彩空间转换码非常多，本文只给出与BGR/RGB色彩空间和GRAY色彩空间相关的转换码，如表1所示。

![](https://i-blog.csdnimg.cn/blog_migrate/be355fe413013e25c57d8baf26372543.png)

下面的代码将彩色图像flower.jpg从BGR色彩空间转换到GRAY色彩空间。

```
import cv2
image = cv2.imread("images/flower.jpg")
# 显示彩色图像
cv2.imshow("flower", image)
# 将BGR色彩空间的图像转换到GRAY色彩空间的图像
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# 显示灰度图像
cv2.imshow("GRAY", gray_image)
cv2.waitKey()
cv2.destroyAllWindows()
```

运行程序，会看到如图2所示的转换效果。

![](https://i-blog.csdnimg.cn/blog_migrate/0097abd4a8fe2f2699662775f4d94279.png)

*注意：尽管色彩空间类型的转换是双向的，而且OpenCV**也提供了  cv2.COLOR\_GRAY2BGR**和cv2.COLOR\_GRAY2RGB**空间转换码，但由于彩色图像转换到灰度图像时，已经将颜色比例（也就是红色、绿色和蓝色之间的混合比例）丢失了，一旦丢失，将无法恢复。所以尽管可以使用这2**个空间转换码将GRAY**色彩空间抓好为BGR**色彩空间和RGB**色彩空间，但转换结果仍然是灰度图像。*

### 3. RGB色彩空间的局限性

        RGB是我们接触最多的色彩空间，通过红色（R），绿色（G）和蓝色（B）这3种颜色的不同组合可以形成几乎所有的颜色。RGB 色彩空间是图像处理中最基本、最常用、面向硬件的颜色空间，比较容易理解。

        RGB 色彩空间利用3个颜色分量的线性组合来表示颜色，任何颜色都与这三个分量有关，而且这3个分量是高度相关的，所以连续变换颜色时并不直观，想对图像的颜色进行调整需要更改这3个分量才行。

        自然环境下获取的图像容易受自然光照、遮挡和阴影等情况的影响，即对亮度比较敏感。而 RGB 色彩空间的3个分量都与亮度密切相关，即只要亮度改变，3个分量都会随之相应地改变。

        但是人眼对于这3种颜色分量的敏感程度是不一样的，在单色中，人眼对红色最不敏感，蓝色最敏感，所以 RGB 色彩空间是一种均匀性较差的色彩空间。如果颜色的相似性直接用欧氏距离来度量，其结果与人眼视觉会有较大的偏差。对于某一种颜色，我们很难推测出较为精确的3个分量数值来表示。

所以RGB 色彩空间适合于显示系统，并不适合于图像处理。

### 4. 适合图像处理的HSV色彩空间

        在图像处理中使用较多的是 HSV 色彩空间，它比 RGB 更接近人们对彩色的感知经验。非常直观地表达颜色的色调、鲜艳程度和明暗程度，方便进行颜色的对比。

        在 HSV 色彩空间下，比 RGB色彩空间更容易跟踪某种颜色的物体，常用于分割指定颜色的物体。

HSV 色彩空间表达彩色图像的方式由3个部分组成：

* Hue（色调）
* Saturation（饱和度）
* Value（亮度）

        用图3所示的圆柱体来表示 HSV 色彩空间，圆柱体的横截面可以看做是一个极坐标系 ，H 用极坐标的极角表示，S 用极坐标的极轴长度表示，V 用圆柱中轴的高度表示。

![](https://i-blog.csdnimg.cn/blog_migrate/97227c4b40cff0b6f71c5f537b514c4a.png)

Hue 用角度表示，取值范围是0～360，表示色彩信息，即所处的光谱颜色的位置，如图4所示。

![](https://i-blog.csdnimg.cn/blog_migrate/61ea5740dcb0b25a83ccf454ddc5a7c0.png)

        颜色圆环上所有的颜色都是光谱上的颜色，从红色开始按逆时针方向旋转，Hue=0 表示红色，Hue=120 表示绿色，Hue=240 表示蓝色，其他角度的颜色都是用R、G、B混合出来的颜色。

        在 RGB色彩空间中，颜色由3个值共同决定，比如黄色是(255,255,0)。在HSV色彩空间中，黄色只由一个值决定，即Hue=60。

        HSV色彩空间的饱和度（Saturation）和透明度（Value）用百分比表示，取值范围是0～100%。饱和度越高，说明颜色越深，越接近光谱色。饱和度越低，说明颜色越浅，越接近白色。饱和度为0表示纯白色。值越大，颜色越饱和。

        透明度越高，表示颜色越明亮，透明度越低，表示颜色越暗，透明度为0表示纯黑色。

        我们也可以利用一些图像处理工具来观察RGB色彩空间与HSV色彩空间的对应关系，如PS就是非常好的图像处理工具，打开PS，选择前景色或背景色，会显示一个颜色选择窗口，如图5所示。将RGB色彩空间中的R、G、B分别调整为255、255、0，即黄色。RGB的黄色对应了HSV色彩空间中H=60的颜色，如果正好是光谱颜色，那么S = V = 100%。

![](https://i-blog.csdnimg.cn/blog_migrate/c21a99d6fbf149e6cab1f8917f5eebcf.png)

        可能很多读者还无法理解到底什么是饱和度和透明度，下面就更直观解释一下饱和度和透明度。在Hue色彩空间中，饱和度减小，就相当于往光谱色中添加白色，光谱色所占的比例也在减小，饱和度减为0，表示光谱色所占的比例为零，导致整个颜色呈现白色。

        透明度减小，就相当于往光谱色中添加黑色，光谱色所占的比例也在减小，透明度减为0，表示光谱色所占的比例为零，导致整个颜色呈现黑色。

        HSV 色彩空间对用户来说是一种比较直观的颜色模型。我们可以很轻松地得到单一颜色值，即指定颜色角H，并让V=S=1，然后通过向其中加入黑色和白色来得到我们需要的颜色。增加黑色可以减小V而S不变，同样增加白色可以减小S而V不变。例如，要得到深蓝色，V=0.4 S=1 H=240。要得到浅蓝色，V=1 S=0.4 H=240度。

### 5. RGB/BGR色彩空间与HSV色彩空间之间相互转换

        OpenCV提供的cvtColor函数不仅可以将图像从RGB/BGR色彩空间转换到GRAY色彩空间，还能将图像在RGB/BGR色彩空间与HSV色彩空间之间相互转换。表2是将图像在RGB/BGR色彩空间与HSV色彩空间之间转换时需要使用的色彩空间转换吗。

![](https://i-blog.csdnimg.cn/blog_migrate/d1fb9c9e56b571d111c379fb305a604c.png)

        下面的代码将BGR色彩空间的图像（flower.jpg）与HSV色彩空间互相转换，并保存转换结果。

```
import cv2
image = cv2.imread("images/flower.jpg")
cv2.imshow("flower", image)
# 从BGR色彩空间转换到HSV色彩空间
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow("hsv", hsv_image)
cv2.imwrite("images/flower_hsv.jpg",hsv_image)
image = cv2.imread("images/flower_hsv.jpg")
cv2.imshow("hsv1", image)
# 从HSV色彩空间转换到BGR色彩空间
rgb_image = cv2.cvtColor(image, cv2.COLOR_HSV2BGR)
cv2.imshow("rgb", rgb_image)
cv2.waitKey()
cv2.destroyAllWindows()
```

        运行这段程序，会显示4个窗口。其中图6是原图，图7是转换到HSV色彩空间的图像。图8是读取的HSV色彩空间的图像。图9是从HSV色彩空间转换到BGR色彩空间后的效果。

![](https://i-blog.csdnimg.cn/blog_migrate/cc3a56ca85f4e8871daf82f166eee764.png)

![](https://i-blog.csdnimg.cn/blog_migrate/e2d58702fc4023d53042203dc09c8df6.png)

![](https://i-blog.csdnimg.cn/blog_migrate/c86a7583b2e5a0aaad1aaf7d22dcb575.png)

![](https://i-blog.csdnimg.cn/blog_migrate/700c65d6d2b303531552e3ddb0bb5f85.png)

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

* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarThumbUpactive.p...
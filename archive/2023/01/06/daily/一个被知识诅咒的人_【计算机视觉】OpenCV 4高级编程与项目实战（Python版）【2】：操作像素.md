---
title: 【计算机视觉】OpenCV 4高级编程与项目实战（Python版）【2】：操作像素
url: https://blog.csdn.net/nokiaguy/article/details/128569218
source: 一个被知识诅咒的人
date: 2023-01-06
fetch_date: 2025-10-04T03:08:39.645225
---

# 【计算机视觉】OpenCV 4高级编程与项目实战（Python版）【2】：操作像素

# 【计算机视觉】OpenCV 4高级编程与项目实战（Python版）【2】：操作像素

![](https://csdnimg.cn/release/blogv2/dist/pc/img/original.png)

[蒙娜丽宁](https://unitymarvel.blog.csdn.net "蒙娜丽宁")
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newUpTime2.png)
已于 2023-01-14 17:28:47 修改

![](https://csdnimg.cn/release/blogv2/dist/pc/img/articleReadEyes2.png)
阅读量1.3k
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)
收藏

6

![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)
点赞数
2

CC 4.0 BY-SA版权

分类专栏：
[OpenCV高级编程与项目实战（Python版）](https://blog.csdn.net/nokiaguy/category_12162950.html)
文章标签：
[python](https://so.csdn.net/so/search/s.do?q=python&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[计算机视觉](https://so.csdn.net/so/search/s.do?q=%E8%AE%A1%E7%AE%97%E6%9C%BA%E8%A7%86%E8%A7%89&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[opencv](https://so.csdn.net/so/search/s.do?q=opencv&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

于 2023-01-05 19:55:10 首次发布

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

本文链接：<https://blog.csdn.net/nokiaguy/article/details/128569218>

[![](https://i-blog.csdnimg.cn/blog_column_migrate/56256b7598fb005a8c32c420b606b60c.png?x-oss-process=image/resize,m_fixed,h_224,w_224)

OpenCV高级编程与项目实战（Python版）
专栏收录该内容](https://blog.csdn.net/nokiaguy/category_12162950.html "OpenCV高级编程与项目实战（Python版）")

9 篇文章

订阅专栏

![](https://i-operation.csdnimg.cn/images/a7311a21245d4888a669ca3155f1f4e5.png)本文介绍了OpenCV4Python版中处理图像的基本方法，包括读取、显示和保存图像，以及获取图像像素的BGR值。文章强调了像素坐标系统（OpenCV使用y,x而非x,y），并展示了如何通过坐标访问和修改像素颜色。此外，还提供了将图像特定区域设为黑色的代码示例。

视频课程：[《Python OpenCV 4高级编程与实战》](https://edu.csdn.net/course/detail/37684)

本系列文章会深入讲解OpenCV 4（Python版）的核心技术，并提供了大量的实战案例。这是本系列文章的第2篇，主要讲解OpenCV处理图像的基本方法，主要包括读取图像、显示图像、保存图像和获取图像的属性。

像素是构成图像的基本单位。现在看图1所示的花卉图像，这幅图看着很细腻，不过将图像的白框区域放大，会看到如图2所示的效果，细腻的图像不见了，取而代之的是一个一个的小方块，每一个小方块就是一个像素。

![](https://i-blog.csdnimg.cn/blog_migrate/71d5d798a45152298dea08f23506ee03.png)

如果从显示器的角度，像素就是显示器可以显示的最小的点。像素之所以在图2所示的图中看着像一个方块，是因为如果将图像的某个区域放大，就需要将一个像素变成多个像素，这就会造成多个相邻的像素的颜色都相同，所以看着这些像素就变成了一个个小方块。

像素本身的形状并不重要，因为显示器已经无法分辨比像素更小的单元了，因此，像素是显示器可以分辨颜色的极限。所以只需要将像素想象成一个没有面积彩色小点即可。

### 1.确定像素的位置

在访问图像的像素之前，需要先了解如何确定图像中的像素。图像中的像素是通过坐标来描述的，例如，(210,235)表示在210和235这一点上的像素。不过先别忙，OpenCV在描述坐标时与传统描述方式不同，传统的坐标描述方式是(x,y)，而OpenCV的描述方式是(y,x)，千万别弄混了。也就是说，如果(210,235)是OpenCV的坐标，那么表示第210行，第235列的交汇点处的像素。

下面来看一下OpenCV的坐标系，图3是一副花卉的图。OpenCV坐标系是以图像的左上角为原点，Y轴正方向向下，X轴正方向向右。这幅图的分辨率是600×400，所以如果用OpenCV坐标描述左下角像素的坐标，应该是(400,0)，右下角像素的坐标是(400,600)。

![](https://i-blog.csdnimg.cn/blog_migrate/c1a0b9d0f5aefbafd7cdaa852896fc80.png)

不过由于Python的列表元素是从0开始的，所以左下角像素的坐标应该是(399,0)，右下角像素的坐标应该是(399, 599)。

如果不想用编程的方式获取图像的某个像素的坐标和分辨率，可以用一些工具软件，例如Windows的“画图”程序（如图4所示）可以很容易获得像素坐标和分辨率，只不过像素坐标是(x,y)形式的，需要将坐标的两个值调换位置后才是OpenCV的像素坐标。用“画图”打开图像，将鼠标放到图像上，左下角黑框中是鼠标所在像素的坐标，整下方黑框内是图像的分辨率。

![](https://i-blog.csdnimg.cn/blog_migrate/de68c6804bd4984394fdab1d60660d66.png)

### 2.读取像素的BGR值

使用imread函数读取图像的数据后，可以使用下面的代码获得像素对应的颜色值。

```
import cv2
image = cv2.imread("flower.jpg")
px = image[200,300]    # 获取坐标(200,300)的像素值
print(px)
```

执行这段代码，会输出如下的内容：

```
[207 142 211]
```

px本身是一个列表，列表中有3个元素值，分别代表B（蓝）、G（绿）和R（红）3中颜色，也就是通常说的三原色。要注意，通过这种方式获取的三原色并不是习惯上的RGB，而是BGR。通过将3种颜色按不同值（每一种颜色值的范围从0到255）组合，就会呈现出各种颜色，三原色总共可以表示16777216（256 × 256 × 256）种颜色。

如果使用imread函数读取的是彩色图像，那么图像数据是包含通道的，BGR中的B、G、R就是彩色图像的3个通道。BGR也成为色彩空间，如果改变了通道顺序，如将BGR变成RGB，那么就又形成了另外一种色彩空间。而OpenCV选择了BGR色彩空间，不过这些色彩空间可以相互转换，在后面的文章会详细介绍这部分内容。

除了一下子获取BGR三个通道的颜色值外，也可以使用下面的代码分别获取独立的B、G、R值。

```
import cv2
image = cv2.imread("images/flower.jpg")
blue = image[200,300,0]            # 获取B通道的颜色值
green = image[200,300,1]        # 获取G通道的颜色值
red = image[200,300,2]            # 获取R通道的颜色值
print(blue, green, red)           # 输出BGR通道的颜色值
```

运行这段代码，会输出如下内容：

```
[207 142 211]
[255   0   0]
```

从输出结果可以看出，像素(200,300)的BGR值已经被修改。但阅读这段代码，需要注意如下几点：

* 这里修改的只是内存中图像的像素值，并没有将修改结果保存到图像文件中，如果想保存修改结果，需要使用imwrite函数。

* 在修改像素值时，不要直接修改px的值，而是直接为image[y,x]赋值，否则修改的只是px变量的值，image[y,x]的值并未改变，如下面的代码是无法修改像素(200,300)的颜色值的。

```
px = [255,255,255]
```

说明：不管是RGB色彩空间，还是BGR色彩空间，只要R、G、B三个通道的值相等，彩色图像就变成了灰度图像，其中R = G = B = 0是纯黑色，R = G = B = 255是纯白色。

下面的代码将flower.jpg中由(120,230)、(120, 310)、(190, 230)和(190, 310)这4个点围起的矩形区域变成纯黑色，并在窗口中展示原图和修改过的图，最后将修改结果保存在flower\_new.jpg文件中。

```
import cv2

image = cv2.imread("images/flower.jpg")
cv2.imshow("oldimage", image)            # 在窗口中显示原图像
for i in range(120, 191):                 # i表示纵坐标，在区间[120，190]内取值
    for j in range(230, 311):             # j表示横坐标，在区间[230, 310]内取值
        image[i, j] = [0, 0, 0]             # 把区域内的所有像素都修改为黑色
cv2.imshow("newimage", image)            # 在窗口中显示修改后的图像
cv2.imwrite("images/flower_new.jpg", image)        # 保存修改结果
cv2.waitKey()
cv2.destroyAllWindows()
```

运行这段程序，会看到如图5（原图）和图6（修改后的图像）所示的效果。

![](https://i-blog.csdnimg.cn/blog_migrate/60376aa17a341b55aa5ff1ed2f2f8d14.png)

![](https://i-blog.csdnimg.cn/blog_migrate/204e1c5a45d13b838c99342179f4066e.png)

同时在images目录多了一个flower\_new.jpg文件，效果与图6所示的效果完全相同。

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

  2

  点赞
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike.png)

  踩
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCollectActive.png)

  6

  收藏

  觉得还不错?
  一键收藏
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/collectionCloseWhite.png)
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/guideRedReward01.png)
  知道了

  [![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/comment.png)

  3](#commentBox)

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

3 条评论
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

[《Python OpenCV从菜鸟到高手》是一本深入探讨Python与OpenCV技术的图像处理教程。从Python的基础知识到OpenCV的强大功能，这本书带领读者逐步掌握计算机视觉的核心技术。Python因其简洁和强大的库生态被广泛应用于数据分析、人工智能等领域，而OpenCV则是图像处理与计算机视觉的利器。本书通过循序渐进的方式，让读者从零基础到掌握高级图像处理技能，帮助你实现从初学者到高手的跃升。](https://unitymarvel.blog.csdn.net/article/details/1...
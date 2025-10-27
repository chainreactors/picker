---
title: 【计算机视觉】OpenCV 4高级编程与项目实战（Python版）【4】：通道详解
url: https://blog.csdn.net/nokiaguy/article/details/128772938
source: 一个被知识诅咒的人
date: 2023-01-28
fetch_date: 2025-10-04T05:02:20.245117
---

# 【计算机视觉】OpenCV 4高级编程与项目实战（Python版）【4】：通道详解

# 【计算机视觉】OpenCV 4高级编程与项目实战（Python版）【4】：通道详解

原创
已于 2023-01-27 22:15:24 修改
·
1.6k 阅读

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)

0

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)

1
·

CC 4.0 BY-SA版权

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

文章标签：

[#opencv](https://so.csdn.net/so/search/s.do?q=opencv&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#python](https://so.csdn.net/so/search/s.do?q=python&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#计算机视觉](https://so.csdn.net/so/search/s.do?q=%E8%AE%A1%E7%AE%97%E6%9C%BA%E8%A7%86%E8%A7%89&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

于 2023-01-27 21:23:30 首次发布

[![](https://i-blog.csdnimg.cn/blog_column_migrate/56256b7598fb005a8c32c420b606b60c.png?x-oss-process=image/resize,m_fixed,h_224,w_224)

OpenCV高级编程与项目实战（Python版）
专栏收录该内容](https://blog.csdn.net/nokiaguy/category_12162950.html "OpenCV高级编程与项目实战（Python版）")

9 篇文章

订阅专栏

视频课程：[《Python OpenCV 4高级编程与实战》](https://edu.csdn.net/course/detail/37684)

相信很多读者朋友对“通道”这个词已经不陌生了，一副BGR图像是由3个通道组成的，这3个通道是B通道、G通道和R通道。本节将介绍如何对通道进行拆分与合并，并达到处理图像的目的。

### 1.拆分BGR图像中的通道

OpenCV提供的split函数可以拆分图像中的通道。split函数的原型如下：

```
    split(image)-> b,g,r
```

参数说明：

* image：待拆分通道的BGR图像，也就是imread函数返回的值。

* b：B通道图像。

* g：G通道图像。

* r：R通道图像。

注意：拆分BGR图像中通道的顺序是B、G、R，因此，split函数的3个返回值的顺序不能打乱顺序，必须是b、g、r。

下面的例子拆分flower.jpg图像中的通道，然后再显示拆分后的通道图像，代码如下：

```
import cv2
rgb_image = cv2.imread("images/flower.jpg")
cv2.imshow("flower", rgb_image)
# 拆分图像的通道
b, g, r = cv2.split(rgb_image)
# 显示B通道图像
cv2.imshow("B", b)
# 显示G通道图像
cv2.imshow("G", g)
# 显示R通道图像
cv2.imshow("R", r)
cv2.waitKey()
cv2.destroyAllWindows()
```

运行这段代码，会得到如下面所示的4个窗口。其中，图1是原图像，图2是B通道图像，图3是G通道图像，图4是R通道图像。

![](https://i-blog.csdnimg.cn/blog_migrate/37615049914dc5acf14e9959feb7df51.png)

![](https://i-blog.csdnimg.cn/blog_migrate/66c34086eea1b07320ec102e58806eaf.png)

![](https://i-blog.csdnimg.cn/blog_migrate/62761ab2dc64d91883c84a0badd55b1e.png)

![](https://i-blog.csdnimg.cn/blog_migrate/b0d4843047b0244b38e447c98a817803.png)

看到这3个通道的图像，可能很多读者会感到奇怪。B通道是蓝色通道，G通道是绿色通道，R通道是红色通道，但图2、图3和图4看到的都是灰度图像，这是为什么呢？

原因是使用cv2.imshow函数时，会用一个通道的值填充另外两个通道。例如，用cv2.imshow("B", b)显示B通道图像时，会用B通道的值填充G通道和R通道，即(B,B,B)，所以用cv2.imshow函数显示的图像，总是灰度图像。

### 2. 拆分HSV图像中的通道

使用split函数不仅可以拆分BGR图像的通道，也可以拆分HSV图像的通道，拆分HSV图像通道，split函数会返回h、s、v，原型如下：

```
split(image)-> h,s,v
```

参数说明：

* image：待拆分的HSV图像。

* h：H通道图像。

* s：S通道图像。

* v：V通道图像。

下面的代码将flower.jpg从BGR色彩空间转换到HSV色彩空间，然后拆分得到HSV图像中的通道，最后显示拆分后的通道图像。代码如下：

```
import cv2

rgb_image = cv2.imread("images/flower.jpg")
# 显示flower.jpg
cv2.imshow("flower", rgb_image)
# 将flower.jpg从BGR色彩空间转换到HSV色彩空间
hsv_image = cv2.cvtColor(rgb_image, cv2.COLOR_BGR2HSV)
# 拆分HSV图像中的通道
h, s, v = cv2.split(hsv_image)
cv2.imshow("H", h)                # 显示HSV图像中H通道的图像
cv2.imshow("S", s)                # 显示HSV图像中S通道的图像
cv2.imshow("V", v)                # 显示HSV图像中V通道的图像
cv2.waitKey()
cv2.destroyAllWindows()
```

运行这段代码，会得到如下面所示的4个窗口。其中，图5是原图像，图6是H通道图像，图7是S通道图像，图8是V通道图像。

![](https://i-blog.csdnimg.cn/blog_migrate/01218872a1c9ffc13322a7f92c441248.png)

![](https://i-blog.csdnimg.cn/blog_migrate/68283fd8c965b722c54a625c6e14a206.png)

![](https://i-blog.csdnimg.cn/blog_migrate/b4423a6dd7096112dc5cce6d2b40bd8b.png)

![](https://i-blog.csdnimg.cn/blog_migrate/25410839e2faaba8c48c3cced7735a2b.png)

合并通道是拆分通道的逆过程。在前面的部分将BGR通道和HSV通道各拆分成3个通道，如果将这3个通道合并，会恢复原来的图像。合并通道的功能是通过merge函数实现的。

### 3. 合并B通道图像、G通道图像和R通道图像

merge函数用于按B、G、R顺序合并通道，如果按这个顺序传入通道图像，就可以得到原图像。merge函数的原型如下：

```
cv.merge([b, g,r])->dst
```

参数说明：

* b：B通道图像。

* g：G通道图像。

* r：R通道图像。

* dst：按B、G、R顺序合并通道后得到的图像。

下面的代码先拆分flower.jpg图像中的通道，然后分别按B、G、R和R、G、B的顺序合并通道，最后分别显示按不同顺序合并通道后的彩色图像。代码如下：

```
import cv2
rgb_image = cv2.imread("images/flower.jpg")
b, g, r = cv2.split(rgb_image)
# 按B、G、R顺序合并通道
bgr = cv2.merge([b, g, r])
cv2.imshow("BGR", bgr)
# 按R、G、B顺序合并通道
rgb = cv2.merge([r, g, b])
cv2.imshow("RGB", rgb)
cv2.waitKey()
cv2.destroyAllWindows()
```

运行这段代码，会得到如下面所示的2个窗口。其中，图9得到了原图像，而图10尽管是彩色图像，但与原图像有一些差异。

![](https://i-blog.csdnimg.cn/blog_migrate/01f6a22870fd1835b794dcfbc78631ef.png)

![](https://i-blog.csdnimg.cn/blog_migrate/e8fbf343fb51661da012771626de6018.png)

### 4. 合并H通道图像、S通道图像和V通道图像

当向merge函数传入H通道图像、S通道图像和V通道图像时，该函数就会将这3个通道合并成一个彩色图像。合并这3个通道的merge函数原型如下：

```
cv.merge([h, s,v])->dst
```

参数说明：

* h：H通道图像。

* s：S通道图像。

* v：V通道图像。

* dst：按H、S、V顺序合并通道后得到的图像。

下面的例子将flower.jpg从BGR色彩空间转换到HSV色彩空间，然后拆分得到HSV图像中的通道，接着合并拆分后的通道图像。最后分别显示原图像、HSV图像和合并后的HSV图像。代码如下：

```
import cv2

rgb_image = cv2.imread("images/flower.jpg")
# 显示原图像
cv2.imshow("flower", rgb_image)
# 将图像从BGR色彩空间转换到HSV色彩空间
hsv_image = cv2.cvtColor(rgb_image, cv2.COLOR_BGR2HSV)
# 显示HSV色彩空间中的图像
cv2.imshow("HSV1",hsv_image)
# 将HSV图像拆分成3个通道图像
h, s, v = cv2.split(hsv_image)
# 合并3个通道图像未HSV图像
hsv = cv2.merge([h, s, v])
# 显示合并后的HSV图像
cv2.imshow("HSV2", hsv)
cv2.waitKey()
cv2.destroyAllWindows()
```

运行这段代码，会得到如下面所示的3个窗口。其中，图11是原图像，图12和图13的效果一样，都是HSV色彩空间的图像。也就是说，一旦将图像从BGR色彩空间转换到HSV色彩空间，尽管也是彩色图像，不过与原图像有一定的差异，而且是无法还原的。

![](https://i-blog.csdnimg.cn/blog_migrate/e722224d0061a3a3ce65df4404995cd2.png)

![](https://i-blog.csdnimg.cn/blog_migrate/00dbfdeaca5d2626002ddc92ce4f1bf3.png)

![](https://i-blog.csdnimg.cn/blog_migrate/6cd89b17c137b6dc0c473ca8ce219bd0.png)

### 5. alpha通道

BGR色彩空间包含3个通道，即B通道、G通道和R通道。OpenCV在这3个通道的基础上，又增加了一个A通道，即alpha通道，用于设置图像的透明度。所以，一个新的BGRA色彩空间诞生了，这个色彩空间由4个通道组成，即B通道、G通道、R通道和A通道。alpha通道在[0, 255]内取值；其中，0表示透明，255表示不透明。

下面的例子将flower.png图像从RGB色彩空间转换到BGRA色彩空间；然后将图像拆分成B通道、G通道、R通道和A通道；接着将图像的透明度调整为150，合并拆分后的4个通道，按同样的方法，再将图像的透明度调整为0，合并拆分后的4个通道；接下来显示合并后的结果，最后保存合并后的结果。

```
import cv2

rgb_image = cv2.imread("images/flower.png")
# 将RGB色彩空间的图像转换为RGBA色彩空间的图像
rgba_image = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2RGBA)
# 显示RGBA色彩空间的原图像
cv2.imshow('RGBA', rgb_image)
# 将RGBA色彩空间的图像拆分成R通道、G通道、B通道和A通道
r, g, b, a = cv2.split(rgba_image)
# 将透明度修改为150
a[:, :] = 150
# 合并4个通道
rgba_150 = cv2.merge([r, g, b, a])
# 将透明度修改为0
a[:, :] = 0
# 合并4个通道
rgba_0 = cv2.merge([r, g, b, a])
# 显示透明度为150的图像
cv2.imshow('A = 150', rgba_150)
# 显示透明度为0的图像
cv2.imshow('A = 0', rgba_0)
# 保存原图像
cv2.imwrite('images/flower_image.png',rgba_image)
# 保存透明度为150的原图像
cv2.imwrite('images/flower_150.png', rgba_150)
# 保存透明度为0的图像
cv2.imwrite('images/flower_0.png', rgba_0)
cv2.waitKey()
cv2.destroyAllWindows()
```

运行程序，会看到如图14、图15和图16所示的效果。

![](https://i-blog.csdnimg.cn/blog_migrate/ec3664a62d11dae417fe266da2b4234d.png)

![](https://i-blog.csdnimg.cn/blog_migrate/e60e0b2e50fc6383753cbf0335dd3e1e.png)

![](https://i-blog.csdnimg.cn/blog_migrate/b431eed9cdad5ab5e224f272fb246f3d.png)

从图14、图15和图16看，这3个图的效果都一样，并未展现出任何透明的效果。这是由于imshow函数的显示机制不支持透明效果。为了看到透明的效果，读者可以直接Windows的资源管理器中打开这些图像文件，也可以使用像PS这样的图像处理软件打开这些图像文件。图17、图18和图19是使用PS查看这3张图的效果。

![](https://i-blog.csdnimg.cn/blog_migrate/b806b973025876f2aa96b60bff5d8bee.png)

![](https://i-blog.csdnimg.cn/blog_migrate/03c608fe964de86a843c61dcc0e61083.png)

![](https://i-blog.csdnimg.cn/blog_migrate/79c808747a5258cb96114335032fcc75.png)

我们可以看到，透明度为0的图像什么都没有，一片空白。图中的网格是PS显示的透明图效果。

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
  ![](htt...
---
title: 【计算机视觉】OpenCV 4高级编程与项目实战（Python版）【8】：图像像素统计
url: https://blog.csdn.net/nokiaguy/article/details/129505190
source: 一个被知识诅咒的人
date: 2023-03-14
fetch_date: 2025-10-04T09:28:40.940327
---

# 【计算机视觉】OpenCV 4高级编程与项目实战（Python版）【8】：图像像素统计

# 【计算机视觉】OpenCV 4高级编程与项目实战（Python版）【8】：图像像素统计

原创
已于 2023-03-14 07:17:47 修改
·
1k 阅读

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

[#OpenCV](https://so.csdn.net/so/search/s.do?q=OpenCV&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#Python](https://so.csdn.net/so/search/s.do?q=Python&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#像素](https://so.csdn.net/so/search/s.do?q=%E5%83%8F%E7%B4%A0&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

于 2023-03-13 20:27:10 首次发布

[![](https://i-blog.csdnimg.cn/blog_column_migrate/56256b7598fb005a8c32c420b606b60c.png?x-oss-process=image/resize,m_fixed,h_224,w_224)

OpenCV高级编程与项目实战（Python版）
专栏收录该内容](https://blog.csdn.net/nokiaguy/category_12162950.html "OpenCV高级编程与项目实战（Python版）")

9 篇文章

订阅专栏

![](https://i-operation.csdnimg.cn/images/a7311a21245d4888a669ca3155f1f4e5.png)本文介绍了OpenCV的minMaxLoc函数用于寻找图像像素的最大值和最小值，以及numpy的reshape函数调整图像尺寸。minMaxLoc函数适用于单通道图像，返回图像中的最值及位置。reshape函数可以改变矩阵的维度，当一个维度设为-1时，会自动计算该值。文章通过示例展示了这两个函数的使用方法。

图像通过一定尺寸的矩阵表示，矩阵中每个元素的大小表示图像中每个像素的明暗程度。查找矩阵中的最大值就是寻找图像中灰度值最大的像素，计算矩阵的平均值就是计算图像像素的平均灰度，可以用平均灰度表示图像整体的亮暗程度。因此，针对图像矩阵数据的统计和分析，在图像处理工作中具有非常重要的意义。OpenCV集成了求取图像像素最大值、最小值、均值、标准差等函数，本节将详细介绍这些函数的使用方法。

OpenCV提供了用于寻找图像像素的最大值、最小值的minMaxLoc函数，该函数的原型如下：

```
cv.minMaxLoc( src[, mask])-> minVal, maxVal, minLoc, maxLoc
```

参数说明：

* src：需要寻找最大值和最小值的图像，必须是表示图像的单通道数组。

* mask：可选参数，图像掩模。

* minVal：返回值，图像中的最小值。

* maxVal：返回值，图像中的最大值。

* minLoc：返回值，图像中的最小值在矩阵中的坐标。

* maxLoc：返回值，图像中的最大值的矩阵中的坐标。

minMaxLoc函数实现的功能是寻找图像中指定区域内的最值，并将寻找到的最值以及相关的数据通过该函数返回。但要注意的是，src参数必须是表示单通道图像的矩阵。如果是多通道图像，需要使用np.reshape函数将其转换为单通道图像，或者分别寻找每个通道的最值，然后寻找指定区域内的最值。第2个参数mask用于在图像的指定区域内寻找最值，默认值是None，表示寻找范围是图像中的所有数据。

注意：如果图像中存在多个最大像素值或最小像素值，那么minMaxLoc函数会输出按行扫描从左到右第1次检测到最值的位置。

在对图像进行操作的过程中，往往需要对图像尺寸和通道数进行调整，NumPy为我们提供了reshape函数可以实现这一功能，reshape函数的原型如下：

```
np.reshape(array, shape[,order]) -> dst
```

参数说明：

* array：需要调整尺寸和通道数的图像矩阵。

* shape：调整后的矩阵的维度。

* order：读取/写入元素时的顺序。

reshape函数可以对图像的尺寸和通道数进行调整，并将调整后的结果通过值返回。第2个参数shape是调整后矩阵的维度，要以元组形式传入，例如，(3,4)表示将矩阵调整为3行4列，当我们不知道矩阵中元素的具体个数时，也可以将其中一个维度设为-1，此时reshape函数会根据元素的个数自动计算这个维度。第3个参数order表示写入元素时的顺序，‘C’表示按C顺序读取/写入元素；‘F’表示按FORTRAN顺序读取/写入元素；‘A’表示如果该矩阵在内存中连续，则按照FORTRAN顺序读取/写入元素，否则，按C顺序写入元素；默认值是‘C’。

注意：在使用第2个参数（shape）时，应该保证shape指定的所有维度的乘积与array指定的数组的所有温度的乘积相同。例如，array指定数组的维度是(3,8)，那么shape指定的维度可以是(2,12)，(4,6)、(3,4,2)等，但不能指定像(2,6)、(3,6)这样的维度。因为array数组维度的乘积是24，而(2,6)的维度乘积是12，(3,6)的维度乘积是18。如果指定了错误的shape参数值，可能会出现错误和矩阵内元素丢失的情况。对于较大的矩阵，若不能预先计算出矩阵元素的个数，可以某个维度指定为-1，如(2, -1)、(-1, 6)等。但只能有1个维度指定为-1，如果有超过一个维度指定为-1，仍然会会抛出异常。即使某一个维度指定为-1，其他维度的乘积也要可以被array数组所有维度的乘积整除，否则仍然会抛出异常。例如，前面的例子，如果设置shape参数值为（5, 2, -1），尽管最后一个维度为-1，但由于array数组维度的乘积为24，而24/（5×2）并不是整数，也就是说，reshape函数是无法算最后一个维度的，因此，指定这样的shape参数值也会抛出异常。

下面的例子使用reshape函数将一维数组（长度为12）转换为二维（3×4）数组和三维（3×2×2）数组，并将其中一个维度的值设置为-1，让reshape函数自动计算该维度，最后使用minMaxLoc函数分别计算这些转换后的数组中的最大值和最小值。

```
import cv2 as cv
import numpy as np

# 新建矩阵array
array = np.array([1, 2, 3, 4, 5, 10, 6, 7, 8, 9, 10, 0])
# 将array调整为3*4的数组
img1 = array.reshape((3, 4))
minval_1, maxval_1, minloc_1, maxloc_1 = cv.minMaxLoc(img1)
print('数组img1中最小值为：{}, 其位置为：{}' .format(minval_1, minloc_1))
print('数组img1中最大值为：{}, 其位置为：{}' .format(maxval_1, maxloc_1))

# 先将array调整为3*2*2的数组
img2 = array.reshape((3, 2, 2))
# 再利用-1的方法调整尺寸
img2_re = img2.reshape((1, -1))
minval_2, maxval_2, minloc_2, maxloc_2 = cv.minMaxLoc(img2_re)
print('数组img2中最小值为：{}, 其位置为：{}'.format(minval_2, minloc_2))
print('数组img2中最大值为：{}, 其位置为：{}'.format(maxval_2, maxloc_2))
```

运行这段程序，会输出如下内容：

```
    数组img1中最小值为：0.0, 其位置为：(3, 2)
    数组img1中最大值为：10.0, 其位置为：(1, 1)
    数组img2中最小值为：0.0, 其位置为：(11, 0)
    数组img2中最大值为：10.0, 其位置为：(5, 0)
```

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

  1

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
3135

[《奇妙的Python——神奇代码漫游之旅》是一本面向实际应用的Python编程指南，涵盖文件操作、GUI设计、多媒体处理、自动化办公、加密解密等多个领域。由华为HDE专家李宁编写，通过丰富的实战案例，帮助读者在工作和项目中高效应用Python，提升编程技能。无论是新手还是有经验的开发者，这本书都将带你深入探索Python的无限可能，开启一段充满创意与实用性的编程之旅。](https://unitymarvel.blog.csdn.net/article/details/141889588)

![](https://csdnimg.cn/release/blogv2/dist/components/img/blogType.png)
博客
[2025机器人产业大洗牌：新兴初创企业的技术革命与崛起之路](https://unitymarvel.blog.csdn.net/article/details/151067555)

09-01
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
1041

[摘要：2025年机器人产业正经历技术驱动的深度变革，AI初创企业通过创新算法和低成本方案挑战传统巨头。本文剖析产业洗牌动因，包括AI融合、融资热潮和应用场景扩展，重点解析人形机器人等关键技术。通过ROS控制、A\*路径规划和PyTorch视觉识别等代码示例（附中文注释），展示初创企业的技术优势。文章预测Figure AI、Unitree等公司将引领消费级机器人市场，推动社会进入智能协作新时代。（150字）](https://unitymarvel.blog.csdn.net/article/details/151067555)

![](https://csdnimg.cn/release/blogv2/dist/components/img/blogType.png)
博客
[Java应用容器化革命：Dock...
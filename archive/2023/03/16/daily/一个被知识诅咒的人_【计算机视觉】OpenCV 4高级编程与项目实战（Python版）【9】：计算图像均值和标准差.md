---
title: 【计算机视觉】OpenCV 4高级编程与项目实战（Python版）【9】：计算图像均值和标准差
url: https://blog.csdn.net/nokiaguy/article/details/129568725
source: 一个被知识诅咒的人
date: 2023-03-16
fetch_date: 2025-10-04T09:43:07.508816
---

# 【计算机视觉】OpenCV 4高级编程与项目实战（Python版）【9】：计算图像均值和标准差

# 【计算机视觉】OpenCV 4高级编程与项目实战（Python版）【9】：计算图像均值和标准差

![](https://i-operation.csdnimg.cn/images/cf31225e169b4512917b2e77694eb0a2.png)OpenCV图像处理：计算均值与标准差

![](https://csdnimg.cn/release/blogv2/dist/pc/img/original.png)

[蒙娜丽宁](https://unitymarvel.blog.csdn.net "蒙娜丽宁")
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCurrentTime2.png)
于 2023-03-15 21:10:02 发布

![](https://csdnimg.cn/release/blogv2/dist/pc/img/articleReadEyes2.png)
阅读量1.6k
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)
收藏

1

![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)
点赞数

CC 4.0 BY-SA版权

分类专栏：
[OpenCV高级编程与项目实战（Python版）](https://blog.csdn.net/nokiaguy/category_12162950.html)
文章标签：
[python](https://so.csdn.net/so/search/s.do?q=python&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[opencv](https://so.csdn.net/so/search/s.do?q=opencv&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[计算机视觉](https://so.csdn.net/so/search/s.do?q=%E8%AE%A1%E7%AE%97%E6%9C%BA%E8%A7%86%E8%A7%89&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

本文链接：<https://blog.csdn.net/nokiaguy/article/details/129568725>

[![](https://i-blog.csdnimg.cn/blog_column_migrate/56256b7598fb005a8c32c420b606b60c.png?x-oss-process=image/resize,m_fixed,h_224,w_224)

OpenCV高级编程与项目实战（Python版）
专栏收录该内容](https://blog.csdn.net/nokiaguy/category_12162950.html "OpenCV高级编程与项目实战（Python版）")

9 篇文章

订阅专栏

![](https://i-operation.csdnimg.cn/images/a7311a21245d4888a669ca3155f1f4e5.png)本文介绍了OpenCV中用于计算图像均值和标准差的mean及meanStdDev函数，包括它们的参数、工作原理和使用示例。均值反映图像亮度，标准差指示明暗变化。通过这两个函数，可以分析图像的亮度分布和对比度。

图像的均值表示图像整体的亮暗程度，图像的均值越大，图像整体越亮。标准差表示图像中明暗变化的程度，标准差越大，表示图像中明暗变化越明显。

OpenCV提供了mean函数用于计算图像的均值，提供了meanStdDev函数用于同时计算图像的均值和标准差。

mean函数的原型如下：

```
mean(src[, mask]) ->   retval
```

参数说明：

* src：待求均值的图像的矩阵。可以是1 ~ 4通道的图像（1 ~ 4维的矩阵）。

* mask：可选参数，图像掩模。尺寸与src参数相同，用于标记求哪些区域的均值。

* retval：返回值，长度为4的元组。每一个元组元素表示对应通道的均值，如果没有该通道，则对应的值为0.0。

计算均值的原理如图1所示。

![](https://i-blog.csdnimg.cn/blog_migrate/cb54b5c11fff632eeeeb29b39fef5613.png)

I表示输入的图像的矩阵；mask表示掩模矩阵；mask(I)表示掩模矩阵中的某个值；N表示图像矩阵元素的个数；Mc表示第C通道的均值；src(I)c表示第C个通道中像素的灰度值。

meanStdDev函数的原型如下：

```
meanStdDev(src[,mean[,stddev[,mask]]])->mean, stddev
```

参数说明：

* src：待求均值和标准差的图像的矩阵。

* mean：可选参数，图像每个通道的均值。

* stddev：可选参数，图像每个通道的标准差。

* mask：可选参数，图像掩模。

* mean：返回值，计算得出的图像的均值。

* stddev：返回值，计算得出的图像的标准差。

meanStdDev函数可以同时计算图像的均值和标准差，并将计算结果返回。第1个参数（src）和第4个参数（mask）与mean函数中同名参数的含义与用法相同。如果不指定第4个参数的值，表示计算矩阵内所有区域的均值和标准差。meanStdDev函数返回的均值和标准差中的值，会根据输入图像的通道数不同而不同，例如，如果输入的图像只有一个通道，则该函数计算得到的均值和标准差也只有一个值。第2个参数（mean）和第3个参数（stddev）是可选的，如果不指定这两个参数，均值和标准差会通过meanStdDev函数的返回值返回，如果指定这两个参数，那么均值和标准差会通过这两个参数返回。

meanStdDev计算均值的公式与图1所示的计算公式完全相同，计算标准差的公式如图2所示。这个公式中相关参数的含义与图1所示的计算均值的公式中同名的参数的含义和用法完全相同。

![](https://i-blog.csdnimg.cn/blog_migrate/6434e3b40c3da705bbf7d27e28fa44b1.png)

下面的代码使用reshape函数将一维数组（长度为12）转换为3×4的单通道图像和3×2×2的多通道图像，然后使用mean函数计算这两个图像的均值，使用meanStdDev函数计算这两个图像的均值和标准差，最后输出计算结果。

```
import cv2
import numpy as np

# 新建矩阵array
array = np.array([1, 2, 3, 4, 5, 10, 6, 7, 8, 9, 10, 0])
# 将array调整为3*4的单通道图像img1
img1 = array.reshape((3, 4))
# 将array调整为3*2*2的多通道图像img2
img2 = array.reshape((3, 2, 2))

# 计算img1的均值
mean_img1 = cv2.mean(img1)
# 计算img2的均值
mean_img2 = cv2.mean(img2)
# 计算img1的均值和标准差
mean_std_dev_img1 = cv2.meanStdDev(img1)
# 计算img2的均值和标准差
mean_std_dev_img2 = cv2.meanStdDev(img2)

print('mean函数计算结果如下：')
print(f'图像img1的均值为：{mean_img1}')
print(f'图像img2的均值为：{mean_img2}\n第一个通道的均值为：{mean_img2[0]}\n第二个通道的均值为：{mean_img2[1]}')
print('*' * 30)
print('meanStdDev函数计算结果如下：')
print(f'图像img1的均值为：{mean_img1[0]}\n标准差为：{mean_std_dev_img1[1]}')
print(f'图像img2的均值为：{mean_img2}\n第一个通道的均值为：{mean_img2[0]}\n'
      f'第二个通道的均值为：{mean_img2[1]}\n'
      f'均值为：{mean_std_dev_img2[0]}\n'
      f'标准差为：{mean_std_dev_img2[1]}\n'
      f'第一个通道的标准差为：{float(mean_std_dev_img2[1][0])}\n'
      f'第二个通道的标准差为：{float(mean_std_dev_img2[1][0])}\n')
```

执行这段代码，会输出如下内容：

```
mean函数计算结果如下：
图像img1的均值为：(5.416666666666666, 0.0, 0.0, 0.0)
图像img2的均值为：(5.5, 5.333333333333333, 0.0, 0.0)
第一个通道的均值为：5.5
第二个通道的均值为：5.333333333333333
******************************
meanStdDev函数计算结果如下：
图像img1的均值为：5.416666666666666
标准差为：[[3.32812092]]
图像img2的均值为：(5.5, 5.333333333333333, 0.0, 0.0)
第一个通道的均值为：5.5
第二个通道的均值为：5.333333333333333
均值为：[[5.5       ]
 [5.33333333]]
标准差为：[[2.98607881]
 [3.63623737]]
第一个通道的标准差为：2.9860788111948193
第二个通道的标准差为：2.9860788111948193
```

从输出结果可以看出，meanStdDev函数通过元组返回了图像的均值和标准差，元组的第1个元素是均值，第2个元素是标准差。也可以将meanStdDev函数的返回值赋给2个变量，这样可以直接将均值和标准差分别赋给这2个变量，代码如下：

```
# 计算img1的均值和标准差
mean1, std_dev_img1 = cv2.meanStdDev(img1)
# 计算img2的均值和标准差
mean2, std_dev_img2 = cv2.meanStdDev(img2)
print('mean1:',mean1)
print('std_dev_img1:', std_dev_img1)
print('mean2:',mean2)
print('std_dev_img2:', std_dev_img2)
```

执行这段代码，会输出下面的内容：

```
mean1: [[5.41666667]]
std_dev_img1: [[3.32812092]]
mean2: [[5.5       ]
 [5.33333333]]
std_dev_img2: [[2.98607881]
 [3.63623737]]
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

![](ht...
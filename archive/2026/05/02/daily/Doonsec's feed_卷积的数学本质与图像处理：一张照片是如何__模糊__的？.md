---
title: 卷积的数学本质与图像处理：一张照片是如何\"模糊\"的？
url: https://mp.weixin.qq.com/s/-POErJMHA2hhXdBsi3tigQ
source: Doonsec's feed
date: 2026-05-02
fetch_date: 2026-05-03T05:25:23.760426
---

# 卷积的数学本质与图像处理：一张照片是如何\"模糊\"的？

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hyaRUFucbbqz23jvMialTBhMuGtyQMqpqF4J9W3FIySSoA7m1f68X02cT1U9eQloKnWfouOKNBX03CKjrcetibcjA3jYctORXSOsTq5JCF9qM/0?wx_fmt=jpeg)

# 卷积的数学本质与图像处理：一张照片是如何"模糊"的？

原创

代码小铺
代码小铺

代码小铺

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

你手机里的修图App，点一下"磨皮"，皮肤瞬间柔滑；点一下"锐化"，细节又清晰锐利。你点的是按钮，但背后真正干活的，是一个叫**卷积**的数学运算。

今天我们就来聊聊，这个看似神秘的卷积到底是什么，以及它是如何操纵你手机里每一张照片的。

## 卷积到底是什么？

先别被名字吓到。卷积的直觉其实非常朴素——**它就是一个"滑动窗口"在数据上做加权平均**。

想象你拿着一块小玻璃板（比如 3×3 的方格），在一张大图片上从左到右、从上到下慢慢滑动。每次停下，玻璃板盖住的 9 个像素各自乘上一个权重，然后加起来——这个结果就是输出图片上对应位置的新像素值。

这个"玻璃板"就叫**卷积核（kernel）**，也叫**滤波器（filter）**。不同的卷积核，会产生完全不同的效果。

## 数学定义：卷积的公式长什么样？

在二维离散的情况下（也就是图像处理中），卷积的公式是这样的：

![](https://mmbiz.qpic.cn/mmbiz_png/hyaRUFucbbqGZA3GD6hVZuFKDnsoK5zAohu3pEUvevv8evmEWUw9o64cY0afeAUhyV7iazwGvicP0pX1zH7yaia3MZwuFCYg4Yx0nparIJ6NEU/640?from=appmsg)

看起来有点吓人？让我翻译一下：

* • *f(x, y)* 是原始图片在位置 *(x, y)* 处的像素值
* • *g(i, j)* 是卷积核在位置 *(i, j)* 处的权重
* • *k* 是卷积核的半径（比如 3×3 的核，*k = 1*）
* • 公式的意思就是：**把卷积核覆盖区域的每个像素值乘以对应的权重，然后全部加起来**

这就是卷积的全部秘密。它本质上就是一个**局部的加权求和**，只不过这个加权求和在整张图上滑动着做了一遍。

## 几个经典的卷积核

理解了原理，我们来看几个实际的卷积核长什么样。

### 1. 均值模糊（Mean Blur）

最简单的模糊操作——把每个像素替换成周围像素的平均值：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hyaRUFucbbrZ3JEO2sZCMq56mlCpKbAicibd1iclkFTOKibStNFmSnpZ1JK5fVJGu3zRibceHQeK1oBPbcy0s1GX5WvN6f0CLmt7nWkOdLoVt0Gs/640?from=appmsg)

每个位置权重都是 1/9，相当于把 3×3 区域内 9 个像素值加起来除以 9。远处的像素被"平均"了，图像就变模糊了。

### 2. 高斯模糊（Gaussian Blur）

比均值模糊更自然——离中心越近的像素权重越大，像一个"小山包"：

![](https://mmbiz.qpic.cn/mmbiz_png/hyaRUFucbbqG8Pyj6uRD4M5J7N2t6aWql0W7MSM9BHcrWicmnGrWOhDLG00FgEP7ZLgfDZMRt8V2zzsYeZjwtyT45FjfQ5OJYkzlNzx6cwq0/640?from=appmsg)

中心的权重最大（4/16），四周逐渐减小。这样模糊出来的效果更柔和，不会像均值模糊那样"死板"。

### 3. 边缘检测（Sobel 算子）

卷积不仅能模糊，还能**检测边缘**！Sobel 算子可以找出图像中像素值变化剧烈的地方——那通常就是物体的轮廓：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hyaRUFucbbrtm4Qrg2S7j7B6ia1IhrNM5n4QibpqTsuQuibwYkDOIiciaNtQDlzOCVlyqzaGLqpAZdqyUSciaj4hrpMSSFbdKSEwFcyRWnfmyMyd4/640?from=appmsg)

这个核在水平方向上做差分运算，能检测出**垂直方向**的边缘。类似地，还有一个 ![](https://mmbiz.qpic.cn/sz_mmbiz_png/hyaRUFucbbqb9xIXxFshRmYqM6veueEFy52Gictcz2OWaHP7Q4qXicXNkTZ49TXc3mC6kd8icAwWMSYW5VQl9TPDB38a67UqfAsf1VdZGqdRHY/640?from=appmsg) 用来检测水平边缘。

## 卷积在深度学习中的角色

你可能听说过卷积神经网络（CNN）——深度学习在图像领域大杀四方的核心武器。

CNN 的核心思想很简单：**让模型自己学习最好的卷积核，而不是人工设计**。

在传统的图像处理中，我们需要手动设计卷积核（比如上面的 Sobel、高斯核）。而在 CNN 中，卷积核的权重是**通过训练自动学习**的——模型会在海量的图像数据中，自己摸索出哪些"滑动窗口"最有用。

卷积操作在 CNN 中的前向传播公式：

![](https://mmbiz.qpic.cn/mmbiz_png/hyaRUFucbbpCyclFsUZmS6PGu1SMcQpUrfP5IF9BOpq2x7wfYdblyumUSicmKibVAVo0uYscNsA0z1oM7Viabgxia2OOIFeuk3ovrsNVuhCBOo8/640?from=appmsg)

这里多了几个维度：

* • *c* 和 *c'* 是输入和输出的通道数（比如 RGB 三个通道）
* • *W* 是学习得到的卷积核权重
* • ![](https://mmbiz.qpic.cn/mmbiz_png/hyaRUFucbbofCGwgB5mhe3xDWicjgxfuNNwJ3oqQVopRZhemxLKMNyNHKZqNmakHlDOnwibqEemQ2srwxx0J2JwBX9hRclrBibORiaSJVjtlqzQ/640?from=appmsg) 是激活函数（如 ReLU）
* • *b* 是偏置项

本质上，它还是我们前面说的"滑动窗口加权求和"，只不过窗口更大、维度更多、权重是学出来的。

## 生活中的卷积无处不在

你可能没意识到，卷积早就融入了你的日常生活：

* • **手机拍照的夜景模式**——通过卷积核降噪，让暗光照片更干净
* • **人脸识别的门禁**——CNN 用卷积核提取面部特征，再和数据库比对
* • **自动驾驶的障碍物检测**——卷积网络实时分析摄像头画面，识别行人和车辆
* • **医疗影像分析**——卷积帮助医生从 CT、MRI 图像中发现病灶
* • **Photoshop 的滤镜**——本质上就是一堆预定义的卷积核

## 总结

卷积，归根结底就是一个**加权滑动求和**的运算。它不神秘，却极其强大——从给照片加滤镜，到让自动驾驶汽车看懂世界，都离不开这个简洁的数学操作。

下次你给照片加"磨皮"效果时，不妨想一想：你的手机正拿着一块小小的卷积核，在像素的海洋里一寸一寸地滑动，用加法与乘法，悄悄改变了整张照片的面貌。

数学之美，就在你指尖。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/XrMnA4yTvjvhoROhAP2xiak56A4IOMjIEIrN56l3cn3vHZXxxfusUjIdhWfLXeSyx73b3DjgT6mdVdVkNPklxug/0?wx_fmt=png)

代码小铺

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/XrMnA4yTvjvhoROhAP2xiak56A4IOMjIEIrN56l3cn3vHZXxxfusUjIdhWfLXeSyx73b3DjgT6mdVdVkNPklxug/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过
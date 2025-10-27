---
title: [译] 以图像识别为例，关于卷积神经网络（CNN）的直观解释（2016）
url: https://arthurchiao.github.io/blog/cnn-intuitive-explanation-zh/
source: ArthurChiao's Blog
date: 2023-06-12
fetch_date: 2025-10-04T11:45:06.038951
---

# [译] 以图像识别为例，关于卷积神经网络（CNN）的直观解释（2016）

# [ArthurChiao's Blog](https://arthurchiao.github.io/)

* [Home](/index.html)
* [Articles (EN)](/articles)
* [Articles (中文)](/articles-zh)
* [Categories](/categories)
* [About](/about)
* [Donate](/donate)

# [译] 以图像识别为例，关于卷积神经网络（CNN）的直观解释（2016）

Published at 2023-06-11 | Last Update 2023-06-11

### 译者序

本文翻译自 2016 年的一篇文章：
[An Intuitive Explanation of Convolutional Neural Networks](https://ujjwalkarn.me/2016/08/11/intuitive-explanation-convnets/)。

作者以图像识别为例，用图文而非数学公式的方式解释了卷积神经网络的工作原理，
适合初学者和外行扫盲。

**译者水平有限，不免存在遗漏或错误之处。如有疑问，敬请查阅原文。**

以下是译文。

---

* [译者序](#译者序)
* [1 卷积神经网络（CNN）](#1-卷积神经网络cnn)
  + [1.1 应用场景](#11-应用场景)
  + [1.2 起源：LeNet, 1990s](#12-起源lenet-1990s)
  + [1.3 现代架构](#13-现代架构)
* [2 CNN：直观解释](#2-cnn直观解释)
  + [2.1 输入：图像（像素值组成的矩阵）](#21-输入图像像素值组成的矩阵)
  + [2.2 第一步：卷积运算](#22-第一步卷积运算)
    - [2.2.2 动图直观解释](#222-动图直观解释)
    - [2.2.2 特征图/卷积特征参数](#222-特征图卷积特征参数)
  + [2.3 第二步：非线性（Non Linearity / ReLU）运算](#23-第二步非线性non-linearity--relu运算)
  + [2.4 第三步：降采样](#24-第三步降采样)
    - [2.4.1 原理：直观解释](#241-原理直观解释)
    - [2.4.2 小结：卷积层 + ReLU + 降采样层](#242-小结卷积层--relu--降采样层)
  + [2.5 第四步：全连接层：基于特征分类](#25-第四步全连接层基于特征分类)
  + [2.6 第五步：反向传播：形成闭环](#26-第五步反向传播形成闭环)
* [3 CNN 完整架构和工作流](#3-cnn-完整架构和工作流)
* [4 案例：CNN 学习识别字符 `8`](#4-案例cnn-学习识别字符-8)
  + [4.1 多层特征](#41-多层特征)
  + [4.2 学习字符 `8`](#42-学习字符-8)
* [5 其他 CNN 架构](#5其他-cnn-架构)
* [6 总结](#6-总结)
* [参考资料](#参考资料)

---

# 1 卷积神经网络（CNN）

## 1.1 应用场景

卷积神经网络（ConvNets 或 CNN）是**一类**神经网络（a category of
[Neural Networks](%22https%3A//ujjwalkarn.me/2016/08/09/quick-intro-neural-networks/)），
在图像识别和分类等领域已经证明非常有效。CNN 已经成功用于
人脸识别、物体和交通标志识别，机器人视觉，自动驾驶等等。下面看两个具体例子。

图 1 是给一个图片，自动识别其中的内容并生成一句描述，

![](/assets/img/cnn-intuitive-explanation/1.png)

图 1：图像识别和自动生成描述。[cs.stanford.edu](http://cs.stanford.edu/people/karpathy/neuraltalk2/demo.html)

图 2 则是 CNN 用于识别日常人和物，

![](/assets/img/cnn-intuitive-explanation/2.png)

图 2：图像识别。来自 [paper pdf](https://arxiv.org/pdf/1506.01497v3.pdf)

此外，CNN 在一些自然语言处理任务（如句子分类）中也展现出很不错的效果。
因此，CNN 在机器学习领域将是一个非常重要的工具。不过，新手学习起来经常比较受挫。
本文试图拿 **CNN for image processing** 为例，向大家直观解释一下 CNN 是如何工作的。

> * 想了解 neural networks 可戳  [this short tutorial on Multi Layer Perceptrons](https://ujjwalkarn.me/2016/08/09/quick-intro-neural-networks/)，不了解也没关系。
> * Multi Layer Perceptrons（多层感知器/多层感知机）在本文中将称为 “Fully Connected Layers”。

## 1.2 起源：LeNet, 1990s

LeNet 由 Yann LeCun 在 1988 提出，是最早推动深度学习领域发展的卷积神经网络之一。
后来经过多次改进，直到 [LeNet5](http://yann.lecun.com/exdb/publis/pdf/lecun-01a.pdf) [3]。
当时 LeNet 架构主要用于**字符识别**，
例如读取邮政编码、数字等。

## 1.3 现代架构

近年来提出了几种新的架构，都是**对 LeNet 的改进**，它们都继承了 LeNet 的主要概念。
因此如果对 LeNet 比较了解，理解现代架构将容易很多。
下图展示了这类架构是**如何学习识别图像**的：

![](/assets/img/cnn-intuitive-explanation/3.png)

图 3：基于卷积神经网络识别图像。[image credit](https://www.clarifai.com/technology)

* 图中的卷积神经网络在架构上与早期 LeNet 差不多，它对输入图像进行分类（LeNet 主要用于字符识别）；
* 这个例子中会分成四类：dog, cat, boat, bird，所有概率的总和是 100%（后文会解释）；
* 从图中可以明显看出，在 boat 图像作为输入时，该网络最终的分类结果中，boat 的概率最高（0.94）。

根据上图，我们可以看到**现代 CNN 主要有四种操作**：

1. 卷积（Convolution）
2. 非线性（Non Linearity，ReLU)）
3. 池化或降采样（Pooling or Sub Sampling）
4. 分类/全连接层（Classification, Fully Connected Layer）

这几个功能是所有卷积神经网络的基本模块。下面我们尝试从直观上来理解每个操作的含义。

# 2 CNN：直观解释

## 2.1 输入：图像（像素值组成的矩阵）

每个图像（image）本质上就是一个由**像素值**（pixel values）组成的矩阵：

![](/assets/img/cnn-intuitive-explanation/8-gif.webp)

图 4：每个图像都是一个像素值组成的矩阵。[6]

[Channel](https://en.wikipedia.org/wiki/Channel_%28digital_image%29)（通道）是一个传统术语，指图像的某一部分数据。
例如，

* 数码相机拍出的图像通常有三个通道 —— red/green/blue —— 可以想象成从下往上依次**堆叠的 3 个二维矩阵**（每种颜色一个），每个像素值都在 0 到 255 范围内。
* [grayscale](https://en.wikipedia.org/wiki/Grayscale)（灰度）图像只有一个通道。

简单起见，本文将只考虑**灰度图像**。
这意味着我们将有一个表示图像的二维矩阵，其中中每个像素的值范围从 0 到 255 —— 0 表示黑色，255 表示白色。

## 2.2 第一步：卷积运算

CNN（卷积神经网络）的名字来源于[“卷积”](http://en.wikipedia.org/wiki/Convolution)运算，

* 卷积的**主要目的**是**从输入图像中提取特征**；
* 通过一个**小矩阵**（称为 filter）对输入矩阵进行运算，来学习图像特征（image features）；
* filter 保留了像素之间的**空间关系**（spatial relationship between pixels）。

这里不深入探讨卷积的数学细节，只尝试了解它如何处理图像。

### 2.2.2 动图直观解释

每个图像都是像素值组成的矩阵。考虑一个 5x5 的图像，其像素值只有 0 和 1（灰度图像的像素值范围为 0 到 255，这里我们进一步简化，像素值只有 0 和 1）：

![](/assets/img/cnn-intuitive-explanation/binary-image.png)

然后引入一个 3x3 矩阵作为 filter，

![](/assets/img/cnn-intuitive-explanation/3x3-matrix.png)

那么，用 5x5 和 3x3 矩阵来计算卷积的过程就如下面的动图所示，

![](/assets/img/cnn-intuitive-explanation/convolution_schematic.webp)

图 5：卷积的计算。计算得到的结果矩阵称为 Convolved Feature or Feature Map（卷积特征，或特征图）。[7]

计算过程：

1. 在 5x5 的输入矩阵上，覆盖一个 3x3 矩阵，
2. 对当前 3x3 覆盖的部分，分别与 3x3 矩阵按像素相乘，然后把 9 个值加起来得到一个整数，
3. 按这种方式，以一个像素为单位依次滑动和计算，最后就得到一个输出矩阵（右边）。

用 CNN 术语来说，

1. 3x3 矩阵叫做 **filter（滤波器），或 kernel、feature detector 等**；
2. 滑动的粒度（这里是一个像素）叫做 **stride（步长）**；
3. 最后得到的矩阵叫 Convolved Feature（**卷积特征**）或 feature map（**特征图**）；

显然，对于同一个图像，**用的卷积矩阵（filter matrix）不同，得到的特征图（feature maps）也就不同**。
或者说**不同的 filter 可以检测不同的特征**。例如对于下面这张图片，

![](/assets/img/cnn-intuitive-explanation/animal.png)

我们可以根据目的（边缘检测、锐化、模糊化等）的不同，选用不同的 filter，得到的效果如下 [8]，

![](/assets/img/cnn-intuitive-explanation/animal-filter-results.png)

下面是另一个例子，用动图展示两个不同的 filter 计算卷积得到的 feature map，

![](https://ujwlkarn.files.wordpress.com/2016/08/giphy.gif?w=480&zoom=2)

图 6：卷积运算。Source [[9](http://cs.nyu.edu/~fergus/tutorials/deep_learning_cvpr12/)]

> 这里需要再提醒一下，image 和 filter 都只是一个数值矩阵（numeric matrix）。

### 2.2.2 特征图/卷积特征参数

实际上，CNN 在训练过程中自行**学习**（learn）这些 filter 的值
（尽管我们仍然需要在训练时指定某些参数，例如过 filter 数量、filter size、网络架构等）。
filter 数量越多，提取的图像特征就越多，训练出来的网络在识别未见过的图像时效果就越好。

Feature Map（Convolved Feature）的大小由三个参数 [4] 控制，在训练之前确定：

1. **深度**（depth）：将要用来做卷积运算的 **filter 数量**。

   在下图所示的网络中，我们使用三个不同的 filter 对原始图像执行卷积，从而生成三个不同的特征图。
   可以将这三个特征图视为三个自下向上**堆叠（stacking）在一起**的二维矩阵，
   这也是为什么成它为特征图的**“深度”**。

   ![](/assets/img/cnn-intuitive-explanation/convolution-operation.png)

   图 7：特征图的深度
2. **步长**（stride）：在输入矩阵上滑动滤波器（filter）矩阵的**像素数**。

   * 步长为 1 就是一次将 filter 移动一个像素，步长为 2 就是一次滑动 2 个像素。
   * **步长越大，得到的特征图越小**。
3. **零值填充**（Zero-padding）：有时需要在图像边界用零填充，这样就可以对输入图像的边界像素应用 filter。

   * zero-padding 会使生成的特征图稍大一些；
   * 使用了 zero-padding 称为 **wide convolution**，不使用的称为 **narrow convolution** [14]。

## 2.3 第二步：非线性（Non Linearity / ReLU）运算

每次卷积运算之后，还会跟着一个称为 ReLU（**Rectified Linear Unit**，修正线性单元）的运算。
这是一个**非线性运算**，输入输出公式为，

![](/assets/img/cnn-intuitive-explanation/ReLU.png)

图 8：ReLU 公式与效果（负值置为零）

ReLU 是一个**像素级别的操作**，**将特征图中所有负值置为零**。
ReLU 的目的是在 CNN 中引入非线性，因为真实世界中的大部分数据都是非线性的，
我们希望 CNN 能与现实更加匹配。

> 卷积是一种线性运算 —— 逐像素做矩阵乘法和加法，因此我们通过引入像 ReLU 这样的非线性函数来解释（account for）非线性。

下图可以清楚地看到 ReLU 操作之后的效果，

![](/assets/img/cnn-intuitive-explanation/ReLU-result.png)

图 9：真实特征图执行 ReLU 操作之后的效果。Source [[10](http://mlss.tuebingen.mpg.de/2015/slides/fergus/Fergus_1.pdf)]

* 左边的特征图是卷积运算之后得到的；
* 右边是接着做了 ReLU 运算（负数全部置零）之后的效果。也称为**“修正之后的”特征图**。

除了 ReLU，还可以使用 `tanh` 或 `sigmoid` 等**非线性函数**，不过在大部分场景下，ReLU 的性能都更好。

## 2.4 第三步：降采样

Spatial Pooling，又称为**降采样、下采样**（subsampling、downsampling），

* 目的是在降低 feature map 维度的同时，保留尽量多的重要信息。
* 有不同的类型：**`Max/Average/Sum`** 等。

### 2.4.1 原理：直观解释

图 10 是对一个卷积 + ReLU 之后得到的特征图执行 **2x2 降采样**，

![](/assets/img/cnn-intuitive-explanation/down-sampling.png)

图 10: Max Pooling. Source [[4](http://cs231n.github.io/convolutional-networks/)]

* 首先定义一个 spatial neighborhood (2x2 窗口)，
* 然后执行降采样函数，这里用的是 `Max` 函数，也就是取其中最大的那个值作为结果，
* 注意这里滑动窗口的步长是 2，也就是降采样矩阵的尺寸；

最终**把 4x4 特征图降维到了 2x2**。

下图是对三个卷积结果（rectified feature map）依次执行降采样，

![](/assets/img/cnn-intuitive-explanation/down-sampling-2.png)

图 11：对三个维度的特征图执行降采样。

Average Pooling 和 sum 类似，只不过取的是平均值和累加和。
实际中，Max Pooling 效果更好一些。下面是一个效果对比：

![](/assets/img/cnn-intuitive-explanation/down-sampling-3.png)

图 12：Max/Sum 降采样函数效果对比。Source [[10](http://mlss.tuebingen.mpg.de/2015/slides/fergus/Fergus_1.pdf)]

Pooling 的作用是主动降低输入表示（input representation）的空间大小（spatial size） [4]，

1. 使输入表示**（特征维度）更小**且更易于管理；
2. **减少网络参数和计算量**，避免过度拟合（overfitting）[4]；
3. 使网络能**容忍输入图像中较小的变换、扭曲和平移**：小扭曲不会改变降采样的输出 —— 因为我们采用相邻区域内的最大值/平均值；
4. 使我们能获得一个几乎**跟输入分辨率无关的特征表示**（确切的术语是 “equivariant representation”）：
   这一点非常重要，因有了这种能力，那无论一个目标是在图像中什么位置，我们都能把它检测出来 [18,19]。

### 2.4.2 小结：卷积层 + ReLU + 降采样层

至此，我们已经了解了卷积、ReLU 和降采样的工作原理，它们是构成任何 CNN 的基本构建块。
如图 13 所示，

![](/assets/img/cnn-intuitive-explanation/basic-block.png)

图 13：两个基本处理单元构成的...
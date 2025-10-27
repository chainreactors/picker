---
title: PyTorch入门 (1)环境搭建、神经网络普及和Torch基础知识
url: https://mp.weixin.qq.com/s?__biz=Mzg5MTM5ODU2Mg==&mid=2247501337&idx=1&sn=1d5b325bd3781d3366805cba31133082&chksm=cfcf76d4f8b8ffc2bbf9a0d4b21b1d25fdb22fba974fb45849f750a272269e03399a890e940f&scene=58&subscene=0#rd
source: 娜璋AI安全之家
date: 2025-02-05
fetch_date: 2025-10-06T20:37:30.093754
---

# PyTorch入门 (1)环境搭建、神经网络普及和Torch基础知识

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/0RFmxdZEDRMK8bIwaqcVLsLG0pNeJuED8EK5kLNvdJlqXiaq3IEUrK3BiaNyJ6ic8LNs1SgkMHcfwOJQb1o2fdhsw/0?wx_fmt=jpeg)

# PyTorch入门 (1)环境搭建、神经网络普及和Torch基础知识

原创

Eastmount

娜璋AI安全之家

> 2024年4月28日是Eastmount的安全星球 —— 『网络攻防和AI安全之家』正式创建和运营的日子，并且已坚持5个月每周7更。该星球目前主营业务为 安全零基础答疑、安全技术分享、AI安全技术分享、AI安全论文交流、威胁情报每日推送、网络攻防技术总结、系统安全技术实战、面试求职、安全考研考博、简历修改及润色、学术交流及答疑、人脉触达、认知提升等。下面是星球的新人券，欢迎新老博友和朋友加入，一起分享更多安全知识，比较良心的星球，非常适合初学者和换安全专业的读者学习。
>
> ”

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRN2D0ib34nN6fIBViblH1xb9RujXz10hUiaqGBEeGK2ibe0KUfwu5rBYEAnluHZ0cAKLqASZvicFRJJ3Mw/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

感谢读者2024年对本公众号的支持。新的一年继续分享干货，共同进步，感恩同行 ^\_^

前面我们的Python人工智能主要以TensorFlow和Keras为主，而现在最主流的深度学习框架是PyTorch。结合读者建议和个人爱好，接下来我们将分享PoTorch入门文章。这篇文章将介绍PyTorch入门知识，希望对初学者有所帮助。

此外，前面几篇文章通过学习莫烦老师视频并结合自身实践案例来深入分析，推荐大家学习莫老师的分享，后续将以各类案例进行实战。基础性文章，希望对您有帮助，如果存在错误或不足之处，还请海涵。且看且珍惜！

* https://study.163.com/course/courseLearn.htm?courseId=1003885021

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRMK8bIwaqcVLsLG0pNeJuED4mzfkro2VxIriaAo06Q4X1YRPAicXxUKRIC0k2DXwj79jR5lJKrO8NDg/640?wx_fmt=png&from=appmsg)

文章目录：

* **一.为什么选PyTorch**
* **二.PyTorch、TensorFlow和Keras**

+ 1.Tensorflow
+ 2.PyTorch
+ 3.Keras

* **三.PyTorch安装及入门示例**

+ 1.安装介绍
+ 2.安装过程

* **四.白话神经网络**
* **五.对比Torch和Numpy**
* **六.总结**

本专栏主要结合作者之前的博客、AI经验和相关视频及论文介绍，后面随着深入会讲解更多的Python人工智能案例及应用。作为人工智能的菜鸟，希望大家能与我在这一笔一划的博客中成长起来。如果有问题随时私聊我，只望您能从这个系列中学到知识，一起加油喔~

* Keras下载地址：https://github.com/eastmountyxz/AI-for-Keras
* TensorFlow下载地址：https://github.com/eastmountyxz/AI-for-TensorFlow

---

# 一.为什么选PyTorch

PyTorch是一个开源的Python深度学习库，由Facebook人工智能研究院（FAIR）在2017年1月基于Torch推出。它既可以看作加入了GPU支持的numpy，又可以看成一个拥有自动求导功能的深度神经网络。PyTorch提供了强大的GPU加速的张量计算和包含自动求导系统的深度神经网络，使得研究人员和开发者能够更快速、更灵活地构建和训练深度学习模型。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRMK8bIwaqcVLsLG0pNeJuEDYaNIozqk6EVcNoibqIeyakv6EItnzzFNlsdqUcY4ibyTvQ6xZ64aDsFg/640?wx_fmt=png&from=appmsg)

下面给出莫言老师的描述：

* PyTorch是比较新的神经网络模块，是Torch在Python上的衍生。因为Torch是一个使用Lua语言的神经网络库，Torch很好用，但是Lua又不是特别流行，所有开发团队将Lua的Torch移植到了更流行的语言Python上。是的，PyTorch 一出生就引来了剧烈的反响。

**为什么PyTorch如此受欢迎呢？**
很简单，我们先看看有谁在用PyTorch 吧。由上图可见，著名的Facebook、Twitter、NVIDIA、CMU等都在使用它，这就说明PyTorch的确是好用的，而且是值得推广的。而且如果您知道Numpy，PyTorch说它就是在神经网络领域可以用来替换Numpy的模块。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRMK8bIwaqcVLsLG0pNeJuEDBld928XMucUcCrOAKm21doehHhiaZdNFedfNh8OPauDtL0I2Hsiceib9A/640?wx_fmt=png&from=appmsg)

**那么，为什么作者最近才分享PyTorch呢？**
因为作者最初学习深度学习时，PyTorch仅支持Linux和OSX操作系统，而作者更喜欢在Windows上进行编程，因此最终选择了Theano、TensorFlow到Keras的学习路线。随着PyTorch的流行以及读者的需求，作者接下来将陆续分享PyTorch的案例代码，其本质和Keras也类似。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRMK8bIwaqcVLsLG0pNeJuEDSyQWcIv6MFuZ0d3SVanyibTfy6VZEsgXpS4McwHw0fmpOsMSYib82AGA/640?wx_fmt=png&from=appmsg)

---

# 二.PyTorch、TensorFlow和Keras

接下来，我们分别介绍PyTorch、TensorFlow和Keras的优缺点，并且引入GPT给出代表性的描述。

Tensorflow \ Keras 和 PyTorch是迄今为止最受欢迎的两个主要机器学习库。TensorFlow由谷歌团队开发，于 2015 年发布。而PyTorch则由 Facebook的团队开发，并于2017年在GitHub上开源。

PyTorch、TensorFlow和Keras作为当前深度学习领域最受欢迎的三个框架，各自具有其独特的优点和缺点。以下是对这三个框架的学术语言描述及其优缺点分析，并解释为什么PyTorch在某些方面比其他框架更受欢迎。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRMK8bIwaqcVLsLG0pNeJuEDnRZHdfAUewC8rWUIRznBjEvGqY7QKKExmmtvGZMrOlcjelU7JQM6Pw/640?wx_fmt=png&from=appmsg)

## 1.Tensorflow

优点：

* 高度灵活

  TensorFlow提供了底层的操作和控制，可以对模型的细节进行精确调整和优化。
* 强大的部署能力

  TensorFlow支持多种平台，包括移动设备、嵌入式系统和分布式环境，提供了广泛的部署选项。
* 大型社区和生态系统

  TensorFlow拥有庞大的用户和开发者社区，提供了丰富的文档、教程和资源。

缺点：

* 学习曲线陡峭

  TensorFlow的API设计相对复杂，可能需要更多的代码和配置，对于初学者来说可能不太友好。
* 静态图机制

  与PyTorch的动态图相比，TensorFlow的静态图在某些情况下可能不太灵活。

---

## 2.PyTorch

优点：

* 动态计算图

  PyTorch采用动态计算图的方式，允许在运行时更改图的行为，这使得模型构建更加灵活和易于调试。与TensorFlow等使用静态计算图的框架相比，PyTorch在处理不确定性或复杂性时具有优势。
* 易用性

  PyTorch的API设计简单直观，易于学习和使用。由于PyTorch与Python的深度集成，Python程序员可以快速上手并进行深度学习任务。此外，PyTorch提供了丰富的文档、教程和示例代码，使得用户能够方便地获取帮助和支持。
* 易于调试

  由于PyTorch的动态性和Python性质，调试PyTorch程序变得相当直接。用户可以使用Python的标准调试工具，如PDB或PyCharm，直接查看每个操作的结果和中间变量的状态。
* 强大的社区支持

  PyTorch拥有一个活跃的社区，提供了大量的资源、教程和代码示例。用户可以在官方论坛、GitHub、Stack Overflow等平台上找到大量的PyTorch用户和开发者，从而获取大量的帮助和支持。
* 高效的GPU利用

  PyTorch可以非常高效地利用NVIDIA的CUDA库来进行GPU计算，支持多GPU分布式训练，加速深度学习模型的训练速度。
* 广泛的预训练模型

  PyTorch提供了大量的预训练模型，包括但不限于ResNet、VGG、Inception、SqueezeNet、EfficientNet等，这些预训练模型可以帮助用户快速开始新的项目。

需要注意的是，PyTorch虽然具有诸多优势，但也存在一些缺点。

* 性能相对较低

  与TensorFlow等使用静态图的框架相比，PyTorch在处理大规模数据时可能表现出较低的性能。
* 部署复杂

  将PyTorch模型部署到生产环境可能需要进行模型转换和优化，这增加了部署的复杂性。
* 缺乏成熟的模型库以及Python依赖

  最早与一些竞争对手相比，缺乏部分库，当前比较完善。此外，对于不熟悉Python的用户来说，学习和使用PyTorch可能会有一定的门槛。

然而，这些缺点并未阻止PyTorch在深度学习领域中的广泛应用和受欢迎程度。

---

## 3.Keras

优点：

* 简单易用

  Keras提供了简洁的API，使得用户可以轻松地构建、训练和测试神经网络模型。
* 灵活性

  Keras支持多种深度学习模型，包括序贯式模型、函数式模型和子类化模型。
* 支持多种后端

  Keras可以在TensorFlow、Theano和CNTK等后端引擎上运行，提供了广泛的兼容性。

缺点：

* 性能相对较低

  与底层深度学习框架相比，Keras在处理大规模数据和复杂模型时可能表现出较低的性能。
* 功能相对有限

  在某些高级功能和特性上，Keras可能不如PyTorch和TensorFlow等深度学习框架强大。

为什么PyTorch比其他框架好？
虽然TensorFlow和Keras都有其独特的优点，但PyTorch在某些方面表现出更好的性能。首先，PyTorch的动态图机制使得模型开发和调试更加灵活和直观，这对于研究人员和开发者来说非常重要。其次，PyTorch的Pythonic编程风格使得代码编写更加自然，易于学习和使用。

此外，PyTorch的GPU支持强大，能够充分利用GPU进行加速，提高模型的训练速度。最后，PyTorch拥有庞大的开源社区，提供了丰富的文档、教程和示例代码，这为用户提供了广泛的支持和资源。因此，对于初学者和寻求灵活性和易用性的研究人员来说，PyTorch可能是一个更好的选择。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRMK8bIwaqcVLsLG0pNeJuED13CbzUqkd8Ufd5sOoQ8EwRZPibQbQnuD9cHwm3Xriau4kiaUB2rdV97GA/640?wx_fmt=png&from=appmsg)

Tensorflow能更有效地处理一些问题，比如说RNN变化时间长度的输出。而莫老师认为：

* 各家有各家的优势和劣势，所以我们要以中立的态度，两者都是大公司，Tensorflow自己说自己在分布式训练上下了很大的功夫，那就默认Tensorflow在这一点上要超出PyTorch，但是Tensorflow的静态计算图使得它在RNN上有一点点被动（虽然它用其他途径解决了），不过用PyTorch的时候，你会对这种动态的RNN有更好的理解，更好地诠释神经网络的功能。
* PyTorch搭建图的时候，它不是先建好一个静态的流程图，然后再把数据放到流程图中计算，而是边输入数据边搭建图，是一个动态的过程。
* Tensorflow的高度工业化，它的底层代码你是看不懂的。PyTorch好那么一点点，如果你深入API，你至少能比看Tensorflow多看懂一点点PyTorch的底层在干嘛。

最后的建议就是:
如果你是学生、随便选一个学，或者稍稍偏向 PvTorch，因为写代码的时候应该更好理解懂了一个模块，转换 Tensorflow 或者其他的模块都好说。如果是上班了，跟着你公司来，公司用什么，你就用什么，不要脱群。

---

# 三.PyTorch安装及入门示例

## 1.安装介绍

PyTorch的安装非常容易，通过官网可以看到安装过程，如下图所示：

* https://pytorch.org/

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRMK8bIwaqcVLsLG0pNeJuEDfZgRtukxY9JMiawPzWnz7xatiaOgib6xyPlliaqgvvicYuA4zjShXKVibeSg/640?wx_fmt=png&from=appmsg)

PyTorch通过高维表示我们的信息，然后在GET STARTED中选择对应的版本。

* https://pytorch.org/get-started/locally/

> GET STARTED：Select preferences and run the command to install PyTorch locally, or get started quickly with one of the supported cloud platforms.

如下图所示，选择对应的版本，包括操作系统、安装包、编程语言、是否GPU加速等。注意，作者当时学习的时候PyTorch还不支持Windows系统，因此选择了TensorFlow和Keras。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRMK8bIwaqcVLsLG0pNeJuEDhR2Za4ZFvzS3VHkVsNjicIiatVfsdVlejvF14Q4jtaAicwlrHNjsPJBGQ/640?wx_fmt=png&from=appmsg)

安装命令如下，它除了安装了PyTorch主模块，还安装了torchvision（数据库和预训练好的模型和网络）。

* pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

如果读者需要GPU，选择对应的即可。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRMK8bIwaqcVLsLG0pNeJuEDpNBRoXGkJV59TfH00nkibvq2rMsHBVr7l0YZXVNvQarPbOCEps1Cutw/640?wx_fmt=png&from=appmsg)

---

## 2.安装过程

接下来是作者电脑上的安装过程。首先，找到Python安装目录的Scripts位置。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRMK8bIwaqcVLsLG0pNeJuEDU3kw4Qd7K2NyOazUgl72H8pK49OTP5pxBX4pAI2oiagGxBXRDx8SIQA/640?wx_fmt=png&from=appmsg)

再打开CMD并输入先前的安装命令。

* pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRMK8bIwaqcVLsLG0pNeJuED4hvYFjTtPIxWmEEq2H4QCH4nZticMXEe9ptkX7LcX2PDF16SFOtbYEA/640?wx_fmt=png&from=appmsg)

安装过程如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRMK8bIwaqcVLsLG0pNeJuEDibMrwFTWfvpjmiauibGxsibadEIPHUQP7SFYh7yLm5Fu7Svv4Luxw8Nq9w/640?wx_fmt=png&from=appmsg)

最后通过pip list可以看到已成功安装。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRMK8bIwaqcVLsLG0pNeJuEDGQzIOWkn2M3umrUjOOtFA3XUibDGvd5OdkmJL4FfK5YEZrCrEzCibGCA/640?wx_fmt=png&from=appmsg)

---

# 四.白话神经网络

该部分还是有必要再给大家普及一遍，参考"莫烦大神"网易云课程对神经网络的介绍，讲得清晰透彻，推荐大家阅读。开始吧！让我们一起进入神经网络和TensorFlow的世界。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRMK8bIwaqcVLsLG0pNeJuED3YMGz6mU0f3ibDoUDHQwNScKWluET3DoiblEMdGQf0WiaLHdsP6iarDrSQ/640?wx_fmt=png&from=appmsg)

首先，什么是神经网络（Neural Networks）？
计算机神经网络是一种模仿生物神经网络或动物神经中枢，特别是大脑的结构和功能，它是一种数学模型或计算机模型。神经网络...
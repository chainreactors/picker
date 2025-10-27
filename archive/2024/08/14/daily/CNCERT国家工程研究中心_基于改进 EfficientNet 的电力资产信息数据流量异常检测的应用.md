---
title: 基于改进 EfficientNet 的电力资产信息数据流量异常检测的应用
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247546359&idx=1&sn=6000d3787ecc508616119efb29a9777d&chksm=fa938336cde40a20510f6798001c0ca471fcf57a22b173ca50b27cc3069b83177773202dd2aa&scene=58&subscene=0#rd
source: CNCERT国家工程研究中心
date: 2024-08-14
fetch_date: 2025-10-06T18:05:37.827100
---

# 基于改进 EfficientNet 的电力资产信息数据流量异常检测的应用

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176kK7yOJ7Nl2ia20Dgl7T6cx9gzMz9jUSpcW90obsftgu5JxqPJnb0sjnh6ohBMmicaSBlzDBzVWZwhQ/0?wx_fmt=jpeg)

# 基于改进 EfficientNet 的电力资产信息数据流量异常检测的应用

网络安全应急技术国家工程中心

以下文章来源于信息安全与通信保密杂志社
，作者Cismag

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM57SpaEcnib8NMGibzYLk6p0uOuGZThgJsy6XBtuoV6SmKQ/0)

**信息安全与通信保密杂志社**
.

网络强国建设的思想库、安全产业发展的情报站、创新企业腾飞的动力源

**摘要：**针对传统异常流量检测方法在面对复杂多样的新型网络攻击时存在的数据特征提取困难、准确率低、误报率高和运行成本高等问题，提出了一种基于 EfficientNet 与贝叶斯超参数优化的电力资产信息流量异常检测方法，通过将流量数据序列转换为二维图像，有效提取网络流量异常特征并进行分类，实现高准确度和效率。在 KDD-NSL、CIC-IDS2017数据集上，相较于 VGG19、Xception、ResNet50，该方法分别提升最高 6.7% 的准确率和 8.1%的 F1 值，表明了该方法的显著优势和实用价值。

随着基于 IEC 61850 标准的智能变电站的快速发展，智能变电站中的电力资产信息网络所面临的网络攻击风险也越来越大。智能变电站以智能电网和能源物联网为基础，以人工智能、物联网等现代信息技术为支撑，采用“全面感知”先进传感技术，能够实现自主巡检、远程监控、主动预警等功能，具有全站信息数字化、通信平台网络化和信息共享标准化等特点。

智能变电站中的电力资产信息网络是一种先进的数字物理双向潮流电力系统，具有自我修复、自适应、恢复和可持续等独有特征。根据 IEC 61850 标准，智能变电站通信结构被分为“三层两网”。三层是指间隔层、过程层和站控层；两网是指站控层网络和过程层网络。站控层网络主要使用制造消息规范、面向通用对象的变电站事件（Generic Object Oriented Substation Event，GOOSE）和简单网络时间协议（Simple Network Time Protocol，SNTP）进行站控层与间隔层之间的信息传输服务。过程层网络通过采样值协议和 GOOSE 协议完成间隔层与过程层之间的信息交换。整个智能变电站的通信装置通过对时设备（简单时钟同步 SNTP 协议或精确时钟同步协议）实现全局时钟实时同步。此外，变电站通过远动装置与远程控制中心或其他变电站进行数据交换，比如控制指令和原始数据文件，以实现跨站的远程通信。

来自外部的攻击以与智能变电站的站控层设备通信为主，通过攻击操作平台向网络中的设备发送恶意指令。电力资产信息网络系统是关键的工业基础设施，具有复杂的架构并包括多层级、多领域的关键设备。当通信系统的保密性、完整性或可用性被破坏时，可能导致国家安全赤字、公共秩序中断、生命损失或大规模经济损失等严重事故。因此，工业界、政府和学术界都在努力加强其安全性 。在当前的研究工作中，机器学习分类器的算法模型被用于将电力流量数据分类为正常数据或入侵数据，例如，Hong 等人使用卷积 - 长短时记忆（CNN-Long Short Term Memory，CNN-LSTM）网络模型对KDDCup99 测试数据集进行评估，以确定连接记录是正常流量还是异常流量，其准确率达到了97% 以上。传统的电力系统主要体现在对边界的防护，使用各种物理隔离或网络防护方式来阻止攻击渗透到网络中。但是传统处理异常网络流量的模型偏向于被动防御，这样就会存在隐藏的威胁，一旦防御被攻破则很容易遭到对手的进一步入侵。

本文旨在解决电力资产信息网络中异常网络流量检测的问题，实现对网络攻击流量的主动检测。首先，通过将一维流量数据序列转换为二维图像，实现对流量数据的特征增强；其次，利用 EfficientNet 深度学习模型对增强后的流量数据进行特征检测，以实现智能变电站电力资产信息网络场景下的网络流量异常检测。此外，对 EfficientNet 模型进行改进，加入注意力机制，改进现有网络以提升异常检测的精度，并且利用贝叶斯参数优化方法得到最佳参数进一步提高模型的分类效果，充分挖掘 EfficientNet 模型在二维数据特征检测上的潜力，并在 KDD-NSL、CIC-IDS2017 数据集上进行实验以验证方案的可行性。

# **1、相关理论**

**1.1　EfficientNet 模型**

卷积网络具有强大的表征学习能力，近几年已经在多个领域的图像识别任务中广泛应用，并且表现出色。本文将预处理后生成的数据图像作为卷积神经网络的表征学习对象，通过分类器对学习到的数据特征进行分类，将流量识别任务转变为卷积模型图像分类任务。一般来说，卷积网络结构越深提取到的特征也就越抽象，越具有语义信息，但结构过深会存在梯度弥散或梯度爆炸、网络退化、参数量过大难以训练等问题 。通常神经网络提升性能的方法有 3 种：一是使用残差网络搭建更深层次的神经网络结构来实现更抽象的特征提取；二是进行数据增强，比如增大输入图片的分辨率，也有利于提高精确度；三是增加网络的宽度以获得具有更高细粒度的特征，并且降低训练难度。

由 Google 提出的快速高精度模型 EfficientNet将这 3 种方法结合起来，使用一组固定的缩放系数同时调整深度、宽度及分辨率。缩放系数采用神经架构搜索（Neural Architecture Search，NAS）来自动进行搜索优化，通过 Swish 激活函数和捷径分支（类似于残差模块）来防止梯度消失和爆炸问题，并在网络中采用 Dropout 随机失活神经元来防止过拟合。

**1.2　卷积注意力模块**

卷积注意力模块（Convolutional Block Attention Module，CBAM）是一种卷积神经网络中的注意力模块，用于在特征图中选择性地强化有用的信息，并抑制噪声和无关信息。CBAM 通过组合通道注意力和空间注意力，将深度卷积网络扩展到更复杂的场景，并实现对大型图像数据集的有效处理。通道注意力机制通过从所有空间位置提取特征信息，并计算其在通道异常值上的重要程度，来实现卷积特征的自适应加权。同时，空间注意力机制可以用于探测不同区域间的空间相关性，并将这些空间信息结合到卷积特征中，从而实现对于空间结构信息的有效提取和学习。本文在 EfficientNet 网络之后引入CBAM 模块使得 EfficientNet 网络可以更加有效地处理高维空间信息。

**1.3　贝叶斯超参数优化**

超参数对于机器学习算法非常重要，它们直接控制训练算法的行为，并且对机器学习模型的性能有显著影响。机器学习算法的性能和超参数之间的关系较为复杂，因此如何优化超参数是机器学习算法中比较重要的一环。

超参数优化方法一般有两种：人工搜索和自动搜索。人工搜索需要相关领域的专家来调整，对专业性要求强且效率较低。自动搜索包含了许多算法，例如网格搜索 或笛卡尔超参数搜索，这种方法理论上可以获得优化目标函数的全局极值，但是随着超参数数量的增加，算法的效率会随之降低。

超参数整定是一个需要优化的问题，其中优化的目标函数为未知函数或黑盒函数，贝叶斯优化是解决此类优化问题的一种有效算法。首先，它将未知函数的先验信息与样本信息相结合，利用贝叶斯公式获得函数分布的后验信息；其次，基于此后验信息，可以推断函数在何处获得最佳值。实验结果表明，贝叶斯优化算法优于其他全局优化算法。利用贝叶斯优化深度学习模型进行检测的一般步骤为：

(1）设定待优化参数范围和优化目标函数；

(2）利用贝叶斯对模型的隐藏层和初始学习率进行优化；

(3）返回优化的最小值及对应模型的超参数；

(4）将贝叶斯优化模型的超参数作为最终模型的参数。

# **2、电力资产信息数据流量异常检测模型**

针对电力资产信息网络流量的安全问题，本文提出了一种基于改进的 EfficientNet 电力资产信息异常流量检测方法。首先，本文提出了一种数据转换方式，将电力资产信息网络数据以基于时间的块为单位，通过维度变换将一维的攻击数据转换到二维空间，并将其可视化。其次，采用主流的卷积神经网络变体 EfficientNet，结合CBAM 注意力机制和贝叶斯超参数优化方法对卷积神经网络进行训练。最后，使用 NSL-KDD、CIC-IDS2017 两个真实网络攻击数据集进行实验，验证本文方法的有效性。异常流量检测模型整体流程如图 1 所示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iclynibMMTgBy0icQVEXRoqViciag1qJLWedgajrLVDOf4Oyj4w2he2qtGJNGn1BqjM6AsoarK9vd2mN5hjFF4Q8mDw/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

图 1　异常流量检测模型整体流程

**2.1　数据描述和处理**

**2.1.1　数据描述**

本文选取的是特征化之后的网络攻击流量数据集 NSL-KDD 与 CIC-IDS2017，其中包含大量特征化的网络连接。数据集中特征化的网络连接定义为：在某个时间内从开始到结束的传输控制协议（Transmission Control Protocol，TCP）数据包序列，并且在这段时间内，数据在预定义的协议下从源 IP 地址到目的 IP 地址的传递。表 1 展示了 CIC-IDS2017 数据集中的 4 条记录，CIC-IDS2017 数 据 集 使 用 CICFlowMeter 提 取85 个网络流特征。其中包含了 6 个基本特征、79 个功能特征和一个标签（正常或攻击）。

表 1　CIC-IDS2017 数据集中的 4 条记录

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iclynibMMTgBy0icQVEXRoqViciag1qJLWedgRnABlsuqcoSEaQ4Z5ricIyOfVYKVJBasT2gPYnhs5NHmWgjXKYpO1YA/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

NSL-KDD 数据集中每个网络连接包含 42 个特征，其中 41 个特征指的是流量输入本身的属性，例如流持续时间、流的平均长度、带有确认 字 符（Acknowledge character，ACK） 包 的 数量等，最后一个是标签（正常或攻击）。表 2 展示了 NSL-KDD 数据集中的 3 条记录及其部分特征，其中，服务是指使用的目标网络服务，相同服务连接数量是指与当前连接相同的服务（端口号）在过去两秒内的连接数，标签是指此条数据流量的类别。

表 2　NSL-KDD 数据集中的 3 条记录及其部分特征

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iclynibMMTgBy0icQVEXRoqViciag1qJLWedgZXXBvdxJKF4FbI5cXwQyHoiaCy630fDSDfhKwJYZmFmATOAMlrJyzZw/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

NSL-KDD 数据集中提供的特征可以分为4 类：TCP 连接基本特征、TCP 连接的内容特征、基于时间和基于主机的网络流量统计特征。以下是对不同类别功能的描述：

(1）TCP 连接基本特征可以从数据包的包头中获得，无须查看有效负载本身，保存有关数据包的基本信息，如连续时间、协议类型、传送的字节数等。

(2）TCP 连接内容特征包含有关原始数据包的信息，原始数据包是分多个而不是一个发送的。有了这些信息，系统就可以访问有效载荷。

(3）基于时间的网络流量统计特征是在两秒的窗口内对流量输入进行分析，并包含诸如尝试与同一主机建立多少连接等信息。这些特征主要是计数和速率，而不是有关流量输入内容的信息。

(4）基于主机的网络流量统计特征是对一系列连接进行分析。这些特征旨在分析访问跨度超过两秒窗口时间跨度的攻击。

CIC-IDS2017 数 据 集 使 用 CICFlowMeter 提取 85 个网络流特征。其中包含了 6 个基本特征、79 个功能特征。每条流量包含一个标签（正常或攻击）。

**2.1.2　数据预处理**

对数据进行清洗与数据增强。将原始数据集中存在的缺失值、无穷值删除。将字符值编码成数字。CIC-IDS2017 数据集中的样本类别数量极不平衡，正常类型样本数量较多，而某些类型的异常样本数量过少，例如结构化查询语言（Structured Query Language，SQL）注入攻击类型只有 21 个样本。针对数据集中特定的攻击类型样本量过少的问题，本文采用合并相似攻击类型的方法，来提高模型的分类准确性和稳定性。合并前后的类型如表 3 所示。

表 3　CIC-IDS2017 数据集中合并的攻击类型

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iclynibMMTgBy0icQVEXRoqViciag1qJLWedgV5FsoPV1QrBhjP2GpOTiaMyzjQ44f05Pb1nadp5fJCOrq708u9FoUWg/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

合并后的各类别样本数量如表 4 所示。

表 4　CIC-IDS2017 数据集分类后各类别数量

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iclynibMMTgBy0icQVEXRoqViciag1qJLWedgPl5qhZdy5puaib0wGry6BwLXPI9ibuBT1duNbOU01KerZyM3Lh1IgCibw/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

NSL-KDD 数据集各类别具体分布如表 5 所示。

表 5　NSL-KDD 数据集各类别数量

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iclynibMMTgBy0icQVEXRoqViciag1qJLWedgGvOJQFpUV0fBG9elGT52632KRbxaznXNhjrZo5r44A0GJD3hqlXkUA/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**2.1.3　数据转换**

NSL-KDD 与 CIC-IDS2017 数据集是人工选择的流量特征数据，样本的形式是一维序列。本文采用的主干网络需要的输入格式为二维数据，所以需要将一维序列形式的样本转换为固定大小的二维图像形式。由于样本的每个特征的数据大小数量级不同，图像像素值取值范围为 [0,255]，因此需要先将样本中所有数据范围转化到 [0,255]，如式（1）所示。

首先，利用 QuantileTransformer 方法对数据进行非线性转换，之后将所有数据乘以 255 扩大至 [0,255] 范围。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iclynibMMTgBy0icQVEXRoqViciag1qJLWedg5WczHKz2mcYpnia8c9nd7PZXEM4WNmvLA4qNPXbpicuchvc4gFhHaUIw/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

式中：QuantileTransformer 为基于分位函数的无参数转换函数，功能是将数据映射到 0～1 的均匀分布上。

其次，根据特征值数量 n 来构建 n×n×3的图片。最后再对 n×n×3 的图片数据集进行数据增强，使用双线性插值方法将图像尺寸扩展至 224×224，其核心思想是在两个方向分别进行一次线性插值。双线性插值的具体过程如下：

假设要得到点 (x, y) 的像素值，并且已知![](https://mmbiz.qpic.cn/sz_mmbiz_png/iclynibMMTgBy0icQVEXRoqViciag1qJLWedgJW2uY7wdaTR5IozgbiaN1YQbibUprN139xPCWd0GW5qakNdKkNuqyy6w/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)4 个点的像素值。首先需要在 x 轴方向进行线性插值，其次在 y 轴方向进行一次线性插值。

（1）在 x 轴方向使用单线性插值分别计算![](https://mmbiz.qpic.cn/sz_mmbiz_png/iclynibMMTgBy0icQVEXRoqViciag1qJLWedg0M5T8SoUJ6yRG4MOiaZuicodjNiavW0nwftmKZmMRj4mMuldrza2TMqGg/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)的像素值。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iclynibMMTgBy0icQVEXRoqViciag1qJLWedgYZtAPqIuUNyXAwibytxziaqGKHkN4UsvrHFwvic7GDCw6o6yVEnhibtoxg/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

(2）在 y 轴方向使用单线性插值计算 (x, y)坐标点的像素值。![](https://mmbiz.qpic.cn/sz_mmbiz_png/iclynibMMTgBy0icQVEXRoqViciag1qJLWedgkfZPkiazr1Mq3b0CVKAaoWniae1ukLUqWH5cicyANx5kJsRLdxmplCMzg/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

式中：f (x, y) 为要计算的 (x, y) 坐标点的像素值；p(x, y)为(x, y) 坐标点的像素值。

图 2 展示了数据集中 6 个类别的一维流量数据进行增强后形成的二维图像数据。

![](https://...